# Creating a VPC<a name="vpc_api01_0001"></a>

## Function<a name="section20114008"></a>

This API is used to create a VPC.

## URI<a name="section46808346"></a>

POST /v1/\{project\_id\}/vpcs

[Table 1](#table3672032)  describes the parameters.

**Table  1**  Parameter description

<a name="table3672032"></a>
<table><thead align="left"><tr id="row10026740"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p6859639"><a name="p6859639"></a><a name="p6859639"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p18759866"><a name="p18759866"></a><a name="p18759866"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p43154149"><a name="p43154149"></a><a name="p43154149"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5825185"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2077973"><a name="p2077973"></a><a name="p2077973"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34098154"><a name="p34098154"></a><a name="p34098154"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p622613501739"><a name="p622613501739"></a><a name="p622613501739"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section18621933"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table59675338144730"></a>
    <table><thead align="left"><tr id="row22732874144730"><th class="cellrowborder" valign="top" width="12.591259125912593%" id="mcps1.2.5.1.1"><p id="p29423469144730"><a name="p29423469144730"></a><a name="p29423469144730"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.122312231223123%" id="mcps1.2.5.1.2"><p id="p34490826144730"><a name="p34490826144730"></a><a name="p34490826144730"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.49204920492049%" id="mcps1.2.5.1.3"><p id="p42293511144730"><a name="p42293511144730"></a><a name="p42293511144730"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.79437943794379%" id="mcps1.2.5.1.4"><p id="p3222348144730"><a name="p3222348144730"></a><a name="p3222348144730"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59683650144730"><td class="cellrowborder" valign="top" width="12.591259125912593%" headers="mcps1.2.5.1.1 "><p id="p2537488144730"><a name="p2537488144730"></a><a name="p2537488144730"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.5.1.2 "><p id="p4210015144730"><a name="p4210015144730"></a><a name="p4210015144730"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.49204920492049%" headers="mcps1.2.5.1.3 "><p id="p41691159213"><a name="p41691159213"></a><a name="p41691159213"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79437943794379%" headers="mcps1.2.5.1.4 "><p id="p32639071144730"><a name="p32639071144730"></a><a name="p32639071144730"></a><a href="#table33750194">Specifies the VPC objects.</a></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  VPC objects

    <a name="table33750194"></a>
    <table><thead align="left"><tr id="row51192804"><th class="cellrowborder" valign="top" width="13.15%" id="mcps1.2.5.1.1"><p id="p52976421"><a name="p52976421"></a><a name="p52976421"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.240000000000002%" id="mcps1.2.5.1.2"><p id="p63231703"><a name="p63231703"></a><a name="p63231703"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.5.1.3"><p id="p2491821616557"><a name="p2491821616557"></a><a name="p2491821616557"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.88%" id="mcps1.2.5.1.4"><p id="p21494305"><a name="p21494305"></a><a name="p21494305"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63317164"><td class="cellrowborder" valign="top" width="13.15%" headers="mcps1.2.5.1.1 "><p id="p28416672"><a name="p28416672"></a><a name="p28416672"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.5.1.2 "><p id="p20049059"><a name="p20049059"></a><a name="p20049059"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p510960516557"><a name="p510960516557"></a><a name="p510960516557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.88%" headers="mcps1.2.5.1.4 "><a name="ul122583362468"></a><a name="ul122583362468"></a><ul id="ul122583362468"><li>Specifies the VPC name.</li><li>The value is a string of no more than 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li><li>Each VPC name of a tenant must be unique if the VPC name is not left blank.</li></ul>
    </td>
    </tr>
    <tr id="row1034214180910"><td class="cellrowborder" valign="top" width="13.15%" headers="mcps1.2.5.1.1 "><p id="p19990426299"><a name="p19990426299"></a><a name="p19990426299"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.5.1.2 "><p id="p149901726897"><a name="p149901726897"></a><a name="p149901726897"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p59901262916"><a name="p59901262916"></a><a name="p59901262916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.88%" headers="mcps1.2.5.1.4 "><a name="ul49905267911"></a><a name="ul49905267911"></a><ul id="ul49905267911"><li>Provides supplementary information about the VPC.</li><li>The value is a string of no more than 255 characters and cannot contain angle brackets (&lt; or &gt;).</li></ul>
    </td>
    </tr>
    <tr id="row18134306"><td class="cellrowborder" valign="top" width="13.15%" headers="mcps1.2.5.1.1 "><p id="p59592696"><a name="p59592696"></a><a name="p59592696"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.5.1.2 "><p id="p62279078"><a name="p62279078"></a><a name="p62279078"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p1122484216557"><a name="p1122484216557"></a><a name="p1122484216557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.88%" headers="mcps1.2.5.1.4 "><a name="ul10389173917465"></a><a name="ul10389173917465"></a><ul id="ul10389173917465"><li>Specifies the available IP address ranges for subnets in the VPC.</li><li>Possible values are as follows:<a name="ul53161626155413"></a><a name="ul53161626155413"></a><ul id="ul53161626155413"><li>10.0.0.0/8-10.255.255.240/28</li><li>172.16.0.0/12-172.31.255.240/28</li><li>192.168.0.0/16-192.168.255.240/28</li></ul>
    </li><li>If <strong id="b544916498325"><a name="b544916498325"></a><a name="b544916498325"></a>cidr</strong> is not specified, the default value is left blank.</li><li>The value must be in CIDR format, for example, <strong id="b842352706211337_1"><a name="b842352706211337_1"></a><a name="b842352706211337_1"></a>192.168.0.0/16</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{Endpoint}/v1/{project_id}/vpcs
    
    {
        "vpc": {
            "name": "vpc",
            "description": "test",
            "cidr": "192.168.0.0/16"
          
        }
    }
    ```


## Response Message<a name="section33379675"></a>

-   Response parameter

    **Table  4**  Response parameter

    <a name="table1969410815449"></a>
    <table><thead align="left"><tr id="row2499368515449"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p1122260615449"><a name="p1122260615449"></a><a name="p1122260615449"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.15%" id="mcps1.2.4.1.2"><p id="p1310021915449"><a name="p1310021915449"></a><a name="p1310021915449"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.51%" id="mcps1.2.4.1.3"><p id="p5448479815449"><a name="p5448479815449"></a><a name="p5448479815449"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5119248915449"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p5295094915449"><a name="p5295094915449"></a><a name="p5295094915449"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.15%" headers="mcps1.2.4.1.2 "><p id="p18458338205916"><a name="p18458338205916"></a><a name="p18458338205916"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.51%" headers="mcps1.2.4.1.3 "><p id="p393482915449"><a name="p393482915449"></a><a name="p393482915449"></a><a href="#table39714111">Specifies the VPC objects.</a></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  VPC objects

    <a name="table39714111"></a>
    <table><thead align="left"><tr id="row36411928"><th class="cellrowborder" valign="top" width="17.34%" id="mcps1.2.4.1.1"><p id="p63685038"><a name="p63685038"></a><a name="p63685038"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.4.1.2"><p id="p3336232165612"><a name="p3336232165612"></a><a name="p3336232165612"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.919999999999995%" id="mcps1.2.4.1.3"><p id="p17753217"><a name="p17753217"></a><a name="p17753217"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28724493"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.1 "><p id="p44982630"><a name="p44982630"></a><a name="p44982630"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.2 "><p id="p1799372165612"><a name="p1799372165612"></a><a name="p1799372165612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.919999999999995%" headers="mcps1.2.4.1.3 "><p id="p53364125"><a name="p53364125"></a><a name="p53364125"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row10515080"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.1 "><p id="p46415143"><a name="p46415143"></a><a name="p46415143"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.2 "><p id="p11531473165612"><a name="p11531473165612"></a><a name="p11531473165612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.919999999999995%" headers="mcps1.2.4.1.3 "><a name="ul951112614463"></a><a name="ul951112614463"></a><ul id="ul951112614463"><li>Specifies the VPC name.</li><li>The value is a string of no more than 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li><li>Each VPC name of a tenant must be unique if the VPC name is not left blank.</li></ul>
    </td>
    </tr>
    <tr id="row1228919121119"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.1 "><p id="p10612132071113"><a name="p10612132071113"></a><a name="p10612132071113"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.2 "><p id="p9612132031119"><a name="p9612132031119"></a><a name="p9612132031119"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.919999999999995%" headers="mcps1.2.4.1.3 "><a name="ul56121201111"></a><a name="ul56121201111"></a><ul id="ul56121201111"><li>Provides supplementary information about the VPC.</li><li>The value is a string of no more than 255 characters and cannot contain angle brackets (&lt; or &gt;).</li></ul>
    </td>
    </tr>
    <tr id="row19659738"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.1 "><p id="p48934940"><a name="p48934940"></a><a name="p48934940"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.2 "><p id="p61634143165612"><a name="p61634143165612"></a><a name="p61634143165612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.919999999999995%" headers="mcps1.2.4.1.3 "><a name="ul62941023970"></a><a name="ul62941023970"></a><ul id="ul62941023970"><li>Specifies the available IP address ranges for subnets in the VPC.</li><li>Possible values are as follows:<a name="ul162941223376"></a><a name="ul162941223376"></a><ul id="ul162941223376"><li>10.0.0.0/8-10.255.255.240/28</li><li>172.16.0.0/12-172.31.255.240/28</li><li>192.168.0.0/16-192.168.255.240/28</li></ul>
    </li><li>If <strong id="b14339912133312"><a name="b14339912133312"></a><a name="b14339912133312"></a>cidr</strong> is not specified, the default value is left blank.</li><li>The value must be in CIDR format, for example, <strong id="b842352706211337_3"><a name="b842352706211337_3"></a><a name="b842352706211337_3"></a>192.168.0.0/16</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row55195381"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.1 "><p id="p41640866"><a name="p41640866"></a><a name="p41640866"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.2 "><p id="p26309661165612"><a name="p26309661165612"></a><a name="p26309661165612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.919999999999995%" headers="mcps1.2.4.1.3 "><a name="ul14742195924610"></a><a name="ul14742195924610"></a><ul id="ul14742195924610"><li>Specifies the VPC status.</li><li>Possible values are as follows:<a name="ul87091357163310"></a><a name="ul87091357163310"></a><ul id="ul87091357163310"><li><strong id="b842352706152546"><a name="b842352706152546"></a><a name="b842352706152546"></a>CREATING</strong>: The VPC is being created.</li><li><strong id="b18125101851010"><a name="b18125101851010"></a><a name="b18125101851010"></a>OK</strong>: The VPC is created successfully.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row680983192136"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.4.1.1 "><p id="p55159683192136"><a name="p55159683192136"></a><a name="p55159683192136"></a>routes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.2 "><p id="p51691433192136"><a name="p51691433192136"></a><a name="p51691433192136"></a>Array of <a href="#table3576833291556">route</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.919999999999995%" headers="mcps1.2.4.1.3 "><a name="ul088823124710"></a><a name="ul088823124710"></a><ul id="ul088823124710"><li>Specifies the route information.</li><li>For details, see the description of the <a href="#table3576833291556">route objects</a>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **route**  objects

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
    <td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.2.4.1.3 "><a name="ul391783612478"></a><a name="ul391783612478"></a><ul id="ul391783612478"><li>Specifies the destination network segment of a route.</li><li>The value must be in the CIDR format. Currently, only the value <strong>0.0.0.0/0</strong> is supported.</li></ul>
    </td>
    </tr>
    <tr id="row6565233911054"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p1623922311054"><a name="p1623922311054"></a><a name="p1623922311054"></a>nexthop</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.2.4.1.2 "><p id="p4377761311054"><a name="p4377761311054"></a><a name="p4377761311054"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.2.4.1.3 "><a name="ul10508545114715"></a><a name="ul10508545114715"></a><ul id="ul10508545114715"><li>Specifies the next hop of a route.</li><li>The value must be an IP address and must belong to the subnet in the VPC. Otherwise, this value does not take effect.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
     "vpc": 
         {
         "id": "99d9d709-8478-4b46-9f3f-2206b1023fd3",
         "name": "vpc",
         "description": "test",
         "cidr": "192.168.0.0/16",
         "status": "CREATING",
         
         "routes": []
         }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

