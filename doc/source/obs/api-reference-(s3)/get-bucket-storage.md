# GET Bucket storage<a name="EN-US_TOPIC_0125560293"></a>

Using this operation, the bucket owner can obtain the bucket's storage information such as the bucket size and number of objects in the bucket. The bucket size is a nonnegative integer, expressed in bytes.

## Request Syntax<a name="section2336166"></a>

```
GET /?storageinfo HTTP/1.1  
 User-Agent: agent
 Host: bucketname.obs.example.com  
 Accept: */*
 Date: date  
 Authorization: authorization
```

## Request Parameters<a name="section21025500"></a>

This request involves no parameters.

## Request Headers<a name="section55011773"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section25343916"></a>

This request involves no elements.

## Response Syntax<a name="section1340439"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: id 
 Content-Type: type 
 Date: date 
 Content-Length: length 
 <Response Body>
```

## Response Headers<a name="section12063958"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section41466763"></a>

This response involves no elements.

## Error Responses<a name="section37656551"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section22366139"></a>

```
GET /?storageinfo HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept-Encoding: gzip,deflate 
 Date: Sat, 20 Oct 2012 06:23:16 +0000 
 Authorization: AWS 08350B985315591007AD:O4jTB/FzS3gXDouwRZgz1wiE2PE= 
```

## Sample Response<a name="section67077527"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 001B21D48A580000013A7CD702AB0011 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: 8NgBZD4YTt+Gi11OlhtdGE/zB1d/q6btnc+L3E5Iq0VU80pf+GtXUfZ9lVmrhU6J 
 Content-Type: application/xml 
 Date: Sat, 20 Oct 2012 06:23:16 GMT 
 Content-Length: 209 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <GetBucketStorageInfoResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Size>14960</Size> 
 <ObjectNumber>11</ObjectNumber> 
 </GetBucketStorageInfoResult>
```

