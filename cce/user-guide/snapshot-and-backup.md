# Snapshot and backup<a name="cce_01_0211"></a>

CCE works with EVS to provide the snapshot function. A snapshot is a complete copy or image of EVS disk data at a certain point of time, which is of great help to data DR.

You can create snapshots to rapidly save the disk data at specified time points. In addition, you can use snapshots to create new disks so that the created disks will contain the snapshot data in the beginning.

## Notes<a name="section113181948104715"></a>

-   The snapshot function is available only for clusters of v1.15 or later and requires the CSI-based  [everest \(System Resource Add-on, Mandatory\)](everest-(system-resource-add-on-mandatory).md).
-   The subtype \(common I/O, high I/O, or ultra-high I/O\), disk mode \(SCSI or VBD\), data encryption, sharing status, and capacity of an EVS disk created from a snapshot must be the same as those of the disk associated with the snapshot. These attributes cannot be modified after being queried or set.

## Application Scenario<a name="section54641247195218"></a>

The snapshot feature helps address your following needs:

-   **Routine data backup**

    You can create snapshots for EVS disks regularly and use snapshots to recover your data in case that data loss or data inconsistency occurred due to misoperations, viruses, or attacks.

-   **Rapid data restoration**

    You can create a snapshot or multiple snapshots before an OS change, application software upgrade, or a service data migration. If an exception occurs during the upgrade or migration, service data can be rapidly restored to the time point when the snapshot was created.

    For example, a fault occurred on system disk A of ECS A, and therefore ECS A cannot be started. Because system disk A is already faulty, the data on system disk A cannot be restored by rolling back snapshots. In this case, you can use an existing snapshot of system disk A to create EVS disk B and attach it to ECS B that is running properly. Then, ECS B can read data from system disk A using EVS disk B.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The snapshot capability provided by CCE is the same as the CSI snapshot function provided by the Kubernetes community. EVS disks can be created only based on snapshots, and snapshots cannot be rolled back to source EVS disks.  

-   **Rapid deployment of multiple services**

    You can use a snapshot to create multiple EVS disks containing the same initial data, and these disks can be used as data resources for various services, for example, data mining, report query, and development and testing. This method protects the initial data and creates disks rapidly, meeting the diversified service data requirements.


## Operation Overview<a name="section1337153534815"></a>

