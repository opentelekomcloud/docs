# Changing a Failover Priority<a name="rds_modify_availability"></a>

## **Scenarios**<a name="section241540814823"></a>

You can change the  failover policy  with a priority on availability or reliability to meet service requirements.

-   **Reliability**: This option is selected by default. Data consistency is preferentially ensured during the primary/standby failover. This is recommended for users whose highest priority is data consistency.
-   **Availability**: Database availability is preferentially ensured during the primary/standby failover. This is recommended for users who require their databases to provide uninterrupted online services.

## Procedure<a name="section45421719172826"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target primary/standby DB instances.
5.  In the  **DB Information**  area on the displayed  **Basic Information**  page, click  **Change**  in the  **Failover Priority**  field. In the displayed dialog box, select a priority and click  **OK**.
6.  View the result of the change on the  **Basic Information**  page.

