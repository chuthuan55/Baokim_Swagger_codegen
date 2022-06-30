# InlineResponse2001

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **float** | Response code | [optional] 
**response_message** | **str** | Response message | [optional] 
**reference_id** | **str** | Unique transaction id in PARTNER system | [optional] 
**acc_no** | **str** | Unique id for each VA | [optional] 
**aff_trans_debt** | **float** | Remain amount of VA | [optional] 
**signature** | **str** | Baokim will sign with digital signature of data returned using RSACryptoServiceProvider. Returns the base64 encoding. Data is structured: ResponseCode|ResponseMessage|ReferenceId| AccNo|AffTransDebt | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

