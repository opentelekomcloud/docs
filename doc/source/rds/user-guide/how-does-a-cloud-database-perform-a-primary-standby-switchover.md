# How Does a Cloud Database Perform a Primary/Standby Switchover?<a name="rds_faq_0065"></a>

RDS provides primary/standby DB instances for high availability. The system will perform a primary/standby switchover in case of a failure.

## Failover \(Automatic\)<a name="sdff147486087439ab2239da8f88afa16"></a>

It is also called out-planned handover. If the primary DB instance fails, the system will automatically switch to the standby DB instance within 5 minutes. No human intervention is required. The connection IP address remains unchanged. DB instances cannot be accessed during the failover. You need to configure automatic reconnections between applications and RDS DB instances to ensure near-continuous availability.

## Switchover \(Manual\)<a name="sabc33311a0ed4885a5bee220bb7fb976"></a>

It is also called out-planned handover. When a DB instance is running properly, you can manually perform a primary/standby switchover as required.

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


