# DELETE Bucket<a name="EN-US_TOPIC_0125560472"></a>

You can use this operation to delete the buckets specified by a user.

Only the bucket owner and users who are granted the permission to delete buckets can delete buckets. Only an empty bucket can be deleted. If a bucket has an object or a multipart task, the bucket is not empty. You can determine whether a bucket is empty by listing objects and multipart upload tasks in the bucket.

>![](/images/icon-note.gif) **NOTE:**   
>If a 5_xx_  error is returned from the server or the request times out during bucket deletion, the system takes about 10 minutes to make bucket information consistent. During the process, bucket information is inaccurate.  

## Request Syntax<a name="section45427372"></a>

```
DELETE / HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section6193166"></a>

This request involves no parameters.

## Request Headers<a name="section55738502"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section31884476"></a>

This request involves no elements.

## Response Syntax<a name="section29213744"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: id 
 Date: date
```

## Response Headers<a name="section61597110"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section17503083"></a>

This response involves no elements.

## Error Responses<a name="section23310024"></a>

No special errors are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section44557004"></a>

```
DELETE / HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: Sat, 03 Dec 2011 07:07:35 +0000 
 Authorization: AWS BF6C09F302931425E9A7:lgEeRg8WE0XOpjurUSX26QDIZRw=
```

## Sample Response<a name="section65468724"></a>

```
HTTP/1.1 204 No Content 
 Server: OBS 
 x-amz-request-id: 001B21A61C6C0000013402BFDBA85281 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: MDAxQjIxQTYxQzZDMDAwMDAxMzQwMkJGREJBODUyODFBQUFBQUFBQWJiYmJiYmJi 
 Date: Sat, 03 Dec 2011 07:07:38 GMT
```

