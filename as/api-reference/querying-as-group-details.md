# Querying AS Group Details<a name="EN-US_TOPIC_0043063073"></a>

## Function<a name="section37186555"></a>

This interface is used to query details about a specified AS group by group ID.

## URI<a name="section66243540"></a>

GET /autoscaling-api/v1/\{project\_id\}/scaling\_group/\{scaling\_group\_id\}

**Table  1**  Parameter description

<a name="table46398558"></a>
<table><thead align="left"><tr id="row27278612"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.1"><p id="p62083996"><a name="p62083996"></a><a name="p62083996"></a><strong id="b174791413163714"><a name="b174791413163714"></a><a name="b174791413163714"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p62747764"><a name="p62747764"></a><a name="p62747764"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p49404100"><a name="p49404100"></a><a name="p49404100"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.5.1.4"><p id="p42309173"><a name="p42309173"></a><a name="p42309173"></a><strong id="b96121414103711"><a name="b96121414103711"></a><a name="b96121414103711"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row4490990"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p28225944"><a name="p28225944"></a><a name="p28225944"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p4600155"><a name="p4600155"></a><a name="p4600155"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p37068254"><a name="p37068254"></a><a name="p37068254"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row44993941"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p20630641"><a name="p20630641"></a><a name="p20630641"></a>scaling_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p60469192"><a name="p60469192"></a><a name="p60469192"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p66166404"><a name="p66166404"></a><a name="p66166404"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p57878541"><a name="p57878541"></a><a name="p57878541"></a>Specifies the AS group ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section59320951"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query details about the AS group with ID  **d4e50321-3777-4135-97f8-9f5e9714a4b0**.

    ```
    GET https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group/d4e50321-3777-4135-97f8-9f5e9714a4b0
    ```


