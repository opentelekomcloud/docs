# HEAD Bucket<a name="EN-US_TOPIC_0125560467"></a>

After being granted  **READ**  permission for a bucket, you can use this operation to query whether the bucket exists.

## Request Syntax<a name="section34833164"></a>

```
HEAD / HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section45063028"></a>

This request involves no parameters.

## Request Headers<a name="section2914074"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

If you want to obtain CORS configuration information, you must use the headers in  [Table 1](#table48864719).

**Table  1**  Request headers of CORS configuration

<a name="table48864719"></a>
<table><thead align="left"><tr id="row29527737"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p42936498"><a name="p42936498"></a><a name="p42936498"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p55304348"><a name="p55304348"></a><a name="p55304348"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p50467231"><a name="p50467231"></a><a name="p50467231"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row61313890"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p369165"><a name="p369165"></a><a name="p369165"></a>Origin</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p29902409"><a name="p29902409"></a><a name="p29902409"></a>Indicates an origin specified by a pre-request. Generally, it is a domain name.</p>
<p id="p686229"><a name="p686229"></a><a name="p686229"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p55584556"><a name="p55584556"></a><a name="p55584556"></a>Mandatory</p>
</td>
</tr>
<tr id="row30498962"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p54496880"><a name="p54496880"></a><a name="p54496880"></a>Access-Control-Request-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52171134"><a name="p52171134"></a><a name="p52171134"></a>Indicates the HTTP headers of a request. The request can use multiple HTTP headers.</p>
<p id="p66887022"><a name="p66887022"></a><a name="p66887022"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p49139720"><a name="p49139720"></a><a name="p49139720"></a>Optional</p>
</td>
</tr>
<tr id="row23410512213"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p12337965214"><a name="p12337965214"></a><a name="p12337965214"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1833717612118"><a name="p1833717612118"></a><a name="p1833717612118"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p633715612119"><a name="p633715612119"></a><a name="p633715612119"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p433710611212"><a name="p433710611212"></a><a name="p433710611212"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section26226671"></a>

This request involves no elements.

## Response Syntax<a name="section56386551"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-bucket-region: region name
 Content-Type: */*
 x-obs-version: version
 x-default-storage-class: staorage class
 x-amz-id-2: id 
 Date: date
 Content-Length: length
```

## Response Headers<a name="section37716915"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

