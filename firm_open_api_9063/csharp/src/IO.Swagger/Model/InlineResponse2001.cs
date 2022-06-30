/* 
 *  Disbursement payments API
 *
 * <h2>Introduction</h2> Welcome! Baokim’s mission is to deliver automated payment infrastructure solutions for your business. We help with both money in (collection payments) and money out (disbursement payments). Our users range from platforms businesses, fintech, e-Commerce, and everything else in between.  <p><strong>Benefits of Baokim</strong></p> Fast integration  Instant transfers  Daily reconciliation  Simple & competitive pricing – no hidden fees  <h2>Regulations and requirements</h2>   - API that Baokim deployed, will be built on the Restful architecture, data transmission between the two sides will be Json.  - Baokim will restrict access to the API by one or more IPs based on each Partner. So before joining , Partner will send the IP list to Baokim to open the access.  - Baokim uses Basic Authentication to allow access to the API. Account information will be provided by Bao Kim at the start of the integration.  <code>Authorization: Basic YmFva2ltOmJrQDEyMzQ1Ng==</code>  <h2>Restful and Digital Signature</h2> <p><strong>Restfull Web Service</strong></p> REST (Representational State Transfer) has been widely adopted instead of Web services based on SOAP and WSDL. REST defines architectural rules for designing Web services that focus on system resources, including how resource states are formatted and transported via HTTP through a large number of users and are written by different languages.  In order to be able to connect REST with the tool and test with BAOKIM, the PARTNER can load and use one of the following two universal tools:  - Postman: https://www.getpostman.com  - Soap UI: https://www.soapui.org  <p><strong>Digital signature</strong></p>  <img src=\"https://thuchiho.baokim.vn/assets/docs/img/sign_model.jpg\" alt=\"Model Sign\">   <p><strong>Private key and public key</strong></p> Baokim is currently using digital signature by RSA-SHA1  There are several ways to generate RSA key pairs.  <strong>Way 1</strong>:  Generate your RSA key pairs online: Generate now  <strong>Way 2</strong>:  Using OpenSSL software for Windows:  <strong>Step 1</strong>: Download the software at:  http://slproweb.com/products/Win32OpenSSL.html. Partner should download the installer \"OpenSSL_Light-1_0_2k\". Then install in any directory, for example \"C:\\OpenSSLWin64\"  <strong>Step 2</strong>: Access \"C:\\OpenSSLWin64\\bin\" then open the command prompt. Type the command to declare the environment config.  set OPENSSL_CONF=C:\\OpenSSL-Win64\\bin\\openssl.cfg  <strong>Step 3</strong>: Generate private key and public key  openssl genrsa -aes256 -out c:\\opensslkeys\\partner\\partner_privatekey.pem 2048  openssl rsa –in c:\\opensslkeys\\partner\\partner_privatekey.pem -pubout >c:\\opensslkeys\\partner\\partner_publickey.pem  After successful pairing, Partner will send back to Baokim the public key to authenticate the signature that the Partner sends via the API.  <h3>Describe the mechanism handling the transaction timeout</h3> Due to traffic problems or during request processing at Baokim, transaction timeout may be generated. Baokim will describe the processing mechanism consists of two cases as follows:  <strong>Case 1</strong>: Baokim proactively returns error code timeout, error code <b>99</b>  - This case occurs when the two parties set the maximum time to return the results for a transaction but for some reason the Baokim or Bank has not finished processing should be proactive return error code timeout  - The way to deal with this situation: Partner when receiving the timeout error code will call the check transaction status. In this function Baokim will return the transaction status for Partner.  <strong>Case 2</strong>: Timeout due to transmission line failure, does not get the result returned  In this case it is possible to timeout from Partner-> Baokim or Baokim-> Partner. So can not determine whether the transaction Baokim reception or not.  - The way to deal with this situation:  1. The Partner will call Check Transaction Status to look up transaction status. If the result is received then the Partner will update the partner status. If timeout is still the case then move on to step 2.  2. In cases where transmission lines meet with long incidents, Baokim and Partner will coordinate with human handling to certification. Partner will email to Baokim to request sending status for a transaction, the Baokim's technique will confirm the status and return to Partner.   <h2>List of bank transfer assistance. </h2>  <table>                     <thead>                         <tr> <th>#</th> <th>BankNo</th> <th>BankName</th> <th>Account</th> <th>Card</th>                         </tr>                     </thead>                     <tbody>                         <tr> <td>1</td> <td>970423</td> <td>TIEN PHONG COMMERCIAL JOINT STOCK BANK</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>2</td> <td>970437</td> <td>Ho Chi Minh City Development Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>3</td> <td>970408</td> <td>Global Petro Sole Member LimitedCommercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>4</td> <td>970407</td> <td>Vietnam Technological and Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>5</td> <td>970442</td> <td>Hong Leong Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>6</td> <td>970414</td> <td>Ocean Commercial Joint - Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>7</td> <td>970438</td> <td>Bao Viet Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>8</td> <td>970422</td> <td>Military Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>9</td> <td>970432</td> <td>Vietnam Prosperity Joint-Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>10</td> <td>970439</td> <td>Public Bank Vietnam Limited (PBVN)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>11</td> <td>970415</td> <td>VIETNAM JOINT STOCK COMMERCIAL BANK FOR INDUSTRY AND TRADE (Viettinbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>12</td> <td>970431</td> <td>VIETNAM EXPORT IMPORT COMMERCIAL JOINT STOCK BANK (Eximbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>13</td> <td>970440</td> <td>Southeast Asia Commercial Joint Stock Bank (SeABank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>14</td> <td>970429</td> <td>Sai Gon Joint StockCommercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>15</td> <td>970448</td> <td>Orient Commercial Joint StockBank (OCB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>16</td> <td>970425</td> <td>An BinhCommercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>17</td> <td>970426</td> <td>Vietnam Maritime Commercial Stock Bank (MSB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>18</td> <td>970427</td> <td>Vietnam Asia Commercial Joint Stock Bank (VietA)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>19</td> <td>970419</td> <td>National Citizen Commercial Joint Stock Bank (NCB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>20</td> <td>970418</td> <td>Joint Stock Commercial Bank for Investment and Development of Vietnam (BIDV)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>21</td> <td>970443</td> <td>Sai Gon- Ha Noi Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>22</td> <td>970406</td> <td>DongA Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>23</td> <td>970441</td> <td>Vietnam International Commercial Joint Stock Bank (VIB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>24</td> <td>970424</td> <td>Shinhan Bank Vietnam Limited</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>25</td> <td>970433</td> <td>Vietnam Thuong Tin Commercial Joint Stock Bank (Vietbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>26</td> <td>970454</td> <td>VIET CAPITAL COMMERCIAL JOINT STOCK BANK (Ban Viet)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>27</td> <td>970452</td> <td>Kien Long Commercial Joint -Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>28</td> <td>970430</td> <td>PETROLIMEX GROUPCOMMERCIAL JOINT STOCK BANK</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>29</td> <td>970400</td> <td>Sai Gon Joint Stock Commercial Bank (Saigon Bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>30</td> <td>970405</td> <td>Vietnam Bank for Agriculture and Rural Development or Agribank (Agribank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>31</td> <td>970403</td> <td>Sacombank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>32</td> <td>970412</td> <td>Vietnam Public Joint Stock Commercial Bank (Vietnam dai chung)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>33</td> <td>970421</td> <td>Vietnam-Russia Joint Venture Bank - VRB</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>34</td> <td>970428</td> <td>Nam A Commercial Joint Stock Bank (Nam A Bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>35</td> <td>970434</td> <td>Indovina Bank Ltd</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>36</td> <td>970449</td> <td>LienViet Post Joint Stock Commercial Bank (LienViet Post bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>37</td> <td>970457</td> <td>Woori Bank Vietnam Limited</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>38</td> <td>970436</td> <td>Joint Stock Commercial Bank for Foreign Trade of Vietnam (Vietcombank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>39</td> <td>970416</td> <td>Asia Commercial Joint Stock Bank</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>40</td> <td>970458</td> <td>UNITED OVERSEAS BANK (VIETNAM) LIMITED</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>41</td> <td>970446</td> <td>Co-operative bank of VietNam</td> <td></td> <td>✓</td>                         </tr>                         <tr> <td>42</td> <td>970455</td> <td>Industrial Bank of Korea - Ha Noi Branch</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>43</td> <td>970409</td> <td>North Asia Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>44</td> <td>422589</td> <td>CIMB Bank (Vietnam) Limited</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>45</td> <td>796500</td> <td>Ngân hàng DBS - Chi nhánh Hồ Chí Minh(DBS)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>46</td> <td>458761</td> <td>TNHH MTV HSBC Việt Nam(HSBC)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>47</td> <td>970410</td> <td>TNHH MTV Standard Chartered Việt Nam(SCVN)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>48</td> <td>801011</td> <td>Nonghuyp - Chi nhánh Hà Nội(NHB)</td> <td>✓</td> <td></td>                         </tr>  <td>49</td> <td>970444</td> <td>TM TNHH MTV Xây Dựng Việt Nam </td> <td>✓</td> <td></td>                         </tr><tr> <td>50</td> <td>970456</td> <td> IBK - chi nhánh HCM</td> <td>✓</td> <td></td>                         </tr><tr> <td>51</td> <td>970462</td> <td>Kookmin - Chi nhánh Hà Nội</td> <td>✓</td> <td>✓</td>                         </tr><tr> <td>52</td> <td>970463</td> <td>Kookmin - Chi nhánh Thành phố Hồ Chí Minh</td> <td>✓</td> <td>✓</td>                         </tr><tr> <td>53</td> <td>546034</td> <td>Ngân hàng số CAKE by VPBank</td> <td>✓</td> <td></td>                         </tr><tr> <td>54</td> <td>546035</td> <td>Ngân hàng số Ubank by VPBank</td> <td>✓</td> <td></td>                   </tbody>                 </table>
 *
 * OpenAPI spec version: 1.0.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// InlineResponse2001
    /// </summary>
    [DataContract]
        public partial class InlineResponse2001 :  IEquatable<InlineResponse2001>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="InlineResponse2001" /> class.
        /// </summary>
        /// <param name="responseCode">200 : Successful. &lt;br&gt; 99 : Transaction timeout.&lt;br&gt; 11 : Failed.&lt;br&gt; 101 : Error processing from Baokim.&lt;br&gt; 102 : Duplicated RequestId.&lt;br&gt; 103 : Incorrect signature.&lt;br&gt; 110 : Incorrect PartnerCode.&lt;br&gt; 111 : PartnerCode deleted from the system.&lt;br&gt; 112 : PartnerCode not yet activated.&lt;br&gt; 113 : Operation code is required.&lt;br&gt; 114 : Incorrect Operation code.&lt;br&gt; 115 : BankID is required.&lt;br&gt; 116 : BankID not supported.&lt;br&gt; 117 : Account no. /Card no. should be from 6-22 characters in length.&lt;br&gt; 118 : Invalid account no./Card no..&lt;br&gt; 119 : Account no./Card no. does not exist.&lt;br&gt; 120 : Incorrect account type.&lt;br&gt; 121 : Transaction ID sent from Partner is required.&lt;br&gt; 122 : Transaction ID sent by Partner is existing.&lt;br&gt; 123 : Transaction unfound.&lt;br&gt; 124 : Transfer amount required.&lt;br&gt; 125 : Invalid transfer amount.&lt;br&gt; 126 : Error processing between Baokim and bank.&lt;br&gt; 127 : Error connecting to bank.&lt;br&gt; 128 : Error processing from bank.&lt;br&gt; 129 : Insufficient disbursement limit or expired guarantee period.&lt;br&gt; 130 : Exceeded transfer limit on day.&lt;br&gt;.</param>
        /// <param name="responseMessage">Description for return status.</param>
        /// <param name="referenceId">Partner information posted.</param>
        /// <param name="transactionId">Transaction code recorded side Baokim.</param>
        /// <param name="transactionTime">Finishing time side Baokim. Format YYYY-MM-DD.</param>
        /// <param name="bankNo">Partner information posted.</param>
        /// <param name="accNo">Partner information posted.</param>
        /// <param name="accName">Full name of the recipient, may or may not, depending on the time.</param>
        /// <param name="accType">Partner information posted.</param>
        /// <param name="requestAmount">Partner information posted.</param>
        /// <param name="transferAmount">The actual amount transferred to the recipient. Will be less if the remittance.</param>
        /// <param name="affterBalance">Current balance of investors.</param>
        /// <param name="afterDisbursementDay">Continue disbursement amount (in limit).</param>
        /// <param name="signature">BAOKIM will sign by digital signature of response data. Structured data: ResponseCode|ResponseMessage| RequestId | PartnerCode | Available | Holding.</param>
        public InlineResponse2001(int? responseCode = default(int?), string responseMessage = default(string), string referenceId = default(string), string transactionId = default(string), string transactionTime = default(string), string bankNo = default(string), string accNo = default(string), string accName = default(string), string accType = default(string), int? requestAmount = default(int?), int? transferAmount = default(int?), int? affterBalance = default(int?), int? afterDisbursementDay = default(int?), string signature = default(string))
        {
            this.ResponseCode = responseCode;
            this.ResponseMessage = responseMessage;
            this.ReferenceId = referenceId;
            this.TransactionId = transactionId;
            this.TransactionTime = transactionTime;
            this.BankNo = bankNo;
            this.AccNo = accNo;
            this.AccName = accName;
            this.AccType = accType;
            this.RequestAmount = requestAmount;
            this.TransferAmount = transferAmount;
            this.AffterBalance = affterBalance;
            this.AfterDisbursementDay = afterDisbursementDay;
            this.Signature = signature;
        }
        
        /// <summary>
        /// 200 : Successful. &lt;br&gt; 99 : Transaction timeout.&lt;br&gt; 11 : Failed.&lt;br&gt; 101 : Error processing from Baokim.&lt;br&gt; 102 : Duplicated RequestId.&lt;br&gt; 103 : Incorrect signature.&lt;br&gt; 110 : Incorrect PartnerCode.&lt;br&gt; 111 : PartnerCode deleted from the system.&lt;br&gt; 112 : PartnerCode not yet activated.&lt;br&gt; 113 : Operation code is required.&lt;br&gt; 114 : Incorrect Operation code.&lt;br&gt; 115 : BankID is required.&lt;br&gt; 116 : BankID not supported.&lt;br&gt; 117 : Account no. /Card no. should be from 6-22 characters in length.&lt;br&gt; 118 : Invalid account no./Card no..&lt;br&gt; 119 : Account no./Card no. does not exist.&lt;br&gt; 120 : Incorrect account type.&lt;br&gt; 121 : Transaction ID sent from Partner is required.&lt;br&gt; 122 : Transaction ID sent by Partner is existing.&lt;br&gt; 123 : Transaction unfound.&lt;br&gt; 124 : Transfer amount required.&lt;br&gt; 125 : Invalid transfer amount.&lt;br&gt; 126 : Error processing between Baokim and bank.&lt;br&gt; 127 : Error connecting to bank.&lt;br&gt; 128 : Error processing from bank.&lt;br&gt; 129 : Insufficient disbursement limit or expired guarantee period.&lt;br&gt; 130 : Exceeded transfer limit on day.&lt;br&gt;
        /// </summary>
        /// <value>200 : Successful. &lt;br&gt; 99 : Transaction timeout.&lt;br&gt; 11 : Failed.&lt;br&gt; 101 : Error processing from Baokim.&lt;br&gt; 102 : Duplicated RequestId.&lt;br&gt; 103 : Incorrect signature.&lt;br&gt; 110 : Incorrect PartnerCode.&lt;br&gt; 111 : PartnerCode deleted from the system.&lt;br&gt; 112 : PartnerCode not yet activated.&lt;br&gt; 113 : Operation code is required.&lt;br&gt; 114 : Incorrect Operation code.&lt;br&gt; 115 : BankID is required.&lt;br&gt; 116 : BankID not supported.&lt;br&gt; 117 : Account no. /Card no. should be from 6-22 characters in length.&lt;br&gt; 118 : Invalid account no./Card no..&lt;br&gt; 119 : Account no./Card no. does not exist.&lt;br&gt; 120 : Incorrect account type.&lt;br&gt; 121 : Transaction ID sent from Partner is required.&lt;br&gt; 122 : Transaction ID sent by Partner is existing.&lt;br&gt; 123 : Transaction unfound.&lt;br&gt; 124 : Transfer amount required.&lt;br&gt; 125 : Invalid transfer amount.&lt;br&gt; 126 : Error processing between Baokim and bank.&lt;br&gt; 127 : Error connecting to bank.&lt;br&gt; 128 : Error processing from bank.&lt;br&gt; 129 : Insufficient disbursement limit or expired guarantee period.&lt;br&gt; 130 : Exceeded transfer limit on day.&lt;br&gt;</value>
        [DataMember(Name="ResponseCode", EmitDefaultValue=false)]
        public int? ResponseCode { get; set; }

        /// <summary>
        /// Description for return status
        /// </summary>
        /// <value>Description for return status</value>
        [DataMember(Name="ResponseMessage", EmitDefaultValue=false)]
        public string ResponseMessage { get; set; }

        /// <summary>
        /// Partner information posted
        /// </summary>
        /// <value>Partner information posted</value>
        [DataMember(Name="ReferenceId", EmitDefaultValue=false)]
        public string ReferenceId { get; set; }

        /// <summary>
        /// Transaction code recorded side Baokim
        /// </summary>
        /// <value>Transaction code recorded side Baokim</value>
        [DataMember(Name="TransactionId", EmitDefaultValue=false)]
        public string TransactionId { get; set; }

        /// <summary>
        /// Finishing time side Baokim. Format YYYY-MM-DD
        /// </summary>
        /// <value>Finishing time side Baokim. Format YYYY-MM-DD</value>
        [DataMember(Name="TransactionTime", EmitDefaultValue=false)]
        public string TransactionTime { get; set; }

        /// <summary>
        /// Partner information posted
        /// </summary>
        /// <value>Partner information posted</value>
        [DataMember(Name="BankNo", EmitDefaultValue=false)]
        public string BankNo { get; set; }

        /// <summary>
        /// Partner information posted
        /// </summary>
        /// <value>Partner information posted</value>
        [DataMember(Name="AccNo", EmitDefaultValue=false)]
        public string AccNo { get; set; }

        /// <summary>
        /// Full name of the recipient, may or may not, depending on the time
        /// </summary>
        /// <value>Full name of the recipient, may or may not, depending on the time</value>
        [DataMember(Name="AccName", EmitDefaultValue=false)]
        public string AccName { get; set; }

        /// <summary>
        /// Partner information posted
        /// </summary>
        /// <value>Partner information posted</value>
        [DataMember(Name="AccType", EmitDefaultValue=false)]
        public string AccType { get; set; }

        /// <summary>
        /// Partner information posted
        /// </summary>
        /// <value>Partner information posted</value>
        [DataMember(Name="RequestAmount", EmitDefaultValue=false)]
        public int? RequestAmount { get; set; }

        /// <summary>
        /// The actual amount transferred to the recipient. Will be less if the remittance
        /// </summary>
        /// <value>The actual amount transferred to the recipient. Will be less if the remittance</value>
        [DataMember(Name="TransferAmount", EmitDefaultValue=false)]
        public int? TransferAmount { get; set; }

        /// <summary>
        /// Current balance of investors
        /// </summary>
        /// <value>Current balance of investors</value>
        [DataMember(Name="AffterBalance", EmitDefaultValue=false)]
        public int? AffterBalance { get; set; }

        /// <summary>
        /// Continue disbursement amount (in limit)
        /// </summary>
        /// <value>Continue disbursement amount (in limit)</value>
        [DataMember(Name="AfterDisbursementDay", EmitDefaultValue=false)]
        public int? AfterDisbursementDay { get; set; }

        /// <summary>
        /// BAOKIM will sign by digital signature of response data. Structured data: ResponseCode|ResponseMessage| RequestId | PartnerCode | Available | Holding
        /// </summary>
        /// <value>BAOKIM will sign by digital signature of response data. Structured data: ResponseCode|ResponseMessage| RequestId | PartnerCode | Available | Holding</value>
        [DataMember(Name="Signature", EmitDefaultValue=false)]
        public string Signature { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class InlineResponse2001 {\n");
            sb.Append("  ResponseCode: ").Append(ResponseCode).Append("\n");
            sb.Append("  ResponseMessage: ").Append(ResponseMessage).Append("\n");
            sb.Append("  ReferenceId: ").Append(ReferenceId).Append("\n");
            sb.Append("  TransactionId: ").Append(TransactionId).Append("\n");
            sb.Append("  TransactionTime: ").Append(TransactionTime).Append("\n");
            sb.Append("  BankNo: ").Append(BankNo).Append("\n");
            sb.Append("  AccNo: ").Append(AccNo).Append("\n");
            sb.Append("  AccName: ").Append(AccName).Append("\n");
            sb.Append("  AccType: ").Append(AccType).Append("\n");
            sb.Append("  RequestAmount: ").Append(RequestAmount).Append("\n");
            sb.Append("  TransferAmount: ").Append(TransferAmount).Append("\n");
            sb.Append("  AffterBalance: ").Append(AffterBalance).Append("\n");
            sb.Append("  AfterDisbursementDay: ").Append(AfterDisbursementDay).Append("\n");
            sb.Append("  Signature: ").Append(Signature).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as InlineResponse2001);
        }

        /// <summary>
        /// Returns true if InlineResponse2001 instances are equal
        /// </summary>
        /// <param name="input">Instance of InlineResponse2001 to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(InlineResponse2001 input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.ResponseCode == input.ResponseCode ||
                    (this.ResponseCode != null &&
                    this.ResponseCode.Equals(input.ResponseCode))
                ) && 
                (
                    this.ResponseMessage == input.ResponseMessage ||
                    (this.ResponseMessage != null &&
                    this.ResponseMessage.Equals(input.ResponseMessage))
                ) && 
                (
                    this.ReferenceId == input.ReferenceId ||
                    (this.ReferenceId != null &&
                    this.ReferenceId.Equals(input.ReferenceId))
                ) && 
                (
                    this.TransactionId == input.TransactionId ||
                    (this.TransactionId != null &&
                    this.TransactionId.Equals(input.TransactionId))
                ) && 
                (
                    this.TransactionTime == input.TransactionTime ||
                    (this.TransactionTime != null &&
                    this.TransactionTime.Equals(input.TransactionTime))
                ) && 
                (
                    this.BankNo == input.BankNo ||
                    (this.BankNo != null &&
                    this.BankNo.Equals(input.BankNo))
                ) && 
                (
                    this.AccNo == input.AccNo ||
                    (this.AccNo != null &&
                    this.AccNo.Equals(input.AccNo))
                ) && 
                (
                    this.AccName == input.AccName ||
                    (this.AccName != null &&
                    this.AccName.Equals(input.AccName))
                ) && 
                (
                    this.AccType == input.AccType ||
                    (this.AccType != null &&
                    this.AccType.Equals(input.AccType))
                ) && 
                (
                    this.RequestAmount == input.RequestAmount ||
                    (this.RequestAmount != null &&
                    this.RequestAmount.Equals(input.RequestAmount))
                ) && 
                (
                    this.TransferAmount == input.TransferAmount ||
                    (this.TransferAmount != null &&
                    this.TransferAmount.Equals(input.TransferAmount))
                ) && 
                (
                    this.AffterBalance == input.AffterBalance ||
                    (this.AffterBalance != null &&
                    this.AffterBalance.Equals(input.AffterBalance))
                ) && 
                (
                    this.AfterDisbursementDay == input.AfterDisbursementDay ||
                    (this.AfterDisbursementDay != null &&
                    this.AfterDisbursementDay.Equals(input.AfterDisbursementDay))
                ) && 
                (
                    this.Signature == input.Signature ||
                    (this.Signature != null &&
                    this.Signature.Equals(input.Signature))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.ResponseCode != null)
                    hashCode = hashCode * 59 + this.ResponseCode.GetHashCode();
                if (this.ResponseMessage != null)
                    hashCode = hashCode * 59 + this.ResponseMessage.GetHashCode();
                if (this.ReferenceId != null)
                    hashCode = hashCode * 59 + this.ReferenceId.GetHashCode();
                if (this.TransactionId != null)
                    hashCode = hashCode * 59 + this.TransactionId.GetHashCode();
                if (this.TransactionTime != null)
                    hashCode = hashCode * 59 + this.TransactionTime.GetHashCode();
                if (this.BankNo != null)
                    hashCode = hashCode * 59 + this.BankNo.GetHashCode();
                if (this.AccNo != null)
                    hashCode = hashCode * 59 + this.AccNo.GetHashCode();
                if (this.AccName != null)
                    hashCode = hashCode * 59 + this.AccName.GetHashCode();
                if (this.AccType != null)
                    hashCode = hashCode * 59 + this.AccType.GetHashCode();
                if (this.RequestAmount != null)
                    hashCode = hashCode * 59 + this.RequestAmount.GetHashCode();
                if (this.TransferAmount != null)
                    hashCode = hashCode * 59 + this.TransferAmount.GetHashCode();
                if (this.AffterBalance != null)
                    hashCode = hashCode * 59 + this.AffterBalance.GetHashCode();
                if (this.AfterDisbursementDay != null)
                    hashCode = hashCode * 59 + this.AfterDisbursementDay.GetHashCode();
                if (this.Signature != null)
                    hashCode = hashCode * 59 + this.Signature.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }
}
