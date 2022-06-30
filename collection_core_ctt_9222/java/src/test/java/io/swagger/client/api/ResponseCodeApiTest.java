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

package io.swagger.client.api;

import org.junit.Test;
import org.junit.Ignore;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


/**
 * API tests for ResponseCodeApi
 */
@Ignore
public class ResponseCodeApiTest {

    private final ResponseCodeApi api = new ResponseCodeApi();

    /**
     * Collection response code
     *
     * &lt;table&gt;         &lt;thead&gt;         &lt;tr&gt;             &lt;th&gt;ResponseCode&lt;/th&gt;             &lt;th&gt;ResponseMessage&lt;/th&gt;         &lt;/tr&gt;         &lt;/thead&gt;         &lt;tbody&gt;         &lt;tr&gt;             &lt;td&gt;200&lt;/td&gt;             &lt;td&gt;Successful&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;99&lt;/td&gt;             &lt;td&gt;Transaction timeout &lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;11&lt;/td&gt;             &lt;td&gt;Failed&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;101&lt;/td&gt;             &lt;td&gt;Error processing from Baokim&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;102&lt;/td&gt;             &lt;td&gt;Error from Bank &lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;103&lt;/td&gt;             &lt;td&gt;Operation is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;104&lt;/td&gt;             &lt;td&gt;RequestId or request  is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;105&lt;/td&gt;             &lt;td&gt;PartnerCode is incorrect  &lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;106&lt;/td&gt;             &lt;td&gt;AccName is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;107&lt;/td&gt;             &lt;td&gt;ClientIdNo is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;108&lt;/td&gt;             &lt;td&gt;IssuedDate hoặc IssuedPlace is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;109&lt;/td&gt;             &lt;td&gt;CollectAmount is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;110&lt;/td&gt;             &lt;td&gt;ExpireDate is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;111&lt;/td&gt;             &lt;td&gt;AccNo is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;112&lt;/td&gt;             &lt;td&gt;AccNo is not exist&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;113&lt;/td&gt;             &lt;td&gt;RefferenceId is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;114&lt;/td&gt;             &lt;td&gt;RefferenceId isn’t exists&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;115&lt;/td&gt;             &lt;td class&#x3D;\&quot;bg-color-red\&quot;&gt;TransAmount  is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;116&lt;/td&gt;             &lt;td class&#x3D;\&quot;bg-color-red\&quot;&gt;TransTime  is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;117&lt;/td&gt;             &lt;td class&#x3D;\&quot;bg-color-red\&quot;&gt;BefTransDebt  is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;118&lt;/td&gt;             &lt;td class&#x3D;\&quot;bg-color-red\&quot;&gt;TransId is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;119&lt;/td&gt;             &lt;td class&#x3D;\&quot;bg-color-red\&quot;&gt;AffTransDebt is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;120&lt;/td&gt;             &lt;td class&#x3D;\&quot;bg-color-red\&quot;&gt;Signature is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;121&lt;/td&gt;             &lt;td&gt;AccountType is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;122&lt;/td&gt;             &lt;td&gt;OrderId is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;127&lt;/td&gt;             &lt;td&gt;Bank is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;128&lt;/td&gt;             &lt;td&gt;CollectionType is incorrect&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;129&lt;/td&gt;             &lt;td&gt;Bank not used this CollectionType&lt;/td&gt;         &lt;/tr&gt;         &lt;/tbody&gt;     &lt;/table&gt;     &lt;p&gt;* &lt;strong class&#x3D;\&quot;bg-color-red\&quot;&gt;Red codes&lt;/strong&gt; represent errors that will arpear when developing the function: &lt;a href&#x3D;\&quot;#notice-of-collection-transaction\&quot;&gt;\&quot;Notice of collection transaction\&quot;&lt;/a&gt;&lt;/p&gt;    
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void collectionResponseCodeGetTest() throws Exception {
        api.collectionResponseCodeGet();

        // TODO: test validations
    }
}