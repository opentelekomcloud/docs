# Creating a BMS Cluster<a name="cce_01_0029"></a>

Bare metal server \(BMS\) clusters  are Kubernetes container clusters with high computing and high network performance. To use a BMS cluster, enable the  BMS service  first.

To provide a high-speed container network, add a high-speed NIC when creating a BMS.

## Preparation<a name="section15394125210466"></a>

-   A  VPC  is available. If you already have a VPC available, skip this preparatory step.

    A VPC provides an isolated, configurable, and manageable virtual network for CCE clusters. For details, see  [Creating a VPC](https://docs.otc.t-systems.com/en-us/usermanual/vpc/en-us_topic_0013935842.html).


-   You have purchased the BMS service. For details, see  [Creating a BMS](https://docs.otc.t-systems.com/en-us/usermanual/bms/en-us_topic_0053536894.html).
-   A high-speed network has been created. For details, see  [Managing High-Speed Networks](https://docs.otc.t-systems.com/en-us/usermanual/bms/en-us_topic_0053537013.html). The high-speed network is used for communication between  **BMSs**. It provides a network with unlimited bandwidth for  BMSs  in the same AZ.

## Precautions<a name="section19763161913217"></a>

BMS clusters support only nodes whose operating system is EulerOS 2.3.

## Creating a cluster<a name="section463761220269"></a>

1.  Log in to the CCE console, choose  **Resource Management**  \>  **Clusters**  in the navigation pane, and click  **Create**  under  **BMS Cluster**.
2.  Set the parameters listed in  [Table 1](#table8638121213265). The parameters marked with \* are mandatory.

    **Table  1**  Parameters for creating a cluster

    <a name="table8638121213265"></a>
    <table><thead align="left"><tr id="row10638181262612"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p1063821214265"><a name="p1063821214265"></a><a name="p1063821214265"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p1638181232617"><a name="p1638181232617"></a><a name="p1638181232617"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9824857125213"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1282695765211"><a name="p1282695765211"></a><a name="p1282695765211"></a>* Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p161283411302"><a name="p161283411302"></a><a name="p161283411302"></a>To minimize network latency and resource access time, select the nearest region. Cloud resources are region-specific and cannot be used across regions through internal network connections.</p>
    </td>
    </tr>
    <tr id="row1063812126263"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p15639812122620"><a name="p15639812122620"></a><a name="p15639812122620"></a>* Cluster Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p26391512172614"><a name="p26391512172614"></a><a name="p26391512172614"></a>Name of the new cluster, which cannot be changed after the cluster is created.</p>
    <p id="p648712133520"><a name="p648712133520"></a><a name="p648712133520"></a>A cluster name contains 4 to 128 characters starting with a letter and not ending with a hyphen (-). Only lowercase letters, digits, and hyphens (-) are allowed.</p>
    </td>
    </tr>
    <tr id="row1820711165158"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1769363161231"><a name="p1769363161231"></a><a name="p1769363161231"></a>* Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p9100682161231"><a name="p9100682161231"></a><a name="p9100682161231"></a>Kubernetes base version used by the cluster. For details, see <a href="cce-cluster-version-release-notes.md">CCE Cluster Version Release Notes</a>.</p>
    </td>
    </tr>
    <tr id="row434114618372"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p14725432104718"><a name="p14725432104718"></a><a name="p14725432104718"></a>* Management Scale</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p872516326476"><a name="p872516326476"></a><a name="p872516326476"></a>Maximum number of nodes that can be managed by the cluster. If you select 10 nodes, it means that the cluster can manage up to 10 nodes. The cluster management scale cannot be modified after a cluster is created. Exercise caution when creating a cluster.</p>
    <div class="p" id="p102308301014"><a name="p102308301014"></a><a name="p102308301014"></a>Each cluster contains a <span class="uicontrol" id="uicontrol144772569118"><a name="uicontrol144772569118"></a><a name="uicontrol144772569118"></a><b>master node</b></span> and a <span class="uicontrol" id="uicontrol181651027113616"><a name="uicontrol181651027113616"></a><a name="uicontrol181651027113616"></a><b>worker node</b></span>. Each node is a cloud server.<a name="ul1045015327013"></a><a name="ul1045015327013"></a><ul id="ul1045015327013"><li>Master node: controls worker nodes in a cluster. The master node is automatically created along with the cluster, and manages and schedules the entire cluster.</li><li>Worker node: a node that runs the workload you deploy. You can create a worker node either when or after creating the cluster. The master node assigns a worker node to each deployable component of your workload. When a worker node is down, the master node migrates the workload to another worker node.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row128144815371"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p545424120477"><a name="p545424120477"></a><a name="p545424120477"></a>* High Availability</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><a name="ul143401352837"></a><a name="ul143401352837"></a><ul id="ul143401352837"><li><strong id="b89125410139"><a name="b89125410139"></a><a name="b89125410139"></a>Yes</strong>: The cluster has three master nodes. The cluster can continue to serve new workloads even when two master nodes are down.</li><li><strong id="b59699261415"><a name="b59699261415"></a><a name="b59699261415"></a>No</strong>: The cluster has only one master node. If the master node is down, the cluster stops serving new workloads, but existing workloads are not affected.</li></ul>
    <div class="p" id="p1155010435554"><a name="p1155010435554"></a><a name="p1155010435554"></a>The HA setting is a one-time configuration and cannot be changed after the cluster is created. If you want to use another HA setting for the cluster, you have to create a new cluster that has exactly the same parameter settings (except for the <strong id="b918913323411"><a name="b918913323411"></a><a name="b918913323411"></a>High Availability</strong> parameter) as the current cluster. Set this parameter based on your needs.<a name="ul20457121412567"></a><a name="ul20457121412567"></a><ul id="ul20457121412567"><li>In production environments, it is advised to set <strong id="b13912527105415"><a name="b13912527105415"></a><a name="b13912527105415"></a>High Availability</strong> to <strong id="b149122274544"><a name="b149122274544"></a><a name="b149122274544"></a>Yes</strong> to improve cluster's disaster recovery capabilities.</li><li>In R&amp;D and testing environments that do not require high reliability, it is not always necessary to set <strong id="b3416230204915"><a name="b3416230204915"></a><a name="b3416230204915"></a>High Availability</strong> to <strong id="b12417130114918"><a name="b12417130114918"></a><a name="b12417130114918"></a>Yes</strong>.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row1763991215268"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p15639181282617"><a name="p15639181282617"></a><a name="p15639181282617"></a>* VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p116393128265"><a name="p116393128265"></a><a name="p116393128265"></a>VPC where the new cluster is located. A VPC provides a secure and logically isolated network environment.</p>
    <p id="p530273312316"><a name="p530273312316"></a><a name="p530273312316"></a>If no VPC is available, click <span class="uicontrol" id="uicontrol55379598118"><a name="uicontrol55379598118"></a><a name="uicontrol55379598118"></a><b><span id="text1553712591514"><a name="text1553712591514"></a><a name="text1553712591514"></a><span id="text1491832462315"><a name="text1491832462315"></a><a name="text1491832462315"></a>Create a VPC</span></span></b></span>. After the VPC is created, click <strong id="b050374111545"><a name="b050374111545"></a><a name="b050374111545"></a>Refresh</strong>.</p>
    </td>
    </tr>
    <tr id="row15639412132615"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p36391812172618"><a name="p36391812172618"></a><a name="p36391812172618"></a>* Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p817112915173"><a name="p817112915173"></a><a name="p817112915173"></a>The subnet where cluster nodes will run. A subnet improves network security by providing exclusive network resources that are isolated from other networks. For details about the relationship between VPCs, subnets, and clusters, see <a href="cluster-overview.md">Cluster Overview</a>.</p>
    <p id="p157871101173"><a name="p157871101173"></a><a name="p157871101173"></a><strong id="b137264200229"><a name="b137264200229"></a><a name="b137264200229"></a>The selected subnet cannot be modified after the cluster is created. Exercise caution when selecting a subnet.</strong></p>
    </td>
    </tr>
    <tr id="row142110462613"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p821946364"><a name="p821946364"></a><a name="p821946364"></a>* Network Model</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p97010306277"><a name="p97010306277"></a><a name="p97010306277"></a><strong id="b217673910272"><a name="b217673910272"></a><a name="b217673910272"></a>Underlay</strong>: A traditional single-layer network used by data centers to forward packets.</p>
    </td>
    </tr>
    <tr id="row8378645411"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1238034510113"><a name="p1238034510113"></a><a name="p1238034510113"></a>* High-Speed Network</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1459091372318"><a name="p1459091372318"></a><a name="p1459091372318"></a>Select a high-speed network.</p>
    <p id="p1239403116491"><a name="p1239403116491"></a><a name="p1239403116491"></a>The high-speed network is used for communication between <span class="uicontrol" id="uicontrol135925197919375_1"><a name="uicontrol135925197919375_1"></a><a name="uicontrol135925197919375_1"></a><b>BMSs</b></span>. It provides a network with unlimited bandwidth for BMSs in the same AZ.</p>
    </td>
    </tr>
    <tr id="row6514088885942"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p4192057185942"><a name="p4192057185942"></a><a name="p4192057185942"></a>* Container Network Segment</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p31209167171234"><a name="p31209167171234"></a><a name="p31209167171234"></a>Container instances' IP address range.</p>
    <a name="ul1423120351449"></a><a name="ul1423120351449"></a><ul id="ul1423120351449"><li>If <strong id="b754142617017"><a name="b754142617017"></a><a name="b754142617017"></a>Automatically select</strong> is deselected, enter a CIDR block manually. If the selected CIDR block conflicts with a subnet CIDR block, the system prompts you to select another CIDR block. Recommended CIDR block: 10.0.0.0/8 to 16, 172.16.0.0/16, or 192.168.0.0/16.<p id="p158661543014"><a name="p158661543014"></a><a name="p158661543014"></a>If different clusters share a container network segment, an IP address conflict will occur and access to the applications in the clusters may fail.</p>
    </li><li>If <strong id="b71579715212"><a name="b71579715212"></a><a name="b71579715212"></a>Automatically select</strong> is selected, the system automatically assigns a CIDR block that does not conflict with any subnet CIDR block.</li></ul>
    <p id="p4602114991818"><a name="p4602114991818"></a><a name="p4602114991818"></a>The mask of the container CIDR block must be appropriate. It determines the number of available nodes in a cluster. A too small mask value will cause the cluster to soon fall short of nodes. After the mask is set, the estimated maximum number of containers supported by the current CIDR block will be displayed.</p>
    </td>
    </tr>
    <tr id="row16704302913"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1867112313298"><a name="p1867112313298"></a><a name="p1867112313298"></a>* Service Network Segment</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p12817710163613"><a name="p12817710163613"></a><a name="p12817710163613"></a>CIDR block of Kubernetes services.</p>
    <p id="p977633218244"><a name="p977633218244"></a><a name="p977633218244"></a><strong id="b12186135314114"><a name="b12186135314114"></a><a name="b12186135314114"></a>Service Network Segment</strong> is selected by default. Set the network segment to <strong id="b73078191424"><a name="b73078191424"></a><a name="b73078191424"></a>10.247.0.0/16</strong>.</p>
    </td>
    </tr>
    <tr id="row19982173311438"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p2098323374311"><a name="p2098323374311"></a><a name="p2098323374311"></a>Authorization Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p13737141735611"><a name="p13737141735611"></a><a name="p13737141735611"></a>By default, <span class="uicontrol" id="uicontrol13753167101316"><a name="uicontrol13753167101316"></a><a name="uicontrol13753167101316"></a><b>RBAC</b></span> is selected.</p>
    <p id="p16141515161117"><a name="p16141515161117"></a><a name="p16141515161117"></a>After RBAC is enabled, IAM users access resources in the cluster according to fine-grained permissions policies.</p>
    </td>
    </tr>
    <tr id="row899013277910"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p6655100911"><a name="p6655100911"></a><a name="p6655100911"></a>Authentication Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p12648843154534"><a name="p12648843154534"></a><a name="p12648843154534"></a>The authentication mechanism performs permission control on resources in a cluster. For example, you can grant user A to read and write applications in a namespace, while granting user B to only read resources in a cluster. For details on how to control permissions based on user roles, see <a href="cluster-management-permission-control.md">Cluster Management Permission Control</a>.</p>
    <a name="ul1970213201317"></a><a name="ul1970213201317"></a><ul id="ul1970213201317"><li>By default, X.509 authentication instead of enhanced authentication is enabled. X.509 is a standard defining the format of public key certificates.</li><li>If permission control on a cluster is required, select <strong id="b094248203310"><a name="b094248203310"></a><a name="b094248203310"></a>Enhanced authentication</strong> and then <strong id="b294298203315"><a name="b294298203315"></a><a name="b294298203315"></a>Authenticating Proxy</strong>.<p id="p126301343172019"><a name="p126301343172019"></a><a name="p126301343172019"></a>Click <strong id="b3909209153913"><a name="b3909209153913"></a><a name="b3909209153913"></a>Upload</strong> next to <strong id="b119101091394"><a name="b119101091394"></a><a name="b119101091394"></a>CA Root Certificate</strong> to upload a valid certificate. Select the check box to confirm that the uploaded certificate is valid.</p>
    <p id="p1529472012212"><a name="p1529472012212"></a><a name="p1529472012212"></a>If the certificate is invalid, the cluster cannot be created. The uploaded certificate file must be smaller than 1 MB and in .crt or .cer format.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row463941216264"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p2063961212268"><a name="p2063961212268"></a><a name="p2063961212268"></a>Cluster Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p664014125268"><a name="p664014125268"></a><a name="p664014125268"></a>Optional. Enter the description of the new container cluster.</p>
    </td>
    </tr>
    <tr id="row15309827155214"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p6310127105212"><a name="p6310127105212"></a><a name="p6310127105212"></a>Advanced Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1911106205716"><a name="p1911106205716"></a><a name="p1911106205716"></a>Click <a name="image1915010019533"></a><a name="image1915010019533"></a><span><img id="image1915010019533" src="figures/icon-monitoring-0.png"></span> to show advanced functions.</p>
    <p id="p0742457132419"><a name="p0742457132419"></a><a name="p0742457132419"></a>Advanced settings will be displayed only if they are supported in the selected AZ. For example, if the flavor of cluster's master node does not support the multi-AZ feature, <span class="uicontrol" id="uicontrol11801424193411"><a name="uicontrol11801424193411"></a><a name="uicontrol11801424193411"></a><b>Master AZs</b></span> will not be displayed.</p>
    <p id="p11404840532"><a name="p11404840532"></a><a name="p11404840532"></a>The following parameters are supported:</p>
    <p id="p8379453144314"><a name="p8379453144314"></a><a name="p8379453144314"></a><strong id="b4380253124316"><a name="b4380253124316"></a><a name="b4380253124316"></a>CPU Policy</strong></p>
    <p id="p43801653134312"><a name="p43801653134312"></a><a name="p43801653134312"></a>This parameter is displayed only for clusters of v1.13.10-r0 and later.</p>
    <a name="ul2038045318436"></a><a name="ul2038045318436"></a><ul id="ul2038045318436"><li><strong id="b19380175318437"><a name="b19380175318437"></a><a name="b19380175318437"></a>On</strong>: Exclusive CPU cores can be allocated to workload pods. Select <strong id="b53801553114312"><a name="b53801553114312"></a><a name="b53801553114312"></a>On</strong> if your workload is sensitive to latency in CPU cache and scheduling.</li><li><strong id="b43801853154317"><a name="b43801853154317"></a><a name="b43801853154317"></a>Off</strong>: Exclusive CPU cores will not be allocated to workload pods. Select <strong id="b183809535438"><a name="b183809535438"></a><a name="b183809535438"></a>Off</strong> if you want a large pool of shareable CPU cores.</li></ul>
    <p id="p3380195324317"><a name="p3380195324317"></a><a name="p3380195324317"></a>For details about CPU management policies, see <a href="https://kubernetes.io/blog/2018/07/24/feature-highlight-cpu-manager/" target="_blank" rel="noopener noreferrer">Feature Highlight: CPU Manager</a>.</p>
    <p id="p1481635155312"><a name="p1481635155312"></a><a name="p1481635155312"></a><strong id="b1683001355312"><a name="b1683001355312"></a><a name="b1683001355312"></a>Open EIP</strong></p>
    <p id="p185657255535"><a name="p185657255535"></a><a name="p185657255535"></a>A public IP address that is reachable from public networks. Select an EIP that has not been bound to any node. A cluster's EIP is preset in the cluster's certificate. Do no delete the EIP after the cluster has been created. Otherwise, two-way authentication will fail.</p>
    <a name="ul5565192510530"></a><a name="ul5565192510530"></a><ul id="ul5565192510530"><li><strong id="b056682519533"><a name="b056682519533"></a><a name="b056682519533"></a>Do not configure</strong>: The cluster's master node will not have an EIP.</li><li><strong id="b1656613257533"><a name="b1656613257533"></a><a name="b1656613257533"></a>Configure now</strong>: If no EIP is available for selection, create a new EIP.</li></ul>
    <p id="p633643879"><a name="p633643879"></a><a name="p633643879"></a><strong id="b13315431477"><a name="b13315431477"></a><a name="b13315431477"></a>Master AZs</strong></p>
    <p id="p333174317718"><a name="p333174317718"></a><a name="p333174317718"></a>The multi-AZ deployment of master nodes achieves disaster tolerance on the cluster management plane at a certain sacrifice of cluster performance.</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click  **Next: Confirm**.
4.  Confirm the specifications, and click  **Submit**.

    It takes about 6 to 10 minutes to create a cluster. You can click  **Back to Cluster List**  to perform other operations on the cluster or click  **Go to Cluster Events**  to view the cluster details.


