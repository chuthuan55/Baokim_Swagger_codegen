# coding: utf-8

"""
     Disbursement payments API

    <h2>Introduction</h2> Welcome! Baokim’s mission is to deliver automated payment infrastructure solutions for your business. We help with both money in (collection payments) and money out (disbursement payments). Our users range from platforms businesses, fintech, e-Commerce, and everything else in between.  <p><strong>Benefits of Baokim</strong></p> Fast integration  Instant transfers  Daily reconciliation  Simple & competitive pricing – no hidden fees  <h2>Regulations and requirements</h2>   - API that Baokim deployed, will be built on the Restful architecture, data transmission between the two sides will be Json.  - Baokim will restrict access to the API by one or more IPs based on each Partner. So before joining , Partner will send the IP list to Baokim to open the access.  - Baokim uses Basic Authentication to allow access to the API. Account information will be provided by Bao Kim at the start of the integration.  <code>Authorization: Basic YmFva2ltOmJrQDEyMzQ1Ng==</code>  <h2>Restful and Digital Signature</h2> <p><strong>Restfull Web Service</strong></p> REST (Representational State Transfer) has been widely adopted instead of Web services based on SOAP and WSDL. REST defines architectural rules for designing Web services that focus on system resources, including how resource states are formatted and transported via HTTP through a large number of users and are written by different languages.  In order to be able to connect REST with the tool and test with BAOKIM, the PARTNER can load and use one of the following two universal tools:  - Postman: https://www.getpostman.com  - Soap UI: https://www.soapui.org  <p><strong>Digital signature</strong></p>  <img src=\"https://thuchiho.baokim.vn/assets/docs/img/sign_model.jpg\" alt=\"Model Sign\">   <p><strong>Private key and public key</strong></p> Baokim is currently using digital signature by RSA-SHA1  There are several ways to generate RSA key pairs.  <strong>Way 1</strong>:  Generate your RSA key pairs online: Generate now  <strong>Way 2</strong>:  Using OpenSSL software for Windows:  <strong>Step 1</strong>: Download the software at:  http://slproweb.com/products/Win32OpenSSL.html. Partner should download the installer \"OpenSSL_Light-1_0_2k\". Then install in any directory, for example \"C:\\OpenSSLWin64\"  <strong>Step 2</strong>: Access \"C:\\OpenSSLWin64\\bin\" then open the command prompt. Type the command to declare the environment config.  set OPENSSL_CONF=C:\\OpenSSL-Win64\\bin\\openssl.cfg  <strong>Step 3</strong>: Generate private key and public key  openssl genrsa -aes256 -out c:\\opensslkeys\\partner\\partner_privatekey.pem 2048  openssl rsa –in c:\\opensslkeys\\partner\\partner_privatekey.pem -pubout >c:\\opensslkeys\\partner\\partner_publickey.pem  After successful pairing, Partner will send back to Baokim the public key to authenticate the signature that the Partner sends via the API.  <h3>Describe the mechanism handling the transaction timeout</h3> Due to traffic problems or during request processing at Baokim, transaction timeout may be generated. Baokim will describe the processing mechanism consists of two cases as follows:  <strong>Case 1</strong>: Baokim proactively returns error code timeout, error code <b>99</b>  - This case occurs when the two parties set the maximum time to return the results for a transaction but for some reason the Baokim or Bank has not finished processing should be proactive return error code timeout  - The way to deal with this situation: Partner when receiving the timeout error code will call the check transaction status. In this function Baokim will return the transaction status for Partner.  <strong>Case 2</strong>: Timeout due to transmission line failure, does not get the result returned  In this case it is possible to timeout from Partner-> Baokim or Baokim-> Partner. So can not determine whether the transaction Baokim reception or not.  - The way to deal with this situation:  1. The Partner will call Check Transaction Status to look up transaction status. If the result is received then the Partner will update the partner status. If timeout is still the case then move on to step 2.  2. In cases where transmission lines meet with long incidents, Baokim and Partner will coordinate with human handling to certification. Partner will email to Baokim to request sending status for a transaction, the Baokim's technique will confirm the status and return to Partner.   <h2>List of bank transfer assistance. </h2>  <table>                     <thead>                         <tr> <th>#</th> <th>BankNo</th> <th>BankName</th> <th>Account</th> <th>Card</th>                         </tr>                     </thead>                     <tbody>                         <tr> <td>1</td> <td>970423</td> <td>TIEN PHONG COMMERCIAL JOINT STOCK BANK</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>2</td> <td>970437</td> <td>Ho Chi Minh City Development Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>3</td> <td>970408</td> <td>Global Petro Sole Member LimitedCommercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>4</td> <td>970407</td> <td>Vietnam Technological and Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>5</td> <td>970442</td> <td>Hong Leong Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>6</td> <td>970414</td> <td>Ocean Commercial Joint - Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>7</td> <td>970438</td> <td>Bao Viet Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>8</td> <td>970422</td> <td>Military Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>9</td> <td>970432</td> <td>Vietnam Prosperity Joint-Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>10</td> <td>970439</td> <td>Public Bank Vietnam Limited (PBVN)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>11</td> <td>970415</td> <td>VIETNAM JOINT STOCK COMMERCIAL BANK FOR INDUSTRY AND TRADE (Viettinbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>12</td> <td>970431</td> <td>VIETNAM EXPORT IMPORT COMMERCIAL JOINT STOCK BANK (Eximbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>13</td> <td>970440</td> <td>Southeast Asia Commercial Joint Stock Bank (SeABank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>14</td> <td>970429</td> <td>Sai Gon Joint StockCommercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>15</td> <td>970448</td> <td>Orient Commercial Joint StockBank (OCB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>16</td> <td>970425</td> <td>An BinhCommercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>17</td> <td>970426</td> <td>Vietnam Maritime Commercial Stock Bank (MSB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>18</td> <td>970427</td> <td>Vietnam Asia Commercial Joint Stock Bank (VietA)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>19</td> <td>970419</td> <td>National Citizen Commercial Joint Stock Bank (NCB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>20</td> <td>970418</td> <td>Joint Stock Commercial Bank for Investment and Development of Vietnam (BIDV)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>21</td> <td>970443</td> <td>Sai Gon- Ha Noi Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>22</td> <td>970406</td> <td>DongA Joint Stock Commercial Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>23</td> <td>970441</td> <td>Vietnam International Commercial Joint Stock Bank (VIB)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>24</td> <td>970424</td> <td>Shinhan Bank Vietnam Limited</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>25</td> <td>970433</td> <td>Vietnam Thuong Tin Commercial Joint Stock Bank (Vietbank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>26</td> <td>970454</td> <td>VIET CAPITAL COMMERCIAL JOINT STOCK BANK (Ban Viet)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>27</td> <td>970452</td> <td>Kien Long Commercial Joint -Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>28</td> <td>970430</td> <td>PETROLIMEX GROUPCOMMERCIAL JOINT STOCK BANK</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>29</td> <td>970400</td> <td>Sai Gon Joint Stock Commercial Bank (Saigon Bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>30</td> <td>970405</td> <td>Vietnam Bank for Agriculture and Rural Development or Agribank (Agribank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>31</td> <td>970403</td> <td>Sacombank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>32</td> <td>970412</td> <td>Vietnam Public Joint Stock Commercial Bank (Vietnam dai chung)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>33</td> <td>970421</td> <td>Vietnam-Russia Joint Venture Bank - VRB</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>34</td> <td>970428</td> <td>Nam A Commercial Joint Stock Bank (Nam A Bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>35</td> <td>970434</td> <td>Indovina Bank Ltd</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>36</td> <td>970449</td> <td>LienViet Post Joint Stock Commercial Bank (LienViet Post bank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>37</td> <td>970457</td> <td>Woori Bank Vietnam Limited</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>38</td> <td>970436</td> <td>Joint Stock Commercial Bank for Foreign Trade of Vietnam (Vietcombank)</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>39</td> <td>970416</td> <td>Asia Commercial Joint Stock Bank</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>40</td> <td>970458</td> <td>UNITED OVERSEAS BANK (VIETNAM) LIMITED</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>41</td> <td>970446</td> <td>Co-operative bank of VietNam</td> <td></td> <td>✓</td>                         </tr>                         <tr> <td>42</td> <td>970455</td> <td>Industrial Bank of Korea - Ha Noi Branch</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>43</td> <td>970409</td> <td>North Asia Commercial Joint Stock Bank</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>44</td> <td>422589</td> <td>CIMB Bank (Vietnam) Limited</td> <td>✓</td> <td>✓</td>                         </tr>                         <tr> <td>45</td> <td>796500</td> <td>Ngân hàng DBS - Chi nhánh Hồ Chí Minh(DBS)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>46</td> <td>458761</td> <td>TNHH MTV HSBC Việt Nam(HSBC)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>47</td> <td>970410</td> <td>TNHH MTV Standard Chartered Việt Nam(SCVN)</td> <td>✓</td> <td></td>                         </tr>                         <tr> <td>48</td> <td>801011</td> <td>Nonghuyp - Chi nhánh Hà Nội(NHB)</td> <td>✓</td> <td></td>                         </tr>  <td>49</td> <td>970444</td> <td>TM TNHH MTV Xây Dựng Việt Nam </td> <td>✓</td> <td></td>                         </tr><tr> <td>50</td> <td>970456</td> <td> IBK - chi nhánh HCM</td> <td>✓</td> <td></td>                         </tr><tr> <td>51</td> <td>970462</td> <td>Kookmin - Chi nhánh Hà Nội</td> <td>✓</td> <td>✓</td>                         </tr><tr> <td>52</td> <td>970463</td> <td>Kookmin - Chi nhánh Thành phố Hồ Chí Minh</td> <td>✓</td> <td>✓</td>                         </tr><tr> <td>53</td> <td>546034</td> <td>Ngân hàng số CAKE by VPBank</td> <td>✓</td> <td></td>                         </tr><tr> <td>54</td> <td>546035</td> <td>Ngân hàng số Ubank by VPBank</td> <td>✓</td> <td></td>                   </tbody>                 </table>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description=" Disbursement payments API",
    author_email="",
    url="",
    keywords=["Swagger", " Disbursement payments API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    &lt;h2&gt;Introduction&lt;/h2&gt; Welcome! Baokim’s mission is to deliver automated payment infrastructure solutions for your business. We help with both money in (collection payments) and money out (disbursement payments). Our users range from platforms businesses, fintech, e-Commerce, and everything else in between.  &lt;p&gt;&lt;strong&gt;Benefits of Baokim&lt;/strong&gt;&lt;/p&gt; Fast integration  Instant transfers  Daily reconciliation  Simple &amp; competitive pricing – no hidden fees  &lt;h2&gt;Regulations and requirements&lt;/h2&gt;   - API that Baokim deployed, will be built on the Restful architecture, data transmission between the two sides will be Json.  - Baokim will restrict access to the API by one or more IPs based on each Partner. So before joining , Partner will send the IP list to Baokim to open the access.  - Baokim uses Basic Authentication to allow access to the API. Account information will be provided by Bao Kim at the start of the integration.  &lt;code&gt;Authorization: Basic YmFva2ltOmJrQDEyMzQ1Ng&#x3D;&#x3D;&lt;/code&gt;  &lt;h2&gt;Restful and Digital Signature&lt;/h2&gt; &lt;p&gt;&lt;strong&gt;Restfull Web Service&lt;/strong&gt;&lt;/p&gt; REST (Representational State Transfer) has been widely adopted instead of Web services based on SOAP and WSDL. REST defines architectural rules for designing Web services that focus on system resources, including how resource states are formatted and transported via HTTP through a large number of users and are written by different languages.  In order to be able to connect REST with the tool and test with BAOKIM, the PARTNER can load and use one of the following two universal tools:  - Postman: https://www.getpostman.com  - Soap UI: https://www.soapui.org  &lt;p&gt;&lt;strong&gt;Digital signature&lt;/strong&gt;&lt;/p&gt;  &lt;img src&#x3D;\&quot;https://thuchiho.baokim.vn/assets/docs/img/sign_model.jpg\&quot; alt&#x3D;\&quot;Model Sign\&quot;&gt;   &lt;p&gt;&lt;strong&gt;Private key and public key&lt;/strong&gt;&lt;/p&gt; Baokim is currently using digital signature by RSA-SHA1  There are several ways to generate RSA key pairs.  &lt;strong&gt;Way 1&lt;/strong&gt;:  Generate your RSA key pairs online: Generate now  &lt;strong&gt;Way 2&lt;/strong&gt;:  Using OpenSSL software for Windows:  &lt;strong&gt;Step 1&lt;/strong&gt;: Download the software at:  http://slproweb.com/products/Win32OpenSSL.html. Partner should download the installer \&quot;OpenSSL_Light-1_0_2k\&quot;. Then install in any directory, for example \&quot;C:\\OpenSSLWin64\&quot;  &lt;strong&gt;Step 2&lt;/strong&gt;: Access \&quot;C:\\OpenSSLWin64\\bin\&quot; then open the command prompt. Type the command to declare the environment config.  set OPENSSL_CONF&#x3D;C:\\OpenSSL-Win64\\bin\\openssl.cfg  &lt;strong&gt;Step 3&lt;/strong&gt;: Generate private key and public key  openssl genrsa -aes256 -out c:\\opensslkeys\\partner\\partner_privatekey.pem 2048  openssl rsa –in c:\\opensslkeys\\partner\\partner_privatekey.pem -pubout &gt;c:\\opensslkeys\\partner\\partner_publickey.pem  After successful pairing, Partner will send back to Baokim the public key to authenticate the signature that the Partner sends via the API.  &lt;h3&gt;Describe the mechanism handling the transaction timeout&lt;/h3&gt; Due to traffic problems or during request processing at Baokim, transaction timeout may be generated. Baokim will describe the processing mechanism consists of two cases as follows:  &lt;strong&gt;Case 1&lt;/strong&gt;: Baokim proactively returns error code timeout, error code &lt;b&gt;99&lt;/b&gt;  - This case occurs when the two parties set the maximum time to return the results for a transaction but for some reason the Baokim or Bank has not finished processing should be proactive return error code timeout  - The way to deal with this situation: Partner when receiving the timeout error code will call the check transaction status. In this function Baokim will return the transaction status for Partner.  &lt;strong&gt;Case 2&lt;/strong&gt;: Timeout due to transmission line failure, does not get the result returned  In this case it is possible to timeout from Partner-&gt; Baokim or Baokim-&gt; Partner. So can not determine whether the transaction Baokim reception or not.  - The way to deal with this situation:  1. The Partner will call Check Transaction Status to look up transaction status. If the result is received then the Partner will update the partner status. If timeout is still the case then move on to step 2.  2. In cases where transmission lines meet with long incidents, Baokim and Partner will coordinate with human handling to certification. Partner will email to Baokim to request sending status for a transaction, the Baokim&#x27;s technique will confirm the status and return to Partner.   &lt;h2&gt;List of bank transfer assistance. &lt;/h2&gt;  &lt;table&gt;                     &lt;thead&gt;                         &lt;tr&gt; &lt;th&gt;#&lt;/th&gt; &lt;th&gt;BankNo&lt;/th&gt; &lt;th&gt;BankName&lt;/th&gt; &lt;th&gt;Account&lt;/th&gt; &lt;th&gt;Card&lt;/th&gt;                         &lt;/tr&gt;                     &lt;/thead&gt;                     &lt;tbody&gt;                         &lt;tr&gt; &lt;td&gt;1&lt;/td&gt; &lt;td&gt;970423&lt;/td&gt; &lt;td&gt;TIEN PHONG COMMERCIAL JOINT STOCK BANK&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;2&lt;/td&gt; &lt;td&gt;970437&lt;/td&gt; &lt;td&gt;Ho Chi Minh City Development Joint Stock Commercial Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;3&lt;/td&gt; &lt;td&gt;970408&lt;/td&gt; &lt;td&gt;Global Petro Sole Member LimitedCommercial Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;4&lt;/td&gt; &lt;td&gt;970407&lt;/td&gt; &lt;td&gt;Vietnam Technological and Commercial Joint Stock Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;5&lt;/td&gt; &lt;td&gt;970442&lt;/td&gt; &lt;td&gt;Hong Leong Commercial Joint Stock Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;6&lt;/td&gt; &lt;td&gt;970414&lt;/td&gt; &lt;td&gt;Ocean Commercial Joint - Stock Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;7&lt;/td&gt; &lt;td&gt;970438&lt;/td&gt; &lt;td&gt;Bao Viet Joint Stock Commercial Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;8&lt;/td&gt; &lt;td&gt;970422&lt;/td&gt; &lt;td&gt;Military Commercial Joint Stock Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;9&lt;/td&gt; &lt;td&gt;970432&lt;/td&gt; &lt;td&gt;Vietnam Prosperity Joint-Stock Commercial Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;10&lt;/td&gt; &lt;td&gt;970439&lt;/td&gt; &lt;td&gt;Public Bank Vietnam Limited (PBVN)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;11&lt;/td&gt; &lt;td&gt;970415&lt;/td&gt; &lt;td&gt;VIETNAM JOINT STOCK COMMERCIAL BANK FOR INDUSTRY AND TRADE (Viettinbank)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;12&lt;/td&gt; &lt;td&gt;970431&lt;/td&gt; &lt;td&gt;VIETNAM EXPORT IMPORT COMMERCIAL JOINT STOCK BANK (Eximbank)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;13&lt;/td&gt; &lt;td&gt;970440&lt;/td&gt; &lt;td&gt;Southeast Asia Commercial Joint Stock Bank (SeABank)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;14&lt;/td&gt; &lt;td&gt;970429&lt;/td&gt; &lt;td&gt;Sai Gon Joint StockCommercial Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;15&lt;/td&gt; &lt;td&gt;970448&lt;/td&gt; &lt;td&gt;Orient Commercial Joint StockBank (OCB)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;16&lt;/td&gt; &lt;td&gt;970425&lt;/td&gt; &lt;td&gt;An BinhCommercial Joint Stock Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;17&lt;/td&gt; &lt;td&gt;970426&lt;/td&gt; &lt;td&gt;Vietnam Maritime Commercial Stock Bank (MSB)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;18&lt;/td&gt; &lt;td&gt;970427&lt;/td&gt; &lt;td&gt;Vietnam Asia Commercial Joint Stock Bank (VietA)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;19&lt;/td&gt; &lt;td&gt;970419&lt;/td&gt; &lt;td&gt;National Citizen Commercial Joint Stock Bank (NCB)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;20&lt;/td&gt; &lt;td&gt;970418&lt;/td&gt; &lt;td&gt;Joint Stock Commercial Bank for Investment and Development of Vietnam (BIDV)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;21&lt;/td&gt; &lt;td&gt;970443&lt;/td&gt; &lt;td&gt;Sai Gon- Ha Noi Commercial Joint Stock Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;22&lt;/td&gt; &lt;td&gt;970406&lt;/td&gt; &lt;td&gt;DongA Joint Stock Commercial Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;23&lt;/td&gt; &lt;td&gt;970441&lt;/td&gt; &lt;td&gt;Vietnam International Commercial Joint Stock Bank (VIB)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;24&lt;/td&gt; &lt;td&gt;970424&lt;/td&gt; &lt;td&gt;Shinhan Bank Vietnam Limited&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;25&lt;/td&gt; &lt;td&gt;970433&lt;/td&gt; &lt;td&gt;Vietnam Thuong Tin Commercial Joint Stock Bank (Vietbank)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;26&lt;/td&gt; &lt;td&gt;970454&lt;/td&gt; &lt;td&gt;VIET CAPITAL COMMERCIAL JOINT STOCK BANK (Ban Viet)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;27&lt;/td&gt; &lt;td&gt;970452&lt;/td&gt; &lt;td&gt;Kien Long Commercial Joint -Stock Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;28&lt;/td&gt; &lt;td&gt;970430&lt;/td&gt; &lt;td&gt;PETROLIMEX GROUPCOMMERCIAL JOINT STOCK BANK&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;29&lt;/td&gt; &lt;td&gt;970400&lt;/td&gt; &lt;td&gt;Sai Gon Joint Stock Commercial Bank (Saigon Bank)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;30&lt;/td&gt; &lt;td&gt;970405&lt;/td&gt; &lt;td&gt;Vietnam Bank for Agriculture and Rural Development or Agribank (Agribank)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;31&lt;/td&gt; &lt;td&gt;970403&lt;/td&gt; &lt;td&gt;Sacombank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;32&lt;/td&gt; &lt;td&gt;970412&lt;/td&gt; &lt;td&gt;Vietnam Public Joint Stock Commercial Bank (Vietnam dai chung)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;33&lt;/td&gt; &lt;td&gt;970421&lt;/td&gt; &lt;td&gt;Vietnam-Russia Joint Venture Bank - VRB&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;34&lt;/td&gt; &lt;td&gt;970428&lt;/td&gt; &lt;td&gt;Nam A Commercial Joint Stock Bank (Nam A Bank)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;35&lt;/td&gt; &lt;td&gt;970434&lt;/td&gt; &lt;td&gt;Indovina Bank Ltd&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;36&lt;/td&gt; &lt;td&gt;970449&lt;/td&gt; &lt;td&gt;LienViet Post Joint Stock Commercial Bank (LienViet Post bank)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;37&lt;/td&gt; &lt;td&gt;970457&lt;/td&gt; &lt;td&gt;Woori Bank Vietnam Limited&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;38&lt;/td&gt; &lt;td&gt;970436&lt;/td&gt; &lt;td&gt;Joint Stock Commercial Bank for Foreign Trade of Vietnam (Vietcombank)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;39&lt;/td&gt; &lt;td&gt;970416&lt;/td&gt; &lt;td&gt;Asia Commercial Joint Stock Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;40&lt;/td&gt; &lt;td&gt;970458&lt;/td&gt; &lt;td&gt;UNITED OVERSEAS BANK (VIETNAM) LIMITED&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;41&lt;/td&gt; &lt;td&gt;970446&lt;/td&gt; &lt;td&gt;Co-operative bank of VietNam&lt;/td&gt; &lt;td&gt;&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;42&lt;/td&gt; &lt;td&gt;970455&lt;/td&gt; &lt;td&gt;Industrial Bank of Korea - Ha Noi Branch&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;43&lt;/td&gt; &lt;td&gt;970409&lt;/td&gt; &lt;td&gt;North Asia Commercial Joint Stock Bank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;44&lt;/td&gt; &lt;td&gt;422589&lt;/td&gt; &lt;td&gt;CIMB Bank (Vietnam) Limited&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;45&lt;/td&gt; &lt;td&gt;796500&lt;/td&gt; &lt;td&gt;Ngân hàng DBS - Chi nhánh Hồ Chí Minh(DBS)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;46&lt;/td&gt; &lt;td&gt;458761&lt;/td&gt; &lt;td&gt;TNHH MTV HSBC Việt Nam(HSBC)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;47&lt;/td&gt; &lt;td&gt;970410&lt;/td&gt; &lt;td&gt;TNHH MTV Standard Chartered Việt Nam(SCVN)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;&lt;/td&gt;                         &lt;/tr&gt;                         &lt;tr&gt; &lt;td&gt;48&lt;/td&gt; &lt;td&gt;801011&lt;/td&gt; &lt;td&gt;Nonghuyp - Chi nhánh Hà Nội(NHB)&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;&lt;/td&gt;                         &lt;/tr&gt;  &lt;td&gt;49&lt;/td&gt; &lt;td&gt;970444&lt;/td&gt; &lt;td&gt;TM TNHH MTV Xây Dựng Việt Nam &lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;&lt;/td&gt;                         &lt;/tr&gt;&lt;tr&gt; &lt;td&gt;50&lt;/td&gt; &lt;td&gt;970456&lt;/td&gt; &lt;td&gt; IBK - chi nhánh HCM&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;&lt;/td&gt;                         &lt;/tr&gt;&lt;tr&gt; &lt;td&gt;51&lt;/td&gt; &lt;td&gt;970462&lt;/td&gt; &lt;td&gt;Kookmin - Chi nhánh Hà Nội&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;&lt;tr&gt; &lt;td&gt;52&lt;/td&gt; &lt;td&gt;970463&lt;/td&gt; &lt;td&gt;Kookmin - Chi nhánh Thành phố Hồ Chí Minh&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt;                         &lt;/tr&gt;&lt;tr&gt; &lt;td&gt;53&lt;/td&gt; &lt;td&gt;546034&lt;/td&gt; &lt;td&gt;Ngân hàng số CAKE by VPBank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;&lt;/td&gt;                         &lt;/tr&gt;&lt;tr&gt; &lt;td&gt;54&lt;/td&gt; &lt;td&gt;546035&lt;/td&gt; &lt;td&gt;Ngân hàng số Ubank by VPBank&lt;/td&gt; &lt;td&gt;✓&lt;/td&gt; &lt;td&gt;&lt;/td&gt;                   &lt;/tbody&gt;                 &lt;/table&gt;  # noqa: E501
    """
)
