# Can an ECS Without an EIP Access the Internet?<a name="EN-US_TOPIC_0030013188"></a>

Yes.

-   Method 1: Configure a SNAT server.

    You can configure the SNAT server so that the ECS without an EIP bound can access the Internet.

    For details, see  ["Configuring a SNAT Server"](https://docs.otc.t-systems.com/en-us/usermanual/vpc/en-us_topic_0038764344.html)  in  _Virtual Private Cloud User Guide_.

-   Method 2: Create a NAT gateway.

    If a large number of concurrent connections are required, you are advised to use the NAT Gateway service provided by the public cloud platform.

    The NAT Gateway service offers the NAT function for ECSs in a VPC, allowing these ECSs to access the Internet using an EIP. For more information about NAT Gateway, see  _NAT Gateway User Guide_.


