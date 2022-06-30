# LookupTransferBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The only code that corresponds to an upload request. Proposed format is as follows: PartnerCode + BK + YYYYMMDD + UniqueId | [optional] 
**request_time** | **str** | It is time to send request from Partner, format: YYYY-MM-DD HH:MM:SS | [optional] 
**partner_code** | **str** | The partner code is defined in the Baokim system. This code will send to the partner when the integration begins. | [optional] 
**operation** | **str** | This parameter will determine which function partner is calling. For transactional lookup information, the fix is \&quot;9003 | [optional] 
**reference_id** | **str** | Transaction code from PARTNER submitted | [optional] 
**signature** | **str** | The partner will digitally sign up data using the RSACryptoServiceProvider algorithm. Before sending to will base64 encoding. Data is structured: RequestId|RequestTime|PartnerCode| Operation|ReferenceId | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

