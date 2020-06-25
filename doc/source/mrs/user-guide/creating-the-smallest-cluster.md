# Creating the Smallest Cluster<a name="EN-US_TOPIC_0127245533"></a>

MRS 1.7.2 and later versions allow you to create the smallest cluster with only one Master node and one Core node. This helps you reduce costs in lightweight use scenarios, for example, development and commissioning of enterprise big data services.

Perform the following steps to create the smallest cluster.

1.  Log in to the MRS management console.
2.  Click  **Create Cluster** in the upper-right corner. The **Create Cluster**  page is displayed.

    The detailed cluster configurations are as follows:

    -   **Region**: Use the default value, for example, eu-de.
    -   **AZ**: Select eu-de-01 or eu-de-02.
    -   **Cluster Name**: You can use the default name. However, you are recommended to include a project name abbreviation or date for consolidated memory and easy distinguishing, for example, **mrs\_20180321**.
    -   **Cluster Version**: Use the default value.
    -   **Kerberos Authentication**: It is enabled by default, as shown in ![](figures/dt_enable.png).
    -   **Username**: Indicates the username for the administrator of MRS Manager.  **admin**  is used by default.
    -   **Password**: Indicates the password of the MRS Manager administrator.
    -   **Cluster Type**: Use the default value **Analysis cluster**.
    -   **Component**: Select Spark, HBase, Hive, and other components for an analysis cluster. Select Kafka, Storm, and other components for a streaming cluster.
    -   **VPC**: Use the default value. If there is no available VPC, click **View VPC** to access the **Virtual Private Cloud**  console and create a new VPC.
    -   **Subnet**: Use the default value.
    -   **Security Group**: Select  **Auto create**.
    -   **EIP**: Select  **Bind later**.
    -   **Cluster HA**: Click ![](figures/dt_enable.png)  to disable cluster HA.
    -   **Instance Specifications**: Select  ****4 vCPUs 16 GB\(c3.xlarge.4\)****  under  **General computing-plus C3**  for both Master and Core nodes.
    -   **Instance Count**: The number of Master nodes is fixed to 1. Set the number of Core nodes to 1.
    -   **Storage Type**: Select **Common I/O**  for both Master and Core nodes.
    -   **Storage Space \(GB\)**: Set **Storage Space**  to 100 GB for both Master and Core nodes.
    -   **Data Disk**: Use the default value. There is one Master node and one Core node by default.
    -   ****Configure**  Task Node**: Do not add a Task node.
    -   **Key Pair**: Select a key pair form the drop-down list. Select "I acknowledge that I have obtained private key file **SSHkey-bba1.pem**  and that without this file I will not be able to log in to my ECS." If you have never created a key pair, click **View Key Pair**  to create or import a key pair. And then, obtain a private key file.
    -   **Advanced Settings**: Select **Configure**.

        >![](/images/icon-note.gif) **NOTE:**   
        >MRS streaming clusters do not support job management and file management functions. When you create a streaming cluster, the  **Add Job**  area will not be displayed on the page.  


3.  After parameter configuration is complete, click  ****Next****  in the lower right corner.
4.  After confirming cluster details, click  **Submit**  to submit a cluster creation task.
5.  Click  **Back to Cluster List**  to view the cluster status.

    Cluster creation takes some time. The initial status of the cluster is  **Starting**. After the cluster is created successfully, the cluster status becomes **Running**.


