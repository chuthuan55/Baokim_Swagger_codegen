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
    /// CollectionV2Body
    /// </summary>
    [DataContract]
        public partial class CollectionV2Body :  IEquatable<CollectionV2Body>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CollectionV2Body" /> class.
        /// </summary>
        /// <param name="requestId">Unique code .</param>
        /// <param name="requestTime">Time send the request from PARTNER , format: YYYY-MM-DD HH:MM:SS..</param>
        /// <param name="partnerCode">Unique code BAOKIM provide.</param>
        /// <param name="operation">9001: create va - 9002: update va.</param>
        /// <param name="createType">Fix &#x3D; 2.</param>
        /// <param name="accName">The name of Account holder (name of USER).</param>
        /// <param name="collectAmountMin">collect amount min (50.000).</param>
        /// <param name="collectAmountMax">collect amount min (50.000.000).</param>
        /// <param name="accNo">Required when update:VA number need to update information. If create VA, send NULL.</param>
        /// <param name="orderId">Unique id for each VA.</param>
        /// <param name="expireDate">Expire date. Format: YYYYMM-DD HH:II:SS.</param>
        public CollectionV2Body(string requestId = default(string), string requestTime = default(string), string partnerCode = default(string), decimal? operation = default(decimal?), string createType = default(string), string accName = default(string), decimal? collectAmountMin = default(decimal?), decimal? collectAmountMax = default(decimal?), string accNo = default(string), string orderId = default(string), string expireDate = default(string))
        {
            this.RequestId = requestId;
            this.RequestTime = requestTime;
            this.PartnerCode = partnerCode;
            this.Operation = operation;
            this.CreateType = createType;
            this.AccName = accName;
            this.CollectAmountMin = collectAmountMin;
            this.CollectAmountMax = collectAmountMax;
            this.AccNo = accNo;
            this.OrderId = orderId;
            this.ExpireDate = expireDate;
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
        /// 9001: create va - 9002: update va
        /// </summary>
        /// <value>9001: create va - 9002: update va</value>
        [DataMember(Name="Operation", EmitDefaultValue=false)]
        public decimal? Operation { get; set; }

        /// <summary>
        /// Fix &#x3D; 2
        /// </summary>
        /// <value>Fix &#x3D; 2</value>
        [DataMember(Name="CreateType", EmitDefaultValue=false)]
        public string CreateType { get; set; }

        /// <summary>
        /// The name of Account holder (name of USER)
        /// </summary>
        /// <value>The name of Account holder (name of USER)</value>
        [DataMember(Name="AccName", EmitDefaultValue=false)]
        public string AccName { get; set; }

        /// <summary>
        /// collect amount min (50.000)
        /// </summary>
        /// <value>collect amount min (50.000)</value>
        [DataMember(Name="CollectAmountMin", EmitDefaultValue=false)]
        public decimal? CollectAmountMin { get; set; }

        /// <summary>
        /// collect amount min (50.000.000)
        /// </summary>
        /// <value>collect amount min (50.000.000)</value>
        [DataMember(Name="CollectAmountMax", EmitDefaultValue=false)]
        public decimal? CollectAmountMax { get; set; }

        /// <summary>
        /// Required when update:VA number need to update information. If create VA, send NULL
        /// </summary>
        /// <value>Required when update:VA number need to update information. If create VA, send NULL</value>
        [DataMember(Name="AccNo", EmitDefaultValue=false)]
        public string AccNo { get; set; }

        /// <summary>
        /// Unique id for each VA
        /// </summary>
        /// <value>Unique id for each VA</value>
        [DataMember(Name="OrderId", EmitDefaultValue=false)]
        public string OrderId { get; set; }

        /// <summary>
        /// Expire date. Format: YYYYMM-DD HH:II:SS
        /// </summary>
        /// <value>Expire date. Format: YYYYMM-DD HH:II:SS</value>
        [DataMember(Name="ExpireDate", EmitDefaultValue=false)]
        public string ExpireDate { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class CollectionV2Body {\n");
            sb.Append("  RequestId: ").Append(RequestId).Append("\n");
            sb.Append("  RequestTime: ").Append(RequestTime).Append("\n");
            sb.Append("  PartnerCode: ").Append(PartnerCode).Append("\n");
            sb.Append("  Operation: ").Append(Operation).Append("\n");
            sb.Append("  CreateType: ").Append(CreateType).Append("\n");
            sb.Append("  AccName: ").Append(AccName).Append("\n");
            sb.Append("  CollectAmountMin: ").Append(CollectAmountMin).Append("\n");
            sb.Append("  CollectAmountMax: ").Append(CollectAmountMax).Append("\n");
            sb.Append("  AccNo: ").Append(AccNo).Append("\n");
            sb.Append("  OrderId: ").Append(OrderId).Append("\n");
            sb.Append("  ExpireDate: ").Append(ExpireDate).Append("\n");
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
            return this.Equals(input as CollectionV2Body);
        }

        /// <summary>
        /// Returns true if CollectionV2Body instances are equal
        /// </summary>
        /// <param name="input">Instance of CollectionV2Body to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(CollectionV2Body input)
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
                ) && 
                (
                    this.Operation == input.Operation ||
                    (this.Operation != null &&
                    this.Operation.Equals(input.Operation))
                ) && 
                (
                    this.CreateType == input.CreateType ||
                    (this.CreateType != null &&
                    this.CreateType.Equals(input.CreateType))
                ) && 
                (
                    this.AccName == input.AccName ||
                    (this.AccName != null &&
                    this.AccName.Equals(input.AccName))
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
                    this.AccNo == input.AccNo ||
                    (this.AccNo != null &&
                    this.AccNo.Equals(input.AccNo))
                ) && 
                (
                    this.OrderId == input.OrderId ||
                    (this.OrderId != null &&
                    this.OrderId.Equals(input.OrderId))
                ) && 
                (
                    this.ExpireDate == input.ExpireDate ||
                    (this.ExpireDate != null &&
                    this.ExpireDate.Equals(input.ExpireDate))
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
                if (this.Operation != null)
                    hashCode = hashCode * 59 + this.Operation.GetHashCode();
                if (this.CreateType != null)
                    hashCode = hashCode * 59 + this.CreateType.GetHashCode();
                if (this.AccName != null)
                    hashCode = hashCode * 59 + this.AccName.GetHashCode();
                if (this.CollectAmountMin != null)
                    hashCode = hashCode * 59 + this.CollectAmountMin.GetHashCode();
                if (this.CollectAmountMax != null)
                    hashCode = hashCode * 59 + this.CollectAmountMax.GetHashCode();
                if (this.AccNo != null)
                    hashCode = hashCode * 59 + this.AccNo.GetHashCode();
                if (this.OrderId != null)
                    hashCode = hashCode * 59 + this.OrderId.GetHashCode();
                if (this.ExpireDate != null)
                    hashCode = hashCode * 59 + this.ExpireDate.GetHashCode();
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