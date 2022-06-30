# Swagger\Client\CreateTransactionApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1PartnerCreateOrderPost**](CreateTransactionApi.md#apiv1partnercreateorderpost) | **POST** /api/v1/partner/create-order | https::devtest.baokim.vn/api/v1/partner/installment

# **apiV1PartnerCreateOrderPost**
> \Swagger\Client\Model\InlineResponse2002 apiV1PartnerCreateOrderPost($body)

https::devtest.baokim.vn/api/v1/partner/installment

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\CreateTransactionApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\PartnerCreateorderBody(); // \Swagger\Client\Model\PartnerCreateorderBody | Process:

1. MERCHANT sends a request to create transaction to BAOKIM.

2. BAOKIM will check this transaction information with the bank, if the transaction has been paid, BAOKIM will initiate the transaction on the system and transfer the information to ISSUING BANK to perform the installment conversion transaction.

try {
    $result = $apiInstance->apiV1PartnerCreateOrderPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreateTransactionApi->apiV1PartnerCreateOrderPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\PartnerCreateorderBody**](../Model/PartnerCreateorderBody.md)| Process:

1. MERCHANT sends a request to create transaction to BAOKIM.

2. BAOKIM will check this transaction information with the bank, if the transaction has been paid, BAOKIM will initiate the transaction on the system and transfer the information to ISSUING BANK to perform the installment conversion transaction. | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2002**](../Model/InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

