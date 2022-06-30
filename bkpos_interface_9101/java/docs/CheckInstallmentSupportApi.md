# CheckInstallmentSupportApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1PartnerCheckInstallmentPost**](CheckInstallmentSupportApi.md#apiV1PartnerCheckInstallmentPost) | **POST** /api/v1/partner/check-installment | https::devtest.baokim.vn/api/v1/partner/installment

<a name="apiV1PartnerCheckInstallmentPost"></a>
# **apiV1PartnerCheckInstallmentPost**
> InlineResponse200 apiV1PartnerCheckInstallmentPost(body)

https::devtest.baokim.vn/api/v1/partner/installment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.CheckInstallmentSupportApi;


CheckInstallmentSupportApi apiInstance = new CheckInstallmentSupportApi();
PartnerCheckinstallmentBody body = new PartnerCheckinstallmentBody(); // PartnerCheckinstallmentBody | Process:

 MERCHANT sends customer's card information such as: card's issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM
try {
    InlineResponse200 result = apiInstance.apiV1PartnerCheckInstallmentPost(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CheckInstallmentSupportApi#apiV1PartnerCheckInstallmentPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartnerCheckinstallmentBody**](PartnerCheckinstallmentBody.md)| Process:

 MERCHANT sends customer&#x27;s card information such as: card&#x27;s issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

