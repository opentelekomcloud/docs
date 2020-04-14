# GET Bucket Notification<a name="EN-US_TOPIC_0125560442"></a>

Obtains the notification configuration of a bucket.

The  **s3:GetBucketNotification**  permission is required to perform this operation. By default, the permission is granted to the bucket owner only. However, it can be granted to other users by configuring the bucket policy.

## Request Syntax<a name="section38789260145638"></a>

```
GET /?notification HTTP/1.1 
User-Agent: agent
Host: bucketname.obs.example.com
Accept: */*
Date: date 
Authorization: authorization
```

## Request Parameters<a name="section24539173145638"></a>

This request contains no parameter.

## Request Headers<a name="section38099522145638"></a>

This request uses common headers. For details, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section58590878145638"></a>

This request contains no element.

## Response Syntax<a name="section4775281714585"></a>

```
HTTP/1.1 status_code 
x-amz-request-id: id 
x-amz-id-2: id 
x-reserved: reserved info 
Content-Type: type 
Date: date 
Content-Length: lenth 

<?xml version="1.0" encoding="UTF-8"?> 
<NotificationConfiguration xmlns="http://obs.example.com/doc/2015-06-30/">
 <TopicConfiguration>
  <Id>topic_001</Id>
  <Topic>urn:smn:example:35667523564:topic001</Topic>
  <Event>s3:ObjectCreated:*</Event>
  ....
 </TopicConfiguration> 
</NotificationConfiguration>
```

## Response Headers<a name="section4941260014585"></a>

This response uses common headers. For details, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section5143470714585"></a>

The following table describes the elements contained in this response.

**Table  1**  Response elements

