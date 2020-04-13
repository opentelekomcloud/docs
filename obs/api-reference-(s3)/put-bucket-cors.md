# PUT Bucket CORS<a name="EN-US_TOPIC_0125560238"></a>

You can use this operation to enable Cross-origin resource sharing \(CORS\) for specified buckets.

CORS is a standard mechanism proposed by the World Wide Web Consortium \(W3C\) that allows cross-origin requests from servers. For standard web page requests, the scripts and contents at one website cannot interact with those at another website due to the existence of the same origin policy \(SOP\).

OBS allows buckets to store static web resources. The buckets of OBS can serve as website resources if the buckets are properly used. For details, see section  [PUT Bucket website](put-bucket-website.md). A website in OBS can respond to requests of another websites only after the CORS is properly configured.

Typical application scenarios are as follows:

-   With the support of the CORS, you can use JavaScript and HTML 5 to construct web applications and directly access the resources in OBS without the need to use proxy servers for transfer.
-   You can enable the dragging function of HTML 5 to directly upload files to OBS \(with the upload progress displayed\) or update OBS contents using web applications.
-   You can host external web pages, style sheets, and HTML 5 applications in different domains. Web fonts or pictures on OBS can be shared by multiple websites.

Only users granted the  **s3:PutBucketCORS**  permission can perform this operation. By default, only the bucket owner can perform this operation. The bucket owner can allow other users to perform this operation by granting them the permission. After the bucket CORS configuration is set, it will take effect within 2 minutes.

## Request Syntax<a name="section43823577"></a>

```
PUT /?cors HTTP/1.1 
 Host: bucketname.obs.example.com
 User-Agent: agent
 Accept: */*
 Date: date 
 Authorization: authorization 
 Content-MD5: MD5
 Content-Length: length 
 Expect: expect

 <?xml version="1.0" encoding="UTF-8"?> 
 <CORSConfiguration> 
   <CORSRule> 
     <ID>id</ID> 
     <AllowedMethod>method</AllowedMethod> 
     <AllowedOrigin>origin</AllowedOrigin> 
     <AllowedHeader>header</AllowedHeader> 
     <MaxAgeSeconds>seconds</MaxAgeSeconds> 
     <ExposeHeader>header</ExposeHeader> 
   </CORSRule> 
 </CORSConfiguration>
```

## Request Parameters<a name="section58867876"></a>

This request involves no parameters.

## Request Headers<a name="section60048837"></a>

