# Associating Subnets with a Firewall<a name="en-us_topic_0051746700"></a>

## Scenarios<a name="section2661009154525"></a>

On the page showing firewall details, associate desired subnets with a firewall. After a firewall is associated with a subnet, the firewall denies all traffic to and from the subnet until you add rules to allow traffic.

## Procedure<a name="section23848003154739"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **Access Control**  \>  **Firewalls**.
5.  Locate the target firewall in the right pane, and click the firewall name to switch to the page showing details of that particular firewall.
6.  On the displayed page, click the  **Associated Subnets**  tab.
7.  On the  **Associated Subnets**  page, click  **Associate**. 
8.  On the displayed page, select the subnets to be associated with the firewall, and click  **OK**.

    The selected subnets are associated with the firewall.


>![](/images/icon-note.gif) **NOTE:**   
>Subnets that have already been associated with firewalls will not be displayed on the page for you to select. One-click subnet association and disassociation are not currently supported. Furthermore, a subnet can only be associated with one firewall. If you want to reassociate a subnet that has already been associated with another firewall, you must first disassociate the subnet from the original firewall.  

