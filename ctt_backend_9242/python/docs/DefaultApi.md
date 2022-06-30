# swagger_client.DefaultApi

All URIs are relative to *https://dev-api.baokim.vn/payment/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bpm_list**](DefaultApi.md#bpm_list) | **GET** api/v5/bpm/list | Bank Payment Method List
[**orders_cancel**](DefaultApi.md#orders_cancel) | **POST** /api/v5/order/cancel | Order Cancel
[**orders_detail**](DefaultApi.md#orders_detail) | **GET** /api/v5/order/detail | Order Detail
[**orders_send**](DefaultApi.md#orders_send) | **POST** /api/v5/order/send | Send Order
[**payment_calculate_bank_fee**](DefaultApi.md#payment_calculate_bank_fee) | **POST** api/v5/payment-txn/calculate-bank-fee | Calculate bank payment transaction fee
[**payment_calculate_fee**](DefaultApi.md#payment_calculate_fee) | **POST** api/v5/payment-txn/calculate-bk-fee | Calculating Bao Kim payment transaction fee
[**refund_create**](DefaultApi.md#refund_create) | **POST** api/v5/refund/create | Create Refund
[**tokenization_send_order**](DefaultApi.md#tokenization_send_order) | **POST** /api/v1/tokenization/transaction | Create Token Order

# **bpm_list**
> InlineResponse2003 bpm_list()

Bank Payment Method List

List of payment methods supported by Bao Kim, Web/App merchants can use this API to display payment methods on their application. This list is sorted by field \"type\" ( type = 1 - ATM cards online banks type = 2 - Visa/Master type = 3 - Internet Banking type = 14 - QR code type = 16 - Virtual Account )

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['jwt'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Bank Payment Method List
    api_response = api_instance.bpm_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bpm_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_cancel**
> InlineResponse2002 orders_cancel(body=body)

Order Cancel

Order cancellation API, used in case you do not want to receive payment for orders anymore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['jwt'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrderCancelBody() # OrderCancelBody |  (optional)

try:
    # Order Cancel
    api_response = api_instance.orders_cancel(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->orders_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCancelBody**](OrderCancelBody.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_detail**
> InlineResponse2001 orders_detail(id=id, mrc_order_id=mrc_order_id)

Order Detail

API Get order details, can be used to check order payment status. An order is considered to have been successfully paid when there stat == 'c'(completed). Payment transaction of order status \"stat\" == 1. Order status list ('p' - processing, 'c' - completed, 'd' - destructed)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['jwt'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Order ID [semi-optional] (optional)
mrc_order_id = 'mrc_order_id_example' # str | Merchant Order ID [semi-optional] (optional)

try:
    # Order Detail
    api_response = api_instance.orders_detail(id=id, mrc_order_id=mrc_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->orders_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID [semi-optional] | [optional] 
 **mrc_order_id** | **str**| Merchant Order ID [semi-optional] | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_send**
> InlineResponse200 orders_send(body=body)

Send Order

API Send order information from merchant's application to Bao Kim to make payment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['jwt'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrderSendBody() # OrderSendBody |  (optional)

try:
    # Send Order
    api_response = api_instance.orders_send(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->orders_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderSendBody**](OrderSendBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_calculate_bank_fee**
> InlineResponse2005 payment_calculate_bank_fee(body=body)

Calculate bank payment transaction fee

The API gets Bank's fee info including the amount and the person who pays the fee( fee_payer = 1 - Buyer bear the fee, fee_payer = 2 - Merchant bears the fee ).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['jwt'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.PaymenttxnCalculatebankfeeBody() # PaymenttxnCalculatebankfeeBody |  (optional)

try:
    # Calculate bank payment transaction fee
    api_response = api_instance.payment_calculate_bank_fee(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->payment_calculate_bank_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymenttxnCalculatebankfeeBody**](PaymenttxnCalculatebankfeeBody.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_calculate_fee**
> InlineResponse2004 payment_calculate_fee(body=body)

Calculating Bao Kim payment transaction fee

The API gets Bao Kim's fee info including the amount and the person who pays the fee( fee_payer = 1 - Buyer bear the fee, fee_payer = 2 - Merchant bears the fee ).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['jwt'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.PaymenttxnCalculatebkfeeBody() # PaymenttxnCalculatebkfeeBody |  (optional)

try:
    # Calculating Bao Kim payment transaction fee
    api_response = api_instance.payment_calculate_fee(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->payment_calculate_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymenttxnCalculatebkfeeBody**](PaymenttxnCalculatebkfeeBody.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_create**
> InlineResponse2006 refund_create(body=body)

Create Refund

Create a refund transaction

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['jwt'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.RefundCreateBody() # RefundCreateBody |  (optional)

try:
    # Create Refund
    api_response = api_instance.refund_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->refund_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RefundCreateBody**](RefundCreateBody.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokenization_send_order**
> InlineResponse200 tokenization_send_order(body=body)

Create Token Order

Create a token order

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['jwt'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.TokenizationTransactionBody() # TokenizationTransactionBody |  (optional)

try:
    # Create Token Order
    api_response = api_instance.tokenization_send_order(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tokenization_send_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenizationTransactionBody**](TokenizationTransactionBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

