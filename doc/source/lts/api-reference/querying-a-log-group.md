# Querying a Log Group<a name="lts_02_0004"></a>

## Function<a name="section13262100202410"></a>

This function describes how to query a log group you have created to obtain the name, ID, expiration time, and creation time of the log group.

## URI<a name="section31681806"></a>

-   URI format

    GET /v2.0/\{project\_id\}/log-groups/\{group\_id\}


-   Parameter description

    **Table  1**  Parameter description

    <a name="table805068"></a>
    <table><thead align="left"><tr id="row57933110"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p62070358"><a name="p62070358"></a><a name="p62070358"></a><strong id="b128317754613"><a name="b128317754613"></a><a name="b128317754613"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p61643119"><a name="p61643119"></a><a name="p61643119"></a><strong id="b1819188124617"><a name="b1819188124617"></a><a name="b1819188124617"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p27036712"><a name="p27036712"></a><a name="p27036712"></a><strong id="b12937918465"><a name="b12937918465"></a><a name="b12937918465"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p42490025"><a name="p42490025"></a><a name="p42490025"></a><strong id="b82209541461"><a name="b82209541461"></a><a name="b82209541461"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19139995"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p166901052205610"><a name="p166901052205610"></a><a name="p166901052205610"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p13690175218569"><a name="p13690175218569"></a><a name="p13690175218569"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1690852165618"><a name="p1690852165618"></a><a name="p1690852165618"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p106901852145617"><a name="p106901852145617"></a><a name="p106901852145617"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row8975271"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1169065215561"><a name="p1169065215561"></a><a name="p1169065215561"></a>group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p969016528569"><a name="p969016528569"></a><a name="p969016528569"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p969011527564"><a name="p969011527564"></a><a name="p969011527564"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p186901852125613"><a name="p186901852125613"></a><a name="p186901852125613"></a>Specifies the log group ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section16700806"></a>

-   Request parameters

    None

-   Example request

    ```
    GET /v2.0/{project_id}/log-groups/{group_id}
    ```


## Response<a name="section16089528"></a>

-   Response parameters

    **Table  2**  Parameter description

    <a name="table894955330"></a>
    <table><thead align="left"><tr id="row396125513310"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p29326511412"><a name="p29326511412"></a><a name="p29326511412"></a><strong id="b1124318619407"><a name="b1124318619407"></a><a name="b1124318619407"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p293213519412"><a name="p293213519412"></a><a name="p293213519412"></a><strong id="afd1c772bc0d34dd0954eb451c30339a1"><a name="afd1c772bc0d34dd0954eb451c30339a1"></a><a name="afd1c772bc0d34dd0954eb451c30339a1"></a>Sub-Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p1693275249"><a name="p1693275249"></a><a name="p1693275249"></a><strong id="b44001144134514"><a name="b44001144134514"></a><a name="b44001144134514"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p79321055418"><a name="p79321055418"></a><a name="p79321055418"></a><strong id="b9717144524512"><a name="b9717144524512"></a><a name="b9717144524512"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14961155834"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p3933557412"><a name="p3933557412"></a><a name="p3933557412"></a>log_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p393310520420"><a name="p393310520420"></a><a name="p393310520420"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p6933955419"><a name="p6933955419"></a><a name="p6933955419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1393365243"><a name="p1393365243"></a><a name="p1393365243"></a>Specifies the log group ID.</p>
    </td>
    </tr>
    <tr id="row2961555431"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1893314511413"><a name="p1893314511413"></a><a name="p1893314511413"></a>log_group_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p9933185745"><a name="p9933185745"></a><a name="p9933185745"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p19933115241"><a name="p19933115241"></a><a name="p19933115241"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p39331751246"><a name="p39331751246"></a><a name="p39331751246"></a>Specifies the log group name.</p>
    </td>
    </tr>
    <tr id="row4961055739"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p0933954411"><a name="p0933954411"></a><a name="p0933954411"></a>creation_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p10933751845"><a name="p10933751845"></a><a name="p10933751845"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p11933251149"><a name="p11933251149"></a><a name="p11933251149"></a>Int64</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p13933152045"><a name="p13933152045"></a><a name="p13933152045"></a>Specifies the log group creation time.</p>
    </td>
    </tr>
    <tr id="row1296185518312"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p39331057410"><a name="p39331057410"></a><a name="p39331057410"></a>ttl_in_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p16933165844"><a name="p16933165844"></a><a name="p16933165844"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1993320514419"><a name="p1993320514419"></a><a name="p1993320514419"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p5933125343"><a name="p5933125343"></a><a name="p5933125343"></a>Specifies the log expiration time.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
                "log_group_id": "8ac95c07-357b-11e9-bc2a-286ed488ce71", 
                "log_group_name": "lts-group-3h0y", 
                "creation_time": 1550714033721, 
                "ttl_in_days": 7
    } 
    ```


## Returned Value<a name="section10588031"></a>

-   Normal

    200

-   Abnormal

    For details, see  [Status Code](status-code.md).


