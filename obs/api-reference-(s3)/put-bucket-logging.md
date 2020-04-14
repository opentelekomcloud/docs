# PUT Bucket logging<a name="EN-US_TOPIC_0125560299"></a>

This operation is used to control access to logs. You can use this operation to grant specific users permission to view or modify bucket logs.

This PUT operation uses the  **logging** subresource to set the logging parameters of a bucket. In the current OBS version, only the bucket owner or users granted the  **s3:PutBucketLogging**  permission can view or modify the bucket logging parameters.

By default, logs are not created during bucket creation. The logs for a bucket are created after logging in enabled. To enable logging, configure the log management function in the  **LoggingEnabled** request element. You can disable logging using an empty **BucketLoggingStatus** request element. To ensure log files are delivered correctly, the log delivery group must also have **WRITE** and  **READ\_ACP**  permission for the target bucket which stores logging.

When configuring bucket log management, the owner of the source bucket can specify a target bucket to store logs. The owner of the source bucket can only deliver logs to any bucket of the owner. In the mean time, the target bucket and source bucket must reside in the same region. When uploading a log object, its storage class is set to Standard.

The traffic consumed by uploading bucket logs is not charged, but it will be reflected in the uplink traffic of the Cloud Eye service.

## Request Syntax<a name="section10337547"></a>

```
PUT /?logging HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com
 Accept: */*
 Date: date 
 Authorization: signatureValue

logging configuration
```

## Request Parameters<a name="section25929063"></a>

This request involves no parameters.

## Request Headers<a name="section32034983"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section13687784426"></a>

**Table  1**  Request elements

<a name="table3648101"></a>
<table><thead align="left"><tr id="row50821317"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p22886023"><a name="p22886023"></a><a name="p22886023"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p41828598"><a name="p41828598"></a><a name="p41828598"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p32673273"><a name="p32673273"></a><a name="p32673273"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row29289465"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p23636445"><a name="p23636445"></a><a name="p23636445"></a>BucketLoggingStatus</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p35503886"><a name="p35503886"></a><a name="p35503886"></a>Indicates the container for logging status information.</p>
<p id="p51099518"><a name="p51099518"></a><a name="p51099518"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p45420300"><a name="p45420300"></a><a name="p45420300"></a>Mandatory</p>
</td>
</tr>
<tr id="row6129524"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p26729467"><a name="p26729467"></a><a name="p26729467"></a>LoggingEnabled</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p17603181"><a name="p17603181"></a><a name="p17603181"></a>Indicates the container for logging information. This element is present when you are enabling logging (and not present when you are disabling logging). You can add specific logging information in this element.</p>
<p id="p24210907"><a name="p24210907"></a><a name="p24210907"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14926427"><a name="p14926427"></a><a name="p14926427"></a>Optional</p>
</td>
</tr>
<tr id="row120120"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9729760"><a name="p9729760"></a><a name="p9729760"></a>Grant</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p49913109"><a name="p49913109"></a><a name="p49913109"></a>Indicates the container for the grantee and the grantee's logging permission.</p>
<p id="p46564799"><a name="p46564799"></a><a name="p46564799"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13652402"><a name="p13652402"></a><a name="p13652402"></a>Optional</p>
</td>
</tr>
<tr id="row55762756"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p20489358"><a name="p20489358"></a><a name="p20489358"></a>Grantee</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p49025284"><a name="p49025284"></a><a name="p49025284"></a>Indicates the container for users granted logging permission.</p>
<p id="p38574380"><a name="p38574380"></a><a name="p38574380"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p37517072"><a name="p37517072"></a><a name="p37517072"></a>Optional</p>
</td>
</tr>
<tr id="row2109335"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p36638467"><a name="p36638467"></a><a name="p36638467"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p14925884"><a name="p14925884"></a><a name="p14925884"></a>DomainId of the grantee, Indicates the globally unique ID.</p>
<p id="p115233"><a name="p115233"></a><a name="p115233"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9333879"><a name="p9333879"></a><a name="p9333879"></a>Optional</p>
</td>
</tr>
<tr id="row16896051"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p26402881"><a name="p26402881"></a><a name="p26402881"></a>DisplayName</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p58258620"><a name="p58258620"></a><a name="p58258620"></a>Indicates the name of the grantee. This element is not globally unique but a user ID corresponds to only one name.</p>
<p id="p54565533"><a name="p54565533"></a><a name="p54565533"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p57732070"><a name="p57732070"></a><a name="p57732070"></a>Optional</p>
</td>
</tr>
<tr id="row49826583"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9421383"><a name="p9421383"></a><a name="p9421383"></a>Permission</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p24934531"><a name="p24934531"></a><a name="p24934531"></a>Indicates the logging permission granted to the grantee for a bucket. The bucket owner is automatically granted the <strong id="b1798523714"><a name="b1798523714"></a><a name="b1798523714"></a>FULL_CONTROL</strong> permission when creating the bucket. Logging permission control access to different logs.</p>
<p id="p6431156"><a name="p6431156"></a><a name="p6431156"></a>Type: String</p>
<p id="p57880412"><a name="p57880412"></a><a name="p57880412"></a>Valid Values: FULL_CONTROL | READ | WRITE</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p57801815"><a name="p57801815"></a><a name="p57801815"></a>Optional</p>
</td>
</tr>
<tr id="row50454292"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p60265875"><a name="p60265875"></a><a name="p60265875"></a>TargetBucket</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p49697702"><a name="p49697702"></a><a name="p49697702"></a>Specifies the target bucket where bucket logs are stored. You can only have your logs delivered to any bucket that you own. User groups that deliver logs to the target bucket must have the <strong id="b44626139"><a name="b44626139"></a><a name="b44626139"></a>WRITE</strong>&nbsp;and&nbsp;<strong id="b66090934"><a name="b66090934"></a><a name="b66090934"></a>READ_ACP</strong>&nbsp;permission. In OBS, logs of multiple buckets can be stored in the same target bucket. In this case, you need to use different&nbsp;<strong id="b57947496"><a name="b57947496"></a><a name="b57947496"></a>TargetPrefix</strong> to distinguish the logs.</p>
<p id="p51765418"><a name="p51765418"></a><a name="p51765418"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p32249323"><a name="p32249323"></a><a name="p32249323"></a>Mandatory</p>
</td>
</tr>
<tr id="row21808451"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p21654113"><a name="p21654113"></a><a name="p21654113"></a>TargetPrefix</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p9152768"><a name="p9152768"></a><a name="p9152768"></a>Specifies a prefix for keys of logs to be stored.</p>
<p id="p15266056"><a name="p15266056"></a><a name="p15266056"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p28590986"><a name="p28590986"></a><a name="p28590986"></a>Mandatory</p>
</td>
</tr>
<tr id="row55992288"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p39081456"><a name="p39081456"></a><a name="p39081456"></a>TargetGrants</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11481377"><a name="p11481377"></a><a name="p11481377"></a>Indicates the container for granting information.</p>
<p id="p36223533"><a name="p36223533"></a><a name="p36223533"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48425074"><a name="p48425074"></a><a name="p48425074"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Response Syntax<a name="section64403877"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: id 
 Date: date 
 Content-Length: length 
