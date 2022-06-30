# swagger_client.GetBankLoanPackageApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_partner_get_loan_post**](GetBankLoanPackageApi.md#api_v1_partner_get_loan_post) | **POST** /api/v1/partner/get-loan | https::devtest.baokim.vn/api/v1/partner/installment

# **api_v1_partner_get_loan_post**
> InlineResponse2001 api_v1_partner_get_loan_post(body=body)

https::devtest.baokim.vn/api/v1/partner/installment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetBankLoanPackageApi()
body = swagger_client.PartnerGetloanBody() # PartnerGetloanBody | Process:

1. Partner will call the Get Bank Loan Package function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return the list of banks. (optional)

try:
    # https::devtest.baokim.vn/api/v1/partner/installment
    api_response = api_instance.api_v1_partner_get_loan_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetBankLoanPackageApi->api_v1_partner_get_loan_post: %s\n" % e)
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