## Response Message<a name="section64126518"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table24727624"></a>
    <table><thead align="left"><tr id="row15561779"><th class="cellrowborder" valign="top" width="20.169999999999998%" id="mcps1.2.4.1.1"><p id="p52544597"><a name="p52544597"></a><a name="p52544597"></a><strong id="b587131633710"><a name="b587131633710"></a><a name="b587131633710"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.21%" id="mcps1.2.4.1.2"><p id="p28253988"><a name="p28253988"></a><a name="p28253988"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.620000000000005%" id="mcps1.2.4.1.3"><p id="p6871687"><a name="p6871687"></a><a name="p6871687"></a><strong id="b965714185377"><a name="b965714185377"></a><a name="b965714185377"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19735783"><td class="cellrowborder" valign="top" width="20.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p55094571"><a name="p55094571"></a><a name="p55094571"></a>scaling_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.21%" headers="mcps1.2.4.1.2 "><p id="p33475260"><a name="p33475260"></a><a name="p33475260"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.620000000000005%" headers="mcps1.2.4.1.3 "><p id="p27141505"><a name="p27141505"></a><a name="p27141505"></a>Specifies details about the AS group.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scaling\_groups**  field description

    <a name="table2571689984111"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063030_row3125168495816"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="en-us_topic_0043063030_p4835851595816"><a name="en-us_topic_0043063030_p4835851595816"></a><a name="en-us_topic_0043063030_p4835851595816"></a><strong id="en-us_topic_0043063030_b14507125433416"><a name="en-us_topic_0043063030_b14507125433416"></a><a name="en-us_topic_0043063030_b14507125433416"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="en-us_topic_0043063030_p2472567595816"><a name="en-us_topic_0043063030_p2472567595816"></a><a name="en-us_topic_0043063030_p2472567595816"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0043063030_p5662264395816"><a name="en-us_topic_0043063030_p5662264395816"></a><a name="en-us_topic_0043063030_p5662264395816"></a><strong id="en-us_topic_0043063030_b966010563343"><a name="en-us_topic_0043063030_b966010563343"></a><a name="en-us_topic_0043063030_b966010563343"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063030_row2303134795816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p5359982895816"><a name="en-us_topic_0043063030_p5359982895816"></a><a name="en-us_topic_0043063030_p5359982895816"></a>scaling_group_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p4661881395816"><a name="en-us_topic_0043063030_p4661881395816"></a><a name="en-us_topic_0043063030_p4661881395816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p1802754395816"><a name="en-us_topic_0043063030_p1802754395816"></a><a name="en-us_topic_0043063030_p1802754395816"></a>Specifies the name of the AS group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row2803016695816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p5585097295816"><a name="en-us_topic_0043063030_p5585097295816"></a><a name="en-us_topic_0043063030_p5585097295816"></a>scaling_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p2763485495816"><a name="en-us_topic_0043063030_p2763485495816"></a><a name="en-us_topic_0043063030_p2763485495816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p2383068495816"><a name="en-us_topic_0043063030_p2383068495816"></a><a name="en-us_topic_0043063030_p2383068495816"></a>Specifies the AS group ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row1314957295816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p5848240895816"><a name="en-us_topic_0043063030_p5848240895816"></a><a name="en-us_topic_0043063030_p5848240895816"></a>scaling_group_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p3945463795816"><a name="en-us_topic_0043063030_p3945463795816"></a><a name="en-us_topic_0043063030_p3945463795816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p4170905195816"><a name="en-us_topic_0043063030_p4170905195816"></a><a name="en-us_topic_0043063030_p4170905195816"></a>Specifies the status of the AS group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row3983714095816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p558291395816"><a name="en-us_topic_0043063030_p558291395816"></a><a name="en-us_topic_0043063030_p558291395816"></a>scaling_configuration_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p4956282795816"><a name="en-us_topic_0043063030_p4956282795816"></a><a name="en-us_topic_0043063030_p4956282795816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p5516604195816"><a name="en-us_topic_0043063030_p5516604195816"></a><a name="en-us_topic_0043063030_p5516604195816"></a>Specifies the AS configuration ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row2673232595816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p1783474195816"><a name="en-us_topic_0043063030_p1783474195816"></a><a name="en-us_topic_0043063030_p1783474195816"></a>scaling_configuration_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p3532793495816"><a name="en-us_topic_0043063030_p3532793495816"></a><a name="en-us_topic_0043063030_p3532793495816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p4299037595816"><a name="en-us_topic_0043063030_p4299037595816"></a><a name="en-us_topic_0043063030_p4299037595816"></a>Specifies the AS configuration name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row5136905595816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p14389995816"><a name="en-us_topic_0043063030_p14389995816"></a><a name="en-us_topic_0043063030_p14389995816"></a>current_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p1165588495816"><a name="en-us_topic_0043063030_p1165588495816"></a><a name="en-us_topic_0043063030_p1165588495816"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p460258695816"><a name="en-us_topic_0043063030_p460258695816"></a><a name="en-us_topic_0043063030_p460258695816"></a>Specifies the number of current instances in the AS group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row4142327995816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p6695131595816"><a name="en-us_topic_0043063030_p6695131595816"></a><a name="en-us_topic_0043063030_p6695131595816"></a>desire_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p5434739895816"><a name="en-us_topic_0043063030_p5434739895816"></a><a name="en-us_topic_0043063030_p5434739895816"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p4006315595816"><a name="en-us_topic_0043063030_p4006315595816"></a><a name="en-us_topic_0043063030_p4006315595816"></a>Specifies the expected number of instances in the AS group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row2502407895816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p1368441895816"><a name="en-us_topic_0043063030_p1368441895816"></a><a name="en-us_topic_0043063030_p1368441895816"></a>min_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p3469606795816"><a name="en-us_topic_0043063030_p3469606795816"></a><a name="en-us_topic_0043063030_p3469606795816"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p5891800895816"><a name="en-us_topic_0043063030_p5891800895816"></a><a name="en-us_topic_0043063030_p5891800895816"></a>Specifies the minimum number of instances in the AS group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row6050002595816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p155503295816"><a name="en-us_topic_0043063030_p155503295816"></a><a name="en-us_topic_0043063030_p155503295816"></a>max_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p5884880095816"><a name="en-us_topic_0043063030_p5884880095816"></a><a name="en-us_topic_0043063030_p5884880095816"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p202348095816"><a name="en-us_topic_0043063030_p202348095816"></a><a name="en-us_topic_0043063030_p202348095816"></a>Specifies the maximum number of instances in the AS group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row1821132195816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p6583092595816"><a name="en-us_topic_0043063030_p6583092595816"></a><a name="en-us_topic_0043063030_p6583092595816"></a>cool_down_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p3070470995816"><a name="en-us_topic_0043063030_p3070470995816"></a><a name="en-us_topic_0043063030_p3070470995816"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p405351495816"><a name="en-us_topic_0043063030_p405351495816"></a><a name="en-us_topic_0043063030_p405351495816"></a>Specifies the cooldown period (s).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row3648162895816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p222191995816"><a name="en-us_topic_0043063030_p222191995816"></a><a name="en-us_topic_0043063030_p222191995816"></a>lb_listener_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p4575773095816"><a name="en-us_topic_0043063030_p4575773095816"></a><a name="en-us_topic_0043063030_p4575773095816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p1538862195816"><a name="en-us_topic_0043063030_p1538862195816"></a><a name="en-us_topic_0043063030_p1538862195816"></a>Specifies the ID of a typical ELB listener. ELB listener IDs are separated using a comma (,).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row33800908174636"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p53519047174636"><a name="en-us_topic_0043063030_p53519047174636"></a><a name="en-us_topic_0043063030_p53519047174636"></a>lbaas_listeners</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p1966763821113"><a name="en-us_topic_0043063030_p1966763821113"></a><a name="en-us_topic_0043063030_p1966763821113"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p24895134174636"><a name="en-us_topic_0043063030_p24895134174636"></a><a name="en-us_topic_0043063030_p24895134174636"></a>Specifies enhanced load balancers. For details, see <a href="querying-as-groups.md#table62452402171652">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row30423366112250"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p48373547112250"><a name="en-us_topic_0043063030_p48373547112250"></a><a name="en-us_topic_0043063030_p48373547112250"></a>available_zones</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p25943212112250"><a name="en-us_topic_0043063030_p25943212112250"></a><a name="en-us_topic_0043063030_p25943212112250"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p21025459112250"><a name="en-us_topic_0043063030_p21025459112250"></a><a name="en-us_topic_0043063030_p21025459112250"></a>Specifies the AZ information.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row427986595816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p1112482195816"><a name="en-us_topic_0043063030_p1112482195816"></a><a name="en-us_topic_0043063030_p1112482195816"></a>networks</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p2869527695816"><a name="en-us_topic_0043063030_p2869527695816"></a><a name="en-us_topic_0043063030_p2869527695816"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p4800004895816"><a name="en-us_topic_0043063030_p4800004895816"></a><a name="en-us_topic_0043063030_p4800004895816"></a>Specifies networks. For details, see <a href="querying-as-groups.md#t67e1f67cb70d4457bab7efeb3dfeee6e">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row2934724995816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p2831697495816"><a name="en-us_topic_0043063030_p2831697495816"></a><a name="en-us_topic_0043063030_p2831697495816"></a>security_groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p569719238385"><a name="en-us_topic_0043063030_p569719238385"></a><a name="en-us_topic_0043063030_p569719238385"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p458485895816"><a name="en-us_topic_0043063030_p458485895816"></a><a name="en-us_topic_0043063030_p458485895816"></a>Specifies security groups. For details, see <a href="querying-as-groups.md#t3db1c8f5898a4179b5029204834c82e5">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row4126372995816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p5402772895816"><a name="en-us_topic_0043063030_p5402772895816"></a><a name="en-us_topic_0043063030_p5402772895816"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p1416983695816"><a name="en-us_topic_0043063030_p1416983695816"></a><a name="en-us_topic_0043063030_p1416983695816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p690602895816"><a name="en-us_topic_0043063030_p690602895816"></a><a name="en-us_topic_0043063030_p690602895816"></a>Specifies the time when an AS group was created. The time format complies with UTC.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row6215425395816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p132972795816"><a name="en-us_topic_0043063030_p132972795816"></a><a name="en-us_topic_0043063030_p132972795816"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p4059904995816"><a name="en-us_topic_0043063030_p4059904995816"></a><a name="en-us_topic_0043063030_p4059904995816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p18869295816"><a name="en-us_topic_0043063030_p18869295816"></a><a name="en-us_topic_0043063030_p18869295816"></a>Specifies the ID of the VPC to which the AS group belongs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row169823395816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p333920895816"><a name="en-us_topic_0043063030_p333920895816"></a><a name="en-us_topic_0043063030_p333920895816"></a>detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p204042795816"><a name="en-us_topic_0043063030_p204042795816"></a><a name="en-us_topic_0043063030_p204042795816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p3105690795816"><a name="en-us_topic_0043063030_p3105690795816"></a><a name="en-us_topic_0043063030_p3105690795816"></a>Specifies details about the AS group. If a scaling action fails, this parameter is used to record errors.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row1107670995816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p2479821895816"><a name="en-us_topic_0043063030_p2479821895816"></a><a name="en-us_topic_0043063030_p2479821895816"></a>is_scaling</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p6249865695816"><a name="en-us_topic_0043063030_p6249865695816"></a><a name="en-us_topic_0043063030_p6249865695816"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p2922638295816"><a name="en-us_topic_0043063030_p2922638295816"></a><a name="en-us_topic_0043063030_p2922638295816"></a>Specifies the scaling flag of the AS group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row6171085495816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p3252330995816"><a name="en-us_topic_0043063030_p3252330995816"></a><a name="en-us_topic_0043063030_p3252330995816"></a>health_periodic_audit_method</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p1714233595816"><a name="en-us_topic_0043063030_p1714233595816"></a><a name="en-us_topic_0043063030_p1714233595816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p4635191095816"><a name="en-us_topic_0043063030_p4635191095816"></a><a name="en-us_topic_0043063030_p4635191095816"></a>Specifies the health check method.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row1451401395816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p3478441495816"><a name="en-us_topic_0043063030_p3478441495816"></a><a name="en-us_topic_0043063030_p3478441495816"></a>health_periodic_audit_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p6607415195816"><a name="en-us_topic_0043063030_p6607415195816"></a><a name="en-us_topic_0043063030_p6607415195816"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p5040604995816"><a name="en-us_topic_0043063030_p5040604995816"></a><a name="en-us_topic_0043063030_p5040604995816"></a>Specifies the health check interval.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row42331571153426"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p6305198153426"><a name="en-us_topic_0043063030_p6305198153426"></a><a name="en-us_topic_0043063030_p6305198153426"></a>health_periodic_audit_grace_period</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p40959034153426"><a name="en-us_topic_0043063030_p40959034153426"></a><a name="en-us_topic_0043063030_p40959034153426"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p29347454153426"><a name="en-us_topic_0043063030_p29347454153426"></a><a name="en-us_topic_0043063030_p29347454153426"></a>Specifies the grace period for health check.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row5100126495816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p3746171895816"><a name="en-us_topic_0043063030_p3746171895816"></a><a name="en-us_topic_0043063030_p3746171895816"></a>instance_terminate_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p1450028895816"><a name="en-us_topic_0043063030_p1450028895816"></a><a name="en-us_topic_0043063030_p1450028895816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p3367266295816"><a name="en-us_topic_0043063030_p3367266295816"></a><a name="en-us_topic_0043063030_p3367266295816"></a>Specifies the instance removal policy.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row3461851095816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p5263592295816"><a name="en-us_topic_0043063030_p5263592295816"></a><a name="en-us_topic_0043063030_p5263592295816"></a>notifications</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p3565131995816"><a name="en-us_topic_0043063030_p3565131995816"></a><a name="en-us_topic_0043063030_p3565131995816"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p207574995816"><a name="en-us_topic_0043063030_p207574995816"></a><a name="en-us_topic_0043063030_p207574995816"></a>Specifies the notification mode.</p>
    <p id="en-us_topic_0043063030_p1868174295816"><a name="en-us_topic_0043063030_p1868174295816"></a><a name="en-us_topic_0043063030_p1868174295816"></a><strong id="en-us_topic_0043063030_b58832166171917"><a name="en-us_topic_0043063030_b58832166171917"></a><a name="en-us_topic_0043063030_b58832166171917"></a>EMAIL</strong> refers to notification by email.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row58376155111614"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p30848135111614"><a name="en-us_topic_0043063030_p30848135111614"></a><a name="en-us_topic_0043063030_p30848135111614"></a>delete_publicip</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p40568935111649"><a name="en-us_topic_0043063030_p40568935111649"></a><a name="en-us_topic_0043063030_p40568935111649"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p64858299111649"><a name="en-us_topic_0043063030_p64858299111649"></a><a name="en-us_topic_0043063030_p64858299111649"></a>Specifies whether to delete the EIP bound to the ECS when deleting the ECS.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row1666213536250"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p1585114581258"><a name="en-us_topic_0043063030_p1585114581258"></a><a name="en-us_topic_0043063030_p1585114581258"></a>delete_volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p19851458122520"><a name="en-us_topic_0043063030_p19851458122520"></a><a name="en-us_topic_0043063030_p19851458122520"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p178519586250"><a name="en-us_topic_0043063030_p178519586250"></a><a name="en-us_topic_0043063030_p178519586250"></a>Specifies whether to delete the data disks attached to the ECS when deleting the ECS.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row50398037163752"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p55709224163752"><a name="en-us_topic_0043063030_p55709224163752"></a><a name="en-us_topic_0043063030_p55709224163752"></a>cloud_location_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p16153275163752"><a name="en-us_topic_0043063030_p16153275163752"></a><a name="en-us_topic_0043063030_p16153275163752"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p33346870163752"><a name="en-us_topic_0043063030_p33346870163752"></a><a name="en-us_topic_0043063030_p33346870163752"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row529918693932"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p2658093993932"><a name="en-us_topic_0043063030_p2658093993932"></a><a name="en-us_topic_0043063030_p2658093993932"></a>enterprise_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p557242093932"><a name="en-us_topic_0043063030_p557242093932"></a><a name="en-us_topic_0043063030_p557242093932"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p4871283793932"><a name="en-us_topic_0043063030_p4871283793932"></a><a name="en-us_topic_0043063030_p4871283793932"></a>Specifies the enterprise project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row870025345713"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p67015533576"><a name="en-us_topic_0043063030_p67015533576"></a><a name="en-us_topic_0043063030_p67015533576"></a>activity_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p14701185316570"><a name="en-us_topic_0043063030_p14701185316570"></a><a name="en-us_topic_0043063030_p14701185316570"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p16701185365719"><a name="en-us_topic_0043063030_p16701185365719"></a><a name="en-us_topic_0043063030_p16701185365719"></a>Specifies the type of the AS action.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row9571105073212"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p1766414574320"><a name="en-us_topic_0043063030_p1766414574320"></a><a name="en-us_topic_0043063030_p1766414574320"></a>multi_az_priority_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p176649575326"><a name="en-us_topic_0043063030_p176649575326"></a><a name="en-us_topic_0043063030_p176649575326"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p1766565743214"><a name="en-us_topic_0043063030_p1766565743214"></a><a name="en-us_topic_0043063030_p1766565743214"></a>Specifies the priority policy used to select target AZs when adjusting the number of instances in an AS group.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **lbaas\_listeners**  field description

    <a name="table62452402171652"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063030_row45038761171652"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="en-us_topic_0043063030_p24261034171652"><a name="en-us_topic_0043063030_p24261034171652"></a><a name="en-us_topic_0043063030_p24261034171652"></a><strong id="en-us_topic_0043063030_b1882212592346"><a name="en-us_topic_0043063030_b1882212592346"></a><a name="en-us_topic_0043063030_b1882212592346"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="en-us_topic_0043063030_p61530925171652"><a name="en-us_topic_0043063030_p61530925171652"></a><a name="en-us_topic_0043063030_p61530925171652"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="en-us_topic_0043063030_p17949056171652"><a name="en-us_topic_0043063030_p17949056171652"></a><a name="en-us_topic_0043063030_p17949056171652"></a><strong id="en-us_topic_0043063030_b1486304193518"><a name="en-us_topic_0043063030_b1486304193518"></a><a name="en-us_topic_0043063030_b1486304193518"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063030_row44587411171652"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p54810510171652"><a name="en-us_topic_0043063030_p54810510171652"></a><a name="en-us_topic_0043063030_p54810510171652"></a>listener_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p42466398171652"><a name="en-us_topic_0043063030_p42466398171652"></a><a name="en-us_topic_0043063030_p42466398171652"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p17226243171652"><a name="en-us_topic_0043063030_p17226243171652"></a><a name="en-us_topic_0043063030_p17226243171652"></a>Specifies the listener ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row16035310115445"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p239701115447"><a name="en-us_topic_0043063030_p239701115447"></a><a name="en-us_topic_0043063030_p239701115447"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p19415824115447"><a name="en-us_topic_0043063030_p19415824115447"></a><a name="en-us_topic_0043063030_p19415824115447"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p14598635115447"><a name="en-us_topic_0043063030_p14598635115447"></a><a name="en-us_topic_0043063030_p14598635115447"></a>Specifies the backend ECS group ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row61114407171742"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p51319960171742"><a name="en-us_topic_0043063030_p51319960171742"></a><a name="en-us_topic_0043063030_p51319960171742"></a>protocol_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p25093240171742"><a name="en-us_topic_0043063030_p25093240171742"></a><a name="en-us_topic_0043063030_p25093240171742"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p19286583171742"><a name="en-us_topic_0043063030_p19286583171742"></a><a name="en-us_topic_0043063030_p19286583171742"></a>Specifies the backend protocol ID, which is the port on which a backend ECS listens for traffic.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row36552334171745"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p7949116171745"><a name="en-us_topic_0043063030_p7949116171745"></a><a name="en-us_topic_0043063030_p7949116171745"></a>weight</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p10566861171745"><a name="en-us_topic_0043063030_p10566861171745"></a><a name="en-us_topic_0043063030_p10566861171745"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p50609408171745"><a name="en-us_topic_0043063030_p50609408171745"></a><a name="en-us_topic_0043063030_p50609408171745"></a>Specifies the weight, which determines the portion of requests a backend ECS processes when being compared to other backend ECSs added to the same listener.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **networks**  field description

    <a name="table125932828469"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063030_r38fbfd545d8b41ac9a165cb5b185293c"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="en-us_topic_0043063030_a25948832a6e540e4aeaf9201f17c6136"><a name="en-us_topic_0043063030_a25948832a6e540e4aeaf9201f17c6136"></a><a name="en-us_topic_0043063030_a25948832a6e540e4aeaf9201f17c6136"></a><strong id="en-us_topic_0043063030_b16850768358"><a name="en-us_topic_0043063030_b16850768358"></a><a name="en-us_topic_0043063030_b16850768358"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="en-us_topic_0043063030_a5fa8352938e048e29a2a0ae3465f8beb"><a name="en-us_topic_0043063030_a5fa8352938e048e29a2a0ae3465f8beb"></a><a name="en-us_topic_0043063030_a5fa8352938e048e29a2a0ae3465f8beb"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="en-us_topic_0043063030_abe4729b8fced431487d765209a10d998"><a name="en-us_topic_0043063030_abe4729b8fced431487d765209a10d998"></a><a name="en-us_topic_0043063030_abe4729b8fced431487d765209a10d998"></a><strong id="en-us_topic_0043063030_b699417913511"><a name="en-us_topic_0043063030_b699417913511"></a><a name="en-us_topic_0043063030_b699417913511"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063030_rc7ffdcdeb84a45feb1ea195ba834fbfd"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_a7d60ed8df47c4992a324abe8c0284e98"><a name="en-us_topic_0043063030_a7d60ed8df47c4992a324abe8c0284e98"></a><a name="en-us_topic_0043063030_a7d60ed8df47c4992a324abe8c0284e98"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_a0c27097a7a204f7f8b84faf6c4ace52c"><a name="en-us_topic_0043063030_a0c27097a7a204f7f8b84faf6c4ace52c"></a><a name="en-us_topic_0043063030_a0c27097a7a204f7f8b84faf6c4ace52c"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_a449a6776950944bda68da138e6abe695"><a name="en-us_topic_0043063030_a449a6776950944bda68da138e6abe695"></a><a name="en-us_topic_0043063030_a449a6776950944bda68da138e6abe695"></a>Specifies the network ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row225972616103"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p168461419171814"><a name="en-us_topic_0043063030_p168461419171814"></a><a name="en-us_topic_0043063030_p168461419171814"></a>ipv6_enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p128463194182"><a name="en-us_topic_0043063030_p128463194182"></a><a name="en-us_topic_0043063030_p128463194182"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p1869495520194"><a name="en-us_topic_0043063030_p1869495520194"></a><a name="en-us_topic_0043063030_p1869495520194"></a>Specifies whether to support IPv6 addresses. If the value of this parameter is set to <strong id="en-us_topic_0043063030_b28331146153114"><a name="en-us_topic_0043063030_b28331146153114"></a><a name="en-us_topic_0043063030_b28331146153114"></a>true</strong>, the NIC supports IPv6 addresses. The default value is <strong id="en-us_topic_0043063030_b8423527060277"><a name="en-us_topic_0043063030_b8423527060277"></a><a name="en-us_topic_0043063030_b8423527060277"></a>false</strong>. This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063030_row10392255147"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p205431522101813"><a name="en-us_topic_0043063030_p205431522101813"></a><a name="en-us_topic_0043063030_p205431522101813"></a>ipv6_bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p571213113810"><a name="en-us_topic_0043063030_p571213113810"></a><a name="en-us_topic_0043063030_p571213113810"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p18543162219184"><a name="en-us_topic_0043063030_p18543162219184"></a><a name="en-us_topic_0043063030_p18543162219184"></a>Specifies the shared bandwidth of an IPv6 address. This parameter is left blank by default, indicating that no IPv6 shared bandwidth is bound. This parameter is reserved.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **ipv6\_bandwidth**  field description

    <a name="table12158109202914"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063030_row1853319428379"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0043063030_p18442811162111"><a name="en-us_topic_0043063030_p18442811162111"></a><a name="en-us_topic_0043063030_p18442811162111"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="en-us_topic_0043063030_p651421810389"><a name="en-us_topic_0043063030_p651421810389"></a><a name="en-us_topic_0043063030_p651421810389"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="en-us_topic_0043063030_p444917113212"><a name="en-us_topic_0043063030_p444917113212"></a><a name="en-us_topic_0043063030_p444917113212"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063030_row1853324213378"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063030_p109011143210"><a name="en-us_topic_0043063030_p109011143210"></a><a name="en-us_topic_0043063030_p109011143210"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063030_p59010416217"><a name="en-us_topic_0043063030_p59010416217"></a><a name="en-us_topic_0043063030_p59010416217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063030_p18389161592217"><a name="en-us_topic_0043063030_p18389161592217"></a><a name="en-us_topic_0043063030_p18389161592217"></a>Specifies the ID of the shared bandwidth of an IPv6 address. This parameter is reserved.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "scaling_group": {
          "networks": [
                    {
                        "id": " a8327883-6b07-4497-9c61-68d03ee193a ",
                        "ipv6_enable": false,
                        "ipv6_bandwidth":  null,
                    }
            ],
            "available_zones": [
                   "XXXa",
                   "XXXb"
            ],
            "detail": null,
            "scaling_group_name": "api_gateway_modify",
            "scaling_group_id": "d4e50321-3777-4135-97f8-9f5e9714a4b0",
            "scaling_group_status": "INSERVICE",
            "scaling_configuration_id": "53579851-3841-418d-a97b-9cecdb663a90",
            "scaling_configuration_name": "press",
            "current_instance_number": 7,
            "desire_instance_number": 8,
            "min_instance_number": 0,
            "max_instance_number": 100,
            "cool_down_time": 900,
            "lb_listener_id": null,
            "security_groups": [
                {
                    "id": "23b7b999-0a30-4b48-ae8f-ee201a88a6ab"
                }
            ],
            "create_time": "2015-09-01T08:36:10Z",
            "vpc_id": "3e22f934-800d-4bb4-a588-0b9a76108190",
            "health_periodic_audit_method": "NOVA_AUDIT",
            "health_periodic_audit_time": 5,
            "health_periodic_audit_grace_period": 600,
            "instance_terminate_policy": "OLD_CONFIG_OLD_INSTANCE",
            "is_scaling": true,
            "delete_publicip": false,
            "notifications": null,
            "enterprise_project_id": "c92b1a5d-6f20-43f2-b1b7-7ce35e58e413",
            "activity_type": "MODIFY_ELB",
            "multi_az_priority_policy": "PICK_FIRST"
        }
    }
    ```


## Returned Values<a name="section40267752"></a>

-   Normal

    200

-   Abnormal

    <a name="table56572634"></a>
    <table><thead align="left"><tr id="row12476353"><th class="cellrowborder" valign="top" width="43.8%" id="mcps1.1.3.1.1"><p id="p3951668"><a name="p3951668"></a><a name="p3951668"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.2%" id="mcps1.1.3.1.2"><p id="p51649700"><a name="p51649700"></a><a name="p51649700"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row22876152"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p41029017"><a name="p41029017"></a><a name="p41029017"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p35016046"><a name="p35016046"></a><a name="p35016046"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row46708959"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p25329374"><a name="p25329374"></a><a name="p25329374"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p38413446"><a name="p38413446"></a><a name="p38413446"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row10176696"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p19006063"><a name="p19006063"></a><a name="p19006063"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p63096163"><a name="p63096163"></a><a name="p63096163"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row30994559"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p27531352"><a name="p27531352"></a><a name="p27531352"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p15447074"><a name="p15447074"></a><a name="p15447074"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row4805945"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p53737263"><a name="p53737263"></a><a name="p53737263"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p57751017"><a name="p57751017"></a><a name="p57751017"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row49997107"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p23233871"><a name="p23233871"></a><a name="p23233871"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p2895395"><a name="p2895395"></a><a name="p2895395"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row26058562"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p30368798"><a name="p30368798"></a><a name="p30368798"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p43953607"><a name="p43953607"></a><a name="p43953607"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row60038148"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p31251786"><a name="p31251786"></a><a name="p31251786"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p48366737"><a name="p48366737"></a><a name="p48366737"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row32647452"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p27197959"><a name="p27197959"></a><a name="p27197959"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p55551046"><a name="p55551046"></a><a name="p55551046"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row30197369"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p30067794"><a name="p30067794"></a><a name="p30067794"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p19572211"><a name="p19572211"></a><a name="p19572211"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row41932174"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p41062959"><a name="p41062959"></a><a name="p41062959"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p37765421"><a name="p37765421"></a><a name="p37765421"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row4344474"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p16358126"><a name="p16358126"></a><a name="p16358126"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p49939793"><a name="p49939793"></a><a name="p49939793"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row46804961"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p33105505"><a name="p33105505"></a><a name="p33105505"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p64300229"><a name="p64300229"></a><a name="p64300229"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row41831152"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p32880166"><a name="p32880166"></a><a name="p32880166"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p46047796"><a name="p46047796"></a><a name="p46047796"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

