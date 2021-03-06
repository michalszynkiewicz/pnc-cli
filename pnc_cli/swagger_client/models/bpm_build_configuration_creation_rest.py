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


class BpmBuildConfigurationCreationRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BpmBuildConfigurationCreationRest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'build_script': 'str',
            'scm_repo_url': 'str',
            'scm_revision': 'str',
            'scm_external_repo_url': 'str',
            'scm_external_revision': 'str',
            'project_id': 'int',
            'build_environment_id': 'int',
            'dependency_ids': 'list[int]',
            'product_version_id': 'int',
            'build_configuration_set_ids': 'list[int]',
            'generic_parameters': 'dict(str, str)'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'build_script': 'buildScript',
            'scm_repo_url': 'scmRepoURL',
            'scm_revision': 'scmRevision',
            'scm_external_repo_url': 'scmExternalRepoURL',
            'scm_external_revision': 'scmExternalRevision',
            'project_id': 'projectId',
            'build_environment_id': 'buildEnvironmentId',
            'dependency_ids': 'dependencyIds',
            'product_version_id': 'productVersionId',
            'build_configuration_set_ids': 'buildConfigurationSetIds',
            'generic_parameters': 'genericParameters'
        }

        self._name = None
        self._description = None
        self._build_script = None
        self._scm_repo_url = None
        self._scm_revision = None
        self._scm_external_repo_url = None
        self._scm_external_revision = None
        self._project_id = None
        self._build_environment_id = None
        self._dependency_ids = None
        self._product_version_id = None
        self._build_configuration_set_ids = None
        self._generic_parameters = None

    @property
    def name(self):
        """
        Gets the name of this BpmBuildConfigurationCreationRest.


        :return: The name of this BpmBuildConfigurationCreationRest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BpmBuildConfigurationCreationRest.


        :param name: The name of this BpmBuildConfigurationCreationRest.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this BpmBuildConfigurationCreationRest.


        :return: The description of this BpmBuildConfigurationCreationRest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BpmBuildConfigurationCreationRest.


        :param description: The description of this BpmBuildConfigurationCreationRest.
        :type: str
        """
        self._description = description

    @property
    def build_script(self):
        """
        Gets the build_script of this BpmBuildConfigurationCreationRest.


        :return: The build_script of this BpmBuildConfigurationCreationRest.
        :rtype: str
        """
        return self._build_script

    @build_script.setter
    def build_script(self, build_script):
        """
        Sets the build_script of this BpmBuildConfigurationCreationRest.


        :param build_script: The build_script of this BpmBuildConfigurationCreationRest.
        :type: str
        """
        self._build_script = build_script

    @property
    def scm_repo_url(self):
        """
        Gets the scm_repo_url of this BpmBuildConfigurationCreationRest.


        :return: The scm_repo_url of this BpmBuildConfigurationCreationRest.
        :rtype: str
        """
        return self._scm_repo_url

    @scm_repo_url.setter
    def scm_repo_url(self, scm_repo_url):
        """
        Sets the scm_repo_url of this BpmBuildConfigurationCreationRest.


        :param scm_repo_url: The scm_repo_url of this BpmBuildConfigurationCreationRest.
        :type: str
        """
        self._scm_repo_url = scm_repo_url

    @property
    def scm_revision(self):
        """
        Gets the scm_revision of this BpmBuildConfigurationCreationRest.


        :return: The scm_revision of this BpmBuildConfigurationCreationRest.
        :rtype: str
        """
        return self._scm_revision

    @scm_revision.setter
    def scm_revision(self, scm_revision):
        """
        Sets the scm_revision of this BpmBuildConfigurationCreationRest.


        :param scm_revision: The scm_revision of this BpmBuildConfigurationCreationRest.
        :type: str
        """
        self._scm_revision = scm_revision

    @property
    def scm_external_repo_url(self):
        """
        Gets the scm_external_repo_url of this BpmBuildConfigurationCreationRest.


        :return: The scm_external_repo_url of this BpmBuildConfigurationCreationRest.
        :rtype: str
        """
        return self._scm_external_repo_url

    @scm_external_repo_url.setter
    def scm_external_repo_url(self, scm_external_repo_url):
        """
        Sets the scm_external_repo_url of this BpmBuildConfigurationCreationRest.


        :param scm_external_repo_url: The scm_external_repo_url of this BpmBuildConfigurationCreationRest.
        :type: str
        """
        self._scm_external_repo_url = scm_external_repo_url

    @property
    def scm_external_revision(self):
        """
        Gets the scm_external_revision of this BpmBuildConfigurationCreationRest.


        :return: The scm_external_revision of this BpmBuildConfigurationCreationRest.
        :rtype: str
        """
        return self._scm_external_revision

    @scm_external_revision.setter
    def scm_external_revision(self, scm_external_revision):
        """
        Sets the scm_external_revision of this BpmBuildConfigurationCreationRest.


        :param scm_external_revision: The scm_external_revision of this BpmBuildConfigurationCreationRest.
        :type: str
        """
        self._scm_external_revision = scm_external_revision

    @property
    def project_id(self):
        """
        Gets the project_id of this BpmBuildConfigurationCreationRest.


        :return: The project_id of this BpmBuildConfigurationCreationRest.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this BpmBuildConfigurationCreationRest.


        :param project_id: The project_id of this BpmBuildConfigurationCreationRest.
        :type: int
        """
        self._project_id = project_id

    @property
    def build_environment_id(self):
        """
        Gets the build_environment_id of this BpmBuildConfigurationCreationRest.


        :return: The build_environment_id of this BpmBuildConfigurationCreationRest.
        :rtype: int
        """
        return self._build_environment_id

    @build_environment_id.setter
    def build_environment_id(self, build_environment_id):
        """
        Sets the build_environment_id of this BpmBuildConfigurationCreationRest.


        :param build_environment_id: The build_environment_id of this BpmBuildConfigurationCreationRest.
        :type: int
        """
        self._build_environment_id = build_environment_id

    @property
    def dependency_ids(self):
        """
        Gets the dependency_ids of this BpmBuildConfigurationCreationRest.


        :return: The dependency_ids of this BpmBuildConfigurationCreationRest.
        :rtype: list[int]
        """
        return self._dependency_ids

    @dependency_ids.setter
    def dependency_ids(self, dependency_ids):
        """
        Sets the dependency_ids of this BpmBuildConfigurationCreationRest.


        :param dependency_ids: The dependency_ids of this BpmBuildConfigurationCreationRest.
        :type: list[int]
        """
        self._dependency_ids = dependency_ids

    @property
    def product_version_id(self):
        """
        Gets the product_version_id of this BpmBuildConfigurationCreationRest.


        :return: The product_version_id of this BpmBuildConfigurationCreationRest.
        :rtype: int
        """
        return self._product_version_id

    @product_version_id.setter
    def product_version_id(self, product_version_id):
        """
        Sets the product_version_id of this BpmBuildConfigurationCreationRest.


        :param product_version_id: The product_version_id of this BpmBuildConfigurationCreationRest.
        :type: int
        """
        self._product_version_id = product_version_id

    @property
    def build_configuration_set_ids(self):
        """
        Gets the build_configuration_set_ids of this BpmBuildConfigurationCreationRest.


        :return: The build_configuration_set_ids of this BpmBuildConfigurationCreationRest.
        :rtype: list[int]
        """
        return self._build_configuration_set_ids

    @build_configuration_set_ids.setter
    def build_configuration_set_ids(self, build_configuration_set_ids):
        """
        Sets the build_configuration_set_ids of this BpmBuildConfigurationCreationRest.


        :param build_configuration_set_ids: The build_configuration_set_ids of this BpmBuildConfigurationCreationRest.
        :type: list[int]
        """
        self._build_configuration_set_ids = build_configuration_set_ids

    @property
    def generic_parameters(self):
        """
        Gets the generic_parameters of this BpmBuildConfigurationCreationRest.


        :return: The generic_parameters of this BpmBuildConfigurationCreationRest.
        :rtype: dict(str, str)
        """
        return self._generic_parameters

    @generic_parameters.setter
    def generic_parameters(self, generic_parameters):
        """
        Sets the generic_parameters of this BpmBuildConfigurationCreationRest.


        :param generic_parameters: The generic_parameters of this BpmBuildConfigurationCreationRest.
        :type: dict(str, str)
        """
        self._generic_parameters = generic_parameters

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
