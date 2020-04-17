# Expanding a Cluster<a name="EN-US_TOPIC_0125375987"></a>

The storage and computing capabilities of MRS can be improved by simply adding Core nodes or Task nodes instead of modifying system architecture, reducing O&M costs. Core nodes can process and store data. You can add Core nodes to increase the number of nodes that process the peak load. Task nodes are used for computing and do not store persistent data.

## Background<a name="section19165099103254"></a>

An MRS cluster supports a maximum of 502 nodes. A cluster has one or two Master nodes by default and must have at least one Core node. A maximum of 500 Core nodes and Task nodes are supported by default. If more than 500 Core nodes and Task nodes are required, contact technical support engineers or invoke a background interface to modify the database.

Core nodes and Task nodes can be added but Master nodes cannot. The maximum number of nodes that can be added equals to 500 minus the number of existing Core nodes or Task nodes. For example, if the number of existing Core nodes is 3, a maximum of 497 nodes can be added. If a cluster fails to be expanded, you can perform capacity expansion for the cluster again.

If no node is added during cluster creation, you can specify the number of nodes to be added during capacity expansion. However, you cannot specify the nodes to be added.

Cluster capacity expansion operations vary according to the cluster version you select.

## Procedure<a name="section6382765316417"></a>

If the cluster version is MRS 1.6.3 or later, perform the following operations:

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)in the upper-left corner on the management console and select **Region** and **Project**.
3.  Choose  **Clusters \> Active Clusters**, select a running cluster, and click its name to switch to the cluster details page.
4.  Click  **Resize Cluster** and go to the **Resize Cluster**  page.

    The expansion operation can only be performed on the running clusters.

5.  Set  **Node Type** to **Core Node** or **Task Node**, configure the **Nodes After Resize** parameter, and click **OK**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If there is no  **Task Node** in the **Node Type** drop-down list, follow instructions in [Related Operations](#section60245328163721)  to configure the Task node type.  
    >-   If you enable  **Run Bootstrap Action**, the bootstrap action script you add during cluster creation will be executed on all added nodes. Only MRS 1.7.2 or later supports bootstrap actions.  
    >-   If the  **New Specifications**  parameter is available, the specifications that are the same as those of the original nodes have been sold out or discontinued. Nodes with new specifications will be added.  

6.  In the  **Resize Cluster** window, click **OK**.
7.  In the  **Expand Node**  dialog box, click  **OK**.

    Cluster expansion is explained as follows:

    -   During expansion: The cluster status is  **Expanding**. The submitted jobs will be executed and you can submit new jobs. You are not allowed to continue to expand, restart, modify, or terminate the cluster.
    -   Successful expansion: The cluster status is  **Running**. The resources used in the old and new nodes are charged.
    -   Failed expansion: The cluster status is  **Running**. You are allowed to execute jobs and expand the cluster again.

    After the cluster expansion is successful, you can view node information on the cluster details page.


## Related Operations<a name="section60245328163721"></a>

Perform the following operations to configure Task nodes:

1.  On the cluster details page, choose  **Nodes**  tab and click  **Configure Task Node**.
2.  On the  **Configure Task Node** page, configure  **Instance Specifications** and **Nodes**. In addition, if **Add Data Disk** is enabled, configure the storage type, size, and number of data disks.
3.  Click  **OK**.

