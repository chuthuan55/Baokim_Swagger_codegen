/* 
 * Baokim Payment Gateway API Documentation
 *
 * __Introduction:__  Bao Kim Payment gateway is an open payment platform, Bao Kim provides a full range of APIs that allow merchants to integrate between applications (web/app) with Bao Kim Payment Gateway to receive payment for your order, check your payment reconciliation.  For example, merchants can perform the following tasks with Bao Kim API. Receive payment for orders on your application (web/app) by sending orders to Bao Kim and display the payment interface for buyers to pay. Reconciliation and search for information of transaction payments, refund transactions, merchants you manage, payment status of orders to perform reconciliation.  You can find out more about Bao Kim at [Baokim.vn](https://baokim.vn).  __Security Method:__ Bao Kim API uses JSON Web Token (JWT), is a required parameter for every request to the API, follow the steps: * Use the assigned API Key and HS256 encryption algorithm to encrypt the JWT (check sample code) * JWT expire in the 60s after created * When request to API, jwt need to pass by 1 of 2 methods: Request Header jwt = Bearer $JWT / Query parameter(url param) &jwt=$JWT  __Sandbox(Test) Enviroment:__ * API key/sec: a18ff78e7a9e44f38de372e093d87ca1 / 9623ac03057e433f95d86cf4f3bef5cc * Portal URL: https://devtest.baokim.vn:9244/login * Merchant ID: 40002 * Card test ATM card:   * Bank: Saigonbank   * Card Number: 9704000000000018   * Card Holder: NGUYEN VAN A   * Effective date: 03/07   * OTP: otp * Card test Debit or credit card:   * Card Number: 5123450000000008   * Valid thru: 12/22   * CVN: 100  __Basic integration process__  This is the simplest and fastest integration process, but please learn more about the Pro integration process below with more advantages to make the right choice.  <img class=\"dia_img\" src=\"../swagger/images/BasicPaymentIntegrationDiagram.svg\" alt=\"\">  Advantages: * Simple integration, only 2 steps of processing are required to send payment request (API Send Order) and confirm payment results.  Defect: * Customers cannot view the payment methods to choose (eg bank list ...) right on the merchant's interface. Customers will choose the payment method on Bao Kim's payment interface.  __Pro integration process (advanced)__  Technically, the only difference between Pro integration and basic integration is the Web / App merchant that uses API Bank Payment Method List to load the list of payment methods and display on its interface to users. Select, then send these parameters along with the order to Bao Kim via the Send Order API  <img class=\"dia_img\" src=\"../swagger/images/PaymentProIntegrationDiagram.svg\" alt=\"\">  The main advantage of Pro integration: * Web / Merchant App can display the list of payment methods customers can use (for Bao Kim, Banks), * When the customer has chosen a payment method, the payment process will be transferred directly from the Web / Merchant App to the bank page (no Bao Kim payment page will be displayed) * Customers feel that the Web / App merchant accepts payment of most domestic banks, increases reliability, professionalism, and anticipates the payment options they have.  Defect: * Technical processing must be performed to display payment methods on the Web / Merchant App interface.  __Payment via Internet Banking (comming soon)__  Basically, payment via Internet Banking is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  However, if you want to be simpler for your customers by displaying your Internet Banking account information on your interface instead of having to redirect to Bao Kim, handle the shortening process below:  <img class=\"dia_img\" src=\"../swagger/images/InternetBankingPaymentIntegrationDiagram.svg\" alt=\"\">  __Payment by QRCode__  Payment by QRCode is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  For Pro integration, if you want to simplify for customers by displaying QRCode images on your interface instead of having to redirect to Bao Kim, please proceed with the shortened process below:  <img class=\"dia_img\" src=\"../swagger/images/QRCodePaymentIntegration.svg\" alt=\"\">  __Installment payment__  Payment by QRCode is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  Customers before payment need to take one more step to select the issuing bank and the term and installment payment (3/6/9/12 months), please refer to the process below:  <img class=\"dia_img\" src=\"../swagger/images/Quy-trinh-thanh-toan-tra-gop.svg\" alt=\"\">  __Virtual account payment__  <strong>Step 1: Create virtual account</strong> * Call to the API ‘payment/api/v4/create-virtual-account-payment’ with parameters:   * mrc_uuid: user_id of merchant (unique)   * mrc_uuid: name: user name   * mrc_uuid: mrc_id: ID Merchant on integrated website  <strong>Step 2: Receive payment results</strong> * After the User has paid, Bao Kim will record the transaction and then return the results to Merchant via webhook.  Please refer to the procedure below:  <img class=\"dia_img\" src=\"../swagger/images/quy-trinh-tao-tai-khoan-ao.svg\" alt=\"\">   __Payment via momo e-wallet__  Payment via momo e-wallet is only one payment method of the above integrated processes (basic / pro), web / merchant app can simply do not need to handle any more.  <img class=\"dia_img\" src=\"../swagger/images/PayByMoMo.svg\" alt=\"\">  __Payment using module Checkout__  <strong>Step 1: Install package:</strong> * Open Terminal and run command: <strong>composer require baokim/baokim-sdk</strong> * Next, run command: <strong>composer dump-autoload</strong>  <strong>Step 2: Conduct integration</strong>  For one-time payments, create a Session with line_items. Line items represent a list of items the customer is purchasing.  Line_items takes the form of an array, refer to the sample code to the right:  $payment_method_types = [1, 2, 3];  payment_method_types is an array (1: Payment by ATM, 2: Payment by QRCode, 3: Payment By Visa).  When your customer successfully completes their payment, they are redirected to the success_url, a page on your website that informs the customer that their payment was successful.  When your customer clicks on your logo in a Checkout Session without completing a payment, Checkout redirects them back to your website by navigating to the cancel_url. Typically, this is the page on your website that the customer viewed prior to redirecting to Checkout.  <strong>Create Payment Session</strong>  Creating a Checkout Session returns $session include information of session saved in Bảo Kim, and payment_url. You need redirect browser to payment_urlto proceed with the payment  __Payment confirmation:__  After the customer makes a successful payment, Bao Kim will send a Webhook notification to the Web/App merchant, then redirect the customer browser to url_success on order with data. Web/App merchant has two ways to confirm the payment result of the order:  1. Web/App merchant receive Webhook notification Bao Kim sent by parameter \"webhooks\" on order (Recommended) 2. After the user pay, Bao Kim redirects the browser to the url_success on the order with the payment result, the Web/App merchant handles results return on url_success (this way may be affected by customer transmission failure)  In both ways, the order is considered successful payment when: * Order status \"stat\" == \"c\" * Payment transaction of order status \"stat\" == 1 * Order amount (total_amount) match with the merchant's order amount  __Webhook Notification:__  Webhook notification is a mechanism to notify Web/App merchants when an order is successfully paid through an HTTP POST request. * How to receive webhook notifications?   * When sending an order to Bao Kim through API Send Order, remember to pass the webhooks parameter as described   * When your order is successfully paid, Bao Kim will POST the payment data to the URL on the webhooks parameter in the order. * How many times will a Webhook notification be sent?   * Send up to 10 times   * Every 5 minutes   * Stop sending when receiving a json string with err_code = 0, eg {\"err_code\": \"0\", \"message\": \"some message\"}   (help Bao Kim determine that the merchant has successfully received the notification)  Description of data on webhook notification: * Method: POST * Header: Content-Type: application/json * Body (check sample code on the right side)  Steps to check and handle when receiving webhook notification: 1. Check the integrity of the received data by checking the correctness of the signature as follows (See sample PHP code on the right tab, under the webhook data description):   * Use the secret value in the key/secret pair in your API Key   * Using the hash_hmac algorithm with sha256, sign the data you receive (except for the $sign field, of course) => $yourSign   * Compare the signature you generated ($yourSign) with the signature you received ($sign), if not the same => data is not incomplete 2. Check order payment status, payment transaction, payment amount, order completion   * Check order status ($order->stat == 'c' //completed)   * Check if the order information ($order) is correct with the order information on your web/app   * If the above checks are correct, you can be sure that the order has been paid and can be completed. 3. Returns JSON string with err_code = 0, eg {\"err_code\": \"0\", \"message\": \"some message\"} so that Bao Kim knows that the merchant has received the notice and does not continue to send it back. The maximum length of the returned data is 255 characters.  Example Webhook:      {       \"order\":{         \"id\":82127,         \"user_id\":1000007,         \"mrc_order_id\":\"Nam1645759079\",         \"txn_id\":69154,         \"ref_no\":null,         \"merchant_id\":40187,         \"total_amount\":3000000,         \"description\":\"eqxI4W4HFUPwyNxH\",         \"items\":\"{           \"period\":3,           \"total_amount\":\"3090000.00\",           \"down_payment\":\"750000.00\",           \"down_payment_percent\":\"25.00\",           \"paylater_amount\":\"2250000.00\",           \"pay_per_month\":\"780000.00\",           \"user_fee\":\"90000\",           \"merchant_fee\":\"90000\"         }\",         \"url_success\":\"https://www.google.com/\",         \"url_cancel\":null,         \"url_detail\":\"https://www.google.com/\",         \"stat\":\"c\",         \"lang\":\"en\",         \"type\":1,         \"bpm_id\":\"339\",         \"accept_qrpay\":1,         \"accept_bank\":1,         \"accept_cc\":1,         \"accept_ib\":1,         \"accept_ewallet\":1,         \"accept_installments\":1,         \"email\":\"2@bk.vn\",         \"name\":\"baokimjsc111\",         \"webhooks\":\"https://google.com\",         \"customer_name\":\"Nguyen Thanh nam\",         \"customer_email\":\"testpay@gmail.com\",         \"customer_phone\":\"84328271591\",         \"customer_address\":\"102 thai thinh\",         \"created_at\":\"2022-02-25 10:18:01\",         \"updated_at\":\"2022-02-25 10:23:12\"       },       \"txn\":{         \"id\":69154,         \"reference_id\":\"bk_82127_69154_41j\",         \"user_id\":1000007,         \"merchant_id\":40187,         \"order_id\":82127,         \"mrc_order_id\":\"nam1645759079\",         \"total_amount\":750550,         \"amount\":750000,         \"fee_amount\":0,         \"bank_fee_amount\":550,         \"bank_fix_fee_amount\":550,         \"fee_payer\":1,         \"bank_fee_payer\":1,         \"auth_code\":null,         \"auth_time\":\"\",         \"ref_no\":null,         \"bpm_id\":\"97\",         \"bank_ref_no\":\"507800079\",         \"bpm_type\":1,         \"gateway\":\"\",         \"stat\":1,         \"init_token\":null,         \"description\":\"eqxi4w4hfupwynxh\",         \"customer_email\":\"testpay@gmail.com\",         \"customer_phone\":\"84328271591\",         \"completed_at\":\"2022-02-25 10:23:12\",         \"created_at\":\"2022-02-25 10:18:24\",         \"updated_at\":\"2022-02-25 10:23:12\",         \"deleted_at\":null       },       \"dataToken\":[],       \"sign\":\"ffc020303d1ed4fbe5df95d83261524793358ab0a8e363ae265e3fc2c33dc560\"     }  __Data return on url_success:__  If the merchant web/app gets notifications through Webhook Notification, you can skip processing the return data on url_success and simply show the successful payment page to the customer. Otherwise, verify the return data on url_success as follows.  Data return on url_success * id: Request id (created by Bao Kim) * mrc_order_id: Order ID on merchant web/app * txn_id: Payment Transaction ID of order * total_amount: Order payment amount * stat: Order status * created_at: Time receive orders * updated_at: Payment confirmation time * checksum: Data security signature (see details below)  The checksum is signed on the parameter passed on url_success using the sha256 hash algorithm, with the security key being the secret key in your API key. How to verify the checksum on url_success please see the steps and sample code on the right tab. 
 *
 * OpenAPI spec version: 5.0.0
 * Contact: developer@baokim.vn
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
    /// InlineResponse2006Data
    /// </summary>
    [DataContract]
        public partial class InlineResponse2006Data :  IEquatable<InlineResponse2006Data>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="InlineResponse2006Data" /> class.
        /// </summary>
        /// <param name="paymentTxnId">paymentTxnId.</param>
        /// <param name="stat">stat.</param>
        /// <param name="userId">userId.</param>
        /// <param name="merchantId">merchantId.</param>
        /// <param name="orderId">orderId.</param>
        /// <param name="mrcOrderId">mrcOrderId.</param>
        /// <param name="netAmount">netAmount.</param>
        /// <param name="orderAmount">orderAmount.</param>
        /// <param name="payAmount">payAmount.</param>
        /// <param name="refundAmount">refundAmount.</param>
        /// <param name="feeAmount">feeAmount.</param>
        /// <param name="bankPercentFeeAmount">bankPercentFeeAmount.</param>
        /// <param name="feePayer">feePayer.</param>
        /// <param name="refNo">refNo.</param>
        /// <param name="bpmId">bpmId.</param>
        /// <param name="bpmType">bpmType.</param>
        /// <param name="description">description.</param>
        /// <param name="count">count.</param>
        /// <param name="amount">amount.</param>
        /// <param name="minusAmount">minusAmount.</param>
        /// <param name="createdAt">createdAt.</param>
        /// <param name="updatedAt">updatedAt.</param>
        /// <param name="id">id.</param>
        public InlineResponse2006Data(int? paymentTxnId = default(int?), int? stat = default(int?), int? userId = default(int?), int? merchantId = default(int?), int? orderId = default(int?), string mrcOrderId = default(string), string netAmount = default(string), string orderAmount = default(string), string payAmount = default(string), Object refundAmount = default(Object), string feeAmount = default(string), int? bankPercentFeeAmount = default(int?), string feePayer = default(string),  refNo = default(), int? bpmId = default(int?), int? bpmType = default(int?), Description description = default(Description), int? count = default(int?), int? amount = default(int?), string minusAmount = default(string), string createdAt = default(string), string updatedAt = default(string), int? id = default(int?))
        {
            this.PaymentTxnId = paymentTxnId;
            this.Stat = stat;
            this.UserId = userId;
            this.MerchantId = merchantId;
            this.OrderId = orderId;
            this.MrcOrderId = mrcOrderId;
            this.NetAmount = netAmount;
            this.OrderAmount = orderAmount;
            this.PayAmount = payAmount;
            this.RefundAmount = refundAmount;
            this.FeeAmount = feeAmount;
            this.BankPercentFeeAmount = bankPercentFeeAmount;
            this.FeePayer = feePayer;
            this.RefNo = refNo;
            this.BpmId = bpmId;
            this.BpmType = bpmType;
            this.Description = description;
            this.Count = count;
            this.Amount = amount;
            this.MinusAmount = minusAmount;
            this.CreatedAt = createdAt;
            this.UpdatedAt = updatedAt;
            this.Id = id;
        }
        
        /// <summary>
        /// Gets or Sets PaymentTxnId
        /// </summary>
        [DataMember(Name="payment_txn_id", EmitDefaultValue=false)]
        public int? PaymentTxnId { get; set; }

        /// <summary>
        /// Gets or Sets Stat
        /// </summary>
        [DataMember(Name="stat", EmitDefaultValue=false)]
        public int? Stat { get; set; }

        /// <summary>
        /// Gets or Sets UserId
        /// </summary>
        [DataMember(Name="user_id", EmitDefaultValue=false)]
        public int? UserId { get; set; }

        /// <summary>
        /// Gets or Sets MerchantId
        /// </summary>
        [DataMember(Name="merchant_id", EmitDefaultValue=false)]
        public int? MerchantId { get; set; }

        /// <summary>
        /// Gets or Sets OrderId
        /// </summary>
        [DataMember(Name="order_id", EmitDefaultValue=false)]
        public int? OrderId { get; set; }

        /// <summary>
        /// Gets or Sets MrcOrderId
        /// </summary>
        [DataMember(Name="mrc_order_id", EmitDefaultValue=false)]
        public string MrcOrderId { get; set; }

        /// <summary>
        /// Gets or Sets NetAmount
        /// </summary>
        [DataMember(Name="net_amount", EmitDefaultValue=false)]
        public string NetAmount { get; set; }

        /// <summary>
        /// Gets or Sets OrderAmount
        /// </summary>
        [DataMember(Name="order_amount", EmitDefaultValue=false)]
        public string OrderAmount { get; set; }

        /// <summary>
        /// Gets or Sets PayAmount
        /// </summary>
        [DataMember(Name="pay_amount", EmitDefaultValue=false)]
        public string PayAmount { get; set; }

        /// <summary>
        /// Gets or Sets RefundAmount
        /// </summary>
        [DataMember(Name="refund_amount", EmitDefaultValue=false)]
        public Object RefundAmount { get; set; }

        /// <summary>
        /// Gets or Sets FeeAmount
        /// </summary>
        [DataMember(Name="fee_amount", EmitDefaultValue=false)]
        public string FeeAmount { get; set; }

        /// <summary>
        /// Gets or Sets BankPercentFeeAmount
        /// </summary>
        [DataMember(Name="bank_percent_fee_amount", EmitDefaultValue=false)]
        public int? BankPercentFeeAmount { get; set; }

        /// <summary>
        /// Gets or Sets FeePayer
        /// </summary>
        [DataMember(Name="fee_payer", EmitDefaultValue=false)]
        public string FeePayer { get; set; }

        /// <summary>
        /// Gets or Sets RefNo
        /// </summary>
        [DataMember(Name="ref_no", EmitDefaultValue=false)]
        public  RefNo { get; set; }

        /// <summary>
        /// Gets or Sets BpmId
        /// </summary>
        [DataMember(Name="bpm_id", EmitDefaultValue=false)]
        public int? BpmId { get; set; }

        /// <summary>
        /// Gets or Sets BpmType
        /// </summary>
        [DataMember(Name="bpm_type", EmitDefaultValue=false)]
        public int? BpmType { get; set; }

        /// <summary>
        /// Gets or Sets Description
        /// </summary>
        [DataMember(Name="description", EmitDefaultValue=false)]
        public Description Description { get; set; }

        /// <summary>
        /// Gets or Sets Count
        /// </summary>
        [DataMember(Name="count", EmitDefaultValue=false)]
        public int? Count { get; set; }

        /// <summary>
        /// Gets or Sets Amount
        /// </summary>
        [DataMember(Name="amount", EmitDefaultValue=false)]
        public int? Amount { get; set; }

        /// <summary>
        /// Gets or Sets MinusAmount
        /// </summary>
        [DataMember(Name="minus_amount", EmitDefaultValue=false)]
        public string MinusAmount { get; set; }

        /// <summary>
        /// Gets or Sets CreatedAt
        /// </summary>
        [DataMember(Name="created_at", EmitDefaultValue=false)]
        public string CreatedAt { get; set; }

        /// <summary>
        /// Gets or Sets UpdatedAt
        /// </summary>
        [DataMember(Name="updated_at", EmitDefaultValue=false)]
        public string UpdatedAt { get; set; }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public int? Id { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class InlineResponse2006Data {\n");
            sb.Append("  PaymentTxnId: ").Append(PaymentTxnId).Append("\n");
            sb.Append("  Stat: ").Append(Stat).Append("\n");
            sb.Append("  UserId: ").Append(UserId).Append("\n");
            sb.Append("  MerchantId: ").Append(MerchantId).Append("\n");
            sb.Append("  OrderId: ").Append(OrderId).Append("\n");
            sb.Append("  MrcOrderId: ").Append(MrcOrderId).Append("\n");
            sb.Append("  NetAmount: ").Append(NetAmount).Append("\n");
            sb.Append("  OrderAmount: ").Append(OrderAmount).Append("\n");
            sb.Append("  PayAmount: ").Append(PayAmount).Append("\n");
            sb.Append("  RefundAmount: ").Append(RefundAmount).Append("\n");
            sb.Append("  FeeAmount: ").Append(FeeAmount).Append("\n");
            sb.Append("  BankPercentFeeAmount: ").Append(BankPercentFeeAmount).Append("\n");
            sb.Append("  FeePayer: ").Append(FeePayer).Append("\n");
            sb.Append("  RefNo: ").Append(RefNo).Append("\n");
            sb.Append("  BpmId: ").Append(BpmId).Append("\n");
            sb.Append("  BpmType: ").Append(BpmType).Append("\n");
            sb.Append("  Description: ").Append(Description).Append("\n");
            sb.Append("  Count: ").Append(Count).Append("\n");
            sb.Append("  Amount: ").Append(Amount).Append("\n");
            sb.Append("  MinusAmount: ").Append(MinusAmount).Append("\n");
            sb.Append("  CreatedAt: ").Append(CreatedAt).Append("\n");
            sb.Append("  UpdatedAt: ").Append(UpdatedAt).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
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
            return this.Equals(input as InlineResponse2006Data);
        }

        /// <summary>
        /// Returns true if InlineResponse2006Data instances are equal
        /// </summary>
        /// <param name="input">Instance of InlineResponse2006Data to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(InlineResponse2006Data input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.PaymentTxnId == input.PaymentTxnId ||
                    (this.PaymentTxnId != null &&
                    this.PaymentTxnId.Equals(input.PaymentTxnId))
                ) && 
                (
                    this.Stat == input.Stat ||
                    (this.Stat != null &&
                    this.Stat.Equals(input.Stat))
                ) && 
                (
                    this.UserId == input.UserId ||
                    (this.UserId != null &&
                    this.UserId.Equals(input.UserId))
                ) && 
                (
                    this.MerchantId == input.MerchantId ||
                    (this.MerchantId != null &&
                    this.MerchantId.Equals(input.MerchantId))
                ) && 
                (
                    this.OrderId == input.OrderId ||
                    (this.OrderId != null &&
                    this.OrderId.Equals(input.OrderId))
                ) && 
                (
                    this.MrcOrderId == input.MrcOrderId ||
                    (this.MrcOrderId != null &&
                    this.MrcOrderId.Equals(input.MrcOrderId))
                ) && 
                (
                    this.NetAmount == input.NetAmount ||
                    (this.NetAmount != null &&
                    this.NetAmount.Equals(input.NetAmount))
                ) && 
                (
                    this.OrderAmount == input.OrderAmount ||
                    (this.OrderAmount != null &&
                    this.OrderAmount.Equals(input.OrderAmount))
                ) && 
                (
                    this.PayAmount == input.PayAmount ||
                    (this.PayAmount != null &&
                    this.PayAmount.Equals(input.PayAmount))
                ) && 
                (
                    this.RefundAmount == input.RefundAmount ||
                    (this.RefundAmount != null &&
                    this.RefundAmount.Equals(input.RefundAmount))
                ) && 
                (
                    this.FeeAmount == input.FeeAmount ||
                    (this.FeeAmount != null &&
                    this.FeeAmount.Equals(input.FeeAmount))
                ) && 
                (
                    this.BankPercentFeeAmount == input.BankPercentFeeAmount ||
                    (this.BankPercentFeeAmount != null &&
                    this.BankPercentFeeAmount.Equals(input.BankPercentFeeAmount))
                ) && 
                (
                    this.FeePayer == input.FeePayer ||
                    (this.FeePayer != null &&
                    this.FeePayer.Equals(input.FeePayer))
                ) && 
                (
                    this.RefNo == input.RefNo ||
                    (this.RefNo != null &&
                    this.RefNo.Equals(input.RefNo))
                ) && 
                (
                    this.BpmId == input.BpmId ||
                    (this.BpmId != null &&
                    this.BpmId.Equals(input.BpmId))
                ) && 
                (
                    this.BpmType == input.BpmType ||
                    (this.BpmType != null &&
                    this.BpmType.Equals(input.BpmType))
                ) && 
                (
                    this.Description == input.Description ||
                    (this.Description != null &&
                    this.Description.Equals(input.Description))
                ) && 
                (
                    this.Count == input.Count ||
                    (this.Count != null &&
                    this.Count.Equals(input.Count))
                ) && 
                (
                    this.Amount == input.Amount ||
                    (this.Amount != null &&
                    this.Amount.Equals(input.Amount))
                ) && 
                (
                    this.MinusAmount == input.MinusAmount ||
                    (this.MinusAmount != null &&
                    this.MinusAmount.Equals(input.MinusAmount))
                ) && 
                (
                    this.CreatedAt == input.CreatedAt ||
                    (this.CreatedAt != null &&
                    this.CreatedAt.Equals(input.CreatedAt))
                ) && 
                (
                    this.UpdatedAt == input.UpdatedAt ||
                    (this.UpdatedAt != null &&
                    this.UpdatedAt.Equals(input.UpdatedAt))
                ) && 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
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
                if (this.PaymentTxnId != null)
                    hashCode = hashCode * 59 + this.PaymentTxnId.GetHashCode();
                if (this.Stat != null)
                    hashCode = hashCode * 59 + this.Stat.GetHashCode();
                if (this.UserId != null)
                    hashCode = hashCode * 59 + this.UserId.GetHashCode();
                if (this.MerchantId != null)
                    hashCode = hashCode * 59 + this.MerchantId.GetHashCode();
                if (this.OrderId != null)
                    hashCode = hashCode * 59 + this.OrderId.GetHashCode();
                if (this.MrcOrderId != null)
                    hashCode = hashCode * 59 + this.MrcOrderId.GetHashCode();
                if (this.NetAmount != null)
                    hashCode = hashCode * 59 + this.NetAmount.GetHashCode();
                if (this.OrderAmount != null)
                    hashCode = hashCode * 59 + this.OrderAmount.GetHashCode();
                if (this.PayAmount != null)
                    hashCode = hashCode * 59 + this.PayAmount.GetHashCode();
                if (this.RefundAmount != null)
                    hashCode = hashCode * 59 + this.RefundAmount.GetHashCode();
                if (this.FeeAmount != null)
                    hashCode = hashCode * 59 + this.FeeAmount.GetHashCode();
                if (this.BankPercentFeeAmount != null)
                    hashCode = hashCode * 59 + this.BankPercentFeeAmount.GetHashCode();
                if (this.FeePayer != null)
                    hashCode = hashCode * 59 + this.FeePayer.GetHashCode();
                if (this.RefNo != null)
                    hashCode = hashCode * 59 + this.RefNo.GetHashCode();
                if (this.BpmId != null)
                    hashCode = hashCode * 59 + this.BpmId.GetHashCode();
                if (this.BpmType != null)
                    hashCode = hashCode * 59 + this.BpmType.GetHashCode();
                if (this.Description != null)
                    hashCode = hashCode * 59 + this.Description.GetHashCode();
                if (this.Count != null)
                    hashCode = hashCode * 59 + this.Count.GetHashCode();
                if (this.Amount != null)
                    hashCode = hashCode * 59 + this.Amount.GetHashCode();
                if (this.MinusAmount != null)
                    hashCode = hashCode * 59 + this.MinusAmount.GetHashCode();
                if (this.CreatedAt != null)
                    hashCode = hashCode * 59 + this.CreatedAt.GetHashCode();
                if (this.UpdatedAt != null)
                    hashCode = hashCode * 59 + this.UpdatedAt.GetHashCode();
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
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
