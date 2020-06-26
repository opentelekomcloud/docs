# ALM-14001 HDFS Disk Usage Exceeds the Threshold<a name="EN-US_TOPIC_0125375625"></a>

## Description<a name="s88945d9f27ac4490b53c50f051eb127e"></a>

The system checks the disk usage of the HDFS cluster every 30 seconds and compares it with the threshold. This alarm is generated when the HDFS disk usage exceeds the threshold and is cleared when the usage is less than or equal to the threshold.

## Attribute<a name="se8bba850550b414db5d60265ee24e62a"></a>

<a name="en-us_topic_0035998721_table48889850"></a>
<table><thead align="left"><tr id="en-us_topic_0035998721_row1927776"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998721_p21932166"><a name="en-us_topic_0035998721_p21932166"></a><a name="en-us_topic_0035998721_p21932166"></a><strong id="ae793ee3150914229a694860018380a9d"><a name="ae793ee3150914229a694860018380a9d"></a><a name="ae793ee3150914229a694860018380a9d"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998721_p31674992"><a name="en-us_topic_0035998721_p31674992"></a><a name="en-us_topic_0035998721_p31674992"></a><strong id="a387108cbc23c442f9af8c3a100b9fba9"><a name="a387108cbc23c442f9af8c3a100b9fba9"></a><a name="a387108cbc23c442f9af8c3a100b9fba9"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998721_p15537542"><a name="en-us_topic_0035998721_p15537542"></a><a name="en-us_topic_0035998721_p15537542"></a><strong id="en-us_topic_0035998721_b496917125439"><a name="en-us_topic_0035998721_b496917125439"></a><a name="en-us_topic_0035998721_b496917125439"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998721_row50581426"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998721_p3454809"><a name="en-us_topic_0035998721_p3454809"></a><a name="en-us_topic_0035998721_p3454809"></a>14001</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998721_p11404133"><a name="en-us_topic_0035998721_p11404133"></a><a name="en-us_topic_0035998721_p11404133"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998721_p51319614"><a name="en-us_topic_0035998721_p51319614"></a><a name="en-us_topic_0035998721_p51319614"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s099bf41c1ebb43b59badc89e2b60d1ae"></a>

<a name="en-us_topic_0035998721_table63248075"></a>
<table><thead align="left"><tr id="en-us_topic_0035998721_row60232767"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998721_p47015983"><a name="en-us_topic_0035998721_p47015983"></a><a name="en-us_topic_0035998721_p47015983"></a><strong id="aeb3076423bc8420bb0aa8c6a13d6086b"><a name="aeb3076423bc8420bb0aa8c6a13d6086b"></a><a name="aeb3076423bc8420bb0aa8c6a13d6086b"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998721_p50198296"><a name="en-us_topic_0035998721_p50198296"></a><a name="en-us_topic_0035998721_p50198296"></a><strong id="a453cb4591cee41328a5978da8d7f52bc"><a name="a453cb4591cee41328a5978da8d7f52bc"></a><a name="a453cb4591cee41328a5978da8d7f52bc"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998721_row39530145"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998721_p47825138"><a name="en-us_topic_0035998721_p47825138"></a><a name="en-us_topic_0035998721_p47825138"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998721_p48630964"><a name="en-us_topic_0035998721_p48630964"></a><a name="en-us_topic_0035998721_p48630964"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998721_row35025494"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998721_p18492804"><a name="en-us_topic_0035998721_p18492804"></a><a name="en-us_topic_0035998721_p18492804"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998721_p21522166"><a name="en-us_topic_0035998721_p21522166"></a><a name="en-us_topic_0035998721_p21522166"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998721_row59481773"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998721_p53294272"><a name="en-us_topic_0035998721_p53294272"></a><a name="en-us_topic_0035998721_p53294272"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998721_p21868813"><a name="en-us_topic_0035998721_p21868813"></a><a name="en-us_topic_0035998721_p21868813"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998721_row62601592"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998721_p37564172"><a name="en-us_topic_0035998721_p37564172"></a><a name="en-us_topic_0035998721_p37564172"></a>NSName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998721_p22799085"><a name="en-us_topic_0035998721_p22799085"></a><a name="en-us_topic_0035998721_p22799085"></a>Specifies the NameService service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998721_row3865173"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998721_p44643603"><a name="en-us_topic_0035998721_p44643603"></a><a name="en-us_topic_0035998721_p44643603"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998721_p59362130"><a name="en-us_topic_0035998721_p59362130"></a><a name="en-us_topic_0035998721_p59362130"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s54e6d21f79a249858b45f852650b1f1c"></a>

The performance of writing data to HDFS is affected.

## Possible Causes<a name="s882202240d134efeb4035ba2cea96a26"></a>

The disk space configured for the HDFS cluster is insufficient.

## Procedure<a name="se6d84c2765444da89c90a3bfd7cecd8e"></a>

1.  Check the disk capacity and delete unnecessary files.
    1.  On the MRS Manager portal, choose  **Service**  \>  **HDFS**. The **Service Status**  page is displayed.
    2.  In the  **Real-Time Statistics**  area, view the value of the monitoring indicator **Percentage of HDFS Capacity**  to check whether the HDFS disk usage exceeds the threshold.
        -   If yes, go to  [1.c](#laa3b4f62b38449b69c3ebad35f03dd44).
        -   If no, go to  [3](#lf12cd82625ea434b8743bad865b1dc69).

    3.  <a name="laa3b4f62b38449b69c3ebad35f03dd44"></a>Use the client on the cluster node and run the  **hdfs dfsadmin -report** command to check whether the value of **DFS Used%**  is less than 100% minus the threshold.
        -   If yes, go to  [1.e](#en-us_topic_0035998721_li39567352).
        -   If no, go to  [3](#lf12cd82625ea434b8743bad865b1dc69).

    4.  Use the client on the cluster node and run the  **hdfs dfs -rm -r** _file or directory_  command to delete unnecessary files.
    5.  <a name="en-us_topic_0035998721_li39567352"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#ldf057b85e7b3461a804168d003659f42).

2.  Expand the system.
    1.  <a name="ldf057b85e7b3461a804168d003659f42"></a>Expand the disk capacity.
    2.  Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#lf12cd82625ea434b8743bad865b1dc69).

3.  <a name="lf12cd82625ea434b8743bad865b1dc69"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s4c2f5e25db70426fa637e7591b4261ed"></a>

N/A

