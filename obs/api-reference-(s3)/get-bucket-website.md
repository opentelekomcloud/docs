# GET Bucket website<a name="EN-US_TOPIC_0125560494"></a>

You can use this operation to get the website configuration of a bucket.

Only users granted the  **s3:GetBucketWebsite**  permission can get the bucket website configuration. By default, only the bucket owner can get the bucket website configuration. The bucket owner can allow other users to get the bucket website configuration by granting them the permission.

## Request Syntax<a name="section12563221"></a>

```
 GET /?website HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com
 Accept: */*
 Date: date 
 Authoirization: authorization
```

## Request Parameters<a name="section45960129"></a>

This request involves no parameters.

## Request Headers<a name="section10987981"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section31782970"></a>

This request involves no elements.

## Response Syntax<a name="section25229732"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-amz-id-2: id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
 Content-Type: type 
 Date: date  
 Content-Length: length     
<?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <WebsiteConfiguration xmlns="http://obs.example.com/doc/2015-06-30/"> 
   <RedirectAllRequestsTo> 
     <HostName>hostName</HostName> 
   </RedirectAllRequestsTo> 
 </WebsiteConfiguration>
```

## Response Headers<a name="section25741004"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section30342446"></a>

This response contains elements the same as those used by the  **PUT Bucket website** request. For details, see section [PUT Bucket website](put-bucket-website.md).

## Error Responses<a name="section4646565"></a>

This response contains common errors. For details, see  [Table 1](error-codes.md#table30733758). In addition, this response contains one special error, as described in [Table 1](#table19964345).

**Table  1**  Special error

<a name="table19964345"></a>
<table><thead align="left"><tr id="row14081115"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p66828554"><a name="p66828554"></a><a name="p66828554"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p44403789"><a name="p44403789"></a><a name="p44403789"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p39937165"><a name="p39937165"></a><a name="p39937165"></a>HTTP Status Code</p>
</th>
</tr>
</thead>
<tbody><tr id="row13684913"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p34736162"><a name="p34736162"></a><a name="p34736162"></a>NoSuchWebsiteConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p62165703"><a name="p62165703"></a><a name="p62165703"></a>Indicates that the website configuration does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2257160"><a name="p2257160"></a><a name="p2257160"></a>404 Not Found</p>
</td>
</tr>
</tbody>
</table>

## Sample Request<a name="section34566005"></a>

```
GET /?website HTTP/1.1
 User-Agent: curl/7.29.0
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Sat, 04 Jan 2014 06:47:16 +0000
 Authorization: AWS C6630CD15B645CB8A3BA:XrepYUF0mA/m1RPvpA0M18FdCfg=
```

## Sample Response<a name="section42658596"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001435C0176F28223 
 x-amz-id-2: 8BSYBZcQKwR5nCgMsLY86TRLwhUZpLbQTxAKIAuMJqx3OURwOMhILeVNwTrEQWyc 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml
 Date: Sat, 04 Jan 2014 06:47:16 GMT 
 Content-Length: 230 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <WebsiteConfiguration xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <RedirectAllRequestsTo> 
 <HostName>www.example.com</HostName>
 </RedirectAllRequestsTo> 
 </WebsiteConfiguration>
```

