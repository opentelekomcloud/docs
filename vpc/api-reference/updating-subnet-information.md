# Updating Subnet Information<a name="vpc_subnet01_0004"></a>

## Function<a name="section52667802"></a>

This API is used to update information about a subnet.

## URI<a name="section4248175"></a>

PUT /v1/\{project\_id\}/vpcs/\{vpc\_id\}/subnets/\{subnet\_id\}

[Table 1](#table27806533)  describes the parameters.

**Table  1**  Parameter description

<a name="table27806533"></a>
<table><thead align="left"><tr id="row25717600"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p2750866"><a name="p2750866"></a><a name="p2750866"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p21493617"><a name="p21493617"></a><a name="p21493617"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p63261412"><a name="p63261412"></a><a name="p63261412"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row23900756"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p56913064"><a name="p56913064"></a><a name="p56913064"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p46555465"><a name="p46555465"></a><a name="p46555465"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row41240337122055"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p52133024122055"><a name="p52133024122055"></a><a name="p52133024122055"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4532040312214"><a name="p4532040312214"></a><a name="p4532040312214"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p58002403122055"><a name="p58002403122055"></a><a name="p58002403122055"></a>Specifies the VPC ID of the subnet.</p>
</td>
</tr>
<tr id="row48957711"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6151694"><a name="p6151694"></a><a name="p6151694"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p28525238"><a name="p28525238"></a><a name="p28525238"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p28842926"><a name="p28842926"></a><a name="p28842926"></a>Specifies the subnet ID, which uniquely identifies the subnet.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section38233575"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table42592295151022"></a>
    <table><thead align="left"><tr id="row13964015151022"><th class="cellrowborder" valign="top" width="12.4%" id="mcps1.2.5.1.1"><p id="p57343407151022"><a name="p57343407151022"></a><a name="p57343407151022"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.990000000000002%" id="mcps1.2.5.1.2"><p id="p14304400151022"><a name="p14304400151022"></a><a name="p14304400151022"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.3"><p id="p17805753151022"><a name="p17805753151022"></a><a name="p17805753151022"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.18%" id="mcps1.2.5.1.4"><p id="p32979923151022"><a name="p32979923151022"></a><a name="p32979923151022"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54128134151022"><td class="cellrowborder" valign="top" width="12.4%" headers="mcps1.2.5.1.1 "><p id="p22302713151022"><a name="p22302713151022"></a><a name="p22302713151022"></a>subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.2.5.1.2 "><p id="p61689300151022"><a name="p61689300151022"></a><a name="p61689300151022"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.3 "><p id="p30777408151022"><a name="p30777408151022"></a><a name="p30777408151022"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="p22370187151022"><a name="p22370187151022"></a><a name="p22370187151022"></a>Specifies the <a href="#table45027976">subnet objects</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **subnet**  objects

    <a name="table45027976"></a>
    <table><thead align="left"><tr id="row34359256"><th class="cellrowborder" valign="top" width="20.862086208620862%" id="mcps1.2.5.1.1"><p id="p31636323"><a name="p31636323"></a><a name="p31636323"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.11201120112011%" id="mcps1.2.5.1.2"><p id="p12405375"><a name="p12405375"></a><a name="p12405375"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.661466146614663%" id="mcps1.2.5.1.3"><p id="p3774167175923"><a name="p3774167175923"></a><a name="p3774167175923"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.364436443644365%" id="mcps1.2.5.1.4"><p id="p65311315"><a name="p65311315"></a><a name="p65311315"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55725192"><td class="cellrowborder" valign="top" width="20.862086208620862%" headers="mcps1.2.5.1.1 "><p id="p17446726"><a name="p17446726"></a><a name="p17446726"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.5.1.2 "><p id="p3898676"><a name="p3898676"></a><a name="p3898676"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.661466146614663%" headers="mcps1.2.5.1.3 "><p id="p37272111175923"><a name="p37272111175923"></a><a name="p37272111175923"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.364436443644365%" headers="mcps1.2.5.1.4 "><a name="ul4675135413562"></a><a name="ul4675135413562"></a><ul id="ul4675135413562"><li>Specifies the subnet name. </li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="row767394553412"><td class="cellrowborder" valign="top" width="20.862086208620862%" headers="mcps1.2.5.1.1 "><p id="p1867344711345"><a name="p1867344711345"></a><a name="p1867344711345"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.5.1.2 "><p id="p5673647103420"><a name="p5673647103420"></a><a name="p5673647103420"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.661466146614663%" headers="mcps1.2.5.1.3 "><p id="p7673164711348"><a name="p7673164711348"></a><a name="p7673164711348"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.364436443644365%" headers="mcps1.2.5.1.4 "><a name="ul196739477344"></a><a name="ul196739477344"></a><ul id="ul196739477344"><li>Provides supplementary information about the subnet.</li><li>The value is a string of no more than 255 characters and cannot contain angle brackets (&lt; or &gt;).</li></ul>
    </td>
    </tr>
    <tr id="row64356400"><td class="cellrowborder" valign="top" width="20.862086208620862%" headers="mcps1.2.5.1.1 "><p id="p45485936"><a name="p45485936"></a><a name="p45485936"></a>dhcp_enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.5.1.2 "><p id="p60482217"><a name="p60482217"></a><a name="p60482217"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.661466146614663%" headers="mcps1.2.5.1.3 "><p id="p66251028175923"><a name="p66251028175923"></a><a name="p66251028175923"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.364436443644365%" headers="mcps1.2.5.1.4 "><a name="ul16629112175711"></a><a name="ul16629112175711"></a><ul id="ul16629112175711"><li>Specifies whether DHCP is enabled for the subnet.</li><li>The value can be <strong>true</strong> (enabled) or <strong>false</strong> (disabled).</li><li>If this parameter is left blank, the system automatically sets it to <strong>true</strong> by default. If this parameter is set to <strong id="b842352706155749"><a name="b842352706155749"></a><a name="b842352706155749"></a>false</strong>, newly created ECSs cannot obtain IP addresses, and usernames and passwords cannot be injected using Cloud-init. Exercise caution when performing this operation.</li></ul>
    </td>
    </tr>
    <tr id="row62687"><td class="cellrowborder" valign="top" width="20.862086208620862%" headers="mcps1.2.5.1.1 "><p id="p5077725"><a name="p5077725"></a><a name="p5077725"></a>primary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.5.1.2 "><p id="p8642591"><a name="p8642591"></a><a name="p8642591"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.661466146614663%" headers="mcps1.2.5.1.3 "><p id="p1069020123190"><a name="p1069020123190"></a><a name="p1069020123190"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.364436443644365%" headers="mcps1.2.5.1.4 "><a name="ul192812028185718"></a><a name="ul192812028185718"></a><ul id="ul192812028185718"><li>Specifies the IP address of DNS server 1 on the subnet.</li><li>The value must be a valid IP address. </li></ul>
    </td>
    </tr>
    <tr id="row40600350"><td class="cellrowborder" valign="top" width="20.862086208620862%" headers="mcps1.2.5.1.1 "><p id="p294043"><a name="p294043"></a><a name="p294043"></a>secondary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.5.1.2 "><p id="p23817504"><a name="p23817504"></a><a name="p23817504"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.661466146614663%" headers="mcps1.2.5.1.3 "><p id="p8884643175923"><a name="p8884643175923"></a><a name="p8884643175923"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.364436443644365%" headers="mcps1.2.5.1.4 "><a name="ul8801931105718"></a><a name="ul8801931105718"></a><ul id="ul8801931105718"><li>Specifies the IP address of DNS server 2 on the subnet.</li><li>The value must be a valid IP address. </li></ul>
    </td>
    </tr>
    <tr id="row4104651911530"><td class="cellrowborder" valign="top" width="20.862086208620862%" headers="mcps1.2.5.1.1 "><p id="p3643375711530"><a name="p3643375711530"></a><a name="p3643375711530"></a>dnsList</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.5.1.2 "><p id="p787474711538"><a name="p787474711538"></a><a name="p787474711538"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.661466146614663%" headers="mcps1.2.5.1.3 "><p id="p10991411530"><a name="p10991411530"></a><a name="p10991411530"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.364436443644365%" headers="mcps1.2.5.1.4 "><a name="ul101991551584"></a><a name="ul101991551584"></a><ul id="ul101991551584"><li>Specifies the DNS server address list of a subnet. This field is required if you need to use more than two DNS servers.</li><li>This parameter value is the superset of both DNS server address 1 and DNS server address 2. </li></ul>
    </td>
    </tr>
    <tr id="row2025452963714"><td class="cellrowborder" valign="top" width="20.862086208620862%" headers="mcps1.2.5.1.1 "><p id="p5714303263"><a name="p5714303263"></a><a name="p5714303263"></a>extra_dhcp_opts</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.5.1.2 "><p id="p01223042610"><a name="p01223042610"></a><a name="p01223042610"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.661466146614663%" headers="mcps1.2.5.1.3 "><p id="p111573015263"><a name="p111573015263"></a><a name="p111573015263"></a>Array of <a href="#table019517383270">extra_dhcp_opt</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.364436443644365%" headers="mcps1.2.5.1.4 "><p id="p52547295374"><a name="p52547295374"></a><a name="p52547295374"></a>Specifies the NTP server address configured for the subnet. For details, see the <a href="#table019517383270">extra_dhcp_opt object</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **extra\_dhcp\_opt**  object

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


-   Example request

    ```
    PUT https://{Endpoint}/v1/{project_id}/vpcs/{vpc_id}/subnets/4779ab1c-7c1a-44b1-a02e-93dfc361b32d
    
    {
        "subnet": {
            "name": "subnetqq",
            "dhcp_enable": false,
            "primary_dns": "114.xx.xx.115",
            "secondary_dns": "114.xx.xx.116",
            "extra_dhcp_opts": [
                {
                    "opt_value": "10.100.0.33,10.100.0.34",
                    "opt_name": "ntp"
                }
            ]
        }
    }
    
    ```


## Response Message<a name="section8557861"></a>

-   Response parameter

    **Table  5**  Response parameter

    <a name="table55739938151015"></a>
    <table><thead align="left"><tr id="row19341165151015"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p23130572151015"><a name="p23130572151015"></a><a name="p23130572151015"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p26547244151015"><a name="p26547244151015"></a><a name="p26547244151015"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="p2843132151015"><a name="p2843132151015"></a><a name="p2843132151015"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28967149151015"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p64637734151015"><a name="p64637734151015"></a><a name="p64637734151015"></a>subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p27267219151015"><a name="p27267219151015"></a><a name="p27267219151015"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="p13579079151015"><a name="p13579079151015"></a><a name="p13579079151015"></a>Specifies the <strong id="b74871128114815"><a name="b74871128114815"></a><a name="b74871128114815"></a>subnet</strong> objects.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **subnet**  objects

    <a name="table1210700"></a>
    <table><thead align="left"><tr id="row43388973"><th class="cellrowborder" valign="top" width="24.57%" id="mcps1.2.4.1.1"><p id="p24845910"><a name="p24845910"></a><a name="p24845910"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.68%" id="mcps1.2.4.1.2"><p id="p697309418033"><a name="p697309418033"></a><a name="p697309418033"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.74999999999999%" id="mcps1.2.4.1.3"><p id="p6587942"><a name="p6587942"></a><a name="p6587942"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63861276"><td class="cellrowborder" valign="top" width="24.57%" headers="mcps1.2.4.1.1 "><p id="p5380904"><a name="p5380904"></a><a name="p5380904"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.68%" headers="mcps1.2.4.1.2 "><p id="p2794974018033"><a name="p2794974018033"></a><a name="p2794974018033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.74999999999999%" headers="mcps1.2.4.1.3 "><p id="p4849307"><a name="p4849307"></a><a name="p4849307"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row43643771"><td class="cellrowborder" valign="top" width="24.57%" headers="mcps1.2.4.1.1 "><p id="p45484537"><a name="p45484537"></a><a name="p45484537"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.68%" headers="mcps1.2.4.1.2 "><p id="p4933643818033"><a name="p4933643818033"></a><a name="p4933643818033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.74999999999999%" headers="mcps1.2.4.1.3 "><a name="ul756817571315"></a><a name="ul756817571315"></a><ul id="ul756817571315"><li>Specifies the status of the subnet.</li><li>The value can be <strong>ACTIVE</strong>, <strong>UNKNOWN</strong>, or <strong>ERROR</strong>.<a name="ul83391032184614"></a><a name="ul83391032184614"></a><ul id="ul83391032184614"><li><strong>ACTIVE</strong>: indicates that the subnet has been associated with the router.</li><li><strong id="b842352706151633"><a name="b842352706151633"></a><a name="b842352706151633"></a>UNKNOWN</strong>: indicates that the subnet has not been associated with the router.</li><li><strong id="b842352706151734"><a name="b842352706151734"></a><a name="b842352706151734"></a>ERROR</strong>: indicates that the subnet is abnormal.</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "subnet": {
            "id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
            "status": "ACTIVE"
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

