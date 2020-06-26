# Authentication<a name="rds_03_0001"></a>

Token authentication must be performed to call APIs.

Authentication using tokens: General requests are authenticated using tokens.

## Token-based Authentication<a name="section2417768214391"></a>

>![](/images/icon-note.gif) **NOTE:**   
>The validity period of a token is 24 hours. When using a token for authentication, cache it to prevent frequently calling the IAM API used to obtain a user token.  

A token specifies temporary permissions in a computer system. During API authentication using a token, the token is added to requests to get permissions for calling the API.

In  [Making an API Request](making-an-api-request.md), the process of calling the API used to  [obtain a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html)  is described.

After a token is obtained, add the  **X-Auth-Token**  header field must be added to requests to specify the token when calling other APIs. For example, if the token is  **ABCDEFJ....**,  **X-Auth-Token: ABCDEFJ....**  can be added to a request as follows:

```

Content-Type: application/json
X-Auth-Token: ABCDEFJ....
```

