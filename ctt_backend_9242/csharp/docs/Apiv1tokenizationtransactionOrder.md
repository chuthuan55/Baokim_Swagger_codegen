# IO.Swagger.Model.Apiv1tokenizationtransactionOrder
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MrcOrderId** | **string** | Merchant Order ID | [optional] 
**TotalAmount** | **int?** | Order amount (Not required if api_operation &#x3D; PAY and init_token &#x3D; 1) | [optional] 
**Description** | **string** | Order description | [optional] 
**UrlSuccess** | **string** | URL redirect when payment success | [optional] 
**UrlDetail** | **string** | URL redirect when payment failed or canceled | [optional] 
**Webhooks** | **string** | URL is used to send notification to sales website, chat, ... when the payment order is successful, allows notify to multiple urls, separated by commas | [optional] 
**CustomerEmail** | **string** | Customer&#x27;s email | [optional] 
**CustomerPhone** | **string** | Customer&#x27;s Phone | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

