# Resetting the Password for Logging In to a Windows ECS<a name="EN-US_TOPIC_0021426802"></a>

## Scenarios<a name="section17131859112916"></a>

You can reset your ECS password if:

-   The password is forgotten.
-   The password has expired.

## Prerequisites<a name="section1344819634213"></a>

-   A temporary Linux ECS which runs Ubuntu 14.04 or later and locates in the same AZ as the target ECS is available.
-   You have bound an EIP to the temporary ECS and configured the apt-get source.
-   You have used either of the following methods to install  **ntfs-3g**  and  **chntpw**  software packages on the temporary ECS:

    Method 1:

    Run the following command to install the  **ntfs-3g**  and  **chntpw**  software packages:

    **sudo apt-get install ntfs-3g chntpw**

    Method 2:

    Download the desired  **ntfs-3g**  and  **chntpw**  software packages according to the temporary ECS OS. For detailed installation and use guide, see the  [NTFS official website](http://www.tuxera.com/community/open-source-ntfs-3g/)  and  [chntpw official website](http://www.chntpw.com/reset-windows-7-admin-password-with-ubuntu/).

    Log in at  [www.tuxera.com/community/open-source-ntfs-3g/](http://www.tuxera.com/community/open-source-ntfs-3g/)  to obtain the  **ntfs-3g**  software package. 

    Log in at  [https://pkgs.org/download/chntpw](https://pkgs.org/download/chntpw)  to obtain the  **chntpw**  software package.


## Procedure<a name="section1052621215437"></a>

1.  Stop the original ECS, detach the system disk from it, and attach the system disk to the temporary ECS.
    1.  Log in to the management console.
    2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
    3.  Under  **Computing**, click  **Elastic Cloud Server**.
    4.  Stop the original Windows ECS, switch to the page providing details about the ECS, and click the  **Disks**  tab.

        >![](/images/icon-note.gif) **NOTE:**   
        >Do not forcibly stop the Windows ECS. Otherwise, password reset may fail.  

    5.  <a name="li49674320202157"></a>Locate the row containing the system disk and click  **Detach**  to detach the system disk from the ECS.
    6.  On the page providing details about the temporary ECS, click the  **Disks**  tab.
    7.  <a name="li32570973202157"></a>Click  **Attach Disk**. In the displayed dialog box, select the system disk detached in step  [1.e](#li49674320202157)  and attach it to the temporary ECS.

2.  Log in to the temporary ECS remotely and attach the system disk.
    1.  <a name="li20334892202157"></a>Run the following command to view the directory of the system disk detached from the original Windows ECS now attached to the temporary ECS:

        **fdisk -l**

    2.  Run the following command to mount the file system of the detached system disk to the temporary ECS:

        **mount -t ntfs-3g /dev/**_Result obtained in step  [2.a](#li20334892202157)_ **/mnt/**

        For example, if the result obtained in step  [2.a](#li20334892202157)  is  **xvde2**, run the following command:

        **mount -t ntfs-3g /dev/xvde2 /mnt/**

        If the following error information is displayed after the preceding command is executed, the ntfs file systems may be inconsistent. In such an event, rectify the file system inconsistency.

        ```
        The disk contains an unclean file system (0, 0).
        Metadata kept in Windows cache, refused to mount.
        Failed to mount '/dev/xvde2': Operation not permitted
        The NTFS partition is in an unsafe state. Please resume and shutdown
        Windows fully (no hibernation or fast restarting), or mount the volume
        read-only with the 'ro' mount option.
        ```

        Back up the disk data, run the following command to rectify the ntfs file system inconsistency, and attach the system disk:

        **ntfsfix /dev/**_Result obtained in step  [2.a](#li20334892202157)_

        For example, if the result obtained in step  [2.a](#li20334892202157)  is  **xvde2**, run the following command:

        **ntfsfix /dev/xvde2**

3.  Change the password and clear the original password.
    1.  Run the following command to back up the SAM file:

        **cp /mnt/Windows/System32/config/SAM /mnt/Windows/System32/config/SAM.bak**

    2.  Run the following command to change the password of a specified user:

        **chntpw -u** **Administrator /mnt/Windows/System32/config/SAM**

    3.  Enter  **1**,  **q**, and  **y**  as prompted, and press  **Enter**

        The password has been reset if the following information is displayed:

        ```
        Select: [q] > 1
        Password cleared!
        Select: [q] > q
        Hives that have changed:
        #Name
        0<SAM>
        Write hive files? (y/n) [n] : y
        0<SAM> - OK
        ```

4.  Stop the temporary ECS, detach the system disk, and attach the system disk to the original Windows ECS.
    1.  Stop the temporary ECS, switch to the page providing details about the ECS, and click the  **Disks**  tab.
    2.  <a name="li46368402202157"></a>Click  **Detach**  to detach the data disk temporarily attached in step  [1.g](#li32570973202157).
    3.  On the page providing details about the original Windows ECS, click the  **Disks**  tab.
    4.  Click  **Attach Disk**. In the displayed dialog box, select the data disk detached in step  [4.b](#li46368402202157)  and device name  **/dev/sda**.

5.  Start the original Windows ECS and set a new login password.
    1.  Click  **Start**  to start the original Windows ECS. After the status becomes  **Running**, click  **Remote Login**  in the  **Operation**  column.
    2.  Click  **Start**. Enter  **CMD**  in the search box and press  **Enter**.
    3.  Run the following command to change the password \(the new password must meet the requirements described in  [Table 1](#en-us_topic_0021426802_table4381109318958)\):

        **net user Administrator **_New password_

        **Table  1**  Password complexity requirements

        <a name="en-us_topic_0021426802_table4381109318958"></a>
        <table><thead align="left"><tr id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_row925712618958"><th class="cellrowborder" valign="top" width="18.000000000000004%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p1162970218958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p1162970218958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p1162970218958"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="58.910000000000004%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p248177818958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p248177818958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p248177818958"></a>Requirement</p>
        </th>
        <th class="cellrowborder" valign="top" width="23.090000000000003%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6680635518958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6680635518958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6680635518958"></a>Example Value</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_row4260571318958"><td class="cellrowborder" valign="top" width="18.000000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p2851073918958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p2851073918958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p2851073918958"></a>Password</p>
        </td>
        <td class="cellrowborder" valign="top" width="58.910000000000004%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul5961106018958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul5961106018958"></a><ul id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul5961106018958"><li>Consists of 8 characters to 26 characters.</li><li>Contains at least three of the following character types:<a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul24583583181022"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul24583583181022"></a><ul id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_ul24583583181022"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters: $!@%-_=+[]:./^,{}?</li></ul>
        </li><li>Cannot contain the username or the username spelled backwards.</li><li>Cannot contain more than two characters in the same sequence as they appear in the username. (This requirement applies only to Windows ECSs.)</li></ul>
        </td>
        <td class="cellrowborder" valign="top" width="23.090000000000003%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6481855218958"><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6481855218958"></a><a name="en-us_topic_0035643949_en-us_topic_0067909751_en-us_topic_0021426802_p6481855218958"></a>YNbUwp!dUc9MClnv</p>
        <div class="note" id="en-us_topic_0035643949_note18511011891"><a name="en-us_topic_0035643949_note18511011891"></a><a name="en-us_topic_0035643949_note18511011891"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0035643949_p351011796"><a name="en-us_topic_0035643949_p351011796"></a><a name="en-us_topic_0035643949_p351011796"></a>The example password is generated randomly. Do not copy this example password.</p>
        </div></div>
        </td>
        </tr>
        </tbody>
        </table>



