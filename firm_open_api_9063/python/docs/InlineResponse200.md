# InlineResponse200

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **int** | 200 : Successful. &lt;br&gt; 99 : Transaction timeout.&lt;br&gt; 11 : Failed.&lt;br&gt; 101 : Error processing from Baokim.&lt;br&gt; 102 : Duplicated RequestId.&lt;br&gt; 103 : Incorrect signature.&lt;br&gt; 110 : Incorrect PartnerCode.&lt;br&gt; 111 : PartnerCode deleted from the system.&lt;br&gt; 112 : PartnerCode not yet activated.&lt;br&gt; 113 : Operation code is required.&lt;br&gt; 114 : Incorrect Operation code.&lt;br&gt; 115 : BankID is required.&lt;br&gt; 116 : BankID not supported.&lt;br&gt; 117 : Account no. /Card no. should be from 6-22 characters in length.&lt;br&gt; 118 : Invalid account no./Card no..&lt;br&gt; 119 : Account no./Card no. does not exist.&lt;br&gt; 120 : Incorrect account type.&lt;br&gt; 121 : Transaction ID sent from Partner is required.&lt;br&gt; 122 : Transaction ID sent by Partner is existing.&lt;br&gt; 123 : Transaction unfound.&lt;br&gt; 124 : Transfer amount required.&lt;br&gt; 125 : Invalid transfer amount.&lt;br&gt; 126 : Error processing between Baokim and bank.&lt;br&gt; 127 : Error connecting to bank.&lt;br&gt; 128 : Error processing from bank.&lt;br&gt; 129 : Insufficient disbursement limit or expired guarantee period.&lt;br&gt; 130 : Exceeded transfer limit on day.&lt;br&gt; | [optional] 
**response_message** | **str** | Description for return status | [optional] 
**request_id** | **str** | Partner information posted | [optional] 
**bank_no** | **str** | Partner information posted | [optional] 
**acc_no** | **str** | Partner information posted | [optional] 
**acc_type** | **str** | Partner information posted | [optional] 
**acc_name** | **str** | Baokim Customer&#x27;s name response if customer information is submitted correctly | [optional] 
**signature** | **str** | Baokim will sign with digital signature of data returned using RSACryptoServiceProvider. Returns the base64 encoding. Data is structured: ResponseCode|ResponseMessage|RequestId| BankNo|AccNo|AccType|AccName | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

