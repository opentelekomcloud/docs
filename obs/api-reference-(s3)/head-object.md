# HEAD Object<a name="EN-US_TOPIC_0125560379"></a>

You can use this operation to view an object's metadata, as long as you have  **READ** permission for the object.

This operation makes server-side encryption available.

## Versioning<a name="section44014347"></a>

By default, the metadata of the object of the latest version is obtained. If the version ID of the object is a deletion mark,  **404**  is returned. You can specify  **versionId**  to obtain the metadata of an object of the desired version.

## Request Syntax<a name="section62065135"></a>

```
HEAD /ObjectName HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section21715305"></a>

[Table 1](#table59191946)  describes the request parameter.

**Table  1**  Request parameter

<a name="table59191946"></a>
<table><thead align="left"><tr id="row1513354"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p55472867"><a name="p55472867"></a><a name="p55472867"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p64117212"><a name="p64117212"></a><a name="p64117212"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p26111645"><a name="p26111645"></a><a name="p26111645"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row33678216"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43581001"><a name="p43581001"></a><a name="p43581001"></a>versionId</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p40400231"><a name="p40400231"></a><a name="p40400231"></a>Indicates the version ID of an object.</p>
<p id="p28057764"><a name="p28057764"></a><a name="p28057764"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p58086424"><a name="p58086424"></a><a name="p58086424"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section61220018"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

If you want to obtain CORS configuration information, you must use the headers in  [Table 2](#table62965470).

**Table  2**  Request headers of CORS configuration

<a name="table62965470"></a>
<table><thead align="left"><tr id="row15558717"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p52296527"><a name="p52296527"></a><a name="p52296527"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="38.74387438743875%" id="mcps1.2.4.1.2"><p id="p8160310"><a name="p8160310"></a><a name="p8160310"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="27.92279227922792%" id="mcps1.2.4.1.3"><p id="p57005402"><a name="p57005402"></a><a name="p57005402"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row54034850"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p14746743"><a name="p14746743"></a><a name="p14746743"></a>Origin</p>
</td>
<td class="cellrowborder" valign="top" width="38.74387438743875%" headers="mcps1.2.4.1.2 "><p id="p53635520"><a name="p53635520"></a><a name="p53635520"></a>Indicates an origin specified by a pre-request. Generally, it is a domain name.</p>
<p id="p12957636"><a name="p12957636"></a><a name="p12957636"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="27.92279227922792%" headers="mcps1.2.4.1.3 "><p id="p42935575"><a name="p42935575"></a><a name="p42935575"></a>Mandatory</p>
</td>
</tr>
<tr id="row50875856"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p27303654"><a name="p27303654"></a><a name="p27303654"></a>Access-Control-Request-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="38.74387438743875%" headers="mcps1.2.4.1.2 "><p id="p64112402"><a name="p64112402"></a><a name="p64112402"></a>Indicates the HTTP headers of a request. The request can use multiple HTTP headers.</p>
<p id="p40140706"><a name="p40140706"></a><a name="p40140706"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="27.92279227922792%" headers="mcps1.2.4.1.3 "><p id="p30171783"><a name="p30171783"></a><a name="p30171783"></a>Optional</p>
</td>
</tr>
<tr id="row49813360103218"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3302128517216"><a name="p3302128517216"></a><a name="p3302128517216"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="38.74387438743875%" headers="mcps1.2.4.1.2 "><p id="p5747846017216"><a name="p5747846017216"></a><a name="p5747846017216"></a>Indicates a decryption algorithm. The header is used in SSE-C mode.</p>
<p id="p4754409217216"><a name="p4754409217216"></a><a name="p4754409217216"></a>Type: string</p>
<p id="p2524364617216"><a name="p2524364617216"></a><a name="p2524364617216"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
<p id="p2586622817216"><a name="p2586622817216"></a><a name="p2586622817216"></a>Constraints: This header must be used together with <strong id="b3146946117216"><a name="b3146946117216"></a><a name="b3146946117216"></a>x-amz-server-side-encryption-customer-key</strong>&nbsp;and&nbsp;<strong id="b1478970017216"><a name="b1478970017216"></a><a name="b1478970017216"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="27.92279227922792%" headers="mcps1.2.4.1.3 "><p id="p5711506117216"><a name="p5711506117216"></a><a name="p5711506117216"></a>No. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row21664203103222"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2938416617216"><a name="p2938416617216"></a><a name="p2938416617216"></a>x-amz-server-side-encryption-customer-key</p>
</td>
<td class="cellrowborder" valign="top" width="38.74387438743875%" headers="mcps1.2.4.1.2 "><p id="p3130723117216"><a name="p3130723117216"></a><a name="p3130723117216"></a>Indicates a key used to decrypt objects. The header is used in SSE-C mode.</p>
<p id="p1332962717216"><a name="p1332962717216"></a><a name="p1332962717216"></a>Type: string</p>
<p id="p5285778117216"><a name="p5285778117216"></a><a name="p5285778117216"></a>Example: x-amz-server-side-encryption-customer-key:K7QkYpBkM5+hcs27fsNkUnNVaobncnLht/rCB2o/9Cw=</p>
<p id="p595798217216"><a name="p595798217216"></a><a name="p595798217216"></a>Constraints: This header is a base64-encoded 256-bit or 512-bit key and must be used together with <strong id="b5362183917216"><a name="b5362183917216"></a><a name="b5362183917216"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b1283450517216"><a name="b1283450517216"></a><a name="b1283450517216"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="27.92279227922792%" headers="mcps1.2.4.1.3 "><p id="p3296198917216"><a name="p3296198917216"></a><a name="p3296198917216"></a>No. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row36443734103226"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p431700017216"><a name="p431700017216"></a><a name="p431700017216"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="38.74387438743875%" headers="mcps1.2.4.1.2 "><p id="p1413274017216"><a name="p1413274017216"></a><a name="p1413274017216"></a>Indicates the MD5 value of a key used to decrypt objects. The header is used in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key.</p>
<p id="p6008580417216"><a name="p6008580417216"></a><a name="p6008580417216"></a>Type: string</p>
<p id="p390132517216"><a name="p390132517216"></a><a name="p390132517216"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
<p id="p3511193017216"><a name="p3511193017216"></a><a name="p3511193017216"></a>Constraints: This header is a base64-encoded 128-bit MD5 value and must be used together with <strong id="b4757191417216"><a name="b4757191417216"></a><a name="b4757191417216"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b2549404817216"><a name="b2549404817216"></a><a name="b2549404817216"></a>x-amz-server-side-encryption-customer-key</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="27.92279227922792%" headers="mcps1.2.4.1.3 "><p id="p5175200717216"><a name="p5175200717216"></a><a name="p5175200717216"></a>No. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row101687305396"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p10523133113916"><a name="p10523133113916"></a><a name="p10523133113916"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="38.74387438743875%" headers="mcps1.2.4.1.2 "><p id="p18523163153915"><a name="p18523163153915"></a><a name="p18523163153915"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p12523183163915"><a name="p12523183163915"></a><a name="p12523183163915"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="27.92279227922792%" headers="mcps1.2.4.1.3 "><p id="p1352316311397"><a name="p1352316311397"></a><a name="p1352316311397"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section14109251"></a>

This request involves no elements.

## Response Syntax<a name="section37049649"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-amz-id-2: id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Accept-Ranges: bytes
 Content-Type: type 
 Date: date 
 Content-Length: length 
 Etag: etag 
 Last-Modified: time
```

