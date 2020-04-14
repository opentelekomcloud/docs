# Assigning a Virtual IP Address<a name="vpc_vip_0002"></a>

## Scenarios<a name="se6c62cd61b874228a8bde0cc58d45fae"></a>

If an ECS requires a virtual IP address or if a virtual IP address needs to be reserved, you can assign a virtual IP address from the subnet.

## Procedure<a name="section56200370103127"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.

1.  In the navigation pane on the left, click  **Virtual Private Cloud**.
2.  On the  **Virtual Private Cloud**  page, locate the VPC containing the subnet where a virtual IP address is to be assigned, and click the VPC name.
3.  On the  **Subnets**  tab, click the name of the subnet where a virtual IP address is to be assigned.
4.  Click the  **Virtual IP Addresses**  tab and click  **Assign Virtual IP Address**.
5.  Select a virtual IP address assignment mode.
    -   **Automatic**: The system assigns an IP address automatically.
    -   **Manual**: You can specify an IP address.

6.  Select  **Manual**  and enter a virtual IP address.
7.  Click  **OK**.

You can then query the assigned virtual IP address in the IP address list.

