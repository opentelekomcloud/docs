# GET Bucket Object versions<a name="EN-US_TOPIC_0125560273"></a>

After being granted the  **READ**  permission for a bucket, you can use this operation to obtain the list of objects in this bucket.

If you specify only the bucket name in the request \(**GET /BucketName**\), OBS returns descriptions of all objects \(a maximum of 1000 objects\) in the bucket.

If you specify one or more parameters among **prefix**, **marker**, **max-keys**, **delimiter**, and **version-id-marker**, OBS returns a list of objects in alphabetic order as specified. [Table 1](#table5679749)  describes the request parameters.

## Request Syntax<a name="section339142"></a>

```
GET /?versions HTTP/1.1 
User-Agent: agent
Host: bucketname.obs.example.com
Accept: */*
Date: date 
Authorization: authorization
```

## Request Parameters<a name="section3052281"></a>

You can specify parameters in this request to list desired objects \(including objects with different version IDs\) in a bucket.  [Table 1](#table5679749)  describes the parameters.

**Table  1**  Request parameters

<a name="table5679749"></a>
<table><thead align="left"><tr id="row25167955"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p25338464"><a name="p25338464"></a><a name="p25338464"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p39149685"><a name="p39149685"></a><a name="p39149685"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p17007931"><a name="p17007931"></a><a name="p17007931"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row35465177"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p54107128"><a name="p54107128"></a><a name="p54107128"></a>prefix</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p20601280"><a name="p20601280"></a><a name="p20601280"></a>Limits the response to object keys that begin with the specified prefix.</p>
<p id="p51193794"><a name="p51193794"></a><a name="p51193794"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p53056665"><a name="p53056665"></a><a name="p53056665"></a>Optional</p>
</td>
</tr>
<tr id="row7747944"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p23603737"><a name="p23603737"></a><a name="p23603737"></a>key-marker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p32854546"><a name="p32854546"></a><a name="p32854546"></a>Indicates the object key to start with when listing objects in a bucket. All objects are listed in the dictionary order.</p>
<p id="p27255466"><a name="p27255466"></a><a name="p27255466"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60209123"><a name="p60209123"></a><a name="p60209123"></a>Optional</p>
</td>
</tr>
<tr id="row5011199"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3253954"><a name="p3253954"></a><a name="p3253954"></a>max-keys</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p62243693"><a name="p62243693"></a><a name="p62243693"></a>Sets the maximum number of object keys returned in the response body. All objects are listed in the dictionary order. The value ranges from 1 to 1000. If the value is not in this range, 1000 is returned by default.</p>
<p id="p23322329"><a name="p23322329"></a><a name="p23322329"></a>Type: Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10060533"><a name="p10060533"></a><a name="p10060533"></a>Optional</p>
</td>
</tr>
<tr id="row23435933"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p19262450"><a name="p19262450"></a><a name="p19262450"></a>delimiter</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p16754640"><a name="p16754640"></a><a name="p16754640"></a>Indicates a character used to group object keys. All object keys that contain the same string between the prefix and the first occurrence of the delimiter after the prefix are grouped under a single result element <strong id="b16574033"><a name="b16574033"></a><a name="b16574033"></a>CommonPrefixes</strong>.</p>
<p id="p14948574"><a name="p14948574"></a><a name="p14948574"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2874948"><a name="p2874948"></a><a name="p2874948"></a>Optional</p>
</td>
</tr>
<tr id="row25874536"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15462662"><a name="p15462662"></a><a name="p15462662"></a>version-id-marker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44516113"><a name="p44516113"></a><a name="p44516113"></a>Indicates the version ID to start with when listing objects in a bucket. All objects are listed in the dictionary order. This parameter is used together with <strong id="b65100698"><a name="b65100698"></a><a name="b65100698"></a>key-marker</strong>.</p>
<p id="p49035376"><a name="p49035376"></a><a name="p49035376"></a>If the value of <strong id="b38665203"><a name="b38665203"></a><a name="b38665203"></a>version-id-marker</strong>&nbsp;is not a version ID specified by&nbsp;<strong id="b12442508"><a name="b12442508"></a><a name="b12442508"></a>key-marker</strong>,&nbsp;<strong id="b44873708"><a name="b44873708"></a><a name="b44873708"></a>version-id-marker</strong> is invalid.</p>
<p id="p1210188"><a name="p1210188"></a><a name="p1210188"></a>Type: String</p>
<p id="p10891693"><a name="p10891693"></a><a name="p10891693"></a>Valid Value: object version ID|None</p>
<p id="p30916376"><a name="p30916376"></a><a name="p30916376"></a>Constraint: This parameter cannot be an empty string.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p21198553"><a name="p21198553"></a><a name="p21198553"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section27470533"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

If you want to obtain CORS configuration information, you must use the headers in  [Table 2](#table51117746).

**Table  2**  Request headers of CORS configuration

<a name="table51117746"></a>
<table><thead align="left"><tr id="row37659904"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p30553390"><a name="p30553390"></a><a name="p30553390"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p58905565"><a name="p58905565"></a><a name="p58905565"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6621493"><a name="p6621493"></a><a name="p6621493"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row66578909"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p24182525"><a name="p24182525"></a><a name="p24182525"></a>Origin</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12627518"><a name="p12627518"></a><a name="p12627518"></a>Indicates an origin specified by a pre-request. Generally, it is a domain name.</p>
<p id="p46538802"><a name="p46538802"></a><a name="p46538802"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11546631"><a name="p11546631"></a><a name="p11546631"></a>Mandatory</p>
</td>
</tr>
<tr id="row36810817"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p28886228"><a name="p28886228"></a><a name="p28886228"></a>Access-Control-Request-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p58083111"><a name="p58083111"></a><a name="p58083111"></a>Indicates the HTTP headers of a request. The request can use multiple HTTP headers.</p>
<p id="p52985952"><a name="p52985952"></a><a name="p52985952"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p64003702"><a name="p64003702"></a><a name="p64003702"></a>Optional</p>
</td>
</tr>
<tr id="row92185571811"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p101601356131815"><a name="p101601356131815"></a><a name="p101601356131815"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6160185661810"><a name="p6160185661810"></a><a name="p6160185661810"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p816065610189"><a name="p816065610189"></a><a name="p816065610189"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1160195691819"><a name="p1160195691819"></a><a name="p1160195691819"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section45908212"></a>

This request involves no elements.

## Response Syntax<a name="section21762404"></a>

```
HTTP/1.1 status_code 
 Server: OBS
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: id 
 Content-Type: type 
 Date: date 
 Content-Length: length 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <ListVersionsResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Name>bucket</Name> 
 <Prefix/> 
 <KeyMarker/> 
 <VersionIdMarker/> 
 <NextKeyMarker>nextKeyMarker</NextKeyMarker> 
 <NextVersionIdMarker>nextVersionIdMarker</NextVersionIdMarker> 
 <MaxKeys>maxKeys</MaxKeys> 
 <IsTruncated>boolean</IsTruncated> 
 <Version> 
 <Key>object</Key> 
 <VersionId>versionId</VersionId> 
 <IsLatest>boolean</IsLatest> 
 <LastModified>date</LastModified> 
 <ETag>String</ETag> 
 <Size>size</Size> 
 <Owner> 
 <ID>ownerID</ID> 
 <DisplayName>name</DisplayName> 
 </Owner> 
 <StorageClass>storageClass</StorageClass> 
 </Version> 
 <DeleteMarker> 
 <Key>object</Key> 
 <VersionId>versionId</VersionId> 
 <IsLatest>boolean</IsLatest> 
 <LastModified>date</LastModified> 
 <Owner> 
 <ID>ownerID</ID> 
 <DisplayName>name</DisplayName> 
 </Owner> 
 </DeleteMarker> 
 </ListVersionsResult>
```

## Response Headers<a name="section61643912"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

In addition to common headers, when CORS is configured for buckets, you can use the response headers in  [Table 3](#table28132937).

**Table  3**  Appended response headers

<a name="table28132937"></a>
<table><thead align="left"><tr id="row27788973"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p36314342"><a name="p36314342"></a><a name="p36314342"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p55780624"><a name="p55780624"></a><a name="p55780624"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row21936723"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p32044118"><a name="p32044118"></a><a name="p32044118"></a>Access-Control-Allow-Origin</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p45436737"><a name="p45436737"></a><a name="p45436737"></a>If <strong id="b6277453"><a name="b6277453"></a><a name="b6277453"></a>Origin</strong>&nbsp;in the request meets the CORS configuration requirements,&nbsp;<strong id="b56497085"><a name="b56497085"></a><a name="b56497085"></a>Origin</strong> is included in the response.</p>
<p id="p38711721"><a name="p38711721"></a><a name="p38711721"></a>Type: String</p>
</td>
</tr>
<tr id="row12861169"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p35121798"><a name="p35121798"></a><a name="p35121798"></a>Access-Control-Allow-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p26293412"><a name="p26293412"></a><a name="p26293412"></a>If <strong id="b35314117"><a name="b35314117"></a><a name="b35314117"></a>headers</strong>&nbsp;in the request meet the CORS configuration requirements,&nbsp;<strong id="b49391602"><a name="b49391602"></a><a name="b49391602"></a>headers</strong> are included in the response.</p>
<p id="p41871234"><a name="p41871234"></a><a name="p41871234"></a>Type: String</p>
</td>
</tr>
<tr id="row41296792"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p56705855"><a name="p56705855"></a><a name="p56705855"></a>Access-Control-Max-Age</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p29771534"><a name="p29771534"></a><a name="p29771534"></a>Indicates <strong id="b66617221"><a name="b66617221"></a><a name="b66617221"></a>MaxAgeSeconds</strong> in the CORS configuration of a server.</p>
<p id="p62684078"><a name="p62684078"></a><a name="p62684078"></a>Type: Integer</p>
</td>
</tr>
<tr id="row27285796"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p62665856"><a name="p62665856"></a><a name="p62665856"></a>Access-Control-Allow-Methods</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p42769536"><a name="p42769536"></a><a name="p42769536"></a>If <strong id="b49381505"><a name="b49381505"></a><a name="b49381505"></a>Access-Control-Request-Method</strong> in the request meets the CORS configuration requirements, methods in the rule are included in the response.</p>
<p id="p41780364"><a name="p41780364"></a><a name="p41780364"></a>Type: String</p>
<p id="p40478963"><a name="p40478963"></a><a name="p40478963"></a>Valid values: <strong id="b28766349"><a name="b28766349"></a><a name="b28766349"></a>GET</strong>,&nbsp;<strong id="b57570557"><a name="b57570557"></a><a name="b57570557"></a>PUT</strong>,&nbsp;<strong id="b48372971"><a name="b48372971"></a><a name="b48372971"></a>HEAD</strong>,&nbsp;<strong id="b32703560"><a name="b32703560"></a><a name="b32703560"></a>POST</strong>, and&nbsp;<strong id="b25896589"><a name="b25896589"></a><a name="b25896589"></a>DELETE</strong></p>
</td>
</tr>
<tr id="row31742716"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p21023167"><a name="p21023167"></a><a name="p21023167"></a>Access-Control-Expose-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p25155004"><a name="p25155004"></a><a name="p25155004"></a>Indicates <strong id="b6654113519582"><a name="b6654113519582"></a><a name="b6654113519582"></a>ExposeHeader</strong> in the CORS configuration of a server.</p>
<p id="p24289433"><a name="p24289433"></a><a name="p24289433"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section17924300"></a>

This response contains elements to specify the objects \(including objects with multiple version IDs\) in a bucket.  [Table 4](#table51869847)  describes the elements.

**Table  4**  Response elements

<a name="table51869847"></a>
<table><thead align="left"><tr id="row60306259"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p52968826"><a name="p52968826"></a><a name="p52968826"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p62616542"><a name="p62616542"></a><a name="p62616542"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row38775142"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p53778811"><a name="p53778811"></a><a name="p53778811"></a>ListVersionsResult</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p61116420"><a name="p61116420"></a><a name="p61116420"></a>Indicates the container for the list of objects (including objects with multiple version IDs).</p>
<p id="p13176872"><a name="p13176872"></a><a name="p13176872"></a>Type: Container</p>
</td>
</tr>
<tr id="row51482986"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p9372308"><a name="p9372308"></a><a name="p9372308"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p20959466"><a name="p20959466"></a><a name="p20959466"></a>Indicates the bucket name.</p>
<p id="p54417474"><a name="p54417474"></a><a name="p54417474"></a>Type: String</p>
<p id="p19995222"><a name="p19995222"></a><a name="p19995222"></a>Ancestor: ListVersionsResult</p>
</td>
</tr>
<tr id="row45739270"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p13893419"><a name="p13893419"></a><a name="p13893419"></a>Prefix</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p51625177"><a name="p51625177"></a><a name="p51625177"></a>Indicates the prefix of an object key. Only objects whose keys have this prefix are listed.</p>
<p id="p61973410"><a name="p61973410"></a><a name="p61973410"></a>Type: String</p>
<p id="p20889783"><a name="p20889783"></a><a name="p20889783"></a>Ancestor: ListVersionsResult</p>
</td>
</tr>
<tr id="row53790319"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p62048601"><a name="p62048601"></a><a name="p62048601"></a>KeyMarker</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p59880775"><a name="p59880775"></a><a name="p59880775"></a>Indicates the object key to start with when listing objects.</p>
<p id="p2056067"><a name="p2056067"></a><a name="p2056067"></a>Type: String</p>
<p id="p18504610"><a name="p18504610"></a><a name="p18504610"></a>Ancestor: ListVersionsResult</p>
</td>
</tr>
<tr id="row32323763"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p979164"><a name="p979164"></a><a name="p979164"></a>VersionIdMarker</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p12203429"><a name="p12203429"></a><a name="p12203429"></a>Indicates the object version ID to start with when listing objects.</p>
<p id="p42721997"><a name="p42721997"></a><a name="p42721997"></a>Type: String</p>
<p id="p48953654"><a name="p48953654"></a><a name="p48953654"></a>Ancestor: ListVersionsResult</p>
</td>
</tr>
<tr id="row37929705"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p52407290"><a name="p52407290"></a><a name="p52407290"></a>NextKeyMarker</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p17132136"><a name="p17132136"></a><a name="p17132136"></a>Indicates the key marker for the last returned object in the list. <strong id="b19971501"><a name="b19971501"></a><a name="b19971501"></a>NextKeyMarker</strong>&nbsp;is returned when not all the objects are listed. You can set the&nbsp;<strong id="b45525786"><a name="b45525786"></a><a name="b45525786"></a>KeyMarker</strong> value to list the remaining objects in follow-up requests.</p>
<p id="p7078897"><a name="p7078897"></a><a name="p7078897"></a>Type: String</p>
<p id="p63710073"><a name="p63710073"></a><a name="p63710073"></a>Ancestor: ListVersionsResult</p>
</td>
</tr>
<tr id="row36519748"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p5309649"><a name="p5309649"></a><a name="p5309649"></a>NextVersionIdMarker</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p27428414"><a name="p27428414"></a><a name="p27428414"></a>Indicates the version ID marker for the last returned object in the list. <strong id="b45529136"><a name="b45529136"></a><a name="b45529136"></a>NextVersionIdMarker</strong>&nbsp;is returned when not all the objects are listed. You can set the&nbsp;<strong id="b7109043"><a name="b7109043"></a><a name="b7109043"></a>VersionIdMarker</strong> value to list the remaining objects in follow-up requests.</p>
<p id="p63981393"><a name="p63981393"></a><a name="p63981393"></a>Type: String</p>
<p id="p38961625"><a name="p38961625"></a><a name="p38961625"></a>Ancestor: ListVersionsResult</p>
</td>
</tr>
<tr id="row15110310"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p15975575"><a name="p15975575"></a><a name="p15975575"></a>MaxKeys</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p18953230"><a name="p18953230"></a><a name="p18953230"></a>Indicates the maximum objects returned.</p>
<p id="p36361342"><a name="p36361342"></a><a name="p36361342"></a>Type: String</p>
<p id="p58816624"><a name="p58816624"></a><a name="p58816624"></a>Ancestor: ListVersionsResult</p>
</td>
</tr>
<tr id="row59587574"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p61864166"><a name="p61864166"></a><a name="p61864166"></a>IsTruncated</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p44941559"><a name="p44941559"></a><a name="p44941559"></a>Determines whether the returned list of objects is truncated. <strong id="b1820851"><a name="b1820851"></a><a name="b1820851"></a>true</strong>&nbsp;indicates that the result is incomplete while&nbsp;<strong id="b16387664"><a name="b16387664"></a><a name="b16387664"></a>false</strong> indicates that the result is complete.</p>
<p id="p13271256"><a name="p13271256"></a><a name="p13271256"></a>Type: Boolean</p>
<p id="p52332442"><a name="p52332442"></a><a name="p52332442"></a>Ancestor: ListVersionsResult</p>
</td>
</tr>
<tr id="row1229937"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p32516071"><a name="p32516071"></a><a name="p32516071"></a>Version</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p16556065"><a name="p16556065"></a><a name="p16556065"></a>Indicates the container for version information.</p>
<p id="p14786859"><a name="p14786859"></a><a name="p14786859"></a>Type: Container</p>
<p id="p65972871"><a name="p65972871"></a><a name="p65972871"></a>Ancestor: ListVersionsResult</p>
</td>
</tr>
<tr id="row56884935"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p44277019"><a name="p44277019"></a><a name="p44277019"></a>DeleteMarker</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p29668816"><a name="p29668816"></a><a name="p29668816"></a>Indicates the container for objects with deletion marks.</p>
<p id="p65692758"><a name="p65692758"></a><a name="p65692758"></a>Type: Container</p>
<p id="p54363918"><a name="p54363918"></a><a name="p54363918"></a>Ancestor: ListVersionsResult</p>
</td>
</tr>
<tr id="row19513215"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p37066588"><a name="p37066588"></a><a name="p37066588"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p49603670"><a name="p49603670"></a><a name="p49603670"></a>Name of an object</p>
<p id="p43779849"><a name="p43779849"></a><a name="p43779849"></a>Type: String</p>
<p id="p58474324"><a name="p58474324"></a><a name="p58474324"></a>Ancestor: ListVersionsResult.Version | ListVersionsResult.DeleteMarker</p>
</td>
</tr>
<tr id="row56506872"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p13653944"><a name="p13653944"></a><a name="p13653944"></a>VersionId</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p32227697"><a name="p32227697"></a><a name="p32227697"></a>Indicates the object version ID.</p>
<p id="p21613818"><a name="p21613818"></a><a name="p21613818"></a>Type: String</p>
<p id="p60306634"><a name="p60306634"></a><a name="p60306634"></a>Ancestor: ListVersionsResult.Version | ListVersionsResult.DeleteMarker</p>
</td>
</tr>
<tr id="row5888794"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p7230278"><a name="p7230278"></a><a name="p7230278"></a>IsLatest</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p48781671"><a name="p48781671"></a><a name="p48781671"></a>Specifies whether the object is or is not of the latest version. If the element is <strong id="b36381863"><a name="b36381863"></a><a name="b36381863"></a>true</strong>, the object is of the latest version.</p>
<p id="p59001317"><a name="p59001317"></a><a name="p59001317"></a>Type: Boolean</p>
<p id="p61249810"><a name="p61249810"></a><a name="p61249810"></a>Ancestor: ListVersionsResult.Version | ListVersionsResult.DeleteMarker</p>
</td>
</tr>
<tr id="row14377383"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p23717398"><a name="p23717398"></a><a name="p23717398"></a>LastModified</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p42061081"><a name="p42061081"></a><a name="p42061081"></a>Indicates the date and time when the last modification was made to an object.</p>
<p id="p43005414"><a name="p43005414"></a><a name="p43005414"></a>Type: Date</p>
<p id="p51504409"><a name="p51504409"></a><a name="p51504409"></a>Ancestor: ListVersionsResult.Version | ListVersionsResult.DeleteMarker</p>
</td>
</tr>
<tr id="row60886499"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p32859368"><a name="p32859368"></a><a name="p32859368"></a>ETag</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p44363166"><a name="p44363166"></a><a name="p44363166"></a>MD5 value of an object</p>
<p id="p63724179"><a name="p63724179"></a><a name="p63724179"></a>Type: String</p>
<p id="p36646700"><a name="p36646700"></a><a name="p36646700"></a>Ancestor: ListVersionsResult.Version</p>
</td>
</tr>
<tr id="row61384852"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p6117147"><a name="p6117147"></a><a name="p6117147"></a>Size</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p25726861"><a name="p25726861"></a><a name="p25726861"></a>Number of bytes of an object</p>
<p id="p30215163"><a name="p30215163"></a><a name="p30215163"></a>Type: String</p>
<p id="p3501012"><a name="p3501012"></a><a name="p3501012"></a>Ancestor: ListVersionsResult.Version</p>
</td>
</tr>
<tr id="row31509115"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p2101532"><a name="p2101532"></a><a name="p2101532"></a>Owner</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p36006405"><a name="p36006405"></a><a name="p36006405"></a>User information, including the DomainId and name</p>
<p id="p55622197"><a name="p55622197"></a><a name="p55622197"></a>Type: Container</p>
<p id="p30837727"><a name="p30837727"></a><a name="p30837727"></a>Ancestor: ListVersionsResult.Version | ListVersionsResult.DeleteMarker</p>
</td>
</tr>
<tr id="row9104094"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p66343012"><a name="p66343012"></a><a name="p66343012"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p5074862"><a name="p5074862"></a><a name="p5074862"></a>DomainId of an object owner</p>
<p id="p45673760"><a name="p45673760"></a><a name="p45673760"></a>Type: String</p>
<p id="p8410660"><a name="p8410660"></a><a name="p8410660"></a>Ancestor: ListVersionsResult.Version.Owner | ListVersionsResult.DeleteMarker.Owner</p>
</td>
</tr>
<tr id="row8587084"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p24465200"><a name="p24465200"></a><a name="p24465200"></a>DisplayName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p35524213"><a name="p35524213"></a><a name="p35524213"></a>Name of an object owner</p>
<p id="p51282467"><a name="p51282467"></a><a name="p51282467"></a>Type: String</p>
<p id="p58889027"><a name="p58889027"></a><a name="p58889027"></a>Ancestor: ListVersionsResult.Version.Owner | ListVersionsResult.Version.Owner</p>
</td>
</tr>
<tr id="row60239196"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p47536713"><a name="p47536713"></a><a name="p47536713"></a>StorageClass</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p25268563"><a name="p25268563"></a><a name="p25268563"></a>Storage type of an object</p>
<p id="p26090478"><a name="p26090478"></a><a name="p26090478"></a>Type: Enumeration</p>
<p id="p33487713"><a name="p33487713"></a><a name="p33487713"></a>Ancestor: ListVersionsResult.Version</p>
</td>
</tr>
<tr id="row32953965"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p52025533"><a name="p52025533"></a><a name="p52025533"></a>CommonPrefixes</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p53318662"><a name="p53318662"></a><a name="p53318662"></a>Grouping information. If you specify a delimiter in the request, the response contains grouping information in <strong id="b10105911"><a name="b10105911"></a><a name="b10105911"></a>CommonPrefixes</strong>.</p>
<p id="p23844335"><a name="p23844335"></a><a name="p23844335"></a>Type: Container</p>
<p id="p13272423"><a name="p13272423"></a><a name="p13272423"></a>Ancestor: ListVersionsResult</p>
</td>
</tr>
<tr id="row52342944"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p11920066"><a name="p11920066"></a><a name="p11920066"></a>Prefix</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p26001276"><a name="p26001276"></a><a name="p26001276"></a>Indicates a different prefix in the grouping information in <strong id="b32684898"><a name="b32684898"></a><a name="b32684898"></a>CommonPrefixes</strong>.</p>
<p id="p25728631"><a name="p25728631"></a><a name="p25728631"></a>Type: String</p>
<p id="p30231092"><a name="p30231092"></a><a name="p30231092"></a>Ancestor: ListVersionsResult.CommonPrefixes</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section27100977"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section57447370"></a>

```
GET /?versions HTTP/1.1 
 User-Agent: curl/7.19.0
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: Thu, 16 Jan 2014 03:31:26 +0000 
 Authorization: AWS C9590CEB8EC051BDEC9D:KfF0yCAt+LAE/AE0YTxQS7IzQ8U=
```

## Sample Response<a name="section47264284"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB7800000143991A7DEECBF4 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: 00QkPL575tIUmU8kth0zA16DlRzzdDiVDHK4OaGeujayXCfdD7phC21ZZYmVqx3W 
 Content-Type: application/xml 
 Date: Thu, 16 Jan 2014 03:31:26 GMT 
 Content-Length: 1275

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <ListVersionsResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
<Name>bucket</Name> 
 <Prefix/> 
 <KeyMarker/> 
 <VersionIdMarker/> 
 <MaxKeys>1000</MaxKeys> 
 <IsTruncated>false</IsTruncated> 
 <DeleteMarker> 
 <Key>key0</Key> 
 <VersionId>AAABQ5kabBnc0vycq3gAAABCVURTRkha</VersionId> 
 <IsLatest>true</IsLatest> 
 <LastModified>2014-01-16T03:31:22.265Z</LastModified> 
 <Owner> 
 <ID>DCD2FC9CAB78000001438EC051BD0002</ID> 
 <DisplayName>user</DisplayName> 
 </Owner> 
 </DeleteMarker> 
 <Version> 
 <Key>key0</Key> 
 <VersionId>AAABQ5kZxWTc0vycq3gAAABBVURTRkha</VersionId> 
 <IsLatest>false</IsLatest> 
 <LastModified>2014-01-16T03:30:39.575Z</LastModified> 
 <ETag>"6b0e1cad9fd2eff22004e28aa8073420"</ETag> 
 <Size>80</Size> 
 <Owner> 
 <ID>DCD2FC9CAB78000001438EC051BD0002</ID> 
 <DisplayName>user</DisplayName> 
 </Owner> 
 <StorageClass>STANDARD</StorageClass> 
 </Version> 
 <Version> 
 <Key>suspend</Key> 
 <VersionId>null</VersionId> 
 <IsLatest>true</IsLatest> 
 <LastModified>2014-01-16T03:25:58.443Z</LastModified> 
 <ETag>"a65d3be0857de44e470e0c069e4b04e3"</ETag> 
 <Size>80</Size> 
 <Owner> 
 <ID>DCD2FC9CAB78000001438EC051BD0002</ID> 
 <DisplayName>user</DisplayName> 
 </Owner> 
 <StorageClass>STANDARD</StorageClass> 
 </Version> 
 </ListVersionsResult>
```

## Sample Request \(Example of getting bucket object versions by using key-marker and version-id-marker\)<a name="section3201777"></a>

```
GET /?versions&key-marker=key0&version-id-marker=AAABQ5kabBnc0vycq3gAAABCVURTRkha HTTP/1.1 
 User-Agent: curl/7.19.0
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Thu, 16 Jan 2014 04:48:20 +0000 
 Authorization: AWS C9590CEB8EC051BDEC9D:iw+nTJEMO5KLMoE66sqzkRF3ik0=
```

## Sample Response \(Example of getting bucket object versions by using key-marker and version-id-marker\)<a name="section28815999"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001439960E2F3F18A 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: P1j6zAy1GOP9KoRUWgJt3mJGKNLlAU4dn7BfL16VXpeWCX/25cZpshp5mTbu1kyw 
 Content-Type: application/xml 
 Date: Thu, 16 Jan 2014 04:48:20 GMT 
 Content-Length: 1051 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <ListVersionsResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Name>bucket</Name> 
 <Prefix/> 
 <KeyMarker>key0</KeyMarker> 
 <VersionIdMarker>AAABQ5kabBnc0vycq3gAAABCVURTRkha</VersionIdMarker> 
 <MaxKeys>1000</MaxKeys> 
 <IsTruncated>false</IsTruncated> 
 <Version> 
 <Key>key0</Key> 
 <VersionId>AAABQ5kZxWTc0vycq3gAAABBVURTRkha</VersionId> 
 <IsLatest>false</IsLatest> 
 <LastModified>2014-01-16T03:30:39.575Z</LastModified> 
 <ETag>"6b0e1cad9fd2eff22004e28aa8073420"</ETag> 
 <Size>80</Size> 
 <Owner> 
 <ID>DCD2FC9CAB78000001438EC051BD0002</ID> 
 <DisplayName>user</DisplayName> 
 </Owner> 
 <StorageClass>STANDARD</StorageClass> 
 </Version> 
 <Version> 
 <Key>suspend</Key> 
 <VersionId>null</VersionId> 
 <IsLatest>true</IsLatest> 
 <LastModified>2014-01-16T03:25:58.443Z</LastModified> 
 <ETag>"a65d3be0857de44e470e0c069e4b04e3"</ETag> 
 <Size>80</Size> 
 <Owner> 
 <ID>DCD2FC9CAB78000001438EC051BD0002</ID> 
 <DisplayName>user</DisplayName> 
 </Owner> 
 <StorageClass>STANDARD</StorageClass> 
 </Version> 
 </ListVersionsResult>
```

