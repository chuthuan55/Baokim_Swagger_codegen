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
        /// <param name="responseCode">Response code.</param>
        /// <param name="responseMessage">Response message.</param>
        /// <param name="referenceId">Unique transaction id in PARTNER system.</param>
        /// <param name="accNo">Unique id for each VA.</param>
        /// <param name="affTransDebt">Remain amount of VA.</param>
        /// <param name="signature">Baokim will sign with digital signature of data returned using RSACryptoServiceProvider. Returns the base64 encoding. Data is structured: ResponseCode|ResponseMessage|ReferenceId| AccNo|AffTransDebt.</param>
        public InlineResponse2001(decimal? responseCode = default(decimal?), string responseMessage = default(string), string referenceId = default(string), string accNo = default(string), decimal? affTransDebt = default(decimal?), string signature = default(string))
        {
            this.ResponseCode = responseCode;
            this.ResponseMessage = responseMessage;
            this.ReferenceId = referenceId;
            this.AccNo = accNo;
            this.AffTransDebt = affTransDebt;
            this.Signature = signature;
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
        /// Unique transaction id in PARTNER system
        /// </summary>
        /// <value>Unique transaction id in PARTNER system</value>
        [DataMember(Name="ReferenceId", EmitDefaultValue=false)]
        public string ReferenceId { get; set; }

        /// <summary>
        /// Unique id for each VA
        /// </summary>
        /// <value>Unique id for each VA</value>
        [DataMember(Name="AccNo", EmitDefaultValue=false)]
        public string AccNo { get; set; }

        /// <summary>
        /// Remain amount of VA
        /// </summary>
        /// <value>Remain amount of VA</value>
        [DataMember(Name="AffTransDebt", EmitDefaultValue=false)]
        public decimal? AffTransDebt { get; set; }

        /// <summary>
        /// Baokim will sign with digital signature of data returned using RSACryptoServiceProvider. Returns the base64 encoding. Data is structured: ResponseCode|ResponseMessage|ReferenceId| AccNo|AffTransDebt
        /// </summary>
        /// <value>Baokim will sign with digital signature of data returned using RSACryptoServiceProvider. Returns the base64 encoding. Data is structured: ResponseCode|ResponseMessage|ReferenceId| AccNo|AffTransDebt</value>
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
            sb.Append("  AccNo: ").Append(AccNo).Append("\n");
            sb.Append("  AffTransDebt: ").Append(AffTransDebt).Append("\n");
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
                    this.AccNo == input.AccNo ||
                    (this.AccNo != null &&
                    this.AccNo.Equals(input.AccNo))
                ) && 
                (
                    this.AffTransDebt == input.AffTransDebt ||
                    (this.AffTransDebt != null &&
                    this.AffTransDebt.Equals(input.AffTransDebt))
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
                if (this.AccNo != null)
                    hashCode = hashCode * 59 + this.AccNo.GetHashCode();
                if (this.AffTransDebt != null)
                    hashCode = hashCode * 59 + this.AffTransDebt.GetHashCode();
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