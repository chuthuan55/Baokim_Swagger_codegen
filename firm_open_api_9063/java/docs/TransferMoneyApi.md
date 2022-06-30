# TransferMoneyApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transferPost**](TransferMoneyApi.md#transferPost) | **POST** /Transfer | https::devtest.baokim.vn/Sandbox/FirmBanking

<a name="transferPost"></a>
# **transferPost**
> InlineResponse2001 transferPost(body)

https::devtest.baokim.vn/Sandbox/FirmBanking

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.TransferMoneyApi;


TransferMoneyApi apiInstance = new TransferMoneyApi();
TransferBody body = new TransferBody(); // TransferBody | Process:

1. Partner will call the money transfer function, Baokim will check the data format and signature authentication, then will check the customer information, the amount to transfer.

2. If the correct information will return successful transfer. 

 Note(*) : If the transaction is pending, the Partner must wait for the final result from Baokim by calling the <a href='/baokim-firm-open-api-9003'> Function look up for transfer info </a>.
try {
    InlineResponse2001 result = apiInstance.transferPost(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TransferMoneyApi#transferPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransferBody**](TransferBody.md)| Process:

1. Partner will call the money transfer function, Baokim will check the data format and signature authentication, then will check the customer information, the amount to transfer.

2. If the correct information will return successful transfer. 

 Note(*) : If the transaction is pending, the Partner must wait for the final result from Baokim by calling the &lt;a href&#x3D;&#x27;/baokim-firm-open-api-9003&#x27;&gt; Function look up for transfer info &lt;/a&gt;. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

