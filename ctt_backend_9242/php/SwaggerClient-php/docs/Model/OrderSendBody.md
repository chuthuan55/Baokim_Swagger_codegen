# OrderSendBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mrc_order_id** | **string** | Merchant order id | [optional] 
**total_amount** | **int** | Order amount | [optional] 
**description** | **string** | Order description | [optional] 
**url_success** | **string** | URL redirect after payment success | [optional] 
**merchant_id** | **int** | ID of merchant | [optional] 
**url_detail** | **string** | Order detail url (redirected when customer cancels order) | [optional] 
**lang** | **string** | Language (en/vi) | [optional] 
**bpm_id** | **int** | Bank payment method ID | [optional] 
**webhooks** | **string** | url is used to send notification to sales website, chat, ... when the payment order is successful, allows notify to multiple urls, separated by commas | [optional] 
**customer_email** | **string** | Customer&#x27;s email | [optional] 
**customer_phone** | **string** | Customer&#x27;s phone | [optional] 
**customer_name** | **string** | Customer&#x27;s full name | [optional] 
**customer_address** | **string** | Customer&#x27;s address | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

