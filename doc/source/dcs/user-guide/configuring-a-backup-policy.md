# Configuring a Backup Policy<a name="EN-US_TOPIC_0237964730"></a>

## Scenario<a name="section66924213"></a>

On the DCS console, you can configure an automatic backup policy. The system then backs up data in your instances according to the backup policy.

If automatic backup is not required, disable the automatic backup function in the backup policy.

## Prerequisites<a name="section65447007"></a>

At least one master/standby DCS instance has been created.

## Procedure<a name="section52152158"></a>

1.  Log in to the management console.
2.  Click![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose  **Database**  \>  **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  On the  **Cache Manager**  page, filter DCS instances by instance status and/or name to find the DCS instance for which you want to configure a backup policy.
6.  Click the name of the chosen DCS instance to display more details about the DCS instance.
7.  On the instance details page, click  **Backup and Restore**.
8.  On the  **Backup and Restore**  page, click  **Backup Policy**.
9.  In the  **Backup Policy**  dialog box, set the  **Auto Backup**  parameter to  **On**  and specify other backup parameters. Click  **OK**  to complete setting the backup policy.

    **Table  1**  Parameters in a backup policy

    <a name="table12779516"></a>
    <table><thead align="left"><tr id="row7899342"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.3.1.1"><p id="p35867003"><a name="p35867003"></a><a name="p35867003"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="72%" id="mcps1.2.3.1.2"><p id="p19546120"><a name="p19546120"></a><a name="p19546120"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39731869"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p64164835"><a name="p64164835"></a><a name="p64164835"></a>Auto Backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p29969153"><a name="p29969153"></a><a name="p29969153"></a>An indicator of whether automatic backup is enabled.</p>
    </td>
    </tr>
    <tr id="row1286929"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p37132456"><a name="p37132456"></a><a name="p37132456"></a>Backup Schedule</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p54938922"><a name="p54938922"></a><a name="p54938922"></a>Day of a week on which data in the chosen DCS instance is automatically backed up.</p>
    <p id="p24688256"><a name="p24688256"></a><a name="p24688256"></a>You can select one or multiple days of a week.</p>
    </td>
    </tr>
    <tr id="row20867713"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p12563221"><a name="p12563221"></a><a name="p12563221"></a>Retention Period (days)</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p10987981"><a name="p10987981"></a><a name="p10987981"></a>The number of days that automatically backed up data is retained.</p>
    <p id="p31782970"><a name="p31782970"></a><a name="p31782970"></a>Backup data will be permanently deleted at the end of retention period and cannot be restored.</p>
    <p id="p17611282"><a name="p17611282"></a><a name="p17611282"></a>Data can be retained for up to 7 days.</p>
    </td>
    </tr>
    <tr id="row24283812"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p20831783"><a name="p20831783"></a><a name="p20831783"></a>Start Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p9652842"><a name="p9652842"></a><a name="p9652842"></a>Time at which automatic backup starts.</p>
    <p id="p19766715"><a name="p19766715"></a><a name="p19766715"></a>Value: the full hour between 00:00 to 23:00</p>
    <p id="p43682709"><a name="p43682709"></a><a name="p43682709"></a>The DCS checks backup policies once every hour. If the backup start time in a backup policy has arrived, data in the corresponding instance is backed up.</p>
    <p id="p57600065"><a name="p57600065"></a><a name="p57600065"></a>NOTE</p>
    <a name="ul48638545"></a><a name="ul48638545"></a><ul id="ul48638545"><li>Instance backup takes 5 to 30 minutes. The data added or modified during the backup process will not be backed up. To reduce the impact of backup on services, it is recommended that data should be backed up during off-peak periods.</li><li>Only instances in the <strong id="b24019444"><a name="b24019444"></a><a name="b24019444"></a>Running</strong> state can be backed up.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


