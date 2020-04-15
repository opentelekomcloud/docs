# ALM-16002 Successful Hive SQL Operations Are Lower than the Threshold<a name="EN-US_TOPIC_0125375869"></a>

## Description<a name="se97c309d57ac4366bece7569caa52cd5"></a>

Every 30 seconds, the system checks the percentage of successfully executed HiveQL statements. Percentage of successfully executed HiveQL statements = Number of HiveQL statements successfully executed by Hive in a specified period/Total number of HiveQL statements executed by Hive. This indicator can be viewed on the Hive service monitoring page.

This alarm is generated when the percentage of successfully executed HiveQL statements is lower than the specified threshold and is cleared when the percentage is greater than or equal to the threshold.

The name of the host where the alarm is generated can be obtained from the alarm location information. The host IP address is the IP address of the HiveServer node.

## Attribute<a name="saf490d7a57e942d2803a9ccd6382895f"></a>

<a name="en-us_topic_0035998734_table9994955"></a>
<table><thead align="left"><tr id="en-us_topic_0035998734_row62312200"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998734_p14123440"><a name="en-us_topic_0035998734_p14123440"></a><a name="en-us_topic_0035998734_p14123440"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998734_p3148005"><a name="en-us_topic_0035998734_p3148005"></a><a name="en-us_topic_0035998734_p3148005"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998734_p53661838"><a name="en-us_topic_0035998734_p53661838"></a><a name="en-us_topic_0035998734_p53661838"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998734_row51641620"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998734_p22221662"><a name="en-us_topic_0035998734_p22221662"></a><a name="en-us_topic_0035998734_p22221662"></a>16002</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998734_p55124180"><a name="en-us_topic_0035998734_p55124180"></a><a name="en-us_topic_0035998734_p55124180"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998734_p35873632"><a name="en-us_topic_0035998734_p35873632"></a><a name="en-us_topic_0035998734_p35873632"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s1c1ec1f722a44470b03bfe107c691049"></a>

<a name="en-us_topic_0035998734_table20083047"></a>
<table><thead align="left"><tr id="en-us_topic_0035998734_row3150961"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998734_p53901255"><a name="en-us_topic_0035998734_p53901255"></a><a name="en-us_topic_0035998734_p53901255"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998734_p3925534"><a name="en-us_topic_0035998734_p3925534"></a><a name="en-us_topic_0035998734_p3925534"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998734_row49532829"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998734_p52736237"><a name="en-us_topic_0035998734_p52736237"></a><a name="en-us_topic_0035998734_p52736237"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998734_p43776822"><a name="en-us_topic_0035998734_p43776822"></a><a name="en-us_topic_0035998734_p43776822"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998734_row58447079"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998734_p36592919"><a name="en-us_topic_0035998734_p36592919"></a><a name="en-us_topic_0035998734_p36592919"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998734_p11236435"><a name="en-us_topic_0035998734_p11236435"></a><a name="en-us_topic_0035998734_p11236435"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998734_row34019058"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998734_p4080300"><a name="en-us_topic_0035998734_p4080300"></a><a name="en-us_topic_0035998734_p4080300"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998734_p62068903"><a name="en-us_topic_0035998734_p62068903"></a><a name="en-us_topic_0035998734_p62068903"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998734_row21749220"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998734_p16856419"><a name="en-us_topic_0035998734_p16856419"></a><a name="en-us_topic_0035998734_p16856419"></a>Trigger condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998734_p23192694"><a name="en-us_topic_0035998734_p23192694"></a><a name="en-us_topic_0035998734_p23192694"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s22bfb4b70ab8437ea8f899f0e494560f"></a>

The system configuration and performance cannot meet service processing requirements.

## Possible Causes<a name="s0340feeac0b84b78b056e25d363408df"></a>

-   A syntax error occurs in HiveQL commands.
-   The HBase service is abnormal when a Hive on HBase task is being performed.
-   Basic services that are depended on are abnormal, such as HDFS, Yarn, and ZooKeeper.

## Procedure<a name="sc3c12edc681c47ba9272ef053c82f8c6"></a>

