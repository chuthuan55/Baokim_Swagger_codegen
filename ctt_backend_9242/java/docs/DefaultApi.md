# DefaultApi

All URIs are relative to *https://dev-api.baokim.vn/payment/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bpmList**](DefaultApi.md#bpmList) | **GET** api/v5/bpm/list | Bank Payment Method List
[**ordersCancel**](DefaultApi.md#ordersCancel) | **POST** /api/v5/order/cancel | Order Cancel
[**ordersDetail**](DefaultApi.md#ordersDetail) | **GET** /api/v5/order/detail | Order Detail
[**ordersSend**](DefaultApi.md#ordersSend) | **POST** /api/v5/order/send | Send Order
[**paymentCalculateBankFee**](DefaultApi.md#paymentCalculateBankFee) | **POST** api/v5/payment-txn/calculate-bank-fee | Calculate bank payment transaction fee
[**paymentCalculateFee**](DefaultApi.md#paymentCalculateFee) | **POST** api/v5/payment-txn/calculate-bk-fee | Calculating Bao Kim payment transaction fee
[**refundCreate**](DefaultApi.md#refundCreate) | **POST** api/v5/refund/create | Create Refund
[**tokenizationSendOrder**](DefaultApi.md#tokenizationSendOrder) | **POST** /api/v1/tokenization/transaction | Create Token Order

<a name="bpmList"></a>
# **bpmList**
> InlineResponse2003 bpmList()

Bank Payment Method List

List of payment methods supported by Bao Kim, Web/App merchants can use this API to display payment methods on their application. This list is sorted by field \&quot;type\&quot; ( type &#x3D; 1 - ATM cards online banks type &#x3D; 2 - Visa/Master type &#x3D; 3 - Internet Banking type &#x3D; 14 - QR code type &#x3D; 16 - Virtual Account )

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: JWT
ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
JWT.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.setApiKeyPrefix("Token");

DefaultApi apiInstance = new DefaultApi();
try {
    InlineResponse2003 result = apiInstance.bpmList();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#bpmList");
    e.printStackTrace();
}
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

<a name="ordersCancel"></a>
# **ordersCancel**
> InlineResponse2002 ordersCancel(body)

Order Cancel

Order cancellation API, used in case you do not want to receive payment for orders anymore

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: JWT
ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
JWT.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.setApiKeyPrefix("Token");

DefaultApi apiInstance = new DefaultApi();
OrderCancelBody body = new OrderCancelBody(); // OrderCancelBody | 
try {
    InlineResponse2002 result = apiInstance.ordersCancel(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#ordersCancel");
    e.printStackTrace();
}
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

<a name="ordersDetail"></a>
# **ordersDetail**
> InlineResponse2001 ordersDetail(id, mrcOrderId)

Order Detail

API Get order details, can be used to check order payment status. An order is considered to have been successfully paid when there stat &#x3D;&#x3D; &#x27;c&#x27;(completed). Payment transaction of order status \&quot;stat\&quot; &#x3D;&#x3D; 1. Order status list (&#x27;p&#x27; - processing, &#x27;c&#x27; - completed, &#x27;d&#x27; - destructed)

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: JWT
ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
JWT.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.setApiKeyPrefix("Token");

DefaultApi apiInstance = new DefaultApi();
Integer id = 56; // Integer | Order ID [semi-optional]
String mrcOrderId = "mrcOrderId_example"; // String | Merchant Order ID [semi-optional]
try {
    InlineResponse2001 result = apiInstance.ordersDetail(id, mrcOrderId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#ordersDetail");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| Order ID [semi-optional] | [optional]
 **mrcOrderId** | **String**| Merchant Order ID [semi-optional] | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="ordersSend"></a>
# **ordersSend**
> InlineResponse200 ordersSend(body)

Send Order

API Send order information from merchant&#x27;s application to Bao Kim to make payment.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: JWT
ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
JWT.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.setApiKeyPrefix("Token");

DefaultApi apiInstance = new DefaultApi();
OrderSendBody body = new OrderSendBody(); // OrderSendBody | 
try {
    InlineResponse200 result = apiInstance.ordersSend(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#ordersSend");
    e.printStackTrace();
}
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

<a name="paymentCalculateBankFee"></a>
# **paymentCalculateBankFee**
> InlineResponse2005 paymentCalculateBankFee(body)

Calculate bank payment transaction fee

The API gets Bank&#x27;s fee info including the amount and the person who pays the fee( fee_payer &#x3D; 1 - Buyer bear the fee, fee_payer &#x3D; 2 - Merchant bears the fee ).

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: JWT
ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
JWT.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.setApiKeyPrefix("Token");

DefaultApi apiInstance = new DefaultApi();
PaymenttxnCalculatebankfeeBody body = new PaymenttxnCalculatebankfeeBody(); // PaymenttxnCalculatebankfeeBody | 
try {
    InlineResponse2005 result = apiInstance.paymentCalculateBankFee(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#paymentCalculateBankFee");
    e.printStackTrace();
}
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

<a name="paymentCalculateFee"></a>
# **paymentCalculateFee**
> InlineResponse2004 paymentCalculateFee(body)

Calculating Bao Kim payment transaction fee

The API gets Bao Kim&#x27;s fee info including the amount and the person who pays the fee( fee_payer &#x3D; 1 - Buyer bear the fee, fee_payer &#x3D; 2 - Merchant bears the fee ).

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: JWT
ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
JWT.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.setApiKeyPrefix("Token");

DefaultApi apiInstance = new DefaultApi();
PaymenttxnCalculatebkfeeBody body = new PaymenttxnCalculatebkfeeBody(); // PaymenttxnCalculatebkfeeBody | 
try {
    InlineResponse2004 result = apiInstance.paymentCalculateFee(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#paymentCalculateFee");
    e.printStackTrace();
}
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

<a name="refundCreate"></a>
# **refundCreate**
> InlineResponse2006 refundCreate(body)

Create Refund

Create a refund transaction

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: JWT
ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
JWT.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.setApiKeyPrefix("Token");

DefaultApi apiInstance = new DefaultApi();
RefundCreateBody body = new RefundCreateBody(); // RefundCreateBody | 
try {
    InlineResponse2006 result = apiInstance.refundCreate(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#refundCreate");
    e.printStackTrace();
}
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

<a name="tokenizationSendOrder"></a>
# **tokenizationSendOrder**
> InlineResponse200 tokenizationSendOrder(body)

Create Token Order

Create a token order

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: JWT
ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
JWT.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.setApiKeyPrefix("Token");

DefaultApi apiInstance = new DefaultApi();
TokenizationTransactionBody body = new TokenizationTransactionBody(); // TokenizationTransactionBody | 
try {
    InlineResponse200 result = apiInstance.tokenizationSendOrder(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#tokenizationSendOrder");
    e.printStackTrace();
}
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

