# Creating a Node<a name="cce_01_0033"></a>

A  node  is a virtual or physical machine that provides computing resources. Sufficient nodes must be available in your project to ensure that operations, such as creating workloads, can be performed.

## Prerequisites<a name="section103205496263"></a>

-   At least one cluster is available. For details on how to create a cluster, see  [Creating a Hybrid Cluster](creating-a-hybrid-cluster.md).
-   A key pair has been created. The key pair will be used for identity authentication upon remote node login. For details, see  [Creating a Key Pair](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0014250631.html).

## Precautions for Using a Node<a name="section115398290518"></a>

Some of the resources on the node need to run some necessary Kubernetes system components and resources to make the node as part of your cluster. Therefore, the total number of node resources and the number of assignable node resources in Kubernetes are different. The larger the node specifications, the more the containers deployed on the node. Therefore, Kubernetes needs to reserve more resources.

To ensure node stability, CCE cluster nodes reserve some resources for Kubernetes components \(such as kubelet, kube-proxy, and docker\) based on node specifications.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You are advised not to install software or modify the operating system \(OS\) configuration on a cluster node. This may cause exceptions on Kubernetes components installed on the node, and make the node unavailable.  

## Creating a Node<a name="section19320144922620"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Clusters**. Click  **Create Node**.
2.  Select a region and an AZ.
    -   **Current Region**: geographic location of the nodes to be created.
    -   **AZ**: Set this parameter based on the site requirements. An AZ is a physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through an internal network.

        To enhance workload availability, create nodes in different AZs.

3.  Configure the node specifications and quantity.
    -   **Node Type**

        **VM node**: A VM node will be created in the cluster.

    -   **Node Name**: Enter a node name.
    -   **DeH**: A Dedicated Host \(DeH\) is a physical server dedicated for your use. You can create nodes on a DeH to physically isolate the nodes from those of other tenants.

        You can select a DeH from the drop-down list box to create a node. If DeH is not required, you can skip the configuration of this parameter.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >This parameter is available only when DeHs exist.  

    -   **Specifications**: Select node specifications that best fit your business needs.

        -   **General-purpose**: provides general computing, storage, and network configurations that can meet a majority of scenarios. General-purpose nodes can be used for web servers, workload development, workload testing, and small databases.
        -   **Memory-optimized**: provides higher memory capacity than general-purpose nodes and is suitable for relational databases, NoSQL, and other workloads that are both memory-intensive and data-intensive.
        -   **GPU-accelerated**: provides powerful floating-point computing and is suitable for real-time, highly concurrent massive computing. Graphical processing units \(GPUs\) of P series are suitable for deep learning, scientific computing, and CAE. GPUs of G series are suitable for 3D animation rendering and CAD. Currently, only clusters of v1.11 support GPU-accelerated nodes. If the cluster version is v1.13 or later,  **GPU-accelerated**  is not displayed on the page.
        -   **General computing-plus**: provides stable performance and exclusive resources to enterprise-level workloads with high and stable computing performance.

        To ensure node stability, the system automatically reserves some resources for running necessary system components. For details, see the  [formula for calculating reserved node resources](formula-for-calculating-the-reserved-resources-of-a-node.md).

    -   **OS**: Select the operating system \(OS\) of the nodes to be created. For details, see  [OS Patch Notes for Cluster Nodes](os-patch-notes-for-cluster-nodes.md).
    -   **VPC**: This parameter is displayed only for clusters of v1.13.10-r0 and later.
    -   **Subnet**: A subnet improves network security by providing exclusive network resources that are isolated from other networks. You can select any subnet in the cluster VPC. Cluster nodes can belong to different subnets. This parameter is displayed only for clusters of v1.13.10-r0 and later.

4.  **System Disk**  and  **Data Disk**: Set the disk space of the nodes.

    -   The system disk capacity ranges from 40 GB to 1,024 GB.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >When accepting a node into a cluster of v1.15, ensure that the system disk of the node has a capacity larger than 50 GB.  

    -   The data disk capacity is configurable and ranges from 100 to 32678 GB.

    System disks and data disks deliver three levels of I/O performance:

    -   **Common I/O**: uses Serial Advanced Technology Attachment \(SATA\) drives to store data. EVS disks of this level provide reliable block storage and a maximum IOPS of 1,000 per disk. They are suitable for key applications.
    -   **High I/O**: uses serial attached SCSI \(SAS\) drives to store data. EVS disks of this level provide a maximum IOPS of 3,000 and a minimum read/write latency of 1 ms. They are suitable for Relational Database Service \(RDS\), NoSQL, data warehouse, and file system applications.
    -   **Ultra-high I/O**: uses solid state disk \(SSD\) drives to store data. EVS disks of this level provide a maximum IOPS of 20,000 and a minimum read/write latency of 1 ms. They are suitable for RDS, NoSQL, and data warehouse applications.