In addition to common headers, when CORS is configured for buckets, you can use the response headers in  [Table 2](#table14722737).

**Table  2**  Appended response headers when CORS is configured for buckets

<a name="table14722737"></a>
<table><thead align="left"><tr id="row48105459"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p4228126"><a name="p4228126"></a><a name="p4228126"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p6933938"><a name="p6933938"></a><a name="p6933938"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24778069"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p60866610"><a name="p60866610"></a><a name="p60866610"></a>Access-Control-Allow-Origin</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p31248367"><a name="p31248367"></a><a name="p31248367"></a>If <strong id="b12799849"><a name="b12799849"></a><a name="b12799849"></a>Origin</strong>&nbsp;in the request meets the CORS configuration requirements,&nbsp;<strong id="b48089780"><a name="b48089780"></a><a name="b48089780"></a>Origin</strong> is included in the response.</p>
<p id="p30154842"><a name="p30154842"></a><a name="p30154842"></a>Type: String</p>
</td>
</tr>
<tr id="row2958122"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p38281336"><a name="p38281336"></a><a name="p38281336"></a>Access-Control-Allow-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p13780551"><a name="p13780551"></a><a name="p13780551"></a>If <strong id="b56916103"><a name="b56916103"></a><a name="b56916103"></a>headers</strong>&nbsp;in the request meet the CORS configuration requirements,&nbsp;<strong id="b42482879"><a name="b42482879"></a><a name="b42482879"></a>headers</strong> are included in the response.</p>
<p id="p46801593"><a name="p46801593"></a><a name="p46801593"></a>Type: String</p>
</td>
</tr>
<tr id="row18561159"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p27058887"><a name="p27058887"></a><a name="p27058887"></a>Access-Control-Max-Age</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p44286248"><a name="p44286248"></a><a name="p44286248"></a>Indicates <strong id="b63031916"><a name="b63031916"></a><a name="b63031916"></a>MaxAgeSeconds</strong> in the CORS configuration of a server.</p>
<p id="p30416337"><a name="p30416337"></a><a name="p30416337"></a>Type: Integer</p>
</td>
</tr>
<tr id="row5311585"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p27585226"><a name="p27585226"></a><a name="p27585226"></a>Access-Control-Allow-Methods</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p19810832"><a name="p19810832"></a><a name="p19810832"></a>If <strong id="b44079761"><a name="b44079761"></a><a name="b44079761"></a>Access-Control-Request-Method</strong> in the request meets the CORS configuration requirements, methods in the rule are included in the response.</p>
<p id="p61173530"><a name="p61173530"></a><a name="p61173530"></a>Type: String</p>
<p id="p13690860"><a name="p13690860"></a><a name="p13690860"></a>Valid values: <strong id="b56108880"><a name="b56108880"></a><a name="b56108880"></a>GET</strong>,&nbsp;<strong id="b35217880"><a name="b35217880"></a><a name="b35217880"></a>PUT</strong>,&nbsp;<strong id="b48525468"><a name="b48525468"></a><a name="b48525468"></a>HEAD</strong>,&nbsp;<strong id="b34076028"><a name="b34076028"></a><a name="b34076028"></a>POST</strong>, and&nbsp;<strong id="b38248803"><a name="b38248803"></a><a name="b38248803"></a>DELETE</strong></p>
</td>
</tr>
<tr id="row8694913"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p33199375"><a name="p33199375"></a><a name="p33199375"></a>Access-Control-Expose-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p4794829"><a name="p4794829"></a><a name="p4794829"></a>Indicates <strong id="b836417014599"><a name="b836417014599"></a><a name="b836417014599"></a>ExposeHeader</strong> in the CORS configuration of a server.</p>
<p id="p52836835"><a name="p52836835"></a><a name="p52836835"></a>Type: String</p>
</td>
</tr>
<tr id="row9577151519011"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1027317387279"><a name="p1027317387279"></a><a name="p1027317387279"></a>x-amz-bucket-region</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p147721719195813"><a name="p147721719195813"></a><a name="p147721719195813"></a>Indicates the region of the bucket.</p>
<p id="p57722197584"><a name="p57722197584"></a><a name="p57722197584"></a>Type: String</p>
</td>
</tr>
<tr id="row625181017236"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p5661593517236"><a name="p5661593517236"></a><a name="p5661593517236"></a>x-default-storage-class</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p2248804017236"><a name="p2248804017236"></a><a name="p2248804017236"></a>Indicates the default storage class of the current bucket. There are three storage classes: STANDARD (OBS Standard), STANDARD_IA (OBS Warm), and GLACIER (OBS Cold).</p>
<p id="p106576917236"><a name="p106576917236"></a><a name="p106576917236"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section3907923"></a>

This response involves no elements.

## Error Responses<a name="section35171311"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section34727050"></a>

```
HEAD / HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Sun, 26 Sep 2010 09:16:00 GMT  
 Authorization: AWS 04RZT432N80TGDF2Y2G2:JUtd9kkJFjbKbkP9f6T/tAxozYY= 
```

## Sample Response<a name="section44108002"></a>

```
HTTP/1.1 200 OK 
Server: OBS 
x-amz-request-id: 367CB63A2F283044981285492719060 
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
x-amz-bucket-region: R1
Content-Type: application/xml
x-obs-version: 3.0
x-default-storage-class: STANDARD 
x-amz-id-2: MzY3Q0I2M0EyRjI4MzA0NDk4MTI4NTQ5MjcxOTA2MEFBQUFBQUFBYmJiYmJiYmJD 
Date: Sun, 26 Sep 2010 09:18:36 GMT
Content-Length: 0
```

## Sample Request \(Getting Bucket Metadata and CORS Configuration when CORS is properly configured\)<a name="section3311378921371"></a>

```
HEAD / HTTP/1.1
User-Agent: curl/7.19.0 (x86_64-suse-linux-gnu) libcurl/7.19.0 OpenSSL/0.9.8{ zlib/1.2.3 libidn/1.10
Host: bucketname.obs.example.com
Accept: */*
Date: Tue, 28 Apr 2015 13:47:30 +0000
Authorization: AWS D13E0C94E722DD69423C:1UL75oi0bFRpJlgZMfvh4lUyjBs=
Origin:www.example.com
Access-Control-Request-Headers:AllowedHeader_1
```

## Sample Response \(Getting Bucket Metadata and CORS Configuration when CORS is properly configured\)<a name="section23469382251"></a>

```
HTTP/1.1 200 OK
x-amz-request-id: BC4C45F57B0DED38D006D5F8FEB738C4
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
Access-Control-Allow-Origin: www.example.com
Access-Control-Allow-Methods: POST,GET,HEAD,PUT
Access-Control-Allow-Headers: AllowedHeader_1
Access-Control-Max-Age: 100
Access-Control-Expose-Headers: ExposeHeader_1
x-amz-bucket-region: R1
Content-Type: text/xml
x-obs-version: 3.0
x-default-storage-class: STANDARD
x-amz-id-2: YkFlH3FTA2Tf/lIc2XiyuICp/EUqpVI4j1/g5hlatg75TTZdERSCYliqitChspgA
Date: Tue, 28 Apr 2015 13:47:30 GMT
Content-Length: 0
```

