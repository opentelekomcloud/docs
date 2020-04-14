# List Buckets<a name="EN-US_TOPIC_0125560308"></a>

You can obtain the list of created buckets.

## Request Syntax<a name="section20467861"></a>

```
GET / HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section49993022"></a>

This request involves no parameters.

## Request Headers<a name="section47284016"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section22902964"></a>

This request involves no elements.

## Response Syntax<a name="section8232218"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
 x-amz-id-2: id2 
 Content-Type: type 
 Date: date 
 Content-Length: length 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
 <ListAllMyBucketsResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Owner>
 <ID>id</ID>
 <DisplayName>name</DisplayName> 
 </Owner>
 <Buckets>
 <Bucket>
 <Name>bucketName</Name> 
 <CreationDate>date</CreationDate> 
 </Bucket>
 ...
 </Buckets> 
 </ListAllMyBucketsResult>
```

## Response Headers<a name="section6981102"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section62829926"></a>

This response contains a bucket list in the XML format.  [Table 1](#table12491043)  describes the elements in this response.

**Table  1**  Response elements

<a name="table12491043"></a>
<table><thead align="left"><tr id="row58274075"><th class="cellrowborder" valign="top" width="37%" id="mcps1.2.3.1.1"><p id="p22579666"><a name="p22579666"></a><a name="p22579666"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.3.1.2"><p id="p17013620"><a name="p17013620"></a><a name="p17013620"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row35925995"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.3.1.1 "><p id="p24324511"><a name="p24324511"></a><a name="p24324511"></a>ListAllMyBucketsResult</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.3.1.2 "><p id="p24128375"><a name="p24128375"></a><a name="p24128375"></a>Indicates the bucket list.</p>
<p id="p15828788"><a name="p15828788"></a><a name="p15828788"></a>Type: XML</p>
</td>
</tr>
<tr id="row8241372"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.3.1.1 "><p id="p63571381"><a name="p63571381"></a><a name="p63571381"></a>Owner</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.3.1.2 "><p id="p49008235"><a name="p49008235"></a><a name="p49008235"></a>Indicates the user information such as the user ID and user name or domain ID and domain name.</p>
<p id="p38420932"><a name="p38420932"></a><a name="p38420932"></a>Type: XML</p>
</td>
</tr>
<tr id="row10244069"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.3.1.1 "><p id="p24463243"><a name="p24463243"></a><a name="p24463243"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.3.1.2 "><p id="p35365703"><a name="p35365703"></a><a name="p35365703"></a>Indicates the user ID or Domain ID.</p>
<p id="p49855871"><a name="p49855871"></a><a name="p49855871"></a>Type: String</p>
</td>
</tr>
<tr id="row46049662"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.3.1.1 "><p id="p39035162"><a name="p39035162"></a><a name="p39035162"></a>DisplayName</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.3.1.2 "><p id="p7731587"><a name="p7731587"></a><a name="p7731587"></a>Indicates the user name.</p>
<p id="p2475424"><a name="p2475424"></a><a name="p2475424"></a>Type: String</p>
</td>
</tr>
<tr id="row22278816"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.3.1.1 "><p id="p59753690"><a name="p59753690"></a><a name="p59753690"></a>Buckets</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.3.1.2 "><p id="p8210712"><a name="p8210712"></a><a name="p8210712"></a>Indicates the buckets that a user owns.</p>
<p id="p6787548"><a name="p6787548"></a><a name="p6787548"></a>Type: XML</p>
</td>
</tr>
<tr id="row61087939"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.3.1.1 "><p id="p49176002"><a name="p49176002"></a><a name="p49176002"></a>Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.3.1.2 "><p id="p23833214"><a name="p23833214"></a><a name="p23833214"></a>Indicates details about a bucket.</p>
<p id="p13172334"><a name="p13172334"></a><a name="p13172334"></a>Type: XML</p>
</td>
</tr>
<tr id="row51442142"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.3.1.1 "><p id="p6063946"><a name="p6063946"></a><a name="p6063946"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.3.1.2 "><p id="p21417643"><a name="p21417643"></a><a name="p21417643"></a>Indicates the bucket name.</p>
<p id="p58541067"><a name="p58541067"></a><a name="p58541067"></a>Type: String</p>
</td>
</tr>
<tr id="row57107561"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.3.1.1 "><p id="p62309739"><a name="p62309739"></a><a name="p62309739"></a>CreationDate</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.3.1.2 "><p id="p13924122"><a name="p13924122"></a><a name="p13924122"></a>Indicates the date on which a bucket was created.</p>
<p id="p58208237"><a name="p58208237"></a><a name="p58208237"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section28598426"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section17783544"></a>

```
GET / HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Sun, 26 Sep 2010 08:24:46 GMT  
 Authorization: AWS 04RZT432N80TGDF2Y2G2:ZyEGq367GyGGyItzr5egJOjaqiM= 
```

## Sample Response<a name="section25834168"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 9D3CC717E561E4D37A1285489689346 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: OUQzQ0M3MTdFNTYxRTREMzdBMTI4NTQ4OTY4OTM0NkFBQUFBQUFBYmJiYmJiYmJD 
 Content-Type: application/xml 
 Date: Sun, 26 Sep 2010 08:28:06 GMT 
 Content-Length: 485 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <ListAllMyBucketsResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Owner> 
 <ID>bcaf1ffd86f41caff1a493dc2ad8c2c281e37522a640e161ca5fb16fd081034f</ID> 
 <DisplayName>user01</DisplayName> 
 </Owner> 
 <Buckets> 
 <Bucket> 
 <Name>bucket01</Name> 
 <CreationDate>2010-09-26T03:10:23.211Z</CreationDate> 
 </Bucket> 
 <Bucket> 
 <Name>bucket02</Name> 
 <CreationDate>2010-09-20T12:05:46.187Z</CreationDate> 
 </Bucket> 
 <Bucket> 
 <Name>bucket03</Name> 
 <CreationDate>2010-09-26T08:25:13.059Z</CreationDate> 
 </Bucket> 
 </Buckets> 
 </ListAllMyBucketsResult>
```

