# LookUpForTransferInfoApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookupTransferPost**](LookUpForTransferInfoApi.md#lookupTransferPost) | **POST** /LookupTransfer | https::devtest.baokim.vn/Sandbox/FirmBanking

<a name="lookupTransferPost"></a>
# **lookupTransferPost**
> InlineResponse2002 lookupTransferPost(body)

https::devtest.baokim.vn/Sandbox/FirmBanking

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.LookUpForTransferInfoApi;


LookUpForTransferInfoApi apiInstance = new LookUpForTransferInfoApi();
LookupTransferBody body = new LookupTransferBody(); // LookupTransferBody | Process:

1. PARTNER will call the transaction information search function, BAOKIM will check the data format and signature authentication, then will check the transaction code..

2. If the information is correct, return the transaction information..
try {
    InlineResponse2002 result = apiInstance.lookupTransferPost(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling LookUpForTransferInfoApi#lookupTransferPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LookupTransferBody**](LookupTransferBody.md)| Process:

1. PARTNER will call the transaction information search function, BAOKIM will check the data format and signature authentication, then will check the transaction code..

2. If the information is correct, return the transaction information.. | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

