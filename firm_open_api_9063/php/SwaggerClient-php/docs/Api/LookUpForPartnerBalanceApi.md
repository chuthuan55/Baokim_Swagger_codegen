# Swagger\Client\LookUpForPartnerBalanceApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookupBalancePost**](LookUpForPartnerBalanceApi.md#lookupbalancepost) | **POST** /LookupBalance | https::devtest.baokim.vn/Sandbox/FirmBanking

# **lookupBalancePost**
> \Swagger\Client\Model\InlineResponse2003 lookupBalancePost($body)

https::devtest.baokim.vn/Sandbox/FirmBanking

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\LookUpForPartnerBalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\LookupBalanceBody(); // \Swagger\Client\Model\LookupBalanceBody | Process:

1. Partner will call the partner balance searching function, Baokim will check the data format and signature authentication

2. If the information is correct, return the availale balance.

try {
    $result = $apiInstance->lookupBalancePost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LookUpForPartnerBalanceApi->lookupBalancePost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\LookupBalanceBody**](../Model/LookupBalanceBody.md)| Process:

1. Partner will call the partner balance searching function, Baokim will check the data format and signature authentication

2. If the information is correct, return the availale balance. | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2003**](../Model/InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

