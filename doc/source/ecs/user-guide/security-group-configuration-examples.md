# Security Group Configuration Examples<a name="EN-US_TOPIC_0140323152"></a>

Common security group configuration examples are as follows: The following examples allow all outgoing data packets by default and only describe how to configure the inbound rules of a security group.

-   [Enabling ECSs in Different Security Groups to Communicate with Each Other Through an Internal Network](#en-us_topic_0118534011_section14197522283)
-   [Enabling Specified IP Addresses to Remotely Access ECSs in a Security Group](#en-us_topic_0118534011_section17693183118306)
-   [Remotely Connecting to Linux ECSs Using SSH](#en-us_topic_0118534011_section115069253338)
-   [Remotely Connecting to Windows ECSs Using RDP](#en-us_topic_0118534011_section168046312349)
-   [Enabling Communication Between ECSs](#en-us_topic_0118534011_section34721049193411)
-   [Hosting a Website on ECSs](#en-us_topic_0118534011_section1517991516357)
-   [Enabling an ECS to Function as a DNS Server](#en-us_topic_0118534011_section2910346123520)
-   [Uploading or Downloading Files Using FTP](#en-us_topic_0118534011_section5964121693610)

## Enabling ECSs in Different Security Groups to Communicate with Each Other Through an Internal Network<a name="en-us_topic_0118534011_section14197522283"></a>

-   Example scenario:

    In this scenario, resources on an ECS in a security group need to be copied to an ECS associated with another security group. The two ECSs are in the same VPC. We recommend that you enable internal network communication between the ECSs and then copy the resources.

-   Security group configuration:

    Within a given VPC, ECSs in the same security group can communicate with one another by default. However, ECSs in different security groups cannot communicate with each other by default. For the networks in these ECSs to communicate with each other, you must add certain security group rules.

    You can add an inbound rule to the security groups containing the ECSs to allow access from ECSs in the other security group. The required rule is as follows.

    <a name="en-us_topic_0118534011_table854766319358"></a>
    <table><thead align="left"><tr id="en-us_topic_0118534011_row2051403019358"><th class="cellrowborder" valign="top" width="12.400000000000002%" id="mcps1.1.5.1.1"><p id="en-us_topic_0118534011_p3928016319358"><a name="en-us_topic_0118534011_p3928016319358"></a><a name="en-us_topic_0118534011_p3928016319358"></a><strong id="en-us_topic_0118534011_en-us_topic_0118646266_en-us_topic_0118534005_b13723751135618"><a name="en-us_topic_0118534011_en-us_topic_0118646266_en-us_topic_0118534005_b13723751135618"></a><a name="en-us_topic_0118534011_en-us_topic_0118646266_en-us_topic_0118534005_b13723751135618"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.43000000000001%" id="mcps1.1.5.1.2"><p id="en-us_topic_0118534011_p5102371419358"><a name="en-us_topic_0118534011_p5102371419358"></a><a name="en-us_topic_0118534011_p5102371419358"></a><strong id="en-us_topic_0118534011_b842352706104812"><a name="en-us_topic_0118534011_b842352706104812"></a><a name="en-us_topic_0118534011_b842352706104812"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.810000000000002%" id="mcps1.1.5.1.3"><p id="en-us_topic_0118534011_p2415644494621"><a name="en-us_topic_0118534011_p2415644494621"></a><a name="en-us_topic_0118534011_p2415644494621"></a><strong id="en-us_topic_0118534011_b842352706161911_1"><a name="en-us_topic_0118534011_b842352706161911_1"></a><a name="en-us_topic_0118534011_b842352706161911_1"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.360000000000003%" id="mcps1.1.5.1.4"><p id="en-us_topic_0118534011_p1911210519358"><a name="en-us_topic_0118534011_p1911210519358"></a><a name="en-us_topic_0118534011_p1911210519358"></a><strong id="en-us_topic_0118534011_en-us_topic_0118646266_en-us_topic_0118534005_b1665113556568"><a name="en-us_topic_0118534011_en-us_topic_0118646266_en-us_topic_0118534005_b1665113556568"></a><a name="en-us_topic_0118534011_en-us_topic_0118646266_en-us_topic_0118534005_b1665113556568"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118534011_row3779122419358"><td class="cellrowborder" valign="top" width="12.400000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0118534011_p4808290419358"><a name="en-us_topic_0118534011_p4808290419358"></a><a name="en-us_topic_0118534011_p4808290419358"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.43000000000001%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0118534011_p4119033619358"><a name="en-us_topic_0118534011_p4119033619358"></a><a name="en-us_topic_0118534011_p4119033619358"></a>Used for communication through an internal network</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.810000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0118534011_p4640703694621"><a name="en-us_topic_0118534011_p4640703694621"></a><a name="en-us_topic_0118534011_p4640703694621"></a>Port or port range</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.360000000000003%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0118534011_p6027368919358"><a name="en-us_topic_0118534011_p6027368919358"></a><a name="en-us_topic_0118534011_p6027368919358"></a>ID of another security group</p>
    </td>
    </tr>
    </tbody>
    </table>


## Enabling Specified IP Addresses to Remotely Access ECSs in a Security Group<a name="en-us_topic_0118534011_section17693183118306"></a>

-   Example scenario:

    To prevent ECSs from being attacked, you can change the port number for remote login and configure security group rules that allow only specified IP addresses to remotely access the ECSs.

-   Security group configuration:

    To allow IP address  **192.168.20.2**  to remotely access Linux ECSs in a security group over the SSH protocol \(port 22\), you can configure the following security group rule.

    <a name="en-us_topic_0118534011_table2497622119555"></a>
    <table><thead align="left"><tr id="en-us_topic_0118534011_row407563919555"><th class="cellrowborder" valign="top" width="12.04120412041204%" id="mcps1.1.5.1.1"><p id="en-us_topic_0118534011_p181361106345"><a name="en-us_topic_0118534011_p181361106345"></a><a name="en-us_topic_0118534011_p181361106345"></a><strong id="en-us_topic_0118534011_b137891355798"><a name="en-us_topic_0118534011_b137891355798"></a><a name="en-us_topic_0118534011_b137891355798"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.51185118511851%" id="mcps1.1.5.1.2"><p id="en-us_topic_0118534011_p6169135719555"><a name="en-us_topic_0118534011_p6169135719555"></a><a name="en-us_topic_0118534011_p6169135719555"></a><strong id="en-us_topic_0118534011_b62878816103"><a name="en-us_topic_0118534011_b62878816103"></a><a name="en-us_topic_0118534011_b62878816103"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.53165316531653%" id="mcps1.1.5.1.3"><p id="en-us_topic_0118534011_p2343829819555"><a name="en-us_topic_0118534011_p2343829819555"></a><a name="en-us_topic_0118534011_p2343829819555"></a><strong id="en-us_topic_0118534011_b9902119131013"><a name="en-us_topic_0118534011_b9902119131013"></a><a name="en-us_topic_0118534011_b9902119131013"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.91529152915292%" id="mcps1.1.5.1.4"><p id="en-us_topic_0118534011_p1945401819555"><a name="en-us_topic_0118534011_p1945401819555"></a><a name="en-us_topic_0118534011_p1945401819555"></a><strong id="en-us_topic_0118534011_b1742151071014"><a name="en-us_topic_0118534011_b1742151071014"></a><a name="en-us_topic_0118534011_b1742151071014"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118534011_row3227161019555"><td class="cellrowborder" valign="top" width="12.04120412041204%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0118534011_p313671093414"><a name="en-us_topic_0118534011_p313671093414"></a><a name="en-us_topic_0118534011_p313671093414"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.51185118511851%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0118534011_p6386359419555"><a name="en-us_topic_0118534011_p6386359419555"></a><a name="en-us_topic_0118534011_p6386359419555"></a>SSH (22)</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.53165316531653%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0118534011_p4840629219555"><a name="en-us_topic_0118534011_p4840629219555"></a><a name="en-us_topic_0118534011_p4840629219555"></a>22</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.91529152915292%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0118534011_p2859561419555"><a name="en-us_topic_0118534011_p2859561419555"></a><a name="en-us_topic_0118534011_p2859561419555"></a>IPv4 CIDR block or ID of another security group</p>
    <p id="en-us_topic_0118534011_p62410334191747"><a name="en-us_topic_0118534011_p62410334191747"></a><a name="en-us_topic_0118534011_p62410334191747"></a>For example, 192.168.20.2/32</p>
    </td>
    </tr>
    </tbody>
    </table>


## Remotely Connecting to Linux ECSs Using SSH<a name="en-us_topic_0118534011_section115069253338"></a>

-   Example scenario:

    After creating Linux ECSs, you can add a security group rule to enable remote SSH access to the Linux ECSs.

-   Security group configuration:

    <a name="en-us_topic_0118534011_table16351717123312"></a>
    <table><thead align="left"><tr id="en-us_topic_0118534011_row19634417153313"><th class="cellrowborder" valign="top" width="14.649999999999999%" id="mcps1.1.5.1.1"><p id="en-us_topic_0118534011_p96349178332"><a name="en-us_topic_0118534011_p96349178332"></a><a name="en-us_topic_0118534011_p96349178332"></a><strong id="en-us_topic_0118534011_b96481030171110"><a name="en-us_topic_0118534011_b96481030171110"></a><a name="en-us_topic_0118534011_b96481030171110"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.779999999999998%" id="mcps1.1.5.1.2"><p id="en-us_topic_0118534011_p0634141717339"><a name="en-us_topic_0118534011_p0634141717339"></a><a name="en-us_topic_0118534011_p0634141717339"></a><strong id="en-us_topic_0118534011_b20568193181112"><a name="en-us_topic_0118534011_b20568193181112"></a><a name="en-us_topic_0118534011_b20568193181112"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.22%" id="mcps1.1.5.1.3"><p id="en-us_topic_0118534011_p19634717103313"><a name="en-us_topic_0118534011_p19634717103313"></a><a name="en-us_topic_0118534011_p19634717103313"></a><strong id="en-us_topic_0118534011_b13935183291110"><a name="en-us_topic_0118534011_b13935183291110"></a><a name="en-us_topic_0118534011_b13935183291110"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.35%" id="mcps1.1.5.1.4"><p id="en-us_topic_0118534011_p166348179336"><a name="en-us_topic_0118534011_p166348179336"></a><a name="en-us_topic_0118534011_p166348179336"></a><strong id="en-us_topic_0118534011_b2110143631114"><a name="en-us_topic_0118534011_b2110143631114"></a><a name="en-us_topic_0118534011_b2110143631114"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118534011_row17635217123314"><td class="cellrowborder" valign="top" width="14.649999999999999%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0118534011_p863501710331"><a name="en-us_topic_0118534011_p863501710331"></a><a name="en-us_topic_0118534011_p863501710331"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.779999999999998%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0118534011_p1663551718336"><a name="en-us_topic_0118534011_p1663551718336"></a><a name="en-us_topic_0118534011_p1663551718336"></a>SSH (22)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0118534011_p5635417133313"><a name="en-us_topic_0118534011_p5635417133313"></a><a name="en-us_topic_0118534011_p5635417133313"></a>22</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.35%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0118534011_p166353177333"><a name="en-us_topic_0118534011_p166353177333"></a><a name="en-us_topic_0118534011_p166353177333"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


## Remotely Connecting to Windows ECSs Using RDP<a name="en-us_topic_0118534011_section168046312349"></a>

-   Example scenario:

    After creating Windows ECSs, you can add a security group rule to enable remote RDP access to the Windows ECSs.

-   Security group configuration:

    <a name="en-us_topic_0118534011_table129650323711"></a>
    <table><thead align="left"><tr id="en-us_topic_0118534011_row145116433715"><th class="cellrowborder" valign="top" width="13.84%" id="mcps1.1.5.1.1"><p id="en-us_topic_0118534011_p155113453713"><a name="en-us_topic_0118534011_p155113453713"></a><a name="en-us_topic_0118534011_p155113453713"></a><strong id="en-us_topic_0118534011_b629416239134"><a name="en-us_topic_0118534011_b629416239134"></a><a name="en-us_topic_0118534011_b629416239134"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.590000000000003%" id="mcps1.1.5.1.2"><p id="en-us_topic_0118534011_p165113443717"><a name="en-us_topic_0118534011_p165113443717"></a><a name="en-us_topic_0118534011_p165113443717"></a><strong id="en-us_topic_0118534011_b11162247131"><a name="en-us_topic_0118534011_b11162247131"></a><a name="en-us_topic_0118534011_b11162247131"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.47%" id="mcps1.1.5.1.3"><p id="en-us_topic_0118534011_p155214163719"><a name="en-us_topic_0118534011_p155214163719"></a><a name="en-us_topic_0118534011_p155214163719"></a><strong id="en-us_topic_0118534011_b595842441314"><a name="en-us_topic_0118534011_b595842441314"></a><a name="en-us_topic_0118534011_b595842441314"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.1%" id="mcps1.1.5.1.4"><p id="en-us_topic_0118534011_p952142371"><a name="en-us_topic_0118534011_p952142371"></a><a name="en-us_topic_0118534011_p952142371"></a><strong id="en-us_topic_0118534011_b8638162571317"><a name="en-us_topic_0118534011_b8638162571317"></a><a name="en-us_topic_0118534011_b8638162571317"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118534011_row18528416375"><td class="cellrowborder" valign="top" width="13.84%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0118534011_p8521445370"><a name="en-us_topic_0118534011_p8521445370"></a><a name="en-us_topic_0118534011_p8521445370"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.590000000000003%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0118534011_p452446375"><a name="en-us_topic_0118534011_p452446375"></a><a name="en-us_topic_0118534011_p452446375"></a>RDP (3389)</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.47%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0118534011_p125215413371"><a name="en-us_topic_0118534011_p125215413371"></a><a name="en-us_topic_0118534011_p125215413371"></a>3389</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.1%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0118534011_p155219414376"><a name="en-us_topic_0118534011_p155219414376"></a><a name="en-us_topic_0118534011_p155219414376"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


## Enabling Communication Between ECSs<a name="en-us_topic_0118534011_section34721049193411"></a>

-   Example scenario:

    After creating ECSs, you need to add a security group rule so that you can run the  **ping**  command to test communication between the ECSs.

-   Security group configuration:

    <a name="en-us_topic_0118534011_table810055173719"></a>
    <table><thead align="left"><tr id="en-us_topic_0118534011_row0160051103719"><th class="cellrowborder" valign="top" width="16.7%" id="mcps1.1.5.1.1"><p id="en-us_topic_0118534011_p2160251153718"><a name="en-us_topic_0118534011_p2160251153718"></a><a name="en-us_topic_0118534011_p2160251153718"></a><strong id="en-us_topic_0118534011_b817717513146"><a name="en-us_topic_0118534011_b817717513146"></a><a name="en-us_topic_0118534011_b817717513146"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.73%" id="mcps1.1.5.1.2"><p id="en-us_topic_0118534011_p141601751113715"><a name="en-us_topic_0118534011_p141601751113715"></a><a name="en-us_topic_0118534011_p141601751113715"></a><strong id="en-us_topic_0118534011_b2703157121418"><a name="en-us_topic_0118534011_b2703157121418"></a><a name="en-us_topic_0118534011_b2703157121418"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.47%" id="mcps1.1.5.1.3"><p id="en-us_topic_0118534011_p14160165111379"><a name="en-us_topic_0118534011_p14160165111379"></a><a name="en-us_topic_0118534011_p14160165111379"></a><strong id="en-us_topic_0118534011_b183020117149"><a name="en-us_topic_0118534011_b183020117149"></a><a name="en-us_topic_0118534011_b183020117149"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.1%" id="mcps1.1.5.1.4"><p id="en-us_topic_0118534011_p161601651183720"><a name="en-us_topic_0118534011_p161601651183720"></a><a name="en-us_topic_0118534011_p161601651183720"></a><strong id="en-us_topic_0118534011_b1961815117140"><a name="en-us_topic_0118534011_b1961815117140"></a><a name="en-us_topic_0118534011_b1961815117140"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118534011_row1216175110371"><td class="cellrowborder" valign="top" width="16.7%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0118534011_p5161175117373"><a name="en-us_topic_0118534011_p5161175117373"></a><a name="en-us_topic_0118534011_p5161175117373"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.73%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0118534011_p816119517376"><a name="en-us_topic_0118534011_p816119517376"></a><a name="en-us_topic_0118534011_p816119517376"></a>ICMP</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.47%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0118534011_p11161205112375"><a name="en-us_topic_0118534011_p11161205112375"></a><a name="en-us_topic_0118534011_p11161205112375"></a>All</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.1%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0118534011_p1316155143713"><a name="en-us_topic_0118534011_p1316155143713"></a><a name="en-us_topic_0118534011_p1316155143713"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


## Hosting a Website on ECSs<a name="en-us_topic_0118534011_section1517991516357"></a>

-   Example scenario:

    If you deploy a website on your ECSs and require that your website be accessed over HTTP or HTTPS, you can add rules to the security group used by the ECSs that function as the web servers.

-   Security group configuration:

    <a name="en-us_topic_0118534011_table30323767195135"></a>
    <table><thead align="left"><tr id="en-us_topic_0118534011_row15770184195135"><th class="cellrowborder" valign="top" width="17.611761176117614%" id="mcps1.1.5.1.1"><p id="en-us_topic_0118534011_p53423553195135"><a name="en-us_topic_0118534011_p53423553195135"></a><a name="en-us_topic_0118534011_p53423553195135"></a><strong id="en-us_topic_0118534011_b659583018152"><a name="en-us_topic_0118534011_b659583018152"></a><a name="en-us_topic_0118534011_b659583018152"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.17231723172317%" id="mcps1.1.5.1.2"><p id="en-us_topic_0118534011_p2316559195135"><a name="en-us_topic_0118534011_p2316559195135"></a><a name="en-us_topic_0118534011_p2316559195135"></a><strong id="en-us_topic_0118534011_b9364183851519"><a name="en-us_topic_0118534011_b9364183851519"></a><a name="en-us_topic_0118534011_b9364183851519"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.203120312031203%" id="mcps1.1.5.1.3"><p id="en-us_topic_0118534011_p32340552195135"><a name="en-us_topic_0118534011_p32340552195135"></a><a name="en-us_topic_0118534011_p32340552195135"></a><strong id="en-us_topic_0118534011_b3222439161517"><a name="en-us_topic_0118534011_b3222439161517"></a><a name="en-us_topic_0118534011_b3222439161517"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.012801280128013%" id="mcps1.1.5.1.4"><p id="en-us_topic_0118534011_p2339084195135"><a name="en-us_topic_0118534011_p2339084195135"></a><a name="en-us_topic_0118534011_p2339084195135"></a><strong id="en-us_topic_0118534011_b885615391151"><a name="en-us_topic_0118534011_b885615391151"></a><a name="en-us_topic_0118534011_b885615391151"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118534011_row55248116195135"><td class="cellrowborder" valign="top" width="17.611761176117614%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0118534011_p27918930195135"><a name="en-us_topic_0118534011_p27918930195135"></a><a name="en-us_topic_0118534011_p27918930195135"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.17231723172317%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0118534011_p45912425195135"><a name="en-us_topic_0118534011_p45912425195135"></a><a name="en-us_topic_0118534011_p45912425195135"></a>HTTP (80)</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.203120312031203%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0118534011_p46840856195135"><a name="en-us_topic_0118534011_p46840856195135"></a><a name="en-us_topic_0118534011_p46840856195135"></a>80</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.012801280128013%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0118534011_p36012962195135"><a name="en-us_topic_0118534011_p36012962195135"></a><a name="en-us_topic_0118534011_p36012962195135"></a>0.0.0.0/0</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534011_row5566305020026"><td class="cellrowborder" valign="top" width="17.611761176117614%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0118534011_p4461017620026"><a name="en-us_topic_0118534011_p4461017620026"></a><a name="en-us_topic_0118534011_p4461017620026"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.17231723172317%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0118534011_p3120540920026"><a name="en-us_topic_0118534011_p3120540920026"></a><a name="en-us_topic_0118534011_p3120540920026"></a>HTTPS (443)</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.203120312031203%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0118534011_p5665449220026"><a name="en-us_topic_0118534011_p5665449220026"></a><a name="en-us_topic_0118534011_p5665449220026"></a>443</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.012801280128013%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0118534011_p2561110020026"><a name="en-us_topic_0118534011_p2561110020026"></a><a name="en-us_topic_0118534011_p2561110020026"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


## Enabling an ECS to Function as a DNS Server<a name="en-us_topic_0118534011_section2910346123520"></a>

-   Example scenario:

    If you need to use an ECS as a DNS server, you must allow TCP and UDP access from port 53 to the DNS server. You can add the following rules to the security group associated with the ECS.

-   Security group configuration:

    <a name="en-us_topic_0118534011_table9719143933517"></a>
    <table><thead align="left"><tr id="en-us_topic_0118534011_row371953993514"><th class="cellrowborder" valign="top" width="16.711671167116712%" id="mcps1.1.5.1.1"><p id="en-us_topic_0118534011_p77202395359"><a name="en-us_topic_0118534011_p77202395359"></a><a name="en-us_topic_0118534011_p77202395359"></a><strong id="en-us_topic_0118534011_b57571227181619"><a name="en-us_topic_0118534011_b57571227181619"></a><a name="en-us_topic_0118534011_b57571227181619"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.072407240724072%" id="mcps1.1.5.1.2"><p id="en-us_topic_0118534011_p107201939133514"><a name="en-us_topic_0118534011_p107201939133514"></a><a name="en-us_topic_0118534011_p107201939133514"></a><strong id="en-us_topic_0118534011_b9830202821610"><a name="en-us_topic_0118534011_b9830202821610"></a><a name="en-us_topic_0118534011_b9830202821610"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.203120312031203%" id="mcps1.1.5.1.3"><p id="en-us_topic_0118534011_p07201398353"><a name="en-us_topic_0118534011_p07201398353"></a><a name="en-us_topic_0118534011_p07201398353"></a><strong id="en-us_topic_0118534011_b139231629111618"><a name="en-us_topic_0118534011_b139231629111618"></a><a name="en-us_topic_0118534011_b139231629111618"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.012801280128013%" id="mcps1.1.5.1.4"><p id="en-us_topic_0118534011_p157201239183513"><a name="en-us_topic_0118534011_p157201239183513"></a><a name="en-us_topic_0118534011_p157201239183513"></a><strong id="en-us_topic_0118534011_b1177753015164"><a name="en-us_topic_0118534011_b1177753015164"></a><a name="en-us_topic_0118534011_b1177753015164"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118534011_row87211239133515"><td class="cellrowborder" valign="top" width="16.711671167116712%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0118534011_p2721163963512"><a name="en-us_topic_0118534011_p2721163963512"></a><a name="en-us_topic_0118534011_p2721163963512"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0118534011_p16721163916353"><a name="en-us_topic_0118534011_p16721163916353"></a><a name="en-us_topic_0118534011_p16721163916353"></a>TCP</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.203120312031203%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0118534011_p1672119392358"><a name="en-us_topic_0118534011_p1672119392358"></a><a name="en-us_topic_0118534011_p1672119392358"></a>53</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.012801280128013%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0118534011_p672163953517"><a name="en-us_topic_0118534011_p672163953517"></a><a name="en-us_topic_0118534011_p672163953517"></a>0.0.0.0/0</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534011_row127214392355"><td class="cellrowborder" valign="top" width="16.711671167116712%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0118534011_p1721739123511"><a name="en-us_topic_0118534011_p1721739123511"></a><a name="en-us_topic_0118534011_p1721739123511"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0118534011_p207221139183518"><a name="en-us_topic_0118534011_p207221139183518"></a><a name="en-us_topic_0118534011_p207221139183518"></a>UDP</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.203120312031203%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0118534011_p3722133933514"><a name="en-us_topic_0118534011_p3722133933514"></a><a name="en-us_topic_0118534011_p3722133933514"></a>53</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.012801280128013%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0118534011_p3722439103510"><a name="en-us_topic_0118534011_p3722439103510"></a><a name="en-us_topic_0118534011_p3722439103510"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


## Uploading or Downloading Files Using FTP<a name="en-us_topic_0118534011_section5964121693610"></a>

-   Example scenario:

    If you want to use File Transfer Protocol \(FTP\) to upload files to or download files from ECSs, you need to add a security group rule.

    >![](/images/icon-note.gif) **NOTE:**   
    >You must first install the FTP server program on the ECSs and check whether ports 20 and 21 are working properly.   

-   Security group configuration:

    <a name="en-us_topic_0118534011_table8479153013395"></a>
    <table><thead align="left"><tr id="en-us_topic_0118534011_row1518203013392"><th class="cellrowborder" valign="top" width="16.17%" id="mcps1.1.5.1.1"><p id="en-us_topic_0118534011_p13518730193918"><a name="en-us_topic_0118534011_p13518730193918"></a><a name="en-us_topic_0118534011_p13518730193918"></a><strong id="en-us_topic_0118534011_b16647191041714"><a name="en-us_topic_0118534011_b16647191041714"></a><a name="en-us_topic_0118534011_b16647191041714"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.26%" id="mcps1.1.5.1.2"><p id="en-us_topic_0118534011_p1651819306397"><a name="en-us_topic_0118534011_p1651819306397"></a><a name="en-us_topic_0118534011_p1651819306397"></a><strong id="en-us_topic_0118534011_b4518131111171"><a name="en-us_topic_0118534011_b4518131111171"></a><a name="en-us_topic_0118534011_b4518131111171"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.47%" id="mcps1.1.5.1.3"><p id="en-us_topic_0118534011_p175183303395"><a name="en-us_topic_0118534011_p175183303395"></a><a name="en-us_topic_0118534011_p175183303395"></a><strong id="en-us_topic_0118534011_b2393161214175"><a name="en-us_topic_0118534011_b2393161214175"></a><a name="en-us_topic_0118534011_b2393161214175"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.1%" id="mcps1.1.5.1.4"><p id="en-us_topic_0118534011_p3518163053913"><a name="en-us_topic_0118534011_p3518163053913"></a><a name="en-us_topic_0118534011_p3518163053913"></a><strong id="en-us_topic_0118534011_b1414191319178"><a name="en-us_topic_0118534011_b1414191319178"></a><a name="en-us_topic_0118534011_b1414191319178"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118534011_row4519143013399"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0118534011_p13519123013393"><a name="en-us_topic_0118534011_p13519123013393"></a><a name="en-us_topic_0118534011_p13519123013393"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.26%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0118534011_p10519113063920"><a name="en-us_topic_0118534011_p10519113063920"></a><a name="en-us_topic_0118534011_p10519113063920"></a>TCP</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.47%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0118534011_p5519930193917"><a name="en-us_topic_0118534011_p5519930193917"></a><a name="en-us_topic_0118534011_p5519930193917"></a>20-21</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.1%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0118534011_p13519630123910"><a name="en-us_topic_0118534011_p13519630123910"></a><a name="en-us_topic_0118534011_p13519630123910"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


