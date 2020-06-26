# Sample Code Description<a name="EN-US_TOPIC_0086093991"></a>

## AK/SK Authentication<a name="section101697221649"></a>

AK/SK authentication is supported for users who access DMS through RESTful APIs.

Example signature source code files:

-   **src/main/java/com/cloud/dms/access/AccessService.java**

    Abstract class that converts the GET, POST, PUT, and DELETE methods into the access method.

-   **src/main/java/com/cloud/dms/access/AccessServiceImpl.java**

    Implementation of the access method. Code required for the API gateway communication is in the access method.


Perform the following procedure to sign a request:

1.  Create request  **com.cloud.sdk.DefaultRequest\(JAVA\)**  used for signing.

    ```
    Request request = new DefaultRequest(this.serviceName);
    ```

    Set  **serviceName**  to  **dms**.

2.  Set the target API URL, HTTPS method, and content of  **com.cloud.sdk.DefaultRequest\(JAVA\)**.

    ```
    request.setEndpoint(url.toURI());
    ...
    if (urlString.contains("?"))
    {
        ...
        request.setParameters(parametersmap);
        ...
    }
    ...
    request.setHttpMethod(httpMethod);
    if (headers != null)
    {
        request.setHeaders(headers);
    }
    request.setContent(content);
    
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >**...**  indicates that some code is not displayed here. For the complete code, see the example source code files.  

3.  Sign request  **com.cloud.sdk.DefaultRequest\(JAVA\)**.
    1.  Call  **SignerFactory.getSigner\(String serviceName, String regionName\)**  to obtain a signature tool instance.

        ```
        Signer signer = SignerFactory.getSigner(serviceName, region);
        ```

        Set  **serviceName**  to  **dms**  and configure  **region**  in  **dms-service-config.properties**.

    2.  Call  **Signer.sign\(Request<?\> request, Credentials credentials\)**  to sign the request.

        ```
        signer.sign(request, new BasicCredentials(this.ak, this.sk));
        ```

        **ak**  and  **sk**  are configured in  **dms-service-config.properties**.

4.  Convert the signed request to one suitable for calling an API, and copy the header of the signed request to the new request.

    ```
    // Make a request that can be sent by the HTTP client
    HttpRequestBase httpRequestBase = createRequest(url, null, request.getContent(), contentLength, httpMethod);
    
    // Put the header of the signed request to the new request
    Map<String, String> requestHeaders = request.getHeaders();
    for (String key : requestHeaders.keySet())
    {
        ...
        httpRequestBase.addHeader(key, requestHeaders.get(key));
    }
    ```

    For details about the  **createRequest**  method, see the example source code files.


## Sending an API Request<a name="section17431689156"></a>

After an API request is constructed following the instructions in AK/SK Authentication, it can be sent to the DMS server. In this sample project, the Apache HttpComponents tool is used. The request sending code is as follows:

```
HttpResponse response = null;
SSLContext sslContext = SSLContexts.custom()
        .loadTrustMaterial(null, new TrustSelfSignedStrategy())
        .useTLS()
        .build();
SSLConnectionSocketFactory sslSocketFactory =
    new SSLConnectionSocketFactory(sslContext, new AllowAllHostnameVerifier());

client = HttpClients.custom().setSSLSocketFactory(sslSocketFactory).build();
// Send the request, and a response will be returned
response = client.execute(httpRequestBase);
```

