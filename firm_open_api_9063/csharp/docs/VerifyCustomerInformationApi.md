# IO.Swagger.Api.VerifyCustomerInformationApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**VerifyPost**](VerifyCustomerInformationApi.md#verifypost) | **POST** /Verify | https::devtest.baokim.vn/Sandbox/FirmBanking

<a name="verifypost"></a>
# **VerifyPost**
> InlineResponse200 VerifyPost (VerifyBody body = null)

https::devtest.baokim.vn/Sandbox/FirmBanking

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class VerifyPostExample
    {
        public void main()
        {
            var apiInstance = new VerifyCustomerInformationApi();
            var body = new VerifyBody(); // VerifyBody | 1. Partner will call the customer authentication function, Baokim will check the data format and signature authentication..

2. Baokim continues to check customer information and corresponding bank

3. If the information is correct, Baokim will return successful information and corresponding customer name. (optional) 

            try
            {
                // https::devtest.baokim.vn/Sandbox/FirmBanking
                InlineResponse200 result = apiInstance.VerifyPost(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling VerifyCustomerInformationApi.VerifyPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyBody**](VerifyBody.md)| 1. Partner will call the customer authentication function, Baokim will check the data format and signature authentication..

2. Baokim continues to check customer information and corresponding bank

3. If the information is correct, Baokim will return successful information and corresponding customer name. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
