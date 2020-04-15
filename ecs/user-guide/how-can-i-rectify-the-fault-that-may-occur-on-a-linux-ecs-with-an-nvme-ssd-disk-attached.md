# How Can I Rectify the Fault That May Occur on a Linux ECS with an NVMe SSD Disk Attached?<a name="EN-US_TOPIC_0087622835"></a>

## Symptom<a name="section46022920143319"></a>

When a Linux ECS with an NVMe SSD disk attached, such as a P1 ECS, becomes faulty, you must contact the administrator to remotely create the ECS again for reconstruction.

If automatic NVMe SSD disk attaching upon ECS startup is enabled in  **/etc/fstab**  on the faulty ECS, the system disk recovers after the ECS is created. However, the attached NVMe SSD disk does not have a file system, and automatic NVMe SSD disk attaching upon ECS startup fails to take effect. As a result, the ECS enters the emergency mode.

**Figure  1**  Emergency mode<a name="fig13243412145029"></a>  
![](figures/emergency-mode.jpg "emergency-mode")

To ensure that the new ECS is functional, you must manually delete the attaching information in  **/etc/fstab**.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the NVMe SSD disk is faulty, data on it will be lost. The operations provided in this section are only used to restore automatic NVMe SSD disk attachment to an ECS, but not restoring the data on the disk.  

## Solution<a name="section17298926143433"></a>

1.  Log in to the ECS.
2.  Enter the password of user  **root**  to log in to the ECS.

    **Figure  2**  Logging in to the ECS<a name="fig14351155425213"></a>  
    ![](figures/logging-in-to-the-ecs.jpg "logging-in-to-the-ecs")

3.  Run the following command to edit the  **/etc/fstab**  file:

    **vi /etc/fstab**

4.  Delete the attaching information of the NVMe SSD disk and save the file.

    **Figure  3**  Deleting the automatic attaching information<a name="fig6022199715759"></a>  
    ![](figures/deleting-the-automatic-attaching-information.jpg "deleting-the-automatic-attaching-information")

5.  Run the following command to restart the ECS:

    **reboot**

6.  Verify that the ECS recovers and can be logged in.

    **Figure  4**  Logging in to the ECS<a name="fig42664483151146"></a>  
    ![](figures/logging-in-to-the-ecs-20.jpg "logging-in-to-the-ecs-20")


