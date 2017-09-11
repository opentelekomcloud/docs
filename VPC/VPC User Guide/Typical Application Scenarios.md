## Typical Application Scenarios

A VPC provides an isolated virtual network for ECSs. You can configure and
manage the network as required.

-   If your ECSs do not need to access the Internet or need to access the Internet using a specified IP address with limited bandwidth on defaultnetwork segment 100.64.0.0/11, for example, the ECSs functioning as the database or server nodes for deploying a website, you can configure a VPC for the ECSs by following the instructions described in section <a href="Configuring the VPC of ECSs That Do Not Need to Access the Internet.md">Configuring the VPC of ECSs That Do Not Need to Access the Internet</a>.

-   If your ECSs need to access the Internet, you can configure EIPs for them.For example, the ECSs functioning as the service nodes for deploying a website need to be accessed by users over the Internet. Then, you can configure the VPC of these ECSs by following the instructions provided in section <a href="Configuring the VPC of ECSs That Access the Internet Using EIPs.md">Configuring the VPC of ECSs That Access the Internet Using EIPs</a>.

-   If you need to access ECSs in a VPC over the Internet to perform maintenance
    operations, you can configure a VPN. For example, a website administrator
    needs to use a VPN to access ECSs functioning as service nodes in the VPC
    over the Internet. Then, you can configure the VPC of these ECSs by
    following the instructions provided in section <a href="Configuring the VPC of ECSs That Access the Internet Through a VPN.md">Configuring the VPC of
    ECSs That Access the Internet Through a VPN</a>.
