# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from pprint import pformat
from six import iteritems


class BuildRecordRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuildRecordRest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'submit_time': 'datetime',
            'start_time': 'datetime',
            'end_time': 'datetime',
            'status': 'str',
            'build_configuration_id': 'int',
            'build_configuration_name': 'str',
            'build_configuration_rev': 'int',
            'project_id': 'int',
            'project_name': 'str',
            'user_id': 'int',
            'username': 'str',
            'scm_repo_url': 'str',
            'scm_revision': 'str',
            'build_environment_id': 'int',
            'attributes': 'dict(str, str)',
            'live_logs_uri': 'str',
            'build_config_set_record_id': 'int',
            'build_content_id': 'str',
            'product_milestone_id': 'int',
            'user': 'UserRest',
            'build_configuration_audited': 'BuildConfigurationAuditedRest',
            'execution_root_name': 'str',
            'execution_root_version': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'submit_time': 'submitTime',
            'start_time': 'startTime',
            'end_time': 'endTime',
            'status': 'status',
            'build_configuration_id': 'buildConfigurationId',
            'build_configuration_name': 'buildConfigurationName',
            'build_configuration_rev': 'buildConfigurationRev',
            'project_id': 'projectId',
            'project_name': 'projectName',
            'user_id': 'userId',
            'username': 'username',
            'scm_repo_url': 'scmRepoURL',
            'scm_revision': 'scmRevision',
            'build_environment_id': 'buildEnvironmentId',
            'attributes': 'attributes',
            'live_logs_uri': 'liveLogsUri',
            'build_config_set_record_id': 'buildConfigSetRecordId',
            'build_content_id': 'buildContentId',
            'product_milestone_id': 'productMilestoneId',
            'user': 'user',
            'build_configuration_audited': 'buildConfigurationAudited',
            'execution_root_name': 'executionRootName',
            'execution_root_version': 'executionRootVersion'
        }

        self._id = None
        self._submit_time = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._build_configuration_id = None
        self._build_configuration_name = None
        self._build_configuration_rev = None
        self._project_id = None
        self._project_name = None
        self._user_id = None
        self._username = None
        self._scm_repo_url = None
        self._scm_revision = None
        self._build_environment_id = None
        self._attributes = None
        self._live_logs_uri = None
        self._build_config_set_record_id = None
        self._build_content_id = None
        self._product_milestone_id = None
        self._user = None
        self._build_configuration_audited = None
        self._execution_root_name = None
        self._execution_root_version = None

    @property
    def id(self):
        """
        Gets the id of this BuildRecordRest.


        :return: The id of this BuildRecordRest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildRecordRest.


        :param id: The id of this BuildRecordRest.
        :type: int
        """
        self._id = id

    @property
    def submit_time(self):
        """
        Gets the submit_time of this BuildRecordRest.


        :return: The submit_time of this BuildRecordRest.
        :rtype: datetime
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        """
        Sets the submit_time of this BuildRecordRest.


        :param submit_time: The submit_time of this BuildRecordRest.
        :type: datetime
        """
        self._submit_time = submit_time

    @property
    def start_time(self):
        """
        Gets the start_time of this BuildRecordRest.


        :return: The start_time of this BuildRecordRest.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this BuildRecordRest.


        :param start_time: The start_time of this BuildRecordRest.
        :type: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this BuildRecordRest.


        :return: The end_time of this BuildRecordRest.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this BuildRecordRest.


        :param end_time: The end_time of this BuildRecordRest.
        :type: datetime
        """
        self._end_time = end_time

    @property
    def status(self):
        """
        Gets the status of this BuildRecordRest.


        :return: The status of this BuildRecordRest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BuildRecordRest.


        :param status: The status of this BuildRecordRest.
        :type: str
        """
        allowed_values = ["NEW", "WAITING_FOR_DEPENDENCIES", "BUILDING", "BUILD_COMPLETED", "DONE", "REJECTED", "REJECTED_FAILED_DEPENDENCIES", "REJECTED_ALREADY_BUILT", "SYSTEM_ERROR", "DONE_WITH_ERRORS", "CANCELLED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def build_configuration_id(self):
        """
        Gets the build_configuration_id of this BuildRecordRest.


        :return: The build_configuration_id of this BuildRecordRest.
        :rtype: int
        """
        return self._build_configuration_id

    @build_configuration_id.setter
    def build_configuration_id(self, build_configuration_id):
        """
        Sets the build_configuration_id of this BuildRecordRest.


        :param build_configuration_id: The build_configuration_id of this BuildRecordRest.
        :type: int
        """
        self._build_configuration_id = build_configuration_id

    @property
    def build_configuration_name(self):
        """
        Gets the build_configuration_name of this BuildRecordRest.


        :return: The build_configuration_name of this BuildRecordRest.
        :rtype: str
        """
        return self._build_configuration_name

    @build_configuration_name.setter
    def build_configuration_name(self, build_configuration_name):
        """
        Sets the build_configuration_name of this BuildRecordRest.


        :param build_configuration_name: The build_configuration_name of this BuildRecordRest.
        :type: str
        """
        self._build_configuration_name = build_configuration_name

    @property
    def build_configuration_rev(self):
        """
        Gets the build_configuration_rev of this BuildRecordRest.


        :return: The build_configuration_rev of this BuildRecordRest.
        :rtype: int
        """
        return self._build_configuration_rev

    @build_configuration_rev.setter
    def build_configuration_rev(self, build_configuration_rev):
        """
        Sets the build_configuration_rev of this BuildRecordRest.


        :param build_configuration_rev: The build_configuration_rev of this BuildRecordRest.
        :type: int
        """
        self._build_configuration_rev = build_configuration_rev

    @property
    def project_id(self):
        """
        Gets the project_id of this BuildRecordRest.


        :return: The project_id of this BuildRecordRest.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this BuildRecordRest.


        :param project_id: The project_id of this BuildRecordRest.
        :type: int
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """
        Gets the project_name of this BuildRecordRest.


        :return: The project_name of this BuildRecordRest.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """
        Sets the project_name of this BuildRecordRest.


        :param project_name: The project_name of this BuildRecordRest.
        :type: str
        """
        self._project_name = project_name

    @property
    def user_id(self):
        """
        Gets the user_id of this BuildRecordRest.


        :return: The user_id of this BuildRecordRest.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this BuildRecordRest.


        :param user_id: The user_id of this BuildRecordRest.
        :type: int
        """
        self._user_id = user_id

    @property
    def username(self):
        """
        Gets the username of this BuildRecordRest.


        :return: The username of this BuildRecordRest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this BuildRecordRest.


        :param username: The username of this BuildRecordRest.
        :type: str
        """
        self._username = username

    @property
    def scm_repo_url(self):
        """
        Gets the scm_repo_url of this BuildRecordRest.


        :return: The scm_repo_url of this BuildRecordRest.
        :rtype: str
        """
        return self._scm_repo_url

    @scm_repo_url.setter
    def scm_repo_url(self, scm_repo_url):
        """
        Sets the scm_repo_url of this BuildRecordRest.


        :param scm_repo_url: The scm_repo_url of this BuildRecordRest.
        :type: str
        """
        self._scm_repo_url = scm_repo_url

    @property
    def scm_revision(self):
        """
        Gets the scm_revision of this BuildRecordRest.


        :return: The scm_revision of this BuildRecordRest.
        :rtype: str
        """
        return self._scm_revision

    @scm_revision.setter
    def scm_revision(self, scm_revision):
        """
        Sets the scm_revision of this BuildRecordRest.


        :param scm_revision: The scm_revision of this BuildRecordRest.
        :type: str
        """
        self._scm_revision = scm_revision

    @property
    def build_environment_id(self):
        """
        Gets the build_environment_id of this BuildRecordRest.


        :return: The build_environment_id of this BuildRecordRest.
        :rtype: int
        """
        return self._build_environment_id

    @build_environment_id.setter
    def build_environment_id(self, build_environment_id):
        """
        Sets the build_environment_id of this BuildRecordRest.


        :param build_environment_id: The build_environment_id of this BuildRecordRest.
        :type: int
        """
        self._build_environment_id = build_environment_id

    @property
    def attributes(self):
        """
        Gets the attributes of this BuildRecordRest.


        :return: The attributes of this BuildRecordRest.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this BuildRecordRest.


        :param attributes: The attributes of this BuildRecordRest.
        :type: dict(str, str)
        """
        self._attributes = attributes

    @property
    def live_logs_uri(self):
        """
        Gets the live_logs_uri of this BuildRecordRest.


        :return: The live_logs_uri of this BuildRecordRest.
        :rtype: str
        """
        return self._live_logs_uri

    @live_logs_uri.setter
    def live_logs_uri(self, live_logs_uri):
        """
        Sets the live_logs_uri of this BuildRecordRest.


        :param live_logs_uri: The live_logs_uri of this BuildRecordRest.
        :type: str
        """
        self._live_logs_uri = live_logs_uri

    @property
    def build_config_set_record_id(self):
        """
        Gets the build_config_set_record_id of this BuildRecordRest.


        :return: The build_config_set_record_id of this BuildRecordRest.
        :rtype: int
        """
        return self._build_config_set_record_id

    @build_config_set_record_id.setter
    def build_config_set_record_id(self, build_config_set_record_id):
        """
        Sets the build_config_set_record_id of this BuildRecordRest.


        :param build_config_set_record_id: The build_config_set_record_id of this BuildRecordRest.
        :type: int
        """
        self._build_config_set_record_id = build_config_set_record_id

    @property
    def build_content_id(self):
        """
        Gets the build_content_id of this BuildRecordRest.


        :return: The build_content_id of this BuildRecordRest.
        :rtype: str
        """
        return self._build_content_id

    @build_content_id.setter
    def build_content_id(self, build_content_id):
        """
        Sets the build_content_id of this BuildRecordRest.


        :param build_content_id: The build_content_id of this BuildRecordRest.
        :type: str
        """
        self._build_content_id = build_content_id

    @property
    def product_milestone_id(self):
        """
        Gets the product_milestone_id of this BuildRecordRest.


        :return: The product_milestone_id of this BuildRecordRest.
        :rtype: int
        """
        return self._product_milestone_id

    @product_milestone_id.setter
    def product_milestone_id(self, product_milestone_id):
        """
        Sets the product_milestone_id of this BuildRecordRest.


        :param product_milestone_id: The product_milestone_id of this BuildRecordRest.
        :type: int
        """
        self._product_milestone_id = product_milestone_id

    @property
    def user(self):
        """
        Gets the user of this BuildRecordRest.


        :return: The user of this BuildRecordRest.
        :rtype: UserRest
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this BuildRecordRest.


        :param user: The user of this BuildRecordRest.
        :type: UserRest
        """
        self._user = user

    @property
    def build_configuration_audited(self):
        """
        Gets the build_configuration_audited of this BuildRecordRest.


        :return: The build_configuration_audited of this BuildRecordRest.
        :rtype: BuildConfigurationAuditedRest
        """
        return self._build_configuration_audited

    @build_configuration_audited.setter
    def build_configuration_audited(self, build_configuration_audited):
        """
        Sets the build_configuration_audited of this BuildRecordRest.


        :param build_configuration_audited: The build_configuration_audited of this BuildRecordRest.
        :type: BuildConfigurationAuditedRest
        """
        self._build_configuration_audited = build_configuration_audited

    @property
    def execution_root_name(self):
        """
        Gets the execution_root_name of this BuildRecordRest.


        :return: The execution_root_name of this BuildRecordRest.
        :rtype: str
        """
        return self._execution_root_name

    @execution_root_name.setter
    def execution_root_name(self, execution_root_name):
        """
        Sets the execution_root_name of this BuildRecordRest.


        :param execution_root_name: The execution_root_name of this BuildRecordRest.
        :type: str
        """
        self._execution_root_name = execution_root_name

    @property
    def execution_root_version(self):
        """
        Gets the execution_root_version of this BuildRecordRest.


        :return: The execution_root_version of this BuildRecordRest.
        :rtype: str
        """
        return self._execution_root_version

    @execution_root_version.setter
    def execution_root_version(self, execution_root_version):
        """
        Sets the execution_root_version of this BuildRecordRest.


        :param execution_root_version: The execution_root_version of this BuildRecordRest.
        :type: str
        """
        self._execution_root_version = execution_root_version

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
	    elif isinstance(value, datetime):
		result[attr] = str(value.date())
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
