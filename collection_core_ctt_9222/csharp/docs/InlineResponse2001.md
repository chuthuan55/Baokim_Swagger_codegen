# IO.Swagger.Model.InlineResponse2001
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ResponseCode** | [**decimal?**](BigDecimal.md) | Response code | [optional] 
**ResponseMessage** | **string** | Response message | [optional] 
**ReferenceId** | **string** | Unique transaction id in PARTNER system | [optional] 
**AccNo** | **string** | Unique id for each VA | [optional] 
**AffTransDebt** | [**decimal?**](BigDecimal.md) | Remain amount of VA | [optional] 
**Signature** | **string** | Baokim will sign with digital signature of data returned using RSACryptoServiceProvider. Returns the base64 encoding. Data is structured: ResponseCode|ResponseMessage|ReferenceId| AccNo|AffTransDebt | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

