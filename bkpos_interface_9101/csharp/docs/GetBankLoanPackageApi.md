# IO.Swagger.Api.GetBankLoanPackageApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ApiV1PartnerGetLoanPost**](GetBankLoanPackageApi.md#apiv1partnergetloanpost) | **POST** /api/v1/partner/get-loan | https::devtest.baokim.vn/api/v1/partner/installment

<a name="apiv1partnergetloanpost"></a>
# **ApiV1PartnerGetLoanPost**
> InlineResponse2001 ApiV1PartnerGetLoanPost (PartnerGetloanBody body = null)

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
    public class ApiV1PartnerGetLoanPostExample
    {
        public void main()
        {
            var apiInstance = new GetBankLoanPackageApi();
            var body = new PartnerGetloanBody(); // PartnerGetloanBody | Process:

1. Partner will call the Get Bank Loan Package function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return the list of banks. (optional) 

            try
            {
                // https::devtest.baokim.vn/api/v1/partner/installment
                InlineResponse2001 result = apiInstance.ApiV1PartnerGetLoanPost(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling GetBankLoanPackageApi.ApiV1PartnerGetLoanPost: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartnerGetloanBody**](PartnerGetloanBody.md)| Process:

1. Partner will call the Get Bank Loan Package function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return the list of banks. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
