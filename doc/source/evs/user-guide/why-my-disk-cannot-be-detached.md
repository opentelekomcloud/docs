# Why My Disk Cannot Be Detached?<a name="evs_faq_0056"></a>

EVS disks can be used as system disks or data disks. The method of detaching a system disk is different from detaching a data disk.

-   System disk detachment: A system disk can only be detached offline. You must first stop the server that uses this system disk and then detach the disk.

    >![](/images/icon-note.gif) **NOTE:**   
    >In Linux, a system disk is mounted on  **/dev/vda**. In Windows, a system disk is  **Volume \(C:\)**.  

-   Data disk detachment: A data disk can be detached online or offline.

    >![](/images/icon-note.gif) **NOTE:**   
    >In Linux, a data disk is mounted on a mount point other than  **/dev/vda**. In Windows, a data disk is a volume other than  **Volume \(C:\)**.  

    -   Offline detachment: The server must be in the  **Stopped**  state. If not, stop the server and then detach the data disk.
    -   Online detachment: Some OSs support online detachment. In this case, you do not need to stop the server before detaching the data disk. For more information, see  **Storage**  \>  **Detaching an EVS Disk from a Running ECS**  in the  _Elastic Cloud Server___ _User Guide_.


