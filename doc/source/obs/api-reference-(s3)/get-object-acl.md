# GET Object acl<a name="EN-US_TOPIC_0125560291"></a>

You can use this operation to view the ACL of an object, as long as you have  **READ\_ACP**  permission for the object.

## Versioning<a name="section9090291"></a>

By default, the ACL of the object of the latest version is obtained. If the version ID of the object is a deletion mark,  **404**  is returned. You can specify  **versionId**  to obtain the ACL of an object of the desired version.

## Request Syntax<a name="section51424131"></a>

```
GET /ObjectName?acl HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section60163996"></a>

This request uses parameters to specify the object ACL to be obtained.  [Table 1](#table22962068)  describes the parameters.

**Table  1**  Request parameter

<a name="table22962068"></a>
<table><thead align="left"><tr id="row903863"><th class="cellrowborder" valign="top" width="24.09240924092409%" id="mcps1.2.4.1.1"><p id="p6104091"><a name="p6104091"></a><a name="p6104091"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="49.164916491649166%" id="mcps1.2.4.1.2"><p id="p24669326"><a name="p24669326"></a><a name="p24669326"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="26.742674267426747%" id="mcps1.2.4.1.3"><p id="p52058427"><a name="p52058427"></a><a name="p52058427"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row55983048"><td class="cellrowborder" valign="top" width="24.09240924092409%" headers="mcps1.2.4.1.1 "><p id="p38333021"><a name="p38333021"></a><a name="p38333021"></a>acl</p>
</td>
<td class="cellrowborder" valign="top" width="49.164916491649166%" headers="mcps1.2.4.1.2 "><p id="p17967011"><a name="p17967011"></a><a name="p17967011"></a>Indicates that the object ACL to be obtained.</p>
<p id="p27485376"><a name="p27485376"></a><a name="p27485376"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="26.742674267426747%" headers="mcps1.2.4.1.3 "><p id="p11722961"><a name="p11722961"></a><a name="p11722961"></a>Mandatory</p>
</td>
</tr>
<tr id="row38397792"><td class="cellrowborder" valign="top" width="24.09240924092409%" headers="mcps1.2.4.1.1 "><p id="p23213480"><a name="p23213480"></a><a name="p23213480"></a>versionId</p>
</td>
<td class="cellrowborder" valign="top" width="49.164916491649166%" headers="mcps1.2.4.1.2 "><p id="p1243712"><a name="p1243712"></a><a name="p1243712"></a>Indicates the version ID of the specified object.</p>
<p id="p11193409"><a name="p11193409"></a><a name="p11193409"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="26.742674267426747%" headers="mcps1.2.4.1.3 "><p id="p34250965"><a name="p34250965"></a><a name="p34250965"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section4605057"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section41445513"></a>

This request involves no elements.

## Response Syntax<a name="section12994411"></a>

```
HTTP/1.1 status_code 
 Server: bucketname.obs.example.com 
 x-amz-request-id: request id 
 x-amz-id-2: id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: date 
 Content-Length: length 
 Content-Type: type 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <AccessControlPolicy xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Owner> 
 <ID>id</ID> 
 <DisplayName>name</DisplayName> 
 </Owner> 
 <AccessControlList> 
 <Grant> 
 <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"> 
 <ID>id</ID> 
 <DisplayName>name</DisplayName> 
 </Grantee> 
 <Permission>permission</Permission> 
 </Grant> 
 </AccessControlList> 
 </AccessControlPolicy>
