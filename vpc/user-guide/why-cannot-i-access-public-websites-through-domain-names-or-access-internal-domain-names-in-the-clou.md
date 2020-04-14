# Why Cannot I Access Public Websites Through Domain Names or Access Internal Domain Names in the Cloud When My ECS Has Multiple NICs?<a name="vpc_faq_0060"></a>

When an ECS has more than one NIC, if different DNS server addresses are configured for the subnets used by the NICs, the ECS cannot access public websites or internal domain names in the cloud.

You can rectify this fault by configuring the same DNS server address for the subnets used by the same ECS. You can perform the following steps to modify DNS server addresses of subnets in a VPC:

1.  Log in to the management console.
2.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
3.  In the navigation pane on the left, click  **Virtual Private Cloud**.
4.  On the  **Virtual Private Cloud**  page, locate the VPC for which a subnet is to be modified and click the VPC name.
5.  In the subnet list, locate the row that contains the subnet to be modified, click  **Modify**. On the displayed page, change the DNS server address as prompted.
6.  Click  **OK**.

