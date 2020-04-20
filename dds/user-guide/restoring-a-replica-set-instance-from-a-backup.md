# Restoring a Replica Set Instance from a Backup<a name="dds_03_0043"></a>

## **Scenarios**<a name="section20967309195347"></a>

This section guides you on how to restore a replica set instance from a backup.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Currently, DDS only supports restoring backups to a new DB instance.  

## Method 1<a name="section5636963115314"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target replica set instance.
3.  In the navigation pane on the left, click  **Backups & Restorations**.
4.  On the  **Backups & Restorations**  page, locate the target backup in the backup list and click  **Restore**  in the  **Operation**  column. In the displayed dialog box, click  **OK**. 
5.  On the displayed page, create a DB instance using the same configurations as the backup. The new DB instance is independent from the original one.
    -   You are recommended to deploy the restored DB instance in a different AZ to ensure that applications will not be adversely affected by the failure in any single AZ, improving data reliability.
    -   The database type, DB instance type, compatible MongoDB version, storage engine, and storage type must be the same as those of the original and cannot be changed.
    -   The storage space is the same as that of the original instance by default. You can only increase the storage space.
    -   Other settings are the same as those of the original DB instance by default and can be modified. For details, see section  [Creating a Replica Set Instance](creating-a-replica-set-instance.md).


## Method 2<a name="section33115794114910"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  In the navigation pane on the left, click  **Backup Management**.
3.  On the  **Backup Management**  page, click the  **Replica Sets**  tab, locate the backup to restore, and click  **Restore**  in the  **Operation**  column. In the displayed dialog box, click  **OK**. 
4.  On the displayed page, create a DB instance using the same configurations as the backup. The new DB instance is independent from the original one.
    -   You are recommended to deploy the restored DB instance in a different AZ to ensure that applications will not be adversely affected by the failure in any single AZ, improving data reliability.
    -   The database type, DB instance type, compatible MongoDB version, storage engine, and storage type must be the same as those of the original and cannot be changed.
    -   The storage space is the same as that of the original instance by default. You can only increase the storage space.
    -   Other settings are the same as those of the original DB instance by default and can be modified. For details, see section  [Creating a Replica Set Instance](creating-a-replica-set-instance.md).


