# Returned Values<a name="dws_02_0065"></a>

## Status Code<a name="en-us_topic_0171007791_en-us_topic_0170155703_section968114282311"></a>

After sending a request, you will receive a response, including the status code, response header, and response body.

A status code is a group of digits ranging from 1xx to 5xx. It indicates the status of a response. For more information, see  [Status Code](status-code.md).

If status code  **201**  is returned for the calling of the API for obtaining a user token, the request is successful.

## Response Header<a name="en-us_topic_0171007791_en-us_topic_0170155703_en-us_topic_0113746487_section61333484715"></a>

A response header corresponds to a request header, for example,  **Content-Type**.

[Figure 1](#en-us_topic_0171007791_en-us_topic_0170155703_fig4865141011511)  shows the response header for the API of obtaining a user token, in which x-subject-token is the desired user token. Then, you can use the token to authenticate the calling of other APIs.

**Figure  1**  Header of the response to the request for obtaining a user token<a name="en-us_topic_0171007791_en-us_topic_0170155703_fig4865141011511"></a>  
![](figures/header-of-the-response-to-the-request-for-obtaining-a-user-token.png "header-of-the-response-to-the-request-for-obtaining-a-user-token")

## Response Body<a name="en-us_topic_0171007791_en-us_topic_0170155703_en-us_topic_0113746487_section2045571671419"></a>

A response body is generally returned in a structured format \(for example, JSON or XML\), corresponding to the Content-Type in the response header, and is used to transfer content other than the response header.

The following shows part of the response body for the API to obtain a user token. 

```
{
    "token": {
        "expires_at": "2019-02-13T06:52:13.855000Z",
        "methods": [
            "password"
        ],
        "catalog": [
            {
                "endpoints": [
                    {
                        "region_id": "eu-de",
......
```

If an error occurs during API calling, the system returns an error code and a message to you. The following shows the format of an error response body:

```
{
    "error_msg": "The format of message is error", 
     "error_code": "AS.0001" 
}
```

In the preceding information,  **error\_code**  is an error code, and  **error\_msg**  describes the error.

