# Querying the Default Protection Policy Configured for the Newly Purchased Public IP Addresses<a name="antiddos_02_0037"></a>

## Functions<a name="section55096476"></a>

This API enables you to query the default protection policy configured for the newly purchased public IP addresses.

## URI<a name="section26106237"></a>

-   URI format

    GET /v1/\{project\_id\}/antiddos/default/config

-   Parameter description

    <a name="table51410791"></a>
    <table><thead align="left"><tr id="row16041741"><th class="cellrowborder" valign="top" width="21.9%" id="mcps1.1.5.1.1"><p id="p24312641"><a name="p24312641"></a><a name="p24312641"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.55%" id="mcps1.1.5.1.2"><p id="p23166934"><a name="p23166934"></a><a name="p23166934"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.1.5.1.3"><p id="p64582388"><a name="p64582388"></a><a name="p64582388"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.1.5.1.4"><p id="p63790914"><a name="p63790914"></a><a name="p63790914"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66790376"><td class="cellrowborder" valign="top" width="21.9%" headers="mcps1.1.5.1.1 "><p id="p41311375"><a name="p41311375"></a><a name="p41311375"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.1.5.1.2 "><p id="p57887070"><a name="p57887070"></a><a name="p57887070"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.1.5.1.3 "><p id="p58341118"><a name="p58341118"></a><a name="p58341118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.1.5.1.4 "><p id="p28010135"><a name="p28010135"></a><a name="p28010135"></a>User ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section33629549"></a>

-   Request example

    ```
    GET /v1/67641fe6886f43fcb78edbbf0ad0b99f/antiddos/default/config
    ```


## Response<a name="section34230492"></a>

-   Parameter description

    <a name="table48692557"></a>
    <table><thead align="left"><tr id="row57013647"><th class="cellrowborder" valign="top" width="23.66%" id="mcps1.1.5.1.1"><p id="p54702703"><a name="p54702703"></a><a name="p54702703"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.28%" id="mcps1.1.5.1.2"><p id="p1733939"><a name="p1733939"></a><a name="p1733939"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.33%" id="mcps1.1.5.1.3"><p id="p6231364"><a name="p6231364"></a><a name="p6231364"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.73%" id="mcps1.1.5.1.4"><p id="p34978441"><a name="p34978441"></a><a name="p34978441"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14681450"><td class="cellrowborder" valign="top" width="23.66%" headers="mcps1.1.5.1.1 "><p id="p48346833"><a name="p48346833"></a><a name="p48346833"></a>enable_L7</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.28%" headers="mcps1.1.5.1.2 "><p id="p23779363"><a name="p23779363"></a><a name="p23779363"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.33%" headers="mcps1.1.5.1.3 "><p id="p47080266"><a name="p47080266"></a><a name="p47080266"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.73%" headers="mcps1.1.5.1.4 "><p id="p28885026"><a name="p28885026"></a><a name="p28885026"></a>Whether to enable layer-7 protection.</p>
    </td>
    </tr>
    <tr id="row58638646"><td class="cellrowborder" valign="top" width="23.66%" headers="mcps1.1.5.1.1 "><p id="p52109899"><a name="p52109899"></a><a name="p52109899"></a>traffic_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.28%" headers="mcps1.1.5.1.2 "><p id="p60152276"><a name="p60152276"></a><a name="p60152276"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.33%" headers="mcps1.1.5.1.3 "><p id="p40496186"><a name="p40496186"></a><a name="p40496186"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.73%" headers="mcps1.1.5.1.4 "><p id="p58965604"><a name="p58965604"></a><a name="p58965604"></a>Position ID of traffic. The value ranges from 1 to 9 and 33 to 36.</p>
    </td>
    </tr>
    <tr id="row60928390"><td class="cellrowborder" valign="top" width="23.66%" headers="mcps1.1.5.1.1 "><p id="p36252562"><a name="p36252562"></a><a name="p36252562"></a>http_request_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.28%" headers="mcps1.1.5.1.2 "><p id="p50776406"><a name="p50776406"></a><a name="p50776406"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.33%" headers="mcps1.1.5.1.3 "><p id="p19248251"><a name="p19248251"></a><a name="p19248251"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.73%" headers="mcps1.1.5.1.4 "><p id="p56757654"><a name="p56757654"></a><a name="p56757654"></a>Position ID of number of HTTP requests. The value ranges from 1 to 15 and 33 to 36.</p>
    </td>
    </tr>
    <tr id="row3262153532716"><td class="cellrowborder" valign="top" width="23.66%" headers="mcps1.1.5.1.1 "><p id="p16262335182711"><a name="p16262335182711"></a><a name="p16262335182711"></a>cleaning_access_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.28%" headers="mcps1.1.5.1.2 "><p id="p13262935172711"><a name="p13262935172711"></a><a name="p13262935172711"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.33%" headers="mcps1.1.5.1.3 "><p id="p3262535152711"><a name="p3262535152711"></a><a name="p3262535152711"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.73%" headers="mcps1.1.5.1.4 "><p id="p15422169"><a name="p15422169"></a><a name="p15422169"></a>Position ID of access limit during cleaning. The value ranges from 1 to 8 and 33 to 36.</p>
    </td>
    </tr>
    <tr id="row145501038152720"><td class="cellrowborder" valign="top" width="23.66%" headers="mcps1.1.5.1.1 "><p id="p15550238192718"><a name="p15550238192718"></a><a name="p15550238192718"></a>app_type_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.28%" headers="mcps1.1.5.1.2 "><p id="p18550438122716"><a name="p18550438122716"></a><a name="p18550438122716"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.33%" headers="mcps1.1.5.1.3 "><p id="p13550438182713"><a name="p13550438182713"></a><a name="p13550438182713"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.73%" headers="mcps1.1.5.1.4 "><div class="p" id="p2630238915650"><a name="p2630238915650"></a><a name="p2630238915650"></a>Application type ID. Possible values:<a name="ul2584619815657"></a><a name="ul2584619815657"></a><ul id="ul2584619815657"><li>0</li><li>1</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    { 
        "enable_L7":true, 
        "traffic_pos_id":1, 
        "http_request_pos_id":1, 
        "cleaning_access_pos_id":1, 
        "app_type_id":1 
    }
    ```


## Status Code<a name="section39638980"></a>

For details, see  [Status Code](status-code.md).

