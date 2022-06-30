# CheckPartnerLimitApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRetailCheckPartnerLimitPost**](CheckPartnerLimitApi.md#apiRetailCheckPartnerLimitPost) | **POST** /api/retail/check-partner-limit | CHECK PARTNER LIMIT

<a name="apiRetailCheckPartnerLimitPost"></a>
# **apiRetailCheckPartnerLimitPost**
> InlineResponse200 apiRetailCheckPartnerLimitPost(body, contentType, signature)

CHECK PARTNER LIMIT

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.CheckPartnerLimitApi;


CheckPartnerLimitApi apiInstance = new CheckPartnerLimitApi();
RetailCheckpartnerlimitBody body = new RetailCheckpartnerlimitBody(); // RetailCheckpartnerlimitBody | 
String contentType = "contentType_example"; // String | 
String signature = "signature_example"; // String | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption
try {
    InlineResponse200 result = apiInstance.apiRetailCheckPartnerLimitPost(body, contentType, signature);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CheckPartnerLimitApi#apiRetailCheckPartnerLimitPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RetailCheckpartnerlimitBody**](RetailCheckpartnerlimitBody.md)|  |
 **contentType** | **String**|  | [optional]
 **signature** | **String**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

