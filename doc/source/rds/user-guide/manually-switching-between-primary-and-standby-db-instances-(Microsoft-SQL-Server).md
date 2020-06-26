# Manually Switching Between Primary and Standby DB Instances<a name="rds_sqlserver_switch_ha"></a>

## Scenarios<a name="section11101174152216"></a>

If you choose to create primary/standby DB instances, RDS will create a primary DB instance and a synchronous standby DB instance in the same region. You can access only the primary DB instance. The standby instance serves as a backup. You can manually promote the standby DB instance to the new primary instance for failover support.

## Prerequisites<a name="section1810114414226"></a>

1.  A DB instance is running properly.
2.  The replication relationship between the primary and standby instances is normal.

## Procedure<a name="section1715094352112"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  In the  **DB Information**  area on the displayed  **Basic Information**  page, click  **Switch**  in the  **DB Instance Type**  field.

    Alternatively, click  ![](figures/switch.PNG)  in the DB instance topology on the  **Basic Information**  page to perform a primary/standby switchover.

    >![](/images/icon-notice.gif) **NOTICE:**   
    >Primary/standby switchover may cause service interruption for some seconds or minutes \(determined by the replication delay\). If the primary/standby synchronization delay is too long, a small amount of data may get lost. After the switchover completes, the DB instance needs to be warmed up to prevent congestion during peak hours.  

6.  In the  **Switch Primary/Standby Instances**  dialog box, click  **Yes**  to switch between the primary and standby DB instances.

    If the replication status is  **Available**  and the replication delay is greater than 300s, the primary/standby switchover task cannot be delivered. 

7.  After a switchover is successful, you can view and manage the DB instance on the  **Instance Management**  page.
    -   During the switchover process, the DB instance status is  **Switchover in progress**.
    -   In the upper right corner of the DB instance list, click  ![](figures/refresh.png)  to refresh the list. After the switchover is successful, the DB instance status will become  **Available** 


