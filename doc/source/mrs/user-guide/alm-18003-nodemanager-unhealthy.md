# ALM-18003 NodeManager Unhealthy<a name="EN-US_TOPIC_0125375681"></a>

## Description<a name="s8a6a0eeae1e8483b8b5f7d7b398d03e2"></a>

The system checks the number of abnormal NodeManager nodes every 30 seconds and compares the number with the threshold. This alarm is generated when the value of the  **Unhealthy Nodes**  indicator exceeds the threshold and is cleared when the value is less than or equal to the threshold.

## Attribute<a name="scd996379543a477eb59f966da859a2c1"></a>

<a name="en-us_topic_0035998738_table8146160"></a>
<table><thead align="left"><tr id="en-us_topic_0035998738_row10966323"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998738_p15856984"><a name="en-us_topic_0035998738_p15856984"></a><a name="en-us_topic_0035998738_p15856984"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998738_p9347313"><a name="en-us_topic_0035998738_p9347313"></a><a name="en-us_topic_0035998738_p9347313"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998738_p18934887"><a name="en-us_topic_0035998738_p18934887"></a><a name="en-us_topic_0035998738_p18934887"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998738_row57330849"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998738_p13287175"><a name="en-us_topic_0035998738_p13287175"></a><a name="en-us_topic_0035998738_p13287175"></a>18003</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998738_p2519427"><a name="en-us_topic_0035998738_p2519427"></a><a name="en-us_topic_0035998738_p2519427"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998738_p2747002"><a name="en-us_topic_0035998738_p2747002"></a><a name="en-us_topic_0035998738_p2747002"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s75ee13de4611475a8c6168d60e6e65ea"></a>

<a name="en-us_topic_0035998738_table21180630"></a>
<table><thead align="left"><tr id="en-us_topic_0035998738_row54284994"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998738_p35008393"><a name="en-us_topic_0035998738_p35008393"></a><a name="en-us_topic_0035998738_p35008393"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998738_p17107576"><a name="en-us_topic_0035998738_p17107576"></a><a name="en-us_topic_0035998738_p17107576"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998738_row43536440"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998738_p36790769"><a name="en-us_topic_0035998738_p36790769"></a><a name="en-us_topic_0035998738_p36790769"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998738_p27262282"><a name="en-us_topic_0035998738_p27262282"></a><a name="en-us_topic_0035998738_p27262282"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998738_row44033946"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998738_p9979846"><a name="en-us_topic_0035998738_p9979846"></a><a name="en-us_topic_0035998738_p9979846"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998738_p3061223"><a name="en-us_topic_0035998738_p3061223"></a><a name="en-us_topic_0035998738_p3061223"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998738_row27551015"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998738_p17039762"><a name="en-us_topic_0035998738_p17039762"></a><a name="en-us_topic_0035998738_p17039762"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998738_p38043494"><a name="en-us_topic_0035998738_p38043494"></a><a name="en-us_topic_0035998738_p38043494"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998738_row6847126"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998738_p17746329"><a name="en-us_topic_0035998738_p17746329"></a><a name="en-us_topic_0035998738_p17746329"></a>Trigger condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998738_p28166553"><a name="en-us_topic_0035998738_p28166553"></a><a name="en-us_topic_0035998738_p28166553"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sa9047c17a16b4e44ba9fcc6eb0e07932"></a>

-   The faulty NodeManager node cannot provide the Yarn service.
-   The number of containers decreases, so the cluster performance deteriorates.

## Possible Causes<a name="sa1fe6b05d73348f7a19b90264eb108ee"></a>

-   The hard disk space of the host where the NodeManager node resides is insufficient.
-   User  **omm**  does not have the permission to access a local directory on the NodeManager node.

## Procedure<a name="s7cff84894f3a41efb3a239919eca3a36"></a>

Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s2db724508e324a488d0efb28fe4145cb"></a>

N/A

