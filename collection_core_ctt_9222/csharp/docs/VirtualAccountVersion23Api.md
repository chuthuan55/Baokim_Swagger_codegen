# IO.Swagger.Api.VirtualAccountVersion23Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**6ce3bcd0268f76548ace52ed5eeeefef**](VirtualAccountVersion23Api.md#6ce3bcd0268f76548ace52ed5eeeefef) | **POST** /api/Sandbox/Collection | create &amp; update va

<a name="6ce3bcd0268f76548ace52ed5eeeefef"></a>
# **6ce3bcd0268f76548ace52ed5eeeefef**
> InlineResponse200 6ce3bcd0268f76548ace52ed5eeeefef (SandboxCollectionBody body, string contentType = null, string signature = null)

create & update va

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
            var apiInstance = new VirtualAccountVersion23Api();
            var body = new SandboxCollectionBody(); // SandboxCollectionBody | 
            var contentType = contentType_example;  // string |  (optional) 
            var signature = signature_example;  // string | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption. (optional) 

            try
            {
                // create & update va
                InlineResponse200 result = apiInstance.6ce3bcd0268f76548ace52ed5eeeefef(body, contentType, signature);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling VirtualAccountVersion23Api.6ce3bcd0268f76548ace52ed5eeeefef: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SandboxCollectionBody**](SandboxCollectionBody.md)|  | 
 **contentType** | **string**|  | [optional] 
 **signature** | **string**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
