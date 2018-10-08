# coding: utf-8

from teamcity.custom.model import TeamCityObject


# from teamcity.models.vcs_root_instance import VcsRootInstance  # noqa: F401,E501


class Revision(TeamCityObject):
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
        'checkout_rules': 'str',
        'internal_version': 'str',
        'vcs_root_instance': 'VcsRootInstance',
        'vcs_branch_name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'checkout_rules': 'checkout-rules',
        'internal_version': 'internalVersion',
        'vcs_root_instance': 'vcs-root-instance',
        'vcs_branch_name': 'vcsBranchName',
        'version': 'version'
    }

    def __init__(self, checkout_rules=None, internal_version=None, vcs_root_instance=None, vcs_branch_name=None, version=None):  # noqa: E501
        """Revision - a model defined in Swagger"""  # noqa: E501
        super(Revision, self).__init__()

        self._checkout_rules = None
        self._internal_version = None
        self._vcs_root_instance = None
        self._vcs_branch_name = None
        self._version = None
        self.discriminator = None

        if checkout_rules is not None:
            self.checkout_rules = checkout_rules
        if internal_version is not None:
            self.internal_version = internal_version
        if vcs_root_instance is not None:
            self.vcs_root_instance = vcs_root_instance
        if vcs_branch_name is not None:
            self.vcs_branch_name = vcs_branch_name
        if version is not None:
            self.version = version

    @property
    def checkout_rules(self):
        """Gets the checkout_rules of this Revision.  # noqa: E501


        :return: The checkout_rules of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._checkout_rules

    @checkout_rules.setter
    def checkout_rules(self, checkout_rules):
        """Sets the checkout_rules of this Revision.


        :param checkout_rules: The checkout_rules of this Revision.  # noqa: E501
        :type: str
        """

        self._checkout_rules = checkout_rules

    @property
    def internal_version(self):
        """Gets the internal_version of this Revision.  # noqa: E501


        :return: The internal_version of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._internal_version

    @internal_version.setter
    def internal_version(self, internal_version):
        """Sets the internal_version of this Revision.


        :param internal_version: The internal_version of this Revision.  # noqa: E501
        :type: str
        """

        self._internal_version = internal_version

    @property
    def vcs_root_instance(self):
        """Gets the vcs_root_instance of this Revision.  # noqa: E501


        :return: The vcs_root_instance of this Revision.  # noqa: E501
        :rtype: VcsRootInstance
        """
        return self._vcs_root_instance

    @vcs_root_instance.setter
    def vcs_root_instance(self, vcs_root_instance):
        """Sets the vcs_root_instance of this Revision.


        :param vcs_root_instance: The vcs_root_instance of this Revision.  # noqa: E501
        :type: VcsRootInstance
        """

        self._vcs_root_instance = vcs_root_instance

    @property
    def vcs_branch_name(self):
        """Gets the vcs_branch_name of this Revision.  # noqa: E501


        :return: The vcs_branch_name of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._vcs_branch_name

    @vcs_branch_name.setter
    def vcs_branch_name(self, vcs_branch_name):
        """Sets the vcs_branch_name of this Revision.


        :param vcs_branch_name: The vcs_branch_name of this Revision.  # noqa: E501
        :type: str
        """

        self._vcs_branch_name = vcs_branch_name

    @property
    def version(self):
        """Gets the version of this Revision.  # noqa: E501


        :return: The version of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Revision.


        :param version: The version of this Revision.  # noqa: E501
        :type: str
        """

        self._version = version

