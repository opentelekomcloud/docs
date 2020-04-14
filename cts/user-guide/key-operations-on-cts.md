# Key Operations on CTS<a name="en-us_topic_0100273718"></a>

Cloud Trace Service \(CTS\) provides records of operations on cloud service resources. With CTS, you can query, audit, and backtrack these operations.

With CTS, you can record operations associated with CTS itself for future query, audit, and backtrack operations.

**Table  1**  CTS operations that can be recorded by itself

<a name="table63238500174222"></a>
<table><thead align="left"><tr id="re27d257dd2e54261bdd2bad18366d5ca"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="a3f247509a83247f1b880dbe2e886b80f"><a name="a3f247509a83247f1b880dbe2e886b80f"></a><a name="a3f247509a83247f1b880dbe2e886b80f"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="a0245ec2e020a40688b398368e1dc0a17"><a name="a0245ec2e020a40688b398368e1dc0a17"></a><a name="a0245ec2e020a40688b398368e1dc0a17"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="ae7c713d14c11489eb4eebc6e3084c94c"><a name="ae7c713d14c11489eb4eebc6e3084c94c"></a><a name="ae7c713d14c11489eb4eebc6e3084c94c"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rc1efa7cd98c44800b66e6cbf829fde69"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="a093e76c2ab06439797a5df0df7f517fa"><a name="a093e76c2ab06439797a5df0df7f517fa"></a><a name="a093e76c2ab06439797a5df0df7f517fa"></a>Creating a tracker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="a0f3f9a2392214c72810437225217a420"><a name="a0f3f9a2392214c72810437225217a420"></a><a name="a0f3f9a2392214c72810437225217a420"></a>tracker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="a48298e35398f4d8d9015bdb2ae6751f9"><a name="a48298e35398f4d8d9015bdb2ae6751f9"></a><a name="a48298e35398f4d8d9015bdb2ae6751f9"></a>createTracker</p>
</td>
</tr>
<tr id="r33a330fea67549aebab4e1b4777e3929"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="a2056d89fed61443b8777e19f6e0028ff"><a name="a2056d89fed61443b8777e19f6e0028ff"></a><a name="a2056d89fed61443b8777e19f6e0028ff"></a>Modifying a tracker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="a6914f69a89074a628c055aac4f0ec552"><a name="a6914f69a89074a628c055aac4f0ec552"></a><a name="a6914f69a89074a628c055aac4f0ec552"></a>tracker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="ab55bc19da8f546e3919f2efa35c52e3a"><a name="ab55bc19da8f546e3919f2efa35c52e3a"></a><a name="ab55bc19da8f546e3919f2efa35c52e3a"></a>updateTracker</p>
</td>
</tr>
<tr id="r3647b6c907494f3b82cd27196c0a389e"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="aae59d219afa848efb71fc81bb3ab02a2"><a name="aae59d219afa848efb71fc81bb3ab02a2"></a><a name="aae59d219afa848efb71fc81bb3ab02a2"></a>Disabling a tracker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="a1206f896ddb546d28fcd2b3995288520"><a name="a1206f896ddb546d28fcd2b3995288520"></a><a name="a1206f896ddb546d28fcd2b3995288520"></a>tracker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="a750b33742ab545719f025ec8535d63ef"><a name="a750b33742ab545719f025ec8535d63ef"></a><a name="a750b33742ab545719f025ec8535d63ef"></a>updateTracker</p>
</td>
</tr>
<tr id="rcc2259b6872449ea8af164fe51dacf9c"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="aacdd14e2ea554fa5a779bcf9155ae41e"><a name="aacdd14e2ea554fa5a779bcf9155ae41e"></a><a name="aacdd14e2ea554fa5a779bcf9155ae41e"></a>Enabling a tracker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240417_p743622217439"><a name="en-us_topic_0100240417_p743622217439"></a><a name="en-us_topic_0100240417_p743622217439"></a>tracker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="a492206b831c2434faa38193b50068d7c"><a name="a492206b831c2434faa38193b50068d7c"></a><a name="a492206b831c2434faa38193b50068d7c"></a>updateTracker</p>
</td>
</tr>
<tr id="r5d52d4bfc1614b59a1b5d5462b633321"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="a668b7566b2564fa1b8bdcbeda4983c8d"><a name="a668b7566b2564fa1b8bdcbeda4983c8d"></a><a name="a668b7566b2564fa1b8bdcbeda4983c8d"></a>Deleting a tracker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="a8a0b57b2730045c9b1d0afc62a5abcab"><a name="a8a0b57b2730045c9b1d0afc62a5abcab"></a><a name="a8a0b57b2730045c9b1d0afc62a5abcab"></a>tracker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="aab4b98cef4c24f5490bebe94f4d22dd4"><a name="aab4b98cef4c24f5490bebe94f4d22dd4"></a><a name="aab4b98cef4c24f5490bebe94f4d22dd4"></a>deleteTracker</p>
</td>
</tr>
</tbody>
</table>

