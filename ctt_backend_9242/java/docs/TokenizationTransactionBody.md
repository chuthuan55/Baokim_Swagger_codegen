# TokenizationTransactionBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiOperation** | **String** | Type of token order (PAY: generate token and include payment if needed or PAY_BY_TOKEN: pay by token generated before) |  [optional]
**merchantId** | **Integer** | Merchant ID |  [optional]
**initToken** | **Integer** | Required with api_operation &#x3D; PAY, distinguish orders only generate token or include payment. (1: Only generate token, 0: Include payment) |  [optional]
**order** | [**Apiv1tokenizationtransactionOrder**](Apiv1tokenizationtransactionOrder.md) |  |  [optional]
**card** | [**Apiv1tokenizationtransactionCard**](Apiv1tokenizationtransactionCard.md) |  |  [optional]
