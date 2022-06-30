# Swagger\Client\CancelOrderApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1PartnerCancelOrderPost**](CancelOrderApi.md#apiv1partnercancelorderpost) | **POST** /api/v1/partner/cancel-order | https::devtest.baokim.vn/api/v1/partner/installment

# **apiV1PartnerCancelOrderPost**
> \Swagger\Client\Model\InlineResponse2003 apiV1PartnerCancelOrderPost($body)

https::devtest.baokim.vn/api/v1/partner/installment

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\CancelOrderApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\PartnerCancelorderBody(); // \Swagger\Client\Model\PartnerCancelorderBody | Process:

1. Partner will call the cancel order function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return successful.

try {
    $result = $apiInstance->apiV1PartnerCancelOrderPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CancelOrderApi->apiV1PartnerCancelOrderPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\PartnerCancelorderBody**](../Model/PartnerCancelorderBody.md)| Process:

1. Partner will call the cancel order function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return successful. | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2003**](../Model/InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

