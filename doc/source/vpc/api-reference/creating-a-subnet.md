# Creating a Subnet<a name="vpc_subnet01_0001"></a>

## Function<a name="section18389930"></a>

This API is used to create a subnet.

## URI<a name="section31291646"></a>

POST /v1/\{project\_id\}/subnets

[Table 1](#table21421675)  describes the parameters.

**Table  1**  Parameter description

<a name="table21421675"></a>
<table><thead align="left"><tr id="row9119245"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p461342"><a name="p461342"></a><a name="p461342"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p37368736"><a name="p37368736"></a><a name="p37368736"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6968762"><a name="p6968762"></a><a name="p6968762"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row27598869"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p20915929"><a name="p20915929"></a><a name="p20915929"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p16468652"><a name="p16468652"></a><a name="p16468652"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section13189358"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table435429715639"></a>
    <table><thead align="left"><tr id="row3955678815639"><th class="cellrowborder" valign="top" width="15.410000000000002%" id="mcps1.2.5.1.1"><p id="p4998329315639"><a name="p4998329315639"></a><a name="p4998329315639"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.12%" id="mcps1.2.5.1.2"><p id="p2211493815639"><a name="p2211493815639"></a><a name="p2211493815639"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.610000000000003%" id="mcps1.2.5.1.3"><p id="p4647957215639"><a name="p4647957215639"></a><a name="p4647957215639"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.86000000000001%" id="mcps1.2.5.1.4"><p id="p674897815639"><a name="p674897815639"></a><a name="p674897815639"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row979634915639"><td class="cellrowborder" valign="top" width="15.410000000000002%" headers="mcps1.2.5.1.1 "><p id="p5530678015639"><a name="p5530678015639"></a><a name="p5530678015639"></a>subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.12%" headers="mcps1.2.5.1.2 "><p id="p5066418415639"><a name="p5066418415639"></a><a name="p5066418415639"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.610000000000003%" headers="mcps1.2.5.1.3 "><p id="p1015820015639"><a name="p1015820015639"></a><a name="p1015820015639"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.86000000000001%" headers="mcps1.2.5.1.4 "><p id="p2335287515639"><a name="p2335287515639"></a><a name="p2335287515639"></a>Specifies the <a href="#table45596481">subnet objects</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **subnet**  objects

    <a name="table45596481"></a>
    <table><thead align="left"><tr id="row36936550"><th class="cellrowborder" valign="top" width="21.990000000000002%" id="mcps1.2.5.1.1"><p id="p39070558"><a name="p39070558"></a><a name="p39070558"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.2"><p id="p10598606"><a name="p10598606"></a><a name="p10598606"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.040000000000001%" id="mcps1.2.5.1.3"><p id="p795223417488"><a name="p795223417488"></a><a name="p795223417488"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.050000000000004%" id="mcps1.2.5.1.4"><p id="p53180767"><a name="p53180767"></a><a name="p53180767"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12674872"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p20031746"><a name="p20031746"></a><a name="p20031746"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p11958757"><a name="p11958757"></a><a name="p11958757"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.2.5.1.3 "><p id="p190787317482"><a name="p190787317482"></a><a name="p190787317482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.2.5.1.4 "><a name="ul16769054204218"></a><a name="ul16769054204218"></a><ul id="ul16769054204218"><li>Specifies the subnet name. </li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="row163965221710"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p1237219541173"><a name="p1237219541173"></a><a name="p1237219541173"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p1372154161713"><a name="p1372154161713"></a><a name="p1372154161713"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.2.5.1.3 "><p id="p837295491716"><a name="p837295491716"></a><a name="p837295491716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.2.5.1.4 "><a name="ul237215542179"></a><a name="ul237215542179"></a><ul id="ul237215542179"><li>Provides supplementary information about the subnet.</li><li>The value is a string of no more than 255 characters and cannot contain angle brackets (&lt; or &gt;).</li></ul>
    </td>
    </tr>
    <tr id="row33189039"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p3957675"><a name="p3957675"></a><a name="p3957675"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p52136226"><a name="p52136226"></a><a name="p52136226"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.2.5.1.3 "><p id="p2032001117482"><a name="p2032001117482"></a><a name="p2032001117482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.2.5.1.4 "><a name="ul4678105864210"></a><a name="ul4678105864210"></a><ul id="ul4678105864210"><li>Specifies the subnet CIDR block.</li><li>The value must be within the VPC CIDR block.</li><li>The value must be in CIDR format. The subnet mask cannot be greater than 28.</li></ul>
    </td>
    </tr>
    <tr id="row24692740"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p53954942"><a name="p53954942"></a><a name="p53954942"></a>gateway_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p8274172"><a name="p8274172"></a><a name="p8274172"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.2.5.1.3 "><p id="p3530821417482"><a name="p3530821417482"></a><a name="p3530821417482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.2.5.1.4 "><a name="ul1561512264319"></a><a name="ul1561512264319"></a><ul id="ul1561512264319"><li>Specifies the gateway of the subnet.</li><li>The value must be an IP address in the subnet.</li><li>The value must be a valid IP address.</li></ul>
    </td>
    </tr>
    <tr id="row60429346"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p62938818"><a name="p62938818"></a><a name="p62938818"></a>dhcp_enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p64879470"><a name="p64879470"></a><a name="p64879470"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.2.5.1.3 "><p id="p4139309817482"><a name="p4139309817482"></a><a name="p4139309817482"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.2.5.1.4 "><a name="ul18877710204319"></a><a name="ul18877710204319"></a><ul id="ul18877710204319"><li>Specifies whether DHCP is enabled for the subnet.</li><li>The value can be <strong>true</strong> (enabled) or <strong>false</strong> (disabled).</li><li>If this parameter is left blank, the system automatically sets it to <strong>true</strong> by default. If this parameter is set to <strong id="b842352706155749"><a name="b842352706155749"></a><a name="b842352706155749"></a>false</strong>, newly created ECSs cannot obtain IP addresses, and usernames and passwords cannot be injected using Cloud-init. Exercise caution when performing this operation.</li></ul>
    </td>
    </tr>
    <tr id="row10232270"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p23507505"><a name="p23507505"></a><a name="p23507505"></a>primary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p25059790"><a name="p25059790"></a><a name="p25059790"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.2.5.1.3 "><p id="p6450660517482"><a name="p6450660517482"></a><a name="p6450660517482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.2.5.1.4 "><a name="ul12206161414435"></a><a name="ul12206161414435"></a><ul id="ul12206161414435"><li>Specifies the IP address of DNS server 1 on the subnet.</li><li>The value must be a valid IP address. </li></ul>
    </td>
    </tr>
    <tr id="row45988614"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p34090260"><a name="p34090260"></a><a name="p34090260"></a>secondary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p9847715"><a name="p9847715"></a><a name="p9847715"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.2.5.1.3 "><p id="p5765255417482"><a name="p5765255417482"></a><a name="p5765255417482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.2.5.1.4 "><a name="ul59230186430"></a><a name="ul59230186430"></a><ul id="ul59230186430"><li>Specifies the IP address of DNS server 2 on the subnet.</li><li>The value must be a valid IP address. </li></ul>
    </td>
    </tr>
    <tr id="row1596910210505"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p1842890810505"><a name="p1842890810505"></a><a name="p1842890810505"></a>dnsList</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p1634655410505"><a name="p1634655410505"></a><a name="p1634655410505"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.2.5.1.3 "><p id="p16634345155517"><a name="p16634345155517"></a><a name="p16634345155517"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.2.5.1.4 "><a name="ul32521424144310"></a><a name="ul32521424144310"></a><ul id="ul32521424144310"><li>Specifies the DNS server address list of a subnet. This field is required if you need to use more than two DNS servers.</li><li>This parameter value is the superset of both DNS server address 1 and DNS server address 2. IPv6 addresses are not supported.</li></ul>
    </td>
    </tr>
    <tr id="row66578044"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p24112512"><a name="p24112512"></a><a name="p24112512"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p6956456"><a name="p6956456"></a><a name="p6956456"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.2.5.1.3 "><p id="p3934528717482"><a name="p3934528717482"></a><a name="p3934528717482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.2.5.1.4 "><a name="ul14409122710438"></a><a name="ul14409122710438"></a><ul id="ul14409122710438"><li>Identifies the AZ to which the subnet belongs.</li><li>The value must be an existing AZ in the system.</li></ul>
    </td>
    </tr>
    <tr id="row53182860"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p12844374"><a name="p12844374"></a><a name="p12844374"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p33761356"><a name="p33761356"></a><a name="p33761356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.2.5.1.3 "><p id="p3285166017482"><a name="p3285166017482"></a><a name="p3285166017482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.2.5.1.4 "><p id="p50315352"><a name="p50315352"></a><a name="p50315352"></a>Specifies the ID of the VPC to which the subnet belongs.</p>
    </td>
    </tr>
    <tr id="row13029301879"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.1 "><p id="p8303103018715"><a name="p8303103018715"></a><a name="p8303103018715"></a>extra_dhcp_opts</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p1030320304714"><a name="p1030320304714"></a><a name="p1030320304714"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.2.5.1.3 "><p id="p8303730570"><a name="p8303730570"></a><a name="p8303730570"></a>Array of <a href="#table1805181451016">extra_dhcp_opt</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.050000000000004%" headers="mcps1.2.5.1.4 "><p id="p130310301176"><a name="p130310301176"></a><a name="p130310301176"></a>Specifies the NTP server address configured for the subnet. For details, see the <strong id="b1787145816910"><a name="b1787145816910"></a><a name="b1787145816910"></a>extra_dhcp_opt</strong> object <a href="#table1805181451016">extra_dhcp_opt objects</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **extra\_dhcp\_opt**  object

    <a name="table1805181451016"></a>
    <table><thead align="left"><tr id="row1806141418109"><th class="cellrowborder" valign="top" width="21.740000000000002%" id="mcps1.2.5.1.1"><p id="p1948182811017"><a name="p1948182811017"></a><a name="p1948182811017"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.17%" id="mcps1.2.5.1.2"><p id="p19515288107"><a name="p19515288107"></a><a name="p19515288107"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.619999999999997%" id="mcps1.2.5.1.3"><p id="p755202861014"><a name="p755202861014"></a><a name="p755202861014"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.47%" id="mcps1.2.5.1.4"><p id="p66018281105"><a name="p66018281105"></a><a name="p66018281105"></a><strong id="b1716215324573"><a name="b1716215324573"></a><a name="b1716215324573"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19806161420105"><td class="cellrowborder" valign="top" width="21.740000000000002%" headers="mcps1.2.5.1.1 "><p id="p1834323611017"><a name="p1834323611017"></a><a name="p1834323611017"></a>opt_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.2.5.1.2 "><p id="p1034310368108"><a name="p1034310368108"></a><a name="p1034310368108"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.619999999999997%" headers="mcps1.2.5.1.3 "><p id="p15343163651014"><a name="p15343163651014"></a><a name="p15343163651014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.47%" headers="mcps1.2.5.1.4 "><a name="ul1734314363102"></a><a name="ul1734314363102"></a><ul id="ul1734314363102"><li>Specifies the NTP server address configured for the subnet.</li><li>Constraints:<p id="p1984274292214"><a name="p1984274292214"></a><a name="p1984274292214"></a>The option <strong id="b18312174218176"><a name="b18312174218176"></a><a name="b18312174218176"></a>ntp</strong> for <strong id="b2456833191713"><a name="b2456833191713"></a><a name="b2456833191713"></a>opt_name</strong> indicates the NTP server configured for the subnet. Currently, only IPv4 addresses are supported. A maximum of four IP addresses can be configured, and each address must be unique. Multiple IP addresses must be separated using commas (,). The option <strong id="b1973813315213"><a name="b1973813315213"></a><a name="b1973813315213"></a>null</strong> for <strong id="b9368121819213"><a name="b9368121819213"></a><a name="b9368121819213"></a>opt_name</strong> indicates that no NTP server is configured for the subnet. The parameter value cannot be an empty string.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row48061714191011"><td class="cellrowborder" valign="top" width="21.740000000000002%" headers="mcps1.2.5.1.1 "><p id="p33437363104"><a name="p33437363104"></a><a name="p33437363104"></a>opt_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.2.5.1.2 "><p id="p1634393613106"><a name="p1634393613106"></a><a name="p1634393613106"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.619999999999997%" headers="mcps1.2.5.1.3 "><p id="p14343113613104"><a name="p14343113613104"></a><a name="p14343113613104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.47%" headers="mcps1.2.5.1.4 "><a name="ul1934353641010"></a><a name="ul1934353641010"></a><ul id="ul1934353641010"><li>Specifies the NTP server address name configured for the subnet.</li><li>Currently, the value can only be set to <strong id="b185618261310"><a name="b185618261310"></a><a name="b185618261310"></a>ntp</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{Endpoint}/v1/{project_id}/subnets
    
    {
        "subnet": {
            "name": "subnet",
            "description": "",
            "cidr": "192.168.20.0/24",
            "gateway_ip": "192.168.20.1",
            "dhcp_enable": true,
            "primary_dns": "114.xx.xx.114",
            "secondary_dns": "114.xx.xx.115",
            "dnsList": [
                "114.xx.xx.114",
                "114.xx.xx.115"
            ],
            "availability_zone": "aa-bb-cc",//For example, the AZ is aa-bb-cc.
            "vpc_id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85",
            "extra_dhcp_opts": [
                {
                    "opt_value": "10.100.0.33,10.100.0.34",
                    "opt_name": "ntp"
                }
            ]
        }
    }
    ```


## Response Message<a name="section51595365"></a>

-   Response parameter

    **Table  5**  Response parameter

    <a name="table3201287115737"></a>
    <table><thead align="left"><tr id="row4941460315737"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p4315992415737"><a name="p4315992415737"></a><a name="p4315992415737"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p3996487815737"><a name="p3996487815737"></a><a name="p3996487815737"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="p1592968015737"><a name="p1592968015737"></a><a name="p1592968015737"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1523569015737"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p2613139715737"><a name="p2613139715737"></a><a name="p2613139715737"></a>subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p5206127615737"><a name="p5206127615737"></a><a name="p5206127615737"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="p3616274015737"><a name="p3616274015737"></a><a name="p3616274015737"></a>Specifies the <a href="#table54041329">subnet objects</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **subnet**  objects

    <a name="table54041329"></a>
    <table><thead align="left"><tr id="row3088388"><th class="cellrowborder" valign="top" width="28.860000000000003%" id="mcps1.2.4.1.1"><p id="p48832851"><a name="p48832851"></a><a name="p48832851"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.25%" id="mcps1.2.4.1.2"><p id="p31305988175034"><a name="p31305988175034"></a><a name="p31305988175034"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.89%" id="mcps1.2.4.1.3"><p id="p14620943"><a name="p14620943"></a><a name="p14620943"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43445707"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p29441404"><a name="p29441404"></a><a name="p29441404"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p52757101175034"><a name="p52757101175034"></a><a name="p52757101175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><p id="p25747420"><a name="p25747420"></a><a name="p25747420"></a>Specifies the resource identifier in the form of UUID.</p>
    </td>
    </tr>
    <tr id="row30400195"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p46496694"><a name="p46496694"></a><a name="p46496694"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p45466823175034"><a name="p45466823175034"></a><a name="p45466823175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><a name="ul23311559134110"></a><a name="ul23311559134110"></a><ul id="ul23311559134110"><li>Specifies the subnet name. </li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="row558919286262"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p71821430112615"><a name="p71821430112615"></a><a name="p71821430112615"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p4182153010268"><a name="p4182153010268"></a><a name="p4182153010268"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><a name="ul183161512131417"></a><a name="ul183161512131417"></a><ul id="ul183161512131417"><li>Provides supplementary information about the subnet.</li><li>The value is a string of no more than 255 characters and cannot contain angle brackets (&lt; or &gt;).</li></ul>
    </td>
    </tr>
    <tr id="row51945267"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p46817064"><a name="p46817064"></a><a name="p46817064"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p58934074175034"><a name="p58934074175034"></a><a name="p58934074175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><a name="ul899517162424"></a><a name="ul899517162424"></a><ul id="ul899517162424"><li>Specifies the subnet CIDR block.</li><li>The value must be within the VPC CIDR block.</li><li>The value must be in CIDR format. The subnet mask cannot be greater than 28.</li></ul>
    </td>
    </tr>
    <tr id="row39696553"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p61304253"><a name="p61304253"></a><a name="p61304253"></a>gateway_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p8930669175034"><a name="p8930669175034"></a><a name="p8930669175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><a name="ul1526163074211"></a><a name="ul1526163074211"></a><ul id="ul1526163074211"><li>Specifies the gateway of the subnet.</li><li>The value must be an IP address in the subnet.</li><li>The value must be a valid IP address.</li></ul>
    </td>
    </tr>
    <tr id="row4606985"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p37621475"><a name="p37621475"></a><a name="p37621475"></a>dhcp_enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p52295560175034"><a name="p52295560175034"></a><a name="p52295560175034"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><p id="p29849008175159"><a name="p29849008175159"></a><a name="p29849008175159"></a>Specifies whether the DHCP function is enabled for the subnet.</p>
    </td>
    </tr>
    <tr id="row1048160"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p17792110"><a name="p17792110"></a><a name="p17792110"></a>primary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p8081972175034"><a name="p8081972175034"></a><a name="p8081972175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><p id="p19162058"><a name="p19162058"></a><a name="p19162058"></a>Specifies the IP address of DNS server 1 on the subnet.</p>
    </td>
    </tr>
    <tr id="row8622890"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p27365507"><a name="p27365507"></a><a name="p27365507"></a>secondary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p50659992175034"><a name="p50659992175034"></a><a name="p50659992175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><p id="p58602024"><a name="p58602024"></a><a name="p58602024"></a>Specifies the IP address of DNS server 2 on the subnet.</p>
    </td>
    </tr>
    <tr id="row29925916105649"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p8080156105649"><a name="p8080156105649"></a><a name="p8080156105649"></a>dnsList</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p9490145416555"><a name="p9490145416555"></a><a name="p9490145416555"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><p id="p31678735105649"><a name="p31678735105649"></a><a name="p31678735105649"></a>Specifies the IP address list of DNS servers on the subnet.</p>
    </td>
    </tr>
    <tr id="row49143529"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p21202951"><a name="p21202951"></a><a name="p21202951"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p9818717175034"><a name="p9818717175034"></a><a name="p9818717175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><p id="p44463652175257"><a name="p44463652175257"></a><a name="p44463652175257"></a>Identifies the AZ to which the subnet belongs.</p>
    </td>
    </tr>
    <tr id="row15677883"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p61948991"><a name="p61948991"></a><a name="p61948991"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p57118635175034"><a name="p57118635175034"></a><a name="p57118635175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><p id="p36052245"><a name="p36052245"></a><a name="p36052245"></a>Specifies the ID of the VPC to which the subnet belongs.</p>
    </td>
    </tr>
    <tr id="row34550710"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p47144157"><a name="p47144157"></a><a name="p47144157"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p63206697175034"><a name="p63206697175034"></a><a name="p63206697175034"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><a name="ul756817571315"></a><a name="ul756817571315"></a><ul id="ul756817571315"><li>Specifies the status of the subnet.</li><li>The value can be <strong>ACTIVE</strong>, <strong>UNKNOWN</strong>, or <strong>ERROR</strong>.<a name="ul83391032184614"></a><a name="ul83391032184614"></a><ul id="ul83391032184614"><li><strong id="b252312334119"><a name="b252312334119"></a><a name="b252312334119"></a>ACTIVE</strong>: indicates that the subnet has been associated with the router.</li><li><strong id="b842352706151633"><a name="b842352706151633"></a><a name="b842352706151633"></a>UNKNOWN</strong>: indicates that the subnet has not been associated with the router.</li><li><strong id="b842352706151734"><a name="b842352706151734"></a><a name="b842352706151734"></a>ERROR</strong>: indicates that the subnet is abnormal.</li></ul>
    </li><li>The system creates a subnet and then associates the subnet with the router in the threads.<p id="p149484964617"><a name="p149484964617"></a><a name="p149484964617"></a>In the concurrent scenario, if the CIDR of the created subnet is the same as that of an existing subnet, the created subnet fails to attach to the router after underlying system verification. As a result, the subnet creation fails.</p>
    <p id="p116091753134614"><a name="p116091753134614"></a><a name="p116091753134614"></a>In this scenario, the returned value of <strong id="b842352706172823"><a name="b842352706172823"></a><a name="b842352706172823"></a>status</strong> is <strong id="b842352706172828"><a name="b842352706172828"></a><a name="b842352706172828"></a>UNKNOWN</strong>.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row3884489103221"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p34960403103221"><a name="p34960403103221"></a><a name="p34960403103221"></a>neutron_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p64221241103221"><a name="p64221241103221"></a><a name="p64221241103221"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><p id="p34538004103221"><a name="p34538004103221"></a><a name="p34538004103221"></a>Specifies the ID of the corresponding network (OpenStack Neutron API).</p>
    </td>
    </tr>
    <tr id="row5205001104010"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p18951959104010"><a name="p18951959104010"></a><a name="p18951959104010"></a>neutron_subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p58188011104010"><a name="p58188011104010"></a><a name="p58188011104010"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><p id="p15608450104010"><a name="p15608450104010"></a><a name="p15608450104010"></a>Specifies the ID of the corresponding subnet (OpenStack Neutron API).</p>
    </td>
    </tr>
    <tr id="row179381878268"><td class="cellrowborder" valign="top" width="28.860000000000003%" headers="mcps1.2.4.1.1 "><p id="p5714303263"><a name="p5714303263"></a><a name="p5714303263"></a>extra_dhcp_opts</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.2 "><p id="p01223042610"><a name="p01223042610"></a><a name="p01223042610"></a>Array of <a href="#table019517383270">extra_dhcp_opt</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.89%" headers="mcps1.2.4.1.3 "><p id="p41825339261"><a name="p41825339261"></a><a name="p41825339261"></a>Specifies the NTP server address configured for the subnet. For details, see <a href="#table019517383270">Table 7</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **extra\_dhcp\_opt**  object

    <a name="table019517383270"></a>
    <table><thead align="left"><tr id="vpc_subnet01_0001_row1806141418109"><th class="cellrowborder" valign="top" width="21.740000000000002%" id="mcps1.2.5.1.1"><p id="vpc_subnet01_0001_p1948182811017"><a name="vpc_subnet01_0001_p1948182811017"></a><a name="vpc_subnet01_0001_p1948182811017"></a><strong id="vpc_subnet01_0001_b842352706195711"><a name="vpc_subnet01_0001_b842352706195711"></a><a name="vpc_subnet01_0001_b842352706195711"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.17%" id="mcps1.2.5.1.2"><p id="vpc_subnet01_0001_p19515288107"><a name="vpc_subnet01_0001_p19515288107"></a><a name="vpc_subnet01_0001_p19515288107"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.619999999999997%" id="mcps1.2.5.1.3"><p id="vpc_subnet01_0001_p755202861014"><a name="vpc_subnet01_0001_p755202861014"></a><a name="vpc_subnet01_0001_p755202861014"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.47%" id="mcps1.2.5.1.4"><p id="vpc_subnet01_0001_p66018281105"><a name="vpc_subnet01_0001_p66018281105"></a><a name="vpc_subnet01_0001_p66018281105"></a><strong id="vpc_subnet01_0001_b1716215324573"><a name="vpc_subnet01_0001_b1716215324573"></a><a name="vpc_subnet01_0001_b1716215324573"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpc_subnet01_0001_row19806161420105"><td class="cellrowborder" valign="top" width="21.740000000000002%" headers="mcps1.2.5.1.1 "><p id="vpc_subnet01_0001_p1834323611017"><a name="vpc_subnet01_0001_p1834323611017"></a><a name="vpc_subnet01_0001_p1834323611017"></a>opt_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.2.5.1.2 "><p id="vpc_subnet01_0001_p1034310368108"><a name="vpc_subnet01_0001_p1034310368108"></a><a name="vpc_subnet01_0001_p1034310368108"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.619999999999997%" headers="mcps1.2.5.1.3 "><p id="vpc_subnet01_0001_p15343163651014"><a name="vpc_subnet01_0001_p15343163651014"></a><a name="vpc_subnet01_0001_p15343163651014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.47%" headers="mcps1.2.5.1.4 "><a name="vpc_subnet01_0001_ul1734314363102"></a><a name="vpc_subnet01_0001_ul1734314363102"></a><ul id="vpc_subnet01_0001_ul1734314363102"><li>Specifies the NTP server address configured for the subnet.</li><li>Constraints:<p id="vpc_subnet01_0001_p1984274292214"><a name="vpc_subnet01_0001_p1984274292214"></a><a name="vpc_subnet01_0001_p1984274292214"></a>The option <strong id="vpc_subnet01_0001_b18312174218176"><a name="vpc_subnet01_0001_b18312174218176"></a><a name="vpc_subnet01_0001_b18312174218176"></a>ntp</strong> for <strong id="vpc_subnet01_0001_b2456833191713"><a name="vpc_subnet01_0001_b2456833191713"></a><a name="vpc_subnet01_0001_b2456833191713"></a>opt_name</strong> indicates the NTP server configured for the subnet. Currently, only IPv4 addresses are supported. A maximum of four IP addresses can be configured, and each address must be unique. Multiple IP addresses must be separated using commas (,). The option <strong id="vpc_subnet01_0001_b1973813315213"><a name="vpc_subnet01_0001_b1973813315213"></a><a name="vpc_subnet01_0001_b1973813315213"></a>null</strong> for <strong id="vpc_subnet01_0001_b9368121819213"><a name="vpc_subnet01_0001_b9368121819213"></a><a name="vpc_subnet01_0001_b9368121819213"></a>opt_name</strong> indicates that no NTP server is configured for the subnet. The parameter value cannot be an empty string.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="vpc_subnet01_0001_row48061714191011"><td class="cellrowborder" valign="top" width="21.740000000000002%" headers="mcps1.2.5.1.1 "><p id="vpc_subnet01_0001_p33437363104"><a name="vpc_subnet01_0001_p33437363104"></a><a name="vpc_subnet01_0001_p33437363104"></a>opt_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.2.5.1.2 "><p id="vpc_subnet01_0001_p1634393613106"><a name="vpc_subnet01_0001_p1634393613106"></a><a name="vpc_subnet01_0001_p1634393613106"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.619999999999997%" headers="mcps1.2.5.1.3 "><p id="vpc_subnet01_0001_p14343113613104"><a name="vpc_subnet01_0001_p14343113613104"></a><a name="vpc_subnet01_0001_p14343113613104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.47%" headers="mcps1.2.5.1.4 "><a name="vpc_subnet01_0001_ul1934353641010"></a><a name="vpc_subnet01_0001_ul1934353641010"></a><ul id="vpc_subnet01_0001_ul1934353641010"><li>Specifies the NTP server address name configured for the subnet.</li><li>Currently, the value can only be set to <strong id="vpc_subnet01_0001_b185618261310"><a name="vpc_subnet01_0001_b185618261310"></a><a name="vpc_subnet01_0001_b185618261310"></a>ntp</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "subnet": {
            "id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
            "name": "subnet",
            "description": "",
            "cidr": "192.168.20.0/24",
            "dnsList": [
                "114.xx.xx.114",
                "1114.xx.xx.115"
            ],
            "status": "UNKNOWN",
            "vpc_id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85",
            "gateway_ip": "192.168.20.1",
            "dhcp_enable": true,
            "primary_dns": "114.xx.xx.114",
            "secondary_dns": "114.xx.xx.115",
            "availability_zone": "aa-bb-cc",//For example, the AZ is aa-bb-cc.
            "neutron_network_id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
            "neutron_subnet_id": "213cb9d-3122-2ac1-1a29-91ffc1231a12"
            "extra_dhcp_opts": [
                {
                    "opt_value": "10.100.0.33,10.100.0.34",
                    "opt_name": "ntp"
                }
            ]
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

