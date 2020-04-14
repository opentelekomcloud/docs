# Attaching Data Disks<a name="EN-US_TOPIC_0102427987"></a>

## Scenarios<a name="section10846155702217"></a>

If the existing disks of a BMS fail to meet service requirements, for example, due to insufficient disk space or poor disk performance, you can attach more available disks to the BMS, or create more disks and attach them to the BMS.

## Prerequisites<a name="section1097071251915"></a>

Disks are available.

For details about how to create disks, see "Creating an EVS Disk" in  _Elastic Volume Service User Guide___.

## Procedure<a name="section52421843111514"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.
3.  In the upper right corner of the BMS list, enter the name, private IP address, ID, or flavor of a BMS and click  ![](figures/search-icon.png)  to search for the desired BMS.
4.  Click the name of the target BMS.

    The page showing details of the BMS is displayed.

5.  Click the  **Disks**  tab. Then, click  **Attach Disk**.

    The  **Attach Disk**  dialog box is displayed.

6.  Select the disk type and target disk, and set the mount point as prompted.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If no EVS disks are available, click  **Create Disk**  in the lower part of the list.  
    >For the restrictions on attaching disks, see  [What Are the Restrictions for Attaching a Disk to a BMS?](what-are-the-restrictions-for-attaching-a-disk-to-a-bms.md)  

7.  Click  **OK**.

    After the disk is attached, you can view the information about it on the  **Disks**  tab.


## Follow-up Operations<a name="section17992207183914"></a>

If the attached disk is newly created, the disk can be used only after it is initialized \(formatted\). For details about how to initialize data disks, see  [Initializing Data Disks](introduction-to-data-disk-initialization-scenarios-and-partition-styles.md).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>After the BMS is restarted, the drive letter of the EVS disk may change. For the mapping between the EVS disk device and drive letter, see  [How Do I Obtain the Drive Letter of an EVS Disk?](how-do-i-obtain-the-drive-letter-of-an-evs-disk.md)  

