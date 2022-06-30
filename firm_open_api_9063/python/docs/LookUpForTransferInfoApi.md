# swagger_client.LookUpForTransferInfoApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookup_transfer_post**](LookUpForTransferInfoApi.md#lookup_transfer_post) | **POST** /LookupTransfer | https::devtest.baokim.vn/Sandbox/FirmBanking

# **lookup_transfer_post**
> InlineResponse2002 lookup_transfer_post(body=body)

https::devtest.baokim.vn/Sandbox/FirmBanking

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LookUpForTransferInfoApi()
body = swagger_client.LookupTransferBody() # LookupTransferBody | Process:

1. PARTNER will call the transaction information search function, BAOKIM will check the data format and signature authentication, then will check the transaction code..

2. If the information is correct, return the transaction information.. (optional)

try:
    # https::devtest.baokim.vn/Sandbox/FirmBanking
    api_response = api_instance.lookup_transfer_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookUpForTransferInfoApi->lookup_transfer_post: %s\n" % e)
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