5.  **EIP**: An independent public IP address. If the nodes to be created require Internet access, select  **Automatically assign**  or  **Use existing**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >By default, VPC's SNAT feature is disabled for CCE. If SNAT is enabled, you do not need to use EIPs to access external networks.  

    -   **Do not use**: A node without an EIP cannot access the Internet. It can be used only as a cloud server for deploying services or clusters on a private network.
    -   **Automatically assign**: An EIP with specified configurations is automatically assigned to each node. If the number of EIPs is less than the number of nodes, the EIPs are randomly bound to the nodes.

        Set the specifications, required quantity, billing mode, and bandwidth as required. When creating an ECS, ensure that the elastic IP address quota is sufficient.

    -   **Use existing**: Existing EIPs are assigned to the nodes to be created.

6.  If the login mode is  **Key pair**, select a key pair for logging to the node.

    A key pair is used for identity authentication when you remotely log in to a node. If no key pair is available, click  **Create a key pair**. For details on how to create a key pair, see  [Creating a Key Pair](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0014250631.html).

7.  **Advanced ECS Settings**  \(optional\): Click  ![](figures/icon-monitoring-0.png)  to show advanced ECS settings.
    -   **ECS Group**: Select an existing ECS group, or click  **Create ECS Group**  to create a new one. After the ECS group is created, click the refresh icon.

        An ECS group allows you to create ECSs on different hosts, thereby improving service reliability.

    -   **Resource Tags**: Resource tags can be added to classify resources.

        You can create predefined tags in Tag Management Service \(TMS\). Predefined tags are visible to all service resources that support the tagging function. You can use predefined tags to improve tag creation and migration efficiency. For details, see  [Creating Predefined Tags](https://docs.otc.t-systems.com/en-us/usermanual/tms/en-us_topic_0144368884.html).

        CCE will automatically create the "CCE-Dynamic-Provisioning-Node=node id" tag. A maximum of 20 tags can be added.

    -   **Agency Name**: An agency is created by the account administrator on the IAM console. By creating an agency, you can share your cloud server resources with another account, or entrust a more professional person or team to manage your resources. To authorize ECS or BMS to call cloud services, select  **Cloud service**  as the agency type, click  **Select**, and then select  **ECS BMS**.
    -   **Pre-installation Script**: Enter a maximum of 1,000 characters.

        The script will be executed before Kubernetes software is installed. Note that if the script is incorrect, Kubernetes software may not be installed successfully. The script is usually used to format data disks.

    -   **Post-installation Script**: Enter a maximum of 1,000 characters.

        The script will be executed after Kubernetes software is installed and will not affect the installation. The script is usually used to modify Docker parameters.

    -   **Add Data Disk**: Click  **Add Data Disk**  to add a data disk and set the capacity of the data disk. To simplify disk formatting, you can enter the disk formatting command in the input box of  **Pre-installation Script**. For details, see  [How Do I Add a Second Data Disk to a Node in a CCE Cluster?](how-do-i-add-a-second-data-disk-to-a-node-in-a-cce-cluster.md).
    -   **Subnet IP Address**: Select  **Automatically assign IP address**  \(recommended\) or  **Manually assigning IP addresses**.

8.  **Advanced Kubernetes Settings**  \(optional\): Click  ![](figures/icon-monitoring-0.png)  to show advanced Kubernetes settings.
    -   **Max Pods**: The maximum number of pods that can be created on a node, including the system's default pods. Value range: 16 to 250.

        This maximum limit prevents the node from being overloaded by managing too many pods.

    -   **insecure-registries**: Click  **Add insecure-registry**  and enter the address of the image repository.

        Add the address of the custom image repository with no valid SSL certificate to the docker startup option to avoid unsuccessful image pulling from the personal image repository. The address is in the format of IP address:Port number \(or domain name\). Post-installation script and insecure-registries cannot be used together.

    -   **Maximum Data Space per Container**: The value ranges from 10 GB to 80 GB. If the value of this field is larger than the data disk space allocated to Docker, the latter will override the value specified here. Typically, 90% of the data disk space is allocated to Docker. This parameter is supported only in v1.13.10-r0 and later versions of clusters. It is not displayed in versions earlier than v1.13.10-r0.

9.  Click  **Next: Confirm**, confirm the information, and click  **Submit**. It takes 6 to 10 minutes to create a node.
10. Click  **Back to Node List**. The node has been created successfully if it is in the Available state.

