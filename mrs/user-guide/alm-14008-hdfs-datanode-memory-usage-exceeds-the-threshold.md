# ALM-14008 HDFS DataNode Memory Usage Exceeds the Threshold<a name="EN-US_TOPIC_0125375358"></a>

## Description<a name="sb13c1951be7c4a1691c10e96af88df0f"></a>

The system checks the HDFS DataNode memory usage every 30 seconds and compares it with the threshold. This alarm is generated when the HDFS DataNode memory usage exceeds the threshold and is cleared when it is less than or equal to the threshold.

## Attribute<a name="sc63ac2eff80948188ed5661cee0f96f2"></a>

<a name="en-us_topic_0035998727_table54967495"></a>
<table><thead align="left"><tr id="en-us_topic_0035998727_row29231803"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998727_p18965813"><a name="en-us_topic_0035998727_p18965813"></a><a name="en-us_topic_0035998727_p18965813"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998727_p59835867"><a name="en-us_topic_0035998727_p59835867"></a><a name="en-us_topic_0035998727_p59835867"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998727_p14867095"><a name="en-us_topic_0035998727_p14867095"></a><a name="en-us_topic_0035998727_p14867095"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998727_row63384014"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998727_p33831530"><a name="en-us_topic_0035998727_p33831530"></a><a name="en-us_topic_0035998727_p33831530"></a>14007</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998727_p55999443"><a name="en-us_topic_0035998727_p55999443"></a><a name="en-us_topic_0035998727_p55999443"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998727_p39661040"><a name="en-us_topic_0035998727_p39661040"></a><a name="en-us_topic_0035998727_p39661040"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sc64715726e20419693eb026a0eb8af55"></a>

<a name="en-us_topic_0035998727_table58427690"></a>
<table><thead align="left"><tr id="en-us_topic_0035998727_row29990828"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998727_p13338021"><a name="en-us_topic_0035998727_p13338021"></a><a name="en-us_topic_0035998727_p13338021"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998727_p6637886"><a name="en-us_topic_0035998727_p6637886"></a><a name="en-us_topic_0035998727_p6637886"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998727_row797855"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998727_p64626289"><a name="en-us_topic_0035998727_p64626289"></a><a name="en-us_topic_0035998727_p64626289"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998727_p238043"><a name="en-us_topic_0035998727_p238043"></a><a name="en-us_topic_0035998727_p238043"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998727_row2142393"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998727_p39316155"><a name="en-us_topic_0035998727_p39316155"></a><a name="en-us_topic_0035998727_p39316155"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998727_p30492010"><a name="en-us_topic_0035998727_p30492010"></a><a name="en-us_topic_0035998727_p30492010"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998727_row5992637"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998727_p15641626"><a name="en-us_topic_0035998727_p15641626"></a><a name="en-us_topic_0035998727_p15641626"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998727_p59012183"><a name="en-us_topic_0035998727_p59012183"></a><a name="en-us_topic_0035998727_p59012183"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998727_row61347601"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998727_p3099778"><a name="en-us_topic_0035998727_p3099778"></a><a name="en-us_topic_0035998727_p3099778"></a>Trigger condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998727_p49755431"><a name="en-us_topic_0035998727_p49755431"></a><a name="en-us_topic_0035998727_p49755431"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sfb5ab6df2ef2473c9e4664fb6da4d6f6"></a>

The HDFS DataNode memory usage is too high, which affects the data read/write performance of the HDFS.

## Possible Causes<a name="s367166161a394b02b899979ebada24f3"></a>

The HDFS DataNode memory is insufficient.

## Procedure<a name="s4980f24826094ca6966609680a3476e0"></a>

1.  Delete unnecessary files.
    1.  Use the client on the cluster node and run the  **hdfs dfs -rm -r** _file or directory_  command to delete unnecessary files.
    2.  Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l7af04ef094864b83b34d97121a58b12f).

2.  <a name="l7af04ef094864b83b34d97121a58b12f"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sd23f4023100841708f3407df4f0299c3"></a>

N/A

