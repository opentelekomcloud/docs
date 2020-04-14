# What Should I Do If an ECS Cannot Connect to a Cluster?<a name="css_02_0025"></a>

Perform the following steps:

1.  Check whether the ECS instance and cluster are in the same VPC.
    -   If yes, go to  [2](#li47021920155415).
    -   If not, create an ECS instance and ensure that the ECS instance is in the same VPC as the cluster.

2.  <a name="li47021920155415"></a>View the security group rule setting of the cluster to check whether port  **9200**  \(TCP protocol\) is allowed or port  **9200**  is included in the port range allowed in both the outbound and inbound directions.
    -   If yes, go to  [3](#li770210445265).
    -   If not, switch to the VPC management console and set the security group rule of the cluster to allow port  **9200**  in both the outbound and inbound directions.

3.  <a name="li770210445265"></a>Check whether the ECS instance is added to a security group.
    -   If added to a security group, check whether the security group configuration rules meet the requirements. For details, see the description of  **Security Group**  in the cluster information table in  **Clusters**. Then go to  [4](#li12702114432619).

        **Figure  1**  Viewing security group information<a name="fig1702184492614"></a>  
        ![](figures/viewing-security-group-information.png "viewing-security-group-information")

    -   If not, go to the VPC page from the ECS instance details page, select a security group, and add the security group.

4.  <a name="li12702114432619"></a>Check whether the ECS instance can connect to the cluster.

    **ssh** _<Private network address and port number of a node\>_

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the cluster contains multiple nodes, check whether the ECS can be connected to each node in the cluster.  

    -   If the connection is normal, the network is running properly.
    -   If the port is unreachable, contact customer service.


