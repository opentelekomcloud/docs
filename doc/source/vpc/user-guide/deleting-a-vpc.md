# Deleting a VPC<a name="vpc_vpc_0003"></a>

## Scenarios<a name="sf9ccb52acbdd4f17b66be073ec8ad0f8"></a>

You can delete a VPC to release network resources if the VPC is no longer required.

A VPC cannot be deleted if it contains subnets, Direct Connect connections, custom routes, VPC peering connections, or VPNs. To delete the VPC, you must first delete or disable the resources.

-   For details about how to delete a subnet, see section  [Deleting a Subnet](deleting-a-subnet.md).
-   For details about how to delete a VPN, see  _Virtual Private Network User Guide_.
-   For details about how to disable a Direct Connect connection, see the  _Direct Connect User Guide_.
-   For details about how to delete a custom route, see section  [Deleting a Route](deleting-a-route.md).
-   For details about how to delete a VPC peering connection, see section  [Deleting a VPC Peering Connection](deleting-a-vpc-peering-connection.md).

## Impact on the System<a name="s8891699f335a4685a89225f1ea2d221c"></a>

There are any EIPs, the last VPC cannot be deleted.

## Procedure<a name="s714023cea7804d31880328b6d78b6a2b"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, click  **Virtual Private Cloud**.
5.  On the  **Virtual Private Cloud**  page, locate the row that contains the VPC to be deleted and click  **Delete**  in the  **Operation**  column.
6.  Click  **Yes**  in the displayed dialog box.

