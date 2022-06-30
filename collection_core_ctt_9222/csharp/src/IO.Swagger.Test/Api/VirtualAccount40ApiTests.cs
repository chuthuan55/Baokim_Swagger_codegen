/* 
 * Collection payments
 *
 * <img src=\"https://devtest.baokim.vn/collection/core_ctt/image/Picture1.png\" class=\"image-collection-payment\" /> <p><strong>Note:</strong></p> <p>+ In case PARTNER want to use collect via Virtual Account, PARTNER will need to buid:</p> <p style=\"padding-left: 50px;\">     - <a href=\"#operations-Virtual_Account_4\\.0-8442c69ffbaf4b3677a52fa3ebcef6d4\">Register virtual account</a> <br>     - <a href=\"#operations-Virtual_Account_4\\.0-1796c61005edee3976097a607fe9dbaa\">Update virtual account informations</a> <br>     - <a href=\"#operations-tag-Notice_of_collection_transaction\">Notice of collection transaction</a> <br> </p>
 *
 * OpenAPI spec version: 2.3 and 4.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using RestSharp;
using NUnit.Framework;

using IO.Swagger.Client;
using IO.Swagger.Api;
using IO.Swagger.Model;

namespace IO.Swagger.Test
{
    /// <summary>
    ///  Class for testing VirtualAccount40Api
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Swagger Codegen.
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    [TestFixture]
    public class VirtualAccount40ApiTests
    {
        private VirtualAccount40Api instance;

        /// <summary>
        /// Setup before each unit test
        /// </summary>
        [SetUp]
        public void Init()
        {
            instance = new VirtualAccount40Api();
        }

        /// <summary>
        /// Clean up after each unit test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of VirtualAccount40Api
        /// </summary>
        [Test]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsInstanceOfType' VirtualAccount40Api
            //Assert.IsInstanceOfType(typeof(VirtualAccount40Api), instance, "instance is a VirtualAccount40Api");
        }

        /// <summary>
        /// Test 1796c61005edee3976097a607fe9dbaa
        /// </summary>
        [Test]
        public void 1796c61005edee3976097a607fe9dbaaTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //V4UpdateBody body = null;
            //string contentType = null;
            //string signature = null;
            //var response = instance.1796c61005edee3976097a607fe9dbaa(body, contentType, signature);
            //Assert.IsInstanceOf<InlineResponse200> (response, "response is InlineResponse200");
        }
        /// <summary>
        /// Test 8442c69ffbaf4b3677a52fa3ebcef6d4
        /// </summary>
        [Test]
        public void 8442c69ffbaf4b3677a52fa3ebcef6d4Test()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //V4CreateBody body = null;
            //string contentType = null;
            //string signature = null;
            //var response = instance.8442c69ffbaf4b3677a52fa3ebcef6d4(body, contentType, signature);
            //Assert.IsInstanceOf<InlineResponse200> (response, "response is InlineResponse200");
        }
    }

}