## Response Headers<a name="section65011387"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

This response can also include an optional header.  [Table 3](#table53033363)  describes the header.

**Table  3**  Optional response header

<a name="table53033363"></a>
<table><thead align="left"><tr id="row11065763"><th class="cellrowborder" valign="top" width="38.35%" id="mcps1.2.3.1.1"><p id="p23911583"><a name="p23911583"></a><a name="p23911583"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="61.650000000000006%" id="mcps1.2.3.1.2"><p id="p57790096"><a name="p57790096"></a><a name="p57790096"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row50486238"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p62853488"><a name="p62853488"></a><a name="p62853488"></a>x-amz-expiration</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p57967791"><a name="p57967791"></a><a name="p57967791"></a>This header is included in the response if the object expiration is configured. This header includes <strong id="b10684135211308"><a name="b10684135211308"></a><a name="b10684135211308"></a>expiry-date</strong> and&nbsp;<strong id="b11283104012151"><a name="b11283104012151"></a><a name="b11283104012151"></a>rule-id</strong> key value pairs to provide object expiration information.</p>
<p id="p47044503"><a name="p47044503"></a><a name="p47044503"></a>Type: String</p>
</td>
</tr>
<tr id="row20747346"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p2813446"><a name="p2813446"></a><a name="p2813446"></a>x-amz-website-redirect-location</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p26562567"><a name="p26562567"></a><a name="p26562567"></a>When a bucket is configured as a website, you can set this metadata for the object so that the website endpoint will evaluate the request for the object as a 301 redirect to another object in the same bucket or an external URL.</p>
<p id="p37736511"><a name="p37736511"></a><a name="p37736511"></a>Type: String</p>
</td>
</tr>
<tr id="row4084284"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p62391565"><a name="p62391565"></a><a name="p62391565"></a>x-amz-version-id</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p20552036"><a name="p20552036"></a><a name="p20552036"></a>Indicates the version ID of an object. If an object has no version ID specified, this header is not returned.</p>
<p id="p50750596"><a name="p50750596"></a><a name="p50750596"></a>Valid values: String</p>
<p id="p54102182"><a name="p54102182"></a><a name="p54102182"></a>Default: None</p>
</td>
</tr>
<tr id="row17157596"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p47588012"><a name="p47588012"></a><a name="p47588012"></a>Access-Control-Allow-Origin</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p29423773"><a name="p29423773"></a><a name="p29423773"></a>CORS is configured for buckets. If <strong id="b63487369"><a name="b63487369"></a><a name="b63487369"></a>Origin</strong>&nbsp;in the request meets the CORS configuration requirements,&nbsp;<strong id="b34515414"><a name="b34515414"></a><a name="b34515414"></a>Origin</strong> is included in the response.</p>
<p id="p42203278"><a name="p42203278"></a><a name="p42203278"></a>Type: String</p>
</td>
</tr>
<tr id="row44285184"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p30330179"><a name="p30330179"></a><a name="p30330179"></a>Access-Control-Allow-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p40825414"><a name="p40825414"></a><a name="p40825414"></a>CORS is configured for buckets. If <strong id="b31884407"><a name="b31884407"></a><a name="b31884407"></a>headers</strong>&nbsp;in the request meet the CORS configuration requirements,&nbsp;<strong id="b18524209"><a name="b18524209"></a><a name="b18524209"></a>headers</strong> are included in the response.</p>
<p id="p32500157"><a name="p32500157"></a><a name="p32500157"></a>Type: String</p>
</td>
</tr>
<tr id="row24065965"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p3186145"><a name="p3186145"></a><a name="p3186145"></a>Access-Control-Max-Age</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p56751222"><a name="p56751222"></a><a name="p56751222"></a>Indicates <strong id="b40998956"><a name="b40998956"></a><a name="b40998956"></a>MaxAgeSeconds</strong> in the CORS configuration of a server when CORS is configured for buckets.</p>
<p id="p33446292"><a name="p33446292"></a><a name="p33446292"></a>Type: Integer</p>
</td>
</tr>
<tr id="row32581173"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p21829362"><a name="p21829362"></a><a name="p21829362"></a>Access-Control-Allow-Methods</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p23347916"><a name="p23347916"></a><a name="p23347916"></a>CORS is configured for buckets. If <strong id="b8804655"><a name="b8804655"></a><a name="b8804655"></a>Access-Control-Request-Method</strong> in the request meets the CORS configuration requirements, methods in the rule are included in the response.</p>
<p id="p12133034"><a name="p12133034"></a><a name="p12133034"></a>Type: String</p>
<p id="p42088446"><a name="p42088446"></a><a name="p42088446"></a>Valid values: <strong id="b43251701"><a name="b43251701"></a><a name="b43251701"></a>GET</strong>,&nbsp;<strong id="b53720990"><a name="b53720990"></a><a name="b53720990"></a>PUT</strong>,&nbsp;<strong id="b13726868"><a name="b13726868"></a><a name="b13726868"></a>HEAD</strong>,&nbsp;<strong id="b56432951"><a name="b56432951"></a><a name="b56432951"></a>POST</strong>, and&nbsp;<strong id="b38134512"><a name="b38134512"></a><a name="b38134512"></a>DELETE</strong></p>
</td>
</tr>
<tr id="row7666288"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p16989553"><a name="p16989553"></a><a name="p16989553"></a>Access-Control-Expose-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p33976547"><a name="p33976547"></a><a name="p33976547"></a>Indicates <strong id="b987214491518"><a name="b987214491518"></a><a name="b987214491518"></a>ExposeHeader</strong> in the CORS configuration of a server when CORS is configured for buckets.</p>
<p id="p636909"><a name="p636909"></a><a name="p636909"></a>Type: String</p>
</td>
</tr>
<tr id="row54805475103250"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p780079817247"><a name="p780079817247"></a><a name="p780079817247"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p2788494017247"><a name="p2788494017247"></a><a name="p2788494017247"></a>This header is included in a response if SSE-KMS is used.</p>
<p id="p4963787317247"><a name="p4963787317247"></a><a name="p4963787317247"></a>Type: string</p>
<p id="p4408767817247"><a name="p4408767817247"></a><a name="p4408767817247"></a>Example: x-amz-server-side-encryption:aws:kms</p>
</td>
</tr>
<tr id="row28852491103254"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p6188084017247"><a name="p6188084017247"></a><a name="p6188084017247"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p4629218117247"><a name="p4629218117247"></a><a name="p4629218117247"></a>Indicates the master key ID. This header is included in a response if SSE-KMS is used.</p>
<p id="p1397644817247"><a name="p1397644817247"></a><a name="p1397644817247"></a>Example: x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
</td>
</tr>
<tr id="row44732321103258"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p5539231117247"><a name="p5539231117247"></a><a name="p5539231117247"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p5759222117247"><a name="p5759222117247"></a><a name="p5759222117247"></a>Indicates a decryption algorithm. This header is included in a response if SSE-C is used.</p>
<p id="p4856794617247"><a name="p4856794617247"></a><a name="p4856794617247"></a>Type: string</p>
<p id="p3445833117247"><a name="p3445833117247"></a><a name="p3445833117247"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
</td>
</tr>
<tr id="row2546809010331"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p2140888217247"><a name="p2140888217247"></a><a name="p2140888217247"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p5639784417247"><a name="p5639784417247"></a><a name="p5639784417247"></a>Indicates the MD5 value of a key used to decrypt objects. This header is included in a response if SSE-C is used.</p>
<p id="p3781855417247"><a name="p3781855417247"></a><a name="p3781855417247"></a>Type: string</p>
<p id="p482266717247"><a name="p482266717247"></a><a name="p482266717247"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
</td>
</tr>
<tr id="row39621742203855"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p6728147203912"><a name="p6728147203912"></a><a name="p6728147203912"></a>x-amz-storage-class</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p5284058595917"><a name="p5284058595917"></a><a name="p5284058595917"></a>This header is returned when the storage class of an object is not Standard.</p>
<p id="p5627849695922"><a name="p5627849695922"></a><a name="p5627849695922"></a>Type: String</p>
<p id="p27438820203855"><a name="p27438820203855"></a><a name="p27438820203855"></a>Valid values: <strong id="b33981158203921"><a name="b33981158203921"></a><a name="b33981158203921"></a>STANDARD_IA</strong>&nbsp;and&nbsp;<strong id="b18355429203924"><a name="b18355429203924"></a><a name="b18355429203924"></a>GLACIER</strong></p>
</td>
</tr>
<tr id="row6625129720391"><td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.3.1.1 "><p id="p6466818203940"><a name="p6466818203940"></a><a name="p6466818203940"></a>x-amz-restore</p>
</td>
<td class="cellrowborder" valign="top" width="61.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p6194510820407"><a name="p6194510820407"></a><a name="p6194510820407"></a>The following provides examples of object restoration status:</p>
<a name="ul2063506520407"></a><a name="ul2063506520407"></a><ul id="ul2063506520407"><li><strong id="b6082754620407"><a name="b6082754620407"></a><a name="b6082754620407"></a>ongoing-request="true"</strong>indicates that the object is being restored.</li><li><strong id="b2808422520407"><a name="b2808422520407"></a><a name="b2808422520407"></a>ongoing-request="false"</strong>indicates that the object has been restored.</li><li>In <strong id="b6022971520407"><a name="b6022971520407"></a><a name="b6022971520407"></a>expiry-date="Wed, 07 Nov 2012 00:00:00 GMT"</strong>,&nbsp;<strong id="b519652920407"><a name="b519652920407"></a><a name="b519652920407"></a>expiry-date</strong> indicates the expiry date of the restored object.</li></ul>
<p id="p4676876220407"><a name="p4676876220407"></a><a name="p4676876220407"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Response elements<a name="section48231578"></a>

This response involves no elements.

## Error Responses<a name="section31431022"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section63026140"></a>

```
HEAD /test HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: Sat, 03 Dec 2011 09:17:57 +0000 
 Authorization: AWS BF6C09F302931425E9A7:++6NkzwVhw4qccNfIqf4G2vMggg=
```

## Sample Response<a name="section30364352"></a>

```
HTTP/1.1 200 OK  
 Server: OBS 
 x-amz-request-id: 001B21A61C6C0000013403373811529D 
 x-amz-id-2: MDAxQjIxQTYxQzZDMDAwMDAxMzQwMzM3MzgxMTUyOURBQUFBQUFBQWJiYmJiYmJi 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Accept-Ranges: bytes
 ETag: "507e3fff69b69bf57d303e807448560b" 
 Last-Modified: Sat, 03 Dec 2011 08:47:50 GMT 
 Content-Length: 30 
 Content-Type: binary/octet-stream 
 Date: Sat, 03 Dec 2011 09:17:57 GMT  
```

## Sample Request \(Getting the Metadata of an Object with Version ID Specified\)<a name="section43593438"></a>

```
HEAD /object?versionId=AAABQ4-glIvc0vycq3gAAAAVVURTRkha HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Tue, 14 Jan 2014 07:22:17 +0000 
 Authorization: AWS C9590CEB8EC051BDEC9D:CTunmEJMuOBqUa4zfJNz6zxkjBE=
```

## Sample Response \(Getting the Metadata of an Object with Version ID Specified\)<a name="section56796626"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001438FA11E6CBB07 
 x-amz-id-2: SSfKQyh2Gr6ygerqHhJLZ6rxPiv+ucjWabr48RssNJMWmGyKh9gDdXC0jvo1JmFs 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Accept-Ranges: bytes 
 ETag: "ba1f2511fc30423bdbb183fe33f3dd0f" 
 Last-Modified: Tue, 14 Jan 2014 07:21:42 GMT 
 Content-Length: 4 
 x-amz-version-id: AAABQ4-glIvc0vycq3gAAAAVVURTRkha 
 Content-Type: binary/octet-stream 
 Date: Tue, 14 Jan 2014 07:22:17 GMT
```

## Sample Request \(Getting Object Metadata and CORS Configuration when CORS is properly configured\)<a name="section3311378921371"></a>

```
HEAD /object HTTP/1.1
User-Agent: curl/7.19.0 (x86_64-suse-linux-gnu) libcurl/7.19.0 OpenSSL/0.9.8{ zlib/1.2.3 libidn/1.10
Host: bucketname.obs.example.com
Accept: */*
Date: Tue, 28 Apr 2015 14:03:45 +0000
Authorization: AWS D13E0C94E722DD69423C:YcuaA/lJkmWn8AqjfWvIodNJ/yM=
Origin:www.example.com
Access-Control-Request-Headers:AllowedHeader_1
```

## Sample Response \(Getting Object Metadata and CORS Configuration when CORS is properly configured\)<a name="section23469382251"></a>

```
HTTP/1.1 200 OK
x-amz-request-id: D168613B12D6EE5744A69C524D3AA876
x-amz-id-2: 35Sas+J9yUY4xz3PrL0O938UKDg+Dc8EfSw0m9LtfoqB7s0wiMc44TOGguSLNyOv
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
Access-Control-Allow-Origin: www.example.com
Access-Control-Allow-Methods: POST,GET,HEAD,PUT,DELETE
Access-Control-Allow-Headers: AllowedHeader_1
Access-Control-Max-Age: 100
Access-Control-Expose-Headers: ExposeHeader_1
Accept-Ranges: bytes
ETag: "6bcb16084a88ae550811429c0c1e8bc7"
Last-Modified: Tue, 28 Apr 2015 13:38:05 GMT
Content-Length: 264
Content-Type: binary/octet-stream
Date: Tue, 28 Apr 2015 14:03:45 GMT
```

