# SwaggerClient-php
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This PHP package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
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

$apiInstance = new Swagger\Client\Api\CHECKPARTNERLIMITApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\RetailCheckpartnerlimitBody(); // \Swagger\Client\Model\RetailCheckpartnerlimitBody | 
$content_type = "content_type_example"; // string | 
$signature = "signature_example"; // string | BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption

try {
    $result = $apiInstance->apiRetailCheckPartnerLimitPost($body, $content_type, $signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CHECKPARTNERLIMITApi->apiRetailCheckPartnerLimitPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CHECKPARTNERLIMITApi* | [**apiRetailCheckPartnerLimitPost**](docs/Api/CHECKPARTNERLIMITApi.md#apiretailcheckpartnerlimitpost) | **POST** /api/retail/check-partner-limit | CHECK PARTNER LIMIT

## Documentation For Models

 - [InlineResponse101](docs/Model/InlineResponse101.md)
 - [InlineResponse200](docs/Model/InlineResponse200.md)
 - [RetailCheckpartnerlimitBody](docs/Model/RetailCheckpartnerlimitBody.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


