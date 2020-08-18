# Making an API Request<a name="EN-US_TOPIC_0172602523"></a>

This section describes the structure of a REST API, and uses the IAM API for  [obtaining a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html)  as an example to demonstrate how to call an API. The obtained token is used to authenticate the calling of other APIs.

## Request URI<a name="en-us_topic_0121682347_en-us_topic_0113746487_section697653216219"></a>

A request URI is in the following format:

**\{URI-scheme\}://\{Endpoint\}/\{resource-path\}?\{query-string\}**

Although a request URI is included in the request header, most programming languages or frameworks require the request URI to be transmitted separately.

**Table  1**  URI parameter description

<a name="table1637277135646"></a>
<table><thead align="left"><tr id="row42856273135646"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p48806094135646"><a name="p48806094135646"></a><a name="p48806094135646"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p60979560135646"><a name="p60979560135646"></a><a name="p60979560135646"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row50093829135713"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p13294067135723"><a name="p13294067135723"></a><a name="p13294067135723"></a>URI-scheme</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p188391318133718"><a name="p188391318133718"></a><a name="p188391318133718"></a>Protocol used to transmit requests. All APIs use HTTPS.</p>
</td>
</tr>
<tr id="row40397318135646"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p50957329135646"><a name="p50957329135646"></a><a name="p50957329135646"></a>Endpoint</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p33902960135646"><a name="p33902960135646"></a><a name="p33902960135646"></a>Domain name or IP address of the server bearing the REST service. The endpoint varies between services in different regions. It can be obtained from <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
</td>
</tr>
<tr id="row1377075135915"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p44434271135915"><a name="p44434271135915"></a><a name="p44434271135915"></a>resource-path</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p42406232135915"><a name="p42406232135915"></a><a name="p42406232135915"></a>Access path of an API for performing a specified operation. Obtain the path from the URI of an API. For example, the <strong id="b6355415185818"><a name="b6355415185818"></a><a name="b6355415185818"></a>resource-path</strong> of the API used to <a href="https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html" target="_blank" rel="noopener noreferrer">obtain a user token</a> is <span class="parmvalue" id="parmvalue19213174111414"><a name="parmvalue19213174111414"></a><a name="parmvalue19213174111414"></a><b>/v3/auth/tokens</b></span>. </p>
</td>
</tr>
<tr id="row11383469135646"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p62949675135953"><a name="p62949675135953"></a><a name="p62949675135953"></a>query-string</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p29437205428"><a name="p29437205428"></a><a name="p29437205428"></a>Query parameter, which is optional. Ensure that a question mark (?) is included before each query parameter that is in the format of "<em id="i565516141204"><a name="i565516141204"></a><a name="i565516141204"></a>Parameter name=Parameter value</em>". For example, <strong id="b865615141309"><a name="b865615141309"></a><a name="b865615141309"></a>? limit=10</strong> indicates that a maximum of 10 data records will be displayed.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>To simplify the URI display in this document, each API is provided only with a  **resource-path**  and a request method. The  **URI-scheme**  of all APIs is  **HTTPS**, and the endpoints of all APIs in the same region are identical.

## Request Methods<a name="en-us_topic_0121682347_en-us_topic_0113746487_section5296154118345"></a>

The HTTP protocol defines the following request methods that can be used to send a request to the server:

**Table  2**  HTTP methods

