# Querying Security Group Details<a name="vpc_sg01_0002"></a>

## Function<a name="section183641929520"></a>

This API is used to query details about a security group.

## URI<a name="section383863439520"></a>

GET /v1/\{project\_id\}/security-groups/\{security\_group\_id\}

[Table 1](#table211310359520)  describes the parameters.

**Table  1**  Parameter description

<a name="table211310359520"></a>
<table><thead align="left"><tr id="row27117139520"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p648001349520"><a name="p648001349520"></a><a name="p648001349520"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p477321789520"><a name="p477321789520"></a><a name="p477321789520"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p94870139520"><a name="p94870139520"></a><a name="p94870139520"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row81820489520"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p551819219520"><a name="p551819219520"></a><a name="p551819219520"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p419930979520"><a name="p419930979520"></a><a name="p419930979520"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row610956059520"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p563498999520"><a name="p563498999520"></a><a name="p563498999520"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p577313839520"><a name="p577313839520"></a><a name="p577313839520"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p482793239520"><a name="p482793239520"></a><a name="p482793239520"></a>Specifies the security group ID, which uniquely identifies the security group.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section166598629520"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}/v1/{project_id}/security-groups/16b6e77a-08fa-42c7-aa8b-106c048884e6
    ```


## Response Message<a name="section77135839520"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table421354429520"></a>
    <table><thead align="left"><tr id="row4869309520"><th class="cellrowborder" valign="top" width="23.26%" id="mcps1.2.4.1.1"><p id="p436004679520"><a name="p436004679520"></a><a name="p436004679520"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.09%" id="mcps1.2.4.1.2"><p id="p503805059520"><a name="p503805059520"></a><a name="p503805059520"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.65%" id="mcps1.2.4.1.3"><p id="p31092159520"><a name="p31092159520"></a><a name="p31092159520"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row402360929520"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p563104169520"><a name="p563104169520"></a><a name="p563104169520"></a>security_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.09%" headers="mcps1.2.4.1.2 "><p id="p115123489520"><a name="p115123489520"></a><a name="p115123489520"></a><em id="i258269969520"><a name="i258269969520"></a><a name="i258269969520"></a>Object</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="54.65%" headers="mcps1.2.4.1.3 "><p id="p119580209520"><a name="p119580209520"></a><a name="p119580209520"></a>Specifies the security group object.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of  **security\_group**  fields

    <a name="table333218689520"></a>
    <table><thead align="left"><tr id="vpc_sg01_0001_row158029169489"><th class="cellrowborder" valign="top" width="34.52%" id="mcps1.2.4.1.1"><p id="vpc_sg01_0001_p581966039489"><a name="vpc_sg01_0001_p581966039489"></a><a name="vpc_sg01_0001_p581966039489"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.45%" id="mcps1.2.4.1.2"><p id="vpc_sg01_0001_p166624639489"><a name="vpc_sg01_0001_p166624639489"></a><a name="vpc_sg01_0001_p166624639489"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.03%" id="mcps1.2.4.1.3"><p id="vpc_sg01_0001_p278965559489"><a name="vpc_sg01_0001_p278965559489"></a><a name="vpc_sg01_0001_p278965559489"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpc_sg01_0001_row643785269489"><td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p329359299489"><a name="vpc_sg01_0001_p329359299489"></a><a name="vpc_sg01_0001_p329359299489"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p230963549489"><a name="vpc_sg01_0001_p230963549489"></a><a name="vpc_sg01_0001_p230963549489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.03%" headers="mcps1.2.4.1.3 "><p id="vpc_sg01_0001_p410063869489"><a name="vpc_sg01_0001_p410063869489"></a><a name="vpc_sg01_0001_p410063869489"></a>Specifies the security group name.</p>
    </td>
    </tr>
    <tr id="vpc_sg01_0001_row32100149489"><td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p522665169489"><a name="vpc_sg01_0001_p522665169489"></a><a name="vpc_sg01_0001_p522665169489"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p513285489489"><a name="vpc_sg01_0001_p513285489489"></a><a name="vpc_sg01_0001_p513285489489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.03%" headers="mcps1.2.4.1.3 "><p id="vpc_sg01_0001_p290727679489"><a name="vpc_sg01_0001_p290727679489"></a><a name="vpc_sg01_0001_p290727679489"></a>Provides supplementary information about the security group.</p>
    </td>
    </tr>
    <tr id="vpc_sg01_0001_row639972559489"><td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p634276169489"><a name="vpc_sg01_0001_p634276169489"></a><a name="vpc_sg01_0001_p634276169489"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p114487449489"><a name="vpc_sg01_0001_p114487449489"></a><a name="vpc_sg01_0001_p114487449489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.03%" headers="mcps1.2.4.1.3 "><p id="vpc_sg01_0001_p259109349489"><a name="vpc_sg01_0001_p259109349489"></a><a name="vpc_sg01_0001_p259109349489"></a>Specifies the security group ID, which uniquely identifies the security group.</p>
    </td>
    </tr>
    <tr id="vpc_sg01_0001_row422544629489"><td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p590727719489"><a name="vpc_sg01_0001_p590727719489"></a><a name="vpc_sg01_0001_p590727719489"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p10272179489"><a name="vpc_sg01_0001_p10272179489"></a><a name="vpc_sg01_0001_p10272179489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.03%" headers="mcps1.2.4.1.3 "><p id="vpc_sg01_0001_p303149719489"><a name="vpc_sg01_0001_p303149719489"></a><a name="vpc_sg01_0001_p303149719489"></a>Specifies the resource ID of the VPC to which the security group belongs.</p>
    <div class="note" id="vpc_sg01_0001_note1071412434342"><a name="vpc_sg01_0001_note1071412434342"></a><a name="vpc_sg01_0001_note1071412434342"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="vpc_sg01_0001_p137151443133411"><a name="vpc_sg01_0001_p137151443133411"></a><a name="vpc_sg01_0001_p137151443133411"></a>This parameter has been discarded, it is not recommended to use it.</p>
    </div></div>
    </td>
    </tr>
    <tr id="vpc_sg01_0001_row30397199489"><td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.1 "><p id="vpc_sg01_0001_p252491199489"><a name="vpc_sg01_0001_p252491199489"></a><a name="vpc_sg01_0001_p252491199489"></a>security_group_rules</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.2.4.1.2 "><p id="vpc_sg01_0001_p193798449489"><a name="vpc_sg01_0001_p193798449489"></a><a name="vpc_sg01_0001_p193798449489"></a>Array of <a href="creating-a-security-group.md#table210704979489">security_group_rule</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.03%" headers="mcps1.2.4.1.3 "><p id="vpc_sg01_0001_p643841019489"><a name="vpc_sg01_0001_p643841019489"></a><a name="vpc_sg01_0001_p643841019489"></a>Specifies the default security group rule, which ensures that resources in the security group can communicate with one another.</p>
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
        "security_group": {
            "id": "16b6e77a-08fa-42c7-aa8b-106c048884e6", 
            "name": "qq", 
            "description": "qq", 
            "vpc_id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85", 
            
            "security_group_rules": [
                {
                    "direction": "egress", 
                    "ethertype": "IPv4", 
                    "id": "369e6499-b2cb-4126-972a-97e589692c62", 
                    "description": "",
                    "security_group_id": "16b6e77a-08fa-42c7-aa8b-106c048884e6"
                }, 
                {
                    "direction": "ingress", 
                    "ethertype": "IPv4", 
                    "id": "0222556c-6556-40ad-8aac-9fd5d3c06171", 
                    "description": "",
                    "remote_group_id": "16b6e77a-08fa-42c7-aa8b-106c048884e6", 
                    "security_group_id": "16b6e77a-08fa-42c7-aa8b-106c048884e6"
                }
            ]
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

