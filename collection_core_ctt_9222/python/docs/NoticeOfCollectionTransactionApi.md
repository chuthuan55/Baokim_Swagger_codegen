# swagger_client.NoticeOfCollectionTransactionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**6ce3bcd0268f76548ace52ed5eeeefef**](NoticeOfCollectionTransactionApi.md#6ce3bcd0268f76548ace52ed5eeeefef) | **POST** (api partner provide) | (PARTNER Provide)

# **6ce3bcd0268f76548ace52ed5eeeefef**
> InlineResponse2001 6ce3bcd0268f76548ace52ed5eeeefef(body, content_type=content_type)

(PARTNER Provide)

<p>Process:</p>                 <p>1. PARTNER build the system, to receive data notice the collection transaction.</p>                 <p>2. When receive a new collection transaction, BAOKIM will call to “collection transaction notification” that provided by PARTNER to notice PARTNER need to update data.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NoticeOfCollectionTransactionApi()
body = swagger_client.Body() # Body | 
content_type = 'content_type_example' # str |  (optional)

try:
    # (PARTNER Provide)
    api_response = api_instance.6ce3bcd0268f76548ace52ed5eeeefef(body, content_type=content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoticeOfCollectionTransactionApi->6ce3bcd0268f76548ace52ed5eeeefef: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | 
 **content_type** | **str**|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

