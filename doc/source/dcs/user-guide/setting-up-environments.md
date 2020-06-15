# Setting Up Environments<a name="EN-US_TOPIC_0237964713"></a>

To access DCS instances through a VPC, create a VPC and configure security groups and subnets for it before using DCS.

A VPC provides an isolated, user-configurable, and user-manageable virtual network environment for DCS. Using VPCs enhances resource security and simplifies network deployment.

Once you have created a VPC, you can use it for all DCS instances you subsequently create.

## Procedure<a name="section52078584"></a>

1.  Log in to the management console.
2.  Click![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose  **Network**  \>  **Virtual Private Cloud**  to launch the VPC console.
4.  On the  **Dashboard**  page, click  **Create VPC**.
5.  Create a VPC as guided by the VPC console, retaining the default values of the VPC parameters unless otherwise required.

    For more information on how to create a VPC, see the  _Virtual Private Cloud User Guide_.

    After a VPC is created, a subnet is also created in the subnet. If the VPC needs more subnets, go to  [Step 6](#li741115910284). Otherwise, go to  [7](#li1940024225812).

6.  <a name="li741115910284"></a>In the navigation pane, choose  **Virtual Private Cloud**. On the  **Virtual Private Cloud**  page, click the name of the VPC in which you intend to create a subnet. On the  **Subnets**  tab page, click  **Create Subnet**.

    Create a subnet as guided by the VPC console, retaining the default values of the subnet parameters unless otherwise required.

    For more information on how to create a subnet, see the  _Virtual Private Cloud User Guide_.

7.  <a name="li1940024225812"></a>In the navigation pane, choose  **Security Group**. On the  **Security Group**  page, click  **Create Security Group**.

    Create a security group for the VPC, retaining the default values of the security group parameters unless otherwise required.

    For more information on how to create a security group, see the  _Virtual Private Cloud User Guide_.


