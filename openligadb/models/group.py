# coding: utf-8

"""
    OpenLigaDB-API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Group(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'group_name': 'str',
        'group_order_id': 'int',
        'group_id': 'int'
    }

    attribute_map = {
        'group_name': 'groupName',
        'group_order_id': 'groupOrderID',
        'group_id': 'groupID'
    }

    def __init__(self, group_name=None, group_order_id=None, group_id=None):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501
        self._group_name = None
        self._group_order_id = None
        self._group_id = None
        self.discriminator = None
        if group_name is not None:
            self.group_name = group_name
        if group_order_id is not None:
            self.group_order_id = group_order_id
        if group_id is not None:
            self.group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this Group.  # noqa: E501


        :return: The group_name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this Group.


        :param group_name: The group_name of this Group.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def group_order_id(self):
        """Gets the group_order_id of this Group.  # noqa: E501


        :return: The group_order_id of this Group.  # noqa: E501
        :rtype: int
        """
        return self._group_order_id

    @group_order_id.setter
    def group_order_id(self, group_order_id):
        """Sets the group_order_id of this Group.


        :param group_order_id: The group_order_id of this Group.  # noqa: E501
        :type: int
        """

        self._group_order_id = group_order_id

    @property
    def group_id(self):
        """Gets the group_id of this Group.  # noqa: E501


        :return: The group_id of this Group.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this Group.


        :param group_id: The group_id of this Group.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Group, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
