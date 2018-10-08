# coding: utf-8

from teamcity.custom.model import TeamCityObject


# from teamcity.models.issue import Issue  # noqa: F401,E501


class Issues(TeamCityObject):
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
        'issues': 'list[Issue]'
    }

    attribute_map = {
        'issues': 'issues'
    }

    def __init__(self, issues=None):  # noqa: E501
        """Issues - a model defined in Swagger"""  # noqa: E501
        super(Issues, self).__init__()

        self._issues = None
        self.discriminator = None

        if issues is not None:
            self.issues = issues

    @property
    def issues(self):
        """Gets the issues of this Issues.  # noqa: E501


        :return: The issues of this Issues.  # noqa: E501
        :rtype: list[Issue]
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        """Sets the issues of this Issues.


        :param issues: The issues of this Issues.  # noqa: E501
        :type: list[Issue]
        """

        self._issues = issues

