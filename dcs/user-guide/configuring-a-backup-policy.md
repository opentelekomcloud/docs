# Configuring a Backup Policy<a name="en-us_topic_0062866097"></a>

## Scenario<a name="section1352821454710"></a>

On the DCS console, you can configure an automatic backup policy. The system then backs up data in your instances according to the backup policy.

If automatic backup is not required, disable the automatic backup function in the backup policy.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>This function is supported only by master/standby and Proxy Cluster instances, but is not supported by single-node instances.

## Procedure<a name="section11528214144715"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png) in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose **Database** \> **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  On the  **Cache** **Manager**  page, filter DCS instances by instance status and/or name to find the DCS instance for which you want to configure a backup policy.
6.  Click the name of the chosen DCS instance to display more details about the DCS instance.
7.  On the instance details page, click  **Backups & Restorations**.
8.  Slide  ![](figures/en-us_image_0232710380.png)  to the right to enable automatic backup. Backup policies will be displayed.

    **Table  1**  Parameters in a backup policy

    <a name="table106612411418"></a>
    <table><thead align="left"><tr id="row8678414410"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="p067174117410"><a name="p067174117410"></a><a name="p067174117410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="p667941542"><a name="p667941542"></a><a name="p667941542"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row267134113411"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p13681741746"><a name="p13681741746"></a><a name="p13681741746"></a>Backup Schedule</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p779464131810"><a name="p779464131810"></a><a name="p779464131810"></a>Day of a week on which data in the chosen DCS instance is automatically backed up.</p>
    <p id="p152041652203214"><a name="p152041652203214"></a><a name="p152041652203214"></a>You can select one or multiple days of a week.</p>
    </td>
    </tr>
    <tr id="row17682411040"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p14687411546"><a name="p14687411546"></a><a name="p14687411546"></a>Retention Period (days)</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p26894110412"><a name="p26894110412"></a><a name="p26894110412"></a>The number of days that automatically backed up data is retained.</p>
    <p id="p145762584192"><a name="p145762584192"></a><a name="p145762584192"></a>Backup data will be permanently deleted at the end of retention period and cannot be restored. Value range: 1–7.</p>
    </td>
    </tr>
    <tr id="row20681841543"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p7681411748"><a name="p7681411748"></a><a name="p7681411748"></a>Start Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p26810411947"><a name="p26810411947"></a><a name="p26810411947"></a>Time at which automatic backup starts. Value: the full hour between 00:00 to 23:00</p>
    <p id="p8472922155520"><a name="p8472922155520"></a><a name="p8472922155520"></a>The DCS checks backup policies once every hour. If the backup start time in a backup policy has arrived, data in the corresponding instance is backed up.</p>
    <div class="note" id="note5249843151515"><a name="note5249843151515"></a><a name="note5249843151515"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p02508432157"><a name="p02508432157"></a><a name="p02508432157"></a>Instance backup takes 5 to 30 minutes. The data added or modified during the backup process will not be backed up. To reduce the impact of backup on services, it is recommended that data should be backed up during off-peak periods.</p>
    <p id="p193271546527"><a name="p193271546527"></a><a name="p193271546527"></a>Only instances in the <strong id="b1061217415115"><a name="b1061217415115"></a><a name="b1061217415115"></a>Running</strong> state can be backed up.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

9.  Click  **OK**.

