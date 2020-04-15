# Returned Values<a name="EN-US_TOPIC_0022067715"></a>

-   Normal

    <a name="table66055775111526"></a>
    <table><thead align="left"><tr id="row26075754111526"><th class="cellrowborder" valign="top" width="20.11%" id="mcps1.1.3.1.1"><p id="p31761291111526"><a name="p31761291111526"></a><a name="p31761291111526"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="79.89%" id="mcps1.1.3.1.2"><p id="p22527773111526"><a name="p22527773111526"></a><a name="p22527773111526"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12810311111526"><td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.3.1.1 "><p id="p31002290111526"><a name="p31002290111526"></a><a name="p31002290111526"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.89%" headers="mcps1.1.3.1.2 "><p id="p28157574111526"><a name="p28157574111526"></a><a name="p28157574111526"></a>The task is successfully delivered.</p>
    </td>
    </tr>
    <tr id="row52091574111526"><td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.3.1.1 "><p id="p58667961111526"><a name="p58667961111526"></a><a name="p58667961111526"></a>202</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.89%" headers="mcps1.1.3.1.2 "><p id="p54484409111526"><a name="p54484409111526"></a><a name="p54484409111526"></a>After the task is successfully delivered, the task to be delivered shall be postponed because the system is busy.</p>
    </td>
    </tr>
    <tr id="row54488434155121"><td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.3.1.1 "><p id="p51487044155121"><a name="p51487044155121"></a><a name="p51487044155121"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.89%" headers="mcps1.1.3.1.2 "><p id="p9701059155121"><a name="p9701059155121"></a><a name="p9701059155121"></a>The task is successfully delivered.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table51160989111526"></a>
    <table><thead align="left"><tr id="row32641740111526"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p26735323111526"><a name="p26735323111526"></a><a name="p26735323111526"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p18077587111526"><a name="p18077587111526"></a><a name="p18077587111526"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54998427111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p25687579111526"><a name="p25687579111526"></a><a name="p25687579111526"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p319164111526"><a name="p319164111526"></a><a name="p319164111526"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row2872480111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p31344341111526"><a name="p31344341111526"></a><a name="p31344341111526"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p55863678111526"><a name="p55863678111526"></a><a name="p55863678111526"></a>You need to enter the username and password to access the page requested.</p>
    </td>
    </tr>
    <tr id="row33011058111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p56650021111526"><a name="p56650021111526"></a><a name="p56650021111526"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p25248960111526"><a name="p25248960111526"></a><a name="p25248960111526"></a>You are forbidden to access the page requested.</p>
    </td>
    </tr>
    <tr id="row25914052111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p18663504111526"><a name="p18663504111526"></a><a name="p18663504111526"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p35348823111526"><a name="p35348823111526"></a><a name="p35348823111526"></a>The server cannot find the page requested.</p>
    </td>
    </tr>
    <tr id="row49703957111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p66597603111526"><a name="p66597603111526"></a><a name="p66597603111526"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p25696737111526"><a name="p25696737111526"></a><a name="p25696737111526"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row29944041111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p9548275111526"><a name="p9548275111526"></a><a name="p9548275111526"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p35212801111526"><a name="p35212801111526"></a><a name="p35212801111526"></a>The response generated by the server cannot be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row48479757111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p34546269111526"><a name="p34546269111526"></a><a name="p34546269111526"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p46784422111526"><a name="p46784422111526"></a><a name="p46784422111526"></a>You must use the proxy server for authentication. Then, the request can be processed.</p>
    </td>
    </tr>
    <tr id="row18406615111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p14540807111526"><a name="p14540807111526"></a><a name="p14540807111526"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p36954691111526"><a name="p36954691111526"></a><a name="p36954691111526"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row64156770111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p29315868111526"><a name="p29315868111526"></a><a name="p29315868111526"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p25775127111526"><a name="p25775127111526"></a><a name="p25775127111526"></a>The request cannot be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row30649556111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p66694995111526"><a name="p66694995111526"></a><a name="p66694995111526"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p33585510111526"><a name="p33585510111526"></a><a name="p33585510111526"></a>Failed to complete the request because an internal service error occurs. A service exception occurred.</p>
    </td>
    </tr>
    <tr id="row33834139111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p56210728111526"><a name="p56210728111526"></a><a name="p56210728111526"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p56775101111526"><a name="p56775101111526"></a><a name="p56775101111526"></a>Failed to complete the request because an internal service error occurs. The server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row41213867111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p49988896111526"><a name="p49988896111526"></a><a name="p49988896111526"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p22568753111526"><a name="p22568753111526"></a><a name="p22568753111526"></a>Failed to complete the request because an internal service error occurs. Failed to complete the request because the server receives an invalid request.</p>
    </td>
    </tr>
    <tr id="row1792192111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p10949896111526"><a name="p10949896111526"></a><a name="p10949896111526"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p14526368111526"><a name="p14526368111526"></a><a name="p14526368111526"></a>Failed to complete the request because an internal service error occurs. The system is currently unavailable.</p>
    </td>
    </tr>
    <tr id="row63628449111526"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p53630773111526"><a name="p53630773111526"></a><a name="p53630773111526"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p49125357111526"><a name="p49125357111526"></a><a name="p49125357111526"></a>A gateway timeout error occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


