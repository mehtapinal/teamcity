# coding: utf-8

from teamcity.custom.model import TeamCityObject



class Role(TeamCityObject):
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
        'href': 'str',
        'role_id': 'str',
        'scope': 'str'
    }

    attribute_map = {
        'href': 'href',
        'role_id': 'roleId',
        'scope': 'scope'
    }

    def __init__(self, href=None, role_id=None, scope=None):  # noqa: E501
        """Role - a model defined in Swagger"""  # noqa: E501
        super(Role, self).__init__()

        self._href = None
        self._role_id = None
        self._scope = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if role_id is not None:
            self.role_id = role_id
        if scope is not None:
            self.scope = scope

    @property
    def href(self):
        """Gets the href of this Role.  # noqa: E501


        :return: The href of this Role.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Role.


        :param href: The href of this Role.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def role_id(self):
        """Gets the role_id of this Role.  # noqa: E501


        :return: The role_id of this Role.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this Role.


        :param role_id: The role_id of this Role.  # noqa: E501
        :type: str
        """

        self._role_id = role_id

    @property
    def scope(self):
        """Gets the scope of this Role.  # noqa: E501


        :return: The scope of this Role.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Role.


        :param scope: The scope of this Role.  # noqa: E501
        :type: str
        """

        self._scope = scope

