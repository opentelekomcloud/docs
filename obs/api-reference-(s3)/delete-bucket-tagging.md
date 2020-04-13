# DELETE Bucket tagging<a name="EN-US_TOPIC_0125560426"></a>

This implementation of the  **DELETE**  operation uses the **tagging**  subresource to remove a tag set from the specified bucket.

Only users granted the  **s3:PutBucketTagging**  permission can perform this operation. By default, the permission is granted to the bucket owner only. However, it can be granted to other users by configuring the bucket policy.

## Request Syntax<a name="section57518732"></a>

```
DELETE /?tagging HTTP/1.1
User-Agent: agent 
Host: bucketname.obs.example.com
Accept: */* 
Date: date 
Authorization: authorization string
```

## Request Parameters<a name="section47906541"></a>

This request involves no parameters.

## Request Headers<a name="section28505693"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section55224652"></a>

This request involves no elements.

## Response Syntax<a name="section46270551"></a>

```
HTTP/1.1 204 No Content
Server: Server Name 
x-amz-request-id: request id 
x-amz-id-2: id
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
Date: date
```

## Response Headers<a name="section13781782"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section56927182"></a>

This response involves no elements.

## Error Responses<a name="section42582590"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section32323009"></a>

```
DELETE /?tagging HTTP/1.1 
User-Agent: curl/7.19.7 (x86_64-suse-linux-gnu) libcurl/7.19.7 OpenSSL/0.9.8j zlib/1.2.7 libidn/1.10 
Host: bucketname.obs.example.com 
Accept: */* 
Date: Tue, 09 May 2017 03:07:13 +0000 
Authorization: authorization string
```

## Sample Response<a name="section22471632"></a>

```
HTTP/1.1 204 No Content
Server: OBS 
x-amz-request-id: request id 
x-amz-id-2: id
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
Date: Tue, 09 May 2017 03:06:29 GMT
```