```

## Response Headers<a name="section42763981"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response elements<a name="section49331514"></a>

This response involves no elements.

## Error Responses<a name="section41330443"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Requests<a name="section57475868"></a>

Configure the ACL for the target bucket to which logs are delivered

```
PUT /?acl HTTP/1.1
User-Agent: Jakarta Commons-HttpClient/3.1
Host: bucketname.obs.example.com
Accept-Encoding: gzip,deflate
Date: Mon, 27 Sep 2010 01:37:17 GMT
Authorization: AWS 04RZT432N80TGDF2Y2G2:9uNLINAQ7IOIrD9OnCpDfY2R6nU=
Content-Length: 598
 
<AccessControlPolicy xmlns="http://obs.example.com/doc/2006-03-01/">
<Owner>
<ID>0022A1B8CD8B00000145870549B10002</ID>
<DisplayName>huangjiang112</DisplayName>
</Owner>
<AccessControlList>
<Grant>
<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
<ID>0022A1B8CD8B00000145870549B10002</ID>
<DisplayName>user</DisplayName>
</Grantee>
<Permission>FULL_CONTROL</Permission>
</Grant>
<Grant>
<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
<URI>http://acs.amazonaws.com/groups/s3/LogDelivery</URI>
</Grantee>
<Permission>FULL_CONTROL</Permission>
</Grant>
</AccessControlList>
</AccessControlPolicy>
```

Configure logging for the source bucket

```
PUT /?logging HTTP/1.1 
 User-Agent: curl/7.19.0
 Host: bucketname.obs.example.com
 Accept: */*
 Date: date 
 Authorization: signatureValue
 Content-Length: 649 

 <?xml version="1.0" encoding="UTF-8"?> 
 <BucketLoggingStatus xmlns="http://obs.example.com/doc/2006-03-01/">
 <LoggingEnabled> 
 <TargetBucket>logging.bucket1</TargetBucket> 
 <TargetPrefix>access_log</TargetPrefix> 
 <TargetGrants> 
 <Grant> 
 <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"> 
 <ID>af258a3a0a1c2cd93011f75c1e031c043f47a25048490c8742f2f942464794e0</ID> 
 <DisplayName>user</DisplayName> 
 </Grantee> 
 <Permission>FULL_CONTROL</Permission> 
 </Grant> 
 </TargetGrants> 
 </LoggingEnabled> 
 </BucketLoggingStatus>
```

## Sample Responses<a name="section47520766"></a>

Set Acl Response

```
HTTP/1.1 200 OK
x-amz-request-id: 7B6DFC9BC71DD58B061285551605709
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
x-amz-id-2: N0I2REZDOUJDNzFERDU4QjA2MTI4NTU1MTYwNTcwOUFBQUFBQUFBYmJiYmJiYmJD
Content-Type: text/xml
Date: Mon, 27 Sep 2010 01:40:03 GMT
Content-Length: 0
```

Put Logging Response

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 7B6DFC9BC71DD58B061285551605709 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: N0I2REZDOUJDNzFERDU4QjA2MTI4NTU1MTYwNTcwOUFBQUFBQUFBYmJiYmJiYmJD 
 Date: Mon, 27 Sep 2010 01:40:03 GMT 
 Content-Length: 0
```

