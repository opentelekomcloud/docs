# Deleting an EVS Disk<a name="evs_01_0005"></a>

## Scenarios<a name="section6567565617247"></a>

If an EVS disk is no longer used, you can release the virtual resources by deleting the disk from the system. 

-   Before deleting a disk, ensure that the disk status is  **Available**,  **Error**,  **Expansion failed**,  **Restoration failed**, or  **Rollback failed**.
-   Before deleting a shared disk, ensure that the disk has been detached from all its servers.

>![](/images/icon-notice.gif) **NOTICE:**   
>-   When you delete a disk, all the disk data including the snapshots created for this disk will be deleted. Exercise caution when performing this operation.  
>-   A deleted disk cannot be restored.  

## Procedure<a name="section29417758172419"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Storage**, click  **Elastic Volume Service**.

    The disk list page is displayed.

4.  In the disk list, locate the row that contains the target disk, click  **More**  in the  **Operation**  column, and choose  **Delete**.
5.  \(Optional\) If multiple disks are to be deleted, select  ![](figures/icon-select.png)  in front of each disk and click  **Delete**  in the upper area of the list.
6.  In the displayed dialog box, confirm the information and click  **Yes**.

