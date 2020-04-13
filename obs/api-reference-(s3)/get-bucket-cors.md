# GET Bucket CORS<a name="EN-US_TOPIC_0125560258"></a>

You can use this operation to obtain CORS configuration information about a specified bucket.

Only users granted the  **s3:GetBucketCORS**  permission can perform this operation. By default, only the bucket owner can perform this operation. The bucket owner can allow other users to perform this operation by granting them the permission.

## Request Syntax<a name="section45406920"></a>

```
 GET /?cors HTTP/1.1
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section6009104"></a>

This request involves no parameters.

## Request Headers<a name="section54081941"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section16975424"></a>

This request involves no elements.

## Response Syntax<a name="section42383756"></a>

```
HTTP/1.1 status_code
 Server: Server Name 
 x-amz-request-id: id 
 x-amz-id-2: id 
 x-reserved: reserved info 
 Content-Type: type 
 Date: date 
 Content-Length: lenth 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <CORSConfiguration xmlns="http://obs.example.com/doc/2015-06-30/"> 
   <CORSRule> 
     ... 
   </CORSRule> 
 </CORSConfiguration>
```

## Response Headers<a name="section45909486"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section10532193"></a>

This response contains elements to detail the CORS configuration.  [Table 1](#table34893051)  describes the elements.

**Table  1**  CORS configuration elements

<a name="table34893051"></a>
<table><thead align="left"><tr id="row38731421"><th class="cellrowborder" valign="top" width="29.110000000000003%" id="mcps1.2.3.1.1"><p id="p50237402"><a name="p50237402"></a><a name="p50237402"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="70.89%" id="mcps1.2.3.1.2"><p id="p42697780"><a name="p42697780"></a><a name="p42697780"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row35968146"><td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.3.1.1 "><p id="p27738717"><a name="p27738717"></a><a name="p27738717"></a>CORSConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="70.89%" headers="mcps1.2.3.1.2 "><p id="p32243580"><a name="p32243580"></a><a name="p32243580"></a>Indicates the <strong id="b21756767"><a name="b21756767"></a><a name="b21756767"></a>CORSRules</strong> root node. The maximum size is 64 KB.</p>
<p id="p61593176"><a name="p61593176"></a><a name="p61593176"></a>Type: Container</p>
<p id="p17467672"><a name="p17467672"></a><a name="p17467672"></a>Ancestor: None</p>
</td>
</tr>
<tr id="row22991320"><td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.3.1.1 "><p id="p50357604"><a name="p50357604"></a><a name="p50357604"></a>CORSRule</p>
</td>
<td class="cellrowborder" valign="top" width="70.89%" headers="mcps1.2.3.1.2 "><p id="p52434149"><a name="p52434149"></a><a name="p52434149"></a>Indicates a CORS rule. <strong id="b136115120613"><a name="b136115120613"></a><a name="b136115120613"></a>CORSConfiguration</strong> can contain a maximum of 100 rules.</p>
<p id="p19307715"><a name="p19307715"></a><a name="p19307715"></a>Type: Container</p>
<p id="p39551712"><a name="p39551712"></a><a name="p39551712"></a>Ancestor: <strong id="b20421093"><a name="b20421093"></a><a name="b20421093"></a>CORSConfiguration</strong></p>
</td>
</tr>
<tr id="row49572116"><td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.3.1.1 "><p id="p55918423"><a name="p55918423"></a><a name="p55918423"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="70.89%" headers="mcps1.2.3.1.2 "><p id="p33098452"><a name="p33098452"></a><a name="p33098452"></a>Indicates the unique identifier of a rule. The value can contain a maximum of 255 characters.</p>
<p id="p29450615"><a name="p29450615"></a><a name="p29450615"></a>Type: String</p>
<p id="p63728945"><a name="p63728945"></a><a name="p63728945"></a>Ancestor: Rule</p>
</td>
</tr>
<tr id="row36689595"><td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.3.1.1 "><p id="p19067212"><a name="p19067212"></a><a name="p19067212"></a>AllowedMethod</p>
</td>
<td class="cellrowborder" valign="top" width="70.89%" headers="mcps1.2.3.1.2 "><p id="p940305"><a name="p940305"></a><a name="p940305"></a>Indicates a method that is allowed by a CORS rule.</p>
<p id="p8462746"><a name="p8462746"></a><a name="p8462746"></a>Type: String</p>
<p id="p9055858"><a name="p9055858"></a><a name="p9055858"></a>Valid values: <strong id="b14393865"><a name="b14393865"></a><a name="b14393865"></a>GET</strong>,&nbsp;<strong id="b62435929"><a name="b62435929"></a><a name="b62435929"></a>PUT</strong>,&nbsp;<strong id="b25052449"><a name="b25052449"></a><a name="b25052449"></a>HEAD</strong>,&nbsp;<strong id="b24145451"><a name="b24145451"></a><a name="b24145451"></a>POST</strong>, and&nbsp;<strong id="b15982473"><a name="b15982473"></a><a name="b15982473"></a>DELETE</strong></p>
<p id="p9624530"><a name="p9624530"></a><a name="p9624530"></a>Ancestor: Rule</p>
</td>
</tr>
<tr id="row19511913"><td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.3.1.1 "><p id="p36961130"><a name="p36961130"></a><a name="p36961130"></a>AllowedOrigin</p>
</td>
<td class="cellrowborder" valign="top" width="70.89%" headers="mcps1.2.3.1.2 "><p id="p41061555"><a name="p41061555"></a><a name="p41061555"></a>Indicates an origin that is allowed by a CORS rule. It is a character string and can contain a wildcard (*). Each <strong id="b34009683"><a name="b34009683"></a><a name="b34009683"></a>AllowedOrigin</strong> can only contain one wildcard (*).</p>
<p id="p37651693"><a name="p37651693"></a><a name="p37651693"></a>Type: String</p>
<p id="p3320924"><a name="p3320924"></a><a name="p3320924"></a>Ancestor: Rule</p>
</td>
</tr>
<tr id="row29888320"><td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.3.1.1 "><p id="p5034835"><a name="p5034835"></a><a name="p5034835"></a>AllowedHeader</p>
</td>
<td class="cellrowborder" valign="top" width="70.89%" headers="mcps1.2.3.1.2 "><p id="p5168462"><a name="p5168462"></a><a name="p5168462"></a>Indicates an allowed header (<strong id="b46516162"><a name="b46516162"></a><a name="b46516162"></a>Access-Control-Request-Headers</strong>) in a CORS request. If a request contains&nbsp;<strong id="b15992282"><a name="b15992282"></a><a name="b15992282"></a>Access-Control-Request-Headers</strong>, only a CORS request that matches the configuration of&nbsp;<strong id="b9712814"><a name="b9712814"></a><a name="b9712814"></a>AllowedHeader</strong>&nbsp;is considered as a valid request. Each&nbsp;<strong id="b20306462"><a name="b20306462"></a><a name="b20306462"></a>AllowedHeader</strong> can only contain one wildcard (*).</p>
<p id="p48540437"><a name="p48540437"></a><a name="p48540437"></a>Type: String</p>
<p id="p34210755"><a name="p34210755"></a><a name="p34210755"></a>Ancestor: Rule</p>
</td>
</tr>
<tr id="row39461345"><td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.3.1.1 "><p id="p42252410"><a name="p42252410"></a><a name="p42252410"></a>MaxAgeSeconds</p>
</td>
<td class="cellrowborder" valign="top" width="70.89%" headers="mcps1.2.3.1.2 "><p id="p67002055"><a name="p67002055"></a><a name="p67002055"></a>Indicates the response time of the CORS that can be cached by a server. It is expressed in seconds.</p>
<p id="p66147589"><a name="p66147589"></a><a name="p66147589"></a>Each <strong id="b328072572"><a name="b328072572"></a><a name="b328072572"></a>CORSRule</strong> can contain only one&nbsp;<strong id="b56354492"><a name="b56354492"></a><a name="b56354492"></a>MaxAgeSeconds</strong>. It can be set to a negative value.</p>
<p id="p37428383"><a name="p37428383"></a><a name="p37428383"></a>Type: Integer</p>
<p id="p1311131"><a name="p1311131"></a><a name="p1311131"></a>Ancestor: Rule</p>
</td>
</tr>
<tr id="row11800186"><td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.3.1.1 "><p id="p16290985"><a name="p16290985"></a><a name="p16290985"></a>ExposeHeader</p>
</td>
<td class="cellrowborder" valign="top" width="70.89%" headers="mcps1.2.3.1.2 "><p id="p44501397"><a name="p44501397"></a><a name="p44501397"></a>Indicates a supplemented header in CORS responses. The header provides additional information for servers. It cannot contain spaces.</p>
<p id="p64968253"><a name="p64968253"></a><a name="p64968253"></a>Type: String</p>
<p id="p47843365"><a name="p47843365"></a><a name="p47843365"></a>Ancestor: Rule</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section27680879"></a>

For details about other error responses, see  [Table 1](error-codes.md#table30733758). In addition, this response contains one special error, as described in [Table 2](#table45602007).

**Table  2**  Special error

<a name="table45602007"></a>
<table><thead align="left"><tr id="row12405700"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p65337652"><a name="p65337652"></a><a name="p65337652"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p57858440"><a name="p57858440"></a><a name="p57858440"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p56022057"><a name="p56022057"></a><a name="p56022057"></a>HTTP Status Code</p>
</th>
</tr>
</thead>
<tbody><tr id="row41492734"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5468271"><a name="p5468271"></a><a name="p5468271"></a>NoSuchCORSConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p40276838"><a name="p40276838"></a><a name="p40276838"></a>Indicates that the CORS configuration of buckets does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p41198408"><a name="p41198408"></a><a name="p41198408"></a>404 Not Found</p>
</td>
</tr>
</tbody>
</table>

## Sample Request<a name="section24954142"></a>

```
GET /?cors HTTP/1.1 
 User-Agent: curl/7.19.0 (x86_64-suse-linux-gnu) libcurl/7.19.0 OpenSSL/0.9.8{ zlib/1.2.3 libidn/1.10 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Tue, 28 Apr 2015 09:11:35 +0000 
 Authorization: AWS D13E0C94E722DD69423C:FJt2xJ1gEnozLSdpRNTJUoy6344=
```

## Sample Response<a name="section23260691"></a>

```
HTTP/1.1 200 OK 
 Server: OBS
 x-amz-request-id: C2D7CDD617B33354C3AA227BF2077071 
 x-amz-id-2: xO3n8Q4eiJKCeAtG6U4nCSnDzhbBbMhgln8fcrOFYVGRJMc8KK/puQyr5bbSdjBU 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 Date: Tue, 28 Apr 2015 09:11:35 GMT 
 Content-Length: 556 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <CORSConfiguration xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <CORSRule> 
 <AllowedMethod>POST</AllowedMethod> 
 <AllowedMethod>GET</AllowedMethod> 
 <AllowedMethod>HEAD</AllowedMethod> 
 <AllowedMethod>PUT</AllowedMethod> 
 <AllowedMethod>DELETE</AllowedMethod> 
 <AllowedOrigin>obs.example.com</AllowedOrigin>
 <AllowedOrigin>www.example.com</AllowedOrigin> 
 <AllowedHeader>AllowedHeader_1</AllowedHeader> 
 <AllowedHeader>AllowedHeader_2</AllowedHeader> 
 <MaxAgeSeconds>100</MaxAgeSeconds> 
 <ExposeHeader>ExposeHeader_1</ExposeHeader> 
 <ExposeHeader>ExposeHeader_2</ExposeHeader> 
 </CORSRule> 
 </CORSConfiguration>
```