<a name="en-us_topic_0121682347_en-us_topic_0113746487_table1961229113819"></a>
<table><thead align="left"><tr id="en-us_topic_0121682347_en-us_topic_0113746487_row86141913816"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="en-us_topic_0121682347_en-us_topic_0113746487_p186147910387"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p186147910387"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p186147910387"></a><strong id="b472420154315"><a name="b472420154315"></a><a name="b472420154315"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="en-us_topic_0121682347_en-us_topic_0113746487_p166141293387"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p166141293387"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p166141293387"></a><strong id="b1891617238"><a name="b1891617238"></a><a name="b1891617238"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0121682347_en-us_topic_0113746487_row146141194381"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p12831539123914"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p12831539123914"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p12831539123914"></a>GET</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p2831123916397"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p2831123916397"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p2831123916397"></a>Requests the server to return specified resources.</p>
</td>
</tr>
<tr id="en-us_topic_0121682347_en-us_topic_0113746487_row161429103817"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p3831239183912"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p3831239183912"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p3831239183912"></a>PUT</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p178311939193911"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p178311939193911"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p178311939193911"></a>Requests the server to update specified resources.</p>
</td>
</tr>
<tr id="en-us_topic_0121682347_en-us_topic_0113746487_row56141190384"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p68311239113912"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p68311239113912"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p68311239113912"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p1583133918391"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p1583133918391"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p1583133918391"></a>Requests the server to add resources or perform special operations.</p>
</td>
</tr>
<tr id="en-us_topic_0121682347_en-us_topic_0113746487_row861411903812"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p1183153943916"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p1183153943916"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p1183153943916"></a>DELETE</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p6831163914392"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p6831163914392"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p6831163914392"></a>Requests the server to delete specified resources, for example, an object.</p>
</td>
</tr>
<tr id="en-us_topic_0121682347_en-us_topic_0113746487_row5614119183810"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p78314395393"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p78314395393"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p78314395393"></a>HEAD</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p38311239153920"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p38311239153920"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p38311239153920"></a>Same as GET except that the server must return only the response header.</p>
</td>
</tr>
<tr id="en-us_topic_0121682347_en-us_topic_0113746487_row2614199163812"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p1483143915390"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p1483143915390"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p1483143915390"></a>PATCH</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p17831173918394"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p17831173918394"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p17831173918394"></a>Requests the server to update partial content of a specified resource.</p>
<p id="en-us_topic_0121682347_en-us_topic_0113746487_p9831123911390"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p9831123911390"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p9831123911390"></a>If the resource does not exist, a new resource will be created.</p>
</td>
</tr>
</tbody>
</table>

For example, in the case of the API used to  [obtain a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html), the request method is  **POST**. The request is as follows:

```
POST https://{{endpoint}}/v3/auth/tokens
```

## Request Header<a name="en-us_topic_0121682347_section479119143310"></a>

You can also add additional header fields to a request, such as the fields required by a specified URI or HTTP method. For example, to request for the authentication information, add  **Content-Type**, which specifies the request body type.

