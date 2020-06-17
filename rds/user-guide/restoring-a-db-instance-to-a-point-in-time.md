# Restoring a DB Instance to a Point in Time<a name="en-us_topic_0044703399"></a>

## **Scenarios**<a name="section3037032812838"></a>

RDS can use existing automated backups to restore DB instances to a point in time.

RDS for MySQL supports  restoration to a new, the original,  or an existing DB instance.

## Constraints<a name="section18971149163412"></a>

-   If you restore backup data to a new DB instance:
    -   The DB engine, version, and port number of the database are the same as those of the original DB instance and cannot be changed.
    -   You need to set a new administrator password.


## Restoring a DB Instance<a name="section26193354164653"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  In the navigation pane on the left, choose  **Backups & Restorations**. On the displayed page, click  **Restore to Point in Time**.
6.  Select a restoration date and time range, enter a time point within the selected time range, and select a restoration method. Then, click  **OK**.
    -   Create New Instance

        The  **Create New Instance**  page is displayed.

        -   The DB engine, version, and port number of the database are the same as those of the original DB instance and cannot be changed.
        -   You need to set a new administrator password.
        -   You can modify the other parameter values.

    -   Restore to Original

        >![](/images/icon-notice.gif) **NOTICE:**   
        >Restoring to the original DB instance will overwrite all existing data and the DB instance will be unavailable during the restoration process.  

    -   Restore to Existing

        >![](/images/icon-notice.gif) **NOTICE:**   
        >-   Restoring to an existing DB instance will overwrite data on it and cause the existing DB instance to be unavailable.  
        >-   To restore backup data to an existing DB instance, the selected DB instance must be in the same VPC as the original DB instance and must have the same DB engine and the same or later version than the original DB instance.   
        >-   Ensure that the storage space of the selected DB instance is greater than or equal to the storage space of the original DB instance. Otherwise, data will not be restored.  

        Select an existing DB instance and click  **OK**.

7.  View the restoration result. The result depends on which restoration method was selected:

    -   Create New Instance

        A new DB instance is created using the backup data. The status of the DB instance changes from  **Creating**  to  **Available**.

        The new DB instance is independent from the original one. If you need read replicas to offload read pressure, create one or more for the new DB instance.

    -   Restore to Original

        On the  **Instance Management**  page, the status of the DB instance changes from  **Restoring**  to  **Available**.

        A new restoration time range is available. There will be a difference between the new and original time ranges. This difference reflects the duration of the restoration.

    -   Restore to Existing

        On the  **Instance Management**  page, the status of the DB instance changes from  **Restoring**  to  **Available**.

    After the restoration, the system will perform a full backup.


