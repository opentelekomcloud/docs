# What Should I Do If a Linux ECS with a SCSI Disk Attached Fails to Restart?<a name="EN-US_TOPIC_0087382187"></a>

## Symptom<a name="section3414486317516"></a>

For a Linux ECS with a SCSI disk attached, if automatic SCSI disk attaching upon ECS startup is enabled in  **/etc/fstab**  and the disk drive letter \(for example,  **/dev/sdb**\) is used, restarting the ECS may fail.

## Possible Causes<a name="section20153596175411"></a>

SCSI disk allocation is determined based on the ID of the slot accommodating the disk as well as the available drive letter in the ECS. Each time when a disk is attached to the ECS, an idle drive letter is automatically allocated in sequence. When the ECS starts, the disks are loaded in slot sequence. Therefore, a slot ID corresponds to a drive letter.

After the SCSI disk is detached from the running ECS, the slot sequence for disks may be changed, leading to the disk drive letter change after the ECS is restarted. As a result, the slot IDs do not correspond to the drive letters, and restarting the ECS failed.

## Solution<a name="section17730319204351"></a>

1.  Log in to the ECS.
2.  Run the following command to switch to user  **root**:

    **sudo su -**

3.  <a name="li2064141120446"></a>Run the following command to obtain the SCSI ID according to the drive letter of the SCSI disk:

    **ll /dev/disk/by-id/|grep **_Disk drive letter_

    For example, if the drive letter of the SCSI disk is  **/dev/sdb**, run the following command:

    **ll /dev/disk/by-id/|grep sdb**

    ```
    CNA64_22:/opt/galax/eucalyptus/ecs_scripts # ll /dev/disk/by-id/|grep sdb
    lrwxrwxrwx 1 root root  9 Dec  6 11:26 scsi-3688860300001436b005014f890338280 -> ../../sdb
    lrwxrwxrwx 1 root root  9 Dec  6 11:26 wwn-0x688860300001436b005014f890338280 -> ../../sdb
    ```

4.  Change the drive letter \(for example,  **/dev/sdb**\) of the SCSI disk to the corresponding SCSI ID in the  **/etc/fstab**  file.

    **/dev/disk/by-id/**_SCSI ID_

    For example, if the SCSI ID obtained in step  [3](#li2064141120446)  is scsi-3688860300001436b005014f890338280, use the following data to replace  **/dev/sdb**:

    **/dev/disk/by-id/scsi-3688860300001436b005014f890338280**


