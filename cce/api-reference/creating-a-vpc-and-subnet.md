# Creating a VPC and Subnet<a name="cce_02_0100"></a>

## Context<a name="en-us_topic_0045969089_section156014348216"></a>

To provide a secure and isolated network environment for CCE, create a VPC before creating a cluster.

If you have already created a VPC, you do not need to create it again.

## Creating a VPC<a name="en-us_topic_0045969089_section4941460313"></a>

1.  On the management console, click  **Service List**, and choose  **Network**  \>  **Virtual Private Cloud**  to launch the VPC console.
2.  On the VPC console, click  **Create VPC**.
3.  The created VPC is displayed in the list. Click its name and obtain the VPC ID, which will be required in  [Creating a Cluster](creating-a-cluster.md).

    **Figure  1**  Obtaining the VPC ID<a name="fig12864043141413"></a>  
    ![](figures/obtaining-the-vpc-id.png "obtaining-the-vpc-id")


## Creating a Subnet<a name="section18343153916445"></a>

1.  On the management console, click  **Service List**, and choose  **Network**  \>  **Virtual Private Cloud**  to launch the VPC console.
2.  In the VPC list, click the VPC name. Then, click  **Create Subnet**  on the  **Subnets**  tab.
3.  After the subnet is created, click its name to obtain the network ID, which will be required in  [Creating a Cluster](creating-a-cluster.md).

    **Figure  2**  Obtaining the network ID of a subnet<a name="fig10205823121619"></a>  
    ![](figures/obtaining-the-network-id-of-a-subnet.png "obtaining-the-network-id-of-a-subnet")


