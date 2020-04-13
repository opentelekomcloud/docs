# Responses<a name="obs_03_0011"></a>

OBS \(compatible with OpenStack Swift\) returns an HTTP response after receiving and processing a request.

## Syntax<a name="section37018344"></a>

```
Status Line: HTTP-Version Status-Code Reason-Phrase
Response Headers
<Conditional Response Body>
```

## Status Line<a name="section48173595"></a>

The first line of a response is the Status-Line, consisting of the protocol version, numeric status code, and textual phrases. The previous elements are separated by spaces. See  [Table 1](responses.md#table47156901).

**Table  1**  Status line elements

<a name="table47156901"></a>
<table><thead align="left"><tr id="row43952359"><th class="cellrowborder" valign="top" width="34.39%" id="mcps1.2.3.1.1"><p id="p3371364"><a name="p3371364"></a><a name="p3371364"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="65.61%" id="mcps1.2.3.1.2"><p id="p41805515"><a name="p41805515"></a><a name="p41805515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8796476"><td class="cellrowborder" valign="top" width="34.39%" headers="mcps1.2.3.1.1 "><p id="p41425962"><a name="p41425962"></a><a name="p41425962"></a>HTTP-Version</p>
</td>
<td class="cellrowborder" valign="top" width="65.61%" headers="mcps1.2.3.1.2 "><p id="p59801"><a name="p59801"></a><a name="p59801"></a>HTTP version. OBS (compatible with OpenStack Swift) uses HTTP 1.1.</p>
</td>
</tr>
<tr id="row538217"><td class="cellrowborder" valign="top" width="34.39%" headers="mcps1.2.3.1.1 "><p id="p43595579"><a name="p43595579"></a><a name="p43595579"></a>Status-Code</p>
</td>
<td class="cellrowborder" valign="top" width="65.61%" headers="mcps1.2.3.1.2 "><p id="p41581026"><a name="p41581026"></a><a name="p41581026"></a>Status code, which describes the response type.</p>
</td>
</tr>
<tr id="row38684921"><td class="cellrowborder" valign="top" width="34.39%" headers="mcps1.2.3.1.1 "><p id="p46470906"><a name="p46470906"></a><a name="p46470906"></a>Reason-Phrase</p>
</td>
<td class="cellrowborder" valign="top" width="65.61%" headers="mcps1.2.3.1.2 "><p id="p6047043"><a name="p6047043"></a><a name="p6047043"></a>Reason phrase, which describes the status code in a short text.</p>
</td>
</tr>
</tbody>
</table>

The first digit of the status code defines the response type. The last two digits do not have this function. Status codes are classified into five types based on the first digit, as described in  [Table 2](#table46218860).

**Table  2**  Status codes in OBS \(compatible with OpenStack Swift\)

<a name="table46218860"></a>
<table><thead align="left"><tr id="row15005906"><th class="cellrowborder" valign="top" width="21.44%" id="mcps1.2.3.1.1"><p id="p7518910"><a name="p7518910"></a><a name="p7518910"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="78.56%" id="mcps1.2.3.1.2"><p id="p45467475"><a name="p45467475"></a><a name="p45467475"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row62876022"><td class="cellrowborder" valign="top" width="21.44%" headers="mcps1.2.3.1.1 "><p id="p64059033"><a name="p64059033"></a><a name="p64059033"></a>1xx</p>
</td>
<td class="cellrowborder" valign="top" width="78.56%" headers="mcps1.2.3.1.2 "><p id="p52338508"><a name="p52338508"></a><a name="p52338508"></a>Prompts the client to wait because the server has received but is still processing the request.</p>
</td>
</tr>
<tr id="row61119882"><td class="cellrowborder" valign="top" width="21.44%" headers="mcps1.2.3.1.1 "><p id="p51763415"><a name="p51763415"></a><a name="p51763415"></a>2xx</p>
</td>
<td class="cellrowborder" valign="top" width="78.56%" headers="mcps1.2.3.1.2 "><p id="p32087105"><a name="p32087105"></a><a name="p32087105"></a>Indicates that the request has been received, understood, and accepted.</p>
</td>
</tr>
<tr id="row20348492"><td class="cellrowborder" valign="top" width="21.44%" headers="mcps1.2.3.1.1 "><p id="p37615147"><a name="p37615147"></a><a name="p37615147"></a>3xx</p>
</td>
<td class="cellrowborder" valign="top" width="78.56%" headers="mcps1.2.3.1.2 "><p id="p26928091"><a name="p26928091"></a><a name="p26928091"></a>Indicates that the client must take further actions to complete the request.</p>
</td>
</tr>
<tr id="row41026233"><td class="cellrowborder" valign="top" width="21.44%" headers="mcps1.2.3.1.1 "><p id="p34790565"><a name="p34790565"></a><a name="p34790565"></a>4xx</p>
</td>
<td class="cellrowborder" valign="top" width="78.56%" headers="mcps1.2.3.1.2 "><p id="p66572341"><a name="p66572341"></a><a name="p66572341"></a>Indicates a client error. The request contains bad syntax or cannot be fulfilled.</p>
</td>
</tr>
<tr id="row62280158"><td class="cellrowborder" valign="top" width="21.44%" headers="mcps1.2.3.1.1 "><p id="p11528032"><a name="p11528032"></a><a name="p11528032"></a>5xx</p>
</td>
<td class="cellrowborder" valign="top" width="78.56%" headers="mcps1.2.3.1.2 "><p id="p61355386"><a name="p61355386"></a><a name="p61355386"></a>Indicates a server error. The server failed to fulfill a valid request.</p>
</td>
</tr>
</tbody>
</table>

-   A 1xx status code indicates a provisional response.  [Table 3](#table52995244111757)  describes the 1xx status code in OBS \(compatible with OpenStack Swift\).

**Table  3**  1xx status code

<a name="table52995244111757"></a>
<table><thead align="left"><tr id="row29855049111757"><th class="cellrowborder" valign="top" width="19.17%" id="mcps1.2.4.1.1"><p id="p7460031111835"><a name="p7460031111835"></a><a name="p7460031111835"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="51.690000000000005%" id="mcps1.2.4.1.2"><p id="p2544753111835"><a name="p2544753111835"></a><a name="p2544753111835"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="29.14%" id="mcps1.2.4.1.3"><p id="p43185690111835"><a name="p43185690111835"></a><a name="p43185690111835"></a>Returned After</p>
</th>
</tr>
</thead>
<tbody><tr id="row58673429111757"><td class="cellrowborder" valign="top" width="19.17%" headers="mcps1.2.4.1.1 "><p id="p2095015111835"><a name="p2095015111835"></a><a name="p2095015111835"></a>100 Continue</p>
</td>
<td class="cellrowborder" valign="top" width="51.690000000000005%" headers="mcps1.2.4.1.2 "><p id="p20943865112432"><a name="p20943865112432"></a><a name="p20943865112432"></a>Indicates that the initial part of the request has been received and has not yet been rejected by the server and the client should continue with its request.</p>
</td>
<td class="cellrowborder" valign="top" width="29.14%" headers="mcps1.2.4.1.3 "><a name="ul55189990111835"></a><a name="ul55189990111835"></a><ul id="ul55189990111835"><li>PUT Object</li><li>POST Object</li></ul>
</td>
</tr>
</tbody>
</table>

-   A 2xx status code indicates that a request has been successfully processed by the server.  [Table 4](responses.md#table33573506)  describes all 2xx status codes in OBS \(compatible with OpenStack Swift\).

**Table  4**  2xx status codes

<a name="table33573506"></a>
<table><thead align="left"><tr id="row66704998"><th class="cellrowborder" valign="top" width="18.740000000000002%" id="mcps1.2.4.1.1"><p id="p34395739"><a name="p34395739"></a><a name="p34395739"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="51.89%" id="mcps1.2.4.1.2"><p id="p42887950"><a name="p42887950"></a><a name="p42887950"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="29.37%" id="mcps1.2.4.1.3"><p id="p59693950"><a name="p59693950"></a><a name="p59693950"></a>Returned After</p>
</th>
</tr>
</thead>
<tbody><tr id="row30346328"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p42133519"><a name="p42133519"></a><a name="p42133519"></a>200 OK</p>
</td>
<td class="cellrowborder" valign="top" width="51.89%" headers="mcps1.2.4.1.2 "><p id="p57371907"><a name="p57371907"></a><a name="p57371907"></a>Indicates that the server has received and accepted the client's request.</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.4.1.3 "><a name="ul4132170419915"></a><a name="ul4132170419915"></a><ul id="ul4132170419915"><li>List Objects</li><li>GET Object</li><li>GET Object Metadata</li></ul>
</td>
</tr>
<tr id="row37559624"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p22430675"><a name="p22430675"></a><a name="p22430675"></a>201 Created</p>
</td>
<td class="cellrowborder" valign="top" width="51.89%" headers="mcps1.2.4.1.2 "><p id="p4945391"><a name="p4945391"></a><a name="p4945391"></a>Indicates that the response may contain an XML file. The XML file describes the response content.</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.4.1.3 "><a name="ul809924219195"></a><a name="ul809924219195"></a><ul id="ul809924219195"><li>PUT Container</li><li>PUT Object</li></ul>
</td>
</tr>
<tr id="row48981207192048"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p8054840192048"><a name="p8054840192048"></a><a name="p8054840192048"></a>202 Accepted</p>
</td>
<td class="cellrowborder" valign="top" width="51.89%" headers="mcps1.2.4.1.2 "><p id="p48462305192048"><a name="p48462305192048"></a><a name="p48462305192048"></a>Indicates that the server has received the request.</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.4.1.3 "><a name="ul55956597192116"></a><a name="ul55956597192116"></a><ul id="ul55956597192116"><li>POST operations (Update object metadata)</li></ul>
</td>
</tr>
<tr id="row33132024"><td class="cellrowborder" valign="top" width="18.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p66448310"><a name="p66448310"></a><a name="p66448310"></a>204 No Content</p>
</td>
<td class="cellrowborder" valign="top" width="51.89%" headers="mcps1.2.4.1.2 "><p id="p13604004"><a name="p13604004"></a><a name="p13604004"></a>Indicates that the server has processed a request successfully and no content is returned.</p>
</td>
<td class="cellrowborder" valign="top" width="29.37%" headers="mcps1.2.4.1.3 "><a name="ul28182506"></a><a name="ul28182506"></a><ul id="ul28182506"><li>HEAD Container</li><li>POST operations on access control lists (ACLs)</li><li>DELETE Object</li><li>DELETE Container</li></ul>
</td>
</tr>
</tbody>
</table>

-   A 3xx status code indicates that a request can be successfully processed only after being redirected.  [Table 5](responses.md#table49785318)  describes all 3xx status codes in OBS \(compatible with OpenStack Swift\).

**Table  5**  3xx status codes

<a name="table49785318"></a>
<table><thead align="left"><tr id="row57477797"><th class="cellrowborder" valign="top" width="18.08180818081808%" id="mcps1.2.4.1.1"><p id="p25189967"><a name="p25189967"></a><a name="p25189967"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="46.55465546554656%" id="mcps1.2.4.1.2"><p id="p42766607"><a name="p42766607"></a><a name="p42766607"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="35.36353635363537%" id="mcps1.2.4.1.3"><p id="p38344177"><a name="p38344177"></a><a name="p38344177"></a>Returned After</p>
</th>
</tr>
</thead>
<tbody><tr id="row35618305"><td class="cellrowborder" valign="top" width="18.08180818081808%" headers="mcps1.2.4.1.1 "><p id="p66510437"><a name="p66510437"></a><a name="p66510437"></a>303 See Other</p>
</td>
<td class="cellrowborder" valign="top" width="46.55465546554656%" headers="mcps1.2.4.1.2 "><p id="p18636310"><a name="p18636310"></a><a name="p18636310"></a>Indicates that a client can use another URL to get a specific object.</p>
</td>
<td class="cellrowborder" valign="top" width="35.36353635363537%" headers="mcps1.2.4.1.3 "><p id="p33146107"><a name="p33146107"></a><a name="p33146107"></a>POST operations (provided that redirection parameters in requests are valid.)</p>
</td>
</tr>
<tr id="row29879508"><td class="cellrowborder" valign="top" width="18.08180818081808%" headers="mcps1.2.4.1.1 "><p id="p4321123"><a name="p4321123"></a><a name="p4321123"></a>304 Not Modified</p>
</td>
<td class="cellrowborder" valign="top" width="46.55465546554656%" headers="mcps1.2.4.1.2 "><p id="p14466715"><a name="p14466715"></a><a name="p14466715"></a>Indicates that after the client has sent a GET request with the required modification time, access is allowed but the resource has not been modified after the specified time.</p>
</td>
<td class="cellrowborder" valign="top" width="35.36353635363537%" headers="mcps1.2.4.1.3 "><p id="p30953251"><a name="p30953251"></a><a name="p30953251"></a>The resource is obtained but the modification time condition is not met.</p>
</td>
</tr>
<tr id="row29907717"><td class="cellrowborder" valign="top" width="18.08180818081808%" headers="mcps1.2.4.1.1 "><p id="p36058933"><a name="p36058933"></a><a name="p36058933"></a>307 Moved Temporarily</p>
</td>
<td class="cellrowborder" valign="top" width="46.55465546554656%" headers="mcps1.2.4.1.2 "><p id="p55363939"><a name="p55363939"></a><a name="p55363939"></a>Indicates that a request has been redirected.</p>
</td>
<td class="cellrowborder" valign="top" width="35.36353635363537%" headers="mcps1.2.4.1.3 "><p id="p41397110"><a name="p41397110"></a><a name="p41397110"></a>A request is redirected after it fails to be processed by the server.</p>
</td>
</tr>
</tbody>
</table>

-   A 4xx status code indicates that a request fails to be processed due to a client error. A 4xx status code is returned together with a response body containing error details. 4xx status codes apply to all request methods except HEAD. For more details, see the definition of 4xx status codes.

**Table  6**  4xx status codes

<a name="table19085693"></a>
<table><thead align="left"><tr id="row38288479"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p39544387"><a name="p39544387"></a><a name="p39544387"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p9737746"><a name="p9737746"></a><a name="p9737746"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p16489013"><a name="p16489013"></a><a name="p16489013"></a>Returned After</p>
</th>
</tr>
</thead>
<tbody><tr id="row9908272"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p18654746"><a name="p18654746"></a><a name="p18654746"></a>400 Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p27090946"><a name="p27090946"></a><a name="p27090946"></a>Indicates that the syntax of a request is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6185012"><a name="p6185012"></a><a name="p6185012"></a>A request in incorrect syntax or containing incorrect parameters is sent.</p>
</td>
</tr>
<tr id="row3245972720531"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1199219720531"><a name="p1199219720531"></a><a name="p1199219720531"></a>401 Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3184390020531"><a name="p3184390020531"></a><a name="p3184390020531"></a>Indicates that the request failed to be authenticated.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2921909920531"><a name="p2921909920531"></a><a name="p2921909920531"></a>The user does not exist or the authentication information in a sent request is incorrect.</p>
</td>
</tr>
<tr id="row62932594"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7077171"><a name="p7077171"></a><a name="p7077171"></a>403 Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p20407581"><a name="p20407581"></a><a name="p20407581"></a>Indicates that the server has refused the request.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p40427477"><a name="p40427477"></a><a name="p40427477"></a>The user does not have sufficient permissions.</p>
</td>
</tr>
<tr id="row15964395"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p45635608"><a name="p45635608"></a><a name="p45635608"></a>404 Not Found</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p988347"><a name="p988347"></a><a name="p988347"></a>Indicates that the requested resource does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13737275"><a name="p13737275"></a><a name="p13737275"></a>The requested resource (such as a container or object) does not exist.</p>
</td>
</tr>
<tr id="row61354196"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p27211468"><a name="p27211468"></a><a name="p27211468"></a>411 Length Required</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p28625474"><a name="p28625474"></a><a name="p28625474"></a>Indicates that a request header does not contain the required <strong id="b37959091"><a name="b37959091"></a><a name="b37959091"></a>Content-Length</strong>&nbsp;or&nbsp;<strong id="b8423527061012"><a name="b8423527061012"></a><a name="b8423527061012"></a>Transfer-Encoding</strong> field.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p39963934"><a name="p39963934"></a><a name="p39963934"></a>A request containing no <strong id="b23325828"><a name="b23325828"></a><a name="b23325828"></a>Content-Length</strong> header is sent.</p>
</td>
</tr>
<tr id="row654012171047"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1554061717414"><a name="p1554061717414"></a><a name="p1554061717414"></a>412 Precondition Failed</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11540417545"><a name="p11540417545"></a><a name="p11540417545"></a>Conditions are not met.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p35404179416"><a name="p35404179416"></a><a name="p35404179416"></a>Conditions are not met, if the object query request contain the <strong id="b84235270610253"><a name="b84235270610253"></a><a name="b84235270610253"></a>If-Match</strong>&nbsp;or&nbsp;<strong id="b8423527061031"><a name="b8423527061031"></a><a name="b8423527061031"></a>If-None-Match</strong> header.</p>
</td>
</tr>
<tr id="row531414131553"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1031661315518"><a name="p1031661315518"></a><a name="p1031661315518"></a>413 Request Entity Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p16316121311557"><a name="p16316121311557"></a><a name="p16316121311557"></a>Insufficient user quota.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19316161345517"><a name="p19316161345517"></a><a name="p19316161345517"></a>User storage capacity exceeds user quota when uploading or replicating objects.</p>
</td>
</tr>
</tbody>
</table>

-   A 5xx status code indicates that the server encountered an error when processing the request or failed to process the request. Except for HEAD requests, a 5xx status code is returned together with a response body containing error details.  [Table 7](responses.md#table16341824)  describes all 5xx status codes in OBS \(compatible with OpenStack Swift\).

**Table  7**  5xx status codes

<a name="table16341824"></a>
<table><thead align="left"><tr id="row7897978"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p35756461"><a name="p35756461"></a><a name="p35756461"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p28220940"><a name="p28220940"></a><a name="p28220940"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p37753560"><a name="p37753560"></a><a name="p37753560"></a>Returned After</p>
</th>
</tr>
</thead>
<tbody><tr id="row7711627"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p20662084"><a name="p20662084"></a><a name="p20662084"></a>500 Internal Error</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p63016113"><a name="p63016113"></a><a name="p63016113"></a>Indicates that an internal error occurred on the server.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4031547"><a name="p4031547"></a><a name="p4031547"></a>An internal error occurred on the server.</p>
</td>
</tr>
<tr id="row40894175"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p57491299"><a name="p57491299"></a><a name="p57491299"></a>503 Service Unavailable</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p28819977"><a name="p28819977"></a><a name="p28819977"></a>Indicates that the server is overloaded.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p27310200"><a name="p27310200"></a><a name="p27310200"></a>The server is processing too many requests.</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section30909172"></a>

A response header is the information appended to a response, as described in  [Table 8](responses.md#table53316885). Response headers describe the server and contain further information about accessing the requested resource.

**Table  8**  Response headers

<a name="table53316885"></a>
<table><thead align="left"><tr id="row66949839"><th class="cellrowborder" valign="top" width="22.15%" id="mcps1.2.4.1.1"><p id="p54227851"><a name="p54227851"></a><a name="p54227851"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="39.01%" id="mcps1.2.4.1.2"><p id="p4983076"><a name="p4983076"></a><a name="p4983076"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="38.84%" id="mcps1.2.4.1.3"><p id="p8784284"><a name="p8784284"></a><a name="p8784284"></a>Applicable To</p>
</th>
</tr>
</thead>
<tbody><tr id="row28401526"><td class="cellrowborder" valign="top" width="22.15%" headers="mcps1.2.4.1.1 "><p id="p18822307"><a name="p18822307"></a><a name="p18822307"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="39.01%" headers="mcps1.2.4.1.2 "><p id="p48211888"><a name="p48211888"></a><a name="p48211888"></a>Indicates the length of a response body.</p>
</td>
<td class="cellrowborder" valign="top" width="38.84%" headers="mcps1.2.4.1.3 "><p id="p12848837"><a name="p12848837"></a><a name="p12848837"></a>All responses (except those responses whose transfer-encoding is chunked)</p>
</td>
</tr>
<tr id="row48530675"><td class="cellrowborder" valign="top" width="22.15%" headers="mcps1.2.4.1.1 "><p id="p38670568"><a name="p38670568"></a><a name="p38670568"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="39.01%" headers="mcps1.2.4.1.2 "><p id="p45308281"><a name="p45308281"></a><a name="p45308281"></a>Indicates the date and time when a response was generated.</p>
</td>
<td class="cellrowborder" valign="top" width="38.84%" headers="mcps1.2.4.1.3 "><p id="p23205770"><a name="p23205770"></a><a name="p23205770"></a>All responses</p>
</td>
</tr>
<tr id="row12176400"><td class="cellrowborder" valign="top" width="22.15%" headers="mcps1.2.4.1.1 "><p id="p46764328"><a name="p46764328"></a><a name="p46764328"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="39.01%" headers="mcps1.2.4.1.2 "><p id="p29814200"><a name="p29814200"></a><a name="p29814200"></a>Indicates a unique identifier generated by OBS (compatible with OpenStack Swift) for a request.</p>
</td>
<td class="cellrowborder" valign="top" width="38.84%" headers="mcps1.2.4.1.3 "><p id="p27453078"><a name="p27453078"></a><a name="p27453078"></a>All responses</p>
</td>
</tr>
<tr id="row37925019222057"><td class="cellrowborder" valign="top" width="22.15%" headers="mcps1.2.4.1.1 "><p id="p30071130104918"><a name="p30071130104918"></a><a name="p30071130104918"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="39.01%" headers="mcps1.2.4.1.2 "><p id="p45466191104918"><a name="p45466191104918"></a><a name="p45466191104918"></a>Indicates the object type returned.</p>
</td>
<td class="cellrowborder" valign="top" width="38.84%" headers="mcps1.2.4.1.3 "><p id="p16837049104918"><a name="p16837049104918"></a><a name="p16837049104918"></a>All responses</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>OBS \(compatible with OpenStack Swift\) normalizes the content of the  **Content-Type**. In comparison to the content returned by OpenStack Swift, the differences are as follows:  
>-   The character set is unified into  **charset=UTF-8** \(UTF in uppercase\) for the content of **Content-Type**.  

## Response Body<a name="section9747098"></a>

In OBS \(compatible with OpenStack Swift\), a response body is included in a request response under the following conditions:

-   GET Object

    If the object is not blank, the response body is the object body.

-   GET Account or Container

    The response body is account or container information.


-   Client error

    The response body describes the client error in detail in XML format so that the user can perform further operations. For details, see client error response codes.

-   Server error

    The response body describes the server error in detail in XML format so that the user can perform further operations.


## Error Responses<a name="section20615021"></a>

OBS \(compatible with OpenStack Swift\) returns an error response if a request is incorrect, the permission is incorrect, or the requested container or object is not found. An error response describes the error. In the event of uploading an object, if the permission fails to pass the authentication, the following error information \(in HTML format\) is displayed:

```
<html><h1>Unauthorized</h1><p>This server could not verify that you are authorized to access the document you requested.</p></html>
```

