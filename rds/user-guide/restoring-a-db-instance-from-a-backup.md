# Restoring a DB Instance from a Backup<a name="en-us_topic_0037000196"></a>

## **Scenarios**<a name="section468581517207"></a>

This section describes how to use an automated or manual backup to restore a DB instance to the status when the backup was created. The restoration is at the DB instance level.

## Procedure<a name="section56693485162629"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Backup Management**  page, select the backup to be restored and click  **Restore**  in the  **Operation**  column.

    Alternatively, click the target DB instance on the  **Instance Management**  page. On the displayed page, choose  **Backups & Restorations**. On the displayed page, select the target backup to be restored and click  **Restore**  in the  **Operation**  column.

5.  Select one of the following restoration methods and click  **OK**.

    -   Create New Instance

        The  **Create New Instance**  page is displayed.

        -   The DB engine and version are the same as those of the original DB instance and cannot be changed. The database port is  **3306**  by default and cannot be changed during the restoration.
        -   By default, storage space of the new DB instance is the same as that of the original DB instance. The new storage space cannot be less than that of the original DB instance. The database password can be reset.
        -   Other settings are the same as those of the original DB instance by default and can be modified. For details, see section  [Step 1: Create a DB Instance](step-1-create-a-db-instance.md).

    -   Restore to Original

        >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
        >-   If the DB instance for which the backup is created has been deleted, data cannot be restored to the original DB instance.  
        >-   Restoring to the original DB instance will overwrite all existing data and the DB instance will be unavailable during the restoration process.  

    -   Restore to Existing

        >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
        >-   If the target existing DB instance has been deleted, data cannot be restored to it.  
        >-   Restoring to an existing DB instance will overwrite data on it and cause the existing DB instance to be unavailable.  
        >-   To restore backup data to an existing DB instance, the selected DB instance must be in the same VPC as the original DB instance and must have the same DB engine and the same or later version than the original DB instance.   
        >-   Ensure that the storage space of the selected existing DB instance is greater than or equal to the storage space of the original DB instance. Otherwise, data will not be restored.  

        Select an existing DB instance and click  **OK**.

        If the automated backup policy is enabled, a full backup will be triggered after the restoration is complete. Otherwise, the full backup will not be triggered.

6.  View the restoration result. The result depends on which restoration method was selected:
    -   Create New Instance

        A new DB instance is created using the backup data. The status of the DB instance changes from  **Creating**  to  **Available**.

        The new DB instance is independent from the original one. If you need read replicas to offload read pressure, create one or more for the new DB instance.

        After the new instance is created, the system will perform a full backup.

    -   Restore to Original

        On the  **Instance Management**  page, the status of the original DB instance changes from  **Restoring**  to  **Available**. If the original DB instance contains read replicas, the read replica status is the same as the original DB instance status.

        If the automated backup policy is enabled, a full backup will be triggered after the restoration is complete. Otherwise, the full backup will not be triggered.

    -   Restore to Existing

        On the  **Instance Management**  page, the status of the target existing DB instance changes from  **Restoring**  to  **Available**. If the target existing DB instance contains read replicas, the read replica status is the same as the target existing DB instance status.

        If the automated backup policy is enabled, a full backup will be triggered after the restoration is complete. Otherwise, the full backup will not be triggered.



