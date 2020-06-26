# GET Bucket versioning<a name="EN-US_TOPIC_0125560345"></a>

The owner of a bucket can use this operation to get the versioning state of the bucket<sub>.</sub>

If versioning is not configured for a bucket, no versioning state information will be returned after this operation. For details, see  **Sample Response \(Bucket Versioning Not Configured\)**.

## Request Syntax<a name="section26289097"></a>

```
GET /?versioning HTTP/1.1 
User-Agent: agent
Host: bucketname.obs.example.com
Accept: */*
Date: date 
Authorization: authorization
```

## Request Parameters<a name="section35275281"></a>

This request involves no parameters.

## Request Headers<a name="section49042080"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section38725542"></a>

This request involves no elements.

## Response Syntax<a name="section20853488"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-amz-id-2: id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: type 
 Date: date 
 Content-Length: length 

 <VersioningConfiguration xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Status>status</Status> 
 </VersioningConfiguration>
```

## Response Headers<a name="section53463670"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response elements<a name="section11410990"></a>

This response contains elements to specify the bucket versioning state.  [Table 1](#table57299616)  describes the elements.

**Table  1**  Response elements

<a name="table57299616"></a>
<table><thead align="left"><tr id="row12098568"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p40459966"><a name="p40459966"></a><a name="p40459966"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p56031820"><a name="p56031820"></a><a name="p56031820"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p42283611"><a name="p42283611"></a><a name="p42283611"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row2420499"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p61842715"><a name="p61842715"></a><a name="p61842715"></a>VersioningConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p43203995"><a name="p43203995"></a><a name="p43203995"></a>Indicates the container for versioning state information.</p>
<p id="p53291640"><a name="p53291640"></a><a name="p53291640"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p21655584"><a name="p21655584"></a><a name="p21655584"></a>Mandatory</p>
</td>
</tr>
<tr id="row60682533"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16338175"><a name="p16338175"></a><a name="p16338175"></a>Status</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p48323826"><a name="p48323826"></a><a name="p48323826"></a>Specifies the versioning state of the bucket.</p>
<p id="p32261252"><a name="p32261252"></a><a name="p32261252"></a>Type: Enumeration</p>
<p id="p21915813"><a name="p21915813"></a><a name="p21915813"></a>Valid Values: Enabled, Suspended</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p30350400"><a name="p30350400"></a><a name="p30350400"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section35590047"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section13517902"></a>

```
GET /?versioning HTTP/1.1
User-Agent: curl/7.29.0
Host: bucketname.obs.example.com
Accept: */*
Date: Mon, 13 Jan 2014 07:41:08 +0000 
Authorization: AWS C5780CDE717D50F4CDAA:0FuFgUd3e9dqi3OeXPj1DiQMJgk=
```

## Sample Response \(Bucket Versioning Enabled\)<a name="section54552261"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001438A8C029703EB 
 x-amz-id-2: TazfhHdpZ7V0YzmLQynVfaQ2+9zaWlTiNokK3wk8+HZPW9lWWBdsz35BXWZiQ1lk 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 Date: Mon, 13 Jan 2014 09:41:08 GMT 
 Content-Length: 178 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <VersioningConfiguration xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Status>Enabled</Status> 
 </VersioningConfiguration>
```

## Sample Response \(Bucket Versioning Suspended\)<a name="section21208306"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB7800000143954C3AE7C0A0 
 x-amz-id-2: zmHdfVr7HvmASeSRQ70pbCkpuiV2shwt2V3pBGzAzue65i8HdixOtLi4ud5ZemN0 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 Date: Wed, 13 Jan 2014 09:47:17 GMT 
 Content-Length: 180 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <VersioningConfiguration xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Status>Suspended</Status> 
 </VersioningConfiguration>
```

## Sample Response \(Bucket Versioning Not Configured\)<a name="section26978383175228"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB780000014395468DB0BDB4 
 x-amz-id-2: iDh4134qyYwtV7mlUr7vhe33DSDiDs/AuGOiU8ggUaz+B1wrNVUO6grsQDDsWf7J 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 Date: Wed, 13 Jan 2014 09:40:00 GMT 
 Content-Length: 129

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <VersioningConfiguration xmlns="http://obs.example.com/doc/2015-06-30/"> 
```

