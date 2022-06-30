# VirtualAccountApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**6ce3bcd0268f76548ace52ed5eeeefef**](VirtualAccountApi.md#6ce3bcd0268f76548ace52ed5eeeefef) | **POST** /Sandbox/Collection/V2 | create &amp; update va

<a name="6ce3bcd0268f76548ace52ed5eeeefef"></a>
# **6ce3bcd0268f76548ace52ed5eeeefef**
> InlineResponse200 6ce3bcd0268f76548ace52ed5eeeefef(body, contentType, signature)

create &amp; update va

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.VirtualAccountApi;


VirtualAccountApi apiInstance = new VirtualAccountApi();
CollectionV2Body body = new CollectionV2Body(); // CollectionV2Body | 
String contentType = "contentType_example"; // String | 
String signature = "signature_example"; // String | BAOKIM sẽ ký Dữ liệu bằng thuật toán sha1WithRSA và sử dụng mã hóa base64
try {
    InlineResponse200 result = apiInstance.6ce3bcd0268f76548ace52ed5eeeefef(body, contentType, signature);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling VirtualAccountApi#6ce3bcd0268f76548ace52ed5eeeefef");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionV2Body**](CollectionV2Body.md)|  |
 **contentType** | **String**|  | [optional]
 **signature** | **String**| BAOKIM sẽ ký Dữ liệu bằng thuật toán sha1WithRSA và sử dụng mã hóa base64 | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

