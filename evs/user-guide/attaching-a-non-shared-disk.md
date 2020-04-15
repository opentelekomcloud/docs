# Attaching a Non-Shared Disk<a name="evs_01_0036"></a>

## Scenarios<a name="section31341812202528"></a>

Independently created EVS disks are data disks. In the disk list, the function of such disks is displayed as  **Data disk**, and the status is displayed as  **Available**. In this case, you need to attach the data disks to servers for use.

A system disk must be created during a server creation and is automatically attached. In the disk list, the function of such disks is displayed as  **System disk**, and the status is displayed as  **In-use**. After a system disk is detached from a server, the disk function changes to  **Bootable disk**, and the status changes to  **Available**.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Bootable disks are the system disks detached from servers. A bootable disk can be re-attached to a server and be used as system disk or data disk depending on the device name selected.  

This topic describes how to attach a non-shared EVS disk to a server. A non-shared EVS disk can be attached to only one server.

## Procedure<a name="section47232828202528"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Storage**, click  **Elastic Volume Service**.

    The disk list page is displayed.

4.  Locate the target disk in the list and click  **Attach**.

    The  **Attach Disk**  dialog box is displayed, as shown in  [Figure 1](#fig15846164615421).

    **Figure  1**  Attach Disk dialog box<a name="fig15846164615421"></a>  
    ![](figures/attach-disk-dialog-box.png "attach-disk-dialog-box")

5.  Select the server and then select a device name from the drop-down list. Ensure that the EVS disk and server are in the same AZ.
6.  Click  **OK**  to return to the disk list page. The status of the disk is  **Attaching**, indicating that the disk is being attached to the server. When the disk status changes to  **In-use**, the disk is successfully attached.
7.  Initialize the EVS disk.

    After the disk has been attached to a server, the disk can be used only after you have initialized it. For details, see  [Introduction to Data Disk Initialization Scenarios and Partition Styles](introduction-to-data-disk-initialization-scenarios-and-partition-styles.md).


