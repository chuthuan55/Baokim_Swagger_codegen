# IO.Swagger.Model.TokenizationTransactionBody
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ApiOperation** | **string** | Type of token order (PAY: generate token and include payment if needed or PAY_BY_TOKEN: pay by token generated before) | [optional] 
**MerchantId** | **int?** | Merchant ID | [optional] 
**InitToken** | **int?** | Required with api_operation &#x3D; PAY, distinguish orders only generate token or include payment. (1: Only generate token, 0: Include payment) | [optional] 
**Order** | [**Apiv1tokenizationtransactionOrder**](Apiv1tokenizationtransactionOrder.md) |  | [optional] 
**Card** | [**Apiv1tokenizationtransactionCard**](Apiv1tokenizationtransactionCard.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

