# Backing Up ECS Data<a name="EN-US_TOPIC_0096304614"></a>

## Scenarios<a name="section5441517105316"></a>

You can back up ECS data using CSBS or VBS.

-   CSBS \(recommended\): Use this backup method if you want to back up the data of all EVS disks \(system and data disks\) on an ECS. This prevents data inconsistency caused by time difference in creating a backup.
-   VBS: Use this backup method if you want to back up the data of one or more EVS disks \(system or data disk\) on an ECS. This minimizes backup costs on the basis of data security.

>![](/images/icon-note.gif) **NOTE:**   
>For Windows ECSs, you can install the Windows Server Backup tool provided by the Windows OS to back up full ECS data. You are advised to use VBS and CSBS provided by the public cloud.  

## CSBS Backup Procedure<a name="section55131850105514"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.

    The  **Elastic Cloud Server**  page is displayed.

4.  In the navigation pane one the left, choose  **Cloud Server Backup Service**.
5.  Click  **Create CSBS Backup**.
6.  Back up the ECS data as prompted.

    For more information, see  _Cloud Server Backup Service User Guide_.


>![](/images/icon-note.gif) **NOTE:**   
>After a CSBS backup is created, you can use it to create an image and use the image to create ECSs in a batch for rapidly restoring the service running environment. To do so, perform the following operations:  
>1.  Create a CSBS backup on the  **Cloud Server Backup Service**  page.  
>2.  Use the CSBS backup to create a private image \(full-ECS image\).  
>3.  Use the full-ECS image to create ECSs in a batch.  
>For more details about how to use CSBS backups to create images, see "Using Backups to Create Images" in  _Cloud Server Backup Service User Guide_  and "Creating a Full-ECS Image Using a CSBS Backup" in  _Image Management Service User Guide_.  

## VBS Backup Procedure<a name="section16144163518523"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.

    The  **Elastic Cloud Server**  page is displayed.

4.  In the navigation pane on the left, choose  **Volume Backup Service**.
5.  Click  **Create VBS Backup**.
6.  Back up data as prompted.

    For more information, see  _Volume Backup Service User Guide_.


