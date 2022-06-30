# IO.Swagger.Api.TransferMoneyApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**TransferPost**](TransferMoneyApi.md#transferpost) | **POST** /Transfer | https::devtest.baokim.vn/Sandbox/FirmBanking

<a name="transferpost"></a>
# **TransferPost**
> InlineResponse2001 TransferPost (TransferBody body = null)

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
    public class TransferPostExample
    {
        public void main()
        {
            var apiInstance = new TransferMoneyApi();
            var body = new TransferBody(); // TransferBody | Process:

1. Partner will call the money transfer function, Baokim will check the data format and signature authentication, then will check the customer information, the amount to transfer.

2. If the correct information will return successful transfer. 

 Note(*) : If the transaction is pending, the Partner must wait for the final result from Baokim by calling the <a href='/baokim-firm-open-api-9003'> Function look up for transfer info </a>. (optional) 

            try
            {
                // https::devtest.baokim.vn/Sandbox/FirmBanking
                InlineResponse2001 result = apiInstance.TransferPost(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TransferMoneyApi.TransferPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransferBody**](TransferBody.md)| Process:

1. Partner will call the money transfer function, Baokim will check the data format and signature authentication, then will check the customer information, the amount to transfer.

2. If the correct information will return successful transfer. 

 Note(*) : If the transaction is pending, the Partner must wait for the final result from Baokim by calling the &lt;a href&#x3D;&#x27;/baokim-firm-open-api-9003&#x27;&gt; Function look up for transfer info &lt;/a&gt;. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
