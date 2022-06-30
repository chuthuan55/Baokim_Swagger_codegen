# Body

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Unique code  | [optional] 
**request_time** | **str** | Time send the request from PARTNER , format: YYYY-MM-DD HH:MM:SS. | [optional] 
**partner_code** | **str** | Fix: BAOKIM | [optional] 
**acc_no** | [**String**](String.md) | VA number | [optional] 
**client_id_no** | **str** | Client id no | [optional] 
**trans_id** | **str** | Unique transaction id in BAOKIM system | [optional] 
**trans_amount** | **float** | collect amount  | [optional] 
**trans_time** | **str** | Transaction time at BAOKIM system  | [optional] 
**bef_trans_debt** | **float** | Amount before transaction | [optional] 
**aff_trans_debt** | **float** | Amount after transaction | [optional] 
**account_type** | **float** | Account with indentifier or without indentifier. 1: Account with identifier. 2: Account without identifier. | [optional] 
**order_id** | **float** | Unique id for each VA  | [optional] 
**signature** | **str** | BAOKIM will sign the data on the following structure sha1withRSA: RequestId|RequestTime|PartnerCode| AccNo|ClientIdNo|TransId|TransAmount| TransTime|BefTransDebt|AffTransDebt| AccountType|OrderId Then will use base64 encoding | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

