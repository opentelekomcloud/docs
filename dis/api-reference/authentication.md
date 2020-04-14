# Authentication<a name="dis_02_0517"></a>

Requests for calling an API can be authenticated using either of the following methods:

-   Token-based authentication: Requests are authenticated using a token.
-   AK/SK-based authentication: Requests are authenticated by encrypting the request body using an AK/SK pair. AK/SK authentication is recommended because it is more secure than token authentication.

## Token-based Authentication<a name="en-us_topic_0121671869_section2417768214391"></a>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   The validity period of a token is 24 hours. When using a token for authentication, cache it to prevent frequently calling the IAM API used to obtain a user token.  
>-   DIS is a project-level service deployed in specific physical regions. When obtaining a token, set  **scope**  in the message body to  **project**, indicating that the obtained token can be used to access only resources in a specific project.  **project**  supports parameters  **ID**  and  **name**. You can set either of them.  

A token specifies temporary permissions in a computer system. During API authentication using a token, the token is added to requests to get permissions for calling the API.

In  [Making an API Request](making-an-api-request.md), the process of calling the API used to obtain  [obtain a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html)  is described. After a token is obtained, the  **X-Auth-Token**  header field must be added to requests to specify the token when calling other APIs. For example, if the token is  **ABCDEFJ....**,  **X-Auth-Token: ABCDEFJ....**  can be added to a request as follows:

```

Content-Type: application/json
X-Auth-Token: ABCDEFJ....
```

