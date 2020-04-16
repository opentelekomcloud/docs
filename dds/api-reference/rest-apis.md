# REST APIs<a name="dds_api_0016"></a>

API requests sent by third-party applications to public cloud services must be authenticated using signatures.

Public cloud APIs follow RESTful API design rules.

In REST, specific information or data on a network is represented by resources. REST allows users to access service resources by creating, querying, updating, and deleting resources.

A REST API request and response are divided into the following parts:

-   Request URI
-   Request header
-   Request body
-   Response header
-   Response body

## Request URI<a name="en-us_topic_0113746487_section697653216219"></a>

A request URI consists of the following:

**\{URI-scheme\}://\{Endpoint\}/\{resource-path\}?\{query-string\}**

Although a request URI is included in a request header, most programming languages or frameworks require the request URI to be separately transmitted, rather than being conveyed in a request message.

**Table  1**  Parameters in a URI

<a name="en-us_topic_0113746487_table4443194632512"></a>
<table><thead align="left"><tr id="en-us_topic_0113746487_row1944414616258"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.3.1.1"><p id="en-us_topic_0113746487_p1644484692510"><a name="en-us_topic_0113746487_p1644484692510"></a><a name="en-us_topic_0113746487_p1644484692510"></a><strong id="b205415181362"><a name="b205415181362"></a><a name="b205415181362"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="74%" id="mcps1.2.3.1.2"><p id="en-us_topic_0113746487_p174441146142511"><a name="en-us_topic_0113746487_p174441146142511"></a><a name="en-us_topic_0113746487_p174441146142511"></a><strong id="b130291913610"><a name="b130291913610"></a><a name="b130291913610"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0113746487_row10444144620259"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p154446465251"><a name="en-us_topic_0113746487_p154446465251"></a><a name="en-us_topic_0113746487_p154446465251"></a>URI-scheme</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p8444144692517"><a name="en-us_topic_0113746487_p8444144692517"></a><a name="en-us_topic_0113746487_p8444144692517"></a>Specifies the protocol used for transmitting requests.</p>
</td>
</tr>
<tr id="en-us_topic_0113746487_row444414692513"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p7444194610257"><a name="en-us_topic_0113746487_p7444194610257"></a><a name="en-us_topic_0113746487_p7444194610257"></a>Endpoint</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p244474613259"><a name="en-us_topic_0113746487_p244474613259"></a><a name="en-us_topic_0113746487_p244474613259"></a>Specifies the domain name or IP address of the server bearing the REST service endpoint.</p>
<p id="p716619178377"><a name="p716619178377"></a><a name="p716619178377"></a>To obtain the parameter value, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0113746487_row1744454612520"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p14442468257"><a name="en-us_topic_0113746487_p14442468257"></a><a name="en-us_topic_0113746487_p14442468257"></a>resource-path</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p1844412467258"><a name="en-us_topic_0113746487_p1844412467258"></a><a name="en-us_topic_0113746487_p1844412467258"></a>Specifies the API access path for performing a specified operation. Obtain this value from the URI of the API, for example, <strong id="b842352706134656"><a name="b842352706134656"></a><a name="b842352706134656"></a>v3/auth/tokens</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0113746487_row184441346152515"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p4444154692516"><a name="en-us_topic_0113746487_p4444154692516"></a><a name="en-us_topic_0113746487_p4444154692516"></a>query-string</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p1444414622514"><a name="en-us_topic_0113746487_p1444414622514"></a><a name="en-us_topic_0113746487_p1444414622514"></a>This parameter is optional. For example, you can set it to API version or resource selection criteria.</p>
</td>
</tr>
</tbody>
</table>

## Request Methods<a name="en-us_topic_0113746487_section5296154118345"></a>

HTTP methods, which are also called operations or actions, specify the type of operations that you are requesting.

**Table  2**  HTTP methods

