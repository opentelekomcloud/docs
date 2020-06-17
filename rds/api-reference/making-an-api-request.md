# Making an API Request<a name="rds_03_0005"></a>

This section describes the structure of a REST API, and uses the IAM API for  [obtaining a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html)  as an example to describe how to call an API. The obtained token is used to authenticate the calling of other APIs.

## Request URI<a name="en-us_topic_0113746487_section697653216219"></a>

A request URI consists of the following:

**\{URI-scheme\}://\{Endpoint\}/\{resource-path\}?\{query-string\}**

Although a request URI is included in a request header, most programming languages or frameworks require the request URI to be separately transmitted, rather than being conveyed in a request message.

**Table  1**  Parameters in a URI

<a name="en-us_topic_0113746487_table4443194632512"></a>
<table><thead align="left"><tr id="en-us_topic_0113746487_row1944414616258"><th class="cellrowborder" valign="top" width="19.48%" id="mcps1.2.3.1.1"><p id="en-us_topic_0113746487_p1644484692510"><a name="en-us_topic_0113746487_p1644484692510"></a><a name="en-us_topic_0113746487_p1644484692510"></a><strong id="b84235270618284"><a name="b84235270618284"></a><a name="b84235270618284"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="80.52%" id="mcps1.2.3.1.2"><p id="en-us_topic_0113746487_p174441146142511"><a name="en-us_topic_0113746487_p174441146142511"></a><a name="en-us_topic_0113746487_p174441146142511"></a><strong id="b84235270611143"><a name="b84235270611143"></a><a name="b84235270611143"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0113746487_row10444144620259"><td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p154446465251"><a name="en-us_topic_0113746487_p154446465251"></a><a name="en-us_topic_0113746487_p154446465251"></a>URI-scheme</p>
</td>
<td class="cellrowborder" valign="top" width="80.52%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p8444144692517"><a name="en-us_topic_0113746487_p8444144692517"></a><a name="en-us_topic_0113746487_p8444144692517"></a>Protocol used to transmit requests. All APIs use HTTPS.</p>
</td>
</tr>
<tr id="en-us_topic_0113746487_row444414692513"><td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p7444194610257"><a name="en-us_topic_0113746487_p7444194610257"></a><a name="en-us_topic_0113746487_p7444194610257"></a>Endpoint</p>
</td>
<td class="cellrowborder" valign="top" width="80.52%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p244474613259"><a name="en-us_topic_0113746487_p244474613259"></a><a name="en-us_topic_0113746487_p244474613259"></a>Domain name or IP address of the server bearing the REST service. The endpoint varies between services in different regions. It can be obtained from <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0113746487_row1744454612520"><td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p14442468257"><a name="en-us_topic_0113746487_p14442468257"></a><a name="en-us_topic_0113746487_p14442468257"></a>resource-path</p>
</td>
<td class="cellrowborder" valign="top" width="80.52%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p1844412467258"><a name="en-us_topic_0113746487_p1844412467258"></a><a name="en-us_topic_0113746487_p1844412467258"></a>Access path of an API for performing a specified operation. Obtain the path from the URI of an API. For example, the <span class="parmname" id="parmname10118203265616"><a name="parmname10118203265616"></a><a name="parmname10118203265616"></a><b>resource-path</b></span> of the API used to obtain a user token is <span class="parmvalue" id="parmvalue51182032175615"><a name="parmvalue51182032175615"></a><a name="parmvalue51182032175615"></a><b>/v3/auth/tokens</b></span>.</p>
</td>
</tr>
<tr id="en-us_topic_0113746487_row184441346152515"><td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p4444154692516"><a name="en-us_topic_0113746487_p4444154692516"></a><a name="en-us_topic_0113746487_p4444154692516"></a>query-string</p>
</td>
<td class="cellrowborder" valign="top" width="80.52%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p1444414622514"><a name="en-us_topic_0113746487_p1444414622514"></a><a name="en-us_topic_0113746487_p1444414622514"></a>Query parameter, which is optional. Ensure that a question mark (?) is included before each query parameter that is in the format of "Parameter name=Parameter value". For example, <strong id="b1670793219241"><a name="b1670793219241"></a><a name="b1670793219241"></a>? limit=10</strong> indicates that a maximum of 10 data records will be displayed.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>To simplify the URI display in this document, each API is provided only with a resource-path and a request method. The  **URI-scheme**  of all APIs is  **HTTPS**, and the endpoints of all APIs in the same region are identical.  

## Request Methods<a name="en-us_topic_0113746487_section5296154118345"></a>

The HTTP protocol defines the following request methods that can be used to send a request to the server:

**Table  2**  HTTP methods

