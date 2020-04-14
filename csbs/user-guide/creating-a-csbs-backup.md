# Creating a CSBS Backup<a name="EN-US_TOPIC_0072046354"></a>

This section explains how to create CSBS backup jobs to protect ECS data.

## Prerequisites<a name="section1638313413316"></a>

-   If you want to use a backup to create an image, perform the following operations before creating a CSBS backup:
    -   You have optimized the Linux ECS \(referring to  [\(Optional\) Optimizing a Linux Private Image](https://docs.otc.t-systems.com/usermanual/ims/en-us_topic_0047501133.html)\) and installed Cloud-Init \(referring to  [Installing Cloud-Init](https://docs.otc.t-systems.com/usermanual/ims/en-us_topic_0030730603.html)\).
    -   You have optimized the Windows ECS \(referring to  [\(Optional\) Optimizing a Windows Private Image](https://docs.otc.t-systems.com/usermanual/ims/en-us_topic_0047501112.html)\) and installed Cloudbase-Init \(referring to  [Installing Cloudbase-Init](https://docs.otc.t-systems.com/usermanual/ims/en-us_topic_0030730602.html)\).


## Procedure<a name="section10714102810610"></a>

1.  Log in to the CSBS management console.
    1.  Log in to the management console.
    2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
    3.  Click  ![](figures/icon-servicelist.png). Under  **Storage**, click  **Cloud Server Backup Service**.

2.  In the upper right corner of the page, click  **Create CSBS Backup**.
3.  In the ECS list, select the ECSs you want to back up. After ECSs are selected, they are added to the list of selected ECSs. See  [Figure 1](#fig7683103644515).

    **Figure  1**  Selecting servers<a name="fig7683103644515"></a>  
    ![](figures/selecting-servers.png "selecting-servers")

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   The selected ECSs must be in the  **Running**  or  **Stopped**  state.  
    >-   ECSs with shared EVS disks can be backed up.  

4.  In the  **Configure Backup**  area, configure a backup scheme for the selected servers. See  [Figure 2](#fig599112219464).

    **Figure  2**  Configuring backup schemes<a name="fig599112219464"></a>  
    ![](figures/configuring-backup-schemes.png "configuring-backup-schemes")

    -   **Auto Backup**:

        In the  **Backup Policy**  drop-down list, select a backup policy. Alternatively, click  **Create Policy**  to create a backup policy. For details about the parameters of a backup policy, see  [Creating a Backup Policy](creating-a-backup-policy.md).

        After a backup job is created, the selected ECSs are associated with the backup policy and will be periodically backed up according to the backup policy.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If a selected ECS has been associated with another backup policy, it will be disassociated from the original backup policy automatically and then associated with the new backup policy.  

    -   **Immediate Backup**:

        After a backup job is created, all selected ECSs will be backed up immediately for once.

        Set the  **Name**  and  **Description**  of the backup, as described in  [Table 1](#table4829135361311).

        **Table  1**  Parameter description

        <a name="table4829135361311"></a>
        <table><thead align="left"><tr id="row148305532138"><th class="cellrowborder" valign="top" width="21.240000000000002%" id="mcps1.2.4.1.1"><p id="p083065318138"><a name="p083065318138"></a><a name="p083065318138"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="56.96%" id="mcps1.2.4.1.2"><p id="p083019532138"><a name="p083019532138"></a><a name="p083019532138"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="21.8%" id="mcps1.2.4.1.3"><p id="p98301553161318"><a name="p98301553161318"></a><a name="p98301553161318"></a>Remarks</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row1783115313136"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p3831135341313"><a name="p3831135341313"></a><a name="p3831135341313"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="56.96%" headers="mcps1.2.4.1.2 "><p id="p1183119535130"><a name="p1183119535130"></a><a name="p1183119535130"></a>Name of the backup you are creating.</p>
        <p id="p12831145311135"><a name="p12831145311135"></a><a name="p12831145311135"></a>It is a string of 1 to 255 characters that can contain only digits, letters, underscores (_), and hyphens (-).</p>
        <div class="note" id="note683113533139"><a name="note683113533139"></a><a name="note683113533139"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p8875521124020"><a name="p8875521124020"></a><a name="p8875521124020"></a>You can use the default name, which defaults to <strong id="b842352706153327"><a name="b842352706153327"></a><a name="b842352706153327"></a>manualbk_</strong><em id="i842352697153330"><a name="i842352697153330"></a><a name="i842352697153330"></a>xxxx</em>.</p>
        <p id="p11831125312137"><a name="p11831125312137"></a><a name="p11831125312137"></a>When multiple ECSs are to be backed up, the system automatically adds suffixes to their names, for example, <strong id="b84235270671449"><a name="b84235270671449"></a><a name="b84235270671449"></a>backup-0001</strong> and <strong id="b50763064071456"><a name="b50763064071456"></a><a name="b50763064071456"></a>backup-0002</strong>.</p>
        </div></div>
        </td>
        <td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.2.4.1.3 "><p id="p15831185312131"><a name="p15831185312131"></a><a name="p15831185312131"></a>manualbk_cbf0</p>
        </td>
        </tr>
        <tr id="row3831195371315"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p9831185391318"><a name="p9831185391318"></a><a name="p9831185391318"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="56.96%" headers="mcps1.2.4.1.2 "><p id="p10831853181310"><a name="p10831853181310"></a><a name="p10831853181310"></a>Supplementary information about the backup.</p>
        <p id="p10831135391313"><a name="p10831135391313"></a><a name="p10831135391313"></a>It cannot exceed 255 characters.</p>
        </td>
        <td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.2.4.1.3 "><p id="p19831165313138"><a name="p19831165313138"></a><a name="p19831165313138"></a>--</p>
        </td>
        </tr>
        </tbody>
        </table>

    You can select both the backup methods at the same time. When both the backup methods are selected, a one-off backup will be performed at once and periodic backups will be performed according to the backup policy subsequently.

5.  Determine whether to select  **Enable**  next to  **Full Backup**. If  **Full Backup**  is enabled, the generated full backup and later generated incremental backups will support  [Instant Restore](basic-concepts.md#section181448505477). See  [Figure 3](#fig21211503353).

    **Figure  3**  Enabling Full Backup or not<a name="fig21211503353"></a>  
    ![](figures/enabling-full-backup-or-not.png "enabling-full-backup-or-not")

6.  Add tags to the backup. \(This operation is optional if you select  **Immediate Backup**.\)

    A tag is represented in the form of a key-value pair. Tags are used to identify, classify, and search for cloud resources. These tags are used to filter and manage backup resources only. A backup can have a maximum of 10 tags.

    See  [Figure 4](#fig09521715453).

    **Figure  4**  Adding a tag<a name="fig09521715453"></a>  
    ![](figures/adding-a-tag.png "adding-a-tag")

    [Table 2](#table191162312815)  describes parameters of a tag.

    **Table  2**  Parameter description

    <a name="table191162312815"></a>
    <table><thead align="left"><tr id="row41151331884"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="p311514319817"><a name="p311514319817"></a><a name="p311514319817"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.4.1.2"><p id="p3115234819"><a name="p3115234819"></a><a name="p3115234819"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.3"><p id="p19990164015312"><a name="p19990164015312"></a><a name="p19990164015312"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51153313816"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p14115183385"><a name="p14115183385"></a><a name="p14115183385"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.2 "><p id="p611511310819"><a name="p611511310819"></a><a name="p611511310819"></a>Tag key. Each tag of a backup has a unique key. The key of a tag is user-definable or is selected from those of existing tags in Tag Management Service (TMS).</p>
    <p id="p191158314810"><a name="p191158314810"></a><a name="p191158314810"></a>The naming rule of a tag key is as follows:</p>
    <a name="ul1277719205177"></a><a name="ul1277719205177"></a><ul id="ul1277719205177"><li>It ranges from 1 to 36 Unicode characters.</li></ul>
    <a name="ul20115438812"></a><a name="ul20115438812"></a><ul id="ul20115438812"><li>It can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p1499017405316"><a name="p1499017405316"></a><a name="p1499017405316"></a>Key_0001</p>
    </td>
    </tr>
    <tr id="row21161531187"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p101151731081"><a name="p101151731081"></a><a name="p101151731081"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.2 "><p id="p1911693486"><a name="p1911693486"></a><a name="p1911693486"></a>Tag value. Tag values can be repetitive or null.</p>
    <p id="p21161131085"><a name="p21161131085"></a><a name="p21161131085"></a>The naming rule of a tag value is as follows:</p>
    <a name="ul1640142918175"></a><a name="ul1640142918175"></a><ul id="ul1640142918175"><li>It ranges from 0 to 43 Unicode characters.</li></ul>
    <a name="ul211610318811"></a><a name="ul211610318811"></a><ul id="ul211610318811"><li>It can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p129902040143116"><a name="p129902040143116"></a><a name="p129902040143116"></a>Value_0001</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **Create Now**.
8.  On the  **Confirm**  page, confirm the resource details and click  **Submit**.
9.  Return to the CSBS page as prompted.
    -   Auto Backup

        On the  **Policies**  tab page, click  ![](figures/icon-down(2).png)  on the left of the backup policy name. If all selected ECSs are displayed under  **Associated Servers**, they are associated with the backup policy successfully, and automatic backup will be periodically performed as scheduled.

    -   Immediate Backup

        On the  **Backups**  tab page, if the generated backups are in the  **Available**  state, the one-off backup job is successful. 



