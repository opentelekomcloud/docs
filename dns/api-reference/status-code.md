# Status Code<a name="dns_api_80002"></a>

-   Normal

    **Table  1**  Return code for successful requests

    <a name="table5683702611201"></a>
    <table><thead align="left"><tr id="row5526436211201"><th class="cellrowborder" valign="top" width="35.15%" id="mcps1.2.3.1.1"><p id="p4722834111201"><a name="p4722834111201"></a><a name="p4722834111201"></a><strong id="b8423527069424_1"><a name="b8423527069424_1"></a><a name="b8423527069424_1"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="64.85%" id="mcps1.2.3.1.2"><p id="p29038811201"><a name="p29038811201"></a><a name="p29038811201"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2352145611201"><td class="cellrowborder" valign="top" width="35.15%" headers="mcps1.2.3.1.1 "><p id="p2618974411201"><a name="p2618974411201"></a><a name="p2618974411201"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.85%" headers="mcps1.2.3.1.2 "><p id="p4099449211201"><a name="p4099449211201"></a><a name="p4099449211201"></a>Request succeeded.</p>
    </td>
    </tr>
    <tr id="row42025997185543"><td class="cellrowborder" valign="top" width="35.15%" headers="mcps1.2.3.1.1 "><p id="p48662634185543"><a name="p48662634185543"></a><a name="p48662634185543"></a>202</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.85%" headers="mcps1.2.3.1.2 "><p id="p49359271185543"><a name="p49359271185543"></a><a name="p49359271185543"></a>Request accepted.</p>
    </td>
    </tr>
    <tr id="row105115417410"><td class="cellrowborder" valign="top" width="35.15%" headers="mcps1.2.3.1.1 "><p id="a6d4ed8df6bdc4a83bd40950f262242fe"><a name="a6d4ed8df6bdc4a83bd40950f262242fe"></a><a name="a6d4ed8df6bdc4a83bd40950f262242fe"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.85%" headers="mcps1.2.3.1.2 "><p id="a474fdbdfe7484794b8fc5c3c28f92cad"><a name="a474fdbdfe7484794b8fc5c3c28f92cad"></a><a name="a474fdbdfe7484794b8fc5c3c28f92cad"></a>No content.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    **Table  2**  Return code for failed requests

    <a name="table61691626164846"></a>
    <table><thead align="left"><tr id="row25494897164846"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.2.3.1.1"><p id="p51820810164846"><a name="p51820810164846"></a><a name="p51820810164846"></a><strong id="b8423527069424_3"><a name="b8423527069424_3"></a><a name="b8423527069424_3"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.3.1.2"><p id="p36736087164846"><a name="p36736087164846"></a><a name="p36736087164846"></a><strong id="b842352706112423_3"><a name="b842352706112423_3"></a><a name="b842352706112423_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row22833089164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p37540911164846"><a name="p37540911164846"></a><a name="p37540911164846"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p20914954164846"><a name="p20914954164846"></a><a name="p20914954164846"></a>The server fails to process the request.</p>
    </td>
    </tr>
    <tr id="row54016859164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p13289476164846"><a name="p13289476164846"></a><a name="p13289476164846"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p2705741164846"><a name="p2705741164846"></a><a name="p2705741164846"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row24351669164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p26328145164846"><a name="p26328145164846"></a><a name="p26328145164846"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p52205026164846"><a name="p52205026164846"></a><a name="p52205026164846"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row83194164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p6738773164846"><a name="p6738773164846"></a><a name="p6738773164846"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p8969753164846"><a name="p8969753164846"></a><a name="p8969753164846"></a>The server cannot find the requested page.</p>
    </td>
    </tr>
    <tr id="row13618913164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p29390164164846"><a name="p29390164164846"></a><a name="p29390164164846"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p31793092164846"><a name="p31793092164846"></a><a name="p31793092164846"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row17702374164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p24606171164846"><a name="p24606171164846"></a><a name="p24606171164846"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p46942849164846"><a name="p46942849164846"></a><a name="p46942849164846"></a>The response generated by the server is not acceptable to the client.</p>
    </td>
    </tr>
    <tr id="row19832462164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p62925567164846"><a name="p62925567164846"></a><a name="p62925567164846"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p63806198164846"><a name="p63806198164846"></a><a name="p63806198164846"></a>You must use the proxy server for authentication.</p>
    </td>
    </tr>
    <tr id="row37384870164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p8275614164846"><a name="p8275614164846"></a><a name="p8275614164846"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p66344974164846"><a name="p66344974164846"></a><a name="p66344974164846"></a>The request is timed out.</p>
    </td>
    </tr>
    <tr id="row60233859164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p47104411164846"><a name="p47104411164846"></a><a name="p47104411164846"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p57360960164846"><a name="p57360960164846"></a><a name="p57360960164846"></a>The request cannot be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row58029662204356"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p2782180204356"><a name="p2782180204356"></a><a name="p2782180204356"></a>413 Payload Too Large</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p24029998204356"><a name="p24029998204356"></a><a name="p24029998204356"></a>The request is too large.</p>
    </td>
    </tr>
    <tr id="row46486594164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p7317797164846"><a name="p7317797164846"></a><a name="p7317797164846"></a>500 internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p55870664164846"><a name="p55870664164846"></a><a name="p55870664164846"></a>The request fails because the server is abnormal.</p>
    </td>
    </tr>
    <tr id="row33073929164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p61742575164846"><a name="p61742575164846"></a><a name="p61742575164846"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p35092715164846"><a name="p35092715164846"></a><a name="p35092715164846"></a>The request fails because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row47398979164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p14112120164846"><a name="p14112120164846"></a><a name="p14112120164846"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p2231094164846"><a name="p2231094164846"></a><a name="p2231094164846"></a>The request fails because the returned response is invalid.</p>
    </td>
    </tr>
    <tr id="row20079847164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p15854916164846"><a name="p15854916164846"></a><a name="p15854916164846"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p9179838164846"><a name="p9179838164846"></a><a name="p9179838164846"></a>The request fails because the system is abnormal.</p>
    </td>
    </tr>
    <tr id="row15509681164846"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.2.3.1.1 "><p id="p48324640164846"><a name="p48324640164846"></a><a name="p48324640164846"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.3.1.2 "><p id="p21981792164846"><a name="p21981792164846"></a><a name="p21981792164846"></a>Gateway times out.</p>
    </td>
    </tr>
    </tbody>
    </table>


