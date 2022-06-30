# swagger_client.CheckInstallmentSupportApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_partner_check_installment_post**](CheckInstallmentSupportApi.md#api_v1_partner_check_installment_post) | **POST** /api/v1/partner/check-installment | https::devtest.baokim.vn/api/v1/partner/installment

# **api_v1_partner_check_installment_post**
> InlineResponse200 api_v1_partner_check_installment_post(body=body)

https::devtest.baokim.vn/api/v1/partner/installment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckInstallmentSupportApi()
body = swagger_client.PartnerCheckinstallmentBody() # PartnerCheckinstallmentBody | Process:

 MERCHANT sends customer's card information such as: card's issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM (optional)

try:
    # https::devtest.baokim.vn/api/v1/partner/installment
    api_response = api_instance.api_v1_partner_check_installment_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckInstallmentSupportApi->api_v1_partner_check_installment_post: %s\n" % e)
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

