# Region-level Key Operations on DNS<a name="en-us_topic_0100273730"></a>

Domain Name Service \(DNS\) provides highly available and scalable authoritative DNS services and domain name management services. It translates domain names or application resources into IP addresses required for network connection. By doing so, visitors' access requests are directed to the desired resources.

With CTS, you can record operations associated with DNS for future query, audit, and backtrack operations.

**Table  1**  DNS operations that can be recorded by CTS \(region level\)

<a name="table3646706020219"></a>
<table><thead align="left"><tr id="rb726b6aee1ac4c0a9d2c0025d07aecbc"><th class="cellrowborder" valign="top" width="31.069999999999997%" id="mcps1.2.4.1.1"><p id="a1bd2503f2e2a4ff79939521ed09e59f9"><a name="a1bd2503f2e2a4ff79939521ed09e59f9"></a><a name="a1bd2503f2e2a4ff79939521ed09e59f9"></a><strong id="en-us_topic_0100240334_b892053810028"><a name="en-us_topic_0100240334_b892053810028"></a><a name="en-us_topic_0100240334_b892053810028"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.189999999999998%" id="mcps1.2.4.1.2"><p id="a5f9ab9b3e88c4a70b7a2131f7b92a698"><a name="a5f9ab9b3e88c4a70b7a2131f7b92a698"></a><a name="a5f9ab9b3e88c4a70b7a2131f7b92a698"></a><strong id="a2df4de945bce4442b3ae7e489ab8c02d"><a name="a2df4de945bce4442b3ae7e489ab8c02d"></a><a name="a2df4de945bce4442b3ae7e489ab8c02d"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.739999999999995%" id="mcps1.2.4.1.3"><p id="en-us_topic_0109830566_p135581045200"><a name="en-us_topic_0109830566_p135581045200"></a><a name="en-us_topic_0109830566_p135581045200"></a><strong id="en-us_topic_0100240334_b872073010028"><a name="en-us_topic_0100240334_b872073010028"></a><a name="en-us_topic_0100240334_b872073010028"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r0847bbc5974b43b2b94a720d15b8b78c"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p856019451504"><a name="en-us_topic_0109830566_p856019451504"></a><a name="en-us_topic_0109830566_p856019451504"></a>Creating a private record set</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="a14faa2e9489c48f88416f7b32990c6f9"><a name="a14faa2e9489c48f88416f7b32990c6f9"></a><a name="a14faa2e9489c48f88416f7b32990c6f9"></a>privateRecordSet</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="a8867e4975b444793b33581ced965a4cb"><a name="a8867e4975b444793b33581ced965a4cb"></a><a name="a8867e4975b444793b33581ced965a4cb"></a>createPrivateRecordSet</p>
</td>
</tr>
<tr id="r118b8884fbcf4c659ea1be477106f656"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p75601745709"><a name="en-us_topic_0109830566_p75601745709"></a><a name="en-us_topic_0109830566_p75601745709"></a>Deleting a private record set</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p956219451003"><a name="en-us_topic_0109830566_p956219451003"></a><a name="en-us_topic_0109830566_p956219451003"></a>privateRecordSet</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p25621245809"><a name="en-us_topic_0109830566_p25621245809"></a><a name="en-us_topic_0109830566_p25621245809"></a>deletePrivateRecordSet</p>
</td>
</tr>
<tr id="r090476a65a654a2fb8bb08b71ea86a16"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="a48e4be6368524414956177114c481526"><a name="a48e4be6368524414956177114c481526"></a><a name="a48e4be6368524414956177114c481526"></a>Modifying a private record set</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p456214516014"><a name="en-us_topic_0109830566_p456214516014"></a><a name="en-us_topic_0109830566_p456214516014"></a>privateRecordSet</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="a072d3610966d417f83ca2b8fa7dcfa58"><a name="a072d3610966d417f83ca2b8fa7dcfa58"></a><a name="a072d3610966d417f83ca2b8fa7dcfa58"></a>updatePrivateRecordSet</p>
</td>
</tr>
<tr id="r13a4542db4ba4f26999d3d5136450b13"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p756214455020"><a name="en-us_topic_0109830566_p756214455020"></a><a name="en-us_topic_0109830566_p756214455020"></a>Creating a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p15562745909"><a name="en-us_topic_0109830566_p15562745909"></a><a name="en-us_topic_0109830566_p15562745909"></a>privateZone</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="af172d9d4477a4278bb4b3b3d4a829fa6"><a name="af172d9d4477a4278bb4b3b3d4a829fa6"></a><a name="af172d9d4477a4278bb4b3b3d4a829fa6"></a>createPrivateZone</p>
</td>
</tr>
<tr id="re01bce5e0a8c47439994f89914c19b47"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="abae20bf8eb3544eab9ca45961816ebb1"><a name="abae20bf8eb3544eab9ca45961816ebb1"></a><a name="abae20bf8eb3544eab9ca45961816ebb1"></a>Modifying a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p256319451408"><a name="en-us_topic_0109830566_p256319451408"></a><a name="en-us_topic_0109830566_p256319451408"></a>privateZone</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p75634451509"><a name="en-us_topic_0109830566_p75634451509"></a><a name="en-us_topic_0109830566_p75634451509"></a>updatePrivateZone</p>
</td>
</tr>
<tr id="rfd07d4244f82416d89d73c1ebbbf3c46"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p556317451301"><a name="en-us_topic_0109830566_p556317451301"></a><a name="en-us_topic_0109830566_p556317451301"></a>Deleting a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p756424514014"><a name="en-us_topic_0109830566_p756424514014"></a><a name="en-us_topic_0109830566_p756424514014"></a>privateZone</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="abe54261b6ba7457c99817c8ebe99c39c"><a name="abe54261b6ba7457c99817c8ebe99c39c"></a><a name="abe54261b6ba7457c99817c8ebe99c39c"></a>deletePrivateZone</p>
</td>
</tr>
<tr id="r6f03cec454b749b3a13064019f231256"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p25648451403"><a name="en-us_topic_0109830566_p25648451403"></a><a name="en-us_topic_0109830566_p25648451403"></a>Associating a VPC</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="a338cfd647384483289ffe45dc271205e"><a name="a338cfd647384483289ffe45dc271205e"></a><a name="a338cfd647384483289ffe45dc271205e"></a>privateZone</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="aa730386e6a2440c5b80750a23eb6a9e3"><a name="aa730386e6a2440c5b80750a23eb6a9e3"></a><a name="aa730386e6a2440c5b80750a23eb6a9e3"></a>associateRouter</p>
</td>
</tr>
<tr id="re9369e1003074ffc988f3f9dc1dbcd19"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p15653451706"><a name="en-us_topic_0109830566_p15653451706"></a><a name="en-us_topic_0109830566_p15653451706"></a>Disassociating a VPC</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p456620451002"><a name="en-us_topic_0109830566_p456620451002"></a><a name="en-us_topic_0109830566_p456620451002"></a>privateZone</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="abb37f3362f8543fe9d2df5a02a03ade1"><a name="abb37f3362f8543fe9d2df5a02a03ade1"></a><a name="abb37f3362f8543fe9d2df5a02a03ade1"></a>disassociateRouter</p>
</td>
</tr>
<tr id="en-us_topic_0109830566_row0566945604"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p156634515019"><a name="en-us_topic_0109830566_p156634515019"></a><a name="en-us_topic_0109830566_p156634515019"></a>Configuring a PTR record</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="ae4c74ac092094eeca6a09c6756cd7259"><a name="ae4c74ac092094eeca6a09c6756cd7259"></a><a name="ae4c74ac092094eeca6a09c6756cd7259"></a>ptrRecord</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p85671845404"><a name="en-us_topic_0109830566_p85671845404"></a><a name="en-us_topic_0109830566_p85671845404"></a>setPTRRecord</p>
</td>
</tr>
<tr id="r708cb653f11a463492f0893c08e66ae4"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p18567745501"><a name="en-us_topic_0109830566_p18567745501"></a><a name="en-us_topic_0109830566_p18567745501"></a>Restoring a PTR record</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p456854512013"><a name="en-us_topic_0109830566_p456854512013"></a><a name="en-us_topic_0109830566_p456854512013"></a>ptrRecord</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="a6e2ff69f09344d019b8477918cf5478f"><a name="a6e2ff69f09344d019b8477918cf5478f"></a><a name="a6e2ff69f09344d019b8477918cf5478f"></a>resetPTRRecord</p>
</td>
</tr>
</tbody>
</table>

