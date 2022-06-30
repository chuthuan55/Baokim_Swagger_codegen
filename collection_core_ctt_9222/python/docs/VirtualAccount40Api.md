# swagger_client.VirtualAccount40Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**1796c61005edee3976097a607fe9dbaa**](VirtualAccount40Api.md#1796c61005edee3976097a607fe9dbaa) | **POST** /api/Sandbox/Collection/V4/update | Update virtual account
[**8442c69ffbaf4b3677a52fa3ebcef6d4**](VirtualAccount40Api.md#8442c69ffbaf4b3677a52fa3ebcef6d4) | **POST** /api/Sandbox/Collection/V4/create | Create virtual account

# **1796c61005edee3976097a607fe9dbaa**
> InlineResponse200 1796c61005edee3976097a607fe9dbaa(body, content_type=content_type, signature=signature)

Update virtual account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VirtualAccount40Api()
body = swagger_client.V4UpdateBody() # V4UpdateBody | 
content_type = 'content_type_example' # str |  (optional)
signature = 'signature_example' # str | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional)

try:
    # Update virtual account
    api_response = api_instance.1796c61005edee3976097a607fe9dbaa(body, content_type=content_type, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualAccount40Api->1796c61005edee3976097a607fe9dbaa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V4UpdateBody**](V4UpdateBody.md)|  | 
 **content_type** | **str**|  | [optional] 
 **signature** | **str**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **8442c69ffbaf4b3677a52fa3ebcef6d4**
> InlineResponse200 8442c69ffbaf4b3677a52fa3ebcef6d4(body, content_type=content_type, signature=signature)

Create virtual account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VirtualAccount40Api()
body = swagger_client.V4CreateBody() # V4CreateBody | 
content_type = 'content_type_example' # str |  (optional)
signature = 'signature_example' # str | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional)

try:
    # Create virtual account
    api_response = api_instance.8442c69ffbaf4b3677a52fa3ebcef6d4(body, content_type=content_type, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualAccount40Api->8442c69ffbaf4b3677a52fa3ebcef6d4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V4CreateBody**](V4CreateBody.md)|  | 
 **content_type** | **str**|  | [optional] 
 **signature** | **str**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

