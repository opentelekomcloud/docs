# Using a New Specifications Template to Create an AS Configuration<a name="EN-US_TOPIC_0042018364"></a>

## Scenarios<a name="section2495449014355"></a>

If you have special requirements on the ECSs for resource expansion, use a new specifications template to create the AS configuration. In such a case, ECSs meeting specifications of the template will be added to the AS group in scaling actions.

## Procedure<a name="section1657416306249"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
4.  Click  **Create AS Configuration**.
5.  Set the parameters for the AS configuration.  [Table 1](#table52838201145822)  lists the AS configuration parameters.

    **Table  1**  AS configuration parameters

    <a name="table52838201145822"></a>
    <table><thead align="left"><tr id="row25161034145822"><th class="cellrowborder" valign="top" width="19.400000000000002%" id="mcps1.2.4.1.1"><p id="p2684068145822"><a name="p2684068145822"></a><a name="p2684068145822"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.480000000000004%" id="mcps1.2.4.1.2"><p id="p16082959145822"><a name="p16082959145822"></a><a name="p16082959145822"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.120000000000005%" id="mcps1.2.4.1.3"><p id="p27651278145822"><a name="p27651278145822"></a><a name="p27651278145822"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row115001543115515"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p650034375512"><a name="p650034375512"></a><a name="p650034375512"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p17184175316413"><a name="p17184175316413"></a><a name="p17184175316413"></a>A region is where an AS configuration resides.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p1650024313554"><a name="p1650024313554"></a><a name="p1650024313554"></a>N/A</p>
    </td>
    </tr>
    <tr id="row56995381145822"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p24777834145822"><a name="p24777834145822"></a><a name="p24777834145822"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p60847510145822"><a name="p60847510145822"></a><a name="p60847510145822"></a>Specifies the name of an AS configuration.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p29701303145822"><a name="p29701303145822"></a><a name="p29701303145822"></a>N/A</p>
    </td>
    </tr>
    <tr id="row59477353145822"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p43196386145822"><a name="p43196386145822"></a><a name="p43196386145822"></a>Configuration Template</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p9246390145822"><a name="p9246390145822"></a><a name="p9246390145822"></a>Select <strong id="b842352706153554"><a name="b842352706153554"></a><a name="b842352706153554"></a>Create a new specifications template</strong>.</p>
    <p id="p16108646145822"><a name="p16108646145822"></a><a name="p16108646145822"></a>If this option is selected, configure parameters, such as the vCPUs, memory, image, disk, and ECS type, to create a new AS configuration.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p29731945145822"><a name="p29731945145822"></a><a name="p29731945145822"></a>Create a new specifications template</p>
    </td>
    </tr>
    <tr id="row32564048145822"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p1738024812366"><a name="p1738024812366"></a><a name="p1738024812366"></a>Specifications</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1284784410497"><a name="p1284784410497"></a><a name="p1284784410497"></a>The public cloud provides various ECS types for different application scenarios.</p>
    <p id="p61271243145822"><a name="p61271243145822"></a><a name="p61271243145822"></a>For more information, see <em id="i842352697104052"><a name="i842352697104052"></a><a name="i842352697104052"></a></em><em id="i84235269710413"><a name="i84235269710413"></a><a name="i84235269710413"></a></em><em id="i17884249004"><a name="i17884249004"></a><a name="i17884249004"></a>Elastic Cloud Server User Guide</em>.</p>
    <p id="p14570276145822"><a name="p14570276145822"></a><a name="p14570276145822"></a>Configure the ECS specifications, including vCPUs, memory, image type, and disk, according to the ECS type.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p39341736145822"><a name="p39341736145822"></a><a name="p39341736145822"></a>Memory-optimized ECS</p>
    </td>
    </tr>
    <tr id="row13585817145822"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p6905151611150"><a name="p6905151611150"></a><a name="p6905151611150"></a>Image</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.480000000000004%" headers="mcps1.2.4.1.2 "><a name="ul19190643145822"></a><a name="ul19190643145822"></a><ul id="ul19190643145822"><li>Public image<p id="p49762479145822"><a name="p49762479145822"></a><a name="p49762479145822"></a>A public image is a standard, widely used image. It contains an OS and preinstalled public applications and is available to all users. You can configure the applications or software in the public image as needed.</p>
    </li><li>Private image<p id="p4229026145822"><a name="p4229026145822"></a><a name="p4229026145822"></a>A private image is an image available only to the user who created it. It contains an OS, preinstalled public applications, and the user's private applications. Using a private image to create ECSs removes the need to configure multiple ECSs repeatedly.</p>
    <div class="note" id="note18690304145822"><a name="note18690304145822"></a><a name="note18690304145822"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p38061236145822"><a name="p38061236145822"></a><a name="p38061236145822"></a>If you select an encrypted image, you must grant key management system (KMS) access rights to EVS. Otherwise, encryption cannot be used. If you have rights granting permission, grant the KMS access rights to EVS. If you do not have the permission, contact the user having the security administrator rights to grant the KMS access rights. For details, see <em id="i1976236060153736"><a name="i1976236060153736"></a><a name="i1976236060153736"></a>Identity and Access Management User Guide</em>.</p>
    <a name="ul7687284145822"></a><a name="ul7687284145822"></a><ul id="ul7687284145822"><li><strong id="b842352706124911"><a name="b842352706124911"></a><a name="b842352706124911"></a>Encrypted</strong>: indicates that the image has been encrypted.</li><li><strong id="b842352706124926"><a name="b842352706124926"></a><a name="b842352706124926"></a>KMS Key Name</strong>: specifies the name of the key used by the encrypted image. By default, the name is <strong id="b2061600687153535"><a name="b2061600687153535"></a><a name="b2061600687153535"></a>ims/default</strong>.</li><li><strong id="b84235270612501"><a name="b84235270612501"></a><a name="b84235270612501"></a>Xrole Name: EVSAccessKMS</strong>: indicates that EVS has obtained the KMS access rights.</li></ul>
    <p id="p2076700145822"><a name="p2076700145822"></a><a name="p2076700145822"></a>For more information about encrypted images, see <em id="i8423526979632"><a name="i8423526979632"></a><a name="i8423526979632"></a>Image Management Service User Guide</em>.</p>
    </div></div>
    </li><li>Shared image<p id="p37519623145822"><a name="p37519623145822"></a><a name="p37519623145822"></a>A shared image is a private image shared by another public cloud system user.</p>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="25.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p10938284145822"><a name="p10938284145822"></a><a name="p10938284145822"></a>Public image</p>
    </td>
    </tr>
    <tr id="row25196531145822"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p55163495145822"><a name="p55163495145822"></a><a name="p55163495145822"></a>License Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p15978673145822"><a name="p15978673145822"></a><a name="p15978673145822"></a>Specifies a license type for using an OS or software on the public cloud platform. If the image you selected is free of charge, this parameter is unavailable. If the image you selected is billed, such as an Ubuntu, SUSE, Oracle Linux, or Windows Server Edition image, this parameter is available.</p>
    <a name="ul41174486145822"></a><a name="ul41174486145822"></a><ul id="ul41174486145822"><li>Use license from the system<p id="p9590333145822"><a name="p9590333145822"></a><a name="p9590333145822"></a>Allows you to use the license provided by the public cloud platform. Obtaining the authorization of such a license is billed.</p>
    </li><li>Bring your own license (BYOL)<p id="p38619533145822"><a name="p38619533145822"></a><a name="p38619533145822"></a>Allows you to use your existing OS license. In such a case, you do not need to apply for a license again.</p>
    </li></ul>
    <p id="p35026055145822"><a name="p35026055145822"></a><a name="p35026055145822"></a>For more information about the license type, see <em id="i1103164017461"><a name="i1103164017461"></a><a name="i1103164017461"></a><a href="https://docs.otc.t-systems.com/usermanual/ecs/en-us_topic_0046566932.html" target="_blank" rel="noopener noreferrer">Elastic Cloud Server User Guide</a></em><em id="i210419402467"><a name="i210419402467"></a><a name="i210419402467"></a></em>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p18538167145822"><a name="p18538167145822"></a><a name="p18538167145822"></a>Bring your own license (BYOL)</p>
    </td>
    </tr>
    <tr id="row5315896145822"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p25442194145822"><a name="p25442194145822"></a><a name="p25442194145822"></a>Disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.480000000000004%" headers="mcps1.2.4.1.2 "><div class="p" id="p32166422145822"><a name="p32166422145822"></a><a name="p32166422145822"></a>Includes system disks and data disks. <a name="ul21763225564"></a><a name="ul21763225564"></a><ul id="ul21763225564"><li><strong id="b117116611815"><a name="b117116611815"></a><a name="b117116611815"></a>System Disk</strong><p id="p15176152285615"><a name="p15176152285615"></a><a name="p15176152285615"></a><strong id="b842352706172120"><a name="b842352706172120"></a><a name="b842352706172120"></a>Common I/O</strong>: uses Serial Advanced Technology Attachment (SATA) drives to store data.</p>
    <p id="p18176722105616"><a name="p18176722105616"></a><a name="p18176722105616"></a><strong id="b842352706172150"><a name="b842352706172150"></a><a name="b842352706172150"></a>High I/O</strong>: uses serial attached SCSI (SAS) drives to store data.</p>
    <p id="p1917642219563"><a name="p1917642219563"></a><a name="p1917642219563"></a><strong id="b287884235"><a name="b287884235"></a><a name="b287884235"></a>Ultra-high I/O</strong>: uses solid state disk (SSD) drives to store data.</p>
    <p id="p817618229565"><a name="p817618229565"></a><a name="p817618229565"></a>If the image based on which an ECS is created is encrypted, the system disk of the ECS is automatically encrypted. In addition, the name of the encrypted key is displayed on the page.</p>
    </li></ul>
    </div>
    <a name="ul11528273145822"></a><a name="ul11528273145822"></a><ul id="ul11528273145822"><li><strong id="b1914510113816"><a name="b1914510113816"></a><a name="b1914510113816"></a>Data Disk</strong><p id="p2766165812449"><a name="p2766165812449"></a><a name="p2766165812449"></a>You can create multiple data disks for an ECS and encrypt them. In addition, you can specify a data disk image for exporting data.</p>
    <p id="p55343398145822"><a name="p55343398145822"></a><a name="p55343398145822"></a>When encrypting a data disk, select <strong id="b842352706154539"><a name="b842352706154539"></a><a name="b842352706154539"></a>Encryption</strong> for it. KMS access rights must be granted to EVS for using the encryption feature. If you have rights granting permission, grant the KMS access rights to EVS. If you do not have the permission, contact the user having the security administrator rights to grant the KMS access rights. For details, see <em id="i443622370"><a name="i443622370"></a><a name="i443622370"></a>Identity and Access Management User Guide</em>.</p>
    <a name="ul49081691145822"></a><a name="ul49081691145822"></a><ul id="ul49081691145822"><li><strong id="b465638357"><a name="b465638357"></a><a name="b465638357"></a>Xrole Name: EVSAccessKMS</strong>: indicates that EVS has obtained the KMS access rights.</li><li><strong id="b86564676"><a name="b86564676"></a><a name="b86564676"></a>KMS Key Name</strong>: specifies the name of the key used by the encrypted data disk. By default, the name is <strong id="b1103545357"><a name="b1103545357"></a><a name="b1103545357"></a>evs/default</strong>.</li><li><strong id="b842352706155046"><a name="b842352706155046"></a><a name="b842352706155046"></a>KMS Key ID</strong>: specifies the ID of the key used by the encrypted data disk.</li></ul>
    <p id="p39082035145822"><a name="p39082035145822"></a><a name="p39082035145822"></a>For more information about EVS disk encryption, see <em id="i842352697115514"><a name="i842352697115514"></a><a name="i842352697115514"></a>Elastic Volume Service User Guide</em>.</p>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="25.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p61374960145822"><a name="p61374960145822"></a><a name="p61374960145822"></a><strong id="b286717501071"><a name="b286717501071"></a><a name="b286717501071"></a>Common I/O</strong> for <strong id="b1154713550716"><a name="b1154713550716"></a><a name="b1154713550716"></a>System Disk</strong></p>
    </td>
    </tr>
    <tr id="row4451533103918"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p1392064718398"><a name="p1392064718398"></a><a name="p1392064718398"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p209231547193913"><a name="p209231547193913"></a><a name="p209231547193913"></a>Controls instance access within or between security groups by defining access rules. ECSs added to a security group are protected by the access rules you define.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p1746103353914"><a name="p1746103353914"></a><a name="p1746103353914"></a>N/A</p>
    </td>
    </tr>
    <tr id="row9178779145822"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p108218336525"><a name="p108218336525"></a><a name="p108218336525"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p50083153145822"><a name="p50083153145822"></a><a name="p50083153145822"></a>An EIP is a static public IP address bound to an ECS in a VPC. Using the EIP, the ECS provides services externally.</p>
    <p id="p48095200145822"><a name="p48095200145822"></a><a name="p48095200145822"></a>The following options are provided:</p>
    <a name="ul30574237145822"></a><a name="ul30574237145822"></a><ul id="ul30574237145822"><li><strong id="b109070192042"><a name="b109070192042"></a><a name="b109070192042"></a>Do not use</strong><p id="p18849270192044"><a name="p18849270192044"></a><a name="p18849270192044"></a>An ECS without an EIP cannot access the Internet. However, it can still be used as a service ECS or deployed in a cluster on a private network.</p>
    </li><li><strong id="b65370391183"><a name="b65370391183"></a><a name="b65370391183"></a>Automatically assign</strong><p id="p1472011411189"><a name="p1472011411189"></a><a name="p1472011411189"></a>An EIP with a dedicated bandwidth is automatically assigned to each ECS. You can set the bandwidth size.</p>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="25.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p60594146145822"><a name="p60594146145822"></a><a name="p60594146145822"></a>Automatically assign</p>
    </td>
    </tr>
    <tr id="row36467360145822"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p47702931"><a name="p47702931"></a><a name="p47702931"></a>Key Pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p10825431145822"><a name="p10825431145822"></a><a name="p10825431145822"></a>A key pair is used for authenticating the ECS. In this mode, create or import a key pair on the <strong id="b427209230171221"><a name="b427209230171221"></a><a name="b427209230171221"></a>Key Pair</strong> page.</p>
    <div class="note" id="note4444705145822"><a name="note4444705145822"></a><a name="note4444705145822"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p30320017145822"><a name="p30320017145822"></a><a name="p30320017145822"></a>If you use an existing key, make sure that you have saved the key file locally. Otherwise, logging in to the ECS will fail.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="25.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p24476844145822"><a name="p24476844145822"></a><a name="p24476844145822"></a>N/A</p>
    </td>
    </tr>
    <tr id="row169972316201"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p199981314203"><a name="p199981314203"></a><a name="p199981314203"></a>Advanced Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p12120173110500"><a name="p12120173110500"></a><a name="p12120173110500"></a>This allows you to configure <strong id="b1326019317101"><a name="b1326019317101"></a><a name="b1326019317101"></a>File Injection</strong>, <strong id="b449213416442"><a name="b449213416442"></a><a name="b449213416442"></a>User Data Injection</strong>, .</p>
    <p id="p152801338145112"><a name="p152801338145112"></a><a name="p152801338145112"></a>You can select <strong id="b3974104514363"><a name="b3974104514363"></a><a name="b3974104514363"></a>Do not configure</strong> or <strong id="b797514458361"><a name="b797514458361"></a><a name="b797514458361"></a>Configure now</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p11998123172016"><a name="p11998123172016"></a><a name="p11998123172016"></a>N/A</p>
    </td>
    </tr>
    <tr id="row49161638145822"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p59770784145822"><a name="p59770784145822"></a><a name="p59770784145822"></a>File Injection</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p9595331145822"><a name="p9595331145822"></a><a name="p9595331145822"></a>Enables the ECS to automatically inject a script file or other files into a specified directory on an ECS when you create the ECS. This configuration is optional.</p>
    <a name="ul15674877145822"></a><a name="ul15674877145822"></a><ul id="ul15674877145822"><li>For Linux, specify the path for storing the injected file, for example <strong>/etc/foo.txt</strong>.</li><li>For Windows, the injected file is automatically stored in the root directory of disk C. You only need to specify the file name, such as <strong id="b19455189172515"><a name="b19455189172515"></a><a name="b19455189172515"></a>foo</strong>. The file name can contain only letters and digits.</li></ul>
    <p id="p61705506145822"><a name="p61705506145822"></a><a name="p61705506145822"></a>For details, see <a href="https://docs.otc.t-systems.com/usermanual/ecs/en-us_topic_0013898301.html" target="_blank" rel="noopener noreferrer">Injecting Files into ECSs</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p32090104145822"><a name="p32090104145822"></a><a name="p32090104145822"></a>N/A</p>
    </td>
    </tr>
    <tr id="row30727146145822"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p39801566145822"><a name="p39801566145822"></a><a name="p39801566145822"></a>User Data Injection</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p2701445145822"><a name="p2701445145822"></a><a name="p2701445145822"></a>Enables the ECS to automatically inject user data when the ECS starts for the first time. This configuration is optional.</p>
    <p id="p17490455145822"><a name="p17490455145822"></a><a name="p17490455145822"></a>For details, see <a href="https://docs.otc.t-systems.com/usermanual/ecs/en-us_topic_0032380449.html" target="_blank" rel="noopener noreferrer">Elastic Cloud Server User Guide</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p65831202145822"><a name="p65831202145822"></a><a name="p65831202145822"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Create Now**. 
7.  If you want to use the newly created AS configuration, add it to the AS group. For details, see  [Replacing AS Configuration in an AS Group](replacing-as-configuration-in-an-as-group.md).
8.  \(Optional\) Enable the AS group.

    If the AS group is in  **Disabled**  state, enable it. For details, see  [Enabling an AS Group](enabling-an-as-group.md).


