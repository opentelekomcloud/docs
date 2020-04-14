# PUT Bucket acl<a name="EN-US_TOPIC_0125560468"></a>

OBS allows you to control access permission for buckets. By default, only the creator of a bucket has  **READ**  and  **WRITE**  permission for the bucket. The creator can also set other access permission. For example, the creator can set a public-read access policy to grant READ permission to other users.

You can set an access control policy when creating a bucket, and modify or obtain the bucket access control list \(ACL\) using the  **PUT Bucket acl**  and  **GET Bucket acl**  operations.

## Request Syntax<a name="section30438641"></a>

```
PUT /?acl HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Date: date 
 Authorization: authorization  
 Content-Length: length 

 <AccessControlPolicy> 
 <Owner> 
 <ID>ID</ID>
 <DisplayName>displayname</DisplayName> 
 </Owner>
 <AccessControlList>
 <Grant>
 <Grantee>grantee</Grantee> 
 <Permission>permission</Permission> 
 </Grant>
 </AccessControlList>
 </AccessControlPolicy> 
```

## Request Parameters<a name="section5512319"></a>

This request involves no parameters.

## Request Headers<a name="section49610875"></a>

You can set the ACL of a bucket to a predefined ACL, also called a canned ACL. Each canned ACL has a predefined set of grantees and permission.

