# Creating a Node Pool<a name="cce_01_0012"></a>

This section describes how to create a node pool for a running CCE cluster and how to perform operations on the node pool. For details about how a node pool works, see  [Node Pool Overview](node-pool-overview.md).

## Procedure<a name="section138731847143716"></a>

To create a node pool in a cluster, perform the following steps:

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Node Pool**.
2.  In the upper right corner of the page, click  **Create Node Pool**.
3.  On the  **Create Node Pool**  page, configure node pool parameters \(see  [Table 1](#table8638121213265)\). Parameters with an asterisk \(\*\) are mandatory.

    **Table  1**  Parameters for creating a node pool

    <a name="table8638121213265"></a>
    <table><thead align="left"><tr id="row10638181262612"><th class="cellrowborder" valign="top" width="20.02%" id="mcps1.2.3.1.1"><p id="p1063821214265"><a name="p1063821214265"></a><a name="p1063821214265"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="79.97999999999999%" id="mcps1.2.3.1.2"><p id="p1638181232617"><a name="p1638181232617"></a><a name="p1638181232617"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42961494311"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p812874116011"><a name="p812874116011"></a><a name="p812874116011"></a>* Current Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p92761950965"><a name="p92761950965"></a><a name="p92761950965"></a>Geographical region where the node pool will be located.</p>
    <p id="p161283411302"><a name="p161283411302"></a><a name="p161283411302"></a>To minimize network latency and resource access time, select the nearest region. Cloud resources are region-specific and cannot be used across regions through internal network connections.</p>
    </td>
    </tr>
    <tr id="row1063812126263"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p15639812122620"><a name="p15639812122620"></a><a name="p15639812122620"></a>* Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p26391512172614"><a name="p26391512172614"></a><a name="p26391512172614"></a>Name of the new node pool. By default, the name is in the format of <em id="i2010433352011"><a name="i2010433352011"></a><a name="i2010433352011"></a>cluster name</em>-nodepool-<em id="i105021037192011"><a name="i105021037192011"></a><a name="i105021037192011"></a>random number</em>. If you do not want to use the default name format, you can customize the name.</p>
    </td>
    </tr>
    <tr id="row6649879161231"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p1769363161231"><a name="p1769363161231"></a><a name="p1769363161231"></a>* Node Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p9100682161231"><a name="p9100682161231"></a><a name="p9100682161231"></a>Currently, only VM nodes are supported.</p>
    </td>
    </tr>
    <tr id="row572593234714"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p14725432104718"><a name="p14725432104718"></a><a name="p14725432104718"></a>* Nodes</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p102308301014"><a name="p102308301014"></a><a name="p102308301014"></a>The specified number of nodes in a node pool cannot exceed the maximum number of nodes that can be managed by the cluster.</p>
    </td>
    </tr>
    <tr id="row1763991215268"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p15639181282617"><a name="p15639181282617"></a><a name="p15639181282617"></a>Autoscaler</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p20736112217461"><a name="p20736112217461"></a><a name="p20736112217461"></a>By default, autoscaler is disabled.</p>
    <p id="p1063941211266"><a name="p1063941211266"></a><a name="p1063941211266"></a>After you click <a name="en-us_topic_0107283640_image17351426631"></a><a name="en-us_topic_0107283640_image17351426631"></a><span><img id="en-us_topic_0107283640_image17351426631" src="figures/icon-autoscalerenable.png"></span> to enable autoscaler, nodes in the node pool will be automatically created or deleted to match the changeable cluster load. You can set <strong id="b83671426202514"><a name="b83671426202514"></a><a name="b83671426202514"></a>Maximum Nodes</strong> and <strong id="b1082992932515"><a name="b1082992932515"></a><a name="b1082992932515"></a>Minimum Nodes</strong> to ensure that the number of nodes will always fall within a specified range.</p>
    <p id="p12614171015488"><a name="p12614171015488"></a><a name="p12614171015488"></a>If the <strong id="b139093213282"><a name="b139093213282"></a><a name="b139093213282"></a>Autoscaler</strong> field is set to on, install the <a href="autoscaler.md">autoscaler add-on</a> to use the autoscaler feature.</p>
    </td>
    </tr>
    <tr id="row75241899266"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p11786989141"><a name="p11786989141"></a><a name="p11786989141"></a>* AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p10360153524719"><a name="p10360153524719"></a><a name="p10360153524719"></a>An AZ is a physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through an internal network.</p>
    <p id="p111211029184020"><a name="p111211029184020"></a><a name="p111211029184020"></a>Set an AZ based on your requirements. To enhance workload reliability, you are advised to select <strong id="b71591621113113"><a name="b71591621113113"></a><a name="b71591621113113"></a>randomAZ</strong>, allowing nodes to be randomly and evenly distributed among different AZs.</p>
    </td>
    </tr>
    <tr id="row15639412132615"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p36391812172618"><a name="p36391812172618"></a><a name="p36391812172618"></a>* Specifications</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p16639712132616"><a name="p16639712132616"></a><a name="p16639712132616"></a>Select node specifications that best fit your business needs.</p>
    <a name="ul2581647145016"></a><a name="ul2581647145016"></a><ul id="ul2581647145016"><li><strong id="b84381459326"><a name="b84381459326"></a><a name="b84381459326"></a>General-purpose</strong>: provides general computing, storage, and network configurations that can meet a majority of scenarios. General-purpose nodes can be used for web servers, workload development, workload testing, and small databases.</li><li><strong id="b0853353123213"><a name="b0853353123213"></a><a name="b0853353123213"></a>Memory-optimized</strong>: provides higher memory capacity than general-purpose nodes and is suitable for relational databases, NoSQL, and other workloads that are both memory-intensive and data-intensive.</li><li><strong id="b6795175616321"><a name="b6795175616321"></a><a name="b6795175616321"></a>GPU-accelerated</strong>: provides powerful floating-point computing and is suitable for real-time, highly concurrent massive computing. Graphical processing units (GPUs) of P series are suitable for deep learning, scientific computing, and CAE. GPUs of G series are suitable for 3D animation rendering and CAD. Currently, only clusters of v1.11 support GPU-accelerated nodes. If the cluster version is v1.13 or later, <strong id="b73914477914"><a name="b73914477914"></a><a name="b73914477914"></a>GPU-accelerated</strong> is not displayed on the page.</li><li><strong id="b1499814150333"><a name="b1499814150333"></a><a name="b1499814150333"></a>General computing-plus</strong>: provides stable performance and exclusive resources to enterprise-level workloads with high and stable computing performance.</li></ul>
    <div class="notice" id="note1654116192613"><a name="note1654116192613"></a><a name="note1654116192613"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p165419642614"><a name="p165419642614"></a><a name="p165419642614"></a>To ensure node stability, the system automatically reserves some resources for running necessary system components. For details, see the <a href="formula-for-calculating-the-reserved-resources-of-a-node.md">formula for calculating reserved node resources</a>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row482955911270"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p9831659192715"><a name="p9831659192715"></a><a name="p9831659192715"></a>* OS</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="li820018141678p0"><a name="li820018141678p0"></a><a name="li820018141678p0"></a>Select an operating system for the node pool. For details, see <a href="os-patch-notes-for-cluster-nodes.md">OS Patch Notes for Cluster Nodes</a>.</p>
    </td>
    </tr>
    <tr id="row2747182915539"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p1874712911531"><a name="p1874712911531"></a><a name="p1874712911531"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p31701028104512"><a name="p31701028104512"></a><a name="p31701028104512"></a>The node pool inherits VPC settings from the cluster to which it belongs.</p>
    <p id="p77481829105313"><a name="p77481829105313"></a><a name="p77481829105313"></a><strong id="b1864310378357"><a name="b1864310378357"></a><a name="b1864310378357"></a>This parameter is displayed only for clusters of v1.13.10-r0 and later.</strong></p>
    </td>
    </tr>
    <tr id="row5182152385316"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p16183192315530"><a name="p16183192315530"></a><a name="p16183192315530"></a>* Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p71844236539"><a name="p71844236539"></a><a name="p71844236539"></a>A subnet improves network security by providing exclusive network resources that are isolated from other networks.</p>
    <p id="p41239614562"><a name="p41239614562"></a><a name="p41239614562"></a>You can select any subnet in the cluster VPC. Cluster nodes can belong to different subnets.</p>
    <p id="p1986144116558"><a name="p1986144116558"></a><a name="p1986144116558"></a><strong id="b154981447133516"><a name="b154981447133516"></a><a name="b154981447133516"></a>This parameter is displayed only for clusters of v1.13.10-r0 and later.</strong></p>
    </td>
    </tr>
    <tr id="row13689105720916"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p16902571497"><a name="p16902571497"></a><a name="p16902571497"></a>* System Disk and Data Disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p11859211151015"><a name="p11859211151015"></a><a name="p11859211151015"></a>Configure the disk space of each node in the node pool.</p>
    <p id="p168599112103"><a name="p168599112103"></a><a name="p168599112103"></a>The system disk capacity ranges from 40 to 1,024 GB. The default value is 40 GB.</p>
    <p id="p1485931114104"><a name="p1485931114104"></a><a name="p1485931114104"></a>The data disk capacity ranges from 100 to 32,678 GB. The default value is 100 GB.</p>
    <div class="p" id="p155112561112"><a name="p155112561112"></a><a name="p155112561112"></a>System disks and data disks are EVS disks and deliver three levels of I/O performance:<a name="ul17511135201117"></a><a name="ul17511135201117"></a><ul id="ul17511135201117"><li><strong id="b651220571120"><a name="b651220571120"></a><a name="b651220571120"></a>Common I/O</strong>: uses SATA drives to store data. EVS disks of this level provide reliable block storage and a maximum IOPS of 1,000 per disk. They are suitable for key applications.</li><li><strong id="b35126571111"><a name="b35126571111"></a><a name="b35126571111"></a>High I/O</strong>: uses SAS drives to store data. EVS disks of this level provide a maximum IOPS of 3,000 and a minimum read/write latency of 1 ms. They are suitable for RDS, NoSQL, data warehouse, and file system applications.</li><li><strong id="b251210531111"><a name="b251210531111"></a><a name="b251210531111"></a>Ultra-high I/O</strong>: uses SSD drives to store data. EVS disks of this level provide a maximum IOPS of 20,000 and a minimum read/write latency of 1 ms. They are suitable for RDS, NoSQL, and data warehouse applications.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row148911429552"><td class="cellrowborder" valign="top" width="20.02%" headers="mcps1.2.3.1.1 "><p id="p089262135520"><a name="p089262135520"></a><a name="p089262135520"></a>* Key Pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p789211215513"><a name="p789211215513"></a><a name="p789211215513"></a>A key pair is used for identity authentication when you remotely log in to a node. If no key pair is available, click <strong id="b85742523417"><a name="b85742523417"></a><a name="b85742523417"></a>Create a key pair</strong> and create one. For details on how to create a key pair, see <a href="https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0014250631.html" target="_blank" rel="noopener noreferrer">Creating a Key Pair</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  **Advanced ECS Settings**  \(optional\): Click  ![](figures/icon-monitoring.png)  to show advanced ECS settings.
    -   **ECS Group**: Select an existing ECS group, or click  **Create ECS Group**  to create a new one. After the ECS group is created, click the refresh icon.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >An ECS group allows you to create ECSs on different hosts, thereby improving service reliability.  

    -   **Resource Tags**: Resource tags can be added to classify resources.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   You can create predefined tags in Tag Management Service \(TMS\). Predefined tags are visible to all service resources that support the tagging function. You can use predefined tags to improve tag creation and migration efficiency. For details, see  [Creating Predefined Tags](https://docs.otc.t-systems.com/en-us/usermanual/tms/en-us_topic_0144368884.html).  
        >-   CCE will automatically create the "CCE-Dynamic-Provisioning-Node=_node id_" tag.  
        >-   A maximum of 20 tags can be added.  

    -   **Agency** **Name**: An agency is created by a tenant administrator on the IAM console. By creating an agency, you can share your cloud server resources with another account, or entrust a more professional person or team to manage your resources. . To authorize ECS or BMS to call cloud services, select  **Cloud service**  as the agency type, click  **Select**, and then select  **ECS BMS**.
    -   <a name="li484421635920"></a>**Pre-installation Script**: Enter the installation script.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   The script will be executed before Kubernetes software is installed. Note that if the script is incorrect, Kubernetes software may not be installed successfully. The script is usually used to format data disks.  
        >-   Enter a maximum of 1,000 characters.  
        >-   The script is written into nodes through  **command line insertion**. For details about the example scripts, see  [How Do I Format a Data Disk Using Command Line Injection?](how-do-i-format-a-data-disk-using-command-line-injection.md). For details on how to inject data, see  [Creating a VPC](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0032380449.html).  

    -   **Post-installation Script**: Enter the installation script.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   The script will be executed after Kubernetes software is installed and will not affect the installation. The script is usually used to modify Docker parameters.  
        >-   Enter a maximum of 1,000 characters.  
        >-   The script is written into nodes through  **command line insertion**. For details about example scripts and how to inject data, see  [Pre-installation Script](#li484421635920).  

    -   **Add Data Disk**: Click  **Add Data Disk**  to add a data disk and set the capacity of the data disk. To simplify disk formatting, you can enter the disk formatting command in the input box of  [Pre-installation Script](#li484421635920).

5.  **Advanced Kubernetes Settings**  \(optional\): Click  ![](figures/icon-ecssettings.png)  to show advanced Kubernetes settings.
    -   **Max Pods**: The maximum number of pods that can be created on a node, including the system's default pods. Value range: 16 to 250.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >This maximum limit prevents the node from being overloaded by managing too many pods.  

    -   **insecure-registries**: Click  **Add insecure-registry**  and enter the address of the image repository.

        Add the address of the custom image repository with no valid SSL certificate to the docker startup option to avoid unsuccessful image pulling from the personal image repository. The address is in the format of IP address:Port number \(or domain name\). Post-installation script and insecure-registries cannot be used together.

    -   **Taints**: This field is left blank by default. Taints allow nodes to repel a set of pods. You can add a maximum of 10 taints for each node pool. Each taint contains the following parameters:

        -   **Key**: A key must contain 1 to 63 characters starting with a letter or digit. Only letters, digits, hyphens \(-\), underscores \(\_\), and periods \(.\) are allowed. A DNS subdomain name can be used as the prefix of a key.
        -   **Value**: A value must start with a letter or digit and can contain a maximum of 63 characters, including letters, digits, hyphens \(-\), underscores \(\_\), and periods \(.\).
        -   **Effect**: Available options are  **NoSchedule**,  **PreferNoSchedule**, and  **NoExecute**.

        >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
        >-   If taints are used, you must configure tolerations in the YAML files of pods. Otherwise, scale-up may fail or pods cannot be scheduled onto the added nodes.  
        >-   Taints cannot be modified after configuration. Incorrect taints may cause a scale-up failure or prevent pods from being scheduled onto the added nodes.  

    -   **K8S Labels**: Labels are key/value pairs that are attached to objects, such as pods. Labels are intended to be used to specify identifying attributes of objects that are meaningful and relevant to users, but do not directly imply semantics to the core system. For more information, see  [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).
    -   **Maximum Data Space per Container**: The value ranges from 10 GB to 80 GB. If the value of this field is larger than the data disk space allocated to Docker, the latter will override the value specified here. Typically, 90% of the data disk space is allocated to Docker. This parameter is supported only in v1.13.10-r0 and later versions of clusters. It is not displayed in versions earlier than v1.13.10-r0.

6.  After the configuration is complete, click  **Next**. Confirm the node pool configuration and click  **Create Now**.

    It takes about 6 to 10 minutes to create a node pool. You can click  **Back to Node Pool List**  to perform other operations on the node pool.


## Viewing Node Pools in a Cluster<a name="section1147314023811"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Node Pool**.
2.  In the upper right corner of the node pool list, select a cluster. All node pools in the cluster will be displayed. You can view the node type, node specifications, autoscaler status, and OS of each node pool.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   A default node pool  **DefaultPool**  is automatically created in each cluster. The default node pool cannot be edited, deleted, or migrated. All nodes created during and after cluster creation are displayed in the default node pool.  
    >-   To display a list of nodes in  **DefaultPool**, click the  **nodes**  subcard in the  **DefaultPool**  card.  

3.  To filter node pools by autoscaler status, select the autoscaler status in the upper right corner of the node pool list.
4.  In the node pool list, click a node pool name. On the node pool details page, view the basic information, advanced ECS settings, advanced Kubernetes settings, and node list of the node pool.

