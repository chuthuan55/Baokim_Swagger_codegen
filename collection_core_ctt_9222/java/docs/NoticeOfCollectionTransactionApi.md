# NoticeOfCollectionTransactionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**6ce3bcd0268f76548ace52ed5eeeefef**](NoticeOfCollectionTransactionApi.md#6ce3bcd0268f76548ace52ed5eeeefef) | **POST** (api partner provide) | (PARTNER Provide)

<a name="6ce3bcd0268f76548ace52ed5eeeefef"></a>
# **6ce3bcd0268f76548ace52ed5eeeefef**
> InlineResponse2001 6ce3bcd0268f76548ace52ed5eeeefef(body, contentType)

(PARTNER Provide)

&lt;p&gt;Process:&lt;/p&gt;                 &lt;p&gt;1. PARTNER build the system, to receive data notice the collection transaction.&lt;/p&gt;                 &lt;p&gt;2. When receive a new collection transaction, BAOKIM will call to “collection transaction notification” that provided by PARTNER to notice PARTNER need to update data.&lt;/p&gt;

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.NoticeOfCollectionTransactionApi;


NoticeOfCollectionTransactionApi apiInstance = new NoticeOfCollectionTransactionApi();
Body body = new Body(); // Body | 
String contentType = "contentType_example"; // String | 
try {
    InlineResponse2001 result = apiInstance.6ce3bcd0268f76548ace52ed5eeeefef(body, contentType);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling NoticeOfCollectionTransactionApi#6ce3bcd0268f76548ace52ed5eeeefef");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  |
 **contentType** | **String**|  | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

