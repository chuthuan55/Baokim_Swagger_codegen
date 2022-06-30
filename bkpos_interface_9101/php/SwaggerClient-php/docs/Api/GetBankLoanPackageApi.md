# Swagger\Client\GetBankLoanPackageApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1PartnerGetLoanPost**](GetBankLoanPackageApi.md#apiv1partnergetloanpost) | **POST** /api/v1/partner/get-loan | https::devtest.baokim.vn/api/v1/partner/installment

# **apiV1PartnerGetLoanPost**
> \Swagger\Client\Model\InlineResponse2001 apiV1PartnerGetLoanPost($body)

https::devtest.baokim.vn/api/v1/partner/installment

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\GetBankLoanPackageApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\PartnerGetloanBody(); // \Swagger\Client\Model\PartnerGetloanBody | Process:

1. Partner will call the Get Bank Loan Package function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return the list of banks.

try {
    $result = $apiInstance->apiV1PartnerGetLoanPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GetBankLoanPackageApi->apiV1PartnerGetLoanPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\PartnerGetloanBody**](../Model/PartnerGetloanBody.md)| Process:

1. Partner will call the Get Bank Loan Package function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return the list of banks. | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2001**](../Model/InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

