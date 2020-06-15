# Creating an Instance<a name="EN-US_TOPIC_0143117108"></a>

## Scenario<a name="section66578044"></a>

DMS provides Kafka premium instances. Each instance uses dedicated resources and is not affected by other instances. You can customize the computing capabilities and storage space of a Kafka instance based on service requirements.

[Comparing Kafka Queues and Kafka Premium Instances](comparing-kafka-queues-and-kafka-premium-instances.md)  lists the differences between Kafka premium instances and Kafka queues.

## Prerequisites<a name="section62331491"></a>

A VPC configured with security groups and subnets is available.

## Procedure<a name="section1474721314405"></a>

1.  Log in to the management console.
2.  Choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
3.  In the navigation pane, choose  **Kafka Premium**.
4.  Click  **Create Kafka Instance**  in the upper right corner of the page.

    By default, you can create a maximum of 100 Kafka instances for each project. To create more instances, contact customer service to increase your quota.

5.  Select a region closest to your application to reduce latency and accelerate access.
6.  Select an AZ.
7.  Specify  **Instance Name**  and  **Description**.
8.  Configure the following instance parameters.
    1.  **Version**: Kafka version. Currently, only 2.3.1 is supported.
    2.  **Bandwidth**:

        Attainable bandwidth during intra-VPC access. Options:  **100 MB/s**,  **300 MB/s**,  **600 MB/s**, and  **1200 MB/s**.

        To ensure service stability, a higher bandwidth is recommended if many connections or topics are involved.

    3.  **Maximum Partitions**: Retain the default value.

        This parameter indicates the maximum number of partitions that can be created for a Kafka premium instance. If the total number of partitions of all topics exceeds this threshold, topic creation will fail.

        -   When  **Bandwidth**  is  **100 MB/s**, the  **Maximum Partitions**  is  **300**.
        -   When  **Bandwidth**  is  **300 MB/s**: the  **Maximum Partitions**  is  **900**.
        -   When  **Bandwidth**  is  **600 MB/s**: the  **Maximum Partitions**  is  **1800**.
        -   When  **Bandwidth**  is  **1200 MB/s**: the  **Maximum Partitions**  is  **1800**.

    4.  **Storage Space**: Select the required type and size of the disk for storing the instance data. Currently, ultra-high I/O and high I/O disk types are supported.

        If the available disk space is less than 5%, you can retrieve but cannot create messages. Messages do not occupy any disk space after the retention period ends.

        Disks are formatted when an instance is created. As a result, the actual available disk space is 93% to 95% of the total disk space.

        -   When  **Bandwidth**  is set to  **100 MB/s**, the disk type can be  **Ultra-high I/O**  or  **High I/O**  and the value range of the disk size is 600–90,000 GB.
        -   When  **Bandwidth**  is set to  **300 MB/s**, the disk type can be  **Ultra-high I/O**  or  **High I/O**  and the value range of the disk size is 1,200–90,000 GB.
        -   When  **Bandwidth**  is set to  **600 MB/s**, the disk type can only be  **Ultra-high I/O**  and the value range of the disk size is 2,400–90,000 GB.
        -   When  **Bandwidth**  is set to  **1200 MB/s**, the disk type can only be  **Ultra-high I/O**  and the value range of the disk size is 4,800–90,000 GB.

        >![](/images/icon-note.gif) **NOTE:**   
        >-   High I/O + 100 MB/s bandwidth: If the average message size is 1 KB, the transactions per second \(TPS\) can reach 100,000 in high throughput scenarios and 60,000 in synchronous replication scenarios.  
        >-   High I/O + 300 MB/s bandwidth: If the average message size is 1 KB, the TPS can reach 300,000 in high throughput scenarios and 150,000 in synchronous replication scenarios.  
        >-   Ultra-high I/O + 100 MB/s bandwidth: If the average message size is 1 KB, the TPS can reach 100,000 in high throughput scenarios and 80,000 in synchronous replication scenarios.  
        >-   Ultra-high I/O + 300 MB/s bandwidth: If the average message size is 1 KB, the TPS can reach 300,000 in high throughput scenarios and 200,000 in synchronous replication scenarios.  
        >-   Ultra-high I/O + 600 MB/s bandwidth: If the average message size is 1 KB, the TPS can reach 600,000 in high throughput scenarios and 300,000 in synchronous replication scenarios.  
        >-   Ultra-high I/O + 1200 MB/s bandwidth: If the average message size is 1 KB, the TPS can reach 1,200,000 in high throughput scenarios and 400,000 in synchronous replication scenarios.  

    5.  Select a VPC.

        If you have available VPCs, the system automatically selects a VPC for you.

        -   A VPC provides an isolated virtual network for your Kafka premium instances. You can configure and manage the network as required.
        -   To view details about your VPCs, click  **View VPC**. On the displayed VPC console, choose the selected VPC to view details about it, including security group rules. If you do not need to view your VPCs, go to  [8.f](#li12208115112186).

    6.  <a name="li12208115112186"></a>Select a created subnet.

        If you have available subnets, the system automatically selects a subnet for you.

        To view details about your subnets, click  **View Subnet**. On the displayed VPC console, choose the selected subnet to view details about it, including the private IP addresses. If you do not need to view your subnets, go to  [8.g](#li173941323182813).

    7.  <a name="li173941323182813"></a>Select a security group.

        If you have available security groups, the system automatically selects a security group for you.

        A security group is a set of rules that control access to ECSs. It provides access policies for mutually trusted ECSs with the same security protection requirements in the same VPC.

        To view details about your security groups, click  **Manage Security Group**. On the displayed console, view or create security groups. If you do not need to manage your security groups, go to  [9](#li167781918124419).

9.  <a name="li167781918124419"></a>Configure  **Capacity Threshold Policy**

    This parameter indicates the action to be taken when the memory usage reaches the disk capacity threshold.

    -   **Stop production**: New messages cannot be created, but existing messages can still be retrieved.
    -   **Automatically delete**: Messages can be created and retrieved, but earliest 10% of messages will be deleted to ensure sufficient disk space.

10. Click  **More Settings**  to configure more parameters.
    1.  Configure  **Public Access**.

        Public access is disabled by default. You can enable or disable it as required. You can create a maximum of three Kafka instances with public access enabled. If you want to create more instances with public access, contact the administrator to increase your quota.

    2.  Configure  **Kafka SASL\_SSL**.

        You can configure whether to enable SSL authentication for clients to access the instance.

        If SSL authentication is enabled, data will be encrypted before transmission to enhance security.

        If you enable  **Kafka SASL\_SSL**, you must also set the username and password for accessing the instance.

        For details about password complexity requirements, see  [DMS Password Complexity Requirements](dms-password-complexity-requirements.md).

    3.  Specify  **Time Window**.

        This parameter indicates the time period when O&M personnel perform maintenance operations on the instance.

        During this period, services can still be used, but occasionally there may be temporary interruptions. Scheduled maintenance occurs infrequently \(typically once every few months\).

11. Click  **Create Now**.
12. Confirm the instance information.
13. After the new Kafka premium instance has been created, return to the  **Kafka Premium**  page to view and manage your Kafka premium instances.
    1.  It takes 3 to 15 minutes to create a Kafka premium instance.
    2.  After a Kafka premium instance has been successfully created, it enters the  **Running**  state by default.

        For more information about other statuses, see  [Table 1](viewing-an-instance.md#table5086721717534).

    3.  If the Kafka premium instance fails to be created, delete the unsuccessful instance creation task by following the procedure in  [Deleting an Instance](deleting-an-instance.md)  and then create the Kafka premium instance again. If the instance creation task fails again, contact customer service.


