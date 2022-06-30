# IO.Swagger.Api.ResponseCodeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CollectionResponseCodeGet**](ResponseCodeApi.md#collectionresponsecodeget) | **GET** Collection response code | Collection response code

<a name="collectionresponsecodeget"></a>
# **CollectionResponseCodeGet**
> void CollectionResponseCodeGet ()

Collection response code

<table>         <thead>         <tr>             <th>ResponseCode</th>             <th>ResponseMessage</th>         </tr>         </thead>         <tbody>         <tr>             <td>200</td>             <td>Successful</td>         </tr>         <tr>             <td>99</td>             <td>Transaction timeout </td>         </tr>         <tr>             <td>11</td>             <td>Failed</td>         </tr>         <tr>             <td>101</td>             <td>Error processing from Baokim</td>         </tr>         <tr>             <td>102</td>             <td>Error from Bank </td>         </tr>         <tr>             <td>103</td>             <td>Operation is incorrect</td>         </tr>         <tr>             <td>104</td>             <td>RequestId or request  is incorrect</td>         </tr>         <tr>             <td>105</td>             <td>PartnerCode is incorrect  </td>         </tr>         <tr>             <td>106</td>             <td>AccName is incorrect</td>         </tr>         <tr>             <td>107</td>             <td>ClientIdNo is incorrect</td>         </tr>         <tr>             <td>108</td>             <td>IssuedDate hoặc IssuedPlace is incorrect</td>         </tr>         <tr>             <td>109</td>             <td>CollectAmount is incorrect</td>         </tr>         <tr>             <td>110</td>             <td>ExpireDate is incorrect</td>         </tr>         <tr>             <td>111</td>             <td>AccNo is incorrect</td>         </tr>         <tr>             <td>112</td>             <td>AccNo is not exist</td>         </tr>         <tr>             <td>113</td>             <td>RefferenceId is incorrect</td>         </tr>         <tr>             <td>114</td>             <td>RefferenceId isn’t exists</td>         </tr>         <tr>             <td>115</td>             <td class=\"bg-color-red\">TransAmount  is incorrect</td>         </tr>         <tr>             <td>116</td>             <td class=\"bg-color-red\">TransTime  is incorrect</td>         </tr>         <tr>             <td>117</td>             <td class=\"bg-color-red\">BefTransDebt  is incorrect</td>         </tr>         <tr>             <td>118</td>             <td class=\"bg-color-red\">TransId is incorrect</td>         </tr>         <tr>             <td>119</td>             <td class=\"bg-color-red\">AffTransDebt is incorrect</td>         </tr>         <tr>             <td>120</td>             <td class=\"bg-color-red\">Signature is incorrect</td>         </tr>         <tr>             <td>121</td>             <td>AccountType is incorrect</td>         </tr>         <tr>             <td>122</td>             <td>OrderId is incorrect</td>         </tr>         <tr>             <td>127</td>             <td>Bank is incorrect</td>         </tr>         <tr>             <td>128</td>             <td>CollectionType is incorrect</td>         </tr>         <tr>             <td>129</td>             <td>Bank not used this CollectionType</td>         </tr>         </tbody>     </table>     <p>* <strong class=\"bg-color-red\">Red codes</strong> represent errors that will arpear when developing the function: <a href=\"#notice-of-collection-transaction\">\"Notice of collection transaction\"</a></p>    

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class CollectionResponseCodeGetExample
    {
        public void main()
        {
            var apiInstance = new ResponseCodeApi();

            try
            {
                // Collection response code
                apiInstance.CollectionResponseCodeGet();
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling ResponseCodeApi.CollectionResponseCodeGet: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
