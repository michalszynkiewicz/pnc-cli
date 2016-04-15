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


class BuiltArtifact(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuiltArtifact - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'identifier': 'str',
            'repo_type': 'str',
            'checksum': 'str',
            'filename': 'str',
            'deploy_url': 'str',
            'type': 'str',
            'dependant_build_records': 'list[BuildRecord]',
            'build_records': 'list[BuildRecord]',
            'field_handler': 'FieldHandler'
        }

        self.attribute_map = {
            'id': 'id',
            'identifier': 'identifier',
            'repo_type': 'repoType',
            'checksum': 'checksum',
            'filename': 'filename',
            'deploy_url': 'deployUrl',
            'type': 'type',
            'dependant_build_records': 'dependantBuildRecords',
            'build_records': 'buildRecords',
            'field_handler': 'fieldHandler'
        }

        self._id = None
        self._identifier = None
        self._repo_type = None
        self._checksum = None
        self._filename = None
        self._deploy_url = None
        self._type = None
        self._dependant_build_records = None
        self._build_records = None
        self._field_handler = None

    @property
    def id(self):
        """
        Gets the id of this BuiltArtifact.


        :return: The id of this BuiltArtifact.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuiltArtifact.


        :param id: The id of this BuiltArtifact.
        :type: int
        """
        self._id = id

    @property
    def identifier(self):
        """
        Gets the identifier of this BuiltArtifact.


        :return: The identifier of this BuiltArtifact.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this BuiltArtifact.


        :param identifier: The identifier of this BuiltArtifact.
        :type: str
        """
        self._identifier = identifier

    @property
    def repo_type(self):
        """
        Gets the repo_type of this BuiltArtifact.


        :return: The repo_type of this BuiltArtifact.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        """
        Sets the repo_type of this BuiltArtifact.


        :param repo_type: The repo_type of this BuiltArtifact.
        :type: str
        """
        allowed_values = ["MAVEN", "DOCKER_REGISTRY", "NPM", "COCOA_POD"]
        if repo_type not in allowed_values:
            raise ValueError(
                "Invalid value for `repo_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._repo_type = repo_type

    @property
    def checksum(self):
        """
        Gets the checksum of this BuiltArtifact.


        :return: The checksum of this BuiltArtifact.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """
        Sets the checksum of this BuiltArtifact.


        :param checksum: The checksum of this BuiltArtifact.
        :type: str
        """
        self._checksum = checksum

    @property
    def filename(self):
        """
        Gets the filename of this BuiltArtifact.


        :return: The filename of this BuiltArtifact.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this BuiltArtifact.


        :param filename: The filename of this BuiltArtifact.
        :type: str
        """
        self._filename = filename

    @property
    def deploy_url(self):
        """
        Gets the deploy_url of this BuiltArtifact.


        :return: The deploy_url of this BuiltArtifact.
        :rtype: str
        """
        return self._deploy_url

    @deploy_url.setter
    def deploy_url(self, deploy_url):
        """
        Sets the deploy_url of this BuiltArtifact.


        :param deploy_url: The deploy_url of this BuiltArtifact.
        :type: str
        """
        self._deploy_url = deploy_url

    @property
    def type(self):
        """
        Gets the type of this BuiltArtifact.


        :return: The type of this BuiltArtifact.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BuiltArtifact.


        :param type: The type of this BuiltArtifact.
        :type: str
        """
        self._type = type

    @property
    def dependant_build_records(self):
        """
        Gets the dependant_build_records of this BuiltArtifact.


        :return: The dependant_build_records of this BuiltArtifact.
        :rtype: list[BuildRecord]
        """
        return self._dependant_build_records

    @dependant_build_records.setter
    def dependant_build_records(self, dependant_build_records):
        """
        Sets the dependant_build_records of this BuiltArtifact.


        :param dependant_build_records: The dependant_build_records of this BuiltArtifact.
        :type: list[BuildRecord]
        """
        self._dependant_build_records = dependant_build_records

    @property
    def build_records(self):
        """
        Gets the build_records of this BuiltArtifact.


        :return: The build_records of this BuiltArtifact.
        :rtype: list[BuildRecord]
        """
        return self._build_records

    @build_records.setter
    def build_records(self, build_records):
        """
        Sets the build_records of this BuiltArtifact.


        :param build_records: The build_records of this BuiltArtifact.
        :type: list[BuildRecord]
        """
        self._build_records = build_records

    @property
    def field_handler(self):
        """
        Gets the field_handler of this BuiltArtifact.


        :return: The field_handler of this BuiltArtifact.
        :rtype: FieldHandler
        """
        return self._field_handler

    @field_handler.setter
    def field_handler(self, field_handler):
        """
        Sets the field_handler of this BuiltArtifact.


        :param field_handler: The field_handler of this BuiltArtifact.
        :type: FieldHandler
        """
        self._field_handler = field_handler

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