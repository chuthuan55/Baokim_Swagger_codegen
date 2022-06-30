# VerifyBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestId** | **String** | The only code that corresponds to an upload request. Proposed format is as follows: PartnerCode + BK + YYYYMMDD + UniqueId |  [optional]
**requestTime** | **String** | It is time to send request from Partner, format: YYYY-MM-DD HH:MM:SS |  [optional]
**partnerCode** | **String** | The partner code is defined in the Baokim system. This code will send to the partner when the integration begins. |  [optional]
**operation** | **String** | This parameter will determine which function that partner is calling. For customer authentication functions, the fix is “9001” |  [optional]
**bankNo** | **String** | Bank code in accordance with Baokim is defined in the section 8. List of remittance banks |  [optional]
**accNo** | **String** | Account number or bank card number of the customer. |  [optional]
**accType** | **String** | AccNo classification 0: Bank account number 1: Bank card number |  [optional]
**signature** | **String** | The partner will sign with digital signature of data transmitted using the algorithm RSACryptoServiceProvider. Before sending ,data will be base64 encoding. Data follow this structure: RequestId|RequestTime| PartnerCode|Operation|BankNo| AccNo|AccType |  [optional]
