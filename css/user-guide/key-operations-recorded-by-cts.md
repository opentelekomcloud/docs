# Key Operations Recorded by CTS<a name="css_01_0050"></a>

Cloud Trace Service \(CTS\) is available on the public cloud platform. With CTS, you can record operations associated with CSS for later query, audit, and backtrack operations.

## Prerequisites<a name="section1294215503448"></a>

CTS has been enabled. For details, see  [Enabling CTS](https://docs.otc.t-systems.com/en-us/usermanual/cts/en-us_topic_0030598498.html).

## Key Operations Recorded by CTS<a name="section1929413643210"></a>

**Table  1**  Key operations recorded by CTS

<a name="table4269161914718"></a>
<table><thead align="left"><tr id="row1226931920470"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p1726971910478"><a name="p1726971910478"></a><a name="p1726971910478"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p18269101964712"><a name="p18269101964712"></a><a name="p18269101964712"></a>Resource Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p9269101924714"><a name="p9269101924714"></a><a name="p9269101924714"></a>Event Name</p>
</th>
</tr>
</thead>
<tbody><tr id="row9269191904711"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p119147155417"><a name="p119147155417"></a><a name="p119147155417"></a>Creating a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p119577547"><a name="p119577547"></a><a name="p119577547"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1914718543"><a name="p1914718543"></a><a name="p1914718543"></a>createCluster</p>
</td>
</tr>
<tr id="row202699195472"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1991478543"><a name="p1991478543"></a><a name="p1991478543"></a>Deleting a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p891579547"><a name="p891579547"></a><a name="p891579547"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p796710542"><a name="p796710542"></a><a name="p796710542"></a>deleteCluster</p>
</td>
</tr>
<tr id="row132691019134716"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4916711546"><a name="p4916711546"></a><a name="p4916711546"></a>Expanding cluster capacity</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p291473545"><a name="p291473545"></a><a name="p291473545"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14912717548"><a name="p14912717548"></a><a name="p14912717548"></a>growCluster</p>
</td>
</tr>
<tr id="row1226931910475"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p169107165416"><a name="p169107165416"></a><a name="p169107165416"></a>Restarting a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1899745419"><a name="p1899745419"></a><a name="p1899745419"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p209117205416"><a name="p209117205416"></a><a name="p209117205416"></a>rebootCluster</p>
</td>
</tr>
<tr id="row82091038523"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p620910345218"><a name="p620910345218"></a><a name="p620910345218"></a>Performing basic configurations for a cluster snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p720911335214"><a name="p720911335214"></a><a name="p720911335214"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p132091632524"><a name="p132091632524"></a><a name="p132091632524"></a>updateSnapshotPolicy</p>
</td>
</tr>
<tr id="row63504515528"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p93502505212"><a name="p93502505212"></a><a name="p93502505212"></a>Setting the automatic snapshot creation policy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1235016565220"><a name="p1235016565220"></a><a name="p1235016565220"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p535015165219"><a name="p535015165219"></a><a name="p535015165219"></a>updateAutoSnapshotPolicy</p>
</td>
</tr>
<tr id="row17755199175217"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p37552917527"><a name="p37552917527"></a><a name="p37552917527"></a>Manually creating a snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p375599115220"><a name="p375599115220"></a><a name="p375599115220"></a>snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p157553995215"><a name="p157553995215"></a><a name="p157553995215"></a>createSnapshot</p>
</td>
</tr>
<tr id="row597411148525"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4974151419527"><a name="p4974151419527"></a><a name="p4974151419527"></a>Restoring a snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p10999834177"><a name="p10999834177"></a><a name="p10999834177"></a>snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6974191416525"><a name="p6974191416525"></a><a name="p6974191416525"></a>restoreSnapshot</p>
</td>
</tr>
<tr id="row16412205214"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p66151220527"><a name="p66151220527"></a><a name="p66151220527"></a>Deleting a snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7701266177"><a name="p7701266177"></a><a name="p7701266177"></a>snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18631218522"><a name="p18631218522"></a><a name="p18631218522"></a>deleteSnapshot</p>
</td>
</tr>
</tbody>
</table>

