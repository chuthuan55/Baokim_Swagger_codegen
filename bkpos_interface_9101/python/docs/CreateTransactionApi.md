# swagger_client.CreateTransactionApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_partner_create_order_post**](CreateTransactionApi.md#api_v1_partner_create_order_post) | **POST** /api/v1/partner/create-order | https::devtest.baokim.vn/api/v1/partner/installment

# **api_v1_partner_create_order_post**
> InlineResponse2002 api_v1_partner_create_order_post(body=body)

https::devtest.baokim.vn/api/v1/partner/installment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateTransactionApi()
body = swagger_client.PartnerCreateorderBody() # PartnerCreateorderBody | Process:

1. MERCHANT sends a request to create transaction to BAOKIM.

2. BAOKIM will check this transaction information with the bank, if the transaction has been paid, BAOKIM will initiate the transaction on the system and transfer the information to ISSUING BANK to perform the installment conversion transaction. (optional)

try:
    # https::devtest.baokim.vn/api/v1/partner/installment
    api_response = api_instance.api_v1_partner_create_order_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateTransactionApi->api_v1_partner_create_order_post: %s\n" % e)
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

