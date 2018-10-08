# coding: utf-8

from teamcity.custom.model import TeamCityObject


# from teamcity.models.group import Group  # noqa: F401,E501


class Groups(TeamCityObject):
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
        'count': 'int',
        'group': 'list[Group]'
    }

    attribute_map = {
        'count': 'count',
        'group': 'group'
    }

    def __init__(self, count=None, group=None):  # noqa: E501
        """Groups - a model defined in Swagger"""  # noqa: E501
        super(Groups, self).__init__()

        self._count = None
        self._group = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if group is not None:
            self.group = group

    @property
    def count(self):
        """Gets the count of this Groups.  # noqa: E501


        :return: The count of this Groups.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Groups.


        :param count: The count of this Groups.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def group(self):
        """Gets the group of this Groups.  # noqa: E501


        :return: The group of this Groups.  # noqa: E501
        :rtype: list[Group]
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Groups.


        :param group: The group of this Groups.  # noqa: E501
        :type: list[Group]
        """

        self._group = group

