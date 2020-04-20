# Can an External Server Access the RDS Database?<a name="rds_faq_0018"></a>

## DB Instance Bound with an EIP<a name="section12917429162714"></a>

For a DB instance that has been bound with an EIP, you can access it through the EIP.

## DB Instance Not Bound with an EIP<a name="section472356162714"></a>

-   Enable a VPN in a VPC and use the VPN to connect to the RDS DB instance.
-   Create an RDS and an ECS in the same VPC and access RDS through the ECS.

