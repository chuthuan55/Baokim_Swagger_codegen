# Swagger\Client\NoticeOfCollectionTransactionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**6ce3bcd0268f76548ace52ed5eeeefef**](NoticeOfCollectionTransactionApi.md#6ce3bcd0268f76548ace52ed5eeeefef) | **POST** (api partner provide) | (PARTNER Provide)

# **6ce3bcd0268f76548ace52ed5eeeefef**
> \Swagger\Client\Model\InlineResponse2001 6ce3bcd0268f76548ace52ed5eeeefef($body, $content_type)

(PARTNER Provide)

<p>Process:</p>                 <p>1. PARTNER build the system, to receive data notice the collection transaction.</p>                 <p>2. When receive a new collection transaction, BAOKIM will call to “collection transaction notification” that provided by PARTNER to notice PARTNER need to update data.</p>

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\NoticeOfCollectionTransactionApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\Body(); // \Swagger\Client\Model\Body | 
$content_type = "content_type_example"; // string | 

try {
    $result = $apiInstance->6ce3bcd0268f76548ace52ed5eeeefef($body, $content_type);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NoticeOfCollectionTransactionApi->6ce3bcd0268f76548ace52ed5eeeefef: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\Body**](../Model/Body.md)|  |
 **content_type** | **string**|  | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2001**](../Model/InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

