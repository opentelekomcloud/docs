# Querying VPCs<a name="vpc_api01_0003"></a>

## Function<a name="section14477792"></a>

This API is used to query VPCs using search criteria and to display the VPCs in a list.

## URI<a name="section63191266"></a>

GET /v1/\{project\_id\}/vpcs

Example:

```
GET https://{Endpoint}/v1/{project_id}/vpcs?limit=10&marker=13551d6b-755d-4757-b956-536f674975c0
```

[Table 1](#table39337169)  describes the parameters.

**Table  1**  Parameter description

<a name="table39337169"></a>
<table><thead align="left"><tr id="row33970761"><th class="cellrowborder" valign="top" width="13.530000000000001%" id="mcps1.2.5.1.1"><p id="p168245"><a name="p168245"></a><a name="p168245"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="21.240000000000002%" id="mcps1.2.5.1.2"><p id="p13627845"><a name="p13627845"></a><a name="p13627845"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.280000000000001%" id="mcps1.2.5.1.3"><p id="p17267522174356"><a name="p17267522174356"></a><a name="p17267522174356"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.949999999999996%" id="mcps1.2.5.1.4"><p id="p30113633"><a name="p30113633"></a><a name="p30113633"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row23285234"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.5.1.1 "><p id="p7055840"><a name="p7055840"></a><a name="p7055840"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.2 "><p id="p34652178"><a name="p34652178"></a><a name="p34652178"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.280000000000001%" headers="mcps1.2.5.1.3 "><p id="p56492018174356"><a name="p56492018174356"></a><a name="p56492018174356"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.949999999999996%" headers="mcps1.2.5.1.4 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row28505468"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.5.1.1 "><p id="p27241609"><a name="p27241609"></a><a name="p27241609"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.2 "><p id="p59086710"><a name="p59086710"></a><a name="p59086710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.280000000000001%" headers="mcps1.2.5.1.3 "><p id="p12450755174356"><a name="p12450755174356"></a><a name="p12450755174356"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.949999999999996%" headers="mcps1.2.5.1.4 "><p id="p24297067174412"><a name="p24297067174412"></a><a name="p24297067174412"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row21315230"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.5.1.1 "><p id="p48812047"><a name="p48812047"></a><a name="p48812047"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.2 "><p id="p61461766"><a name="p61461766"></a><a name="p61461766"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.280000000000001%" headers="mcps1.2.5.1.3 "><p id="p1878236174356"><a name="p1878236174356"></a><a name="p1878236174356"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50.949999999999996%" headers="mcps1.2.5.1.4 "><a name="ul15798159502"></a><a name="ul15798159502"></a><ul id="ul15798159502"><li>Specifies the number of records returned on each page.</li><li>The value ranges from 0 to intmax.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section31850483"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}/v1/{project_id}/vpcs
    ```


## Response Message<a name="section18218892"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table6229176715519"></a>
    <table><thead align="left"><tr id="row6055323715519"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p586512615519"><a name="p586512615519"></a><a name="p586512615519"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="27.97%" id="mcps1.2.4.1.2"><p id="p2771539415519"><a name="p2771539415519"></a><a name="p2771539415519"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.690000000000005%" id="mcps1.2.4.1.3"><p id="p3035446115519"><a name="p3035446115519"></a><a name="p3035446115519"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4279228915519"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p4362334815519"><a name="p4362334815519"></a><a name="p4362334815519"></a>vpcs</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.97%" headers="mcps1.2.4.1.2 "><p id="p26395826172022"><a name="p26395826172022"></a><a name="p26395826172022"></a>Array of <a href="#table65129753">vpcs</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.690000000000005%" headers="mcps1.2.4.1.3 "><p id="p1714182515519"><a name="p1714182515519"></a><a name="p1714182515519"></a>Specifies the VPC objects.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **vpcs**  field

    <a name="table65129753"></a>
    <table><thead align="left"><tr id="row16647026"><th class="cellrowborder" valign="top" width="15.870000000000001%" id="mcps1.2.4.1.1"><p id="p6231886"><a name="p6231886"></a><a name="p6231886"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.91%" id="mcps1.2.4.1.2"><p id="p25347041174441"><a name="p25347041174441"></a><a name="p25347041174441"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.22%" id="mcps1.2.4.1.3"><p id="p18111828"><a name="p18111828"></a><a name="p18111828"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57771982"><td class="cellrowborder" valign="top" width="15.870000000000001%" headers="mcps1.2.4.1.1 "><p id="p49018956"><a name="p49018956"></a><a name="p49018956"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.91%" headers="mcps1.2.4.1.2 "><p id="p39844479174441"><a name="p39844479174441"></a><a name="p39844479174441"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.2.4.1.3 "><p id="p27697526"><a name="p27697526"></a><a name="p27697526"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row47951145"><td class="cellrowborder" valign="top" width="15.870000000000001%" headers="mcps1.2.4.1.1 "><p id="p58837506"><a name="p58837506"></a><a name="p58837506"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.91%" headers="mcps1.2.4.1.2 "><p id="p6177377174441"><a name="p6177377174441"></a><a name="p6177377174441"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.2.4.1.3 "><a name="ul951112614463"></a><a name="ul951112614463"></a><ul id="ul951112614463"><li>Specifies the VPC name.</li><li>The value is a string of no more than 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li><li>Each VPC name of a tenant must be unique if the VPC name is not left blank.</li></ul>
    </td>
    </tr>
    <tr id="row18577115091311"><td class="cellrowborder" valign="top" width="15.870000000000001%" headers="mcps1.2.4.1.1 "><p id="p174994533139"><a name="p174994533139"></a><a name="p174994533139"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.91%" headers="mcps1.2.4.1.2 "><p id="p349935312131"><a name="p349935312131"></a><a name="p349935312131"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.2.4.1.3 "><a name="ul16499115318137"></a><a name="ul16499115318137"></a><ul id="ul16499115318137"><li>Provides supplementary information about the VPC.</li><li>The value is a string of no more than 255 characters and cannot contain angle brackets (&lt; or &gt;).</li></ul>
    </td>
    </tr>
    <tr id="row2894687"><td class="cellrowborder" valign="top" width="15.870000000000001%" headers="mcps1.2.4.1.1 "><p id="p33143133"><a name="p33143133"></a><a name="p33143133"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.91%" headers="mcps1.2.4.1.2 "><p id="p30605552174441"><a name="p30605552174441"></a><a name="p30605552174441"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.2.4.1.3 "><a name="ul10389173917465"></a><a name="ul10389173917465"></a><ul id="ul10389173917465"><li>Specifies the available IP address ranges for subnets in the VPC.</li><li>Possible values are as follows:<a name="ul53161626155413"></a><a name="ul53161626155413"></a><ul id="ul53161626155413"><li>10.0.0.0/8-10.255.255.240/28</li><li>172.16.0.0/12-172.31.255.240/28</li><li>192.168.0.0/16-192.168.255.240/28</li></ul>
    </li><li>If <strong id="b1338817432"><a name="b1338817432"></a><a name="b1338817432"></a>cidr</strong> is not specified, the default value is left blank.</li><li>The value must be in CIDR format, for example, <strong id="b118892120317"><a name="b118892120317"></a><a name="b118892120317"></a>192.168.0.0/16</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row40205569"><td class="cellrowborder" valign="top" width="15.870000000000001%" headers="mcps1.2.4.1.1 "><p id="p35425694"><a name="p35425694"></a><a name="p35425694"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.91%" headers="mcps1.2.4.1.2 "><p id="p63130643174441"><a name="p63130643174441"></a><a name="p63130643174441"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.2.4.1.3 "><a name="ul74552213513"></a><a name="ul74552213513"></a><ul id="ul74552213513"><li>Specifies the VPC status.</li><li>Possible values are as follows:<a name="ul5890854165417"></a><a name="ul5890854165417"></a><ul id="ul5890854165417"><li><strong id="b768725632"><a name="b768725632"></a><a name="b768725632"></a>CREATING</strong>: The VPC is being created.</li><li><strong id="b412910318311"><a name="b412910318311"></a><a name="b412910318311"></a>OK</strong>: The VPC is created successfully.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row56256918135346"><td class="cellrowborder" valign="top" width="15.870000000000001%" headers="mcps1.2.4.1.1 "><p id="p60516514135346"><a name="p60516514135346"></a><a name="p60516514135346"></a>routes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.91%" headers="mcps1.2.4.1.2 "><p id="p32811915135346"><a name="p32811915135346"></a><a name="p32811915135346"></a>Array of <a href="#table3576833291556">route</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.2.4.1.3 "><a name="ul93249349513"></a><a name="ul93249349513"></a><ul id="ul93249349513"><li>Specifies the route information.</li><li>For details, see <a href="#table3576833291556">Table 4</a>.</li></ul>
    </td>
    </tr>
    <tr id="row1426011201318"><td class="cellrowborder" valign="top" width="15.870000000000001%" headers="mcps1.2.4.1.1 "><p id="p41373254402"><a name="p41373254402"></a><a name="p41373254402"></a>enable_shared_snat</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.91%" headers="mcps1.2.4.1.2 "><p id="p18137202516409"><a name="p18137202516409"></a><a name="p18137202516409"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.2.4.1.3 "><p id="p51371325174011"><a name="p51371325174011"></a><a name="p51371325174011"></a>Specifies whether the shared SNAT function is enabled. The value <strong id="b84235270612178"><a name="b84235270612178"></a><a name="b84235270612178"></a>true</strong> indicates that the function is enabled, and the value <strong id="b84235270614243"><a name="b84235270614243"></a><a name="b84235270614243"></a>false</strong> indicates that the function is not enabled.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **route**  objects

    <a name="table3576833291556"></a>
    <table><thead align="left"><tr id="row921218691556"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p798956991556"><a name="p798956991556"></a><a name="p798956991556"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.38%" id="mcps1.2.4.1.2"><p id="p754435891556"><a name="p754435891556"></a><a name="p754435891556"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.28%" id="mcps1.2.4.1.3"><p id="p711326791556"><a name="p711326791556"></a><a name="p711326791556"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3930377391556"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p2948903591556"><a name="p2948903591556"></a><a name="p2948903591556"></a>destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.2.4.1.2 "><p id="p270722191556"><a name="p270722191556"></a><a name="p270722191556"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.2.4.1.3 "><a name="ul5555115211517"></a><a name="ul5555115211517"></a><ul id="ul5555115211517"><li>Specifies the destination network segment of a route.</li><li>The value must be in the CIDR format. Currently, only the value <strong>0.0.0.0/0</strong> is supported.</li></ul>
    </td>
    </tr>
    <tr id="row6565233911054"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p1623922311054"><a name="p1623922311054"></a><a name="p1623922311054"></a>nexthop</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.2.4.1.2 "><p id="p4377761311054"><a name="p4377761311054"></a><a name="p4377761311054"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.2.4.1.3 "><a name="ul69731859205110"></a><a name="ul69731859205110"></a><ul id="ul69731859205110"><li>Specifies the next hop of a route.</li><li>The value must be an IP address and must belong to the subnet in the VPC. Otherwise, this value does not take effect.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "vpcs": [
            {
                "id": "13551d6b-755d-4757-b956-536f674975c0",
                "name": "default",
                "description": "test",
                "cidr": "172.16.0.0/16",
                "status": "OK",
                
                "routes": [],
                "enable_shared_snat": false
            },
            {
                "id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85",
                "name": "222",
                "description": "test",
                "cidr": "192.168.0.0/16",
                "status": "OK",
                
                "routes": [],
                "enable_shared_snat": false
            },
            {
                "id": "99d9d709-8478-4b46-9f3f-2206b1023fd3",
                "name": "vpc",
                "description": "test",
                "cidr": "192.168.0.0/16",
                "status": "OK",
                
                "routes": [],
                "enable_shared_snat": false
            }
        ]
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

