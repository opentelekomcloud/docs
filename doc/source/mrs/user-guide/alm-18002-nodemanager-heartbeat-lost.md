# ALM-18002 NodeManager Heartbeat Lost<a name="EN-US_TOPIC_0125375385"></a>

## Description<a name="s11c341269985462b95b9e014a79a3a80"></a>

The system checks the number of lost NodeManager nodes every 30 seconds and compares the number with the threshold. This alarm is generated when the value of the  **Lost Nodes**  indicator exceeds the threshold and is cleared when the value is less than or equal to the threshold.

## Attribute<a name="s270934954c8646c781df6e5c1fad404b"></a>

<a name="en-us_topic_0035998737_table65488131"></a>
<table><thead align="left"><tr id="en-us_topic_0035998737_row18827362"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998737_p48621330"><a name="en-us_topic_0035998737_p48621330"></a><a name="en-us_topic_0035998737_p48621330"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998737_p46013667"><a name="en-us_topic_0035998737_p46013667"></a><a name="en-us_topic_0035998737_p46013667"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998737_p36119548"><a name="en-us_topic_0035998737_p36119548"></a><a name="en-us_topic_0035998737_p36119548"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998737_row40002310"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998737_p18961705"><a name="en-us_topic_0035998737_p18961705"></a><a name="en-us_topic_0035998737_p18961705"></a>18002</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998737_p59503116"><a name="en-us_topic_0035998737_p59503116"></a><a name="en-us_topic_0035998737_p59503116"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998737_p55023063"><a name="en-us_topic_0035998737_p55023063"></a><a name="en-us_topic_0035998737_p55023063"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sf68ff60281704f84a14f3600dc6c39c9"></a>

<a name="en-us_topic_0035998737_table27683123"></a>
<table><thead align="left"><tr id="en-us_topic_0035998737_row23047586"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998737_p54915211"><a name="en-us_topic_0035998737_p54915211"></a><a name="en-us_topic_0035998737_p54915211"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998737_p18947112"><a name="en-us_topic_0035998737_p18947112"></a><a name="en-us_topic_0035998737_p18947112"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998737_row58321122"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998737_p26390432"><a name="en-us_topic_0035998737_p26390432"></a><a name="en-us_topic_0035998737_p26390432"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998737_p57250251"><a name="en-us_topic_0035998737_p57250251"></a><a name="en-us_topic_0035998737_p57250251"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998737_row45490212"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998737_p60828573"><a name="en-us_topic_0035998737_p60828573"></a><a name="en-us_topic_0035998737_p60828573"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998737_p28167350"><a name="en-us_topic_0035998737_p28167350"></a><a name="en-us_topic_0035998737_p28167350"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998737_row52179558"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998737_p65794642"><a name="en-us_topic_0035998737_p65794642"></a><a name="en-us_topic_0035998737_p65794642"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998737_p27765811"><a name="en-us_topic_0035998737_p27765811"></a><a name="en-us_topic_0035998737_p27765811"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998737_row48565715"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998737_p41508862"><a name="en-us_topic_0035998737_p41508862"></a><a name="en-us_topic_0035998737_p41508862"></a>Trigger condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998737_p6774674"><a name="en-us_topic_0035998737_p6774674"></a><a name="en-us_topic_0035998737_p6774674"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s86d6a012d5a24b13ae6e7f0159299fc0"></a>

-   The lost NodeManager node cannot provide the Yarn service.
-   The number of containers decreases, so the cluster performance deteriorates.

## Possible Causes<a name="s71f777d5e4d742b99363a755bd0b178f"></a>

-   NodeManager is forcibly deleted without decommission.
-   All NodeManager instances are stopped or the NodeManager process is faulty.
-   The host where the NodeManager node resides is faulty.
-   The network between the NodeManager and ResourceManager is disconnected or busy.

## Procedure<a name="s99ca0426600d49beb1edd42982fe7a0d"></a>

Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="sc2afa0a5b88b4c4cacadeae88ec0e348"></a>

N/A

