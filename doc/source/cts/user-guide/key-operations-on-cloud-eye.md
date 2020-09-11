# Key Operations on Cloud Eye<a name="en-us_topic_0100273719"></a>

Cloud Eye is an open monitoring platform. It provides monitoring, alarm reporting, and alarm notification for your resources in near-real time.

With CTS, you can record operations associated with Cloud Eye for future query, audit, and backtrack operations.

**Table  1**  Cloud Eye operations that can be recorded by CTS

<a name="table1775899155120"></a>
<table><thead align="left"><tr id="re4bb0c4ccc0c41b4ad9aa989f62a2e4a"><th class="cellrowborder" valign="top" width="35.18648135186481%" id="mcps1.2.4.1.1"><p id="ab645c14aa1d74278ac1cfefd40b4a8b6"><a name="ab645c14aa1d74278ac1cfefd40b4a8b6"></a><a name="ab645c14aa1d74278ac1cfefd40b4a8b6"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.247375262473753%" id="mcps1.2.4.1.2"><p id="aa2339cc4632c4ead8c4107912a5e707c"><a name="aa2339cc4632c4ead8c4107912a5e707c"></a><a name="aa2339cc4632c4ead8c4107912a5e707c"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.566143385661434%" id="mcps1.2.4.1.3"><p id="a2aa757d1273944c7b6216bec666b2f3e"><a name="a2aa757d1273944c7b6216bec666b2f3e"></a><a name="a2aa757d1273944c7b6216bec666b2f3e"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r45c19c3a6c9b4c10b28f269981812ed2"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="a076d3c1c2c5d4f0187a374668ad34e71"><a name="a076d3c1c2c5d4f0187a374668ad34e71"></a><a name="a076d3c1c2c5d4f0187a374668ad34e71"></a>Adding an alarm rule</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="a78db00863c3048ea8e1a43dc5767d2b1"><a name="a78db00863c3048ea8e1a43dc5767d2b1"></a><a name="a78db00863c3048ea8e1a43dc5767d2b1"></a>alarm_rule</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="a6d3556c4ac11485ab1bca3066f96c688"><a name="a6d3556c4ac11485ab1bca3066f96c688"></a><a name="a6d3556c4ac11485ab1bca3066f96c688"></a>createAlarmRule</p>
</td>
</tr>
<tr id="rc1b821b81b4546939fa046eb592088bd"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="a0cf0ced943fb4d39b95b2a18219eb5f5"><a name="a0cf0ced943fb4d39b95b2a18219eb5f5"></a><a name="a0cf0ced943fb4d39b95b2a18219eb5f5"></a>Deleting an alarm rule</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240417_p527404616850"><a name="en-us_topic_0100240417_p527404616850"></a><a name="en-us_topic_0100240417_p527404616850"></a>alarm_rule</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="afa395e73105144598f0c23ba2d180b31"><a name="afa395e73105144598f0c23ba2d180b31"></a><a name="afa395e73105144598f0c23ba2d180b31"></a>deleteAlarmRule</p>
</td>
</tr>
<tr id="r449e7e4483a84f949d8be8a5202283af"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="ad3ed555cca2a4ee6b3a81bb970b6605d"><a name="ad3ed555cca2a4ee6b3a81bb970b6605d"></a><a name="ad3ed555cca2a4ee6b3a81bb970b6605d"></a>Disabling an alarm rule</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="ab0560f80a8454100815f546914c7f372"><a name="ab0560f80a8454100815f546914c7f372"></a><a name="ab0560f80a8454100815f546914c7f372"></a>alarm_rule</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="af0ccd4ee7e214395966926a0fc5d2fd9"><a name="af0ccd4ee7e214395966926a0fc5d2fd9"></a><a name="af0ccd4ee7e214395966926a0fc5d2fd9"></a>disableAlarmRule</p>
</td>
</tr>
<tr id="r24c8d21a1d1645e9afd9f41a83993752"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="a5fac830a3a804861b0f945834d273074"><a name="a5fac830a3a804861b0f945834d273074"></a><a name="a5fac830a3a804861b0f945834d273074"></a>Enabling an alarm rule</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="a29347772e971469281cd4d3834aa7fea"><a name="a29347772e971469281cd4d3834aa7fea"></a><a name="a29347772e971469281cd4d3834aa7fea"></a>alarm_rule</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="ad815488064d7441ead7d3d7f7c2b575d"><a name="ad815488064d7441ead7d3d7f7c2b575d"></a><a name="ad815488064d7441ead7d3d7f7c2b575d"></a>enableAlarmRule</p>
</td>
</tr>
<tr id="rb9ae25d7cde44bb2b2352859314dbd14"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="aa43f2faf297f4be8af377b3a5f092f49"><a name="aa43f2faf297f4be8af377b3a5f092f49"></a><a name="aa43f2faf297f4be8af377b3a5f092f49"></a>Modifying an alarm rule</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="a9fcaf7121cb14e66b9cec89a2dd4054f"><a name="a9fcaf7121cb14e66b9cec89a2dd4054f"></a><a name="a9fcaf7121cb14e66b9cec89a2dd4054f"></a>alarm_rule</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="a6f9dc3b5041645dba953a40d6a3060c2"><a name="a6f9dc3b5041645dba953a40d6a3060c2"></a><a name="a6f9dc3b5041645dba953a40d6a3060c2"></a>updateAlarmRule</p>
</td>
</tr>
<tr id="r22a3b3fcc3fd42d4933612b426929db5"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="a9bf389ba936a425bb188092f7f69304b"><a name="a9bf389ba936a425bb188092f7f69304b"></a><a name="a9bf389ba936a425bb188092f7f69304b"></a>Updating the alarm status to alarm</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="a3352c9a3d533483e8e9eb3211ed77656"><a name="a3352c9a3d533483e8e9eb3211ed77656"></a><a name="a3352c9a3d533483e8e9eb3211ed77656"></a>alarm_rule</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="aaa1d8bf410b1425da08913c1089867ba"><a name="aaa1d8bf410b1425da08913c1089867ba"></a><a name="aaa1d8bf410b1425da08913c1089867ba"></a>alarmStatusChangeToAlarm</p>
</td>
</tr>
<tr id="r49271d810408442daeefe2e67542ccd8"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="ad05205bb252744f29b5abf006f69fecc"><a name="ad05205bb252744f29b5abf006f69fecc"></a><a name="ad05205bb252744f29b5abf006f69fecc"></a>Updating the alarm status to insufficient data</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="a0b15008ddc194893836b34ed7a47d5bd"><a name="a0b15008ddc194893836b34ed7a47d5bd"></a><a name="a0b15008ddc194893836b34ed7a47d5bd"></a>alarm_rule</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="ae0222442401341ed951586b53ce878c9"><a name="ae0222442401341ed951586b53ce878c9"></a><a name="ae0222442401341ed951586b53ce878c9"></a>alarmStatusChangeToInsufficientData</p>
</td>
</tr>
<tr id="rb5437663ae4848a9a94aa9394bde8bf3"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="acfab1737a4db403c81d690c555f03117"><a name="acfab1737a4db403c81d690c555f03117"></a><a name="acfab1737a4db403c81d690c555f03117"></a>Updating the alarm status to normal</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="a052dc38cb3af48b4bf90c0f15c795c09"><a name="a052dc38cb3af48b4bf90c0f15c795c09"></a><a name="a052dc38cb3af48b4bf90c0f15c795c09"></a>alarm_rule</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="a1d1133a8925d4e7eb7d54b046a1604f7"><a name="a1d1133a8925d4e7eb7d54b046a1604f7"></a><a name="a1d1133a8925d4e7eb7d54b046a1604f7"></a>alarmStatusChangeToOk</p>
</td>
</tr>
<tr id="r199ded59c7884da2adf41669eff2058f"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="ad824eceec88746b8b89e84656f00f7ed"><a name="ad824eceec88746b8b89e84656f00f7ed"></a><a name="ad824eceec88746b8b89e84656f00f7ed"></a>Creating a custom alarm template</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="a046829c7ff874eccada11426b7bc85c6"><a name="a046829c7ff874eccada11426b7bc85c6"></a><a name="a046829c7ff874eccada11426b7bc85c6"></a>alarm_template</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240417_p511277416859"><a name="en-us_topic_0100240417_p511277416859"></a><a name="en-us_topic_0100240417_p511277416859"></a>createAlarmTemplate</p>
</td>
</tr>
<tr id="re3d3c3e26b1c4819b212c0b3b303ecbc"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="ad51d9a5c0f3040f79f3049149b8dc481"><a name="ad51d9a5c0f3040f79f3049149b8dc481"></a><a name="ad51d9a5c0f3040f79f3049149b8dc481"></a>Deleting a custom alarm template</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240417_p962681516850"><a name="en-us_topic_0100240417_p962681516850"></a><a name="en-us_topic_0100240417_p962681516850"></a>alarm_template</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="a72133ed03acf423ca6f8b56670133774"><a name="a72133ed03acf423ca6f8b56670133774"></a><a name="a72133ed03acf423ca6f8b56670133774"></a>deleteAlarmTemplate</p>
</td>
</tr>
<tr id="rbab285d4151244f482f2aed99a321e9a"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240417_p913311516831"><a name="en-us_topic_0100240417_p913311516831"></a><a name="en-us_topic_0100240417_p913311516831"></a>Modifying a custom alarm template</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="a13ec85ea17504c9fa5046d0cd5b3645f"><a name="a13ec85ea17504c9fa5046d0cd5b3645f"></a><a name="a13ec85ea17504c9fa5046d0cd5b3645f"></a>alarm_template</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="a9a7f77ebc06c44e49263d75f138fd75e"><a name="a9a7f77ebc06c44e49263d75f138fd75e"></a><a name="a9a7f77ebc06c44e49263d75f138fd75e"></a>updateAlarmTemplate</p>
</td>
</tr>
<tr id="r77ed3659f6364c56b5a73252b9c60993"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="a396a15076aef4f90a2cbd9af85fa6076"><a name="a396a15076aef4f90a2cbd9af85fa6076"></a><a name="a396a15076aef4f90a2cbd9af85fa6076"></a>Creating a monitoring panel</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="a73d3d0ed60a04a59aacba741703af5a9"><a name="a73d3d0ed60a04a59aacba741703af5a9"></a><a name="a73d3d0ed60a04a59aacba741703af5a9"></a>dashboard</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240417_p848670116859"><a name="en-us_topic_0100240417_p848670116859"></a><a name="en-us_topic_0100240417_p848670116859"></a>createDashboard</p>
</td>
</tr>
<tr id="rd19fbcbd9ff440ae8beb0b5051fb5ab0"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="a8f4a591b775b4edcb4852c13f1d44050"><a name="a8f4a591b775b4edcb4852c13f1d44050"></a><a name="a8f4a591b775b4edcb4852c13f1d44050"></a>Deleting a monitoring panel</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240417_p633696916850"><a name="en-us_topic_0100240417_p633696916850"></a><a name="en-us_topic_0100240417_p633696916850"></a>dashboard</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="af1402bbd8c1f4c3ab7bceff7d04ce30f"><a name="af1402bbd8c1f4c3ab7bceff7d04ce30f"></a><a name="af1402bbd8c1f4c3ab7bceff7d04ce30f"></a>deleteDashboard</p>
</td>
</tr>
<tr id="rf6743f59f681451b806665672975d6da"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="a21971df3dc5f4c828deef47143b47942"><a name="a21971df3dc5f4c828deef47143b47942"></a><a name="a21971df3dc5f4c828deef47143b47942"></a>Modifying a monitoring panel</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="a388bc3abcca54b3c9ca7cfd3844521d6"><a name="a388bc3abcca54b3c9ca7cfd3844521d6"></a><a name="a388bc3abcca54b3c9ca7cfd3844521d6"></a>dashboard</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="af75148706abd4bfb86997cebab8617fe"><a name="af75148706abd4bfb86997cebab8617fe"></a><a name="af75148706abd4bfb86997cebab8617fe"></a>updateDashboard</p>
</td>
</tr>
<tr id="r0f620ec2293645bbbd83dd47610049f7"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="abccdf55793434f39994b859e337bff55"><a name="abccdf55793434f39994b859e337bff55"></a><a name="abccdf55793434f39994b859e337bff55"></a>Adding monitoring data</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240417_p151117716850"><a name="en-us_topic_0100240417_p151117716850"></a><a name="en-us_topic_0100240417_p151117716850"></a>metric</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="a6da4317eeb2240b2b8f0aa019cf77cec"><a name="a6da4317eeb2240b2b8f0aa019cf77cec"></a><a name="a6da4317eeb2240b2b8f0aa019cf77cec"></a>addMetricData</p>
</td>
</tr>
<tr id="r9289dc4b4dff4380a07ea30c8d99ed8e"><td class="cellrowborder" valign="top" width="35.18648135186481%" headers="mcps1.2.4.1.1 "><p id="a4708702f89684268af421358a7c0f685"><a name="a4708702f89684268af421358a7c0f685"></a><a name="a4708702f89684268af421358a7c0f685"></a>Exporting monitoring data</p>
</td>
<td class="cellrowborder" valign="top" width="26.247375262473753%" headers="mcps1.2.4.1.2 "><p id="a0845a41d264a46ef9fc32e273489459e"><a name="a0845a41d264a46ef9fc32e273489459e"></a><a name="a0845a41d264a46ef9fc32e273489459e"></a>metric</p>
</td>
<td class="cellrowborder" valign="top" width="38.566143385661434%" headers="mcps1.2.4.1.3 "><p id="abae2629aaa7b4fe999df0149fb21d838"><a name="abae2629aaa7b4fe999df0149fb21d838"></a><a name="abae2629aaa7b4fe999df0149fb21d838"></a>downloadMetricsReport</p>
</td>
</tr>
</tbody>
</table>

