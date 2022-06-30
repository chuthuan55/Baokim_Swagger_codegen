# IO.Swagger.Model.CollectionV2Body
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RequestId** | **string** | Unique code  | [optional] 
**RequestTime** | **string** | Time send the request from PARTNER , format: YYYY-MM-DD HH:MM:SS. | [optional] 
**PartnerCode** | **string** | Unique code BAOKIM provide | [optional] 
**Operation** | [**decimal?**](BigDecimal.md) | 9001: create va - 9002: update va | [optional] 
**CreateType** | **string** | Fix &#x3D; 2 | [optional] 
**AccName** | **string** | The name of Account holder (name of USER) | [optional] 
**CollectAmountMin** | [**decimal?**](BigDecimal.md) | collect amount min (50.000) | [optional] 
**CollectAmountMax** | [**decimal?**](BigDecimal.md) | collect amount min (50.000.000) | [optional] 
**AccNo** | **string** | Required when update:VA number need to update information. If create VA, send NULL | [optional] 
**OrderId** | **string** | Unique id for each VA | [optional] 
**ExpireDate** | **string** | Expire date. Format: YYYYMM-DD HH:II:SS | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

