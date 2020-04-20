# Scaling Up Storage Space<a name="en-us_topic_scale_cluster"></a>

## **Scenarios**<a name="section3404387132643"></a>

You can  scale up  storage space if it is no longer sufficient for your requirements. When the DB instance status is  **Storage full**, data cannot be written to databases. 

For details about the causes and solutions of insufficient storage space, see section  [What Should I Do If My Data Exceeds the Database Storage Space of an RDS DB Instance?](what-should-i-do-if-my-data-exceeds-the-database-storage-space-of-an-rds-db-instance.md)

RDS allows you to  scale up storage space  of DB instances but you cannot change the storage type. Services are not interrupted during scaling.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   DB instances can be scaled up enormous times.  
>-   The DB instance is in  **Scaling up**  state when its storage space is being scaled up and the backup services are not affected.  
>-   For primary/standby DB instances, scaling up the primary DB instance will cause the standby DB instance to also be scaled up accordingly.  
>-   You cannot reboot or delete a DB instance that is being scaled up.  
>-   Storage space can only be scaled up, not down.  
>-   If you scale up a DB instance with disks encrypted, the expanded storage space will be encrypted using the original encryption key.  

## Scaling Up a Primary DB Instance<a name="section3535102285710"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target DB instance and choose  **More**  \>  **Scale Storage Space**  in the  **Operation**  column.

    You can also scale up storage space in either of the following ways:

    -   Click the target DB instance to enter the  **Basic Information**  page. In the  **Storage/Backup Space**  area, click  **Scale**.

5.  On the displayed page, specify the new storage space and click  **Next**.

    The minimum start value of each scaling is 10 GB. A read replica can be scaled up only by a multiple of 10 GB. The allowed maximum storage space is 4000 GB.

6.  Confirm your specifications.
    -   If you need to modify your settings, click  **Previous**.
    -   If you do not need to modify your settings, click  **Submit**.

7.  View the scale-up result.

    Scaling up storage space takes 3-5 minutes. During this time, the status of the DB instance on the  **Instance Management**  page will be  **Scaling up**. Click the DB instance and view the utilization on the displayed  **Basic Information**  page to verify that the scale-up is successful.

    If the DB instance is running the MySQL DB engine, you can view the detailed progress and result of the task on the  **Task Center**  page. For details, see section  [Task Center](task-center.md).


## Scaling Up a Read Replica<a name="section25847103185530"></a>

Scaling up the storage space of a read replica does not affect that of the primary DB instance. Therefore, you can separately scale read replicas to meet service requirements. New storage space of read replicas after scaling up must be greater than or equal to that of the primary DB instance. 

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target DB instance and click  ![](figures/expand.PNG)  in front of it. Locate a read replica to be scaled and choose  **More**  \>  **Scale Storage Space**  in the  **Operation**  column.

    You can also scale up storage space in either of the following ways:

    -   Click the target DB instance to enter the  **Basic Information**  page. In the  **Storage/Backup Space**  area, click  **Scale**.

5.  On the displayed page, specify the new storage space and click  **Next**.

    The minimum start value of each scaling is 10 GB. A read replica can be scaled up only by a multiple of 10 GB. The allowed maximum storage space is 4000 GB.

6.  Confirm your specifications.
    -   If you need to modify your settings, click  **Previous**.
    -   If you do not need to modify your settings, click  **Submit**.

7.  View the scale-up result.

    Scaling up storage space takes 3-5 minutes. During this time, the status of the read replica on the  **Instance Management**  page will be  **Scaling up**. Click the read replica and view the utilization on the displayed  **Basic Information**  page to verify that the scale-up is successful.

    If the read replica is running the MySQL DB engine, you can view the detailed progress and result of the task on the  **Task Center**  page. For details, see section  [Task Center](task-center.md).


