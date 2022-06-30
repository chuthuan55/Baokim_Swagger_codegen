# InlineResponse2001

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responseCode** | **Integer** | 200 : Successful. &lt;br&gt; 99 : Transaction timeout.&lt;br&gt; 11 : Failed.&lt;br&gt; 101 : Error processing from Baokim.&lt;br&gt; 102 : Duplicated RequestId.&lt;br&gt; 103 : Incorrect signature.&lt;br&gt; 110 : Incorrect PartnerCode.&lt;br&gt; 111 : PartnerCode deleted from the system.&lt;br&gt; 112 : PartnerCode not yet activated.&lt;br&gt; 113 : Operation code is required.&lt;br&gt; 114 : Incorrect Operation code.&lt;br&gt; 115 : BankID is required.&lt;br&gt; 116 : BankID not supported.&lt;br&gt; 117 : Account no. /Card no. should be from 6-22 characters in length.&lt;br&gt; 118 : Invalid account no./Card no..&lt;br&gt; 119 : Account no./Card no. does not exist.&lt;br&gt; 120 : Incorrect account type.&lt;br&gt; 121 : Transaction ID sent from Partner is required.&lt;br&gt; 122 : Transaction ID sent by Partner is existing.&lt;br&gt; 123 : Transaction unfound.&lt;br&gt; 124 : Transfer amount required.&lt;br&gt; 125 : Invalid transfer amount.&lt;br&gt; 126 : Error processing between Baokim and bank.&lt;br&gt; 127 : Error connecting to bank.&lt;br&gt; 128 : Error processing from bank.&lt;br&gt; 129 : Insufficient disbursement limit or expired guarantee period.&lt;br&gt; 130 : Exceeded transfer limit on day.&lt;br&gt; |  [optional]
**responseMessage** | **String** | Description for return status |  [optional]
**referenceId** | **String** | Partner information posted |  [optional]
**transactionId** | **String** | Transaction code recorded side Baokim |  [optional]
**transactionTime** | **String** | Finishing time side Baokim. Format YYYY-MM-DD |  [optional]
**bankNo** | **String** | Partner information posted |  [optional]
**accNo** | **String** | Partner information posted |  [optional]
**accName** | **String** | Full name of the recipient, may or may not, depending on the time |  [optional]
**accType** | **String** | Partner information posted |  [optional]
**requestAmount** | **Integer** | Partner information posted |  [optional]
**transferAmount** | **Integer** | The actual amount transferred to the recipient. Will be less if the remittance |  [optional]
**affterBalance** | **Integer** | Current balance of investors |  [optional]
**afterDisbursementDay** | **Integer** | Continue disbursement amount (in limit) |  [optional]
**signature** | **String** | BAOKIM will sign by digital signature of response data. Structured data: ResponseCode|ResponseMessage| RequestId | PartnerCode | Available | Holding |  [optional]
