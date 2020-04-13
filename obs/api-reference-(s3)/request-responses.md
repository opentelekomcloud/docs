# Request Responses<a name="EN-US_TOPIC_0125560255"></a>

OBS returns an HTTP response after receiving and processing a request. A response contains a status line, response headers, and an optional response body.

## Response Syntax<a name="section31902586"></a>

```
Status Line: HTTP-Version Status-Code Reason-Phrase 
 Response Headers 
 <Conditional Response Body>
```

## Status Line<a name="section18687820"></a>

The first line of an HTTP response is a status line consisting of space-separated elements.  [Table 1](#table47156901)  describes the elements in a status line.

**Table  1**  Status line elements

<a name="table47156901"></a>
<table><thead align="left"><tr id="row28699899"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p42990474"><a name="p42990474"></a><a name="p42990474"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p59676394"><a name="p59676394"></a><a name="p59676394"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1949763"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p23713084"><a name="p23713084"></a><a name="p23713084"></a>HTTP-Version</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p41711613"><a name="p41711613"></a><a name="p41711613"></a>Indicates an HTTP version. OBS uses HTTP 1.1.</p>
</td>
</tr>
<tr id="row39860200"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p7450793"><a name="p7450793"></a><a name="p7450793"></a>Status-Code</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p66643399"><a name="p66643399"></a><a name="p66643399"></a>Indicates a status code. This element describes the state of a response.</p>
</td>
</tr>
<tr id="row62919684"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p63329656"><a name="p63329656"></a><a name="p63329656"></a>Reason-Phrase</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p29428475"><a name="p29428475"></a><a name="p29428475"></a>Indicates a reason phrase. This element describes a status code in a short text.</p>
</td>
</tr>
</tbody>
</table>

A status code consists of three digits. The first digit defines the type of a status code. Status codes are classified into five types based on request states, as described in  [Table 2](#table46218860).

**Table  2**  OBS status codes

<a name="table46218860"></a>
<table><thead align="left"><tr id="row31049086"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p31948077"><a name="p31948077"></a><a name="p31948077"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p37657477"><a name="p37657477"></a><a name="p37657477"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row30356781"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p42980173"><a name="p42980173"></a><a name="p42980173"></a>1<em id="i51277242"><a name="i51277242"></a><a name="i51277242"></a>xx</em></p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1914018265425"><a name="p1914018265425"></a><a name="p1914018265425"></a>Indicates that a request sent by a client has been received and is being processed by the server.</p>
<p id="p59815938"><a name="p59815938"></a><a name="p59815938"></a>This status code is returned to inform the client must wait before the request is successfully processed.</p>
</td>
</tr>
<tr id="row1472535"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p52166545"><a name="p52166545"></a><a name="p52166545"></a>2<em id="i66845728"><a name="i66845728"></a><a name="i66845728"></a>xx</em></p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p45794886"><a name="p45794886"></a><a name="p45794886"></a>Indicates that a request has been received, understood, and accepted.</p>
</td>
</tr>
<tr id="row9500791"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p31366578"><a name="p31366578"></a><a name="p31366578"></a>3<em id="i13863750"><a name="i13863750"></a><a name="i13863750"></a>xx</em></p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p49222002"><a name="p49222002"></a><a name="p49222002"></a>Indicates that a request can be successfully processed only after being redirected.</p>
</td>
</tr>
<tr id="row40344834"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p46706151"><a name="p46706151"></a><a name="p46706151"></a>4<em id="i17702181"><a name="i17702181"></a><a name="i17702181"></a>xx</em></p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p24590590"><a name="p24590590"></a><a name="p24590590"></a>Indicates that a request fails to be processed due to client error. For example, a request sent by a client is invalid or uses incorrect syntax.</p>
</td>
</tr>
<tr id="row19988723"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p8473833"><a name="p8473833"></a><a name="p8473833"></a>5<em id="i9155637"><a name="i9155637"></a><a name="i9155637"></a>xx</em></p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p3409123"><a name="p3409123"></a><a name="p3409123"></a>Indicates that a request fails to be processed due to client error.</p>
</td>
</tr>
</tbody>
</table>

1_xx_ status codes indicate a provisional response. [Table 3](#table66448310) describes all 1_xx_  status codes.

**Table  3**  1_xx_  status codes

<a name="table66448310"></a>
<table><thead align="left"><tr id="row1085622"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p20826581"><a name="p20826581"></a><a name="p20826581"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p9231496"><a name="p9231496"></a><a name="p9231496"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p9553720"><a name="p9553720"></a><a name="p9553720"></a>Returned After</p>
</th>
</tr>
</thead>
<tbody><tr id="row35653836"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="ole_link19"><a name="ole_link19"></a><a name="ole_link19"></a>100 Continue</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p50429634"><a name="p50429634"></a><a name="p50429634"></a>Indicates that the initial part of the request has been received and has not yet been rejected by the server and the client should continue with its request.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul58268531"></a><a name="ul58268531"></a><ul id="ul58268531"><li>PUT Object</li><li>POST Object</li></ul>
</td>
</tr>
</tbody>
</table>

2_xx_ status codes indicate that a request has been successfully processed by the server. [Table 4](#table22235105164842) describes all 2_xx_  status codes.

**Table  4**  2xx status codes

<a name="table22235105164842"></a>
<table><thead align="left"><tr id="row58972892"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p12074919"><a name="p12074919"></a><a name="p12074919"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p38544387"><a name="p38544387"></a><a name="p38544387"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p35087639"><a name="p35087639"></a><a name="p35087639"></a>Returned After</p>
</th>
</tr>
</thead>
<tbody><tr id="row23526540"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p26601610"><a name="p26601610"></a><a name="p26601610"></a>200 OK</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7246776"><a name="p7246776"></a><a name="p7246776"></a>Indicates that the server has accepted a request.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul50117950"></a><a name="ul50117950"></a><ul id="ul50117950"><li>PUT Bucket</li><li>HEAD Bucket</li><li>GET Bucket (List Objects)</li><li>PUT Object</li><li>GET Object</li><li>HEAD Object</li><li>Operations on the ACL (such as <strong id="b20615021"><a name="b20615021"></a><a name="b20615021"></a>GET Object acl</strong>,&nbsp;<strong id="b51317462"><a name="b51317462"></a><a name="b51317462"></a>PUT Object acl</strong>,&nbsp;<strong id="b59203974"><a name="b59203974"></a><a name="b59203974"></a>PUT Bucket acl</strong>, and&nbsp;<strong id="b63073718"><a name="b63073718"></a><a name="b63073718"></a>GET Bucket acl</strong>)</li><li><strong id="b8697506"><a name="b8697506"></a><a name="b8697506"></a>POST</strong>&nbsp;operations (Status code&nbsp;<strong id="b1671962394610"><a name="b1671962394610"></a><a name="b1671962394610"></a>200</strong> is specified to be returned.)</li><li>Restore cold objects (The object has been restored before and the expiry date has been updated.)</li></ul>
</td>
</tr>
<tr id="row11168697"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p32249251"><a name="p32249251"></a><a name="p32249251"></a>201 Created</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p62052558"><a name="p62052558"></a><a name="p62052558"></a>Indicates that a request response contains an XML file recording response details.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul60201314"></a><a name="ul60201314"></a><ul id="ul60201314"><li><strong id="b44468229"><a name="b44468229"></a><a name="b44468229"></a>POST</strong>&nbsp;operations (Status code&nbsp;<strong id="b9599142820465"><a name="b9599142820465"></a><a name="b9599142820465"></a>201</strong> is specified to be returned.)</li></ul>
</td>
</tr>
<tr id="row57148007145442"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p64133835145450"><a name="p64133835145450"></a><a name="p64133835145450"></a>202 Accepted</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p27458107145450"><a name="p27458107145450"></a><a name="p27458107145450"></a>Indicates that a command for restoring a cold object is successfully delivered.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9514167145450"><a name="p9514167145450"></a><a name="p9514167145450"></a>The cold objects are not restored before the storage objects restore. After the cold objects are restored, <strong id="b585920175311"><a name="b585920175311"></a><a name="b585920175311"></a>202</strong> is returned.</p>
</td>
</tr>
<tr id="row64669749"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3758325"><a name="p3758325"></a><a name="p3758325"></a>204 No Content</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p35988889"><a name="p35988889"></a><a name="p35988889"></a>Indicates that the server has processed a request successfully and no content is returned.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul29418890"></a><a name="ul29418890"></a><ul id="ul29418890"><li><strong id="b34119855"><a name="b34119855"></a><a name="b34119855"></a>DELETE</strong> Object</li><li><strong id="b12244848"><a name="b12244848"></a><a name="b12244848"></a>DELETE</strong> Bucket</li><li><strong id="b52308663"><a name="b52308663"></a><a name="b52308663"></a>POST</strong> operations (No status codes are specified to be returned.)</li><li><strong id="b9143273"><a name="b9143273"></a><a name="b9143273"></a>POST</strong>&nbsp;operations (Status code&nbsp;<strong id="b143921839104613"><a name="b143921839104613"></a><a name="b143921839104613"></a>204</strong> is specified to be returned.)</li><li><strong id="b2407664"><a name="b2407664"></a><a name="b2407664"></a>POST</strong> operations (The status code specified to be returned is invalid.)</li></ul>
</td>
</tr>
<tr id="row485939314559"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p42073411145525"><a name="p42073411145525"></a><a name="p42073411145525"></a>206 Partial Content</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52503106145525"><a name="p52503106145525"></a><a name="p52503106145525"></a>Succeeded in downloading some of the objects.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p24893182145525"><a name="p24893182145525"></a><a name="p24893182145525"></a>The message is returned after the objects with the <strong id="b22712046145525"><a name="b22712046145525"></a><a name="b22712046145525"></a>Range</strong> header are successfully downloaded.</p>
</td>
</tr>
</tbody>
</table>

3_xx_ status codes indicate that a request can be successfully processed only after being redirected. [Table 5](#table20089767165948) describes all 3_xx_  status codes.

**Table  5**  3_xx_  status codes

<a name="table20089767165948"></a>
<table><thead align="left"><tr id="row52422860"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p18393235"><a name="p18393235"></a><a name="p18393235"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p13457087"><a name="p13457087"></a><a name="p13457087"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p16282296"><a name="p16282296"></a><a name="p16282296"></a>Returned After</p>
</th>
</tr>
</thead>
<tbody><tr id="row43797605"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p57945135"><a name="p57945135"></a><a name="p57945135"></a>303 See Other</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p63044349"><a name="p63044349"></a><a name="p63044349"></a>Indicates that a client can use another URI to obtain a specific object.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul6318648"></a><a name="ul6318648"></a><ul id="ul6318648"><li><strong id="b42048455"><a name="b42048455"></a><a name="b42048455"></a>POST</strong> operations (Redirection parameters in requests are valid.)</li></ul>
</td>
</tr>
<tr id="row42891778"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p51681963"><a name="p51681963"></a><a name="p51681963"></a>304 Not Modified</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p25489436"><a name="p25489436"></a><a name="p25489436"></a>Indicates that the requested resource in a <strong id="b28078335"><a name="b28078335"></a><a name="b28078335"></a>GET</strong> request is not modified at the specified time.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul59752688"></a><a name="ul59752688"></a><ul id="ul59752688"><li>Obtaining a resource that is not modified at the specified time</li></ul>
</td>
</tr>
<tr id="row8129598"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p54517712"><a name="p54517712"></a><a name="p54517712"></a>307 Moved Temporarily</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p53858575"><a name="p53858575"></a><a name="p53858575"></a>Indicates that a request has been redirected.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul468450"></a><a name="ul468450"></a><ul id="ul468450"><li>A request is redirected after it fails to be processed by the server.</li></ul>
</td>
</tr>
</tbody>
</table>

4_xx_  status codes indicate that a request fails to be processed due to a client error. When 4_xx_ status codes are returned \(except response to a _HEAD_ request\), the server must contain an error message with an error explanation. 4_xx_  status codes apply to all request methods. [Table 6](#table61163879) describes all 4_xx_  status codes.

**Table  6**  4_xx_  status codes

<a name="table61163879"></a>
<table><thead align="left"><tr id="row18756585"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p42888430"><a name="p42888430"></a><a name="p42888430"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p51410791"><a name="p51410791"></a><a name="p51410791"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p3524541"><a name="p3524541"></a><a name="p3524541"></a>Returned After</p>
</th>
</tr>
</thead>
<tbody><tr id="row17052375"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p39065117"><a name="p39065117"></a><a name="p39065117"></a>400 Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p10157945"><a name="p10157945"></a><a name="p10157945"></a>Indicates that the syntax of a request is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p17487184"><a name="p17487184"></a><a name="p17487184"></a>A request in incorrect syntax or containing incorrect parameters is sent.</p>
</td>
</tr>
<tr id="row23166934"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p64582388"><a name="p64582388"></a><a name="p64582388"></a>403 Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p63790914"><a name="p63790914"></a><a name="p63790914"></a>Indicates that a request fails to be authenticated.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p66790376"><a name="p66790376"></a><a name="p66790376"></a>The requested user does not exist or authentication information in a sent request is incorrect.</p>
</td>
</tr>
<tr id="row64242476"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p36258058"><a name="p36258058"></a><a name="p36258058"></a>404 Not Found</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p51221589"><a name="p51221589"></a><a name="p51221589"></a>Indicates that the requested resource does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p55308020"><a name="p55308020"></a><a name="p55308020"></a>The requested resource (such as a bucket or an object) does not exist.</p>
</td>
</tr>
<tr id="row28010135"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p54228432"><a name="p54228432"></a><a name="p54228432"></a>411 Length Required</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p30426833"><a name="p30426833"></a><a name="p30426833"></a>Indicates that the <strong id="b16832135265317"><a name="b16832135265317"></a><a name="b16832135265317"></a>Content-Length</strong> header is missing in a request.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p35236445"><a name="p35236445"></a><a name="p35236445"></a>A request containing no <strong id="b48692557"><a name="b48692557"></a><a name="b48692557"></a>Content-Length</strong> header is sent.</p>
</td>
</tr>
</tbody>
</table>

5_xx_ status codes indicate that a request fails to be processed due to a client error. A 5_xx_ status code is returned together with a response body containing error details. 5_xx_ status codes can be returned after requests using all HTTP methods \(except HEAD\) are sent. [Table 7](#table16341824) describes all 5_xx_  status codes.

**Table  7**  5_xx_  status codes

<a name="table16341824"></a>
<table><thead align="left"><tr id="row65024193"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p32468313"><a name="p32468313"></a><a name="p32468313"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p12687681"><a name="p12687681"></a><a name="p12687681"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p21069217"><a name="p21069217"></a><a name="p21069217"></a>Returned After</p>
</th>
</tr>
</thead>
<tbody><tr id="row28885026"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p57985771"><a name="p57985771"></a><a name="p57985771"></a>500 Internal Error</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p66335909"><a name="p66335909"></a><a name="p66335909"></a>Indicates that an error occurs on the server.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4499576"><a name="p4499576"></a><a name="p4499576"></a>An error occurs on the server.</p>
</td>
</tr>
<tr id="row40496186"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p58965604"><a name="p58965604"></a><a name="p58965604"></a>503 Service Unavailable</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11484602"><a name="p11484602"></a><a name="p11484602"></a>Indicates that the server is overloaded.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p57837606"><a name="p57837606"></a><a name="p57837606"></a>The server realizes that it is processing too many requests at once.</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section33972659"></a>

Response headers are included in responses to provide additional information about servers and requested resources.  [Table 8](#table53316885)  lists the response headers.

**Table  8**  Response headers

<a name="table53316885"></a>
<table><thead align="left"><tr id="row38686068"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p46563795"><a name="p46563795"></a><a name="p46563795"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p13571075"><a name="p13571075"></a><a name="p13571075"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p25515308"><a name="p25515308"></a><a name="p25515308"></a>Applicable To</p>
</th>
</tr>
</thead>
<tbody><tr id="row53474037"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p36429702"><a name="p36429702"></a><a name="p36429702"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p65124744"><a name="p65124744"></a><a name="p65124744"></a>Indicates the length of a response body.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p40612898"><a name="p40612898"></a><a name="p40612898"></a>All responses</p>
</td>
</tr>
<tr id="row29971768"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11794154"><a name="p11794154"></a><a name="p11794154"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15802441"><a name="p15802441"></a><a name="p15802441"></a>Indicates the date when a request response is returned.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4929340"><a name="p4929340"></a><a name="p4929340"></a>All responses</p>
</td>
</tr>
<tr id="row44364065"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p36719502"><a name="p36719502"></a><a name="p36719502"></a>x-amz-request-id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p21489667"><a name="p21489667"></a><a name="p21489667"></a>Indicates the unique identifier for an OBS request.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62941481"><a name="p62941481"></a><a name="p62941481"></a>All responses</p>
</td>
</tr>
<tr id="row29602422"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p48985959"><a name="p48985959"></a><a name="p48985959"></a>x-amz-id-2</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p8439774"><a name="p8439774"></a><a name="p8439774"></a>Indicates a special token that helps OBS troubleshoot faults.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p12533056"><a name="p12533056"></a><a name="p12533056"></a>All responses</p>
</td>
</tr>
<tr id="row45688646"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9792822"><a name="p9792822"></a><a name="p9792822"></a>x-reserved</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p55021127"><a name="p55021127"></a><a name="p55021127"></a>Indicates the copyright.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p27526304"><a name="p27526304"></a><a name="p27526304"></a>All responses</p>
</td>
</tr>
<tr id="row48651131"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p48427543"><a name="p48427543"></a><a name="p48427543"></a>ETag</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p30316907"><a name="p30316907"></a><a name="p30316907"></a>Indicates the hash value of an object. The entity tag (ETag) only reflects changes to the contents of an object, not its metadata.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p39750432"><a name="p39750432"></a><a name="p39750432"></a>Responses returned after <strong id="b22209574"><a name="b22209574"></a><a name="b22209574"></a>PUT Object</strong>,&nbsp;<strong id="b65668446"><a name="b65668446"></a><a name="b65668446"></a>GET Object</strong>, and&nbsp;<strong id="b61301179542"><a name="b61301179542"></a><a name="b61301179542"></a>HEAD Object</strong> requests are successfully processed.</p>
</td>
</tr>
<tr id="row23677228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p38807334"><a name="p38807334"></a><a name="p38807334"></a>Last-Modified</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p56386340"><a name="p56386340"></a><a name="p56386340"></a>Indicates the date and time at which the last modification to an object is recorded.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3890831"><a name="p3890831"></a><a name="p3890831"></a>Responses returned after <strong id="b35017480"><a name="b35017480"></a><a name="b35017480"></a>GET Object</strong>&nbsp;and <strong id="b49501814175412"><a name="b49501814175412"></a><a name="b49501814175412"></a>HEAD Object</strong> requests are successfully processed.</p>
</td>
</tr>
<tr id="row17843649"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p36049434"><a name="p36049434"></a><a name="p36049434"></a>Location</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34323003"><a name="p34323003"></a><a name="p34323003"></a>Indicates the URI of an object.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p28699853"><a name="p28699853"></a><a name="p28699853"></a>Responses returned after a <strong id="b56972087"><a name="b56972087"></a><a name="b56972087"></a>POST Object</strong> request is successfully processed.</p>
</td>
</tr>
</tbody>
</table>

## Response Body<a name="section37318479"></a>

A response body is included in a request response under the following conditions:

-   Obtaining object content

    If a requested object is not blank, the response body is the content of the object.

-   Obtaining the ACL of a bucket or object

    The response body is the ACL of the requested bucket or object in the XML format.

-   Client error

    The response body describes the client error in detail in the XML format so that the user can perform further operations. For details, see  [Table 1](error-codes.md#table30733758).

-   Server error

    The response body contains error details in the XML format.


## Error Response<a name="section321993"></a>

An error response is returned if a request is incorrect, permission is incorrect, or the requested bucket or object is not found. An error response contains error details in the XML format. The following is an example error response returned after the requested object is not found:

```
<Error> 
 <Code>NoSuchBucket</Code> 
 <Message>The specified bucket does not exist</Message> 
 <RequestId>FDBD2D47937FBD89F71285474962843</RequestId> 
 <HostId>RkRCRDJENDc5MzdGQkQ4OUY3MTI4NTQ3NDk2Mjg0M0FB 
 QUFBQUFBYmJiYmJiYmJD</HostId> 
  …… 
 </Error>     
```

[Table 9](#table127440)  describes the common elements contained in an error response.

**Table  9**  Error response elements

<a name="table127440"></a>
<table><thead align="left"><tr id="row14347060"><th class="cellrowborder" valign="top" width="23.5%" id="mcps1.2.3.1.1"><p id="p21261182"><a name="p21261182"></a><a name="p21261182"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="76.5%" id="mcps1.2.3.1.2"><p id="p44434164"><a name="p44434164"></a><a name="p44434164"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42397568"><td class="cellrowborder" valign="top" width="23.5%" headers="mcps1.2.3.1.1 "><p id="p11650951"><a name="p11650951"></a><a name="p11650951"></a>Code</p>
</td>
<td class="cellrowborder" valign="top" width="76.5%" headers="mcps1.2.3.1.2 "><p id="p4202995"><a name="p4202995"></a><a name="p4202995"></a>A character string that uniquely identifies an error.</p>
</td>
</tr>
<tr id="row37826963"><td class="cellrowborder" valign="top" width="23.5%" headers="mcps1.2.3.1.1 "><p id="p44085137"><a name="p44085137"></a><a name="p44085137"></a>Error</p>
</td>
<td class="cellrowborder" valign="top" width="76.5%" headers="mcps1.2.3.1.2 "><p id="p14126311"><a name="p14126311"></a><a name="p14126311"></a>Container for all error elements in the XML response body.</p>
</td>
</tr>
<tr id="row60027939"><td class="cellrowborder" valign="top" width="23.5%" headers="mcps1.2.3.1.1 "><p id="p30424881"><a name="p30424881"></a><a name="p30424881"></a>Message</p>
</td>
<td class="cellrowborder" valign="top" width="76.5%" headers="mcps1.2.3.1.2 "><p id="p48496300"><a name="p48496300"></a><a name="p48496300"></a>Error details that help you read and understand an error.</p>
</td>
</tr>
<tr id="row33813517"><td class="cellrowborder" valign="top" width="23.5%" headers="mcps1.2.3.1.1 "><p id="p54540374"><a name="p54540374"></a><a name="p54540374"></a>RequestId</p>
</td>
<td class="cellrowborder" valign="top" width="76.5%" headers="mcps1.2.3.1.2 "><p id="p55694143"><a name="p55694143"></a><a name="p55694143"></a>The unique ID of the request whose error response is returned.</p>
</td>
</tr>
<tr id="row31485239"><td class="cellrowborder" valign="top" width="23.5%" headers="mcps1.2.3.1.1 "><p id="p167539"><a name="p167539"></a><a name="p167539"></a>HostId</p>
</td>
<td class="cellrowborder" valign="top" width="76.5%" headers="mcps1.2.3.1.2 "><p id="p13570724"><a name="p13570724"></a><a name="p13570724"></a>ID of the server that returns an error response.</p>
</td>
</tr>
</tbody>
</table>

The preceding elements are commonly found in error responses in the XML format. To facilitate error diagnosis, most error responses also contain other elements to describe error details. For example, if the MD5 value calculated by OBS is inconsistent with that specified in a request for uploading an object, OBS returns an error response that contains both the calculated MD5 value and the user-defined MD5 value.

