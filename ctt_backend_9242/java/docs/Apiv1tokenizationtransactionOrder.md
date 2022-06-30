# Apiv1tokenizationtransactionOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mrcOrderId** | **String** | Merchant Order ID |  [optional]
**totalAmount** | **Integer** | Order amount (Not required if api_operation &#x3D; PAY and init_token &#x3D; 1) |  [optional]
**description** | **String** | Order description |  [optional]
**urlSuccess** | **String** | URL redirect when payment success |  [optional]
**urlDetail** | **String** | URL redirect when payment failed or canceled |  [optional]
**webhooks** | **String** | URL is used to send notification to sales website, chat, ... when the payment order is successful, allows notify to multiple urls, separated by commas |  [optional]
**customerEmail** | **String** | Customer&#x27;s email |  [optional]
**customerPhone** | **String** | Customer&#x27;s Phone |  [optional]
