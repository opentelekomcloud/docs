# Querying an EIP<a name="eip_api_0002"></a>

## Function<a name="en-us_topic_0201534285_section40040492"></a>

This API is used to query an EIP.

## URI<a name="en-us_topic_0201534285_section24820109"></a>

GET /v1/\{project\_id\}/publicips/\{publicip\_id\}

[Table 1](#en-us_topic_0201534285_table57982344)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534285_table57982344"></a>
<table><thead align="left"><tr id="en-us_topic_0201534285_row19130757"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534285_p6087504"><a name="en-us_topic_0201534285_p6087504"></a><a name="en-us_topic_0201534285_p6087504"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534285_p23325828"><a name="en-us_topic_0201534285_p23325828"></a><a name="en-us_topic_0201534285_p23325828"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534285_p10343879"><a name="en-us_topic_0201534285_p10343879"></a><a name="en-us_topic_0201534285_p10343879"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534285_row32547908"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534285_p19134881"><a name="en-us_topic_0201534285_p19134881"></a><a name="en-us_topic_0201534285_p19134881"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534285_p6421510"><a name="en-us_topic_0201534285_p6421510"></a><a name="en-us_topic_0201534285_p6421510"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534285_p10487112"><a name="en-us_topic_0201534285_p10487112"></a><a name="en-us_topic_0201534285_p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="en-us_topic_0201534285_row50769665"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534285_p18702178"><a name="en-us_topic_0201534285_p18702178"></a><a name="en-us_topic_0201534285_p18702178"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534285_p38481481"><a name="en-us_topic_0201534285_p38481481"></a><a name="en-us_topic_0201534285_p38481481"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534285_p29992219"><a name="en-us_topic_0201534285_p29992219"></a><a name="en-us_topic_0201534285_p29992219"></a>Specifies the unique identifier of the EIP.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534285_section22054394"></a>

-   Request parameter

    None

-   Example request

    None


## Response Message<a name="en-us_topic_0201534285_section64271818"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="en-us_topic_0201534285_table64961662152123"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534285_row7248731152123"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534285_p50276345152123"><a name="en-us_topic_0201534285_p50276345152123"></a><a name="en-us_topic_0201534285_p50276345152123"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534285_p23039456152123"><a name="en-us_topic_0201534285_p23039456152123"></a><a name="en-us_topic_0201534285_p23039456152123"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534285_p54256632152123"><a name="en-us_topic_0201534285_p54256632152123"></a><a name="en-us_topic_0201534285_p54256632152123"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534285_row32711048152123"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534285_p32349241152123"><a name="en-us_topic_0201534285_p32349241152123"></a><a name="en-us_topic_0201534285_p32349241152123"></a>publicip</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534285_p45145628152123"><a name="en-us_topic_0201534285_p45145628152123"></a><a name="en-us_topic_0201534285_p45145628152123"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534285_p27820057152123"><a name="en-us_topic_0201534285_p27820057152123"></a><a name="en-us_topic_0201534285_p27820057152123"></a>Specifies the EIP objects. For details, see <a href="#en-us_topic_0201534285_table3035698">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **publicip**  field

    <a name="en-us_topic_0201534285_table3035698"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534285_row64466590"><th class="cellrowborder" valign="top" width="36.046395360463954%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534285_p54411269"><a name="en-us_topic_0201534285_p54411269"></a><a name="en-us_topic_0201534285_p54411269"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="27.90720927907209%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534285_p3124580518523"><a name="en-us_topic_0201534285_p3124580518523"></a><a name="en-us_topic_0201534285_p3124580518523"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="36.046395360463954%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534285_p40293226"><a name="en-us_topic_0201534285_p40293226"></a><a name="en-us_topic_0201534285_p40293226"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534285_row42525879"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534285_p22044193"><a name="en-us_topic_0201534285_p22044193"></a><a name="en-us_topic_0201534285_p22044193"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534285_p4788225318523"><a name="en-us_topic_0201534285_p4788225318523"></a><a name="en-us_topic_0201534285_p4788225318523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534285_p44048571"><a name="en-us_topic_0201534285_p44048571"></a><a name="en-us_topic_0201534285_p44048571"></a>Specifies the unique identifier of the EIP.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534285_row60892825"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534285_p33371781"><a name="en-us_topic_0201534285_p33371781"></a><a name="en-us_topic_0201534285_p33371781"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534285_p5325729418523"><a name="en-us_topic_0201534285_p5325729418523"></a><a name="en-us_topic_0201534285_p5325729418523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534285_ul1945793192"></a><a name="en-us_topic_0201534285_ul1945793192"></a><ul id="en-us_topic_0201534285_ul1945793192"><li>Specifies the EIP status.</li><li>Possible values are as follows:<a name="en-us_topic_0201534285_ul4678228115815"></a><a name="en-us_topic_0201534285_ul4678228115815"></a><ul id="en-us_topic_0201534285_ul4678228115815"><li><strong id="en-us_topic_0201534285_b84235270610153"><a name="en-us_topic_0201534285_b84235270610153"></a><a name="en-us_topic_0201534285_b84235270610153"></a>FREEZED</strong> (Frozen)</li><li><strong id="en-us_topic_0201534285_b842352706181622"><a name="en-us_topic_0201534285_b842352706181622"></a><a name="en-us_topic_0201534285_b842352706181622"></a>BIND_ERROR</strong> (Binding failed)</li><li><strong id="en-us_topic_0201534285_b842352706181646"><a name="en-us_topic_0201534285_b842352706181646"></a><a name="en-us_topic_0201534285_b842352706181646"></a>BINDING</strong> (Binding)</li><li><strong id="en-us_topic_0201534285_b84235270618176"><a name="en-us_topic_0201534285_b84235270618176"></a><a name="en-us_topic_0201534285_b84235270618176"></a>PENDING_DELETE</strong> (Releasing)</li><li><strong id="en-us_topic_0201534285_b842352706181716"><a name="en-us_topic_0201534285_b842352706181716"></a><a name="en-us_topic_0201534285_b842352706181716"></a>PENDING_CREATE</strong> (Assigning)</li><li><strong id="en-us_topic_0201534285_b842352706181818"><a name="en-us_topic_0201534285_b842352706181818"></a><a name="en-us_topic_0201534285_b842352706181818"></a>PENDING_UPDATE</strong> (Updating)</li><li><strong id="en-us_topic_0201534285_b842352706181834"><a name="en-us_topic_0201534285_b842352706181834"></a><a name="en-us_topic_0201534285_b842352706181834"></a>DOWN</strong> (Unbound)</li><li><strong id="en-us_topic_0201534285_b84235270610164"><a name="en-us_topic_0201534285_b84235270610164"></a><a name="en-us_topic_0201534285_b84235270610164"></a>ACTIVE</strong> (Bound)</li><li><strong id="en-us_topic_0201534285_b842352706181859"><a name="en-us_topic_0201534285_b842352706181859"></a><a name="en-us_topic_0201534285_b842352706181859"></a>ELB</strong> (Bound to a load balancer)</li><li><strong id="en-us_topic_0201534285_b842352706103022"><a name="en-us_topic_0201534285_b842352706103022"></a><a name="en-us_topic_0201534285_b842352706103022"></a>ERROR</strong> (Exceptions)</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534285_row1722212174296"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534285_p15848707"><a name="en-us_topic_0201534285_p15848707"></a><a name="en-us_topic_0201534285_p15848707"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534285_p3408038918330"><a name="en-us_topic_0201534285_p3408038918330"></a><a name="en-us_topic_0201534285_p3408038918330"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534285_ul7176216121014"></a><a name="en-us_topic_0201534285_ul7176216121014"></a><ul id="en-us_topic_0201534285_ul7176216121014"><li>Specifies the EIP type.</li><li>Constraints:<a name="en-us_topic_0201534285_ul9738153015499"></a><a name="en-us_topic_0201534285_ul9738153015499"></a><ul id="en-us_topic_0201534285_ul9738153015499"><li>The configured value must be supported by the system. </li><li><strong id="en-us_topic_0201534285_b1663115310288"><a name="en-us_topic_0201534285_b1663115310288"></a><a name="en-us_topic_0201534285_b1663115310288"></a>publicip_id</strong> is an IPv4 port. If <strong id="en-us_topic_0201534285_b1651253172819"><a name="en-us_topic_0201534285_b1651253172819"></a><a name="en-us_topic_0201534285_b1651253172819"></a>publicip_type</strong> is not specified, the default value is <strong id="en-us_topic_0201534285_b26695319283"><a name="en-us_topic_0201534285_b26695319283"></a><a name="en-us_topic_0201534285_b26695319283"></a>5_bgp</strong>.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534285_row66070243"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534285_p50089467"><a name="en-us_topic_0201534285_p50089467"></a><a name="en-us_topic_0201534285_p50089467"></a>private_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534285_p1357258018523"><a name="en-us_topic_0201534285_p1357258018523"></a><a name="en-us_topic_0201534285_p1357258018523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534285_ul1693412582014"></a><a name="en-us_topic_0201534285_ul1693412582014"></a><ul id="en-us_topic_0201534285_ul1693412582014"><li>Specifies the private IP address bound with the EIP.</li><li>This parameter is returned only when a private IP address is bound with the EIP.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534285_row12246230153229"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534285_p11971849153234"><a name="en-us_topic_0201534285_p11971849153234"></a><a name="en-us_topic_0201534285_p11971849153234"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534285_p2563717518523"><a name="en-us_topic_0201534285_p2563717518523"></a><a name="en-us_topic_0201534285_p2563717518523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534285_ul420471472010"></a><a name="en-us_topic_0201534285_ul420471472010"></a><ul id="en-us_topic_0201534285_ul420471472010"><li>Specifies the port ID.</li><li>This parameter is returned only when a private IP address is bound with the EIP.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534285_row7204713"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534285_p46710863"><a name="en-us_topic_0201534285_p46710863"></a><a name="en-us_topic_0201534285_p46710863"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534285_p6334526618523"><a name="en-us_topic_0201534285_p6334526618523"></a><a name="en-us_topic_0201534285_p6334526618523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534285_p25354291121"><a name="en-us_topic_0201534285_p25354291121"></a><a name="en-us_topic_0201534285_p25354291121"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534285_row55494360"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534285_p65858198"><a name="en-us_topic_0201534285_p65858198"></a><a name="en-us_topic_0201534285_p65858198"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534285_p3069292618523"><a name="en-us_topic_0201534285_p3069292618523"></a><a name="en-us_topic_0201534285_p3069292618523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534285_p36292894"><a name="en-us_topic_0201534285_p36292894"></a><a name="en-us_topic_0201534285_p36292894"></a>Specifies the time (UTC time) when the EIP was assigned.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534285_row58200593"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534285_p16627584"><a name="en-us_topic_0201534285_p16627584"></a><a name="en-us_topic_0201534285_p16627584"></a>bandwidth_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534285_p309907418523"><a name="en-us_topic_0201534285_p309907418523"></a><a name="en-us_topic_0201534285_p309907418523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534285_p3934181618641"><a name="en-us_topic_0201534285_p3934181618641"></a><a name="en-us_topic_0201534285_p3934181618641"></a>Specifies the ID of the bandwidth associated with the EIP.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534285_row51415138"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534285_p3876622"><a name="en-us_topic_0201534285_p3876622"></a><a name="en-us_topic_0201534285_p3876622"></a>bandwidth_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534285_p4969847118523"><a name="en-us_topic_0201534285_p4969847118523"></a><a name="en-us_topic_0201534285_p4969847118523"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534285_p2365466"><a name="en-us_topic_0201534285_p2365466"></a><a name="en-us_topic_0201534285_p2365466"></a>Specifies the bandwidth (Mbit/s).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534285_row21289199"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534285_p46703582"><a name="en-us_topic_0201534285_p46703582"></a><a name="en-us_topic_0201534285_p46703582"></a>bandwidth_share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534285_p6615323718523"><a name="en-us_topic_0201534285_p6615323718523"></a><a name="en-us_topic_0201534285_p6615323718523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534285_ul2255712095"></a><a name="en-us_topic_0201534285_ul2255712095"></a><ul id="en-us_topic_0201534285_ul2255712095"><li>Specifies the EIP bandwidth type.</li><li>The value can be <strong id="en-us_topic_0201534285_b732433921164019"><a name="en-us_topic_0201534285_b732433921164019"></a><a name="en-us_topic_0201534285_b732433921164019"></a>PER</strong> or <strong id="en-us_topic_0201534285_b1729357023164019"><a name="en-us_topic_0201534285_b1729357023164019"></a><a name="en-us_topic_0201534285_b1729357023164019"></a>WHOLE</strong>.<a name="en-us_topic_0201534285_ul729412507220"></a><a name="en-us_topic_0201534285_ul729412507220"></a><ul id="en-us_topic_0201534285_ul729412507220"><li><strong id="en-us_topic_0201534285_b842352706204716"><a name="en-us_topic_0201534285_b842352706204716"></a><a name="en-us_topic_0201534285_b842352706204716"></a>PER</strong>: Dedicated bandwidth</li><li><strong id="en-us_topic_0201534285_b842352706204729"><a name="en-us_topic_0201534285_b842352706204729"></a><a name="en-us_topic_0201534285_b842352706204729"></a>WHOLE</strong>: Shared bandwidth</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "publicip": {
            "id": "2ec9b78d-9368-46f3-8f29-d1a95622a568",
            "status": "DOWN",
            "type": "5_bgp",
            "public_ip_address": "161.xx.xx.12",
            "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
            "private_ip_address": "192.168.10.5",
            "create_time": "2015-07-16 04:32:50",
            "bandwidth_id": "49c8825b-bed9-46ff-9416-704b96d876a2",
            "bandwidth_share_type": "PER",
    "bandwidth_size": 10,    //The EIP bandwidth size is 10 Mbit/s.
           
            "ip_version": 4
        }
    }
    ```


## Status Code<a name="en-us_topic_0201534285_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534285_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

