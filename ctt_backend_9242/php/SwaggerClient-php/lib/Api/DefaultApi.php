<?php
/**
 * DefaultApi
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

namespace Swagger\Client\Api;

use GuzzleHttp\Client;
use GuzzleHttp\ClientInterface;
use GuzzleHttp\Exception\RequestException;
use GuzzleHttp\Psr7\MultipartStream;
use GuzzleHttp\Psr7\Request;
use GuzzleHttp\RequestOptions;
use Swagger\Client\ApiException;
use Swagger\Client\Configuration;
use Swagger\Client\HeaderSelector;
use Swagger\Client\ObjectSerializer;

/**
 * DefaultApi Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class DefaultApi
{
    /**
     * @var ClientInterface
     */
    protected $client;

    /**
     * @var Configuration
     */
    protected $config;

    /**
     * @var HeaderSelector
     */
    protected $headerSelector;

    /**
     * @param ClientInterface $client
     * @param Configuration   $config
     * @param HeaderSelector  $selector
     */
    public function __construct(
        ClientInterface $client = null,
        Configuration $config = null,
        HeaderSelector $selector = null
    ) {
        $this->client = $client ?: new Client();
        $this->config = $config ?: new Configuration();
        $this->headerSelector = $selector ?: new HeaderSelector();
    }

    /**
     * @return Configuration
     */
    public function getConfig()
    {
        return $this->config;
    }

    /**
     * Operation bpmList
     *
     * Bank Payment Method List
     *
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return \Swagger\Client\Model\InlineResponse2003
     */
    public function bpmList()
    {
        list($response) = $this->bpmListWithHttpInfo();
        return $response;
    }

    /**
     * Operation bpmListWithHttpInfo
     *
     * Bank Payment Method List
     *
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return array of \Swagger\Client\Model\InlineResponse2003, HTTP status code, HTTP response headers (array of strings)
     */
    public function bpmListWithHttpInfo()
    {
        $returnType = '\Swagger\Client\Model\InlineResponse2003';
        $request = $this->bpmListRequest();

        try {
            $options = $this->createHttpClientOption();
            try {
                $response = $this->client->send($request, $options);
            } catch (RequestException $e) {
                throw new ApiException(
                    "[{$e->getCode()}] {$e->getMessage()}",
                    $e->getCode(),
                    $e->getResponse() ? $e->getResponse()->getHeaders() : null,
                    $e->getResponse() ? $e->getResponse()->getBody()->getContents() : null
                );
            }

            $statusCode = $response->getStatusCode();

            if ($statusCode < 200 || $statusCode > 299) {
                throw new ApiException(
                    sprintf(
                        '[%d] Error connecting to the API (%s)',
                        $statusCode,
                        $request->getUri()
                    ),
                    $statusCode,
                    $response->getHeaders(),
                    $response->getBody()
                );
            }

            $responseBody = $response->getBody();
            if ($returnType === '\SplFileObject') {
                $content = $responseBody; //stream goes to serializer
            } else {
                $content = $responseBody->getContents();
                if (!in_array($returnType, ['string','integer','bool'])) {
                    $content = json_decode($content);
                }
            }

            return [
                ObjectSerializer::deserialize($content, $returnType, []),
                $response->getStatusCode(),
                $response->getHeaders()
            ];

        } catch (ApiException $e) {
            switch ($e->getCode()) {
                case 200:
                    $data = ObjectSerializer::deserialize(
                        $e->getResponseBody(),
                        '\Swagger\Client\Model\InlineResponse2003',
                        $e->getResponseHeaders()
                    );
                    $e->setResponseObject($data);
                    break;
            }
            throw $e;
        }
    }

    /**
     * Operation bpmListAsync
     *
     * Bank Payment Method List
     *
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function bpmListAsync()
    {
        return $this->bpmListAsyncWithHttpInfo()
            ->then(
                function ($response) {
                    return $response[0];
                }
            );
    }

    /**
     * Operation bpmListAsyncWithHttpInfo
     *
     * Bank Payment Method List
     *
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function bpmListAsyncWithHttpInfo()
    {
        $returnType = '\Swagger\Client\Model\InlineResponse2003';
        $request = $this->bpmListRequest();

        return $this->client
            ->sendAsync($request, $this->createHttpClientOption())
            ->then(
                function ($response) use ($returnType) {
                    $responseBody = $response->getBody();
                    if ($returnType === '\SplFileObject') {
                        $content = $responseBody; //stream goes to serializer
                    } else {
                        $content = $responseBody->getContents();
                        if ($returnType !== 'string') {
                            $content = json_decode($content);
                        }
                    }

                    return [
                        ObjectSerializer::deserialize($content, $returnType, []),
                        $response->getStatusCode(),
                        $response->getHeaders()
                    ];
                },
                function ($exception) {
                    $response = $exception->getResponse();
                    $statusCode = $response->getStatusCode();
                    throw new ApiException(
                        sprintf(
                            '[%d] Error connecting to the API (%s)',
                            $statusCode,
                            $exception->getRequest()->getUri()
                        ),
                        $statusCode,
                        $response->getHeaders(),
                        $response->getBody()
                    );
                }
            );
    }

    /**
     * Create request for operation 'bpmList'
     *
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Psr7\Request
     */
    protected function bpmListRequest()
    {

        $resourcePath = 'api/v5/bpm/list';
        $formParams = [];
        $queryParams = [];
        $headerParams = [];
        $httpBody = '';
        $multipart = false;



        // body params
        $_tempBody = null;

        if ($multipart) {
            $headers = $this->headerSelector->selectHeadersForMultipart(
                ['application/json']
            );
        } else {
            $headers = $this->headerSelector->selectHeaders(
                ['application/json'],
                []
            );
        }

        // for model (json/xml)
        if (isset($_tempBody)) {
            // $_tempBody is the method argument, if present
            $httpBody = $_tempBody;
            // \stdClass has no __toString(), so we should encode it manually
            if ($httpBody instanceof \stdClass && $headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($httpBody);
            }
        } elseif (count($formParams) > 0) {
            if ($multipart) {
                $multipartContents = [];
                foreach ($formParams as $formParamName => $formParamValue) {
                    $multipartContents[] = [
                        'name' => $formParamName,
                        'contents' => $formParamValue
                    ];
                }
                // for HTTP post (form)
                $httpBody = new MultipartStream($multipartContents);

            } elseif ($headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($formParams);

            } else {
                // for HTTP post (form)
                $httpBody = \GuzzleHttp\Psr7\build_query($formParams);
            }
        }

        // this endpoint requires API key authentication
        $apiKey = $this->config->getApiKeyWithPrefix('jwt');
        if ($apiKey !== null) {
            $headers['jwt'] = $apiKey;
        }

        $defaultHeaders = [];
        if ($this->config->getUserAgent()) {
            $defaultHeaders['User-Agent'] = $this->config->getUserAgent();
        }

        $headers = array_merge(
            $defaultHeaders,
            $headerParams,
            $headers
        );

        $query = \GuzzleHttp\Psr7\build_query($queryParams);
        return new Request(
            'GET',
            $this->config->getHost() . $resourcePath . ($query ? "?{$query}" : ''),
            $headers,
            $httpBody
        );
    }

    /**
     * Operation ordersCancel
     *
     * Order Cancel
     *
     * @param  \Swagger\Client\Model\OrderCancelBody $body body (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return \Swagger\Client\Model\InlineResponse2002
     */
    public function ordersCancel($body = null)
    {
        list($response) = $this->ordersCancelWithHttpInfo($body);
        return $response;
    }

    /**
     * Operation ordersCancelWithHttpInfo
     *
     * Order Cancel
     *
     * @param  \Swagger\Client\Model\OrderCancelBody $body (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return array of \Swagger\Client\Model\InlineResponse2002, HTTP status code, HTTP response headers (array of strings)
     */
    public function ordersCancelWithHttpInfo($body = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse2002';
        $request = $this->ordersCancelRequest($body);

        try {
            $options = $this->createHttpClientOption();
            try {
                $response = $this->client->send($request, $options);
            } catch (RequestException $e) {
                throw new ApiException(
                    "[{$e->getCode()}] {$e->getMessage()}",
                    $e->getCode(),
                    $e->getResponse() ? $e->getResponse()->getHeaders() : null,
                    $e->getResponse() ? $e->getResponse()->getBody()->getContents() : null
                );
            }

            $statusCode = $response->getStatusCode();

            if ($statusCode < 200 || $statusCode > 299) {
                throw new ApiException(
                    sprintf(
                        '[%d] Error connecting to the API (%s)',
                        $statusCode,
                        $request->getUri()
                    ),
                    $statusCode,
                    $response->getHeaders(),
                    $response->getBody()
                );
            }

            $responseBody = $response->getBody();
            if ($returnType === '\SplFileObject') {
                $content = $responseBody; //stream goes to serializer
            } else {
                $content = $responseBody->getContents();
                if (!in_array($returnType, ['string','integer','bool'])) {
                    $content = json_decode($content);
                }
            }

            return [
                ObjectSerializer::deserialize($content, $returnType, []),
                $response->getStatusCode(),
                $response->getHeaders()
            ];

        } catch (ApiException $e) {
            switch ($e->getCode()) {
                case 200:
                    $data = ObjectSerializer::deserialize(
                        $e->getResponseBody(),
                        '\Swagger\Client\Model\InlineResponse2002',
                        $e->getResponseHeaders()
                    );
                    $e->setResponseObject($data);
                    break;
            }
            throw $e;
        }
    }

    /**
     * Operation ordersCancelAsync
     *
     * Order Cancel
     *
     * @param  \Swagger\Client\Model\OrderCancelBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function ordersCancelAsync($body = null)
    {
        return $this->ordersCancelAsyncWithHttpInfo($body)
            ->then(
                function ($response) {
                    return $response[0];
                }
            );
    }

    /**
     * Operation ordersCancelAsyncWithHttpInfo
     *
     * Order Cancel
     *
     * @param  \Swagger\Client\Model\OrderCancelBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function ordersCancelAsyncWithHttpInfo($body = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse2002';
        $request = $this->ordersCancelRequest($body);

        return $this->client
            ->sendAsync($request, $this->createHttpClientOption())
            ->then(
                function ($response) use ($returnType) {
                    $responseBody = $response->getBody();
                    if ($returnType === '\SplFileObject') {
                        $content = $responseBody; //stream goes to serializer
                    } else {
                        $content = $responseBody->getContents();
                        if ($returnType !== 'string') {
                            $content = json_decode($content);
                        }
                    }

                    return [
                        ObjectSerializer::deserialize($content, $returnType, []),
                        $response->getStatusCode(),
                        $response->getHeaders()
                    ];
                },
                function ($exception) {
                    $response = $exception->getResponse();
                    $statusCode = $response->getStatusCode();
                    throw new ApiException(
                        sprintf(
                            '[%d] Error connecting to the API (%s)',
                            $statusCode,
                            $exception->getRequest()->getUri()
                        ),
                        $statusCode,
                        $response->getHeaders(),
                        $response->getBody()
                    );
                }
            );
    }

    /**
     * Create request for operation 'ordersCancel'
     *
     * @param  \Swagger\Client\Model\OrderCancelBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Psr7\Request
     */
    protected function ordersCancelRequest($body = null)
    {

        $resourcePath = '/api/v5/order/cancel';
        $formParams = [];
        $queryParams = [];
        $headerParams = [];
        $httpBody = '';
        $multipart = false;



        // body params
        $_tempBody = null;
        if (isset($body)) {
            $_tempBody = $body;
        }

        if ($multipart) {
            $headers = $this->headerSelector->selectHeadersForMultipart(
                ['application/json']
            );
        } else {
            $headers = $this->headerSelector->selectHeaders(
                ['application/json'],
                ['application/json']
            );
        }

        // for model (json/xml)
        if (isset($_tempBody)) {
            // $_tempBody is the method argument, if present
            $httpBody = $_tempBody;
            // \stdClass has no __toString(), so we should encode it manually
            if ($httpBody instanceof \stdClass && $headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($httpBody);
            }
        } elseif (count($formParams) > 0) {
            if ($multipart) {
                $multipartContents = [];
                foreach ($formParams as $formParamName => $formParamValue) {
                    $multipartContents[] = [
                        'name' => $formParamName,
                        'contents' => $formParamValue
                    ];
                }
                // for HTTP post (form)
                $httpBody = new MultipartStream($multipartContents);

            } elseif ($headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($formParams);

            } else {
                // for HTTP post (form)
                $httpBody = \GuzzleHttp\Psr7\build_query($formParams);
            }
        }

        // this endpoint requires API key authentication
        $apiKey = $this->config->getApiKeyWithPrefix('jwt');
        if ($apiKey !== null) {
            $headers['jwt'] = $apiKey;
        }

        $defaultHeaders = [];
        if ($this->config->getUserAgent()) {
            $defaultHeaders['User-Agent'] = $this->config->getUserAgent();
        }

        $headers = array_merge(
            $defaultHeaders,
            $headerParams,
            $headers
        );

        $query = \GuzzleHttp\Psr7\build_query($queryParams);
        return new Request(
            'POST',
            $this->config->getHost() . $resourcePath . ($query ? "?{$query}" : ''),
            $headers,
            $httpBody
        );
    }

    /**
     * Operation ordersDetail
     *
     * Order Detail
     *
     * @param  int $id Order ID [semi-optional] (optional)
     * @param  string $mrc_order_id Merchant Order ID [semi-optional] (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return \Swagger\Client\Model\InlineResponse2001
     */
    public function ordersDetail($id = null, $mrc_order_id = null)
    {
        list($response) = $this->ordersDetailWithHttpInfo($id, $mrc_order_id);
        return $response;
    }

    /**
     * Operation ordersDetailWithHttpInfo
     *
     * Order Detail
     *
     * @param  int $id Order ID [semi-optional] (optional)
     * @param  string $mrc_order_id Merchant Order ID [semi-optional] (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return array of \Swagger\Client\Model\InlineResponse2001, HTTP status code, HTTP response headers (array of strings)
     */
    public function ordersDetailWithHttpInfo($id = null, $mrc_order_id = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse2001';
        $request = $this->ordersDetailRequest($id, $mrc_order_id);

        try {
            $options = $this->createHttpClientOption();
            try {
                $response = $this->client->send($request, $options);
            } catch (RequestException $e) {
                throw new ApiException(
                    "[{$e->getCode()}] {$e->getMessage()}",
                    $e->getCode(),
                    $e->getResponse() ? $e->getResponse()->getHeaders() : null,
                    $e->getResponse() ? $e->getResponse()->getBody()->getContents() : null
                );
            }

            $statusCode = $response->getStatusCode();

            if ($statusCode < 200 || $statusCode > 299) {
                throw new ApiException(
                    sprintf(
                        '[%d] Error connecting to the API (%s)',
                        $statusCode,
                        $request->getUri()
                    ),
                    $statusCode,
                    $response->getHeaders(),
                    $response->getBody()
                );
            }

            $responseBody = $response->getBody();
            if ($returnType === '\SplFileObject') {
                $content = $responseBody; //stream goes to serializer
            } else {
                $content = $responseBody->getContents();
                if (!in_array($returnType, ['string','integer','bool'])) {
                    $content = json_decode($content);
                }
            }

            return [
                ObjectSerializer::deserialize($content, $returnType, []),
                $response->getStatusCode(),
                $response->getHeaders()
            ];

        } catch (ApiException $e) {
            switch ($e->getCode()) {
                case 200:
                    $data = ObjectSerializer::deserialize(
                        $e->getResponseBody(),
                        '\Swagger\Client\Model\InlineResponse2001',
                        $e->getResponseHeaders()
                    );
                    $e->setResponseObject($data);
                    break;
            }
            throw $e;
        }
    }

    /**
     * Operation ordersDetailAsync
     *
     * Order Detail
     *
     * @param  int $id Order ID [semi-optional] (optional)
     * @param  string $mrc_order_id Merchant Order ID [semi-optional] (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function ordersDetailAsync($id = null, $mrc_order_id = null)
    {
        return $this->ordersDetailAsyncWithHttpInfo($id, $mrc_order_id)
            ->then(
                function ($response) {
                    return $response[0];
                }
            );
    }

    /**
     * Operation ordersDetailAsyncWithHttpInfo
     *
     * Order Detail
     *
     * @param  int $id Order ID [semi-optional] (optional)
     * @param  string $mrc_order_id Merchant Order ID [semi-optional] (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function ordersDetailAsyncWithHttpInfo($id = null, $mrc_order_id = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse2001';
        $request = $this->ordersDetailRequest($id, $mrc_order_id);

        return $this->client
            ->sendAsync($request, $this->createHttpClientOption())
            ->then(
                function ($response) use ($returnType) {
                    $responseBody = $response->getBody();
                    if ($returnType === '\SplFileObject') {
                        $content = $responseBody; //stream goes to serializer
                    } else {
                        $content = $responseBody->getContents();
                        if ($returnType !== 'string') {
                            $content = json_decode($content);
                        }
                    }

                    return [
                        ObjectSerializer::deserialize($content, $returnType, []),
                        $response->getStatusCode(),
                        $response->getHeaders()
                    ];
                },
                function ($exception) {
                    $response = $exception->getResponse();
                    $statusCode = $response->getStatusCode();
                    throw new ApiException(
                        sprintf(
                            '[%d] Error connecting to the API (%s)',
                            $statusCode,
                            $exception->getRequest()->getUri()
                        ),
                        $statusCode,
                        $response->getHeaders(),
                        $response->getBody()
                    );
                }
            );
    }

    /**
     * Create request for operation 'ordersDetail'
     *
     * @param  int $id Order ID [semi-optional] (optional)
     * @param  string $mrc_order_id Merchant Order ID [semi-optional] (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Psr7\Request
     */
    protected function ordersDetailRequest($id = null, $mrc_order_id = null)
    {

        $resourcePath = '/api/v5/order/detail';
        $formParams = [];
        $queryParams = [];
        $headerParams = [];
        $httpBody = '';
        $multipart = false;

        // query params
        if ($id !== null) {
            $queryParams['id'] = ObjectSerializer::toQueryValue($id, null);
        }
        // query params
        if ($mrc_order_id !== null) {
            $queryParams['mrc_order_id'] = ObjectSerializer::toQueryValue($mrc_order_id, null);
        }


        // body params
        $_tempBody = null;

        if ($multipart) {
            $headers = $this->headerSelector->selectHeadersForMultipart(
                ['application/json']
            );
        } else {
            $headers = $this->headerSelector->selectHeaders(
                ['application/json'],
                []
            );
        }

        // for model (json/xml)
        if (isset($_tempBody)) {
            // $_tempBody is the method argument, if present
            $httpBody = $_tempBody;
            // \stdClass has no __toString(), so we should encode it manually
            if ($httpBody instanceof \stdClass && $headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($httpBody);
            }
        } elseif (count($formParams) > 0) {
            if ($multipart) {
                $multipartContents = [];
                foreach ($formParams as $formParamName => $formParamValue) {
                    $multipartContents[] = [
                        'name' => $formParamName,
                        'contents' => $formParamValue
                    ];
                }
                // for HTTP post (form)
                $httpBody = new MultipartStream($multipartContents);

            } elseif ($headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($formParams);

            } else {
                // for HTTP post (form)
                $httpBody = \GuzzleHttp\Psr7\build_query($formParams);
            }
        }

        // this endpoint requires API key authentication
        $apiKey = $this->config->getApiKeyWithPrefix('jwt');
        if ($apiKey !== null) {
            $headers['jwt'] = $apiKey;
        }

        $defaultHeaders = [];
        if ($this->config->getUserAgent()) {
            $defaultHeaders['User-Agent'] = $this->config->getUserAgent();
        }

        $headers = array_merge(
            $defaultHeaders,
            $headerParams,
            $headers
        );

        $query = \GuzzleHttp\Psr7\build_query($queryParams);
        return new Request(
            'GET',
            $this->config->getHost() . $resourcePath . ($query ? "?{$query}" : ''),
            $headers,
            $httpBody
        );
    }

    /**
     * Operation ordersSend
     *
     * Send Order
     *
     * @param  \Swagger\Client\Model\OrderSendBody $body body (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return \Swagger\Client\Model\InlineResponse200
     */
    public function ordersSend($body = null)
    {
        list($response) = $this->ordersSendWithHttpInfo($body);
        return $response;
    }

    /**
     * Operation ordersSendWithHttpInfo
     *
     * Send Order
     *
     * @param  \Swagger\Client\Model\OrderSendBody $body (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return array of \Swagger\Client\Model\InlineResponse200, HTTP status code, HTTP response headers (array of strings)
     */
    public function ordersSendWithHttpInfo($body = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse200';
        $request = $this->ordersSendRequest($body);

        try {
            $options = $this->createHttpClientOption();
            try {
                $response = $this->client->send($request, $options);
            } catch (RequestException $e) {
                throw new ApiException(
                    "[{$e->getCode()}] {$e->getMessage()}",
                    $e->getCode(),
                    $e->getResponse() ? $e->getResponse()->getHeaders() : null,
                    $e->getResponse() ? $e->getResponse()->getBody()->getContents() : null
                );
            }

            $statusCode = $response->getStatusCode();

            if ($statusCode < 200 || $statusCode > 299) {
                throw new ApiException(
                    sprintf(
                        '[%d] Error connecting to the API (%s)',
                        $statusCode,
                        $request->getUri()
                    ),
                    $statusCode,
                    $response->getHeaders(),
                    $response->getBody()
                );
            }

            $responseBody = $response->getBody();
            if ($returnType === '\SplFileObject') {
                $content = $responseBody; //stream goes to serializer
            } else {
                $content = $responseBody->getContents();
                if (!in_array($returnType, ['string','integer','bool'])) {
                    $content = json_decode($content);
                }
            }

            return [
                ObjectSerializer::deserialize($content, $returnType, []),
                $response->getStatusCode(),
                $response->getHeaders()
            ];

        } catch (ApiException $e) {
            switch ($e->getCode()) {
                case 200:
                    $data = ObjectSerializer::deserialize(
                        $e->getResponseBody(),
                        '\Swagger\Client\Model\InlineResponse200',
                        $e->getResponseHeaders()
                    );
                    $e->setResponseObject($data);
                    break;
            }
            throw $e;
        }
    }

    /**
     * Operation ordersSendAsync
     *
     * Send Order
     *
     * @param  \Swagger\Client\Model\OrderSendBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function ordersSendAsync($body = null)
    {
        return $this->ordersSendAsyncWithHttpInfo($body)
            ->then(
                function ($response) {
                    return $response[0];
                }
            );
    }

    /**
     * Operation ordersSendAsyncWithHttpInfo
     *
     * Send Order
     *
     * @param  \Swagger\Client\Model\OrderSendBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function ordersSendAsyncWithHttpInfo($body = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse200';
        $request = $this->ordersSendRequest($body);

        return $this->client
            ->sendAsync($request, $this->createHttpClientOption())
            ->then(
                function ($response) use ($returnType) {
                    $responseBody = $response->getBody();
                    if ($returnType === '\SplFileObject') {
                        $content = $responseBody; //stream goes to serializer
                    } else {
                        $content = $responseBody->getContents();
                        if ($returnType !== 'string') {
                            $content = json_decode($content);
                        }
                    }

                    return [
                        ObjectSerializer::deserialize($content, $returnType, []),
                        $response->getStatusCode(),
                        $response->getHeaders()
                    ];
                },
                function ($exception) {
                    $response = $exception->getResponse();
                    $statusCode = $response->getStatusCode();
                    throw new ApiException(
                        sprintf(
                            '[%d] Error connecting to the API (%s)',
                            $statusCode,
                            $exception->getRequest()->getUri()
                        ),
                        $statusCode,
                        $response->getHeaders(),
                        $response->getBody()
                    );
                }
            );
    }

    /**
     * Create request for operation 'ordersSend'
     *
     * @param  \Swagger\Client\Model\OrderSendBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Psr7\Request
     */
    protected function ordersSendRequest($body = null)
    {

        $resourcePath = '/api/v5/order/send';
        $formParams = [];
        $queryParams = [];
        $headerParams = [];
        $httpBody = '';
        $multipart = false;



        // body params
        $_tempBody = null;
        if (isset($body)) {
            $_tempBody = $body;
        }

        if ($multipart) {
            $headers = $this->headerSelector->selectHeadersForMultipart(
                ['application/json']
            );
        } else {
            $headers = $this->headerSelector->selectHeaders(
                ['application/json'],
                ['application/json']
            );
        }

        // for model (json/xml)
        if (isset($_tempBody)) {
            // $_tempBody is the method argument, if present
            $httpBody = $_tempBody;
            // \stdClass has no __toString(), so we should encode it manually
            if ($httpBody instanceof \stdClass && $headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($httpBody);
            }
        } elseif (count($formParams) > 0) {
            if ($multipart) {
                $multipartContents = [];
                foreach ($formParams as $formParamName => $formParamValue) {
                    $multipartContents[] = [
                        'name' => $formParamName,
                        'contents' => $formParamValue
                    ];
                }
                // for HTTP post (form)
                $httpBody = new MultipartStream($multipartContents);

            } elseif ($headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($formParams);

            } else {
                // for HTTP post (form)
                $httpBody = \GuzzleHttp\Psr7\build_query($formParams);
            }
        }

        // this endpoint requires API key authentication
        $apiKey = $this->config->getApiKeyWithPrefix('jwt');
        if ($apiKey !== null) {
            $headers['jwt'] = $apiKey;
        }

        $defaultHeaders = [];
        if ($this->config->getUserAgent()) {
            $defaultHeaders['User-Agent'] = $this->config->getUserAgent();
        }

        $headers = array_merge(
            $defaultHeaders,
            $headerParams,
            $headers
        );

        $query = \GuzzleHttp\Psr7\build_query($queryParams);
        return new Request(
            'POST',
            $this->config->getHost() . $resourcePath . ($query ? "?{$query}" : ''),
            $headers,
            $httpBody
        );
    }

    /**
     * Operation paymentCalculateBankFee
     *
     * Calculate bank payment transaction fee
     *
     * @param  \Swagger\Client\Model\PaymenttxnCalculatebankfeeBody $body body (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return \Swagger\Client\Model\InlineResponse2005
     */
    public function paymentCalculateBankFee($body = null)
    {
        list($response) = $this->paymentCalculateBankFeeWithHttpInfo($body);
        return $response;
    }

    /**
     * Operation paymentCalculateBankFeeWithHttpInfo
     *
     * Calculate bank payment transaction fee
     *
     * @param  \Swagger\Client\Model\PaymenttxnCalculatebankfeeBody $body (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return array of \Swagger\Client\Model\InlineResponse2005, HTTP status code, HTTP response headers (array of strings)
     */
    public function paymentCalculateBankFeeWithHttpInfo($body = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse2005';
        $request = $this->paymentCalculateBankFeeRequest($body);

        try {
            $options = $this->createHttpClientOption();
            try {
                $response = $this->client->send($request, $options);
            } catch (RequestException $e) {
                throw new ApiException(
                    "[{$e->getCode()}] {$e->getMessage()}",
                    $e->getCode(),
                    $e->getResponse() ? $e->getResponse()->getHeaders() : null,
                    $e->getResponse() ? $e->getResponse()->getBody()->getContents() : null
                );
            }

            $statusCode = $response->getStatusCode();

            if ($statusCode < 200 || $statusCode > 299) {
                throw new ApiException(
                    sprintf(
                        '[%d] Error connecting to the API (%s)',
                        $statusCode,
                        $request->getUri()
                    ),
                    $statusCode,
                    $response->getHeaders(),
                    $response->getBody()
                );
            }

            $responseBody = $response->getBody();
            if ($returnType === '\SplFileObject') {
                $content = $responseBody; //stream goes to serializer
            } else {
                $content = $responseBody->getContents();
                if (!in_array($returnType, ['string','integer','bool'])) {
                    $content = json_decode($content);
                }
            }

            return [
                ObjectSerializer::deserialize($content, $returnType, []),
                $response->getStatusCode(),
                $response->getHeaders()
            ];

        } catch (ApiException $e) {
            switch ($e->getCode()) {
                case 200:
                    $data = ObjectSerializer::deserialize(
                        $e->getResponseBody(),
                        '\Swagger\Client\Model\InlineResponse2005',
                        $e->getResponseHeaders()
                    );
                    $e->setResponseObject($data);
                    break;
            }
            throw $e;
        }
    }

    /**
     * Operation paymentCalculateBankFeeAsync
     *
     * Calculate bank payment transaction fee
     *
     * @param  \Swagger\Client\Model\PaymenttxnCalculatebankfeeBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function paymentCalculateBankFeeAsync($body = null)
    {
        return $this->paymentCalculateBankFeeAsyncWithHttpInfo($body)
            ->then(
                function ($response) {
                    return $response[0];
                }
            );
    }

    /**
     * Operation paymentCalculateBankFeeAsyncWithHttpInfo
     *
     * Calculate bank payment transaction fee
     *
     * @param  \Swagger\Client\Model\PaymenttxnCalculatebankfeeBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function paymentCalculateBankFeeAsyncWithHttpInfo($body = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse2005';
        $request = $this->paymentCalculateBankFeeRequest($body);

        return $this->client
            ->sendAsync($request, $this->createHttpClientOption())
            ->then(
                function ($response) use ($returnType) {
                    $responseBody = $response->getBody();
                    if ($returnType === '\SplFileObject') {
                        $content = $responseBody; //stream goes to serializer
                    } else {
                        $content = $responseBody->getContents();
                        if ($returnType !== 'string') {
                            $content = json_decode($content);
                        }
                    }

                    return [
                        ObjectSerializer::deserialize($content, $returnType, []),
                        $response->getStatusCode(),
                        $response->getHeaders()
                    ];
                },
                function ($exception) {
                    $response = $exception->getResponse();
                    $statusCode = $response->getStatusCode();
                    throw new ApiException(
                        sprintf(
                            '[%d] Error connecting to the API (%s)',
                            $statusCode,
                            $exception->getRequest()->getUri()
                        ),
                        $statusCode,
                        $response->getHeaders(),
                        $response->getBody()
                    );
                }
            );
    }

    /**
     * Create request for operation 'paymentCalculateBankFee'
     *
     * @param  \Swagger\Client\Model\PaymenttxnCalculatebankfeeBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Psr7\Request
     */
    protected function paymentCalculateBankFeeRequest($body = null)
    {

        $resourcePath = 'api/v5/payment-txn/calculate-bank-fee';
        $formParams = [];
        $queryParams = [];
        $headerParams = [];
        $httpBody = '';
        $multipart = false;



        // body params
        $_tempBody = null;
        if (isset($body)) {
            $_tempBody = $body;
        }

        if ($multipart) {
            $headers = $this->headerSelector->selectHeadersForMultipart(
                ['application/json']
            );
        } else {
            $headers = $this->headerSelector->selectHeaders(
                ['application/json'],
                ['application/json']
            );
        }

        // for model (json/xml)
        if (isset($_tempBody)) {
            // $_tempBody is the method argument, if present
            $httpBody = $_tempBody;
            // \stdClass has no __toString(), so we should encode it manually
            if ($httpBody instanceof \stdClass && $headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($httpBody);
            }
        } elseif (count($formParams) > 0) {
            if ($multipart) {
                $multipartContents = [];
                foreach ($formParams as $formParamName => $formParamValue) {
                    $multipartContents[] = [
                        'name' => $formParamName,
                        'contents' => $formParamValue
                    ];
                }
                // for HTTP post (form)
                $httpBody = new MultipartStream($multipartContents);

            } elseif ($headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($formParams);

            } else {
                // for HTTP post (form)
                $httpBody = \GuzzleHttp\Psr7\build_query($formParams);
            }
        }

        // this endpoint requires API key authentication
        $apiKey = $this->config->getApiKeyWithPrefix('jwt');
        if ($apiKey !== null) {
            $headers['jwt'] = $apiKey;
        }

        $defaultHeaders = [];
        if ($this->config->getUserAgent()) {
            $defaultHeaders['User-Agent'] = $this->config->getUserAgent();
        }

        $headers = array_merge(
            $defaultHeaders,
            $headerParams,
            $headers
        );

        $query = \GuzzleHttp\Psr7\build_query($queryParams);
        return new Request(
            'POST',
            $this->config->getHost() . $resourcePath . ($query ? "?{$query}" : ''),
            $headers,
            $httpBody
        );
    }

    /**
     * Operation paymentCalculateFee
     *
     * Calculating Bao Kim payment transaction fee
     *
     * @param  \Swagger\Client\Model\PaymenttxnCalculatebkfeeBody $body body (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return \Swagger\Client\Model\InlineResponse2004
     */
    public function paymentCalculateFee($body = null)
    {
        list($response) = $this->paymentCalculateFeeWithHttpInfo($body);
        return $response;
    }

    /**
     * Operation paymentCalculateFeeWithHttpInfo
     *
     * Calculating Bao Kim payment transaction fee
     *
     * @param  \Swagger\Client\Model\PaymenttxnCalculatebkfeeBody $body (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return array of \Swagger\Client\Model\InlineResponse2004, HTTP status code, HTTP response headers (array of strings)
     */
    public function paymentCalculateFeeWithHttpInfo($body = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse2004';
        $request = $this->paymentCalculateFeeRequest($body);

        try {
            $options = $this->createHttpClientOption();
            try {
                $response = $this->client->send($request, $options);
            } catch (RequestException $e) {
                throw new ApiException(
                    "[{$e->getCode()}] {$e->getMessage()}",
                    $e->getCode(),
                    $e->getResponse() ? $e->getResponse()->getHeaders() : null,
                    $e->getResponse() ? $e->getResponse()->getBody()->getContents() : null
                );
            }

            $statusCode = $response->getStatusCode();

            if ($statusCode < 200 || $statusCode > 299) {
                throw new ApiException(
                    sprintf(
                        '[%d] Error connecting to the API (%s)',
                        $statusCode,
                        $request->getUri()
                    ),
                    $statusCode,
                    $response->getHeaders(),
                    $response->getBody()
                );
            }

            $responseBody = $response->getBody();
            if ($returnType === '\SplFileObject') {
                $content = $responseBody; //stream goes to serializer
            } else {
                $content = $responseBody->getContents();
                if (!in_array($returnType, ['string','integer','bool'])) {
                    $content = json_decode($content);
                }
            }

            return [
                ObjectSerializer::deserialize($content, $returnType, []),
                $response->getStatusCode(),
                $response->getHeaders()
            ];

        } catch (ApiException $e) {
            switch ($e->getCode()) {
                case 200:
                    $data = ObjectSerializer::deserialize(
                        $e->getResponseBody(),
                        '\Swagger\Client\Model\InlineResponse2004',
                        $e->getResponseHeaders()
                    );
                    $e->setResponseObject($data);
                    break;
            }
            throw $e;
        }
    }

    /**
     * Operation paymentCalculateFeeAsync
     *
     * Calculating Bao Kim payment transaction fee
     *
     * @param  \Swagger\Client\Model\PaymenttxnCalculatebkfeeBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function paymentCalculateFeeAsync($body = null)
    {
        return $this->paymentCalculateFeeAsyncWithHttpInfo($body)
            ->then(
                function ($response) {
                    return $response[0];
                }
            );
    }

    /**
     * Operation paymentCalculateFeeAsyncWithHttpInfo
     *
     * Calculating Bao Kim payment transaction fee
     *
     * @param  \Swagger\Client\Model\PaymenttxnCalculatebkfeeBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function paymentCalculateFeeAsyncWithHttpInfo($body = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse2004';
        $request = $this->paymentCalculateFeeRequest($body);

        return $this->client
            ->sendAsync($request, $this->createHttpClientOption())
            ->then(
                function ($response) use ($returnType) {
                    $responseBody = $response->getBody();
                    if ($returnType === '\SplFileObject') {
                        $content = $responseBody; //stream goes to serializer
                    } else {
                        $content = $responseBody->getContents();
                        if ($returnType !== 'string') {
                            $content = json_decode($content);
                        }
                    }

                    return [
                        ObjectSerializer::deserialize($content, $returnType, []),
                        $response->getStatusCode(),
                        $response->getHeaders()
                    ];
                },
                function ($exception) {
                    $response = $exception->getResponse();
                    $statusCode = $response->getStatusCode();
                    throw new ApiException(
                        sprintf(
                            '[%d] Error connecting to the API (%s)',
                            $statusCode,
                            $exception->getRequest()->getUri()
                        ),
                        $statusCode,
                        $response->getHeaders(),
                        $response->getBody()
                    );
                }
            );
    }

    /**
     * Create request for operation 'paymentCalculateFee'
     *
     * @param  \Swagger\Client\Model\PaymenttxnCalculatebkfeeBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Psr7\Request
     */
    protected function paymentCalculateFeeRequest($body = null)
    {

        $resourcePath = 'api/v5/payment-txn/calculate-bk-fee';
        $formParams = [];
        $queryParams = [];
        $headerParams = [];
        $httpBody = '';
        $multipart = false;



        // body params
        $_tempBody = null;
        if (isset($body)) {
            $_tempBody = $body;
        }

        if ($multipart) {
            $headers = $this->headerSelector->selectHeadersForMultipart(
                ['application/json']
            );
        } else {
            $headers = $this->headerSelector->selectHeaders(
                ['application/json'],
                ['application/json']
            );
        }

        // for model (json/xml)
        if (isset($_tempBody)) {
            // $_tempBody is the method argument, if present
            $httpBody = $_tempBody;
            // \stdClass has no __toString(), so we should encode it manually
            if ($httpBody instanceof \stdClass && $headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($httpBody);
            }
        } elseif (count($formParams) > 0) {
            if ($multipart) {
                $multipartContents = [];
                foreach ($formParams as $formParamName => $formParamValue) {
                    $multipartContents[] = [
                        'name' => $formParamName,
                        'contents' => $formParamValue
                    ];
                }
                // for HTTP post (form)
                $httpBody = new MultipartStream($multipartContents);

            } elseif ($headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($formParams);

            } else {
                // for HTTP post (form)
                $httpBody = \GuzzleHttp\Psr7\build_query($formParams);
            }
        }

        // this endpoint requires API key authentication
        $apiKey = $this->config->getApiKeyWithPrefix('jwt');
        if ($apiKey !== null) {
            $headers['jwt'] = $apiKey;
        }

        $defaultHeaders = [];
        if ($this->config->getUserAgent()) {
            $defaultHeaders['User-Agent'] = $this->config->getUserAgent();
        }

        $headers = array_merge(
            $defaultHeaders,
            $headerParams,
            $headers
        );

        $query = \GuzzleHttp\Psr7\build_query($queryParams);
        return new Request(
            'POST',
            $this->config->getHost() . $resourcePath . ($query ? "?{$query}" : ''),
            $headers,
            $httpBody
        );
    }

    /**
     * Operation refundCreate
     *
     * Create Refund
     *
     * @param  \Swagger\Client\Model\RefundCreateBody $body body (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return \Swagger\Client\Model\InlineResponse2006
     */
    public function refundCreate($body = null)
    {
        list($response) = $this->refundCreateWithHttpInfo($body);
        return $response;
    }

    /**
     * Operation refundCreateWithHttpInfo
     *
     * Create Refund
     *
     * @param  \Swagger\Client\Model\RefundCreateBody $body (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return array of \Swagger\Client\Model\InlineResponse2006, HTTP status code, HTTP response headers (array of strings)
     */
    public function refundCreateWithHttpInfo($body = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse2006';
        $request = $this->refundCreateRequest($body);

        try {
            $options = $this->createHttpClientOption();
            try {
                $response = $this->client->send($request, $options);
            } catch (RequestException $e) {
                throw new ApiException(
                    "[{$e->getCode()}] {$e->getMessage()}",
                    $e->getCode(),
                    $e->getResponse() ? $e->getResponse()->getHeaders() : null,
                    $e->getResponse() ? $e->getResponse()->getBody()->getContents() : null
                );
            }

            $statusCode = $response->getStatusCode();

            if ($statusCode < 200 || $statusCode > 299) {
                throw new ApiException(
                    sprintf(
                        '[%d] Error connecting to the API (%s)',
                        $statusCode,
                        $request->getUri()
                    ),
                    $statusCode,
                    $response->getHeaders(),
                    $response->getBody()
                );
            }

            $responseBody = $response->getBody();
            if ($returnType === '\SplFileObject') {
                $content = $responseBody; //stream goes to serializer
            } else {
                $content = $responseBody->getContents();
                if (!in_array($returnType, ['string','integer','bool'])) {
                    $content = json_decode($content);
                }
            }

            return [
                ObjectSerializer::deserialize($content, $returnType, []),
                $response->getStatusCode(),
                $response->getHeaders()
            ];

        } catch (ApiException $e) {
            switch ($e->getCode()) {
                case 200:
                    $data = ObjectSerializer::deserialize(
                        $e->getResponseBody(),
                        '\Swagger\Client\Model\InlineResponse2006',
                        $e->getResponseHeaders()
                    );
                    $e->setResponseObject($data);
                    break;
            }
            throw $e;
        }
    }

    /**
     * Operation refundCreateAsync
     *
     * Create Refund
     *
     * @param  \Swagger\Client\Model\RefundCreateBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function refundCreateAsync($body = null)
    {
        return $this->refundCreateAsyncWithHttpInfo($body)
            ->then(
                function ($response) {
                    return $response[0];
                }
            );
    }

    /**
     * Operation refundCreateAsyncWithHttpInfo
     *
     * Create Refund
     *
     * @param  \Swagger\Client\Model\RefundCreateBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function refundCreateAsyncWithHttpInfo($body = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse2006';
        $request = $this->refundCreateRequest($body);

        return $this->client
            ->sendAsync($request, $this->createHttpClientOption())
            ->then(
                function ($response) use ($returnType) {
                    $responseBody = $response->getBody();
                    if ($returnType === '\SplFileObject') {
                        $content = $responseBody; //stream goes to serializer
                    } else {
                        $content = $responseBody->getContents();
                        if ($returnType !== 'string') {
                            $content = json_decode($content);
                        }
                    }

                    return [
                        ObjectSerializer::deserialize($content, $returnType, []),
                        $response->getStatusCode(),
                        $response->getHeaders()
                    ];
                },
                function ($exception) {
                    $response = $exception->getResponse();
                    $statusCode = $response->getStatusCode();
                    throw new ApiException(
                        sprintf(
                            '[%d] Error connecting to the API (%s)',
                            $statusCode,
                            $exception->getRequest()->getUri()
                        ),
                        $statusCode,
                        $response->getHeaders(),
                        $response->getBody()
                    );
                }
            );
    }

    /**
     * Create request for operation 'refundCreate'
     *
     * @param  \Swagger\Client\Model\RefundCreateBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Psr7\Request
     */
    protected function refundCreateRequest($body = null)
    {

        $resourcePath = 'api/v5/refund/create';
        $formParams = [];
        $queryParams = [];
        $headerParams = [];
        $httpBody = '';
        $multipart = false;



        // body params
        $_tempBody = null;
        if (isset($body)) {
            $_tempBody = $body;
        }

        if ($multipart) {
            $headers = $this->headerSelector->selectHeadersForMultipart(
                ['application/json']
            );
        } else {
            $headers = $this->headerSelector->selectHeaders(
                ['application/json'],
                ['application/json']
            );
        }

        // for model (json/xml)
        if (isset($_tempBody)) {
            // $_tempBody is the method argument, if present
            $httpBody = $_tempBody;
            // \stdClass has no __toString(), so we should encode it manually
            if ($httpBody instanceof \stdClass && $headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($httpBody);
            }
        } elseif (count($formParams) > 0) {
            if ($multipart) {
                $multipartContents = [];
                foreach ($formParams as $formParamName => $formParamValue) {
                    $multipartContents[] = [
                        'name' => $formParamName,
                        'contents' => $formParamValue
                    ];
                }
                // for HTTP post (form)
                $httpBody = new MultipartStream($multipartContents);

            } elseif ($headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($formParams);

            } else {
                // for HTTP post (form)
                $httpBody = \GuzzleHttp\Psr7\build_query($formParams);
            }
        }

        // this endpoint requires API key authentication
        $apiKey = $this->config->getApiKeyWithPrefix('jwt');
        if ($apiKey !== null) {
            $headers['jwt'] = $apiKey;
        }

        $defaultHeaders = [];
        if ($this->config->getUserAgent()) {
            $defaultHeaders['User-Agent'] = $this->config->getUserAgent();
        }

        $headers = array_merge(
            $defaultHeaders,
            $headerParams,
            $headers
        );

        $query = \GuzzleHttp\Psr7\build_query($queryParams);
        return new Request(
            'POST',
            $this->config->getHost() . $resourcePath . ($query ? "?{$query}" : ''),
            $headers,
            $httpBody
        );
    }

    /**
     * Operation tokenizationSendOrder
     *
     * Create Token Order
     *
     * @param  \Swagger\Client\Model\TokenizationTransactionBody $body body (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return \Swagger\Client\Model\InlineResponse200
     */
    public function tokenizationSendOrder($body = null)
    {
        list($response) = $this->tokenizationSendOrderWithHttpInfo($body);
        return $response;
    }

    /**
     * Operation tokenizationSendOrderWithHttpInfo
     *
     * Create Token Order
     *
     * @param  \Swagger\Client\Model\TokenizationTransactionBody $body (optional)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return array of \Swagger\Client\Model\InlineResponse200, HTTP status code, HTTP response headers (array of strings)
     */
    public function tokenizationSendOrderWithHttpInfo($body = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse200';
        $request = $this->tokenizationSendOrderRequest($body);

        try {
            $options = $this->createHttpClientOption();
            try {
                $response = $this->client->send($request, $options);
            } catch (RequestException $e) {
                throw new ApiException(
                    "[{$e->getCode()}] {$e->getMessage()}",
                    $e->getCode(),
                    $e->getResponse() ? $e->getResponse()->getHeaders() : null,
                    $e->getResponse() ? $e->getResponse()->getBody()->getContents() : null
                );
            }

            $statusCode = $response->getStatusCode();

            if ($statusCode < 200 || $statusCode > 299) {
                throw new ApiException(
                    sprintf(
                        '[%d] Error connecting to the API (%s)',
                        $statusCode,
                        $request->getUri()
                    ),
                    $statusCode,
                    $response->getHeaders(),
                    $response->getBody()
                );
            }

            $responseBody = $response->getBody();
            if ($returnType === '\SplFileObject') {
                $content = $responseBody; //stream goes to serializer
            } else {
                $content = $responseBody->getContents();
                if (!in_array($returnType, ['string','integer','bool'])) {
                    $content = json_decode($content);
                }
            }

            return [
                ObjectSerializer::deserialize($content, $returnType, []),
                $response->getStatusCode(),
                $response->getHeaders()
            ];

        } catch (ApiException $e) {
            switch ($e->getCode()) {
                case 200:
                    $data = ObjectSerializer::deserialize(
                        $e->getResponseBody(),
                        '\Swagger\Client\Model\InlineResponse200',
                        $e->getResponseHeaders()
                    );
                    $e->setResponseObject($data);
                    break;
            }
            throw $e;
        }
    }

    /**
     * Operation tokenizationSendOrderAsync
     *
     * Create Token Order
     *
     * @param  \Swagger\Client\Model\TokenizationTransactionBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function tokenizationSendOrderAsync($body = null)
    {
        return $this->tokenizationSendOrderAsyncWithHttpInfo($body)
            ->then(
                function ($response) {
                    return $response[0];
                }
            );
    }

    /**
     * Operation tokenizationSendOrderAsyncWithHttpInfo
     *
     * Create Token Order
     *
     * @param  \Swagger\Client\Model\TokenizationTransactionBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function tokenizationSendOrderAsyncWithHttpInfo($body = null)
    {
        $returnType = '\Swagger\Client\Model\InlineResponse200';
        $request = $this->tokenizationSendOrderRequest($body);

        return $this->client
            ->sendAsync($request, $this->createHttpClientOption())
            ->then(
                function ($response) use ($returnType) {
                    $responseBody = $response->getBody();
                    if ($returnType === '\SplFileObject') {
                        $content = $responseBody; //stream goes to serializer
                    } else {
                        $content = $responseBody->getContents();
                        if ($returnType !== 'string') {
                            $content = json_decode($content);
                        }
                    }

                    return [
                        ObjectSerializer::deserialize($content, $returnType, []),
                        $response->getStatusCode(),
                        $response->getHeaders()
                    ];
                },
                function ($exception) {
                    $response = $exception->getResponse();
                    $statusCode = $response->getStatusCode();
                    throw new ApiException(
                        sprintf(
                            '[%d] Error connecting to the API (%s)',
                            $statusCode,
                            $exception->getRequest()->getUri()
                        ),
                        $statusCode,
                        $response->getHeaders(),
                        $response->getBody()
                    );
                }
            );
    }

    /**
     * Create request for operation 'tokenizationSendOrder'
     *
     * @param  \Swagger\Client\Model\TokenizationTransactionBody $body (optional)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Psr7\Request
     */
    protected function tokenizationSendOrderRequest($body = null)
    {

        $resourcePath = '/api/v1/tokenization/transaction';
        $formParams = [];
        $queryParams = [];
        $headerParams = [];
        $httpBody = '';
        $multipart = false;



        // body params
        $_tempBody = null;
        if (isset($body)) {
            $_tempBody = $body;
        }

        if ($multipart) {
            $headers = $this->headerSelector->selectHeadersForMultipart(
                ['application/json']
            );
        } else {
            $headers = $this->headerSelector->selectHeaders(
                ['application/json'],
                ['application/json']
            );
        }

        // for model (json/xml)
        if (isset($_tempBody)) {
            // $_tempBody is the method argument, if present
            $httpBody = $_tempBody;
            // \stdClass has no __toString(), so we should encode it manually
            if ($httpBody instanceof \stdClass && $headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($httpBody);
            }
        } elseif (count($formParams) > 0) {
            if ($multipart) {
                $multipartContents = [];
                foreach ($formParams as $formParamName => $formParamValue) {
                    $multipartContents[] = [
                        'name' => $formParamName,
                        'contents' => $formParamValue
                    ];
                }
                // for HTTP post (form)
                $httpBody = new MultipartStream($multipartContents);

            } elseif ($headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($formParams);

            } else {
                // for HTTP post (form)
                $httpBody = \GuzzleHttp\Psr7\build_query($formParams);
            }
        }

        // this endpoint requires API key authentication
        $apiKey = $this->config->getApiKeyWithPrefix('jwt');
        if ($apiKey !== null) {
            $headers['jwt'] = $apiKey;
        }

        $defaultHeaders = [];
        if ($this->config->getUserAgent()) {
            $defaultHeaders['User-Agent'] = $this->config->getUserAgent();
        }

        $headers = array_merge(
            $defaultHeaders,
            $headerParams,
            $headers
        );

        $query = \GuzzleHttp\Psr7\build_query($queryParams);
        return new Request(
            'POST',
            $this->config->getHost() . $resourcePath . ($query ? "?{$query}" : ''),
            $headers,
            $httpBody
        );
    }

    /**
     * Create http client option
     *
     * @throws \RuntimeException on file opening failure
     * @return array of http client options
     */
    protected function createHttpClientOption()
    {
        $options = [];
        if ($this->config->getDebug()) {
            $options[RequestOptions::DEBUG] = fopen($this->config->getDebugFile(), 'a');
            if (!$options[RequestOptions::DEBUG]) {
                throw new \RuntimeException('Failed to open the debug file: ' . $this->config->getDebugFile());
            }
        }

        return $options;
    }
}
