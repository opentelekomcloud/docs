# SFS Metrics<a name="EN-US_TOPIC_0171212583"></a>

## Function<a name="section48080847153328"></a>

This topic describes metrics reported by Scalable File Service \(SFS\) to Cloud Eye as well as their namespaces and dimensions. You can use APIs provided by Cloud Eye to query the metrics of the monitored object and alarms generated for SFS.

## Namespace<a name="section20110798153328"></a>

SYS.SFS

## Metrics<a name="section31039493153328"></a>

<a name="table31171041153328"></a>
<table><thead align="left"><tr id="row42397114153328"><th class="cellrowborder" valign="top" width="15.310000000000002%" id="mcps1.1.6.1.1"><p id="p11614228153328"><a name="p11614228153328"></a><a name="p11614228153328"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="16.33%" id="mcps1.1.6.1.2"><p id="p1228402153328"><a name="p1228402153328"></a><a name="p1228402153328"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="36.620000000000005%" id="mcps1.1.6.1.3"><p id="p32391741153328"><a name="p32391741153328"></a><a name="p32391741153328"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="17.27%" id="mcps1.1.6.1.4"><p id="p6485340153328"><a name="p6485340153328"></a><a name="p6485340153328"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="14.469999999999999%" id="mcps1.1.6.1.5"><p id="p58103874155224"><a name="p58103874155224"></a><a name="p58103874155224"></a>Monitored Object</p>
</th>
</tr>
</thead>
<tbody><tr id="row3298232153328"><td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.6.1.1 "><p id="p42751914173912"><a name="p42751914173912"></a><a name="p42751914173912"></a>read_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.1.6.1.2 "><p id="p1227531423917"><a name="p1227531423917"></a><a name="p1227531423917"></a>Read Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="36.620000000000005%" headers="mcps1.1.6.1.3 "><p id="p15275514113912"><a name="p15275514113912"></a><a name="p15275514113912"></a>Read bandwidth of the file system within a monitoring period</p>
<p id="p192563149569"><a name="p192563149569"></a><a name="p192563149569"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="17.27%" headers="mcps1.1.6.1.4 "><p id="p9072094155224"><a name="p9072094155224"></a><a name="p9072094155224"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.6.1.5 "><p id="p63750977155224"><a name="p63750977155224"></a><a name="p63750977155224"></a>File sharing</p>
</td>
</tr>
<tr id="row21884471153328"><td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.6.1.1 "><p id="p1527512146393"><a name="p1527512146393"></a><a name="p1527512146393"></a>write_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.1.6.1.2 "><p id="p0275161413911"><a name="p0275161413911"></a><a name="p0275161413911"></a>Write Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="36.620000000000005%" headers="mcps1.1.6.1.3 "><p id="p527691413398"><a name="p527691413398"></a><a name="p527691413398"></a>Write bandwidth of the file system within a monitoring period</p>
<p id="p267311455718"><a name="p267311455718"></a><a name="p267311455718"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="17.27%" headers="mcps1.1.6.1.4 "><p id="p05381407578"><a name="p05381407578"></a><a name="p05381407578"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.6.1.5 "><p id="p34127948155224"><a name="p34127948155224"></a><a name="p34127948155224"></a>File sharing</p>
</td>
</tr>
<tr id="row58957821154029"><td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.6.1.1 "><p id="p32761214133911"><a name="p32761214133911"></a><a name="p32761214133911"></a>rw_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.1.6.1.2 "><p id="p7276614173915"><a name="p7276614173915"></a><a name="p7276614173915"></a>Read Write Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="36.620000000000005%" headers="mcps1.1.6.1.3 "><p id="p162085814429"><a name="p162085814429"></a><a name="p162085814429"></a>Read and write bandwidth of the file system within a monitoring period</p>
<p id="p127232169573"><a name="p127232169573"></a><a name="p127232169573"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="17.27%" headers="mcps1.1.6.1.4 "><p id="p8260756155224"><a name="p8260756155224"></a><a name="p8260756155224"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.6.1.5 "><p id="p65141501155224"><a name="p65141501155224"></a><a name="p65141501155224"></a>File sharing</p>
</td>
</tr>
</tbody>
</table>

## **Dimension**<a name="section43930857153328"></a>

<a name="table1629697153328"></a>
<table><thead align="left"><tr id="row64993686153328"><th class="cellrowborder" valign="top" width="40.400000000000006%" id="mcps1.1.3.1.1"><p id="p29997214153328"><a name="p29997214153328"></a><a name="p29997214153328"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="59.599999999999994%" id="mcps1.1.3.1.2"><p id="p13855283153328"><a name="p13855283153328"></a><a name="p13855283153328"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row48536124153328"><td class="cellrowborder" valign="top" width="40.400000000000006%" headers="mcps1.1.3.1.1 "><p id="p1344191314404"><a name="p1344191314404"></a><a name="p1344191314404"></a>share_id</p>
</td>
<td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.1.3.1.2 "><p id="p4441121324012"><a name="p4441121324012"></a><a name="p4441121324012"></a>File sharing</p>
</td>
</tr>
</tbody>
</table>

