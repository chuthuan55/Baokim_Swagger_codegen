# GetBankLoanPackageApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1PartnerGetLoanPost**](GetBankLoanPackageApi.md#apiV1PartnerGetLoanPost) | **POST** /api/v1/partner/get-loan | https::devtest.baokim.vn/api/v1/partner/installment

<a name="apiV1PartnerGetLoanPost"></a>
# **apiV1PartnerGetLoanPost**
> InlineResponse2001 apiV1PartnerGetLoanPost(body)

https::devtest.baokim.vn/api/v1/partner/installment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.GetBankLoanPackageApi;


GetBankLoanPackageApi apiInstance = new GetBankLoanPackageApi();
PartnerGetloanBody body = new PartnerGetloanBody(); // PartnerGetloanBody | Process:

1. Partner will call the Get Bank Loan Package function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return the list of banks.
try {
    InlineResponse2001 result = apiInstance.apiV1PartnerGetLoanPost(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling GetBankLoanPackageApi#apiV1PartnerGetLoanPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartnerGetloanBody**](PartnerGetloanBody.md)| Process:

1. Partner will call the Get Bank Loan Package function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return the list of banks. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