<a name="en-us_topic_0113746487_table1961229113819"></a>
<table><thead align="left"><tr id="en-us_topic_0113746487_row86141913816"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="en-us_topic_0113746487_p186147910387"><a name="en-us_topic_0113746487_p186147910387"></a><a name="en-us_topic_0113746487_p186147910387"></a><strong id="en-us_topic_0113746487_b1093312238395"><a name="en-us_topic_0113746487_b1093312238395"></a><a name="en-us_topic_0113746487_b1093312238395"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="en-us_topic_0113746487_p166141293387"><a name="en-us_topic_0113746487_p166141293387"></a><a name="en-us_topic_0113746487_p166141293387"></a><strong id="b18836332155546"><a name="b18836332155546"></a><a name="b18836332155546"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0113746487_row146141194381"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p12831539123914"><a name="en-us_topic_0113746487_p12831539123914"></a><a name="en-us_topic_0113746487_p12831539123914"></a>GET</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p2831123916397"><a name="en-us_topic_0113746487_p2831123916397"></a><a name="en-us_topic_0113746487_p2831123916397"></a>Requests a server to return the specified resources.</p>
</td>
</tr>
<tr id="en-us_topic_0113746487_row56141190384"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p68311239113912"><a name="en-us_topic_0113746487_p68311239113912"></a><a name="en-us_topic_0113746487_p68311239113912"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p1583133918391"><a name="en-us_topic_0113746487_p1583133918391"></a><a name="en-us_topic_0113746487_p1583133918391"></a>Requests a server to add resources or perform special operations.</p>
</td>
</tr>
<tr id="en-us_topic_0113746487_row861411903812"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0113746487_p1183153943916"><a name="en-us_topic_0113746487_p1183153943916"></a><a name="en-us_topic_0113746487_p1183153943916"></a>DELETE</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0113746487_p6831163914392"><a name="en-us_topic_0113746487_p6831163914392"></a><a name="en-us_topic_0113746487_p6831163914392"></a>Requests a server to delete a specific resource, for example, an object.</p>
</td>
</tr>
</tbody>
</table>

## Request Header<a name="section479119143310"></a>

