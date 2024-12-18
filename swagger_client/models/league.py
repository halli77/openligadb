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

class League(object):
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
        'league_id': 'int',
        'league_name': 'str',
        'league_shortcut': 'str',
        'league_season': 'str',
        'sport': 'Sport'
    }

    attribute_map = {
        'league_id': 'leagueId',
        'league_name': 'leagueName',
        'league_shortcut': 'leagueShortcut',
        'league_season': 'leagueSeason',
        'sport': 'sport'
    }

    def __init__(self, league_id=None, league_name=None, league_shortcut=None, league_season=None, sport=None):  # noqa: E501
        """League - a model defined in Swagger"""  # noqa: E501
        self._league_id = None
        self._league_name = None
        self._league_shortcut = None
        self._league_season = None
        self._sport = None
        self.discriminator = None
        if league_id is not None:
            self.league_id = league_id
        if league_name is not None:
            self.league_name = league_name
        if league_shortcut is not None:
            self.league_shortcut = league_shortcut
        if league_season is not None:
            self.league_season = league_season
        if sport is not None:
            self.sport = sport

    @property
    def league_id(self):
        """Gets the league_id of this League.  # noqa: E501


        :return: The league_id of this League.  # noqa: E501
        :rtype: int
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this League.


        :param league_id: The league_id of this League.  # noqa: E501
        :type: int
        """

        self._league_id = league_id

    @property
    def league_name(self):
        """Gets the league_name of this League.  # noqa: E501


        :return: The league_name of this League.  # noqa: E501
        :rtype: str
        """
        return self._league_name

    @league_name.setter
    def league_name(self, league_name):
        """Sets the league_name of this League.


        :param league_name: The league_name of this League.  # noqa: E501
        :type: str
        """

        self._league_name = league_name

    @property
    def league_shortcut(self):
        """Gets the league_shortcut of this League.  # noqa: E501


        :return: The league_shortcut of this League.  # noqa: E501
        :rtype: str
        """
        return self._league_shortcut

    @league_shortcut.setter
    def league_shortcut(self, league_shortcut):
        """Sets the league_shortcut of this League.


        :param league_shortcut: The league_shortcut of this League.  # noqa: E501
        :type: str
        """

        self._league_shortcut = league_shortcut

    @property
    def league_season(self):
        """Gets the league_season of this League.  # noqa: E501


        :return: The league_season of this League.  # noqa: E501
        :rtype: str
        """
        return self._league_season

    @league_season.setter
    def league_season(self, league_season):
        """Sets the league_season of this League.


        :param league_season: The league_season of this League.  # noqa: E501
        :type: str
        """

        self._league_season = league_season

    @property
    def sport(self):
        """Gets the sport of this League.  # noqa: E501


        :return: The sport of this League.  # noqa: E501
        :rtype: Sport
        """
        return self._sport

    @sport.setter
    def sport(self, sport):
        """Sets the sport of this League.


        :param sport: The sport of this League.  # noqa: E501
        :type: Sport
        """

        self._sport = sport

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
        if issubclass(League, dict):
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
        if not isinstance(other, League):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
