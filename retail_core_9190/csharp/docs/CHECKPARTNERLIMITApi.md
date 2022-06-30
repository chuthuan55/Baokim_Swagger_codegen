# IO.Swagger.Api.CHECKPARTNERLIMITApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiRetailCheckPartnerLimitPost**](CHECKPARTNERLIMITApi.md#apiretailcheckpartnerlimitpost) | **POST** /api/retail/check-partner-limit | CHECK PARTNER LIMIT

<a name="apiretailcheckpartnerlimitpost"></a>
# **ApiRetailCheckPartnerLimitPost**
> InlineResponse200 ApiRetailCheckPartnerLimitPost (RetailCheckpartnerlimitBody body, string contentType = null, string signature = null)

CHECK PARTNER LIMIT

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiRetailCheckPartnerLimitPostExample
    {
        public void main()
        {
            var apiInstance = new CHECKPARTNERLIMITApi();
            var body = new RetailCheckpartnerlimitBody(); // RetailCheckpartnerlimitBody | 
            var contentType = contentType_example;  // string |  (optional) 
            var signature = signature_example;  // string | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional) 

            try
            {
                // CHECK PARTNER LIMIT
                InlineResponse200 result = apiInstance.ApiRetailCheckPartnerLimitPost(body, contentType, signature);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CHECKPARTNERLIMITApi.ApiRetailCheckPartnerLimitPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RetailCheckpartnerlimitBody**](RetailCheckpartnerlimitBody.md)|  | 
 **contentType** | **string**|  | [optional] 
 **signature** | **string**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
