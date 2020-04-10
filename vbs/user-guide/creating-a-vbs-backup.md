# Creating a VBS Backup<a name="EN-US_TOPIC_0015667820"></a>

You can create backups for your EVS disks to protect the disk data through the VBS console or the EVS console.

## Precautions<a name="section8398849193"></a>

An EVS disk can be backed up only when its status is  **Available**  or  **In-use**. If you have performed operations such as expanding, attaching, detaching, or deleting an EVS disk, refresh the page first to ensure the completion of the operation and then determine whether to back up the disk.

## Create a VBS Backup \(Method 1\)<a name="section2110139017525"></a>

1.  Log in to the management console.
2.  Click  ![](figures/service-list.png). Under  **Storage**, click  **Volume Backup Service**.
3.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
4.  On the VBS page, click  **Create Backup**.
5.  From the EVS disk list on the left, click  ![](figures/icon-checkbox.png)  to select the EVS disks you want to back up. Then they appear in the  **Selected Disks**  list on the right. See  [Figure 1](#fig64893544452). You can click  ![](figures/icon-bin.png)  in the  **Operation**  column to delete EVS disks that do not need to be backed up.

    **Figure  1**  Selecting a disk<a name="fig64893544452"></a>  
    ![](figures/selecting-a-disk.png "selecting-a-disk")

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The system will identify whether the selected EVS disk is encrypted. If it is encrypted, its backup data will be stored in encrypted mode.  
    >In earlier versions, backup data of encrypted EVS disks is stored in non-encrypted mode. In the current version, newly generated backup data is stored in encrypted mode; however, historical non-encrypted backups will remain unchanged.  

6.  Confirm the EVS disks selected for backup are correct. Then in the  **Configure Backup**  area below, set  **Auto Backup**  or  **Immediate Backup**  or both. See  [Figure 2](#fig17436105514815).

    **Figure  2**  Configuring backup schemes<a name="fig17436105514815"></a>  
    ![](figures/configuring-backup-schemes.png "configuring-backup-schemes")

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >**Auto Backup**: The selected EVS disks will be associated with the backup policy. If the policy is enabled, the EVS disks will be automatically backed up according to the backup policy. If the selected EVS disks have been associated with another backup policy, they will be disassociated from that backup policy first and then associated with the new backup policy.  
    >**Immediate Backup**: backs up the selected EVS disks at once.  

    -   Select  **Auto Backup**: In the  **Backup Policy**  drop-down list, select an existing one. You can also click  **Create Policy**  to create a new one. For details, see  [Data Backup Using a Backup Policy](data-backup-using-a-backup-policy.md).
    -   Select  **Immediate Backup**: Enter the backup name and description.  [Table 1](#table11869527309)  describes the parameters.

        **Table  1**  Parameter description

        <a name="table11869527309"></a>
        <table><thead align="left"><tr id="row138618523302"><th class="cellrowborder" valign="top" width="22.830000000000002%" id="mcps1.2.4.1.1"><p id="p178635293011"><a name="p178635293011"></a><a name="p178635293011"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="49.17%" id="mcps1.2.4.1.2"><p id="p48625263017"><a name="p48625263017"></a><a name="p48625263017"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.3"><p id="p18645216306"><a name="p18645216306"></a><a name="p18645216306"></a>Example Value</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row1786352123012"><td class="cellrowborder" valign="top" width="22.830000000000002%" headers="mcps1.2.4.1.1 "><p id="p88645215302"><a name="p88645215302"></a><a name="p88645215302"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="49.17%" headers="mcps1.2.4.1.2 "><p id="p586115293019"><a name="p586115293019"></a><a name="p586115293019"></a>The name can only contain letters, digits, underscores (_), and hyphens (-). It cannot contain special characters or start with <strong id="b842352706104426"><a name="b842352706104426"></a><a name="b842352706104426"></a>auto</strong>. If you select only one EVS disk to back up, the backup name ranges from 1 to 64 characters. If you select more than one EVS disk to back up, the backup name ranges from 1 to 59 characters.</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.3 "><p id="p168685293017"><a name="p168685293017"></a><a name="p168685293017"></a>disk01_backup</p>
        </td>
        </tr>
        <tr id="row158615214302"><td class="cellrowborder" valign="top" width="22.830000000000002%" headers="mcps1.2.4.1.1 "><p id="p1086175214304"><a name="p1086175214304"></a><a name="p1086175214304"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="49.17%" headers="mcps1.2.4.1.2 "><p id="p18861552203013"><a name="p18861552203013"></a><a name="p18861552203013"></a>The description consists of 0 to 64 characters and cannot contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.3 "><p id="p986952143013"><a name="p986952143013"></a><a name="p986952143013"></a>for_test</p>
        </td>
        </tr>
        </tbody>
        </table>

7.  Determine whether to select  **Enable**  next to  **Full Backup**. If  **Full Backup**  is enabled, the generated full backup and later generated incremental backups will support instant restoration. When you use Instant Restore for the first time through APIs and the to-be-restored disk has been backed up before the feature is enabled, enable full backup. After doing this, the disk backups generated through APIs will support instant restoration.
8.  Add tags to the backup.

    A tag is represented in the form of a key-value pair. Tags are used to identify, classify, and search for cloud resources. Tags are used to filter and manage backup resources only. A backup can have a maximum of 10 tags.

    [Table 2](#table191162312815)  describes parameters of a tag.

    **Table  2**  Parameter description

    <a name="table191162312815"></a>
    <table><thead align="left"><tr id="row41151331884"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="p311514319817"><a name="p311514319817"></a><a name="p311514319817"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="66%" id="mcps1.2.4.1.2"><p id="p3115234819"><a name="p3115234819"></a><a name="p3115234819"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.3"><p id="p19990164015312"><a name="p19990164015312"></a><a name="p19990164015312"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51153313816"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p14115183385"><a name="p14115183385"></a><a name="p14115183385"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.2 "><p id="p611511310819"><a name="p611511310819"></a><a name="p611511310819"></a>Each tag of a backup has a unique key. The key of a tag is user-definable or is selected from those of existing tags in Tag Management Service (TMS).</p>
    <p id="p191158314810"><a name="p191158314810"></a><a name="p191158314810"></a>The naming rules for a tag key are as follows:</p>
    <a name="ul20115438812"></a><a name="ul20115438812"></a><ul id="ul20115438812"><li>It ranges from 1 to 36 Unicode characters.</li><li>It can contain only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p1499017405316"><a name="p1499017405316"></a><a name="p1499017405316"></a>Key_0001</p>
    </td>
    </tr>
    <tr id="row21161531187"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p101151731081"><a name="p101151731081"></a><a name="p101151731081"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.2 "><p id="p1911693486"><a name="p1911693486"></a><a name="p1911693486"></a>The values of tags can be repetitive and can be blank.</p>
    <p id="p21161131085"><a name="p21161131085"></a><a name="p21161131085"></a>The naming rules for a tag value are as follows:</p>
    <a name="ul211610318811"></a><a name="ul211610318811"></a><ul id="ul211610318811"><li>It ranges from 0 to 43 Unicode characters.</li><li>It can contain only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p129902040143116"><a name="p129902040143116"></a><a name="p129902040143116"></a>Value_0001</p>
    </td>
    </tr>
    </tbody>
    </table>

9.  Click  **Create Now**.
10. Confirm the VBS backup information and click  **Submit**.
11. Switch back to the VBS backup list.

    You can refresh the page after 10 seconds to view the backup creation status. When the  **Status**  of the backup changes to  **Available**, the VBS backup has been successfully created.


## Create a VBS Backup \(Method 2\)<a name="section304810668184"></a>

1.  Log in to the management console.
2.  Click  ![](figures/service-list-0.png). Under  **Storage**, click  **Volume Backup Service**.
3.  Click  ![](figures/icon-region-1.png)  in the upper left corner of the management console and select a region and a project.
4.  Locate the row that contains the target EVS disk, click  **More**  in the  **Operation**  column, and select  **Back Up**.
5.  From the EVS disk list on the left, click  ![](figures/icon-checkbox.png)  to select the EVS disks you want to back up. Then they appear in the  **Selected Disks**  list on the right. See  [Figure 3](#fig19341916182310). You can click  ![](figures/icon-bin.png)  in the  **Operation**  column to delete EVS disks that do not need to be backed up.

    **Figure  3**  Selecting a disk<a name="fig19341916182310"></a>  
    ![](figures/selecting-a-disk-2.png "selecting-a-disk-2")

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The system will identify whether the selected EVS disk is encrypted. If it is encrypted, its backup data will be stored in encrypted mode.  
    >In earlier versions, backup data of encrypted EVS disks is stored in non-encrypted mode. In the current version, newly generated backup data is stored in encrypted mode; however, historical non-encrypted backups will remain unchanged.  

6.  Confirm the EVS disks selected for backup are correct. Then in the  **Configure Backup**  area below, set  **Auto Backup**  or  **Immediate Backup**  or both. See  [Figure 4](#fig22827152142).

    **Figure  4**  Configuring backup schemes<a name="fig22827152142"></a>  
    ![](figures/configuring-backup-schemes-3.png "configuring-backup-schemes-3")

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >**Auto Backup**: The selected EVS disks will be associated with the backup policy and will be automatically backed up according to the backup policy. If the selected EVS disks have been associated with another backup policy, they will be disassociated from that backup policy first and then associated with the new backup policy.  
    >**Immediate Backup**: backs up the selected EVS disks at once.  

    -   Select  **Auto Backup**: In the  **Backup Policy**  drop-down list, select an existing one. You can also click  **Create Policy**  to create a new one. For details, see  [Data Backup Using a Backup Policy](data-backup-using-a-backup-policy.md).
    -   Select  **Immediate Backup**: Enter the backup name and description.  [Table 1](#table11869527309)  describes the parameters.

7.  Determine whether to select  **Enable**  next to  **Full Backup**. If  **Full Backup**  is enabled, the generated full backup and later generated incremental backups will support instant restoration. When you use Instant Restore for the first time through APIs and the to-be-restored disk has been backed up before the feature is enabled, enable full backup. After doing this, the disk backups generated through APIs will support instant restoration.
8.  Add tags to the VBS backup.  [Table 2](#table191162312815)  describes the parameters.

    A tag is represented in the form of a key-value pair. Tags are used to identify, classify, and search for cloud resources. Tags are used to filter and manage backup resources only. A backup can have a maximum of 10 tags.

9.  Click  **Create Now**.
10. Confirm the VBS backup information and click  **Submit**.
11. Switch back to the VBS backup list.

    You can refresh the page after 10 seconds to view the backup creation status. When the  **Status**  of the backup changes to  **Available**, the VBS backup has been successfully created.