You can also add additional fields to the request header, for example, the fields required by a specified URI and an HTTP method.  [Table 3](#table18389930)  lists common request header fields.

**Table  3**  Common request headers

<a name="table18389930"></a>
<table><thead align="left"><tr id="row24749807"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p58577354"><a name="p58577354"></a><a name="p58577354"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p47145209"><a name="p47145209"></a><a name="p47145209"></a><strong id="b84235270611143"><a name="b84235270611143"></a><a name="b84235270611143"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p60665573"><a name="p60665573"></a><a name="p60665573"></a><strong id="en-us_topic_0091754394_b842352706102346"><a name="en-us_topic_0091754394_b842352706102346"></a><a name="en-us_topic_0091754394_b842352706102346"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p14964341"><a name="p14964341"></a><a name="p14964341"></a><strong id="b842352706103845"><a name="b842352706103845"></a><a name="b842352706103845"></a>Example</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row4152081"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p774306"><a name="p774306"></a><a name="p774306"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p62718864"><a name="p62718864"></a><a name="p62718864"></a>Specifies the MIME type of the request body.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p47063234"><a name="p47063234"></a><a name="p47063234"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p54025633"><a name="p54025633"></a><a name="p54025633"></a>application/json</p>
</td>
</tr>
<tr id="row16468652"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p58892473"><a name="p58892473"></a><a name="p58892473"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p5560998"><a name="p5560998"></a><a name="p5560998"></a>Specifies the length of the request body. The unit is byte.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p47787675"><a name="p47787675"></a><a name="p47787675"></a>This parameter is optional for POST requests, but must be left blank for GET requests.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p45596481"><a name="p45596481"></a><a name="p45596481"></a>3495</p>
</td>
</tr>
<tr id="row102809013611"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5563313"><a name="p5563313"></a><a name="p5563313"></a>X-Project-Id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p47975183"><a name="p47975183"></a><a name="p47975183"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p60784581"><a name="p60784581"></a><a name="p60784581"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p24604028"><a name="p24604028"></a><a name="p24604028"></a>e9993fc787d94b6c886cbaa340f9c0f4</p>
</td>
</tr>
<tr id="row7715150"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p20947391"><a name="p20947391"></a><a name="p20947391"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p19017142"><a name="p19017142"></a><a name="p19017142"></a>Specifies the user token.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p63993496"><a name="p63993496"></a><a name="p63993496"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p16090703"><a name="p16090703"></a><a name="p16090703"></a>-</p>
</td>
</tr>
</tbody>
</table>

## \(Optional\) Request Body<a name="en-us_topic_0113746487_section1437471411"></a>

A request body is generally sent in a structured format \(for example, JSON or XML\), corresponding to  **Content-Type**  in the request header, and is used to transfer content other than the request header.

If the request body contains Chinese characters, convert the Chinese characters into the UTF-8 encoding format.

## Response Headers<a name="en-us_topic_0113746487_section61333484715"></a>

A response header consists of the following two parts:

-   An HTTP status code, which is a service-defined status code indicating a success or an error
-   Additional fields, for example  **Content-Type**

    [Table 4](#en-us_topic_0113746487_en-us_topic_0020536997_table3877208613139)  lists common response header fields.

    **Table  4**  Common response headers

    <a name="en-us_topic_0113746487_en-us_topic_0020536997_table3877208613139"></a>
    <table><thead align="left"><tr id="en-us_topic_0113746487_en-us_topic_0020536997_row3771309013139"><th class="cellrowborder" valign="top" width="19.15%" id="mcps1.2.4.1.1"><p id="p66697461"><a name="p66697461"></a><a name="p66697461"></a><strong id="b853217512492"><a name="b853217512492"></a><a name="b853217512492"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.830000000000005%" id="mcps1.2.4.1.2"><p id="p33785274"><a name="p33785274"></a><a name="p33785274"></a><strong id="b1257416612495"><a name="b1257416612495"></a><a name="b1257416612495"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.019999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0113746487_en-us_topic_0020536997_p5162099210429"><a name="en-us_topic_0113746487_en-us_topic_0020536997_p5162099210429"></a><a name="en-us_topic_0113746487_en-us_topic_0020536997_p5162099210429"></a><strong id="b66630724911"><a name="b66630724911"></a><a name="b66630724911"></a>Example</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0113746487_en-us_topic_0020536997_row1673548413139"><td class="cellrowborder" valign="top" width="19.15%" headers="mcps1.2.4.1.1 "><p id="p45638969"><a name="p45638969"></a><a name="p45638969"></a>Date</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.830000000000005%" headers="mcps1.2.4.1.2 "><p id="p5769005"><a name="p5769005"></a><a name="p5769005"></a>Standard HTTP header field, which represents the date and time at which the message was originated. The format is defined by RFC 822.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0113746487_en-us_topic_0020536997_p59381193104213"><a name="en-us_topic_0113746487_en-us_topic_0020536997_p59381193104213"></a><a name="en-us_topic_0113746487_en-us_topic_0020536997_p59381193104213"></a>Wed, 27 Dec 2018 06:49:46 GMT</p>
    </td>
    </tr>
    <tr id="row89631076206"><td class="cellrowborder" valign="top" width="19.15%" headers="mcps1.2.4.1.1 "><p id="p14341151362016"><a name="p14341151362016"></a><a name="p14341151362016"></a>Content-Length</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.830000000000005%" headers="mcps1.2.4.1.2 "><p id="p93417134203"><a name="p93417134203"></a><a name="p93417134203"></a>Standard HTTP header field, which specifies the size of the entity body, in decimal number of bytes, sent to the recipient.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.4.1.3 "><p id="p63435135202"><a name="p63435135202"></a><a name="p63435135202"></a>-</p>
    </td>
    </tr>
    <tr id="en-us_topic_0113746487_en-us_topic_0020536997_row2720466144725"><td class="cellrowborder" valign="top" width="19.15%" headers="mcps1.2.4.1.1 "><p id="p44855704"><a name="p44855704"></a><a name="p44855704"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.830000000000005%" headers="mcps1.2.4.1.2 "><p id="p445862101910"><a name="p445862101910"></a><a name="p445862101910"></a>Standard HTTP header field, which specifies the media type of the entity body sent to the recipient.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0113746487_en-us_topic_0020536997_p21477025104246"><a name="en-us_topic_0113746487_en-us_topic_0020536997_p21477025104246"></a><a name="en-us_topic_0113746487_en-us_topic_0020536997_p21477025104246"></a>application/json</p>
    </td>
    </tr>
    </tbody>
    </table>


## \(Optional\) Response Body<a name="en-us_topic_0113746487_section2045571671419"></a>

A response body is generally returned in a structured format \(for example, JSON or XML\), corresponding to  **Content-Type**  in the response header, and is used to transfer content other than the response header.

