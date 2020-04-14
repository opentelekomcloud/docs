# Adding a Custom Route<a name="vpc_route_0006"></a>

## Scenarios<a name="s974a02c09b8e44f59dcc9335de2d030a"></a>

When ECSs in a VPC need to access the Internet, add a custom route to enable the ECSs to access the Internet through the ECS that has an EIP bound.

## Procedure<a name="sdec7a81b54b0476b8e37270f45edcca7"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, click  **Virtual Private Cloud**.
5.  On the  **Virtual Private Cloud**  page, locate the VPC to which a route is to be added and click the VPC name.
6.  On the  **Route Tables**  tab, click  **Add Route**.
7.  Set route details on the displayed page.

    -   **Destination**  indicates the destination CIDR block. The default value is  **0.0.0.0/0**. If the traffic originates from a VPC, the destination can be a subnet CIDR block in this VPC. If the traffic originates from outside the VPC, the destination CIDR block cannot conflict with any of the subnet CIDR blocks in this VPC. The destination of each route must be unique.
    -   **Next Hop**: indicates the IP address of the next hop. Set it to a private IP address or a virtual IP address in a VPC.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the next hop is a virtual IP address, an EIP must be bound to the virtual IP address. Otherwise, access to the Internet through this virtual IP address is not possible. \(A custom route is used to forward traffic from the virtual IP address to the Internet.\)  

8.  Click  **OK**.

