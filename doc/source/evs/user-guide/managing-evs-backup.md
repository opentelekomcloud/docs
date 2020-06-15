# Managing EVS Backup<a name="evs_01_0110"></a>

## Scenarios<a name="section20439890153621"></a>

EVS disk backups are created using the VBS service. For details, see  **Creating a VBS Backup**  in the  _Volume Backup Service User Guide_.

This topic describes how to configure a backup policy for disks. With backup policies configured, data on EVS disks can be periodically backed up to improve data security.

## Configuring a Backup Policy<a name="section4076182216216"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Storage**, click  **Elastic Volume Service**.

    The disk list page is displayed.

4.  In the disk list, locate the disk whose data needs to be backed up and choose  **More**  \>  **Configure Backup Policy**  in the  **Operation**  column.

    The  **Configure Backup Policy**  dialog box is displayed.

5.  In the backup policy list, click  **Associate**  to select the target backup policy.

    >![](/images/icon-note.gif) **NOTE:**   
    >If the EVS disk has been associated with a backup policy, you need to disassociate the disk with its backup policy and then associate it with the new policy. For details, see  **Data Backup Using a Backup Policy**  in the  _Volume Backup Service User Guide_.  

6.  \(Optional\) To create a new backup policy, click  **Edit Backup Policy**.

    The  **Volume Backup Service**  page is displayed.

7.  In the displayed  **Associate Backup Policy**  dialog box, click  **Yes**.

    After the association is complete, the system automatically backs up the data on the EVS disk according to the backup policy.