[Table 3](#td181b06f1c0949cb913acd8d77f21ec3)  lists common request header fields.

**Table  3**  Common request header fields

<a name="td181b06f1c0949cb913acd8d77f21ec3"></a>
<table><thead align="left"><tr id="r97d2c57e12614bd3afdc94a4204ed595"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="aa019e06442ea43f7a2dd236b9eeb153c"><a name="aa019e06442ea43f7a2dd236b9eeb153c"></a><a name="aa019e06442ea43f7a2dd236b9eeb153c"></a>Field</p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.2.5.1.2"><p id="a0b5237510efb47c185142788a435c90a"><a name="a0b5237510efb47c185142788a435c90a"></a><a name="a0b5237510efb47c185142788a435c90a"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.3"><p id="a8df98fec2ab9432c90753890865721a1"><a name="a8df98fec2ab9432c90753890865721a1"></a><a name="a8df98fec2ab9432c90753890865721a1"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.2.5.1.4"><p id="en-us_topic_0037324703_p865237161145"><a name="en-us_topic_0037324703_p865237161145"></a><a name="en-us_topic_0037324703_p865237161145"></a>Example</p>
</th>
</tr>
</thead>
<tbody><tr id="r775e22ddde31427cb0c75310d3b275f5"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="ad5553c8196a14fbcb91cb55152fee53d"><a name="ad5553c8196a14fbcb91cb55152fee53d"></a><a name="ad5553c8196a14fbcb91cb55152fee53d"></a>X-Sdk-Date</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.2 "><p id="a7cd5e01a2bc34080b44f606c2c248dc7"><a name="a7cd5e01a2bc34080b44f606c2c248dc7"></a><a name="a7cd5e01a2bc34080b44f606c2c248dc7"></a>Time when the request is sent. The time is in <strong id="b3354142286"><a name="b3354142286"></a><a name="b3354142286"></a>YYYYMMDD'T'HHMMSS'Z'</strong> format.</p>
<p id="a5ea5e42d645143bbbae5f9c4ab452d7d"><a name="a5ea5e42d645143bbbae5f9c4ab452d7d"></a><a name="a5ea5e42d645143bbbae5f9c4ab452d7d"></a>The value is the current Greenwich Mean Time (GMT) of the system.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="ab64471a82ff44053a057c927cbf9ddc9"><a name="ab64471a82ff44053a057c927cbf9ddc9"></a><a name="ab64471a82ff44053a057c927cbf9ddc9"></a>This field is mandatory for AK/SK-based authentication.</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.4 "><p id="a3e18fe766b9a4185830a0fe282eb2680"><a name="a3e18fe766b9a4185830a0fe282eb2680"></a><a name="a3e18fe766b9a4185830a0fe282eb2680"></a>20150907T101459Z</p>
</td>
</tr>
<tr id="r982b99c7ac074e80b63e96059bc375ff"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="a6a9ab4af31ef41978c7cd032050ae14a"><a name="a6a9ab4af31ef41978c7cd032050ae14a"></a><a name="a6a9ab4af31ef41978c7cd032050ae14a"></a>Host</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.2 "><p id="aaa38a9c8e2dc4fb78234cbb5c1cd580d"><a name="aaa38a9c8e2dc4fb78234cbb5c1cd580d"></a><a name="aaa38a9c8e2dc4fb78234cbb5c1cd580d"></a>Server information of the resource being requested. The value can be obtained from the URL of a service API. The value is <strong id="b0331141320181"><a name="b0331141320181"></a><a name="b0331141320181"></a>hostname[:port]</strong>. If the port number is not specified, the default port is used. The default port number for HTTPS is <strong id="b817353814182"><a name="b817353814182"></a><a name="b817353814182"></a>443</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="a084e3b07cf104f05944d08ef2a96b1c4"><a name="a084e3b07cf104f05944d08ef2a96b1c4"></a><a name="a084e3b07cf104f05944d08ef2a96b1c4"></a>This field is mandatory for AK/SK-based authentication.</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.4 "><p id="a8de4dbac3b7a483b9d39efbdf632998a"><a name="a8de4dbac3b7a483b9d39efbdf632998a"></a><a name="a8de4dbac3b7a483b9d39efbdf632998a"></a>code.test.com</p>
<p id="ac8a2d0ee992c40cfa38782c0b85210a9"><a name="ac8a2d0ee992c40cfa38782c0b85210a9"></a><a name="ac8a2d0ee992c40cfa38782c0b85210a9"></a>or</p>
<p id="ab29d121a7fb94fe3822dca91b79fe760"><a name="ab29d121a7fb94fe3822dca91b79fe760"></a><a name="ab29d121a7fb94fe3822dca91b79fe760"></a>code.test.com:443</p>
</td>
</tr>
<tr id="rc7911eda8b784dceb1da661d56877f0c"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="a5f1759adb3ce437a842cc9af6a3fb071"><a name="a5f1759adb3ce437a842cc9af6a3fb071"></a><a name="a5f1759adb3ce437a842cc9af6a3fb071"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.2 "><p id="p632810083617"><a name="p632810083617"></a><a name="p632810083617"></a>MIME type of the request body This field is mandatory and its default value is <strong id="b8846115917192"><a name="b8846115917192"></a><a name="b8846115917192"></a>application/json</strong>. Other values of this field will be provided for specific APIs if any.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="a2ca751e0d5904460aae7f6d5f5dc3334"><a name="a2ca751e0d5904460aae7f6d5f5dc3334"></a><a name="a2ca751e0d5904460aae7f6d5f5dc3334"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.4 "><p id="a17e3634848fc49ae9ea11717665e49ea"><a name="a17e3634848fc49ae9ea11717665e49ea"></a><a name="a17e3634848fc49ae9ea11717665e49ea"></a>application/json</p>
</td>
</tr>
<tr id="r38eb00e3fde947918d9a8cf46c11b74f"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="aa2ffb672489a4ff4b2b47b0ee711625e"><a name="aa2ffb672489a4ff4b2b47b0ee711625e"></a><a name="aa2ffb672489a4ff4b2b47b0ee711625e"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.2 "><p id="a67d79ec8bb3d412fb1f2d59a3767248a"><a name="a67d79ec8bb3d412fb1f2d59a3767248a"></a><a name="a67d79ec8bb3d412fb1f2d59a3767248a"></a>Length of the request body. The unit is byte.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="a9815cc0accf94167b7f3607db7b90880"><a name="a9815cc0accf94167b7f3607db7b90880"></a><a name="a9815cc0accf94167b7f3607db7b90880"></a>This field is mandatory for POST and PUT requests, but must be left blank for GET requests.</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.4 "><p id="af6f5766e2ad548dcb9e40b3a0074c125"><a name="af6f5766e2ad548dcb9e40b3a0074c125"></a><a name="af6f5766e2ad548dcb9e40b3a0074c125"></a>3495</p>
</td>
</tr>
<tr id="r47347abb1c994c38bacebe25ec1d218e"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="ab8ee25b819d94be08bf7cabf1d921b9a"><a name="ab8ee25b819d94be08bf7cabf1d921b9a"></a><a name="ab8ee25b819d94be08bf7cabf1d921b9a"></a>X-Project-Id</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.2 "><p id="af63b53a9158e418c9317dd79ddcac3db"><a name="af63b53a9158e418c9317dd79ddcac3db"></a><a name="af63b53a9158e418c9317dd79ddcac3db"></a>Project ID. This field is used to obtain the token for each project.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="a234f4a7f440b4413b1aa19c9462695ab"><a name="a234f4a7f440b4413b1aa19c9462695ab"></a><a name="a234f4a7f440b4413b1aa19c9462695ab"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.4 "><p id="a148d7ff92e5e49cfbb4ac0238cd2ebd4"><a name="a148d7ff92e5e49cfbb4ac0238cd2ebd4"></a><a name="a148d7ff92e5e49cfbb4ac0238cd2ebd4"></a>e9993fc787d94b6c886cbaa340f9c0f4</p>
</td>
</tr>
<tr id="rbec1d01d1f9b4bcb8a183ded144e2f0a"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="a5ad0cfc3781243c9ac6fd8e5c47b8894"><a name="a5ad0cfc3781243c9ac6fd8e5c47b8894"></a><a name="a5ad0cfc3781243c9ac6fd8e5c47b8894"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.2 "><p id="a399eb5e20970416186d95d614e84af10"><a name="a399eb5e20970416186d95d614e84af10"></a><a name="a399eb5e20970416186d95d614e84af10"></a>User token.</p>
<p id="p1499864363419"><a name="p1499864363419"></a><a name="p1499864363419"></a>It is a response to the API used to <a href="https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html" target="_blank" rel="noopener noreferrer">obtain a user token</a>. This API is the only one that does not require authentication.</p>
<p id="p18998543163416"><a name="p18998543163416"></a><a name="p18998543163416"></a>The token is the value of <strong id="b1429211919265"><a name="b1429211919265"></a><a name="b1429211919265"></a>X-Subject-Token</strong> in the response header.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="a8ef6da5c4a3742a0b50adb96d3a52baf"><a name="a8ef6da5c4a3742a0b50adb96d3a52baf"></a><a name="a8ef6da5c4a3742a0b50adb96d3a52baf"></a>No</p>
<p id="a90d30c52a285436c8efb6b0924bc3912"><a name="a90d30c52a285436c8efb6b0924bc3912"></a><a name="a90d30c52a285436c8efb6b0924bc3912"></a>This field is mandatory for token-based authentication.</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.4 "><p id="ac1a9d7862596407ba9dc5ca0dfa508c8"><a name="ac1a9d7862596407ba9dc5ca0dfa508c8"></a><a name="ac1a9d7862596407ba9dc5ca0dfa508c8"></a>-</p>
</td>
</tr>
<tr id="row16125640113240"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p31108482113240"><a name="p31108482113240"></a><a name="p31108482113240"></a>X-Language</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.2 "><p id="p36759104113240"><a name="p36759104113240"></a><a name="p36759104113240"></a>Request language. The options are as follows:</p>
<a name="ul5220882114910"></a><a name="ul5220882114910"></a><ul id="ul5220882114910"><li><strong id="b1937151720297"><a name="b1937151720297"></a><a name="b1937151720297"></a>zh-cn</strong>: Chinese</li><li><strong id="b1949891720345"><a name="b1949891720345"></a><a name="b1949891720345"></a>en-us</strong>: English</li></ul>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p24697451113240"><a name="p24697451113240"></a><a name="p24697451113240"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.4 "><p id="p54336490113240"><a name="p54336490113240"></a><a name="p54336490113240"></a>en-us</p>
</td>
</tr>
<tr id="row1305912154611"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p59561232104612"><a name="p59561232104612"></a><a name="p59561232104612"></a>X-Domain-Id</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.2 "><p id="p33051712144616"><a name="p33051712144616"></a><a name="p33051712144616"></a>Domain ID</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p2305312124612"><a name="p2305312124612"></a><a name="p2305312124612"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.4 "><p id="p193051912134613"><a name="p193051912134613"></a><a name="p193051912134613"></a>-</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>In addition to supporting token-based authentication, APIs also support authentication using access key ID/secret access key \(AK/SK\). During AK/SK-based authentication, an SDK is used to sign the request, and the  **Authorization**  \(signature authentication\) and  **X-Sdk-Date**  \(time when the request is sent\) header fields are automatically added to the request.
>For more information, see  **AK/SK-based Authentication**  in  [Authentication](authentication.md).

The API used to  [obtain a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html)  does not require authentication. Therefore, only the  **Content-Type**  field needs to be added to requests for calling the API. An example of such requests is as follows:

```
POST https://{{endpoint}}/v3/auth/tokens
Content-Type: application/json
```

## \(Optional\) Request Body<a name="en-us_topic_0121682347_en-us_topic_0113746487_section1437471411"></a>

This part is optional. The body of a request is often sent in a structured format \(for example, JSON or XML\) as specified in the  **Content-Type**  header field. The request body transfers content except the request header. If the request body contains Chinese characters, these characters must be coded in UTF-8.

The request body varies between APIs. Some APIs do not require the request body, such as the APIs requested using the GET and DELETE methods.

In the case of the API used to  [obtain a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html), the request parameters and parameter description can be obtained from the API request. The following provides an example request with a body included. Replace  _username_,  _domainname_,  _\*\*\*\*\*\*\*\*_  \(login password\), and  _xxxxxxxxxxxxxxxxxx_ _\(project ID\)_  with the actual values. To learn how to obtain a project ID, see  [Obtaining a Project ID](obtaining-a-project-id.md).

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>The  **scope**  parameter specifies where a token takes effect. You can set  **scope**  to an account or a project under an account. In the following example, the token takes effect only for the resources in a specified project. For more information about this API, see  [Obtaining a User Token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html)  of the IAM service.

```

POST https://{{endpoint}}/v3/auth/tokens
Content-Type: application/json

{
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "username",
                    "password": "********",
                    "domain": {
                        "name": "domainname"
                    }
                }
            }
        },
        "scope": {
            "project": {
                "id": "xxxxxxxxxxxxxxxxxx"
            }
        }
    }
}
```

If all data required for the API request is available, you can send the request to call the API through  [curl](https://curl.haxx.se/),  [Postman](https://www.getpostman.com/), or coding. In the response to the API used to obtain a user token,  **x-subject-token**  is the desired user token. This token can then be used to authenticate the calling of other APIs.

