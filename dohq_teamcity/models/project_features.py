# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.project_feature import ProjectFeature  # noqa: F401,E501


class ProjectFeatures(TeamCityObject):
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
        'href': 'str',
        'project_feature': 'list[ProjectFeature]'
    }

    attribute_map = {
        'count': 'count',
        'href': 'href',
        'project_feature': 'projectFeature'
    }

    def __init__(self, count=None, href=None, project_feature=None, teamcity=None):  # noqa: E501
        """ProjectFeatures - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._href = None
        self._project_feature = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if href is not None:
            self.href = href
        if project_feature is not None:
            self.project_feature = project_feature
        super(ProjectFeatures, self).__init__(teamcity=teamcity)

    @property
    def count(self):
        """Gets the count of this ProjectFeatures.  # noqa: E501


        :return: The count of this ProjectFeatures.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ProjectFeatures.


        :param count: The count of this ProjectFeatures.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def href(self):
        """Gets the href of this ProjectFeatures.  # noqa: E501


        :return: The href of this ProjectFeatures.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ProjectFeatures.


        :param href: The href of this ProjectFeatures.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def project_feature(self):
        """Gets the project_feature of this ProjectFeatures.  # noqa: E501


        :return: The project_feature of this ProjectFeatures.  # noqa: E501
        :rtype: list[ProjectFeature]
        """
        return self._project_feature

    @project_feature.setter
    def project_feature(self, project_feature):
        """Sets the project_feature of this ProjectFeatures.


        :param project_feature: The project_feature of this ProjectFeatures.  # noqa: E501
        :type: list[ProjectFeature]
        """

        self._project_feature = project_feature