1.  You can  [create a snapshot](#section106169536555)  to rapidly save the disk data at specified time points.
2.  You can  [create an EVS disk from a snapshot](#section9617195365510)  so that the EVS disk contains the snapshot data in the beginning. When data is lost, the snapshot can be used to restore the data to point in time when the snapshot was taken.
3.  When a snapshot is no longer needed,  [delete it](#section20618135335519)  to release the virtual resources.

## Creating a Snapshot<a name="section106169536555"></a>

You can create EVS snapshots to save the disk data at specific time points.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>**Snapshots can be created only for EVS disks that are available or in use.**  A maximum of seven snapshots can be created for a single EVS disk. For details about how to create an EVS disk, see  [Using EVS Disks for Storage](using-evs-disks-for-storage.md).  
>Snapshot data of encrypted disks is stored encrypted, and that of non-encrypted disks is stored non-encrypted.  

1.  Log in to the CCE Console. In the navigation pane on the left, choose  **Resource Management**  \>  **Storage**.
2.  On the  **Snapshot and backup**  tab page, click  **Create Snapshot**.
3.  On the  **Create Snapshot**  page displayed, configure parameters listed in  [Table 1](#table195712416594).

    **Table  1**  Parameters for creating a snapshot

    <a name="table195712416594"></a>
    <table><thead align="left"><tr id="row95724185917"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.3.1.1"><p id="p105744115910"><a name="p105744115910"></a><a name="p105744115910"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="74%" id="mcps1.2.3.1.2"><p id="p1857194185919"><a name="p1857194185919"></a><a name="p1857194185919"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1657144115592"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p85719414598"><a name="p85719414598"></a><a name="p85719414598"></a>Snapshot Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p55718418591"><a name="p55718418591"></a><a name="p55718418591"></a>Name of the snapshot to be created. The name starts with <strong id="b91071630172017"><a name="b91071630172017"></a><a name="b91071630172017"></a>cce-disksnap-</strong> by default, for example, <strong id="b191679438222"><a name="b191679438222"></a><a name="b191679438222"></a>cce-disksnap-01</strong>.</p>
    </td>
    </tr>
    <tr id="row1557341165911"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p1957114125916"><a name="p1957114125916"></a><a name="p1957114125916"></a>Cluster Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p165784195917"><a name="p165784195917"></a><a name="p165784195917"></a>Cluster where the snapshot is deployed.</p>
    </td>
    </tr>
    <tr id="row18574414594"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p757241185913"><a name="p757241185913"></a><a name="p757241185913"></a>Namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p55784195910"><a name="p55784195910"></a><a name="p55784195910"></a>Namespace with which the snapshot is associated.</p>
    </td>
    </tr>
    <tr id="row1457124155912"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p105764115595"><a name="p105764115595"></a><a name="p105764115595"></a>Select Storage</p>
    </td>
    <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p05774112594"><a name="p05774112594"></a><a name="p05774112594"></a>Select the EVS disk for which the snapshot is to be created.</p>
    <p id="p85724113595"><a name="p85724113595"></a><a name="p85724113595"></a>The disk must be available or in use. For details about how to create a disk, see <a href="using-evs-disks-for-storage.md">Using EVS Disks for Storage</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **Create**.
5.  Click  **Back to Snapshot List**. When the snapshot status changes to Normal, the snapshot is successfully created.

    Click  ![](figures/icon-up.png)  on the left of the snapshot name to view the snapshot status and details.


## Creating a Disk from a Snapshot<a name="section9617195365510"></a>

On the snapshot list page, you can select a snapshot to create an EVS disk.

In this mode, pay attention to the following constraints:

-   The disk type, disk mode, and encryption setting of the created disk are consistent with those of the snapshot's source EVS disk.
-   A snapshot can be used to create a maximum of 128 EVS disks.
-   Batch disk creation is not supported, and the quantity parameter must be set to  **1**.

1.  Log in to the CCE Console. In the navigation pane on the left, choose  **Resource Management**  \>  **Storage**.
2.  Click the  **Snapshot and backup**  tab. In the snapshot list, locate the target snapshot and click  **Create Data Volume**  in the  **Operation**  column.
3.  Set the parameters of the EVS disk. For details, see  [Using EVS Disks for Storage](using-evs-disks-for-storage.md).

    When you use a snapshot to create an EVS disk, the capacity must be greater than or equal to the snapshot size. In the condition that you do not specify the disk capacity, if the snapshot size is smaller than 10 GB, the default capacity 10 GB will be used as the disk capacity; if the snapshot size is greater than 10 GB, the disk capacity will be consistent with the snapshot size.

4.  Click  **Create Now**  and click  **Submit**.
5.  On the page indicating that the task is submitted successfully, click  **Go to Storage**. On the  **EVS**  tab page, view the status of the EVS disk.

    When the EVS disk status changes to  **Available**, the EVS disk is created successfully.


## Deleting a Snapshot<a name="section20618135335519"></a>

If a snapshot is no longer used, you can release the virtual resources by deleting the snapshot from the system. Snapshot deletion has the following constraints:

-   A snapshot can be deleted only when its status is  **Available**  or  **Error**.
-   If an EVS disk is deleted, all the snapshots created for this disk will also be deleted.

1.  Log in to the CCE Console. In the navigation pane on the left, choose  **Resource Management**  \>  **Storage**.
2.  Click the  **Snapshot and backup**  tab. In the snapshot list, locate the target snapshot and click  **Delete**  in the  **Operation**  column.
3.  \(Optional\) If multiple snapshots are to be deleted, select  ![](figures/icon-snapshots.png)  in front of each snapshot and click  **Delete**  in the upper area of the list.
4.  In the dialog box displayed, enter  **DELETE**, and click  **Yes**.

## Reference Documents<a name="section14627184153810"></a>

[Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/#lifecycle-of-a-volume-snapshot-and-volume-snapshot-content)

