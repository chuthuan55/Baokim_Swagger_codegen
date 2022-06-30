/* 
 * Example for response examples value
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0
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
    /// InlineResponse200
    /// </summary>
    [DataContract]
        public partial class InlineResponse200 :  IEquatable<InlineResponse200>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="InlineResponse200" /> class.
        /// </summary>
        /// <param name="responseCode">Response code.</param>
        /// <param name="responseMessage">Response message.</param>
        /// <param name="partnerCode">BAOKIM.</param>
        /// <param name="orderId">Unique id for each VA.</param>
        /// <param name="collectAmountMin">Min collect amount (Min 50.000 vnd).</param>
        /// <param name="collectAmountMax">Max collect amount (Max 50.000.000vnd).</param>
        /// <param name="expireDate">Expire date. Format: YYYYMM-DD HH:II:SS.</param>
        /// <param name="accountInfo">accountInfo.</param>
        public InlineResponse200(decimal? responseCode = default(decimal?), string responseMessage = default(string), string partnerCode = default(string), string orderId = default(string), decimal? collectAmountMin = default(decimal?), decimal? collectAmountMax = default(decimal?), string expireDate = default(string), List<Object> accountInfo = default(List<Object>))
        {
            this.ResponseCode = responseCode;
            this.ResponseMessage = responseMessage;
            this.PartnerCode = partnerCode;
            this.OrderId = orderId;
            this.CollectAmountMin = collectAmountMin;
            this.CollectAmountMax = collectAmountMax;
            this.ExpireDate = expireDate;
            this.AccountInfo = accountInfo;
        }
        
        /// <summary>
        /// Response code
        /// </summary>
        /// <value>Response code</value>
        [DataMember(Name="ResponseCode", EmitDefaultValue=false)]
        public decimal? ResponseCode { get; set; }

        /// <summary>
        /// Response message
        /// </summary>
        /// <value>Response message</value>
        [DataMember(Name="ResponseMessage", EmitDefaultValue=false)]
        public string ResponseMessage { get; set; }

        /// <summary>
        /// BAOKIM
        /// </summary>
        /// <value>BAOKIM</value>
        [DataMember(Name="PartnerCode", EmitDefaultValue=false)]
        public string PartnerCode { get; set; }

        /// <summary>
        /// Unique id for each VA
        /// </summary>
        /// <value>Unique id for each VA</value>
        [DataMember(Name="OrderId", EmitDefaultValue=false)]
        public string OrderId { get; set; }

        /// <summary>
        /// Min collect amount (Min 50.000 vnd)
        /// </summary>
        /// <value>Min collect amount (Min 50.000 vnd)</value>
        [DataMember(Name="CollectAmountMin", EmitDefaultValue=false)]
        public decimal? CollectAmountMin { get; set; }

        /// <summary>
        /// Max collect amount (Max 50.000.000vnd)
        /// </summary>
        /// <value>Max collect amount (Max 50.000.000vnd)</value>
        [DataMember(Name="CollectAmountMax", EmitDefaultValue=false)]
        public decimal? CollectAmountMax { get; set; }

        /// <summary>
        /// Expire date. Format: YYYYMM-DD HH:II:SS
        /// </summary>
        /// <value>Expire date. Format: YYYYMM-DD HH:II:SS</value>
        [DataMember(Name="ExpireDate", EmitDefaultValue=false)]
        public string ExpireDate { get; set; }

        /// <summary>
        /// Gets or Sets AccountInfo
        /// </summary>
        [DataMember(Name="AccountInfo", EmitDefaultValue=false)]
        public List<Object> AccountInfo { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class InlineResponse200 {\n");
            sb.Append("  ResponseCode: ").Append(ResponseCode).Append("\n");
            sb.Append("  ResponseMessage: ").Append(ResponseMessage).Append("\n");
            sb.Append("  PartnerCode: ").Append(PartnerCode).Append("\n");
            sb.Append("  OrderId: ").Append(OrderId).Append("\n");
            sb.Append("  CollectAmountMin: ").Append(CollectAmountMin).Append("\n");
            sb.Append("  CollectAmountMax: ").Append(CollectAmountMax).Append("\n");
            sb.Append("  ExpireDate: ").Append(ExpireDate).Append("\n");
            sb.Append("  AccountInfo: ").Append(AccountInfo).Append("\n");
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
            return this.Equals(input as InlineResponse200);
        }

        /// <summary>
        /// Returns true if InlineResponse200 instances are equal
        /// </summary>
        /// <param name="input">Instance of InlineResponse200 to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(InlineResponse200 input)
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
                    this.PartnerCode == input.PartnerCode ||
                    (this.PartnerCode != null &&
                    this.PartnerCode.Equals(input.PartnerCode))
                ) && 
                (
                    this.OrderId == input.OrderId ||
                    (this.OrderId != null &&
                    this.OrderId.Equals(input.OrderId))
                ) && 
                (
                    this.CollectAmountMin == input.CollectAmountMin ||
                    (this.CollectAmountMin != null &&
                    this.CollectAmountMin.Equals(input.CollectAmountMin))
                ) && 
                (
                    this.CollectAmountMax == input.CollectAmountMax ||
                    (this.CollectAmountMax != null &&
                    this.CollectAmountMax.Equals(input.CollectAmountMax))
                ) && 
                (
                    this.ExpireDate == input.ExpireDate ||
                    (this.ExpireDate != null &&
                    this.ExpireDate.Equals(input.ExpireDate))
                ) && 
                (
                    this.AccountInfo == input.AccountInfo ||
                    this.AccountInfo != null &&
                    input.AccountInfo != null &&
                    this.AccountInfo.SequenceEqual(input.AccountInfo)
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
                if (this.PartnerCode != null)
                    hashCode = hashCode * 59 + this.PartnerCode.GetHashCode();
                if (this.OrderId != null)
                    hashCode = hashCode * 59 + this.OrderId.GetHashCode();
                if (this.CollectAmountMin != null)
                    hashCode = hashCode * 59 + this.CollectAmountMin.GetHashCode();
                if (this.CollectAmountMax != null)
                    hashCode = hashCode * 59 + this.CollectAmountMax.GetHashCode();
                if (this.ExpireDate != null)
                    hashCode = hashCode * 59 + this.ExpireDate.GetHashCode();
                if (this.AccountInfo != null)
                    hashCode = hashCode * 59 + this.AccountInfo.GetHashCode();
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
