# EVS Metrics<a name="EN-US_TOPIC_0171212574"></a>

## Function<a name="s6ecc50b2bd1f49338f0598cff6a2131a"></a>

This section describes metrics reported by EVS to Cloud Eye as well as their namespaces and dimensions. You can use APIs provided by Cloud Eye to query the metrics of the monitored object and alarms generated for EVS.

## Namespace<a name="s3f078bb17e5647de9889544b9dd7caaf"></a>

SYS.EVS

## Metrics<a name="s475caf4f55ee40c189977e03bf8366b3"></a>

<a name="t1cf78e9000a54f828c740cca1862c355"></a>
<table><thead align="left"><tr id="reccbfc8ba9194822a89754d03f05d15a"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.1.6.1.1"><p id="adff343b697e74f789008173f77c2cbb4"><a name="adff343b697e74f789008173f77c2cbb4"></a><a name="adff343b697e74f789008173f77c2cbb4"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="14.14%" id="mcps1.1.6.1.2"><p id="a8c086f77f3d3472f9b9a87c0ac42d163"><a name="a8c086f77f3d3472f9b9a87c0ac42d163"></a><a name="a8c086f77f3d3472f9b9a87c0ac42d163"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="32.93%" id="mcps1.1.6.1.3"><p id="ac4db4e5c815a4942a17671f23f95bfe0"><a name="ac4db4e5c815a4942a17671f23f95bfe0"></a><a name="ac4db4e5c815a4942a17671f23f95bfe0"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="14.29%" id="mcps1.1.6.1.4"><p id="a06f528e78bd447cd9594fb1b2b82c381"><a name="a06f528e78bd447cd9594fb1b2b82c381"></a><a name="a06f528e78bd447cd9594fb1b2b82c381"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="23.49%" id="mcps1.1.6.1.5"><p id="p16345141818109"><a name="p16345141818109"></a><a name="p16345141818109"></a>Monitored Object</p>
</th>
</tr>
</thead>
<tbody><tr id="row1610913035210"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.6.1.1 "><p id="p1332384419524"><a name="p1332384419524"></a><a name="p1332384419524"></a>disk_device_read_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.1.6.1.2 "><p id="p1132534417525"><a name="p1132534417525"></a><a name="p1132534417525"></a>Disk Read Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="32.93%" headers="mcps1.1.6.1.3 "><p id="p1332614415523"><a name="p1332614415523"></a><a name="p1332614415523"></a>Number of bytes read from the monitored disk per second</p>
<p id="p1832614414527"><a name="p1832614414527"></a><a name="p1832614414527"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.6.1.4 "><p id="p3330244105216"><a name="p3330244105216"></a><a name="p3330244105216"></a>≥ 0 bytes/s</p>
<p id="p3332744175213"><a name="p3332744175213"></a><a name="p3332744175213"></a></p>
</td>
<td class="cellrowborder" valign="top" width="23.49%" headers="mcps1.1.6.1.5 "><p id="p12334174495215"><a name="p12334174495215"></a><a name="p12334174495215"></a>EVS disk</p>
</td>
</tr>
<tr id="row915633818528"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.6.1.1 "><p id="p833534413522"><a name="p833534413522"></a><a name="p833534413522"></a>disk_device_write_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.1.6.1.2 "><p id="p203387443523"><a name="p203387443523"></a><a name="p203387443523"></a>Disk Write Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="32.93%" headers="mcps1.1.6.1.3 "><p id="p4339114419522"><a name="p4339114419522"></a><a name="p4339114419522"></a>Number of bytes written to the monitored disk per second</p>
<p id="p1534112445524"><a name="p1534112445524"></a><a name="p1534112445524"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.6.1.4 "><p id="p133431844115213"><a name="p133431844115213"></a><a name="p133431844115213"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="23.49%" headers="mcps1.1.6.1.5 "><p id="p9345104414527"><a name="p9345104414527"></a><a name="p9345104414527"></a>EVS disk</p>
</td>
</tr>
<tr id="row165911356524"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.6.1.1 "><p id="p20346174415522"><a name="p20346174415522"></a><a name="p20346174415522"></a>disk_device_read_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.1.6.1.2 "><p id="p20349124455216"><a name="p20349124455216"></a><a name="p20349124455216"></a>Disk Read IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="32.93%" headers="mcps1.1.6.1.3 "><p id="p5350184455210"><a name="p5350184455210"></a><a name="p5350184455210"></a>Number of read requests sent to the monitored disk per second</p>
<p id="p123505444524"><a name="p123505444524"></a><a name="p123505444524"></a>Unit: Request/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.6.1.4 "><p id="p1035114415524"><a name="p1035114415524"></a><a name="p1035114415524"></a>≥ 0 Requests/s</p>
</td>
<td class="cellrowborder" valign="top" width="23.49%" headers="mcps1.1.6.1.5 "><p id="p17354144185215"><a name="p17354144185215"></a><a name="p17354144185215"></a>EVS disk</p>
</td>
</tr>
<tr id="row1087763285220"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.6.1.1 "><p id="p735510449529"><a name="p735510449529"></a><a name="p735510449529"></a>disk_device_write_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.1.6.1.2 "><p id="p23561944115211"><a name="p23561944115211"></a><a name="p23561944115211"></a>Disk Write IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="32.93%" headers="mcps1.1.6.1.3 "><p id="p3357144413526"><a name="p3357144413526"></a><a name="p3357144413526"></a>Number of write requests sent to the monitored disk per second</p>
<p id="p0358344135218"><a name="p0358344135218"></a><a name="p0358344135218"></a>Unit: Request/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.6.1.4 "><p id="p3361144495218"><a name="p3361144495218"></a><a name="p3361144495218"></a>≥ 0 Requests/s</p>
</td>
<td class="cellrowborder" valign="top" width="23.49%" headers="mcps1.1.6.1.5 "><p id="p13362104445216"><a name="p13362104445216"></a><a name="p13362104445216"></a>EVS disk</p>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="s4527acf0f97f47dc99997b1361f2af3b"></a>

<a name="tea3f5a4ae14a409c8e21bf2b071f687c"></a>
<table><thead align="left"><tr id="r047c7dbd3ac74b6cad02a81925ede1ad"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="ad4c09725144c4599a86eed8564b8b147"><a name="ad4c09725144c4599a86eed8564b8b147"></a><a name="ad4c09725144c4599a86eed8564b8b147"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a7d945928f7f94ec094ad0ea6da468396"><a name="a7d945928f7f94ec094ad0ea6da468396"></a><a name="a7d945928f7f94ec094ad0ea6da468396"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="r7671d104eb8b43bdb5603abef9823b2a"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a568cd715005f4286a5f6a1b8ff2a439d"><a name="a568cd715005f4286a5f6a1b8ff2a439d"></a><a name="a568cd715005f4286a5f6a1b8ff2a439d"></a>disk_name</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a263f56989ef94917adb666d195bb26fa"><a name="a263f56989ef94917adb666d195bb26fa"></a><a name="a263f56989ef94917adb666d195bb26fa"></a>ECS ID-disk name, for example, 6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d-sda (sda is the disk name)</p>
</td>
</tr>
</tbody>
</table>

