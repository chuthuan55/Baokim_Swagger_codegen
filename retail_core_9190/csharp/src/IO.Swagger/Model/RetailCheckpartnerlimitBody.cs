/* 
 * Retail api
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
    /// RetailCheckpartnerlimitBody
    /// </summary>
    [DataContract]
        public partial class RetailCheckpartnerlimitBody :  IEquatable<RetailCheckpartnerlimitBody>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="RetailCheckpartnerlimitBody" /> class.
        /// </summary>
        /// <param name="requestId">Unique code .</param>
        /// <param name="requestTime">Time send the request from PARTNER , format: YYYY-MM-DD HH:MM:SS..</param>
        /// <param name="partnerCode">Unique code BAOKIM provide.</param>
        public RetailCheckpartnerlimitBody(string requestId = default(string), string requestTime = default(string), string partnerCode = default(string))
        {
            this.RequestId = requestId;
            this.RequestTime = requestTime;
            this.PartnerCode = partnerCode;
        }
        
        /// <summary>
        /// Unique code 
        /// </summary>
        /// <value>Unique code </value>
        [DataMember(Name="RequestId", EmitDefaultValue=false)]
        public string RequestId { get; set; }

        /// <summary>
        /// Time send the request from PARTNER , format: YYYY-MM-DD HH:MM:SS.
        /// </summary>
        /// <value>Time send the request from PARTNER , format: YYYY-MM-DD HH:MM:SS.</value>
        [DataMember(Name="RequestTime", EmitDefaultValue=false)]
        public string RequestTime { get; set; }

        /// <summary>
        /// Unique code BAOKIM provide
        /// </summary>
        /// <value>Unique code BAOKIM provide</value>
        [DataMember(Name="PartnerCode", EmitDefaultValue=false)]
        public string PartnerCode { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class RetailCheckpartnerlimitBody {\n");
            sb.Append("  RequestId: ").Append(RequestId).Append("\n");
            sb.Append("  RequestTime: ").Append(RequestTime).Append("\n");
            sb.Append("  PartnerCode: ").Append(PartnerCode).Append("\n");
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
            return this.Equals(input as RetailCheckpartnerlimitBody);
        }

        /// <summary>
        /// Returns true if RetailCheckpartnerlimitBody instances are equal
        /// </summary>
        /// <param name="input">Instance of RetailCheckpartnerlimitBody to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(RetailCheckpartnerlimitBody input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.RequestId == input.RequestId ||
                    (this.RequestId != null &&
                    this.RequestId.Equals(input.RequestId))
                ) && 
                (
                    this.RequestTime == input.RequestTime ||
                    (this.RequestTime != null &&
                    this.RequestTime.Equals(input.RequestTime))
                ) && 
                (
                    this.PartnerCode == input.PartnerCode ||
                    (this.PartnerCode != null &&
                    this.PartnerCode.Equals(input.PartnerCode))
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
                if (this.RequestId != null)
                    hashCode = hashCode * 59 + this.RequestId.GetHashCode();
                if (this.RequestTime != null)
                    hashCode = hashCode * 59 + this.RequestTime.GetHashCode();
                if (this.PartnerCode != null)
                    hashCode = hashCode * 59 + this.PartnerCode.GetHashCode();
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
