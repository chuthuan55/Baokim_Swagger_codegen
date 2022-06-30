# IO.Swagger.Api.DefaultApi

All URIs are relative to *https://dev-api.baokim.vn/payment/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BpmList**](DefaultApi.md#bpmlist) | **GET** api/v5/bpm/list | Bank Payment Method List
[**OrdersCancel**](DefaultApi.md#orderscancel) | **POST** /api/v5/order/cancel | Order Cancel
[**OrdersDetail**](DefaultApi.md#ordersdetail) | **GET** /api/v5/order/detail | Order Detail
[**OrdersSend**](DefaultApi.md#orderssend) | **POST** /api/v5/order/send | Send Order
[**PaymentCalculateBankFee**](DefaultApi.md#paymentcalculatebankfee) | **POST** api/v5/payment-txn/calculate-bank-fee | Calculate bank payment transaction fee
[**PaymentCalculateFee**](DefaultApi.md#paymentcalculatefee) | **POST** api/v5/payment-txn/calculate-bk-fee | Calculating Bao Kim payment transaction fee
[**RefundCreate**](DefaultApi.md#refundcreate) | **POST** api/v5/refund/create | Create Refund
[**TokenizationSendOrder**](DefaultApi.md#tokenizationsendorder) | **POST** /api/v1/tokenization/transaction | Create Token Order

<a name="bpmlist"></a>
# **BpmList**
> InlineResponse2003 BpmList ()

Bank Payment Method List

List of payment methods supported by Bao Kim, Web/App merchants can use this API to display payment methods on their application. This list is sorted by field \"type\" ( type = 1 - ATM cards online banks type = 2 - Visa/Master type = 3 - Internet Banking type = 14 - QR code type = 16 - Virtual Account )

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class BpmListExample
    {
        public void main()
        {
            // Configure API key authorization: JWT
            Configuration.Default.AddApiKey("jwt", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("jwt", "Bearer");

            var apiInstance = new DefaultApi();

            try
            {
                // Bank Payment Method List
                InlineResponse2003 result = apiInstance.BpmList();
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.BpmList: " + e.Message );
            }
        }
    }
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="orderscancel"></a>
# **OrdersCancel**
> InlineResponse2002 OrdersCancel (OrderCancelBody body = null)

Order Cancel

Order cancellation API, used in case you do not want to receive payment for orders anymore

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class OrdersCancelExample
    {
        public void main()
        {
            // Configure API key authorization: JWT
            Configuration.Default.AddApiKey("jwt", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("jwt", "Bearer");

            var apiInstance = new DefaultApi();
            var body = new OrderCancelBody(); // OrderCancelBody |  (optional) 

            try
            {
                // Order Cancel
                InlineResponse2002 result = apiInstance.OrdersCancel(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.OrdersCancel: " + e.Message );
            }
        }
    }
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="ordersdetail"></a>
# **OrdersDetail**
> InlineResponse2001 OrdersDetail (int? id = null, string mrcOrderId = null)

Order Detail

API Get order details, can be used to check order payment status. An order is considered to have been successfully paid when there stat == 'c'(completed). Payment transaction of order status \"stat\" == 1. Order status list ('p' - processing, 'c' - completed, 'd' - destructed)

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class OrdersDetailExample
    {
        public void main()
        {
            // Configure API key authorization: JWT
            Configuration.Default.AddApiKey("jwt", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("jwt", "Bearer");

            var apiInstance = new DefaultApi();
            var id = 56;  // int? | Order ID [semi-optional] (optional) 
            var mrcOrderId = mrcOrderId_example;  // string | Merchant Order ID [semi-optional] (optional) 

            try
            {
                // Order Detail
                InlineResponse2001 result = apiInstance.OrdersDetail(id, mrcOrderId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.OrdersDetail: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int?**| Order ID [semi-optional] | [optional] 
 **mrcOrderId** | **string**| Merchant Order ID [semi-optional] | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="orderssend"></a>
# **OrdersSend**
> InlineResponse200 OrdersSend (OrderSendBody body = null)

Send Order

API Send order information from merchant's application to Bao Kim to make payment.

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class OrdersSendExample
    {
        public void main()
        {
            // Configure API key authorization: JWT
            Configuration.Default.AddApiKey("jwt", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("jwt", "Bearer");

            var apiInstance = new DefaultApi();
            var body = new OrderSendBody(); // OrderSendBody |  (optional) 

            try
            {
                // Send Order
                InlineResponse200 result = apiInstance.OrdersSend(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.OrdersSend: " + e.Message );
            }
        }
    }
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="paymentcalculatebankfee"></a>
# **PaymentCalculateBankFee**
> InlineResponse2005 PaymentCalculateBankFee (PaymenttxnCalculatebankfeeBody body = null)

Calculate bank payment transaction fee

The API gets Bank's fee info including the amount and the person who pays the fee( fee_payer = 1 - Buyer bear the fee, fee_payer = 2 - Merchant bears the fee ).

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PaymentCalculateBankFeeExample
    {
        public void main()
        {
            // Configure API key authorization: JWT
            Configuration.Default.AddApiKey("jwt", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("jwt", "Bearer");

            var apiInstance = new DefaultApi();
            var body = new PaymenttxnCalculatebankfeeBody(); // PaymenttxnCalculatebankfeeBody |  (optional) 

            try
            {
                // Calculate bank payment transaction fee
                InlineResponse2005 result = apiInstance.PaymentCalculateBankFee(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PaymentCalculateBankFee: " + e.Message );
            }
        }
    }
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="paymentcalculatefee"></a>
# **PaymentCalculateFee**
> InlineResponse2004 PaymentCalculateFee (PaymenttxnCalculatebkfeeBody body = null)

Calculating Bao Kim payment transaction fee

The API gets Bao Kim's fee info including the amount and the person who pays the fee( fee_payer = 1 - Buyer bear the fee, fee_payer = 2 - Merchant bears the fee ).

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class PaymentCalculateFeeExample
    {
        public void main()
        {
            // Configure API key authorization: JWT
            Configuration.Default.AddApiKey("jwt", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("jwt", "Bearer");

            var apiInstance = new DefaultApi();
            var body = new PaymenttxnCalculatebkfeeBody(); // PaymenttxnCalculatebkfeeBody |  (optional) 

            try
            {
                // Calculating Bao Kim payment transaction fee
                InlineResponse2004 result = apiInstance.PaymentCalculateFee(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.PaymentCalculateFee: " + e.Message );
            }
        }
    }
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="refundcreate"></a>
# **RefundCreate**
> InlineResponse2006 RefundCreate (RefundCreateBody body = null)

Create Refund

Create a refund transaction

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class RefundCreateExample
    {
        public void main()
        {
            // Configure API key authorization: JWT
            Configuration.Default.AddApiKey("jwt", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("jwt", "Bearer");

            var apiInstance = new DefaultApi();
            var body = new RefundCreateBody(); // RefundCreateBody |  (optional) 

            try
            {
                // Create Refund
                InlineResponse2006 result = apiInstance.RefundCreate(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.RefundCreate: " + e.Message );
            }
        }
    }
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="tokenizationsendorder"></a>
# **TokenizationSendOrder**
> InlineResponse200 TokenizationSendOrder (TokenizationTransactionBody body = null)

Create Token Order

Create a token order

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class TokenizationSendOrderExample
    {
        public void main()
        {
            // Configure API key authorization: JWT
            Configuration.Default.AddApiKey("jwt", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("jwt", "Bearer");

            var apiInstance = new DefaultApi();
            var body = new TokenizationTransactionBody(); // TokenizationTransactionBody |  (optional) 

            try
            {
                // Create Token Order
                InlineResponse200 result = apiInstance.TokenizationSendOrder(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.TokenizationSendOrder: " + e.Message );
            }
        }
    }
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
