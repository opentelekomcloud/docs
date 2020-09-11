# How Can I Create and Log In to an ECS?<a name="dds_faq_0034"></a>

For details on how to create and log in to an ECS, see "Creating and Logging In to a Windows ECS" or "Creating and Logging In to a Linux ECS" in the  _Elastic Cloud Server User Guide_.

-   The ECS to be created must be in the same VPC with the DDS DB instance to which it connects.
-   When you create an ECS, select an OS, such as Red Hat 6.6, and bind an EIP to it.
-   Configure the security group to enable the ECS to access the DB instance through the private IP address, that is, the value of  **Private IP Address**  of mongos on the  **Basic Information**  page.

