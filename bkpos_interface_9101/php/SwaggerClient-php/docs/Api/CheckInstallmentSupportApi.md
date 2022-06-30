# Swagger\Client\CheckInstallmentSupportApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1PartnerCheckInstallmentPost**](CheckInstallmentSupportApi.md#apiv1partnercheckinstallmentpost) | **POST** /api/v1/partner/check-installment | https::devtest.baokim.vn/api/v1/partner/installment

# **apiV1PartnerCheckInstallmentPost**
> \Swagger\Client\Model\InlineResponse200 apiV1PartnerCheckInstallmentPost($body)

https::devtest.baokim.vn/api/v1/partner/installment

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\CheckInstallmentSupportApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\PartnerCheckinstallmentBody(); // \Swagger\Client\Model\PartnerCheckinstallmentBody | Process:

 MERCHANT sends customer's card information such as: card's issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM

try {
    $result = $apiInstance->apiV1PartnerCheckInstallmentPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CheckInstallmentSupportApi->apiV1PartnerCheckInstallmentPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\PartnerCheckinstallmentBody**](../Model/PartnerCheckinstallmentBody.md)| Process:

 MERCHANT sends customer&#x27;s card information such as: card&#x27;s issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse200**](../Model/InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

