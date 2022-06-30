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

class InlineResponse2006Data(object):
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
        'payment_txn_id': 'int',
        'stat': 'int',
        'user_id': 'int',
        'merchant_id': 'int',
        'order_id': 'int',
        'mrc_order_id': 'str',
        'net_amount': 'str',
        'order_amount': 'str',
        'pay_amount': 'str',
        'refund_amount': 'object',
        'fee_amount': 'str',
        'bank_percent_fee_amount': 'int',
        'fee_payer': 'str',
        'ref_no': 'object',
        'bpm_id': 'int',
        'bpm_type': 'int',
        'description': 'Description',
        'count': 'int',
        'amount': 'int',
        'minus_amount': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'id': 'int'
    }

    attribute_map = {
        'payment_txn_id': 'payment_txn_id',
        'stat': 'stat',
        'user_id': 'user_id',
        'merchant_id': 'merchant_id',
        'order_id': 'order_id',
        'mrc_order_id': 'mrc_order_id',
        'net_amount': 'net_amount',
        'order_amount': 'order_amount',
        'pay_amount': 'pay_amount',
        'refund_amount': 'refund_amount',
        'fee_amount': 'fee_amount',
        'bank_percent_fee_amount': 'bank_percent_fee_amount',
        'fee_payer': 'fee_payer',
        'ref_no': 'ref_no',
        'bpm_id': 'bpm_id',
        'bpm_type': 'bpm_type',
        'description': 'description',
        'count': 'count',
        'amount': 'amount',
        'minus_amount': 'minus_amount',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'id': 'id'
    }

    def __init__(self, payment_txn_id=None, stat=None, user_id=None, merchant_id=None, order_id=None, mrc_order_id=None, net_amount=None, order_amount=None, pay_amount=None, refund_amount=None, fee_amount=None, bank_percent_fee_amount=None, fee_payer=None, ref_no=None, bpm_id=None, bpm_type=None, description=None, count=None, amount=None, minus_amount=None, created_at=None, updated_at=None, id=None):  # noqa: E501
        """InlineResponse2006Data - a model defined in Swagger"""  # noqa: E501
        self._payment_txn_id = None
        self._stat = None
        self._user_id = None
        self._merchant_id = None
        self._order_id = None
        self._mrc_order_id = None
        self._net_amount = None
        self._order_amount = None
        self._pay_amount = None
        self._refund_amount = None
        self._fee_amount = None
        self._bank_percent_fee_amount = None
        self._fee_payer = None
        self._ref_no = None
        self._bpm_id = None
        self._bpm_type = None
        self._description = None
        self._count = None
        self._amount = None
        self._minus_amount = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self.discriminator = None
        if payment_txn_id is not None:
            self.payment_txn_id = payment_txn_id
        if stat is not None:
            self.stat = stat
        if user_id is not None:
            self.user_id = user_id
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if order_id is not None:
            self.order_id = order_id
        if mrc_order_id is not None:
            self.mrc_order_id = mrc_order_id
        if net_amount is not None:
            self.net_amount = net_amount
        if order_amount is not None:
            self.order_amount = order_amount
        if pay_amount is not None:
            self.pay_amount = pay_amount
        if refund_amount is not None:
            self.refund_amount = refund_amount
        if fee_amount is not None:
            self.fee_amount = fee_amount
        if bank_percent_fee_amount is not None:
            self.bank_percent_fee_amount = bank_percent_fee_amount
        if fee_payer is not None:
            self.fee_payer = fee_payer
        if ref_no is not None:
            self.ref_no = ref_no
        if bpm_id is not None:
            self.bpm_id = bpm_id
        if bpm_type is not None:
            self.bpm_type = bpm_type
        if description is not None:
            self.description = description
        if count is not None:
            self.count = count
        if amount is not None:
            self.amount = amount
        if minus_amount is not None:
            self.minus_amount = minus_amount
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id

    @property
    def payment_txn_id(self):
        """Gets the payment_txn_id of this InlineResponse2006Data.  # noqa: E501


        :return: The payment_txn_id of this InlineResponse2006Data.  # noqa: E501
        :rtype: int
        """
        return self._payment_txn_id

    @payment_txn_id.setter
    def payment_txn_id(self, payment_txn_id):
        """Sets the payment_txn_id of this InlineResponse2006Data.


        :param payment_txn_id: The payment_txn_id of this InlineResponse2006Data.  # noqa: E501
        :type: int
        """

        self._payment_txn_id = payment_txn_id

    @property
    def stat(self):
        """Gets the stat of this InlineResponse2006Data.  # noqa: E501


        :return: The stat of this InlineResponse2006Data.  # noqa: E501
        :rtype: int
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this InlineResponse2006Data.


        :param stat: The stat of this InlineResponse2006Data.  # noqa: E501
        :type: int
        """

        self._stat = stat

    @property
    def user_id(self):
        """Gets the user_id of this InlineResponse2006Data.  # noqa: E501


        :return: The user_id of this InlineResponse2006Data.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this InlineResponse2006Data.


        :param user_id: The user_id of this InlineResponse2006Data.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def merchant_id(self):
        """Gets the merchant_id of this InlineResponse2006Data.  # noqa: E501


        :return: The merchant_id of this InlineResponse2006Data.  # noqa: E501
        :rtype: int
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this InlineResponse2006Data.


        :param merchant_id: The merchant_id of this InlineResponse2006Data.  # noqa: E501
        :type: int
        """

        self._merchant_id = merchant_id

    @property
    def order_id(self):
        """Gets the order_id of this InlineResponse2006Data.  # noqa: E501


        :return: The order_id of this InlineResponse2006Data.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InlineResponse2006Data.


        :param order_id: The order_id of this InlineResponse2006Data.  # noqa: E501
        :type: int
        """

        self._order_id = order_id

    @property
    def mrc_order_id(self):
        """Gets the mrc_order_id of this InlineResponse2006Data.  # noqa: E501


        :return: The mrc_order_id of this InlineResponse2006Data.  # noqa: E501
        :rtype: str
        """
        return self._mrc_order_id

    @mrc_order_id.setter
    def mrc_order_id(self, mrc_order_id):
        """Sets the mrc_order_id of this InlineResponse2006Data.


        :param mrc_order_id: The mrc_order_id of this InlineResponse2006Data.  # noqa: E501
        :type: str
        """

        self._mrc_order_id = mrc_order_id

    @property
    def net_amount(self):
        """Gets the net_amount of this InlineResponse2006Data.  # noqa: E501


        :return: The net_amount of this InlineResponse2006Data.  # noqa: E501
        :rtype: str
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this InlineResponse2006Data.


        :param net_amount: The net_amount of this InlineResponse2006Data.  # noqa: E501
        :type: str
        """

        self._net_amount = net_amount

    @property
    def order_amount(self):
        """Gets the order_amount of this InlineResponse2006Data.  # noqa: E501


        :return: The order_amount of this InlineResponse2006Data.  # noqa: E501
        :rtype: str
        """
        return self._order_amount

    @order_amount.setter
    def order_amount(self, order_amount):
        """Sets the order_amount of this InlineResponse2006Data.


        :param order_amount: The order_amount of this InlineResponse2006Data.  # noqa: E501
        :type: str
        """

        self._order_amount = order_amount

    @property
    def pay_amount(self):
        """Gets the pay_amount of this InlineResponse2006Data.  # noqa: E501


        :return: The pay_amount of this InlineResponse2006Data.  # noqa: E501
        :rtype: str
        """
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, pay_amount):
        """Sets the pay_amount of this InlineResponse2006Data.


        :param pay_amount: The pay_amount of this InlineResponse2006Data.  # noqa: E501
        :type: str
        """

        self._pay_amount = pay_amount

    @property
    def refund_amount(self):
        """Gets the refund_amount of this InlineResponse2006Data.  # noqa: E501


        :return: The refund_amount of this InlineResponse2006Data.  # noqa: E501
        :rtype: object
        """
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, refund_amount):
        """Sets the refund_amount of this InlineResponse2006Data.


        :param refund_amount: The refund_amount of this InlineResponse2006Data.  # noqa: E501
        :type: object
        """

        self._refund_amount = refund_amount

    @property
    def fee_amount(self):
        """Gets the fee_amount of this InlineResponse2006Data.  # noqa: E501


        :return: The fee_amount of this InlineResponse2006Data.  # noqa: E501
        :rtype: str
        """
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """Sets the fee_amount of this InlineResponse2006Data.


        :param fee_amount: The fee_amount of this InlineResponse2006Data.  # noqa: E501
        :type: str
        """

        self._fee_amount = fee_amount

    @property
    def bank_percent_fee_amount(self):
        """Gets the bank_percent_fee_amount of this InlineResponse2006Data.  # noqa: E501


        :return: The bank_percent_fee_amount of this InlineResponse2006Data.  # noqa: E501
        :rtype: int
        """
        return self._bank_percent_fee_amount

    @bank_percent_fee_amount.setter
    def bank_percent_fee_amount(self, bank_percent_fee_amount):
        """Sets the bank_percent_fee_amount of this InlineResponse2006Data.


        :param bank_percent_fee_amount: The bank_percent_fee_amount of this InlineResponse2006Data.  # noqa: E501
        :type: int
        """

        self._bank_percent_fee_amount = bank_percent_fee_amount

    @property
    def fee_payer(self):
        """Gets the fee_payer of this InlineResponse2006Data.  # noqa: E501


        :return: The fee_payer of this InlineResponse2006Data.  # noqa: E501
        :rtype: str
        """
        return self._fee_payer

    @fee_payer.setter
    def fee_payer(self, fee_payer):
        """Sets the fee_payer of this InlineResponse2006Data.


        :param fee_payer: The fee_payer of this InlineResponse2006Data.  # noqa: E501
        :type: str
        """

        self._fee_payer = fee_payer

    @property
    def ref_no(self):
        """Gets the ref_no of this InlineResponse2006Data.  # noqa: E501


        :return: The ref_no of this InlineResponse2006Data.  # noqa: E501
        :rtype: object
        """
        return self._ref_no

    @ref_no.setter
    def ref_no(self, ref_no):
        """Sets the ref_no of this InlineResponse2006Data.


        :param ref_no: The ref_no of this InlineResponse2006Data.  # noqa: E501
        :type: object
        """

        self._ref_no = ref_no

    @property
    def bpm_id(self):
        """Gets the bpm_id of this InlineResponse2006Data.  # noqa: E501


        :return: The bpm_id of this InlineResponse2006Data.  # noqa: E501
        :rtype: int
        """
        return self._bpm_id

    @bpm_id.setter
    def bpm_id(self, bpm_id):
        """Sets the bpm_id of this InlineResponse2006Data.


        :param bpm_id: The bpm_id of this InlineResponse2006Data.  # noqa: E501
        :type: int
        """

        self._bpm_id = bpm_id

    @property
    def bpm_type(self):
        """Gets the bpm_type of this InlineResponse2006Data.  # noqa: E501


        :return: The bpm_type of this InlineResponse2006Data.  # noqa: E501
        :rtype: int
        """
        return self._bpm_type

    @bpm_type.setter
    def bpm_type(self, bpm_type):
        """Sets the bpm_type of this InlineResponse2006Data.


        :param bpm_type: The bpm_type of this InlineResponse2006Data.  # noqa: E501
        :type: int
        """

        self._bpm_type = bpm_type

    @property
    def description(self):
        """Gets the description of this InlineResponse2006Data.  # noqa: E501


        :return: The description of this InlineResponse2006Data.  # noqa: E501
        :rtype: Description
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse2006Data.


        :param description: The description of this InlineResponse2006Data.  # noqa: E501
        :type: Description
        """

        self._description = description

    @property
    def count(self):
        """Gets the count of this InlineResponse2006Data.  # noqa: E501


        :return: The count of this InlineResponse2006Data.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this InlineResponse2006Data.


        :param count: The count of this InlineResponse2006Data.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def amount(self):
        """Gets the amount of this InlineResponse2006Data.  # noqa: E501


        :return: The amount of this InlineResponse2006Data.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse2006Data.


        :param amount: The amount of this InlineResponse2006Data.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def minus_amount(self):
        """Gets the minus_amount of this InlineResponse2006Data.  # noqa: E501


        :return: The minus_amount of this InlineResponse2006Data.  # noqa: E501
        :rtype: str
        """
        return self._minus_amount

    @minus_amount.setter
    def minus_amount(self, minus_amount):
        """Sets the minus_amount of this InlineResponse2006Data.


        :param minus_amount: The minus_amount of this InlineResponse2006Data.  # noqa: E501
        :type: str
        """

        self._minus_amount = minus_amount

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse2006Data.  # noqa: E501


        :return: The created_at of this InlineResponse2006Data.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse2006Data.


        :param created_at: The created_at of this InlineResponse2006Data.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this InlineResponse2006Data.  # noqa: E501


        :return: The updated_at of this InlineResponse2006Data.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InlineResponse2006Data.


        :param updated_at: The updated_at of this InlineResponse2006Data.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this InlineResponse2006Data.  # noqa: E501


        :return: The id of this InlineResponse2006Data.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2006Data.


        :param id: The id of this InlineResponse2006Data.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(InlineResponse2006Data, dict):
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
        if not isinstance(other, InlineResponse2006Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
