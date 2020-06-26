# Creating a Security Group<a name="vpc_sg01_0001"></a>

## Function<a name="section1251609489"></a>

This API is used to create a security group.

## URI<a name="section33062409489"></a>

POST /v1/\{project\_id\}/security-groups

[Table 1](#table483113939489)  describes the parameters.

**Table  1**  Parameter description

<a name="table483113939489"></a>
<table><thead align="left"><tr id="row411182539489"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p463378669489"><a name="p463378669489"></a><a name="p463378669489"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p564715189489"><a name="p564715189489"></a><a name="p564715189489"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p724579489"><a name="p724579489"></a><a name="p724579489"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row527882029489"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p111312999489"><a name="p111312999489"></a><a name="p111312999489"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p660990279489"><a name="p660990279489"></a><a name="p660990279489"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section604597999489"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table44974649489"></a>
    <table><thead align="left"><tr id="row299697129489"><th class="cellrowborder" valign="top" width="20.412041204120413%" id="mcps1.2.5.1.1"><p id="p285205769489"><a name="p285205769489"></a><a name="p285205769489"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.45214521452145%" id="mcps1.2.5.1.2"><p id="p465402789489"><a name="p465402789489"></a><a name="p465402789489"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.311431143114312%" id="mcps1.2.5.1.3"><p id="p238240519489"><a name="p238240519489"></a><a name="p238240519489"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.824382438243816%" id="mcps1.2.5.1.4"><p id="p48352879489"><a name="p48352879489"></a><a name="p48352879489"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16369959489"><td class="cellrowborder" valign="top" width="20.412041204120413%" headers="mcps1.2.5.1.1 "><p id="p319354459489"><a name="p319354459489"></a><a name="p319354459489"></a>security_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.45214521452145%" headers="mcps1.2.5.1.2 "><p id="p302461269489"><a name="p302461269489"></a><a name="p302461269489"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.311431143114312%" headers="mcps1.2.5.1.3 "><p id="p12807519489"><a name="p12807519489"></a><a name="p12807519489"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.824382438243816%" headers="mcps1.2.5.1.4 "><p id="p151006069489"><a name="p151006069489"></a><a name="p151006069489"></a>Specifies the security group objects. For details, see <a href="#table495783939489">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of  **security\_group**  fields

    <a name="table495783939489"></a>
    <table><thead align="left"><tr id="row256595299489"><th class="cellrowborder" valign="top" width="15.310000000000002%" id="mcps1.2.5.1.1"><p id="p210585389489"><a name="p210585389489"></a><a name="p210585389489"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.5.1.2"><p id="p583665309489"><a name="p583665309489"></a><a name="p583665309489"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.93%" id="mcps1.2.5.1.3"><p id="p382880489489"><a name="p382880489489"></a><a name="p382880489489"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.03%" id="mcps1.2.5.1.4"><p id="p120218469489"><a name="p120218469489"></a><a name="p120218469489"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row289879879489"><td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.2.5.1.1 "><p id="p422266319489"><a name="p422266319489"></a><a name="p422266319489"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.2 "><p id="p392406589489"><a name="p392406589489"></a><a name="p392406589489"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.93%" headers="mcps1.2.5.1.3 "><p id="p291833799489"><a name="p291833799489"></a><a name="p291833799489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.03%" headers="mcps1.2.5.1.4 "><a name="ul152111153467"></a><a name="ul152111153467"></a><ul id="ul152111153467"><li>Specifies the security group name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="row335873009489"><td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.2.5.1.1 "><p id="p505959349489"><a name="p505959349489"></a><a name="p505959349489"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.2 "><p id="p24479189489"><a name="p24479189489"></a><a name="p24479189489"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.93%" headers="mcps1.2.5.1.3 "><p id="p518535589489"><a name="p518535589489"></a><a name="p518535589489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.03%" headers="mcps1.2.5.1.4 "><p id="p220374619489"><a name="p220374619489"></a><a name="p220374619489"></a>Specifies the resource ID of the VPC to which the security group belongs.</p>
    <div class="note" id="note4236171919347"><a name="note4236171919347"></a><a name="note4236171919347"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142368196344"><a name="p142368196344"></a><a name="p142368196344"></a>This parameter has been discarded, it is not recommended to use it.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{Endpoint}/v1/{project_id}/security-groups
    
    {
        "security_group": {
            "name": "qq", 
            "vpc_id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85"
            
        }
    }
    ```


## Response Message<a name="section488521769489"></a>

-   Response parameter

    **Table  4**  Response parameter

    <a name="table187664789489"></a>
    <table><thead align="left"><tr id="row101573199489"><th class="cellrowborder" valign="top" width="23.26%" id="mcps1.2.4.1.1"><p id="p444890459489"><a name="p444890459489"></a><a name="p444890459489"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.09%" id="mcps1.2.4.1.2"><p id="p437522139489"><a name="p437522139489"></a><a name="p437522139489"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.65%" id="mcps1.2.4.1.3"><p id="p578362329489"><a name="p578362329489"></a><a name="p578362329489"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row449165309489"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p268266119489"><a name="p268266119489"></a><a name="p268266119489"></a>security_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.09%" headers="mcps1.2.4.1.2 "><p id="p630794179489"><a name="p630794179489"></a><a name="p630794179489"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.65%" headers="mcps1.2.4.1.3 "><p id="p349251459489"><a name="p349251459489"></a><a name="p349251459489"></a>Specifies the security group objects. For details, see <a href="#table661472489489">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Description of  **security\_group**  fields

    <a name="table661472489489"></a>
    <table><thead align="left"><tr id="row158029169489"><th class="cellrowborder" valign="top" width="34.52%" id="mcps1.2.4.1.1"><p id="p581966039489"><a name="p581966039489"></a><a name="p581966039489"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.45%" id="mcps1.2.4.1.2"><p id="p166624639489"><a name="p166624639489"></a><a name="p166624639489"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.03%" id="mcps1.2.4.1.3"><p id="p278965559489"><a name="p278965559489"></a><a name="p278965559489"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row643785269489"><td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.1 "><p id="p329359299489"><a name="p329359299489"></a><a name="p329359299489"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.2.4.1.2 "><p id="p230963549489"><a name="p230963549489"></a><a name="p230963549489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.03%" headers="mcps1.2.4.1.3 "><p id="p410063869489"><a name="p410063869489"></a><a name="p410063869489"></a>Specifies the security group name.</p>
    </td>
    </tr>
    <tr id="row32100149489"><td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.1 "><p id="p522665169489"><a name="p522665169489"></a><a name="p522665169489"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.2.4.1.2 "><p id="p513285489489"><a name="p513285489489"></a><a name="p513285489489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.03%" headers="mcps1.2.4.1.3 "><p id="p290727679489"><a name="p290727679489"></a><a name="p290727679489"></a>Provides supplementary information about the security group.</p>
    </td>
    </tr>
    <tr id="row639972559489"><td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.1 "><p id="p634276169489"><a name="p634276169489"></a><a name="p634276169489"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.2.4.1.2 "><p id="p114487449489"><a name="p114487449489"></a><a name="p114487449489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.03%" headers="mcps1.2.4.1.3 "><p id="p259109349489"><a name="p259109349489"></a><a name="p259109349489"></a>Specifies the security group ID, which uniquely identifies the security group.</p>
    </td>
    </tr>
    <tr id="row422544629489"><td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.1 "><p id="p590727719489"><a name="p590727719489"></a><a name="p590727719489"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.2.4.1.2 "><p id="p10272179489"><a name="p10272179489"></a><a name="p10272179489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.03%" headers="mcps1.2.4.1.3 "><p id="p303149719489"><a name="p303149719489"></a><a name="p303149719489"></a>Specifies the resource ID of the VPC to which the security group belongs.</p>
    <div class="note" id="note1071412434342"><a name="note1071412434342"></a><a name="note1071412434342"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p137151443133411"><a name="p137151443133411"></a><a name="p137151443133411"></a>This parameter has been discarded, it is not recommended to use it.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row30397199489"><td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.1 "><p id="p252491199489"><a name="p252491199489"></a><a name="p252491199489"></a>security_group_rules</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.2.4.1.2 "><p id="p193798449489"><a name="p193798449489"></a><a name="p193798449489"></a>Array of <a href="#table210704979489">security_group_rule</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.03%" headers="mcps1.2.4.1.3 "><p id="p643841019489"><a name="p643841019489"></a><a name="p643841019489"></a>Specifies the default security group rule, which ensures that resources in the security group can communicate with one another.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **security\_group\_rule**  objects

    <a name="table210704979489"></a>
    <table><thead align="left"><tr id="row611024789489"><th class="cellrowborder" valign="top" width="34.143414341434145%" id="mcps1.2.4.1.1"><p id="p98931099489"><a name="p98931099489"></a><a name="p98931099489"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.732073207320735%" id="mcps1.2.4.1.2"><p id="p368367439489"><a name="p368367439489"></a><a name="p368367439489"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.124512451245124%" id="mcps1.2.4.1.3"><p id="p23523719489"><a name="p23523719489"></a><a name="p23523719489"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row397690789489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="p656951529489"><a name="p656951529489"></a><a name="p656951529489"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="p307102169489"><a name="p307102169489"></a><a name="p307102169489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><p id="p216633359489"><a name="p216633359489"></a><a name="p216633359489"></a>Specifies the security group rule ID, which uniquely identifies the security group rule.</p>
    </td>
    </tr>
    <tr id="row2447898388"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="p432391116381"><a name="p432391116381"></a><a name="p432391116381"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="p20328111163813"><a name="p20328111163813"></a><a name="p20328111163813"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="ul12329121935111"></a><a name="ul12329121935111"></a><ul id="ul12329121935111"><li>Provides supplementary information about the security group rule.</li><li>The value is a string of no more than 255 characters that can contain letters and digits.</li></ul>
    </td>
    </tr>
    <tr id="row320377939489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="p620577269489"><a name="p620577269489"></a><a name="p620577269489"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="p644725909489"><a name="p644725909489"></a><a name="p644725909489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><p id="p260700169489"><a name="p260700169489"></a><a name="p260700169489"></a>Specifies the security group rule ID, which uniquely identifies the security group rule.</p>
    </td>
    </tr>
    <tr id="row602307149489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="p184092199489"><a name="p184092199489"></a><a name="p184092199489"></a>direction</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="p499849219489"><a name="p499849219489"></a><a name="p499849219489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="ul8415142317513"></a><a name="ul8415142317513"></a><ul id="ul8415142317513"><li>Specifies the direction of access control.</li><li>Possible values are as follows:<a name="ul6968104419355"></a><a name="ul6968104419355"></a><ul id="ul6968104419355"><li><strong id="b96381611133314"><a name="b96381611133314"></a><a name="b96381611133314"></a>egress</strong></li><li><strong id="b9979172133411"><a name="b9979172133411"></a><a name="b9979172133411"></a>ingress</strong></li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row53906049489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="p460392719489"><a name="p460392719489"></a><a name="p460392719489"></a>ethertype</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="p248464689489"><a name="p248464689489"></a><a name="p248464689489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="ul78261926205119"></a><a name="ul78261926205119"></a><ul id="ul78261926205119"><li>Specifies the IP protocol version.</li><li>The value can be <strong>IPv4</strong> or <strong>IPv6</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row619098859489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="p520137079489"><a name="p520137079489"></a><a name="p520137079489"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="p17867349489"><a name="p17867349489"></a><a name="p17867349489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="ul585593011517"></a><a name="ul585593011517"></a><ul id="ul585593011517"><li>Specifies the protocol type.</li><li>The value can be <strong id="b1459493374214"><a name="b1459493374214"></a><a name="b1459493374214"></a>icmp</strong>, <strong id="b115948336427"><a name="b115948336427"></a><a name="b115948336427"></a>tcp</strong>, or <strong id="b659723354216"><a name="b659723354216"></a><a name="b659723354216"></a>udp</strong>.</li><li>If the parameter is left blank, all protocols are supported.</li></ul>
    </td>
    </tr>
    <tr id="row29885099489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="p424368709489"><a name="p424368709489"></a><a name="p424368709489"></a>port_range_min</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="p167549899489"><a name="p167549899489"></a><a name="p167549899489"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="ul1445493595119"></a><a name="ul1445493595119"></a><ul id="ul1445493595119"><li>Specifies the start port number.</li><li>The value ranges from 1 to 65535.</li><li>The value cannot be greater than the <strong id="b842352706195750"><a name="b842352706195750"></a><a name="b842352706195750"></a>port_range_max</strong> value. An empty value indicates all ports. If the protocol is <strong id="b842352706195910"><a name="b842352706195910"></a><a name="b842352706195910"></a>icmp</strong>, the value range is shown in <a href="icmp-port-range-relationship-table.md">ICMP-Port Range Relationship Table</a>.</li></ul>
    </td>
    </tr>
    <tr id="row330228649489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="p239666849489"><a name="p239666849489"></a><a name="p239666849489"></a>port_range_max</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="p641378179489"><a name="p641378179489"></a><a name="p641378179489"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="ul23372407514"></a><a name="ul23372407514"></a><ul id="ul23372407514"><li>Specifies the end port number.</li><li>The value ranges from 1 to 65535.</li><li>If the protocol is not <strong id="b842352706195730"><a name="b842352706195730"></a><a name="b842352706195730"></a>icmp</strong>, the value cannot be smaller than the <strong id="b33723164"><a name="b33723164"></a><a name="b33723164"></a>port_range_min</strong> value. An empty value indicates all ports. If the protocol is <strong id="b1736655103"><a name="b1736655103"></a><a name="b1736655103"></a>icmp</strong>, the value range is shown in <a href="icmp-port-range-relationship-table.md">ICMP-Port Range Relationship Table</a>.</li></ul>
    </td>
    </tr>
    <tr id="row1745649489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="p144166029489"><a name="p144166029489"></a><a name="p144166029489"></a>remote_ip_prefix</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="p139601239489"><a name="p139601239489"></a><a name="p139601239489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="ul42481344125119"></a><a name="ul42481344125119"></a><ul id="ul42481344125119"><li>Specifies the remote IP address. If the access control direction is set to <strong>egress</strong>, the parameter specifies the source IP address. If the access control direction is set to <strong>ingress</strong>, the parameter specifies the destination IP address.</li><li>The value can be in the CIDR format or IP addresses.</li><li>The parameter is exclusive with parameter <strong>remote_group_id</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row436879079489"><td class="cellrowborder" valign="top" width="34.143414341434145%" headers="mcps1.2.4.1.1 "><p id="p420105089489"><a name="p420105089489"></a><a name="p420105089489"></a>remote_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.732073207320735%" headers="mcps1.2.4.1.2 "><p id="p465213149489"><a name="p465213149489"></a><a name="p465213149489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.124512451245124%" headers="mcps1.2.4.1.3 "><a name="ul12672447145118"></a><a name="ul12672447145118"></a><ul id="ul12672447145118"><li>Specifies the ID of the peer security group.</li><li>The value is exclusive with parameter <strong>remote_ip_prefix</strong>.</li></ul>
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
            "description": "", 
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

