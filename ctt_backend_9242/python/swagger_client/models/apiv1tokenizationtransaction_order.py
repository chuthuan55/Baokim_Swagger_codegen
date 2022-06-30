# coding: utf-8

"""
    Baokim Payment Gateway API Documentation

    __Introduction:__  Bao Kim Payment gateway is an open payment platform, Bao Kim provides a full range of APIs that allow merchants to integrate between applications (web/app) with Bao Kim Payment Gateway to receive payment for your order, check your payment reconciliation.  For example, merchants can perform the following tasks with Bao Kim API. Receive payment for orders on your application (web/app) by sending orders to Bao Kim and display the payment interface for buyers to pay. Reconciliation and search for information of transaction payments, refund transactions, merchants you manage, payment status of orders to perform reconciliation.  You can find out more about Bao Kim at [Baokim.vn](https://baokim.vn).  __Security Method:__ Bao Kim API uses JSON Web Token (JWT), is a required parameter for every request to the API, follow the steps: * Use the assigned API Key and HS256 encryption algorithm to encrypt the JWT (check sample code) * JWT expire in the 60s after created * When request to API, jwt need to pass by 1 of 2 methods: Request Header jwt = Bearer $JWT / Query parameter(url param) &jwt=$JWT  __Sandbox(Test) Enviroment:__ * API key/sec: a18ff78e7a9e44f38de372e093d87ca1 / 9623ac03057e433f95d86cf4f3bef5cc * Portal URL: https://devtest.baokim.vn:9244/login * Merchant ID: 40002 * Card test ATM card:   * Bank: Saigonbank   * Card Number: 9704000000000018   * Card Holder: NGUYEN VAN A   * Effective date: 03/07   * OTP: otp * Card test Debit or credit card:   * Card Number: 5123450000000008   * Valid thru: 12/22   * CVN: 100  __Basic integration process__  This is the simplest and fastest integration process, but please learn more about the Pro integration process below with more advantages to make the right choice.  <img class=\"dia_img\" src=\"../swagger/images/BasicPaymentIntegrationDiagram.svg\" alt=\"\">  Advantages: * Simple integration, only 2 steps of processing are required to send payment request (API Send Order) and confirm payment results.  Defect: * Customers cannot view the payment methods to choose (eg bank list ...) right on the merchant's interface. Customers will choose the payment method on Bao Kim's payment interface.  __Pro integration process (advanced)__  Technically, the only difference between Pro integration and basic integration is the Web / App merchant that uses API Bank Payment Method List to load the list of payment methods and display on its interface to users. Select, then send these parameters along with the order to Bao Kim via the Send Order API  <img class=\"dia_img\" src=\"../swagger/images/PaymentProIntegrationDiagram.svg\" alt=\"\">  The main advantage of Pro integration: * Web / Merchant App can display the list of payment methods customers can use (for Bao Kim, Banks), * When the customer has chosen a payment method, the payment process will be transferred directly from the Web / Merchant App to the bank page (no Bao Kim payment page will be displayed) * Customers feel that the Web / App merchant accepts payment of most domestic banks, increases reliability, professionalism, and anticipates the payment options they have.  Defect: * Technical processing must be performed to display payment methods on the Web / Merchant App interface.  __Payment via Internet Banking (comming soon)__  Basically, payment via Internet Banking is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  However, if you want to be simpler for your customers by displaying your Internet Banking account information on your interface instead of having to redirect to Bao Kim, handle the shortening process below:  <img class=\"dia_img\" src=\"../swagger/images/InternetBankingPaymentIntegrationDiagram.svg\" alt=\"\">  __Payment by QRCode__  Payment by QRCode is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  For Pro integration, if you want to simplify for customers by displaying QRCode images on your interface instead of having to redirect to Bao Kim, please proceed with the shortened process below:  <img class=\"dia_img\" src=\"../swagger/images/QRCodePaymentIntegration.svg\" alt=\"\">  __Installment payment__  Payment by QRCode is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  Customers before payment need to take one more step to select the issuing bank and the term and installment payment (3/6/9/12 months), please refer to the process below:  <img class=\"dia_img\" src=\"../swagger/images/Quy-trinh-thanh-toan-tra-gop.svg\" alt=\"\">  __Virtual account payment__  <strong>Step 1: Create virtual account</strong> * Call to the API ‘payment/api/v4/create-virtual-account-payment’ with parameters:   * mrc_uuid: user_id of merchant (unique)   * mrc_uuid: name: user name   * mrc_uuid: mrc_id: ID Merchant on integrated website  <strong>Step 2: Receive payment results</strong> * After the User has paid, Bao Kim will record the transaction and then return the results to Merchant via webhook.  Please refer to the procedure below:  <img class=\"dia_img\" src=\"../swagger/images/quy-trinh-tao-tai-khoan-ao.svg\" alt=\"\">   __Payment via momo e-wallet__  Payment via momo e-wallet is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  <img class=\"dia_img\" src=\"../swagger/images/PayByMoMo.svg\" alt=\"\">  __Payment using module Checkout__  <strong>Step 1: Install package:</strong> * Open Terminal and run command: <strong>composer require baokim/baokim-sdk</strong> * Next, run command: <strong>composer dump-autoload</strong>  <strong>Step 2: Conduct integration</strong>  For one-time payments, create a Session with line_items. Line items represent a list of items the customer is purchasing.  Line_items takes the form of an array, refer to the sample code to the right:  $payment_method_types = [1, 2, 3];  payment_method_types is an array (1: Payment by ATM, 2: Payment by QRCode, 3: Payment By Visa).  When your customer successfully completes their payment, they are redirected to the success_url, a page on your website that informs the customer that their payment was successful.  When your customer clicks on your logo in a Checkout Session without completing a payment, Checkout redirects them back to your website by navigating to the cancel_url. Typically, this is the page on your website that the customer viewed prior to redirecting to Checkout.  <strong>Create Payment Session</strong>  Creating a Checkout Session returns $session include information of session saved in Bảo Kim, and payment_url. You need redirect browser to payment_urlto proceed with the payment  __Payment confirmation:__  After the customer makes a successful payment, Bao Kim will send a Webhook notification to the Web/App merchant, then redirect the customer browser to url_success on order with data. Web/App merchant has two ways to confirm the payment result of the order:  1. Web/App merchant receive Webhook notification Bao Kim sent by parameter \"webhooks\" on order (Recommended) 2. After the user pay, Bao Kim redirects the browser to the url_success on the order with the payment result, the Web/App merchant handles results return on url_success (this way may be affected by customer transmission failure)  In both ways, the order is considered successful payment when: * Order status \"stat\" == \"c\" * Payment transaction of order status \"stat\" == 1 * Order amount (total_amount) match with the merchant's order amount  __Webhook Notification:__  Webhook notification is a mechanism to notify Web/App merchants when an order is successfully paid through an HTTP POST request. * How to receive webhook notifications?   * When sending an order to Bao Kim through API Send Order, remember to pass the webhooks parameter as described   * When your order is successfully paid, Bao Kim will POST the payment data to the URL on the webhooks parameter in the order. * How many times will a Webhook notification be sent?   * Send up to 10 times   * Every 5 minutes   * Stop sending when receiving a json string with err_code = 0, eg {\"err_code\": \"0\", \"message\": \"some message\"}   (help Bao Kim determine that the merchant has successfully received the notification)  Description of data on webhook notification: * Method: POST * Header: Content-Type: application/json * Body (check sample code on the right side)  Steps to check and handle when receiving webhook notification: 1. Check the integrity of the received data by checking the correctness of the signature as follows (See sample PHP code on the right tab, under the webhook data description):   * Use the secret value in the key/secret pair in your API Key   * Using the hash_hmac algorithm with sha256, sign the data you receive (except for the $sign field, of course) => $yourSign   * Compare the signature you generated ($yourSign) with the signature you received ($sign), if not the same => data is not incomplete 2. Check order payment status, payment transaction, payment amount, order completion   * Check order status ($order->stat == 'c' //completed)   * Check if the order information ($order) is correct with the order information on your web/app   * If the above checks are correct, you can be sure that the order has been paid and can be completed. 3. Returns JSON string with err_code = 0, eg {\"err_code\": \"0\", \"message\": \"some message\"} so that Bao Kim knows that the merchant has received the notice and does not continue to send it back. The maximum length of the returned data is 255 characters.  Example Webhook:      {       \"order\":{         \"id\":82127,         \"user_id\":1000007,         \"mrc_order_id\":\"Nam1645759079\",         \"txn_id\":69154,         \"ref_no\":null,         \"merchant_id\":40187,         \"total_amount\":3000000,         \"description\":\"eqxI4W4HFUPwyNxH\",         \"items\":\"{           \"period\":3,           \"total_amount\":\"3090000.00\",           \"down_payment\":\"750000.00\",           \"down_payment_percent\":\"25.00\",           \"paylater_amount\":\"2250000.00\",           \"pay_per_month\":\"780000.00\",           \"user_fee\":\"90000\",           \"merchant_fee\":\"90000\"         }\",         \"url_success\":\"https://www.google.com/\",         \"url_cancel\":null,         \"url_detail\":\"https://www.google.com/\",         \"stat\":\"c\",         \"lang\":\"en\",         \"type\":1,         \"bpm_id\":\"339\",         \"accept_qrpay\":1,         \"accept_bank\":1,         \"accept_cc\":1,         \"accept_ib\":1,         \"accept_ewallet\":1,         \"accept_installments\":1,         \"email\":\"2@bk.vn\",         \"name\":\"baokimjsc111\",         \"webhooks\":\"https://google.com\",         \"customer_name\":\"Nguyen Thanh nam\",         \"customer_email\":\"testpay@gmail.com\",         \"customer_phone\":\"84328271591\",         \"customer_address\":\"102 thai thinh\",         \"created_at\":\"2022-02-25 10:18:01\",         \"updated_at\":\"2022-02-25 10:23:12\"       },       \"txn\":{         \"id\":69154,         \"reference_id\":\"bk_82127_69154_41j\",         \"user_id\":1000007,         \"merchant_id\":40187,         \"order_id\":82127,         \"mrc_order_id\":\"nam1645759079\",         \"total_amount\":750550,         \"amount\":750000,         \"fee_amount\":0,         \"bank_fee_amount\":550,         \"bank_fix_fee_amount\":550,         \"fee_payer\":1,         \"bank_fee_payer\":1,         \"auth_code\":null,         \"auth_time\":\"\",         \"ref_no\":null,         \"bpm_id\":\"97\",         \"bank_ref_no\":\"507800079\",         \"bpm_type\":1,         \"gateway\":\"\",         \"stat\":1,         \"init_token\":null,         \"description\":\"eqxi4w4hfupwynxh\",         \"customer_email\":\"testpay@gmail.com\",         \"customer_phone\":\"84328271591\",         \"completed_at\":\"2022-02-25 10:23:12\",         \"created_at\":\"2022-02-25 10:18:24\",         \"updated_at\":\"2022-02-25 10:23:12\",         \"deleted_at\":null       },       \"dataToken\":[],       \"sign\":\"ffc020303d1ed4fbe5df95d83261524793358ab0a8e363ae265e3fc2c33dc560\"     }  __Data return on url_success:__  If the merchant web/app gets notifications through Webhook Notification, you can skip processing the return data on url_success and simply show the successful payment page to the customer. Otherwise, verify the return data on url_success as follows.  Data return on url_success * id: Request id (created by Bao Kim) * mrc_order_id: Order ID on merchant web/app * txn_id: Payment Transaction ID of order * total_amount: Order payment amount * stat: Order status * created_at: Time receive orders * updated_at: Payment confirmation time * checksum: Data security signature (see details below)  The checksum is signed on the parameter passed on url_success using the sha256 hash algorithm, with the security key being the secret key in your API key. How to verify the checksum on url_success please see the steps and sample code on the right tab.   # noqa: E501

    OpenAPI spec version: 5.0.0
    Contact: developer@baokim.vn
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Apiv1tokenizationtransactionOrder(object):
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
        'mrc_order_id': 'str',
        'total_amount': 'int',
        'description': 'str',
        'url_success': 'str',
        'url_detail': 'str',
        'webhooks': 'str',
        'customer_email': 'str',
        'customer_phone': 'str'
    }

    attribute_map = {
        'mrc_order_id': 'mrc_order_id',
        'total_amount': 'total_amount',
        'description': 'description',
        'url_success': 'url_success',
        'url_detail': 'url_detail',
        'webhooks': 'webhooks',
        'customer_email': 'customer_email',
        'customer_phone': 'customer_phone'
    }

    def __init__(self, mrc_order_id=None, total_amount=None, description=None, url_success=None, url_detail=None, webhooks=None, customer_email=None, customer_phone=None):  # noqa: E501
        """Apiv1tokenizationtransactionOrder - a model defined in Swagger"""  # noqa: E501
        self._mrc_order_id = None
        self._total_amount = None
        self._description = None
        self._url_success = None
        self._url_detail = None
        self._webhooks = None
        self._customer_email = None
        self._customer_phone = None
        self.discriminator = None
        if mrc_order_id is not None:
            self.mrc_order_id = mrc_order_id
        if total_amount is not None:
            self.total_amount = total_amount
        if description is not None:
            self.description = description
        if url_success is not None:
            self.url_success = url_success
        if url_detail is not None:
            self.url_detail = url_detail
        if webhooks is not None:
            self.webhooks = webhooks
        if customer_email is not None:
            self.customer_email = customer_email
        if customer_phone is not None:
            self.customer_phone = customer_phone

    @property
    def mrc_order_id(self):
        """Gets the mrc_order_id of this Apiv1tokenizationtransactionOrder.  # noqa: E501

        Merchant Order ID  # noqa: E501

        :return: The mrc_order_id of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :rtype: str
        """
        return self._mrc_order_id

    @mrc_order_id.setter
    def mrc_order_id(self, mrc_order_id):
        """Sets the mrc_order_id of this Apiv1tokenizationtransactionOrder.

        Merchant Order ID  # noqa: E501

        :param mrc_order_id: The mrc_order_id of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :type: str
        """

        self._mrc_order_id = mrc_order_id

    @property
    def total_amount(self):
        """Gets the total_amount of this Apiv1tokenizationtransactionOrder.  # noqa: E501

        Order amount (Not required if api_operation = PAY and init_token = 1)  # noqa: E501

        :return: The total_amount of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :rtype: int
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this Apiv1tokenizationtransactionOrder.

        Order amount (Not required if api_operation = PAY and init_token = 1)  # noqa: E501

        :param total_amount: The total_amount of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :type: int
        """

        self._total_amount = total_amount

    @property
    def description(self):
        """Gets the description of this Apiv1tokenizationtransactionOrder.  # noqa: E501

        Order description  # noqa: E501

        :return: The description of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Apiv1tokenizationtransactionOrder.

        Order description  # noqa: E501

        :param description: The description of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def url_success(self):
        """Gets the url_success of this Apiv1tokenizationtransactionOrder.  # noqa: E501

        URL redirect when payment success  # noqa: E501

        :return: The url_success of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :rtype: str
        """
        return self._url_success

    @url_success.setter
    def url_success(self, url_success):
        """Sets the url_success of this Apiv1tokenizationtransactionOrder.

        URL redirect when payment success  # noqa: E501

        :param url_success: The url_success of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :type: str
        """

        self._url_success = url_success

    @property
    def url_detail(self):
        """Gets the url_detail of this Apiv1tokenizationtransactionOrder.  # noqa: E501

        URL redirect when payment failed or canceled  # noqa: E501

        :return: The url_detail of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :rtype: str
        """
        return self._url_detail

    @url_detail.setter
    def url_detail(self, url_detail):
        """Sets the url_detail of this Apiv1tokenizationtransactionOrder.

        URL redirect when payment failed or canceled  # noqa: E501

        :param url_detail: The url_detail of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :type: str
        """

        self._url_detail = url_detail

    @property
    def webhooks(self):
        """Gets the webhooks of this Apiv1tokenizationtransactionOrder.  # noqa: E501

        URL is used to send notification to sales website, chat, ... when the payment order is successful, allows notify to multiple urls, separated by commas  # noqa: E501

        :return: The webhooks of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :rtype: str
        """
        return self._webhooks

    @webhooks.setter
    def webhooks(self, webhooks):
        """Sets the webhooks of this Apiv1tokenizationtransactionOrder.

        URL is used to send notification to sales website, chat, ... when the payment order is successful, allows notify to multiple urls, separated by commas  # noqa: E501

        :param webhooks: The webhooks of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :type: str
        """

        self._webhooks = webhooks

    @property
    def customer_email(self):
        """Gets the customer_email of this Apiv1tokenizationtransactionOrder.  # noqa: E501

        Customer's email  # noqa: E501

        :return: The customer_email of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :rtype: str
        """
        return self._customer_email

    @customer_email.setter
    def customer_email(self, customer_email):
        """Sets the customer_email of this Apiv1tokenizationtransactionOrder.

        Customer's email  # noqa: E501

        :param customer_email: The customer_email of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :type: str
        """

        self._customer_email = customer_email

    @property
    def customer_phone(self):
        """Gets the customer_phone of this Apiv1tokenizationtransactionOrder.  # noqa: E501

        Customer's Phone  # noqa: E501

        :return: The customer_phone of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :rtype: str
        """
        return self._customer_phone

    @customer_phone.setter
    def customer_phone(self, customer_phone):
        """Sets the customer_phone of this Apiv1tokenizationtransactionOrder.

        Customer's Phone  # noqa: E501

        :param customer_phone: The customer_phone of this Apiv1tokenizationtransactionOrder.  # noqa: E501
        :type: str
        """

        self._customer_phone = customer_phone

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
        if issubclass(Apiv1tokenizationtransactionOrder, dict):
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
        if not isinstance(other, Apiv1tokenizationtransactionOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
