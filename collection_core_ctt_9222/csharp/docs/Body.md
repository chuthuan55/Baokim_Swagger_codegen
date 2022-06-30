# IO.Swagger.Model.Body
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RequestId** | **string** | Unique code  | [optional] 
**RequestTime** | **string** | Time send the request from PARTNER , format: YYYY-MM-DD HH:MM:SS. | [optional] 
**PartnerCode** | **string** | Fix: BAOKIM | [optional] 
**AccNo** | **string** | VA number | [optional] 
**ClientIdNo** | **string** | Client id no | [optional] 
**TransId** | **string** | Unique transaction id in BAOKIM system | [optional] 
**TransAmount** | [**decimal?**](BigDecimal.md) | collect amount  | [optional] 
**TransTime** | **string** | Transaction time at BAOKIM system  | [optional] 
**BefTransDebt** | [**decimal?**](BigDecimal.md) | Amount before transaction | [optional] 
**AffTransDebt** | [**decimal?**](BigDecimal.md) | Amount after transaction | [optional] 
**AccountType** | [**decimal?**](BigDecimal.md) | Account with indentifier or without indentifier. 1: Account with identifier. 2: Account without identifier. | [optional] 
**OrderId** | [**decimal?**](BigDecimal.md) | Unique id for each VA  | [optional] 
**Signature** | **string** | BAOKIM will sign the data on the following structure sha1withRSA: RequestId|RequestTime|PartnerCode| AccNo|ClientIdNo|TransId|TransAmount| TransTime|BefTransDebt|AffTransDebt| AccountType|OrderId Then will use base64 encoding | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

