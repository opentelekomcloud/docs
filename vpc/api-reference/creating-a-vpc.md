# Creating a VPC<a name="EN-US_TOPIC_0020090608"></a>

## Function<a name="section20114008"></a>

This interface is used to create a VPC.

## URI<a name="section46808346"></a>

-   POST /v1/\{tenant\_id\}/vpcs
-   Parameter description

    <a name="table3672032"></a><table><thead align="left"><tr id="row10026740"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p6859639"><a name="p6859639"></a><a name="p6859639"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p18759866"><a name="p18759866"></a><a name="p18759866"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p43154149"><a name="p43154149"></a><a name="p43154149"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5825185"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p2077973"><a name="p2077973"></a><a name="p2077973"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p34098154"><a name="p34098154"></a><a name="p34098154"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the tenant ID of the operator.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section18621933"></a>

-   Parameter description

    <a name="table59675338144730"></a><table><thead align="left"><tr id="row22732874144730"><th class="cellrowborder" valign="top" width="12.591259125912593%" id="mcps1.1.5.1.1"><p id="p29423469144730"><a name="p29423469144730"></a><a name="p29423469144730"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.122312231223123%" id="mcps1.1.5.1.2"><p id="p34490826144730"><a name="p34490826144730"></a><a name="p34490826144730"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.49204920492049%" id="mcps1.1.5.1.3"><p id="p42293511144730"><a name="p42293511144730"></a><a name="p42293511144730"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.79437943794379%" id="mcps1.1.5.1.4"><p id="p3222348144730"><a name="p3222348144730"></a><a name="p3222348144730"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59683650144730"><td class="cellrowborder" valign="top" width="12.591259125912593%" headers="mcps1.1.5.1.1 "><p id="p2537488144730"><a name="p2537488144730"></a><a name="p2537488144730"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.1.5.1.2 "><p id="p4210015144730"><a name="p4210015144730"></a><a name="p4210015144730"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.49204920492049%" headers="mcps1.1.5.1.3 "><p id="p5466967144730"><a name="p5466967144730"></a><a name="p5466967144730"></a><em id="i5439540717147"><a name="i5439540717147"></a><a name="i5439540717147"></a>Dictionary data structure</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="43.79437943794379%" headers="mcps1.1.5.1.4 "><p id="p32639071144730"><a name="p32639071144730"></a><a name="p32639071144730"></a>Specifies the VPC objects.</p>
    </td>
    </tr>
    </tbody>
    </table>


Descriptions of  **vpc**  fields

<a name="table33750194"></a><table><thead align="left"><tr id="row51192804"><th class="cellrowborder" valign="top" width="13.15%" id="mcps1.1.5.1.1"><p id="p52976421"><a name="p52976421"></a><a name="p52976421"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="18.240000000000002%" id="mcps1.1.5.1.2"><p id="p63231703"><a name="p63231703"></a><a name="p63231703"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.73%" id="mcps1.1.5.1.3"><p id="p2491821616557"><a name="p2491821616557"></a><a name="p2491821616557"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.88%" id="mcps1.1.5.1.4"><p id="p21494305"><a name="p21494305"></a><a name="p21494305"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row63317164"><td class="cellrowborder" valign="top" width="13.15%" headers="mcps1.1.5.1.1 "><p id="p28416672"><a name="p28416672"></a><a name="p28416672"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.1.5.1.2 "><p id="p20049059"><a name="p20049059"></a><a name="p20049059"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.1.5.1.3 "><p id="p510960516557"><a name="p510960516557"></a><a name="p510960516557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.88%" headers="mcps1.1.5.1.4 "><p id="p13361120"><a name="p13361120"></a><a name="p13361120"></a>Specifies the VPC name.</p>
<p id="p8508925"><a name="p8508925"></a><a name="p8508925"></a>The name must be unique for a tenant.</p>
<p id="p9471463"><a name="p9471463"></a><a name="p9471463"></a>The value is a string of no more than 64 characters and can contain digits, letters, underscores (_), hyphens (-), and periods (.).</p>
</td>
</tr>
<tr id="row18134306"><td class="cellrowborder" valign="top" width="13.15%" headers="mcps1.1.5.1.1 "><p id="p59592696"><a name="p59592696"></a><a name="p59592696"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.1.5.1.2 "><p id="p62279078"><a name="p62279078"></a><a name="p62279078"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.1.5.1.3 "><p id="p1122484216557"><a name="p1122484216557"></a><a name="p1122484216557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.88%" headers="mcps1.1.5.1.4 "><p id="p11440597"><a name="p11440597"></a><a name="p11440597"></a>Specifies the available subnets in the VPC.</p>
<p id="p34052821"><a name="p34052821"></a><a name="p34052821"></a>The value must be in CIDR format, for example, <strong>192.168.0.0/16</strong>.</p>
<p id="p38039934"><a name="p38039934"></a><a name="p38039934"></a>The value ranges from <strong>10.0.0.0/8</strong>&nbsp;to&nbsp;<strong>10.255.255.240/28</strong>,&nbsp;<strong>172.16.0.0/12</strong>&nbsp;to&nbsp;<strong>172.31.255.240/28</strong>, or&nbsp;<strong>192.168.0.0/16</strong>&nbsp;to&nbsp;<strong>192.168.255.240/28</strong>.</p>
</td>
</tr>
</tbody>
</table>

