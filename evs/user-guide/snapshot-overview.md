# Snapshot Overview<a name="evs_01_0098"></a>

## What Is EVS Snapshot<a name="section1574010163515"></a>

EVS allows you to create snapshots for disks on the management console or by making API calls. An EVS snapshot is a complete copy or image of the disk data at a specific time point. As a major disaster recovery \(DR\) approach, you can use a snapshot to completely restore the data to the time point when the snapshot was created.

EVS snapshots are sometimes referred to as snapshots in this document.

You can create snapshots to rapidly save the disk data at specified time points. In addition, you can use snapshots to create new disks so that the created disks will contain the snapshot data in the beginning.

## Application Scenarios<a name="section18370026103714"></a>

The snapshot function helps address your following needs:

-   Routine data backup

    You can create snapshots for disks on a timely basis and use snapshots to recover your data in case that data loss or data inconsistency occurred due to misoperations, viruses, or attacks.

-   Rapid data restoration

    You can create a snapshot or multiple snapshots before an OS change, application software upgrade, or a service data migration. If an exception occurs during the upgrade or migration, service data can be rapidly restored to the time point when the snapshot was created.

    For example, a fault occurred on system disk A of server A, and therefore server A cannot be started. Because system disk A is already faulty, the data on system disk A cannot be restored by rolling back snapshots. However, you can create disk B using an existing snapshot of system disk A and attach disk B to a properly running server, for example server B. In this case, server B can read the data of system disk A from disk B.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Currently, when rolling back data from snapshots, the snapshot data can be rolled back only to its source EVS disk, and a rollback to another EVS disk is not possible.  

-   Multi-service quick deployment

    You can use a snapshot to create multiple disks containing the same initial data, and these disks can be used as data resources for various services, for example data mining, report query, and development and testing. This method protects the initial data and creates disks rapidly, meeting the diversified service data requirements.


## Operation Overview<a name="section13814103473817"></a>

You can create snapshots according to  [Creating a Snapshot](creating-a-snapshot.md)  to rapidly save the disk data at specified points in time.

If data lost occurs, you may choose to roll back the disk data to the snapshot creation time based on  [Rolling Back Data from a Snapshot](rolling-back-data-from-a-snapshot.md). In addition, you may create a new disk from the snapshot so that the disk will contain the snapshot data in the beginning. For details, see  [Creating an EVS Disk from a Snapshot](creating-an-evs-disk-from-a-snapshot.md).

When a snapshot is no longer needed, delete it according to  [Deleting a Snapshot](deleting-a-snapshot.md)  to release the virtual resources.