[Table 1](#table52047770)  lists the request header.

**Table  1**  CORS request header

<a name="table52047770"></a>
<table><thead align="left"><tr id="row62702560"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p45742585"><a name="p45742585"></a><a name="p45742585"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p14161903"><a name="p14161903"></a><a name="p14161903"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6263465"><a name="p6263465"></a><a name="p6263465"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row37578639"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p23970955"><a name="p23970955"></a><a name="p23970955"></a>Content-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p62599170"><a name="p62599170"></a><a name="p62599170"></a>The MD5 digest string of the message body is calculated according to the RFC 1864 standard. That is, calculate the 128-bit binary array (the message header data encrypted with MD5) first, and then use Base 64 encoding to convert the binary data to a character string.</p>
<p id="p26521624"><a name="p26521624"></a><a name="p26521624"></a>Type: String</p>
<p id="p37368030"><a name="p37368030"></a><a name="p37368030"></a>Example: n58IG6hfM7vqI4K0vnWpog==</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6911623"><a name="p6911623"></a><a name="p6911623"></a>Mandatory</p>
</td>
</tr>
<tr id="row167671044112412"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29431645102418"><a name="p29431645102418"></a><a name="p29431645102418"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1194320452248"><a name="p1194320452248"></a><a name="p1194320452248"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p1494334516242"><a name="p1494334516242"></a><a name="p1494334516242"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p179431845122412"><a name="p179431845122412"></a><a name="p179431845122412"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section19319315217"></a>

In this request, you must configure the CORS of buckets in the request body. The configuration information is uploaded in the XML format.  [Table 2](#table65776751)  lists the CORS configuration elements.

**Table  2**  CORS configuration elements

<a name="table65776751"></a>
<table><thead align="left"><tr id="row12020482"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p34134946"><a name="p34134946"></a><a name="p34134946"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p13467214"><a name="p13467214"></a><a name="p13467214"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p17102575"><a name="p17102575"></a><a name="p17102575"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row43131373"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3980335"><a name="p3980335"></a><a name="p3980335"></a>CORSConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p53971742"><a name="p53971742"></a><a name="p53971742"></a>Indicates the <strong id="b15983633"><a name="b15983633"></a><a name="b15983633"></a>CORSRules</strong> root node. The maximum size is 64 KB.</p>
<p id="p9634977"><a name="p9634977"></a><a name="p9634977"></a>Type: Container</p>
<p id="p19605934"><a name="p19605934"></a><a name="p19605934"></a>Ancestor: None</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p44576811"><a name="p44576811"></a><a name="p44576811"></a>Mandatory</p>
</td>
</tr>
<tr id="row65646981"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15805238"><a name="p15805238"></a><a name="p15805238"></a>CORSRule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5155867"><a name="p5155867"></a><a name="p5155867"></a>Indicates a CORS rule. <strong id="b1868418351862"><a name="b1868418351862"></a><a name="b1868418351862"></a>CORSConfiguration</strong> can contain a maximum of 100 rules.</p>
<p id="p14972060"><a name="p14972060"></a><a name="p14972060"></a>Type: Container</p>
<p id="p530819"><a name="p530819"></a><a name="p530819"></a>Ancestor: <strong id="b4777379"><a name="b4777379"></a><a name="b4777379"></a>CORSConfiguration</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p51423381"><a name="p51423381"></a><a name="p51423381"></a>Mandatory</p>
</td>
</tr>
<tr id="row60157251"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p40899139"><a name="p40899139"></a><a name="p40899139"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p24495972"><a name="p24495972"></a><a name="p24495972"></a>Indicates the unique identifier of a rule. The value can contain a maximum of 255 characters.</p>
<p id="p19137160"><a name="p19137160"></a><a name="p19137160"></a>Type: String</p>
<p id="p38016717"><a name="p38016717"></a><a name="p38016717"></a>Ancestor: Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p59455271"><a name="p59455271"></a><a name="p59455271"></a>Optional</p>
</td>
</tr>
<tr id="row65335398"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p57675884"><a name="p57675884"></a><a name="p57675884"></a>AllowedMethod</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p41234998"><a name="p41234998"></a><a name="p41234998"></a>Indicates a method that is allowed by a CORS rule.</p>
<p id="p35570664"><a name="p35570664"></a><a name="p35570664"></a>Type: String</p>
<p id="p51700524"><a name="p51700524"></a><a name="p51700524"></a>Valid values: <strong id="b62651540"><a name="b62651540"></a><a name="b62651540"></a>GET</strong>,&nbsp;<strong id="b26992952"><a name="b26992952"></a><a name="b26992952"></a>PUT</strong>,&nbsp;<strong id="b41609976"><a name="b41609976"></a><a name="b41609976"></a>HEAD</strong>,&nbsp;<strong id="b38945471"><a name="b38945471"></a><a name="b38945471"></a>POST</strong>, and&nbsp;<strong id="b14964925"><a name="b14964925"></a><a name="b14964925"></a>DELETE</strong></p>
<p id="p466603"><a name="p466603"></a><a name="p466603"></a>Ancestor: Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p37794916"><a name="p37794916"></a><a name="p37794916"></a>Mandatory</p>
</td>
</tr>
<tr id="row4609929"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p37859935"><a name="p37859935"></a><a name="p37859935"></a>AllowedOrigin</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p46755894"><a name="p46755894"></a><a name="p46755894"></a>Indicates an origin that is allowed by a CORS rule. It is a character string and can contain a wildcard (*). Each <strong id="b18149865"><a name="b18149865"></a><a name="b18149865"></a>AllowedOrigin</strong> can only contain one wildcard (*).</p>
<p id="p29131061"><a name="p29131061"></a><a name="p29131061"></a>Type: String</p>
<p id="p60852964"><a name="p60852964"></a><a name="p60852964"></a>Ancestor: Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p30143027"><a name="p30143027"></a><a name="p30143027"></a>Mandatory</p>
</td>
</tr>
<tr id="row2851790"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29668407"><a name="p29668407"></a><a name="p29668407"></a>AllowedHeader</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p54330728"><a name="p54330728"></a><a name="p54330728"></a>Indicates an allowed header (<strong id="b19214507"><a name="b19214507"></a><a name="b19214507"></a>Access-Control-Request-Headers</strong>) in a CORS request. If a request contains&nbsp;<strong id="b38712842"><a name="b38712842"></a><a name="b38712842"></a>Access-Control-Request-Headers</strong>, only a CORS request that matches the configuration of&nbsp;<strong id="b12871260"><a name="b12871260"></a><a name="b12871260"></a>AllowedHeader</strong>&nbsp;is considered as a valid request. Each&nbsp;<strong id="b48732484"><a name="b48732484"></a><a name="b48732484"></a>AllowedHeader</strong> can only contain one wildcard (*).</p>
<p id="p35939178"><a name="p35939178"></a><a name="p35939178"></a>Type: String</p>
<p id="p55017151"><a name="p55017151"></a><a name="p55017151"></a>Ancestor: Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p27204259"><a name="p27204259"></a><a name="p27204259"></a>Optional</p>
</td>
</tr>
<tr id="row43511739"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p34789966"><a name="p34789966"></a><a name="p34789966"></a>MaxAgeSeconds</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p66523870"><a name="p66523870"></a><a name="p66523870"></a>Indicates the response time of the CORS that can be cached by a server. It is expressed in seconds.</p>
<p id="p61843920"><a name="p61843920"></a><a name="p61843920"></a>Each <strong id="b11901342963"><a name="b11901342963"></a><a name="b11901342963"></a>CORSRule</strong> can contain only one&nbsp;<strong id="b43301605"><a name="b43301605"></a><a name="b43301605"></a>MaxAgeSeconds</strong>. It can be set to a negative value.</p>
<p id="p54170131"><a name="p54170131"></a><a name="p54170131"></a>Type: Integer</p>
<p id="p17769131"><a name="p17769131"></a><a name="p17769131"></a>Ancestor: Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p30013513"><a name="p30013513"></a><a name="p30013513"></a>Optional</p>
</td>
</tr>
<tr id="row1686169"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2362032"><a name="p2362032"></a><a name="p2362032"></a>ExposeHeader</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p57106866"><a name="p57106866"></a><a name="p57106866"></a>Indicates a supplemented header in CORS responses. The header provides additional information for servers. It cannot contain spaces.</p>
<p id="p44199752"><a name="p44199752"></a><a name="p44199752"></a>Type: String</p>
<p id="p62253449"><a name="p62253449"></a><a name="p62253449"></a>Ancestor: Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9364637"><a name="p9364637"></a><a name="p9364637"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Response Syntax<a name="section48398424"></a>

```
HTTP/1.1 status_code
 Server: Server Name 
 x-amz-request-id: request id 
 x-amz-id-2: id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: date 
 Content-Length: 0
```

## Response Headers<a name="section32932634"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section27958252"></a>

This response involves no elements.

## Error Responses<a name="section50297679"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section51895228"></a>

```
PUT /?cors HTTP/1.1 
 User-Agent: curl/7.19.0 (x86_64-suse-linux-gnu) libcurl/7.19.0 OpenSSL/0.9.8{ zlib/1.2.3 libidn/1.10 
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: Tue, 28 Apr 2015 08:56:07 +0000 
 Authorization:  AWS D13E0C94E722DD69423C:QhHpU6Amg/2r6wIYdU3RXIx7Tlc= 
 Content-MD5: x3R4DBZgOrwsI6DwztrQCg== 
 Content-Length: 468
<CORSConfiguration> 
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

## Sample Response<a name="section64403869"></a>

```
HTTP/1.1 200 OK
 Server: OBS 
 x-amz-request-id: C2D2F581B3C5AF6C6698322AB56836F6 
 x-amz-id-2: lDGZAj4h+A33eYauDCTsPvFSHzBXEtZon6Eg1idIZl18/2/odotyqJUJ/lTh80uA 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
 Date: Tue, 28 Apr 2015 08:56:07 GMT
 Content-Length: 0
```

