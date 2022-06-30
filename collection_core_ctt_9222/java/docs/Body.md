# Body

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestId** | **String** | Unique code  |  [optional]
**requestTime** | **String** | Time send the request from PARTNER , format: YYYY-MM-DD HH:MM:SS. |  [optional]
**partnerCode** | **String** | Fix: BAOKIM |  [optional]
**accNo** | **String** | VA number |  [optional]
**clientIdNo** | **String** | Client id no |  [optional]
**transId** | **String** | Unique transaction id in BAOKIM system |  [optional]
**transAmount** | [**BigDecimal**](BigDecimal.md) | collect amount  |  [optional]
**transTime** | **String** | Transaction time at BAOKIM system  |  [optional]
**befTransDebt** | [**BigDecimal**](BigDecimal.md) | Amount before transaction |  [optional]
**affTransDebt** | [**BigDecimal**](BigDecimal.md) | Amount after transaction |  [optional]
**accountType** | [**BigDecimal**](BigDecimal.md) | Account with indentifier or without indentifier. 1: Account with identifier. 2: Account without identifier. |  [optional]
**orderId** | [**BigDecimal**](BigDecimal.md) | Unique id for each VA  |  [optional]
**signature** | **String** | BAOKIM will sign the data on the following structure sha1withRSA: RequestId|RequestTime|PartnerCode| AccNo|ClientIdNo|TransId|TransAmount| TransTime|BefTransDebt|AffTransDebt| AccountType|OrderId Then will use base64 encoding |  [optional]
