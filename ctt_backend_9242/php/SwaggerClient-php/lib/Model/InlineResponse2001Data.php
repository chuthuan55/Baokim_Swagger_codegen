<?php
/**
 * InlineResponse2001Data
 *
 * PHP version 5
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * Baokim Payment Gateway API Documentation
 *
 * __Introduction:__  Bao Kim Payment gateway is an open payment platform, Bao Kim provides a full range of APIs that allow merchants to integrate between applications (web/app) with Bao Kim Payment Gateway to receive payment for your order, check your payment reconciliation.  For example, merchants can perform the following tasks with Bao Kim API. Receive payment for orders on your application (web/app) by sending orders to Bao Kim and display the payment interface for buyers to pay. Reconciliation and search for information of transaction payments, refund transactions, merchants you manage, payment status of orders to perform reconciliation.  You can find out more about Bao Kim at [Baokim.vn](https://baokim.vn).  __Security Method:__ Bao Kim API uses JSON Web Token (JWT), is a required parameter for every request to the API, follow the steps: * Use the assigned API Key and HS256 encryption algorithm to encrypt the JWT (check sample code) * JWT expire in the 60s after created * When request to API, jwt need to pass by 1 of 2 methods: Request Header jwt = Bearer $JWT / Query parameter(url param) &jwt=$JWT  __Sandbox(Test) Enviroment:__ * API key/sec: a18ff78e7a9e44f38de372e093d87ca1 / 9623ac03057e433f95d86cf4f3bef5cc * Portal URL: https://devtest.baokim.vn:9244/login * Merchant ID: 40002 * Card test ATM card:   * Bank: Saigonbank   * Card Number: 9704000000000018   * Card Holder: NGUYEN VAN A   * Effective date: 03/07   * OTP: otp * Card test Debit or credit card:   * Card Number: 5123450000000008   * Valid thru: 12/22   * CVN: 100  __Basic integration process__  This is the simplest and fastest integration process, but please learn more about the Pro integration process below with more advantages to make the right choice.  <img class=\"dia_img\" src=\"../swagger/images/BasicPaymentIntegrationDiagram.svg\" alt=\"\">  Advantages: * Simple integration, only 2 steps of processing are required to send payment request (API Send Order) and confirm payment results.  Defect: * Customers cannot view the payment methods to choose (eg bank list ...) right on the merchant's interface. Customers will choose the payment method on Bao Kim's payment interface.  __Pro integration process (advanced)__  Technically, the only difference between Pro integration and basic integration is the Web / App merchant that uses API Bank Payment Method List to load the list of payment methods and display on its interface to users. Select, then send these parameters along with the order to Bao Kim via the Send Order API  <img class=\"dia_img\" src=\"../swagger/images/PaymentProIntegrationDiagram.svg\" alt=\"\">  The main advantage of Pro integration: * Web / Merchant App can display the list of payment methods customers can use (for Bao Kim, Banks), * When the customer has chosen a payment method, the payment process will be transferred directly from the Web / Merchant App to the bank page (no Bao Kim payment page will be displayed) * Customers feel that the Web / App merchant accepts payment of most domestic banks, increases reliability, professionalism, and anticipates the payment options they have.  Defect: * Technical processing must be performed to display payment methods on the Web / Merchant App interface.  __Payment via Internet Banking (comming soon)__  Basically, payment via Internet Banking is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  However, if you want to be simpler for your customers by displaying your Internet Banking account information on your interface instead of having to redirect to Bao Kim, handle the shortening process below:  <img class=\"dia_img\" src=\"../swagger/images/InternetBankingPaymentIntegrationDiagram.svg\" alt=\"\">  __Payment by QRCode__  Payment by QRCode is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  For Pro integration, if you want to simplify for customers by displaying QRCode images on your interface instead of having to redirect to Bao Kim, please proceed with the shortened process below:  <img class=\"dia_img\" src=\"../swagger/images/QRCodePaymentIntegration.svg\" alt=\"\">  __Installment payment__  Payment by QRCode is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  Customers before payment need to take one more step to select the issuing bank and the term and installment payment (3/6/9/12 months), please refer to the process below:  <img class=\"dia_img\" src=\"../swagger/images/Quy-trinh-thanh-toan-tra-gop.svg\" alt=\"\">  __Virtual account payment__  <strong>Step 1: Create virtual account</strong> * Call to the API ‘payment/api/v4/create-virtual-account-payment’ with parameters:   * mrc_uuid: user_id of merchant (unique)   * mrc_uuid: name: user name   * mrc_uuid: mrc_id: ID Merchant on integrated website  <strong>Step 2: Receive payment results</strong> * After the User has paid, Bao Kim will record the transaction and then return the results to Merchant via webhook.  Please refer to the procedure below:  <img class=\"dia_img\" src=\"../swagger/images/quy-trinh-tao-tai-khoan-ao.svg\" alt=\"\">   __Payment via momo e-wallet__  Payment via momo e-wallet is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  <img class=\"dia_img\" src=\"../swagger/images/PayByMoMo.svg\" alt=\"\">  __Payment using module Checkout__  <strong>Step 1: Install package:</strong> * Open Terminal and run command: <strong>composer require baokim/baokim-sdk</strong> * Next, run command: <strong>composer dump-autoload</strong>  <strong>Step 2: Conduct integration</strong>  For one-time payments, create a Session with line_items. Line items represent a list of items the customer is purchasing.  Line_items takes the form of an array, refer to the sample code to the right:  $payment_method_types = [1, 2, 3];  payment_method_types is an array (1: Payment by ATM, 2: Payment by QRCode, 3: Payment By Visa).  When your customer successfully completes their payment, they are redirected to the success_url, a page on your website that informs the customer that their payment was successful.  When your customer clicks on your logo in a Checkout Session without completing a payment, Checkout redirects them back to your website by navigating to the cancel_url. Typically, this is the page on your website that the customer viewed prior to redirecting to Checkout.  <strong>Create Payment Session</strong>  Creating a Checkout Session returns $session include information of session saved in Bảo Kim, and payment_url. You need redirect browser to payment_urlto proceed with the payment  __Payment confirmation:__  After the customer makes a successful payment, Bao Kim will send a Webhook notification to the Web/App merchant, then redirect the customer browser to url_success on order with data. Web/App merchant has two ways to confirm the payment result of the order:  1. Web/App merchant receive Webhook notification Bao Kim sent by parameter \"webhooks\" on order (Recommended) 2. After the user pay, Bao Kim redirects the browser to the url_success on the order with the payment result, the Web/App merchant handles results return on url_success (this way may be affected by customer transmission failure)  In both ways, the order is considered successful payment when: * Order status \"stat\" == \"c\" * Payment transaction of order status \"stat\" == 1 * Order amount (total_amount) match with the merchant's order amount  __Webhook Notification:__  Webhook notification is a mechanism to notify Web/App merchants when an order is successfully paid through an HTTP POST request. * How to receive webhook notifications?   * When sending an order to Bao Kim through API Send Order, remember to pass the webhooks parameter as described   * When your order is successfully paid, Bao Kim will POST the payment data to the URL on the webhooks parameter in the order. * How many times will a Webhook notification be sent?   * Send up to 10 times   * Every 5 minutes   * Stop sending when receiving a json string with err_code = 0, eg {\"err_code\": \"0\", \"message\": \"some message\"}   (help Bao Kim determine that the merchant has successfully received the notification)  Description of data on webhook notification: * Method: POST * Header: Content-Type: application/json * Body (check sample code on the right side)  Steps to check and handle when receiving webhook notification: 1. Check the integrity of the received data by checking the correctness of the signature as follows (See sample PHP code on the right tab, under the webhook data description):   * Use the secret value in the key/secret pair in your API Key   * Using the hash_hmac algorithm with sha256, sign the data you receive (except for the $sign field, of course) => $yourSign   * Compare the signature you generated ($yourSign) with the signature you received ($sign), if not the same => data is not incomplete 2. Check order payment status, payment transaction, payment amount, order completion   * Check order status ($order->stat == 'c' //completed)   * Check if the order information ($order) is correct with the order information on your web/app   * If the above checks are correct, you can be sure that the order has been paid and can be completed. 3. Returns JSON string with err_code = 0, eg {\"err_code\": \"0\", \"message\": \"some message\"} so that Bao Kim knows that the merchant has received the notice and does not continue to send it back. The maximum length of the returned data is 255 characters.  Example Webhook:      {       \"order\":{         \"id\":82127,         \"user_id\":1000007,         \"mrc_order_id\":\"Nam1645759079\",         \"txn_id\":69154,         \"ref_no\":null,         \"merchant_id\":40187,         \"total_amount\":3000000,         \"description\":\"eqxI4W4HFUPwyNxH\",         \"items\":\"{           \"period\":3,           \"total_amount\":\"3090000.00\",           \"down_payment\":\"750000.00\",           \"down_payment_percent\":\"25.00\",           \"paylater_amount\":\"2250000.00\",           \"pay_per_month\":\"780000.00\",           \"user_fee\":\"90000\",           \"merchant_fee\":\"90000\"         }\",         \"url_success\":\"https://www.google.com/\",         \"url_cancel\":null,         \"url_detail\":\"https://www.google.com/\",         \"stat\":\"c\",         \"lang\":\"en\",         \"type\":1,         \"bpm_id\":\"339\",         \"accept_qrpay\":1,         \"accept_bank\":1,         \"accept_cc\":1,         \"accept_ib\":1,         \"accept_ewallet\":1,         \"accept_installments\":1,         \"email\":\"2@bk.vn\",         \"name\":\"baokimjsc111\",         \"webhooks\":\"https://google.com\",         \"customer_name\":\"Nguyen Thanh nam\",         \"customer_email\":\"testpay@gmail.com\",         \"customer_phone\":\"84328271591\",         \"customer_address\":\"102 thai thinh\",         \"created_at\":\"2022-02-25 10:18:01\",         \"updated_at\":\"2022-02-25 10:23:12\"       },       \"txn\":{         \"id\":69154,         \"reference_id\":\"bk_82127_69154_41j\",         \"user_id\":1000007,         \"merchant_id\":40187,         \"order_id\":82127,         \"mrc_order_id\":\"nam1645759079\",         \"total_amount\":750550,         \"amount\":750000,         \"fee_amount\":0,         \"bank_fee_amount\":550,         \"bank_fix_fee_amount\":550,         \"fee_payer\":1,         \"bank_fee_payer\":1,         \"auth_code\":null,         \"auth_time\":\"\",         \"ref_no\":null,         \"bpm_id\":\"97\",         \"bank_ref_no\":\"507800079\",         \"bpm_type\":1,         \"gateway\":\"\",         \"stat\":1,         \"init_token\":null,         \"description\":\"eqxi4w4hfupwynxh\",         \"customer_email\":\"testpay@gmail.com\",         \"customer_phone\":\"84328271591\",         \"completed_at\":\"2022-02-25 10:23:12\",         \"created_at\":\"2022-02-25 10:18:24\",         \"updated_at\":\"2022-02-25 10:23:12\",         \"deleted_at\":null       },       \"dataToken\":[],       \"sign\":\"ffc020303d1ed4fbe5df95d83261524793358ab0a8e363ae265e3fc2c33dc560\"     }  __Data return on url_success:__  If the merchant web/app gets notifications through Webhook Notification, you can skip processing the return data on url_success and simply show the successful payment page to the customer. Otherwise, verify the return data on url_success as follows.  Data return on url_success * id: Request id (created by Bao Kim) * mrc_order_id: Order ID on merchant web/app * txn_id: Payment Transaction ID of order * total_amount: Order payment amount * stat: Order status * created_at: Time receive orders * updated_at: Payment confirmation time * checksum: Data security signature (see details below)  The checksum is signed on the parameter passed on url_success using the sha256 hash algorithm, with the security key being the secret key in your API key. How to verify the checksum on url_success please see the steps and sample code on the right tab.
 *
 * OpenAPI spec version: 5.0.0
 * Contact: developer@baokim.vn
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 * Swagger Codegen version: 3.0.35-SNAPSHOT
 */
