# Restoring a DB Instance from a Backup<a name="en-us_topic_0053089727"></a>

## **Scenarios**<a name="section51567119122258"></a>

This section describes how to use an automated or manual backup to restore a DB instance to the status when the backup was created.

## Procedure<a name="section51247315503"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Backups & Restorations**  page, locate the target backup and click  **Restore**  in the  **Operation**  column.

    Alternatively, click the target DB instance on the  **Instance Management**  page. On the displayed page, choose  **Backups & Restorations**. On the displayed page, select the target backup to be restored and click  **Restore**  in the  **Operation**  column.

5.  In the displayed dialog box, configure required information and click  **OK**.
    1.  Select a restoration method.
        -   Create New Instance

            The  **Create New Instance**  page is displayed.

            -   The DB engine and version are the same as those of the original DB instance and cannot be changed. The database port number is  **1433**  by default and cannot be changed during the restoration.
            -   By default, storage space of the new DB instance is the same as that of the original DB instance. The new storage space cannot be less than that of the original DB instance. The database password can be reset.
            -   Other settings are the same as those of the original DB instance by default and can be modified. For details, see section  [Step 1: Create a DB Instance](step-1-create-a-db-instance-(Microsoft-SQL-Server).md).

        -   Restore to Original

            >![](/images/icon-notice.gif) **NOTICE:**   
            >-   If the DB instance for which the backup is created has been deleted, data cannot be restored to the original DB instance.  
            >-   Restoring to the original DB instance will overwrite data on it and cause the original DB instance to be unavailable during the restoration.  

        -   Restore to Existing

            >![](/images/icon-notice.gif) **NOTICE:**   
            >-   Restoring to an existing DB instance will overwrite data on it and cause the existing DB instance to be unavailable.  
            >-   To restore backup data to an existing DB instance, the selected DB instance must be in the same VPC as the original DB instance and must have the same DB engine and the same or later version than the original DB instance.  
            >-   Ensure that the storage space of the selected DB instance is greater than or equal to the storage space of the original DB instance. Otherwise, data will not be restored.  
            >-   DB instances with the TDE function enabled cannot be restored from backups to existing DB instances.  

            Select an existing DB instance and click  **Next**.

    2.  Select the databases to be restored. You can rename these databases as required. If you do not enter a new name, the original database name will be used.

        >![](/images/icon-note.gif) **NOTE:**   
        >-   The new database names must be different from each other and must be different from the original database names.  
        >-   The new database names cannot contain the following fields \(case-insensitive\): rdsadmin, master, msdb, tempdb, model, and resource.  
        >-   Each database name consists of 1 to 64 characters. Only letters, digits, hyphens \(-\), and underscores \(\_\) are allowed.  


6.  View the restoration result. The result depends on which restoration method was selected:
    -   Create New Instance

        A new DB instance is created using the backup data. The status of the DB instance changes from  **Creating**  to  **Available**.

        The new DB instance is independent from the original one. If you need read replicas to offload read pressure, create one or more for the new DB instance.

    -   Restore to Original

        On the  **Instance Management**  page, the status of the target existing DB instance changes from  **Restoring**  to  **Available**. If the target existing DB instance contains read replicas, the read replica status is the same as the target existing DB instance status.

        If the automated backup policy is enabled, a full backup will be triggered after the restoration is complete. Otherwise, the full backup will not be triggered.

    -   Restore to Existing

        On the  **Instance Management**  page, the status of the DB instance changes from  **Restoring**  to  **Available**.



