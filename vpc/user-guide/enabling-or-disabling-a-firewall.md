# Enabling or Disabling a Firewall<a name="vpc_acl_0011"></a>

## Scenarios<a name="section42378806145341"></a>

After a firewall is created, you may need to enable it based on network security requirements. You can also disable an enabled firewall if need. Before enabling a firewall, ensure that subnets have been associated with the firewall and that inbound and outbound rules have been added to the firewall.

When a firewall is disabled, custom rules will become invalid. Only the default firewall rules will still apply. Disabling a firewall may interrupt network traffic. Exercise caution when performing this operation. For information about the default firewall rules, see  [Default Firewall Rules](firewall-overview.md#section99541345213).

## Procedure<a name="section2117296514586"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **Access Control**  \>  **Firewalls**.
5.  Locate the target firewall in the right pane, click  **More**  in the  **Operation**  column, and click  **Enable**  or  **Disable**.
6.  Click  **Yes**  in the displayed dialog box.

    The firewall is enabled or disabled.


