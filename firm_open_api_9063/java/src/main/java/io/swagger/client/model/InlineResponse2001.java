/*
 *  Disbursement payments API
 * <h2>Introduction</h2> Welcome! Baokim’s mission is to deliver automated payment infrastructure solutions for your business. We help with both money in (collection payments) and money out (disbursement payments). Our users range from platforms businesses, fintech, e-Commerce, and everything else in between.  <p><strong>Benefits of Baokim</strong></p> Fast integration  Instant transfers  Daily reconciliation  Simple & competitive pricing – no hidden fees  <h2>Regulations and requirements</h2>   - API that Baokim deployed, will be built on the Restful architecture, data transmission between the two sides will be Json.  - Baokim will restrict access to the API by one or more IPs based on each Partner. So before joining , Partner will send the IP list to Baokim to open the access.  - Baokim uses Basic Authentication to allow access to the API. Account information will be provided by Bao Kim at the start of the integration.  <code>Authorization: Basic YmFva2ltOmJrQDEyMzQ1Ng==</code>  <h2>Restful and Digital Signature</h2> <p><strong>Restfull Web Service</strong></p> REST (Representational State Transfer) has been widely adopted instead of Web services based on SOAP and WSDL. REST defines architectural rules for designing Web services that focus on system resources, including how resource states are formatted and transported via HTTP through a large number of users and are written by different languages.  In order to be able to connect REST with the tool and test with BAOKIM, the PARTNER can load and use one of the following two universal tools:  - Postman: https://www.getpostman.com  - Soap UI: https://www.soapui.org  <p><strong>Digital signature</strong></p>  <img src=\"https://thuchiho.baokim.vn/assets/docs/img/sign_model.jpg\" alt=\"Model Sign\">   <p><strong>Private key and public key</strong></p> Baokim is currently using digital signature by RSA-SHA1  There are several ways to generate RSA key pairs.  <strong>Way 1</strong>:  Generate your RSA key pairs online: Generate now  <strong>Way 2</strong>:  Using OpenSSL software for Windows:  <strong>Step 1</strong>: Download the software at:  http://slproweb.com/products/Win32OpenSSL.html. Partner should download the installer \"OpenSSL_Light-1_0_2k\". Then install in any directory, for example \"C:\\OpenSSLWin64\"  <strong>Step 2</strong>: Access \"C:\\OpenSSLWin64\\bin\" then open the command prompt. Type the command to declare the environment config.  set OPENSSL_CONF=C:\\OpenSSL-Win64\\bin\\openssl.cfg  <strong>Step 3</strong>: Generate private key and public key  openssl genrsa -aes256 -out c:\\opensslkeys\\partner\\partner_privatekey.pem 2048  openssl rsa –in c:\\opensslkeys\\partner\\partner_privatekey.pem -pubout >c:\\opensslkeys\\partner\\partner_publickey.pem  After successful pairing, Partner will send back to Baokim the public key to authenticate the signature that the Partner sends via the API.  <h3>Describe the mechanism handling the transaction timeout</h3> Due to traffic problems or during request processing at Baokim, transaction timeout may be generated. Baokim will describe the processing mechanism consists of two cases as follows:  <strong>Case 1</strong>: Baokim proactively returns error code timeout, error code <b>99</b>  - This case occurs when the two parties set the maximum time to return the results for a transaction but for some reason the Baokim or Bank has not finished processing should be proactive return error code timeout  - The way to deal with this situation: Partner when receiving the timeout error code will call the check transaction status. In this function Baokim will return the transaction status for Partner.  <strong>Case 2</strong>: Timeout due to transmission line failure, does not get the result returned  In this case it is possible to timeout from Partner-> Baokim or Baokim-> Partner. So can not determine whether the transaction Baokim reception or not.  - The way to deal with this situation:  1. The Partner will call Check Transaction Status to look up transaction status. If the result is received then the Partner will update the partner status. If timeout is still the case then move on to step 2.  2. In cases where transmission lines meet with long incidents, Baokim and Partner will coordinate with human handling to certification. Partner will email to Baokim to request sending status for a transaction, the Baokim's technique will confirm the status and return to Partner.   <h2>List of bank transfer assistance. </h2>  <table>                     <thead>                         <tr> <th>#</th> <th>BankNo</th> <th>BankName</th> <th>Account</th> <th>Card</th>                         </tr>                     </thead>                     <tbody>                         <tr> <td>1</td> <td>970423</td> <td>TIEN PHONG COMMERCIAL JOINT STOCK BANK</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>2</td> <td>970437</td> <td>Ho Chi Minh City Development Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>3</td> <td>970408</td> <td>Global Petro Sole Member LimitedCommercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>4</td> <td>970407</td> <td>Vietnam Technological and Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>5</td> <td>970442</td> <td>Hong Leong Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>6</td> <td>970414</td> <td>Ocean Commercial Joint - Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>7</td> <td>970438</td> <td>Bao Viet Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>8</td> <td>970422</td> <td>Military Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>9</td> <td>970432</td> <td>Vietnam Prosperity Joint-Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>10</td> <td>970439</td> <td>Public Bank Vietnam Limited (PBVN)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>11</td> <td>970415</td> <td>VIETNAM JOINT STOCK COMMERCIAL BANK FOR INDUSTRY AND TRADE (Viettinbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>12</td> <td>970431</td> <td>VIETNAM EXPORT IMPORT COMMERCIAL JOINT STOCK BANK (Eximbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>13</td> <td>970440</td> <td>Southeast Asia Commercial Joint Stock Bank (SeABank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>14</td> <td>970429</td> <td>Sai Gon Joint StockCommercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>15</td> <td>970448</td> <td>Orient Commercial Joint StockBank (OCB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>16</td> <td>970425</td> <td>An BinhCommercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>17</td> <td>970426</td> <td>Vietnam Maritime Commercial Stock Bank (MSB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>18</td> <td>970427</td> <td>Vietnam Asia Commercial Joint Stock Bank (VietA)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>19</td> <td>970419</td> <td>National Citizen Commercial Joint Stock Bank (NCB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>20</td> <td>970418</td> <td>Joint Stock Commercial Bank for Investment and Development of Vietnam (BIDV)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>21</td> <td>970443</td> <td>Sai Gon- Ha Noi Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>22</td> <td>970406</td> <td>DongA Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>23</td> <td>970441</td> <td>Vietnam International Commercial Joint Stock Bank (VIB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>24</td> <td>970424</td> <td>Shinhan Bank Vietnam Limited</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>25</td> <td>970433</td> <td>Vietnam Thuong Tin Commercial Joint Stock Bank (Vietbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>26</td> <td>970454</td> <td>VIET CAPITAL COMMERCIAL JOINT STOCK BANK (Ban Viet)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>27</td> <td>970452</td> <td>Kien Long Commercial Joint -Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>28</td> <td>970430</td> <td>PETROLIMEX GROUPCOMMERCIAL JOINT STOCK BANK</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>29</td> <td>970400</td> <td>Sai Gon Joint Stock Commercial Bank (Saigon Bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>30</td> <td>970405</td> <td>Vietnam Bank for Agriculture and Rural Development or Agribank (Agribank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>31</td> <td>970403</td> <td>Sacombank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>32</td> <td>970412</td> <td>Vietnam Public Joint Stock Commercial Bank (Vietnam dai chung)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>33</td> <td>970421</td> <td>Vietnam-Russia Joint Venture Bank - VRB</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>34</td> <td>970428</td> <td>Nam A Commercial Joint Stock Bank (Nam A Bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>35</td> <td>970434</td> <td>Indovina Bank Ltd</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>36</td> <td>970449</td> <td>LienViet Post Joint Stock Commercial Bank (LienViet Post bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>37</td> <td>970457</td> <td>Woori Bank Vietnam Limited</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>38</td> <td>970436</td> <td>Joint Stock Commercial Bank for Foreign Trade of Vietnam (Vietcombank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>39</td> <td>970416</td> <td>Asia Commercial Joint Stock Bank</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>40</td> <td>970458</td> <td>UNITED OVERSEAS BANK (VIETNAM) LIMITED</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>41</td> <td>970446</td> <td>Co-operative bank of VietNam</td> <td></td> <td>✓</td>                         </tr>                         <tr> <td>42</td> <td>970455</td> <td>Industrial Bank of Korea - Ha Noi Branch</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>43</td> <td>970409</td> <td>North Asia Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>44</td> <td>422589</td> <td>CIMB Bank (Vietnam) Limited</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>45</td> <td>796500</td> <td>Ngân hàng DBS - Chi nhánh Hồ Chí Minh(DBS)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>46</td> <td>458761</td> <td>TNHH MTV HSBC Việt Nam(HSBC)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>47</td> <td>970410</td> <td>TNHH MTV Standard Chartered Việt Nam(SCVN)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>48</td> <td>801011</td> <td>Nonghuyp - Chi nhánh Hà Nội(NHB)</td> <td>✓</td> <td></td>                         </tr>  <td>49</td> <td>970444</td> <td>TM TNHH MTV Xây Dựng Việt Nam </td> <td>✓</td> <td></td>                         </tr><tr> <td>50</td> <td>970456</td> <td> IBK - chi nhánh HCM</td> <td>✓</td> <td></td>                         </tr><tr> <td>51</td> <td>970462</td> <td>Kookmin - Chi nhánh Hà Nội</td> <td>✓</td> <td>✓</td>                         </tr><tr> <td>52</td> <td>970463</td> <td>Kookmin - Chi nhánh Thành phố Hồ Chí Minh</td> <td>✓</td> <td>✓</td>                         </tr><tr> <td>53</td> <td>546034</td> <td>Ngân hàng số CAKE by VPBank</td> <td>✓</td> <td></td>                         </tr><tr> <td>54</td> <td>546035</td> <td>Ngân hàng số Ubank by VPBank</td> <td>✓</td> <td></td>                   </tbody>                 </table>
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
/**
 * InlineResponse2001
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-06-30T01:32:59.379Z[Etc/UTC]")
public class InlineResponse2001 {
  @SerializedName("ResponseCode")
  private Integer responseCode = null;

  @SerializedName("ResponseMessage")
  private String responseMessage = null;

  @SerializedName("ReferenceId")
  private String referenceId = null;

  @SerializedName("TransactionId")
  private String transactionId = null;

  @SerializedName("TransactionTime")
  private String transactionTime = null;

  @SerializedName("BankNo")
  private String bankNo = null;

  @SerializedName("AccNo")
  private String accNo = null;

  @SerializedName("AccName")
  private String accName = null;

  @SerializedName("AccType")
  private String accType = null;

  @SerializedName("RequestAmount")
  private Integer requestAmount = null;

  @SerializedName("TransferAmount")
  private Integer transferAmount = null;

  @SerializedName("AffterBalance")
  private Integer affterBalance = null;

  @SerializedName("AfterDisbursementDay")
  private Integer afterDisbursementDay = null;

  @SerializedName("Signature")
  private String signature = null;

  public InlineResponse2001 responseCode(Integer responseCode) {
    this.responseCode = responseCode;
    return this;
  }

   /**
   * 200 : Successful. &lt;br&gt; 99 : Transaction timeout.&lt;br&gt; 11 : Failed.&lt;br&gt; 101 : Error processing from Baokim.&lt;br&gt; 102 : Duplicated RequestId.&lt;br&gt; 103 : Incorrect signature.&lt;br&gt; 110 : Incorrect PartnerCode.&lt;br&gt; 111 : PartnerCode deleted from the system.&lt;br&gt; 112 : PartnerCode not yet activated.&lt;br&gt; 113 : Operation code is required.&lt;br&gt; 114 : Incorrect Operation code.&lt;br&gt; 115 : BankID is required.&lt;br&gt; 116 : BankID not supported.&lt;br&gt; 117 : Account no. /Card no. should be from 6-22 characters in length.&lt;br&gt; 118 : Invalid account no./Card no..&lt;br&gt; 119 : Account no./Card no. does not exist.&lt;br&gt; 120 : Incorrect account type.&lt;br&gt; 121 : Transaction ID sent from Partner is required.&lt;br&gt; 122 : Transaction ID sent by Partner is existing.&lt;br&gt; 123 : Transaction unfound.&lt;br&gt; 124 : Transfer amount required.&lt;br&gt; 125 : Invalid transfer amount.&lt;br&gt; 126 : Error processing between Baokim and bank.&lt;br&gt; 127 : Error connecting to bank.&lt;br&gt; 128 : Error processing from bank.&lt;br&gt; 129 : Insufficient disbursement limit or expired guarantee period.&lt;br&gt; 130 : Exceeded transfer limit on day.&lt;br&gt;
   * @return responseCode
  **/
  @Schema(example = "200", description = "200 : Successful. <br> 99 : Transaction timeout.<br> 11 : Failed.<br> 101 : Error processing from Baokim.<br> 102 : Duplicated RequestId.<br> 103 : Incorrect signature.<br> 110 : Incorrect PartnerCode.<br> 111 : PartnerCode deleted from the system.<br> 112 : PartnerCode not yet activated.<br> 113 : Operation code is required.<br> 114 : Incorrect Operation code.<br> 115 : BankID is required.<br> 116 : BankID not supported.<br> 117 : Account no. /Card no. should be from 6-22 characters in length.<br> 118 : Invalid account no./Card no..<br> 119 : Account no./Card no. does not exist.<br> 120 : Incorrect account type.<br> 121 : Transaction ID sent from Partner is required.<br> 122 : Transaction ID sent by Partner is existing.<br> 123 : Transaction unfound.<br> 124 : Transfer amount required.<br> 125 : Invalid transfer amount.<br> 126 : Error processing between Baokim and bank.<br> 127 : Error connecting to bank.<br> 128 : Error processing from bank.<br> 129 : Insufficient disbursement limit or expired guarantee period.<br> 130 : Exceeded transfer limit on day.<br>")
  public Integer getResponseCode() {
    return responseCode;
  }

  public void setResponseCode(Integer responseCode) {
    this.responseCode = responseCode;
  }

  public InlineResponse2001 responseMessage(String responseMessage) {
    this.responseMessage = responseMessage;
    return this;
  }

   /**
   * Description for return status
   * @return responseMessage
  **/
  @Schema(example = "Successful", description = "Description for return status")
  public String getResponseMessage() {
    return responseMessage;
  }

  public void setResponseMessage(String responseMessage) {
    this.responseMessage = responseMessage;
  }

  public InlineResponse2001 referenceId(String referenceId) {
    this.referenceId = referenceId;
    return this;
  }

   /**
   * Partner information posted
   * @return referenceId
  **/
  @Schema(example = "5CBCAB920C63CED5E0540010E099E090", description = "Partner information posted")
  public String getReferenceId() {
    return referenceId;
  }

  public void setReferenceId(String referenceId) {
    this.referenceId = referenceId;
  }

  public InlineResponse2001 transactionId(String transactionId) {
    this.transactionId = transactionId;
    return this;
  }

   /**
   * Transaction code recorded side Baokim
   * @return transactionId
  **/
  @Schema(example = "BK5CF8D68AE3CF8JY", description = "Transaction code recorded side Baokim")
  public String getTransactionId() {
    return transactionId;
  }

  public void setTransactionId(String transactionId) {
    this.transactionId = transactionId;
  }

  public InlineResponse2001 transactionTime(String transactionTime) {
    this.transactionTime = transactionTime;
    return this;
  }

   /**
   * Finishing time side Baokim. Format YYYY-MM-DD
   * @return transactionTime
  **/
  @Schema(example = "2019-06-06", description = "Finishing time side Baokim. Format YYYY-MM-DD")
  public String getTransactionTime() {
    return transactionTime;
  }

  public void setTransactionTime(String transactionTime) {
    this.transactionTime = transactionTime;
  }

  public InlineResponse2001 bankNo(String bankNo) {
    this.bankNo = bankNo;
    return this;
  }

   /**
   * Partner information posted
   * @return bankNo
  **/
  @Schema(example = "970436", description = "Partner information posted")
  public String getBankNo() {
    return bankNo;
  }

  public void setBankNo(String bankNo) {
    this.bankNo = bankNo;
  }

  public InlineResponse2001 accNo(String accNo) {
    this.accNo = accNo;
    return this;
  }

   /**
   * Partner information posted
   * @return accNo
  **/
  @Schema(example = "0021000382448", description = "Partner information posted")
  public String getAccNo() {
    return accNo;
  }

  public void setAccNo(String accNo) {
    this.accNo = accNo;
  }

  public InlineResponse2001 accName(String accName) {
    this.accName = accName;
    return this;
  }

   /**
   * Full name of the recipient, may or may not, depending on the time
   * @return accName
  **/
  @Schema(example = "TRUONG DUC THUAN", description = "Full name of the recipient, may or may not, depending on the time")
  public String getAccName() {
    return accName;
  }

  public void setAccName(String accName) {
    this.accName = accName;
  }

  public InlineResponse2001 accType(String accType) {
    this.accType = accType;
    return this;
  }

   /**
   * Partner information posted
   * @return accType
  **/
  @Schema(example = "0", description = "Partner information posted")
  public String getAccType() {
    return accType;
  }

  public void setAccType(String accType) {
    this.accType = accType;
  }

  public InlineResponse2001 requestAmount(Integer requestAmount) {
    this.requestAmount = requestAmount;
    return this;
  }

   /**
   * Partner information posted
   * @return requestAmount
  **/
  @Schema(example = "1000000", description = "Partner information posted")
  public Integer getRequestAmount() {
    return requestAmount;
  }

  public void setRequestAmount(Integer requestAmount) {
    this.requestAmount = requestAmount;
  }

  public InlineResponse2001 transferAmount(Integer transferAmount) {
    this.transferAmount = transferAmount;
    return this;
  }

   /**
   * The actual amount transferred to the recipient. Will be less if the remittance
   * @return transferAmount
  **/
  @Schema(example = "1000000", description = "The actual amount transferred to the recipient. Will be less if the remittance")
  public Integer getTransferAmount() {
    return transferAmount;
  }

  public void setTransferAmount(Integer transferAmount) {
    this.transferAmount = transferAmount;
  }

  public InlineResponse2001 affterBalance(Integer affterBalance) {
    this.affterBalance = affterBalance;
    return this;
  }

   /**
   * Current balance of investors
   * @return affterBalance
  **/
  @Schema(example = "100000000", description = "Current balance of investors")
  public Integer getAffterBalance() {
    return affterBalance;
  }

  public void setAffterBalance(Integer affterBalance) {
    this.affterBalance = affterBalance;
  }

  public InlineResponse2001 afterDisbursementDay(Integer afterDisbursementDay) {
    this.afterDisbursementDay = afterDisbursementDay;
    return this;
  }

   /**
   * Continue disbursement amount (in limit)
   * @return afterDisbursementDay
  **/
  @Schema(example = "100000000", description = "Continue disbursement amount (in limit)")
  public Integer getAfterDisbursementDay() {
    return afterDisbursementDay;
  }

  public void setAfterDisbursementDay(Integer afterDisbursementDay) {
    this.afterDisbursementDay = afterDisbursementDay;
  }

  public InlineResponse2001 signature(String signature) {
    this.signature = signature;
    return this;
  }

   /**
   * BAOKIM will sign by digital signature of response data. Structured data: ResponseCode|ResponseMessage| RequestId | PartnerCode | Available | Holding
   * @return signature
  **/
  @Schema(example = "zzhBMeZuDNPDD1TE9q3ojo+SSwA/FehW3H77y+3JkNHrdpRentPD 1TE9q3ojo FehW3H77y+3JkNHrdpRentPDbb =", description = "BAOKIM will sign by digital signature of response data. Structured data: ResponseCode|ResponseMessage| RequestId | PartnerCode | Available | Holding")
  public String getSignature() {
    return signature;
  }

  public void setSignature(String signature) {
    this.signature = signature;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InlineResponse2001 inlineResponse2001 = (InlineResponse2001) o;
    return Objects.equals(this.responseCode, inlineResponse2001.responseCode) &&
        Objects.equals(this.responseMessage, inlineResponse2001.responseMessage) &&
        Objects.equals(this.referenceId, inlineResponse2001.referenceId) &&
        Objects.equals(this.transactionId, inlineResponse2001.transactionId) &&
        Objects.equals(this.transactionTime, inlineResponse2001.transactionTime) &&
        Objects.equals(this.bankNo, inlineResponse2001.bankNo) &&
        Objects.equals(this.accNo, inlineResponse2001.accNo) &&
        Objects.equals(this.accName, inlineResponse2001.accName) &&
        Objects.equals(this.accType, inlineResponse2001.accType) &&
        Objects.equals(this.requestAmount, inlineResponse2001.requestAmount) &&
        Objects.equals(this.transferAmount, inlineResponse2001.transferAmount) &&
        Objects.equals(this.affterBalance, inlineResponse2001.affterBalance) &&
        Objects.equals(this.afterDisbursementDay, inlineResponse2001.afterDisbursementDay) &&
        Objects.equals(this.signature, inlineResponse2001.signature);
  }

  @Override
  public int hashCode() {
    return Objects.hash(responseCode, responseMessage, referenceId, transactionId, transactionTime, bankNo, accNo, accName, accType, requestAmount, transferAmount, affterBalance, afterDisbursementDay, signature);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InlineResponse2001 {\n");
    
    sb.append("    responseCode: ").append(toIndentedString(responseCode)).append("\n");
    sb.append("    responseMessage: ").append(toIndentedString(responseMessage)).append("\n");
    sb.append("    referenceId: ").append(toIndentedString(referenceId)).append("\n");
    sb.append("    transactionId: ").append(toIndentedString(transactionId)).append("\n");
    sb.append("    transactionTime: ").append(toIndentedString(transactionTime)).append("\n");
    sb.append("    bankNo: ").append(toIndentedString(bankNo)).append("\n");
    sb.append("    accNo: ").append(toIndentedString(accNo)).append("\n");
    sb.append("    accName: ").append(toIndentedString(accName)).append("\n");
    sb.append("    accType: ").append(toIndentedString(accType)).append("\n");
    sb.append("    requestAmount: ").append(toIndentedString(requestAmount)).append("\n");
    sb.append("    transferAmount: ").append(toIndentedString(transferAmount)).append("\n");
    sb.append("    affterBalance: ").append(toIndentedString(affterBalance)).append("\n");
    sb.append("    afterDisbursementDay: ").append(toIndentedString(afterDisbursementDay)).append("\n");
    sb.append("    signature: ").append(toIndentedString(signature)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
