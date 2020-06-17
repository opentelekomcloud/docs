# Rebooting a DB Instance<a name="en-us_topic_sqlserver_0031146654"></a>

## **Scenarios**<a name="en-us_topic_0031146654_section11160182171227"></a>

When you maintain a DB instance, you may need to reboot it. After modifying some parameters, you must reboot the DB instance for the modifications to take effect. You can reboot a primary DB instance or a read replica on the management console. 

To reboot a DB instance, the following requirements must be met:

-   The status of the DB instance is  **Available**.
-   No backup is being created or no read replica is being created.

>![](/images/icon-notice.gif) **NOTICE:**   
>-   You can reboot a DB instance only when its status is  **Available**. Your database may be unavailable in some cases such as data is being backed up or some modifications are being made.  
>-   Rebooting DB instances will reboot database services. Rebooting a DB instance will cause service interruption. During this period, the DB instance status is  **Rebooting**.  
>-   This DB instance will not be available when it is being rebooted. After the reboot completes, the cached memory will be automatically cleared. The DB instance needs to be warmed up to prevent congestion during peak hours.  

## Procedure<a name="en-us_topic_0031146654_s22e3edfb1cdd4405b64cad650a1cf9a0"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target DB instance, or click  ![](figures/expand.PNG)  and then locate the target read replica. Choose  **More**  \>  **Reboot**  in the  **Operation**  column.

    Alternatively, click the target DB instance on the  **Instance Management**  page to go to the  **Basic Information**  page. In the upper right corner, click  **Reboot**.

    For primary/standby DB instances, if you reboot the primary DB instance, the standby DB instance is also rebooted automatically.

5.  In the displayed  **Reboot DB Instance**  dialog box, click  **Yes**.
6.  Refresh the DB instance list and view the status of the DB instance. If its status is  **Available**, it has rebooted successfully.

