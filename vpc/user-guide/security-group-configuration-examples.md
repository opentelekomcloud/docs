# Security Group Configuration Examples<a name="en-us_topic_0081124350"></a>

Common security group configurations are presented here. The examples in this section allow all outgoing data packets by default. This section will only describe how to configure inbound rules.

-   <a name="li2921164192410"></a>[Allowing External Access to a Specified Port](#li2921164192410)
-   [Enabling ECSs in Different Security Groups to Communicate with Each Other Through an Internal Network](#section14197522283)
-   [Enabling Specified IP Addresses to Remotely Access ECSs in a Security Group](#section17693183118306)
-   [Remotely Connecting to Linux ECSs Using SSH](#section115069253338)
-   [Remotely Connecting to Windows ECSs Using RDP](#section168046312349)
-   [Enabling Communication Between ECSs](#section34721049193411)
-   [Hosting a Website on ECSs](#section1517991516357)
-   [Enabling an ECS to Function as a DNS Server](#section2910346123520)
-   [Uploading or Downloading Files Using FTP](#section5964121693610)

You can use the default security group or create a security group in advance. For details, see sections  [Creating a Security Group](creating-a-security-group.md)  and  [Adding a Security Group Rule](adding-a-security-group-rule.md).

## Allowing External Access to a Specified Port<a name="section128977321300"></a>

-   Example scenario:

    After services are deployed, you can add security group rules to allow external access to a specified port \(for example, 1100\).

-   Security group configuration:

    <a name="table07907420339"></a>
    <table><thead align="left"><tr id="row127902042103316"><th class="cellrowborder" valign="top" width="12.400000000000002%" id="mcps1.1.5.1.1"><p id="p13791114217333"><a name="p13791114217333"></a><a name="p13791114217333"></a><strong id="b96481030171110"><a name="b96481030171110"></a><a name="b96481030171110"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.43000000000001%" id="mcps1.1.5.1.2"><p id="p37917422334"><a name="p37917422334"></a><a name="p37917422334"></a><strong id="b842352706104812"><a name="b842352706104812"></a><a name="b842352706104812"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.810000000000002%" id="mcps1.1.5.1.3"><p id="p779174215330"><a name="p779174215330"></a><a name="p779174215330"></a><strong id="b842352706161911_1"><a name="b842352706161911_1"></a><a name="b842352706161911_1"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.360000000000003%" id="mcps1.1.5.1.4"><p id="p579110423330"><a name="p579110423330"></a><a name="p579110423330"></a><strong id="en-us_topic_0118646266_en-us_topic_0118534005_b1665113556568"><a name="en-us_topic_0118646266_en-us_topic_0118534005_b1665113556568"></a><a name="en-us_topic_0118646266_en-us_topic_0118534005_b1665113556568"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row079115427333"><td class="cellrowborder" valign="top" width="12.400000000000002%" headers="mcps1.1.5.1.1 "><p id="p9791342133314"><a name="p9791342133314"></a><a name="p9791342133314"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.43000000000001%" headers="mcps1.1.5.1.2 "><p id="p37911428339"><a name="p37911428339"></a><a name="p37911428339"></a>TCP</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.810000000000002%" headers="mcps1.1.5.1.3 "><p id="p107911742123314"><a name="p107911742123314"></a><a name="p107911742123314"></a>1100</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.360000000000003%" headers="mcps1.1.5.1.4 "><p id="p590063763513"><a name="p590063763513"></a><a name="p590063763513"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


## Enabling ECSs in Different Security Groups to Communicate with Each Other Through an Internal Network<a name="section14197522283"></a>

-   Example scenario:

    In this scenario, resources on an ECS in a security group need to be copied to an ECS associated with another security group. The two ECSs are in the same VPC. We recommend that you enable internal network communication between the ECSs and then copy the resources.

-   Security group configuration:

    Within a given VPC, ECSs in the same security group can communicate with one another by default. However, ECSs in different security groups cannot communicate with each other by default. For the networks in these ECSs to communicate with each other, you must add certain security group rules.

    You can add an inbound rule to the security groups containing the ECSs to allow access from ECSs in the other security group. The required rule is as follows.

    <a name="table854766319358"></a>
    <table><thead align="left"><tr id="row2051403019358"><th class="cellrowborder" valign="top" width="12.400000000000002%" id="mcps1.1.5.1.1"><p id="p3928016319358"><a name="p3928016319358"></a><a name="p3928016319358"></a><strong id="en-us_topic_0118646266_en-us_topic_0118534005_b13723751135618"><a name="en-us_topic_0118646266_en-us_topic_0118534005_b13723751135618"></a><a name="en-us_topic_0118646266_en-us_topic_0118534005_b13723751135618"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.43000000000001%" id="mcps1.1.5.1.2"><p id="p5102371419358"><a name="p5102371419358"></a><a name="p5102371419358"></a><strong id="b842352706104812_1"><a name="b842352706104812_1"></a><a name="b842352706104812_1"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.810000000000002%" id="mcps1.1.5.1.3"><p id="p2415644494621"><a name="p2415644494621"></a><a name="p2415644494621"></a><strong id="b842352706161911_1_1"><a name="b842352706161911_1_1"></a><a name="b842352706161911_1_1"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.360000000000003%" id="mcps1.1.5.1.4"><p id="p1911210519358"><a name="p1911210519358"></a><a name="p1911210519358"></a><strong id="en-us_topic_0118646266_en-us_topic_0118534005_b1665113556568_1"><a name="en-us_topic_0118646266_en-us_topic_0118534005_b1665113556568_1"></a><a name="en-us_topic_0118646266_en-us_topic_0118534005_b1665113556568_1"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3779122419358"><td class="cellrowborder" valign="top" width="12.400000000000002%" headers="mcps1.1.5.1.1 "><p id="p4808290419358"><a name="p4808290419358"></a><a name="p4808290419358"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.43000000000001%" headers="mcps1.1.5.1.2 "><p id="p4119033619358"><a name="p4119033619358"></a><a name="p4119033619358"></a>Used for communication through an internal network</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.810000000000002%" headers="mcps1.1.5.1.3 "><p id="p4640703694621"><a name="p4640703694621"></a><a name="p4640703694621"></a>Port or port range</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.360000000000003%" headers="mcps1.1.5.1.4 "><p id="p6027368919358"><a name="p6027368919358"></a><a name="p6027368919358"></a>ID of another security group</p>
    </td>
    </tr>
    </tbody>
    </table>


## Enabling Specified IP Addresses to Remotely Access ECSs in a Security Group<a name="section17693183118306"></a>

-   Example scenario:

    To prevent ECSs from being attacked, you can change the port number for remote login and configure security group rules that allow only specified IP addresses to remotely access the ECSs.

-   Security group configuration:

    To allow IP address  **192.168.20.2**  to remotely access Linux ECSs in a security group over the SSH protocol \(port 22\), you can configure the following security group rule.

    <a name="table2497622119555"></a>
    <table><thead align="left"><tr id="row407563919555"><th class="cellrowborder" valign="top" width="12.04120412041204%" id="mcps1.1.5.1.1"><p id="p181361106345"><a name="p181361106345"></a><a name="p181361106345"></a><strong id="b137891355798"><a name="b137891355798"></a><a name="b137891355798"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.51185118511851%" id="mcps1.1.5.1.2"><p id="p6169135719555"><a name="p6169135719555"></a><a name="p6169135719555"></a><strong id="b62878816103"><a name="b62878816103"></a><a name="b62878816103"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.53165316531653%" id="mcps1.1.5.1.3"><p id="p2343829819555"><a name="p2343829819555"></a><a name="p2343829819555"></a><strong id="b9902119131013"><a name="b9902119131013"></a><a name="b9902119131013"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.91529152915292%" id="mcps1.1.5.1.4"><p id="p1945401819555"><a name="p1945401819555"></a><a name="p1945401819555"></a><strong id="b1742151071014"><a name="b1742151071014"></a><a name="b1742151071014"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3227161019555"><td class="cellrowborder" valign="top" width="12.04120412041204%" headers="mcps1.1.5.1.1 "><p id="p313671093414"><a name="p313671093414"></a><a name="p313671093414"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.51185118511851%" headers="mcps1.1.5.1.2 "><p id="p6386359419555"><a name="p6386359419555"></a><a name="p6386359419555"></a>SSH (22)</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.53165316531653%" headers="mcps1.1.5.1.3 "><p id="p4840629219555"><a name="p4840629219555"></a><a name="p4840629219555"></a>22</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.91529152915292%" headers="mcps1.1.5.1.4 "><p id="p2859561419555"><a name="p2859561419555"></a><a name="p2859561419555"></a>IPv4 CIDR block or ID of another security group</p>
    <p id="p62410334191747"><a name="p62410334191747"></a><a name="p62410334191747"></a>For example, 192.168.20.2/32</p>
    </td>
    </tr>
    </tbody>
    </table>


## Remotely Connecting to Linux ECSs Using SSH<a name="section115069253338"></a>

-   Example scenario:

    After creating Linux ECSs, you can add a security group rule to enable remote SSH access to the Linux ECSs.

-   Security group configuration:

    <a name="table16351717123312"></a>
    <table><thead align="left"><tr id="row19634417153313"><th class="cellrowborder" valign="top" width="14.649999999999999%" id="mcps1.1.5.1.1"><p id="p96349178332"><a name="p96349178332"></a><a name="p96349178332"></a><strong id="b96481030171110_1"><a name="b96481030171110_1"></a><a name="b96481030171110_1"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.779999999999998%" id="mcps1.1.5.1.2"><p id="p0634141717339"><a name="p0634141717339"></a><a name="p0634141717339"></a><strong id="b20568193181112"><a name="b20568193181112"></a><a name="b20568193181112"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.22%" id="mcps1.1.5.1.3"><p id="p19634717103313"><a name="p19634717103313"></a><a name="p19634717103313"></a><strong id="b13935183291110"><a name="b13935183291110"></a><a name="b13935183291110"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.35%" id="mcps1.1.5.1.4"><p id="p166348179336"><a name="p166348179336"></a><a name="p166348179336"></a><strong id="b2110143631114"><a name="b2110143631114"></a><a name="b2110143631114"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17635217123314"><td class="cellrowborder" valign="top" width="14.649999999999999%" headers="mcps1.1.5.1.1 "><p id="p863501710331"><a name="p863501710331"></a><a name="p863501710331"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.779999999999998%" headers="mcps1.1.5.1.2 "><p id="p1663551718336"><a name="p1663551718336"></a><a name="p1663551718336"></a>SSH (22)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.5.1.3 "><p id="p5635417133313"><a name="p5635417133313"></a><a name="p5635417133313"></a>22</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.35%" headers="mcps1.1.5.1.4 "><p id="p166353177333"><a name="p166353177333"></a><a name="p166353177333"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


## Remotely Connecting to Windows ECSs Using RDP<a name="section168046312349"></a>

-   Example scenario:

    After creating Windows ECSs, you can add a security group rule to enable remote RDP access to the Windows ECSs.

-   Security group configuration:

    <a name="table129650323711"></a>
    <table><thead align="left"><tr id="row145116433715"><th class="cellrowborder" valign="top" width="13.84%" id="mcps1.1.5.1.1"><p id="p155113453713"><a name="p155113453713"></a><a name="p155113453713"></a><strong id="b629416239134"><a name="b629416239134"></a><a name="b629416239134"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.590000000000003%" id="mcps1.1.5.1.2"><p id="p165113443717"><a name="p165113443717"></a><a name="p165113443717"></a><strong id="b11162247131"><a name="b11162247131"></a><a name="b11162247131"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.47%" id="mcps1.1.5.1.3"><p id="p155214163719"><a name="p155214163719"></a><a name="p155214163719"></a><strong id="b595842441314"><a name="b595842441314"></a><a name="b595842441314"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.1%" id="mcps1.1.5.1.4"><p id="p952142371"><a name="p952142371"></a><a name="p952142371"></a><strong id="b8638162571317"><a name="b8638162571317"></a><a name="b8638162571317"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18528416375"><td class="cellrowborder" valign="top" width="13.84%" headers="mcps1.1.5.1.1 "><p id="p8521445370"><a name="p8521445370"></a><a name="p8521445370"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.590000000000003%" headers="mcps1.1.5.1.2 "><p id="p452446375"><a name="p452446375"></a><a name="p452446375"></a>RDP (3389)</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.47%" headers="mcps1.1.5.1.3 "><p id="p125215413371"><a name="p125215413371"></a><a name="p125215413371"></a>3389</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.1%" headers="mcps1.1.5.1.4 "><p id="p155219414376"><a name="p155219414376"></a><a name="p155219414376"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


## Enabling Communication Between ECSs<a name="section34721049193411"></a>

-   Example scenario:

    After creating ECSs, you need to add a security group rule so that you can run the  **ping**  command to test communication between the ECSs.

-   Security group configuration:

    <a name="table810055173719"></a>
    <table><thead align="left"><tr id="row0160051103719"><th class="cellrowborder" valign="top" width="16.7%" id="mcps1.1.5.1.1"><p id="p2160251153718"><a name="p2160251153718"></a><a name="p2160251153718"></a><strong id="b817717513146"><a name="b817717513146"></a><a name="b817717513146"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.73%" id="mcps1.1.5.1.2"><p id="p141601751113715"><a name="p141601751113715"></a><a name="p141601751113715"></a><strong id="b2703157121418"><a name="b2703157121418"></a><a name="b2703157121418"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.47%" id="mcps1.1.5.1.3"><p id="p14160165111379"><a name="p14160165111379"></a><a name="p14160165111379"></a><strong id="b183020117149"><a name="b183020117149"></a><a name="b183020117149"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.1%" id="mcps1.1.5.1.4"><p id="p161601651183720"><a name="p161601651183720"></a><a name="p161601651183720"></a><strong id="b1961815117140"><a name="b1961815117140"></a><a name="b1961815117140"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1216175110371"><td class="cellrowborder" valign="top" width="16.7%" headers="mcps1.1.5.1.1 "><p id="p5161175117373"><a name="p5161175117373"></a><a name="p5161175117373"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.73%" headers="mcps1.1.5.1.2 "><p id="p816119517376"><a name="p816119517376"></a><a name="p816119517376"></a>ICMP</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.47%" headers="mcps1.1.5.1.3 "><p id="p11161205112375"><a name="p11161205112375"></a><a name="p11161205112375"></a>All</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.1%" headers="mcps1.1.5.1.4 "><p id="p1316155143713"><a name="p1316155143713"></a><a name="p1316155143713"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


## Hosting a Website on ECSs<a name="section1517991516357"></a>

-   Example scenario:

    If you deploy a website on your ECSs and require that your website be accessed over HTTP or HTTPS, you can add rules to the security group used by the ECSs that function as the web servers.

-   Security group configuration:

    <a name="table30323767195135"></a>
    <table><thead align="left"><tr id="row15770184195135"><th class="cellrowborder" valign="top" width="17.611761176117614%" id="mcps1.1.5.1.1"><p id="p53423553195135"><a name="p53423553195135"></a><a name="p53423553195135"></a><strong id="b659583018152"><a name="b659583018152"></a><a name="b659583018152"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.17231723172317%" id="mcps1.1.5.1.2"><p id="p2316559195135"><a name="p2316559195135"></a><a name="p2316559195135"></a><strong id="b9364183851519"><a name="b9364183851519"></a><a name="b9364183851519"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.203120312031203%" id="mcps1.1.5.1.3"><p id="p32340552195135"><a name="p32340552195135"></a><a name="p32340552195135"></a><strong id="b3222439161517"><a name="b3222439161517"></a><a name="b3222439161517"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.012801280128013%" id="mcps1.1.5.1.4"><p id="p2339084195135"><a name="p2339084195135"></a><a name="p2339084195135"></a><strong id="b885615391151"><a name="b885615391151"></a><a name="b885615391151"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55248116195135"><td class="cellrowborder" valign="top" width="17.611761176117614%" headers="mcps1.1.5.1.1 "><p id="p27918930195135"><a name="p27918930195135"></a><a name="p27918930195135"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.17231723172317%" headers="mcps1.1.5.1.2 "><p id="p45912425195135"><a name="p45912425195135"></a><a name="p45912425195135"></a>HTTP (80)</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.203120312031203%" headers="mcps1.1.5.1.3 "><p id="p46840856195135"><a name="p46840856195135"></a><a name="p46840856195135"></a>80</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.012801280128013%" headers="mcps1.1.5.1.4 "><p id="p36012962195135"><a name="p36012962195135"></a><a name="p36012962195135"></a>0.0.0.0/0</p>
    </td>
    </tr>
    <tr id="row5566305020026"><td class="cellrowborder" valign="top" width="17.611761176117614%" headers="mcps1.1.5.1.1 "><p id="p4461017620026"><a name="p4461017620026"></a><a name="p4461017620026"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.17231723172317%" headers="mcps1.1.5.1.2 "><p id="p3120540920026"><a name="p3120540920026"></a><a name="p3120540920026"></a>HTTPS (443)</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.203120312031203%" headers="mcps1.1.5.1.3 "><p id="p5665449220026"><a name="p5665449220026"></a><a name="p5665449220026"></a>443</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.012801280128013%" headers="mcps1.1.5.1.4 "><p id="p2561110020026"><a name="p2561110020026"></a><a name="p2561110020026"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


## Enabling an ECS to Function as a DNS Server<a name="section2910346123520"></a>

-   Example scenario:

    If you need to use an ECS as a DNS server, you must allow TCP and UDP access from port 53 to the DNS server. You can add the following rules to the security group associated with the ECS.

-   Security group configuration:

    <a name="table9719143933517"></a>
    <table><thead align="left"><tr id="row371953993514"><th class="cellrowborder" valign="top" width="16.711671167116712%" id="mcps1.1.5.1.1"><p id="p77202395359"><a name="p77202395359"></a><a name="p77202395359"></a><strong id="b57571227181619"><a name="b57571227181619"></a><a name="b57571227181619"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.072407240724072%" id="mcps1.1.5.1.2"><p id="p107201939133514"><a name="p107201939133514"></a><a name="p107201939133514"></a><strong id="b9830202821610"><a name="b9830202821610"></a><a name="b9830202821610"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.203120312031203%" id="mcps1.1.5.1.3"><p id="p07201398353"><a name="p07201398353"></a><a name="p07201398353"></a><strong id="b139231629111618"><a name="b139231629111618"></a><a name="b139231629111618"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.012801280128013%" id="mcps1.1.5.1.4"><p id="p157201239183513"><a name="p157201239183513"></a><a name="p157201239183513"></a><strong id="b1177753015164"><a name="b1177753015164"></a><a name="b1177753015164"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row87211239133515"><td class="cellrowborder" valign="top" width="16.711671167116712%" headers="mcps1.1.5.1.1 "><p id="p2721163963512"><a name="p2721163963512"></a><a name="p2721163963512"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.1.5.1.2 "><p id="p16721163916353"><a name="p16721163916353"></a><a name="p16721163916353"></a>TCP</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.203120312031203%" headers="mcps1.1.5.1.3 "><p id="p1672119392358"><a name="p1672119392358"></a><a name="p1672119392358"></a>53</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.012801280128013%" headers="mcps1.1.5.1.4 "><p id="p672163953517"><a name="p672163953517"></a><a name="p672163953517"></a>0.0.0.0/0</p>
    </td>
    </tr>
    <tr id="row127214392355"><td class="cellrowborder" valign="top" width="16.711671167116712%" headers="mcps1.1.5.1.1 "><p id="p1721739123511"><a name="p1721739123511"></a><a name="p1721739123511"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.1.5.1.2 "><p id="p207221139183518"><a name="p207221139183518"></a><a name="p207221139183518"></a>UDP</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.203120312031203%" headers="mcps1.1.5.1.3 "><p id="p3722133933514"><a name="p3722133933514"></a><a name="p3722133933514"></a>53</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.012801280128013%" headers="mcps1.1.5.1.4 "><p id="p3722439103510"><a name="p3722439103510"></a><a name="p3722439103510"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


## Uploading or Downloading Files Using FTP<a name="section5964121693610"></a>

-   Example scenario:

    If you want to use File Transfer Protocol \(FTP\) to upload files to or download files from ECSs, you need to add a security group rule.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You must first install the FTP server program on the ECSs and check whether ports 20 and 21 are working properly.   

-   Security group configuration:

    <a name="table8479153013395"></a>
    <table><thead align="left"><tr id="row1518203013392"><th class="cellrowborder" valign="top" width="16.17%" id="mcps1.1.5.1.1"><p id="p13518730193918"><a name="p13518730193918"></a><a name="p13518730193918"></a><strong id="b16647191041714"><a name="b16647191041714"></a><a name="b16647191041714"></a>Direction</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.26%" id="mcps1.1.5.1.2"><p id="p1651819306397"><a name="p1651819306397"></a><a name="p1651819306397"></a><strong id="b4518131111171"><a name="b4518131111171"></a><a name="b4518131111171"></a>Protocol/Application</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.47%" id="mcps1.1.5.1.3"><p id="p175183303395"><a name="p175183303395"></a><a name="p175183303395"></a><strong id="b2393161214175"><a name="b2393161214175"></a><a name="b2393161214175"></a>Port</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.1%" id="mcps1.1.5.1.4"><p id="p3518163053913"><a name="p3518163053913"></a><a name="p3518163053913"></a><strong id="b1414191319178"><a name="b1414191319178"></a><a name="b1414191319178"></a>Source</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4519143013399"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p13519123013393"><a name="p13519123013393"></a><a name="p13519123013393"></a>Inbound</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.26%" headers="mcps1.1.5.1.2 "><p id="p10519113063920"><a name="p10519113063920"></a><a name="p10519113063920"></a>TCP</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.47%" headers="mcps1.1.5.1.3 "><p id="p5519930193917"><a name="p5519930193917"></a><a name="p5519930193917"></a>20-21</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.1%" headers="mcps1.1.5.1.4 "><p id="p13519630123910"><a name="p13519630123910"></a><a name="p13519630123910"></a>0.0.0.0/0</p>
    </td>
    </tr>
    </tbody>
    </table>


