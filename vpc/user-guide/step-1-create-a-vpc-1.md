# Step 1: Create a VPC<a name="vpc_qs_0009"></a>

## Scenarios<a name="section87731937861"></a>

A VPC provides an isolated virtual network for ECSs. You can configure and manage the network as required.

Create a VPC by following the procedure provided in this section. Then, create subnets, security groups, and assign EIPs by following the procedure provided in subsequent sections based on your actual network requirements.

## Procedure<a name="section6773143718614"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  On the  **Dashboard**  page, click  **Create VPC**.
5.  On the  **Create VPC**  page, set parameters as prompted.

    During VPC creation, a default subnet will be created. You can also click  **Add Subnet**  to create more subnets for the VPC.

    **Table  1**  VPC parameter description

    <a name="en-us_topic_0013935842_table1168883712472"></a>
    <table><thead align="left"><tr id="en-us_topic_0013935842_row17700537104713"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.2.5.1.1"><p id="en-us_topic_0013935842_p3444547103715"><a name="en-us_topic_0013935842_p3444547103715"></a><a name="en-us_topic_0013935842_p3444547103715"></a>Category</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.18181818181818%" id="mcps1.2.5.1.2"><p id="en-us_topic_0013935842_p17713173714472"><a name="en-us_topic_0013935842_p17713173714472"></a><a name="en-us_topic_0013935842_p17713173714472"></a><strong id="en-us_topic_0013935842_b1483272480"><a name="en-us_topic_0013935842_b1483272480"></a><a name="en-us_topic_0013935842_b1483272480"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.464646464646464%" id="mcps1.2.5.1.3"><p id="en-us_topic_0013935842_p157202037194711"><a name="en-us_topic_0013935842_p157202037194711"></a><a name="en-us_topic_0013935842_p157202037194711"></a><strong id="en-us_topic_0013935842_b902637693"><a name="en-us_topic_0013935842_b902637693"></a><a name="en-us_topic_0013935842_b902637693"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.19191919191919%" id="mcps1.2.5.1.4"><p id="en-us_topic_0013935842_p97241237164712"><a name="en-us_topic_0013935842_p97241237164712"></a><a name="en-us_topic_0013935842_p97241237164712"></a><strong id="en-us_topic_0013935842_b937216832"><a name="en-us_topic_0013935842_b937216832"></a><a name="en-us_topic_0013935842_b937216832"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0013935842_row17320372477"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0013935842_p24440476373"><a name="en-us_topic_0013935842_p24440476373"></a><a name="en-us_topic_0013935842_p24440476373"></a>Basic Information</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0013935842_p1274273714718"><a name="en-us_topic_0013935842_p1274273714718"></a><a name="en-us_topic_0013935842_p1274273714718"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0013935842_p6748113774713"><a name="en-us_topic_0013935842_p6748113774713"></a><a name="en-us_topic_0013935842_p6748113774713"></a>Specifies the desired region. Regions are geographic areas that are physically isolated from each other. The networks inside different regions are not connected to each other, so resources cannot be shared across different regions. For lower network latency and faster access to your resources, select the region nearest you.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0013935842_p7738111114910"><a name="en-us_topic_0013935842_p7738111114910"></a><a name="en-us_topic_0013935842_p7738111114910"></a>eu-de</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_row157551937204713"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0013935842_p15444194723717"><a name="en-us_topic_0013935842_p15444194723717"></a><a name="en-us_topic_0013935842_p15444194723717"></a>Basic Information</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0013935842_p1575823764710"><a name="en-us_topic_0013935842_p1575823764710"></a><a name="en-us_topic_0013935842_p1575823764710"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0013935842_p107634373470"><a name="en-us_topic_0013935842_p107634373470"></a><a name="en-us_topic_0013935842_p107634373470"></a>Specifies the VPC name.</p>
    <p id="en-us_topic_0013935842_p1458018820378"><a name="en-us_topic_0013935842_p1458018820378"></a><a name="en-us_topic_0013935842_p1458018820378"></a>The VPC flow log name can contain a maximum of 64 characters, which may consist of letters, digits, underscores (_), hyphens (-), and periods (.). The name cannot contain spaces.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0013935842_p1976793794713"><a name="en-us_topic_0013935842_p1976793794713"></a><a name="en-us_topic_0013935842_p1976793794713"></a>VPC-001</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_row1768437154711"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0013935842_p54441647173717"><a name="en-us_topic_0013935842_p54441647173717"></a><a name="en-us_topic_0013935842_p54441647173717"></a>Basic Information</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0013935842_p7770103714473"><a name="en-us_topic_0013935842_p7770103714473"></a><a name="en-us_topic_0013935842_p7770103714473"></a>CIDR Block</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0013935842_p07741437114718"><a name="en-us_topic_0013935842_p07741437114718"></a><a name="en-us_topic_0013935842_p07741437114718"></a>Specifies the CIDR block for the VPC. The CIDR block of a subnet can be the same as the CIDR block for the VPC (for a single subnet in the VPC) or a subset (for multiple subnets in the VPC).</p>
    <p id="en-us_topic_0013935842_p187780374473"><a name="en-us_topic_0013935842_p187780374473"></a><a name="en-us_topic_0013935842_p187780374473"></a>The following CIDR blocks are supported:</p>
    <p id="en-us_topic_0013935842_p1780103716472"><a name="en-us_topic_0013935842_p1780103716472"></a><a name="en-us_topic_0013935842_p1780103716472"></a>10.0.0.0 – 10.255.255.255</p>
    <p id="en-us_topic_0013935842_p13782237154715"><a name="en-us_topic_0013935842_p13782237154715"></a><a name="en-us_topic_0013935842_p13782237154715"></a>172.16.0.0 – 172.31.255.255 </p>
    <p id="en-us_topic_0013935842_p15782637144715"><a name="en-us_topic_0013935842_p15782637144715"></a><a name="en-us_topic_0013935842_p15782637144715"></a>192.168.0.0 – 192.168.255.255</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0013935842_p1785163744718"><a name="en-us_topic_0013935842_p1785163744718"></a><a name="en-us_topic_0013935842_p1785163744718"></a>192.168.0.0/16</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_row5787153719479"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0013935842_p84441447183715"><a name="en-us_topic_0013935842_p84441447183715"></a><a name="en-us_topic_0013935842_p84441447183715"></a>Basic Information</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0013935842_p157901437174712"><a name="en-us_topic_0013935842_p157901437174712"></a><a name="en-us_topic_0013935842_p157901437174712"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0013935842_p11793537164717"><a name="en-us_topic_0013935842_p11793537164717"></a><a name="en-us_topic_0013935842_p11793537164717"></a>Specifies the VPC tag, which consists of a key and value pair. You can add a maximum of ten tags to each VPC.</p>
    <p id="en-us_topic_0013935842_p7797133718477"><a name="en-us_topic_0013935842_p7797133718477"></a><a name="en-us_topic_0013935842_p7797133718477"></a>The tag key and value must meet the requirements listed in <a href="#en-us_topic_0013935842_table248245914136">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0013935842_ul1080513754718"></a><a name="en-us_topic_0013935842_ul1080513754718"></a><ul id="en-us_topic_0013935842_ul1080513754718"><li>Key: vpc_key1</li><li>Value: vpc-01</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_row17818237194711"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0013935842_p0444447193713"><a name="en-us_topic_0013935842_p0444447193713"></a><a name="en-us_topic_0013935842_p0444447193713"></a>Subnet Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0013935842_p5825193724719"><a name="en-us_topic_0013935842_p5825193724719"></a><a name="en-us_topic_0013935842_p5825193724719"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0013935842_p1683033718471"><a name="en-us_topic_0013935842_p1683033718471"></a><a name="en-us_topic_0013935842_p1683033718471"></a>Specifies the subnet name.</p>
    <p id="en-us_topic_0013935842_p14852213173720"><a name="en-us_topic_0013935842_p14852213173720"></a><a name="en-us_topic_0013935842_p14852213173720"></a>The VPC flow log name can contain a maximum of 64 characters, which may consist of letters, digits, underscores (_), hyphens (-), and periods (.). The name cannot contain spaces.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0013935842_p178351137184711"><a name="en-us_topic_0013935842_p178351137184711"></a><a name="en-us_topic_0013935842_p178351137184711"></a>Subnet</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_row8837123719474"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0013935842_p1544410476376"><a name="en-us_topic_0013935842_p1544410476376"></a><a name="en-us_topic_0013935842_p1544410476376"></a>Subnet Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0013935842_p1284223764717"><a name="en-us_topic_0013935842_p1284223764717"></a><a name="en-us_topic_0013935842_p1284223764717"></a>CIDR Block</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0013935842_p15845173713472"><a name="en-us_topic_0013935842_p15845173713472"></a><a name="en-us_topic_0013935842_p15845173713472"></a>Specifies the CIDR block for the subnet. This value must be within the VPC CIDR block.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0013935842_p184773774715"><a name="en-us_topic_0013935842_p184773774715"></a><a name="en-us_topic_0013935842_p184773774715"></a>192.168.0.0/24</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_row2050052115164"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0013935842_p14501192115167"><a name="en-us_topic_0013935842_p14501192115167"></a><a name="en-us_topic_0013935842_p14501192115167"></a>Subnet Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0013935842_p1887214237161"><a name="en-us_topic_0013935842_p1887214237161"></a><a name="en-us_topic_0013935842_p1887214237161"></a>Advanced Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0013935842_p118721923161618"><a name="en-us_topic_0013935842_p118721923161618"></a><a name="en-us_topic_0013935842_p118721923161618"></a>Two options are available, <strong id="en-us_topic_0013935842_b8203281417"><a name="en-us_topic_0013935842_b8203281417"></a><a name="en-us_topic_0013935842_b8203281417"></a>Default</strong> and <strong id="en-us_topic_0013935842_b112222818416"><a name="en-us_topic_0013935842_b112222818416"></a><a name="en-us_topic_0013935842_b112222818416"></a>Custom</strong>. You can set <strong id="en-us_topic_0013935842_b13285133118419"><a name="en-us_topic_0013935842_b13285133118419"></a><a name="en-us_topic_0013935842_b13285133118419"></a>Advanced Settings</strong> to <strong id="en-us_topic_0013935842_b22854314411"><a name="en-us_topic_0013935842_b22854314411"></a><a name="en-us_topic_0013935842_b22854314411"></a>Custom</strong> to configure advanced subnet parameters.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0013935842_p1872142311614"><a name="en-us_topic_0013935842_p1872142311614"></a><a name="en-us_topic_0013935842_p1872142311614"></a>Default</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_row12850193724713"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0013935842_p64441047173713"><a name="en-us_topic_0013935842_p64441047173713"></a><a name="en-us_topic_0013935842_p64441047173713"></a>Subnet Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0013935842_p158559376477"><a name="en-us_topic_0013935842_p158559376477"></a><a name="en-us_topic_0013935842_p158559376477"></a>Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0013935842_p485963744718"><a name="en-us_topic_0013935842_p485963744718"></a><a name="en-us_topic_0013935842_p485963744718"></a>Specifies the gateway address of the subnet.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0013935842_p28646379474"><a name="en-us_topic_0013935842_p28646379474"></a><a name="en-us_topic_0013935842_p28646379474"></a>192.168.0.1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_row16401281486"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0013935842_p74441147133716"><a name="en-us_topic_0013935842_p74441147133716"></a><a name="en-us_topic_0013935842_p74441147133716"></a>Subnet Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0013935842_p3868137104715"><a name="en-us_topic_0013935842_p3868137104715"></a><a name="en-us_topic_0013935842_p3868137104715"></a>DNS Server Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0013935842_p12393185622820"><a name="en-us_topic_0013935842_p12393185622820"></a><a name="en-us_topic_0013935842_p12393185622820"></a>By default, two DNS server addresses are configured. You can change them as required. A maximum of five DNS server addresses can be configured. Multiple IP addresses must be separated using commas (,).</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0013935842_p108271634171219"><a name="en-us_topic_0013935842_p108271634171219"></a><a name="en-us_topic_0013935842_p108271634171219"></a>100.125.x.x</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_row1832812810404"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0013935842_p14444164743719"><a name="en-us_topic_0013935842_p14444164743719"></a><a name="en-us_topic_0013935842_p14444164743719"></a>Subnet Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0013935842_p136581510164016"><a name="en-us_topic_0013935842_p136581510164016"></a><a name="en-us_topic_0013935842_p136581510164016"></a>NTP Server Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0013935842_p86331841139"><a name="en-us_topic_0013935842_p86331841139"></a><a name="en-us_topic_0013935842_p86331841139"></a>Specifies the IP address of the NTP server. This parameter is optional.</p>
    <p id="en-us_topic_0013935842_p7633342312"><a name="en-us_topic_0013935842_p7633342312"></a><a name="en-us_topic_0013935842_p7633342312"></a>You can configure the NTP server IP addresses to be added to the subnet as required. The IP addresses are added in addition to the default NTP server addresses. If this parameter is left empty, no IP address of the NTP server is added.</p>
    <p id="en-us_topic_0013935842_p7633194133"><a name="en-us_topic_0013935842_p7633194133"></a><a name="en-us_topic_0013935842_p7633194133"></a>A maximum of four IP addresses can be configured. Multiple IP addresses must be separated using commas (,).</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0013935842_p4670101094012"><a name="en-us_topic_0013935842_p4670101094012"></a><a name="en-us_topic_0013935842_p4670101094012"></a>192.168.2.1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_row7876103724712"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0013935842_p1044474743711"><a name="en-us_topic_0013935842_p1044474743711"></a><a name="en-us_topic_0013935842_p1044474743711"></a>Subnet Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0013935842_p987993754719"><a name="en-us_topic_0013935842_p987993754719"></a><a name="en-us_topic_0013935842_p987993754719"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0013935842_p10882937104713"><a name="en-us_topic_0013935842_p10882937104713"></a><a name="en-us_topic_0013935842_p10882937104713"></a>Specifies the subnet tag, which consists of a key and value pair. You can add a maximum of ten tags to each subnet.</p>
    <p id="en-us_topic_0013935842_p988417379473"><a name="en-us_topic_0013935842_p988417379473"></a><a name="en-us_topic_0013935842_p988417379473"></a>The tag key and value must meet the requirements listed in <a href="#en-us_topic_0013935842_table6536185812515">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0013935842_ul6890193724718"></a><a name="en-us_topic_0013935842_ul6890193724718"></a><ul id="en-us_topic_0013935842_ul6890193724718"><li>Key: subnet_key1</li><li>Value: subnet-01</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  VPC tag key and value requirements

    <a name="en-us_topic_0013935842_table248245914136"></a>
    <table><thead align="left"><tr id="en-us_topic_0013935842_vpc_vpc_0004_r8f725dd873f74d5689a397a96364525f"><th class="cellrowborder" valign="top" width="17.71%" id="mcps1.2.4.1.1"><p id="en-us_topic_0013935842_vpc_vpc_0004_ae7200181216040679ba0b08613e317f0"><a name="en-us_topic_0013935842_vpc_vpc_0004_ae7200181216040679ba0b08613e317f0"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_ae7200181216040679ba0b08613e317f0"></a><strong id="en-us_topic_0013935842_vpc_vpc_0004_b84235270618434"><a name="en-us_topic_0013935842_vpc_vpc_0004_b84235270618434"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_b84235270618434"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65.29%" id="mcps1.2.4.1.2"><p id="en-us_topic_0013935842_vpc_vpc_0004_a30f1778a977845c0a6948f77fd9efada"><a name="en-us_topic_0013935842_vpc_vpc_0004_a30f1778a977845c0a6948f77fd9efada"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_a30f1778a977845c0a6948f77fd9efada"></a><strong id="en-us_topic_0013935842_vpc_vpc_0004_b842352706174218"><a name="en-us_topic_0013935842_vpc_vpc_0004_b842352706174218"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_b842352706174218"></a>Requirements</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.3"><p id="en-us_topic_0013935842_vpc_vpc_0004_a34827669831a48ec96262bfcabc61519"><a name="en-us_topic_0013935842_vpc_vpc_0004_a34827669831a48ec96262bfcabc61519"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_a34827669831a48ec96262bfcabc61519"></a><strong id="en-us_topic_0013935842_vpc_vpc_0004_b842352706174227"><a name="en-us_topic_0013935842_vpc_vpc_0004_b842352706174227"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_b842352706174227"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0013935842_vpc_vpc_0004_ra6c6dfb7a5c344f1af2c7664d34e7d80"><td class="cellrowborder" valign="top" width="17.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013935842_vpc_vpc_0004_a45a01bdce58d410d8ee06b6f374e401b"><a name="en-us_topic_0013935842_vpc_vpc_0004_a45a01bdce58d410d8ee06b6f374e401b"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_a45a01bdce58d410d8ee06b6f374e401b"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.29%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0013935842_vpc_vpc_0004_ub2cf5f68e02742d49e3f8d80289eab77"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_ub2cf5f68e02742d49e3f8d80289eab77"></a><ul id="en-us_topic_0013935842_vpc_vpc_0004_ub2cf5f68e02742d49e3f8d80289eab77"><li>Cannot be left blank.</li><li>Must be unique for the same VPC and can be the same for different VPCs.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0013935842_vpc_vpc_0004_uccb317c6616b4445aa84b125e5aa017f"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_uccb317c6616b4445aa84b125e5aa017f"></a><ul id="en-us_topic_0013935842_vpc_vpc_0004_uccb317c6616b4445aa84b125e5aa017f"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013935842_vpc_vpc_0004_a735c9e74ec274598ac7051f7d65e7bce"><a name="en-us_topic_0013935842_vpc_vpc_0004_a735c9e74ec274598ac7051f7d65e7bce"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_a735c9e74ec274598ac7051f7d65e7bce"></a>vpc_key1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_vpc_vpc_0004_rcabbd61ffcd048ec8408a15332fde94d"><td class="cellrowborder" valign="top" width="17.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013935842_vpc_vpc_0004_a5f7f1bb378214abcaf0c661567a47535"><a name="en-us_topic_0013935842_vpc_vpc_0004_a5f7f1bb378214abcaf0c661567a47535"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_a5f7f1bb378214abcaf0c661567a47535"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.29%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0013935842_vpc_vpc_0004_u463eb9034f3d456b81073b15ba62f102"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_u463eb9034f3d456b81073b15ba62f102"></a><ul id="en-us_topic_0013935842_vpc_vpc_0004_u463eb9034f3d456b81073b15ba62f102"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0013935842_vpc_vpc_0004_ub74c759faad544c3b4428accc9c42b80"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_ub74c759faad544c3b4428accc9c42b80"></a><ul id="en-us_topic_0013935842_vpc_vpc_0004_ub74c759faad544c3b4428accc9c42b80"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013935842_vpc_vpc_0004_a3ac5d865f6a848458eb5fae95f81fee0"><a name="en-us_topic_0013935842_vpc_vpc_0004_a3ac5d865f6a848458eb5fae95f81fee0"></a><a name="en-us_topic_0013935842_vpc_vpc_0004_a3ac5d865f6a848458eb5fae95f81fee0"></a>vpc-01</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Subnet tag key and value requirements

    <a name="en-us_topic_0013935842_table6536185812515"></a>
    <table><thead align="left"><tr id="en-us_topic_0013935842_vpc_vpc_0005_rd57708e01e6443a9805ca72f554fae7f"><th class="cellrowborder" valign="top" width="18.54%" id="mcps1.2.4.1.1"><p id="en-us_topic_0013935842_vpc_vpc_0005_abc7708d69440476086850b219c70efa8"><a name="en-us_topic_0013935842_vpc_vpc_0005_abc7708d69440476086850b219c70efa8"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_abc7708d69440476086850b219c70efa8"></a><strong id="en-us_topic_0013935842_vpc_vpc_0005_b842352706165123"><a name="en-us_topic_0013935842_vpc_vpc_0005_b842352706165123"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_b842352706165123"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.39%" id="mcps1.2.4.1.2"><p id="en-us_topic_0013935842_vpc_vpc_0005_a0df2f83c3277432ab05b525e4ffb1c2c"><a name="en-us_topic_0013935842_vpc_vpc_0005_a0df2f83c3277432ab05b525e4ffb1c2c"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_a0df2f83c3277432ab05b525e4ffb1c2c"></a><strong id="en-us_topic_0013935842_vpc_vpc_0005_b842352706174218"><a name="en-us_topic_0013935842_vpc_vpc_0005_b842352706174218"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_b842352706174218"></a>Requirements</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.3"><p id="en-us_topic_0013935842_vpc_vpc_0005_a902e732241f94e96b0b1b718cf7ed639"><a name="en-us_topic_0013935842_vpc_vpc_0005_a902e732241f94e96b0b1b718cf7ed639"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_a902e732241f94e96b0b1b718cf7ed639"></a><strong id="en-us_topic_0013935842_vpc_vpc_0005_b842352706174227"><a name="en-us_topic_0013935842_vpc_vpc_0005_b842352706174227"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_b842352706174227"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0013935842_vpc_vpc_0005_r95612b479088487b99e620f90b71f798"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013935842_vpc_vpc_0005_a7694a48138124d1daf3804556a27bfd6"><a name="en-us_topic_0013935842_vpc_vpc_0005_a7694a48138124d1daf3804556a27bfd6"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_a7694a48138124d1daf3804556a27bfd6"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0013935842_vpc_vpc_0005_uac40e19ce4ac49d0913d48b334564c45"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_uac40e19ce4ac49d0913d48b334564c45"></a><ul id="en-us_topic_0013935842_vpc_vpc_0005_uac40e19ce4ac49d0913d48b334564c45"><li>Cannot be left blank.</li><li>Must be unique for each subnet.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0013935842_vpc_vpc_0005_uccb317c6616b4445aa84b125e5aa017f"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_uccb317c6616b4445aa84b125e5aa017f"></a><ul id="en-us_topic_0013935842_vpc_vpc_0005_uccb317c6616b4445aa84b125e5aa017f"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013935842_vpc_vpc_0005_a1a10de6d67c04555a3508a8cdc3500e7"><a name="en-us_topic_0013935842_vpc_vpc_0005_a1a10de6d67c04555a3508a8cdc3500e7"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_a1a10de6d67c04555a3508a8cdc3500e7"></a>subnet_key1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_vpc_vpc_0005_r32a79d8bde844fda8a6254383317e58f"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013935842_vpc_vpc_0005_a1ebd1dda592448d49631c7f099519113"><a name="en-us_topic_0013935842_vpc_vpc_0005_a1ebd1dda592448d49631c7f099519113"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_a1ebd1dda592448d49631c7f099519113"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0013935842_vpc_vpc_0005_uaf17b1ea9b9a4e58b95cafefa2898283"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_uaf17b1ea9b9a4e58b95cafefa2898283"></a><ul id="en-us_topic_0013935842_vpc_vpc_0005_uaf17b1ea9b9a4e58b95cafefa2898283"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0013935842_vpc_vpc_0005_ub74c759faad544c3b4428accc9c42b80"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_ub74c759faad544c3b4428accc9c42b80"></a><ul id="en-us_topic_0013935842_vpc_vpc_0005_ub74c759faad544c3b4428accc9c42b80"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013935842_vpc_vpc_0005_a21a035aeb72143f5ab0fd45a08248d08"><a name="en-us_topic_0013935842_vpc_vpc_0005_a21a035aeb72143f5ab0fd45a08248d08"></a><a name="en-us_topic_0013935842_vpc_vpc_0005_a21a035aeb72143f5ab0fd45a08248d08"></a>subnet-01</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Create Now**.

