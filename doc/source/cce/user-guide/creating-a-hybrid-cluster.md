# Creating a Hybrid Cluster<a name="cce_01_0028"></a>

On the CCE console, you can easily create Kubernetes clusters. Kubernetes can manage container clusters at scale. A cluster manages a group of node resources.

The former VM clusters are renamed to hybrid clusters, which can manage both VM nodes and bare-metal nodes.

## Preparation<a name="section1675221242512"></a>

-   Before creating your first cluster, you must create a  VPC. If you already have an available VPC, skip this preparatory step.

    A VPC provides an isolated, configurable, and manageable virtual network for CCE clusters. For details, see  [Creating a VPC](https://docs.otc.t-systems.com/en-us/usermanual/vpc/en-us_topic_0013935842.html).

-   Create a key pair, which will be used for identity authentication upon a remote node login. For details, see  [Creating a Key Pair](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0014250631.html).
-   Plan the container CIDR block and service CIDR block before creating a cluster. The CIDR block is a one-time configuration and cannot be changed after the cluster is created. If you want to use another container CIDR block, you have to create a new cluster and assign the new container CIDR block to the cluster.

## Precautions for Creating a Cluster<a name="section2086419142214"></a>

Some basic resources are created during  cluster creation, as shown in the following table.

**Table  1**  Precautions for creating a cluster

<a name="table108111152195919"></a>
<table><thead align="left"><tr id="row20811252105914"><th class="cellrowborder" valign="top" width="29.99%" id="mcps1.2.3.1.1"><p id="p14811135212593"><a name="p14811135212593"></a><a name="p14811135212593"></a>Resource</p>
</th>
<th class="cellrowborder" valign="top" width="70.00999999999999%" id="mcps1.2.3.1.2"><p id="p15811452145913"><a name="p15811452145913"></a><a name="p15811452145913"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row88111652155915"><td class="cellrowborder" valign="top" width="29.99%" headers="mcps1.2.3.1.1 "><p id="p1298265916593"><a name="p1298265916593"></a><a name="p1298265916593"></a><span class="keyword" id="keyword106215694317048"><a name="keyword106215694317048"></a><a name="keyword106215694317048"></a>Masters</span> and related resources</p>
</td>
<td class="cellrowborder" valign="top" width="70.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p6982145965918"><a name="p6982145965918"></a><a name="p6982145965918"></a>Associated with CCE resource tenants, and invisible to you.</p>
</td>
</tr>
<tr id="row981135210590"><td class="cellrowborder" valign="top" width="29.99%" headers="mcps1.2.3.1.1 "><p id="p199826593596"><a name="p199826593596"></a><a name="p199826593596"></a><span class="keyword" id="keyword97504591317126"><a name="keyword97504591317126"></a><a name="keyword97504591317126"></a>ECSs</span> (optional)</p>
</td>
<td class="cellrowborder" valign="top" width="70.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p11801128222"><a name="p11801128222"></a><a name="p11801128222"></a>An ECS corresponds to a cluster node that provides computing resources.</p>
<p id="p1498225945915"><a name="p1498225945915"></a><a name="p1498225945915"></a>An ECS is named in the format of <em id="i2089181718171121"><a name="i2089181718171121"></a><a name="i2089181718171121"></a>Cluster name-Random number</em>. The name format is user-defined. ECSs created in batches are named in the format of <em id="i83831083398"><a name="i83831083398"></a><a name="i83831083398"></a>Cluster name-Random number 1-Random number 2</em>.</p>
</td>
</tr>
<tr id="row6811952165919"><td class="cellrowborder" valign="top" width="29.99%" headers="mcps1.2.3.1.1 "><p id="p1298215925914"><a name="p1298215925914"></a><a name="p1298215925914"></a><span class="keyword" id="keyword14692484517246"><a name="keyword14692484517246"></a><a name="keyword14692484517246"></a>Security groups</span></p>
</td>
<td class="cellrowborder" valign="top" width="70.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p598216599595"><a name="p598216599595"></a><a name="p598216599595"></a>Two security groups are created for a cluster: one for managing master nodes, and the other for managing worker nodes.</p>
<div class="notice" id="note1890117181312"><a name="note1890117181312"></a><a name="note1890117181312"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p490115751314"><a name="p490115751314"></a><a name="p490115751314"></a>Do not delete the security group settings and security group rules configured during cluster creation. Otherwise, the cluster will exhibit unexpected behavior.</p>
</div></div>
<a name="ol57751237359"></a><a name="ol57751237359"></a><ol id="ol57751237359"><li><span class="keyword" id="keyword2331700991731"><a name="keyword2331700991731"></a><a name="keyword2331700991731"></a>Security group for master nodes</span><p id="p1383640122418"><a name="p1383640122418"></a><a name="p1383640122418"></a>Name format: <em id="i114441054144313"><a name="i114441054144313"></a><a name="i114441054144313"></a>Cluster name</em>-<strong id="b78831033658"><a name="b78831033658"></a><a name="b78831033658"></a>cce-control</strong>-<em id="i11444354134312"><a name="i11444354134312"></a><a name="i11444354134312"></a>Random number</em></p>
<p id="p2477145154415"><a name="p2477145154415"></a><a name="p2477145154415"></a>Functions:</p>
<a name="ul516535584419"></a><a name="ul516535584419"></a><ul id="ul516535584419"><li>Allows outbound traffic.</li><li>Allows other nodes to access Kubernetes services of masters.</li></ul>
</li><li><span class="keyword" id="keyword3917609517322"><a name="keyword3917609517322"></a><a name="keyword3917609517322"></a>Security group for nodes</span><p id="p1872943734519"><a name="p1872943734519"></a><a name="p1872943734519"></a>Name format: <em id="i18242113434513"><a name="i18242113434513"></a><a name="i18242113434513"></a>Cluster name</em>-<strong id="b6266945856"><a name="b6266945856"></a><a name="b6266945856"></a>cce-node</strong>-<em id="i3242123413452"><a name="i3242123413452"></a><a name="i3242123413452"></a>Random number</em></p>
<p id="p15118379456"><a name="p15118379456"></a><a name="p15118379456"></a>Functions:</p>
<a name="ul1579276164613"></a><a name="ul1579276164613"></a><ul id="ul1579276164613"><li>Allows outbound traffic.</li><li>Allows remote login to Linux or Windows OS using ports 22 and 3389.</li><li>Allows communication between Kubernetes components using ports 4789 and 10250.</li><li>Allows Kubernetes to provide services for external systems using ports 30000 and 32767.</li><li>Allows communication between nodes in the same security group.</li></ul>
</li></ol>
</td>
</tr>
<tr id="row7811135245911"><td class="cellrowborder" valign="top" width="29.99%" headers="mcps1.2.3.1.1 "><p id="p16982155995917"><a name="p16982155995917"></a><a name="p16982155995917"></a><span class="keyword" id="keyword12377316711761"><a name="keyword12377316711761"></a><a name="keyword12377316711761"></a>Disks</span> (optional)</p>
</td>
<td class="cellrowborder" valign="top" width="70.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p398225975918"><a name="p398225975918"></a><a name="p398225975918"></a>Two disks are configured for each node. One is the system disk, and the other is the data disk used to run Docker.</p>
</td>
</tr>
<tr id="row13811752135919"><td class="cellrowborder" valign="top" width="29.99%" headers="mcps1.2.3.1.1 "><p id="p1298215916594"><a name="p1298215916594"></a><a name="p1298215916594"></a><span class="keyword" id="keyword17542011317615"><a name="keyword17542011317615"></a><a name="keyword17542011317615"></a>Elastic IP address</span> (optional)4</p>
</td>
<td class="cellrowborder" valign="top" width="70.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p42997393017"><a name="p42997393017"></a><a name="p42997393017"></a>Any node that requires access to external networks must have an elastic IP address (EIP).</p>
</td>
</tr>
</tbody>
</table>

## Procedure<a name="section463761220269"></a>

1.  Log in to the CCE console. Choose  **Dashboard**  \>  **Create Cluster**  to open the  **Create Hybrid Cluster**  page. An alternative way to open that page is to choose  **Resource Management**  \>  **Clusters**  in the navigation pane and click  **Create**  under  **Hybrid Cluster**.
2.  Set the parameters listed in  [Table 2](#table8638121213265). The parameters marked with an asterisk \(\*\) are mandatory.

    **Table  2**  Parameters for creating a cluster

    <a name="table8638121213265"></a>
    <table><thead align="left"><tr id="row10638181262612"><th class="cellrowborder" valign="top" width="19.98%" id="mcps1.2.3.1.1"><p id="p1063821214265"><a name="p1063821214265"></a><a name="p1063821214265"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80.02%" id="mcps1.2.3.1.2"><p id="p1638181232617"><a name="p1638181232617"></a><a name="p1638181232617"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42961494311"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p812874116011"><a name="p812874116011"></a><a name="p812874116011"></a>* Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p161283411302"><a name="p161283411302"></a><a name="p161283411302"></a>To minimize network latency and resource access time, select the nearest region. Cloud resources are region-specific and cannot be used across regions through internal network connections.</p>
    </td>
    </tr>
    <tr id="row1063812126263"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p15639812122620"><a name="p15639812122620"></a><a name="p15639812122620"></a>* Cluster Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p26391512172614"><a name="p26391512172614"></a><a name="p26391512172614"></a>Name of the new cluster, which cannot be changed after the cluster is created.</p>
    <p id="p1520317181911"><a name="p1520317181911"></a><a name="p1520317181911"></a>A cluster name contains 4 to 128 characters starting with a letter and not ending with a hyphen (-). Only lowercase letters, digits, and hyphens (-) are allowed.</p>
    </td>
    </tr>
    <tr id="row6649879161231"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p1769363161231"><a name="p1769363161231"></a><a name="p1769363161231"></a>* Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p9100682161231"><a name="p9100682161231"></a><a name="p9100682161231"></a>Kubernetes community baseline version. The latest version is recommended. For details, see <a href="cce-cluster-version-release-notes.md">CCE Cluster Version Release Notes</a>.</p>
    </td>
    </tr>
    <tr id="row572593234714"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p14725432104718"><a name="p14725432104718"></a><a name="p14725432104718"></a>* Management Scale</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p14899102111550"><a name="p14899102111550"></a><a name="p14899102111550"></a>Maximum number of nodes that can be managed by a cluster.</p>
    <p id="p192696516218"><a name="p192696516218"></a><a name="p192696516218"></a>If you select <span class="uicontrol" id="uicontrol35596531909"><a name="uicontrol35596531909"></a><a name="uicontrol35596531909"></a><b>50 nodes</b></span>, the cluster can manage a maximum of 50 nodes. The cluster management scale cannot be modified after a cluster is created. Exercise caution when creating a cluster.</p>
    <div class="p" id="p102308301014"><a name="p102308301014"></a><a name="p102308301014"></a>Each cluster contains at least one <span class="uicontrol" id="uicontrol152621531193016"><a name="uicontrol152621531193016"></a><a name="uicontrol152621531193016"></a><b>master node</b></span> and at least one <span class="uicontrol" id="uicontrol1173533873013"><a name="uicontrol1173533873013"></a><a name="uicontrol1173533873013"></a><b>worker node</b></span>. A worker node is a cloud server.<a name="ul1045015327013"></a><a name="ul1045015327013"></a><ul id="ul1045015327013"><li>Master node: controls worker nodes in the cluster. The master node is automatically created along with the cluster, and manages and schedules the entire cluster.</li><li>Worker node: a node that runs the workload you deploy. You can create a new worker node. The master node assigns a worker node to each deployable component of your workload. When a worker node is down, the master node migrates the workload to another worker node.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row680585841419"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p11786989141"><a name="p11786989141"></a><a name="p11786989141"></a>* High Availability</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><a name="ul97916871415"></a><a name="ul97916871415"></a><ul id="ul97916871415"><li><strong id="b1789520576201"><a name="b1789520576201"></a><a name="b1789520576201"></a>Yes</strong>: An HA cluster will be created. Typically, an HA cluster has three master nodes. The cluster is still available even when a master node is down.</li><li><strong id="b1046822011214"><a name="b1046822011214"></a><a name="b1046822011214"></a>No</strong>: The cluster has only one master node. If the master node is down, the cluster stops serving new workloads, but existing workloads are not affected.</li></ul>
    <div class="p" id="p1155010435554"><a name="p1155010435554"></a><a name="p1155010435554"></a>The HA setting is a one-time configuration and cannot be changed after the cluster is created. If you want to use another HA setting for the cluster, you have to create a new cluster that has exactly the same parameter settings (except for the <strong id="b81221810151"><a name="b81221810151"></a><a name="b81221810151"></a>High Availability</strong> parameter) as the current cluster. Set this parameter based on the site requirements.<a name="ul20457121412567"></a><a name="ul20457121412567"></a><ul id="ul20457121412567"><li>In production environments, it is advised to set <strong id="b1289881833116"><a name="b1289881833116"></a><a name="b1289881833116"></a>High Availability</strong> to <strong id="b189861811312"><a name="b189861811312"></a><a name="b189861811312"></a>Yes</strong> to improve cluster's disaster recovery capabilities.</li><li>In R&amp;D and testing environments that do not require high reliability, it is not always necessary to set <strong id="b123342391312"><a name="b123342391312"></a><a name="b123342391312"></a>High Availability</strong> to <strong id="b1333463993119"><a name="b1333463993119"></a><a name="b1333463993119"></a>Yes</strong>.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row1763991215268"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p15639181282617"><a name="p15639181282617"></a><a name="p15639181282617"></a>* VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p116393128265"><a name="p116393128265"></a><a name="p116393128265"></a>VPC where the new cluster is located. A VPC provides a secure and logically isolated network environment.</p>
    <p id="p1063941211266"><a name="p1063941211266"></a><a name="p1063941211266"></a>If no VPC is available, click <span class="uicontrol" id="uicontrol045415317323"><a name="uicontrol045415317323"></a><a name="uicontrol045415317323"></a><b><span id="text164531531325"><a name="text164531531325"></a><a name="text164531531325"></a>Create a VPC</span></b></span> to create a VPC. After the VPC is created, click the refresh icon.</p>
    </td>
    </tr>
    <tr id="row15639412132615"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p36391812172618"><a name="p36391812172618"></a><a name="p36391812172618"></a>* Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p1108371202"><a name="p1108371202"></a><a name="p1108371202"></a>The subnet where cluster nodes will run. A subnet improves network security by providing exclusive network resources that are isolated from other networks. For details about the relationship between VPCs, subnets, and clusters, see <a href="cluster-overview.md">Cluster Overview</a>.</p>
    <p id="p41882822012"><a name="p41882822012"></a><a name="p41882822012"></a><strong id="b61610445552"><a name="b61610445552"></a><a name="b61610445552"></a>The selected subnet cannot be modified after the cluster is created.</strong> Exercise caution when selecting a subnet.</p>
    </td>
    </tr>
    <tr id="row482955911270"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p9831659192715"><a name="p9831659192715"></a><a name="p9831659192715"></a>* Network Model</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><a name="ul19705159132810"></a><a name="ul19705159132810"></a><ul id="ul19705159132810"><li><strong id="b780582516487"><a name="b780582516487"></a><a name="b780582516487"></a>Tunnel network</strong>: The container network is an overlay tunnel network on top of a VPC network and uses the VXLAN technology. This network model is applicable when there is no high requirements on performance. VXLAN encapsulates Ethernet packets as UDP packets for tunnel transmission. Though at some cost of performance, the tunnel encapsulation enables higher interoperability and compatibility with advanced features (such as network policy-based isolation), meeting the requirements of most applications.</li><li><strong id="b1152753444812"><a name="b1152753444812"></a><a name="b1152753444812"></a>VPC network</strong>: The container network uses VPC routing to integrate with the underlying network. This network model is applicable to performance-intensive scenarios. The maximum number of nodes allowed in a cluster depends on the route quota in a VPC network. Each node is assigned a CIDR block of a fixed size. VPC networks are free from tunnel encapsulation overhead and outperform container tunnel network models. In addition, as VPC routing includes routes to node IP addresses and container network segment, container instances in the cluster can be directly accessed from outside the cluster.<div class="note" id="note1110055162218"><a name="note1110055162218"></a><a name="note1110055162218"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p339201494019"><a name="p339201494019"></a><a name="p339201494019"></a>If <strong id="b14340131517409"><a name="b14340131517409"></a><a name="b14340131517409"></a>VPC network</strong> is selected, you can set the maximum number of pods allowed to be created in the cluster nodes. This value cannot be changed after the cluster is created. When creating a node, ensure that the value of <strong id="b73408150408"><a name="b73408150408"></a><a name="b73408150408"></a>Max Pods</strong> in <strong id="b11340151512405"><a name="b11340151512405"></a><a name="b11340151512405"></a>Advanced Kubernetes Settings</strong> does not exceed the maximum number of pods you have set.</p>
    </div></div>
    </li></ul>
    </td>
    </tr>
    <tr id="row64648564171234"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p2042307171234"><a name="p2042307171234"></a><a name="p2042307171234"></a>* Container Network Segment</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p31209167171234"><a name="p31209167171234"></a><a name="p31209167171234"></a>An IP address range that can be allocated to container instances.</p>
    <a name="ul1423120351449"></a><a name="ul1423120351449"></a><ul id="ul1423120351449"><li>If <strong id="b13880123135013"><a name="b13880123135013"></a><a name="b13880123135013"></a>Automatically select</strong> is deselected, you must select a CIDR block. If the CIDR block you select conflicts with a subnet CIDR block, the system prompts you to select another CIDR block. The recommended CIDR blocks are 10.0.0.0/12-19, 172.16.0.0/16-19, and 192.168.0.0/16-19.<p id="p158661543014"><a name="p158661543014"></a><a name="p158661543014"></a><strong id="b1135314113592"><a name="b1135314113592"></a><a name="b1135314113592"></a>If different clusters share a container CIDR block, an IP address conflict will occur and access to applications will fail.</strong></p>
    </li><li>If <strong id="b18918152155411"><a name="b18918152155411"></a><a name="b18918152155411"></a>Automatically select</strong> is selected, the system automatically assigns a CIDR block that does not conflict with any subnet CIDR block.</li></ul>
    <p id="p873618346117"><a name="p873618346117"></a><a name="p873618346117"></a>The mask of the container CIDR block must be appropriate. It determines the number of available nodes in a cluster. A too small mask value will cause the cluster to soon fall short of nodes. After the mask is set, the estimated maximum number of containers supported by the current CIDR block will be displayed.</p>
    </td>
    </tr>
    <tr id="row1039985411200"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p63991154192010"><a name="p63991154192010"></a><a name="p63991154192010"></a>* Service Network Segment</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p977633218244"><a name="p977633218244"></a><a name="p977633218244"></a>CIDR block of Kubernetes Service.</p>
    <a name="ul13104152611581"></a><a name="ul13104152611581"></a><ul id="ul13104152611581"><li><strong id="b13640627515"><a name="b13640627515"></a><a name="b13640627515"></a>Default</strong>: The default CIDR block 10.247.0.0/16 will be used.</li><li><strong id="b723663413517"><a name="b723663413517"></a><a name="b723663413517"></a>Custom</strong>: Manually set a network segment and mask based on service requirements. The mask determines the maximum number of Service IP addresses available in the cluster.</li></ul>
    </td>
    </tr>
    <tr id="row773511171567"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p37371717105616"><a name="p37371717105616"></a><a name="p37371717105616"></a>Authorization Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p13737141735611"><a name="p13737141735611"></a><a name="p13737141735611"></a>By default, <span class="uicontrol" id="uicontrol13753167101316"><a name="uicontrol13753167101316"></a><a name="uicontrol13753167101316"></a><b>RBAC</b></span> is selected.</p>
    <p id="p16141515161117"><a name="p16141515161117"></a><a name="p16141515161117"></a>After RBAC is enabled, IAM users access resources in the cluster according to fine-grained permissions policies.</p>
    </td>
    </tr>
    <tr id="row15698545125718"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p13699164565719"><a name="p13699164565719"></a><a name="p13699164565719"></a>Authentication Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p933784218111"><a name="p933784218111"></a><a name="p933784218111"></a>The authentication mechanism controls user permission on resources in a cluster. For example, you can grant user A the read and write permissions on applications in a specified namespace, while granting user B the read permission on resources in a cluster. For details about role-based permission control, see <a href="cluster-management-permission-control.md">Cluster Management Permission Control</a>.</p>
    <a name="ul208851410646"></a><a name="ul208851410646"></a><ul id="ul208851410646"><li>By default, X.509 authentication instead of <span class="uicontrol" id="uicontrol10477202816215"><a name="uicontrol10477202816215"></a><a name="uicontrol10477202816215"></a><b>Enhanced authentication</b></span> is enabled. X.509 is a standard defining the format of public key certificates. X.509 certificates are used in many Internet protocols.</li><li>If permission control on a cluster is required, select <strong id="b16465195017215"><a name="b16465195017215"></a><a name="b16465195017215"></a>Enhanced authentication</strong> and then <strong id="b646610500215"><a name="b646610500215"></a><a name="b646610500215"></a>Authenticating Proxy</strong>.<p id="p129632614510"><a name="p129632614510"></a><a name="p129632614510"></a>Click <strong id="b19349111931"><a name="b19349111931"></a><a name="b19349111931"></a>Upload</strong> next to <strong id="b83510116317"><a name="b83510116317"></a><a name="b83510116317"></a>CA Root Certificate</strong> to upload a valid certificate. Select the check box to confirm that the uploaded certificate is valid.</p>
    <p id="p36719411534"><a name="p36719411534"></a><a name="p36719411534"></a>If the certificate is invalid, the cluster cannot be created. The uploaded certificate file must be smaller than 1 MB and in .crt or .cer format.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row463941216264"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p2063961212268"><a name="p2063961212268"></a><a name="p2063961212268"></a>Cluster Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p664014125268"><a name="p664014125268"></a><a name="p664014125268"></a>Optional. Enter the description of the new container cluster.</p>
    </td>
    </tr>
    <tr id="row82974816363"><td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.2.3.1.1 "><p id="p729716814364"><a name="p729716814364"></a><a name="p729716814364"></a>Advanced Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.02%" headers="mcps1.2.3.1.2 "><p id="p15438181703614"><a name="p15438181703614"></a><a name="p15438181703614"></a>Click <a name="image13552162420443"></a><a name="image13552162420443"></a><span><img id="image13552162420443" src="figures/icon-pull-down-5.png"></span> to show advanced settings.</p>
    <p id="p143811175361"><a name="p143811175361"></a><a name="p143811175361"></a>Advanced settings will be displayed only if they are supported in the selected AZ. For example, if the flavor of cluster's master node does not support the multi-AZ feature, <span class="uicontrol" id="uicontrol204382172365"><a name="uicontrol204382172365"></a><a name="uicontrol204382172365"></a><b>Master AZs</b></span> will not be displayed.</p>
    <p id="p184381317173615"><a name="p184381317173615"></a><a name="p184381317173615"></a>The following parameters are supported:</p>
    <p id="p659018381201"><a name="p659018381201"></a><a name="p659018381201"></a><strong id="b2590123892018"><a name="b2590123892018"></a><a name="b2590123892018"></a>Service Forwarding Mode</strong></p>
    <a name="ul18590113892017"></a><a name="ul18590113892017"></a><ul id="ul18590113892017"><li><strong id="b3590113815208"><a name="b3590113815208"></a><a name="b3590113815208"></a>iptables</strong>: Traditional kube-proxy uses iptables rules to implement service load balancing. In this mode, too many iptables rules will be generated when many services are deployed. In addition, non-incremental updates will cause a latency and even obvious performance issues in the case of heavy service traffic.</li><li><strong id="b3590438112011"><a name="b3590438112011"></a><a name="b3590438112011"></a>ipvs</strong>: Optimized kube-proxy mode with higher throughput and faster speed. This mode supports incremental updates and can keep connections uninterrupted during service updates. It is suitable for large-sized clusters.</li></ul>
    <div class="note" id="note17590153811200"><a name="note17590153811200"></a><a name="note17590153811200"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul7590123852011"></a><a name="ul7590123852011"></a><ul id="ul7590123852011"><li>ipvs provides better scalability and performance for large clusters.</li><li>ipvs supports more complex load balancing algorithms than iptables.</li><li>ipvs supports server health checking and connection retries.</li></ul>
    </div></div>
    <p id="p8379453144314"><a name="p8379453144314"></a><a name="p8379453144314"></a><strong id="b4380253124316"><a name="b4380253124316"></a><a name="b4380253124316"></a>CPU Policy</strong></p>
    <p id="p43801653134312"><a name="p43801653134312"></a><a name="p43801653134312"></a>This parameter is displayed only for clusters of v1.13.10-r0 and later.</p>
    <a name="ul2038045318436"></a><a name="ul2038045318436"></a><ul id="ul2038045318436"><li><strong id="b19380175318437"><a name="b19380175318437"></a><a name="b19380175318437"></a>On</strong>: Exclusive CPU cores can be allocated to workload pods. Select <strong id="b53801553114312"><a name="b53801553114312"></a><a name="b53801553114312"></a>On</strong> if your workload is sensitive to latency in CPU cache and scheduling.</li><li><strong id="b43801853154317"><a name="b43801853154317"></a><a name="b43801853154317"></a>Off</strong>: Exclusive CPU cores will not be allocated to workload pods. Select <strong id="b183809535438"><a name="b183809535438"></a><a name="b183809535438"></a>Off</strong> if you want a large pool of shareable CPU cores.</li></ul>
    <p id="p3380195324317"><a name="p3380195324317"></a><a name="p3380195324317"></a>For details about CPU management policies, see <a href="https://kubernetes.io/blog/2018/07/24/feature-highlight-cpu-manager/" target="_blank" rel="noopener noreferrer">Feature Highlight: CPU Manager</a>.</p>
    <p id="p14786438113618"><a name="p14786438113618"></a><a name="p14786438113618"></a><strong id="b8778041153612"><a name="b8778041153612"></a><a name="b8778041153612"></a>Open EIP</strong></p>
    <p id="p10652122133717"><a name="p10652122133717"></a><a name="p10652122133717"></a>A public IP address that is reachable from public networks. Select an EIP that has not been bound to any node. A cluster's EIP is preset in the cluster's certificate. Do no delete the EIP after the cluster has been created. Otherwise, two-way authentication will fail.</p>
    <a name="ul16521721113715"></a><a name="ul16521721113715"></a><ul id="ul16521721113715"><li><strong id="b965292113371"><a name="b965292113371"></a><a name="b965292113371"></a>Do not configure</strong>: The cluster's master node will not have an EIP.</li><li><strong id="b1265212211375"><a name="b1265212211375"></a><a name="b1265212211375"></a>Configure now</strong>: If no EIP is available for selection, create a new EIP.</li></ul>
    <p id="p9765155074814"><a name="p9765155074814"></a><a name="p9765155074814"></a><strong id="b1276535024813"><a name="b1276535024813"></a><a name="b1276535024813"></a>Master AZs</strong></p>
    <p id="p127664507487"><a name="p127664507487"></a><a name="p127664507487"></a>Deploy master nodes in multiple AZs. The multi-AZ deployment of master nodes achieves disaster tolerance on the cluster management plane at a certain sacrifice of cluster performance.</p>
    <div class="note" id="note25679441377"><a name="note25679441377"></a><a name="note25679441377"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p195713441376"><a name="p195713441376"></a><a name="p195713441376"></a>This parameter is available only when there are three or more AZs.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click  **Next: Create Node**. On the  **Create Node**  page, set the following parameters.
    -   **Create Node**
        -   **Create now**: A specified number of nodes will be created along with the cluster. The  **Nodes**  parameter indicates the quantity of nodes.
        -   **Create later**: Create an empty cluster without creating nodes. Click  **Next**.

    -   **Current Region**: geographic location of the nodes to be created.
    -   **AZ**: Set this parameter based on the site requirements. An AZ is a physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through an internal network.

        To enhance workload availability, create nodes in different AZs.

    -   **Node Type**

        **VM node**: A VM node will be created in the cluster.

    -   **Node Name**: Name of the new node.
    -   **DeH**: A Dedicated Host \(DeH\) is a physical server dedicated for your use. You can create nodes on a DeH to physically isolate the nodes from those of other tenants.

        You can select a DeH from the drop-down list box to create a node. If DeH is not required, you can skip the configuration of this parameter.

        >![](/images/icon-note.gif) **NOTE:** 
        >This parameter is available only when DeHs exist.

    -   **Specifications**: Select node specifications that best fit your business needs.

        -   **General-purpose**: provides general computing, storage, and network configurations that can meet a majority of scenarios. General-purpose nodes can be used for web servers, workload development, workload testing, and small databases.
        -   **Memory-optimized**: provides higher memory capacity than general-purpose nodes and is suitable for relational databases, NoSQL, and other workloads that are both memory-intensive and data-intensive.
        -   **GPU-accelerated**: provides powerful floating-point computing and is suitable for real-time, highly concurrent massive computing. Graphical processing units \(GPUs\) of P series are suitable for deep learning, scientific computing, and CAE. GPUs of G series are suitable for 3D animation rendering and CAD.
        -   **General computing-plus**: provides stable performance and exclusive resources to enterprise-level workloads with high and stable computing performance.

        To ensure node stability, CCE automatically reserves some resources to run necessary system components. For details, see  [Formula for Calculating the Reserved Resources of a Node](formula-for-calculating-the-reserved-resources-of-a-node.md).

    -   **OS**: Select the operating system \(OS\) of the nodes to be created. For details, see  [OS Patch Notes for Cluster Nodes](os-patch-notes-for-cluster-nodes.md).
    -   **System Disk**  and  **Data Disk**: Set the disk space of the nodes.

        -   The system disk capacity ranges from 40 GB to 1,024 GB.

            >![](/images/icon-note.gif) **NOTE:** 
            >When creating a cluster of v1.15, ensure that the system disk of the node to be created has a capacity larger than 50 GB.

        -   The data disk capacity is configurable and ranges from 100 to 32678 GB.

        System disks and data disks deliver three levels of I/O performance:

        -   **Common I/O**: uses Serial Advanced Technology Attachment \(SATA\) drives to store data. EVS disks of this level provide reliable block storage and a maximum IOPS of 1,000 per disk. They are suitable for key applications.
        -   **High I/O**: uses serial attached SCSI \(SAS\) drives to store data. EVS disks of this level provide a maximum IOPS of 3,000 and a minimum read/write latency of 1 ms. They are suitable for Relational Database Service \(RDS\), NoSQL, data warehouse, and file system applications.
        -   **Ultra-high I/O**: uses solid state disk \(SSD\) drives to store data. EVS disks of this level provide a maximum IOPS of 20,000 and a minimum read/write latency of 1 ms. They are suitable for RDS, NoSQL, and data warehouse applications.

    -   **VPC**: This parameter is displayed only for clusters of v1.13.10-r0 and later.
    -   **Subnet**: A subnet improves network security by providing exclusive network resources that are isolated from other networks. You can select any subnet in the cluster VPC. Cluster nodes can belong to different subnets.

        This parameter is displayed only for clusters of v1.13.10-r0 and later.

    -   **EIP**: An independent public IP address. If the nodes to be created require Internet access, select  **Automatically assign**  or  **Use existing**.

        >![](/images/icon-note.gif) **NOTE:** 
        >By default, VPC's SNAT feature is disabled for CCE. If SNAT is enabled, you do not need to use EIPs to access external networks.

        -   **Do not use**: A node without an EIP cannot access the Internet. It can be used only as a cloud server for deploying services or clusters on a private network.
        -   **Automatically assign**: An EIP with specified configurations is automatically assigned to each node. If the number of EIPs is less than the number of nodes, the EIPs are randomly bound to the nodes.

            Set the specifications, required quantity, billing mode, and bandwidth as required. When creating an ECS, ensure that the elastic IP address quota is sufficient.

        -   **Use existing**: Existing EIPs are assigned to the nodes to be created.

    -   **Key pair**: A key pair is used for identity authentication when you remotely log in to a node. If no key pair is available, click  **Create a key pair**  and create one.
    -   **Advanced ECS Settings**: \(Optional\) Click  ![](figures/icon-monitoring.png)  to show advanced ECS settings.
        -   **ECS Group**: Select an existing ECS group, or click  **Create ECS Group**  to create a new one. After the ECS group is created, click the refresh icon.

            An ECS group allows you to create ECSs on different hosts, thereby improving service reliability.

        -   **Resource Tags**: By adding tags to resources, you can classify resources.

            You can create predefined tags in Tag Management Service \(TMS\). Predefined tags are visible to all service resources that support the tagging function. You can use predefined tags to improve tag creation and migration efficiency. 

            CCE will automatically create the "CCE-Dynamic-Provisioning-Node=node id" tag. A maximum of 20 tags can be added.

        -   **Agency Name**: An agency is created by the account administrator on the IAM console. By creating an agency, you can share your cloud server resources with another account, or entrust a more professional person or team to manage your resources. To authorize ECS or BMS to call cloud services, select  **Cloud service**  as the agency type, click  **Select**, and then select  **ECS BMS**.
        -   **Pre-installation Script**: Enter a maximum of 1,000 characters.

            The script will be executed before Kubernetes software is installed. Note that if the script is incorrect, Kubernetes software may not be installed successfully. The script is usually used to format data disks.

        -   **Post-installation Script**: Enter a maximum of 1,000 characters.

            The script will be executed after Kubernetes software is installed and will not affect the installation. The script is usually used to modify Docker parameters.

        -   **Add Data Disk**: Click  **Add Data Disk**  to add a data disk and set the capacity of the data disk. To simplify disk formatting, you can enter the disk formatting command in the input box of  **Pre-installation Script**. For details, see  [How Do I Add a Second Data Disk to a Node in a CCE Cluster?](how-do-i-add-a-second-data-disk-to-a-node-in-a-cce-cluster.md).
        -   **Subnet IP Address**: Select  **Automatically assign IP address**  \(recommended\) or  **Manually assigning IP addresses**.

    -   **Advanced Kubernetes Settings**: \(Optional\) Click  ![](figures/icon-monitoring-0.png)  to show advanced ECS settings.
        -   **Max Pods**: The maximum number of pods that can be created on a node, including the system's default pods. Value range: 16 to 250.

            This maximum limit prevents the node from being overloaded by managing too many pods.

        -   **insecure-registries**: Click  **Add insecure-registry**  and enter the address of the image repository.

            Add the address of the custom image repository with no valid SSL certificate to the docker startup option to avoid unsuccessful image pulling from the personal image repository. The address is in the format of IP address:Port number \(or domain name\). Post-installation script and insecure-registries cannot be used together.

        -   **Maximum Data Space per Container**: the maximum data space that can be used by a container. Value range: 10 GB to 80 GB. If the value of this field is larger than the data disk space allocated to Docker, the latter will override the value specified here. Typically, 90% of the data disk space is allocated to Docker. This parameter is displayed only for clusters of v1.13.10-r0 and later.

    -   **Nodes**: The specified number of nodes cannot exceed the maximum number of nodes that can be managed by the cluster.

4.  Click  **Next: Install Add-on**  to install add-ons.

    System resource add-ons must be installed. Advanced functional add-ons are optional.

    You can also install optional add-ons after the cluster is created. To do so, choose  **Add-ons**  in the navigation pane of the CCE console and select the add-on you will install. For details, see  [Add-ons](addons).

5.  Click  **Next: Confirm**. Read the product constraints and select  **I am aware of the above limitations**. Confirm the configured parameters and specifications.
6.  Confirm the specifications, and click  **Submit**.

    It takes about 6 to 10 minutes to create a cluster. You can click  **Back to Cluster List**  to perform other operations on the cluster or click  **Go to Cluster Events**  to view the cluster details.


## Related Operations<a name="section125261255139"></a>

-   After creating a cluster, you can use the Kubernetes command line \(CLI\) tool kubectl to connect to the cluster. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).
-   Add more nodes to the cluster. For details, see  [Creating a Node](creating-a-node.md).
-   Log in to a node. For details, see  [Logging In to a Node](logging-in-to-a-node.md).

-   Create a namespace. You can create multiple namespaces in a cluster and organize resources in the cluster into different namespaces. These namespaces serve as logical groups and can be managed separately. For more information about how to create a namespace for a cluster, see  [Namespace](namespace.md).
-   Click the cluster name to view cluster details.

    **Table  3**  Cluster details

    <a name="table1642185503514"></a>
    <table><thead align="left"><tr id="row1264365516359"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p76431955153512"><a name="p76431955153512"></a><a name="p76431955153512"></a>Tab</p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p176431155163517"><a name="p176431155163517"></a><a name="p176431155163517"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5975069716956"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p796825616956"><a name="p796825616956"></a><a name="p796825616956"></a>Cluster Details</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p4144902016956"><a name="p4144902016956"></a><a name="p4144902016956"></a>View the details and operating status of the cluster.</p>
    </td>
    </tr>
    <tr id="row106431055133510"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1364315552359"><a name="p1364315552359"></a><a name="p1364315552359"></a>Monitoring</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5583863516649"><a name="p5583863516649"></a><a name="p5583863516649"></a>Check the CPU and memory usage of the cluster over the past 1 hour, 3 hours, or 12 hours.</p>
    </td>
    </tr>
    <tr id="row1464335593515"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1264365518351"><a name="p1264365518351"></a><a name="p1264365518351"></a>Events</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><a name="ul42186174161243"></a><a name="ul42186174161243"></a><ul id="ul42186174161243"><li>View cluster events on the <strong id="b842352706143826"><a name="b842352706143826"></a><a name="b842352706143826"></a>Events</strong> tab page.</li><li>Set search criteria. For example, you can set the time segment or enter an event name to view corresponding events.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


