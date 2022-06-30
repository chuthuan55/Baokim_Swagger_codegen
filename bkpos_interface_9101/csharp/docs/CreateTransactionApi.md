# IO.Swagger.Api.CreateTransactionApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV1PartnerCreateOrderPost**](CreateTransactionApi.md#apiv1partnercreateorderpost) | **POST** /api/v1/partner/create-order | https::devtest.baokim.vn/api/v1/partner/installment

<a name="apiv1partnercreateorderpost"></a>
# **ApiV1PartnerCreateOrderPost**
> InlineResponse2002 ApiV1PartnerCreateOrderPost (PartnerCreateorderBody body = null)

https::devtest.baokim.vn/api/v1/partner/installment

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ApiV1PartnerCreateOrderPostExample
    {
        public void main()
        {
            var apiInstance = new CreateTransactionApi();
            var body = new PartnerCreateorderBody(); // PartnerCreateorderBody | Process:

1. MERCHANT sends a request to create transaction to BAOKIM.

2. BAOKIM will check this transaction information with the bank, if the transaction has been paid, BAOKIM will initiate the transaction on the system and transfer the information to ISSUING BANK to perform the installment conversion transaction. (optional) 

            try
            {
                // https::devtest.baokim.vn/api/v1/partner/installment
                InlineResponse2002 result = apiInstance.ApiV1PartnerCreateOrderPost(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CreateTransactionApi.ApiV1PartnerCreateOrderPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartnerCreateorderBody**](PartnerCreateorderBody.md)| Process:

1. MERCHANT sends a request to create transaction to BAOKIM.

2. BAOKIM will check this transaction information with the bank, if the transaction has been paid, BAOKIM will initiate the transaction on the system and transfer the information to ISSUING BANK to perform the installment conversion transaction. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
