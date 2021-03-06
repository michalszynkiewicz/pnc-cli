from argh import arg
import ConfigParser
import atexit
import getpass
import json
import os
import pickle

import requests

import swagger_client
import pnc_cli.utils as utils
import keycloak_config as kc
import pnc_server_config as psc



# make sure that input behaves as expected
try:
    input = raw_input
except NameError:
    pass

SAVED_USER_FILENAME = "saved-user.p"
SAVED_USER = utils.CONFIG_LOCATION + SAVED_USER_FILENAME


class UserConfig():
    def __init__(self):
        config = utils.get_config()
        self.token_time = 0
        self.username = self.load_username_from_config(config)
        self.password = self.load_password_from_config(config)
        self.pnc_config = psc.PncServerConfig(config)
        self.keycloak_config = kc.KeycloakConfig(config)
        self.token = self.retrieve_keycloak_token()
        self.apiclient = self.create_api_client()

    def __getstate__(self):
        return self.keycloak_config, self.username, self.token, self.token_time

    def __setstate__(self, state):
        # here we need to read the config file again, to check that values for URLs haven't changed. the way to
        # change the username / password will be a login function the user calls. ideally the config file won't need
        # to be changed much once it's in place
        newtoken = False
        config = utils.get_config()
        saved_kc_config, self.username, self.token, self.token_time = state
        self.pnc_config = psc.PncServerConfig(config)

        # check for changes in keycloak configuration; if so, we'll need to get a new token regardless of time
        current_keycloak_config = kc.KeycloakConfig(config)
        if not current_keycloak_config == saved_kc_config:
            print("Keycloak server has been reconfigured. Retrieving new token...")
            self.keycloak_config = current_keycloak_config
            newtoken = True
        else:
            self.keycloak_config = saved_kc_config

        # if more than a day has passed since we saved the token, and keycloak server configuration is not modified,
        # get a new one
        if not newtoken and utils.current_time_millis() - self.token_time > 86400000:
            # input the password again since we no longer cache it
            print("Keycloak token has expired for user {}. Retrieving new token...".format(self.username))
            newtoken = True

        if newtoken:
            # enter password to get new token, but only if the user has not entered a password in pnc-cli.conf
            password = self.load_password_from_config(config)
            if password:
                self.password = password
            else:
                self.password = self.input_password()
            self.token = self.retrieve_keycloak_token()
        self.apiclient = self.create_api_client()

    # this function gets input from the user to set the username
    def input_username(self):
        username = input('PNC username: ')
        return username

    # this function gets input from the user to set the password
    def input_password(self):
        password = getpass.getpass('PNC password: ')
        return password

    def load_username_from_config(self, config):
        try:
            username = config.get('PNC', 'username')
            print("Loaded username from pnc-cli.conf: {}").format(username)
            return username
        except ConfigParser.NoOptionError:
            return None

    def load_password_from_config(self, config):
        try:
            password = config.get('PNC', 'password')
            print("Loaded password from pnc-cli.conf")
            return password
        except ConfigParser.NoOptionError:
            return None


    # retrieves a token from the keycloak server using the configured username / password / keycloak server
    def retrieve_keycloak_token(self):
        if self.username and self.password:
            params = {'grant_type': 'password',
                      'client_id': self.keycloak_config.client_id,
                      'username': self.username,
                      'password': self.password}
            r = requests.post(self.keycloak_config.url, params, verify=False)
            if r.status_code == 200:
                print("Token retrieved for {}.".format(self.username))
                self.token_time = utils.current_time_millis()
                reply = json.loads(r.content.decode('utf-8'))
                return str(reply.get('access_token'))
            else:
                print("Failed to retrieve token:")
                print(r)
                print(r.content)
                exit(1)
        else:
            print("No credentials. Authentication is not possible.")

    def create_api_client(self):
        if self.token:
            return swagger_client.ApiClient(self.pnc_config.url, header_name='Authorization',
                                            header_value='Bearer ' + self.token)
        else:
            print("No Keycloak token is present. Commands requiring authentication will fail.")
            return swagger_client.ApiClient(self.pnc_config.url)

    def get_api_client(self):
        return self.apiclient


if os.path.exists(SAVED_USER):
    user = pickle.load(open(SAVED_USER, "rb"))
    print("Command performed with user: {}").format(user.username)
else:
    user = UserConfig()


def save():
    if user.token:
        pickle.dump(user, open(SAVED_USER, "wb"), protocol=pickle.HIGHEST_PROTOCOL)


atexit.register(save)


@arg("-u", "--username", help="Username for the new user")
@arg("-p", "--password", help="Password for the specified user")
def login(username=None, password=None):
    """
    Log in to PNC using the supplied username and password. The keycloak token will
    be saved for all subsequent pnc-cli operations until login is called again
    :return:
    """
    if username:
        user.username = username
    else:
        user.username = user.input_username()

    if password:
        user.password = password
    else:
        user.password = user.input_password()

    user.token = user.retrieve_keycloak_token()
    user.apiclient = user.create_api_client()
    save()