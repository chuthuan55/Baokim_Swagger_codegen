# Swagger\Client\VirtualAccount40Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**1796c61005edee3976097a607fe9dbaa**](VirtualAccount40Api.md#1796c61005edee3976097a607fe9dbaa) | **POST** /api/Sandbox/Collection/V4/update | Update virtual account
[**8442c69ffbaf4b3677a52fa3ebcef6d4**](VirtualAccount40Api.md#8442c69ffbaf4b3677a52fa3ebcef6d4) | **POST** /api/Sandbox/Collection/V4/create | Create virtual account

# **1796c61005edee3976097a607fe9dbaa**
> \Swagger\Client\Model\InlineResponse200 1796c61005edee3976097a607fe9dbaa($body, $content_type, $signature)

Update virtual account

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\VirtualAccount40Api(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\V4UpdateBody(); // \Swagger\Client\Model\V4UpdateBody | 
$content_type = "content_type_example"; // string | 
$signature = "signature_example"; // string | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption

try {
    $result = $apiInstance->1796c61005edee3976097a607fe9dbaa($body, $content_type, $signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling VirtualAccount40Api->1796c61005edee3976097a607fe9dbaa: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\V4UpdateBody**](../Model/V4UpdateBody.md)|  |
 **content_type** | **string**|  | [optional]
 **signature** | **string**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse200**](../Model/InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **8442c69ffbaf4b3677a52fa3ebcef6d4**
> \Swagger\Client\Model\InlineResponse200 8442c69ffbaf4b3677a52fa3ebcef6d4($body, $content_type, $signature)

Create virtual account

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\VirtualAccount40Api(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\V4CreateBody(); // \Swagger\Client\Model\V4CreateBody | 
$content_type = "content_type_example"; // string | 
$signature = "signature_example"; // string | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption

try {
    $result = $apiInstance->8442c69ffbaf4b3677a52fa3ebcef6d4($body, $content_type, $signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling VirtualAccount40Api->8442c69ffbaf4b3677a52fa3ebcef6d4: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\V4CreateBody**](../Model/V4CreateBody.md)|  |
 **content_type** | **string**|  | [optional]
 **signature** | **string**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse200**](../Model/InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

