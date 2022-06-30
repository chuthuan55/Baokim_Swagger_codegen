# IO.Swagger.Api.LookUpForTransferInfoApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**LookupTransferPost**](LookUpForTransferInfoApi.md#lookuptransferpost) | **POST** /LookupTransfer | https::devtest.baokim.vn/Sandbox/FirmBanking

<a name="lookuptransferpost"></a>
# **LookupTransferPost**
> InlineResponse2002 LookupTransferPost (LookupTransferBody body = null)

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
    public class LookupTransferPostExample
    {
        public void main()
        {
            var apiInstance = new LookUpForTransferInfoApi();
            var body = new LookupTransferBody(); // LookupTransferBody | Process:

1. PARTNER will call the transaction information search function, BAOKIM will check the data format and signature authentication, then will check the transaction code..

2. If the information is correct, return the transaction information.. (optional) 

            try
            {
                // https::devtest.baokim.vn/Sandbox/FirmBanking
                InlineResponse2002 result = apiInstance.LookupTransferPost(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling LookUpForTransferInfoApi.LookupTransferPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LookupTransferBody**](LookupTransferBody.md)| Process:

1. PARTNER will call the transaction information search function, BAOKIM will check the data format and signature authentication, then will check the transaction code..

2. If the information is correct, return the transaction information.. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
