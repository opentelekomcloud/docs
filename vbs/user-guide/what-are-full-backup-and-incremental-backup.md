# What Are Full Backup and Incremental Backup?<a name="EN-US_TOPIC_0126537915"></a>

After an initial full backup, an ECS continues to be backed up incrementally by default.

-   The initial full backup covers data on every disk of the ECS. If a 100 GB disk contains 40 GB data, the initial backup consumes 40 GB backup space.
-   Subsequent incremental backup backs up data changed since the last backup. If 5 GB data changed since the last backup, only the 5 GB changed data will be backed up.

VBS allows you to use any backup \(no matter it is a full or incremental one\) to restore the data of the entire EVS disk. By virtue of this, manual or automatic deletion of a backup will not affect the restoration function.

Suppose EVS disk  **X**  has backups  **A**,  **B**, and  **C**  \(in time sequence\) and every backup involves data changes. If backup  **B**  is deleted, you can still use backup  **A**  or  **C**  to restore data.