/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace Swagger\Client\Model;

use \ArrayAccess;
use \Swagger\Client\ObjectSerializer;

/**
 * InlineResponse2001Data Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class InlineResponse2001Data implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'inline_response_200_1_data';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'id' => 'int',
'user_id' => 'int',
'mrc_order_id' => 'string',
'txn_id' => 'int',
'ref_no' => 'string',
'total_amount' => 'string',
'description' => 'string',
'items' => '',
'url_success' => 'string',
'url_cancel' => 'object',
'url_detail' => 'string',
'stat' => 'string',
'lang' => 'string',
'bpm_id' => 'int',
'type' => 'int',
'accept_qrpay' => 'int',
'accept_bank' => 'int',
'accept_cc' => 'int',
'accept_ib' => 'int',
'accept_ewallet' => 'int',
'accept_installments' => 'int',
'order_id' => 'int',
'email' => 'string',
'name' => 'string',
'webhooks' => 'string',
'customer_name' => 'string',
'customer_email' => 'string',
'customer_phone' => 'string',
'customer_address' => 'string',
'created_at' => 'string',
'updated_at' => 'string'    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'id' => null,
'user_id' => null,
'mrc_order_id' => null,
'txn_id' => null,
'ref_no' => null,
'total_amount' => null,
'description' => null,
'items' => null,
'url_success' => null,
'url_cancel' => null,
'url_detail' => null,
'stat' => null,
'lang' => null,
'bpm_id' => null,
'type' => null,
'accept_qrpay' => null,
'accept_bank' => null,
'accept_cc' => null,
'accept_ib' => null,
'accept_ewallet' => null,
'accept_installments' => null,
'order_id' => null,
'email' => null,
'name' => null,
'webhooks' => null,
'customer_name' => null,
'customer_email' => null,
'customer_phone' => null,
'customer_address' => null,
'created_at' => null,
'updated_at' => null    ];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerTypes()
    {
        return self::$swaggerTypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerFormats()
    {
        return self::$swaggerFormats;
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'id' => 'id',
'user_id' => 'user_id',
'mrc_order_id' => 'mrc_order_id',
'txn_id' => 'txn_id',
'ref_no' => 'ref_no',
'total_amount' => 'total_amount',
'description' => 'description',
'items' => 'items',
'url_success' => 'url_success',
'url_cancel' => 'url_cancel',
'url_detail' => 'url_detail',
'stat' => 'stat',
'lang' => 'lang',
'bpm_id' => 'bpm_id',
'type' => 'type',
'accept_qrpay' => 'accept_qrpay',
'accept_bank' => 'accept_bank',
'accept_cc' => 'accept_cc',
'accept_ib' => 'accept_ib',
'accept_ewallet' => 'accept_ewallet',
'accept_installments' => 'accept_installments',
'order_id' => 'order_id',
'email' => 'email',
'name' => 'name',
'webhooks' => 'webhooks',
'customer_name' => 'customer_name',
'customer_email' => 'customer_email',
'customer_phone' => 'customer_phone',
'customer_address' => 'customer_address',
'created_at' => 'created_at',
'updated_at' => 'updated_at'    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'id' => 'setId',
'user_id' => 'setUserId',
'mrc_order_id' => 'setMrcOrderId',
'txn_id' => 'setTxnId',
'ref_no' => 'setRefNo',
'total_amount' => 'setTotalAmount',
'description' => 'setDescription',
'items' => 'setItems',
'url_success' => 'setUrlSuccess',
'url_cancel' => 'setUrlCancel',
'url_detail' => 'setUrlDetail',
'stat' => 'setStat',
'lang' => 'setLang',
'bpm_id' => 'setBpmId',
'type' => 'setType',
'accept_qrpay' => 'setAcceptQrpay',
'accept_bank' => 'setAcceptBank',
'accept_cc' => 'setAcceptCc',
'accept_ib' => 'setAcceptIb',
'accept_ewallet' => 'setAcceptEwallet',
'accept_installments' => 'setAcceptInstallments',
'order_id' => 'setOrderId',
'email' => 'setEmail',
'name' => 'setName',
'webhooks' => 'setWebhooks',
'customer_name' => 'setCustomerName',
'customer_email' => 'setCustomerEmail',
'customer_phone' => 'setCustomerPhone',
'customer_address' => 'setCustomerAddress',
'created_at' => 'setCreatedAt',
'updated_at' => 'setUpdatedAt'    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'id' => 'getId',
'user_id' => 'getUserId',
'mrc_order_id' => 'getMrcOrderId',
'txn_id' => 'getTxnId',
'ref_no' => 'getRefNo',
'total_amount' => 'getTotalAmount',
'description' => 'getDescription',
'items' => 'getItems',
'url_success' => 'getUrlSuccess',
'url_cancel' => 'getUrlCancel',
'url_detail' => 'getUrlDetail',
'stat' => 'getStat',
'lang' => 'getLang',
'bpm_id' => 'getBpmId',
'type' => 'getType',
'accept_qrpay' => 'getAcceptQrpay',
'accept_bank' => 'getAcceptBank',
'accept_cc' => 'getAcceptCc',
'accept_ib' => 'getAcceptIb',
'accept_ewallet' => 'getAcceptEwallet',
'accept_installments' => 'getAcceptInstallments',
'order_id' => 'getOrderId',
'email' => 'getEmail',
'name' => 'getName',
'webhooks' => 'getWebhooks',
'customer_name' => 'getCustomerName',
'customer_email' => 'getCustomerEmail',
'customer_phone' => 'getCustomerPhone',
'customer_address' => 'getCustomerAddress',
'created_at' => 'getCreatedAt',
'updated_at' => 'getUpdatedAt'    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$swaggerModelName;
    }

    

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['id'] = isset($data['id']) ? $data['id'] : null;
        $this->container['user_id'] = isset($data['user_id']) ? $data['user_id'] : null;
        $this->container['mrc_order_id'] = isset($data['mrc_order_id']) ? $data['mrc_order_id'] : null;
        $this->container['txn_id'] = isset($data['txn_id']) ? $data['txn_id'] : null;
        $this->container['ref_no'] = isset($data['ref_no']) ? $data['ref_no'] : null;
        $this->container['total_amount'] = isset($data['total_amount']) ? $data['total_amount'] : null;
        $this->container['description'] = isset($data['description']) ? $data['description'] : null;
        $this->container['items'] = isset($data['items']) ? $data['items'] : null;
        $this->container['url_success'] = isset($data['url_success']) ? $data['url_success'] : null;
        $this->container['url_cancel'] = isset($data['url_cancel']) ? $data['url_cancel'] : null;
        $this->container['url_detail'] = isset($data['url_detail']) ? $data['url_detail'] : null;
        $this->container['stat'] = isset($data['stat']) ? $data['stat'] : null;
        $this->container['lang'] = isset($data['lang']) ? $data['lang'] : null;
        $this->container['bpm_id'] = isset($data['bpm_id']) ? $data['bpm_id'] : null;
        $this->container['type'] = isset($data['type']) ? $data['type'] : null;
        $this->container['accept_qrpay'] = isset($data['accept_qrpay']) ? $data['accept_qrpay'] : null;
        $this->container['accept_bank'] = isset($data['accept_bank']) ? $data['accept_bank'] : null;
        $this->container['accept_cc'] = isset($data['accept_cc']) ? $data['accept_cc'] : null;
        $this->container['accept_ib'] = isset($data['accept_ib']) ? $data['accept_ib'] : null;
        $this->container['accept_ewallet'] = isset($data['accept_ewallet']) ? $data['accept_ewallet'] : null;
        $this->container['accept_installments'] = isset($data['accept_installments']) ? $data['accept_installments'] : null;
        $this->container['order_id'] = isset($data['order_id']) ? $data['order_id'] : null;
        $this->container['email'] = isset($data['email']) ? $data['email'] : null;
        $this->container['name'] = isset($data['name']) ? $data['name'] : null;
        $this->container['webhooks'] = isset($data['webhooks']) ? $data['webhooks'] : null;
        $this->container['customer_name'] = isset($data['customer_name']) ? $data['customer_name'] : null;
        $this->container['customer_email'] = isset($data['customer_email']) ? $data['customer_email'] : null;
        $this->container['customer_phone'] = isset($data['customer_phone']) ? $data['customer_phone'] : null;
        $this->container['customer_address'] = isset($data['customer_address']) ? $data['customer_address'] : null;
        $this->container['created_at'] = isset($data['created_at']) ? $data['created_at'] : null;
        $this->container['updated_at'] = isset($data['updated_at']) ? $data['updated_at'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets id
     *
     * @return int
     */
    public function getId()
    {
        return $this->container['id'];
    }

    /**
     * Sets id
     *
     * @param int $id id
     *
     * @return $this
     */
    public function setId($id)
    {
        $this->container['id'] = $id;

        return $this;
    }

    /**
     * Gets user_id
     *
     * @return int
     */
    public function getUserId()
    {
        return $this->container['user_id'];
    }

    /**
     * Sets user_id
     *
     * @param int $user_id user_id
     *
     * @return $this
     */
    public function setUserId($user_id)
    {
        $this->container['user_id'] = $user_id;

        return $this;
    }

    /**
     * Gets mrc_order_id
     *
     * @return string
     */
    public function getMrcOrderId()
    {
        return $this->container['mrc_order_id'];
    }

    /**
     * Sets mrc_order_id
     *
     * @param string $mrc_order_id mrc_order_id
     *
     * @return $this
     */
    public function setMrcOrderId($mrc_order_id)
    {
        $this->container['mrc_order_id'] = $mrc_order_id;

        return $this;
    }

    /**
     * Gets txn_id
     *
     * @return int
     */
    public function getTxnId()
    {
        return $this->container['txn_id'];
    }

    /**
     * Sets txn_id
     *
     * @param int $txn_id txn_id
     *
     * @return $this
     */
    public function setTxnId($txn_id)
    {
        $this->container['txn_id'] = $txn_id;

        return $this;
    }

    /**
     * Gets ref_no
     *
     * @return string
     */
    public function getRefNo()
    {
        return $this->container['ref_no'];
    }

    /**
     * Sets ref_no
     *
     * @param string $ref_no ref_no
     *
     * @return $this
     */
    public function setRefNo($ref_no)
    {
        $this->container['ref_no'] = $ref_no;

        return $this;
    }

    /**
     * Gets total_amount
     *
     * @return string
     */
    public function getTotalAmount()
    {
        return $this->container['total_amount'];
    }

    /**
     * Sets total_amount
     *
     * @param string $total_amount total_amount
     *
     * @return $this
     */
    public function setTotalAmount($total_amount)
    {
        $this->container['total_amount'] = $total_amount;

        return $this;
    }

    /**
     * Gets description
     *
     * @return string
     */
    public function getDescription()
    {
        return $this->container['description'];
    }

    /**
     * Sets description
     *
     * @param string $description description
     *
     * @return $this
     */
    public function setDescription($description)
    {
        $this->container['description'] = $description;

        return $this;
    }

    /**
     * Gets items
     *
     * @return 
     */
    public function getItems()
    {
        return $this->container['items'];
    }

    /**
     * Sets items
     *
     * @param  $items items
     *
     * @return $this
     */
    public function setItems($items)
    {
        $this->container['items'] = $items;

        return $this;
    }

    /**
     * Gets url_success
     *
     * @return string
     */
    public function getUrlSuccess()
    {
        return $this->container['url_success'];
    }

    /**
     * Sets url_success
     *
     * @param string $url_success url_success
     *
     * @return $this
     */
    public function setUrlSuccess($url_success)
    {
        $this->container['url_success'] = $url_success;

        return $this;
    }

    /**
     * Gets url_cancel
     *
     * @return object
     */
    public function getUrlCancel()
    {
        return $this->container['url_cancel'];
    }

    /**
     * Sets url_cancel
     *
     * @param object $url_cancel url_cancel
     *
     * @return $this
     */
    public function setUrlCancel($url_cancel)
    {
        $this->container['url_cancel'] = $url_cancel;

        return $this;
    }

    /**
     * Gets url_detail
     *
     * @return string
     */
    public function getUrlDetail()
    {
        return $this->container['url_detail'];
    }

    /**
     * Sets url_detail
     *
     * @param string $url_detail url_detail
     *
     * @return $this
     */
    public function setUrlDetail($url_detail)
    {
        $this->container['url_detail'] = $url_detail;

        return $this;
    }

    /**
     * Gets stat
     *
     * @return string
     */
    public function getStat()
    {
        return $this->container['stat'];
    }

    /**
     * Sets stat
     *
     * @param string $stat stat
     *
     * @return $this
     */
    public function setStat($stat)
    {
        $this->container['stat'] = $stat;

        return $this;
    }

    /**
     * Gets lang
     *
     * @return string
     */
    public function getLang()
    {
        return $this->container['lang'];
    }

    /**
     * Sets lang
     *
     * @param string $lang lang
     *
     * @return $this
     */
    public function setLang($lang)
    {
        $this->container['lang'] = $lang;

        return $this;
    }

    /**
     * Gets bpm_id
     *
     * @return int
     */
    public function getBpmId()
    {
        return $this->container['bpm_id'];
    }

    /**
     * Sets bpm_id
     *
     * @param int $bpm_id bpm_id
     *
     * @return $this
     */
    public function setBpmId($bpm_id)
    {
        $this->container['bpm_id'] = $bpm_id;

        return $this;
    }

    /**
     * Gets type
     *
     * @return int
     */
    public function getType()
    {
        return $this->container['type'];
    }

    /**
     * Sets type
     *
     * @param int $type type
     *
     * @return $this
     */
    public function setType($type)
    {
        $this->container['type'] = $type;

        return $this;
    }

    /**
     * Gets accept_qrpay
     *
     * @return int
     */
    public function getAcceptQrpay()
    {
        return $this->container['accept_qrpay'];
    }

    /**
     * Sets accept_qrpay
     *
     * @param int $accept_qrpay accept_qrpay
     *
     * @return $this
     */
    public function setAcceptQrpay($accept_qrpay)
    {
        $this->container['accept_qrpay'] = $accept_qrpay;

        return $this;
    }

    /**
     * Gets accept_bank
     *
     * @return int
     */
    public function getAcceptBank()
    {
        return $this->container['accept_bank'];
    }

    /**
     * Sets accept_bank
     *
     * @param int $accept_bank accept_bank
     *
     * @return $this
     */
    public function setAcceptBank($accept_bank)
    {
        $this->container['accept_bank'] = $accept_bank;

        return $this;
    }

    /**
     * Gets accept_cc
     *
     * @return int
     */
    public function getAcceptCc()
    {
        return $this->container['accept_cc'];
    }

    /**
     * Sets accept_cc
     *
     * @param int $accept_cc accept_cc
     *
     * @return $this
     */
    public function setAcceptCc($accept_cc)
    {
        $this->container['accept_cc'] = $accept_cc;

        return $this;
    }

    /**
     * Gets accept_ib
     *
     * @return int
     */
    public function getAcceptIb()
    {
        return $this->container['accept_ib'];
    }

    /**
     * Sets accept_ib
     *
     * @param int $accept_ib accept_ib
     *
     * @return $this
     */
    public function setAcceptIb($accept_ib)
    {
        $this->container['accept_ib'] = $accept_ib;

        return $this;
    }

    /**
     * Gets accept_ewallet
     *
     * @return int
     */
    public function getAcceptEwallet()
    {
        return $this->container['accept_ewallet'];
    }

    /**
     * Sets accept_ewallet
     *
     * @param int $accept_ewallet accept_ewallet
     *
     * @return $this
     */
    public function setAcceptEwallet($accept_ewallet)
    {
        $this->container['accept_ewallet'] = $accept_ewallet;

        return $this;
    }

    /**
     * Gets accept_installments
     *
     * @return int
     */
    public function getAcceptInstallments()
    {
        return $this->container['accept_installments'];
    }

    /**
     * Sets accept_installments
     *
     * @param int $accept_installments accept_installments
     *
     * @return $this
     */
    public function setAcceptInstallments($accept_installments)
    {
        $this->container['accept_installments'] = $accept_installments;

        return $this;
    }

    /**
     * Gets order_id
     *
     * @return int
     */
    public function getOrderId()
    {
        return $this->container['order_id'];
    }

    /**
     * Sets order_id
     *
     * @param int $order_id order_id
     *
     * @return $this
     */
    public function setOrderId($order_id)
    {
        $this->container['order_id'] = $order_id;

        return $this;
    }

    /**
     * Gets email
     *
     * @return string
     */
    public function getEmail()
    {
        return $this->container['email'];
    }

    /**
     * Sets email
     *
     * @param string $email email
     *
     * @return $this
     */
    public function setEmail($email)
    {
        $this->container['email'] = $email;

        return $this;
    }

    /**
     * Gets name
     *
     * @return string
     */
    public function getName()
    {
        return $this->container['name'];
    }

    /**
     * Sets name
     *
     * @param string $name name
     *
     * @return $this
     */
    public function setName($name)
    {
        $this->container['name'] = $name;

        return $this;
    }

    /**
     * Gets webhooks
     *
     * @return string
     */
    public function getWebhooks()
    {
        return $this->container['webhooks'];
    }

    /**
     * Sets webhooks
     *
     * @param string $webhooks webhooks
     *
     * @return $this
     */
    public function setWebhooks($webhooks)
    {
        $this->container['webhooks'] = $webhooks;

        return $this;
    }

    /**
     * Gets customer_name
     *
     * @return string
     */
    public function getCustomerName()
    {
        return $this->container['customer_name'];
    }

    /**
     * Sets customer_name
     *
     * @param string $customer_name customer_name
     *
     * @return $this
     */
    public function setCustomerName($customer_name)
    {
        $this->container['customer_name'] = $customer_name;

        return $this;
    }

    /**
     * Gets customer_email
     *
     * @return string
     */
    public function getCustomerEmail()
    {
        return $this->container['customer_email'];
    }

    /**
     * Sets customer_email
     *
     * @param string $customer_email customer_email
     *
     * @return $this
     */
    public function setCustomerEmail($customer_email)
    {
        $this->container['customer_email'] = $customer_email;

        return $this;
    }

    /**
     * Gets customer_phone
     *
     * @return string
     */
    public function getCustomerPhone()
    {
        return $this->container['customer_phone'];
    }

    /**
     * Sets customer_phone
     *
     * @param string $customer_phone customer_phone
     *
     * @return $this
     */
    public function setCustomerPhone($customer_phone)
    {
        $this->container['customer_phone'] = $customer_phone;

        return $this;
    }

    /**
     * Gets customer_address
     *
     * @return string
     */
    public function getCustomerAddress()
    {
        return $this->container['customer_address'];
    }

    /**
     * Sets customer_address
     *
     * @param string $customer_address customer_address
     *
     * @return $this
     */
    public function setCustomerAddress($customer_address)
    {
        $this->container['customer_address'] = $customer_address;

        return $this;
    }

    /**
     * Gets created_at
     *
     * @return string
     */
    public function getCreatedAt()
    {
        return $this->container['created_at'];
    }

    /**
     * Sets created_at
     *
     * @param string $created_at created_at
     *
     * @return $this
     */
    public function setCreatedAt($created_at)
    {
        $this->container['created_at'] = $created_at;

        return $this;
    }

    /**
     * Gets updated_at
     *
     * @return string
     */
    public function getUpdatedAt()
    {
        return $this->container['updated_at'];
    }

    /**
     * Sets updated_at
     *
     * @param string $updated_at updated_at
     *
     * @return $this
     */
    public function setUpdatedAt($updated_at)
    {
        $this->container['updated_at'] = $updated_at;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     *
     * @param integer $offset Offset
     * @param mixed   $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        if (defined('JSON_PRETTY_PRINT')) { // use JSON pretty print
            return json_encode(
                ObjectSerializer::sanitizeForSerialization($this),
                JSON_PRETTY_PRINT
            );
        }

        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}
