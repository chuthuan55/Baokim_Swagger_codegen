# Swagger\Client\VIRTUALACCOUNTApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**6ce3bcd0268f76548ace52ed5eeeefef**](VIRTUALACCOUNTApi.md#6ce3bcd0268f76548ace52ed5eeeefef) | **POST** /Sandbox/Collection/V2 | create &amp; update va

# **6ce3bcd0268f76548ace52ed5eeeefef**
> \Swagger\Client\Model\InlineResponse200 6ce3bcd0268f76548ace52ed5eeeefef($body, $content_type, $signature)

create & update va

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\VIRTUALACCOUNTApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\CollectionV2Body(); // \Swagger\Client\Model\CollectionV2Body | 
$content_type = "content_type_example"; // string | 
$signature = "signature_example"; // string | BAOKIM sẽ ký Dữ liệu bằng thuật toán sha1WithRSA và sử dụng mã hóa base64

try {
    $result = $apiInstance->6ce3bcd0268f76548ace52ed5eeeefef($body, $content_type, $signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling VIRTUALACCOUNTApi->6ce3bcd0268f76548ace52ed5eeeefef: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\CollectionV2Body**](../Model/CollectionV2Body.md)|  |
 **content_type** | **string**|  | [optional]
 **signature** | **string**| BAOKIM sẽ ký Dữ liệu bằng thuật toán sha1WithRSA và sử dụng mã hóa base64 | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse200**](../Model/InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

