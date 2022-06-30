# VerifyCustomerInformationApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verifyPost**](VerifyCustomerInformationApi.md#verifyPost) | **POST** /Verify | https::devtest.baokim.vn/Sandbox/FirmBanking

<a name="verifyPost"></a>
# **verifyPost**
> InlineResponse200 verifyPost(body)

https::devtest.baokim.vn/Sandbox/FirmBanking

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.VerifyCustomerInformationApi;


VerifyCustomerInformationApi apiInstance = new VerifyCustomerInformationApi();
VerifyBody body = new VerifyBody(); // VerifyBody | 1. Partner will call the customer authentication function, Baokim will check the data format and signature authentication..

2. Baokim continues to check customer information and corresponding bank

3. If the information is correct, Baokim will return successful information and corresponding customer name.
try {
    InlineResponse200 result = apiInstance.verifyPost(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling VerifyCustomerInformationApi#verifyPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyBody**](VerifyBody.md)| 1. Partner will call the customer authentication function, Baokim will check the data format and signature authentication..

2. Baokim continues to check customer information and corresponding bank

3. If the information is correct, Baokim will return successful information and corresponding customer name. | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

