# swagger_client.VerifyCustomerInformationApi

All URIs are relative to *https://https://devtest.baokim.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_post**](VerifyCustomerInformationApi.md#verify_post) | **POST** /Verify | https::devtest.baokim.vn/Sandbox/FirmBanking

# **verify_post**
> InlineResponse200 verify_post(body=body)

https::devtest.baokim.vn/Sandbox/FirmBanking

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifyCustomerInformationApi()
body = swagger_client.VerifyBody() # VerifyBody | 1. Partner will call the customer authentication function, Baokim will check the data format and signature authentication..

2. Baokim continues to check customer information and corresponding bank

3. If the information is correct, Baokim will return successful information and corresponding customer name. (optional)

try:
    # https::devtest.baokim.vn/Sandbox/FirmBanking
    api_response = api_instance.verify_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerifyCustomerInformationApi->verify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyBody**](VerifyBody.md)| 1. Partner will call the customer authentication function, Baokim will check the data format and signature authentication..

2. Baokim continues to check customer information and corresponding bank

3. If the information is correct, Baokim will return successful information and corresponding customer name. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

