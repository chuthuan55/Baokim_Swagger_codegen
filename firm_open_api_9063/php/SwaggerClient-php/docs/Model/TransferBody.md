# TransferBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **string** | The only code that corresponds to an upload request. Proposed format is as follows: PartnerCode + BK + YYYYMMDD + UniqueId | [optional] 
**request_time** | **string** | It is time to send request from Partner, format: YYYY-MM-DD HH:MM:SS | [optional] 
**partner_code** | **string** | The partner code is defined in the Baokim system. This code will send to the partner when the integration begins. | [optional] 
**operation** | **string** | This parameter will determine which function partner is calling. For the transfer function, the fix is “9002” | [optional] 
**reference_id** | **string** | Transaction code sent by the partner | [optional] 
**bank_no** | **string** | Bank code in accordance with Baokim is defined in the section 8. List of remittance banks | [optional] 
**acc_no** | **string** | Account number or bank card number of the customer. | [optional] 
**acc_type** | **string** | AccNo classification 0: Bank account number 1: Bank card number | [optional] 
**request_amount** | **string** | The amount requested by the partner to transfer to the recipient. | [optional] 
**memo** | **string** | Money transfer contents | [optional] 
**signature** | **string** | The partner will sign with digital signature of data transmitted using the algorithm RSACryptoServiceProvider. Before sending ,data will be base64 encoding. Data follow this structure: RequestId|RequestTime|PartnerCode| Operation|ReferenceId|BankNo|AccNo| AccType|RequestAmount|Memo | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

