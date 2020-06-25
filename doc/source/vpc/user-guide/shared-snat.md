# Shared SNAT<a name="vpc_Concepts_0010"></a>

The VPC service provides free, shared source network address translation \(SNAT\), which allows ECSs to use a limited number of public IP addresses to gain one-way access to the Internet for operations, such as updating software. However, Internet users cannot directly access the ECSs.

[Figure 1](#f04fc5d5739d142e5b38d73f3746f6cad)  shows how shared SNAT works. The SNAT device forwards traffic from ECSs to the Internet and the response traffic from the Internet to the ECSs. When forwarding ECS traffic to the Internet, the SNAT device converts the source IP addresses \(ECS private IP addresses\) in the data packets into the public IP addresses set on the SNAT device. When processing the response packets from the Internet to the ECSs, the SNAT device changes the public IP addresses in the response data packets to the private IP addresses of the ECSs.

**Figure  1**  SNAT function<a name="f04fc5d5739d142e5b38d73f3746f6cad"></a>  
![](figures/snat-function.png "snat-function")

-   To enable shared SNAT using the API, set  **enable\_snat**  to  **true**  by following the instructions provided in  **Neutron**  \>  **Routers**  \>  **Update router**  in the  _Native OpenStack API Reference_.
-   To enable shared SNAT on the management console:
    1.  Log in to the management console.
    2.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
    3.  On the  **Virtual Private Cloud**  page, locate the VPC for which shared SNAT is to be enabled, and click  **Modify**.
    4.  In the displayed dialog box, enable  **Shared SNAT**.
    5.  Click  **OK**.


After being configured for a VPC, shared SNAT takes effect for the whole VPC. If EIPs are bound to ECSs in a VPC for which shared SNAT is configured, Internet traffic is preferentially forwarded using the EIPs. If you want to prevent an ECS from connecting to the Internet, you can configure an outbound rule for the security group associated with the ECS.

For example:

To prevent an ECS from connecting to the Internet but allow the ECS to access the 192.168.10.0/24 network segment, configure the following rule for the security group associated with the ECS:

1.  Delete the default outbound rule that allows all outgoing data packets from the security group.

    After this rule is deleted, ECSs associated with this security group are not allowed to access any network, including the internal networks in the VPC of the ECSs.

    **Figure  2**  Deleting the default outbound rule from the security group<a name="fig940762518111"></a>  
    ![](figures/deleting-the-default-outbound-rule-from-the-security-group.png "deleting-the-default-outbound-rule-from-the-security-group")

2.  Add the required outbound rule.

    The following shows the added outbound rule that allows the ECS to access the 192.168.10.0/24 CIDR block.

    **Figure  3**  Adding an outbound rule for the security group<a name="fig57288721181150"></a>  
    ![](figures/adding-an-outbound-rule-for-the-security-group.png "adding-an-outbound-rule-for-the-security-group")

    The differences between shared SNAT and custom routes are as follows:

    -   Shared SNAT provides the SNAT function for a specified VPC through an API or the management console and enables all ECSs in the VPC to gain one-way access to the Internet.
    -   A custom route enables ECSs to access the Internet through an SNAT server that has an EIP bound. The ECSs' access requests are routed to the SNAT server based on the route table.
    -   Shared SNAT takes effect for the whole VPC by default, while a custom route takes effect for the VPC or subnet for which routes have been configured.
    -   A custom route has a higher priority than a shared SNAT.


