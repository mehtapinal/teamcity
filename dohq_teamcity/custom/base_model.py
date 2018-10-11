import pprint

import six

# import for typing only
try:
    from dohq_teamcity.custom.client import TeamCity
except:
    pass


class TeamCityException(Exception):
    pass


class TeamCityCodeException(Exception):
    pass


class TeamCityRuntimeException(Exception):
    pass


class TeamCityObject(object):
    swagger_types = {}

    def __init__(self, teamcity=None, *args, **kwargs):
        self.teamcity = teamcity  # type: TeamCity

    @property
    def locator(self):
        if self.id is None:
            raise TeamCityRuntimeException("object does not have attribute id: ''".format(self))
        return "id:{}".format(self.id)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, type(self)):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


class ReadMixin(object):
    def _read(self):
        return None

    def read(self):
        load_func = self._read()
        if load_func is None:
            raise TeamCityCodeException("load_function is not defined in class '{}'".format(self.__class__.__name__))
        self = load_func(self.locator)
        return self
