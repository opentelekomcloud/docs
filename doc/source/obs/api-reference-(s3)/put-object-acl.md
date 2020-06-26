# PUT Object acl<a name="EN-US_TOPIC_0125560460"></a>

You can use this operation to modify an object ACL.

OBS allows you to control access permission for objects. By default, only an object creator can access the object. However, the creator can set an access policy \(such as a public access policy\) to grant  **READ** permission for the object to other users. For the object in SSE-KMS model, it does not take effect.

You can set an access control policy when uploading an object or send  **PUT Object acl** or **GET Object acl**  request to modify or obtain the object ACL.

## Versioning<a name="section56432055"></a>

By default, this operation modifies the ACL of an object of the latest version. You can specify  **versionId**  to modify the ACL of an object of the desired version.

## Request Syntax<a name="section4767735"></a>

```
PUT /ObjectName?acl HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: authorization 
 Content-Length: length
 Expect: expect

 <AccessControlPolicy> 
 <Owner> 
 <ID>ID</ID> 
 <DisplayName>displayname</DisplayName> 
 </Owner> 
 <AccessControlList> 
 <Grant> 
 <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">grantee</Grantee> 
 <Permission>permission</Permission> 
 </Grant> 
 </AccessControlList> 
 </AccessControlPolicy>
```

## Request Parameters<a name="section42909617"></a>

