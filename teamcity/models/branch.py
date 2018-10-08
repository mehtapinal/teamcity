# coding: utf-8

from teamcity.custom.model import TeamCityObject



class Branch(TeamCityObject):
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
        'default': 'bool',
        'name': 'str',
        'unspecified': 'bool'
    }

    attribute_map = {
        'default': 'default',
        'name': 'name',
        'unspecified': 'unspecified'
    }

    def __init__(self, default=False, name=None, unspecified=False):  # noqa: E501
        """Branch - a model defined in Swagger"""  # noqa: E501
        super(Branch, self).__init__()

        self._default = None
        self._name = None
        self._unspecified = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if name is not None:
            self.name = name
        if unspecified is not None:
            self.unspecified = unspecified

    @property
    def default(self):
        """Gets the default of this Branch.  # noqa: E501


        :return: The default of this Branch.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this Branch.


        :param default: The default of this Branch.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def name(self):
        """Gets the name of this Branch.  # noqa: E501


        :return: The name of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Branch.


        :param name: The name of this Branch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def unspecified(self):
        """Gets the unspecified of this Branch.  # noqa: E501


        :return: The unspecified of this Branch.  # noqa: E501
        :rtype: bool
        """
        return self._unspecified

    @unspecified.setter
    def unspecified(self, unspecified):
        """Sets the unspecified of this Branch.


        :param unspecified: The unspecified of this Branch.  # noqa: E501
        :type: bool
        """

        self._unspecified = unspecified

