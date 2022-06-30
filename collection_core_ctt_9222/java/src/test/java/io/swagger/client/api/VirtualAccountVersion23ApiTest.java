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

import io.swagger.client.model.InlineResponse101;
import io.swagger.client.model.InlineResponse200;
import io.swagger.client.model.SandboxCollectionBody;
import org.junit.Test;
import org.junit.Ignore;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


/**
 * API tests for VirtualAccountVersion23Api
 */
@Ignore
public class VirtualAccountVersion23ApiTest {

    private final VirtualAccountVersion23Api api = new VirtualAccountVersion23Api();

    /**
     * create &amp; update va
     *
     * 
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void 6ce3bcd0268f76548ace52ed5eeeefefTest() throws Exception {
        SandboxCollectionBody body = null;
        String contentType = null;
        String signature = null;
        InlineResponse200 response = api.6ce3bcd0268f76548ace52ed5eeeefef(body, contentType, signature);

        // TODO: test validations
    }
}