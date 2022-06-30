# OrderSendBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mrcOrderId** | **String** | Merchant order id |  [optional]
**totalAmount** | **Integer** | Order amount |  [optional]
**description** | **String** | Order description |  [optional]
**urlSuccess** | **String** | URL redirect after payment success |  [optional]
**merchantId** | **Integer** | ID of merchant |  [optional]
**urlDetail** | **String** | Order detail url (redirected when customer cancels order) |  [optional]
**lang** | **String** | Language (en/vi) |  [optional]
**bpmId** | **Integer** | Bank payment method ID |  [optional]
**webhooks** | **String** | url is used to send notification to sales website, chat, ... when the payment order is successful, allows notify to multiple urls, separated by commas |  [optional]
**customerEmail** | **String** | Customer&#x27;s email |  [optional]
**customerPhone** | **String** | Customer&#x27;s phone |  [optional]
**customerName** | **String** | Customer&#x27;s full name |  [optional]
**customerAddress** | **String** | Customer&#x27;s address |  [optional]
