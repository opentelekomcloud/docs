# Using an Existing ECS to Create an AS Configuration<a name="EN-US_TOPIC_0042018363"></a>

## Scenarios<a name="section2495449014355"></a>

You can use an existing ECS to rapidly create an AS configuration. In such a case, the parameter settings, such as the vCPUs, memory, image, disk, and ECS type in the AS configuration are the same as those of the selected ECS by default.

## Procedure<a name="section1657416306249"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
4.  Click  **Create AS Configuration**.
5.  Set the parameters for the AS configuration.  [Table 1](#table27476571)  lists the AS configuration parameters.

    **Table  1**  AS configuration parameters

    <a name="table27476571"></a>
    <table><thead align="left"><tr id="row32016662"><th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.2.4.1.1"><p id="p43212834"><a name="p43212834"></a><a name="p43212834"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="61.5%" id="mcps1.2.4.1.2"><p id="p10578662"><a name="p10578662"></a><a name="p10578662"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.31%" id="mcps1.2.4.1.3"><p id="p51565323"><a name="p51565323"></a><a name="p51565323"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row515341432317"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.1 "><p id="p51531114202310"><a name="p51531114202310"></a><a name="p51531114202310"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.5%" headers="mcps1.2.4.1.2 "><p id="p17184175316413"><a name="p17184175316413"></a><a name="p17184175316413"></a>A region is where an AS configuration resides.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.31%" headers="mcps1.2.4.1.3 "><p id="p4153191417231"><a name="p4153191417231"></a><a name="p4153191417231"></a>N/A</p>
    </td>
    </tr>
    <tr id="row57496954161325"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.1 "><p id="p26741679161325"><a name="p26741679161325"></a><a name="p26741679161325"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.5%" headers="mcps1.2.4.1.2 "><p id="p18592405161325"><a name="p18592405161325"></a><a name="p18592405161325"></a>Specifies the name of an AS configuration.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.31%" headers="mcps1.2.4.1.3 "><p id="p29589843161325"><a name="p29589843161325"></a><a name="p29589843161325"></a>N/A</p>
    </td>
    </tr>
    <tr id="row16041657"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.1 "><p id="p24305815"><a name="p24305815"></a><a name="p24305815"></a>Configuration Template</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.5%" headers="mcps1.2.4.1.2 "><p id="p59011025101558"><a name="p59011025101558"></a><a name="p59011025101558"></a>Select <strong id="b192280263166"><a name="b192280263166"></a><a name="b192280263166"></a>Use specifications of an existing ECS</strong> and click <strong id="b1499215771617"><a name="b1499215771617"></a><a name="b1499215771617"></a>Select ECS</strong>.</p>
    <p id="p32378487175332"><a name="p32378487175332"></a><a name="p32378487175332"></a>The ECS type, vCPUs, memory, image, and disk information in the AS configuration are the same as those of the selected ECS by default. </p>
    </td>
    <td class="cellrowborder" valign="top" width="19.31%" headers="mcps1.2.4.1.3 "><p id="p59638115"><a name="p59638115"></a><a name="p59638115"></a>Use specifications of an existing ECS</p>
    </td>
    </tr>
    <tr id="row8624119112542"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.1 "><p id="p814113820394"><a name="p814113820394"></a><a name="p814113820394"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.5%" headers="mcps1.2.4.1.2 "><p id="p10128370112614"><a name="p10128370112614"></a><a name="p10128370112614"></a>An EIP is a static public IP address bound to an ECS in a VPC. Using the EIP, the ECS provides services externally.</p>
    <div class="p" id="p24046472112614"><a name="p24046472112614"></a><a name="p24046472112614"></a>The following options are provided:<a name="ul1338415125618"></a><a name="ul1338415125618"></a><ul id="ul1338415125618"><li>Do not use<p id="p77776467592"><a name="p77776467592"></a><a name="p77776467592"></a>An ECS without an EIP cannot access the Internet. However, it can still be used as a service ECS or deployed in a cluster on a private network.</p>
    </li><li>Automatically assign<p id="p1353012513593"><a name="p1353012513593"></a><a name="p1353012513593"></a>An EIP with a dedicated bandwidth is automatically assigned to each ECS. The bandwidth size is configurable.</p>
    </li></ul>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="19.31%" headers="mcps1.2.4.1.3 "><p id="p30834244112614"><a name="p30834244112614"></a><a name="p30834244112614"></a>Automatically assign</p>
    </td>
    </tr>
    <tr id="row42842654"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.1 "><p id="p47702931"><a name="p47702931"></a><a name="p47702931"></a>Key Pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.5%" headers="mcps1.2.4.1.2 "><p id="p38732217"><a name="p38732217"></a><a name="p38732217"></a>A key pair is used for authenticating the ECS. In this mode, create or import a key pair on the <strong id="b427209230171221"><a name="b427209230171221"></a><a name="b427209230171221"></a>Key Pair</strong> page.</p>
    <div class="note" id="note13045638"><a name="note13045638"></a><a name="note13045638"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="textintable" id="p50301879"><a name="p50301879"></a><a name="p50301879"></a>If you use an existing key, make sure that you have saved the key file locally. Otherwise, logging in to the ECS will fail.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19.31%" headers="mcps1.2.4.1.3 "><p id="p47920438"><a name="p47920438"></a><a name="p47920438"></a>N/A</p>
    </td>
    </tr>
    <tr id="row118911154313"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.1 "><p id="p5189015123111"><a name="p5189015123111"></a><a name="p5189015123111"></a>Advanced Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.5%" headers="mcps1.2.4.1.2 "><p id="p12120173110500"><a name="p12120173110500"></a><a name="p12120173110500"></a>This allows you to configure <strong id="b0857125582117"><a name="b0857125582117"></a><a name="b0857125582117"></a>File Injection</strong>, <strong id="b1675310922216"><a name="b1675310922216"></a><a name="b1675310922216"></a>User Data Injection</strong>.</p>
    <p id="p152801338145112"><a name="p152801338145112"></a><a name="p152801338145112"></a>You can select <strong id="b552719595111"><a name="b552719595111"></a><a name="b552719595111"></a>Do not configure</strong> or <strong id="b125287594114"><a name="b125287594114"></a><a name="b125287594114"></a>Configure now</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.31%" headers="mcps1.2.4.1.3 "><p id="p15189715173120"><a name="p15189715173120"></a><a name="p15189715173120"></a>N/A</p>
    </td>
    </tr>
    <tr id="row28630766"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.1 "><p id="p37390672"><a name="p37390672"></a><a name="p37390672"></a>File Injection</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.5%" headers="mcps1.2.4.1.2 "><p id="p8745607"><a name="p8745607"></a><a name="p8745607"></a>Enables the ECS to automatically inject a script file or other files into a specified directory on an ECS when you create the ECS. This configuration is optional.</p>
    <a name="ul11601606"></a><a name="ul11601606"></a><ul id="ul11601606"><li>For Linux, specify the path for storing the injected file, for example <strong id="b119078396115"><a name="b119078396115"></a><a name="b119078396115"></a>/etc/foo.txt</strong>.</li><li>For Windows, the injected file is automatically stored in the root directory of disk C. You only need to specify the file name, such as <strong id="b19455189172515"><a name="b19455189172515"></a><a name="b19455189172515"></a>foo</strong>. The file name can contain only letters and digits.</li></ul>
    <p id="p43727721142043"><a name="p43727721142043"></a><a name="p43727721142043"></a>For details, see <a href="https://docs.otc.t-systems.com/usermanual/ecs/en-us_topic_0013898301.html" target="_blank" rel="noopener noreferrer">Injecting Files into ECSs</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.31%" headers="mcps1.2.4.1.3 "><p id="p16689200"><a name="p16689200"></a><a name="p16689200"></a>N/A</p>
    </td>
    </tr>
    <tr id="row15985080"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.1 "><p id="p19723089"><a name="p19723089"></a><a name="p19723089"></a>User Data Injection</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.5%" headers="mcps1.2.4.1.2 "><p id="p54066375"><a name="p54066375"></a><a name="p54066375"></a>Enables the ECS to automatically inject user data when the ECS starts for the first time. This configuration is optional.</p>
    <p id="p22810194143312"><a name="p22810194143312"></a><a name="p22810194143312"></a>For details, see <a href="https://docs.otc.t-systems.com/usermanual/ecs/en-us_topic_0032380449.html" target="_blank" rel="noopener noreferrer">Injecting User Data into ECSs</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.31%" headers="mcps1.2.4.1.3 "><p id="p17300225"><a name="p17300225"></a><a name="p17300225"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  After setting the parameters, click  **Create Now**.
7.  Click  **Create Now**. 
8.  If you want to use the newly created AS configuration, add it to the AS group. For details, see  [Replacing AS Configuration in an AS Group](replacing-as-configuration-in-an-as-group.md).
9.  \(Optional\) Enable the AS group.

    If the AS group is in  **Disabled**  state, enable it. For details, see  [Enabling an AS Group](enabling-an-as-group.md).


