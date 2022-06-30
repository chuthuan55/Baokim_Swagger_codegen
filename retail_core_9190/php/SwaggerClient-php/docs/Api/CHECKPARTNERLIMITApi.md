# Swagger\Client\CHECKPARTNERLIMITApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRetailCheckPartnerLimitPost**](CHECKPARTNERLIMITApi.md#apiretailcheckpartnerlimitpost) | **POST** /api/retail/check-partner-limit | CHECK PARTNER LIMIT

# **apiRetailCheckPartnerLimitPost**
> \Swagger\Client\Model\InlineResponse200 apiRetailCheckPartnerLimitPost($body, $content_type, $signature)

CHECK PARTNER LIMIT

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\CHECKPARTNERLIMITApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\RetailCheckpartnerlimitBody(); // \Swagger\Client\Model\RetailCheckpartnerlimitBody | 
$content_type = "content_type_example"; // string | 
$signature = "signature_example"; // string | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption

try {
    $result = $apiInstance->apiRetailCheckPartnerLimitPost($body, $content_type, $signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CHECKPARTNERLIMITApi->apiRetailCheckPartnerLimitPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\RetailCheckpartnerlimitBody**](../Model/RetailCheckpartnerlimitBody.md)|  |
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

