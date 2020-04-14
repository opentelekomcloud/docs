# What Are Full Backup and Incremental Backup?<a name="EN-US_TOPIC_0102012341"></a>

After an initial full backup, an ECS continues to be backed up incrementally by default.

-   A full backup backs up the used capacity, that is, all data in the disk. For example, if a 100 GB disk is allocated with 40 GB data, the backup storage space occupies 40 GB, and the backup size is 40 GB.
-   A subsequent incremental backup backs up data changed since the last backup. If 5 GB data changed since the last backup, only the 5 GB changed data will be backed up.

CSBS allows you to use any backup \(no matter it is a full or incremental one\) to restore the whole data of an ECS. By virtue of this, manual or automatic deletion of a backup will not affect the restoration function.

Suppose ECS  **X**  has backups  **A**,  **B**, and  **C**  \(in time sequence\) and every backup involves data changes. If backup  **B**  is deleted, you can still use backup  **A**  or  **C**  to restore data.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>In extreme cases, the size of a backup is the same as the disk size. The used capacity in a full backup and the changed capacity in an incremental backup are calculated based on the data block change in a disk, not by calculating the file change in the operating system. The size of a full backup cannot be evaluated based on the file capacity in the operating system, and the size of an incremental backup cannot be evaluated based on the file size change.  

