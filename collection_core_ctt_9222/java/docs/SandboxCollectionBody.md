# SandboxCollectionBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestId** | **String** | Unique code  |  [optional]
**requestTime** | **String** | Time send the request from PARTNER , format: YYYY-MM-DD HH:MM:SS. |  [optional]
**partnerCode** | **String** | Unique code BAOKIM provide |  [optional]
**operation** | [**BigDecimal**](BigDecimal.md) | 9001: create va - 9002: update va |  [optional]
**accNo** | **String** | Required when update:VA number need to update information |  [optional]
**accName** | **String** | The name of Account holder (name of USER) |  [optional]
**collectAmount** | [**BigDecimal**](BigDecimal.md) | collect amount  |  [optional]
**orderId** | **String** | Unique id for each VA |  [optional]
**expireDate** | **String** | Expire date. Format: YYYYMM-DD HH:II:SS |  [optional]
**collectionType** | **String** | Collection type(MORE,CORRECT,LESS,INFINITE) |  [optional]
**bank** | **String** | Bank |  [optional]
