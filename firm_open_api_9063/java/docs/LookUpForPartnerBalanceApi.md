# LookUpForPartnerBalanceApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookupBalancePost**](LookUpForPartnerBalanceApi.md#lookupBalancePost) | **POST** /LookupBalance | https::devtest.baokim.vn/Sandbox/FirmBanking

<a name="lookupBalancePost"></a>
# **lookupBalancePost**
> InlineResponse2003 lookupBalancePost(body)

https::devtest.baokim.vn/Sandbox/FirmBanking

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.LookUpForPartnerBalanceApi;


LookUpForPartnerBalanceApi apiInstance = new LookUpForPartnerBalanceApi();
LookupBalanceBody body = new LookupBalanceBody(); // LookupBalanceBody | Process:

1. Partner will call the partner balance searching function, Baokim will check the data format and signature authentication

2. If the information is correct, return the availale balance.
try {
    InlineResponse2003 result = apiInstance.lookupBalancePost(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling LookUpForPartnerBalanceApi#lookupBalancePost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LookupBalanceBody**](LookupBalanceBody.md)| Process:

1. Partner will call the partner balance searching function, Baokim will check the data format and signature authentication

2. If the information is correct, return the availale balance. | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

