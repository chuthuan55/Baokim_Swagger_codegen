# CollectionV2Body

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Unique code  | [optional] 
**request_time** | **str** | Time send the request from PARTNER , format: YYYY-MM-DD HH:MM:SS. | [optional] 
**partner_code** | **str** | Unique code BAOKIM provide | [optional] 
**operation** | **float** | 9001: create va - 9002: update va | [optional] 
**create_type** | **str** | Fix &#x3D; 2 | [optional] 
**acc_name** | **str** | The name of Account holder (name of USER) | [optional] 
**collect_amount_min** | **float** | collect amount min (50.000) | [optional] 
**collect_amount_max** | **float** | collect amount min (50.000.000) | [optional] 
**acc_no** | **str** | Required when update:VA number need to update information. If create VA, send NULL | [optional] 
**order_id** | **str** | Unique id for each VA | [optional] 
**expire_date** | **str** | Expire date. Format: YYYYMM-DD HH:II:SS | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

