# Querying Scaling Action Logs \(V2\)<a name="EN-US_TOPIC_0141976500"></a>

## Function<a name="section37368030"></a>

This interface is used to query scaling action logs based on search criteria. The scaling actions include increasing instances and migrating instances to balance load. The results are displayed by page.

-   The difference between the V2 and V1 interfaces for querying scaling action logs is that V2 displays more detailed action logs, such as ELB migration logs.
-   Search criteria can be the start time, end time, start line number, number of records, and scaling action type.
-   If no search criteria are specified, a maximum of 20 scaling action logs can be queried by default.

## URI<a name="section767958"></a>

GET /autoscaling-api/v2/\{project\_id\}/scaling\_activity\_log/\{scaling\_group\_id\}

>![](/images/icon-note.gif) **NOTE:**   
>You can type the question mark \(?\) and ampersand \(&\) at the end of the URI to define multiple search criteria. Scaling action logs can be searched by all optional parameters in the following table. For details, see the example request.  

**Table  1**  Parameter description

<a name="table34134946"></a>
<table><thead align="left"><tr id="row52638042"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p35823022"><a name="p35823022"></a><a name="p35823022"></a><strong id="b1997413551123"><a name="b1997413551123"></a><a name="b1997413551123"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p15983633"><a name="p15983633"></a><a name="p15983633"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p19605934"><a name="p19605934"></a><a name="p19605934"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="p44576811"><a name="p44576811"></a><a name="p44576811"></a><strong id="b44317574219"><a name="b44317574219"></a><a name="b44317574219"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row53951920"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p8029414"><a name="p8029414"></a><a name="p8029414"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p46402804"><a name="p46402804"></a><a name="p46402804"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p530819"><a name="p530819"></a><a name="p530819"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row51423381"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p4544348"><a name="p4544348"></a><a name="p4544348"></a>scaling_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p32547936"><a name="p32547936"></a><a name="p32547936"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p19137160"><a name="p19137160"></a><a name="p19137160"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p6606141"><a name="p6606141"></a><a name="p6606141"></a>Specifies the AS group ID.</p>
</td>
</tr>
<tr id="row1961714575714"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p96175458573"><a name="p96175458573"></a><a name="p96175458573"></a>log_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p1761704510577"><a name="p1761704510577"></a><a name="p1761704510577"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p13596104914575"><a name="p13596104914575"></a><a name="p13596104914575"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p11617184514574"><a name="p11617184514574"></a><a name="p11617184514574"></a>Specifies the scaling action log ID.</p>
</td>
</tr>
<tr id="row59455271"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p51147674"><a name="p51147674"></a><a name="p51147674"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p49320909"><a name="p49320909"></a><a name="p49320909"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p35570664"><a name="p35570664"></a><a name="p35570664"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p62651540"><a name="p62651540"></a><a name="p62651540"></a>Specifies the start time that complies with UTC for querying scaling action logs. The format of the start time is <strong id="b14044178162939"><a name="b14044178162939"></a><a name="b14044178162939"></a>yyyy-MM-ddThh:mm:ssZ</strong>.</p>
</td>
</tr>
<tr id="row26992952"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p38945471"><a name="p38945471"></a><a name="p38945471"></a>end_time</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p466603"><a name="p466603"></a><a name="p466603"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p37794916"><a name="p37794916"></a><a name="p37794916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p41489361"><a name="p41489361"></a><a name="p41489361"></a>Specifies the end time that complies with UTC for querying scaling action logs. The format of the end time is <strong id="b11263138162939"><a name="b11263138162939"></a><a name="b11263138162939"></a>yyyy-MM-ddThh:mm:ssZ</strong>.</p>
</td>
</tr>
<tr id="row37859935"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p46755894"><a name="p46755894"></a><a name="p46755894"></a>start_number</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p29131061"><a name="p29131061"></a><a name="p29131061"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p10805765"><a name="p10805765"></a><a name="p10805765"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p59373825"><a name="p59373825"></a><a name="p59373825"></a>Specifies the start line number. The default value is <strong id="b1485413357018"><a name="b1485413357018"></a><a name="b1485413357018"></a>0</strong>. The minimum parameter value is <strong id="b18744142621611"><a name="b18744142621611"></a><a name="b18744142621611"></a>0</strong>.</p>
</td>
</tr>
<tr id="row25666111"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p65689071"><a name="p65689071"></a><a name="p65689071"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p19214507"><a name="p19214507"></a><a name="p19214507"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p12871260"><a name="p12871260"></a><a name="p12871260"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p21968676"><a name="p21968676"></a><a name="p21968676"></a>Specifies the number of query records. The default value is <strong id="b168447885495335"><a name="b168447885495335"></a><a name="b168447885495335"></a>20</strong>. The value range is 0 to 100.</p>
</td>
</tr>
<tr id="row0863844830"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p5407546231"><a name="p5407546231"></a><a name="p5407546231"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p64073468314"><a name="p64073468314"></a><a name="p64073468314"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p104071346434"><a name="p104071346434"></a><a name="p104071346434"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p740744613313"><a name="p740744613313"></a><a name="p740744613313"></a>Specifies the types of the scaling actions to be queried. Different types are separated by commas (,).</p>
<a name="ul12513726546"></a><a name="ul12513726546"></a><ul id="ul12513726546"><li><strong id="b1914793241511"><a name="b1914793241511"></a><a name="b1914793241511"></a>NORMAL</strong>: indicates a common scaling action.</li><li><strong id="b25101655151520"><a name="b25101655151520"></a><a name="b25101655151520"></a>MANUAL_REMOVE</strong>: indicates manually removing instances from an AS group.</li><li><strong id="b75377258178"><a name="b75377258178"></a><a name="b75377258178"></a>MANUAL_DELETE</strong>: indicates manually removing and deleting instances from an AS group.</li><li><strong id="b358111419188"><a name="b358111419188"></a><a name="b358111419188"></a>MANUAL_ADD</strong>: indicates manually adding instances to an AS group.</li><li><strong id="b1025644410187"><a name="b1025644410187"></a><a name="b1025644410187"></a>ELB_CHECK_DELETE</strong>: indicates that instances are removed from an AS group and deleted based on the ELB health check result.</li><li><strong id="b69341817172015"><a name="b69341817172015"></a><a name="b69341817172015"></a>AUDIT_CHECK_DELETE</strong>: indicates that instances are removed from an AS group and deleted based on the OpenStack audit.</li><li><strong id="b396793182115"><a name="b396793182115"></a><a name="b396793182115"></a>DIFF</strong>: indicates that the number of expected instances is different from the actual number of instances.</li><li><strong id="b1226105317210"><a name="b1226105317210"></a><a name="b1226105317210"></a>MODIFY_ELB</strong>: indicates the load balancer migration.</li></ul>
</td>
</tr>
<tr id="row17585104714498"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p7585347184917"><a name="p7585347184917"></a><a name="p7585347184917"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p16585134784916"><a name="p16585134784916"></a><a name="p16585134784916"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p158512477494"><a name="p158512477494"></a><a name="p158512477494"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p548341495012"><a name="p548341495012"></a><a name="p548341495012"></a>Specifies the status of the scaling action.</p>
<a name="ul41131372506"></a><a name="ul41131372506"></a><ul id="ul41131372506"><li><strong id="b19351324113913"><a name="b19351324113913"></a><a name="b19351324113913"></a>SUCCESS</strong>: The scaling action has been performed.</li><li><strong id="b18717131515"><a name="b18717131515"></a><a name="b18717131515"></a>FAIL</strong>: Performing the scaling action failed.</li><li><strong id="b3237638111513"><a name="b3237638111513"></a><a name="b3237638111513"></a>DOING</strong>: The scaling action is being performed.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section6911623"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query the scaling action logs of the AS group with ID  **e5d27f5c-dd76-4a61-b4bc-a67c5686719a**. The start time is 2018-11-22T00:00:00Z, and the end time is 2018-11-22T14:00:00Z.

    ```
    GET https://{Endpoint}/autoscaling-api/v2/{project_id}/scaling_activity_log/e5d27f5c-dd76-4a61-b4bc-a67c5686719a?start_time=2018-11-22T00:00:00Z&end_time=2018-11-22T14:00:00Z
    ```


