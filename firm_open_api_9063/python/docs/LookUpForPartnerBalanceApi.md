# swagger_client.LookUpForPartnerBalanceApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookup_balance_post**](LookUpForPartnerBalanceApi.md#lookup_balance_post) | **POST** /LookupBalance | https::devtest.baokim.vn/Sandbox/FirmBanking

# **lookup_balance_post**
> InlineResponse2003 lookup_balance_post(body=body)

https::devtest.baokim.vn/Sandbox/FirmBanking

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookUpForPartnerBalanceApi()
body = swagger_client.LookupBalanceBody() # LookupBalanceBody | Process:

1. Partner will call the partner balance searching function, Baokim will check the data format and signature authentication

2. If the information is correct, return the availale balance. (optional)

try:
    # https::devtest.baokim.vn/Sandbox/FirmBanking
    api_response = api_instance.lookup_balance_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookUpForPartnerBalanceApi->lookup_balance_post: %s\n" % e)
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

