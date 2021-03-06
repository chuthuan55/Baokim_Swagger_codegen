/*
 * Baokim Payment Gateway API Documentation
 * __Introduction:__  Bao Kim Payment gateway is an open payment platform, Bao Kim provides a full range of APIs that allow merchants to integrate between applications (web/app) with Bao Kim Payment Gateway to receive payment for your order, check your payment reconciliation.  For example, merchants can perform the following tasks with Bao Kim API. Receive payment for orders on your application (web/app) by sending orders to Bao Kim and display the payment interface for buyers to pay. Reconciliation and search for information of transaction payments, refund transactions, merchants you manage, payment status of orders to perform reconciliation.  You can find out more about Bao Kim at [Baokim.vn](https://baokim.vn).  __Security Method:__ Bao Kim API uses JSON Web Token (JWT), is a required parameter for every request to the API, follow the steps: * Use the assigned API Key and HS256 encryption algorithm to encrypt the JWT (check sample code) * JWT expire in the 60s after created * When request to API, jwt need to pass by 1 of 2 methods: Request Header jwt = Bearer $JWT / Query parameter(url param) &jwt=$JWT  __Sandbox(Test) Enviroment:__ * API key/sec: a18ff78e7a9e44f38de372e093d87ca1 / 9623ac03057e433f95d86cf4f3bef5cc * Portal URL: https://devtest.baokim.vn:9244/login * Merchant ID: 40002 * Card test ATM card:   * Bank: Saigonbank   * Card Number: 9704000000000018   * Card Holder: NGUYEN VAN A   * Effective date: 03/07   * OTP: otp * Card test Debit or credit card:   * Card Number: 5123450000000008   * Valid thru: 12/22   * CVN: 100  __Basic integration process__  This is the simplest and fastest integration process, but please learn more about the Pro integration process below with more advantages to make the right choice.  <img class=\"dia_img\" src=\"../swagger/images/BasicPaymentIntegrationDiagram.svg\" alt=\"\">  Advantages: * Simple integration, only 2 steps of processing are required to send payment request (API Send Order) and confirm payment results.  Defect: * Customers cannot view the payment methods to choose (eg bank list ...) right on the merchant's interface. Customers will choose the payment method on Bao Kim's payment interface.  __Pro integration process (advanced)__  Technically, the only difference between Pro integration and basic integration is the Web / App merchant that uses API Bank Payment Method List to load the list of payment methods and display on its interface to users. Select, then send these parameters along with the order to Bao Kim via the Send Order API  <img class=\"dia_img\" src=\"../swagger/images/PaymentProIntegrationDiagram.svg\" alt=\"\">  The main advantage of Pro integration: * Web / Merchant App can display the list of payment methods customers can use (for Bao Kim, Banks), * When the customer has chosen a payment method, the payment process will be transferred directly from the Web / Merchant App to the bank page (no Bao Kim payment page will be displayed) * Customers feel that the Web / App merchant accepts payment of most domestic banks, increases reliability, professionalism, and anticipates the payment options they have.  Defect: * Technical processing must be performed to display payment methods on the Web / Merchant App interface.  __Payment via Internet Banking (comming soon)__  Basically, payment via Internet Banking is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  However, if you want to be simpler for your customers by displaying your Internet Banking account information on your interface instead of having to redirect to Bao Kim, handle the shortening process below:  <img class=\"dia_img\" src=\"../swagger/images/InternetBankingPaymentIntegrationDiagram.svg\" alt=\"\">  __Payment by QRCode__  Payment by QRCode is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  For Pro integration, if you want to simplify for customers by displaying QRCode images on your interface instead of having to redirect to Bao Kim, please proceed with the shortened process below:  <img class=\"dia_img\" src=\"../swagger/images/QRCodePaymentIntegration.svg\" alt=\"\">  __Installment payment__  Payment by QRCode is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  Customers before payment need to take one more step to select the issuing bank and the term and installment payment (3/6/9/12 months), please refer to the process below:  <img class=\"dia_img\" src=\"../swagger/images/Quy-trinh-thanh-toan-tra-gop.svg\" alt=\"\">  __Virtual account payment__  <strong>Step 1: Create virtual account</strong> * Call to the API ???payment/api/v4/create-virtual-account-payment??? with parameters:   * mrc_uuid: user_id of merchant (unique)   * mrc_uuid: name: user name   * mrc_uuid: mrc_id: ID Merchant on integrated website  <strong>Step 2: Receive payment results</strong> * After the User has paid, Bao Kim will record the transaction and then return the results to Merchant via webhook.  Please refer to the procedure below:  <img class=\"dia_img\" src=\"../swagger/images/quy-trinh-tao-tai-khoan-ao.svg\" alt=\"\">   __Payment via momo e-wallet__  Payment via momo e-wallet is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  <img class=\"dia_img\" src=\"../swagger/images/PayByMoMo.svg\" alt=\"\">  __Payment using module Checkout__  <strong>Step 1: Install package:</strong> * Open Terminal and run command: <strong>composer require baokim/baokim-sdk</strong> * Next, run command: <strong>composer dump-autoload</strong>  <strong>Step 2: Conduct integration</strong>  For one-time payments, create a Session with line_items. Line items represent a list of items the customer is purchasing.  Line_items takes the form of an array, refer to the sample code to the right:  $payment_method_types = [1, 2, 3];  payment_method_types is an array (1: Payment by ATM, 2: Payment by QRCode, 3: Payment By Visa).  When your customer successfully completes their payment, they are redirected to the success_url, a page on your website that informs the customer that their payment was successful.  When your customer clicks on your logo in a Checkout Session without completing a payment, Checkout redirects them back to your website by navigating to the cancel_url. Typically, this is the page on your website that the customer viewed prior to redirecting to Checkout.  <strong>Create Payment Session</strong>  Creating a Checkout Session returns $session include information of session saved in B???o Kim, and payment_url. You need redirect browser to payment_urlto proceed with the payment  __Payment confirmation:__  After the customer makes a successful payment, Bao Kim will send a Webhook notification to the Web/App merchant, then redirect the customer browser to url_success on order with data. Web/App merchant has two ways to confirm the payment result of the order:  1. Web/App merchant receive Webhook notification Bao Kim sent by parameter \"webhooks\" on order (Recommended) 2. After the user pay, Bao Kim redirects the browser to the url_success on the order with the payment result, the Web/App merchant handles results return on url_success (this way may be affected by customer transmission failure)  In both ways, the order is considered successful payment when: * Order status \"stat\" == \"c\" * Payment transaction of order status \"stat\" == 1 * Order amount (total_amount) match with the merchant's order amount  __Webhook Notification:__  Webhook notification is a mechanism to notify Web/App merchants when an order is successfully paid through an HTTP POST request. * How to receive webhook notifications?   * When sending an order to Bao Kim through API Send Order, remember to pass the webhooks parameter as described   * When your order is successfully paid, Bao Kim will POST the payment data to the URL on the webhooks parameter in the order. * How many times will a Webhook notification be sent?   * Send up to 10 times   * Every 5 minutes   * Stop sending when receiving a json string with err_code = 0, eg {\"err_code\": \"0\", \"message\": \"some message\"}   (help Bao Kim determine that the merchant has successfully received the notification)  Description of data on webhook notification: * Method: POST * Header: Content-Type: application/json * Body (check sample code on the right side)  Steps to check and handle when receiving webhook notification: 1. Check the integrity of the received data by checking the correctness of the signature as follows (See sample PHP code on the right tab, under the webhook data description):   * Use the secret value in the key/secret pair in your API Key   * Using the hash_hmac algorithm with sha256, sign the data you receive (except for the $sign field, of course) => $yourSign   * Compare the signature you generated ($yourSign) with the signature you received ($sign), if not the same => data is not incomplete 2. Check order payment status, payment transaction, payment amount, order completion   * Check order status ($order->stat == 'c' //completed)   * Check if the order information ($order) is correct with the order information on your web/app   * If the above checks are correct, you can be sure that the order has been paid and can be completed. 3. Returns JSON string with err_code = 0, eg {\"err_code\": \"0\", \"message\": \"some message\"} so that Bao Kim knows that the merchant has received the notice and does not continue to send it back. The maximum length of the returned data is 255 characters.  Example Webhook:      {       \"order\":{         \"id\":82127,         \"user_id\":1000007,         \"mrc_order_id\":\"Nam1645759079\",         \"txn_id\":69154,         \"ref_no\":null,         \"merchant_id\":40187,         \"total_amount\":3000000,         \"description\":\"eqxI4W4HFUPwyNxH\",         \"items\":\"{           \"period\":3,           \"total_amount\":\"3090000.00\",           \"down_payment\":\"750000.00\",           \"down_payment_percent\":\"25.00\",           \"paylater_amount\":\"2250000.00\",           \"pay_per_month\":\"780000.00\",           \"user_fee\":\"90000\",           \"merchant_fee\":\"90000\"         }\",         \"url_success\":\"https://www.google.com/\",         \"url_cancel\":null,         \"url_detail\":\"https://www.google.com/\",         \"stat\":\"c\",         \"lang\":\"en\",         \"type\":1,         \"bpm_id\":\"339\",         \"accept_qrpay\":1,         \"accept_bank\":1,         \"accept_cc\":1,         \"accept_ib\":1,         \"accept_ewallet\":1,         \"accept_installments\":1,         \"email\":\"2@bk.vn\",         \"name\":\"baokimjsc111\",         \"webhooks\":\"https://google.com\",         \"customer_name\":\"Nguyen Thanh nam\",         \"customer_email\":\"testpay@gmail.com\",         \"customer_phone\":\"84328271591\",         \"customer_address\":\"102 thai thinh\",         \"created_at\":\"2022-02-25 10:18:01\",         \"updated_at\":\"2022-02-25 10:23:12\"       },       \"txn\":{         \"id\":69154,         \"reference_id\":\"bk_82127_69154_41j\",         \"user_id\":1000007,         \"merchant_id\":40187,         \"order_id\":82127,         \"mrc_order_id\":\"nam1645759079\",         \"total_amount\":750550,         \"amount\":750000,         \"fee_amount\":0,         \"bank_fee_amount\":550,         \"bank_fix_fee_amount\":550,         \"fee_payer\":1,         \"bank_fee_payer\":1,         \"auth_code\":null,         \"auth_time\":\"\",         \"ref_no\":null,         \"bpm_id\":\"97\",         \"bank_ref_no\":\"507800079\",         \"bpm_type\":1,         \"gateway\":\"\",         \"stat\":1,         \"init_token\":null,         \"description\":\"eqxi4w4hfupwynxh\",         \"customer_email\":\"testpay@gmail.com\",         \"customer_phone\":\"84328271591\",         \"completed_at\":\"2022-02-25 10:23:12\",         \"created_at\":\"2022-02-25 10:18:24\",         \"updated_at\":\"2022-02-25 10:23:12\",         \"deleted_at\":null       },       \"dataToken\":[],       \"sign\":\"ffc020303d1ed4fbe5df95d83261524793358ab0a8e363ae265e3fc2c33dc560\"     }  __Data return on url_success:__  If the merchant web/app gets notifications through Webhook Notification, you can skip processing the return data on url_success and simply show the successful payment page to the customer. Otherwise, verify the return data on url_success as follows.  Data return on url_success * id: Request id (created by Bao Kim) * mrc_order_id: Order ID on merchant web/app * txn_id: Payment Transaction ID of order * total_amount: Order payment amount * stat: Order status * created_at: Time receive orders * updated_at: Payment confirmation time * checksum: Data security signature (see details below)  The checksum is signed on the parameter passed on url_success using the sha256 hash algorithm, with the security key being the secret key in your API key. How to verify the checksum on url_success please see the steps and sample code on the right tab. 
 *
 * OpenAPI spec version: 5.0.0
 * Contact: developer@baokim.vn
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
import io.swagger.client.model.Description;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
/**
 * InlineResponse2006Data
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-06-30T01:34:10.320Z[Etc/UTC]")
public class InlineResponse2006Data {
  @SerializedName("payment_txn_id")
  private Integer paymentTxnId = null;

  @SerializedName("stat")
  private Integer stat = null;

  @SerializedName("user_id")
  private Integer userId = null;

  @SerializedName("merchant_id")
  private Integer merchantId = null;

  @SerializedName("order_id")
  private Integer orderId = null;

  @SerializedName("mrc_order_id")
  private String mrcOrderId = null;

  @SerializedName("net_amount")
  private String netAmount = null;

  @SerializedName("order_amount")
  private String orderAmount = null;

  @SerializedName("pay_amount")
  private String payAmount = null;

  @SerializedName("refund_amount")
  private Object refundAmount = null;

  @SerializedName("fee_amount")
  private String feeAmount = null;

  @SerializedName("bank_percent_fee_amount")
  private Integer bankPercentFeeAmount = null;

  @SerializedName("fee_payer")
  private String feePayer = null;

  @SerializedName("ref_no")
  private Object refNo = null;

  @SerializedName("bpm_id")
  private Integer bpmId = null;

  @SerializedName("bpm_type")
  private Integer bpmType = null;

  @SerializedName("description")
  private Description description = null;

  @SerializedName("count")
  private Integer count = null;

  @SerializedName("amount")
  private Integer amount = null;

  @SerializedName("minus_amount")
  private String minusAmount = null;

  @SerializedName("created_at")
  private String createdAt = null;

  @SerializedName("updated_at")
  private String updatedAt = null;

  @SerializedName("id")
  private Integer id = null;

  public InlineResponse2006Data paymentTxnId(Integer paymentTxnId) {
    this.paymentTxnId = paymentTxnId;
    return this;
  }

   /**
   * Get paymentTxnId
   * @return paymentTxnId
  **/
  @Schema(example = "66985", description = "")
  public Integer getPaymentTxnId() {
    return paymentTxnId;
  }

  public void setPaymentTxnId(Integer paymentTxnId) {
    this.paymentTxnId = paymentTxnId;
  }

  public InlineResponse2006Data stat(Integer stat) {
    this.stat = stat;
    return this;
  }

   /**
   * Get stat
   * @return stat
  **/
  @Schema(example = "0", description = "")
  public Integer getStat() {
    return stat;
  }

  public void setStat(Integer stat) {
    this.stat = stat;
  }

  public InlineResponse2006Data userId(Integer userId) {
    this.userId = userId;
    return this;
  }

   /**
   * Get userId
   * @return userId
  **/
  @Schema(example = "1000007", description = "")
  public Integer getUserId() {
    return userId;
  }

  public void setUserId(Integer userId) {
    this.userId = userId;
  }

  public InlineResponse2006Data merchantId(Integer merchantId) {
    this.merchantId = merchantId;
    return this;
  }

   /**
   * Get merchantId
   * @return merchantId
  **/
  @Schema(example = "40095", description = "")
  public Integer getMerchantId() {
    return merchantId;
  }

  public void setMerchantId(Integer merchantId) {
    this.merchantId = merchantId;
  }

  public InlineResponse2006Data orderId(Integer orderId) {
    this.orderId = orderId;
    return this;
  }

   /**
   * Get orderId
   * @return orderId
  **/
  @Schema(example = "78709", description = "")
  public Integer getOrderId() {
    return orderId;
  }

  public void setOrderId(Integer orderId) {
    this.orderId = orderId;
  }

  public InlineResponse2006Data mrcOrderId(String mrcOrderId) {
    this.mrcOrderId = mrcOrderId;
    return this;
  }

   /**
   * Get mrcOrderId
   * @return mrcOrderId
  **/
  @Schema(example = "test_44", description = "")
  public String getMrcOrderId() {
    return mrcOrderId;
  }

  public void setMrcOrderId(String mrcOrderId) {
    this.mrcOrderId = mrcOrderId;
  }

  public InlineResponse2006Data netAmount(String netAmount) {
    this.netAmount = netAmount;
    return this;
  }

   /**
   * Get netAmount
   * @return netAmount
  **/
  @Schema(example = "17760.0", description = "")
  public String getNetAmount() {
    return netAmount;
  }

  public void setNetAmount(String netAmount) {
    this.netAmount = netAmount;
  }

  public InlineResponse2006Data orderAmount(String orderAmount) {
    this.orderAmount = orderAmount;
    return this;
  }

   /**
   * Get orderAmount
   * @return orderAmount
  **/
  @Schema(example = "20000.0", description = "")
  public String getOrderAmount() {
    return orderAmount;
  }

  public void setOrderAmount(String orderAmount) {
    this.orderAmount = orderAmount;
  }

  public InlineResponse2006Data payAmount(String payAmount) {
    this.payAmount = payAmount;
    return this;
  }

   /**
   * Get payAmount
   * @return payAmount
  **/
  @Schema(example = "21980.0", description = "")
  public String getPayAmount() {
    return payAmount;
  }

  public void setPayAmount(String payAmount) {
    this.payAmount = payAmount;
  }

  public InlineResponse2006Data refundAmount(Object refundAmount) {
    this.refundAmount = refundAmount;
    return this;
  }

   /**
   * Get refundAmount
   * @return refundAmount
  **/
  @Schema(example = "20000.0", description = "")
  public Object getRefundAmount() {
    return refundAmount;
  }

  public void setRefundAmount(Object refundAmount) {
    this.refundAmount = refundAmount;
  }

  public InlineResponse2006Data feeAmount(String feeAmount) {
    this.feeAmount = feeAmount;
    return this;
  }

   /**
   * Get feeAmount
   * @return feeAmount
  **/
  @Schema(example = "1760.0", description = "")
  public String getFeeAmount() {
    return feeAmount;
  }

  public void setFeeAmount(String feeAmount) {
    this.feeAmount = feeAmount;
  }

  public InlineResponse2006Data bankPercentFeeAmount(Integer bankPercentFeeAmount) {
    this.bankPercentFeeAmount = bankPercentFeeAmount;
    return this;
  }

   /**
   * Get bankPercentFeeAmount
   * @return bankPercentFeeAmount
  **/
  @Schema(example = "220", description = "")
  public Integer getBankPercentFeeAmount() {
    return bankPercentFeeAmount;
  }

  public void setBankPercentFeeAmount(Integer bankPercentFeeAmount) {
    this.bankPercentFeeAmount = bankPercentFeeAmount;
  }

  public InlineResponse2006Data feePayer(String feePayer) {
    this.feePayer = feePayer;
    return this;
  }

   /**
   * Get feePayer
   * @return feePayer
  **/
  @Schema(example = "1", description = "")
  public String getFeePayer() {
    return feePayer;
  }

  public void setFeePayer(String feePayer) {
    this.feePayer = feePayer;
  }

  public InlineResponse2006Data refNo(Object refNo) {
    this.refNo = refNo;
    return this;
  }

   /**
   * Get refNo
   * @return refNo
  **/
  @Schema(description = "")
  public Object getRefNo() {
    return refNo;
  }

  public void setRefNo(Object refNo) {
    this.refNo = refNo;
  }

  public InlineResponse2006Data bpmId(Integer bpmId) {
    this.bpmId = bpmId;
    return this;
  }

   /**
   * Get bpmId
   * @return bpmId
  **/
  @Schema(example = "97", description = "")
  public Integer getBpmId() {
    return bpmId;
  }

  public void setBpmId(Integer bpmId) {
    this.bpmId = bpmId;
  }

  public InlineResponse2006Data bpmType(Integer bpmType) {
    this.bpmType = bpmType;
    return this;
  }

   /**
   * Get bpmType
   * @return bpmType
  **/
  @Schema(example = "1", description = "")
  public Integer getBpmType() {
    return bpmType;
  }

  public void setBpmType(Integer bpmType) {
    this.bpmType = bpmType;
  }

  public InlineResponse2006Data description(Description description) {
    this.description = description;
    return this;
  }

   /**
   * Get description
   * @return description
  **/
  @Schema(example = "test", description = "")
  public Description getDescription() {
    return description;
  }

  public void setDescription(Description description) {
    this.description = description;
  }

  public InlineResponse2006Data count(Integer count) {
    this.count = count;
    return this;
  }

   /**
   * Get count
   * @return count
  **/
  @Schema(example = "0", description = "")
  public Integer getCount() {
    return count;
  }

  public void setCount(Integer count) {
    this.count = count;
  }

  public InlineResponse2006Data amount(Integer amount) {
    this.amount = amount;
    return this;
  }

   /**
   * Get amount
   * @return amount
  **/
  @Schema(example = "18460", description = "")
  public Integer getAmount() {
    return amount;
  }

  public void setAmount(Integer amount) {
    this.amount = amount;
  }

  public InlineResponse2006Data minusAmount(String minusAmount) {
    this.minusAmount = minusAmount;
    return this;
  }

   /**
   * Get minusAmount
   * @return minusAmount
  **/
  @Schema(example = "20000.0", description = "")
  public String getMinusAmount() {
    return minusAmount;
  }

  public void setMinusAmount(String minusAmount) {
    this.minusAmount = minusAmount;
  }

  public InlineResponse2006Data createdAt(String createdAt) {
    this.createdAt = createdAt;
    return this;
  }

   /**
   * Get createdAt
   * @return createdAt
  **/
  @Schema(example = "2022-01-17 10:58:02", description = "")
  public String getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(String createdAt) {
    this.createdAt = createdAt;
  }

  public InlineResponse2006Data updatedAt(String updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

   /**
   * Get updatedAt
   * @return updatedAt
  **/
  @Schema(example = "2022-01-17 10:58:02", description = "")
  public String getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(String updatedAt) {
    this.updatedAt = updatedAt;
  }

  public InlineResponse2006Data id(Integer id) {
    this.id = id;
    return this;
  }

   /**
   * Get id
   * @return id
  **/
  @Schema(example = "1572", description = "")
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InlineResponse2006Data inlineResponse2006Data = (InlineResponse2006Data) o;
    return Objects.equals(this.paymentTxnId, inlineResponse2006Data.paymentTxnId) &&
        Objects.equals(this.stat, inlineResponse2006Data.stat) &&
        Objects.equals(this.userId, inlineResponse2006Data.userId) &&
        Objects.equals(this.merchantId, inlineResponse2006Data.merchantId) &&
        Objects.equals(this.orderId, inlineResponse2006Data.orderId) &&
        Objects.equals(this.mrcOrderId, inlineResponse2006Data.mrcOrderId) &&
        Objects.equals(this.netAmount, inlineResponse2006Data.netAmount) &&
        Objects.equals(this.orderAmount, inlineResponse2006Data.orderAmount) &&
        Objects.equals(this.payAmount, inlineResponse2006Data.payAmount) &&
        Objects.equals(this.refundAmount, inlineResponse2006Data.refundAmount) &&
        Objects.equals(this.feeAmount, inlineResponse2006Data.feeAmount) &&
        Objects.equals(this.bankPercentFeeAmount, inlineResponse2006Data.bankPercentFeeAmount) &&
        Objects.equals(this.feePayer, inlineResponse2006Data.feePayer) &&
        Objects.equals(this.refNo, inlineResponse2006Data.refNo) &&
        Objects.equals(this.bpmId, inlineResponse2006Data.bpmId) &&
        Objects.equals(this.bpmType, inlineResponse2006Data.bpmType) &&
        Objects.equals(this.description, inlineResponse2006Data.description) &&
        Objects.equals(this.count, inlineResponse2006Data.count) &&
        Objects.equals(this.amount, inlineResponse2006Data.amount) &&
        Objects.equals(this.minusAmount, inlineResponse2006Data.minusAmount) &&
        Objects.equals(this.createdAt, inlineResponse2006Data.createdAt) &&
        Objects.equals(this.updatedAt, inlineResponse2006Data.updatedAt) &&
        Objects.equals(this.id, inlineResponse2006Data.id);
  }

  @Override
  public int hashCode() {
    return Objects.hash(paymentTxnId, stat, userId, merchantId, orderId, mrcOrderId, netAmount, orderAmount, payAmount, refundAmount, feeAmount, bankPercentFeeAmount, feePayer, refNo, bpmId, bpmType, description, count, amount, minusAmount, createdAt, updatedAt, id);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InlineResponse2006Data {\n");
    
    sb.append("    paymentTxnId: ").append(toIndentedString(paymentTxnId)).append("\n");
    sb.append("    stat: ").append(toIndentedString(stat)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
    sb.append("    merchantId: ").append(toIndentedString(merchantId)).append("\n");
    sb.append("    orderId: ").append(toIndentedString(orderId)).append("\n");
    sb.append("    mrcOrderId: ").append(toIndentedString(mrcOrderId)).append("\n");
    sb.append("    netAmount: ").append(toIndentedString(netAmount)).append("\n");
    sb.append("    orderAmount: ").append(toIndentedString(orderAmount)).append("\n");
    sb.append("    payAmount: ").append(toIndentedString(payAmount)).append("\n");
    sb.append("    refundAmount: ").append(toIndentedString(refundAmount)).append("\n");
    sb.append("    feeAmount: ").append(toIndentedString(feeAmount)).append("\n");
    sb.append("    bankPercentFeeAmount: ").append(toIndentedString(bankPercentFeeAmount)).append("\n");
    sb.append("    feePayer: ").append(toIndentedString(feePayer)).append("\n");
    sb.append("    refNo: ").append(toIndentedString(refNo)).append("\n");
    sb.append("    bpmId: ").append(toIndentedString(bpmId)).append("\n");
    sb.append("    bpmType: ").append(toIndentedString(bpmType)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    count: ").append(toIndentedString(count)).append("\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    minusAmount: ").append(toIndentedString(minusAmount)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
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
