# CreateTransactionApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1PartnerCreateOrderPost**](CreateTransactionApi.md#apiV1PartnerCreateOrderPost) | **POST** /api/v1/partner/create-order | https::devtest.baokim.vn/api/v1/partner/installment

<a name="apiV1PartnerCreateOrderPost"></a>
# **apiV1PartnerCreateOrderPost**
> InlineResponse2002 apiV1PartnerCreateOrderPost(body)

https::devtest.baokim.vn/api/v1/partner/installment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.CreateTransactionApi;


CreateTransactionApi apiInstance = new CreateTransactionApi();
PartnerCreateorderBody body = new PartnerCreateorderBody(); // PartnerCreateorderBody | Process:

1. MERCHANT sends a request to create transaction to BAOKIM.

2. BAOKIM will check this transaction information with the bank, if the transaction has been paid, BAOKIM will initiate the transaction on the system and transfer the information to ISSUING BANK to perform the installment conversion transaction.
try {
    InlineResponse2002 result = apiInstance.apiV1PartnerCreateOrderPost(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CreateTransactionApi#apiV1PartnerCreateOrderPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartnerCreateorderBody**](PartnerCreateorderBody.md)| Process:

1. MERCHANT sends a request to create transaction to BAOKIM.

2. BAOKIM will check this transaction information with the bank, if the transaction has been paid, BAOKIM will initiate the transaction on the system and transfer the information to ISSUING BANK to perform the installment conversion transaction. | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

