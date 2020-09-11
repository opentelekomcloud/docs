# Mounting a File System Automatically<a name="sfs_01_0025"></a>

To prevent mounting information loss after a restart of the ECS where a file system is mounted, you can configure the ECS and make the file system automatically be mounted after the ECS restarts.

## Restrictions<a name="section133730912414"></a>

Due to different mechanisms for managing startup items \(service startup sequence\), some ECSs running CentOS may not support the following automatic mounting schemes. In this case, manually mount the file system.

## Procedure \(Linux\)<a name="section38954620214447"></a>

1.  Log in to the ECS as user  **root**.
2.  Run the  **vi /etc/fstab**  command to edit the  **/etc/fstab**  file.

    At the end of the file, add the file system information, for example:

    ```
    example.com:/share-xxx /local_path nfs vers=3,timeo=600,nolock 0 0
    ```

    Replace  _example.com:/share-xxx_  and  _/local\_path_  with actual values. Each record in the  **/etc/fstab**  file corresponds to a mount. Each record has six fields, as described in  [Field Description](#section241009011643).

    >![](/images/icon-notice.gif) **NOTICE:**   
    >For optimal system performance, configure file system information based on the previous example configuration. If needed, you can customize part of mount parameters. However, the customization may affect system performance.  

3.  Press  **Esc**, input  **:wq**, and press  **Enter**  to save and exit.

    After the preceding configurations are complete, the system reads mounting information from the  **/etc/fstab**  file to automatically mount the file system when the ECS restarts.

4.  \(Optional\) Run the following command to view the updated content of the  **/etc/fstab**  file.

    **cat /etc/fstab**

    [Figure 1](#fig1023252822220)  shows the updated file content.

    **Figure  1**  Updated file content<a name="fig1023252822220"></a>  
    ![](figures/updated-file-content.png "updated-file-content")


## Field Description<a name="section241009011643"></a>

[Table 1](#table215511301179)  describes the mount fields.

**Table  1**  Field description

<a name="table215511301179"></a>
<table><thead align="left"><tr id="en-us_topic_0072155931_row1990488511206"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="en-us_topic_0072155931_p168295211206"><a name="en-us_topic_0072155931_p168295211206"></a><a name="en-us_topic_0072155931_p168295211206"></a>Field</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="en-us_topic_0072155931_p210146111206"><a name="en-us_topic_0072155931_p210146111206"></a><a name="en-us_topic_0072155931_p210146111206"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0072155931_row3037087111206"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0072155931_p4412150111206"><a name="en-us_topic_0072155931_p4412150111206"></a><a name="en-us_topic_0072155931_p4412150111206"></a><em id="i4077341814844"><a name="i4077341814844"></a><a name="i4077341814844"></a>example.com:/share-xxx</em></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0072155931_p1707183511206"><a name="en-us_topic_0072155931_p1707183511206"></a><a name="en-us_topic_0072155931_p1707183511206"></a>Mount object, that is, the shared path of the file system to be mounted. Set this parameter to the shared path in the <strong id="b173934555816"><a name="b173934555816"></a><a name="b173934555816"></a>mount</strong> command that is used in <a href="mounting-an-nfs-file-system-to-ecss-(linux).md">Mounting an NFS File System to ECSs (Linux)</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0072155931_row3259701211206"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0072155931_p2311233111206"><a name="en-us_topic_0072155931_p2311233111206"></a><a name="en-us_topic_0072155931_p2311233111206"></a><em id="i272352251490"><a name="i272352251490"></a><a name="i272352251490"></a>/local_path</em></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0072155931_p6015955111206"><a name="en-us_topic_0072155931_p6015955111206"></a><a name="en-us_topic_0072155931_p6015955111206"></a>Mount point, that is, the directory created on the ECS for mounting the file system. Set this parameter to the local path in the <strong id="b1463681911119"><a name="b1463681911119"></a><a name="b1463681911119"></a>mount</strong> command that is used in <a href="mounting-an-nfs-file-system-to-ecss-(linux).md">Mounting an NFS File System to ECSs (Linux)</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0072155931_row2074966211206"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0072155931_p300108911206"><a name="en-us_topic_0072155931_p300108911206"></a><a name="en-us_topic_0072155931_p300108911206"></a>nfs</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0072155931_p4176163611206"><a name="en-us_topic_0072155931_p4176163611206"></a><a name="en-us_topic_0072155931_p4176163611206"></a>Mount type, that is, file system or partition type. Set it to <strong id="b842352706112326"><a name="b842352706112326"></a><a name="b842352706112326"></a>nfs</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0072155931_row4391735511206"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p34504224917"><a name="p34504224917"></a><a name="p34504224917"></a>vers=3,timeo=600,nolock</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0072155931_p4341916611206"><a name="en-us_topic_0072155931_p4341916611206"></a><a name="en-us_topic_0072155931_p4341916611206"></a>Mount options, used to set mount parameters. Use commas (,) to separate between multiple options.</p>
<a name="ul53831621205"></a><a name="ul53831621205"></a><ul id="ul53831621205"><li>vers: File system version. The value <strong id="b124841935181512"><a name="b124841935181512"></a><a name="b124841935181512"></a>3</strong> indicates NFSv3.</li><li>timeo: Waiting time before the NFS client retransmits a request. The unit is 0.1 second. The recommended value is <strong id="b07071648185217"><a name="b07071648185217"></a><a name="b07071648185217"></a>600</strong>.</li><li>nolock: Whether to lock files on the server using the NLM protocol.</li></ul>
</td>
</tr>
<tr id="row6225105612613"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1422617561867"><a name="p1422617561867"></a><a name="p1422617561867"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p142261656967"><a name="p142261656967"></a><a name="p142261656967"></a>Choose whether to back up file systems using the dump command.</p>
<a name="ul870812575717"></a><a name="ul870812575717"></a><ul id="ul870812575717"><li><strong id="b84235270614443"><a name="b84235270614443"></a><a name="b84235270614443"></a>0</strong>: not to back up</li><li>An integer larger than 0: to back up file systems. A file system with a smaller integer is checked earlier than that with a larger integer.</li></ul>
</td>
</tr>
<tr id="row15551659469"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1255116591667"><a name="p1255116591667"></a><a name="p1255116591667"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p11551359261"><a name="p11551359261"></a><a name="p11551359261"></a>Choose whether to check file systems using the fsck command when the ECS is starting and specify the sequence for checking file systems.</p>
<a name="ul747910315101"></a><a name="ul747910315101"></a><ul id="ul747910315101"><li><strong id="b842352706144845"><a name="b842352706144845"></a><a name="b842352706144845"></a>0</strong>: to check</li><li>By default, this field is set to <strong id="b842352706144957"><a name="b842352706144957"></a><a name="b842352706144957"></a>1</strong> for the root directory partition. Other partitions start from <strong id="b842352706145033"><a name="b842352706145033"></a><a name="b842352706145033"></a>2</strong>, and a partition with a smaller integer is checked earlier than that with a larger integer.</li></ul>
</td>
</tr>
</tbody>
</table>

## Procedure \(Windows\)<a name="section6323162217518"></a>

Ensure that an NFS client has been installed on the target server before mounting. This section uses Windows Server 2012 as an example to describe how to mount a file system.

1.  Before mounting the file system, create a script named  **auto\_mount.bat**, save the script to a local host, and record the save path. The script contains the following content:

    ```
    mount -o nolock Shared path Corresponding drive letter
    ```

    For example, content of a file system's  **auto\_mount.bat**  script can be  **mount -o nolock sfs.nas1.xxx.com/share-xxx X:**

    >![](/images/icon-note.gif) **NOTE:**   
    >After the script is created, you are advised to manually run the script in the Command Prompt interface to ensure that the script can be executed successfully.  

2.  Create a .txt file whose name is  **_XXX_.vbs**  and  **Save Type**  is  **All Files**, and save the file to the directory  **C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup**. The file contains the following content: 

    ```
    set ws=WScript.CreateObject("WScript.Shell") 
    ws.Run "Local path of the auto_mount.bat script /start", 0
    ```

3.  After the task is created, you can restart the ECS and check whether the configuration is successful.

