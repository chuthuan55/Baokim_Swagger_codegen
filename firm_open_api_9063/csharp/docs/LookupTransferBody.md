# IO.Swagger.Model.LookupTransferBody
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RequestId** | **string** | The only code that corresponds to an upload request. Proposed format is as follows: PartnerCode + BK + YYYYMMDD + UniqueId | [optional] 
**RequestTime** | **string** | It is time to send request from Partner, format: YYYY-MM-DD HH:MM:SS | [optional] 
**PartnerCode** | **string** | The partner code is defined in the Baokim system. This code will send to the partner when the integration begins. | [optional] 
**Operation** | **string** | This parameter will determine which function partner is calling. For transactional lookup information, the fix is \&quot;9003 | [optional] 
**ReferenceId** | **string** | Transaction code from PARTNER submitted | [optional] 
**Signature** | **string** | The partner will digitally sign up data using the RSACryptoServiceProvider algorithm. Before sending to will base64 encoding. Data is structured: RequestId|RequestTime|PartnerCode| Operation|ReferenceId | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

