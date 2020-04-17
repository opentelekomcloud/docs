# DCS Metrics<a name="EN-US_TOPIC_0171212630"></a>

## Function<a name="s5bef70b523b7497589c9e05f0571674e"></a>

This topic describes the namespace, list, and dimensions of Distributed Cache Service \(DCS\) metrics on Cloud Eye. You can use APIs provided by Cloud Eye to query the metrics of the monitored object and alarms generated for DCS.

## Namespace<a name="seb67a3c3c7674640a799cdb3c27cb0b8"></a>

SYS.DCS

## Redis 3.0 Instance Metrics<a name="section61092036153615"></a>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This topic describes Redis3.0 instance metrics monitored by Cloud Eye. The dimension ID of the following metrics is  **dcs\_instance\_id**.  

**Table  1**  Redis 3.0 instance metrics

<a name="table111117367367"></a>
<table><thead align="left"><tr id="row611114364367"><th class="cellrowborder" valign="top" width="19.78%" id="mcps1.2.6.1.1"><p id="p011115366360"><a name="p011115366360"></a><a name="p011115366360"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="17.810000000000002%" id="mcps1.2.6.1.2"><p id="p611143643620"><a name="p611143643620"></a><a name="p611143643620"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="36.16%" id="mcps1.2.6.1.3"><p id="p1911214361369"><a name="p1911214361369"></a><a name="p1911214361369"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="12.17%" id="mcps1.2.6.1.4"><p id="p8112123614366"><a name="p8112123614366"></a><a name="p8112123614366"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="14.08%" id="mcps1.2.6.1.5"><p id="p11112153616365"><a name="p11112153616365"></a><a name="p11112153616365"></a>Monitored Object</p>
</th>
</tr>
</thead>
<tbody><tr id="row9112183612365"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p191120363366"><a name="p191120363366"></a><a name="p191120363366"></a>cpu_usage</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p1511243693615"><a name="p1511243693615"></a><a name="p1511243693615"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p87971428326"><a name="p87971428326"></a><a name="p87971428326"></a>CPU consumed by the monitored object</p>
<p id="p611203623618"><a name="p611203623618"></a><a name="p611203623618"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p911211362367"><a name="p911211362367"></a><a name="p911211362367"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p1411253613361"><a name="p1411253613361"></a><a name="p1411253613361"></a>Redis instance</p>
</td>
</tr>
<tr id="row181121436173610"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p911223643611"><a name="p911223643611"></a><a name="p911223643611"></a>memory_usage</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p911220362361"><a name="p911220362361"></a><a name="p911220362361"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p131124362363"><a name="p131124362363"></a><a name="p131124362363"></a>Memory consumed by the monitored object</p>
<p id="p483619613316"><a name="p483619613316"></a><a name="p483619613316"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p9113113663615"><a name="p9113113663615"></a><a name="p9113113663615"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p18113236193616"><a name="p18113236193616"></a><a name="p18113236193616"></a>Redis instance</p>
</td>
</tr>
<tr id="row15113163617366"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p2011318366361"><a name="p2011318366361"></a><a name="p2011318366361"></a>net_in_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p181131736153615"><a name="p181131736153615"></a><a name="p181131736153615"></a>Network Input Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p1711315366366"><a name="p1711315366366"></a><a name="p1711315366366"></a>Inbound throughput per second on a port</p>
<p id="p57403541844"><a name="p57403541844"></a><a name="p57403541844"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p10113183616368"><a name="p10113183616368"></a><a name="p10113183616368"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p711319361363"><a name="p711319361363"></a><a name="p711319361363"></a>Redis instance</p>
</td>
</tr>
<tr id="row13113236193616"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p111313613363"><a name="p111313613363"></a><a name="p111313613363"></a>net_out_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p7113133612361"><a name="p7113133612361"></a><a name="p7113133612361"></a>Network Output Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p19114336193613"><a name="p19114336193613"></a><a name="p19114336193613"></a>Outbound throughput per second on a port</p>
<p id="p179455171558"><a name="p179455171558"></a><a name="p179455171558"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p1111411369369"><a name="p1111411369369"></a><a name="p1111411369369"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p1711414361365"><a name="p1711414361365"></a><a name="p1711414361365"></a>Redis instance</p>
</td>
</tr>
<tr id="row511473617369"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p711413673610"><a name="p711413673610"></a><a name="p711413673610"></a>connected_clients</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p14114153633613"><a name="p14114153633613"></a><a name="p14114153633613"></a>Connected Clients</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p13114203693620"><a name="p13114203693620"></a><a name="p13114203693620"></a>Number of connected clients, including connections established by the DCS server (a management service in the background) to monitor DCS instances and excluding connections from standby nodes</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p111141536143613"><a name="p111141536143613"></a><a name="p111141536143613"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p15114936103619"><a name="p15114936103619"></a><a name="p15114936103619"></a>Redis instance</p>
</td>
</tr>
<tr id="row2114193673612"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p20114173663616"><a name="p20114173663616"></a><a name="p20114173663616"></a>client_longest_out_list</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p311433673615"><a name="p311433673615"></a><a name="p311433673615"></a>Client Longest Output List</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p6114236163620"><a name="p6114236163620"></a><a name="p6114236163620"></a>Longest output list among all current client connections</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p13114113618368"><a name="p13114113618368"></a><a name="p13114113618368"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p91141836103610"><a name="p91141836103610"></a><a name="p91141836103610"></a>Redis instance</p>
</td>
</tr>
<tr id="row11114123613364"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p4114183615363"><a name="p4114183615363"></a><a name="p4114183615363"></a>client_biggest_in_buf</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p8115163613365"><a name="p8115163613365"></a><a name="p8115163613365"></a>Client Biggest Input Buf</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p41792818611"><a name="p41792818611"></a><a name="p41792818611"></a>Maximum input data length among current client connections</p>
<p id="p51152364363"><a name="p51152364363"></a><a name="p51152364363"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p2115113610361"><a name="p2115113610361"></a><a name="p2115113610361"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p1711523616361"><a name="p1711523616361"></a><a name="p1711523616361"></a>Redis instance</p>
</td>
</tr>
<tr id="row1115183617361"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p0115236103615"><a name="p0115236103615"></a><a name="p0115236103615"></a>blocked_clients</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p181153367367"><a name="p181153367367"></a><a name="p181153367367"></a>Blocked Clients</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p2011513362364"><a name="p2011513362364"></a><a name="p2011513362364"></a>Number of clients suspended by block operations, such as BLPOP, BRPOP, and BRPOPLPUSH</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p31151436173616"><a name="p31151436173616"></a><a name="p31151436173616"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p13115836143618"><a name="p13115836143618"></a><a name="p13115836143618"></a>Redis instance</p>
</td>
</tr>
<tr id="row1911523693620"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p161157362366"><a name="p161157362366"></a><a name="p161157362366"></a>used_memory</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p7115153623611"><a name="p7115153623611"></a><a name="p7115153623611"></a>Used Memory</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p201153363362"><a name="p201153363362"></a><a name="p201153363362"></a>Number of bytes used by the Redis server</p>
<p id="p194001381264"><a name="p194001381264"></a><a name="p194001381264"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p9115183611364"><a name="p9115183611364"></a><a name="p9115183611364"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p161161536103618"><a name="p161161536103618"></a><a name="p161161536103618"></a>Redis instance</p>
</td>
</tr>
<tr id="row811673673612"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p5116153603619"><a name="p5116153603619"></a><a name="p5116153603619"></a>used_memory_rss</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p01162036143619"><a name="p01162036143619"></a><a name="p01162036143619"></a>Used Memory RSS</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p811613614366"><a name="p811613614366"></a><a name="p811613614366"></a>Resident set size (RSS) memory that the Redis server has used, which is the memory that actually resides in the memory, including all stack and heap memory but not swapped-out memory</p>
<p id="p87726481061"><a name="p87726481061"></a><a name="p87726481061"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p51164365369"><a name="p51164365369"></a><a name="p51164365369"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p7116163613612"><a name="p7116163613612"></a><a name="p7116163613612"></a>Redis instance</p>
</td>
</tr>
<tr id="row101161336163610"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p6116173673616"><a name="p6116173673616"></a><a name="p6116173673616"></a>used_memory_peak</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p1011612369360"><a name="p1011612369360"></a><a name="p1011612369360"></a>Used Memory Peak</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p31168367365"><a name="p31168367365"></a><a name="p31168367365"></a>Peak memory consumed by Redis since the Redis server last started</p>
<p id="p1730312166121"><a name="p1730312166121"></a><a name="p1730312166121"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p151168368364"><a name="p151168368364"></a><a name="p151168368364"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p711683610368"><a name="p711683610368"></a><a name="p711683610368"></a>Redis instance</p>
</td>
</tr>
<tr id="row5117173615366"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p1911733611365"><a name="p1911733611365"></a><a name="p1911733611365"></a>used_memory_lua</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p9117193617361"><a name="p9117193617361"></a><a name="p9117193617361"></a>Used Memory Lua</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p11171236123610"><a name="p11171236123610"></a><a name="p11171236123610"></a>Number of bytes used by the Lua engine</p>
<p id="p1045332061217"><a name="p1045332061217"></a><a name="p1045332061217"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p101171136123617"><a name="p101171136123617"></a><a name="p101171136123617"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p811783663612"><a name="p811783663612"></a><a name="p811783663612"></a>Redis instance</p>
</td>
</tr>
<tr id="row131171336163610"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p8117636123618"><a name="p8117636123618"></a><a name="p8117636123618"></a>memory_frag_ratio</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p1311753619368"><a name="p1311753619368"></a><a name="p1311753619368"></a>Memory Fragmentation Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p12868164818264"><a name="p12868164818264"></a><a name="p12868164818264"></a>Ratio between Used Memory RSS and Used Memory</p>
<p id="p1011743633617"><a name="p1011743633617"></a><a name="p1011743633617"></a>Its value is the same as that of <strong id="b11902112015213"><a name="b11902112015213"></a><a name="b11902112015213"></a>used_memory_rss</strong>/<strong id="b091619207217"><a name="b091619207217"></a><a name="b091619207217"></a>used_memory</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p17118183618365"><a name="p17118183618365"></a><a name="p17118183618365"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p12118173616363"><a name="p12118173616363"></a><a name="p12118173616363"></a>Redis instance</p>
</td>
</tr>
<tr id="row111803613366"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p1118103617368"><a name="p1118103617368"></a><a name="p1118103617368"></a>total_connections_received</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p13118336163620"><a name="p13118336163620"></a><a name="p13118336163620"></a>Connections Received</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p911815361363"><a name="p911815361363"></a><a name="p911815361363"></a>Number of connections received during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p8118136143611"><a name="p8118136143611"></a><a name="p8118136143611"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p7118193615364"><a name="p7118193615364"></a><a name="p7118193615364"></a>Redis instance</p>
</td>
</tr>
<tr id="row12118133633611"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p1011893653618"><a name="p1011893653618"></a><a name="p1011893653618"></a>total_commands_processed</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p121181736173611"><a name="p121181736173611"></a><a name="p121181736173611"></a>Commands Processed</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p711815369361"><a name="p711815369361"></a><a name="p711815369361"></a>Number of commands processed during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p2118436183619"><a name="p2118436183619"></a><a name="p2118436183619"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p7118436123611"><a name="p7118436123611"></a><a name="p7118436123611"></a>Redis instance</p>
</td>
</tr>
<tr id="row12118163623617"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p13118436123615"><a name="p13118436123615"></a><a name="p13118436123615"></a>instantaneous_ops</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p3119163615368"><a name="p3119163615368"></a><a name="p3119163615368"></a>Instantaneous Ops per Second</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p111910369360"><a name="p111910369360"></a><a name="p111910369360"></a>Number of commands processed per second</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p3119163653614"><a name="p3119163653614"></a><a name="p3119163653614"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p1011973613617"><a name="p1011973613617"></a><a name="p1011973613617"></a>Redis instance</p>
</td>
</tr>
<tr id="row1111910368369"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p14119736113618"><a name="p14119736113618"></a><a name="p14119736113618"></a>total_net_input_bytes</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p12119103633617"><a name="p12119103633617"></a><a name="p12119103633617"></a>Net Input Bytes</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p171191036123620"><a name="p171191036123620"></a><a name="p171191036123620"></a>Number of bytes received during the monitoring period</p>
<p id="p2191112538"><a name="p2191112538"></a><a name="p2191112538"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p311912361360"><a name="p311912361360"></a><a name="p311912361360"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p91199368368"><a name="p91199368368"></a><a name="p91199368368"></a>Redis instance</p>
</td>
</tr>
<tr id="row91191236123613"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p4119193673615"><a name="p4119193673615"></a><a name="p4119193673615"></a>total_net_output_bytes</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p911916361362"><a name="p911916361362"></a><a name="p911916361362"></a>Net Output Bytes</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p17119736143612"><a name="p17119736143612"></a><a name="p17119736143612"></a>Number of bytes sent during the monitoring period</p>
<p id="p57401231632"><a name="p57401231632"></a><a name="p57401231632"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p131194365369"><a name="p131194365369"></a><a name="p131194365369"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p101195366363"><a name="p101195366363"></a><a name="p101195366363"></a>Redis instance</p>
</td>
</tr>
<tr id="row1911917369369"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p17119836193615"><a name="p17119836193615"></a><a name="p17119836193615"></a>instantaneous_input_kbps</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p141204369363"><a name="p141204369363"></a><a name="p141204369363"></a>Instantaneous Input Kbps</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p945315107148"><a name="p945315107148"></a><a name="p945315107148"></a>Instantaneous input traffic</p>
<p id="p01204365368"><a name="p01204365368"></a><a name="p01204365368"></a>Unit: kbit/s</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p191205363361"><a name="p191205363361"></a><a name="p191205363361"></a>≥ 0 kbits/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p112014362360"><a name="p112014362360"></a><a name="p112014362360"></a>Redis instance</p>
</td>
</tr>
<tr id="row121201236183613"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p71201236143613"><a name="p71201236143613"></a><a name="p71201236143613"></a>instantaneous_output_kbps</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p1312023653610"><a name="p1312023653610"></a><a name="p1312023653610"></a>Instantaneous Output Kbps</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p1112053614364"><a name="p1112053614364"></a><a name="p1112053614364"></a>Instantaneous output traffic</p>
<p id="p101211220111416"><a name="p101211220111416"></a><a name="p101211220111416"></a>Unit: kbit/s</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p1312063633614"><a name="p1312063633614"></a><a name="p1312063633614"></a>≥ 0 kbits/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p112173611361"><a name="p112173611361"></a><a name="p112173611361"></a>Redis instance</p>
</td>
</tr>
<tr id="row161219361363"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p171211336143614"><a name="p171211336143614"></a><a name="p171211336143614"></a>rejected_connections</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p131217360366"><a name="p131217360366"></a><a name="p131217360366"></a>Rejected Connections</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p19121193653620"><a name="p19121193653620"></a><a name="p19121193653620"></a>Number of connections that have exceeded maxclients and been rejected during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p11217367367"><a name="p11217367367"></a><a name="p11217367367"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p41211436133611"><a name="p41211436133611"></a><a name="p41211436133611"></a>Redis instance</p>
</td>
</tr>
<tr id="row912113633615"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p71211736183615"><a name="p71211736183615"></a><a name="p71211736183615"></a>expired_keys</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p712119361361"><a name="p712119361361"></a><a name="p712119361361"></a>Expired Keys</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p1912118365365"><a name="p1912118365365"></a><a name="p1912118365365"></a>Number of keys that have expired and been deleted during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p1912117364361"><a name="p1912117364361"></a><a name="p1912117364361"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p6121136123617"><a name="p6121136123617"></a><a name="p6121136123617"></a>Redis instance</p>
</td>
</tr>
<tr id="row2121236123614"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p5121036133617"><a name="p5121036133617"></a><a name="p5121036133617"></a>evicted_keys</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p11212364364"><a name="p11212364364"></a><a name="p11212364364"></a>Evicted Keys</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p19121193614367"><a name="p19121193614367"></a><a name="p19121193614367"></a>Number of keys that have been evicted and deleted during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p912193653618"><a name="p912193653618"></a><a name="p912193653618"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p81221366364"><a name="p81221366364"></a><a name="p81221366364"></a>Redis instance</p>
</td>
</tr>
<tr id="row912223613614"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p16122436173614"><a name="p16122436173614"></a><a name="p16122436173614"></a>keyspace_hits</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p191221136193613"><a name="p191221136193613"></a><a name="p191221136193613"></a>Keyspace Hits</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p1912283693612"><a name="p1912283693612"></a><a name="p1912283693612"></a>Number of successful lookups of keys in the main dictionary during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p412293603611"><a name="p412293603611"></a><a name="p412293603611"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p151221836123619"><a name="p151221836123619"></a><a name="p151221836123619"></a>Redis instance</p>
</td>
</tr>
<tr id="row3122193618364"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p91221036203616"><a name="p91221036203616"></a><a name="p91221036203616"></a>keyspace_misses</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p6122133683611"><a name="p6122133683611"></a><a name="p6122133683611"></a>Keyspace Misses</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p8122163643619"><a name="p8122163643619"></a><a name="p8122163643619"></a>Number of failed lookups of keys in the main dictionary during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p17122036173612"><a name="p17122036173612"></a><a name="p17122036173612"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p41220367365"><a name="p41220367365"></a><a name="p41220367365"></a>Redis instance</p>
</td>
</tr>
<tr id="row1012219366366"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p8122193611363"><a name="p8122193611363"></a><a name="p8122193611363"></a>pubsub_channels</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p012223613368"><a name="p012223613368"></a><a name="p012223613368"></a>PubSub Channels</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p121238367362"><a name="p121238367362"></a><a name="p121238367362"></a>Number of Pub/Sub channels</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p1212343673618"><a name="p1212343673618"></a><a name="p1212343673618"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p2123113603613"><a name="p2123113603613"></a><a name="p2123113603613"></a>Redis instance</p>
</td>
</tr>
<tr id="row1312333617361"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p912313617363"><a name="p912313617363"></a><a name="p912313617363"></a>pubsub_patterns</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p712343615364"><a name="p712343615364"></a><a name="p712343615364"></a>PubSub Patterns</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p612383618364"><a name="p612383618364"></a><a name="p612383618364"></a>Number of Pub/Sub patterns</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p1612363633619"><a name="p1612363633619"></a><a name="p1612363633619"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p151231136133617"><a name="p151231136133617"></a><a name="p151231136133617"></a>Redis instance</p>
</td>
</tr>
<tr id="row212511368364"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p1125836123610"><a name="p1125836123610"></a><a name="p1125836123610"></a>keyspace_hits_perc</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p3125143603612"><a name="p3125143603612"></a><a name="p3125143603612"></a>Percentage of Keyspace Hits</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p1212593633610"><a name="p1212593633610"></a><a name="p1212593633610"></a>Ratio of the number of Redis cache hits to the number of lookups</p>
<p id="p1836416013615"><a name="p1836416013615"></a><a name="p1836416013615"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p912563623620"><a name="p912563623620"></a><a name="p912563623620"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p11126143616369"><a name="p11126143616369"></a><a name="p11126143616369"></a>Redis instance</p>
</td>
</tr>
<tr id="row1012653614364"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p512610363369"><a name="p512610363369"></a><a name="p512610363369"></a>auth_errors</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p01264367363"><a name="p01264367363"></a><a name="p01264367363"></a>Authentication Failures</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p20126203653610"><a name="p20126203653610"></a><a name="p20126203653610"></a>Number of failed authentications</p>
<p id="p118901020104412"><a name="p118901020104412"></a><a name="p118901020104412"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p6126736183619"><a name="p6126736183619"></a><a name="p6126736183619"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p8126123613365"><a name="p8126123613365"></a><a name="p8126123613365"></a>Redis instance</p>
</td>
</tr>
<tr id="row1126103614369"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p19127183613369"><a name="p19127183613369"></a><a name="p19127183613369"></a>command_max_delay</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p10127163610362"><a name="p10127163610362"></a><a name="p10127163610362"></a>Maximum Command Latency</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p54271741519"><a name="p54271741519"></a><a name="p54271741519"></a>Maximum latency of commands</p>
<p id="p151272361369"><a name="p151272361369"></a><a name="p151272361369"></a>Unit: ms</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><p id="p1512743663612"><a name="p1512743663612"></a><a name="p1512743663612"></a>≥ 0 ms</p>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p5127336163616"><a name="p5127336163616"></a><a name="p5127336163616"></a>Redis instance</p>
</td>
</tr>
<tr id="row612733612369"><td class="cellrowborder" valign="top" width="19.78%" headers="mcps1.2.6.1.1 "><p id="p1712715365363"><a name="p1712715365363"></a><a name="p1712715365363"></a>is_slow_log_exist</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.6.1.2 "><p id="p0127936183617"><a name="p0127936183617"></a><a name="p0127936183617"></a>Slow Query Logs</p>
</td>
<td class="cellrowborder" valign="top" width="36.16%" headers="mcps1.2.6.1.3 "><p id="p19127113613364"><a name="p19127113613364"></a><a name="p19127113613364"></a>Existence of slow query logs in the instance</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.6.1.4 "><a name="ul1612723614365"></a><a name="ul1612723614365"></a><ul id="ul1612723614365"><li>1 indicates yes.</li><li>0 indicates no.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="14.08%" headers="mcps1.2.6.1.5 "><p id="p61271036123614"><a name="p61271036123614"></a><a name="p61271036123614"></a>Redis instance</p>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="section10507421184117"></a>

<a name="table850711216413"></a>
<table><thead align="left"><tr id="row1650814216415"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p6508621194118"><a name="p6508621194118"></a><a name="p6508621194118"></a><strong id="b84235270616476"><a name="b84235270616476"></a><a name="b84235270616476"></a>Key</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p9509172120416"><a name="p9509172120416"></a><a name="p9509172120416"></a><strong id="b842352706164710"><a name="b842352706164710"></a><a name="b842352706164710"></a>Value</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1550910213415"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p17510721104113"><a name="p17510721104113"></a><a name="p17510721104113"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p175107217410"><a name="p175107217410"></a><a name="p175107217410"></a>Redis instances</p>
</td>
</tr>
</tbody>
</table>

