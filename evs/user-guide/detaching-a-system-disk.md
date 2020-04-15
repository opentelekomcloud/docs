# Detaching a System Disk<a name="evs_01_0003"></a>

## Scenarios<a name="section21771672164455"></a>

A system disk can only be detached offline, that is, its server must be in the  **Stopped**  state before the system disk is detached. Therefore, you need to first stop the server and then detach the system disk.

For the system disk attached to a server, the disk function is displayed as  **System disk**, and the disk status is displayed as  **In-use**  in the disk list. After a system disk is detached from the server, the disk function changes to  **Bootable disk**, and the status changes to  **Available**.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Bootable disks are the system disks detached from servers. A bootable disk can be re-attached to a server and be used as a system disk or data disk depending on the device name selected.  

## Procedure<a name="section58976207172837"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.

    The  **Elastic Cloud Server**  page is displayed.

4.  In the server list, locate the row that contains the server whose system disk is to be detached, click  **More**  in the  **Operation**  column, and choose  **Stop**.

    When the server status changes to  **Stopped**, the server has been stopped.

5.  Click the name of this server.

    The server details page is displayed.

6.  Click the  **Disks**  tab to view the system disk attached to the server.
7.  Locate the row that contains the system disk and click  **Detach**.

    The  **Detach Disk**  dialog box is displayed, as shown in  [Figure 1](#fig13846812115521).

    **Figure  1**  Detach Disk \(system disk\)<a name="fig13846812115521"></a>  
    ![](figures/detach-disk-(system-disk).png "detach-disk-(system-disk)")

8.  Click  **Yes**  to detach the disk.

    After the operation had succeeded, the detached system disk is no longer displayed under the  **Disks**  tab.


## Related Operations<a name="section1980071942010"></a>

For more detachment FAQs, see  [Disk Detachment FAQs](disk-detachment-faqs.md).

