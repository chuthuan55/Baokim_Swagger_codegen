# Swagger\Client\VerifyCustomerInformationApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verifyPost**](VerifyCustomerInformationApi.md#verifypost) | **POST** /Verify | https::devtest.baokim.vn/Sandbox/FirmBanking

# **verifyPost**
> \Swagger\Client\Model\InlineResponse200 verifyPost($body)

https::devtest.baokim.vn/Sandbox/FirmBanking

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\VerifyCustomerInformationApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\VerifyBody(); // \Swagger\Client\Model\VerifyBody | 1. Partner will call the customer authentication function, Baokim will check the data format and signature authentication..

2. Baokim continues to check customer information and corresponding bank

3. If the information is correct, Baokim will return successful information and corresponding customer name.

try {
    $result = $apiInstance->verifyPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling VerifyCustomerInformationApi->verifyPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\VerifyBody**](../Model/VerifyBody.md)| 1. Partner will call the customer authentication function, Baokim will check the data format and signature authentication..

2. Baokim continues to check customer information and corresponding bank

3. If the information is correct, Baokim will return successful information and corresponding customer name. | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse200**](../Model/InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

