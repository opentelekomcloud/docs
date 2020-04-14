# Querying VPC Details<a name="vpc_api01_0002"></a>

## Function<a name="section48604061"></a>

This API is used to query details about a VPC.

## URI<a name="section34783366"></a>

GET /v1/\{project\_id\}/vpcs/\{vpc\_id\}

[Table 1](#table26431778)  describes the parameters.

**Table  1**  Parameter description

<a name="table26431778"></a>
<table><thead align="left"><tr id="row38955607"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p1287621"><a name="p1287621"></a><a name="p1287621"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p37188451"><a name="p37188451"></a><a name="p37188451"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p59474521"><a name="p59474521"></a><a name="p59474521"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row52706896"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p41400175"><a name="p41400175"></a><a name="p41400175"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p65079903"><a name="p65079903"></a><a name="p65079903"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row64391817"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p48354649"><a name="p48354649"></a><a name="p48354649"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p24412469"><a name="p24412469"></a><a name="p24412469"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p31252998"><a name="p31252998"></a><a name="p31252998"></a>Specifies the VPC ID, which uniquely identifies the VPC.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section44614845"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}/v1/{project_id}/vpcs/99d9d709-8478-4b46-9f3f-2206b1023fd3
    ```


## Response Message<a name="section65989290"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table574587231556"></a>
    <table><thead align="left"><tr id="row118397001556"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p194916751556"><a name="p194916751556"></a><a name="p194916751556"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.16%" id="mcps1.2.4.1.2"><p id="p424939721556"><a name="p424939721556"></a><a name="p424939721556"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.49999999999999%" id="mcps1.2.4.1.3"><p id="p194597361556"><a name="p194597361556"></a><a name="p194597361556"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row327347841556"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p342718611556"><a name="p342718611556"></a><a name="p342718611556"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.16%" headers="mcps1.2.4.1.2 "><p id="p41691159213"><a name="p41691159213"></a><a name="p41691159213"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.49999999999999%" headers="mcps1.2.4.1.3 "><p id="p652911041556"><a name="p652911041556"></a><a name="p652911041556"></a><a href="#table1945411214515">Specifies the VPC objects.</a></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  VPC objects

    <a name="table1945411214515"></a>
    <table><thead align="left"><tr id="row15454222515"><th class="cellrowborder" valign="top" width="21.66%" id="mcps1.2.4.1.1"><p id="p164549255115"><a name="p164549255115"></a><a name="p164549255115"></a><strong id="b222394852013"><a name="b222394852013"></a><a name="b222394852013"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.32%" id="mcps1.2.4.1.2"><p id="p15454182165114"><a name="p15454182165114"></a><a name="p15454182165114"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.02%" id="mcps1.2.4.1.3"><p id="p1045413215513"><a name="p1045413215513"></a><a name="p1045413215513"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1945414213517"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.2.4.1.1 "><p id="p64541721513"><a name="p64541721513"></a><a name="p64541721513"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.32%" headers="mcps1.2.4.1.2 "><p id="p134540217519"><a name="p134540217519"></a><a name="p134540217519"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.02%" headers="mcps1.2.4.1.3 "><p id="p17454223516"><a name="p17454223516"></a><a name="p17454223516"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row54543212511"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.2.4.1.1 "><p id="p1145412211516"><a name="p1145412211516"></a><a name="p1145412211516"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.32%" headers="mcps1.2.4.1.2 "><p id="p645413265113"><a name="p645413265113"></a><a name="p645413265113"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.02%" headers="mcps1.2.4.1.3 "><a name="ul951112614463"></a><a name="ul951112614463"></a><ul id="ul951112614463"><li>Specifies the VPC name.</li><li>The value is a string of no more than 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li><li>Each VPC name of a tenant must be unique if the VPC name is not left blank.</li></ul>
    </td>
    </tr>
    <tr id="row57274330378"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.2.4.1.1 "><p id="p572773313373"><a name="p572773313373"></a><a name="p572773313373"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.32%" headers="mcps1.2.4.1.2 "><p id="p272783315379"><a name="p272783315379"></a><a name="p272783315379"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.02%" headers="mcps1.2.4.1.3 "><a name="ul621614305363"></a><a name="ul621614305363"></a><ul id="ul621614305363"><li>Provides supplementary information about the VPC.</li><li>The value is a string of no more than 255 characters and cannot contain angle brackets (&lt; or &gt;).</li></ul>
    </td>
    </tr>
    <tr id="row445515275116"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.2.4.1.1 "><p id="p545592185110"><a name="p545592185110"></a><a name="p545592185110"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.32%" headers="mcps1.2.4.1.2 "><p id="p745592125117"><a name="p745592125117"></a><a name="p745592125117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.02%" headers="mcps1.2.4.1.3 "><a name="ul10389173917465"></a><a name="ul10389173917465"></a><ul id="ul10389173917465"><li>Specifies the available IP address ranges for subnets in the VPC.</li><li>Possible values are as follows:<a name="ul53161626155413"></a><a name="ul53161626155413"></a><ul id="ul53161626155413"><li>10.0.0.0/8-10.255.255.240/28</li><li>172.16.0.0/12-172.31.255.240/28</li><li>192.168.0.0/16-192.168.255.240/28</li></ul>
    </li><li>If <strong id="b123151546173110"><a name="b123151546173110"></a><a name="b123151546173110"></a>cidr</strong> is not specified, the default value is left blank.</li><li>The value must be in CIDR format, for example, <strong id="b785094873120"><a name="b785094873120"></a><a name="b785094873120"></a>192.168.0.0/16</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row645513212511"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.2.4.1.1 "><p id="p124551621516"><a name="p124551621516"></a><a name="p124551621516"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.32%" headers="mcps1.2.4.1.2 "><p id="p1545552115110"><a name="p1545552115110"></a><a name="p1545552115110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.02%" headers="mcps1.2.4.1.3 "><a name="ul74552213513"></a><a name="ul74552213513"></a><ul id="ul74552213513"><li>Specifies the VPC status.</li><li>Possible values are as follows:<a name="ul5890854165417"></a><a name="ul5890854165417"></a><ul id="ul5890854165417"><li><strong id="b11671325184317"><a name="b11671325184317"></a><a name="b11671325184317"></a>CREATING</strong>: The VPC is being created.</li><li><strong id="b7480226204319"><a name="b7480226204319"></a><a name="b7480226204319"></a>OK</strong>: The VPC is created successfully.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row134563245111"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.2.4.1.1 "><p id="p145614219511"><a name="p145614219511"></a><a name="p145614219511"></a>routes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.32%" headers="mcps1.2.4.1.2 "><p id="p539717333282"><a name="p539717333282"></a><a name="p539717333282"></a>Array of <a href="#table3576833291556">route</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.02%" headers="mcps1.2.4.1.3 "><a name="ul34563265116"></a><a name="ul34563265116"></a><ul id="ul34563265116"><li>Specifies the route information.</li><li>For details, see the description of the <a href="#table3576833291556">route objects</a>.</li></ul>
    </td>
    </tr>
    <tr id="row14561326518"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.2.4.1.1 "><p id="p114561520515"><a name="p114561520515"></a><a name="p114561520515"></a>enable_shared_snat</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.32%" headers="mcps1.2.4.1.2 "><p id="p5456112185112"><a name="p5456112185112"></a><a name="p5456112185112"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.02%" headers="mcps1.2.4.1.3 "><p id="p204561128510"><a name="p204561128510"></a><a name="p204561128510"></a>Specifies whether the shared SNAT function is enabled. The value <strong id="b84235270612178"><a name="b84235270612178"></a><a name="b84235270612178"></a>true</strong> indicates that the function is enabled, and the value <strong id="b84235270614243"><a name="b84235270614243"></a><a name="b84235270614243"></a>false</strong> indicates that the function is not enabled.</p>
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
    <td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.2.4.1.3 "><a name="ul15801323493"></a><a name="ul15801323493"></a><ul id="ul15801323493"><li>Specifies the destination network segment of a route.</li><li>The value must be in the CIDR format. Currently, only the value <strong>0.0.0.0/0</strong> is supported.</li></ul>
    </td>
    </tr>
    <tr id="row6565233911054"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p1623922311054"><a name="p1623922311054"></a><a name="p1623922311054"></a>nexthop</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.2.4.1.2 "><p id="p4377761311054"><a name="p4377761311054"></a><a name="p4377761311054"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.2.4.1.3 "><a name="ul1344883624911"></a><a name="ul1344883624911"></a><ul id="ul1344883624911"><li>Specifies the next hop of a route.</li><li>The value must be an IP address and must belong to the subnet in the VPC. Otherwise, this value does not take effect.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "vpc": {
            "id": "99d9d709-8478-4b46-9f3f-2206b1023fd3",
            "name": "vpc",
            "description": "test",
            "cidr": "192.168.0.0/16",
            "status": "OK",
             
            "routes": [],
            "enable_shared_snat": false
    }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

