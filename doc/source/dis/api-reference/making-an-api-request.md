# Making an API Request<a name="dis_02_0400"></a>

This section describes the structure of a REST API request, and uses the IAM API for  [obtaining a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html)  as an example to demonstrate how to call an API. The obtained token can then be used to authenticate the calling of other APIs.

## Request URI<a name="en-us_topic_0121682347_en-us_topic_0113746487_section697653216219"></a>

A request URI is in the following format:

**\{URI-scheme\}://\{Endpoint\}/\{resource-path\}?\{query-string\}**

Although a request URI is included in the request header, most programming languages or frameworks require the request URI to be transmitted separately.

**Table  1**  URI parameter description

<a name="en-us_topic_0121682347_en-us_topic_0113746487_table4443194632512"></a>
<table><thead align="left"><tr id="en-us_topic_0121682347_en-us_topic_0113746487_row1944414616258"><th class="cellrowborder" valign="top" width="19.48%" id="mcps1.2.3.1.1"><p id="en-us_topic_0121682347_en-us_topic_0113746487_p1644484692510"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p1644484692510"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p1644484692510"></a><strong id="en-us_topic_0121682347_b23574928194256"><a name="en-us_topic_0121682347_b23574928194256"></a><a name="en-us_topic_0121682347_b23574928194256"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="80.52%" id="mcps1.2.3.1.2"><p id="en-us_topic_0121682347_en-us_topic_0113746487_p174441146142511"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p174441146142511"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p174441146142511"></a><strong id="en-us_topic_0121682347_en-us_topic_0113746487_b131565362615"><a name="en-us_topic_0121682347_en-us_topic_0113746487_b131565362615"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_b131565362615"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0121682347_en-us_topic_0113746487_row10444144620259"><td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p154446465251"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p154446465251"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p154446465251"></a>URI-scheme</p>
</td>
<td class="cellrowborder" valign="top" width="80.52%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p8444144692517"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p8444144692517"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p8444144692517"></a>Protocol used to transmit requests. All APIs use HTTPS.</p>
</td>
</tr>
<tr id="en-us_topic_0121682347_en-us_topic_0113746487_row444414692513"><td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p7444194610257"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p7444194610257"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p7444194610257"></a>Endpoint</p>
</td>
<td class="cellrowborder" valign="top" width="80.52%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p244474613259"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p244474613259"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p244474613259"></a>Domain name or IP address of the server bearing the REST service. The endpoint varies between services in different regions. It can be obtained from <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0121682347_en-us_topic_0113746487_row1744454612520"><td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p14442468257"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p14442468257"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p14442468257"></a>resource-path</p>
</td>
<td class="cellrowborder" valign="top" width="80.52%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p1844412467258"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p1844412467258"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p1844412467258"></a>Access path of an API for performing a specified operation. Obtain the path from the URI of an API. For example, the <strong id="b598026563"><a name="b598026563"></a><a name="b598026563"></a>resource-path</strong> of the API used to obtain a user token is <span class="parmvalue" id="parmvalue11981361063"><a name="parmvalue11981361063"></a><a name="parmvalue11981361063"></a><b>/v3/auth/tokens</b></span>.</p>
</td>
</tr>
<tr id="en-us_topic_0121682347_en-us_topic_0113746487_row184441346152515"><td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p4444154692516"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p4444154692516"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p4444154692516"></a>qcnuery-string</p>
</td>
<td class="cellrowborder" valign="top" width="80.52%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0121682347_en-us_topic_0113746487_p1444414622514"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p1444414622514"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p1444414622514"></a>Query parameter, which is optional. Ensure that a question mark (?) is included before each query parameter that is in the format of "<em id="i9336125020386"><a name="i9336125020386"></a><a name="i9336125020386"></a>Parameter name=Parameter value</em>". For example, <strong id="b1190023920610"><a name="b1190023920610"></a><a name="b1190023920610"></a>? limit=10</strong> indicates that a maximum of 10 data records will be displayed.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>To simplify the URI display in this document, each API is provided only with a  **resource-path**  and a request method. The  **URI-scheme**  of all APIs is  **HTTPS**, and the endpoints of all APIs in the same region are identical.  

