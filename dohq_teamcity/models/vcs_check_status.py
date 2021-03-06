# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class VcsCheckStatus(TeamCityObject):
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
        'status': 'str',
        'requestor_type': 'str',
        'timestamp': 'str'
    }

    attribute_map = {
        'status': 'status',
        'requestor_type': 'requestorType',
        'timestamp': 'timestamp'
    }

    def __init__(self, status=None, requestor_type=None, timestamp=None, teamcity=None):  # noqa: E501
        """VcsCheckStatus - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._requestor_type = None
        self._timestamp = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if requestor_type is not None:
            self.requestor_type = requestor_type
        if timestamp is not None:
            self.timestamp = timestamp
        super(VcsCheckStatus, self).__init__(teamcity=teamcity)

    @property
    def status(self):
        """Gets the status of this VcsCheckStatus.  # noqa: E501


        :return: The status of this VcsCheckStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VcsCheckStatus.


        :param status: The status of this VcsCheckStatus.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def requestor_type(self):
        """Gets the requestor_type of this VcsCheckStatus.  # noqa: E501


        :return: The requestor_type of this VcsCheckStatus.  # noqa: E501
        :rtype: str
        """
        return self._requestor_type

    @requestor_type.setter
    def requestor_type(self, requestor_type):
        """Sets the requestor_type of this VcsCheckStatus.


        :param requestor_type: The requestor_type of this VcsCheckStatus.  # noqa: E501
        :type: str
        """

        self._requestor_type = requestor_type

    @property
    def timestamp(self):
        """Gets the timestamp of this VcsCheckStatus.  # noqa: E501


        :return: The timestamp of this VcsCheckStatus.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this VcsCheckStatus.


        :param timestamp: The timestamp of this VcsCheckStatus.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp
