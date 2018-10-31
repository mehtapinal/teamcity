# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.step import Step  # noqa: F401,E501


class Steps(TeamCityObject):
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
        'step': 'list[Step]'
    }

    attribute_map = {
        'count': 'count',
        'step': 'step'
    }

    def __init__(self, count=None, step=None, teamcity=None):  # noqa: E501
        """Steps - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._step = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if step is not None:
            self.step = step
        super(Steps, self).__init__(teamcity=teamcity)

    @property
    def count(self):
        """Gets the count of this Steps.  # noqa: E501


        :return: The count of this Steps.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Steps.


        :param count: The count of this Steps.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def step(self):
        """Gets the step of this Steps.  # noqa: E501


        :return: The step of this Steps.  # noqa: E501
        :rtype: list[Step]
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this Steps.


        :param step: The step of this Steps.  # noqa: E501
        :type: list[Step]
        """

        self._step = step
