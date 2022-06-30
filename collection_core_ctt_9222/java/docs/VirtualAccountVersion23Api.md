# VirtualAccountVersion23Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**6ce3bcd0268f76548ace52ed5eeeefef**](VirtualAccountVersion23Api.md#6ce3bcd0268f76548ace52ed5eeeefef) | **POST** /api/Sandbox/Collection | create &amp; update va

<a name="6ce3bcd0268f76548ace52ed5eeeefef"></a>
# **6ce3bcd0268f76548ace52ed5eeeefef**
> InlineResponse200 6ce3bcd0268f76548ace52ed5eeeefef(body, contentType, signature)

create &amp; update va

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.VirtualAccountVersion23Api;


VirtualAccountVersion23Api apiInstance = new VirtualAccountVersion23Api();
SandboxCollectionBody body = new SandboxCollectionBody(); // SandboxCollectionBody | 
String contentType = "contentType_example"; // String | 
String signature = "signature_example"; // String | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption.
try {
    InlineResponse200 result = apiInstance.6ce3bcd0268f76548ace52ed5eeeefef(body, contentType, signature);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling VirtualAccountVersion23Api#6ce3bcd0268f76548ace52ed5eeeefef");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SandboxCollectionBody**](SandboxCollectionBody.md)|  |
 **contentType** | **String**|  | [optional]
 **signature** | **String**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption. | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

