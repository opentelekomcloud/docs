# Creating a Security Group Rule<a name="vpc_sg01_0005"></a>

## Function<a name="section4195542395259"></a>

This API is used to create a security group rule.

## URI<a name="section5844660495259"></a>

POST /v1/\{project\_id\}/security-group-rules

## Request Message<a name="section3936161695259"></a>

-   Request parameter

    **Table  1**  Request parameter

    <a name="table64406641102826"></a>
    <table><thead align="left"><tr id="row57921141102826"><th class="cellrowborder" valign="top" width="25.729999999999997%" id="mcps1.2.5.1.1"><p id="p61100872102826"><a name="p61100872102826"></a><a name="p61100872102826"></a><strong id="b842352706195711_1"><a name="b842352706195711_1"></a><a name="b842352706195711_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.979999999999999%" id="mcps1.2.5.1.2"><p id="p50223579102826"><a name="p50223579102826"></a><a name="p50223579102826"></a><strong id="b842352706145619_1"><a name="b842352706145619_1"></a><a name="b842352706145619_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.3%" id="mcps1.2.5.1.3"><p id="p12571728103332"><a name="p12571728103332"></a><a name="p12571728103332"></a><strong id="b842352706145623_1"><a name="b842352706145623_1"></a><a name="b842352706145623_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.99%" id="mcps1.2.5.1.4"><p id="p41578070102826"><a name="p41578070102826"></a><a name="p41578070102826"></a><strong id="b372029376201138_1"><a name="b372029376201138_1"></a><a name="b372029376201138_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12380514102826"><td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.5.1.1 "><p id="p63297574102826"><a name="p63297574102826"></a><a name="p63297574102826"></a>security_group_rule</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.2 "><p id="p26829899102826"><a name="p26829899102826"></a><a name="p26829899102826"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.3 "><p id="p11677013103332"><a name="p11677013103332"></a><a name="p11677013103332"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.99%" headers="mcps1.2.5.1.4 "><p id="p25738233102826"><a name="p25738233102826"></a><a name="p25738233102826"></a>Specifies the security group rule objects. For details, see <a href="#table40497645103533">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Description of the  **security\_group\_rule**  field

    <a name="table40497645103533"></a>
    <table><thead align="left"><tr id="row53169346103533"><th class="cellrowborder" valign="top" width="25.729999999999997%" id="mcps1.2.5.1.1"><p id="p11749806103533"><a name="p11749806103533"></a><a name="p11749806103533"></a><strong id="b842352706195711_3"><a name="b842352706195711_3"></a><a name="b842352706195711_3"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.979999999999999%" id="mcps1.2.5.1.2"><p id="p12210197103533"><a name="p12210197103533"></a><a name="p12210197103533"></a><strong id="b842352706145619_3"><a name="b842352706145619_3"></a><a name="b842352706145619_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.3%" id="mcps1.2.5.1.3"><p id="p49501921103533"><a name="p49501921103533"></a><a name="p49501921103533"></a><strong id="b842352706145623_3"><a name="b842352706145623_3"></a><a name="b842352706145623_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.99%" id="mcps1.2.5.1.4"><p id="p50232698103533"><a name="p50232698103533"></a><a name="p50232698103533"></a><strong id="b372029376201138_3"><a name="b372029376201138_3"></a><a name="b372029376201138_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42316743103533"><td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.5.1.1 "><p id="p5104177103533"><a name="p5104177103533"></a><a name="p5104177103533"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.2 "><p id="p10785183103533"><a name="p10785183103533"></a><a name="p10785183103533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.3 "><p id="p1184634103533"><a name="p1184634103533"></a><a name="p1184634103533"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.99%" headers="mcps1.2.5.1.4 "><p id="p28846505103533"><a name="p28846505103533"></a><a name="p28846505103533"></a>Specifies the security group ID.</p>
    </td>
    </tr>
    <tr id="row837164644616"><td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.5.1.1 "><p id="p432391116381"><a name="p432391116381"></a><a name="p432391116381"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.2 "><p id="p20328111163813"><a name="p20328111163813"></a><a name="p20328111163813"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.3 "><p id="p193371011103810"><a name="p193371011103810"></a><a name="p193371011103810"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.99%" headers="mcps1.2.5.1.4 "><a name="ul1225611189157"></a><a name="ul1225611189157"></a><ul id="ul1225611189157"><li>Provides supplementary information about the security group rule.</li><li>The value is a string of no more than 255 characters that can contain letters and digits.</li></ul>
    </td>
    </tr>
    <tr id="row21341412103542"><td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.5.1.1 "><p id="p57854982103542"><a name="p57854982103542"></a><a name="p57854982103542"></a>direction</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.2 "><p id="p55741936103542"><a name="p55741936103542"></a><a name="p55741936103542"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.3 "><p id="p18802950103542"><a name="p18802950103542"></a><a name="p18802950103542"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.99%" headers="mcps1.2.5.1.4 "><a name="ul1268116179462"></a><a name="ul1268116179462"></a><ul id="ul1268116179462"><li>Possible values are as follows:<a name="ul6968104419355"></a><a name="ul6968104419355"></a><ul id="ul6968104419355"><li><strong id="b15904714116"><a name="b15904714116"></a><a name="b15904714116"></a>egress</strong></li><li><strong id="b195461181119"><a name="b195461181119"></a><a name="b195461181119"></a>ingress</strong></li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row4645343310375"><td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.5.1.1 "><p id="p1542771910375"><a name="p1542771910375"></a><a name="p1542771910375"></a>ethertype</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.2 "><p id="p4168576010375"><a name="p4168576010375"></a><a name="p4168576010375"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.3 "><p id="p2110340510375"><a name="p2110340510375"></a><a name="p2110340510375"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.99%" headers="mcps1.2.5.1.4 "><a name="ul117531010191518"></a><a name="ul117531010191518"></a><ul id="ul117531010191518"><li>Specifies the IP protocol version.</li><li>The value can be <strong>IPv4</strong> or <strong>IPv6</strong>.</li><li>If you do not set this parameter, <strong id="b842352706111846"><a name="b842352706111846"></a><a name="b842352706111846"></a>IPv4</strong> is used by default.</li></ul>
    </td>
    </tr>
    <tr id="row978280010378"><td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.5.1.1 "><p id="p2093634110378"><a name="p2093634110378"></a><a name="p2093634110378"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.2 "><p id="p1812206110378"><a name="p1812206110378"></a><a name="p1812206110378"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.3 "><p id="p5860085010378"><a name="p5860085010378"></a><a name="p5860085010378"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.99%" headers="mcps1.2.5.1.4 "><a name="ul8194236156"></a><a name="ul8194236156"></a><ul id="ul8194236156"><li>Specifies the protocol type.</li><li>The value can be <strong id="b191601956161314"><a name="b191601956161314"></a><a name="b191601956161314"></a>tcp</strong>, <strong id="b3825301144"><a name="b3825301144"></a><a name="b3825301144"></a>udp</strong>, <strong id="b193416516143"><a name="b193416516143"></a><a name="b193416516143"></a>icmp</strong> or an IP protocol number</li><li>If the parameter is left blank, all protocols are supported. </li></ul>
    </td>
    </tr>
    <tr id="row18668800103711"><td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.5.1.1 "><p id="p33801475103711"><a name="p33801475103711"></a><a name="p33801475103711"></a>port_range_min</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.2 "><p id="p53564969103711"><a name="p53564969103711"></a><a name="p53564969103711"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.3 "><p id="p43795239103711"><a name="p43795239103711"></a><a name="p43795239103711"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.99%" headers="mcps1.2.5.1.4 "><a name="ul8924125811144"></a><a name="ul8924125811144"></a><ul id="ul8924125811144"><li>Specifies the start port number.</li><li>The value ranges from 1 to 65535.</li><li>The value cannot be greater than the <strong id="b842352706195750_1"><a name="b842352706195750_1"></a><a name="b842352706195750_1"></a>port_range_max</strong> value. An empty value indicates all ports. If the protocol is <strong id="b842352706195910_1"><a name="b842352706195910_1"></a><a name="b842352706195910_1"></a>icmp</strong>, the value range is shown in <a href="icmp-port-range-relationship-table.md">ICMP-Port Range Relationship Table</a>.</li></ul>
    </td>
    </tr>
    <tr id="row13883795103937"><td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.5.1.1 "><p id="p57845296103937"><a name="p57845296103937"></a><a name="p57845296103937"></a>port_range_max</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.2 "><p id="p54957377103937"><a name="p54957377103937"></a><a name="p54957377103937"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.3 "><p id="p22362584103937"><a name="p22362584103937"></a><a name="p22362584103937"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.99%" headers="mcps1.2.5.1.4 "><a name="ul39421154151419"></a><a name="ul39421154151419"></a><ul id="ul39421154151419"><li>Specifies the end port number.</li><li>The value ranges from 1 to 65535.</li><li>If the protocol is not <strong id="b842352706195730"><a name="b842352706195730"></a><a name="b842352706195730"></a>icmp</strong>, the value cannot be smaller than the <strong id="b842352706195750_3"><a name="b842352706195750_3"></a><a name="b842352706195750_3"></a>port_range_min</strong> value. An empty value indicates all ports. If the protocol is <strong id="b842352706195910_3"><a name="b842352706195910_3"></a><a name="b842352706195910_3"></a>icmp</strong>, the value range is shown in <a href="icmp-port-range-relationship-table.md">ICMP-Port Range Relationship Table</a>.</li></ul>
    </td>
    </tr>
    <tr id="row6541391310401"><td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.5.1.1 "><p id="p5185430910401"><a name="p5185430910401"></a><a name="p5185430910401"></a>remote_ip_prefix</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.2 "><p id="p3944952510401"><a name="p3944952510401"></a><a name="p3944952510401"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.3 "><p id="p4129497410401"><a name="p4129497410401"></a><a name="p4129497410401"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.99%" headers="mcps1.2.5.1.4 "><a name="ul14397351121414"></a><a name="ul14397351121414"></a><ul id="ul14397351121414"><li>Specifies the remote IP address. If the access control direction is set to <strong>egress</strong>, the parameter specifies the source IP address. If the access control direction is set to <strong>ingress</strong>, the parameter specifies the destination IP address.</li><li>The value can be in the CIDR format or IP addresses.</li><li>The parameter is exclusive with parameter <strong>remote_group_id</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row58771576104026"><td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.5.1.1 "><p id="p59182141104026"><a name="p59182141104026"></a><a name="p59182141104026"></a>remote_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.2 "><p id="p29024106104026"><a name="p29024106104026"></a><a name="p29024106104026"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.3 "><p id="p2142367104026"><a name="p2142367104026"></a><a name="p2142367104026"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.99%" headers="mcps1.2.5.1.4 "><a name="ul3180184851416"></a><a name="ul3180184851416"></a><ul id="ul3180184851416"><li>Specifies the ID of the peer security group.</li><li>The value is exclusive with parameter <strong>remote_ip_prefix</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{Endpoint}/v1/{project_id}/security-group-rules
    
    {
        "security_group_rule": {
            "direction": "ingress", 
            "port_range_min": "80", 
            "ethertype": "IPv4", 
            "port_range_max": "80", 
            "protocol": "tcp", 
            "remote_group_id": "85cc3048-abc3-43cc-89b3-377341426ac5", 
            "security_group_id": "a7734e61-b545-452d-a3cd-0189cbd9747a"
        }
    }
    ```


## Response Message<a name="section3532656695259"></a>

-   Response parameter

    **Table  3**  Response parameter

    <a name="table187664789489"></a>
    <table><thead align="left"><tr id="row101573199489"><th class="cellrowborder" valign="top" width="23.09%" id="mcps1.2.4.1.1"><p id="p444890459489"><a name="p444890459489"></a><a name="p444890459489"></a><strong id="b842352706195711_5"><a name="b842352706195711_5"></a><a name="b842352706195711_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.14%" id="mcps1.2.4.1.2"><p id="p437522139489"><a name="p437522139489"></a><a name="p437522139489"></a><strong id="b842352706145623_5"><a name="b842352706145623_5"></a><a name="b842352706145623_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.769999999999996%" id="mcps1.2.4.1.3"><p id="p578362329489"><a name="p578362329489"></a><a name="p578362329489"></a><strong id="b372029376201138_5"><a name="b372029376201138_5"></a><a name="b372029376201138_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row449165309489"><td class="cellrowborder" valign="top" width="23.09%" headers="mcps1.2.4.1.1 "><p id="p268266119489"><a name="p268266119489"></a><a name="p268266119489"></a>security_group_rule</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.14%" headers="mcps1.2.4.1.2 "><p id="p630794179489"><a name="p630794179489"></a><a name="p630794179489"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.2.4.1.3 "><p id="p349251459489"><a name="p349251459489"></a><a name="p349251459489"></a>Specifies the security group rule objects. For details, see <a href="#table488727239520">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **security\_group\_rule**  objects

    <a name="table488727239520"></a>
    <table><thead align="left"><tr id="vpc_sg01_0001_row611024789489"><th class="cellrowborder" valign="top" width="34.143414341434145%" id="mcps1.2.4.1.1"><p id="vpc_sg01_0001_p98931099489"><a name="vpc_sg01_0001_p98931099489"></a><a name="vpc_sg01_0001_p98931099489"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.732073207320735%" id="mcps1.2.4.1.2"><p id="vpc_sg01_0001_p368367439489"><a name="vpc_sg01_0001_p368367439489"></a><a name="vpc_sg01_0001_p368367439489"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.124512451245124%" id="mcps1.2.4.1.3"><p id="vpc_sg01_0001_p23523719489"><a name="vpc_sg01_0001_p23523719489"></a><a name="vpc_sg01_0001_p23523719489"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpc_sg01_0001_row397690789489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p656951529489"><a name="vpc_sg01_0001_p656951529489"></a><a name="vpc_sg01_0001_p656951529489"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p307102169489"><a name="vpc_sg01_0001_p307102169489"></a><a name="vpc_sg01_0001_p307102169489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><p id="vpc_sg01_0001_p216633359489"><a name="vpc_sg01_0001_p216633359489"></a><a name="vpc_sg01_0001_p216633359489"></a>Specifies the security group rule ID, which uniquely identifies the security group rule.</p>
    </td>
    </tr>
    <tr id="vpc_sg01_0001_row2447898388"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p432391116381"><a name="vpc_sg01_0001_p432391116381"></a><a name="vpc_sg01_0001_p432391116381"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p20328111163813"><a name="vpc_sg01_0001_p20328111163813"></a><a name="vpc_sg01_0001_p20328111163813"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="vpc_sg01_0001_ul12329121935111"></a><a name="vpc_sg01_0001_ul12329121935111"></a><ul id="vpc_sg01_0001_ul12329121935111"><li>Provides supplementary information about the security group rule.</li><li>The value is a string of no more than 255 characters that can contain letters and digits.</li></ul>
    </td>
    </tr>
    <tr id="vpc_sg01_0001_row320377939489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p620577269489"><a name="vpc_sg01_0001_p620577269489"></a><a name="vpc_sg01_0001_p620577269489"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p644725909489"><a name="vpc_sg01_0001_p644725909489"></a><a name="vpc_sg01_0001_p644725909489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><p id="vpc_sg01_0001_p260700169489"><a name="vpc_sg01_0001_p260700169489"></a><a name="vpc_sg01_0001_p260700169489"></a>Specifies the security group rule ID, which uniquely identifies the security group rule.</p>
    </td>
    </tr>
    <tr id="vpc_sg01_0001_row602307149489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p184092199489"><a name="vpc_sg01_0001_p184092199489"></a><a name="vpc_sg01_0001_p184092199489"></a>direction</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p499849219489"><a name="vpc_sg01_0001_p499849219489"></a><a name="vpc_sg01_0001_p499849219489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="vpc_sg01_0001_ul8415142317513"></a><a name="vpc_sg01_0001_ul8415142317513"></a><ul id="vpc_sg01_0001_ul8415142317513"><li>Specifies the direction of access control.</li><li>Possible values are as follows:<a name="vpc_sg01_0001_ul6968104419355"></a><a name="vpc_sg01_0001_ul6968104419355"></a><ul id="vpc_sg01_0001_ul6968104419355"><li><strong id="vpc_sg01_0001_b96381611133314"><a name="vpc_sg01_0001_b96381611133314"></a><a name="vpc_sg01_0001_b96381611133314"></a>egress</strong></li><li><strong id="vpc_sg01_0001_b9979172133411"><a name="vpc_sg01_0001_b9979172133411"></a><a name="vpc_sg01_0001_b9979172133411"></a>ingress</strong></li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="vpc_sg01_0001_row53906049489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p460392719489"><a name="vpc_sg01_0001_p460392719489"></a><a name="vpc_sg01_0001_p460392719489"></a>ethertype</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p248464689489"><a name="vpc_sg01_0001_p248464689489"></a><a name="vpc_sg01_0001_p248464689489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="vpc_sg01_0001_ul78261926205119"></a><a name="vpc_sg01_0001_ul78261926205119"></a><ul id="vpc_sg01_0001_ul78261926205119"><li>Specifies the IP protocol version.</li><li>The value can be <strong>IPv4</strong> or <strong>IPv6</strong>.</li></ul>
    </td>
    </tr>
    <tr id="vpc_sg01_0001_row619098859489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p520137079489"><a name="vpc_sg01_0001_p520137079489"></a><a name="vpc_sg01_0001_p520137079489"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p17867349489"><a name="vpc_sg01_0001_p17867349489"></a><a name="vpc_sg01_0001_p17867349489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="vpc_sg01_0001_ul585593011517"></a><a name="vpc_sg01_0001_ul585593011517"></a><ul id="vpc_sg01_0001_ul585593011517"><li>Specifies the protocol type.</li><li>The value can be <strong id="vpc_sg01_0001_b1459493374214"><a name="vpc_sg01_0001_b1459493374214"></a><a name="vpc_sg01_0001_b1459493374214"></a>icmp</strong>, <strong id="vpc_sg01_0001_b115948336427"><a name="vpc_sg01_0001_b115948336427"></a><a name="vpc_sg01_0001_b115948336427"></a>tcp</strong>, or <strong id="vpc_sg01_0001_b659723354216"><a name="vpc_sg01_0001_b659723354216"></a><a name="vpc_sg01_0001_b659723354216"></a>udp</strong>.</li><li>If the parameter is left blank, all protocols are supported.</li></ul>
    </td>
    </tr>
    <tr id="vpc_sg01_0001_row29885099489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p424368709489"><a name="vpc_sg01_0001_p424368709489"></a><a name="vpc_sg01_0001_p424368709489"></a>port_range_min</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p167549899489"><a name="vpc_sg01_0001_p167549899489"></a><a name="vpc_sg01_0001_p167549899489"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="vpc_sg01_0001_ul1445493595119"></a><a name="vpc_sg01_0001_ul1445493595119"></a><ul id="vpc_sg01_0001_ul1445493595119"><li>Specifies the start port number.</li><li>The value ranges from 1 to 65535.</li><li>The value cannot be greater than the <strong id="vpc_sg01_0001_b842352706195750"><a name="vpc_sg01_0001_b842352706195750"></a><a name="vpc_sg01_0001_b842352706195750"></a>port_range_max</strong> value. An empty value indicates all ports. If the protocol is <strong id="vpc_sg01_0001_b842352706195910"><a name="vpc_sg01_0001_b842352706195910"></a><a name="vpc_sg01_0001_b842352706195910"></a>icmp</strong>, the value range is shown in <a href="icmp-port-range-relationship-table.md">ICMP-Port Range Relationship Table</a>.</li></ul>
    </td>
    </tr>
    <tr id="vpc_sg01_0001_row330228649489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p239666849489"><a name="vpc_sg01_0001_p239666849489"></a><a name="vpc_sg01_0001_p239666849489"></a>port_range_max</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p641378179489"><a name="vpc_sg01_0001_p641378179489"></a><a name="vpc_sg01_0001_p641378179489"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="vpc_sg01_0001_ul23372407514"></a><a name="vpc_sg01_0001_ul23372407514"></a><ul id="vpc_sg01_0001_ul23372407514"><li>Specifies the end port number.</li><li>The value ranges from 1 to 65535.</li><li>If the protocol is not <strong id="vpc_sg01_0001_b842352706195730"><a name="vpc_sg01_0001_b842352706195730"></a><a name="vpc_sg01_0001_b842352706195730"></a>icmp</strong>, the value cannot be smaller than the <strong id="vpc_sg01_0001_b33723164"><a name="vpc_sg01_0001_b33723164"></a><a name="vpc_sg01_0001_b33723164"></a>port_range_min</strong> value. An empty value indicates all ports. If the protocol is <strong id="vpc_sg01_0001_b1736655103"><a name="vpc_sg01_0001_b1736655103"></a><a name="vpc_sg01_0001_b1736655103"></a>icmp</strong>, the value range is shown in <a href="icmp-port-range-relationship-table.md">ICMP-Port Range Relationship Table</a>.</li></ul>
    </td>
    </tr>
    <tr id="vpc_sg01_0001_row1745649489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p144166029489"><a name="vpc_sg01_0001_p144166029489"></a><a name="vpc_sg01_0001_p144166029489"></a>remote_ip_prefix</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p139601239489"><a name="vpc_sg01_0001_p139601239489"></a><a name="vpc_sg01_0001_p139601239489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="vpc_sg01_0001_ul42481344125119"></a><a name="vpc_sg01_0001_ul42481344125119"></a><ul id="vpc_sg01_0001_ul42481344125119"><li>Specifies the remote IP address. If the access control direction is set to <strong>egress</strong>, the parameter specifies the source IP address. If the access control direction is set to <strong>ingress</strong>, the parameter specifies the destination IP address.</li><li>The value can be in the CIDR format or IP addresses.</li><li>The parameter is exclusive with parameter <strong>remote_group_id</strong>.</li></ul>
    </td>
    </tr>
    <tr id="vpc_sg01_0001_row436879079489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p420105089489"><a name="vpc_sg01_0001_p420105089489"></a><a name="vpc_sg01_0001_p420105089489"></a>remote_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p465213149489"><a name="vpc_sg01_0001_p465213149489"></a><a name="vpc_sg01_0001_p465213149489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="vpc_sg01_0001_ul12672447145118"></a><a name="vpc_sg01_0001_ul12672447145118"></a><ul id="vpc_sg01_0001_ul12672447145118"><li>Specifies the ID of the peer security group.</li><li>The value is exclusive with parameter <strong>remote_ip_prefix</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "security_group_rule": {
            "direction": "ingress",
            "ethertype": "IPv4",
            "id": "2bc0accf-312e-429a-956e-e4407625eb62",
            "description": "",
            "port_range_max": 80,
            "port_range_min": 80,
            "protocol": "tcp",
            "remote_group_id": "85cc3048-abc3-43cc-89b3-377341426ac5",
            "remote_ip_prefix": null,
            "security_group_id": "a7734e61-b545-452d-a3cd-0189cbd9747a",
            "tenant_id": "e4f50856753b4dc6afee5fa6b9b6c550"
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

