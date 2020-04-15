# Key Operations on EVS<a name="en-us_topic_0100273731"></a>

Elastic Volume Service \(EVS\) is a scalable virtual block storage service that is based on the distributed architecture. EVS disks can be operated online. Using them is similar to using common server hard disks. Compared with common server hard disks, EVS disks have higher data reliability and I/O throughput capabilities. They are also easier to use. EVS disks apply to file systems, databases, or system software or other applications that require block storage devices.

With CTS, you can record operations associated with EVS for future query, audit, and backtrack operations.

**Table  1**  EVS operations that can be recorded by CTS

<a name="table61500354155120"></a>
<table><thead align="left"><tr id="r63f8e10b314d4c88ad59b123f419f647"><th class="cellrowborder" valign="top" width="31.633163316331636%" id="mcps1.2.4.1.1"><p id="a1d862653566d4c02969a15fda6de6802"><a name="a1d862653566d4c02969a15fda6de6802"></a><a name="a1d862653566d4c02969a15fda6de6802"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.592959295929592%" id="mcps1.2.4.1.2"><p id="ac7cea1b870e54220b7ad8937e61d8ce0"><a name="ac7cea1b870e54220b7ad8937e61d8ce0"></a><a name="ac7cea1b870e54220b7ad8937e61d8ce0"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.77387738773877%" id="mcps1.2.4.1.3"><p id="a6799aa916404462f992fad5c5acc7954"><a name="a6799aa916404462f992fad5c5acc7954"></a><a name="a6799aa916404462f992fad5c5acc7954"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="ra24e12a7930a4bb393727d5fa94c1323"><td class="cellrowborder" valign="top" width="31.633163316331636%" headers="mcps1.2.4.1.1 "><p id="a782de7e7204e40a58efb520fa20c6628"><a name="a782de7e7204e40a58efb520fa20c6628"></a><a name="a782de7e7204e40a58efb520fa20c6628"></a>Creating an EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="29.592959295929592%" headers="mcps1.2.4.1.2 "><p id="aa4d9f3fdede04b10b3961ec63a68c3bf"><a name="aa4d9f3fdede04b10b3961ec63a68c3bf"></a><a name="aa4d9f3fdede04b10b3961ec63a68c3bf"></a>evs</p>
</td>
<td class="cellrowborder" valign="top" width="38.77387738773877%" headers="mcps1.2.4.1.3 "><p id="a1d6161d5cd344931949cea70a75a7295"><a name="a1d6161d5cd344931949cea70a75a7295"></a><a name="a1d6161d5cd344931949cea70a75a7295"></a>createVolume</p>
</td>
</tr>
<tr id="r923c58ab76c04900a9eca9c60ec9d5cf"><td class="cellrowborder" valign="top" width="31.633163316331636%" headers="mcps1.2.4.1.1 "><p id="a7763b798879e4ae9bd3e062993ef739e"><a name="a7763b798879e4ae9bd3e062993ef739e"></a><a name="a7763b798879e4ae9bd3e062993ef739e"></a>Updating an EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="29.592959295929592%" headers="mcps1.2.4.1.2 "><p id="ae9ab1609cdf94f848c810a6d30d5d73b"><a name="ae9ab1609cdf94f848c810a6d30d5d73b"></a><a name="ae9ab1609cdf94f848c810a6d30d5d73b"></a>evs</p>
</td>
<td class="cellrowborder" valign="top" width="38.77387738773877%" headers="mcps1.2.4.1.3 "><p id="a4d8b92d46fc34bad81ad1e65eb4f36df"><a name="a4d8b92d46fc34bad81ad1e65eb4f36df"></a><a name="a4d8b92d46fc34bad81ad1e65eb4f36df"></a>updateVolume</p>
</td>
</tr>
<tr id="r439946ca7ec340a0b5a9ae1f0c23c943"><td class="cellrowborder" valign="top" width="31.633163316331636%" headers="mcps1.2.4.1.1 "><p id="aaf9d547084ee462493e9dda3a064e3b3"><a name="aaf9d547084ee462493e9dda3a064e3b3"></a><a name="aaf9d547084ee462493e9dda3a064e3b3"></a>Expanding an EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="29.592959295929592%" headers="mcps1.2.4.1.2 "><p id="ade70ae3339e541f7a3cb01b472c4f886"><a name="ade70ae3339e541f7a3cb01b472c4f886"></a><a name="ade70ae3339e541f7a3cb01b472c4f886"></a>evs</p>
</td>
<td class="cellrowborder" valign="top" width="38.77387738773877%" headers="mcps1.2.4.1.3 "><p id="a82341b08658945cf83cbe731680b8dcc"><a name="a82341b08658945cf83cbe731680b8dcc"></a><a name="a82341b08658945cf83cbe731680b8dcc"></a>extendVolume</p>
</td>
</tr>
<tr id="rc388ae6514db476b9b0063390752f179"><td class="cellrowborder" valign="top" width="31.633163316331636%" headers="mcps1.2.4.1.1 "><p id="aae3308590a5b42db9a66cde7de86dd19"><a name="aae3308590a5b42db9a66cde7de86dd19"></a><a name="aae3308590a5b42db9a66cde7de86dd19"></a>Deleting an EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="29.592959295929592%" headers="mcps1.2.4.1.2 "><p id="aff6b7c30f35b49bd9e446a7780c8b432"><a name="aff6b7c30f35b49bd9e446a7780c8b432"></a><a name="aff6b7c30f35b49bd9e446a7780c8b432"></a>evs</p>
</td>
<td class="cellrowborder" valign="top" width="38.77387738773877%" headers="mcps1.2.4.1.3 "><p id="ad81f9e98a54e452ea330b6887df6af71"><a name="ad81f9e98a54e452ea330b6887df6af71"></a><a name="ad81f9e98a54e452ea330b6887df6af71"></a>deleteVolume</p>
</td>
</tr>
</tbody>
</table>

