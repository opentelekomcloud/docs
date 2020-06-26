# EVS Snapshot<a name="en-us_topic_0066809008"></a>

## What Is EVS Snapshot<a name="section16961952104231"></a>

EVS allows you to create snapshots for disks on the management console or by making API calls. An EVS snapshot is a complete copy or image of the disk data at a specific time point. As a major disaster recovery \(DR\) approach, you can use a snapshot to completely restore the data to the time point when the snapshot was created.

EVS snapshots are sometimes referred to as snapshots in this document.

You can create snapshots to rapidly save the disk data at specified time points. In addition, you can use snapshots to create new disks so that the created disks will contain the snapshot data in the beginning.

## Differences Between Snapshots and Backups<a name="section1236302010432"></a>

-   Both snapshots and backups are key approaches for data disaster recovery, but they use different storage plans.
    -   The snapshot data is stored with the disk data so that you can rapidly back up and restore the disk data using snapshots.
    -   The backup data is stored in the Object Storage Service \(OBS\). If the disk data is damaged, you can restore the data using backups.

-   EVS snapshot does not support automatic creation, whereas backup does. You can set a backup policy, and the system will automatically back up the disk data according to this policy.

## Application Scenarios<a name="section8885956105220"></a>

The snapshot function helps address your following needs:

-   Routine data backup

    You can create snapshots for disks on a timely basis and use snapshots to recover your data in case that data loss or data inconsistency occurred due to misoperations, viruses, or attacks.

-   Rapid data restoration

    You can create a snapshot or multiple snapshots before an OS change, application software upgrade, or a service data migration. If an exception occurs during the upgrade or migration, service data can be rapidly restored to the time point when the snapshot was created.

    For example, a fault occurred on system disk A of server A, and therefore server A cannot be started. Because system disk A is already faulty, the data on system disk A cannot be restored by rolling back snapshots. However, you can create disk B using an existing snapshot of system disk A and attach disk B to a properly running server, for example server B. In this case, server B can read the data of system disk A from disk B.

    >![](/images/icon-note.gif) **NOTE:**   
    >Currently, when rolling back data from snapshots, the snapshot data can be rolled back only to its source EVS disk, and a rollback to another EVS disk is not possible.  

-   Multi-service quick deployment

    You can use a snapshot to create multiple disks containing the same initial data, and these disks can be used as data resources for various services, for example data mining, report query, and development and testing. This method protects the initial data and creates disks rapidly, meeting the diversified service data requirements.


## Usage Instructions<a name="section27269138163743"></a>

For details about the snapshot usages, see  [Managing Snapshots](managing_snapshots).

