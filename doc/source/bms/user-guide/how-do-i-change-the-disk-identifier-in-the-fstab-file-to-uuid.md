# How Do I Change the Disk Identifier in the fstab file to UUID?<a name="EN-US_TOPIC_0151841134"></a>

## Scenarios<a name="section8777165815715"></a>

After attaching disks to a Linux BMS, you must change the disk identifier in the  **fstab**  file to UUID. Otherwise, you cannot enter the BMS OS or the BMS becomes unavailable due to a mount point disorder after you stop and start the BMS, or restart the BMS.

>![](/images/icon-note.gif) **NOTE:**   
>Universally Unique Identifier \(UUID\) is a 128-bit number used to identify information in computer systems.  

## Procedure<a name="section19667181242113"></a>

This section takes CentOS 7 as an example to describe how to change the disk identifier in the  **fstab**  file to UUID.

1.  Log in to the BMS as user  **root**. Run the  **blkid**  command to query all types of file systems that have been mounted to the BMS and UUIDs of the corresponding devices.

    ```
    /dev/sda2: UUID="4eb40294-4c6f-4384-bbb6-b8795bbb1130" TYPE="xfs"
    /dev/sda1: UUID="2de37c6b-2648-43b4-a4f5-40162154e135" TYPE="swap"
    ```

2.  Run the  **cat /etc/fstab**  command to open the  **fstab**  file.

    ```
    /dev/sda2  /       xfs     defaults    0 0
    /dev/sda1  swap    swap    defaults    0 0
    ```

3.  Check the disk identifier in the  **fstab**  file.
    -   If the disk identifier is UUID, no further action is required.
    -   If the disk identifier is the device name, go to  [4](#li784575352211).

4.  <a name="li784575352211"></a>Run the  **vi /etc/fstab**  command to open the  **fstab**  file, press  **i**  to enter editing mode, and change the disk identifier to UUID.

    ```
    UUID=4eb40294-4c6f-4384-bbb6-b8795bbb1130 /       xfs     defaults    0 0
    UUID=2de37c6b-2648-43b4-a4f5-40162154e135 swap    swap    defaults    0 0
    ```

    Press  **Esc**  and enter  **:wq**  to save and exit the file.


