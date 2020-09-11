# GET Bucket policy<a name="EN-US_TOPIC_0125560369"></a>

You can use this operation to return the policy of a specified bucket.

Only the bucket owner or users granted the  **s3:GetBucketPolicy**  permission can get the bucket policy.

If the bucket specified in this operation does not have a policy, OBS returns  **404 error NoSuchBucketPolicy**.

## Request Syntax<a name="section8537732"></a>

```
GET /?policy HTTP/1.1 
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section9730728"></a>

This request involves no parameters.

## Request Headers<a name="section20467690"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section49991483"></a>

This request involves no elements.

## Response Syntax<a name="section61673188"></a>

```
HTTP/1.1 status_code 
 Server: OBS 
 x-amz-request-id: 90E2BA26427C00000140F21821AA017A 
 x-amz-id-2: kwE/ohXjGAEm+DJ6Q0bu/ovJsX99na/V16xuDPFFp6C4OXrF+8V1Uu8nK6tvppvE 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 Date: date 
 Content-Length: length

 Policy Content
```

## Response Headers<a name="section18187781"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response elements<a name="section29472302"></a>

The response body is a JSON string containing bucket policies.

## Error Responses<a name="section63924128"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section43934385"></a>

```
GET /?policy HTTP/1.1 
 Host: bucketname.obs.example.com
Accept: */*
Date: Fri, 06 Sep 2013 07:06:42 GMT
Authorization: signature
```

## Sample Response<a name="section59865151"></a>

```
HTTP/1.1 200 OK
Server: OBS 
 x-amz-request-id: 90E2BA26427C00000140F21821AA017A 
 x-amz-id-2: kwE/ohXjGAEm+DJ6Q0bu/ovJsX99na/V16xuDPFFp6C4OXrF+8V1Uu8nK6tvppvE 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 Date: Fri, 06 Sep 2013 07:06:42 GMT
 Content-Length: 184
{ 
 "Id": "Policy1375342051334", 
 "Statement": [ 
 { 
 "Sid": "Stmt1375240018061", 
 "Action": [ 
 "s3:GetBucketLogging" 
 ], 
 "Effect": "Allow", 
 "Resource": "arn:aws:s3:::logging.bucket3", 
 "Principal": { 
 "AWS": [ 
 "norman" 
 ] 
 } 
 } 
 ] 
 }
```

