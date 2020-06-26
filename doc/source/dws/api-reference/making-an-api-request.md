# Making an API Request<a name="dws_02_0063"></a>

This section describes the structure of a REST API, and uses the IAM API for obtaining a user token as an example to describe how to call an API. The obtained token is used to authenticate the calling of other APIs.

## Request URI<a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_section697653216219"></a>

A request URI is in the following format:

**\{URI-scheme\}://\{Endpoint\}/\{resource-path\}?\{query-string\}**

Although a request URI is included in a request header, most programming languages or frameworks require the request URI to be separately transmitted, rather than being conveyed in a request message.

**Table  1**  URI parameter description

<a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_table4443194632512"></a>
<table><thead align="left"><tr id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_row1944414616258"><th class="cellrowborder" valign="top" width="19.48%" id="mcps1.2.3.1.1"><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1644484692510"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1644484692510"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1644484692510"></a><strong id="en-us_topic_0171007788_en-us_topic_0121682347_b23574928194256"><a name="en-us_topic_0171007788_en-us_topic_0121682347_b23574928194256"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_b23574928194256"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="80.52%" id="mcps1.2.3.1.2"><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p174441146142511"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p174441146142511"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p174441146142511"></a><strong id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b131565362615"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b131565362615"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b131565362615"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_row10444144620259"><td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p154446465251"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p154446465251"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p154446465251"></a>URI-scheme</p>
</td>
<td class="cellrowborder" valign="top" width="80.52%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p8444144692517"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p8444144692517"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p8444144692517"></a>Protocol used to transmit requests. All APIs use HTTPS.</p>
</td>
</tr>
<tr id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_row444414692513"><td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p7444194610257"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p7444194610257"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p7444194610257"></a>Endpoint</p>
</td>
<td class="cellrowborder" valign="top" width="80.52%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p244474613259"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p244474613259"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p244474613259"></a>Domain name or IP address of the server bearing the REST service endpoint. Obtain the value from <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
<p id="p15129619134716"><a name="p15129619134716"></a><a name="p15129619134716"></a>For example, the endpoint of IAM in region <span class="parmname" id="parmname51291019104710"><a name="parmname51291019104710"></a><a name="parmname51291019104710"></a><b>eu-de</b></span> is <span class="parmname" id="parmname144291017134818"><a name="parmname144291017134818"></a><a name="parmname144291017134818"></a><b>iam.eu-de.otc.t-systems.com</b></span>.</p>
</td>
</tr>
<tr id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_row1744454612520"><td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p14442468257"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p14442468257"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p14442468257"></a>resource-path</p>
</td>
<td class="cellrowborder" valign="top" width="80.52%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1844412467258"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1844412467258"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1844412467258"></a>API access path for performing a specified operation. Obtain the value from the URI of the API. For example, the <strong id="b1237161619462"><a name="b1237161619462"></a><a name="b1237161619462"></a>resource-path</strong> of the API for obtaining a user token is <strong id="b59951427124618"><a name="b59951427124618"></a><a name="b59951427124618"></a>/v3/auth/tokens</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_row184441346152515"><td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p4444154692516"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p4444154692516"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p4444154692516"></a>query-string</p>
</td>
<td class="cellrowborder" valign="top" width="80.52%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1444414622514"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1444414622514"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1444414622514"></a>Query parameter, which is optional. Not all APIs have a query parameter. Ensure that a question mark (?) is included before a query parameter that is in the format of "Parameter name=Parameter value". For example, <span class="parmname" id="parmname199605132483"><a name="parmname199605132483"></a><a name="parmname199605132483"></a><b>? limit=10</b></span> indicates that a maximum of 10 pieces of data is to be viewed.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>To simplify the URI display, each API is provided with only a  **resource-path**  and a request method. This is because the  **URI-scheme**  value of all APIs is  **HTTPS**, and the endpoints in a region are the same. Therefore, the two parts are omitted.  

## Request Methods<a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_section5296154118345"></a>

HTTP-based request methods, which are also called operations or actions, specify the type of operations that you are requesting.

**Table  2**  HTTP methods

<a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_table1961229113819"></a>
<table><thead align="left"><tr id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_row86141913816"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p186147910387"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p186147910387"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p186147910387"></a><strong id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b1093312238395"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b1093312238395"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b1093312238395"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p166141293387"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p166141293387"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p166141293387"></a><strong id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b169341023133919"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b169341023133919"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b169341023133919"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_row146141194381"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p12831539123914"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p12831539123914"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p12831539123914"></a>GET</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p2831123916397"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p2831123916397"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p2831123916397"></a>Requests the server to return specified resources.</p>
</td>
</tr>
<tr id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_row161429103817"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p3831239183912"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p3831239183912"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p3831239183912"></a>PUT</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p178311939193911"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p178311939193911"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p178311939193911"></a>Requests the server to update specified resources.</p>
</td>
</tr>
<tr id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_row56141190384"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p68311239113912"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p68311239113912"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p68311239113912"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1583133918391"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1583133918391"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1583133918391"></a>Requests the server to add resources or perform special operations.</p>
</td>
</tr>
<tr id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_row861411903812"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1183153943916"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1183153943916"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1183153943916"></a>DELETE</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p6831163914392"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p6831163914392"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p6831163914392"></a>Requests the server to delete specified resources, for example, an object.</p>
</td>
</tr>
<tr id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_row5614119183810"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p78314395393"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p78314395393"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p78314395393"></a>HEAD</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p38311239153920"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p38311239153920"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p38311239153920"></a>Requests a server resource header.</p>
</td>
</tr>
<tr id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_row2614199163812"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1483143915390"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1483143915390"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p1483143915390"></a>PATCH</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p17831173918394"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p17831173918394"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p17831173918394"></a>Requests the server to update partial content of a specified resource.</p>
<p id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p9831123911390"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p9831123911390"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_p9831123911390"></a>If the resource is unavailable, the PATCH method is used to create a resource.</p>
</td>
</tr>
</tbody>
</table>

