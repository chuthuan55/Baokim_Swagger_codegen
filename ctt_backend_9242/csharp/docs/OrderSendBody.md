# IO.Swagger.Model.OrderSendBody
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MrcOrderId** | **string** | Merchant order id | [optional] 
**TotalAmount** | **int?** | Order amount | [optional] 
**Description** | **string** | Order description | [optional] 
**UrlSuccess** | **string** | URL redirect after payment success | [optional] 
**MerchantId** | **int?** | ID of merchant | [optional] 
**UrlDetail** | **string** | Order detail url (redirected when customer cancels order) | [optional] 
**Lang** | **string** | Language (en/vi) | [optional] 
**BpmId** | **int?** | Bank payment method ID | [optional] 
**Webhooks** | **string** | url is used to send notification to sales website, chat, ... when the payment order is successful, allows notify to multiple urls, separated by commas | [optional] 
**CustomerEmail** | **string** | Customer&#x27;s email | [optional] 
**CustomerPhone** | **string** | Customer&#x27;s phone | [optional] 
**CustomerName** | **string** | Customer&#x27;s full name | [optional] 
**CustomerAddress** | **string** | Customer&#x27;s address | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

