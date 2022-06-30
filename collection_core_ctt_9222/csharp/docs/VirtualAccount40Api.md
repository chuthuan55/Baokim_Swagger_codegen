# IO.Swagger.Api.VirtualAccount40Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**1796c61005edee3976097a607fe9dbaa**](VirtualAccount40Api.md#1796c61005edee3976097a607fe9dbaa) | **POST** /api/Sandbox/Collection/V4/update | Update virtual account
[**8442c69ffbaf4b3677a52fa3ebcef6d4**](VirtualAccount40Api.md#8442c69ffbaf4b3677a52fa3ebcef6d4) | **POST** /api/Sandbox/Collection/V4/create | Create virtual account

<a name="1796c61005edee3976097a607fe9dbaa"></a>
# **1796c61005edee3976097a607fe9dbaa**
> InlineResponse200 1796c61005edee3976097a607fe9dbaa (V4UpdateBody body, string contentType = null, string signature = null)

Update virtual account

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class 1796c61005edee3976097a607fe9dbaaExample
    {
        public void main()
        {
            var apiInstance = new VirtualAccount40Api();
            var body = new V4UpdateBody(); // V4UpdateBody | 
            var contentType = contentType_example;  // string |  (optional) 
            var signature = signature_example;  // string | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional) 

            try
            {
                // Update virtual account
                InlineResponse200 result = apiInstance.1796c61005edee3976097a607fe9dbaa(body, contentType, signature);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling VirtualAccount40Api.1796c61005edee3976097a607fe9dbaa: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V4UpdateBody**](V4UpdateBody.md)|  | 
 **contentType** | **string**|  | [optional] 
 **signature** | **string**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="8442c69ffbaf4b3677a52fa3ebcef6d4"></a>
# **8442c69ffbaf4b3677a52fa3ebcef6d4**
> InlineResponse200 8442c69ffbaf4b3677a52fa3ebcef6d4 (V4CreateBody body, string contentType = null, string signature = null)

Create virtual account

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class 8442c69ffbaf4b3677a52fa3ebcef6d4Example
    {
        public void main()
        {
            var apiInstance = new VirtualAccount40Api();
            var body = new V4CreateBody(); // V4CreateBody | 
            var contentType = contentType_example;  // string |  (optional) 
            var signature = signature_example;  // string | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional) 

            try
            {
                // Create virtual account
                InlineResponse200 result = apiInstance.8442c69ffbaf4b3677a52fa3ebcef6d4(body, contentType, signature);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling VirtualAccount40Api.8442c69ffbaf4b3677a52fa3ebcef6d4: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V4CreateBody**](V4CreateBody.md)|  | 
 **contentType** | **string**|  | [optional] 
 **signature** | **string**| BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
