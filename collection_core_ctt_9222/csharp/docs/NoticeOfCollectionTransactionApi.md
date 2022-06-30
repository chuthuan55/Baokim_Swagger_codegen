# IO.Swagger.Api.NoticeOfCollectionTransactionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**6ce3bcd0268f76548ace52ed5eeeefef**](NoticeOfCollectionTransactionApi.md#6ce3bcd0268f76548ace52ed5eeeefef) | **POST** (api partner provide) | (PARTNER Provide)

<a name="6ce3bcd0268f76548ace52ed5eeeefef"></a>
# **6ce3bcd0268f76548ace52ed5eeeefef**
> InlineResponse2001 6ce3bcd0268f76548ace52ed5eeeefef (Body body, string contentType = null)

(PARTNER Provide)

<p>Process:</p>                 <p>1. PARTNER build the system, to receive data notice the collection transaction.</p>                 <p>2. When receive a new collection transaction, BAOKIM will call to “collection transaction notification” that provided by PARTNER to notice PARTNER need to update data.</p>

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class 6ce3bcd0268f76548ace52ed5eeeefefExample
    {
        public void main()
        {
            var apiInstance = new NoticeOfCollectionTransactionApi();
            var body = new Body(); // Body | 
            var contentType = contentType_example;  // string |  (optional) 

            try
            {
                // (PARTNER Provide)
                InlineResponse2001 result = apiInstance.6ce3bcd0268f76548ace52ed5eeeefef(body, contentType);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling NoticeOfCollectionTransactionApi.6ce3bcd0268f76548ace52ed5eeeefef: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | 
 **contentType** | **string**|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
