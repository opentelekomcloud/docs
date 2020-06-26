# ALM-12035 Unknown Data Status After Recovery Task Failure<a name="EN-US_TOPIC_0125376054"></a>

## Description<a name="sa00398fd751c4b06bcc5ce580b941a12"></a>

If a recovery task fails, the system automatically rolls back. If the rollback fails, data may be lost. When this occurs, an alarm is generated. This alarm is cleared when the next recovery task is executed successfully.

## Attribute<a name="s7981bd31788044e48d405f4d44217a1d"></a>

<a name="t882bfffbdd1c496d9a59c54264c9fb83"></a>
<table><thead align="left"><tr id="ree922f78407b474fa15d7bb27fde0cd7"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a49417dde673646b9b31c9df5aaabdf1b"><a name="a49417dde673646b9b31c9df5aaabdf1b"></a><a name="a49417dde673646b9b31c9df5aaabdf1b"></a><strong id="a0f534bcbea7c4f85857b4e660944c9cc"><a name="a0f534bcbea7c4f85857b4e660944c9cc"></a><a name="a0f534bcbea7c4f85857b4e660944c9cc"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="ab71b5243daa5444891f449d015434ef0"><a name="ab71b5243daa5444891f449d015434ef0"></a><a name="ab71b5243daa5444891f449d015434ef0"></a><strong id="a59ecd706f88d4dd182bad90b20a26d31"><a name="a59ecd706f88d4dd182bad90b20a26d31"></a><a name="a59ecd706f88d4dd182bad90b20a26d31"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035512809_p829466511461"><a name="en-us_topic_0035512809_p829466511461"></a><a name="en-us_topic_0035512809_p829466511461"></a><strong id="en-us_topic_0035512809_b754312911461"><a name="en-us_topic_0035512809_b754312911461"></a><a name="en-us_topic_0035512809_b754312911461"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r1b7ceee183e9413ebbedc2b8c6df3bb4"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a67b0e74c803f461d9a7b234a19311641"><a name="a67b0e74c803f461d9a7b234a19311641"></a><a name="a67b0e74c803f461d9a7b234a19311641"></a>12035</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="acbb2f39bae3242de9d309c095328b8de"><a name="acbb2f39bae3242de9d309c095328b8de"></a><a name="acbb2f39bae3242de9d309c095328b8de"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="ab02e95df7bff43fa91628dd8cd39e256"><a name="ab02e95df7bff43fa91628dd8cd39e256"></a><a name="ab02e95df7bff43fa91628dd8cd39e256"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="se665858007c147bd941f5f1da63a0b4b"></a>

<a name="t9df683d81c72438f998825c247c1354c"></a>
<table><thead align="left"><tr id="r2708269c45e04c3ba7fbcd546e3b0fc6"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="ac3ba6e4c6fa34fd6a8e5899a56afd2df"><a name="ac3ba6e4c6fa34fd6a8e5899a56afd2df"></a><a name="ac3ba6e4c6fa34fd6a8e5899a56afd2df"></a><strong id="a332deb4386274acab3a20485fa866d91"><a name="a332deb4386274acab3a20485fa866d91"></a><a name="a332deb4386274acab3a20485fa866d91"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a37cb5fe6fde54a43ab54fe3bae40efff"><a name="a37cb5fe6fde54a43ab54fe3bae40efff"></a><a name="a37cb5fe6fde54a43ab54fe3bae40efff"></a><strong id="a60c90f6a05744d2ca316b885b0fdd00e"><a name="a60c90f6a05744d2ca316b885b0fdd00e"></a><a name="a60c90f6a05744d2ca316b885b0fdd00e"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rbbad4af095d74c32bb416e90ccc00935"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab1c637c099ff43f09c4793bce0e7da85"><a name="ab1c637c099ff43f09c4793bce0e7da85"></a><a name="ab1c637c099ff43f09c4793bce0e7da85"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aef105938f70d4cbc86ef78800b9375de"><a name="aef105938f70d4cbc86ef78800b9375de"></a><a name="aef105938f70d4cbc86ef78800b9375de"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rb23e99b11fe84ffe978a1cae780236f5"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aed7c3ec501f84cb49146d799719fa399"><a name="aed7c3ec501f84cb49146d799719fa399"></a><a name="aed7c3ec501f84cb49146d799719fa399"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a1f0c7ea64aae45c8a11f9ed3dfd3862c"><a name="a1f0c7ea64aae45c8a11f9ed3dfd3862c"></a><a name="a1f0c7ea64aae45c8a11f9ed3dfd3862c"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rf4c087ae8cef41e5aa19131ce1184339"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a065e1d6e981e4df48853e9afa071787f"><a name="a065e1d6e981e4df48853e9afa071787f"></a><a name="a065e1d6e981e4df48853e9afa071787f"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a2f04f9bce24640e2a8a43c32b06015f2"><a name="a2f04f9bce24640e2a8a43c32b06015f2"></a><a name="a2f04f9bce24640e2a8a43c32b06015f2"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="ra45ad8686a0d41bba2607991a1c56426"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a75eae777435a4c4f80a6129bf8d2cd5e"><a name="a75eae777435a4c4f80a6129bf8d2cd5e"></a><a name="a75eae777435a4c4f80a6129bf8d2cd5e"></a>TaskName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035512809_p829733711461"><a name="en-us_topic_0035512809_p829733711461"></a><a name="en-us_topic_0035512809_p829733711461"></a>Specifies the task.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s1b3e4f1828ad46b1b2c67927c73226e5"></a>

Data may be lost or the data status may be unknown, both of which may affect services.

## Possible Causes<a name="se450ceeb1cde41d39f91abfa5f5f7c5e"></a>

The alarm cause depends on the task details. Handle the alarm according to the logs and alarm details.

## Procedure<a name="sbd627995cd2e4a5e8a98445c95e8a3d6"></a>

Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="sf972df0225f84ee49aa6e2bbf7b46fed"></a>

N/A

