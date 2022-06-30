# Swagger\Client\TransferMoneyApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transferPost**](TransferMoneyApi.md#transferpost) | **POST** /Transfer | https::devtest.baokim.vn/Sandbox/FirmBanking

# **transferPost**
> \Swagger\Client\Model\InlineResponse2001 transferPost($body)

https::devtest.baokim.vn/Sandbox/FirmBanking

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\TransferMoneyApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\TransferBody(); // \Swagger\Client\Model\TransferBody | Process:

1. Partner will call the money transfer function, Baokim will check the data format and signature authentication, then will check the customer information, the amount to transfer.

2. If the correct information will return successful transfer. 

 Note(*) : If the transaction is pending, the Partner must wait for the final result from Baokim by calling the <a href='/baokim-firm-open-api-9003'> Function look up for transfer info </a>.

try {
    $result = $apiInstance->transferPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TransferMoneyApi->transferPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\TransferBody**](../Model/TransferBody.md)| Process:

1. Partner will call the money transfer function, Baokim will check the data format and signature authentication, then will check the customer information, the amount to transfer.

2. If the correct information will return successful transfer. 

 Note(*) : If the transaction is pending, the Partner must wait for the final result from Baokim by calling the &lt;a href&#x3D;&#x27;/baokim-firm-open-api-9003&#x27;&gt; Function look up for transfer info &lt;/a&gt;. | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2001**](../Model/InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

