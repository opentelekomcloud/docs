# Creating a Backup Policy<a name="EN-US_TOPIC_0112805383"></a>

To implement periodic automatic backup on EVS disks, you need to create a backup policy first. Then the system will periodically perform backups according to the execution time specified in the backup policy. You can choose to use the default backup policy provided by the system or create one as needed.

The system automatically creates EVS disk data backups and deletes expired data backups only when a backup policy is created and enabled.

You can create a backup policy to associate all those EVS disks whose data needs to be periodically backed up.

>![](/images/icon-note.gif) **NOTE:**   
>-   The system provides a default backup policy for associating EVS disks. This default backup policy can be enabled, disabled, edited, and executed. For details about how to execute the default backup policy, see  [Executing a backup policy]((optional)-other-operations-with-backup-policies.md#li17723809281). For details about how to edit the default backup policy, see  [Editing a backup policy]((optional)-other-operations-with-backup-policies.md#li58602112277).  
>-   In addition to the default backup policy, you can create another 31 backup policies. Once there are 32 backup policies in total, the  **Create Policy**  button becomes unavailable and no more policies can be created.  
>-   Deleting expired automatic data backups does not delete manual data backups.  

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  ![](figures/service-list.png). Under  **Storage**, click  **Volume Backup Service**.
4.  On the  **Volume Backup Service**  page, click  **Policies**  to go to the  **Policies**  tab page.

    The  **Policies**  tab page displays existing backup policies. Expand the desired backup policy to view EVS disks associated with it.

5.  Click  **Create Backup Policy**  to expand the setting items.  [Figure 1](#fig103975522358)  displays the page.  [Table 1](#table98735364165)  describes the backup policy parameters.

    **Figure  1**  Creating a backup policy<a name="fig103975522358"></a>  
    ![](figures/creating-a-backup-policy.png "creating-a-backup-policy")

    **Table  1**  Parameter description

    <a name="table98735364165"></a>
    <table><thead align="left"><tr id="row887311366166"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.4.1.1"><p id="p254211511183"><a name="p254211511183"></a><a name="p254211511183"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.44444444444445%" id="mcps1.2.4.1.2"><p id="p19542141510183"><a name="p19542141510183"></a><a name="p19542141510183"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.3"><p id="p125421015111819"><a name="p125421015111819"></a><a name="p125421015111819"></a>Remarks</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7742134210513"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.4.1.1 "><p id="p9879612769"><a name="p9879612769"></a><a name="p9879612769"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p48795125612"><a name="p48795125612"></a><a name="p48795125612"></a>The name is a string of 1 to 64 characters consisting of letters, digits, underscores (_), and hyphens (-), and cannot start with <strong id="b842352706174824"><a name="b842352706174824"></a><a name="b842352706174824"></a>default</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p28796125619"><a name="p28796125619"></a><a name="p28796125619"></a>Example value: <strong id="b842352706153827"><a name="b842352706153827"></a><a name="b842352706153827"></a>autobk_78ba</strong></p>
    </td>
    </tr>
    <tr id="row188736362161"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.4.1.1 "><p id="p149017245183"><a name="p149017245183"></a><a name="p149017245183"></a>Execution Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p290132411183"><a name="p290132411183"></a><a name="p290132411183"></a>Detailed time for backing up data of the EVS disks associated with the backup policy.</p>
    <p id="p121573393241"><a name="p121573393241"></a><a name="p121573393241"></a>Backup can be scheduled on integral hours and multiple selections are supported.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p15901112416185"><a name="p15901112416185"></a><a name="p15901112416185"></a>Example value: <strong id="b842352706153838"><a name="b842352706153838"></a><a name="b842352706153838"></a>02:00</strong></p>
    </td>
    </tr>
    <tr id="row168737368168"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.4.1.1 "><p id="p15284193919185"><a name="p15284193919185"></a><a name="p15284193919185"></a>Backup Period</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p8284173912181"><a name="p8284173912181"></a><a name="p8284173912181"></a><strong id="b204415531453"><a name="b204415531453"></a><a name="b204415531453"></a>Weekly</strong>: specifies on which days of each week the backup job will be executed. You can select all.</p>
    <p id="p9284203911811"><a name="p9284203911811"></a><a name="p9284203911811"></a><strong id="b18081548114517"><a name="b18081548114517"></a><a name="b18081548114517"></a>Daily</strong>: specifies the interval (every 1 to 14 days) for executing the backup job (on the hour).</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p12284639181814"><a name="p12284639181814"></a><a name="p12284639181814"></a>Example value: <strong id="b84235270615400"><a name="b84235270615400"></a><a name="b84235270615400"></a>Every 3 days</strong></p>
    <p id="p142841139171811"><a name="p142841139171811"></a><a name="p142841139171811"></a>If you select <strong id="b842352706105626"><a name="b842352706105626"></a><a name="b842352706105626"></a>Daily</strong>, the first backup time is irrelevant to the time when the backup policy is created. A backup policy takes effect from the month when it is created. Policies with the same <strong id="b1533115316357"><a name="b1533115316357"></a><a name="b1533115316357"></a>Backup Period</strong> execute backup jobs at the same times. For example, if a backup policy with "Every 3 days" is created on the second date of a month, the first backup will be created on the fourth date of the month. "Every 3 days" indicates that backups will be created on the first date, fourth date, seventh date, and so on.</p>
    <p id="p152841739191816"><a name="p152841739191816"></a><a name="p152841739191816"></a>To ensure stable service running, back up EVS disks during off-peak hours.</p>
    </td>
    </tr>
    <tr id="row14873036121611"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.4.1.1 "><p id="p142787091919"><a name="p142787091919"></a><a name="p142787091919"></a>Retention Rule</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p10278205192"><a name="p10278205192"></a><a name="p10278205192"></a><strong id="b84235270611412"><a name="b84235270611412"></a><a name="b84235270611412"></a>Time Period</strong>: You can choose to retain backups for one month, three months, six months, or one year, or for any desired number (2 to 99999) of days.</p>
    <p id="p192781801197"><a name="p192781801197"></a><a name="p192781801197"></a><strong id="b84235270611534"><a name="b84235270611534"></a><a name="b84235270611534"></a>Backup Quantity</strong>: specifies the maximum allowed number of backups for a single EVS disk.</p>
    <div class="note" id="note1045115620234"><a name="note1045115620234"></a><a name="note1045115620234"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p44512056202314"><a name="p44512056202314"></a><a name="p44512056202314"></a>Set this parameter based on the applied quota. For example, if 10 EVS disks are associated with the backup policy and this parameter is set to 10, then at least a quota of 100 backups is required. If the applied quota is smaller than 100, the backup job will fail due to the insufficient quota. To view the quota, read the related tip above the VBS backup list.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p17278150201914"><a name="p17278150201914"></a><a name="p17278150201914"></a>Example value: <strong id="b842352706154215"><a name="b842352706154215"></a><a name="b842352706154215"></a>6</strong></p>
    <p id="p327870171912"><a name="p327870171912"></a><a name="p327870171912"></a>A more frequent backup of EVS disks creates more backups and delivers a higher level of data protection but occupies more storage space. Determine the backup frequency based on the data importance and service volume. Perform relatively frequent backup operations for important data.</p>
    <p id="p1727820131916"><a name="p1727820131916"></a><a name="p1727820131916"></a>When the number of backups to be retained has exceeded the value of <strong id="b40729550611834"><a name="b40729550611834"></a><a name="b40729550611834"></a>Backup Quantity</strong>, the system automatically deletes the earliest backups. After a backup is deleted, the other backups can still be used for restoration.</p>
    </td>
    </tr>
    <tr id="row4873183612161"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.4.1.1 "><p id="p752101213194"><a name="p752101213194"></a><a name="p752101213194"></a>Retain the first backup in this month</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p1352812181915"><a name="p1352812181915"></a><a name="p1352812181915"></a>If you select this option, the initial data backup in the current month will be retained.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1752212161912"><a name="p1752212161912"></a><a name="p1752212161912"></a>The first backup in the current month will not be deleted. For example, if the current month is February, the first backup generated in February will not be deleted during February. The first backup generated in January, together with other backups generated in January, will be deleted in sequence.</p>
    </td>
    </tr>
    <tr id="row16860111671910"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.4.1.1 "><p id="p2860416181910"><a name="p2860416181910"></a><a name="p2860416181910"></a>Enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.4.1.2 "><p id="p13860116101920"><a name="p13860116101920"></a><a name="p13860116101920"></a>You can turn on the switch (<a name="image7513351173012"></a><a name="image7513351173012"></a><span><img id="image7513351173012" src="figures/button.png"></span>) to enable the backup policy or turn off the switch (<a name="image13184659114519"></a><a name="image13184659114519"></a><span><img id="image13184659114519" src="figures/icon-off.png"></span>) to disable the backup policy.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p5860416141913"><a name="p5860416141913"></a><a name="p5860416141913"></a>If you have disabled the backup policy or have turned off the switch (<a name="image59767267484"></a><a name="image59767267484"></a><span><img id="image59767267484" src="figures/icon-off.png"></span>), you can select the backup policy in the backup policy list and turn on the switch (<a name="image87619614312"></a><a name="image87619614312"></a><span><img id="image87619614312" src="figures/button-4.png"></span>) to enable it.</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Add tags to the backup.

    A tag is represented in the form of a key-value pair. Tags are used to identify, classify, and search for cloud resources.

    Tags added in a backup policy apply to all backups generated using the backup policy. Tags are used to filter and manage backup resources only. A backup policy can have a maximum of 10 tags.

    [Table 2](#table1499463312)  describes parameters of a tag.

    **Table  2**  Parameter description

    <a name="table1499463312"></a>
    <table><thead align="left"><tr id="row7997693112"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="p311514319817"><a name="p311514319817"></a><a name="p311514319817"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="66%" id="mcps1.2.4.1.2"><p id="p3115234819"><a name="p3115234819"></a><a name="p3115234819"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.3"><p id="p19990164015312"><a name="p19990164015312"></a><a name="p19990164015312"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41005620310"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p14115183385"><a name="p14115183385"></a><a name="p14115183385"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.2 "><p id="p611511310819"><a name="p611511310819"></a><a name="p611511310819"></a>Each tag of a backup has a unique key. The key of a tag is user-definable or is selected from those of existing tags in TMS.</p>
    <p id="p191158314810"><a name="p191158314810"></a><a name="p191158314810"></a>The naming rules for a tag key are as follows:</p>
    <a name="ul20115438812"></a><a name="ul20115438812"></a><ul id="ul20115438812"><li>It ranges from 1 to 36 Unicode characters.</li><li>It can contain only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p1499017405316"><a name="p1499017405316"></a><a name="p1499017405316"></a>Key_0001</p>
    </td>
    </tr>
    <tr id="row1310014614314"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p101151731081"><a name="p101151731081"></a><a name="p101151731081"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.2 "><p id="p1911693486"><a name="p1911693486"></a><a name="p1911693486"></a>The values of tags can be repetitive and can be blank.</p>
    <p id="p21161131085"><a name="p21161131085"></a><a name="p21161131085"></a>The naming rules for a tag value are as follows:</p>
    <a name="ul211610318811"></a><a name="ul211610318811"></a><ul id="ul211610318811"><li>It ranges from 0 to 43 Unicode characters.</li><li>It can contain only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="p129902040143116"><a name="p129902040143116"></a><a name="p129902040143116"></a>Value_0001</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

