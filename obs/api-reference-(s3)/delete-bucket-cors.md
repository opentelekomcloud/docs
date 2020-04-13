# DELETE Bucket CORS<a name="EN-US_TOPIC_0125560432"></a>

You can use this operation to delete the CORS configuration of a bucket.

After the CORS configuration is deleted, the bucket and objects in it cannot be accessed by requests from other websites.

Only users granted the  **s3:PutBucketCORS**  permission can perform this operation. By default, only the bucket owner can perform this operation. The bucket owner can allow other users to perform this operation by granting them the permission.

## Request Syntax<a name="section57518732"></a>

```
DELETE /?cors HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section47906541"></a>

This request involves no parameters.

## Request Headers<a name="section28505693"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section55224652"></a>

This request involves no elements.

## Response Syntax<a name="section46270551"></a>

```
HTTP/1.1 status_code 
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
DELETE /?cors HTTP/1.1 
 User-Agent: curl/7.19.0 (x86_64-suse-linux-gnu) libcurl/7.19.0 OpenSSL/0.9.8{ zlib/1.2.3 libidn/1.10 
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: Tue, 28 Apr 2015 09:34:51 +0000 
 Authorization: AWS D13E0C94E722DD69423C:YiZ7gMEMnxjYM32AjsCpoR4FpoI=
```

## Sample Response<a name="section22471632"></a>

```
HTTP/1.1 204 No Content 
 Server: OBS
 x-amz-request-id: 400535B2BF32AD9B6B21873AF4D5A57D 
 x-amz-id-2: ihd0YbWuLj8XsU7IZKQFqK9KPoPean7wCQ2QYLqv9lkOCNr40+67DneNvK3Nfjt6 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: Tue, 28 Apr 2015 09:34:51 GMT
```

