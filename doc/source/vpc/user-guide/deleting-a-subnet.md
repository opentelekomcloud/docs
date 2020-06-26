# Deleting a Subnet<a name="vpc_vpc_0002"></a>

## Scenarios<a name="s8ad0e546d9d54aa58a7129000d48ed42"></a>

You can delete a subnet to release network resources if the subnet is no longer required.

## Prerequisites<a name="section15525141093410"></a>

Before deleting a subnet, ensure that any of the following resources using the subnet have been deleted.

-   ECS
-   BMS
-   CCE cluster
-   RDS instance
-   Workspace
-   MRS cluster
-   DCS instance
-   Elastic load balancer
-   VPN
-   Private IP address
-   Custom route
-   NAT gateway

Check and delete related resources on the management console.

## Procedure<a name="s4b884e9768c64c3098a294765ad64bc9"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, click  **Virtual Private Cloud**.
5.  On the  **Virtual Private Cloud**  page, locate the VPC from which a subnet is to be deleted and click the VPC name.
6.  On the  **Subnets**  page, locate the target subnet and click  **Delete**.
7.  Click  **Yes**  in the displayed dialog box.

