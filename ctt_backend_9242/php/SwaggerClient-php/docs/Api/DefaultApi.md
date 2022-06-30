# Swagger\Client\DefaultApi

All URIs are relative to *https://dev-api.baokim.vn/payment/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bpmList**](DefaultApi.md#bpmlist) | **GET** api/v5/bpm/list | Bank Payment Method List
[**ordersCancel**](DefaultApi.md#orderscancel) | **POST** /api/v5/order/cancel | Order Cancel
[**ordersDetail**](DefaultApi.md#ordersdetail) | **GET** /api/v5/order/detail | Order Detail
[**ordersSend**](DefaultApi.md#orderssend) | **POST** /api/v5/order/send | Send Order
[**paymentCalculateBankFee**](DefaultApi.md#paymentcalculatebankfee) | **POST** api/v5/payment-txn/calculate-bank-fee | Calculate bank payment transaction fee
[**paymentCalculateFee**](DefaultApi.md#paymentcalculatefee) | **POST** api/v5/payment-txn/calculate-bk-fee | Calculating Bao Kim payment transaction fee
[**refundCreate**](DefaultApi.md#refundcreate) | **POST** api/v5/refund/create | Create Refund
[**tokenizationSendOrder**](DefaultApi.md#tokenizationsendorder) | **POST** /api/v1/tokenization/transaction | Create Token Order

# **bpmList**
> \Swagger\Client\Model\InlineResponse2003 bpmList()

Bank Payment Method List

List of payment methods supported by Bao Kim, Web/App merchants can use this API to display payment methods on their application. This list is sorted by field \"type\" ( type = 1 - ATM cards online banks type = 2 - Visa/Master type = 3 - Internet Banking type = 14 - QR code type = 16 - Virtual Account )

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure API key authorization: JWT
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('jwt', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('jwt', 'Bearer');

$apiInstance = new Swagger\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->bpmList();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->bpmList: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**\Swagger\Client\Model\InlineResponse2003**](../Model/InlineResponse2003.md)

### Authorization

[JWT](../../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **ordersCancel**
> \Swagger\Client\Model\InlineResponse2002 ordersCancel($body)

Order Cancel

Order cancellation API, used in case you do not want to receive payment for orders anymore

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure API key authorization: JWT
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('jwt', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('jwt', 'Bearer');

$apiInstance = new Swagger\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\OrderCancelBody(); // \Swagger\Client\Model\OrderCancelBody | 

try {
    $result = $apiInstance->ordersCancel($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->ordersCancel: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\OrderCancelBody**](../Model/OrderCancelBody.md)|  | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2002**](../Model/InlineResponse2002.md)

### Authorization

[JWT](../../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **ordersDetail**
> \Swagger\Client\Model\InlineResponse2001 ordersDetail($id, $mrc_order_id)

Order Detail

API Get order details, can be used to check order payment status. An order is considered to have been successfully paid when there stat == 'c'(completed). Payment transaction of order status \"stat\" == 1. Order status list ('p' - processing, 'c' - completed, 'd' - destructed)

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure API key authorization: JWT
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('jwt', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('jwt', 'Bearer');

$apiInstance = new Swagger\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 56; // int | Order ID [semi-optional]
$mrc_order_id = "mrc_order_id_example"; // string | Merchant Order ID [semi-optional]

try {
    $result = $apiInstance->ordersDetail($id, $mrc_order_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->ordersDetail: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID [semi-optional] | [optional]
 **mrc_order_id** | **string**| Merchant Order ID [semi-optional] | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2001**](../Model/InlineResponse2001.md)

### Authorization

[JWT](../../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **ordersSend**
> \Swagger\Client\Model\InlineResponse200 ordersSend($body)

Send Order

API Send order information from merchant's application to Bao Kim to make payment.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure API key authorization: JWT
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('jwt', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('jwt', 'Bearer');

$apiInstance = new Swagger\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\OrderSendBody(); // \Swagger\Client\Model\OrderSendBody | 

try {
    $result = $apiInstance->ordersSend($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->ordersSend: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\OrderSendBody**](../Model/OrderSendBody.md)|  | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse200**](../Model/InlineResponse200.md)

### Authorization

[JWT](../../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **paymentCalculateBankFee**
> \Swagger\Client\Model\InlineResponse2005 paymentCalculateBankFee($body)

Calculate bank payment transaction fee

The API gets Bank's fee info including the amount and the person who pays the fee( fee_payer = 1 - Buyer bear the fee, fee_payer = 2 - Merchant bears the fee ).

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure API key authorization: JWT
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('jwt', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('jwt', 'Bearer');

$apiInstance = new Swagger\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\PaymenttxnCalculatebankfeeBody(); // \Swagger\Client\Model\PaymenttxnCalculatebankfeeBody | 

try {
    $result = $apiInstance->paymentCalculateBankFee($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->paymentCalculateBankFee: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\PaymenttxnCalculatebankfeeBody**](../Model/PaymenttxnCalculatebankfeeBody.md)|  | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2005**](../Model/InlineResponse2005.md)

### Authorization

[JWT](../../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **paymentCalculateFee**
> \Swagger\Client\Model\InlineResponse2004 paymentCalculateFee($body)

Calculating Bao Kim payment transaction fee

The API gets Bao Kim's fee info including the amount and the person who pays the fee( fee_payer = 1 - Buyer bear the fee, fee_payer = 2 - Merchant bears the fee ).

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure API key authorization: JWT
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('jwt', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('jwt', 'Bearer');

$apiInstance = new Swagger\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\PaymenttxnCalculatebkfeeBody(); // \Swagger\Client\Model\PaymenttxnCalculatebkfeeBody | 

try {
    $result = $apiInstance->paymentCalculateFee($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->paymentCalculateFee: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\PaymenttxnCalculatebkfeeBody**](../Model/PaymenttxnCalculatebkfeeBody.md)|  | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2004**](../Model/InlineResponse2004.md)

### Authorization

[JWT](../../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **refundCreate**
> \Swagger\Client\Model\InlineResponse2006 refundCreate($body)

Create Refund

Create a refund transaction

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure API key authorization: JWT
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('jwt', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('jwt', 'Bearer');

$apiInstance = new Swagger\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\RefundCreateBody(); // \Swagger\Client\Model\RefundCreateBody | 

try {
    $result = $apiInstance->refundCreate($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->refundCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\RefundCreateBody**](../Model/RefundCreateBody.md)|  | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2006**](../Model/InlineResponse2006.md)

### Authorization

[JWT](../../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **tokenizationSendOrder**
> \Swagger\Client\Model\InlineResponse200 tokenizationSendOrder($body)

Create Token Order

Create a token order

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure API key authorization: JWT
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('jwt', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('jwt', 'Bearer');

$apiInstance = new Swagger\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\TokenizationTransactionBody(); // \Swagger\Client\Model\TokenizationTransactionBody | 

try {
    $result = $apiInstance->tokenizationSendOrder($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->tokenizationSendOrder: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\TokenizationTransactionBody**](../Model/TokenizationTransactionBody.md)|  | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse200**](../Model/InlineResponse200.md)

### Authorization

[JWT](../../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

