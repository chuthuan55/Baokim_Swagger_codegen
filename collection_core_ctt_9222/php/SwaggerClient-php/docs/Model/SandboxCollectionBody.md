# SandboxCollectionBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **string** | Unique code | [optional] 
**request_time** | **string** | Time send the request from PARTNER , format: YYYY-MM-DD HH:MM:SS. | [optional] 
**partner_code** | **string** | Unique code BAOKIM provide | [optional] 
**operation** | **float** | 9001: create va - 9002: update va | [optional] 
**acc_no** | **string** | Required when update:VA number need to update information | [optional] 
**acc_name** | **string** | The name of Account holder (name of USER) | [optional] 
**collect_amount** | **float** | collect amount | [optional] 
**order_id** | **string** | Unique id for each VA | [optional] 
**expire_date** | **string** | Expire date. Format: YYYYMM-DD HH:II:SS | [optional] 
**collection_type** | **string** | Collection type(MORE,CORRECT,LESS,INFINITE) | [optional] 
**bank** | **string** | Bank | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