<a name="en-us_topic_0113746487_table1961229113819"></a>
<table><thead align="left"><tr id="en-us_topic_0113746487_row86141913816"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="en-us_topic_0113746487_p186147910387"><a name="en-us_topic_0113746487_p186147910387"></a><a name="en-us_topic_0113746487_p186147910387"></a><strong id="b84235270616346"><a name="b84235270616346"></a><a name="b84235270616346"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="en-us_topic_0113746487_p166141293387"><a name="en-us_topic_0113746487_p166141293387"></a><a name="en-us_topic_0113746487_p166141293387"></a><strong id="b7106036145712"><a name="b7106036145712"></a><a name="b7106036145712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0113746487_row146141194381"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p12831539123914"><a name="en-us_topic_0113746487_p12831539123914"></a><a name="en-us_topic_0113746487_p12831539123914"></a>GET</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p2831123916397"><a name="en-us_topic_0113746487_p2831123916397"></a><a name="en-us_topic_0113746487_p2831123916397"></a>Requests the server to return specified resources.</p>
</td>
</tr>
<tr id="en-us_topic_0113746487_row161429103817"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p3831239183912"><a name="en-us_topic_0113746487_p3831239183912"></a><a name="en-us_topic_0113746487_p3831239183912"></a>PUT</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p178311939193911"><a name="en-us_topic_0113746487_p178311939193911"></a><a name="en-us_topic_0113746487_p178311939193911"></a>Requests the server to update specified resources.</p>
</td>
</tr>
<tr id="en-us_topic_0113746487_row56141190384"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p68311239113912"><a name="en-us_topic_0113746487_p68311239113912"></a><a name="en-us_topic_0113746487_p68311239113912"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p1583133918391"><a name="en-us_topic_0113746487_p1583133918391"></a><a name="en-us_topic_0113746487_p1583133918391"></a>Requests the server to add resources or perform special operations.</p>
</td>
</tr>
<tr id="en-us_topic_0113746487_row861411903812"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p1183153943916"><a name="en-us_topic_0113746487_p1183153943916"></a><a name="en-us_topic_0113746487_p1183153943916"></a>DELETE</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p6831163914392"><a name="en-us_topic_0113746487_p6831163914392"></a><a name="en-us_topic_0113746487_p6831163914392"></a>Requests the server to delete specified resources, for example, an object.</p>
</td>
</tr>
<tr id="en-us_topic_0113746487_row2614199163812"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p1483143915390"><a name="en-us_topic_0113746487_p1483143915390"></a><a name="en-us_topic_0113746487_p1483143915390"></a>PATCH</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p17831173918394"><a name="en-us_topic_0113746487_p17831173918394"></a><a name="en-us_topic_0113746487_p17831173918394"></a>Requests the server to update partial content of a specified resource.</p>
<p id="en-us_topic_0113746487_p9831123911390"><a name="en-us_topic_0113746487_p9831123911390"></a><a name="en-us_topic_0113746487_p9831123911390"></a>If the resource does not exist, a new resource will be created.</p>
</td>
</tr>
</tbody>
</table>

For example, in the case of the API used to  [obtain a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html), the request method is POST. The request is as follows:

## Request Header<a name="section479119143310"></a>

You can also add additional fields to a request, such as the fields required by a specified URI or an HTTP method. For example, to request for the authentication information, add  **Content-Type**, which specifies the request body type.

