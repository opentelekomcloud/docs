# Assigning an EIP<a name="eip_api_0001"></a>

## Function<a name="en-us_topic_0201534274_section12153337"></a>

This API is used to assign an EIP. 

The EIP service provides independent public IP addresses and bandwidth for Internet access. EIPs can be bound to or unbound from ECSs, BMSs, virtual IP addresses, load balancers, and NAT gateways. 

## URI<a name="en-us_topic_0201534274_section42271171"></a>

POST /v1/\{project\_id\}/publicips

[Table 1](#en-us_topic_0201534274_table57311924)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534274_table57311924"></a>
<table><thead align="left"><tr id="en-us_topic_0201534274_row11854613"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534274_p20699582"><a name="en-us_topic_0201534274_p20699582"></a><a name="en-us_topic_0201534274_p20699582"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534274_p66053444"><a name="en-us_topic_0201534274_p66053444"></a><a name="en-us_topic_0201534274_p66053444"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534274_p48728718"><a name="en-us_topic_0201534274_p48728718"></a><a name="en-us_topic_0201534274_p48728718"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534274_row54712068"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534274_p2492560"><a name="en-us_topic_0201534274_p2492560"></a><a name="en-us_topic_0201534274_p2492560"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534274_p570775"><a name="en-us_topic_0201534274_p570775"></a><a name="en-us_topic_0201534274_p570775"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534274_p10487112"><a name="en-us_topic_0201534274_p10487112"></a><a name="en-us_topic_0201534274_p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534274_section44896221"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="en-us_topic_0201534274_table62031189151043"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534274_row4339910151043"><th class="cellrowborder" valign="top" width="14.280000000000001%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534274_p15988448151043"><a name="en-us_topic_0201534274_p15988448151043"></a><a name="en-us_topic_0201534274_p15988448151043"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.61%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534274_p19995902151043"><a name="en-us_topic_0201534274_p19995902151043"></a><a name="en-us_topic_0201534274_p19995902151043"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.93%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534274_p9055369151043"><a name="en-us_topic_0201534274_p9055369151043"></a><a name="en-us_topic_0201534274_p9055369151043"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.18%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534274_p62396264151043"><a name="en-us_topic_0201534274_p62396264151043"></a><a name="en-us_topic_0201534274_p62396264151043"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534274_row20932612151043"><td class="cellrowborder" valign="top" width="14.280000000000001%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534274_p17819972151043"><a name="en-us_topic_0201534274_p17819972151043"></a><a name="en-us_topic_0201534274_p17819972151043"></a>publicip</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534274_p34131600151043"><a name="en-us_topic_0201534274_p34131600151043"></a><a name="en-us_topic_0201534274_p34131600151043"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.93%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534274_p13196241151043"><a name="en-us_topic_0201534274_p13196241151043"></a><a name="en-us_topic_0201534274_p13196241151043"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534274_p23492844151043"><a name="en-us_topic_0201534274_p23492844151043"></a><a name="en-us_topic_0201534274_p23492844151043"></a>Specifies the EIP objects. For details, see <a href="#en-us_topic_0201534274_table4491214">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534274_row13560713151050"><td class="cellrowborder" valign="top" width="14.280000000000001%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534274_p24675975151050"><a name="en-us_topic_0201534274_p24675975151050"></a><a name="en-us_topic_0201534274_p24675975151050"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534274_p52596998151050"><a name="en-us_topic_0201534274_p52596998151050"></a><a name="en-us_topic_0201534274_p52596998151050"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.93%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534274_p12429959151120"><a name="en-us_topic_0201534274_p12429959151120"></a><a name="en-us_topic_0201534274_p12429959151120"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534274_p1744019151120"><a name="en-us_topic_0201534274_p1744019151120"></a><a name="en-us_topic_0201534274_p1744019151120"></a>Specifies the bandwidth objects. For details, see <a href="#en-us_topic_0201534274_table11041789">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **publicip**  field

    <a name="en-us_topic_0201534274_table4491214"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534274_row21610982"><th class="cellrowborder" valign="top" width="30.830000000000002%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534274_p5659087"><a name="en-us_topic_0201534274_p5659087"></a><a name="en-us_topic_0201534274_p5659087"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534274_p55732864"><a name="en-us_topic_0201534274_p55732864"></a><a name="en-us_topic_0201534274_p55732864"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.05%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534274_p4226242618129"><a name="en-us_topic_0201534274_p4226242618129"></a><a name="en-us_topic_0201534274_p4226242618129"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.830000000000002%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534274_p18068130"><a name="en-us_topic_0201534274_p18068130"></a><a name="en-us_topic_0201534274_p18068130"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534274_row54232412"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534274_p30749271"><a name="en-us_topic_0201534274_p30749271"></a><a name="en-us_topic_0201534274_p30749271"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534274_p7663035"><a name="en-us_topic_0201534274_p7663035"></a><a name="en-us_topic_0201534274_p7663035"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534274_p70444218129"><a name="en-us_topic_0201534274_p70444218129"></a><a name="en-us_topic_0201534274_p70444218129"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0201534274_ul29589093174724"></a><a name="en-us_topic_0201534274_ul29589093174724"></a><ul id="en-us_topic_0201534274_ul29589093174724"><li>Specifies the EIP type.</li><li>The value can be <strong id="en-us_topic_0201534274_b610775542514"><a name="en-us_topic_0201534274_b610775542514"></a><a name="en-us_topic_0201534274_b610775542514"></a>5_bgp</strong> and <strong id="en-us_topic_0201534274_b15441185113256"><a name="en-us_topic_0201534274_b15441185113256"></a><a name="en-us_topic_0201534274_b15441185113256"></a>5_mailbgp</strong>.</li><li>Constraints:<a name="en-us_topic_0201534274_ul9738153015499"></a><a name="en-us_topic_0201534274_ul9738153015499"></a><ul id="en-us_topic_0201534274_ul9738153015499"><li>The configured value must be supported by the system. </li><li><strong id="en-us_topic_0201534274_b1719710451843"><a name="en-us_topic_0201534274_b1719710451843"></a><a name="en-us_topic_0201534274_b1719710451843"></a>publicip_id</strong> is an IPv4 port. If <strong id="en-us_topic_0201534274_b128290317518"><a name="en-us_topic_0201534274_b128290317518"></a><a name="en-us_topic_0201534274_b128290317518"></a>publicip_type</strong> is not specified, the default value is <strong id="en-us_topic_0201534274_b2471543767"><a name="en-us_topic_0201534274_b2471543767"></a><a name="en-us_topic_0201534274_b2471543767"></a>5_bgp</strong>.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534274_row116305209446"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534274_p25480789446"><a name="en-us_topic_0201534274_p25480789446"></a><a name="en-us_topic_0201534274_p25480789446"></a>ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534274_p50677729446"><a name="en-us_topic_0201534274_p50677729446"></a><a name="en-us_topic_0201534274_p50677729446"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534274_p78364279446"><a name="en-us_topic_0201534274_p78364279446"></a><a name="en-us_topic_0201534274_p78364279446"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0201534274_ul3888143018611"></a><a name="en-us_topic_0201534274_ul3888143018611"></a><ul id="en-us_topic_0201534274_ul3888143018611"><li>Specifies the EIP to be assigned. The system automatically assigns an EIP if you do not specify it.</li><li>The value must be a valid IPv4 address in the available IP address range.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **bandwidth**  field

    <a name="en-us_topic_0201534274_table11041789"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534274_row60677888"><th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534274_p15961928"><a name="en-us_topic_0201534274_p15961928"></a><a name="en-us_topic_0201534274_p15961928"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.10828917108289%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534274_p17847776"><a name="en-us_topic_0201534274_p17847776"></a><a name="en-us_topic_0201534274_p17847776"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534274_p3784029918155"><a name="en-us_topic_0201534274_p3784029918155"></a><a name="en-us_topic_0201534274_p3784029918155"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.886911308869113%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534274_p36383728"><a name="en-us_topic_0201534274_p36383728"></a><a name="en-us_topic_0201534274_p36383728"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534274_row61400865"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534274_p7414170"><a name="en-us_topic_0201534274_p7414170"></a><a name="en-us_topic_0201534274_p7414170"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.10828917108289%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534274_p63676932"><a name="en-us_topic_0201534274_p63676932"></a><a name="en-us_topic_0201534274_p63676932"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534274_p4516535118155"><a name="en-us_topic_0201534274_p4516535118155"></a><a name="en-us_topic_0201534274_p4516535118155"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.886911308869113%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0201534274_ul518119181073"></a><a name="en-us_topic_0201534274_ul518119181073"></a><ul id="en-us_topic_0201534274_ul518119181073"><li>Specifies the bandwidth name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li><li>This parameter is mandatory when <strong id="en-us_topic_0201534274_b276165742195527"><a name="en-us_topic_0201534274_b276165742195527"></a><a name="en-us_topic_0201534274_b276165742195527"></a>share_type</strong> is set to <strong id="en-us_topic_0201534274_b1379441107195527"><a name="en-us_topic_0201534274_b1379441107195527"></a><a name="en-us_topic_0201534274_b1379441107195527"></a>PER</strong>. This parameter will be ignored when <strong id="en-us_topic_0201534274_b1701699234195527"><a name="en-us_topic_0201534274_b1701699234195527"></a><a name="en-us_topic_0201534274_b1701699234195527"></a>share_type</strong> is set to <strong id="en-us_topic_0201534274_b1218397550195527"><a name="en-us_topic_0201534274_b1218397550195527"></a><a name="en-us_topic_0201534274_b1218397550195527"></a>WHOLE</strong> with an ID specified.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534274_row15772917"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534274_p2537905"><a name="en-us_topic_0201534274_p2537905"></a><a name="en-us_topic_0201534274_p2537905"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.10828917108289%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534274_p4243749"><a name="en-us_topic_0201534274_p4243749"></a><a name="en-us_topic_0201534274_p4243749"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534274_p3451484018155"><a name="en-us_topic_0201534274_p3451484018155"></a><a name="en-us_topic_0201534274_p3451484018155"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.886911308869113%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0201534274_ul194366475712"></a><a name="en-us_topic_0201534274_ul194366475712"></a><ul id="en-us_topic_0201534274_ul194366475712"><li>Specifies the bandwidth size.</li><li>The value ranges from 1 Mbit/s to 1000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the bandwidth range of each region on the management console.)</li><li>This parameter is mandatory when <strong id="en-us_topic_0201534274_b1269381197"><a name="en-us_topic_0201534274_b1269381197"></a><a name="en-us_topic_0201534274_b1269381197"></a>share_type</strong> is set to <strong id="en-us_topic_0201534274_b1412280890"><a name="en-us_topic_0201534274_b1412280890"></a><a name="en-us_topic_0201534274_b1412280890"></a>PER</strong>. This parameter will be ignored when <strong id="en-us_topic_0201534274_b2109803823"><a name="en-us_topic_0201534274_b2109803823"></a><a name="en-us_topic_0201534274_b2109803823"></a>share_type</strong> is set to <strong id="en-us_topic_0201534274_b152335900"><a name="en-us_topic_0201534274_b152335900"></a><a name="en-us_topic_0201534274_b152335900"></a>WHOLE</strong> with an ID specified.</li><li>The minimum unit for bandwidth adjustment varies depending on the bandwidth range. The details are as follows:<a name="en-us_topic_0201534274_ul9790510185"></a><a name="en-us_topic_0201534274_ul9790510185"></a><ul id="en-us_topic_0201534274_ul9790510185"><li>The minimum unit is 1 Mbit/s if the allowed bandwidth size ranges from 0 to 300 Mbit/s (with 300 Mbit/s included).</li><li>The minimum unit is 50 Mbit/s if the allowed bandwidth size ranges 300 Mbit/s to 1000 Mbit/s (with 1000 Mbit/s included).</li><li>The minimum unit is 500 Mbit/s if the allowed bandwidth size is greater than 1000 Mbit/s.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534274_row33642107"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534274_p40656116"><a name="en-us_topic_0201534274_p40656116"></a><a name="en-us_topic_0201534274_p40656116"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.10828917108289%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534274_p4811061"><a name="en-us_topic_0201534274_p4811061"></a><a name="en-us_topic_0201534274_p4811061"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534274_p2656447218155"><a name="en-us_topic_0201534274_p2656447218155"></a><a name="en-us_topic_0201534274_p2656447218155"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.886911308869113%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0201534274_ul2255712095"></a><a name="en-us_topic_0201534274_ul2255712095"></a><ul id="en-us_topic_0201534274_ul2255712095"><li>Specifies the bandwidth type.</li><li>The value is <strong id="en-us_topic_0201534274_b25288513165924"><a name="en-us_topic_0201534274_b25288513165924"></a><a name="en-us_topic_0201534274_b25288513165924"></a>PER</strong>, indicating that the bandwidth is dedicated.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534274_row17737188172319"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534274_p27426113172319"><a name="en-us_topic_0201534274_p27426113172319"></a><a name="en-us_topic_0201534274_p27426113172319"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.10828917108289%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534274_p55776100172330"><a name="en-us_topic_0201534274_p55776100172330"></a><a name="en-us_topic_0201534274_p55776100172330"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534274_p23864764172319"><a name="en-us_topic_0201534274_p23864764172319"></a><a name="en-us_topic_0201534274_p23864764172319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.886911308869113%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0201534274_ul152417331215"></a><a name="en-us_topic_0201534274_ul152417331215"></a><ul id="en-us_topic_0201534274_ul152417331215"><li>The value is <strong id="en-us_topic_0201534274_b842352706173820"><a name="en-us_topic_0201534274_b842352706173820"></a><a name="en-us_topic_0201534274_b842352706173820"></a>traffic</strong>, indicating that the billing is based on traffic.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request 1 \(IPv4 EIP with dedicated bandwidth\)

    ```
    POST https://{Endpoint}/v1/{project_id}/publicips
    
    {
        "publicip": {
            "type": "5_bgp",
            "ip_version": 4
        },
        "bandwidth": {
            "name": "bandwidth123",
            "size": 10,
            "share_type": "PER"
        }
    }
    ```


## Response Message<a name="en-us_topic_0201534274_section1412808"></a>

-   Response parameter

    **Table  5**  Response parameter

    <a name="en-us_topic_0201534274_table32663367152049"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534274_row49418185152049"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534274_p43450028152049"><a name="en-us_topic_0201534274_p43450028152049"></a><a name="en-us_topic_0201534274_p43450028152049"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534274_p64289235152049"><a name="en-us_topic_0201534274_p64289235152049"></a><a name="en-us_topic_0201534274_p64289235152049"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534274_p40045543152049"><a name="en-us_topic_0201534274_p40045543152049"></a><a name="en-us_topic_0201534274_p40045543152049"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534274_row22463580152049"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534274_p7610714152049"><a name="en-us_topic_0201534274_p7610714152049"></a><a name="en-us_topic_0201534274_p7610714152049"></a>publicip</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534274_p4900878152049"><a name="en-us_topic_0201534274_p4900878152049"></a><a name="en-us_topic_0201534274_p4900878152049"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534274_p15970624152049"><a name="en-us_topic_0201534274_p15970624152049"></a><a name="en-us_topic_0201534274_p15970624152049"></a>Specifies the EIP objects. For details, see <a href="#en-us_topic_0201534274_table44471219">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Description of the  **publicip**  field

    <a name="en-us_topic_0201534274_table44471219"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534274_row33860402"><th class="cellrowborder" valign="top" width="37.96379637963796%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534274_p58338056"><a name="en-us_topic_0201534274_p58338056"></a><a name="en-us_topic_0201534274_p58338056"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.072407240724072%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534274_p4133121218330"><a name="en-us_topic_0201534274_p4133121218330"></a><a name="en-us_topic_0201534274_p4133121218330"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="37.96379637963796%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534274_p34137829"><a name="en-us_topic_0201534274_p34137829"></a><a name="en-us_topic_0201534274_p34137829"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534274_row13700797"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534274_p36022757"><a name="en-us_topic_0201534274_p36022757"></a><a name="en-us_topic_0201534274_p36022757"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534274_p5949386218330"><a name="en-us_topic_0201534274_p5949386218330"></a><a name="en-us_topic_0201534274_p5949386218330"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534274_p25236858"><a name="en-us_topic_0201534274_p25236858"></a><a name="en-us_topic_0201534274_p25236858"></a>Specifies the unique identifier of the EIP.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534274_row25805135"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534274_p9841225"><a name="en-us_topic_0201534274_p9841225"></a><a name="en-us_topic_0201534274_p9841225"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534274_p5427353718330"><a name="en-us_topic_0201534274_p5427353718330"></a><a name="en-us_topic_0201534274_p5427353718330"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534274_ul052132731516"></a><a name="en-us_topic_0201534274_ul052132731516"></a><ul id="en-us_topic_0201534274_ul052132731516"><li>Specifies the EIP status.</li><li>Possible values are as follows:<a name="en-us_topic_0201534274_ul10603143175810"></a><a name="en-us_topic_0201534274_ul10603143175810"></a><ul id="en-us_topic_0201534274_ul10603143175810"><li><strong id="en-us_topic_0201534274_b84235270610153"><a name="en-us_topic_0201534274_b84235270610153"></a><a name="en-us_topic_0201534274_b84235270610153"></a>FREEZED</strong> (Frozen)</li><li><strong id="en-us_topic_0201534274_b842352706181622"><a name="en-us_topic_0201534274_b842352706181622"></a><a name="en-us_topic_0201534274_b842352706181622"></a>BIND_ERROR</strong> (Binding failed)</li><li><strong id="en-us_topic_0201534274_b842352706181646"><a name="en-us_topic_0201534274_b842352706181646"></a><a name="en-us_topic_0201534274_b842352706181646"></a>BINDING</strong> (Binding)</li><li><strong id="en-us_topic_0201534274_b84235270618176"><a name="en-us_topic_0201534274_b84235270618176"></a><a name="en-us_topic_0201534274_b84235270618176"></a>PENDING_DELETE</strong> (Releasing)</li><li><strong id="en-us_topic_0201534274_b842352706181716"><a name="en-us_topic_0201534274_b842352706181716"></a><a name="en-us_topic_0201534274_b842352706181716"></a>PENDING_CREATE</strong> (Assigning)</li><li><strong id="en-us_topic_0201534274_b842352706181818"><a name="en-us_topic_0201534274_b842352706181818"></a><a name="en-us_topic_0201534274_b842352706181818"></a>PENDING_UPDATE</strong> (Updating)</li><li><strong id="en-us_topic_0201534274_b842352706181834"><a name="en-us_topic_0201534274_b842352706181834"></a><a name="en-us_topic_0201534274_b842352706181834"></a>DOWN</strong> (Unbound)</li><li><strong id="en-us_topic_0201534274_b84235270610164"><a name="en-us_topic_0201534274_b84235270610164"></a><a name="en-us_topic_0201534274_b84235270610164"></a>ACTIVE</strong> (Bound)</li><li><strong id="en-us_topic_0201534274_b842352706181859"><a name="en-us_topic_0201534274_b842352706181859"></a><a name="en-us_topic_0201534274_b842352706181859"></a>ELB</strong> (Bound to a load balancer)</li><li><strong id="en-us_topic_0201534274_b842352706103022"><a name="en-us_topic_0201534274_b842352706103022"></a><a name="en-us_topic_0201534274_b842352706103022"></a>ERROR</strong> (Exceptions)</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534274_row66476022"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534274_p1332417268438"><a name="en-us_topic_0201534274_p1332417268438"></a><a name="en-us_topic_0201534274_p1332417268438"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534274_p3408038918330"><a name="en-us_topic_0201534274_p3408038918330"></a><a name="en-us_topic_0201534274_p3408038918330"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534274_ul61069400416"></a><a name="en-us_topic_0201534274_ul61069400416"></a><ul id="en-us_topic_0201534274_ul61069400416"><li>Specifies the EIP type.</li><li>Constraints:<a name="en-us_topic_0201534274_ul1010714409416"></a><a name="en-us_topic_0201534274_ul1010714409416"></a><ul id="en-us_topic_0201534274_ul1010714409416"><li>The configured value must be supported by the system. </li><li><strong id="en-us_topic_0201534274_b1030218389543"><a name="en-us_topic_0201534274_b1030218389543"></a><a name="en-us_topic_0201534274_b1030218389543"></a>publicip_id</strong> is an IPv4 port. If <strong id="en-us_topic_0201534274_b103031389542"><a name="en-us_topic_0201534274_b103031389542"></a><a name="en-us_topic_0201534274_b103031389542"></a>publicip_type</strong> is not specified, the default value is <strong id="en-us_topic_0201534274_b030323835419"><a name="en-us_topic_0201534274_b030323835419"></a><a name="en-us_topic_0201534274_b030323835419"></a>5_bgp</strong>.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534274_row53754023"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534274_p59108624"><a name="en-us_topic_0201534274_p59108624"></a><a name="en-us_topic_0201534274_p59108624"></a>public_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534274_p904808818330"><a name="en-us_topic_0201534274_p904808818330"></a><a name="en-us_topic_0201534274_p904808818330"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534274_p40237373"><a name="en-us_topic_0201534274_p40237373"></a><a name="en-us_topic_0201534274_p40237373"></a>Specifies the obtained EIP if only IPv4 EIPs are available. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534274_row26592044"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534274_p6471942"><a name="en-us_topic_0201534274_p6471942"></a><a name="en-us_topic_0201534274_p6471942"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534274_p6180656518330"><a name="en-us_topic_0201534274_p6180656518330"></a><a name="en-us_topic_0201534274_p6180656518330"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534274_p17634333267"><a name="en-us_topic_0201534274_p17634333267"></a><a name="en-us_topic_0201534274_p17634333267"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534274_row43875021"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534274_p64215808"><a name="en-us_topic_0201534274_p64215808"></a><a name="en-us_topic_0201534274_p64215808"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534274_p4027585818330"><a name="en-us_topic_0201534274_p4027585818330"></a><a name="en-us_topic_0201534274_p4027585818330"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534274_p27139175"><a name="en-us_topic_0201534274_p27139175"></a><a name="en-us_topic_0201534274_p27139175"></a>Specifies the time (UTC time) when the EIP was assigned.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534274_row42925989"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534274_p54453050"><a name="en-us_topic_0201534274_p54453050"></a><a name="en-us_topic_0201534274_p54453050"></a>bandwidth_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534274_p4111904718330"><a name="en-us_topic_0201534274_p4111904718330"></a><a name="en-us_topic_0201534274_p4111904718330"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534274_p11161650"><a name="en-us_topic_0201534274_p11161650"></a><a name="en-us_topic_0201534274_p11161650"></a>Specifies the bandwidth (Mbit/s).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response 1 \(IPv4 EIP with dedicated bandwidth\)

    ```
    {
        "publicip": {
            "id": "f588ccfa-8750-4d7c-bf5d-2ede24414706",
            "status": "PENDING_CREATE",
            "type": "5_bgp",
            "public_ip_address": "161.xx.xx.7",
            "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
            "ip_version": 4,
            "create_time": "2015-07-16 04:10:52",
            "bandwidth_size": 0
            
        }
    }
    ```


## Status Code<a name="en-us_topic_0201534274_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534274_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

