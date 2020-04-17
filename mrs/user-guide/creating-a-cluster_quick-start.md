# Creating a Cluster<a name="EN-US_TOPIC_0125375368"></a>

This section describes how to create a cluster using MRS.

## Procedure<a name="sbf7c49869f2346b49e6253f2e5683090"></a>

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)in the upper-left corner on the management console and select **Region** and **Project**.
3.  Click  **Create Cluster** and open the **Create Cluster**  page.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Note the usage of quotas when you create a cluster. If the resource quotas are insufficient, apply for new quotas based on the prompted information and create new clusters.  

    The following is a cluster configuration example:

    -   **AZ**: Use the default value. If a cluster already exists in the region, you are advised to use a different region to create a cluster.
    -   **Cluster Name**: This parameter can be set to the default system name. For the ease of distinguishing and memorizing, it is recommended that the cluster name be set to a value consisting of the employee ID, short spelling of the user's name, or the date. For example: **mrs\_20160907**
    -   **Cluster Version**: Use the default value MRS 1.7.2. The latest version of MRS is used by default. Currently, the latest version is MRS 1.7.2.
    -   **Kerberos Authentication**: The default value is  ****Enable****: ![](figures/dt_enable.png).
    -   **Username**: Indicates the username for the administrator of MRS Manager.  **admin**  is used by default.
    -   **Password**: Indicates the password of the MRS Manager administrator.
    -   **Cluster Type**: Use the default value **Analysis cluster** or select **Streaming cluster**.
    -   **Component**: For an analysis cluster, select components Spark, HBase, Hive, and so on. For a streaming cluster, select components Kafka, Storm, and so on.
    -   **VPC**: Use the default value. If no virtual private cloud \(VPC\) exists, click **View VPC**  to enter VPC, and create a VPC.
    -   **Subnet**: Use the default value. If no subnet is created in the VPC, click **Create Subnet**  to create a subnet in the corresponding VPC.
    -   **Security Group**: Select  **Auto Create**.
    -   **EIP**: Select  **Bind later**.
    -   **Cluster HA**: Cluster HA is enabled by default.
    -   **Instance Specifications**: Select **4 vCPUs 16 GB |  ****c3.xlarge.4******  for both the Master and Core nodes.
    -   **Quantity**: Retain the default number **2** for the Master nodes and set the number of Core nodes to **3**.
    -   **Storage Type**: Select **Common I/O**.
    -   **Storage Space \(GB\)**: Use the default value.
    -   **Data Disk**: Use the default value.
    -   **Login Mode**: Select a mode to log in to an ECS node.
        -   **Password**: Set a password for logging in to an ECS node.
        -   **Key Pair**: Select a key pair form the drop-down list. Select "I acknowledge that I have obtained private key file **SSHkey-bba1.pem**  and that without this file I will not be able to log in to my ECS." If you have never created a key pair, click **View Key Pair**  to create or import a key pair. And then, obtain a private key file.

    -   **Logging**: Select "**Disable**": ![](figures/icon_mrs_disable_dt.png). The default value is "**Enable**": ![](figures/dt_enable.png).
    -   **Advanced Settings**: Select **Skip**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >MRS streaming clusters do not support  **Jobs** or **Files**. If the cluster type is **Streaming Cluster**, the **Create Job**  area is not displayed on the cluster creation page.  


4.  Click  **Create now**.
5.  Confirm cluster specifications and click  **Submit**  to submit a cluster creation task.
6.  Click  **Back to Cluster List**  to view the cluster status.

    The cluster creation takes a while. The initial state of the cluster created is  **Starting**. After the cluster is created successfully, the status will be updated to **Running**. Please be patient.