```

## Response Headers<a name="section49840843"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

This response also uses one optional header, as described in  [Table 2](#table14642465).

**Table  2**  Optional response header

<a name="table14642465"></a>
<table><thead align="left"><tr id="row45794042"><th class="cellrowborder" valign="top" width="28.610000000000003%" id="mcps1.2.3.1.1"><p id="p18329947"><a name="p18329947"></a><a name="p18329947"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="71.39%" id="mcps1.2.3.1.2"><p id="p8330777"><a name="p8330777"></a><a name="p8330777"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3704347"><td class="cellrowborder" valign="top" width="28.610000000000003%" headers="mcps1.2.3.1.1 "><p id="p31616714"><a name="p31616714"></a><a name="p31616714"></a>x-amz-version-id</p>
</td>
<td class="cellrowborder" valign="top" width="71.39%" headers="mcps1.2.3.1.2 "><p id="p10817037"><a name="p10817037"></a><a name="p10817037"></a>Indicates the version ID of the specified object.</p>
<p id="p30244474"><a name="p30244474"></a><a name="p30244474"></a>Valid values: String</p>
<p id="p3764813"><a name="p3764813"></a><a name="p3764813"></a>Default: None</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section45914410"></a>

This response contains elements to specify the returned object ACL.  [Table 3](#table23161487)  describes the elements.

**Table  3**  Response elements

<a name="table23161487"></a>
<table><thead align="left"><tr id="row45665679"><th class="cellrowborder" valign="top" width="28.610000000000003%" id="mcps1.2.3.1.1"><p id="p7932481"><a name="p7932481"></a><a name="p7932481"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="71.39%" id="mcps1.2.3.1.2"><p id="p38551240"><a name="p38551240"></a><a name="p38551240"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row35642764"><td class="cellrowborder" valign="top" width="28.610000000000003%" headers="mcps1.2.3.1.1 "><p id="p1382772"><a name="p1382772"></a><a name="p1382772"></a>DisplayName</p>
</td>
<td class="cellrowborder" valign="top" width="71.39%" headers="mcps1.2.3.1.2 "><p id="p44895721"><a name="p44895721"></a><a name="p44895721"></a>Indicates the user name.</p>
<p id="p1408307"><a name="p1408307"></a><a name="p1408307"></a>Type: String</p>
</td>
</tr>
<tr id="row12674770"><td class="cellrowborder" valign="top" width="28.610000000000003%" headers="mcps1.2.3.1.1 "><p id="p20023448"><a name="p20023448"></a><a name="p20023448"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="71.39%" headers="mcps1.2.3.1.2 "><p id="p11286562"><a name="p11286562"></a><a name="p11286562"></a>DomainId of the user.</p>
<p id="p34470196"><a name="p34470196"></a><a name="p34470196"></a>Type: String</p>
</td>
</tr>
<tr id="row41796312"><td class="cellrowborder" valign="top" width="28.610000000000003%" headers="mcps1.2.3.1.1 "><p id="p30058148"><a name="p30058148"></a><a name="p30058148"></a>AccessControlList</p>
</td>
<td class="cellrowborder" valign="top" width="71.39%" headers="mcps1.2.3.1.2 "><p id="p18790891"><a name="p18790891"></a><a name="p18790891"></a>Indicates the ACL that records all users who have permission to access the bucket.</p>
<p id="p34900297"><a name="p34900297"></a><a name="p34900297"></a>Type: XML</p>
</td>
</tr>
<tr id="row45667223"><td class="cellrowborder" valign="top" width="28.610000000000003%" headers="mcps1.2.3.1.1 "><p id="p8057616"><a name="p8057616"></a><a name="p8057616"></a>Grant</p>
</td>
<td class="cellrowborder" valign="top" width="71.39%" headers="mcps1.2.3.1.2 "><p id="p48687165"><a name="p48687165"></a><a name="p48687165"></a>Container for the grantee and its permission.</p>
<p id="p35531307"><a name="p35531307"></a><a name="p35531307"></a>Type: XML</p>
</td>
</tr>
<tr id="row51346311"><td class="cellrowborder" valign="top" width="28.610000000000003%" headers="mcps1.2.3.1.1 "><p id="p65410517"><a name="p65410517"></a><a name="p65410517"></a>Grantee</p>
</td>
<td class="cellrowborder" valign="top" width="71.39%" headers="mcps1.2.3.1.2 "><p id="p63760528"><a name="p63760528"></a><a name="p63760528"></a>Container for the details about the grantee.</p>
<p id="p36973841"><a name="p36973841"></a><a name="p36973841"></a>Type: XML</p>
</td>
</tr>
<tr id="row64329119"><td class="cellrowborder" valign="top" width="28.610000000000003%" headers="mcps1.2.3.1.1 "><p id="p43276139"><a name="p43276139"></a><a name="p43276139"></a>Permission</p>
</td>
<td class="cellrowborder" valign="top" width="71.39%" headers="mcps1.2.3.1.2 "><p id="p15706331"><a name="p15706331"></a><a name="p15706331"></a>Indicates the grantee's permission for an object.</p>
<p id="p7139252"><a name="p7139252"></a><a name="p7139252"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section10576514"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section56611863"></a>

```
GET /test?acl HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Mon, 27 Sep 2010 01:51:25 GMT 
 Authorization:  AWS 04RZT432N80TGDF2Y2G2:pkRtbbpzetVSUoTralXIkRLWsCQ=  
```

## Sample Response<a name="section39744725"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 5FBCAEB7BB9A1AD0FF1285552415340 
 x-amz-id-2: NUZCQ0FFQjdCQjlBMUFEMEZGMTI4NTU1MjQxNTM0MEFBQUFBQUFBYmJiYmJiYmJD 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 Date: Mon, 27 Sep 2010 01:53:35 GMT 
 Content-Length: 560 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <AccessControlPolicy xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Owner> 
 <ID>bcaf1ffd86f41caff1a493dc2ad8c2c281e37522a640e161ca5fb16fd081034f</ID> 
 <DisplayName>apple</DisplayName> 
 </Owner> 
 <AccessControlList> 
 <Grant> 
 <Grantee xmlns:xsi="http:// www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">            <ID>bcaf1ffd86f41caff1a493dc2ad8c2c281e37522a640e161ca5fb16fd081034f</ID> 
 <DisplayName>apple</DisplayName> 
 </Grantee> 
 <Permission>FULL_CONTROL</Permission> 
 </Grant> 
 </AccessControlList> 
 </AccessControlPolicy>
```

## Sample Request \(Getting the ACL of an Object with Version ID Specified\)<a name="section65206156"></a>

```
GET /object?acl&versionId=AAABQ4-glIvc0vycq3gAAAAVVURTRkha HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Tue, 14 Jan 2014 07:32:21 +0000 
 Authorization: AWS C9590CEB8EC051BDEC9D:IsCyQSOY8rbyp8E6W/ftU6GFcGg= 
```

## Sample Response \(Getting the ACL of an Object with Version ID Specified\)<a name="section49984495"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001438FAA5667BFF4 
 x-amz-id-2: 5R2cHP9X7aa+ukdrBQEVgW688/0yEpB+0wgUE7J3QdBLAi9NmHAfeCudmlwgxhk4 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 x-amz-version-id: AAABQ4-glIvc0vycq3gAAAAVVURTRkha 
 Date: Tue, 14 Jan 2014 07:32:21 GMT 
 Content-Length: 494
 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
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
 <Permission>FULL_CONTROL</Permission> 
 </Grant> 
 </AccessControlList> 
 </AccessControlPolicy>
```