For example, in the URI for obtaining a user token, the request method is POST, and the request is as follows:

```
POST https://iam.eu-de.otc.t-systems.com/v3/auth/tokens
```

## Request Header<a name="en-us_topic_0171007788_en-us_topic_0121682347_section479119143310"></a>

You can also add additional fields to a request, such as the fields required by a specified URI or an HTTP method. For example, add  **Content-Type**  that defines a request body type to request for the authentication information.

[Table 3](#en-us_topic_0171007788_en-us_topic_0121682347_table1986821153312)  lists common request headers.

**Table  3**  Common request headers

<a name="en-us_topic_0171007788_en-us_topic_0121682347_table1986821153312"></a>
<table><thead align="left"><tr id="en-us_topic_0171007788_en-us_topic_0121682347_row1286841153311"><th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0171007788_en-us_topic_0121682347_p178680183310"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p178680183310"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p178680183310"></a><strong id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b1355613001117"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b1355613001117"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b1355613001117"></a>Field</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.5%" id="mcps1.2.5.1.2"><p id="en-us_topic_0171007788_en-us_topic_0121682347_p78688118335"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p78688118335"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p78688118335"></a><strong id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b612662015512"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b612662015512"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b612662015512"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.11%" id="mcps1.2.5.1.3"><p id="en-us_topic_0171007788_en-us_topic_0121682347_p58686123316"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p58686123316"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p58686123316"></a><strong id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b812872012519"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b812872012519"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b812872012519"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.650000000000006%" id="mcps1.2.5.1.4"><p id="en-us_topic_0171007788_en-us_topic_0121682347_p48681314333"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p48681314333"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p48681314333"></a><strong id="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b812932085119"><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b812932085119"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_b812932085119"></a>Example</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row821411541852"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p15264191183511"><a name="p15264191183511"></a><a name="p15264191183511"></a>x-sdk-date</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="p1926814111357"><a name="p1926814111357"></a><a name="p1926814111357"></a>Time when the request is sent. The time is in <strong id="b1911116118"><a name="b1911116118"></a><a name="b1911116118"></a>YYYYMMDD'T'HHMMSS'Z'</strong> format.</p>
<p id="p13270111103511"><a name="p13270111103511"></a><a name="p13270111103511"></a>The value is the current GMT time of the system.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="p202731111356"><a name="p202731111356"></a><a name="p202731111356"></a>No</p>
<p id="p102751114359"><a name="p102751114359"></a><a name="p102751114359"></a>This parameter is mandatory for AK/SK authentication.</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="p1427891113519"><a name="p1427891113519"></a><a name="p1427891113519"></a>20150907T101459Z</p>
</td>
</tr>
<tr id="en-us_topic_0171007788_en-us_topic_0121682347_row1286861153311"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p2086813163316"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p2086813163316"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p2086813163316"></a>Host</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p58681814333"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p58681814333"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p58681814333"></a>Server information of the resource being requested. The value can be obtained from the URL of the service API. The value is in the format of <em id="en-us_topic_0171007788_en-us_topic_0121682347_i1012185414574"><a name="en-us_topic_0171007788_en-us_topic_0121682347_i1012185414574"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_i1012185414574"></a>hostname[:port]</em>. If the port number is not specified, the default port is used. The default port number for HTTPS is <strong id="b1343812411410"><a name="b1343812411410"></a><a name="b1343812411410"></a>443</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p886815123319"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p886815123319"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p886815123319"></a>No</p>
<p id="en-us_topic_0171007788_en-us_topic_0121682347_p386811116333"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p386811116333"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p386811116333"></a>This parameter is mandatory for AK/SK authentication.</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p486814118330"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p486814118330"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p486814118330"></a>code.test.com</p>
<p id="en-us_topic_0171007788_en-us_topic_0121682347_p5868161163317"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p5868161163317"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p5868161163317"></a>or</p>
<p id="en-us_topic_0171007788_en-us_topic_0121682347_p786841123315"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p786841123315"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p786841123315"></a>code.test.com:443</p>
</td>
</tr>
<tr id="en-us_topic_0171007788_en-us_topic_0121682347_row386818143313"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p118689123320"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p118689123320"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p118689123320"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p1486815116337"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p1486815116337"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p1486815116337"></a>Request body MIME type. You are advised to use the default value <strong id="en-us_topic_0171007788_en-us_topic_0121682347_b842352706171425"><a name="en-us_topic_0171007788_en-us_topic_0121682347_b842352706171425"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_b842352706171425"></a>application/json</strong>. For APIs used to upload objects or images, the value can vary depending on the flow type.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p1086812114335"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p1086812114335"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p1086812114335"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p1186841163310"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p1186841163310"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p1186841163310"></a>application/json</p>
</td>
</tr>
<tr id="en-us_topic_0171007788_en-us_topic_0121682347_row11868419337"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p178687119330"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p178687119330"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p178687119330"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p178681813332"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p178681813332"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p178681813332"></a>Length of the request body. The unit is byte.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p18687183316"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p18687183316"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p18687183316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p148689110334"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p148689110334"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p148689110334"></a>3495</p>
</td>
</tr>
<tr id="en-us_topic_0171007788_en-us_topic_0121682347_row2868171143313"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p586815118338"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p586815118338"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p586815118338"></a>X-Project-Id</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p1586811163312"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p1586811163312"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p1586811163312"></a>Project ID. Obtain the project ID by following the instructions in <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p886812110335"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p886812110335"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p886812110335"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p198684143315"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p198684143315"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p198684143315"></a>e9993fc787d94b6c886cbaa340f9c0f4</p>
</td>
</tr>
<tr id="en-us_topic_0171007788_en-us_topic_0121682347_row188688113337"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p198684111335"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p198684111335"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p198684111335"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p1086851153317"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p1086851153317"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p1086851153317"></a>User token,</p>
<p id="en-us_topic_0171007788_en-us_topic_0121682347_p1057635831"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p1057635831"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p1057635831"></a>which is a response to the API for obtaining a user token (only this API does not require authentication).</p>
<p id="en-us_topic_0171007788_en-us_topic_0121682347_p15868417337"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p15868417337"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p15868417337"></a>The <strong id="b232885320109"><a name="b232885320109"></a><a name="b232885320109"></a>X-Subject-Token</strong> value contained in the returned message header is the token.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p4868514338"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p4868514338"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p4868514338"></a>No</p>
<p id="en-us_topic_0171007788_en-us_topic_0121682347_p986818114339"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p986818114339"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p986818114339"></a>This field is mandatory for token authentication.</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0171007788_en-us_topic_0121682347_p27152505302"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p27152505302"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p27152505302"></a>The following is part of an example token:</p>
<p id="en-us_topic_0171007788_en-us_topic_0121682347_p168689113318"><a name="en-us_topic_0171007788_en-us_topic_0121682347_p168689113318"></a><a name="en-us_topic_0171007788_en-us_topic_0121682347_p168689113318"></a>MIIPAgYJKoZIhvcNAQcCo...ggg1BBIINPXsidG9rZ</p>
</td>
</tr>
<tr id="row87451312414"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p5388211133515"><a name="p5388211133515"></a><a name="p5388211133515"></a>X-Language</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="p16391101119350"><a name="p16391101119350"></a><a name="p16391101119350"></a>Request language.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="p539461143514"><a name="p539461143514"></a><a name="p539461143514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="p439731173518"><a name="p439731173518"></a><a name="p439731173518"></a>en_us</p>
</td>
</tr>
</tbody>
</table>

The API for obtaining a user token does not require authentication. Therefore, this API only requires adding the  **Content-Type**  field. The request with the added  **Content-Type**  header is as follows:

```
POST https://iam.eu-de.otc.t-systems.com/v3/auth/tokens
Content-Type: application/json
```

## Request Body<a name="en-us_topic_0171007788_en-us_topic_0121682347_en-us_topic_0113746487_section1437471411"></a>

A request body is generally sent in a structured format \(JSON or XML\). It corresponds to  **Content-Type**  in the request header and transfers data except for the request header. If the request body contains Chinese characters, these characters must be coded in UTF-8.

The request body varies according to the APIs. Certain APIs do not require the request body, such as the GET and DELETE APIs.

For the API of obtaining a user token, obtain the request parameters and parameter description in the API request. The following section provides an example request with the body included. Set username \(first  **name**\), domain name \(second  **name**\), login password \(**password**\), and project ID \(**id**\) as required. For details about parameter settings, see  [Obtaining a Project ID](obtaining-a-project-id.md).

>![](/images/icon-note.gif) **NOTE:**   
>**scope**  specifies where a token takes effect. In the following example, the token takes effect only on the resources specified by the project ID. In the following example, the token takes effect only on the resources specified by the project ID. You can set the  **scope**  to a domain or a project under a domain. For details, see Obtaining a User Token.  

```
POST https://iam.eu-de.otc.t-systems.com/v3/auth/tokens
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

If all data required by a request is available, you can send the request to call an API through  [curl](https://curl.haxx.se/),  [Postman](https://www.getpostman.com/), or coding. For the API of obtaining a user token,  **x-subject-token**  in the response header is the desired user token. Then, you can use the token to authenticate the calling of other APIs.

