# Body

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **string** | Unique code | [optional] 
**request_time** | **string** | Time send the request from PARTNER , format: YYYY-MM-DD HH:MM:SS. | [optional] 
**partner_code** | **string** | Fix: BAOKIM | [optional] 
**acc_no** | [**String**](String.md) | VA number | [optional] 
**client_id_no** | **string** | Client id no | [optional] 
**trans_id** | **string** | Unique transaction id in BAOKIM system | [optional] 
**trans_amount** | **float** | collect amount | [optional] 
**trans_time** | **string** | Transaction time at BAOKIM system | [optional] 
**bef_trans_debt** | **float** | Amount before transaction | [optional] 
**aff_trans_debt** | **float** | Amount after transaction | [optional] 
**account_type** | **float** | Account with indentifier or without indentifier. 1: Account with identifier. 2: Account without identifier. | [optional] 
**order_id** | **float** | Unique id for each VA | [optional] 
**signature** | **string** | BAOKIM will sign the data on the following structure sha1withRSA: RequestId|RequestTime|PartnerCode| AccNo|ClientIdNo|TransId|TransAmount| TransTime|BefTransDebt|AffTransDebt| AccountType|OrderId Then will use base64 encoding | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

