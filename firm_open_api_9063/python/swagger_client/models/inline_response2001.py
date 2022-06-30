# coding: utf-8

"""
     Disbursement payments API

    <h2>Introduction</h2> Welcome! Baokim’s mission is to deliver automated payment infrastructure solutions for your business. We help with both money in (collection payments) and money out (disbursement payments). Our users range from platforms businesses, fintech, e-Commerce, and everything else in between.  <p><strong>Benefits of Baokim</strong></p> Fast integration  Instant transfers  Daily reconciliation  Simple & competitive pricing – no hidden fees  <h2>Regulations and requirements</h2>   - API that Baokim deployed, will be built on the Restful architecture, data transmission between the two sides will be Json.  - Baokim will restrict access to the API by one or more IPs based on each Partner. So before joining , Partner will send the IP list to Baokim to open the access.  - Baokim uses Basic Authentication to allow access to the API. Account information will be provided by Bao Kim at the start of the integration.  <code>Authorization: Basic YmFva2ltOmJrQDEyMzQ1Ng==</code>  <h2>Restful and Digital Signature</h2> <p><strong>Restfull Web Service</strong></p> REST (Representational State Transfer) has been widely adopted instead of Web services based on SOAP and WSDL. REST defines architectural rules for designing Web services that focus on system resources, including how resource states are formatted and transported via HTTP through a large number of users and are written by different languages.  In order to be able to connect REST with the tool and test with BAOKIM, the PARTNER can load and use one of the following two universal tools:  - Postman: https://www.getpostman.com  - Soap UI: https://www.soapui.org  <p><strong>Digital signature</strong></p>  <img src=\"https://thuchiho.baokim.vn/assets/docs/img/sign_model.jpg\" alt=\"Model Sign\">   <p><strong>Private key and public key</strong></p> Baokim is currently using digital signature by RSA-SHA1  There are several ways to generate RSA key pairs.  <strong>Way 1</strong>:  Generate your RSA key pairs online: Generate now  <strong>Way 2</strong>:  Using OpenSSL software for Windows:  <strong>Step 1</strong>: Download the software at:  http://slproweb.com/products/Win32OpenSSL.html. Partner should download the installer \"OpenSSL_Light-1_0_2k\". Then install in any directory, for example \"C:\\OpenSSLWin64\"  <strong>Step 2</strong>: Access \"C:\\OpenSSLWin64\\bin\" then open the command prompt. Type the command to declare the environment config.  set OPENSSL_CONF=C:\\OpenSSL-Win64\\bin\\openssl.cfg  <strong>Step 3</strong>: Generate private key and public key  openssl genrsa -aes256 -out c:\\opensslkeys\\partner\\partner_privatekey.pem 2048  openssl rsa –in c:\\opensslkeys\\partner\\partner_privatekey.pem -pubout >c:\\opensslkeys\\partner\\partner_publickey.pem  After successful pairing, Partner will send back to Baokim the public key to authenticate the signature that the Partner sends via the API.  <h3>Describe the mechanism handling the transaction timeout</h3> Due to traffic problems or during request processing at Baokim, transaction timeout may be generated. Baokim will describe the processing mechanism consists of two cases as follows:  <strong>Case 1</strong>: Baokim proactively returns error code timeout, error code <b>99</b>  - This case occurs when the two parties set the maximum time to return the results for a transaction but for some reason the Baokim or Bank has not finished processing should be proactive return error code timeout  - The way to deal with this situation: Partner when receiving the timeout error code will call the check transaction status. In this function Baokim will return the transaction status for Partner.  <strong>Case 2</strong>: Timeout due to transmission line failure, does not get the result returned  In this case it is possible to timeout from Partner-> Baokim or Baokim-> Partner. So can not determine whether the transaction Baokim reception or not.  - The way to deal with this situation:  1. The Partner will call Check Transaction Status to look up transaction status. If the result is received then the Partner will update the partner status. If timeout is still the case then move on to step 2.  2. In cases where transmission lines meet with long incidents, Baokim and Partner will coordinate with human handling to certification. Partner will email to Baokim to request sending status for a transaction, the Baokim's technique will confirm the status and return to Partner.   <h2>List of bank transfer assistance. </h2>  <table>                     <thead>                         <tr> <th>#</th> <th>BankNo</th> <th>BankName</th> <th>Account</th> <th>Card</th>                         </tr>                     </thead>                     <tbody>                         <tr> <td>1</td> <td>970423</td> <td>TIEN PHONG COMMERCIAL JOINT STOCK BANK</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>2</td> <td>970437</td> <td>Ho Chi Minh City Development Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>3</td> <td>970408</td> <td>Global Petro Sole Member LimitedCommercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>4</td> <td>970407</td> <td>Vietnam Technological and Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>5</td> <td>970442</td> <td>Hong Leong Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>6</td> <td>970414</td> <td>Ocean Commercial Joint - Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>7</td> <td>970438</td> <td>Bao Viet Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>8</td> <td>970422</td> <td>Military Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>9</td> <td>970432</td> <td>Vietnam Prosperity Joint-Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>10</td> <td>970439</td> <td>Public Bank Vietnam Limited (PBVN)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>11</td> <td>970415</td> <td>VIETNAM JOINT STOCK COMMERCIAL BANK FOR INDUSTRY AND TRADE (Viettinbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>12</td> <td>970431</td> <td>VIETNAM EXPORT IMPORT COMMERCIAL JOINT STOCK BANK (Eximbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>13</td> <td>970440</td> <td>Southeast Asia Commercial Joint Stock Bank (SeABank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>14</td> <td>970429</td> <td>Sai Gon Joint StockCommercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>15</td> <td>970448</td> <td>Orient Commercial Joint StockBank (OCB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>16</td> <td>970425</td> <td>An BinhCommercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>17</td> <td>970426</td> <td>Vietnam Maritime Commercial Stock Bank (MSB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>18</td> <td>970427</td> <td>Vietnam Asia Commercial Joint Stock Bank (VietA)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>19</td> <td>970419</td> <td>National Citizen Commercial Joint Stock Bank (NCB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>20</td> <td>970418</td> <td>Joint Stock Commercial Bank for Investment and Development of Vietnam (BIDV)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>21</td> <td>970443</td> <td>Sai Gon- Ha Noi Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>22</td> <td>970406</td> <td>DongA Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>23</td> <td>970441</td> <td>Vietnam International Commercial Joint Stock Bank (VIB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>24</td> <td>970424</td> <td>Shinhan Bank Vietnam Limited</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>25</td> <td>970433</td> <td>Vietnam Thuong Tin Commercial Joint Stock Bank (Vietbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>26</td> <td>970454</td> <td>VIET CAPITAL COMMERCIAL JOINT STOCK BANK (Ban Viet)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>27</td> <td>970452</td> <td>Kien Long Commercial Joint -Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>28</td> <td>970430</td> <td>PETROLIMEX GROUPCOMMERCIAL JOINT STOCK BANK</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>29</td> <td>970400</td> <td>Sai Gon Joint Stock Commercial Bank (Saigon Bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>30</td> <td>970405</td> <td>Vietnam Bank for Agriculture and Rural Development or Agribank (Agribank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>31</td> <td>970403</td> <td>Sacombank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>32</td> <td>970412</td> <td>Vietnam Public Joint Stock Commercial Bank (Vietnam dai chung)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>33</td> <td>970421</td> <td>Vietnam-Russia Joint Venture Bank - VRB</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>34</td> <td>970428</td> <td>Nam A Commercial Joint Stock Bank (Nam A Bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>35</td> <td>970434</td> <td>Indovina Bank Ltd</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>36</td> <td>970449</td> <td>LienViet Post Joint Stock Commercial Bank (LienViet Post bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>37</td> <td>970457</td> <td>Woori Bank Vietnam Limited</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>38</td> <td>970436</td> <td>Joint Stock Commercial Bank for Foreign Trade of Vietnam (Vietcombank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>39</td> <td>970416</td> <td>Asia Commercial Joint Stock Bank</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>40</td> <td>970458</td> <td>UNITED OVERSEAS BANK (VIETNAM) LIMITED</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>41</td> <td>970446</td> <td>Co-operative bank of VietNam</td> <td></td> <td>✓</td>                         </tr>                         <tr> <td>42</td> <td>970455</td> <td>Industrial Bank of Korea - Ha Noi Branch</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>43</td> <td>970409</td> <td>North Asia Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>44</td> <td>422589</td> <td>CIMB Bank (Vietnam) Limited</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>45</td> <td>796500</td> <td>Ngân hàng DBS - Chi nhánh Hồ Chí Minh(DBS)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>46</td> <td>458761</td> <td>TNHH MTV HSBC Việt Nam(HSBC)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>47</td> <td>970410</td> <td>TNHH MTV Standard Chartered Việt Nam(SCVN)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>48</td> <td>801011</td> <td>Nonghuyp - Chi nhánh Hà Nội(NHB)</td> <td>✓</td> <td></td>                         </tr>  <td>49</td> <td>970444</td> <td>TM TNHH MTV Xây Dựng Việt Nam </td> <td>✓</td> <td></td>                         </tr><tr> <td>50</td> <td>970456</td> <td> IBK - chi nhánh HCM</td> <td>✓</td> <td></td>                         </tr><tr> <td>51</td> <td>970462</td> <td>Kookmin - Chi nhánh Hà Nội</td> <td>✓</td> <td>✓</td>                         </tr><tr> <td>52</td> <td>970463</td> <td>Kookmin - Chi nhánh Thành phố Hồ Chí Minh</td> <td>✓</td> <td>✓</td>                         </tr><tr> <td>53</td> <td>546034</td> <td>Ngân hàng số CAKE by VPBank</td> <td>✓</td> <td></td>                         </tr><tr> <td>54</td> <td>546035</td> <td>Ngân hàng số Ubank by VPBank</td> <td>✓</td> <td></td>                   </tbody>                 </table>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2001(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'response_code': 'int',
        'response_message': 'str',
        'reference_id': 'str',
        'transaction_id': 'str',
        'transaction_time': 'str',
        'bank_no': 'str',
        'acc_no': 'str',
        'acc_name': 'str',
        'acc_type': 'str',
        'request_amount': 'int',
        'transfer_amount': 'int',
        'affter_balance': 'int',
        'after_disbursement_day': 'int',
        'signature': 'str'
    }

    attribute_map = {
        'response_code': 'ResponseCode',
        'response_message': 'ResponseMessage',
        'reference_id': 'ReferenceId',
        'transaction_id': 'TransactionId',
        'transaction_time': 'TransactionTime',
        'bank_no': 'BankNo',
        'acc_no': 'AccNo',
        'acc_name': 'AccName',
        'acc_type': 'AccType',
        'request_amount': 'RequestAmount',
        'transfer_amount': 'TransferAmount',
        'affter_balance': 'AffterBalance',
        'after_disbursement_day': 'AfterDisbursementDay',
        'signature': 'Signature'
    }

    def __init__(self, response_code=None, response_message=None, reference_id=None, transaction_id=None, transaction_time=None, bank_no=None, acc_no=None, acc_name=None, acc_type=None, request_amount=None, transfer_amount=None, affter_balance=None, after_disbursement_day=None, signature=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501
        self._response_code = None
        self._response_message = None
        self._reference_id = None
        self._transaction_id = None
        self._transaction_time = None
        self._bank_no = None
        self._acc_no = None
        self._acc_name = None
        self._acc_type = None
        self._request_amount = None
        self._transfer_amount = None
        self._affter_balance = None
        self._after_disbursement_day = None
        self._signature = None
        self.discriminator = None
        if response_code is not None:
            self.response_code = response_code
        if response_message is not None:
            self.response_message = response_message
        if reference_id is not None:
            self.reference_id = reference_id
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if transaction_time is not None:
            self.transaction_time = transaction_time
        if bank_no is not None:
            self.bank_no = bank_no
        if acc_no is not None:
            self.acc_no = acc_no
        if acc_name is not None:
            self.acc_name = acc_name
        if acc_type is not None:
            self.acc_type = acc_type
        if request_amount is not None:
            self.request_amount = request_amount
        if transfer_amount is not None:
            self.transfer_amount = transfer_amount
        if affter_balance is not None:
            self.affter_balance = affter_balance
        if after_disbursement_day is not None:
            self.after_disbursement_day = after_disbursement_day
        if signature is not None:
            self.signature = signature

    @property
    def response_code(self):
        """Gets the response_code of this InlineResponse2001.  # noqa: E501

        200 : Successful. <br> 99 : Transaction timeout.<br> 11 : Failed.<br> 101 : Error processing from Baokim.<br> 102 : Duplicated RequestId.<br> 103 : Incorrect signature.<br> 110 : Incorrect PartnerCode.<br> 111 : PartnerCode deleted from the system.<br> 112 : PartnerCode not yet activated.<br> 113 : Operation code is required.<br> 114 : Incorrect Operation code.<br> 115 : BankID is required.<br> 116 : BankID not supported.<br> 117 : Account no. /Card no. should be from 6-22 characters in length.<br> 118 : Invalid account no./Card no..<br> 119 : Account no./Card no. does not exist.<br> 120 : Incorrect account type.<br> 121 : Transaction ID sent from Partner is required.<br> 122 : Transaction ID sent by Partner is existing.<br> 123 : Transaction unfound.<br> 124 : Transfer amount required.<br> 125 : Invalid transfer amount.<br> 126 : Error processing between Baokim and bank.<br> 127 : Error connecting to bank.<br> 128 : Error processing from bank.<br> 129 : Insufficient disbursement limit or expired guarantee period.<br> 130 : Exceeded transfer limit on day.<br>  # noqa: E501

        :return: The response_code of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this InlineResponse2001.

        200 : Successful. <br> 99 : Transaction timeout.<br> 11 : Failed.<br> 101 : Error processing from Baokim.<br> 102 : Duplicated RequestId.<br> 103 : Incorrect signature.<br> 110 : Incorrect PartnerCode.<br> 111 : PartnerCode deleted from the system.<br> 112 : PartnerCode not yet activated.<br> 113 : Operation code is required.<br> 114 : Incorrect Operation code.<br> 115 : BankID is required.<br> 116 : BankID not supported.<br> 117 : Account no. /Card no. should be from 6-22 characters in length.<br> 118 : Invalid account no./Card no..<br> 119 : Account no./Card no. does not exist.<br> 120 : Incorrect account type.<br> 121 : Transaction ID sent from Partner is required.<br> 122 : Transaction ID sent by Partner is existing.<br> 123 : Transaction unfound.<br> 124 : Transfer amount required.<br> 125 : Invalid transfer amount.<br> 126 : Error processing between Baokim and bank.<br> 127 : Error connecting to bank.<br> 128 : Error processing from bank.<br> 129 : Insufficient disbursement limit or expired guarantee period.<br> 130 : Exceeded transfer limit on day.<br>  # noqa: E501

        :param response_code: The response_code of this InlineResponse2001.  # noqa: E501
        :type: int
        """

        self._response_code = response_code

    @property
    def response_message(self):
        """Gets the response_message of this InlineResponse2001.  # noqa: E501

        Description for return status  # noqa: E501

        :return: The response_message of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._response_message

    @response_message.setter
    def response_message(self, response_message):
        """Sets the response_message of this InlineResponse2001.

        Description for return status  # noqa: E501

        :param response_message: The response_message of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._response_message = response_message

    @property
    def reference_id(self):
        """Gets the reference_id of this InlineResponse2001.  # noqa: E501

        Partner information posted  # noqa: E501

        :return: The reference_id of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this InlineResponse2001.

        Partner information posted  # noqa: E501

        :param reference_id: The reference_id of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def transaction_id(self):
        """Gets the transaction_id of this InlineResponse2001.  # noqa: E501

        Transaction code recorded side Baokim  # noqa: E501

        :return: The transaction_id of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this InlineResponse2001.

        Transaction code recorded side Baokim  # noqa: E501

        :param transaction_id: The transaction_id of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def transaction_time(self):
        """Gets the transaction_time of this InlineResponse2001.  # noqa: E501

        Finishing time side Baokim. Format YYYY-MM-DD  # noqa: E501

        :return: The transaction_time of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """Sets the transaction_time of this InlineResponse2001.

        Finishing time side Baokim. Format YYYY-MM-DD  # noqa: E501

        :param transaction_time: The transaction_time of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._transaction_time = transaction_time

    @property
    def bank_no(self):
        """Gets the bank_no of this InlineResponse2001.  # noqa: E501

        Partner information posted  # noqa: E501

        :return: The bank_no of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._bank_no

    @bank_no.setter
    def bank_no(self, bank_no):
        """Sets the bank_no of this InlineResponse2001.

        Partner information posted  # noqa: E501

        :param bank_no: The bank_no of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._bank_no = bank_no

    @property
    def acc_no(self):
        """Gets the acc_no of this InlineResponse2001.  # noqa: E501

        Partner information posted  # noqa: E501

        :return: The acc_no of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._acc_no

    @acc_no.setter
    def acc_no(self, acc_no):
        """Sets the acc_no of this InlineResponse2001.

        Partner information posted  # noqa: E501

        :param acc_no: The acc_no of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._acc_no = acc_no

    @property
    def acc_name(self):
        """Gets the acc_name of this InlineResponse2001.  # noqa: E501

        Full name of the recipient, may or may not, depending on the time  # noqa: E501

        :return: The acc_name of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._acc_name

    @acc_name.setter
    def acc_name(self, acc_name):
        """Sets the acc_name of this InlineResponse2001.

        Full name of the recipient, may or may not, depending on the time  # noqa: E501

        :param acc_name: The acc_name of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._acc_name = acc_name

    @property
    def acc_type(self):
        """Gets the acc_type of this InlineResponse2001.  # noqa: E501

        Partner information posted  # noqa: E501

        :return: The acc_type of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._acc_type

    @acc_type.setter
    def acc_type(self, acc_type):
        """Sets the acc_type of this InlineResponse2001.

        Partner information posted  # noqa: E501

        :param acc_type: The acc_type of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._acc_type = acc_type

    @property
    def request_amount(self):
        """Gets the request_amount of this InlineResponse2001.  # noqa: E501

        Partner information posted  # noqa: E501

        :return: The request_amount of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._request_amount

    @request_amount.setter
    def request_amount(self, request_amount):
        """Sets the request_amount of this InlineResponse2001.

        Partner information posted  # noqa: E501

        :param request_amount: The request_amount of this InlineResponse2001.  # noqa: E501
        :type: int
        """

        self._request_amount = request_amount

    @property
    def transfer_amount(self):
        """Gets the transfer_amount of this InlineResponse2001.  # noqa: E501

        The actual amount transferred to the recipient. Will be less if the remittance  # noqa: E501

        :return: The transfer_amount of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._transfer_amount

    @transfer_amount.setter
    def transfer_amount(self, transfer_amount):
        """Sets the transfer_amount of this InlineResponse2001.

        The actual amount transferred to the recipient. Will be less if the remittance  # noqa: E501

        :param transfer_amount: The transfer_amount of this InlineResponse2001.  # noqa: E501
        :type: int
        """

        self._transfer_amount = transfer_amount

    @property
    def affter_balance(self):
        """Gets the affter_balance of this InlineResponse2001.  # noqa: E501

        Current balance of investors  # noqa: E501

        :return: The affter_balance of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._affter_balance

    @affter_balance.setter
    def affter_balance(self, affter_balance):
        """Sets the affter_balance of this InlineResponse2001.

        Current balance of investors  # noqa: E501

        :param affter_balance: The affter_balance of this InlineResponse2001.  # noqa: E501
        :type: int
        """

        self._affter_balance = affter_balance

    @property
    def after_disbursement_day(self):
        """Gets the after_disbursement_day of this InlineResponse2001.  # noqa: E501

        Continue disbursement amount (in limit)  # noqa: E501

        :return: The after_disbursement_day of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._after_disbursement_day

    @after_disbursement_day.setter
    def after_disbursement_day(self, after_disbursement_day):
        """Sets the after_disbursement_day of this InlineResponse2001.

        Continue disbursement amount (in limit)  # noqa: E501

        :param after_disbursement_day: The after_disbursement_day of this InlineResponse2001.  # noqa: E501
        :type: int
        """

        self._after_disbursement_day = after_disbursement_day

    @property
    def signature(self):
        """Gets the signature of this InlineResponse2001.  # noqa: E501

        BAOKIM will sign by digital signature of response data. Structured data: ResponseCode|ResponseMessage| RequestId | PartnerCode | Available | Holding  # noqa: E501

        :return: The signature of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this InlineResponse2001.

        BAOKIM will sign by digital signature of response data. Structured data: ResponseCode|ResponseMessage| RequestId | PartnerCode | Available | Holding  # noqa: E501

        :param signature: The signature of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._signature = signature

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse2001, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
