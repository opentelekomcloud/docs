# Related Services<a name="EN-US_TOPIC_0056725844"></a>

**Table  1**  Related services

<a name="table17588842174917"></a>
<table><thead align="left"><tr id="row459074213498"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p659044234913"><a name="p659044234913"></a><a name="p659044234913"></a>Interactive Function</p>
</th>
<th class="cellrowborder" valign="top" width="33.223322332233224%" id="mcps1.2.4.1.2"><p id="p14590144213494"><a name="p14590144213494"></a><a name="p14590144213494"></a>Related Service</p>
</th>
<th class="cellrowborder" valign="top" width="33.44334433443344%" id="mcps1.2.4.1.3"><p id="p259064217498"><a name="p259064217498"></a><a name="p259064217498"></a>Reference</p>
</th>
</tr>
</thead>
<tbody><tr id="row35905426493"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p859018425498"><a name="p859018425498"></a><a name="p859018425498"></a>CSBS can back up data of the EVS disks on an ECS, and restore backup data to the EVS disks of an ECS so as to retrieve lost or corrupted data. Generated backups can be used to create images for fast restoring the service running environment.</p>
</td>
<td class="cellrowborder" valign="top" width="33.223322332233224%" headers="mcps1.2.4.1.2 "><p id="p1159011426497"><a name="p1159011426497"></a><a name="p1159011426497"></a>Elastic Cloud Server (ECS)</p>
</td>
<td class="cellrowborder" valign="top" width="33.44334433443344%" headers="mcps1.2.4.1.3 "><p id="p119016318311"><a name="p119016318311"></a><a name="p119016318311"></a><a href="creating-a-csbs-backup.md">Creating a CSBS Backup</a></p>
</td>
</tr>
<tr id="row0590442124918"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p18887161116207"><a name="p18887161116207"></a><a name="p18887161116207"></a>CSBS combines ECS and OBS to back up ECS data to object storage, enhancing backup data security.</p>
</td>
<td class="cellrowborder" valign="top" width="33.223322332233224%" headers="mcps1.2.4.1.2 "><p id="p1330519223206"><a name="p1330519223206"></a><a name="p1330519223206"></a><strong id="b2598897319953"><a name="b2598897319953"></a><a name="b2598897319953"></a>Object Storage Service (OBS)</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.44334433443344%" headers="mcps1.2.4.1.3 "><p id="p099311170387"><a name="p099311170387"></a><a name="p099311170387"></a><a href="csbs.md">CSBS</a></p>
</td>
</tr>
<tr id="row859034244920"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p21816578235"><a name="p21816578235"></a><a name="p21816578235"></a>Cloud Trace Service (CTS) records operations of CSBS resources, facilitating query, audit, and backtracking.</p>
</td>
<td class="cellrowborder" valign="top" width="33.223322332233224%" headers="mcps1.2.4.1.2 "><p id="p129817316245"><a name="p129817316245"></a><a name="p129817316245"></a>Cloud Trace Service (CTS)</p>
</td>
<td class="cellrowborder" valign="top" width="33.44334433443344%" headers="mcps1.2.4.1.3 "><p id="p237013492406"><a name="p237013492406"></a><a name="p237013492406"></a><a href="events.md">Events</a></p>
</td>
</tr>
<tr id="row1590154214495"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p459024219490"><a name="p459024219490"></a><a name="p459024219490"></a>CSBS and VBS both provide data backup protection. <a href="#table1965919985417">Table 2</a> describes the differences between CSBS and VBS.</p>
</td>
<td class="cellrowborder" valign="top" width="33.223322332233224%" headers="mcps1.2.4.1.2 "><p id="p722451922520"><a name="p722451922520"></a><a name="p722451922520"></a>Volume Backup Service (VBS)</p>
</td>
<td class="cellrowborder" valign="top" width="33.44334433443344%" headers="mcps1.2.4.1.3 "><p id="p6325194019546"><a name="p6325194019546"></a><a name="p6325194019546"></a><a href="what-are-the-differences-between-csbs-and-vbs.md">What Are the Differences Between CSBS and VBS?</a></p>
</td>
</tr>
</tbody>
</table>

**Table  2**  CSBS and VBS

<a name="table1965919985417"></a>
<table><thead align="left"><tr id="row76591917540"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p5659792540"><a name="p5659792540"></a><a name="p5659792540"></a>Item</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.2.4.1.2"><p id="p11659209155417"><a name="p11659209155417"></a><a name="p11659209155417"></a>CSBS</p>
</th>
<th class="cellrowborder" valign="top" width="36%" id="mcps1.2.4.1.3"><p id="p116609917545"><a name="p116609917545"></a><a name="p116609917545"></a>VBS</p>
</th>
</tr>
</thead>
<tbody><tr id="row66600985420"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p766009155410"><a name="p766009155410"></a><a name="p766009155410"></a>Backup and restoration objects</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p11949021115513"><a name="p11949021115513"></a><a name="p11949021115513"></a>All EVS disks (including system and data disks) on a single ECS</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p1182342185615"><a name="p1182342185615"></a><a name="p1182342185615"></a>One or more specified EVS disks (system or data disks)</p>
</td>
</tr>
<tr id="row96601391546"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p186600918548"><a name="p186600918548"></a><a name="p186600918548"></a>Recommended scenarios</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p1438511314554"><a name="p1438511314554"></a><a name="p1438511314554"></a>An entire ECS needs to be protected.</p>
<p id="p1384392621111"><a name="p1384392621111"></a><a name="p1384392621111"></a>Use images created using backups to fast restore the service running environment.</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p75761524145610"><a name="p75761524145610"></a><a name="p75761524145610"></a>Only data disks need to be backed up, because the system disk does not contain personal data.</p>
</td>
</tr>
<tr id="row136601799549"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p13660149185415"><a name="p13660149185415"></a><a name="p13660149185415"></a>Advantages</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p17764194815558"><a name="p17764194815558"></a><a name="p17764194815558"></a>Consistency backup is supported. You can back up all EVS disks simultaneously, eliminating data inconsistency caused by backup time difference.</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.3 "><p id="p13825113235615"><a name="p13825113235615"></a><a name="p13825113235615"></a>Backup cost is reduced while maintaining data security.</p>
</td>
</tr>
</tbody>
</table>

