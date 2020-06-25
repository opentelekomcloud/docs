# Authentication<a name="dws_02_0064"></a>

Calling an API can be authenticated using tokens.

## Authentication Using Tokens<a name="en-us_topic_0171007790_en-us_topic_0121671869_section2417768214391"></a>

>![](/images/icon-note.gif) **NOTE:**   
>The validity period of a token is 24 hours. When using a token for authentication, cache it to prevent frequently calling the IAM API.  

A token specifies certain permissions in a computer system. Authentication using a token adds the token in a request as its header during API calling to obtain permissions to operate APIs through IAM.

In  [Making an API Request](making-an-api-request.md), the process of calling the API for obtaining a user token is described as an example. After obtaining the token, add the  **X-Auth-Token**  header in a request to specify the token when calling other APIs. For example, if the token is  **ABCDEFJ....**, add  **X-Auth-Token: ABCDEFJ....**  in a request as follows:

```

POST https://iam.eu-de.otc.t-systems.com/v3/auth/tokens
Content-Type: application/json
X-Auth-Token: ABCDEFJ....
```

