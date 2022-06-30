/*
 * Collection payments
 * <img src=\"https://devtest.baokim.vn/collection/core_ctt/image/Picture1.png\" class=\"image-collection-payment\" /> <p><strong>Note:</strong></p> <p>+ In case PARTNER want to use collect via Virtual Account, PARTNER will need to buid:</p> <p style=\"padding-left: 50px;\">     - <a href=\"#operations-Virtual_Account_4\\.0-8442c69ffbaf4b3677a52fa3ebcef6d4\">Register virtual account</a> <br>     - <a href=\"#operations-Virtual_Account_4\\.0-1796c61005edee3976097a607fe9dbaa\">Update virtual account informations</a> <br>     - <a href=\"#operations-tag-Notice_of_collection_transaction\">Notice of collection transaction</a> <br> </p>
 *
 * OpenAPI spec version: 2.3 and 4.0
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
import java.math.BigDecimal;
/**
 * InlineResponse2001
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-06-30T01:31:18.186Z[Etc/UTC]")
public class InlineResponse2001 {
  @SerializedName("ResponseCode")
  private BigDecimal responseCode = null;

  @SerializedName("ResponseMessage")
  private String responseMessage = null;

  @SerializedName("ReferenceId")
  private String referenceId = null;

  @SerializedName("AccNo")
  private String accNo = null;

  @SerializedName("AffTransDebt")
  private BigDecimal affTransDebt = null;

  @SerializedName("Signature")
  private String signature = null;

  public InlineResponse2001 responseCode(BigDecimal responseCode) {
    this.responseCode = responseCode;
    return this;
  }

   /**
   * Response code
   * @return responseCode
  **/
  @Schema(example = "200", description = "Response code")
  public BigDecimal getResponseCode() {
    return responseCode;
  }

  public void setResponseCode(BigDecimal responseCode) {
    this.responseCode = responseCode;
  }

  public InlineResponse2001 responseMessage(String responseMessage) {
    this.responseMessage = responseMessage;
    return this;
  }

   /**
   * Response message
   * @return responseMessage
  **/
  @Schema(example = "Success", description = "Response message")
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
   * Unique transaction id in PARTNER system
   * @return referenceId
  **/
  @Schema(example = "PARTNERCODE58b480bcb05126f7f789", description = "Unique transaction id in PARTNER system")
  public String getReferenceId() {
    return referenceId;
  }

  public void setReferenceId(String referenceId) {
    this.referenceId = referenceId;
  }

  public InlineResponse2001 accNo(String accNo) {
    this.accNo = accNo;
    return this;
  }

   /**
   * Unique id for each VA
   * @return accNo
  **/
  @Schema(example = "BK1632129167822619", description = "Unique id for each VA")
  public String getAccNo() {
    return accNo;
  }

  public void setAccNo(String accNo) {
    this.accNo = accNo;
  }

  public InlineResponse2001 affTransDebt(BigDecimal affTransDebt) {
    this.affTransDebt = affTransDebt;
    return this;
  }

   /**
   * Remain amount of VA
   * @return affTransDebt
  **/
  @Schema(example = "9500000", description = "Remain amount of VA")
  public BigDecimal getAffTransDebt() {
    return affTransDebt;
  }

  public void setAffTransDebt(BigDecimal affTransDebt) {
    this.affTransDebt = affTransDebt;
  }

  public InlineResponse2001 signature(String signature) {
    this.signature = signature;
    return this;
  }

   /**
   * Baokim will sign with digital signature of data returned using RSACryptoServiceProvider. Returns the base64 encoding. Data is structured: ResponseCode|ResponseMessage|ReferenceId| AccNo|AffTransDebt
   * @return signature
  **/
  @Schema(example = "HqsE04yJKM/82YWPDXN9KBCGbwA5T/MhgQHmo4fkzbG9LGxPBdX+8vLDlR6EzO9HnMM5FNIQ8AjfReD+d13ksIwImzocr80S13gnPfYiCL611hfpQFZDz3KsXnYIXrm9TcIhwnuRnFibQ9GoBHCqGjiV9I5SPIoykzFiiyzdtKI=", description = "Baokim will sign with digital signature of data returned using RSACryptoServiceProvider. Returns the base64 encoding. Data is structured: ResponseCode|ResponseMessage|ReferenceId| AccNo|AffTransDebt")
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
        Objects.equals(this.accNo, inlineResponse2001.accNo) &&
        Objects.equals(this.affTransDebt, inlineResponse2001.affTransDebt) &&
        Objects.equals(this.signature, inlineResponse2001.signature);
  }

  @Override
  public int hashCode() {
    return Objects.hash(responseCode, responseMessage, referenceId, accNo, affTransDebt, signature);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InlineResponse2001 {\n");
    
    sb.append("    responseCode: ").append(toIndentedString(responseCode)).append("\n");
    sb.append("    responseMessage: ").append(toIndentedString(responseMessage)).append("\n");
    sb.append("    referenceId: ").append(toIndentedString(referenceId)).append("\n");
    sb.append("    accNo: ").append(toIndentedString(accNo)).append("\n");
    sb.append("    affTransDebt: ").append(toIndentedString(affTransDebt)).append("\n");
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
