## Enabling or Disabling a Firewall

### Scenario

After a firewall is created, enable it based on your network security
requirements. You can also disable an enabled firewall when required. Before
enabling or disabling a firewall, ensure that subnets have been associated with
the firewall and that inbound and outbound rules have been added to the
firewall.

A firewall is in the **Inactive** state if no subnets are associated with the
firewall. If you enable a firewall in the **Inactive** state, the firewall does
not take effect for any subnet.

A firewall is in the **Normal** state if subnets are associated with the
firewall. If you enable a firewall in the **Normal** state, the firewall has the
following default rules:

-   Allows broadcast packets with a destination of 255.255.255.255/32.

-   Allows multicast packets with a destination of 224.0.0.0/24.

-   Allows metadata packets with a destination of 169.254.169.254/32 and with
    TCP port 80.

-   Allows packets from the CIDR blocks that are reserved for public services.
    For example, allows packets with a destination of 100.126.0.0/16.

-   Denies all other packets by default.

After the firewall is enabled, firewall rules take precedence over security
group rules.

### Procedure

2.  Log in to the management console.

3.  On the console homepage, under **Network**, click **Virtual Private Cloud**.

4.  In the navigation tree on the left, click **Firewall**.

5.  Locate the required firewall in the right pane, and click **Enable** or
    **Disable** in the **Operation** column.

6.  Click **OK** in the displayed dialog box.

	The firewall is enabled or disabled.
