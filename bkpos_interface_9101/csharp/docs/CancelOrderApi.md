# IO.Swagger.Api.CancelOrderApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV1PartnerCancelOrderPost**](CancelOrderApi.md#apiv1partnercancelorderpost) | **POST** /api/v1/partner/cancel-order | https::devtest.baokim.vn/api/v1/partner/installment

<a name="apiv1partnercancelorderpost"></a>
# **ApiV1PartnerCancelOrderPost**
> InlineResponse2003 ApiV1PartnerCancelOrderPost (PartnerCancelorderBody body = null)

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
    public class ApiV1PartnerCancelOrderPostExample
    {
        public void main()
        {
            var apiInstance = new CancelOrderApi();
            var body = new PartnerCancelorderBody(); // PartnerCancelorderBody | Process:

1. Partner will call the cancel order function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return successful. (optional) 

            try
            {
                // https::devtest.baokim.vn/api/v1/partner/installment
                InlineResponse2003 result = apiInstance.ApiV1PartnerCancelOrderPost(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CancelOrderApi.ApiV1PartnerCancelOrderPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartnerCancelorderBody**](PartnerCancelorderBody.md)| Process:

1. Partner will call the cancel order function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return successful. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
