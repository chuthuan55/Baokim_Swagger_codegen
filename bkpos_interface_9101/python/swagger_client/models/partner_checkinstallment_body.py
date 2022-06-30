# coding: utf-8

"""
     Installment docs API

    <a href='/baokim-firm-open-api-9050'>1: Function Check Installment Support </a>  <a href='/baokim-firm-open-api-9051'>2: Function Get Bank Loan Package </a>  <a href='/baokim-firm-open-api-9052'>3: Function Create Transaction </a>  <a href='/baokim-firm-open-api-9062'>4: Function Cancel order</a>  Private key and public key Baokim is currently using digital signature by RSA-SHA1  There are several ways to generate RSA key pairs.  Way 1:  Generate your RSA key pairs online: <a href=\"http://travistidwell.com/blog/2013/09/06/an-online-rsa-public-and-private-key-generator/\" target=\"_blank\">Generate now</a>  Way 2:  Using OpenSSL software for Windows:  Step 1: Download the software at:  http://slproweb.com/products/Win32OpenSSL.html. Partner should download the installer \"OpenSSL_Light-1_0_2k\". Then install in any directory, for example \"C:\\OpenSSLWin64\"  Step 2: Access \"C:\\OpenSSLWin64\\bin\" then open the command prompt. Type the command to declare the environment config.  set OPENSSL_CONF=C:\\OpenSSL-Win64\\bin\\openssl.cfg  Step 3: Generate private key and public key  openssl genrsa -aes256 -out c:\\opensslkeys\\partner\\partner_privatekey.pem 2048  openssl rsa –in c:\\opensslkeys\\partner\\partner_privatekey.pem -pubout >c:\\opensslkeys\\partner\\partner_publickey.pem  After successful pairing, Partner will send back to Baokim the public key to authenticate the signature that the Partner sends via the API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PartnerCheckinstallmentBody(object):
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
        'request_id': 'str',
        'request_time': 'str',
        'partner_code': 'str',
        'operation': 'str',
        'card_no': 'str',
        'bank_code': 'str'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'request_time': 'RequestTime',
        'partner_code': 'PartnerCode',
        'operation': 'Operation',
        'card_no': 'CardNo',
        'bank_code': 'BankCode'
    }

    def __init__(self, request_id=None, request_time=None, partner_code=None, operation=None, card_no=None, bank_code=None):  # noqa: E501
        """PartnerCheckinstallmentBody - a model defined in Swagger"""  # noqa: E501
        self._request_id = None
        self._request_time = None
        self._partner_code = None
        self._operation = None
        self._card_no = None
        self._bank_code = None
        self.discriminator = None
        if request_id is not None:
            self.request_id = request_id
        if request_time is not None:
            self.request_time = request_time
        if partner_code is not None:
            self.partner_code = partner_code
        if operation is not None:
            self.operation = operation
        if card_no is not None:
            self.card_no = card_no
        if bank_code is not None:
            self.bank_code = bank_code

    @property
    def request_id(self):
        """Gets the request_id of this PartnerCheckinstallmentBody.  # noqa: E501


        :return: The request_id of this PartnerCheckinstallmentBody.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PartnerCheckinstallmentBody.


        :param request_id: The request_id of this PartnerCheckinstallmentBody.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def request_time(self):
        """Gets the request_time of this PartnerCheckinstallmentBody.  # noqa: E501


        :return: The request_time of this PartnerCheckinstallmentBody.  # noqa: E501
        :rtype: str
        """
        return self._request_time

    @request_time.setter
    def request_time(self, request_time):
        """Sets the request_time of this PartnerCheckinstallmentBody.


        :param request_time: The request_time of this PartnerCheckinstallmentBody.  # noqa: E501
        :type: str
        """

        self._request_time = request_time

    @property
    def partner_code(self):
        """Gets the partner_code of this PartnerCheckinstallmentBody.  # noqa: E501


        :return: The partner_code of this PartnerCheckinstallmentBody.  # noqa: E501
        :rtype: str
        """
        return self._partner_code

    @partner_code.setter
    def partner_code(self, partner_code):
        """Sets the partner_code of this PartnerCheckinstallmentBody.


        :param partner_code: The partner_code of this PartnerCheckinstallmentBody.  # noqa: E501
        :type: str
        """

        self._partner_code = partner_code

    @property
    def operation(self):
        """Gets the operation of this PartnerCheckinstallmentBody.  # noqa: E501


        :return: The operation of this PartnerCheckinstallmentBody.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this PartnerCheckinstallmentBody.


        :param operation: The operation of this PartnerCheckinstallmentBody.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def card_no(self):
        """Gets the card_no of this PartnerCheckinstallmentBody.  # noqa: E501


        :return: The card_no of this PartnerCheckinstallmentBody.  # noqa: E501
        :rtype: str
        """
        return self._card_no

    @card_no.setter
    def card_no(self, card_no):
        """Sets the card_no of this PartnerCheckinstallmentBody.


        :param card_no: The card_no of this PartnerCheckinstallmentBody.  # noqa: E501
        :type: str
        """

        self._card_no = card_no

    @property
    def bank_code(self):
        """Gets the bank_code of this PartnerCheckinstallmentBody.  # noqa: E501


        :return: The bank_code of this PartnerCheckinstallmentBody.  # noqa: E501
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this PartnerCheckinstallmentBody.


        :param bank_code: The bank_code of this PartnerCheckinstallmentBody.  # noqa: E501
        :type: str
        """

        self._bank_code = bank_code

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
        if issubclass(PartnerCheckinstallmentBody, dict):
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
        if not isinstance(other, PartnerCheckinstallmentBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
