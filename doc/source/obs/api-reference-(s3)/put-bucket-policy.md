# PUT Bucket policy<a name="EN-US_TOPIC_0125560316"></a>

You can use this operation to create or modify a policy on a bucket. If the bucket already has a policy, the policy will be overwritten by the one specified in this request.

Only the bucket owner or users granted the  **s3:PutBucketPolicy**  permission can create or modify the bucket policy.

## Request Syntax<a name="section17192404"></a>

```
PUT /?policy HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com
 Accept: */*
 Date: date 
 Authorization: signatureValue
 Content-Length: length 

 Policy written in JSON
```

## Request Parameters<a name="section20513908"></a>

This request involves no parameters.

## Request Headers<a name="section50407447"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section51013847"></a>

The request body is a JSON string containing bucket policies. For details about JSON elements, see  [Bucket Policy](bucket-policy.md).

## Response Syntax<a name="section15687104"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: id 
 Date: date 
```

## Response Headers<a name="section6966214"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response elements<a name="section62695926"></a>

This response involves no elements.

## Error Responses<a name="section27392427"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request: Grant OBS account permission<a name="section48331085"></a>

Account's domain ID is  **783fc6652cf246c096ea836694f71855**.

```
PUT /?policy HTTP/1.1 
 User-Agent: curl/7.19.0
 Host: bucketname.obs.example.com 
 Date: Mon, 27 Sep 2010 01:40:03 GMT 
 Accept: */* 
 Authorization: AWS UDSIAMSTUBTEST000002:1YPpMv6hAokMd/r6Ft5/6SZANDw=
 Content-Length: 223

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
 "arn:aws:iam::783fc6652cf246c096ea836694f71855:root" 
 ] 
 } 
 } 
 ] 
 }
```

## Sample Response: Grant OBS account permission<a name="section32326581"></a>

```
HTTP/1.1 204 No Content 
 Server: OBS 
 x-amz-request-id: 7B6DFC9BC71DD58B061285551605709 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: N0I2REZDOUJDNzFERDU4QjA2MTI4NTU1MTYwNTcwOUFBQUFBQUFBYmJiYmJiYmJD 
 Date: Mon, 27 Sep 2010 01:40:03 GMT 
```

## Sample Request: Grant OBS user permission<a name="section26981558165327"></a>

User ID is  **71f3901173514e6988115ea2c26d1999** and Account's domain ID is **219d520ceac84c5a98b237431a2cf4c2**.

```
PUT /?policy HTTP/1.1
User-Agent: curl/7.19.0
Host: bucketname.obs.example.com
Accept: */*
Date: Mon, 27 Sep 2010 01:40:03 GMT 
Authorization: AWS UDSIAMSTUBTEST000002:1YPpMv6hAokMd/r6Ft5/6SZANDw=
Content-Length: 256

{
"Id": "Policy1375342051335",
"Statement": [
{
"Sid": "Stmt1375240018062",
"Action": [
"s3:PutBucketLogging"
],
"Effect": "Allow",
"Resource": "arn:aws:s3:::logging.bucket3",
"Principal": {
"AWS": [
"arn:aws:iam::219d520ceac84c5a98b237431a2cf4c2:user/71f3901173514e6988115ea2c26d1999"
]
}
}
]
}
```

## Sample Response: Grant OBS user permission<a name="section8966703165327"></a>

```
HTTP/1.1 204 No Content
x-amz-request-id: 7B6DFC9BC71DD58B061285551605709
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
x-amz-id-2: N0I2REZDOUJDNzFERDU4QjA2MTI4NTU1MTYwNTcwOUFBQUFBQUFBYmJiYmJiYmJD
Date: Mon, 27 Sep 2010 01:40:03 GMT
```

## Sample Request: Deny Operations of an OBS User<a name="section18012296430"></a>

The user ID is  **useriduseriduseriduseridus004001** and the account's domain ID is **domainiddomainiddomainiddo006666**.

```
PUT /?policy HTTP/1.1 
User-Agent: curl/7.19.0
Host: testbucketpolicy.obs.example.com
Accept: */* 
Date: Mon, 27 Sep 2010 01:40:03 GMT
Authorization: AWS UDSIAMSTUBTEST000002:1YPpMv6hAokMd/r6Ft5/6SZANDw=
Content-Length: 311 
 
{
    "Statement": [
        {
            "Effect": "Deny", 
            "Action": [
                "s3:*"
            ], 
            "Resource": [
                "arn:aws:s3:::testbucketpolicy/*", 
                "arn:aws:s3:::testbucketpolicy"
            ], 
            "Principal": {
                "AWS": [
                    "arn:aws:iam::domainiddomainiddomainiddo006666:user/useriduseriduseriduseridus004001", 
                    "arn:aws:iam::domainiddomainiddomainiddo006666:root"
                ]
            }
        }
     ]
}
```

## Sample Response<a name="section582262994311"></a>

```
HTTP/1.1 204 No Content 
x-amz-request-id: A603000001604A7DFE4A4AF31E301891
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
x-amz-id-2: BKOvGmTlt6sda5X4G89PuMO4fabObGYmnpRGkaMba1LqPt0fCACEuCMllAObRK1n
Date: Mon, 27 Sep 2010 01:40:03 GMT 
```

