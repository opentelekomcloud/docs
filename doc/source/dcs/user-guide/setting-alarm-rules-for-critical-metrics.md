# Setting Alarm Rules for Critical Metrics<a name="dcs-ug-190905001"></a>

As listed in  [DCS Metrics](dcs-metrics.md), Cloud Eye monitors a wide variety of DCS metrics.

Among all the metrics, the ones listed in the following table are of particular importance. Configure alarm rules for these metrics to be notified immediately after the set thresholds are reached.

**Table  1**  Metrics to set alarm rules for

<a name="table114102532214"></a>
<table><thead align="left"><tr id="row74121453152110"><th class="cellrowborder" valign="top" width="15.17%" id="mcps1.2.5.1.1"><p id="p441275316217"><a name="p441275316217"></a><a name="p441275316217"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="20.27%" id="mcps1.2.5.1.2"><p id="p184128537213"><a name="p184128537213"></a><a name="p184128537213"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="12.120000000000001%" id="mcps1.2.5.1.3"><p id="p1141245342110"><a name="p1141245342110"></a><a name="p1141245342110"></a>Recommended Threshold</p>
</th>
<th class="cellrowborder" valign="top" width="52.44%" id="mcps1.2.5.1.4"><p id="p16478114516274"><a name="p16478114516274"></a><a name="p16478114516274"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row541355317219"><td class="cellrowborder" valign="top" width="15.17%" headers="mcps1.2.5.1.1 "><p id="p86158013230"><a name="p86158013230"></a><a name="p86158013230"></a>cpu_usage</p>
</td>
<td class="cellrowborder" valign="top" width="20.27%" headers="mcps1.2.5.1.2 "><p id="p441325310215"><a name="p441325310215"></a><a name="p441325310215"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.120000000000001%" headers="mcps1.2.5.1.3 "><p id="p8183201082618"><a name="p8183201082618"></a><a name="p8183201082618"></a>80</p>
</td>
<td class="cellrowborder" valign="top" width="52.44%" headers="mcps1.2.5.1.4 "><p id="p15478164511275"><a name="p15478164511275"></a><a name="p15478164511275"></a>CPU consumed by the monitored object</p>
<p id="p16141123993715"><a name="p16141123993715"></a><a name="p16141123993715"></a>The recommended threshold indicates that an alarm will be triggered when the CPU usage of the instance reaches 80% for the set number of consecutive periods during the monitoring period.</p>
<p id="p1818612207403"><a name="p1818612207403"></a><a name="p1818612207403"></a>For example, an alarm may be triggered if the average CPU usage ≥ 80% for 3 consecutive periods of 1 minute.</p>
</td>
</tr>
<tr id="row1941318532214"><td class="cellrowborder" valign="top" width="15.17%" headers="mcps1.2.5.1.1 "><p id="p1261617062311"><a name="p1261617062311"></a><a name="p1261617062311"></a>memory_usage</p>
</td>
<td class="cellrowborder" valign="top" width="20.27%" headers="mcps1.2.5.1.2 "><p id="p84131253112116"><a name="p84131253112116"></a><a name="p84131253112116"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.120000000000001%" headers="mcps1.2.5.1.3 "><p id="p10183131062619"><a name="p10183131062619"></a><a name="p10183131062619"></a>80</p>
</td>
<td class="cellrowborder" valign="top" width="52.44%" headers="mcps1.2.5.1.4 "><p id="p147834552712"><a name="p147834552712"></a><a name="p147834552712"></a>Memory consumed by the monitored object</p>
<p id="p75271234124415"><a name="p75271234124415"></a><a name="p75271234124415"></a>The recommended threshold indicates that an alarm will be triggered when the memory usage of the instance reaches 80% for the set number of consecutive periods during the monitoring period.</p>
<p id="p65271734154418"><a name="p65271734154418"></a><a name="p65271734154418"></a>For example, an alarm may be triggered if the average memory usage ≥ 80% for 3 consecutive periods of 1 minute.</p>
</td>
</tr>
<tr id="row74131853162115"><td class="cellrowborder" valign="top" width="15.17%" headers="mcps1.2.5.1.1 "><p id="p7616209239"><a name="p7616209239"></a><a name="p7616209239"></a>connected_clients</p>
</td>
<td class="cellrowborder" valign="top" width="20.27%" headers="mcps1.2.5.1.2 "><p id="p15414453132116"><a name="p15414453132116"></a><a name="p15414453132116"></a>Connected Clients</p>
</td>
<td class="cellrowborder" valign="top" width="12.120000000000001%" headers="mcps1.2.5.1.3 "><p id="p81835104269"><a name="p81835104269"></a><a name="p81835104269"></a>8,000</p>
</td>
<td class="cellrowborder" valign="top" width="52.44%" headers="mcps1.2.5.1.4 "><p id="p138933716469"><a name="p138933716469"></a><a name="p138933716469"></a>Number of connected clients (excluding those to standby nodes)</p>
<p id="p118626816914"><a name="p118626816914"></a><a name="p118626816914"></a>The minimum threshold is 8,000. Set the threshold to 80% of the maximum allowed connections indicated in the instance specifications.</p>
<p id="p1299371711316"><a name="p1299371711316"></a><a name="p1299371711316"></a>For example, an alarm may be triggered if the average number of connected clients ≥ 8,000 for 3 consecutive periods of 1 minute.</p>
</td>
</tr>
</tbody>
</table>

## Procedure<a name="section1118571110427"></a>

In the following example, an alarm rule is set for the  **Connected Clients \(connected\_clients\)**  metric.

1.  Log in to the DCS console.
2.  Click  ![](figures/project.png) in the upper left corner of the management console and select a region and a project.
3.  In the navigation pane, choose  **Cache Manager**.
4.  In the same row as the DCS instance whose metrics you want to view, click  **View Metric**.

    **Figure  1**  Viewing instance metrics<a name="fig1114294224611"></a>  
    ![](figures/viewing-instance-metrics.png "viewing-instance-metrics")

5.  On the displayed page, locate the  **Connected Clients**  metric. Hover over the metric and click  ![](figures/en-us_image_0232710455.png)  to create an alarm rule for the metric.

    The  **Create Alarm Rule**  page is displayed.

6.  Specify the alarm details.
    1.  Specify the alarm policy and alarm severity.

        For example, the alarm policy shown in  [Figure 2](#fig112961424225)  indicates that an alarm will be triggered if the average number of clients connected to the instance exceeds the preset value for two consecutive periods and no actions are taken.

        **Figure  2**  Setting the alarm policy and alarm severity<a name="fig112961424225"></a>  
        ![](figures/setting-the-alarm-policy-and-alarm-severity.png "setting-the-alarm-policy-and-alarm-severity")

    2.  Set the alarm notification configurations. If you enable  **Alarm Notification**, set the validity period, notification object, and trigger condition.
    3.  Click  **Next**  to set the alarm name and description.
    4.  Click  **Finish**.


