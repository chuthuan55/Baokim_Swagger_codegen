/*
 * Retail api
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.api;

import io.swagger.client.model.InlineResponse101;
import io.swagger.client.model.InlineResponse200;
import io.swagger.client.model.RetailCheckpartnerlimitBody;
import org.junit.Test;
import org.junit.Ignore;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


/**
 * API tests for CheckPartnerLimitApi
 */
@Ignore
public class CheckPartnerLimitApiTest {

    private final CheckPartnerLimitApi api = new CheckPartnerLimitApi();

    /**
     * CHECK PARTNER LIMIT
     *
     * 
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void apiRetailCheckPartnerLimitPostTest() throws Exception {
        RetailCheckpartnerlimitBody body = null;
        String contentType = null;
        String signature = null;
        InlineResponse200 response = api.apiRetailCheckPartnerLimitPost(body, contentType, signature);

        // TODO: test validations
    }
}