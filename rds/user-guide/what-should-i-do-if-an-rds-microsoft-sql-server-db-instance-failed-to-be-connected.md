# What Should I Do If an RDS Microsoft SQL Server DB Instance Failed to Be Connected?<a name="rds_faq_0100"></a>

## Fault Location<a name="section1659771718232"></a>

-   Check whether the ECS can connect to the RDS DB instance.

    If the ECS cannot connect to the RDS DB instance, check whether the ECS and RDS DB instance are located in the same VPC and security group.


-   Check whether the IP address and port number are correct.

    Use a colon to separate an IP address and a port number.

-   Check whether the RDS service is running properly.
-   Check whether the username and password are correct. You can reset the password.
-   Reboot the RDS DB instance and check whether it can be connected through an ECS.

## Solution<a name="section6611183220249"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance. On the  **Basic Information**  and  **Backups & Restorations**  pages, check connection and backup information.
5.  On the  **Basic Information**  page, check the administrator.
6.  Download an SQL Server Management Studio installation package and install it on an ECS.
7.  Connect to the RDS DB instance through an ECS.

