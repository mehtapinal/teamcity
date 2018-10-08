# coding: utf-8

from teamcity.custom.model import TeamCityObject



class ProgressInfo(TeamCityObject):
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
        'current_stage_text': 'str',
        'elapsed_seconds': 'int',
        'estimated_total_seconds': 'int',
        'outdated': 'bool',
        'percentage_complete': 'int',
        'probably_hanging': 'bool'
    }

    attribute_map = {
        'current_stage_text': 'currentStageText',
        'elapsed_seconds': 'elapsedSeconds',
        'estimated_total_seconds': 'estimatedTotalSeconds',
        'outdated': 'outdated',
        'percentage_complete': 'percentageComplete',
        'probably_hanging': 'probablyHanging'
    }

    def __init__(self, current_stage_text=None, elapsed_seconds=None, estimated_total_seconds=None, outdated=False, percentage_complete=None, probably_hanging=False):  # noqa: E501
        """ProgressInfo - a model defined in Swagger"""  # noqa: E501
        super(ProgressInfo, self).__init__()

        self._current_stage_text = None
        self._elapsed_seconds = None
        self._estimated_total_seconds = None
        self._outdated = None
        self._percentage_complete = None
        self._probably_hanging = None
        self.discriminator = None

        if current_stage_text is not None:
            self.current_stage_text = current_stage_text
        if elapsed_seconds is not None:
            self.elapsed_seconds = elapsed_seconds
        if estimated_total_seconds is not None:
            self.estimated_total_seconds = estimated_total_seconds
        if outdated is not None:
            self.outdated = outdated
        if percentage_complete is not None:
            self.percentage_complete = percentage_complete
        if probably_hanging is not None:
            self.probably_hanging = probably_hanging

    @property
    def current_stage_text(self):
        """Gets the current_stage_text of this ProgressInfo.  # noqa: E501


        :return: The current_stage_text of this ProgressInfo.  # noqa: E501
        :rtype: str
        """
        return self._current_stage_text

    @current_stage_text.setter
    def current_stage_text(self, current_stage_text):
        """Sets the current_stage_text of this ProgressInfo.


        :param current_stage_text: The current_stage_text of this ProgressInfo.  # noqa: E501
        :type: str
        """

        self._current_stage_text = current_stage_text

    @property
    def elapsed_seconds(self):
        """Gets the elapsed_seconds of this ProgressInfo.  # noqa: E501


        :return: The elapsed_seconds of this ProgressInfo.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_seconds

    @elapsed_seconds.setter
    def elapsed_seconds(self, elapsed_seconds):
        """Sets the elapsed_seconds of this ProgressInfo.


        :param elapsed_seconds: The elapsed_seconds of this ProgressInfo.  # noqa: E501
        :type: int
        """

        self._elapsed_seconds = elapsed_seconds

    @property
    def estimated_total_seconds(self):
        """Gets the estimated_total_seconds of this ProgressInfo.  # noqa: E501


        :return: The estimated_total_seconds of this ProgressInfo.  # noqa: E501
        :rtype: int
        """
        return self._estimated_total_seconds

    @estimated_total_seconds.setter
    def estimated_total_seconds(self, estimated_total_seconds):
        """Sets the estimated_total_seconds of this ProgressInfo.


        :param estimated_total_seconds: The estimated_total_seconds of this ProgressInfo.  # noqa: E501
        :type: int
        """

        self._estimated_total_seconds = estimated_total_seconds

    @property
    def outdated(self):
        """Gets the outdated of this ProgressInfo.  # noqa: E501


        :return: The outdated of this ProgressInfo.  # noqa: E501
        :rtype: bool
        """
        return self._outdated

    @outdated.setter
    def outdated(self, outdated):
        """Sets the outdated of this ProgressInfo.


        :param outdated: The outdated of this ProgressInfo.  # noqa: E501
        :type: bool
        """

        self._outdated = outdated

    @property
    def percentage_complete(self):
        """Gets the percentage_complete of this ProgressInfo.  # noqa: E501


        :return: The percentage_complete of this ProgressInfo.  # noqa: E501
        :rtype: int
        """
        return self._percentage_complete

    @percentage_complete.setter
    def percentage_complete(self, percentage_complete):
        """Sets the percentage_complete of this ProgressInfo.


        :param percentage_complete: The percentage_complete of this ProgressInfo.  # noqa: E501
        :type: int
        """

        self._percentage_complete = percentage_complete

    @property
    def probably_hanging(self):
        """Gets the probably_hanging of this ProgressInfo.  # noqa: E501


        :return: The probably_hanging of this ProgressInfo.  # noqa: E501
        :rtype: bool
        """
        return self._probably_hanging

    @probably_hanging.setter
    def probably_hanging(self, probably_hanging):
        """Sets the probably_hanging of this ProgressInfo.


        :param probably_hanging: The probably_hanging of this ProgressInfo.  # noqa: E501
        :type: bool
        """

        self._probably_hanging = probably_hanging

