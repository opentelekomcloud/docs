# GET Bucket acl<a name="EN-US_TOPIC_0125560314"></a>

After being granted  **READ\_ACP**  or  **FULL\_CONTROL**  permission for a bucket, you can obtain its ACL.

## Request Syntax<a name="section14898996"></a>

```
GET /?acl HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section66982100"></a>

This request involves no parameters.

## Request Headers<a name="section65967991"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section56841015"></a>

This request involves no elements.

## Response Syntax<a name="section33178753"></a>

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

## Response Headers<a name="section30173329"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section3124510"></a>

This response contains elements to provide details about a bucket ACL.  [Table 1](#table46938871)  describes the elements.

**Table  1**  Response elements

<a name="table46938871"></a>
<table><thead align="left"><tr id="row9451173"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p27347573"><a name="p27347573"></a><a name="p27347573"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p560958"><a name="p560958"></a><a name="p560958"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row45437607"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p56567512"><a name="p56567512"></a><a name="p56567512"></a>Owner</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p18565754"><a name="p18565754"></a><a name="p18565754"></a>Indicates the bucket owner.</p>
<p id="p32874060"><a name="p32874060"></a><a name="p32874060"></a>Type: XML</p>
</td>
</tr>
<tr id="row27431092"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p7325999"><a name="p7325999"></a><a name="p7325999"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p56535059"><a name="p56535059"></a><a name="p56535059"></a>DomainId of the user.</p>
<p id="p39053483"><a name="p39053483"></a><a name="p39053483"></a>Type: String</p>
</td>
</tr>
<tr id="row15937030"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p15831091"><a name="p15831091"></a><a name="p15831091"></a>DisplayName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p7249984"><a name="p7249984"></a><a name="p7249984"></a>Indicates the user name.</p>
<p id="p65249858"><a name="p65249858"></a><a name="p65249858"></a>Type: String</p>
</td>
</tr>
<tr id="row50377813"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p54071067"><a name="p54071067"></a><a name="p54071067"></a>AccessControlList</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p17680313"><a name="p17680313"></a><a name="p17680313"></a>Indicates the ACL that records all users who have permission to access the bucket and permission granted to the users.</p>
<p id="p24905097"><a name="p24905097"></a><a name="p24905097"></a>Type: XML</p>
</td>
</tr>
<tr id="row22819288"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p36423072"><a name="p36423072"></a><a name="p36423072"></a>Grant</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p64587704"><a name="p64587704"></a><a name="p64587704"></a>Container for the grantee and its permission.</p>
<p id="p44418425"><a name="p44418425"></a><a name="p44418425"></a>Type: XML</p>
</td>
</tr>
<tr id="row64221512"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p34559993"><a name="p34559993"></a><a name="p34559993"></a>Grantee</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p47896050"><a name="p47896050"></a><a name="p47896050"></a>Container for the details about the grantee.</p>
<p id="p28411274"><a name="p28411274"></a><a name="p28411274"></a>Type: XML</p>
</td>
</tr>
<tr id="row54374876"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p42288863"><a name="p42288863"></a><a name="p42288863"></a>Permission</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p2845858"><a name="p2845858"></a><a name="p2845858"></a>Indicates the grantee's permission for a bucket.</p>
<p id="p25612723"><a name="p25612723"></a><a name="p25612723"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section28120593"></a>

No special errors are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section11432386"></a>

```
GET /?acl HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1
 Host: bucketname.obs.example.com
 Accept-Encoding: gzip,deflate 
 Date: Mon, 27 Sep 2010 01:22:05 GMT  
 Authorization: AWS 04RZT432N80TGDF2Y2G2:FAcC4bDx0izVL9lEH521v01in/Y=  
```

## Sample Response<a name="section35782611"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 7B6DFC9BC71DD58B061285550689635 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: N0I2REZDOUJDNzFERDU4QjA2MTI4NTU1MDY4OTYzNUFBQUFBQUFBYmJiYmJiYmJD 
 Content-Type: application/xml 
 Date: Mon, 27 Sep 2010 01:24:47 GMT 
 Content-Length: 560  

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <AccessControlPolicy xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Owner> 
 <ID>bcaf1ffd86f41caff1a493dc2ad8c2c281e37522a640e161ca5fb16fd081034f</ID>
 <DisplayName>apple</DisplayName> 
 </Owner> 
 <AccessControlList> 
 <Grant> 
 <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">            <ID>bcaf1ffd86f41caff1a493dc2ad881e37540e161ca5fb16fd081034f</ID> 
 <DisplayName>apple</DisplayName> 
 </Grantee> 
 <Permission>FULL_CONTROL</Permission> 
 </Grant> 
 </AccessControlList> 
 </AccessControlPolicy>
```