[Table 3](#table1986821153312)  lists common request header fields.

**Table  3**  Common request headers

<a name="table1986821153312"></a>
<table><thead align="left"><tr id="row1286841153311"><th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.1"><p id="p178680183310"><a name="p178680183310"></a><a name="p178680183310"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.5%" id="mcps1.2.5.1.2"><p id="p78688118335"><a name="p78688118335"></a><a name="p78688118335"></a><strong id="b16629161878"><a name="b16629161878"></a><a name="b16629161878"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.11%" id="mcps1.2.5.1.3"><p id="p58686123316"><a name="p58686123316"></a><a name="p58686123316"></a><strong id="b1652015178718"><a name="b1652015178718"></a><a name="b1652015178718"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.650000000000006%" id="mcps1.2.5.1.4"><p id="p48681314333"><a name="p48681314333"></a><a name="p48681314333"></a><strong id="b842352706103845"><a name="b842352706103845"></a><a name="b842352706103845"></a>Example</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1286861153311"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p2086813163316"><a name="p2086813163316"></a><a name="p2086813163316"></a>Host</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="p58681814333"><a name="p58681814333"></a><a name="p58681814333"></a>Specifies the requested server information, which can be obtained from the URL of the service API. The value is in the <em id="i19094210714"><a name="i19094210714"></a><a name="i19094210714"></a>hostname[:port]</em> format. If the port number is not specified, the default port is used. The default port number for <strong id="b5371537315524"><a name="b5371537315524"></a><a name="b5371537315524"></a>https</strong> is <strong id="b1367631015524"><a name="b1367631015524"></a><a name="b1367631015524"></a>443</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="p886815123319"><a name="p886815123319"></a><a name="p886815123319"></a>No</p>
<p id="p386811116333"><a name="p386811116333"></a><a name="p386811116333"></a>This parameter is mandatory for AK/SK authentication.</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="p486814118330"><a name="p486814118330"></a><a name="p486814118330"></a>code.test.com</p>
<p id="p5868161163317"><a name="p5868161163317"></a><a name="p5868161163317"></a>or</p>
<p id="p786841123315"><a name="p786841123315"></a><a name="p786841123315"></a>code.test.com:443</p>
</td>
</tr>
<tr id="row386818143313"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p118689123320"><a name="p118689123320"></a><a name="p118689123320"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="p1486815116337"><a name="p1486815116337"></a><a name="p1486815116337"></a>Specifies the MIME type of the request body. You are advised to use the default value <strong id="en-us_topic_0121682347_b842352706171425"><a name="en-us_topic_0121682347_b842352706171425"></a><a name="en-us_topic_0121682347_b842352706171425"></a>application/json</strong>. For APIs used to upload objects or images, the value can vary depending on the flow type.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="p1086812114335"><a name="p1086812114335"></a><a name="p1086812114335"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="p1186841163310"><a name="p1186841163310"></a><a name="p1186841163310"></a>application/json</p>
</td>
</tr>
<tr id="row11868419337"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p178687119330"><a name="p178687119330"></a><a name="p178687119330"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="p178681813332"><a name="p178681813332"></a><a name="p178681813332"></a>Specifies the length of the request body. The unit is byte.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="p18687183316"><a name="p18687183316"></a><a name="p18687183316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="p148689110334"><a name="p148689110334"></a><a name="p148689110334"></a>3495</p>
</td>
</tr>
<tr id="row2868171143313"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p586815118338"><a name="p586815118338"></a><a name="p586815118338"></a>X-Project-Id</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="p1586811163312"><a name="p1586811163312"></a><a name="p1586811163312"></a>Specifies the project ID. Obtain the project ID by following the instructions in <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="p886812110335"><a name="p886812110335"></a><a name="p886812110335"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="p198684143315"><a name="p198684143315"></a><a name="p198684143315"></a>e9993fc787d94b6c886cbaa340f9c0f4</p>
</td>
</tr>
<tr id="row188688113337"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p198684111335"><a name="p198684111335"></a><a name="p198684111335"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.5.1.2 "><p id="p1086851153317"><a name="p1086851153317"></a><a name="p1086851153317"></a>Specifies the user token.</p>
<p id="p1057635831"><a name="p1057635831"></a><a name="p1057635831"></a>The user token is a response to the API used to <a href="https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html" target="_blank" rel="noopener noreferrer">obtain a user token</a>. This API is the only one that does not require authentication.</p>
<p id="p15868417337"><a name="p15868417337"></a><a name="p15868417337"></a>After the request is processed, the value of <strong id="b842352706205322"><a name="b842352706205322"></a><a name="b842352706205322"></a>X-Subject-Token</strong> in the message header is the token value.</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.5.1.3 "><p id="p4868514338"><a name="p4868514338"></a><a name="p4868514338"></a>No</p>
<p id="p986818114339"><a name="p986818114339"></a><a name="p986818114339"></a>This parameter is mandatory for token authentication.</p>
</td>
<td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.2.5.1.4 "><p id="p27152505302"><a name="p27152505302"></a><a name="p27152505302"></a>The following is part of an example token:</p>
<p id="p168689113318"><a name="p168689113318"></a><a name="p168689113318"></a>MIIPAgYJKoZIhvcNAQcCo...ggg1BBIINPXsidG9rZ</p>
</td>
</tr>
</tbody>
</table>

The API used to  [obtain a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html)  does not require authentication. Therefore, only the  **Content-Type**  field needs to be added to requests for calling the API. An example of such requests is as follows:

## \(Optional\) Request Body<a name="en-us_topic_0113746487_section1437471411"></a>

This part is optional. The body of a request is often sent in a structured format \(for example, JSON or XML\) as specified in the  **Content-Type**  header field. If the request body contains Chinese characters, these characters must be coded in UTF-8.

The request body varies between APIs. Some APIs do not require the request body, such as the APIs requested using the GET and DELETE methods.

In the case of the API used to  [obtain a user token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html), the request parameters and parameter description can be obtained from the API request. The following provides an example request with a body included. Replace  _**username**_,  _**domainname**_,  **_\*\*\*\*\*\*\*\*_**  \(login password\), and  **_xxxxxxxxxxxxxxxxxx_**  \(project name\) with actual values. You can obtain the values from  [Regions and Endpoints](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

>![](/images/icon-note.gif) **NOTE:**   
>The  **scope**  parameter specifies where a token takes effect. You can set  **scope**  to an account or a project under an account. In the following example, the token takes effect only for the resources in a specified project. For more information about this API, see  [Obtaining a User Token](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845583.html).  

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

