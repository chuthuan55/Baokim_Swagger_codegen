# coding: utf-8

"""
     Disbursement payments API

    <h2>Introduction</h2> Welcome! Baokim’s mission is to deliver automated payment infrastructure solutions for your business. We help with both money in (collection payments) and money out (disbursement payments). Our users range from platforms businesses, fintech, e-Commerce, and everything else in between.  <p><strong>Benefits of Baokim</strong></p> Fast integration  Instant transfers  Daily reconciliation  Simple & competitive pricing – no hidden fees  <h2>Regulations and requirements</h2>   - API that Baokim deployed, will be built on the Restful architecture, data transmission between the two sides will be Json.  - Baokim will restrict access to the API by one or more IPs based on each Partner. So before joining , Partner will send the IP list to Baokim to open the access.  - Baokim uses Basic Authentication to allow access to the API. Account information will be provided by Bao Kim at the start of the integration.  <code>Authorization: Basic YmFva2ltOmJrQDEyMzQ1Ng==</code>  <h2>Restful and Digital Signature</h2> <p><strong>Restfull Web Service</strong></p> REST (Representational State Transfer) has been widely adopted instead of Web services based on SOAP and WSDL. REST defines architectural rules for designing Web services that focus on system resources, including how resource states are formatted and transported via HTTP through a large number of users and are written by different languages.  In order to be able to connect REST with the tool and test with BAOKIM, the PARTNER can load and use one of the following two universal tools:  - Postman: https://www.getpostman.com  - Soap UI: https://www.soapui.org  <p><strong>Digital signature</strong></p>  <img src=\"https://thuchiho.baokim.vn/assets/docs/img/sign_model.jpg\" alt=\"Model Sign\">   <p><strong>Private key and public key</strong></p> Baokim is currently using digital signature by RSA-SHA1  There are several ways to generate RSA key pairs.  <strong>Way 1</strong>:  Generate your RSA key pairs online: Generate now  <strong>Way 2</strong>:  Using OpenSSL software for Windows:  <strong>Step 1</strong>: Download the software at:  http://slproweb.com/products/Win32OpenSSL.html. Partner should download the installer \"OpenSSL_Light-1_0_2k\". Then install in any directory, for example \"C:\\OpenSSLWin64\"  <strong>Step 2</strong>: Access \"C:\\OpenSSLWin64\\bin\" then open the command prompt. Type the command to declare the environment config.  set OPENSSL_CONF=C:\\OpenSSL-Win64\\bin\\openssl.cfg  <strong>Step 3</strong>: Generate private key and public key  openssl genrsa -aes256 -out c:\\opensslkeys\\partner\\partner_privatekey.pem 2048  openssl rsa –in c:\\opensslkeys\\partner\\partner_privatekey.pem -pubout >c:\\opensslkeys\\partner\\partner_publickey.pem  After successful pairing, Partner will send back to Baokim the public key to authenticate the signature that the Partner sends via the API.  <h3>Describe the mechanism handling the transaction timeout</h3> Due to traffic problems or during request processing at Baokim, transaction timeout may be generated. Baokim will describe the processing mechanism consists of two cases as follows:  <strong>Case 1</strong>: Baokim proactively returns error code timeout, error code <b>99</b>  - This case occurs when the two parties set the maximum time to return the results for a transaction but for some reason the Baokim or Bank has not finished processing should be proactive return error code timeout  - The way to deal with this situation: Partner when receiving the timeout error code will call the check transaction status. In this function Baokim will return the transaction status for Partner.  <strong>Case 2</strong>: Timeout due to transmission line failure, does not get the result returned  In this case it is possible to timeout from Partner-> Baokim or Baokim-> Partner. So can not determine whether the transaction Baokim reception or not.  - The way to deal with this situation:  1. The Partner will call Check Transaction Status to look up transaction status. If the result is received then the Partner will update the partner status. If timeout is still the case then move on to step 2.  2. In cases where transmission lines meet with long incidents, Baokim and Partner will coordinate with human handling to certification. Partner will email to Baokim to request sending status for a transaction, the Baokim's technique will confirm the status and return to Partner.   <h2>List of bank transfer assistance. </h2>  <table>                     <thead>                         <tr> <th>#</th> <th>BankNo</th> <th>BankName</th> <th>Account</th> <th>Card</th>                         </tr>                     </thead>                     <tbody>                         <tr> <td>1</td> <td>970423</td> <td>TIEN PHONG COMMERCIAL JOINT STOCK BANK</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>2</td> <td>970437</td> <td>Ho Chi Minh City Development Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>3</td> <td>970408</td> <td>Global Petro Sole Member LimitedCommercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>4</td> <td>970407</td> <td>Vietnam Technological and Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>5</td> <td>970442</td> <td>Hong Leong Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>6</td> <td>970414</td> <td>Ocean Commercial Joint - Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>7</td> <td>970438</td> <td>Bao Viet Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>8</td> <td>970422</td> <td>Military Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>9</td> <td>970432</td> <td>Vietnam Prosperity Joint-Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>10</td> <td>970439</td> <td>Public Bank Vietnam Limited (PBVN)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>11</td> <td>970415</td> <td>VIETNAM JOINT STOCK COMMERCIAL BANK FOR INDUSTRY AND TRADE (Viettinbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>12</td> <td>970431</td> <td>VIETNAM EXPORT IMPORT COMMERCIAL JOINT STOCK BANK (Eximbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>13</td> <td>970440</td> <td>Southeast Asia Commercial Joint Stock Bank (SeABank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>14</td> <td>970429</td> <td>Sai Gon Joint StockCommercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>15</td> <td>970448</td> <td>Orient Commercial Joint StockBank (OCB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>16</td> <td>970425</td> <td>An BinhCommercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>17</td> <td>970426</td> <td>Vietnam Maritime Commercial Stock Bank (MSB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>18</td> <td>970427</td> <td>Vietnam Asia Commercial Joint Stock Bank (VietA)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>19</td> <td>970419</td> <td>National Citizen Commercial Joint Stock Bank (NCB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>20</td> <td>970418</td> <td>Joint Stock Commercial Bank for Investment and Development of Vietnam (BIDV)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>21</td> <td>970443</td> <td>Sai Gon- Ha Noi Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>22</td> <td>970406</td> <td>DongA Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>23</td> <td>970441</td> <td>Vietnam International Commercial Joint Stock Bank (VIB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>24</td> <td>970424</td> <td>Shinhan Bank Vietnam Limited</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>25</td> <td>970433</td> <td>Vietnam Thuong Tin Commercial Joint Stock Bank (Vietbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>26</td> <td>970454</td> <td>VIET CAPITAL COMMERCIAL JOINT STOCK BANK (Ban Viet)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>27</td> <td>970452</td> <td>Kien Long Commercial Joint -Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>28</td> <td>970430</td> <td>PETROLIMEX GROUPCOMMERCIAL JOINT STOCK BANK</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>29</td> <td>970400</td> <td>Sai Gon Joint Stock Commercial Bank (Saigon Bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>30</td> <td>970405</td> <td>Vietnam Bank for Agriculture and Rural Development or Agribank (Agribank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>31</td> <td>970403</td> <td>Sacombank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>32</td> <td>970412</td> <td>Vietnam Public Joint Stock Commercial Bank (Vietnam dai chung)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>33</td> <td>970421</td> <td>Vietnam-Russia Joint Venture Bank - VRB</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>34</td> <td>970428</td> <td>Nam A Commercial Joint Stock Bank (Nam A Bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>35</td> <td>970434</td> <td>Indovina Bank Ltd</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>36</td> <td>970449</td> <td>LienViet Post Joint Stock Commercial Bank (LienViet Post bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>37</td> <td>970457</td> <td>Woori Bank Vietnam Limited</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>38</td> <td>970436</td> <td>Joint Stock Commercial Bank for Foreign Trade of Vietnam (Vietcombank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>39</td> <td>970416</td> <td>Asia Commercial Joint Stock Bank</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>40</td> <td>970458</td> <td>UNITED OVERSEAS BANK (VIETNAM) LIMITED</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>41</td> <td>970446</td> <td>Co-operative bank of VietNam</td> <td></td> <td>✓</td>                         </tr>                         <tr> <td>42</td> <td>970455</td> <td>Industrial Bank of Korea - Ha Noi Branch</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>43</td> <td>970409</td> <td>North Asia Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>44</td> <td>422589</td> <td>CIMB Bank (Vietnam) Limited</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>45</td> <td>796500</td> <td>Ngân hàng DBS - Chi nhánh Hồ Chí Minh(DBS)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>46</td> <td>458761</td> <td>TNHH MTV HSBC Việt Nam(HSBC)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>47</td> <td>970410</td> <td>TNHH MTV Standard Chartered Việt Nam(SCVN)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>48</td> <td>801011</td> <td>Nonghuyp - Chi nhánh Hà Nội(NHB)</td> <td>✓</td> <td></td>                         </tr>  <td>49</td> <td>970444</td> <td>TM TNHH MTV Xây Dựng Việt Nam </td> <td>✓</td> <td></td>                         </tr><tr> <td>50</td> <td>970456</td> <td> IBK - chi nhánh HCM</td> <td>✓</td> <td></td>                         </tr><tr> <td>51</td> <td>970462</td> <td>Kookmin - Chi nhánh Hà Nội</td> <td>✓</td> <td>✓</td>                         </tr><tr> <td>52</td> <td>970463</td> <td>Kookmin - Chi nhánh Thành phố Hồ Chí Minh</td> <td>✓</td> <td>✓</td>                         </tr><tr> <td>53</td> <td>546034</td> <td>Ngân hàng số CAKE by VPBank</td> <td>✓</td> <td></td>                         </tr><tr> <td>54</td> <td>546035</td> <td>Ngân hàng số Ubank by VPBank</td> <td>✓</td> <td></td>                   </tbody>                 </table>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import copy
import logging
import multiprocessing
import sys
import urllib3

import six
from six.moves import http_client as httplib


class TypeWithDefault(type):
    def __init__(cls, name, bases, dct):
        super(TypeWithDefault, cls).__init__(name, bases, dct)
        cls._default = None

    def __call__(cls):
        if cls._default is None:
            cls._default = type.__call__(cls)
        return copy.copy(cls._default)

    def set_default(cls, default):
        cls._default = copy.copy(default)


class Configuration(six.with_metaclass(TypeWithDefault, object)):
    """NOTE: This class is auto generated by the swagger code generator program.

    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.
    """

    def __init__(self):
        """Constructor"""
        # Default Base url
        self.host = "https://https://devtest.baokim.vn"
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # dict to store API key(s)
        self.api_key = {}
        # dict to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}
        # function to refresh API key if expired
        self.refresh_api_key_hook = None
        # Username for HTTP basic authentication
        self.username = ""
        # Password for HTTP basic authentication
        self.password = ""
        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("swagger_client")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API
        # from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        self.assert_hostname = None

        # urllib3 connection pool's maximum number of connections saved
        # per pool. urllib3 uses 1 connection as default value, but this is
        # not the best value when you are making a lot of possibly parallel
        # requests to the same host, which is often the case here.
        # cpu_count * 5 is used as default value to increase performance.
        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5

        # Proxy URL
        self.proxy = None
        # Safe chars for path_param
        self.safe_chars_for_path_param = ''

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.refresh_api_key_hook:
            self.refresh_api_key_hook(self)

        key = self.api_key.get(identifier)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        return urllib3.util.make_headers(
            basic_auth=self.username + ':' + self.password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        return {
        }

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 1.0.0\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)
