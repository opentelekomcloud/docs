# VBS Operation Instances<a name="EN-US_TOPIC_0033871603"></a>

This section explains how to use VBS to ensure data security in different scenarios, its limitations, and its typical operations.

## Scenarios<a name="section3694475715447"></a>

VBS applies to the following scenarios:

-   Hardware faults

    Production storage devices on the cloud platform have faults.

-   Software faults

    System faults cause data losses \(for example, the system malfunctions and the system incorrectly delivers resource deletion commands\) and application system faults on a user's guest OSs.

-   User misoperations

    User misoperations cause data loss and system bootup failures.


## Requirements and Limitations<a name="section3336760215143"></a>

-   EVS disks cannot be restored in a batch.
-   If you use data backups to create an EVS disk, the new EVS disk cannot be used as a system disk.

## EVS Disk Data Backup<a name="section46623325151518"></a>

VBS works only on EVS disks. For details, see  [Creating a VBS Backup](creating-a-vbs-backup.md).

## EVS Disk Data Restoration<a name="section2060996152453"></a>

You can use a VBS backup to restore an EVS disk to the time when the backup was created.

Before restoring the disk data, stop the server to which the EVS disk is attached and detach the EVS disk from the server. After the restoration is complete, re-attach the EVS disk and start the server. For details, see  [Data Restoration Using a VBS Backup](data-restoration-using-a-vbs-backup.md).

## Create an EVS Disk Using a VBS Backup<a name="section2522598415452"></a>

After an EVS disk is created using a data backup, the initial data of the new EVS disk is the same as the initial backup data. For details, see  [Create an EVS Disk Using a VBS Backup](data-restoration-using-a-vbs-backup.md#section44845024152024).