-   Example request

    ```
    { 
     "vpc": 
         { 
         "name": "vpc", 
         "cidr": "192.168.0.0/16"
         } 
    }
    ```


## Response<a name="section33379675"></a>

-   Parameter description

<a name="table1969410815449"></a><table><thead align="left"><tr id="row2499368515449"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.1.4.1.1"><p id="p1122260615449"><a name="p1122260615449"></a><a name="p1122260615449"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="22.15%" id="mcps1.1.4.1.2"><p id="p1310021915449"><a name="p1310021915449"></a><a name="p1310021915449"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.51%" id="mcps1.1.4.1.3"><p id="p5448479815449"><a name="p5448479815449"></a><a name="p5448479815449"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5119248915449"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p5295094915449"><a name="p5295094915449"></a><a name="p5295094915449"></a>vpc</p>
</td>
<td class="cellrowborder" valign="top" width="22.15%" headers="mcps1.1.4.1.2 "><p id="p5569931015449"><a name="p5569931015449"></a><a name="p5569931015449"></a><em id="i5439540717147_1"><a name="i5439540717147_1"></a><a name="i5439540717147_1"></a>Dictionary data structure</em></p>
</td>
<td class="cellrowborder" valign="top" width="59.51%" headers="mcps1.1.4.1.3 "><p id="p393482915449"><a name="p393482915449"></a><a name="p393482915449"></a>Specifies the VPC objects.</p>
</td>
</tr>
</tbody>
</table>

Descriptions of  **vpc**  fields