Optional header  **x-amz-acl**  is used in this request to specify canned ACLs. [Table 1](#table37355450)  describes the optional header.

**Table  1**  Optional header for specifying canned ACLs

<a name="table37355450"></a>
<table><thead align="left"><tr id="row24384169"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p28960701"><a name="p28960701"></a><a name="p28960701"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p64115445"><a name="p64115445"></a><a name="p64115445"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p25968570"><a name="p25968570"></a><a name="p25968570"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row23079411"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p57493001"><a name="p57493001"></a><a name="p57493001"></a>x-amz-acl</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p26421475"><a name="p26421475"></a><a name="p26421475"></a>Indicates the canned ACL applied to a bucket.</p>
<p id="p36466685"><a name="p36466685"></a><a name="p36466685"></a>Type: String</p>
<p id="p59764713"><a name="p59764713"></a><a name="p59764713"></a>Valid values: <strong id="b14792139108"><a name="b14792139108"></a><a name="b14792139108"></a>private| public-read| public-read-write|authenticated-read|bucket-owner-read|bucket-owner-full-control|log-delivery-write</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14823725"><a name="p14823725"></a><a name="p14823725"></a>Optional</p>
</td>
</tr>
<tr id="row2241432115215"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7527144324018"><a name="p7527144324018"></a><a name="p7527144324018"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p19527124310403"><a name="p19527124310403"></a><a name="p19527124310403"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p1852713433401"><a name="p1852713433401"></a><a name="p1852713433401"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18527843164011"><a name="p18527843164011"></a><a name="p18527843164011"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section03197424278"></a>

This request uses elements to specify an ACL.  [Table 2](#table41811761)  describes the elements.

**Table  2**  Request elements

<a name="table41811761"></a>
<table><thead align="left"><tr id="row48086049"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p2655872"><a name="p2655872"></a><a name="p2655872"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p13799068"><a name="p13799068"></a><a name="p13799068"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p43982684"><a name="p43982684"></a><a name="p43982684"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row5827624"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2275561"><a name="p2275561"></a><a name="p2275561"></a>Owner</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p50102791"><a name="p50102791"></a><a name="p50102791"></a>Indicates the bucket owner. This element consists of <strong id="b48271940"><a name="b48271940"></a><a name="b48271940"></a>ID</strong>&nbsp;and&nbsp;<strong id="b31794281"><a name="b31794281"></a><a name="b31794281"></a>DisplayName</strong>.</p>
<p id="p17713080"><a name="p17713080"></a><a name="p17713080"></a>Type: XML</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p25473339"><a name="p25473339"></a><a name="p25473339"></a>Optional</p>
</td>
</tr>
<tr id="row27933467"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p48018363"><a name="p48018363"></a><a name="p48018363"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p64282175"><a name="p64282175"></a><a name="p64282175"></a>Indicates the DomainId of a grantee.</p>
<p id="p41668666"><a name="p41668666"></a><a name="p41668666"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19718800"><a name="p19718800"></a><a name="p19718800"></a>Optional</p>
</td>
</tr>
<tr id="row43251477"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13708726"><a name="p13708726"></a><a name="p13708726"></a>DisplayName</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p36665053"><a name="p36665053"></a><a name="p36665053"></a>Indicates the name of the grantee.</p>
<p id="p61550021"><a name="p61550021"></a><a name="p61550021"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19495789"><a name="p19495789"></a><a name="p19495789"></a>Optional</p>
</td>
</tr>
<tr id="row41244374"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="ole_link23"><a name="ole_link23"></a><a name="ole_link23"></a>Grant</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p21403714"><a name="p21403714"></a><a name="p21403714"></a>Container for the grantee and its permission.</p>
<p id="p58415703"><a name="p58415703"></a><a name="p58415703"></a>Type: XML</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p34051537"><a name="p34051537"></a><a name="p34051537"></a>Optional</p>
</td>
</tr>
<tr id="row38028384"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="ole_link22"><a name="ole_link22"></a><a name="ole_link22"></a>Grantee</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p60583024"><a name="p60583024"></a><a name="p60583024"></a>Container for the details about the grantee. For details, see <a href="acl.md#table49181932">Table 1</a>.</p>
<p id="p8277894"><a name="p8277894"></a><a name="p8277894"></a>Type: XML</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p66529714"><a name="p66529714"></a><a name="p66529714"></a>Optional</p>
</td>
</tr>
<tr id="row61896514"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p47561767"><a name="p47561767"></a><a name="p47561767"></a>Permission</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p27297941"><a name="p27297941"></a><a name="p27297941"></a>Indicates the permission to be granted. For details, see <a href="acl.md#table39984204">Table 2</a>.</p>
<p id="p63649587"><a name="p63649587"></a><a name="p63649587"></a>Type: Enumeration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p55342889"><a name="p55342889"></a><a name="p55342889"></a>Optional</p>
</td>
</tr>
<tr id="row28323957"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p12539171"><a name="p12539171"></a><a name="p12539171"></a>AccessControlList</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p9039934"><a name="p9039934"></a><a name="p9039934"></a>Indicates the ACL. This element consists of <strong id="b14250543"><a name="b14250543"></a><a name="b14250543"></a>Grant</strong>,&nbsp;<strong id="b61146029"><a name="b61146029"></a><a name="b61146029"></a>Grantee</strong>, and&nbsp;<strong id="b13443352"><a name="b13443352"></a><a name="b13443352"></a>Permission</strong>.</p>
<p id="p53881305"><a name="p53881305"></a><a name="p53881305"></a>Type: XML</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2309545"><a name="p2309545"></a><a name="p2309545"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Response Syntax<a name="section58709759"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: id 
 Date: date 
 Content-Length: length 
```

## Response Headers<a name="section58625791"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section57870072"></a>

This response involves no elements.

## Error Responses<a name="section51068605"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request for Setting the Bucket ACL<a name="section4238260"></a>

```
PUT /?acl HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept-Encoding: gzip,deflate 
 Date: Mon, 27 Sep 2010 01:37:17 GMT 
 Authorization: AWS 04RZT432N80TGDF2Y2G2:9uNLINAQ7IOIrD9OnCpDfY2R6nU= 
 Content-Length: 598 

 <AccessControlPolicy> 
 <Owner> 
 <ID>bcaf1ffd86f41caff1a493dc2ad8c2c2</ID> 
 <DisplayName>user</DisplayName> 
 </Owner> 
 <AccessControlList> 
 <Grant> 
 <Grantee xsi:type="CanonicalUser" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> 
 <ID>bcaf1ffd86f41caff1a493dc2ad8c2c2</ID> 
 <DisplayName>user</DisplayName> 
 </Grantee> 
 <Permission>READ</Permission> 
 </Grant> 
 </AccessControlList> 
 </AccessControlPolicy>    
```

## Sample Response for Setting the Bucket ACL<a name="section38144343"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 7B6DFC9BC71DD58B061285551605709 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: N0I2REZDOUJDNzFERDU4QjA2MTI4NTU1MTYwNTcwOUFBQUFBQUFBYmJiYmJiYmJD 
 Date: Mon, 27 Sep 2010 01:40:03 GMT 
 Content-Length: 0
```

## Sample Request for Setting the Bucket ACL Using Headers<a name="section7754771"></a>

```
PUT /?acl HTTP/1.1 
User-Agent: curl/7.19.0
Host: bucketname.obs.example.com
Accept: */* 
Date: Mon, 27 Sep 2010 01:37:17 GMT 
Authorization: AWS 04RZT432N80TGDF2Y2G2:9uNLINAQ7IOIrD9OnCpDfY2R6nU=
x-amz-acl: private 
```

## Sample Response for Setting the Bucket ACL Using Headers<a name="section2684082"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 7B6DFC9BC71DD58B061285551605709 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
 x-amz-id-2: N0I2REZDOUJDNzFERDU4QjA2MTI4NTU1MTYwNTcwOUFBQUFBQUFBYmJiYmJiYmJD 
 Content-Type: application/xml
 Date: Mon, 27 Sep 2010 01:40:03 GMT 
 Content-Length: 526
```

