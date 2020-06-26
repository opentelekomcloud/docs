# DELETE Object<a name="EN-US_TOPIC_0125560459"></a>

You can use this operation to delete an object as long as you have  **WRITE**  permission for the object, you can delete the object. OBS returns a success response even if the object to be deleted does not exist.

## Versioning<a name="section63825615"></a>

If a bucket has versioning enabled, a deletion mark with a unique version ID is generated after an object in the bucket is deleted with no version ID specified.

If a bucket has versioning suspended, a deletion mark with version ID  **null**  is generated after an object in the bucket is deleted with no version ID specified. The object whose version is  **null**  \(if such an object exists\) is physically deleted.

You can specify  **versionId**  to delete an object of the specified version.

## Request Syntax<a name="section26250571"></a>

```
DELETE /ObjectKey HTTP/1.1
 User-Agent: agent 
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: authorization
```

## Request parameters<a name="section34928551"></a>

[Table 1](#table57902635)  describes the request parameter.

>![](/images/icon-notice.gif) **NOTICE:**   
>For deleting an object, only parameters listed in  [Table1 Request parameter](#table57902635)  are supported. If the request contains parameters that cannot be identified by OBS, the server returns the 400 error code.  

**Table  1**  Request parameter

<a name="table57902635"></a>
<table><thead align="left"><tr id="row15224096"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p25192244"><a name="p25192244"></a><a name="p25192244"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p27305877"><a name="p27305877"></a><a name="p27305877"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p64292394"><a name="p64292394"></a><a name="p64292394"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row41760635"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p27168314"><a name="p27168314"></a><a name="p27168314"></a>versionId</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p53149858"><a name="p53149858"></a><a name="p53149858"></a>Indicates the version ID of an object to be deleted.</p>
<p id="p8586676"><a name="p8586676"></a><a name="p8586676"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p24432171"><a name="p24432171"></a><a name="p24432171"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section45921510"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section10640407"></a>

This request involves no elements.

## Response Syntax<a name="section38530503"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-amz-id-2: id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: date
```

## Response Headers<a name="section11230212"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md). In addition, this response also uses optional headers, as described in  [Table 2](#table2749429).

**Table  2**  Optional response headers

<a name="table2749429"></a>
<table><thead align="left"><tr id="row18981865"><th class="cellrowborder" valign="top" width="30.97%" id="mcps1.2.3.1.1"><p id="p61136126"><a name="p61136126"></a><a name="p61136126"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="69.03%" id="mcps1.2.3.1.2"><p id="p53079196"><a name="p53079196"></a><a name="p53079196"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4447594"><td class="cellrowborder" valign="top" width="30.97%" headers="mcps1.2.3.1.1 "><p id="p24710800"><a name="p24710800"></a><a name="p24710800"></a>x-amz-delete-marker</p>
</td>
<td class="cellrowborder" valign="top" width="69.03%" headers="mcps1.2.3.1.2 "><p id="p55417783"><a name="p55417783"></a><a name="p55417783"></a>Indicates whether an object is marked as deleted. If an object is not marked as deleted, the header is not returned.</p>
<p id="p28998002"><a name="p28998002"></a><a name="p28998002"></a>Type: Boolean</p>
<p id="p59655430"><a name="p59655430"></a><a name="p59655430"></a>Valid values: true|false</p>
<p id="p27965"><a name="p27965"></a><a name="p27965"></a>Default: false</p>
</td>
</tr>
<tr id="row251686"><td class="cellrowborder" valign="top" width="30.97%" headers="mcps1.2.3.1.1 "><p id="p20386623"><a name="p20386623"></a><a name="p20386623"></a>x-amz-version-id</p>
</td>
<td class="cellrowborder" valign="top" width="69.03%" headers="mcps1.2.3.1.2 "><p id="p40703736"><a name="p40703736"></a><a name="p40703736"></a>Indicates the version ID of an object. If an object has no version ID, this header is not returned.</p>
<p id="p30789304"><a name="p30789304"></a><a name="p30789304"></a>Valid values: String</p>
<p id="p8668281"><a name="p8668281"></a><a name="p8668281"></a>Default: None</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section33963045"></a>

This response involves no elements.

## Error Responses<a name="section37231957"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section2524942"></a>

```
DELETE /test HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Sat, 03 Dec 2011 08:38:16 +0000 
 Authorization: AWS BF6C09F302931425E9A7:wQ1Tp3rD7kaUCsYfPKxOIN7NoSA=
```

## Sample Response<a name="section22724481"></a>

```
HTTP/1.1 204 No Content 
 Server: OBS 
 x-amz-request-id: 001B21A61C6C000001340312E226528D 
 x-amz-id-2: MDAxQjIxQTYxQzZDMDAwMDAxMzQwMzEyRTIyNjUyOERBQUFBQUFBQWJiYmJiYmJi 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: text/xml 
 Date: Sat, 03 Dec 2011 08:38:18 GMT
```

## Sample Request \(Deleting an Object with Version ID Specified\)<a name="section28743664"></a>

```
DELETE /object?versionId=AAABQ4-YOzfc0vycq3gAAAAUVURTRkha HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Tue, 14 Jan 2014 07:12:57 +0000 
 Authorization: AWS C9590CEB8EC051BDEC9D:DxZpQ520WCv/yMgrUjBemFORuN0=
```

## Sample Response \(Deleting an Object with Version ID Specified\)<a name="section57366391"></a>

```
HTTP/1.1 204 No Content 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001438F98937AB673 
 x-amz-id-2: UOWLHKBXWfKaBEToXGU3Om6pl0/Bid6OmhzgdJJDxN40twtrmuCHY0rEtDdSX7zp 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: text/xml 
 x-amz-version-id: AAABQ4-YOzfc0vycq3gAAAAUVURTRkha 
 Date: Tue, 14 Jan 2014 07:12:57 GMT
```

## Sample Request \(Deleting an Object with a Deletion Mark from a Bucket with Versioning Enabled\)<a name="section16166070"></a>

```
DELETE /object HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Tue, 14 Jan 2014 06:16:51 +0000 
 Authorization: AWS C9590CEB8EC051BDEC9D:VlzVUv3z3WOuSyu2l8NzVsOXY0U=
```

## Sample Response \(Deleting an Object with a Deletion Mark from a Bucket with Versioning Enabled\)<a name="section11276905"></a>

```
HTTP/1.1 204 No Content 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001438F65352A9AF5 
 x-amz-id-2: CzNX/O9/H0oZRUwAk/sWgyfVDNJMMX+v9DAzArbD40AlLtZ/TCC7H73FNIo5K81I 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: text/xml 
 x-amz-delete-marker: true 
 x-amz-version-id: AAABQ49lNT_c0vycq3gAAAAOVURTRkha 
 Date: Tue, 14 Jan 2014 06:16:51 GMT
```