1.  Check whether the HiveQL commands comply with syntax.
    1.  Use the Hive client to log in to the HiveServer node where the alarm is generated. Query the HiveQL syntax standard provided by Apache, and check whether the HiveQL commands are correct. For details, see https://cwiki.apache.org/confluence/display/hive/languagemanual.

        -   If yes, go to  [2.a](#en-us_topic_0035998734_step11).
        -   If no, go to  [1.b](#lc75f5e46a3e14bc88aa962575ac01ad6).

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >To view the user who runs an incorrect statement, download the HiveServerAudit logs of the HiveServer node where this alarm is generated. Set  **Start Time** and **End Time** to 10 minutes before and after the alarm generation time respectively. Open the log file and search for the **Result=FAIL**  keyword to filter the log information about the incorrect statement, and then view the user who runs the incorrect statement according to UserName in the log information.  

    2.  <a name="lc75f5e46a3e14bc88aa962575ac01ad6"></a>Enter correct HiveQL statements, and check whether the command can be properly executed.
        -   If yes, go to  [4.e](#en-us_topic_0035998734_step_6).
        -   If no, go to  [2.a](#en-us_topic_0035998734_step11).

2.  Check whether the HBase service is abnormal.
    1.  <a name="en-us_topic_0035998734_step11"></a>Check whether a Hive on HBase task is performed.
        -   If yes, go to  [2.b](#l7b1a3633e5134551a9d417445619442f).
        -   If no, go to  [3.a](#en-us_topic_0035998734_step22).

    2.  <a name="l7b1a3633e5134551a9d417445619442f"></a>Check whether the HBase service is in the normal state in the service list.
        -   If yes, go to  [3.a](#en-us_topic_0035998734_step22).
        -   If no, go to  [2.c](#l6155a7f24fee4320aaa96ec877b2ff30).

    3.  <a name="l6155a7f24fee4320aaa96ec877b2ff30"></a>Check the alarms displayed on the alarm page and clear them according to Alarm Help.
    4.  Enter correct HiveQL statements, and check whether the command can be properly executed.
        -   If yes, go to  [4.e](#en-us_topic_0035998734_step_6).
        -   If no, go to  [3.a](#en-us_topic_0035998734_step22).

3.  Check whether the Spark service is abnormal.
    1.  <a name="en-us_topic_0035998734_step22"></a>Check whether the Spark service is in the normal state in the service list.
        -   If yes, go to  [4.a](#l1c66fa3284424176a2ac2909d3e55837).
        -   If no, go to  [3.b](#en-us_topic_0035998734_step_25).

    2.  <a name="en-us_topic_0035998734_step_25"></a>Check the alarms displayed on the alarm page and clear them according to Alarm Help.
    3.  Enter correct HiveQL statements, and check whether the command can be properly executed.
        -   If yes, go to  [4.e](#en-us_topic_0035998734_step_6).
        -   If no, go to  [4.a](#l1c66fa3284424176a2ac2909d3e55837).

4.  Check whether HDFS, Yarn, and ZooKeeper are in the normal state.
    1.  <a name="l1c66fa3284424176a2ac2909d3e55837"></a>On the MRS Manager portal, click  **Service**.
    2.  In the service list, check whether the services, such as HDFS, Yarn, and ZooKeeper are in the normal state.
        -   If yes, go to  [4.e](#en-us_topic_0035998734_step_6).
        -   If no, go to  [4.c](#l9e31f264908d480389089d160f979dfe).

    3.  <a name="l9e31f264908d480389089d160f979dfe"></a>Check the alarms displayed on the alarm page and clear them according to Alarm Help.
    4.  Enter correct HiveQL statements, and check whether the command can be properly executed.
        -   If yes, go to  [4.e](#en-us_topic_0035998734_step_6).
        -   If no, go to  [5](#lb2a4c736d2884bbbac1c2a6a133aec1f).

    5.  <a name="en-us_topic_0035998734_step_6"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [5](#lb2a4c736d2884bbbac1c2a6a133aec1f).

5.  <a name="lb2a4c736d2884bbbac1c2a6a133aec1f"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s1f3bf7ec1ea34cbca10610a5392d1c82"></a>

N/A

