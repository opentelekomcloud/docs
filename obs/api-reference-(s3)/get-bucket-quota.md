# GET Bucket quota<a name="EN-US_TOPIC_0125560383"></a>

Using this operation, an active bucket owner can obtain its quota.

A bucket quota is expressed in bytes. If the quota is set to  **0**, the quota has no upper limit.

## Request Syntax<a name="section27998217"></a>

```
GET /?quota HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section50657369"></a>

This request involves no parameters.

## Request Headers<a name="section53263142"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section9606233"></a>

This request involves no elements.

## Response Syntax<a name="section12985168"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: id 
 Content-Type: type 
 Date: date 
 Content-Length: length 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <Quota xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <StorageQuota>value</StorageQuota> 
 </Quota>
```

## Response Headers<a name="section49757651"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section45165677"></a>

This response contains elements to provide details about a bucket quota.  [Table 1](#table40100219)  describes the elements.

**Table  1**  Response elements

<a name="table40100219"></a>
<table><thead align="left"><tr id="row27660031"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p25870061"><a name="p25870061"></a><a name="p25870061"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p15100171"><a name="p15100171"></a><a name="p15100171"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15154305"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p19539192"><a name="p19539192"></a><a name="p19539192"></a>Quota</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p39170711"><a name="p39170711"></a><a name="p39170711"></a>Indicates bucket quota details. This element contains the <strong id="b16992086"><a name="b16992086"></a><a name="b16992086"></a>StorageQuota</strong> element.</p>
<p id="p18711047"><a name="p18711047"></a><a name="p18711047"></a>Type: XML</p>
</td>
</tr>
<tr id="row34181701"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p17254385"><a name="p17254385"></a><a name="p17254385"></a>StorageQuota</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p55427905"><a name="p55427905"></a><a name="p55427905"></a>Indicates the bucket quota value.</p>
<p id="p29089098"><a name="p29089098"></a><a name="p29089098"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section3837911"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section23778621"></a>

```
GET /?quota HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1
 Host: bucketname.obs.example.com
 Accept-Encoding: gzip,deflate 
 Date: Thu, 22 Nov 2012 09:37:38 +0000  
 Authorization: AWS 08350B985315591007AD:O4jTB/FzS3gXDouwRZgz1wiE2PE= 
```

## Sample Response<a name="section12681003"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 90E2BA0F80EC0000013B277AD1970001 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: ReSvzDszzWqXunSRGkNv+aIjXO56ekT48XVAOcyjIEU6zufqkoqJRO6z1VPLvDcm 
 Content-Type: application/xml 
 Date: Thu, 22 Nov 2012 09:37:38 GMT 
 Content-Length: 148 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <Quota xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <StorageQuota>8</StorageQuota> 
 </Quota>
```

