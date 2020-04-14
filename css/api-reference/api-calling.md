# API Calling<a name="css_03_0006"></a>

Public cloud services provide RESTful APIs. Representational State Transfer \(REST\) allocates Uniform Resource Identifiers \(URIs\) to dispersed resources so that the resources can be located. Applications on clients use unified resource locators \(URLs\) to obtain the resources. The URL is in the following format:  **https://_Endpoint/uri_**.  **uri**  indicates the resource path. That is, the API access path.

Public cloud APIs use HTTPS as the transmission protocol. Requests/Responses are transmitted by using JSON packets, with media type represented by  **Application/json**.

## REST APIs<a name="section5507642125011"></a>

CSS provides REST APIs.

In REST, specific information or data on a network is represented by resources. REST allows users to access service resources by creating, querying, updating, and deleting resources.

A RESTful API request or response consists of the following five parts:

-   Request URI

    A request URI consists of the following:

    **\{URI-scheme\} :// \{**Endpoint**\} / \{resource-path\} ? \{query-string\}**

    Although the request URI is included in the request header, most languages or frameworks require that it be transmitted separately from the request message. Therefore, the request URI is listed independently.

    **Table  1**  Parameters in a URI

    <a name="t1797260c744a4e1a85d354f259cae55a"></a>
    <table><thead align="left"><tr id="r6dceed05bcc649d2b032accbb2980a31"><th class="cellrowborder" valign="top" width="24.529999999999998%" id="mcps1.2.3.1.1"><p id="a3446b6b785cb432bae9f45aef9177041"><a name="a3446b6b785cb432bae9f45aef9177041"></a><a name="a3446b6b785cb432bae9f45aef9177041"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="75.47%" id="mcps1.2.3.1.2"><p id="abe71244a12ac45308e99d4bbf975a9f8"><a name="abe71244a12ac45308e99d4bbf975a9f8"></a><a name="abe71244a12ac45308e99d4bbf975a9f8"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row106982018513"><td class="cellrowborder" valign="top" width="24.529999999999998%" headers="mcps1.2.3.1.1 "><p id="p136991001517"><a name="p136991001517"></a><a name="p136991001517"></a>URI-scheme</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.47%" headers="mcps1.2.3.1.2 "><p id="p56992017520"><a name="p56992017520"></a><a name="p56992017520"></a>Specifies the protocol used for transmitting requests.</p>
    </td>
    </tr>
    <tr id="rb217758afff146a1b40b0dcbb28a4ae1"><td class="cellrowborder" valign="top" width="24.529999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0035614179_p480227019422"><a name="en-us_topic_0035614179_p480227019422"></a><a name="en-us_topic_0035614179_p480227019422"></a>Endpoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.47%" headers="mcps1.2.3.1.2 "><p id="ad82b3484a1be43ddadf436efbe15285e"><a name="ad82b3484a1be43ddadf436efbe15285e"></a><a name="ad82b3484a1be43ddadf436efbe15285e"></a>Name of the server used by the request, which is obtained from <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
    </td>
    </tr>
    <tr id="refeed61892004ea682639be281a1a707"><td class="cellrowborder" valign="top" width="24.529999999999998%" headers="mcps1.2.3.1.1 "><p id="p1797614317513"><a name="p1797614317513"></a><a name="p1797614317513"></a>resource-path</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.47%" headers="mcps1.2.3.1.2 "><p id="a90409cbb8b1c49c4ad4d3cfee16f475e"><a name="a90409cbb8b1c49c4ad4d3cfee16f475e"></a><a name="a90409cbb8b1c49c4ad4d3cfee16f475e"></a>Resource path, that is, API access path for performing a specified operation. Obtain this value from the URI of a specific API, for example, <strong id="b842352706112757"><a name="b842352706112757"></a><a name="b842352706112757"></a>v3/auth/tokens</strong>.</p>
    </td>
    </tr>
    <tr id="row19939365518"><td class="cellrowborder" valign="top" width="24.529999999999998%" headers="mcps1.2.3.1.1 "><p id="p393966455"><a name="p393966455"></a><a name="p393966455"></a>Query string</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.47%" headers="mcps1.2.3.1.2 "><p id="p159401867517"><a name="p159401867517"></a><a name="p159401867517"></a>This parameter is optional. You can set it to the API version or resource selection criteria.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request method

    HTTPS methods, which are also called operations or actions, specify the type of operations that you are requesting.

    **Table  2**  HTTPS methods

    <a name="table26515221161"></a>
    <table><thead align="left"><tr id="row10728192251616"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.3.1.1"><p id="p157281422201616"><a name="p157281422201616"></a><a name="p157281422201616"></a>Method</p>
    </th>
    <th class="cellrowborder" valign="top" width="82%" id="mcps1.2.3.1.2"><p id="p672872219161"><a name="p672872219161"></a><a name="p672872219161"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1394642154919"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p13848247114919"><a name="p13848247114919"></a><a name="p13848247114919"></a>GET</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p2850147164917"><a name="p2850147164917"></a><a name="p2850147164917"></a>Requests the server to return the specified resource.</p>
    </td>
    </tr>
    <tr id="row5728322121617"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p97281922111616"><a name="p97281922111616"></a><a name="p97281922111616"></a>PUT</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p1572882241617"><a name="p1572882241617"></a><a name="p1572882241617"></a>Requests the server to update the specified resource.</p>
    </td>
    </tr>
    <tr id="row172872211168"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p472820225166"><a name="p472820225166"></a><a name="p472820225166"></a>POST</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p272812212161"><a name="p272812212161"></a><a name="p272812212161"></a>Requests the server to add a resource or perform special operations.</p>
    </td>
    </tr>
    <tr id="row8728132231620"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p16729422151616"><a name="p16729422151616"></a><a name="p16729422151616"></a>DELETE</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p10729122261616"><a name="p10729122261616"></a><a name="p10729122261616"></a>Requests the server to delete the specified resource, for example, an object.</p>
    </td>
    </tr>
    <tr id="row2157183019175"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p15159030201715"><a name="p15159030201715"></a><a name="p15159030201715"></a>HEAD</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p42261787492"><a name="p42261787492"></a><a name="p42261787492"></a>Requests the server resource header. </p>
    </td>
    </tr>
    <tr id="row16729182210163"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p1772932218162"><a name="p1772932218162"></a><a name="p1772932218162"></a>PATCH</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p13729192251620"><a name="p13729192251620"></a><a name="p13729192251620"></a>Requests the server to apply partial modifications to a resource.</p>
    <p id="p0729142221616"><a name="p0729142221616"></a><a name="p0729142221616"></a>If the resource does not exist, the PATCH method may create a resource.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request header

    The request header is optional and refers to the additional request field, for example a field required by a specific URI or HTTPS method. For details about common request headers, see  [Table 3](#t24b12299374a4f4ba9fbf5880aec2658). For details about the request authentication information, see  [Obtaining Request Authentication](obtaining-request-authentication.md).

    **Table  3**  Common request headers

    <a name="t24b12299374a4f4ba9fbf5880aec2658"></a>
    <table><thead align="left"><tr id="r4c9188c98a9542db96d6d1aa49483890"><th class="cellrowborder" valign="top" width="16.25742574257426%" id="mcps1.2.5.1.1"><p id="a0e8fe10f8be440a59cea60dfcef9d616"><a name="a0e8fe10f8be440a59cea60dfcef9d616"></a><a name="a0e8fe10f8be440a59cea60dfcef9d616"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="29.287128712871286%" id="mcps1.2.5.1.2"><p id="a0c5134defa3643d4a487a98564df4386"><a name="a0c5134defa3643d4a487a98564df4386"></a><a name="a0c5134defa3643d4a487a98564df4386"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.3"><p id="a5e198cd1f1c84cd4a906d9afd43ee792"><a name="a5e198cd1f1c84cd4a906d9afd43ee792"></a><a name="a5e198cd1f1c84cd4a906d9afd43ee792"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.663366336633665%" id="mcps1.2.5.1.4"><p id="ac34a236127304521999242538b072c58"><a name="ac34a236127304521999242538b072c58"></a><a name="ac34a236127304521999242538b072c58"></a>Examples</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10629133710114"><td class="cellrowborder" valign="top" width="16.25742574257426%" headers="mcps1.2.5.1.1 "><p id="p46301737411"><a name="p46301737411"></a><a name="p46301737411"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.287128712871286%" headers="mcps1.2.5.1.2 "><p id="p363011371216"><a name="p363011371216"></a><a name="p363011371216"></a>Message body type (format).</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.3 "><p id="p1263043712111"><a name="p1263043712111"></a><a name="p1263043712111"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.5.1.4 "><p id="p13630183715110"><a name="p13630183715110"></a><a name="p13630183715110"></a>application/json</p>
    </td>
    </tr>
    <tr id="r48b466a7608e4d6eb042a35f56cbdfb8"><td class="cellrowborder" valign="top" width="16.25742574257426%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0035614236_p792363911913"><a name="en-us_topic_0035614236_p792363911913"></a><a name="en-us_topic_0035614236_p792363911913"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.287128712871286%" headers="mcps1.2.5.1.2 "><p id="p3237430121524"><a name="p3237430121524"></a><a name="p3237430121524"></a>Information about authentication using tokens. For details about how to obtain the information, see <a href="obtaining-request-authentication.md">Obtaining Request Authentication</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.3 "><p id="a1f6108d2189d4cd09376eebef87bb335"><a name="a1f6108d2189d4cd09376eebef87bb335"></a><a name="a1f6108d2189d4cd09376eebef87bb335"></a>This field is mandatory when authentication using tokens is used.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.5.1.4 "><p id="a993f118dde7d4c2f9164d578e9bc8c13"><a name="a993f118dde7d4c2f9164d578e9bc8c13"></a><a name="a993f118dde7d4c2f9164d578e9bc8c13"></a>-</p>
    </td>
    </tr>
    <tr id="r0a259195cce44cee955af0a771a20d71"><td class="cellrowborder" valign="top" width="16.25742574257426%" headers="mcps1.2.5.1.1 "><p id="a4259b0099d3e432f88928e25c01d1127"><a name="a4259b0099d3e432f88928e25c01d1127"></a><a name="a4259b0099d3e432f88928e25c01d1127"></a>X-Sdk-Date</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.287128712871286%" headers="mcps1.2.5.1.2 "><p id="abe5e383ccc8543c2aa4563830f67957a"><a name="abe5e383ccc8543c2aa4563830f67957a"></a><a name="abe5e383ccc8543c2aa4563830f67957a"></a>Time when a request was sent.</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.3 "><p id="p1309136221732"><a name="p1309136221732"></a><a name="p1309136221732"></a>This field is mandatory when authentication using AK/SK is used.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.5.1.4 "><p id="a0f19b458af404df982f0dbb457a13925"><a name="a0f19b458af404df982f0dbb457a13925"></a><a name="a0f19b458af404df982f0dbb457a13925"></a>20151222T034042Z</p>
    </td>
    </tr>
    <tr id="rc97d5ad8e26a47d9aadce68591dbbe62"><td class="cellrowborder" valign="top" width="16.25742574257426%" headers="mcps1.2.5.1.1 "><p id="a7238e21480a841c7a1cbbbb21bdfc864"><a name="a7238e21480a841c7a1cbbbb21bdfc864"></a><a name="a7238e21480a841c7a1cbbbb21bdfc864"></a>Authorization</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.287128712871286%" headers="mcps1.2.5.1.2 "><p id="p952592421823"><a name="p952592421823"></a><a name="p952592421823"></a>Signature authentication information, which comes from the request signature result.</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.3 "><p id="p865747321840"><a name="p865747321840"></a><a name="p865747321840"></a>This field is mandatory when authentication using AK/SK is used.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.663366336633665%" headers="mcps1.2.5.1.4 "><p id="p608112012194"><a name="p608112012194"></a><a name="p608112012194"></a>SDK-HMACSHA256</p>
    <p id="p104299002194"><a name="p104299002194"></a><a name="p104299002194"></a>Credential=ZIRRKMTWPTQFQI1WKNKB/20151222/cnnorth-1/ec2/sdk_request,</p>
    <p id="p171599602194"><a name="p171599602194"></a><a name="p171599602194"></a>SignedHeaders=connection;contenttype;host;x-sdk-date,</p>
    <p id="p273627752194"><a name="p273627752194"></a><a name="p273627752194"></a>Signature=7972cc9145876d174b3862188a0f61819431fa71c8a8a060809ea8b898e3eaa9</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request body

    A request body is generally sent in a structured format \(for example, JSON or XML\). It corresponds to  **Content-type**  in the request header and is used to transfer content other than the request header.

-   Response header

    A response header consists of the following two parts:

    -   An HTTPS status code, from 2_xx_  success code to 4_xx_  or 5_xx_  error code, or a status code that can return the service definition, as shown in the API document.
    -   Additional fields in the response header required by a specific response, for example, the  **Content-Type**  response header. For details about common response headers, see  [Table 4](#tb5107e70c1d545de8b97ed913f602b83).

        **Table  4**  Response header

        <a name="tb5107e70c1d545de8b97ed913f602b83"></a>
        <table><thead align="left"><tr id="rf674063bc81649e8b9789a311a3bcf6e"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="a4db082cf93e748d7b44040c488d0d38c"><a name="a4db082cf93e748d7b44040c488d0d38c"></a><a name="a4db082cf93e748d7b44040c488d0d38c"></a>Name</p>
        </th>
        <th class="cellrowborder" valign="top" width="44%" id="mcps1.2.4.1.2"><p id="aa3e3c39e04e2407ea5bcda8fc61f112d"><a name="aa3e3c39e04e2407ea5bcda8fc61f112d"></a><a name="aa3e3c39e04e2407ea5bcda8fc61f112d"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.3"><p id="a53b16f94658d4903834e1c161d7759af"><a name="a53b16f94658d4903834e1c161d7759af"></a><a name="a53b16f94658d4903834e1c161d7759af"></a>Examples</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="r471495aa79dc4a88a7110f2db9a835e3"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="acebd9ce341d144b38d8674ad67443074"><a name="acebd9ce341d144b38d8674ad67443074"></a><a name="acebd9ce341d144b38d8674ad67443074"></a>Date</p>
        </td>
        <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="a14609642298f4650890b08516c7db143"><a name="a14609642298f4650890b08516c7db143"></a><a name="a14609642298f4650890b08516c7db143"></a>Standard HTTPS header, which represents the date and time at which the message was originated. The format is defined by RFC 822. </p>
        </td>
        <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.3 "><p id="ab1d152d4a35a4fbb86ed423b4b6d9bad"><a name="ab1d152d4a35a4fbb86ed423b4b6d9bad"></a><a name="ab1d152d4a35a4fbb86ed423b4b6d9bad"></a>Mon, 12 Nov 2007 15:55:01 GMT</p>
        </td>
        </tr>
        <tr id="r0588e315fb784df790128bb6aecf61c9"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035614305_p306646695935"><a name="en-us_topic_0035614305_p306646695935"></a><a name="en-us_topic_0035614305_p306646695935"></a>Server</p>
        </td>
        <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="a572e7868aa564539a661a36c8134adc4"><a name="a572e7868aa564539a661a36c8134adc4"></a><a name="a572e7868aa564539a661a36c8134adc4"></a>Standard HTTPS header, which includes the software information that the server uses to process the request.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.3 "><p id="afb122eb44b7446dd9a410167ac7c06ff"><a name="afb122eb44b7446dd9a410167ac7c06ff"></a><a name="afb122eb44b7446dd9a410167ac7c06ff"></a>Apache</p>
        </td>
        </tr>
        <tr id="raa835d5c2e194ed19dc56366f0aedbe9"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="a4bc2f8a7407b40329d7549814743dba4"><a name="a4bc2f8a7407b40329d7549814743dba4"></a><a name="a4bc2f8a7407b40329d7549814743dba4"></a>Content-Length</p>
        </td>
        <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="a5db1494308504d32b0ed7464c14f3c91"><a name="a5db1494308504d32b0ed7464c14f3c91"></a><a name="a5db1494308504d32b0ed7464c14f3c91"></a>Standard HTTPS header, which specifies the size of the entity body, in decimal number of bytes, sent to the recipient.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.3 "><p id="a016917505ad54f32bf5ae9e73c561ad2"><a name="a016917505ad54f32bf5ae9e73c561ad2"></a><a name="a016917505ad54f32bf5ae9e73c561ad2"></a>-</p>
        </td>
        </tr>
        <tr id="rb4087468a73c487a84c136020cc4ef89"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="ad6ed459cd4494fe1a0cbfe7988567c6f"><a name="ad6ed459cd4494fe1a0cbfe7988567c6f"></a><a name="ad6ed459cd4494fe1a0cbfe7988567c6f"></a>Content-Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="ab38ec730e7b243d89e12ba173377ba37"><a name="ab38ec730e7b243d89e12ba173377ba37"></a><a name="ab38ec730e7b243d89e12ba173377ba37"></a>Standard HTTPS header, Specifies the media type of the entity body sent to the recipient.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035614305_p940161295935"><a name="en-us_topic_0035614305_p940161295935"></a><a name="en-us_topic_0035614305_p940161295935"></a>application/json</p>
        </td>
        </tr>
        </tbody>
        </table>


-   Response body

    The response body is generally returned in a structured format \(for example, JSON or XML\), corresponding to Content-type in the response header, and is used to transfer content other than the response header.


You can initiate a request based on constructed request messages using any of the following three methods:

-   cURL

    cURL is a command-line tool used to perform URL operations and transmit information. It can serve as an HTTPS client to send HTTPS requests to the server end and receive response messages. cURL is suitable for use in API tuning scenarios. For more information about cURL, visit  [https://curl.haxx.se/](https://curl.haxx.se/).

-   Code

    You can invoke APIs using code to assemble, send, and process request messages.

-   REST client

    Both Mozilla and Google Chrome provide a graphical browser plug-in REST client to send and process requests. For Mozilla Firefox, see  [Firefox RESTClient](https://addons.mozilla.org/en-US/firefox/addon/restclient/). For details about Google Chrome, see  [Postman](https://chrome.google.com/webstore/detail/postman-interceptor/aicmkgpgakddgnaphhhpliifpcfhicfo?hl=en).


