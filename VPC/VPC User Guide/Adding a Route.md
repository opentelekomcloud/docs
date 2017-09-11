## Adding a Route

### Scenarios

When ECSs in a VPC need to access the Internet, add a route to enable the ECSs
to access the Internet through the ECS that has an EIP bound.

### Procedure

2.  Log in to the management console.

3.  On the console homepage, under **Network**, click **Virtual Private Cloud**.

4.  In the navigation pane on the left, select a VPC to which a route is to be
    added and click **Route Table**.

5.  On the **Route Table** page, click **Add Route**.

6.  Set route information on the displayed page.

	-   **Destination**: indicates the destination network segment. The default
    value is **0.0.0.0/0**.

	-   **Next Hop**: indicates the IP address of the next hop. Set it to a private
    IP address or a floating private IP address in a VPC.

	![](figure/NOTE.png)

	If **Next Hop** is set to a floating private IP address, the floating private IP
addresses in the VPC cannot have EIPs bound. Otherwise, the route will not take
effect.

1.  Click **OK**.
