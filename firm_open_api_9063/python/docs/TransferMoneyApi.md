# swagger_client.TransferMoneyApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfer_post**](TransferMoneyApi.md#transfer_post) | **POST** /Transfer | https::devtest.baokim.vn/Sandbox/FirmBanking

# **transfer_post**
> InlineResponse2001 transfer_post(body=body)

https::devtest.baokim.vn/Sandbox/FirmBanking

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransferMoneyApi()
body = swagger_client.TransferBody() # TransferBody | Process:

1. Partner will call the money transfer function, Baokim will check the data format and signature authentication, then will check the customer information, the amount to transfer.

2. If the correct information will return successful transfer. 

 Note(*) : If the transaction is pending, the Partner must wait for the final result from Baokim by calling the <a href='/baokim-firm-open-api-9003'> Function look up for transfer info </a>. (optional)

try:
    # https::devtest.baokim.vn/Sandbox/FirmBanking
    api_response = api_instance.transfer_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferMoneyApi->transfer_post: %s\n" % e)
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

