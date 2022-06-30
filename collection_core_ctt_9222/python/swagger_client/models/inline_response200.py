# coding: utf-8

"""
    Collection payments

    <img src=\"https://devtest.baokim.vn/collection/core_ctt/image/Picture1.png\" class=\"image-collection-payment\" /> <p><strong>Note:</strong></p> <p>+ In case PARTNER want to use collect via Virtual Account, PARTNER will need to buid:</p> <p style=\"padding-left: 50px;\">     - <a href=\"#operations-Virtual_Account_4\\.0-8442c69ffbaf4b3677a52fa3ebcef6d4\">Register virtual account</a> <br>     - <a href=\"#operations-Virtual_Account_4\\.0-1796c61005edee3976097a607fe9dbaa\">Update virtual account informations</a> <br>     - <a href=\"#operations-tag-Notice_of_collection_transaction\">Notice of collection transaction</a> <br> </p>  # noqa: E501

    OpenAPI spec version: 2.3 and 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse200(object):
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
        'response_code': 'float',
        'response_message': 'str',
        'partner_code': 'str',
        'order_id': 'str',
        'collect_amount_min': 'float',
        'collect_amount_max': 'float',
        'expire_date': 'str',
        'account_info': 'list[object]'
    }

    attribute_map = {
        'response_code': 'ResponseCode',
        'response_message': 'ResponseMessage',
        'partner_code': 'PartnerCode',
        'order_id': 'OrderId',
        'collect_amount_min': 'CollectAmountMin',
        'collect_amount_max': 'CollectAmountMax',
        'expire_date': 'ExpireDate',
        'account_info': 'AccountInfo'
    }

    def __init__(self, response_code=None, response_message=None, partner_code=None, order_id=None, collect_amount_min=None, collect_amount_max=None, expire_date=None, account_info=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._response_code = None
        self._response_message = None
        self._partner_code = None
        self._order_id = None
        self._collect_amount_min = None
        self._collect_amount_max = None
        self._expire_date = None
        self._account_info = None
        self.discriminator = None
        if response_code is not None:
            self.response_code = response_code
        if response_message is not None:
            self.response_message = response_message
        if partner_code is not None:
            self.partner_code = partner_code
        if order_id is not None:
            self.order_id = order_id
        if collect_amount_min is not None:
            self.collect_amount_min = collect_amount_min
        if collect_amount_max is not None:
            self.collect_amount_max = collect_amount_max
        if expire_date is not None:
            self.expire_date = expire_date
        if account_info is not None:
            self.account_info = account_info

    @property
    def response_code(self):
        """Gets the response_code of this InlineResponse200.  # noqa: E501

        Response code  # noqa: E501

        :return: The response_code of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this InlineResponse200.

        Response code  # noqa: E501

        :param response_code: The response_code of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._response_code = response_code

    @property
    def response_message(self):
        """Gets the response_message of this InlineResponse200.  # noqa: E501

        Response message  # noqa: E501

        :return: The response_message of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._response_message

    @response_message.setter
    def response_message(self, response_message):
        """Sets the response_message of this InlineResponse200.

        Response message  # noqa: E501

        :param response_message: The response_message of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._response_message = response_message

    @property
    def partner_code(self):
        """Gets the partner_code of this InlineResponse200.  # noqa: E501

        BAOKIM  # noqa: E501

        :return: The partner_code of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._partner_code

    @partner_code.setter
    def partner_code(self, partner_code):
        """Sets the partner_code of this InlineResponse200.

        BAOKIM  # noqa: E501

        :param partner_code: The partner_code of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._partner_code = partner_code

    @property
    def order_id(self):
        """Gets the order_id of this InlineResponse200.  # noqa: E501

        Unique id for each VA  # noqa: E501

        :return: The order_id of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InlineResponse200.

        Unique id for each VA  # noqa: E501

        :param order_id: The order_id of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def collect_amount_min(self):
        """Gets the collect_amount_min of this InlineResponse200.  # noqa: E501

        Min collect amount (Min 50.000 vnd)  # noqa: E501

        :return: The collect_amount_min of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._collect_amount_min

    @collect_amount_min.setter
    def collect_amount_min(self, collect_amount_min):
        """Sets the collect_amount_min of this InlineResponse200.

        Min collect amount (Min 50.000 vnd)  # noqa: E501

        :param collect_amount_min: The collect_amount_min of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._collect_amount_min = collect_amount_min

    @property
    def collect_amount_max(self):
        """Gets the collect_amount_max of this InlineResponse200.  # noqa: E501

        Max collect amount (Max 50.000.000vnd)  # noqa: E501

        :return: The collect_amount_max of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._collect_amount_max

    @collect_amount_max.setter
    def collect_amount_max(self, collect_amount_max):
        """Sets the collect_amount_max of this InlineResponse200.

        Max collect amount (Max 50.000.000vnd)  # noqa: E501

        :param collect_amount_max: The collect_amount_max of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._collect_amount_max = collect_amount_max

    @property
    def expire_date(self):
        """Gets the expire_date of this InlineResponse200.  # noqa: E501

        Expire date. Format: YYYYMM-DD HH:II:SS  # noqa: E501

        :return: The expire_date of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """Sets the expire_date of this InlineResponse200.

        Expire date. Format: YYYYMM-DD HH:II:SS  # noqa: E501

        :param expire_date: The expire_date of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._expire_date = expire_date

    @property
    def account_info(self):
        """Gets the account_info of this InlineResponse200.  # noqa: E501


        :return: The account_info of this InlineResponse200.  # noqa: E501
        :rtype: list[object]
        """
        return self._account_info

    @account_info.setter
    def account_info(self, account_info):
        """Sets the account_info of this InlineResponse200.


        :param account_info: The account_info of this InlineResponse200.  # noqa: E501
        :type: list[object]
        """

        self._account_info = account_info

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
        if issubclass(InlineResponse200, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other