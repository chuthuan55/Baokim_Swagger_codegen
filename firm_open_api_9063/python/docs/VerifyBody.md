# VerifyBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The only code that corresponds to an upload request. Proposed format is as follows: PartnerCode + BK + YYYYMMDD + UniqueId | [optional] 
**request_time** | **str** | It is time to send request from Partner, format: YYYY-MM-DD HH:MM:SS | [optional] 
**partner_code** | **str** | The partner code is defined in the Baokim system. This code will send to the partner when the integration begins. | [optional] 
**operation** | **str** | This parameter will determine which function that partner is calling. For customer authentication functions, the fix is “9001” | [optional] 
**bank_no** | **str** | Bank code in accordance with Baokim is defined in the section 8. List of remittance banks | [optional] 
**acc_no** | **str** | Account number or bank card number of the customer. | [optional] 
**acc_type** | **str** | AccNo classification 0: Bank account number 1: Bank card number | [optional] 
**signature** | **str** | The partner will sign with digital signature of data transmitted using the algorithm RSACryptoServiceProvider. Before sending ,data will be base64 encoding. Data follow this structure: RequestId|RequestTime| PartnerCode|Operation|BankNo| AccNo|AccType | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

