# Detaching a Disk<a name="EN-US_TOPIC_0102427988"></a>

## Scenarios<a name="section1646133262316"></a>

A disk attached to a BMS can be detached.

-   A disk mounted to  **/dev/sda**  functions as the system disk. You can only detach the system disk from a stopped BMS.
-   Disks mounted to a mount point other than  **/dev/sda**  function as data disks and can be detached from a running or stopped BMS.

## Restrictions and Limitations<a name="section1433771213718"></a>

-   Detaching the system disk is a mission-critical operation. A BMS without the system disk cannot start. Exercise caution when performing this operation.
-   Before detaching a data disk from a running Windows BMS, ensure that no program is reading data from or writing data to the disk. Otherwise, data will be lost.

-   Before detaching a data disk from a running Linux BMS, you must log in to the BMS and run the  **umount**  command to cancel the association between the disk and the file system. In addition, ensure that no program is reading data from or writing data to the disk. Otherwise, detaching the disk will fail.

## Procedure<a name="section188901751214"></a>

1.  Log in to the management console. 
2.  Under  **Computing**, click  **Bare Metal Server**.
3.  Click the name of the BMS from which the disk is to be detached. The page showing details of the BMS is displayed.
4.  Click the  **Disks**  tab. Locate the row containing the disk to be detached and click  **Detach**.

