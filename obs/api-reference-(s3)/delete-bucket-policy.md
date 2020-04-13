# DELETE Bucket policy<a name="EN-US_TOPIC_0125560427"></a>

You can use this operation to delete the policy of a specified bucket.

Only the bucket owner can delete the bucket policy.

OBS returns  **204 No Content**  whether a requested bucket policy exists or not.

## Request Syntax<a name="section50184984"></a>

```
DELETE /?policy HTTP/1.1 
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section49011679"></a>

This request involves no parameters.

## Request Headers<a name="section38451933"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section10523083"></a>

This request involves no elements.

## Response Syntax<a name="section31093287"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-amz-id-2: id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: date 
 Content-Type: type
```

## Response Headers<a name="section11404133"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response elements<a name="section35528341"></a>

This response involves no elements.

## Error Responses<a name="section51319614"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section6925935"></a>

```
DELETE /?policy HTTP/1.1 
Host: bucketname.obs.example.com
Accept: */* 
Date: Fri, 06 Sep 2013 07:06:42 GMT
Authorization: signature
```

## Sample Response<a name="section62333418"></a>

```
HTTP/1.1 204 No Content 
Server: OBS 
x-amz-request-id: 7B6DFC9BC71DD58B061285551605709 
x-amz-id-2: N0I2REZDOUJDNzFERDU4QjA2MTI4NTU1MTYwNTcwOUFBQUFBQUFBYmJiYmJiYmJD 
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
Content-Type: text/xml 
Date: Mon, 27 Sep 2010 01:40:03 GMT 
```

