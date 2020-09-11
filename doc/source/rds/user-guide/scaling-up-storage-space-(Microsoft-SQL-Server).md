# Scaling Up Storage Space<a name="en-us_topic_sqlserver_scale_cluster"></a>

## **Scenarios**<a name="section12164121514"></a>

You can  scale up  storage space if it is no longer sufficient for your requirements. When the DB instance status is  **Storage full**, data cannot be written to databases. 

For details about the causes and solutions of insufficient storage space, see section  [What Should I Do If My Data Exceeds the Database Storage Space of an RDS DB Instance?](what-should-i-do-if-my-data-exceeds-the-database-storage-space-of-an-rds-db-instance.md)

RDS allows you to  scale up storage space  of DB instances but you cannot change the storage type. Services are not interrupted during scaling.

>![](/images/icon-note.gif) **NOTE:**   
>-   DB instances can be scaled up enormous times.  
>-   For primary/standby DB instances, scaling up the primary DB instance will cause the standby DB instance to also be scaled up accordingly.  
>-   You cannot reboot or delete a DB instance that is being scaled up.  
>-   Storage space can only be scaled up, not down.  
>-   If you scale up a DB instance with disks encrypted, the expanded storage space will be encrypted using the original encryption key.  

## Procedure<a name="section5406175751315"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target DB instance and choose  **More**  \>  **Scale Storage Space**  in the  **Operation**  column.

    You can also scale up storage space in either of the following ways:

    -   Click the target DB instance to enter the  **Basic Information**  page. In the  **Storage/Backup Space**  area, click  **Scale**.

5.  On the displayed page, specify the new storage space and click  **Next**.

    The minimum start value of each scaling is 10 GB. A DB instance can be scaled up only by a multiple of 10 GB. The allowed maximum storage space is 4000 GB.

6.  Confirm your specifications.
    -   If you need to modify your settings, click  **Previous**.
    -   If you do not need to modify your settings, click  **Submit**.

7.  View the scale-up result.

    Scaling up storage space takes 3-5 minutes. During this time, the status of the DB instance on the  **Instance Management**  page will be  **Scaling up**. Click the DB instance and view the utilization on the displayed  **Basic Information**  page to verify that the scale-up is successful.


