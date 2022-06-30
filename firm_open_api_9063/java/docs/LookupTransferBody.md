# LookupTransferBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestId** | **String** | The only code that corresponds to an upload request. Proposed format is as follows: PartnerCode + BK + YYYYMMDD + UniqueId |  [optional]
**requestTime** | **String** | It is time to send request from Partner, format: YYYY-MM-DD HH:MM:SS |  [optional]
**partnerCode** | **String** | The partner code is defined in the Baokim system. This code will send to the partner when the integration begins. |  [optional]
**operation** | **String** | This parameter will determine which function partner is calling. For transactional lookup information, the fix is \&quot;9003 |  [optional]
**referenceId** | **String** | Transaction code from PARTNER submitted |  [optional]
**signature** | **String** | The partner will digitally sign up data using the RSACryptoServiceProvider algorithm. Before sending to will base64 encoding. Data is structured: RequestId|RequestTime|PartnerCode| Operation|ReferenceId |  [optional]
