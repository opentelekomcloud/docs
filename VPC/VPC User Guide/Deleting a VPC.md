## Deleting a VPC
### Scenarios

You can delete a VPC to release network resources if the VPC is no longer
required.

A VPC cannot be deleted if it contains VPN, Direct Connect connections, custom
routes, VPC peering connections, or subnets. To delete the VPC, you must first
delete or disable the resources.

-   For details about how to delete a subnet, see section <a href="Deleting a
    Subnet.md">Deleting a Subnet</a>.

-   For details about how to delete a VPN, see section <a href="Deleting a VPN.md">Deleting a VPN</a>.

-   For details about how to disable a Direct Connect connection, see the
    ***Direct Connect User Guide***.

-   For details about how to delete a custom route, see section <a href="Deleting a Route.md">Deleting a Route</a>.

-   For details about how to delete a VPC peering connection, see section <a href="Deleting a VPC Peering Connection.md">Deleting a VPC Peering Connection</a>.

### Impact on the System

If EIPs exist, the last VPC cannot be deleted.

### Procedure

2.  Log in to the management console.

3.  On the console homepage, under **Network**, click **Virtual Private Cloud**.

4.  In the navigation pane on the left, choose **Virtual Private Cloud**.

5.  On the **Virtual Private Cloud** page, locate the target VPC, and click
 ![](figure/156606d9df3d2a26c70e1841e80d1d0c.png).

6.  Click **OK** in the displayed dialog box.
