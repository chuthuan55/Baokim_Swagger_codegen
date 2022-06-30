# Swagger\Client\LookUpForTransferInfoApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookupTransferPost**](LookUpForTransferInfoApi.md#lookuptransferpost) | **POST** /LookupTransfer | https::devtest.baokim.vn/Sandbox/FirmBanking

# **lookupTransferPost**
> \Swagger\Client\Model\InlineResponse2002 lookupTransferPost($body)

https::devtest.baokim.vn/Sandbox/FirmBanking

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\LookUpForTransferInfoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\LookupTransferBody(); // \Swagger\Client\Model\LookupTransferBody | Process:

1. PARTNER will call the transaction information search function, BAOKIM will check the data format and signature authentication, then will check the transaction code..

2. If the information is correct, return the transaction information..

try {
    $result = $apiInstance->lookupTransferPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling LookUpForTransferInfoApi->lookupTransferPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\LookupTransferBody**](../Model/LookupTransferBody.md)| Process:

1. PARTNER will call the transaction information search function, BAOKIM will check the data format and signature authentication, then will check the transaction code..

2. If the information is correct, return the transaction information.. | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2002**](../Model/InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

