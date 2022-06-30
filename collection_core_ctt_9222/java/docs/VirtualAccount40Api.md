# VirtualAccount40Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**1796c61005edee3976097a607fe9dbaa**](VirtualAccount40Api.md#1796c61005edee3976097a607fe9dbaa) | **POST** /api/Sandbox/Collection/V4/update | Update virtual account
[**8442c69ffbaf4b3677a52fa3ebcef6d4**](VirtualAccount40Api.md#8442c69ffbaf4b3677a52fa3ebcef6d4) | **POST** /api/Sandbox/Collection/V4/create | Create virtual account

<a name="1796c61005edee3976097a607fe9dbaa"></a>
# **1796c61005edee3976097a607fe9dbaa**
> InlineResponse200 1796c61005edee3976097a607fe9dbaa(body, contentType, signature)

Update virtual account

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.VirtualAccount40Api;


VirtualAccount40Api apiInstance = new VirtualAccount40Api();
V4UpdateBody body = new V4UpdateBody(); // V4UpdateBody | 
String contentType = "contentType_example"; // String | 
String signature = "signature_example"; // String | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption
try {
    InlineResponse200 result = apiInstance.1796c61005edee3976097a607fe9dbaa(body, contentType, signature);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling VirtualAccount40Api#1796c61005edee3976097a607fe9dbaa");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V4UpdateBody**](V4UpdateBody.md)|  |
 **contentType** | **String**|  | [optional]
 **signature** | **String**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="8442c69ffbaf4b3677a52fa3ebcef6d4"></a>
# **8442c69ffbaf4b3677a52fa3ebcef6d4**
> InlineResponse200 8442c69ffbaf4b3677a52fa3ebcef6d4(body, contentType, signature)

Create virtual account

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.VirtualAccount40Api;


VirtualAccount40Api apiInstance = new VirtualAccount40Api();
V4CreateBody body = new V4CreateBody(); // V4CreateBody | 
String contentType = "contentType_example"; // String | 
String signature = "signature_example"; // String | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption
try {
    InlineResponse200 result = apiInstance.8442c69ffbaf4b3677a52fa3ebcef6d4(body, contentType, signature);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling VirtualAccount40Api#8442c69ffbaf4b3677a52fa3ebcef6d4");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V4CreateBody**](V4CreateBody.md)|  |
 **contentType** | **String**|  | [optional]
 **signature** | **String**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

