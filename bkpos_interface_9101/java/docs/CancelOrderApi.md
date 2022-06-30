# CancelOrderApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1PartnerCancelOrderPost**](CancelOrderApi.md#apiV1PartnerCancelOrderPost) | **POST** /api/v1/partner/cancel-order | https::devtest.baokim.vn/api/v1/partner/installment

<a name="apiV1PartnerCancelOrderPost"></a>
# **apiV1PartnerCancelOrderPost**
> InlineResponse2003 apiV1PartnerCancelOrderPost(body)

https::devtest.baokim.vn/api/v1/partner/installment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.CancelOrderApi;


CancelOrderApi apiInstance = new CancelOrderApi();
PartnerCancelorderBody body = new PartnerCancelorderBody(); // PartnerCancelorderBody | Process:

1. Partner will call the cancel order function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return successful.
try {
    InlineResponse2003 result = apiInstance.apiV1PartnerCancelOrderPost(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CancelOrderApi#apiV1PartnerCancelOrderPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartnerCancelorderBody**](PartnerCancelorderBody.md)| Process:

1. Partner will call the cancel order function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return successful. | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

