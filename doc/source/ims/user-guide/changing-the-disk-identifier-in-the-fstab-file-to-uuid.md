# Changing the Disk Identifier in the fstab File to UUID<a name="EN-US_TOPIC_0086024961"></a>

## Scenarios<a name="section2074321418513"></a>

When optimizing a Linux private image, you need to change the disk identifier to UUID in the fstab configuration file of the ECS.

## Procedure<a name="section60166277114746"></a>

-   Take CentOS 7.0 for example. Run  **blkid**  to obtain the UUIDs of all partitions. Modify the  **/etc/fstab**  file and use the partition  UUIDs  to configure automatic partition mounting.

1.  Log in to the ECS as user  **root**.
2.  Run the following command to query all types of mounted file systems and device UUIDs:

    **blkid**

    The following information is displayed:

    ```
    /dev/xvda2: UUID="4eb40294-4c6f-4384-bbb6-b8795bbb1130" TYPE="xfs"  
    /dev/xvda1: UUID="2de37c6b-2648-43b4-a4f5-40162154e135" TYPE="swap"
    ```

3.  Run the following command to query the  **fstab**  file:

    **cat /etc/fstab**

    The following information is displayed:

    ```
    [root@CTU1000028010 ~]# cat /etc/fstab  
    /dev/xvda2  /       xfs     defaults    0 0 
    /dev/xvda1  swap    swap    defaults    0 0     
    ```

4.  Check whether the disk identifier in the  **fstab**  file is the device name.
    -   If the disk is represented by UUID, no further operation is required.
    -   If the disk is represented by the device name, go to  [5](#li63646666154817).

5.  <a name="li63646666154817"></a>Run the following command to open the  **fstab**  file:

    **vi /etc/fstab**

6.  Press  **i**  to enter editing mode and change the disk identifier in the  **fstab**  file to UUID.

-   Take CentOS 7.1 for example. Run  **blkid**  to obtain the UUIDs of all partitions. Modify the  **/etc/fstab**  file and use the partition UUIDs to configure automatic partition mounting.

1.  Log in to the ECS as user  **root**.
2.  Run the following command to query all types of mounted file systems and device UUIDs:

    **blkid**

    ```
    /dev/xvda2: UUID="4eb40294-4c6f-4384-bbb6-b8795bbb1130" TYPE="xfs" 
    /dev/xvda1: UUID="2de37c6b-2648-43b4-a4f5-40162154e135" TYPE="swap"
    ```

    Before the change:

    ```
    [root@CTU1000028010 ~]# cat /etc/fstab 
    /dev/xvda2  /       xfs     defaults    0 0
    /dev/xvda1  swap    swap    defaults    0 0
    ```

    After the change:

    ```
    [root@CTU1000028010 ~]# cat /etc/fstab 
    UUID=4eb40294-4c6f-4384-bbb6-b8795bbb1130  /       xfs     defaults    0 0
    UUID=2de37c6b-2648-43b4-a4f5-40162154e135  swap    swap    defaults    0 0
    ```

3.  Press  **Esc**, enter  **:wq**, and press  **Enter**. The system saves the configuration and exits the vi editor.
4.  Run the following command to verify the change:

    **cat /etc/fstab**

    The change is successful if information similar to the following is displayed:

    ```
    [root@CTU1000028010 ~]# cat /etc/fstab  
    UUID=4eb40294-4c6f-4384-bbb6-b8795bbb1130  /       xfs     defaults    0 0 
    UUID=2de37c6b-2648-43b4-a4f5-40162154e135  swap    swap    defaults    0 0     
    ```


