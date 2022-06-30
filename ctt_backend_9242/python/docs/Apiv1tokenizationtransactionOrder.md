# Apiv1tokenizationtransactionOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mrc_order_id** | **str** | Merchant Order ID | [optional] 
**total_amount** | **int** | Order amount (Not required if api_operation &#x3D; PAY and init_token &#x3D; 1) | [optional] 
**description** | **str** | Order description | [optional] 
**url_success** | **str** | URL redirect when payment success | [optional] 
**url_detail** | **str** | URL redirect when payment failed or canceled | [optional] 
**webhooks** | **str** | URL is used to send notification to sales website, chat, ... when the payment order is successful, allows notify to multiple urls, separated by commas | [optional] 
**customer_email** | **str** | Customer&#x27;s email | [optional] 
**customer_phone** | **str** | Customer&#x27;s Phone | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