<a name="table39714111"></a><table><thead align="left"><tr id="row36411928"><th class="cellrowborder" valign="top" width="17.34%" id="mcps1.1.4.1.1"><p id="p63685038"><a name="p63685038"></a><a name="p63685038"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="22.74%" id="mcps1.1.4.1.2"><p id="p3336232165612"><a name="p3336232165612"></a><a name="p3336232165612"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.919999999999995%" id="mcps1.1.4.1.3"><p id="p17753217"><a name="p17753217"></a><a name="p17753217"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row28724493"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.4.1.1 "><p id="p44982630"><a name="p44982630"></a><a name="p44982630"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.1.4.1.2 "><p id="p1799372165612"><a name="p1799372165612"></a><a name="p1799372165612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.919999999999995%" headers="mcps1.1.4.1.3 "><p id="p53364125"><a name="p53364125"></a><a name="p53364125"></a>Specifies a resource ID in UUID format.</p>
</td>
</tr>
<tr id="row10515080"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.4.1.1 "><p id="p46415143"><a name="p46415143"></a><a name="p46415143"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.1.4.1.2 "><p id="p11531473165612"><a name="p11531473165612"></a><a name="p11531473165612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.919999999999995%" headers="mcps1.1.4.1.3 "><p id="p56842496"><a name="p56842496"></a><a name="p56842496"></a>Specifies the VPC name.</p>
<p id="p40839433"><a name="p40839433"></a><a name="p40839433"></a>The name must be unique for a tenant.</p>
<p id="p32010577"><a name="p32010577"></a><a name="p32010577"></a>The value is a string of no more than 64 characters and can contain digits, letters, underscores (_), hyphens (-), and periods (.).</p>
</td>
</tr>
<tr id="row19659738"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.4.1.1 "><p id="p48934940"><a name="p48934940"></a><a name="p48934940"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.1.4.1.2 "><p id="p61634143165612"><a name="p61634143165612"></a><a name="p61634143165612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.919999999999995%" headers="mcps1.1.4.1.3 "><p id="p111391011216"><a name="p111391011216"></a><a name="p111391011216"></a>Specifies the available subnets in the VPC.</p>
<p id="p4876088012147"><a name="p4876088012147"></a><a name="p4876088012147"></a>The value must be in CIDR format, for example, <strong>192.168.0.0/16</strong>.</p>
<p id="p1218002912147"><a name="p1218002912147"></a><a name="p1218002912147"></a>The value ranges from <strong>10.0.0.0/8</strong>&nbsp;to&nbsp;<strong>10.255.255.240/28</strong>,&nbsp;<strong>172.16.0.0/12</strong>&nbsp;to&nbsp;<strong>172.31.255.240/28</strong>, or&nbsp;<strong>192.168.0.0/16</strong>&nbsp;to&nbsp;<strong>192.168.255.240/28</strong>.</p>
</td>
</tr>
<tr id="row55195381"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.4.1.1 "><p id="p41640866"><a name="p41640866"></a><a name="p41640866"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.1.4.1.2 "><p id="p26309661165612"><a name="p26309661165612"></a><a name="p26309661165612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.919999999999995%" headers="mcps1.1.4.1.3 "><p id="p5538237"><a name="p5538237"></a><a name="p5538237"></a>Specifies the status of the VPC.</p>
<p id="p30481338"><a name="p30481338"></a><a name="p30481338"></a>The value can be <strong>CREATING</strong>,&nbsp;<strong>OK</strong>,&nbsp;<strong>DOWN</strong>,&nbsp;<strong>PENDING_UPDATE</strong>,&nbsp;<strong>PENDING_DELETE</strong>, or&nbsp;<strong>ERROR</strong>.</p>
</td>
</tr>
<tr id="row680983192136"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.4.1.1 "><p id="p55159683192136"><a name="p55159683192136"></a><a name="p55159683192136"></a>routes</p>
</td>
<td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.1.4.1.2 "><p id="p51691433192136"><a name="p51691433192136"></a><a name="p51691433192136"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="59.919999999999995%" headers="mcps1.1.4.1.3 "><p id="p26256563192136"><a name="p26256563192136"></a><a name="p26256563192136"></a>Specifies the route information.</p>
<p id="p42971876202757"><a name="p42971876202757"></a><a name="p42971876202757"></a>For details, see descriptions of <strong>route</strong> fields.</p>
</td>
</tr>
</tbody>
</table>

Descriptions of  **route**  fields

