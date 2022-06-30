# swagger_client.VirtualAccountVersion23Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**6ce3bcd0268f76548ace52ed5eeeefef**](VirtualAccountVersion23Api.md#6ce3bcd0268f76548ace52ed5eeeefef) | **POST** /api/Sandbox/Collection | create &amp; update va

# **6ce3bcd0268f76548ace52ed5eeeefef**
> InlineResponse200 6ce3bcd0268f76548ace52ed5eeeefef(body, content_type=content_type, signature=signature)

create & update va

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VirtualAccountVersion23Api()
body = swagger_client.SandboxCollectionBody() # SandboxCollectionBody | 
content_type = 'content_type_example' # str |  (optional)
signature = 'signature_example' # str | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption. (optional)

try:
    # create & update va
    api_response = api_instance.6ce3bcd0268f76548ace52ed5eeeefef(body, content_type=content_type, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualAccountVersion23Api->6ce3bcd0268f76548ace52ed5eeeefef: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SandboxCollectionBody**](SandboxCollectionBody.md)|  | 
 **content_type** | **str**|  | [optional] 
 **signature** | **str**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

