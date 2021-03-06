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


import io.swagger.client.model.InlineResponse101;
import io.swagger.client.model.InlineResponse200;
import io.swagger.client.model.V4CreateBody;
import io.swagger.client.model.V4UpdateBody;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class VirtualAccount40Api {
    private ApiClient apiClient;

    public VirtualAccount40Api() {
        this(Configuration.getDefaultApiClient());
    }

    public VirtualAccount40Api(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return apiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    /**
     * Build call for 1796c61005edee3976097a607fe9dbaa
     * @param body  (required)
     * @param contentType  (optional)
     * @param signature BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call 1796c61005edee3976097a607fe9dbaaCall(V4UpdateBody body, String contentType, String signature, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = body;
        
        // create path and map variables
        String localVarPath = "/api/Sandbox/Collection/V4/update";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        if (contentType != null)
        localVarHeaderParams.put("Content-Type", apiClient.parameterToString(contentType));
        if (signature != null)
        localVarHeaderParams.put("Signature", apiClient.parameterToString(signature));

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
    private com.squareup.okhttp.Call 1796c61005edee3976097a607fe9dbaaValidateBeforeCall(V4UpdateBody body, String contentType, String signature, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        // verify the required parameter 'body' is set
        if (body == null) {
            throw new ApiException("Missing the required parameter 'body' when calling 1796c61005edee3976097a607fe9dbaa(Async)");
        }
        
        com.squareup.okhttp.Call call = 1796c61005edee3976097a607fe9dbaaCall(body, contentType, signature, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * Update virtual account
     * 
     * @param body  (required)
     * @param contentType  (optional)
     * @param signature BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional)
     * @return InlineResponse200
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public InlineResponse200 1796c61005edee3976097a607fe9dbaa(V4UpdateBody body, String contentType, String signature) throws ApiException {
        ApiResponse<InlineResponse200> resp = 1796c61005edee3976097a607fe9dbaaWithHttpInfo(body, contentType, signature);
        return resp.getData();
    }

    /**
     * Update virtual account
     * 
     * @param body  (required)
     * @param contentType  (optional)
     * @param signature BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional)
     * @return ApiResponse&lt;InlineResponse200&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<InlineResponse200> 1796c61005edee3976097a607fe9dbaaWithHttpInfo(V4UpdateBody body, String contentType, String signature) throws ApiException {
        com.squareup.okhttp.Call call = 1796c61005edee3976097a607fe9dbaaValidateBeforeCall(body, contentType, signature, null, null);
        Type localVarReturnType = new TypeToken<InlineResponse200>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

    /**
     * Update virtual account (asynchronously)
     * 
     * @param body  (required)
     * @param contentType  (optional)
     * @param signature BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call 1796c61005edee3976097a607fe9dbaaAsync(V4UpdateBody body, String contentType, String signature, final ApiCallback<InlineResponse200> callback) throws ApiException {

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

        com.squareup.okhttp.Call call = 1796c61005edee3976097a607fe9dbaaValidateBeforeCall(body, contentType, signature, progressListener, progressRequestListener);
        Type localVarReturnType = new TypeToken<InlineResponse200>(){}.getType();
        apiClient.executeAsync(call, localVarReturnType, callback);
        return call;
    }
    /**
     * Build call for 8442c69ffbaf4b3677a52fa3ebcef6d4
     * @param body  (required)
     * @param contentType  (optional)
     * @param signature BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call 8442c69ffbaf4b3677a52fa3ebcef6d4Call(V4CreateBody body, String contentType, String signature, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = body;
        
        // create path and map variables
        String localVarPath = "/api/Sandbox/Collection/V4/create";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        if (contentType != null)
        localVarHeaderParams.put("Content-Type", apiClient.parameterToString(contentType));
        if (signature != null)
        localVarHeaderParams.put("Signature", apiClient.parameterToString(signature));

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
    private com.squareup.okhttp.Call 8442c69ffbaf4b3677a52fa3ebcef6d4ValidateBeforeCall(V4CreateBody body, String contentType, String signature, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        // verify the required parameter 'body' is set
        if (body == null) {
            throw new ApiException("Missing the required parameter 'body' when calling 8442c69ffbaf4b3677a52fa3ebcef6d4(Async)");
        }
        
        com.squareup.okhttp.Call call = 8442c69ffbaf4b3677a52fa3ebcef6d4Call(body, contentType, signature, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * Create virtual account
     * 
     * @param body  (required)
     * @param contentType  (optional)
     * @param signature BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional)
     * @return InlineResponse200
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public InlineResponse200 8442c69ffbaf4b3677a52fa3ebcef6d4(V4CreateBody body, String contentType, String signature) throws ApiException {
        ApiResponse<InlineResponse200> resp = 8442c69ffbaf4b3677a52fa3ebcef6d4WithHttpInfo(body, contentType, signature);
        return resp.getData();
    }

    /**
     * Create virtual account
     * 
     * @param body  (required)
     * @param contentType  (optional)
     * @param signature BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional)
     * @return ApiResponse&lt;InlineResponse200&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<InlineResponse200> 8442c69ffbaf4b3677a52fa3ebcef6d4WithHttpInfo(V4CreateBody body, String contentType, String signature) throws ApiException {
        com.squareup.okhttp.Call call = 8442c69ffbaf4b3677a52fa3ebcef6d4ValidateBeforeCall(body, contentType, signature, null, null);
        Type localVarReturnType = new TypeToken<InlineResponse200>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

    /**
     * Create virtual account (asynchronously)
     * 
     * @param body  (required)
     * @param contentType  (optional)
     * @param signature BAOKIM will sign the Data with sha1WithRSA algorithm and use base64 encryption (optional)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call 8442c69ffbaf4b3677a52fa3ebcef6d4Async(V4CreateBody body, String contentType, String signature, final ApiCallback<InlineResponse200> callback) throws ApiException {

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

        com.squareup.okhttp.Call call = 8442c69ffbaf4b3677a52fa3ebcef6d4ValidateBeforeCall(body, contentType, signature, progressListener, progressRequestListener);
        Type localVarReturnType = new TypeToken<InlineResponse200>(){}.getType();
        apiClient.executeAsync(call, localVarReturnType, callback);
        return call;
    }
}
