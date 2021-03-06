# coding: utf-8

"""
    Collection payments

    <img src=\"https://devtest.baokim.vn/collection/core_ctt/image/Picture1.png\" class=\"image-collection-payment\" /> <p><strong>Note:</strong></p> <p>+ In case PARTNER want to use collect via Virtual Account, PARTNER will need to buid:</p> <p style=\"padding-left: 50px;\">     - <a href=\"#operations-Virtual_Account_4\\.0-8442c69ffbaf4b3677a52fa3ebcef6d4\">Register virtual account</a> <br>     - <a href=\"#operations-Virtual_Account_4\\.0-1796c61005edee3976097a607fe9dbaa\">Update virtual account informations</a> <br>     - <a href=\"#operations-tag-Notice_of_collection_transaction\">Notice of collection transaction</a> <br> </p>  # noqa: E501

    OpenAPI spec version: 2.3 and 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ResponseCodeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def collection_response_code_get(self, **kwargs):  # noqa: E501
        """Collection response code  # noqa: E501

        <table>         <thead>         <tr>             <th>ResponseCode</th>             <th>ResponseMessage</th>         </tr>         </thead>         <tbody>         <tr>             <td>200</td>             <td>Successful</td>         </tr>         <tr>             <td>99</td>             <td>Transaction timeout </td>         </tr>         <tr>             <td>11</td>             <td>Failed</td>         </tr>         <tr>             <td>101</td>             <td>Error processing from Baokim</td>         </tr>         <tr>             <td>102</td>             <td>Error from Bank </td>         </tr>         <tr>             <td>103</td>             <td>Operation is incorrect</td>         </tr>         <tr>             <td>104</td>             <td>RequestId or request  is incorrect</td>         </tr>         <tr>             <td>105</td>             <td>PartnerCode is incorrect  </td>         </tr>         <tr>             <td>106</td>             <td>AccName is incorrect</td>         </tr>         <tr>             <td>107</td>             <td>ClientIdNo is incorrect</td>         </tr>         <tr>             <td>108</td>             <td>IssuedDate ho???c IssuedPlace is incorrect</td>         </tr>         <tr>             <td>109</td>             <td>CollectAmount is incorrect</td>         </tr>         <tr>             <td>110</td>             <td>ExpireDate is incorrect</td>         </tr>         <tr>             <td>111</td>             <td>AccNo is incorrect</td>         </tr>         <tr>             <td>112</td>             <td>AccNo is not exist</td>         </tr>         <tr>             <td>113</td>             <td>RefferenceId is incorrect</td>         </tr>         <tr>             <td>114</td>             <td>RefferenceId isn???t exists</td>         </tr>         <tr>             <td>115</td>             <td class=\"bg-color-red\">TransAmount  is incorrect</td>         </tr>         <tr>             <td>116</td>             <td class=\"bg-color-red\">TransTime  is incorrect</td>         </tr>         <tr>             <td>117</td>             <td class=\"bg-color-red\">BefTransDebt  is incorrect</td>         </tr>         <tr>             <td>118</td>             <td class=\"bg-color-red\">TransId is incorrect</td>         </tr>         <tr>             <td>119</td>             <td class=\"bg-color-red\">AffTransDebt is incorrect</td>         </tr>         <tr>             <td>120</td>             <td class=\"bg-color-red\">Signature is incorrect</td>         </tr>         <tr>             <td>121</td>             <td>AccountType is incorrect</td>         </tr>         <tr>             <td>122</td>             <td>OrderId is incorrect</td>         </tr>         <tr>             <td>127</td>             <td>Bank is incorrect</td>         </tr>         <tr>             <td>128</td>             <td>CollectionType is incorrect</td>         </tr>         <tr>             <td>129</td>             <td>Bank not used this CollectionType</td>         </tr>         </tbody>     </table>     <p>* <strong class=\"bg-color-red\">Red codes</strong> represent errors that will arpear when developing the function: <a href=\"#notice-of-collection-transaction\">\"Notice of collection transaction\"</a></p>      # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.collection_response_code_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.collection_response_code_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.collection_response_code_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def collection_response_code_get_with_http_info(self, **kwargs):  # noqa: E501
        """Collection response code  # noqa: E501

        <table>         <thead>         <tr>             <th>ResponseCode</th>             <th>ResponseMessage</th>         </tr>         </thead>         <tbody>         <tr>             <td>200</td>             <td>Successful</td>         </tr>         <tr>             <td>99</td>             <td>Transaction timeout </td>         </tr>         <tr>             <td>11</td>             <td>Failed</td>         </tr>         <tr>             <td>101</td>             <td>Error processing from Baokim</td>         </tr>         <tr>             <td>102</td>             <td>Error from Bank </td>         </tr>         <tr>             <td>103</td>             <td>Operation is incorrect</td>         </tr>         <tr>             <td>104</td>             <td>RequestId or request  is incorrect</td>         </tr>         <tr>             <td>105</td>             <td>PartnerCode is incorrect  </td>         </tr>         <tr>             <td>106</td>             <td>AccName is incorrect</td>         </tr>         <tr>             <td>107</td>             <td>ClientIdNo is incorrect</td>         </tr>         <tr>             <td>108</td>             <td>IssuedDate ho???c IssuedPlace is incorrect</td>         </tr>         <tr>             <td>109</td>             <td>CollectAmount is incorrect</td>         </tr>         <tr>             <td>110</td>             <td>ExpireDate is incorrect</td>         </tr>         <tr>             <td>111</td>             <td>AccNo is incorrect</td>         </tr>         <tr>             <td>112</td>             <td>AccNo is not exist</td>         </tr>         <tr>             <td>113</td>             <td>RefferenceId is incorrect</td>         </tr>         <tr>             <td>114</td>             <td>RefferenceId isn???t exists</td>         </tr>         <tr>             <td>115</td>             <td class=\"bg-color-red\">TransAmount  is incorrect</td>         </tr>         <tr>             <td>116</td>             <td class=\"bg-color-red\">TransTime  is incorrect</td>         </tr>         <tr>             <td>117</td>             <td class=\"bg-color-red\">BefTransDebt  is incorrect</td>         </tr>         <tr>             <td>118</td>             <td class=\"bg-color-red\">TransId is incorrect</td>         </tr>         <tr>             <td>119</td>             <td class=\"bg-color-red\">AffTransDebt is incorrect</td>         </tr>         <tr>             <td>120</td>             <td class=\"bg-color-red\">Signature is incorrect</td>         </tr>         <tr>             <td>121</td>             <td>AccountType is incorrect</td>         </tr>         <tr>             <td>122</td>             <td>OrderId is incorrect</td>         </tr>         <tr>             <td>127</td>             <td>Bank is incorrect</td>         </tr>         <tr>             <td>128</td>             <td>CollectionType is incorrect</td>         </tr>         <tr>             <td>129</td>             <td>Bank not used this CollectionType</td>         </tr>         </tbody>     </table>     <p>* <strong class=\"bg-color-red\">Red codes</strong> represent errors that will arpear when developing the function: <a href=\"#notice-of-collection-transaction\">\"Notice of collection transaction\"</a></p>      # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.collection_response_code_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method collection_response_code_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            'Collection response code', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
