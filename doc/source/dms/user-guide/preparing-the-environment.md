# Preparing the Environment<a name="EN-US_TOPIC_0143117136"></a>

Before creating Kafka premium instances, you need to create a VPC and configure security groups and subnets for it. If you already have a VPC, you do not need to create one again. A VPC creates an isolated virtual network environment for you to configure and manage Kafka instances, improving resource security and simplifying network deployment.

If your Kafka client runs on an ECS in the same VPC as your Kafka instance, access the instance using the intra-VPC connection address of the instance. If your Kafka client is deployed in external networks or runs on an ECS in a different VPC from your Kafka instance, access the instance using the public access address of the instance.

## Procedure<a name="section120910819351"></a>

1.  Log in to the management console.
2.  Choose  **Network**  \>  **Virtual Private Cloud**  to launch the VPC console.
3.  On the  **Dashboard**  page, click  **Create VPC**.
4.  Create a VPC as prompted, retaining the default values unless otherwise required. For details on how to create a VPC, see the  _Virtual Private Cloud User Guide_.

    After a VPC is created, a subnet is also created in the VPC. If the VPC needs more subnets, perform  [5](#li18952995367). Otherwise, go to  [6](#li1095210933611).

5.  <a name="li18952995367"></a>Click the name of the VPC for which you want to create a subnet. On the  **Subnets**  tab page, click  **Create Subnet**. Create a subnet as prompted, retaining the default values unless otherwise required.

    For details on how to create a subnet, see the  _Virtual Private Cloud User Guide_.

6.  <a name="li1095210933611"></a>Go back to the  **Virtual Private Cloud**  page. In the navigation pane, choose  **Access Control**  \>  **Security Group**  and then click  **Create Security Group**. Create a security group as prompted, retaining the default values unless otherwise required.

    For details on how to create a security group, see the  _Virtual Private Cloud User Guide_.