[Table 1](#table48052128)  describes the request parameter.

**Table  1**  Request parameter

<a name="table48052128"></a>
<table><thead align="left"><tr id="row53988209"><th class="cellrowborder" valign="top" width="25.47254725472547%" id="mcps1.2.4.1.1"><p id="p10968783"><a name="p10968783"></a><a name="p10968783"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="49.85498549854985%" id="mcps1.2.4.1.2"><p id="p16056197"><a name="p16056197"></a><a name="p16056197"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="24.672467246724672%" id="mcps1.2.4.1.3"><p id="p25483580"><a name="p25483580"></a><a name="p25483580"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row28025631"><td class="cellrowborder" valign="top" width="25.47254725472547%" headers="mcps1.2.4.1.1 "><p id="p55483642"><a name="p55483642"></a><a name="p55483642"></a>versionId</p>
</td>
<td class="cellrowborder" valign="top" width="49.85498549854985%" headers="mcps1.2.4.1.2 "><p id="p64989993"><a name="p64989993"></a><a name="p64989993"></a>Indicates the version ID of an object. The ACL of the object with the version ID specified by this parameter is modified.</p>
<p id="p48039028"><a name="p48039028"></a><a name="p48039028"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="24.672467246724672%" headers="mcps1.2.4.1.3 "><p id="p65956029"><a name="p65956029"></a><a name="p65956029"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section50642235"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section53126934"></a>

This request contains elements to specify the ACL.  [Table 2](#table6365150)  describes the elements.

**Table  2**  Request elements

<a name="table6365150"></a>
<table><thead align="left"><tr id="row2102614"><th class="cellrowborder" valign="top" width="25.47254725472547%" id="mcps1.2.4.1.1"><p id="p36094027"><a name="p36094027"></a><a name="p36094027"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="48.57485748574857%" id="mcps1.2.4.1.2"><p id="p37935089"><a name="p37935089"></a><a name="p37935089"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="25.95259525952595%" id="mcps1.2.4.1.3"><p id="p52843375"><a name="p52843375"></a><a name="p52843375"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row52455022"><td class="cellrowborder" valign="top" width="25.47254725472547%" headers="mcps1.2.4.1.1 "><p id="p20998422"><a name="p20998422"></a><a name="p20998422"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="48.57485748574857%" headers="mcps1.2.4.1.2 "><p id="p23150606"><a name="p23150606"></a><a name="p23150606"></a>DomainId of the user.</p>
<p id="p7028863"><a name="p7028863"></a><a name="p7028863"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.3 "><p id="p32467059"><a name="p32467059"></a><a name="p32467059"></a>Optional</p>
</td>
</tr>
<tr id="row23768079"><td class="cellrowborder" valign="top" width="25.47254725472547%" headers="mcps1.2.4.1.1 "><p id="p46166248"><a name="p46166248"></a><a name="p46166248"></a>DisplayName</p>
</td>
<td class="cellrowborder" valign="top" width="48.57485748574857%" headers="mcps1.2.4.1.2 "><p id="p48478642"><a name="p48478642"></a><a name="p48478642"></a>Indicates the user name.</p>
<p id="p33654601"><a name="p33654601"></a><a name="p33654601"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.3 "><p id="p41668159"><a name="p41668159"></a><a name="p41668159"></a>Optional</p>
</td>
</tr>
<tr id="row39469112"><td class="cellrowborder" valign="top" width="25.47254725472547%" headers="mcps1.2.4.1.1 "><p id="p42881475"><a name="p42881475"></a><a name="p42881475"></a>Permission</p>
</td>
<td class="cellrowborder" valign="top" width="48.57485748574857%" headers="mcps1.2.4.1.2 "><p id="p50847455"><a name="p50847455"></a><a name="p50847455"></a>Indicates the permission to be granted.</p>
<p id="p54973915"><a name="p54973915"></a><a name="p54973915"></a>Type: Enumeration</p>
</td>
<td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.3 "><p id="p23702098"><a name="p23702098"></a><a name="p23702098"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Response Syntax<a name="section7458393"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-amz-id-2: id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: date 
 Content-Length: length 
```

## Response Headers<a name="section16677"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

This response also uses one optional header, as described in  [Table 3](#table40821806).

**Table  3**  Optional response header

<a name="table40821806"></a>
<table><thead align="left"><tr id="row65951706"><th class="cellrowborder" valign="top" width="29.5%" id="mcps1.2.3.1.1"><p id="p40487987"><a name="p40487987"></a><a name="p40487987"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="70.5%" id="mcps1.2.3.1.2"><p id="p58301484"><a name="p58301484"></a><a name="p58301484"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24799725"><td class="cellrowborder" valign="top" width="29.5%" headers="mcps1.2.3.1.1 "><p id="p62620703"><a name="p62620703"></a><a name="p62620703"></a>x-amz-version-id</p>
</td>
<td class="cellrowborder" valign="top" width="70.5%" headers="mcps1.2.3.1.2 "><p id="p39112169"><a name="p39112169"></a><a name="p39112169"></a>Indicates the version ID of the object whose ACL is modified.</p>
<p id="p16465207"><a name="p16465207"></a><a name="p16465207"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section150098"></a>

This response involves no elements.

## Error Responses<a name="section1350890"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section52175844"></a>

```
PUT /test?acl HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: Mon, 27 Sep 2010 02:00:40 GMT 
 Authorization: AWS 04RZT432N80TGDF2Y2G2:vktmLfCDhy0XbJw2T2mhNM9PZ70=  
 Content-Length: 916 
 Expect: 100-continue

 <AccessControlPolicy> 
 <Owner> 
 <ID>bcaf1ffd86f41caff1a493dc2ad8c2c281e37522a640e161ca5fb16fd081034f</ID> 
 <DisplayName>user</DisplayName> 
 </Owner> 
 <AccessControlList> 
 <Grant> 
 <Grantee xsi:type="CanonicalUser" xmlns:xsi="http:// www.w3.org/2001/XMLSchema-instance">            <ID>bcaf1ffd86f41caff1a493dc2ad8c2c281e37522a640e161ca5fb16fd081034f</ID> 
 <DisplayName>user</DisplayName> 
 </Grantee> 
 <Permission>READ</Permission> 
 </Grant> 
 <Grant> 
 <Grantee xsi:type="CanonicalUser" xmlns:xsi="http:// www.w3.org/2001/XMLSchema-instance">            <ID>bcaf1ffd86f41caff1a493dc8c2c281e37522a640e161ca5fb16fd081034f</ID> 
 <DisplayName>user</DisplayName> 
 </Grantee> 
 <Permission>WRITE</Permission> 
 </Grant> 
 </AccessControlList> 
 </AccessControlPolicy>
```

## Sample Response<a name="section66929418"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 5FBCAEB7BB9A1AD0FF1285553243654 
 x-amz-id-2: NUZCQ0FFQjdCQjlBMUFEMEZGMTI4NTU1MzI0MzY1NEFBQUFBQUFBYmJiYmJiYmJD 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: Mon, 27 Sep 2010 02:07:23 GMT 
 Content-Length: 0
```

## Sample Request \(Setting the ACL of an Object with Version ID Specified\)<a name="section52573766"></a>

```
PUT /object?acl&versionId=AAABQ47OMnbc0vycq3gAAAANVURTRkha HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Tue, 14 Jan 2014 05:39:29 +0000 
 Authorization: AWS C9590CEB8EC051BDEC9D:PrLaB1TR7ok53Oui4jImSpWbcik= 
 Content-Length: 504 
 Expect: 100-continue

 <AccessControlPolicy xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Owner> 
 <ID>DCD2FC9CAB78000001438EC051BD0002</ID> 
 <DisplayName>user</DisplayName> 
 </Owner> 
 <AccessControlList> 
 <Grant> 
 <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"> 
 <ID>DCD2FC9CAB78000001438EC051BD0002</ID> 
 <DisplayName>user</DisplayName> 
 </Grantee> 
 <Permission>READ</Permission> 
 </Grant> 
 </AccessControlList> 
 </AccessControlPolicy>
```

## Sample Response \(Setting the ACL of an Object with Version ID Specified\)<a name="section3401846"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 5FBCAEB7BB9A1AD0FF1285553243654 
 x-amz-id-2: NUZCQ0FFQjdCQjlBMUFEMEZGMTI4NTU1MzI0MzY1NEFBQUFBQUFBYmJiYmJiYmJD 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-version-id: AAABQ47OMnbc0vycq3gAAAANVURTRkha
 Date: Mon, 27 Sep 2010 02:07:23 GMT 
 Content-Length: 0
```

