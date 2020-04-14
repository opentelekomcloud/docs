# Overview<a name="EN-US_TOPIC_0237964729"></a>

## Need for DCS Instance Backup<a name="section11170862"></a>

There is a small chance that dirty data could exist in a DCS instance owing to service system exceptions or problems in loading data from persistence files. In addition, some systems demand not only high reliability but also data security, data restoration, and even permanent data storage.

Currently, data in DCS instances can be backed up to OBS. If a DCS instance becomes faulty, data in the instance can be restored from backup so that service continuity is not affected.

## Backup Modes<a name="section33428900"></a>

DCS instances support the following backup modes:

-   Scheduled backup

    You can create a scheduled backup policy on the DCS console. Then, data in the chosen DCS instances will be automatically backed up at the scheduled time.

    You can choose the days of the week on which scheduled backup will run. Backup data will be retained for a maximum of seven days. Backup data older than seven days will be automatically deleted.

    The primary purpose of scheduled backups is to create complete data replicas of DCS instances so that the instance can be quickly restored if necessary.

-   Manual backup

    Backup requests can also be issued manually. Then, data in the chosen DCS instances will be permanently backed up to OBS. Backup data can be deleted manually.

    Before performing high-risk operations, such as system maintenance or upgrade, DCS instance data needs to be backed up.


## Additional Information About Data Backup<a name="section32424647"></a>

-   Instance type

    Currently, only master/standby and cluster DCS instances can be backed up and restored. Single-node DCS instances do not support backup or restoration.

-   Working principle

    Instance data is persisted using the Redis Append Only Files \(AOF\) feature.

    Backup tasks are run on standby cache nodes. DCS instance data is backed up by compressing and storing the data persistence files from the standby cache node to OBS.

    DCS checks instance backup policies once an hour. If a backup policy is matched, DCS runs a backup task for the corresponding DCS instance.

-   Impact on DCS instances during backup

    DCS instances can continue to provide services during backup.

    In the event of full-data synchronization or heavy instance load, it takes a few minutes to complete data synchronization. If instance backup starts before data synchronization is complete, the backup data will be slightly behind the data in the master cache node.

    During instance backup, the standby cache node stops persisting the latest changes to disk files. If new data is written to the master cache node during backup, the backup file will not contain the new data.

-   Backup time

    It is advisable to back up instance data during off-peak periods.

-   Storage and pricing of backup files

    Backup files are stored to OBS.

    DCS provides the backup service free of charge, but OBS charges will be incurred for the amount and period that storage space is consumed.

-   Handling exceptions in scheduled backup

    If a scheduled backup task is triggered while the DCS instance is restarting or being scaled up, the scheduled backup task will be run in the next cycle.

    If backing up a DCS instance fails or the backup is postponed because another task is in progress, DCS will try to back up the instance in the next cycle. A maximum of three retries are allowed within a single day.

-   Retention period of backup data

    Scheduled backup files are retained for up to seven days. The retention period is user configurable. At the end of the retention period, most backup files of the DCS instance will be automatically deleted, but at least one backup file will be retained.

    Manual backup files are retained permanently and need to be manually deleted.


## Data Restoration<a name="section23386368"></a>

-   Data restoration process
    1.  A user initiates a data restoration request using the DCS console.
    2.  DCS obtains the backup file from OBS.
    3.  Read/write to the DCS instance is suspended.
    4.  The original data persistence file of the master cache node is replaced by the backup file.
    5.  The new data persistence file \(that is, the backup file\) is reloaded.
    6.  Data is restored, and the DCS instance starts to provide read/write service again.

-   Impact on service systems

    Data read/write is suspended during instance data restoration and resumed after data in the master cache node is restored.

-   Handling data restoration exceptions

    If a backup file is corrupted, DCS will try to fix the backup file while restoring instance data. If the backup file is successfully fixed, DCS proceeds to restore instance data. If the backup file cannot be fixed, the DCS instance \(if the instance type is master/standby\) or the cache node with an unrepairable backup file \(if the instance type is cluster\) will be restored to the state in which it was before data restoration.


