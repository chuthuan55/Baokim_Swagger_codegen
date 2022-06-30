# swagger-java-client

 Installment docs API
- API version: 1.0.0
  - Build date: 2022-06-30T01:29:43.937Z[Etc/UTC]

<a href='/baokim-firm-open-api-9050'>1: Function Check Installment Support </a>  <a href='/baokim-firm-open-api-9051'>2: Function Get Bank Loan Package </a>  <a href='/baokim-firm-open-api-9052'>3: Function Create Transaction </a>  <a href='/baokim-firm-open-api-9062'>4: Function Cancel order</a>  Private key and public key Baokim is currently using digital signature by RSA-SHA1  There are several ways to generate RSA key pairs.  Way 1:  Generate your RSA key pairs online: <a href=\"http://travistidwell.com/blog/2013/09/06/an-online-rsa-public-and-private-key-generator/\" target=\"_blank\">Generate now</a>  Way 2:  Using OpenSSL software for Windows:  Step 1: Download the software at:  http://slproweb.com/products/Win32OpenSSL.html. Partner should download the installer \"OpenSSL_Light-1_0_2k\". Then install in any directory, for example \"C:\\OpenSSLWin64\"  Step 2: Access \"C:\\OpenSSLWin64\\bin\" then open the command prompt. Type the command to declare the environment config.  set OPENSSL_CONF=C:\\OpenSSL-Win64\\bin\\openssl.cfg  Step 3: Generate private key and public key  openssl genrsa -aes256 -out c:\\opensslkeys\\partner\\partner_privatekey.pem 2048  openssl rsa –in c:\\opensslkeys\\partner\\partner_privatekey.pem -pubout >c:\\opensslkeys\\partner\\partner_publickey.pem  After successful pairing, Partner will send back to Baokim the public key to authenticate the signature that the Partner sends via the API


*Automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen)*


## Requirements

Building the API client library requires:
1. Java 1.7+
2. Maven/Gradle

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>io.swagger</groupId>
  <artifactId>swagger-java-client</artifactId>
  <version>1.0.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "io.swagger:swagger-java-client:1.0.0"
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/swagger-java-client-1.0.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.CancelOrderApi;

import java.io.File;
import java.util.*;

public class CancelOrderApiExample {

    public static void main(String[] args) {
        
        CancelOrderApi apiInstance = new CancelOrderApi();
        PartnerCancelorderBody body = new PartnerCancelorderBody(); // PartnerCancelorderBody | Process:

1. Partner will call the cancel order function, Baokim will check the data format and signature authentication, then will check the customer information.

2. If the correct information will return successful.
        try {
            InlineResponse2003 result = apiInstance.apiV1PartnerCancelOrderPost(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CancelOrderApi#apiV1PartnerCancelOrderPost");
            e.printStackTrace();
        }
    }
}
```

## Documentation for API Endpoints

All URIs are relative to *https://https://devtest.baokim.vn*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CancelOrderApi* | [**apiV1PartnerCancelOrderPost**](docs/CancelOrderApi.md#apiV1PartnerCancelOrderPost) | **POST** /api/v1/partner/cancel-order | https::devtest.baokim.vn/api/v1/partner/installment
*CheckInstallmentSupportApi* | [**apiV1PartnerCheckInstallmentPost**](docs/CheckInstallmentSupportApi.md#apiV1PartnerCheckInstallmentPost) | **POST** /api/v1/partner/check-installment | https::devtest.baokim.vn/api/v1/partner/installment
*CreateTransactionApi* | [**apiV1PartnerCreateOrderPost**](docs/CreateTransactionApi.md#apiV1PartnerCreateOrderPost) | **POST** /api/v1/partner/create-order | https::devtest.baokim.vn/api/v1/partner/installment
*GetBankLoanPackageApi* | [**apiV1PartnerGetLoanPost**](docs/GetBankLoanPackageApi.md#apiV1PartnerGetLoanPost) | **POST** /api/v1/partner/get-loan | https::devtest.baokim.vn/api/v1/partner/installment

## Documentation for Models

 - [InlineResponse106](docs/InlineResponse106.md)
 - [InlineResponse106Data](docs/InlineResponse106Data.md)
 - [InlineResponse157](docs/InlineResponse157.md)
 - [InlineResponse157Data](docs/InlineResponse157Data.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2001Data](docs/InlineResponse2001Data.md)
 - [InlineResponse2001DataBankList](docs/InlineResponse2001DataBankList.md)
 - [InlineResponse2001DataLoanPackages](docs/InlineResponse2001DataLoanPackages.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2002Data](docs/InlineResponse2002Data.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [PartnerCancelorderBody](docs/PartnerCancelorderBody.md)
 - [PartnerCheckinstallmentBody](docs/PartnerCheckinstallmentBody.md)
 - [PartnerCreateorderBody](docs/PartnerCreateorderBody.md)
 - [PartnerGetloanBody](docs/PartnerGetloanBody.md)

## Documentation for Authorization

All endpoints do not require authorization.
Authentication schemes defined for the API:

## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

