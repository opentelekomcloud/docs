# Restoring a DB Instance to a Point in Time<a name="en-us_topic_sqlserver_0053089726"></a>

## **Scenarios**<a name="section3037032812838"></a>

RDS can use existing automated backups to restore DB instances to a point in time.

RDS for Microsoft SQL Server supports  restoration to a new, the original, or an existing DB instance.

If you delete a database or modify some records in a database at a specified time, you only need to restore the database instead of restoring the whole DB instance. You can also restore databases to a point in time as required.

## Constraints<a name="section10943038114813"></a>

If you restore backup data to a new DB instance:

-   The DB engine and port number of the database are the same as those of the original DB instance and cannot be changed.
-   You need to set a new administrator password.

## Procedure<a name="section116671682181"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  In the navigation pane on the left, choose  **Backups & Restorations**. On the displayed page, click  **Restore to Point in Time**.
6.  In the displayed dialog box, configure required information and click  **OK**.
    1.  Select the time range, select or enter a time point within the acceptable range.
    2.  Select a restoration method. 
        -   Create New Instance

            The  **Create New Instance**  page is displayed.

            -   The DB engine and port of the database are the same as those of the original DB instance and cannot be changed.
            -   By default, storage space of the new DB instance is the same as that of the original DB instance. The new storage space cannot be less than that of the original DB instance. The database password can be reset.
            -   Other settings are the same as those of the original DB instance by default and can be modified. For details, see section  [Step 1: Create a DB Instance](step-1-create-a-db-instance-(Microsoft-SQL-Server).md).

        -   Restore to Original

            >![](/images/icon-notice.gif) **NOTICE:**   
            >-   Restoring to the original DB instance will overwrite data on it and cause the original DB instance to be unavailable during the restoration.  

        -   Restore to Existing

            >![](/images/icon-notice.gif) **NOTICE:**   
            >-   Restoring to an existing DB instance will overwrite data on it and cause the existing DB instance to be unavailable.  
            >-   To restore backup data to an existing DB instance, the selected DB instance must be in the same VPC as the original DB instance and must have the same DB engine and the same or later version than the original DB instance.  
            >-   Ensure that the storage space of the selected DB instance is greater than or equal to the storage space of the original DB instance. Otherwise, data will not be restored.  
            >-   DB instances with the TDE function enabled cannot be restored from backups to existing DB instances.  

            Select an existing DB instance and click  **Next**.

    3.  Select the databases to be restored. You can rename these databases as required. If you do not enter a new name, the original database name will be used.

        >![](/images/icon-note.gif) **NOTE:**   
        >-   The new database names must be different from each other and must be different from the original database names.  
        >-   The new database names cannot contain the following fields \(case-insensitive\): rdsadmin, master, msdb, tempdb, model, and resource.  
        >-   Each database name consists of 1 to 64 characters. Only letters, digits, hyphens \(-\), and underscores \(\_\) are allowed.  


7.  View the restoration result. The result depends on which restoration method was selected:
    -   Create New Instance

        A new DB instance is created using the backup data. The status of the DB instance changes from  **Creating**  to  **Available**.

        The new DB instance is independent from the original one. 

    -   Restore to Original

        On the  **Instance Management**  page, the status of the DB instance changes from  **Restoring**  to  **Available**.

        A new restoration time range is available. There will be a difference between the new and original time ranges. This difference reflects the duration of the restoration.

    -   Restore to Existing

        On the  **Instance Management**  page, the status of the DB instance changes from  **Restoring**  to  **Available**.



