# Resetting the Password for Logging In to a Linux ECS<a name="EN-US_TOPIC_0021427650"></a>

## Scenarios<a name="section17131859112916"></a>

You can reset your ECS password if:

-   The password is forgotten.
-   The password has expired.

## Prerequisites<a name="section35515688202027"></a>

-   A temporary Linux ECS which locates in the same AZ as the target ECS is available.
-   You have bound an EIP to the temporary ECS.

## Procedure<a name="section9546131644416"></a>

1.  Download the script for resetting the password and upload the script to the temporary ECS.
    1.  Log in to the management console and click  **Elastic Cloud Server**  under  **Computing**.
    2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
    3.  Locate the row containing the target ECS, click  **More**  in the  **Operation**  column, and select  **Reset Password**. Then, download the password reset script as prompted.
    4.  Use a connection tool, such as WinSCP, to upload the obtained  **changepasswd.sh**  script to the temporary ECS.

        To download WinSCP, log in at  [https://winscp.net/](https://winscp.net/).

2.  <a name="li19814359584"></a>Stop the original Linux ECS, detach the system disk, and attach the system disk to the temporary ECS.
    1.  Stop the original Linux ECS, switch to the page providing details about the ECS, and click the  **Disks**  tab.

        >![](/images/icon-note.gif) **NOTE:**   
        >Do not forcibly stop the original ECS. Otherwise, password reset may fail.  

    2.  <a name="li5640121684418"></a>Locate the row containing the system disk to be detached and click  **Detach**  to detach the system disk from the ECS.
    3.  On the page providing details about the temporary ECS, click the  **Disks**  tab.
    4.  Click  **Attach Disk**. In the displayed dialog box, select the system disk detached in step  [2.b](#li5640121684418)  and attach it to the temporary ECS.

3.  Log in to the temporary ECS remotely and reset the password.
    1.  Locate the row containing the temporary ECS and click  **Remote Login**  in the  **Operation**  column.
    2.  <a name="li664021617445"></a>Run the following command to view the directory of the system disk detached from the original Linux ECS now attached to the temporary ECS:

        **fdisk -l**

    3.  Run the following commands in the directory where the script is stored to run the script for resetting the password:

        **chmod +x changepasswd.sh**

        **./changepasswd.sh**

        When you run the password reset script, if the system displays a message indicating that there is no command related to logical volume manager \(LVM\), such as the message "no lvs command", install an LVM tool on the temporary ECS. The LVM2 tool is recommended, which can be installed by running the  **yum install lvm2**  command.

        >![](/images/icon-notice.gif) **NOTICE:**   
        >If the original ECS and the temporary ECS both run CentOS 7, a mount failure may occur during script execution. To resolve this issue, replace  **mount $dev $mountPath**  with  **mount -o nouuid $dev $mountPath**  in the script.  

    4.  Enter the new password and the directory obtained in step  [3.b](#li664021617445)  as prompted.

        If the following information is displayed, the password has been changed:

        ```
        set password success.
        ```

4.  Stop the temporary ECS, detach the system disk, attach the system disk to the original Linux ECS, and restart the original Linux ECS.
    1.  Stop the temporary ECS, switch to the page providing details about the ECS, and click the  **Disks**  tab.
    2.  <a name="li964031614447"></a>Click  **Detach**  to detach the data disk attached in step  [2](#li19814359584).
    3.  On the page providing details about the original Linux ECS, click the  **Disks**  tab.
    4.  Click  **Attach Disk**. In the displayed dialog box, select the data disk detached in step  [4.b](#li964031614447)  and device name  **/dev/sda**.
    5.  Restart the original Linux ECS.