## Response Message<a name="section62204612"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table23410136"></a>
    <table><thead align="left"><tr id="row62549356"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.1"><p id="p33333103"><a name="p33333103"></a><a name="p33333103"></a><strong id="b7288809310"><a name="b7288809310"></a><a name="b7288809310"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="p15626802"><a name="p15626802"></a><a name="p15626802"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="p57811421"><a name="p57811421"></a><a name="p57811421"></a><strong id="b13781011032"><a name="b13781011032"></a><a name="b13781011032"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52213529"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p1437453"><a name="p1437453"></a><a name="p1437453"></a>total_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p49324898"><a name="p49324898"></a><a name="p49324898"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p35893824"><a name="p35893824"></a><a name="p35893824"></a>Specifies the total number of query records.</p>
    </td>
    </tr>
    <tr id="row54608961"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p61249726"><a name="p61249726"></a><a name="p61249726"></a>start_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p62280792"><a name="p62280792"></a><a name="p62280792"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p11579382"><a name="p11579382"></a><a name="p11579382"></a>Specifies the start line number.</p>
    </td>
    </tr>
    <tr id="row37105578"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p52761866"><a name="p52761866"></a><a name="p52761866"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p45852771"><a name="p45852771"></a><a name="p45852771"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p23086940"><a name="p23086940"></a><a name="p23086940"></a>Specifies the maximum number of resources to be queried.</p>
    </td>
    </tr>
    <tr id="row6455868"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p53163272"><a name="p53163272"></a><a name="p53163272"></a>scaling_activity_log</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p11257801"><a name="p11257801"></a><a name="p11257801"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p39466727"><a name="p39466727"></a><a name="p39466727"></a>Specifies scaling action logs. For details, see <a href="#table5100505111129">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scaling\_activity\_log**  field description

    <a name="table5100505111129"></a>
    <table><thead align="left"><tr id="r2f50795d76cf453c9dc60f658a624810"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.1"><p id="a69f0ad0844e544b9a8cd7c6c96155fdf"><a name="a69f0ad0844e544b9a8cd7c6c96155fdf"></a><a name="a69f0ad0844e544b9a8cd7c6c96155fdf"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="a3dfdc81a6cc0409db1eedc7cf822ed37"><a name="a3dfdc81a6cc0409db1eedc7cf822ed37"></a><a name="a3dfdc81a6cc0409db1eedc7cf822ed37"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="a8238ba808fdb4829b4f15ea7e48befa2"><a name="a8238ba808fdb4829b4f15ea7e48befa2"></a><a name="a8238ba808fdb4829b4f15ea7e48befa2"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r74ce6d1664164a38b25d42101210a7c0"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="a47bbfe35b287448db539f535eff78327"><a name="a47bbfe35b287448db539f535eff78327"></a><a name="a47bbfe35b287448db539f535eff78327"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="a3e1edba5712c431cabcd001866b1b410"><a name="a3e1edba5712c431cabcd001866b1b410"></a><a name="a3e1edba5712c431cabcd001866b1b410"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="a0346256b63b14f3a956d7d5f32b83134"><a name="a0346256b63b14f3a956d7d5f32b83134"></a><a name="a0346256b63b14f3a956d7d5f32b83134"></a>Specifies the status of the scaling action.</p>
    <a name="ul346119411218"></a><a name="ul346119411218"></a><ul id="ul346119411218"><li><strong id="b19351324113913_1"><a name="b19351324113913_1"></a><a name="b19351324113913_1"></a>SUCCESS</strong>: The scaling action has been performed.</li><li><strong id="b10147194110395"><a name="b10147194110395"></a><a name="b10147194110395"></a>FAIL</strong>: Performing the scaling action failed.</li><li><strong id="b1641345583914"><a name="b1641345583914"></a><a name="b1641345583914"></a>DOING</strong>: The scaling action is being performed.</li></ul>
    </td>
    </tr>
    <tr id="rbbfd1b372fcb4b0baddc196b7d09df49"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="a008e65853fde473b8450d208c18d69e0"><a name="a008e65853fde473b8450d208c18d69e0"></a><a name="a008e65853fde473b8450d208c18d69e0"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="a11a097f6ba114149932d358048dbc3ce"><a name="a11a097f6ba114149932d358048dbc3ce"></a><a name="a11a097f6ba114149932d358048dbc3ce"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="a0c1c1d336fc64fc586107d994ca5baa8"><a name="a0c1c1d336fc64fc586107d994ca5baa8"></a><a name="a0c1c1d336fc64fc586107d994ca5baa8"></a>Specifies the start time of the scaling action. The time format must comply with UTC.</p>
    </td>
    </tr>
    <tr id="r3ce78f22df7540a6b8ca010f03ee8764"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="ad1345bea1ad4473a90bf1ac673b1e722"><a name="ad1345bea1ad4473a90bf1ac673b1e722"></a><a name="ad1345bea1ad4473a90bf1ac673b1e722"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="adebff9ceb0c94e8da3278ab781c33a0e"><a name="adebff9ceb0c94e8da3278ab781c33a0e"></a><a name="adebff9ceb0c94e8da3278ab781c33a0e"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="a59970e70708b45fd876375d5a8b039ce"><a name="a59970e70708b45fd876375d5a8b039ce"></a><a name="a59970e70708b45fd876375d5a8b039ce"></a>Specifies the end time of the scaling action. The time format must comply with UTC.</p>
    </td>
    </tr>
    <tr id="r353afd89b086409b87683d796011ea0d"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="a2b1b93d204c9427b962d16643bb54bd0"><a name="a2b1b93d204c9427b962d16643bb54bd0"></a><a name="a2b1b93d204c9427b962d16643bb54bd0"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="a96c0e7acbc3345bfa0b96f2f2730af76"><a name="a96c0e7acbc3345bfa0b96f2f2730af76"></a><a name="a96c0e7acbc3345bfa0b96f2f2730af76"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="a53a786e08fb340138998e54070a09a16"><a name="a53a786e08fb340138998e54070a09a16"></a><a name="a53a786e08fb340138998e54070a09a16"></a>Specifies the scaling action log ID.</p>
    </td>
    </tr>
    <tr id="r2a965ee79b664b7dbb172f7c13211adc"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="ac587d719a7494651835024bc76830e6d"><a name="ac587d719a7494651835024bc76830e6d"></a><a name="ac587d719a7494651835024bc76830e6d"></a>instance_removed_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="ab41902ac9f224f77b5694422279e4a27"><a name="ab41902ac9f224f77b5694422279e4a27"></a><a name="ab41902ac9f224f77b5694422279e4a27"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0021400639_p672823715567"><a name="en-us_topic_0021400639_p672823715567"></a><a name="en-us_topic_0021400639_p672823715567"></a>Specifies names of the ECSs that are removed from the AS group in a scaling action. For details, see <a href="#table54708193137">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="rae14399a79384a1fa32f64132c5063e7"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0021400639_p593774715567"><a name="en-us_topic_0021400639_p593774715567"></a><a name="en-us_topic_0021400639_p593774715567"></a>instance_deleted_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="adf76f011c5004c0ab0734c7581eb0616"><a name="adf76f011c5004c0ab0734c7581eb0616"></a><a name="adf76f011c5004c0ab0734c7581eb0616"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="af42ad1a314304e9eb473095b14730ef3"><a name="af42ad1a314304e9eb473095b14730ef3"></a><a name="af42ad1a314304e9eb473095b14730ef3"></a>Specifies names of the ECSs that are removed from the AS group and deleted in a scaling action. For details, see <a href="#table54708193137">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="r2b10b36488f14a8abe004656288f6ee3"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="af9614300bbba4ca29bf63f4c25a4cbf6"><a name="af9614300bbba4ca29bf63f4c25a4cbf6"></a><a name="af9614300bbba4ca29bf63f4c25a4cbf6"></a>instance_added_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0021400639_p804543115567"><a name="en-us_topic_0021400639_p804543115567"></a><a name="en-us_topic_0021400639_p804543115567"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="aa7a68694a8d7497cbaf64c6d128195a0"><a name="aa7a68694a8d7497cbaf64c6d128195a0"></a><a name="aa7a68694a8d7497cbaf64c6d128195a0"></a>Specifies names of the ECSs that are added to the AS group in a scaling action. For details, see <a href="#table54708193137">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row25543207614"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p331452812620"><a name="p331452812620"></a><a name="p331452812620"></a>instance_failed_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1931413289618"><a name="p1931413289618"></a><a name="p1931413289618"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p131472819613"><a name="p131472819613"></a><a name="p131472819613"></a>Specifies the ECSs for which a scaling action fails. For details, see <a href="#table54708193137">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="rd2b0cba3f6ac4f85a61bd72efff96a76"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="adf005843b6f04767a113662ad46f2a46"><a name="adf005843b6f04767a113662ad46f2a46"></a><a name="adf005843b6f04767a113662ad46f2a46"></a>scaling_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="abba7c061addb4776ae0612c65f4d8d5c"><a name="abba7c061addb4776ae0612c65f4d8d5c"></a><a name="abba7c061addb4776ae0612c65f4d8d5c"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0021400639_p3081215567"><a name="en-us_topic_0021400639_p3081215567"></a><a name="en-us_topic_0021400639_p3081215567"></a>Specifies the number of added or deleted instances during the scaling.</p>
    </td>
    </tr>
    <tr id="rfa29ea8a914e452a84f738e1c56efdc1"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="a97f9d365379e45eba520166fa1ba0d8d"><a name="a97f9d365379e45eba520166fa1ba0d8d"></a><a name="a97f9d365379e45eba520166fa1ba0d8d"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0021400639_p748687915567"><a name="en-us_topic_0021400639_p748687915567"></a><a name="en-us_topic_0021400639_p748687915567"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0021400639_p245743015567"><a name="en-us_topic_0021400639_p245743015567"></a><a name="en-us_topic_0021400639_p245743015567"></a>Specifies the description of the scaling action.</p>
    </td>
    </tr>
    <tr id="re7f4724989884b4488b2af0f7f8feaa2"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="a933a6e84e9c14f5cadfe840317e33c32"><a name="a933a6e84e9c14f5cadfe840317e33c32"></a><a name="a933a6e84e9c14f5cadfe840317e33c32"></a>instance_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="ae46063a5a6d84619bcc7dde0e0dd7a76"><a name="ae46063a5a6d84619bcc7dde0e0dd7a76"></a><a name="ae46063a5a6d84619bcc7dde0e0dd7a76"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="a137ae1c7eb2b4cd0a938c0d9509e462f"><a name="a137ae1c7eb2b4cd0a938c0d9509e462f"></a><a name="a137ae1c7eb2b4cd0a938c0d9509e462f"></a>Specifies the number of instances in the AS group.</p>
    </td>
    </tr>
    <tr id="rab90ab2baf6e48eb801e81e791e8b45c"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="a3abee0c2188d4a83862789649dc4462a"><a name="a3abee0c2188d4a83862789649dc4462a"></a><a name="a3abee0c2188d4a83862789649dc4462a"></a>desire_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0021400639_p585410715567"><a name="en-us_topic_0021400639_p585410715567"></a><a name="en-us_topic_0021400639_p585410715567"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0021400639_p442063415567"><a name="en-us_topic_0021400639_p442063415567"></a><a name="en-us_topic_0021400639_p442063415567"></a>Specifies the expected number of instances for the scaling action.</p>
    </td>
    </tr>
    <tr id="row939415311717"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p183391431385"><a name="p183391431385"></a><a name="p183391431385"></a>lb_bind_success_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p9893532506"><a name="p9893532506"></a><a name="p9893532506"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p63391431387"><a name="p63391431387"></a><a name="p63391431387"></a>Specifies the load balancers that are bound to the AS group. For details, see <a href="#table1680205901311">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row1594410331173"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p133391932811"><a name="p133391932811"></a><a name="p133391932811"></a>lb_bind_failed_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p33391311818"><a name="p33391311818"></a><a name="p33391311818"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p10339631781"><a name="p10339631781"></a><a name="p10339631781"></a>Specifies the load balancers that failed to be bound to the AS group. For details, see <a href="#table1680205901311">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row111380458710"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p1433993881"><a name="p1433993881"></a><a name="p1433993881"></a>lb_unbind_success_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p272519486507"><a name="p272519486507"></a><a name="p272519486507"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p5339331982"><a name="p5339331982"></a><a name="p5339331982"></a>Specifies the load balancers that are unbound from the AS group. For details, see <a href="#table1680205901311">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row343744814712"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p20339163481"><a name="p20339163481"></a><a name="p20339163481"></a>lb_unbind_failed_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p6339193387"><a name="p6339193387"></a><a name="p6339193387"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1934017312818"><a name="p1934017312818"></a><a name="p1934017312818"></a>Specifies the load balancers that failed to be unbound from the AS group. For details, see <a href="#table1680205901311">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row175611952572"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p11340531382"><a name="p11340531382"></a><a name="p11340531382"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p3340173280"><a name="p3340173280"></a><a name="p3340173280"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p834053287"><a name="p834053287"></a><a name="p834053287"></a>Specifies the type of the scaling action.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **scaling\_instance**  field description

    <a name="table54708193137"></a>
    <table><thead align="left"><tr id="row16471131931311"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.1"><p id="p1166033415138"><a name="p1166033415138"></a><a name="p1166033415138"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="11%" id="mcps1.2.4.1.2"><p id="p966013419133"><a name="p966013419133"></a><a name="p966013419133"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p16660113414136"><a name="p16660113414136"></a><a name="p16660113414136"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8471101914131"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p1066015343137"><a name="p1066015343137"></a><a name="p1066015343137"></a>instance_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p4660334161318"><a name="p4660334161318"></a><a name="p4660334161318"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p366063401315"><a name="p366063401315"></a><a name="p366063401315"></a>Specifies the ECS name.</p>
    </td>
    </tr>
    <tr id="row6471161991317"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p666043471312"><a name="p666043471312"></a><a name="p666043471312"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p76601934121310"><a name="p76601934121310"></a><a name="p76601934121310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p19660334171314"><a name="p19660334171314"></a><a name="p19660334171314"></a>Specifies the ECS ID.</p>
    </td>
    </tr>
    <tr id="row1547181941316"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p156601234121320"><a name="p156601234121320"></a><a name="p156601234121320"></a>failed_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p1166043471316"><a name="p1166043471316"></a><a name="p1166043471316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p16660123414134"><a name="p16660123414134"></a><a name="p16660123414134"></a>Specifies the cause of the instance scaling failure.</p>
    </td>
    </tr>
    <tr id="row1471141917138"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p4299194141310"><a name="p4299194141310"></a><a name="p4299194141310"></a>failed_details</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p10300741191320"><a name="p10300741191320"></a><a name="p10300741191320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p8300184114138"><a name="p8300184114138"></a><a name="p8300184114138"></a>Specifies details of the instance scaling failure.</p>
    </td>
    </tr>
    <tr id="row17715017203510"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p14281152443513"><a name="p14281152443513"></a><a name="p14281152443513"></a>instance_config</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p92811824163513"><a name="p92811824163513"></a><a name="p92811824163513"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p10281102433513"><a name="p10281102433513"></a><a name="p10281102433513"></a>Specifies the information about instance configurations.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **modify\_lb**  field description

    <a name="table1680205901311"></a>
    <table><thead align="left"><tr id="row169195931319"><th class="cellrowborder" valign="top" width="26.732673267326735%" id="mcps1.2.4.1.1"><p id="p1094155912136"><a name="p1094155912136"></a><a name="p1094155912136"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.4.1.2"><p id="p15117155971319"><a name="p15117155971319"></a><a name="p15117155971319"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.37623762376238%" id="mcps1.2.4.1.3"><p id="p151211059181317"><a name="p151211059181317"></a><a name="p151211059181317"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8124145951311"><td class="cellrowborder" valign="top" width="26.732673267326735%" headers="mcps1.2.4.1.1 "><p id="p370235510152"><a name="p370235510152"></a><a name="p370235510152"></a>lbaas_listener</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.4.1.2 "><p id="p77023552159"><a name="p77023552159"></a><a name="p77023552159"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.37623762376238%" headers="mcps1.2.4.1.3 "><p id="p270213558151"><a name="p270213558151"></a><a name="p270213558151"></a>Specifies information about an enhanced load balancer. For details, see <a href="#table153260162">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row19135559201316"><td class="cellrowborder" valign="top" width="26.732673267326735%" headers="mcps1.2.4.1.1 "><p id="p157021855191518"><a name="p157021855191518"></a><a name="p157021855191518"></a>listener</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.4.1.2 "><p id="p16702115516159"><a name="p16702115516159"></a><a name="p16702115516159"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.37623762376238%" headers="mcps1.2.4.1.3 "><p id="p5702125514157"><a name="p5702125514157"></a><a name="p5702125514157"></a>Specifies information about a classic load balancer.</p>
    </td>
    </tr>
    <tr id="row814785915137"><td class="cellrowborder" valign="top" width="26.732673267326735%" headers="mcps1.2.4.1.1 "><p id="p1670217557158"><a name="p1670217557158"></a><a name="p1670217557158"></a>failed_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.4.1.2 "><p id="p1270265517156"><a name="p1270265517156"></a><a name="p1270265517156"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.37623762376238%" headers="mcps1.2.4.1.3 "><p id="p7702135511514"><a name="p7702135511514"></a><a name="p7702135511514"></a>Specifies the cause of a load balancer migration failure.</p>
    </td>
    </tr>
    <tr id="row10157105951316"><td class="cellrowborder" valign="top" width="26.732673267326735%" headers="mcps1.2.4.1.1 "><p id="p1270495511512"><a name="p1270495511512"></a><a name="p1270495511512"></a>failed_details</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.4.1.2 "><p id="p137043554155"><a name="p137043554155"></a><a name="p137043554155"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.37623762376238%" headers="mcps1.2.4.1.3 "><p id="p18704145531516"><a name="p18704145531516"></a><a name="p18704145531516"></a>Specifies the details of a load balancer migration failure.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **lbaas\_listener**  field description

    <a name="table153260162"></a>
    <table><thead align="left"><tr id="row1117826161613"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.1"><p id="p322112611165"><a name="p322112611165"></a><a name="p322112611165"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="11%" id="mcps1.2.4.1.2"><p id="p16251726111618"><a name="p16251726111618"></a><a name="p16251726111618"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p928326171613"><a name="p928326171613"></a><a name="p928326171613"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23192612165"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p1844110159170"><a name="p1844110159170"></a><a name="p1844110159170"></a>listener_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p544118157174"><a name="p544118157174"></a><a name="p544118157174"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p944141513172"><a name="p944141513172"></a><a name="p944141513172"></a>Specifies the listener ID.</p>
    </td>
    </tr>
    <tr id="row240026101615"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p17441815191716"><a name="p17441815191716"></a><a name="p17441815191716"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p104412158173"><a name="p104412158173"></a><a name="p104412158173"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p10441915141711"><a name="p10441915141711"></a><a name="p10441915141711"></a>Specifies the backend ECS group ID.</p>
    </td>
    </tr>
    <tr id="row15518266164"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p14441415151716"><a name="p14441415151716"></a><a name="p14441415151716"></a>protocol_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p244151531712"><a name="p244151531712"></a><a name="p244151531712"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p16441915121718"><a name="p16441915121718"></a><a name="p16441915121718"></a>Specifies the backend protocol port, which is the port on which a backend ECS listens for traffic.</p>
    </td>
    </tr>
    <tr id="row1362122621618"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.1 "><p id="p1044191519179"><a name="p1044191519179"></a><a name="p1044191519179"></a>weight</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.4.1.2 "><p id="p184417156173"><a name="p184417156173"></a><a name="p184417156173"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p13441131511177"><a name="p13441131511177"></a><a name="p13441131511177"></a>Specifies the weight, which determines the portion of requests a backend ECS processes when being compared to other backend ECSs added to the same listener.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "limit": 20,
        "scaling_activity_log": [
        {
          "id": "8753a18c-931d-4cb8-8d49-6c99396af348",
          "instance_value": 0,
          "desire_value": 0,
          "scaling_value": 0,
          "start_time": "2018-11-22T13:46:20Z",
          "end_time": "2018-11-22T13:47:38Z",
          "status": "SUCCESS",
          "lb_bind_success_list": [
            {
              "lbaas_listener": {
                "weight": 1,
                "listener_id": null,
                "pool_id": "0f0a9dd8-2e1d-4432-8ca2-49adc75aa662",
                "protocol_port": 82
              }
            }
          ],
          "lb_bind_failed_list": [],
          "lb_unbind_success_list": [],
          "lb_unbind_failed_list": [],
          "type": "MODIFY_ELB"
        },
        {
          "id": "44152cf2-a005-4507-b6e9-66a2a64eff52",
          "instance_value": 0,
          "desire_value": 1,
          "scaling_value": 1,
          "start_time": "2018-11-22T13:44:22Z",
          "end_time": "2018-11-22T13:46:02Z",
          "instance_added_list": [
            {
              "instance_id": "8e273bac-d303-46dc-9883-628be2294bdf",
              "instance_name": "as-config-t66a_9W8L9SSK"
            }
          ],
          "instance_deleted_list": [],
          "instance_removed_list": [],
          "instance_failed_list": [],
          "status": "SUCCESS",
          "description": "{\"reason\":[{\"change_reason\":\"MANNUAL\",\"old_value\":0,\"change_time\":\"2018-11-22T13:44:19Z\",\"new_value\":1}]}",
          "type": "NORMAL"
        }
    ],
        "total_number": 2,
        "start_number": 0
    }
    ```


## Returned Values<a name="section22970596"></a>

-   Normal

    200

-   Abnormal

    <a name="table15568903"></a>
    <table><thead align="left"><tr id="row3870635"><th class="cellrowborder" valign="top" width="32.67%" id="mcps1.1.3.1.1"><p id="p45086037"><a name="p45086037"></a><a name="p45086037"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="67.33%" id="mcps1.1.3.1.2"><p id="p28090371"><a name="p28090371"></a><a name="p28090371"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60727582"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p19987085"><a name="p19987085"></a><a name="p19987085"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p8341177"><a name="p8341177"></a><a name="p8341177"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row7961729"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p40920274"><a name="p40920274"></a><a name="p40920274"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p26207892"><a name="p26207892"></a><a name="p26207892"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row34544438"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p46636132"><a name="p46636132"></a><a name="p46636132"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p19430358"><a name="p19430358"></a><a name="p19430358"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row40655501"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p4761248"><a name="p4761248"></a><a name="p4761248"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p50116845"><a name="p50116845"></a><a name="p50116845"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row48398424"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p27958252"><a name="p27958252"></a><a name="p27958252"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p50025933"><a name="p50025933"></a><a name="p50025933"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row47580213"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p28792051"><a name="p28792051"></a><a name="p28792051"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p50454834"><a name="p50454834"></a><a name="p50454834"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row51440330"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p5917164"><a name="p5917164"></a><a name="p5917164"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p9528291"><a name="p9528291"></a><a name="p9528291"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row18645762"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p33911763"><a name="p33911763"></a><a name="p33911763"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p62498284"><a name="p62498284"></a><a name="p62498284"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row25613652"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p61439917"><a name="p61439917"></a><a name="p61439917"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p10577379"><a name="p10577379"></a><a name="p10577379"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row28087548"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p60498887"><a name="p60498887"></a><a name="p60498887"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p1462819"><a name="p1462819"></a><a name="p1462819"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row13165375"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p59762422"><a name="p59762422"></a><a name="p59762422"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p8918034"><a name="p8918034"></a><a name="p8918034"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row13153450"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p58796504"><a name="p58796504"></a><a name="p58796504"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p64896350"><a name="p64896350"></a><a name="p64896350"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row47196242"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p64799248"><a name="p64799248"></a><a name="p64799248"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p14247739"><a name="p14247739"></a><a name="p14247739"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row61120788"><td class="cellrowborder" valign="top" width="32.67%" headers="mcps1.1.3.1.1 "><p id="p51836813"><a name="p51836813"></a><a name="p51836813"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.1.3.1.2 "><p id="p38032294"><a name="p38032294"></a><a name="p38032294"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

