# PUT Bucket versioning<a name="EN-US_TOPIC_0125560444"></a>

You can use this operation to enable or suspend versioning for a bucket.

Versioning can be used to restore an object that is incorrectly overwritten or deleted. You can use versioning to save, query, and restore objects of different versions. Versioning allows you to easily recover data lost due to misoperations or program faults. Versioning can also be used for retaining and archiving data.

By default, versioning is disabled for a bucket.

After the versioning state is set to  **Enabled**:

-   OBS creates a unique version ID for each uploaded object. Namesake objects are not overwritten and are distinguished by their own version IDs.
-   Objects can be downloaded by version ID. By default, the latest object is downloaded if the version ID is not specified.
-   Objects can be deleted by version ID. If an object is deleted with no version ID specified, the object is only attached with a deletion mark and a unique version ID but is not physically deleted.
-   The latest objects in a bucket are returned by default after a  **GET Object**  request. You can also send a request to obtain a bucket's objects with all version IDs.
-   Except deletion marks and object metadata, storage space occupied by objects with all version IDs is billed.

After the versioning state is set to  **Suspended**:

-   Existing objects with version IDs are not affected.
-   OBS creates version ID  **null**  to an uploaded object and the object will be overwritten after a namesake one is uploaded.
-   Objects can be downloaded by version ID. By default, the latest object is downloaded if the version ID is not specified.
-   Objects can be deleted by version ID. If an object is deleted with no version ID specified, the object is only attached with a deletion mark and version ID  **null**. Objects with version ID  **null**  are physically deleted.
-   Except deletion marks and object metadata, storage space occupied by objects with all version IDs is billed.

Only the bucket owner can set the bucket versioning state.

## Request Syntax<a name="section11440597"></a>

```
PUT /?versioning HTTP/1.1 
 User-Agent: agnet
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: date 
 Authorization: authorization 
 Content-Length: length 
 Expect: expect

 <VersioningConfiguration> 
 <Status>status</Status> 
 </VersioningConfiguration>
```

## Request Parameters<a name="section35856517"></a>

This request involves no parameters.

## Request Headers<a name="section54273197"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section15363155315813"></a>

This request contains elements to configure the bucket versioning in the XML format.  [Table 1](#table62924030)  describes the elements.

**Table  1**  Elements for configuring bucket versioning

<a name="table62924030"></a>
<table><thead align="left"><tr id="row27526859"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p15083110"><a name="p15083110"></a><a name="p15083110"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p13772373"><a name="p13772373"></a><a name="p13772373"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p41820417"><a name="p41820417"></a><a name="p41820417"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row32010577"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p42719917"><a name="p42719917"></a><a name="p42719917"></a>VersioningConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p37761278"><a name="p37761278"></a><a name="p37761278"></a>Indicates the container for the versioning state configuration.</p>
<p id="p4307190"><a name="p4307190"></a><a name="p4307190"></a>Ancestor: None</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13338129"><a name="p13338129"></a><a name="p13338129"></a>Mandatory</p>
</td>
</tr>
<tr id="row52934302"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p59820093"><a name="p59820093"></a><a name="p59820093"></a>Status</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p13589360"><a name="p13589360"></a><a name="p13589360"></a>Specifies the versioning state of the bucket.</p>
<p id="ole_link9"><a name="ole_link9"></a><a name="ole_link9"></a>Type: Enumeration</p>
<p id="p26996384"><a name="p26996384"></a><a name="p26996384"></a>Ancestor: VersioningConfiguration</p>
<p id="p41640866"><a name="p41640866"></a><a name="p41640866"></a>Valid Values: Enabled, Suspended</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p17466967"><a name="p17466967"></a><a name="p17466967"></a>Mandatory</p>
</td>
</tr>
</tbody>
</table>

## Response Syntax<a name="section44303172"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-amz-id-2: id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: date  
 Content-Length: length
```

## Response Headers<a name="section63184231"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response elements<a name="section31787174"></a>

This response involves no elements.

## Error Responses<a name="section17649112"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section5291760"></a>

```
PUT /?versioning HTTP/1.1 
User-Agent: curl/7.29.0
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Mon, 13 Jan 2014 07:33:22 +0000 
 Authorization: AWS C5780CDE717D50F4CDAA:MxAazqX4BdUfCXpbNd1VpZqyDD4= 
 Content-Length: 80
 Expect: 100-continue 

 <VersioningConfiguration> 
 <Status>Enabled</Status> 
 </VersioningConfiguration>
```

## Sample Response<a name="section47625841"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001438A84E693000F 
 x-amz-id-2: iRQ+xOfSLXxasHqbPqqtDcXRKHXzrz9cNrrW4wjNum2DGHAgr359+tU6QCcwiT0y
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: Mon, 13 Jan 2014 07:33:22 GMT 
 Content-Length: 0
```

