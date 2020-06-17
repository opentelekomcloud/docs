# Migrating Clusters<a name="cce_01_9996"></a>

Create VM clusters on the CCE 2.0 console. These new VM clusters should have the same specifications with those created on CCE 1.0.

To create clusters using APIs, see  _Cloud Container Engine API Reference 2.0_.

## Procedure<a name="section19537122151811"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Clusters**. Click  **Create VM Cluster**.
2.  Set cluster parameters. Parameters with \* are mandatory.

    **Figure  1**  Cluster specifications in CCE 1.0<a name="fig106971619281"></a>  
    ![](figures/cluster-specifications-in-cce-1-0.png "cluster-specifications-in-cce-1-0")

    **Table  1**  Parameters for creating a cluster

    <a name="table719344644718"></a>
    <table><thead align="left"><tr id="row41944465471"><th class="cellrowborder" valign="top" width="33.32666733326668%" id="mcps1.2.4.1.1"><p id="p121946465472"><a name="p121946465472"></a><a name="p121946465472"></a>Parameter in CCE 2.0</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33666633336666%" id="mcps1.2.4.1.2"><p id="p1819474624712"><a name="p1819474624712"></a><a name="p1819474624712"></a>Parameter in CCE 1.0</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33666633336666%" id="mcps1.2.4.1.3"><p id="p919444644711"><a name="p919444644711"></a><a name="p919444644711"></a>Configuration</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row111944461478"><td class="cellrowborder" valign="top" width="33.32666733326668%" headers="mcps1.2.4.1.1 "><p id="p7194146104719"><a name="p7194146104719"></a><a name="p7194146104719"></a>* Cluster Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.2 "><p id="p4194104610478"><a name="p4194104610478"></a><a name="p4194104610478"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.3 "><p id="p13359185414815"><a name="p13359185414815"></a><a name="p13359185414815"></a>Name of the cluster to be created.</p>
    </td>
    </tr>
    <tr id="row61941446114718"><td class="cellrowborder" valign="top" width="33.32666733326668%" headers="mcps1.2.4.1.1 "><p id="p5194114614719"><a name="p5194114614719"></a><a name="p5194114614719"></a>*Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.2 "><p id="p1819424615471"><a name="p1819424615471"></a><a name="p1819424615471"></a>This parameter does not exist in CCE 1.0. Retain the default value.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.3 "><p id="p1819544694716"><a name="p1819544694716"></a><a name="p1819544694716"></a>Cluster version, namely, corresponding Kubernetes baseline version.</p>
    </td>
    </tr>
    <tr id="row819554684711"><td class="cellrowborder" valign="top" width="33.32666733326668%" headers="mcps1.2.4.1.1 "><p id="p019544612477"><a name="p019544612477"></a><a name="p019544612477"></a>*Management Scale</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.2 "><p id="p13195174615471"><a name="p13195174615471"></a><a name="p13195174615471"></a>This parameter does not exist in CCE 1.0. Set this parameter based on your requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.3 "><p id="p1332691794920"><a name="p1332691794920"></a><a name="p1332691794920"></a>Maximum number of nodes that can be managed by the cluster.</p>
    </td>
    </tr>
    <tr id="row15195104634719"><td class="cellrowborder" valign="top" width="33.32666733326668%" headers="mcps1.2.4.1.1 "><p id="p61954462472"><a name="p61954462472"></a><a name="p61954462472"></a>* High Availability</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.2 "><p id="p161950461470"><a name="p161950461470"></a><a name="p161950461470"></a>Cluster Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.3 "><a name="ul327822913496"></a><a name="ul327822913496"></a><ul id="ul327822913496"><li><strong id="b842352706171012"><a name="b842352706171012"></a><a name="b842352706171012"></a>Yes</strong>: The cluster has three master nodes. The cluster is still available even when two master nodes are down.</li><li><strong id="b842352706172612"><a name="b842352706172612"></a><a name="b842352706172612"></a>No</strong>: The cluster has only one master node. If the master node is down, the whole cluster becomes unavailable, but existing applications are not affected.</li></ul>
    </td>
    </tr>
    <tr id="row41950463470"><td class="cellrowborder" valign="top" width="33.32666733326668%" headers="mcps1.2.4.1.1 "><p id="p1619512465472"><a name="p1619512465472"></a><a name="p1619512465472"></a>*VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.2 "><p id="p919554615475"><a name="p919554615475"></a><a name="p919554615475"></a>VPCs created in CCE 1.0 can be used in CCE 2.0.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.3 "><p id="p168051740164919"><a name="p168051740164919"></a><a name="p168051740164919"></a>VPC where the new cluster is located.</p>
    <p id="p20805940184919"><a name="p20805940184919"></a><a name="p20805940184919"></a>If no VPCs are available, click <span class="uicontrol" id="uicontrol13805840174914"><a name="uicontrol13805840174914"></a><a name="uicontrol13805840174914"></a><b><span id="text1580544017495"><a name="text1580544017495"></a><a name="text1580544017495"></a>Create a </span>VPC</b></span>.</p>
    </td>
    </tr>
    <tr id="row4195446174711"><td class="cellrowborder" valign="top" width="33.32666733326668%" headers="mcps1.2.4.1.1 "><p id="p17195124684714"><a name="p17195124684714"></a><a name="p17195124684714"></a>*Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.2 "><p id="p719514617477"><a name="p719514617477"></a><a name="p719514617477"></a>Subnets created in CCE 1.0 can be used in CCE 2.0.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.3 "><p id="p1019504613475"><a name="p1019504613475"></a><a name="p1019504613475"></a>Subnet in which the cluster will run.</p>
    </td>
    </tr>
    <tr id="row15195104604716"><td class="cellrowborder" valign="top" width="33.32666733326668%" headers="mcps1.2.4.1.1 "><p id="p819564610471"><a name="p819564610471"></a><a name="p819564610471"></a>*Network Model</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.2 "><p id="p191958466470"><a name="p191958466470"></a><a name="p191958466470"></a>This parameter does not exist in CCE 1.0. Set this parameter based on your requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.3 "><a name="ul9659865509"></a><a name="ul9659865509"></a><ul id="ul9659865509"><li><strong id="b134963219220"><a name="b134963219220"></a><a name="b134963219220"></a>Tunnel network</strong>: An independent container network constructed using VXLAN tunnels based on the underlying VPC network. This model is appropriate for typical scenarios.</li><li><strong id="b101229131337"><a name="b101229131337"></a><a name="b101229131337"></a>VPC network</strong>: The VPC routing mode is used to deeply integrate with the underlying network. This mode applies to high-performance scenarios where the number of nodes is limited by the VPC routing quota. Only one cluster using the VPC network model can be created in a single VPC.</li></ul>
    </td>
    </tr>
    <tr id="row15435442162514"><td class="cellrowborder" valign="top" width="33.32666733326668%" headers="mcps1.2.4.1.1 "><p id="p943584232511"><a name="p943584232511"></a><a name="p943584232511"></a>Container Network Segment</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.2 "><p id="p12435442172520"><a name="p12435442172520"></a><a name="p12435442172520"></a>This parameter does not exist in CCE 1.0. Set this parameter based on your requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.3 "><p id="p31209167171234"><a name="p31209167171234"></a><a name="p31209167171234"></a>Select a container network segment based on service requirements. Container instances will be assigned with IP addresses within the planned network segment.</p>
    <a name="ul1423120351449"></a><a name="ul1423120351449"></a><ul id="ul1423120351449"><li>If <strong id="b754142617017"><a name="b754142617017"></a><a name="b754142617017"></a>Automatically select</strong> is deselected, enter a CIDR block manually. If the selected CIDR block conflicts with a subnet CIDR block, the system prompts you to select another CIDR block. The recommended CIDR blocks are 10.0.0.0/12-19, 172.16.0.0/16-19, and 192.168.0.0/16-19.<p id="p158661543014"><a name="p158661543014"></a><a name="p158661543014"></a>If different clusters share a container network segment, an IP address conflict will occur and access to the applications in the clusters may fail.</p>
    </li><li>If <strong id="b71579715212"><a name="b71579715212"></a><a name="b71579715212"></a>Automatically select</strong> is selected, the system automatically assigns a CIDR block that does not conflict with any subnet CIDR block.</li></ul>
    <p id="p873618346117"><a name="p873618346117"></a><a name="p873618346117"></a>The mask of the container CIDR block must be appropriate. It determines the number of available nodes in a cluster. A too small mask value will cause the cluster to soon fall short of nodes. After the mask is set, the estimated maximum number of containers supported by the current CIDR block will be displayed.</p>
    </td>
    </tr>
    <tr id="row18518105316198"><td class="cellrowborder" valign="top" width="33.32666733326668%" headers="mcps1.2.4.1.1 "><p id="p115197538194"><a name="p115197538194"></a><a name="p115197538194"></a>Service Network Segment</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.2 "><p id="p1519253191918"><a name="p1519253191918"></a><a name="p1519253191918"></a>This parameter does not exist in CCE 1.0. Set this parameter based on your requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.3 "><p id="p1670517155126"><a name="p1670517155126"></a><a name="p1670517155126"></a>This parameter is left unspecified, by default. This parameter applies only to clusters of v1.11.7 and later versions.</p>
    <p id="p977633218244"><a name="p977633218244"></a><a name="p977633218244"></a>This parameter indicates a CIDR block of Kubernetes services. The mask of the service CIDR block must be appropriate. It determines the number of available nodes in a cluster.</p>
    </td>
    </tr>
    <tr id="row18755646142217"><td class="cellrowborder" valign="top" width="33.32666733326668%" headers="mcps1.2.4.1.1 "><p id="p15755124612219"><a name="p15755124612219"></a><a name="p15755124612219"></a>Open EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.2 "><p id="p77551846122212"><a name="p77551846122212"></a><a name="p77551846122212"></a>This parameter does not exist in CCE 1.0. Set this parameter based on your requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.3 "><p id="p102917292184"><a name="p102917292184"></a><a name="p102917292184"></a>A public IP address that is reachable from public networks. Select an EIP that has not been bound to any node. A cluster's EIP is preset in the cluster's certificate. Do no delete the EIP after the cluster has been created. Otherwise, two-way authentication will fail.</p>
    <a name="ul126461217182315"></a><a name="ul126461217182315"></a><ul id="ul126461217182315"><li><strong id="b3774148151915"><a name="b3774148151915"></a><a name="b3774148151915"></a>Do no configure</strong>: No EIP will be preset in the cluster certificate.</li><li><strong id="b62171020122020"><a name="b62171020122020"></a><a name="b62171020122020"></a>Configure now</strong>: If no EIP is available for selection, create a new EIP.</li></ul>
    </td>
    </tr>
    <tr id="row112688564198"><td class="cellrowborder" valign="top" width="33.32666733326668%" headers="mcps1.2.4.1.1 "><p id="p37371717105616"><a name="p37371717105616"></a><a name="p37371717105616"></a>Authorization Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.2 "><p id="p1226813566192"><a name="p1226813566192"></a><a name="p1226813566192"></a>This parameter does not exist in CCE 1.0. Set this parameter based on your requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.3 "><p id="p13737141735611"><a name="p13737141735611"></a><a name="p13737141735611"></a>By default, <span class="uicontrol" id="uicontrol13753167101316"><a name="uicontrol13753167101316"></a><a name="uicontrol13753167101316"></a><b>RBAC</b></span> is selected. Read <a href="granting-namespace-level-permissions-(kubernetes-rbac-authorization).md">CCE Role Management Instructions</a> and select <span class="uicontrol" id="uicontrol1663915553130"><a name="uicontrol1663915553130"></a><a name="uicontrol1663915553130"></a><b>I am aware of the above limitations and read the CCE Role Management Instructions</b></span>.</p>
    <p id="p16141515161117"><a name="p16141515161117"></a><a name="p16141515161117"></a>After RBAC is enabled, users access resources in the cluster according to fine-grained permissions policies.</p>
    </td>
    </tr>
    <tr id="row12131512162315"><td class="cellrowborder" valign="top" width="33.32666733326668%" headers="mcps1.2.4.1.1 "><p id="p21461217230"><a name="p21461217230"></a><a name="p21461217230"></a>Authentication Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.2 "><p id="p1214101252312"><a name="p1214101252312"></a><a name="p1214101252312"></a>This parameter does not exist in CCE 1.0. Set this parameter based on your requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.3 "><p id="p933784218111"><a name="p933784218111"></a><a name="p933784218111"></a>The authentication mechanism performs permission control on resources in a cluster. For example, you can grant user A to read and write applications in a namespace, while granting user B to only read resources in a cluster. For details about role-based permission control, see <a href="cluster-management-permission-control.md">3.7- Cluster Management Permission Control</a>.</p>
    <a name="ul208851410646"></a><a name="ul208851410646"></a><ul id="ul208851410646"><li>By default, X.509 authentication instead of <span class="uicontrol" id="uicontrol1371105874614"><a name="uicontrol1371105874614"></a><a name="uicontrol1371105874614"></a><b>Enhanced authentication</b></span> is enabled. X.509 is a standard defining the format of public key certificates. X.509 certificates are used in many Internet protocols.</li><li>If permission control on a cluster is required, select <strong id="b1631132022213"><a name="b1631132022213"></a><a name="b1631132022213"></a>Enhanced authentication</strong> and then <strong id="b113212042216"><a name="b113212042216"></a><a name="b113212042216"></a>Authenticating Proxy</strong>.<p id="p129632614510"><a name="p129632614510"></a><a name="p129632614510"></a>Click <strong id="b185463373227"><a name="b185463373227"></a><a name="b185463373227"></a>Upload</strong> next to <strong id="b1354616374228"><a name="b1354616374228"></a><a name="b1354616374228"></a>CA Root Certificate</strong> to upload a valid certificate. Select the check box to confirm that the uploaded certificate is valid.</p>
    <p id="p36719411534"><a name="p36719411534"></a><a name="p36719411534"></a>If the certificate is invalid, the cluster cannot be created. The uploaded certificate file must be smaller than 1 MB and in .crt or .cer format.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row1519564604716"><td class="cellrowborder" valign="top" width="33.32666733326668%" headers="mcps1.2.4.1.1 "><p id="p19195154664715"><a name="p19195154664715"></a><a name="p19195154664715"></a>Cluster Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.2 "><p id="p8195246194719"><a name="p8195246194719"></a><a name="p8195246194719"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33666633336666%" headers="mcps1.2.4.1.3 "><p id="p7195194624713"><a name="p7195194624713"></a><a name="p7195194624713"></a>Description of the cluster.</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  After the configuration is complete, click  **Next**  to add a node.
