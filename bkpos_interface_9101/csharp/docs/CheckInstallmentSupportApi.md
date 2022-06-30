# IO.Swagger.Api.CheckInstallmentSupportApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV1PartnerCheckInstallmentPost**](CheckInstallmentSupportApi.md#apiv1partnercheckinstallmentpost) | **POST** /api/v1/partner/check-installment | https::devtest.baokim.vn/api/v1/partner/installment

<a name="apiv1partnercheckinstallmentpost"></a>
# **ApiV1PartnerCheckInstallmentPost**
> InlineResponse200 ApiV1PartnerCheckInstallmentPost (PartnerCheckinstallmentBody body = null)

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
    public class ApiV1PartnerCheckInstallmentPostExample
    {
        public void main()
        {
            var apiInstance = new CheckInstallmentSupportApi();
            var body = new PartnerCheckinstallmentBody(); // PartnerCheckinstallmentBody | Process:

 MERCHANT sends customer's card information such as: card's issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM (optional) 

            try
            {
                // https::devtest.baokim.vn/api/v1/partner/installment
                InlineResponse200 result = apiInstance.ApiV1PartnerCheckInstallmentPost(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CheckInstallmentSupportApi.ApiV1PartnerCheckInstallmentPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartnerCheckinstallmentBody**](PartnerCheckinstallmentBody.md)| Process:

 MERCHANT sends customer&#x27;s card information such as: card&#x27;s issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
