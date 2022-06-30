# swagger_client.CHECKPARTNERLIMITApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_retail_check_partner_limit_post**](CHECKPARTNERLIMITApi.md#api_retail_check_partner_limit_post) | **POST** /api/retail/check-partner-limit | CHECK PARTNER LIMIT

# **api_retail_check_partner_limit_post**
> InlineResponse200 api_retail_check_partner_limit_post(body, content_type=content_type, signature=signature)

CHECK PARTNER LIMIT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CHECKPARTNERLIMITApi()
body = swagger_client.RetailCheckpartnerlimitBody() # RetailCheckpartnerlimitBody | 
content_type = 'content_type_example' # str |  (optional)
signature = 'signature_example' # str | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional)

try:
    # CHECK PARTNER LIMIT
    api_response = api_instance.api_retail_check_partner_limit_post(body, content_type=content_type, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CHECKPARTNERLIMITApi->api_retail_check_partner_limit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RetailCheckpartnerlimitBody**](RetailCheckpartnerlimitBody.md)|  | 
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

