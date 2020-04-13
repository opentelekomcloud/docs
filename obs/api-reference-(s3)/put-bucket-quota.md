# PUT Bucket quota<a name="EN-US_TOPIC_0125560329"></a>

Using this operation, an active bucket owner can modify the bucket quota.

A bucket quota must be a non-negative integer expressed in bytes. The maximum allowed quota is \(2^63 - 1\) bytes. If a bucket quota is set to  **0**, the quota has no upper limit.

## Request Syntax<a name="section35542142"></a>

```
PUT /?quota HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: authorization 
 Content-Length:length 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <Quota xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <StorageQuota>value</StorageQuota> 
 </Quota>
```

## Request Parameters<a name="section51443830"></a>

This request involves no parameters.

## Request Headers<a name="section60341288"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section6200687"></a>

This request contains one element to specify the bucket quota, as described in  [Table 1](#table63485364).

**Table  1**  Request element

<a name="table63485364"></a>
<table><thead align="left"><tr id="row23836773"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p51730499"><a name="p51730499"></a><a name="p51730499"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p29420901"><a name="p29420901"></a><a name="p29420901"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p34282804"><a name="p34282804"></a><a name="p34282804"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row25443735"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p47676663"><a name="p47676663"></a><a name="p47676663"></a>StorageQuota</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p36604475"><a name="p36604475"></a><a name="p36604475"></a>Indicates a bucket quota.</p>
<p id="p61004822"><a name="p61004822"></a><a name="p61004822"></a>Type: Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p42443564"><a name="p42443564"></a><a name="p42443564"></a>Mandatory</p>
</td>
</tr>
</tbody>
</table>

## Response Syntax<a name="section40246421"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: id 
 Date: date 
 Content-Length: length
```

## Response Headers<a name="section26673471"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section38734655"></a>

This response involves no elements.

## Error Responses<a name="section13067581"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section15860434"></a>

```
PUT /?quota HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept-Encoding: gzip,deflate 
 Date: Thu, 22 Nov 2012 09:37:17 +0000 
 Authorization: AWS 08350B985315591007AD:O4jTB/FzS3gXDouwRZgz1wiE2PE= 
 Content-Length:149 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <Quota xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <StorageQuota>8</StorageQuota> 
 </Quota>
```

## Sample Response<a name="section8526181"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 90E2BA0F80EC0000013B277A80860000 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: dSLkVtVbslB8z967VtfTQmFbD3q4IzeNUBL+tlpGLMGT1FgXnlady4r+oRI/bx2y 
 Date: Thu, 22 Nov 2012 09:37:17 GMT 
 Content-Length: 0
```

