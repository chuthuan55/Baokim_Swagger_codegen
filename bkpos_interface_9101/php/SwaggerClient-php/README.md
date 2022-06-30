# SwaggerClient-php
<a href='/baokim-firm-open-api-9050'>1: Function Check Installment Support </a>  <a href='/baokim-firm-open-api-9051'>2: Function Get Bank Loan Package </a>  <a href='/baokim-firm-open-api-9052'>3: Function Create Transaction </a>  <a href='/baokim-firm-open-api-9062'>4: Function Cancel order</a>  Private key and public key Baokim is currently using digital signature by RSA-SHA1  There are several ways to generate RSA key pairs.  Way 1:  Generate your RSA key pairs online: <a href=\"http://travistidwell.com/blog/2013/09/06/an-online-rsa-public-and-private-key-generator/\" target=\"_blank\">Generate now</a>  Way 2:  Using OpenSSL software for Windows:  Step 1: Download the software at:  http://slproweb.com/products/Win32OpenSSL.html. Partner should download the installer \"OpenSSL_Light-1_0_2k\". Then install in any directory, for example \"C:\\OpenSSLWin64\"  Step 2: Access \"C:\\OpenSSLWin64\\bin\" then open the command prompt. Type the command to declare the environment config.  set OPENSSL_CONF=C:\\OpenSSL-Win64\\bin\\openssl.cfg  Step 3: Generate private key and public key  openssl genrsa -aes256 -out c:\\opensslkeys\\partner\\partner_privatekey.pem 2048  openssl rsa –in c:\\opensslkeys\\partner\\partner_privatekey.pem -pubout >c:\\opensslkeys\\partner\\partner_publickey.pem  After successful pairing, Partner will send back to Baokim the public key to authenticate the signature that the Partner sends via the API

This PHP package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.php.PhpClientCodegen

## Requirements

PHP 5.5 and later

## Installation & Usage
### Composer

To install the bindings via [Composer](http://getcomposer.org/), add the following to `composer.json`:

```
{
  "repositories": [
    {
      "type": "git",
      "url": "https://github.com/GIT_USER_ID/GIT_REPO_ID.git"
    }
  ],
  "require": {
    "GIT_USER_ID/GIT_REPO_ID": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
    require_once('/path/to/SwaggerClient-php/vendor/autoload.php');
```

## Tests

To run the unit tests:

```
composer install
./vendor/bin/phpunit
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\CancelOrderApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\PartnerCancelorderBody(); // \Swagger\Client\Model\PartnerCancelorderBody | Process:

1. Partner will call the cancel order function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return successful.

try {
    $result = $apiInstance->apiV1PartnerCancelOrderPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CancelOrderApi->apiV1PartnerCancelOrderPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

## Documentation for API Endpoints

All URIs are relative to *https://https://devtest.baokim.vn*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CancelOrderApi* | [**apiV1PartnerCancelOrderPost**](docs/Api/CancelOrderApi.md#apiv1partnercancelorderpost) | **POST** /api/v1/partner/cancel-order | https::devtest.baokim.vn/api/v1/partner/installment
*CheckInstallmentSupportApi* | [**apiV1PartnerCheckInstallmentPost**](docs/Api/CheckInstallmentSupportApi.md#apiv1partnercheckinstallmentpost) | **POST** /api/v1/partner/check-installment | https::devtest.baokim.vn/api/v1/partner/installment
*CreateTransactionApi* | [**apiV1PartnerCreateOrderPost**](docs/Api/CreateTransactionApi.md#apiv1partnercreateorderpost) | **POST** /api/v1/partner/create-order | https::devtest.baokim.vn/api/v1/partner/installment
*GetBankLoanPackageApi* | [**apiV1PartnerGetLoanPost**](docs/Api/GetBankLoanPackageApi.md#apiv1partnergetloanpost) | **POST** /api/v1/partner/get-loan | https::devtest.baokim.vn/api/v1/partner/installment

## Documentation For Models

 - [InlineResponse106](docs/Model/InlineResponse106.md)
 - [InlineResponse106Data](docs/Model/InlineResponse106Data.md)
 - [InlineResponse157](docs/Model/InlineResponse157.md)
 - [InlineResponse157Data](docs/Model/InlineResponse157Data.md)
 - [InlineResponse200](docs/Model/InlineResponse200.md)
 - [InlineResponse2001](docs/Model/InlineResponse2001.md)
 - [InlineResponse2001Data](docs/Model/InlineResponse2001Data.md)
 - [InlineResponse2001DataBankList](docs/Model/InlineResponse2001DataBankList.md)
 - [InlineResponse2001DataLoanPackages](docs/Model/InlineResponse2001DataLoanPackages.md)
 - [InlineResponse2002](docs/Model/InlineResponse2002.md)
 - [InlineResponse2002Data](docs/Model/InlineResponse2002Data.md)
 - [InlineResponse2003](docs/Model/InlineResponse2003.md)
 - [PartnerCancelorderBody](docs/Model/PartnerCancelorderBody.md)
 - [PartnerCheckinstallmentBody](docs/Model/PartnerCheckinstallmentBody.md)
 - [PartnerCreateorderBody](docs/Model/PartnerCreateorderBody.md)
 - [PartnerGetloanBody](docs/Model/PartnerGetloanBody.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


