# Creating a Backup Policy<a name="en-us_topic_0056584629"></a>

A  backup policy  can drive the system to automatically execute CSBS backup jobs at the specified interval.  Periodic backups  can be used to restore data quickly against data corruption or loss.

## Context<a name="section3333171185517"></a>

-   Automatic backup jobs require enabling the backup policy. The system automatically backs up ECSs associated with the backup policy and deletes expired backups.
-   Each user can create a maximum of 32 backup policies.
-   A maximum of 64 ECSs can be associated with a backup policy.

## Procedure<a name="section1873403013810"></a>

1.  Log in to the CSBS management console.
    1.  Log in to the management console.
    2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
    3.  Click  ![](figures/icon-servicelist.png). Under  **Storage**, click  **Cloud Server Backup Service**.

2.  On the  **Policies**  tab page, click  **Create Backup Policy**. See  [Figure 1](#fig16533334552).

    **Figure  1**  Creating a backup policy<a name="fig16533334552"></a>  
    ![](figures/creating-a-backup-policy.png "creating-a-backup-policy")

3.  Set the backup policy parameters according to  [Table 1](#table18975142115146).

    **Table  1**  Parameter description

    <a name="table18975142115146"></a>
    <table><thead align="left"><tr id="row1997514210149"><th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.4.1.1"><p id="p13976421151411"><a name="p13976421151411"></a><a name="p13976421151411"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.2.4.1.2"><p id="p1497652113146"><a name="p1497652113146"></a><a name="p1497652113146"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.3"><p id="p1597662113147"><a name="p1597662113147"></a><a name="p1597662113147"></a>Remarks</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4976122191416"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.4.1.1 "><p id="p6976162141412"><a name="p6976162141412"></a><a name="p6976162141412"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.4.1.2 "><p id="p18976321111413"><a name="p18976321111413"></a><a name="p18976321111413"></a>Backup policy name.</p>
    <p id="p79769215148"><a name="p79769215148"></a><a name="p79769215148"></a>It is a string of 1 to 255 characters that can contain only digits, letters, underscores (_), and hyphens (-).</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1697662117143"><a name="p1697662117143"></a><a name="p1697662117143"></a>backup_policy</p>
    </td>
    </tr>
    <tr id="row1248223165716"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.4.1.1 "><p id="p104838317576"><a name="p104838317576"></a><a name="p104838317576"></a>Status</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.4.1.2 "><p id="p548333175713"><a name="p548333175713"></a><a name="p548333175713"></a>Whether to enable the backup policy.</p>
    <a name="ul14659163365820"></a><a name="ul14659163365820"></a><ul id="ul14659163365820"><li>Enabled: <a name="image82561154143416"></a><a name="image82561154143416"></a><span><img id="image82561154143416" src="figures/icon-blueenable.png"></span></li><li>Disabled: <a name="image192651120192716"></a><a name="image192651120192716"></a><span><img id="image192651120192716" src="figures/icon-off.png"></span></li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p15483131105714"><a name="p15483131105714"></a><a name="p15483131105714"></a>Only after the backup policy is enabled, the system automatically backs up ECSs associated with the backup policy and deletes expired backups.</p>
    </td>
    </tr>
    <tr id="row1631531981516"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.4.1.1 "><p id="p331615194152"><a name="p331615194152"></a><a name="p331615194152"></a>Execution Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.4.1.2 "><p id="p14316419131512"><a name="p14316419131512"></a><a name="p14316419131512"></a>Execution time of the backup policy in a day</p>
    <p id="p1445292591817"><a name="p1445292591817"></a><a name="p1445292591817"></a>A maximum of 24 backup times can be set in a day. The backup interval must be one hour or more. If backup jobs are executed in two consecutive days, the interval between the execution times of the last backup of the former day and the first backup of the latter day must be one hour or more.</p>
    <p id="p1956165211711"><a name="p1956165211711"></a><a name="p1956165211711"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p631620196155"><a name="p631620196155"></a><a name="p631620196155"></a>00:00, 02:00</p>
    <p id="p19767124972810"><a name="p19767124972810"></a><a name="p19767124972810"></a>It is recommended that backup jobs be executed during off-peak hours or when there are no services running.</p>
    </td>
    </tr>
    <tr id="row8447021201515"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.4.1.1 "><p id="p12447122111511"><a name="p12447122111511"></a><a name="p12447122111511"></a>Backup Period</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.4.1.2 "><p id="p2099535614183"><a name="p2099535614183"></a><a name="p2099535614183"></a>Dates for executing the backup job.</p>
    <a name="ul172457131819"></a><a name="ul172457131819"></a><ul id="ul172457131819"><li>Weekly<p id="p17814654190"><a name="p17814654190"></a><a name="p17814654190"></a>Specifies on which days of each week the backup job will be executed. You can select multiple days.</p>
    </li><li>Daily<p id="p1510912112020"><a name="p1510912112020"></a><a name="p1510912112020"></a>Specifies the interval (every 1 to 30 days) for executing the backup job.</p>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p20229131519311"><a name="p20229131519311"></a><a name="p20229131519311"></a>Every day</p>
    <p id="p35261251144815"><a name="p35261251144815"></a><a name="p35261251144815"></a>If you select <strong id="b12865125557"><a name="b12865125557"></a><a name="b12865125557"></a>Daily</strong>, the first backup time is supposed to be in the day when the backup policy is created. If the creation time of the backup policy is later than the latest execution time, the initial backup will be performed in the next backup cycle.</p>
    <p id="p780882374520"><a name="p780882374520"></a><a name="p780882374520"></a>It is recommended that backup jobs be executed during off-peak hours or when there are no services running.</p>
    </td>
    </tr>
    <tr id="row9482950131718"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.4.1.1 "><p id="p1648219506178"><a name="p1648219506178"></a><a name="p1648219506178"></a>Retention Rule</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.4.1.2 "><p id="p9482850191713"><a name="p9482850191713"></a><a name="p9482850191713"></a>Rule that specifies how backups will be retained.</p>
    <a name="ul1544815182330"></a><a name="ul1544815182330"></a><ul id="ul1544815182330"><li>Time Period<p id="p493811214366"><a name="p493811214366"></a><a name="p493811214366"></a>You can choose to retain backups for one month, three months, six months, or one year, or for any desired number (1 to 99999) of days.</p>
    </li><li>Backup Quantity<p id="p5958151317388"><a name="p5958151317388"></a><a name="p5958151317388"></a>Specifies the maximum allowed number of backups for a single ECS. The value ranges from 1 to 99999.</p>
    </li><li>Permanent<div class="note" id="note5251621114717"><a name="note5251621114717"></a><a name="note5251621114717"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul513693919476"></a><a name="ul513693919476"></a><ul id="ul513693919476"><li>When the number of retained backups exceeds the preset value, the system automatically deletes the earliest backups. When the retention periods of retained backups exceed the preset value, the system automatically deletes all expired backups. By default, the system automatically clears data every other day. The deleted backup does not affect other backups for restoration.</li><li>This parameter applies only to backups automatically scheduled by a backup policy. Those backups generated by a manually executed backup policy are not affected by this parameter and are not automatically deleted. You can manually delete them from the backup list.</li><li>After a backup is used to create an image, the backup will not be counted as a retained backup and will not be deleted automatically.</li><li>A maximum of 10 backups are retained for failed periodic backup jobs. They are retained for one month and can be manually deleted.</li></ul>
    </div></div>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1648275016171"><a name="p1648275016171"></a><a name="p1648275016171"></a>6 months</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >More frequent backup intervals create more backups or retain backups for a longer time, protecting data with a higher level but occupying more storage space. Set an appropriate backup period as required.  

4.  Add tags to the backup.

    A tag is represented in the form of a key-value pair. Tags are used to identify, classify, and search for cloud resources.

    Tags added in a backup policy apply to all backups generated using the backup policy. These tags are used to filter and manage backup resources only. A backup policy can have a maximum of 10 tags.

    [Table 2](#table1499463312)  describes parameters of a tag.

    **Table  2**  Parameter description

    <a name="table1499463312"></a>
    <table><thead align="left"><tr id="row7997693112"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="p610096163114"><a name="p610096163114"></a><a name="p610096163114"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.2"><p id="p111001683118"><a name="p111001683118"></a><a name="p111001683118"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.3"><p id="p13176100134"><a name="p13176100134"></a><a name="p13176100134"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41005620310"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p51007653114"><a name="p51007653114"></a><a name="p51007653114"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.2 "><p id="p1100765311"><a name="p1100765311"></a><a name="p1100765311"></a>Tag key. Each tag of a backup policy has a unique key. The key of a tag is user-definable or is selected from those of existing tags in TMS.</p>
    <p id="p1310012619313"><a name="p1310012619313"></a><a name="p1310012619313"></a>The naming rule of a tag key is as follows:</p>
    <a name="ul20115438812"></a><a name="ul20115438812"></a><ul id="ul20115438812"><li>It ranges from 1 to 36 Unicode characters.</li><li>It can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p1617616012310"><a name="p1617616012310"></a><a name="p1617616012310"></a>Key_0001</p>
    </td>
    </tr>
    <tr id="row1310014614314"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p141001968315"><a name="p141001968315"></a><a name="p141001968315"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.2 "><p id="p1510056203114"><a name="p1510056203114"></a><a name="p1510056203114"></a>Tag value. Tag values can be repetitive or null.</p>
    <p id="p2100186133115"><a name="p2100186133115"></a><a name="p2100186133115"></a>The naming rule of a tag value is as follows:</p>
    <a name="ul211610318811"></a><a name="ul211610318811"></a><ul id="ul211610318811"><li>It ranges from 0 to 43 Unicode characters.</li><li>It can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p19176601033"><a name="p19176601033"></a><a name="p19176601033"></a>Value_0001</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **OK**  to complete the policy creation.
6.  In the row of the backup policy, click  **Associate Server**. See  [Figure 2](#fig154919316596).

    **Figure  2**  Associating servers<a name="fig154919316596"></a>  
    ![](figures/associating-servers.png "associating-servers")

7.  In the available server list, select the ECSs you want to associate. After ECSs are selected, they are added to the list of selected servers.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   A maximum of 64 ECSs can be associated with a backup policy.  
    >-   If a selected ECS has been associated with another backup policy, it will be disassociated from the original backup policy automatically and then associated with the new backup policy.  
    >-   If EVS disks on an ECS have been associated with a VBS backup policy, disassociate them from the VBS backup policy. Otherwise, two backups are generated for each of the EVS disks.  
    >-   CSBS supports backing up ECSs with shared EVS disks.  
    >-   You can only select ECSs that are in the  **Running**  or  **Stopped**  state.  

8.  Click  **OK**.

