# Changing the Sequence of a Firewall Rule<a name="vpc_acl_0004"></a>

## Scenarios<a name="section23874042184557"></a>

If multiple firewall rules conflict, the rule in the front takes precedence. If you need a rule to take effect before or after a specific rule, you can insert that rule before or after the specific rule.

## Procedure<a name="section57145188185621"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **Access Control**  \>  **Firewalls**.
5.  Locate the target firewall in the right pane, and click the firewall name to switch to the page showing details of that particular firewall.
6.  On the  **Inbound Rules**  or  **Outbound Rules**  tab, locate the target rule, click  **More**  in the  **Operation**  column, and select  **Insert Rule Above**  or  **Insert Rule Below**.
7.  In the displayed dialog box, configure required parameters and click  **OK**.

    The firewall rule is inserted. The procedure for inserting an outbound firewall rule is the same as that for inserting an inbound firewall rule.