<a name="table3576833291556"></a><table><thead align="left"><tr id="row921218691556"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.1.4.1.1"><p id="p798956991556"><a name="p798956991556"></a><a name="p798956991556"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="22.38%" id="mcps1.1.4.1.2"><p id="p754435891556"><a name="p754435891556"></a><a name="p754435891556"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.28%" id="mcps1.1.4.1.3"><p id="p711326791556"><a name="p711326791556"></a><a name="p711326791556"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3930377391556"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p2948903591556"><a name="p2948903591556"></a><a name="p2948903591556"></a>destination</p>
</td>
<td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.1.4.1.2 "><p id="p270722191556"><a name="p270722191556"></a><a name="p270722191556"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.1.4.1.3 "><p id="p2740730591556"><a name="p2740730591556"></a><a name="p2740730591556"></a>Specifies the destination network segment of a route.</p>
<p id="p2436469411021"><a name="p2436469411021"></a><a name="p2436469411021"></a>The value must be in the CIDR format. Currently, only the value <strong id="b842352706144646"><a name="b842352706144646"></a><a name="b842352706144646"></a>0.0.0.0/0</strong> is supported.</p>
</td>
</tr>
<tr id="row6565233911054"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p1623922311054"><a name="p1623922311054"></a><a name="p1623922311054"></a>nexthop</p>
</td>
<td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.1.4.1.2 "><p id="p4377761311054"><a name="p4377761311054"></a><a name="p4377761311054"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.28%" headers="mcps1.1.4.1.3 "><p id="p5632574211054"><a name="p5632574211054"></a><a name="p5632574211054"></a>Specifies the next hop of a route.</p>
<p id="p2794258711440"><a name="p2794258711440"></a><a name="p2794258711440"></a>The value must be an IP address and must belong to the subnet in the VPC. Otherwise, this value does not take effect.</p>
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
         "cidr": "192.168.0.0/16",
         "status": "CREATING",
         "routes": null
         }
    }
    ```


## Returned Value<a name="section31981619"></a>

-   Normal

    200

-   Abnormal

    <a name="table29386549503"></a><table><thead align="left"><tr id="row481907099503"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p111333969503"><a name="p111333969503"></a><a name="p111333969503"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p293899169503"><a name="p293899169503"></a><a name="p293899169503"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row317729809503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p234745649503"><a name="p234745649503"></a><a name="p234745649503"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p223915419503"><a name="p223915419503"></a><a name="p223915419503"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row1972819503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p159798149503"><a name="p159798149503"></a><a name="p159798149503"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p192965439503"><a name="p192965439503"></a><a name="p192965439503"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row394511639503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p414276149503"><a name="p414276149503"></a><a name="p414276149503"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1935459503"><a name="p1935459503"></a><a name="p1935459503"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row17419099503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p68769779503"><a name="p68769779503"></a><a name="p68769779503"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p201642329503"><a name="p201642329503"></a><a name="p201642329503"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row472603669503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p28844609503"><a name="p28844609503"></a><a name="p28844609503"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p323146829503"><a name="p323146829503"></a><a name="p323146829503"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row223966829503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p21919729503"><a name="p21919729503"></a><a name="p21919729503"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p433320349503"><a name="p433320349503"></a><a name="p433320349503"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row544439909503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p478870949503"><a name="p478870949503"></a><a name="p478870949503"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p536494239503"><a name="p536494239503"></a><a name="p536494239503"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row130827609503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p530706009503"><a name="p530706009503"></a><a name="p530706009503"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p37513169503"><a name="p37513169503"></a><a name="p37513169503"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row337618519503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p503553979503"><a name="p503553979503"></a><a name="p503553979503"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p522553769503"><a name="p522553769503"></a><a name="p522553769503"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row5363419503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p434436849503"><a name="p434436849503"></a><a name="p434436849503"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p292775119503"><a name="p292775119503"></a><a name="p292775119503"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row621710129503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p26872019503"><a name="p26872019503"></a><a name="p26872019503"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p163367109503"><a name="p163367109503"></a><a name="p163367109503"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row128126689503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p311931539503"><a name="p311931539503"></a><a name="p311931539503"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p436174429503"><a name="p436174429503"></a><a name="p436174429503"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row570126659503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p546231859503"><a name="p546231859503"></a><a name="p546231859503"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p624018499503"><a name="p624018499503"></a><a name="p624018499503"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row247457309503"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p582471429503"><a name="p582471429503"></a><a name="p582471429503"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p203980629503"><a name="p203980629503"></a><a name="p203980629503"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section85821649202813"></a>

For details, see section  [Error Codes](error-codes-27.md).

