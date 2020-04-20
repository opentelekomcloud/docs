# Changing a DB Instance Type from Single to Primary/Standby<a name="rds_pg_05_0023"></a>

## Scenarios<a name="en-us_topic_0171122491_section1715294212120"></a>

-   RDS enables you to  change single DB instances to primary/standby DB instances  to improve DB instance reliability.
-   Primary/standby DB instances support automatic failover. If the primary DB instance fails, the standby DB instance takes over services quickly. You are advised to deploy primary and standby DB instances in different AZs for high availability and disaster recovery.

## Procedure<a name="en-us_topic_0171122491_section2247117297"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target DB instance and choose  **More**  \>  **Change Type to Primary/Standby**  in the  **Operation**  column.

    Alternatively, click the target DB instance. In the DB instance topology, click  ![](figures/read.png)  on the left to change type from single to primary/standby.

5.  Select a standby AZ. Other configurations are the same as those of the primary DB instance by default. Confirm the configurations and click  **Submit**.
6.  After a single DB instance is changed to primary/standby instances, you can view and manage it on the  **Instance Management**  page.
    -   The DB instance is in the  **Changing type to primary/standby**  status. You can view the progress on the  **Task Center**  page. For details, see  [Task Center](task-center-(PostgreSQL).md).
    -   In the upper right corner of the DB instance list, click  ![](figures/refresh.png)  to refresh the list. After the DB instance type is changed to primary/standby, the instance status will change to  **Available**  and the instance type will change to  **Primary/Standby**.