## Request Methods<a name="en-us_topic_0121682347_en-us_topic_0113746487_section5296154118345"></a>

The HTTP protocol defines the following request methods that can be used to send a request to the server:

**Table  2**  HTTP methods

<a name="en-us_topic_0121682347_en-us_topic_0113746487_table1961229113819"></a>
<table><thead align="left"><tr id="en-us_topic_0121682347_en-us_topic_0113746487_row86141913816"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="en-us_topic_0121682347_en-us_topic_0113746487_p186147910387"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p186147910387"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p186147910387"></a><strong id="en-us_topic_0121682347_en-us_topic_0113746487_b1093312238395"><a name="en-us_topic_0121682347_en-us_topic_0113746487_b1093312238395"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_b1093312238395"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="en-us_topic_0121682347_en-us_topic_0113746487_p166141293387"><a name="en-us_topic_0121682347_en-us_topic_0113746487_p166141293387"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_p166141293387"></a><strong id="en-us_topic_0121682347_en-us_topic_0113746487_b169341023133919"><a name="en-us_topic_0121682347_en-us_topic_0113746487_b169341023133919"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_b169341023133919"></a>Description</strong></p>
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

For example, in the case of the API used to  [obtain a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html), the request method is  **POST**, and the request is as follows:

## Request Header<a name="en-us_topic_0121682347_section479119143310"></a>

You can also add additional header fields to a request, such as the fields required by a specified URI or HTTP method. For example, to request for the authentication information, add  **Content-Type**, which specifies the request body type.

