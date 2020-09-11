# Creating a VPC Endpoint<a name="vpcep_06_0303"></a>

## Function<a name="section43389233"></a>

This API is used to create a VPC endpoint for accessing a VPC endpoint service.

## URI<a name="section54958778"></a>

POST /v1/\{project\_id\}/vpc-endpoints

[Table 1](#table40572397)  describes the required parameters.

**Table  1**  Parameters

<a name="table40572397"></a>
<table><thead align="left"><tr id="row57566450"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p32370843"><a name="p32370843"></a><a name="p32370843"></a><strong id="b193009351313"><a name="b193009351313"></a><a name="b193009351313"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p4792588"><a name="p4792588"></a><a name="p4792588"></a><strong id="b205942361039"><a name="b205942361039"></a><a name="b205942361039"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p52655342"><a name="p52655342"></a><a name="p52655342"></a><strong id="b196929379312"><a name="b196929379312"></a><a name="b196929379312"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row37224296"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p62378019"><a name="p62378019"></a><a name="p62378019"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p19454791"><a name="p19454791"></a><a name="p19454791"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p32334202"><a name="p32334202"></a><a name="p32334202"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section24866956"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table29607260"></a>
    <table><thead align="left"><tr id="row33522038"><th class="cellrowborder" valign="top" width="20.407959204079592%" id="mcps1.2.5.1.1"><p id="p30930573"><a name="p30930573"></a><a name="p30930573"></a><strong id="b590964517320"><a name="b590964517320"></a><a name="b590964517320"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.36816318368163%" id="mcps1.2.5.1.2"><p id="p22348513"><a name="p22348513"></a><a name="p22348513"></a><strong id="b1991327773"><a name="b1991327773"></a><a name="b1991327773"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p65399129"><a name="p65399129"></a><a name="p65399129"></a><strong id="b159017488317"><a name="b159017488317"></a><a name="b159017488317"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.89551044895511%" id="mcps1.2.5.1.4"><p id="p62838110"><a name="p62838110"></a><a name="p62838110"></a><strong id="b1348463598"><a name="b1348463598"></a><a name="b1348463598"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56722135"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.2.5.1.1 "><p id="p31090221"><a name="p31090221"></a><a name="p31090221"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p35279943"><a name="p35279943"></a><a name="p35279943"></a>No</p>
    <div class="note" id="note26594588243"><a name="note26594588243"></a><a name="note26594588243"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p466016583249"><a name="p466016583249"></a><a name="p466016583249"></a>This parameter is mandatory to create an interface VPC endpoint.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p39103117"><a name="p39103117"></a><a name="p39103117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p244375111217"><a name="p244375111217"></a><a name="p244375111217"></a>The value must be the ID of the subnet created in the VPC specified by <strong id="b8191945122110"><a name="b8191945122110"></a><a name="b8191945122110"></a>vpc_id</strong> and in the format of the UUID.</p>
    <p id="p418516465816"><a name="p418516465816"></a><a name="p418516465816"></a>For details, see response field <strong id="b16931153814488"><a name="b16931153814488"></a><a name="b16931153814488"></a>id</strong> in <a href="https://docs.otc.t-systems.com/api/vpc/vpc_subnet01_0002.html" target="_blank" rel="noopener noreferrer">Querying Subnet Details</a> in the <em id="i1593243818487"><a name="i1593243818487"></a><a name="i1593243818487"></a>Virtual Private Cloud API Reference</em>.</p>
    <p id="p357318621418"><a name="p357318621418"></a><a name="p357318621418"></a>This parameter is mandatory only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    <div class="note" id="note1510244415810"><a name="note1510244415810"></a><a name="note1510244415810"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul114411483253"></a><a name="ul114411483253"></a><ul id="ul114411483253"><li>The CIDR block of the VPC subnet cannot overlap with 198.19.128.0/20.</li><li>The destination address of the custom route in the VPC route table cannot overlap with the CIDR block 198.19.128.0/20.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row52014641"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.2.5.1.1 "><p id="p52436422"><a name="p52436422"></a><a name="p52436422"></a>endpoint_service_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p19491812"><a name="p19491812"></a><a name="p19491812"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p35332914"><a name="p35332914"></a><a name="p35332914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p43393752"><a name="p43393752"></a><a name="p43393752"></a>Specifies the ID of the VPC endpoint service.</p>
    <p id="p3352101421816"><a name="p3352101421816"></a><a name="p3352101421816"></a>You can obtain the ID of the VPC endpoint service to be connected by performing operations in <a href="querying-basic-information-of-a-vpc-endpoint-service.md">Querying Basic Information of a VPC Endpoint Service</a>.</p>
    </td>
    </tr>
    <tr id="row54999452"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.2.5.1.1 "><p id="p25770618"><a name="p25770618"></a><a name="p25770618"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p7045317"><a name="p7045317"></a><a name="p7045317"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p33799780"><a name="p33799780"></a><a name="p33799780"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p53427648"><a name="p53427648"></a><a name="p53427648"></a>Specifies the ID of the VPC where the VPC endpoint is to be created.</p>
    <p id="p59954614198"><a name="p59954614198"></a><a name="p59954614198"></a>For details, see response field <strong id="vpcep_06_0201_b9758154713317"><a name="vpcep_06_0201_b9758154713317"></a><a name="vpcep_06_0201_b9758154713317"></a>id</strong> in <a href="https://docs.otc.t-systems.com/api/vpc/vpc_api01_0002.html" target="_blank" rel="noopener noreferrer">Querying VPC Details</a> in the <em id="vpcep_06_0201_i12759144715337"><a name="vpcep_06_0201_i12759144715337"></a><a name="vpcep_06_0201_i12759144715337"></a>Virtual Private Cloud API Reference</em>.</p>
    </td>
    </tr>
    <tr id="row11346893"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.2.5.1.1 "><p id="p182860438018"><a name="p182860438018"></a><a name="p182860438018"></a>enable_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p132868431013"><a name="p132868431013"></a><a name="p132868431013"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p728634315016"><a name="p728634315016"></a><a name="p728634315016"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p1255315192149"><a name="p1255315192149"></a><a name="p1255315192149"></a>Specifies whether to create a private domain name.</p>
    <a name="ul7640194412147"></a><a name="ul7640194412147"></a><ul id="ul7640194412147"><li><strong id="b144641053101013"><a name="b144641053101013"></a><a name="b144641053101013"></a>true</strong>: indicates that a private domain name is created.</li><li><strong id="b5944823201120"><a name="b5944823201120"></a><a name="b5944823201120"></a>false</strong>: indicates that a private domain name is not created.</li></ul>
    <p id="p59011829135010"><a name="p59011829135010"></a><a name="p59011829135010"></a>The default value is <strong id="b789259195017"><a name="b789259195017"></a><a name="b789259195017"></a>false</strong>.</p>
    <div class="note" id="note13996125195911"><a name="note13996125195911"></a><a name="note13996125195911"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p119994525918"><a name="p119994525918"></a><a name="p119994525918"></a>When a VPC endpoint for connecting to a gateway VPC endpoint service is created, no private domain name is created no matter <strong id="b960193116271"><a name="b960193116271"></a><a name="b960193116271"></a>enable_dns</strong> is set to <strong id="b1156335172819"><a name="b1156335172819"></a><a name="b1156335172819"></a>true</strong> or <strong id="b844393752815"><a name="b844393752815"></a><a name="b844393752815"></a>false</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row46314724514"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.2.5.1.1 "><p id="p20921314144517"><a name="p20921314144517"></a><a name="p20921314144517"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p3931314204513"><a name="p3931314204513"></a><a name="p3931314204513"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p89314144458"><a name="p89314144458"></a><a name="p89314144458"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p18931714134517"><a name="p18931714134517"></a><a name="p18931714134517"></a>Lists the resource tags. For details, see <a href="#table15695152144819">Table 3</a>.</p>
    <p id="p14442944172811"><a name="p14442944172811"></a><a name="p14442944172811"></a>A maximum of 10 tags can be added to each VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row1487961904518"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.2.5.1.1 "><p id="p6869132344515"><a name="p6869132344515"></a><a name="p6869132344515"></a>routeTables</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p1386917232451"><a name="p1386917232451"></a><a name="p1386917232451"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p168691923164510"><a name="p168691923164510"></a><a name="p168691923164510"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p1489814476216"><a name="p1489814476216"></a><a name="p1489814476216"></a>Lists the IDs of route tables.</p>
    <p id="p178431235172013"><a name="p178431235172013"></a><a name="p178431235172013"></a>For details, see response field <strong id="b0617155320111"><a name="b0617155320111"></a><a name="b0617155320111"></a>id</strong> in <a href="https://docs.otc.t-systems.com/api/vpc/vpc_route_0002.html" target="_blank" rel="noopener noreferrer">Querying a VPC Route</a> in the <em id="i66180533110"><a name="i66180533110"></a><a name="i66180533110"></a>Virtual Private Cloud API Reference</em>.</p>
    <p id="p20869223194517"><a name="p20869223194517"></a><a name="p20869223194517"></a>This parameter is mandatory only if you create a VPC endpoint for connecting to a gateway VPC endpoint service.</p>
    <div class="note" id="note13572522151911"><a name="note13572522151911"></a><a name="note13572522151911"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p115731227197"><a name="p115731227197"></a><a name="p115731227197"></a>If this parameter is not configured, use the default route table.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1429802964411"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.2.5.1.1 "><p id="p159701149124410"><a name="p159701149124410"></a><a name="p159701149124410"></a>port_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p11970104919445"><a name="p11970104919445"></a><a name="p11970104919445"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p3970249144419"><a name="p3970249144419"></a><a name="p3970249144419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p1197012493446"><a name="p1197012493446"></a><a name="p1197012493446"></a>Specifies the IP address for accessing the associated VPC endpoint service.</p>
    <p id="p1397074954416"><a name="p1397074954416"></a><a name="p1397074954416"></a>You can specify IP addresses for accessing the associated VPC endpoint service when creating a VPC endpoint. Only IPv4 addresses are supported.</p>
    <p id="p867517423248"><a name="p867517423248"></a><a name="p867517423248"></a>This parameter is mandatory only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row4298229184418"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.2.5.1.1 "><p id="p1697064913441"><a name="p1697064913441"></a><a name="p1697064913441"></a>whitelist</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p20970114919441"><a name="p20970114919441"></a><a name="p20970114919441"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p8970349104420"><a name="p8970349104420"></a><a name="p8970349104420"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p179701249104416"><a name="p179701249104416"></a><a name="p179701249104416"></a>Specifies the whitelist for controlling access to the VPC endpoint.</p>
    <p id="p697184913445"><a name="p697184913445"></a><a name="p697184913445"></a>IPv4 addresses or CIDR blocks can be specified to control access when you create a VPC endpoint.</p>
    <p id="p163717616252"><a name="p163717616252"></a><a name="p163717616252"></a>This parameter is mandatory only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row42991929124416"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.2.5.1.1 "><p id="p1197117499448"><a name="p1197117499448"></a><a name="p1197117499448"></a>enable_whitelist</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p697164919446"><a name="p697164919446"></a><a name="p697164919446"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p2971849104416"><a name="p2971849104416"></a><a name="p2971849104416"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.5.1.4 "><p id="p2097154974411"><a name="p2097154974411"></a><a name="p2097154974411"></a>Specifies whether to enable access control.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **ResourceTags**  parameters

    <a name="table15695152144819"></a>
    <table><thead align="left"><tr id="vpcep_06_0201_en-us_topic_0056765542_row4410728"><th class="cellrowborder" valign="top" width="15.601560156015601%" id="mcps1.2.5.1.1"><p id="vpcep_06_0201_en-us_topic_0056765542_p21724664"><a name="vpcep_06_0201_en-us_topic_0056765542_p21724664"></a><a name="vpcep_06_0201_en-us_topic_0056765542_p21724664"></a><strong id="vpcep_06_0201_b1563612711"><a name="vpcep_06_0201_b1563612711"></a><a name="vpcep_06_0201_b1563612711"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.061506150615061%" id="mcps1.2.5.1.2"><p id="vpcep_06_0201_p10931647101614"><a name="vpcep_06_0201_p10931647101614"></a><a name="vpcep_06_0201_p10931647101614"></a><strong id="vpcep_06_0201_b1948657836"><a name="vpcep_06_0201_b1948657836"></a><a name="vpcep_06_0201_b1948657836"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.121712171217123%" id="mcps1.2.5.1.3"><p id="vpcep_06_0201_en-us_topic_0056765542_p63406242"><a name="vpcep_06_0201_en-us_topic_0056765542_p63406242"></a><a name="vpcep_06_0201_en-us_topic_0056765542_p63406242"></a><strong id="vpcep_06_0201_b1564672112114"><a name="vpcep_06_0201_b1564672112114"></a><a name="vpcep_06_0201_b1564672112114"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.21522152215221%" id="mcps1.2.5.1.4"><p id="vpcep_06_0201_en-us_topic_0056765542_p35632012"><a name="vpcep_06_0201_en-us_topic_0056765542_p35632012"></a><a name="vpcep_06_0201_en-us_topic_0056765542_p35632012"></a><strong id="vpcep_06_0201_b12940209153810"><a name="vpcep_06_0201_b12940209153810"></a><a name="vpcep_06_0201_b12940209153810"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpcep_06_0201_en-us_topic_0056765542_row511887"><td class="cellrowborder" valign="top" width="15.601560156015601%" headers="mcps1.2.5.1.1 "><p id="vpcep_06_0201_en-us_topic_0056765542_p41462866"><a name="vpcep_06_0201_en-us_topic_0056765542_p41462866"></a><a name="vpcep_06_0201_en-us_topic_0056765542_p41462866"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.061506150615061%" headers="mcps1.2.5.1.2 "><p id="vpcep_06_0201_p12931547141613"><a name="vpcep_06_0201_p12931547141613"></a><a name="vpcep_06_0201_p12931547141613"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.121712171217123%" headers="mcps1.2.5.1.3 "><p id="vpcep_06_0201_en-us_topic_0056765542_p45638969"><a name="vpcep_06_0201_en-us_topic_0056765542_p45638969"></a><a name="vpcep_06_0201_en-us_topic_0056765542_p45638969"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.21522152215221%" headers="mcps1.2.5.1.4 "><p id="vpcep_06_0201_p48921437201850"><a name="vpcep_06_0201_p48921437201850"></a><a name="vpcep_06_0201_p48921437201850"></a>Specifies the tag key. A tag key contains a maximum of 36 Unicode characters. This parameter cannot be left empty. It can contain only digits, letters, hyphens (-), at signs (@), and underscores (_).</p>
    </td>
    </tr>
    <tr id="vpcep_06_0201_en-us_topic_0056765542_row51921052"><td class="cellrowborder" valign="top" width="15.601560156015601%" headers="mcps1.2.5.1.1 "><p id="vpcep_06_0201_en-us_topic_0056765542_p44855704"><a name="vpcep_06_0201_en-us_topic_0056765542_p44855704"></a><a name="vpcep_06_0201_en-us_topic_0056765542_p44855704"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.061506150615061%" headers="mcps1.2.5.1.2 "><p id="vpcep_06_0201_p2093118475163"><a name="vpcep_06_0201_p2093118475163"></a><a name="vpcep_06_0201_p2093118475163"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.121712171217123%" headers="mcps1.2.5.1.3 "><p id="vpcep_06_0201_en-us_topic_0056765542_p25911262"><a name="vpcep_06_0201_en-us_topic_0056765542_p25911262"></a><a name="vpcep_06_0201_en-us_topic_0056765542_p25911262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.21522152215221%" headers="mcps1.2.5.1.4 "><p id="vpcep_06_0201_p61714725112922"><a name="vpcep_06_0201_p61714725112922"></a><a name="vpcep_06_0201_p61714725112922"></a>Specifies the tag value. A tag value contains a maximum of 43 Unicode characters and can be left blank. It can contain only digits, letters, hyphens (-), at signs (@), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{endpoint}/v1/{project_id}/vpc-endpoints
    ```

    ```
    { 
    "subnet_id": "68bfbcc1-dff2-47e4-a9d4-332b9bc1b8de",
    "vpc_id": "84758cf5-9c62-43ae-a778-3dbd8370c0a4",
    "tags":[
                {
                    "key":"test1",
                    "value":"test1"
                }
           ],
    "endpoint_service_id":"e0c748b7-d982-47df-ba06-b9c8c7650c1a",
    "enable_dns":true
    }
    ```


## Response<a name="section22476016"></a>

-   Parameter description

    **Table  4**  Response parameters

    <a name="table65138754"></a>
    <table><thead align="left"><tr id="row19593361"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p43558418"><a name="p43558418"></a><a name="p43558418"></a><strong id="b1380681493"><a name="b1380681493"></a><a name="b1380681493"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.292929292929294%" id="mcps1.2.4.1.2"><p id="p38570971"><a name="p38570971"></a><a name="p38570971"></a><strong id="b1677158776"><a name="b1677158776"></a><a name="b1677158776"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.464646464646464%" id="mcps1.2.4.1.3"><p id="p37240981"><a name="p37240981"></a><a name="p37240981"></a><strong id="b1242019559"><a name="b1242019559"></a><a name="b1242019559"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63729512"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p61816827"><a name="p61816827"></a><a name="p61816827"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p41107062"><a name="p41107062"></a><a name="p41107062"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p41337730"><a name="p41337730"></a><a name="p41337730"></a>Specifies the unique ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row36495254"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p3325565"><a name="p3325565"></a><a name="p3325565"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p935369"><a name="p935369"></a><a name="p935369"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p20173443232"><a name="p20173443232"></a><a name="p20173443232"></a>Specifies the type of the VPC endpoint service that is associated with the VPC endpoint.</p>
    <a name="ul649612552553"></a><a name="ul649612552553"></a><ul id="ul649612552553"><li>Gateway: VPC endpoint services of this type are configured by operations people. You can use them directly without the need to create one by yourselves.</li><li>Interface: VPC endpoint services of this type include cloud services configured by operations people and private services created by yourselves. You cannot configure these cloud services, but can use them.</li></ul>
    <p id="p1318010403317"><a name="p1318010403317"></a><a name="p1318010403317"></a>You can view those VPC endpoint services that are configured by operations people and are visible and accessible to all users. For detailed steps, see <a href="querying-public-vpc-endpoint-services.md">Querying Public VPC Endpoint Services</a>. Perform the operations in <a href="creating-a-vpc-endpoint-service.md">Creating a VPC Endpoint Service</a> to create an interface VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row10796023"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p2062637"><a name="p2062637"></a><a name="p2062637"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p32855908"><a name="p32855908"></a><a name="p32855908"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p583352918492"><a name="p583352918492"></a><a name="p583352918492"></a>Specifies the connection status of the VPC endpoint.</p>
    <a name="ul1594515565918"></a><a name="ul1594515565918"></a><ul id="ul1594515565918"><li><strong id="b1396163511383"><a name="b1396163511383"></a><a name="b1396163511383"></a>pendingAcceptance</strong>: indicates that the VPC endpoint is pending acceptance.</li><li><strong id="b11729191041010"><a name="b11729191041010"></a><a name="b11729191041010"></a>creating</strong>: indicates the VPC endpoint is being created.</li><li><strong id="b18375142441019"><a name="b18375142441019"></a><a name="b18375142441019"></a>accepted</strong>: indicates the VPC endpoint has been accepted.</li><li><strong id="b17317153019104"><a name="b17317153019104"></a><a name="b17317153019104"></a>failed</strong>: indicates the creation of the VPC endpoint failed.</li></ul>
    </td>
    </tr>
    <tr id="row16105144313515"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p11324544145112"><a name="p11324544145112"></a><a name="p11324544145112"></a>active_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p1832415441514"><a name="p1832415441514"></a><a name="p1832415441514"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p14324144165119"><a name="p14324144165119"></a><a name="p14324144165119"></a>Specifies the domain status.</p>
    <a name="ul13303174918418"></a><a name="ul13303174918418"></a><ul id="ul13303174918418"><li><strong id="b34043383318171"><a name="b34043383318171"></a><a name="b34043383318171"></a>frozen</strong>: indicates that the domain is frozen.</li><li><strong id="b8423527061970"><a name="b8423527061970"></a><a name="b8423527061970"></a>active</strong>: indicates that the domain is normal.</li></ul>
    </td>
    </tr>
    <tr id="row55705628"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p15861989"><a name="p15861989"></a><a name="p15861989"></a>endpoint_service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p9752694"><a name="p9752694"></a><a name="p9752694"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p51770744"><a name="p51770744"></a><a name="p51770744"></a>Specifies the name of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row63283514"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p25691048"><a name="p25691048"></a><a name="p25691048"></a>marker_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p600154"><a name="p600154"></a><a name="p600154"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p48612537"><a name="p48612537"></a><a name="p48612537"></a>Specifies the packet ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row34859652"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p5059601"><a name="p5059601"></a><a name="p5059601"></a>endpoint_service_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p7174526"><a name="p7174526"></a><a name="p7174526"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p44265715"><a name="p44265715"></a><a name="p44265715"></a>Specifies the ID of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row62847121"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p57452006"><a name="p57452006"></a><a name="p57452006"></a>enable_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p23100887"><a name="p23100887"></a><a name="p23100887"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p72792580273"><a name="p72792580273"></a><a name="p72792580273"></a>Specifies whether to create a private domain name.</p>
    <a name="ul145169269292"></a><a name="ul145169269292"></a><ul id="ul145169269292"><li><strong id="b10358124333210"><a name="b10358124333210"></a><a name="b10358124333210"></a>true</strong>: indicates that a private domain name is created.</li><li><strong id="b6604154417322"><a name="b6604154417322"></a><a name="b6604154417322"></a>false</strong>: indicates that a private domain name is not created.</li></ul>
    <div class="note" id="note1021533535814"><a name="note1021533535814"></a><a name="note1021533535814"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="vpcep_06_0303_p119994525918"><a name="vpcep_06_0303_p119994525918"></a><a name="vpcep_06_0303_p119994525918"></a>When a VPC endpoint for connecting to a gateway VPC endpoint service is created, no private domain name is created no matter <strong id="vpcep_06_0303_b960193116271"><a name="vpcep_06_0303_b960193116271"></a><a name="vpcep_06_0303_b960193116271"></a>enable_dns</strong> is set to <strong id="vpcep_06_0303_b1156335172819"><a name="vpcep_06_0303_b1156335172819"></a><a name="vpcep_06_0303_b1156335172819"></a>true</strong> or <strong id="vpcep_06_0303_b844393752815"><a name="vpcep_06_0303_b844393752815"></a><a name="vpcep_06_0303_b844393752815"></a>false</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row63331262"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p8679183214469"><a name="p8679183214469"></a><a name="p8679183214469"></a>dns_names</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p467910327469"><a name="p467910327469"></a><a name="p467910327469"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p116791149101913"><a name="p116791149101913"></a><a name="p116791149101913"></a>Specifies the domain name for accessing the associated VPC endpoint service.</p>
    <p id="p13679143220466"><a name="p13679143220466"></a><a name="p13679143220466"></a>This parameter is only available when <strong id="b513454594811"><a name="b513454594811"></a><a name="b513454594811"></a>enable_dns</strong> is set to <strong id="b10660919124617"><a name="b10660919124617"></a><a name="b10660919124617"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="row63900256"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p8538219"><a name="p8538219"></a><a name="p8538219"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p20507143"><a name="p20507143"></a><a name="p20507143"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p50465883"><a name="p50465883"></a><a name="p50465883"></a>Specifies the ID of the subnet created in the VPC specified by <strong id="b1757761010202"><a name="b1757761010202"></a><a name="b1757761010202"></a>vpc_id</strong>. The value is in the UUID format.</p>
    </td>
    </tr>
    <tr id="row55267714"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p751213210"><a name="p751213210"></a><a name="p751213210"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p205121639116"><a name="p205121639116"></a><a name="p205121639116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p122415282419"><a name="p122415282419"></a><a name="p122415282419"></a>Specifies the ID of the VPC where the VPC endpoint is to be created.</p>
    </td>
    </tr>
    <tr id="row3635902"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p26072634"><a name="p26072634"></a><a name="p26072634"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p31508570"><a name="p31508570"></a><a name="p31508570"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p22890001"><a name="p22890001"></a><a name="p22890001"></a>Specifies the creation time of the VPC endpoint.</p>
    <p id="p871616113394"><a name="p871616113394"></a><a name="p871616113394"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row18516157"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p23413735"><a name="p23413735"></a><a name="p23413735"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p17464402"><a name="p17464402"></a><a name="p17464402"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p27321481"><a name="p27321481"></a><a name="p27321481"></a>Specifies the update time of the VPC endpoint.</p>
    <p id="p181016810016"><a name="p181016810016"></a><a name="p181016810016"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row47974230"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p60707417"><a name="p60707417"></a><a name="p60707417"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p18353753"><a name="p18353753"></a><a name="p18353753"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p10259005"><a name="p10259005"></a><a name="p10259005"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row204491010122314"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p13103244015"><a name="p13103244015"></a><a name="p13103244015"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p21037441512"><a name="p21037441512"></a><a name="p21037441512"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p1510414411116"><a name="p1510414411116"></a><a name="p1510414411116"></a>Lists the resource tags. For details, see <a href="#table489217571060">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row4213193174716"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p165011381477"><a name="p165011381477"></a><a name="p165011381477"></a>whitelist</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p450173820473"><a name="p450173820473"></a><a name="p450173820473"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p2538528143320"><a name="p2538528143320"></a><a name="p2538528143320"></a>Specifies the whitelist for controlling access to the VPC endpoint.</p>
    <p id="p386713773414"><a name="p386713773414"></a><a name="p386713773414"></a>If you do not specify this parameter, an empty whitelist is returned.</p>
    <p id="p1093618430819"><a name="p1093618430819"></a><a name="p1093618430819"></a>This parameter is available only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row192131031144718"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p050938124710"><a name="p050938124710"></a><a name="p050938124710"></a>enable_whitelist</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p85019382479"><a name="p85019382479"></a><a name="p85019382479"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p1458051113412"><a name="p1458051113412"></a><a name="p1458051113412"></a>Specifies whether to enable access control.</p>
    <a name="ul1998774161110"></a><a name="ul1998774161110"></a><ul id="ul1998774161110"><li><strong id="b11313153317138"><a name="b11313153317138"></a><a name="b11313153317138"></a>true</strong>: indicates that access control is enabled.</li><li><strong id="b12134145911314"><a name="b12134145911314"></a><a name="b12134145911314"></a>false</strong>: indicates that access control is disabled.</li></ul>
    <p id="p16973392358"><a name="p16973392358"></a><a name="p16973392358"></a>If you do not specify this parameter, the whitelist is not enabled.</p>
    <p id="p14198121916915"><a name="p14198121916915"></a><a name="p14198121916915"></a>This parameter is available only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row42141317475"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p9502038174719"><a name="p9502038174719"></a><a name="p9502038174719"></a>routetables</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p650203810476"><a name="p650203810476"></a><a name="p650203810476"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p422280153614"><a name="p422280153614"></a><a name="p422280153614"></a>Lists the IDs of route tables.</p>
    <p id="p17737722113611"><a name="p17737722113611"></a><a name="p17737722113611"></a>If you do not specify this parameter, the route table ID of the VPC is returned.</p>
    <p id="p5900254395"><a name="p5900254395"></a><a name="p5900254395"></a>This parameter is available only if you create a VPC endpoint for connecting to a gateway VPC endpoint service.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **ResourceTags**  parameters

    <a name="table489217571060"></a>
    <table><thead align="left"><tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row4410728"><th class="cellrowborder" valign="top" width="18.09%" id="mcps1.2.4.1.1"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"></a><strong id="vpcep_06_0201_b1866348132314"><a name="vpcep_06_0201_b1866348132314"></a><a name="vpcep_06_0201_b1866348132314"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"></a><strong id="vpcep_06_0201_b616714104231"><a name="vpcep_06_0201_b616714104231"></a><a name="vpcep_06_0201_b616714104231"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.91%" id="mcps1.2.4.1.3"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"></a><strong id="vpcep_06_0201_b163691023811"><a name="vpcep_06_0201_b163691023811"></a><a name="vpcep_06_0201_b163691023811"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row511887"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.91%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"><a name="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"></a>Specifies the tag key. A tag key contains a maximum of 36 Unicode characters. This parameter cannot be left empty. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row51921052"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.91%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"><a name="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"></a>Specifies the tag value. A tag value contains a maximum of 43 Unicode characters and can be left blank. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "id": "4189d3c2-8882-4871-a3c2-d380272eed83",
        "service_type": "interface",
        "marker_id": 322312312312,
        "status": "creating",
        "vpc_id": "4189d3c2-8882-4871-a3c2-d380272eed83",
        "enable_dns": false,
        "endpoint_service_name": "test123",
        "endpoint_service_id": "test123",
        "project_id": "6e9dfd51d1124e8d8498dce894923a0d",
        "whitelist": [
            "127.0.0.1"
        ],
        "enable_whitelist": true,
        "created_at": "2018-01-30T07:42:01.174",
        "update_at": "2018-01-30T07:42:01.174",
        "tags": [
            {
                "key": "test1",
                "value": "test1"
            }
        ]
    }
    ```


## Status Code<a name="section8618044"></a>

For details about status codes, see  [Status Code](/vpcep/api-reference/common/status-code.md).