4.  Continue to add a node.
5.  Set the parameters based on  [Table 2](#table16351025186).

    **Table  2**  Parameters for adding a node

    <a name="table16351025186"></a>
    <table><thead align="left"><tr id="row1380143111819"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p19809311186"><a name="p19809311186"></a><a name="p19809311186"></a>Parameter in CCE 2.0</p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.2"><p id="p18801235187"><a name="p18801235187"></a><a name="p18801235187"></a>Parameter in CCE 1.0</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="p18803317189"><a name="p18803317189"></a><a name="p18803317189"></a>Configuration</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row138010391812"><td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.4.1.1 mcps1.2.4.1.2 mcps1.2.4.1.3 "><p id="p380193141810"><a name="p380193141810"></a><a name="p380193141810"></a>Region</p>
    </td>
    </tr>
    <tr id="row926763182720"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p7267831142718"><a name="p7267831142718"></a><a name="p7267831142718"></a>Current Region</p>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p02449717228"><a name="p02449717228"></a><a name="p02449717228"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p182671631162718"><a name="p182671631162718"></a><a name="p182671631162718"></a>Physical location of the node.</p>
    </td>
    </tr>
    <tr id="row14803371815"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p28019331810"><a name="p28019331810"></a><a name="p28019331810"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="li177052161496p0"><a name="li177052161496p0"></a><a name="li177052161496p0"></a>An AZ is an isolated area in which physical resources use independent power supplies and networks. AZs are interconnected through internal networks. To enhance application availability, create nodes in different AZs.</p>
    </td>
    </tr>
    <tr id="row18011321814"><td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.4.1.1 mcps1.2.4.1.2 mcps1.2.4.1.3 "><p id="p683193181810"><a name="p683193181810"></a><a name="p683193181810"></a>Specifications</p>
    </td>
    </tr>
    <tr id="row18317361811"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p188314321811"><a name="p188314321811"></a><a name="p188314321811"></a>Node Name</p>
    </td>
    <td class="cellrowborder" rowspan="3" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p583331184"><a name="p583331184"></a><a name="p583331184"></a>Specifications</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p383143141818"><a name="p383143141818"></a><a name="p383143141818"></a>Name of the node.</p>
    </td>
    </tr>
    <tr id="row9836311812"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p198319361812"><a name="p198319361812"></a><a name="p198319361812"></a>Specifications</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="ul13834318182"></a><a name="ul13834318182"></a><ul id="ul13834318182"><li><strong id="b84381459326"><a name="b84381459326"></a><a name="b84381459326"></a>General-purpose</strong>: provides general computing, storage, and network configurations that can meet a majority of scenarios. General-purpose nodes can be used for web servers, workload development, workload testing, and small databases.</li><li><strong id="b0853353123213"><a name="b0853353123213"></a><a name="b0853353123213"></a>Memory-optimized</strong>: provides higher memory capacity than general-purpose nodes and is suitable for relational databases, NoSQL, and other workloads that are both memory-intensive and data-intensive.</li><li><strong id="b6795175616321"><a name="b6795175616321"></a><a name="b6795175616321"></a>GPU-accelerated</strong>: provides powerful floating-point computing and is suitable for real-time, highly concurrent massive computing. Graphical processing units (GPUs) of P series are suitable for deep learning, scientific computing, and CAE. GPUs of G series are suitable for 3D animation rendering and CAD. Currently, only clusters of v1.11 support GPU-accelerated nodes. If the cluster version is v1.13 or later, <strong id="b358315533315"><a name="b358315533315"></a><a name="b358315533315"></a>GPU-accelerated</strong> is not displayed on the page.</li></ul>
    </td>
    </tr>
    <tr id="row178313381813"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p08318320187"><a name="p08318320187"></a><a name="p08318320187"></a>OS</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1258174011292"><a name="p1258174011292"></a><a name="p1258174011292"></a>Select an operating system for the node.</p>
    <p id="p47999261331"><a name="p47999261331"></a><a name="p47999261331"></a>Reinstalling OSs or modifying OS configurations could make nodes unavailable. Exercise caution when performing these operations. For more information, see <a href="risky-operations-on-cluster-nodes.md">Risky Operations on Cluster Nodes</a>.</p>
    </td>
    </tr>
    <tr id="row950585532910"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p25051955142914"><a name="p25051955142914"></a><a name="p25051955142914"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p14505115511292"><a name="p14505115511292"></a><a name="p14505115511292"></a>This parameter does not exist in CCE 1.0. Set this parameter based on your requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p14505155572912"><a name="p14505155572912"></a><a name="p14505155572912"></a>The value cannot be changed. This parameter is supported only in v1.13.10-r0 and later versions of clusters. It is not displayed in versions earlier than v1.13.10-r0.</p>
    </td>
    </tr>
    <tr id="row18842158122911"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p20842195882912"><a name="p20842195882912"></a><a name="p20842195882912"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p1784210585290"><a name="p1784210585290"></a><a name="p1784210585290"></a>This parameter does not exist in CCE 1.0. Set this parameter based on your requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1330216329308"><a name="p1330216329308"></a><a name="p1330216329308"></a>A subnet improves network security by providing exclusive network resources that are isolated from other networks.</p>
    <p id="p165159103173"><a name="p165159103173"></a><a name="p165159103173"></a>You can select any subnet in the cluster VPC. Cluster nodes can belong to different subnets. This parameter is supported only in v1.13.10-r0 and later versions of clusters. It is not displayed in versions earlier than v1.13.10-r0.</p>
    </td>
    </tr>
    <tr id="row6831538187"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p083113121816"><a name="p083113121816"></a><a name="p083113121816"></a>Nodes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p883431187"><a name="p883431187"></a><a name="p883431187"></a>Quantity</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1583143171820"><a name="p1583143171820"></a><a name="p1583143171820"></a>Number of nodes to be created.</p>
    </td>
    </tr>
    <tr id="row12831038186"><td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.4.1.1 mcps1.2.4.1.2 mcps1.2.4.1.3 "><p id="p108315311810"><a name="p108315311810"></a><a name="p108315311810"></a>Network</p>
    <div class="note" id="note1067410216188"><a name="note1067410216188"></a><a name="note1067410216188"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p188420311810"><a name="p188420311810"></a><a name="p188420311810"></a>If the nodes to be created require Internet access, select <strong id="b167012020101215"><a name="b167012020101215"></a><a name="b167012020101215"></a>Automatically assign</strong> or <strong id="b14701520131217"><a name="b14701520131217"></a><a name="b14701520131217"></a>Use existing</strong> for <strong id="b070112010123"><a name="b070112010123"></a><a name="b070112010123"></a>EIP</strong>. If an EIP is not bound to a node, applications running on the node cannot be accessed by the external network.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row11841033189"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p158411391811"><a name="p158411391811"></a><a name="p158411391811"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p18841331819"><a name="p18841331819"></a><a name="p18841331819"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1084143141814"><a name="p1084143141814"></a><a name="p1084143141814"></a>A public IP address that is reachable from public networks.</p>
    <a name="ul14841934185"></a><a name="ul14841934185"></a><ul id="ul14841934185"><li><strong id="b22048311322"><a name="b22048311322"></a><a name="b22048311322"></a>Do not use</strong>: A node without an EIP cannot access the Internet. It can be used only as an elastic cloud server (ECS) for deploying services or clusters on a private network.</li><li><strong id="b1504126181514"><a name="b1504126181514"></a><a name="b1504126181514"></a>Automatically assign</strong>: An EIP with exclusive bandwidth is automatically assigned to each ECS. When creating an ECS, ensure that the elastic IP address quota is sufficient. Set the specifications, required quantity, billing mode, and bandwidth as required.</li><li><strong id="b2299857182012"><a name="b2299857182012"></a><a name="b2299857182012"></a>Use existing</strong>: Existing EIPs are assigned to the nodes to be created.</li></ul>
    </td>
    </tr>
    <tr id="row98413311820"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p5841331182"><a name="p5841331182"></a><a name="p5841331182"></a>Disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p2084183131819"><a name="p2084183131819"></a><a name="p2084183131819"></a>Storage</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><div class="p" id="p32291130113920"><a name="p32291130113920"></a><a name="p32291130113920"></a>Disk type, which can be <strong id="b912017972517"><a name="b912017972517"></a><a name="b912017972517"></a>System Disk</strong> or <strong id="b51202982512"><a name="b51202982512"></a><a name="b51202982512"></a>Data Disk</strong>.<a name="ul1848032811217"></a><a name="ul1848032811217"></a><ul id="ul1848032811217"><li>The system disk capacity ranges from 40 to 1024 GB. The default value is 40 GB.</li><li>The data disk capacity ranges from 100 to 32678 GB. The default value is 100 GB.</li></ul>
    </div>
    <p id="p84931828182118"><a name="p84931828182118"></a><a name="p84931828182118"></a>Data disks deliver three levels of I/O performance:</p>
    <a name="ul64951628112115"></a><a name="ul64951628112115"></a><ul id="ul64951628112115"><li><strong id="b1965924217581"><a name="b1965924217581"></a><a name="b1965924217581"></a>Common I/O</strong>: uses SATA drives to store data. EVS disks of this level provide reliable block storage and a maximum IOPS of 1,000 per disk. They are suitable for key applications.</li><li><strong id="b449525045915"><a name="b449525045915"></a><a name="b449525045915"></a>High I/O</strong>: uses SAS drives to store data. EVS disks of this level provide a maximum IOPS of 3,000 and a minimum read/write latency of 1 ms. They are suitable for RDS, NoSQL, data warehouse, and file system applications.</li><li><strong id="b389210152012"><a name="b389210152012"></a><a name="b389210152012"></a>Ultra-high I/O</strong>: uses SSD drives to store data. EVS disks of this level provide a maximum IOPS of 20,000 and a minimum read/write latency of 1 ms. They are suitable for RDS, NoSQL, and data warehouse applications.</li></ul>
    </td>
    </tr>
    <tr id="row13851631189"><td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.4.1.1 mcps1.2.4.1.2 mcps1.2.4.1.3 "><p id="p98511341813"><a name="p98511341813"></a><a name="p98511341813"></a>Login information</p>
    </td>
    </tr>
    <tr id="row1085193111812"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p9859310183"><a name="p9859310183"></a><a name="p9859310183"></a>Key Pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p10851311185"><a name="p10851311185"></a><a name="p10851311185"></a>Key Pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1285936183"><a name="p1285936183"></a><a name="p1285936183"></a>A key pair is used for identity authentication when you remotely log in to a node. If no key pair is available, click <strong id="b1066412472518"><a name="b1066412472518"></a><a name="b1066412472518"></a>Create a key pair</strong> and create one.</p>
    </td>
    </tr>
    <tr id="row485103201812"><td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.4.1.1 mcps1.2.4.1.2 mcps1.2.4.1.3 "><p id="p1885938185"><a name="p1885938185"></a><a name="p1885938185"></a>Advanced ECS Settings</p>
    </td>
    </tr>
    <tr id="row1980213371444"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p3802123713448"><a name="p3802123713448"></a><a name="p3802123713448"></a>ECS Group</p>
    </td>
    <td class="cellrowborder" rowspan="7" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p3927055114816"><a name="p3927055114816"></a><a name="p3927055114816"></a>This parameter does not exist in CCE 1.0. Set this parameter based on your requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p7325184317489"><a name="p7325184317489"></a><a name="p7325184317489"></a>Select an existing ECS group, or click <span class="uicontrol" id="uicontrol18315104663515"><a name="uicontrol18315104663515"></a><a name="uicontrol18315104663515"></a><b>Create ECS Group</b></span> to create a new one. After the ECS group is created, click the refresh icon.</p>
    <p id="p4227124213218"><a name="p4227124213218"></a><a name="p4227124213218"></a>An ECS group allows you to create ECSs on different hosts, thereby improving service reliability.</p>
    </td>
    </tr>
    <tr id="row770816592447"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1270865944411"><a name="p1270865944411"></a><a name="p1270865944411"></a>Resource Tags</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p975613243456"><a name="p975613243456"></a><a name="p975613243456"></a>By adding tags to resources, you can classify resources.</p>
    <p id="p10327184710426"><a name="p10327184710426"></a><a name="p10327184710426"></a>You can create predefined tags in Tag Management Service (TMS). Predefined tags are visible to all service resources that support the tagging function. You can use predefined tags to improve tag creation and migration efficiency. For details, see <a href="https://docs.otc.t-systems.com/en-us/usermanual/tms/en-us_topic_0144368884.html" target="_blank" rel="noopener noreferrer">Creating Predefined Tags</a>.</p>
    <p id="p1311422274512"><a name="p1311422274512"></a><a name="p1311422274512"></a>CCE will automatically create the "CCE-Dynamic-Provisioning-Node=node id" tag. A maximum of 20 tags can be added.</p>
    </td>
    </tr>
    <tr id="row10556133134513"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p125562033174515"><a name="p125562033174515"></a><a name="p125562033174515"></a>Agency Name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p96304546457"><a name="p96304546457"></a><a name="p96304546457"></a>The agency is created by the account administrator on the IAM console. By creating an agency, you can share your resources with another account, or delegate a more professional person or team to manage your resources. When creating an agency, set the agency type to <strong id="b56366226449"><a name="b56366226449"></a><a name="b56366226449"></a>Cloud service</strong>. Click <strong id="b13411946104411"><a name="b13411946104411"></a><a name="b13411946104411"></a>Select</strong>, and select <strong id="b197501418459"><a name="b197501418459"></a><a name="b197501418459"></a>ECS BMS</strong> in the dialog box displayed, which allows ECS or BMS to call cloud services.</p>
    </td>
    </tr>
    <tr id="row16961102914515"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p16961122914515"><a name="p16961122914515"></a><a name="p16961122914515"></a>Pre-installation Script</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p98763572469"><a name="p98763572469"></a><a name="p98763572469"></a>Script commands. Enter 0 to 1000 characters.</p>
    <p id="p1956335218469"><a name="p1956335218469"></a><a name="p1956335218469"></a>The script will be executed before Kubernetes software is installed. Note that if the script is incorrect, Kubernetes software may not be installed successfully. The script is usually used to format data disks.</p>
    </td>
    </tr>
    <tr id="row474002711458"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1574042754510"><a name="p1574042754510"></a><a name="p1574042754510"></a>Post-installation Script</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p18628174413478"><a name="p18628174413478"></a><a name="p18628174413478"></a>Script commands. Enter 0 to 1000 characters.</p>
    <p id="p121041911114618"><a name="p121041911114618"></a><a name="p121041911114618"></a>The script will be executed after Kubernetes software is installed and will not affect the installation. The script is usually used to modify Docker parameters.</p>
    </td>
    </tr>
    <tr id="row014232420462"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p61428243461"><a name="p61428243461"></a><a name="p61428243461"></a>Add Data Disk</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1814215244461"><a name="p1814215244461"></a><a name="p1814215244461"></a>Click <strong id="b650211569524"><a name="b650211569524"></a><a name="b650211569524"></a>Add Data Disk</strong> to add a data disk and set the capacity of the data disk. Enter a disk formatting command in the input box of <a href="how-do-i-add-a-second-data-disk-to-a-cce-node.md">Pre-installation Script</a>. For a sample command, see <a href="how-do-i-add-a-second-data-disk-to-a-cce-node.md">How Do I Add a Second Data Disk to a CCE Node?</a>.</p>
    </td>
    </tr>
    <tr id="row1510851394712"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p91081813144715"><a name="p91081813144715"></a><a name="p91081813144715"></a>Subnet IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p14108181324717"><a name="p14108181324717"></a><a name="p14108181324717"></a>Select <strong id="b929155565520"><a name="b929155565520"></a><a name="b929155565520"></a>Automatically assign IP address</strong> (recommended) or <strong id="b6305556555"><a name="b6305556555"></a><a name="b6305556555"></a>Manually assigning IP addresses</strong>.</p>
    </td>
    </tr>
    <tr id="row1366141311492"><td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.4.1.1 mcps1.2.4.1.2 mcps1.2.4.1.3 "><p id="p103660132494"><a name="p103660132494"></a><a name="p103660132494"></a>Advanced Kubernetes Settings</p>
    </td>
    </tr>
    <tr id="row13385113320498"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1438603324917"><a name="p1438603324917"></a><a name="p1438603324917"></a>Max Pods</p>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p468274605013"><a name="p468274605013"></a><a name="p468274605013"></a>This parameter does not exist in CCE 1.0. Set this parameter based on your requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p2753113812503"><a name="p2753113812503"></a><a name="p2753113812503"></a>The maximum number of pods that can be created on a node, including the system's default pods. Value range: 16 to 250.</p>
    <p id="p1867372514496"><a name="p1867372514496"></a><a name="p1867372514496"></a>This maximum limit prevents the node from being overloaded by managing too many instances.</p>
    </td>
    </tr>
    <tr id="row47510365497"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p775436164920"><a name="p775436164920"></a><a name="p775436164920"></a>insecure-registries</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p11638194095014"><a name="p11638194095014"></a><a name="p11638194095014"></a>Click <strong id="b65644457574"><a name="b65644457574"></a><a name="b65644457574"></a>Add insecure-registry</strong> and enter a repository address.</p>
    <p id="p72681429135017"><a name="p72681429135017"></a><a name="p72681429135017"></a>Add the address of the custom image repository with no valid SSL certificate to the docker startup option to avoid unsuccessful image pulling from the personal image repository. The address is in the format of IP address:Port number (or domain name). Post-installation script and insecure-registries cannot be used together.</p>
    </td>
    </tr>
    <tr id="row2078953145011"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1178916355012"><a name="p1178916355012"></a><a name="p1178916355012"></a>Maximum Data Space per Container</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p3226192019296"><a name="p3226192019296"></a><a name="p3226192019296"></a>This parameter does not exist in CCE 1.0. Set this parameter based on your requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p8789838501"><a name="p8789838501"></a><a name="p8789838501"></a>The maximum data space that can be used by a container. Value range: 10 GB to 80 GB. If the value of this field is larger than the data disk space allocated to Docker, the latter will override the value specified here. Typically, 90% of the data disk space is allocated to Docker. This parameter is supported only in v1.13.10-r0 and later versions of clusters. It is not displayed in versions earlier than v1.13.10-r0.</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Next**  to install add-ons.

    System resource add-ons must be installed. Advanced functional add-ons are optional.

    You can also install optional add-ons after the cluster is created. To do so, choose  **Add-ons**  in the navigation pane of the CCE console and select the add-on you will install. For details, see  [13 Add-on Management](autoscaler.md).

7.  Click  **Create Now**. Check all the configurations, and click  **Submit**.

    It takes 6 to 10 minutes to create a cluster. Information indicating the progress of the creation process will be displayed.


