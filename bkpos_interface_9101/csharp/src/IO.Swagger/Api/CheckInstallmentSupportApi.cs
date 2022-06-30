/* 
 *  Installment docs API
 *
 * <a href='/baokim-firm-open-api-9050'>1: Function Check Installment Support </a>  <a href='/baokim-firm-open-api-9051'>2: Function Get Bank Loan Package </a>  <a href='/baokim-firm-open-api-9052'>3: Function Create Transaction </a>  <a href='/baokim-firm-open-api-9062'>4: Function Cancel order</a>  Private key and public key Baokim is currently using digital signature by RSA-SHA1  There are several ways to generate RSA key pairs.  Way 1:  Generate your RSA key pairs online: <a href=\"http://travistidwell.com/blog/2013/09/06/an-online-rsa-public-and-private-key-generator/\" target=\"_blank\">Generate now</a>  Way 2:  Using OpenSSL software for Windows:  Step 1: Download the software at:  http://slproweb.com/products/Win32OpenSSL.html. Partner should download the installer \"OpenSSL_Light-1_0_2k\". Then install in any directory, for example \"C:\\OpenSSLWin64\"  Step 2: Access \"C:\\OpenSSLWin64\\bin\" then open the command prompt. Type the command to declare the environment config.  set OPENSSL_CONF=C:\\OpenSSL-Win64\\bin\\openssl.cfg  Step 3: Generate private key and public key  openssl genrsa -aes256 -out c:\\opensslkeys\\partner\\partner_privatekey.pem 2048  openssl rsa –in c:\\opensslkeys\\partner\\partner_privatekey.pem -pubout >c:\\opensslkeys\\partner\\partner_publickey.pem  After successful pairing, Partner will send back to Baokim the public key to authenticate the signature that the Partner sends via the API
 *
 * OpenAPI spec version: 1.0.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using RestSharp;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace IO.Swagger.Api
{
    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
        public interface ICheckInstallmentSupportApi : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// https::devtest.baokim.vn/api/v1/partner/installment
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Process:

 MERCHANT sends customer&#x27;s card information such as: card&#x27;s issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM (optional)</param>
        /// <returns>InlineResponse200</returns>
        InlineResponse200 ApiV1PartnerCheckInstallmentPost (PartnerCheckinstallmentBody body = null);

        /// <summary>
        /// https::devtest.baokim.vn/api/v1/partner/installment
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Process:

 MERCHANT sends customer&#x27;s card information such as: card&#x27;s issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM (optional)</param>
        /// <returns>ApiResponse of InlineResponse200</returns>
        ApiResponse<InlineResponse200> ApiV1PartnerCheckInstallmentPostWithHttpInfo (PartnerCheckinstallmentBody body = null);
        #endregion Synchronous Operations
        #region Asynchronous Operations
        /// <summary>
        /// https::devtest.baokim.vn/api/v1/partner/installment
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Process:

 MERCHANT sends customer&#x27;s card information such as: card&#x27;s issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM (optional)</param>
        /// <returns>Task of InlineResponse200</returns>
        System.Threading.Tasks.Task<InlineResponse200> ApiV1PartnerCheckInstallmentPostAsync (PartnerCheckinstallmentBody body = null);

        /// <summary>
        /// https::devtest.baokim.vn/api/v1/partner/installment
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Process:

 MERCHANT sends customer&#x27;s card information such as: card&#x27;s issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM (optional)</param>
        /// <returns>Task of ApiResponse (InlineResponse200)</returns>
        System.Threading.Tasks.Task<ApiResponse<InlineResponse200>> ApiV1PartnerCheckInstallmentPostAsyncWithHttpInfo (PartnerCheckinstallmentBody body = null);
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
        public partial class CheckInstallmentSupportApi : ICheckInstallmentSupportApi
    {
        private IO.Swagger.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="CheckInstallmentSupportApi"/> class.
        /// </summary>
        /// <returns></returns>
        public CheckInstallmentSupportApi(String basePath)
        {
            this.Configuration = new IO.Swagger.Client.Configuration { BasePath = basePath };

            ExceptionFactory = IO.Swagger.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="CheckInstallmentSupportApi"/> class
        /// </summary>
        /// <returns></returns>
        public CheckInstallmentSupportApi()
        {
            this.Configuration = IO.Swagger.Client.Configuration.Default;

            ExceptionFactory = IO.Swagger.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="CheckInstallmentSupportApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public CheckInstallmentSupportApi(IO.Swagger.Client.Configuration configuration = null)
        {
            if (configuration == null) // use the default one in Configuration
                this.Configuration = IO.Swagger.Client.Configuration.Default;
            else
                this.Configuration = configuration;

            ExceptionFactory = IO.Swagger.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Gets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        public String GetBasePath()
        {
            return this.Configuration.ApiClient.RestClient.BaseUrl.ToString();
        }

        /// <summary>
        /// Sets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        [Obsolete("SetBasePath is deprecated, please do 'Configuration.ApiClient = new ApiClient(\"http://new-path\")' instead.")]
        public void SetBasePath(String basePath)
        {
            // do nothing
        }

        /// <summary>
        /// Gets or sets the configuration object
        /// </summary>
        /// <value>An instance of the Configuration</value>
        public IO.Swagger.Client.Configuration Configuration {get; set;}

        /// <summary>
        /// Provides a factory method hook for the creation of exceptions.
        /// </summary>
        public IO.Swagger.Client.ExceptionFactory ExceptionFactory
        {
            get
            {
                if (_exceptionFactory != null && _exceptionFactory.GetInvocationList().Length > 1)
                {
                    throw new InvalidOperationException("Multicast delegate for ExceptionFactory is unsupported.");
                }
                return _exceptionFactory;
            }
            set { _exceptionFactory = value; }
        }

        /// <summary>
        /// Gets the default header.
        /// </summary>
        /// <returns>Dictionary of HTTP header</returns>
        [Obsolete("DefaultHeader is deprecated, please use Configuration.DefaultHeader instead.")]
        public IDictionary<String, String> DefaultHeader()
        {
            return new ReadOnlyDictionary<string, string>(this.Configuration.DefaultHeader);
        }

        /// <summary>
        /// Add default header.
        /// </summary>
        /// <param name="key">Header field name.</param>
        /// <param name="value">Header field value.</param>
        /// <returns></returns>
        [Obsolete("AddDefaultHeader is deprecated, please use Configuration.AddDefaultHeader instead.")]
        public void AddDefaultHeader(string key, string value)
        {
            this.Configuration.AddDefaultHeader(key, value);
        }

        /// <summary>
        /// https::devtest.baokim.vn/api/v1/partner/installment 
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Process:

 MERCHANT sends customer&#x27;s card information such as: card&#x27;s issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM (optional)</param>
        /// <returns>InlineResponse200</returns>
        public InlineResponse200 ApiV1PartnerCheckInstallmentPost (PartnerCheckinstallmentBody body = null)
        {
             ApiResponse<InlineResponse200> localVarResponse = ApiV1PartnerCheckInstallmentPostWithHttpInfo(body);
             return localVarResponse.Data;
        }

        /// <summary>
        /// https::devtest.baokim.vn/api/v1/partner/installment 
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Process:

 MERCHANT sends customer&#x27;s card information such as: card&#x27;s issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM (optional)</param>
        /// <returns>ApiResponse of InlineResponse200</returns>
        public ApiResponse< InlineResponse200 > ApiV1PartnerCheckInstallmentPostWithHttpInfo (PartnerCheckinstallmentBody body = null)
        {

            var localVarPath = "/api/v1/partner/check-installment";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
                "application/json"
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (body != null && body.GetType() != typeof(byte[]))
            {
                localVarPostBody = this.Configuration.ApiClient.Serialize(body); // http body (model) parameter
            }
            else
            {
                localVarPostBody = body; // byte array
            }

            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.POST, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("ApiV1PartnerCheckInstallmentPost", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<InlineResponse200>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (InlineResponse200) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(InlineResponse200)));
        }

        /// <summary>
        /// https::devtest.baokim.vn/api/v1/partner/installment 
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Process:

 MERCHANT sends customer&#x27;s card information such as: card&#x27;s issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM (optional)</param>
        /// <returns>Task of InlineResponse200</returns>
        public async System.Threading.Tasks.Task<InlineResponse200> ApiV1PartnerCheckInstallmentPostAsync (PartnerCheckinstallmentBody body = null)
        {
             ApiResponse<InlineResponse200> localVarResponse = await ApiV1PartnerCheckInstallmentPostAsyncWithHttpInfo(body);
             return localVarResponse.Data;

        }

        /// <summary>
        /// https::devtest.baokim.vn/api/v1/partner/installment 
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Process:

 MERCHANT sends customer&#x27;s card information such as: card&#x27;s issuing bank code and card number (first 6 + last 4, first 7 + last 4 digits for Express cards of Acb with prefix 9704163) to BAOKIM (optional)</param>
        /// <returns>Task of ApiResponse (InlineResponse200)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<InlineResponse200>> ApiV1PartnerCheckInstallmentPostAsyncWithHttpInfo (PartnerCheckinstallmentBody body = null)
        {

            var localVarPath = "/api/v1/partner/check-installment";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
                "application/json"
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (body != null && body.GetType() != typeof(byte[]))
            {
                localVarPostBody = this.Configuration.ApiClient.Serialize(body); // http body (model) parameter
            }
            else
            {
                localVarPostBody = body; // byte array
            }

            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.POST, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("ApiV1PartnerCheckInstallmentPost", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<InlineResponse200>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (InlineResponse200) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(InlineResponse200)));
        }

    }
}