<a name="table4915564514585"></a>
<table><thead align="left"><tr id="row5925512314585"><th class="cellrowborder" valign="top" width="31.31%" id="mcps1.2.3.1.1"><p id="p3493561914585"><a name="p3493561914585"></a><a name="p3493561914585"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="68.69%" id="mcps1.2.3.1.2"><p id="p1121286314585"><a name="p1121286314585"></a><a name="p1121286314585"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3582673614585"><td class="cellrowborder" valign="top" width="31.31%" headers="mcps1.2.3.1.1 "><p id="p1628454214585"><a name="p1628454214585"></a><a name="p1628454214585"></a>NotificationConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="68.69%" headers="mcps1.2.3.1.2 "><p id="p4397953614585"><a name="p4397953614585"></a><a name="p4397953614585"></a>Container for configuring the event notification function of a bucket. If this element is null, the function is disabled.</p>
<p id="p6027151114585"><a name="p6027151114585"></a><a name="p6027151114585"></a>Type: Container</p>
<p id="p557268714585"><a name="p557268714585"></a><a name="p557268714585"></a>Ancestor: None</p>
<p id="p5015418614585"><a name="p5015418614585"></a><a name="p5015418614585"></a>Children: one TopicConfiguration or TopicConfigurations</p>
</td>
</tr>
<tr id="row4873449814585"><td class="cellrowborder" valign="top" width="31.31%" headers="mcps1.2.3.1.1 "><p id="p5518027414585"><a name="p5518027414585"></a><a name="p5518027414585"></a>TopicConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="68.69%" headers="mcps1.2.3.1.2 "><p id="p4041719014585"><a name="p4041719014585"></a><a name="p4041719014585"></a>Container for configuring the event notification topic</p>
<p id="p2821039314585"><a name="p2821039314585"></a><a name="p2821039314585"></a>Type: Container</p>
<p id="p5256695114585"><a name="p5256695114585"></a><a name="p5256695114585"></a>Ancestor: NotificationConfiguration</p>
<p id="p334051114585"><a name="p334051114585"></a><a name="p334051114585"></a>Children: Id, Filter, Topic, Event or Events</p>
</td>
</tr>
<tr id="row3006460414585"><td class="cellrowborder" valign="top" width="31.31%" headers="mcps1.2.3.1.1 "><p id="p1931383714585"><a name="p1931383714585"></a><a name="p1931383714585"></a>Topic</p>
</td>
<td class="cellrowborder" valign="top" width="68.69%" headers="mcps1.2.3.1.2 "><p id="p2091699614585"><a name="p2091699614585"></a><a name="p2091699614585"></a>URN of the event notification topic. After detecting a specific event, OBS sends a message to the topic.</p>
<p id="p5403523614585"><a name="p5403523614585"></a><a name="p5403523614585"></a>Type: String</p>
<p id="p1655507814585"><a name="p1655507814585"></a><a name="p1655507814585"></a>Ancestor: TopicConfiguration</p>
</td>
</tr>
<tr id="row1477798014585"><td class="cellrowborder" valign="top" width="31.31%" headers="mcps1.2.3.1.1 "><p id="p5616570814585"><a name="p5616570814585"></a><a name="p5616570814585"></a>Id</p>
</td>
<td class="cellrowborder" valign="top" width="68.69%" headers="mcps1.2.3.1.2 "><p id="p5312850914585"><a name="p5312850914585"></a><a name="p5312850914585"></a>Unique ID of each event notification. If the user does not specify an ID, the system assigns an ID automatically.</p>
<p id="p839453714585"><a name="p839453714585"></a><a name="p839453714585"></a>Type: String</p>
<p id="p844197414585"><a name="p844197414585"></a><a name="p844197414585"></a>Ancestor: TopicConfiguration</p>
</td>
</tr>
<tr id="row886891014585"><td class="cellrowborder" valign="top" width="31.31%" headers="mcps1.2.3.1.1 "><p id="p4729309514585"><a name="p4729309514585"></a><a name="p4729309514585"></a>Filter</p>
</td>
<td class="cellrowborder" valign="top" width="68.69%" headers="mcps1.2.3.1.2 "><p id="p553548514585"><a name="p553548514585"></a><a name="p553548514585"></a>Container of S3Key used to store rules of filtering object names</p>
<p id="p4981936614585"><a name="p4981936614585"></a><a name="p4981936614585"></a>Type: Container</p>
<p id="p4572111114585"><a name="p4572111114585"></a><a name="p4572111114585"></a>Ancestor: TopicConfiguration</p>
<p id="p883681714585"><a name="p883681714585"></a><a name="p883681714585"></a>Children: S3Key</p>
</td>
</tr>
<tr id="row1242249314585"><td class="cellrowborder" valign="top" width="31.31%" headers="mcps1.2.3.1.1 "><p id="p6669791314585"><a name="p6669791314585"></a><a name="p6669791314585"></a>S3Key</p>
</td>
<td class="cellrowborder" valign="top" width="68.69%" headers="mcps1.2.3.1.2 "><p id="p3382184014585"><a name="p3382184014585"></a><a name="p3382184014585"></a>Container of S3Key used to store rules of filtering object names</p>
<p id="p3596111014585"><a name="p3596111014585"></a><a name="p3596111014585"></a>Type: Container</p>
<p id="p5521454014585"><a name="p5521454014585"></a><a name="p5521454014585"></a>Ancestor: TopicConfiguration</p>
<p id="p2716882014585"><a name="p2716882014585"></a><a name="p2716882014585"></a>Children: Name,Value</p>
</td>
</tr>
<tr id="row4319278914585"><td class="cellrowborder" valign="top" width="31.31%" headers="mcps1.2.3.1.1 "><p id="p895502614585"><a name="p895502614585"></a><a name="p895502614585"></a>FilterRule</p>
</td>
<td class="cellrowborder" valign="top" width="68.69%" headers="mcps1.2.3.1.2 "><p id="p5426852414585"><a name="p5426852414585"></a><a name="p5426852414585"></a>Container that defines key-value pairs of filtering rules</p>
<p id="p1865467114585"><a name="p1865467114585"></a><a name="p1865467114585"></a>Type: Container</p>
<p id="p3367431414585"><a name="p3367431414585"></a><a name="p3367431414585"></a>Ancestor: S3Key</p>
<p id="p3463337414585"><a name="p3463337414585"></a><a name="p3463337414585"></a>Children: Name, Value</p>
</td>
</tr>
<tr id="row4326491714585"><td class="cellrowborder" valign="top" width="31.31%" headers="mcps1.2.3.1.1 "><p id="p1479736414585"><a name="p1479736414585"></a><a name="p1479736414585"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="68.69%" headers="mcps1.2.3.1.2 "><p id="p5773582414585"><a name="p5773582414585"></a><a name="p5773582414585"></a>Specifies the prefix or suffix of object names for filtering The value contains a maximum of 1024 characters.</p>
<p id="p4986036814585"><a name="p4986036814585"></a><a name="p4986036814585"></a>Type: String</p>
<p id="p4609012814585"><a name="p4609012814585"></a><a name="p4609012814585"></a>Ancestor: FilterRule</p>
<p id="p1215796914585"><a name="p1215796914585"></a><a name="p1215796914585"></a>Legal value: prefix or suffix</p>
</td>
</tr>
<tr id="row4231286014585"><td class="cellrowborder" valign="top" width="31.31%" headers="mcps1.2.3.1.1 "><p id="p478966114585"><a name="p478966114585"></a><a name="p478966114585"></a>Value</p>
</td>
<td class="cellrowborder" valign="top" width="68.69%" headers="mcps1.2.3.1.2 "><p id="p5241829914585"><a name="p5241829914585"></a><a name="p5241829914585"></a>Specifies keywords of object names so that objects can be filtered based on the prefixes or suffixes.</p>
<p id="p200264814585"><a name="p200264814585"></a><a name="p200264814585"></a>Type: String</p>
<p id="p1802383714585"><a name="p1802383714585"></a><a name="p1802383714585"></a>Ancestor: FilterRule</p>
</td>
</tr>
<tr id="row2799681214585"><td class="cellrowborder" valign="top" width="31.31%" headers="mcps1.2.3.1.1 "><p id="p5314926314585"><a name="p5314926314585"></a><a name="p5314926314585"></a>Event</p>
</td>
<td class="cellrowborder" valign="top" width="68.69%" headers="mcps1.2.3.1.2 "><p id="p1012308414585"><a name="p1012308414585"></a><a name="p1012308414585"></a>Type of events that need to be notified</p>
<div class="note" id="note2399889514585"><a name="note2399889514585"></a><a name="note2399889514585"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="textintable" id="p1466346514585"><a name="p1466346514585"></a><a name="p1466346514585"></a>Multiple event types can be added in one TopicConfiguration configuration item.</p>
</div></div>
<p id="p6486232314585"><a name="p6486232314585"></a><a name="p6486232314585"></a>Type: String</p>
<p id="p3999350814585"><a name="p3999350814585"></a><a name="p3999350814585"></a>Ancestor: TopicConfiguration</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section1824872214585"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section1353531615134"></a>

```
GET /?notification HTTP/1.1 
User-Agent: curl/7.19.0 (x86_64-suse-linux-gnu) libcurl/7.19.0 OpenSSL/0.9.8{ zlib/1.2.3 libidn/1.10 
Host: bucketname.obs.example.com
Accept: */* 
Date: Tue, 28 Apr 2015 09:11:35 +0000 
Authorization: AWS D13E0C94E722DD69423C:FJt2xJ1gEnozLSdpRNTJUoy6344=
```

## Sample Response<a name="section224302915134"></a>

```
HTTP/1.1 200 OK 
x-amz-id-2: YgIPIfBiKa2bj0KMgUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 236A8905248E5A02 
Date: Wed, 15 Oct 2014 16:59:04 GMT 
Server: AmazonS3 

<?xml version="1.0" encoding="UTF-8"?> 
<NotificationConfiguration xmlns="http://obs.huawie.com/doc/2015-06-30/">
 <TopicConfiguration>
  <Id>id001</Id>
  <Topic>urn:smn:example:1236598854:topic1</Topic>
  <Event>s3:ObjectCreated:*</Event>
 </TopicConfiguration> 
</NotificationConfiguration>
```

