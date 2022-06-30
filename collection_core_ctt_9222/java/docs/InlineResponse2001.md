# InlineResponse2001

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responseCode** | [**BigDecimal**](BigDecimal.md) | Response code |  [optional]
**responseMessage** | **String** | Response message |  [optional]
**referenceId** | **String** | Unique transaction id in PARTNER system |  [optional]
**accNo** | **String** | Unique id for each VA |  [optional]
**affTransDebt** | [**BigDecimal**](BigDecimal.md) | Remain amount of VA |  [optional]
**signature** | **String** | Baokim will sign with digital signature of data returned using RSACryptoServiceProvider. Returns the base64 encoding. Data is structured: ResponseCode|ResponseMessage|ReferenceId| AccNo|AffTransDebt |  [optional]
