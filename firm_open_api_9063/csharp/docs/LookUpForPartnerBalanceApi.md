# IO.Swagger.Api.LookUpForPartnerBalanceApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**LookupBalancePost**](LookUpForPartnerBalanceApi.md#lookupbalancepost) | **POST** /LookupBalance | https::devtest.baokim.vn/Sandbox/FirmBanking

<a name="lookupbalancepost"></a>
# **LookupBalancePost**
> InlineResponse2003 LookupBalancePost (LookupBalanceBody body = null)

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
    public class LookupBalancePostExample
    {
        public void main()
        {
            var apiInstance = new LookUpForPartnerBalanceApi();
            var body = new LookupBalanceBody(); // LookupBalanceBody | Process:

1. Partner will call the partner balance searching function, Baokim will check the data format and signature authentication

2. If the information is correct, return the availale balance. (optional) 

            try
            {
                // https::devtest.baokim.vn/Sandbox/FirmBanking
                InlineResponse2003 result = apiInstance.LookupBalancePost(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling LookUpForPartnerBalanceApi.LookupBalancePost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LookupBalanceBody**](LookupBalanceBody.md)| Process:

1. Partner will call the partner balance searching function, Baokim will check the data format and signature authentication

2. If the information is correct, return the availale balance. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