[Table 3](#en-us_topic_0121682347_table1986821153312)  lists common request headers.

**Table  3**  Common request headers

<a name="en-us_topic_0121682347_table1986821153312"></a>
<table><thead align="left"><tr id="en-us_topic_0121682347_row1286841153311"><th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0121682347_p178680183310"><a name="en-us_topic_0121682347_p178680183310"></a><a name="en-us_topic_0121682347_p178680183310"></a><strong id="en-us_topic_0121682347_en-us_topic_0113746487_b1355613001117"><a name="en-us_topic_0121682347_en-us_topic_0113746487_b1355613001117"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_b1355613001117"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.5%" id="mcps1.2.5.1.2"><p id="en-us_topic_0121682347_p78688118335"><a name="en-us_topic_0121682347_p78688118335"></a><a name="en-us_topic_0121682347_p78688118335"></a><strong id="en-us_topic_0121682347_en-us_topic_0113746487_b612662015512"><a name="en-us_topic_0121682347_en-us_topic_0113746487_b612662015512"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_b612662015512"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.11%" id="mcps1.2.5.1.3"><p id="en-us_topic_0121682347_p58686123316"><a name="en-us_topic_0121682347_p58686123316"></a><a name="en-us_topic_0121682347_p58686123316"></a><strong id="en-us_topic_0121682347_en-us_topic_0113746487_b812872012519"><a name="en-us_topic_0121682347_en-us_topic_0113746487_b812872012519"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_b812872012519"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.650000000000006%" id="mcps1.2.5.1.4"><p id="en-us_topic_0121682347_p48681314333"><a name="en-us_topic_0121682347_p48681314333"></a><a name="en-us_topic_0121682347_p48681314333"></a><strong id="en-us_topic_0121682347_en-us_topic_0113746487_b812932085119"><a name="en-us_topic_0121682347_en-us_topic_0113746487_b812932085119"></a><a name="en-us_topic_0121682347_en-us_topic_0113746487_b812932085119"></a>Example</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0121682347_row1286861153311"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0121682347_p2086813163316"><a name="en-us_topic_0121682347_p2086813163316"></a><a name="en-us_topic_0121682347_p2086813163316"></a>Host</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0121682347_p58681814333"><a name="en-us_topic_0121682347_p58681814333"></a><a name="en-us_topic_0121682347_p58681814333"></a>Specifies the server domain name and port number of the resources being requested. The value can be obtained from the URL of the service API. The value is in the format of <em id="en-us_topic_0121682347_i1012185414574"><a name="en-us_topic_0121682347_i1012185414574"></a><a name="en-us_topic_0121682347_i1012185414574"></a>Hostname:Port number</em>. If the port number is not specified, the default port is used. The default port number for HTTPS is 443.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0121682347_p886815123319"><a name="en-us_topic_0121682347_p886815123319"></a><a name="en-us_topic_0121682347_p886815123319"></a>No</p>
<p id="en-us_topic_0121682347_p386811116333"><a name="en-us_topic_0121682347_p386811116333"></a><a name="en-us_topic_0121682347_p386811116333"></a>This field is mandatory for AK/SK authentication.</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0121682347_p486814118330"><a name="en-us_topic_0121682347_p486814118330"></a><a name="en-us_topic_0121682347_p486814118330"></a>code.test.com</p>
<p id="en-us_topic_0121682347_p5868161163317"><a name="en-us_topic_0121682347_p5868161163317"></a><a name="en-us_topic_0121682347_p5868161163317"></a>or</p>
<p id="en-us_topic_0121682347_p786841123315"><a name="en-us_topic_0121682347_p786841123315"></a><a name="en-us_topic_0121682347_p786841123315"></a>code.test.com:443</p>
</td>
</tr>
<tr id="en-us_topic_0121682347_row386818143313"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0121682347_p118689123320"><a name="en-us_topic_0121682347_p118689123320"></a><a name="en-us_topic_0121682347_p118689123320"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0121682347_p1486815116337"><a name="en-us_topic_0121682347_p1486815116337"></a><a name="en-us_topic_0121682347_p1486815116337"></a>Specifies the request body MIME type. Its default value is <strong id="b199163912328"><a name="b199163912328"></a><a name="b199163912328"></a>application/json</strong>. Other values of this field will be provided for specific APIs if any.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0121682347_p1086812114335"><a name="en-us_topic_0121682347_p1086812114335"></a><a name="en-us_topic_0121682347_p1086812114335"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0121682347_p1186841163310"><a name="en-us_topic_0121682347_p1186841163310"></a><a name="en-us_topic_0121682347_p1186841163310"></a>application/json</p>
</td>
</tr>
<tr id="en-us_topic_0121682347_row11868419337"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0121682347_p178687119330"><a name="en-us_topic_0121682347_p178687119330"></a><a name="en-us_topic_0121682347_p178687119330"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0121682347_p178681813332"><a name="en-us_topic_0121682347_p178681813332"></a><a name="en-us_topic_0121682347_p178681813332"></a>Specifies the length of the request body. The unit is byte.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0121682347_p18687183316"><a name="en-us_topic_0121682347_p18687183316"></a><a name="en-us_topic_0121682347_p18687183316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0121682347_p148689110334"><a name="en-us_topic_0121682347_p148689110334"></a><a name="en-us_topic_0121682347_p148689110334"></a>3495</p>
</td>
</tr>
<tr id="en-us_topic_0121682347_row2868171143313"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0121682347_p586815118338"><a name="en-us_topic_0121682347_p586815118338"></a><a name="en-us_topic_0121682347_p586815118338"></a>X-Project-Id</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0121682347_p1586811163312"><a name="en-us_topic_0121682347_p1586811163312"></a><a name="en-us_topic_0121682347_p1586811163312"></a>Specifies the project ID. Obtain the project ID by following the instructions in <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0121682347_p886812110335"><a name="en-us_topic_0121682347_p886812110335"></a><a name="en-us_topic_0121682347_p886812110335"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0121682347_p198684143315"><a name="en-us_topic_0121682347_p198684143315"></a><a name="en-us_topic_0121682347_p198684143315"></a>e9993fc787d94b6c886cbaa340f9c0f4</p>
</td>
</tr>
<tr id="en-us_topic_0121682347_row188688113337"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0121682347_p198684111335"><a name="en-us_topic_0121682347_p198684111335"></a><a name="en-us_topic_0121682347_p198684111335"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0121682347_p1086851153317"><a name="en-us_topic_0121682347_p1086851153317"></a><a name="en-us_topic_0121682347_p1086851153317"></a>Specifies the user token.</p>
<p id="en-us_topic_0121682347_p1057635831"><a name="en-us_topic_0121682347_p1057635831"></a><a name="en-us_topic_0121682347_p1057635831"></a>It is a response to the API used to <a href="https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html" target="_blank" rel="noopener noreferrer">obtain a user token</a>. This API is the only one that does not require authentication.</p>
<p id="en-us_topic_0121682347_p15868417337"><a name="en-us_topic_0121682347_p15868417337"></a><a name="en-us_topic_0121682347_p15868417337"></a>After the request is processed, the value of <strong id="en-us_topic_0121682347_b842352706205322"><a name="en-us_topic_0121682347_b842352706205322"></a><a name="en-us_topic_0121682347_b842352706205322"></a>X-Subject-Token</strong> in the header is the token value.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0121682347_p4868514338"><a name="en-us_topic_0121682347_p4868514338"></a><a name="en-us_topic_0121682347_p4868514338"></a>No</p>
<p id="en-us_topic_0121682347_p986818114339"><a name="en-us_topic_0121682347_p986818114339"></a><a name="en-us_topic_0121682347_p986818114339"></a>This field is mandatory for token authentication.</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0121682347_p27152505302"><a name="en-us_topic_0121682347_p27152505302"></a><a name="en-us_topic_0121682347_p27152505302"></a>The following is part of an example token:</p>
<p id="en-us_topic_0121682347_p168689113318"><a name="en-us_topic_0121682347_p168689113318"></a><a name="en-us_topic_0121682347_p168689113318"></a>MIIPAgYJKoZIhvcNAQcCo...ggg1BBIINPXsidG9rZ</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>In addition to supporting token-based authentication, APIs also support authentication using access key ID/secret access key \(AK/SK\). During AK/SK-based authentication, an SDK is used to sign the request, and the  **Authorization**  \(signature authentication\) and  **X-Sdk-Date**  \(time when the request is sent\) header fields are automatically added to the request.  
>For more information, see "AK/SK-based Authentication" in  [Authentication](authentication.md).  

The API used to  [obtain a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html)  does not require authentication. Therefore, only the  **Content-Type**  field needs to be added to requests for calling the API. An example of such requests is as follows:

## \(Optional\) Request Body<a name="en-us_topic_0121682347_en-us_topic_0113746487_section1437471411"></a>

This part is optional. The body of a request is often sent in a structured format as specified in the  **Content-Type**  header field, such as JSON or XML. The request body transfers content except the request header.

The request body varies between APIs. Some APIs do not require the request body, such as the APIs requested using the GET and DELETE methods.

In the case of the API used to  [obtain a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html), the request parameters and parameter description can be obtained from the API request. The following provides an example request with a body included. Replace  _username_,  _domainname_,  _\*\*\*\*\*\*\*\*_  \(login password\), and  _xxxxxxxxxxxxxxxxxx_  \(project ID\) with the actual values. To learn how to obtain a project ID, see  [Obtaining a Project ID](obtaining-a-project-id.md).

>![](/images/icon-note.gif) **NOTE:**   
>The  **scope**  parameter specifies where a token takes effect. In the following example, the token takes effect only for the resources in a specified project. You can set  **scope**  to a domain or a project under a domain. In the following example, the token takes effect only for the resources in a specified project. For more information about this API, see  [obtaining a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html).  

```

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
                "name": "xxxxxxxxxxxxxxxxxx"
            }
        }
    }
}
```

If all data required for the API request is available, you can send the request to call the API through  [curl](https://curl.haxx.se/),  [Postman](https://www.getpostman.com/), or coding. In the response to the API used to obtain a user token,  **x-subject-token**  is the desired user token. This token can then be used to authenticate the calling of other APIs.

