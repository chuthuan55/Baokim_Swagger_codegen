/* 
 *  Installment docs API
 *
 * <a href='/baokim-firm-open-api-9050'>1: Function Check Installment Support </a>  <a href='/baokim-firm-open-api-9051'>2: Function Get Bank Loan Package </a>  <a href='/baokim-firm-open-api-9052'>3: Function Create Transaction </a>  <a href='/baokim-firm-open-api-9062'>4: Function Cancel order</a>  Private key and public key Baokim is currently using digital signature by RSA-SHA1  There are several ways to generate RSA key pairs.  Way 1:  Generate your RSA key pairs online: <a href=\"http://travistidwell.com/blog/2013/09/06/an-online-rsa-public-and-private-key-generator/\" target=\"_blank\">Generate now</a>  Way 2:  Using OpenSSL software for Windows:  Step 1: Download the software at:  http://slproweb.com/products/Win32OpenSSL.html. Partner should download the installer \"OpenSSL_Light-1_0_2k\". Then install in any directory, for example \"C:\\OpenSSLWin64\"  Step 2: Access \"C:\\OpenSSLWin64\\bin\" then open the command prompt. Type the command to declare the environment config.  set OPENSSL_CONF=C:\\OpenSSL-Win64\\bin\\openssl.cfg  Step 3: Generate private key and public key  openssl genrsa -aes256 -out c:\\opensslkeys\\partner\\partner_privatekey.pem 2048  openssl rsa –in c:\\opensslkeys\\partner\\partner_privatekey.pem -pubout >c:\\opensslkeys\\partner\\partner_publickey.pem  After successful pairing, Partner will send back to Baokim the public key to authenticate the signature that the Partner sends via the API
 *
 * OpenAPI spec version: 1.0.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using NUnit.Framework;

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using IO.Swagger.Api;
using IO.Swagger.Model;
using IO.Swagger.Client;
using System.Reflection;
using Newtonsoft.Json;

namespace IO.Swagger.Test
{
    /// <summary>
    ///  Class for testing PartnerCheckinstallmentBody
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Swagger Codegen.
    /// Please update the test case below to test the model.
    /// </remarks>
    [TestFixture]
    public class PartnerCheckinstallmentBodyTests
    {
        // TODO uncomment below to declare an instance variable for PartnerCheckinstallmentBody
        //private PartnerCheckinstallmentBody instance;

        /// <summary>
        /// Setup before each test
        /// </summary>
        [SetUp]
        public void Init()
        {
            // TODO uncomment below to create an instance of PartnerCheckinstallmentBody
            //instance = new PartnerCheckinstallmentBody();
        }

        /// <summary>
        /// Clean up after each test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of PartnerCheckinstallmentBody
        /// </summary>
        [Test]
        public void PartnerCheckinstallmentBodyInstanceTest()
        {
            // TODO uncomment below to test "IsInstanceOfType" PartnerCheckinstallmentBody
            //Assert.IsInstanceOfType<PartnerCheckinstallmentBody> (instance, "variable 'instance' is a PartnerCheckinstallmentBody");
        }


        /// <summary>
        /// Test the property 'RequestId'
        /// </summary>
        [Test]
        public void RequestIdTest()
        {
            // TODO unit test for the property 'RequestId'
        }
        /// <summary>
        /// Test the property 'RequestTime'
        /// </summary>
        [Test]
        public void RequestTimeTest()
        {
            // TODO unit test for the property 'RequestTime'
        }
        /// <summary>
        /// Test the property 'PartnerCode'
        /// </summary>
        [Test]
        public void PartnerCodeTest()
        {
            // TODO unit test for the property 'PartnerCode'
        }
        /// <summary>
        /// Test the property 'Operation'
        /// </summary>
        [Test]
        public void OperationTest()
        {
            // TODO unit test for the property 'Operation'
        }
        /// <summary>
        /// Test the property 'CardNo'
        /// </summary>
        [Test]
        public void CardNoTest()
        {
            // TODO unit test for the property 'CardNo'
        }
        /// <summary>
        /// Test the property 'BankCode'
        /// </summary>
        [Test]
        public void BankCodeTest()
        {
            // TODO unit test for the property 'BankCode'
        }

    }

}
