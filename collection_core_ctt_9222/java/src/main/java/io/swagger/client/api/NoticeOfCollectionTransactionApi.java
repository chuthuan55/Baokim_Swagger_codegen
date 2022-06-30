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

import io.swagger.client.ApiCallback;
import io.swagger.client.ApiClient;
import io.swagger.client.ApiException;
import io.swagger.client.ApiResponse;
import io.swagger.client.Configuration;
import io.swagger.client.Pair;
import io.swagger.client.ProgressRequestBody;
import io.swagger.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import io.swagger.client.model.Body;
import io.swagger.client.model.InlineResponse2001;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class NoticeOfCollectionTransactionApi {
    private ApiClient apiClient;

    public NoticeOfCollectionTransactionApi() {
        this(Configuration.getDefaultApiClient());
    }

    public NoticeOfCollectionTransactionApi(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return apiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    /**
     * Build call for 6ce3bcd0268f76548ace52ed5eeeefef
     * @param body  (required)
     * @param contentType  (optional)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call 6ce3bcd0268f76548ace52ed5eeeefefCall(Body body, String contentType, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = body;
        
        // create path and map variables
        String localVarPath = "(api partner provide)";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        if (contentType != null)
        localVarHeaderParams.put("Content-Type", apiClient.parameterToString(contentType));

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) localVarHeaderParams.put("Accept", localVarAccept);

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        if(progressListener != null) {
            apiClient.getHttpClient().networkInterceptors().add(new com.squareup.okhttp.Interceptor() {
                @Override
                public com.squareup.okhttp.Response intercept(com.squareup.okhttp.Interceptor.Chain chain) throws IOException {
                    com.squareup.okhttp.Response originalResponse = chain.proceed(chain.request());
                    return originalResponse.newBuilder()
                    .body(new ProgressResponseBody(originalResponse.body(), progressListener))
                    .build();
                }
            });
        }

        String[] localVarAuthNames = new String[] {  };
        return apiClient.buildCall(localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, progressRequestListener);
    }
    
    @SuppressWarnings("rawtypes")
    private com.squareup.okhttp.Call 6ce3bcd0268f76548ace52ed5eeeefefValidateBeforeCall(Body body, String contentType, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        // verify the required parameter 'body' is set
        if (body == null) {
            throw new ApiException("Missing the required parameter 'body' when calling 6ce3bcd0268f76548ace52ed5eeeefef(Async)");
        }
        
        com.squareup.okhttp.Call call = 6ce3bcd0268f76548ace52ed5eeeefefCall(body, contentType, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * (PARTNER Provide)
     * &lt;p&gt;Process:&lt;/p&gt;                 &lt;p&gt;1. PARTNER build the system, to receive data notice the collection transaction.&lt;/p&gt;                 &lt;p&gt;2. When receive a new collection transaction, BAOKIM will call to “collection transaction notification” that provided by PARTNER to notice PARTNER need to update data.&lt;/p&gt;
     * @param body  (required)
     * @param contentType  (optional)
     * @return InlineResponse2001
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public InlineResponse2001 6ce3bcd0268f76548ace52ed5eeeefef(Body body, String contentType) throws ApiException {
        ApiResponse<InlineResponse2001> resp = 6ce3bcd0268f76548ace52ed5eeeefefWithHttpInfo(body, contentType);
        return resp.getData();
    }

    /**
     * (PARTNER Provide)
     * &lt;p&gt;Process:&lt;/p&gt;                 &lt;p&gt;1. PARTNER build the system, to receive data notice the collection transaction.&lt;/p&gt;                 &lt;p&gt;2. When receive a new collection transaction, BAOKIM will call to “collection transaction notification” that provided by PARTNER to notice PARTNER need to update data.&lt;/p&gt;
     * @param body  (required)
     * @param contentType  (optional)
     * @return ApiResponse&lt;InlineResponse2001&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<InlineResponse2001> 6ce3bcd0268f76548ace52ed5eeeefefWithHttpInfo(Body body, String contentType) throws ApiException {
        com.squareup.okhttp.Call call = 6ce3bcd0268f76548ace52ed5eeeefefValidateBeforeCall(body, contentType, null, null);
        Type localVarReturnType = new TypeToken<InlineResponse2001>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

    /**
     * (PARTNER Provide) (asynchronously)
     * &lt;p&gt;Process:&lt;/p&gt;                 &lt;p&gt;1. PARTNER build the system, to receive data notice the collection transaction.&lt;/p&gt;                 &lt;p&gt;2. When receive a new collection transaction, BAOKIM will call to “collection transaction notification” that provided by PARTNER to notice PARTNER need to update data.&lt;/p&gt;
     * @param body  (required)
     * @param contentType  (optional)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call 6ce3bcd0268f76548ace52ed5eeeefefAsync(Body body, String contentType, final ApiCallback<InlineResponse2001> callback) throws ApiException {

        ProgressResponseBody.ProgressListener progressListener = null;
        ProgressRequestBody.ProgressRequestListener progressRequestListener = null;

        if (callback != null) {
            progressListener = new ProgressResponseBody.ProgressListener() {
                @Override
                public void update(long bytesRead, long contentLength, boolean done) {
                    callback.onDownloadProgress(bytesRead, contentLength, done);
                }
            };

            progressRequestListener = new ProgressRequestBody.ProgressRequestListener() {
                @Override
                public void onRequestProgress(long bytesWritten, long contentLength, boolean done) {
                    callback.onUploadProgress(bytesWritten, contentLength, done);
                }
            };
        }

        com.squareup.okhttp.Call call = 6ce3bcd0268f76548ace52ed5eeeefefValidateBeforeCall(body, contentType, progressListener, progressRequestListener);
        Type localVarReturnType = new TypeToken<InlineResponse2001>(){}.getType();
        apiClient.executeAsync(call, localVarReturnType, callback);
        return call;
    }
}
