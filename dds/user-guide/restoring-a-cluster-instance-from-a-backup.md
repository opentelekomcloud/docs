# Restoring a Cluster Instance from a Backup<a name="dds_03_0042"></a>

## **Scenarios**<a name="section20967309195347"></a>

This section guides you on how to restore a DB instance from a backup.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Currently, DDS only supports restoring backups to a new DB instance.  

## Method 1<a name="section5636963115314"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target cluster instance.
3.  In the navigation pane on the left, click  **Backups & Restorations**.
4.  On the  **Backups & Restorations**  page, locate the target backup in the backup list and click  **Restore**  in the  **Operation**  column. In the displayed dialog box, click  **OK**. 
5.  On the displayed page, create a DB instance using the same configurations as the backup. The new DB instance is independent from the original one.
    -   You are recommended to deploy the restored DB instance in a different AZ to ensure that applications will not be adversely affected by the failure in any single AZ, improving data reliability.
    -   The database type, DB instance type, compatible MongoDB version, storage engine, storage type, and shard quantity must be the same as those of the original and cannot be changed.
    -   The quantity of mongos is 2 by default and ranges from 2 to 12. You can specify the quantity.
    -   The storage space is the same as that of the original instance by default. You can only increase the storage space.
    -   Other settings are the same as those of the original DB instance by default and can be modified. For details, see section  [Creating a Cluster Instance](creating-a-cluster-instance.md).


## Method 2<a name="section33115794114910"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  In the navigation pane on the left, click  **Backup Management**.
3.  On the  **Backup Management**  page, locate the backup to restore on the  **Clusters**  tab and click  **Restore**  in the  **Operation**  column. In the displayed dialog box, click  **OK**.
4.  On the displayed page, create a DB instance using the same configurations as the backup. The new DB instance is independent from the original one.
    -   You are recommended to deploy the restored DB instance in a different AZ to ensure that applications will not be adversely affected by the failure in any single AZ, improving data reliability.
    -   The database type, DB instance type, compatible MongoDB version, storage engine, storage type, and shard quantity must be the same as those of the original and cannot be changed.
    -   The quantity of mongos is 2 by default and ranges from 2 to 12. You can specify the quantity.
    -   The storage space is the same as that of the original instance by default. You can only increase the storage space.
    -   Other settings are the same as those of the original DB instance by default and can be modified. For details, see section  [Creating a Cluster Instance](creating-a-cluster-instance.md).


