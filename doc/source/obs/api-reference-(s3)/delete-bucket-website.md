# DELETE Bucket website<a name="EN-US_TOPIC_0125560295"></a>

You can use this operation to delete the website configuration of a bucket.

Only users granted the  **s3:DeleteBucketWebsite**  permission can delete the bucket website configuration. By default, only the bucket owner can delete the bucket website configuration. The bucket owner can allow other users to delete the bucket website configuration by granting them the permission.

## Request Syntax<a name="section27556393"></a>

```
 DELETE /?website HTTP/1.1
 User-Agent: agent 
 Host: bucketname.obs.example.com
 Accept: */*
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section46680953"></a>

This request involves no parameters.

## Request Headers<a name="section17475399"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section23060868"></a>

This request involves no elements.

## Response Syntax<a name="section46957633"></a>

```
HTTP/1.1 status_code
 Server: Server Name
 x-amz-request-id: request id 
 x-amz-id-2: id
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: date 
```

## Response Headers<a name="section19965518"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section45471939"></a>

This response involves no elements.

## Error Responses<a name="section6594274"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section11442060"></a>

```
DELETE /?website HTTP/1.1
 User-Agent: curl/7.29.0 
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Sat, 04 Jan 2014 06:55:26 +0000 
 Authorization: AWS C6630CD15B645CB8A3BA:iWz49B3sO2HTFlcsKdEsSULl5GI=
```

## Sample Response<a name="section35869679"></a>

```
HTTP/1.1 204 No Content 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001435C08F1018EDD 
 x-amz-id-2: QeEqZzxKPinUt9LmE9sFGcR+5xCpm2HoqFCqFFuFAB9Y84NcX6/MjhZqpN0+cE2P 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc  
 Date: Sat, 04 Jan 2014 06:55:26 GMT
```

