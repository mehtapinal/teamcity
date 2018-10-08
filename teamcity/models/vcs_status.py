# coding: utf-8

from teamcity.custom.model import TeamCityObject


# from teamcity.models.vcs_check_status import VcsCheckStatus  # noqa: F401,E501


class VcsStatus(TeamCityObject):
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
        'current': 'VcsCheckStatus',
        'previous': 'VcsCheckStatus'
    }

    attribute_map = {
        'current': 'current',
        'previous': 'previous'
    }

    def __init__(self, current=None, previous=None):  # noqa: E501
        """VcsStatus - a model defined in Swagger"""  # noqa: E501
        super(VcsStatus, self).__init__()

        self._current = None
        self._previous = None
        self.discriminator = None

        if current is not None:
            self.current = current
        if previous is not None:
            self.previous = previous

    @property
    def current(self):
        """Gets the current of this VcsStatus.  # noqa: E501


        :return: The current of this VcsStatus.  # noqa: E501
        :rtype: VcsCheckStatus
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this VcsStatus.


        :param current: The current of this VcsStatus.  # noqa: E501
        :type: VcsCheckStatus
        """

        self._current = current

    @property
    def previous(self):
        """Gets the previous of this VcsStatus.  # noqa: E501


        :return: The previous of this VcsStatus.  # noqa: E501
        :rtype: VcsCheckStatus
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this VcsStatus.


        :param previous: The previous of this VcsStatus.  # noqa: E501
        :type: VcsCheckStatus
        """

        self._previous = previous

