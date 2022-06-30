# Swagger\Client\VirtualAccountVersion23Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**6ce3bcd0268f76548ace52ed5eeeefef**](VirtualAccountVersion23Api.md#6ce3bcd0268f76548ace52ed5eeeefef) | **POST** /api/Sandbox/Collection | create &amp; update va

# **6ce3bcd0268f76548ace52ed5eeeefef**
> \Swagger\Client\Model\InlineResponse200 6ce3bcd0268f76548ace52ed5eeeefef($body, $content_type, $signature)

create & update va

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\VirtualAccountVersion23Api(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\SandboxCollectionBody(); // \Swagger\Client\Model\SandboxCollectionBody | 
$content_type = "content_type_example"; // string | 
$signature = "signature_example"; // string | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption.

try {
    $result = $apiInstance->6ce3bcd0268f76548ace52ed5eeeefef($body, $content_type, $signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling VirtualAccountVersion23Api->6ce3bcd0268f76548ace52ed5eeeefef: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\SandboxCollectionBody**](../Model/SandboxCollectionBody.md)|  |
 **content_type** | **string**|  | [optional]
 **signature** | **string**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption. | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse200**](../Model/InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

