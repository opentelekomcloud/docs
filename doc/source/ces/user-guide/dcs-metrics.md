# DCS Metrics<a name="EN-US_TOPIC_0084572266"></a>

## Function<a name="section188941271489"></a>

This topic describes the namespace, list, and dimensions of Distributed Cache Service \(DCS\) metrics on Cloud Eye. You can use APIs provided by Cloud Eye to query the metrics of the monitored object and alarms generated for DCS.

## **Namespace**<a name="seb67a3c3c7674640a799cdb3c27cb0b8"></a>

SYS.DCS

## Redis 3.0 Instance Metrics<a name="section61092036153615"></a>

>![](/images/icon-note.gif) **NOTE:**   
>The  **Measurement Object & Dimension**  column indicates the instance, instance type, and dimension of a measured object.  

**Table  1**  Redis 3.0 instance metrics

<a name="table111117367367"></a>
<table><thead align="left"><tr id="row611114364367"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.7.1.1"><p id="p011115366360"><a name="p011115366360"></a><a name="p011115366360"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.7.1.2"><p id="p611143643620"><a name="p611143643620"></a><a name="p611143643620"></a>Metric Name</p>
</th>
<th class="cellrowborder" valign="top" width="22%" id="mcps1.2.7.1.3"><p id="p1911214361369"><a name="p1911214361369"></a><a name="p1911214361369"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.7.1.4"><p id="p8112123614366"><a name="p8112123614366"></a><a name="p8112123614366"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.7.1.5"><p id="p11112153616365"><a name="p11112153616365"></a><a name="p11112153616365"></a><strong id="b17473125718265"><a name="b17473125718265"></a><a name="b17473125718265"></a>Measurement Object &amp; Dimension</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.7.1.6"><p id="p1627205117465"><a name="p1627205117465"></a><a name="p1627205117465"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row9112183612365"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p191120363366"><a name="p191120363366"></a><a name="p191120363366"></a>cpu_usage</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p1511243693615"><a name="p1511243693615"></a><a name="p1511243693615"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p87971428326"><a name="p87971428326"></a><a name="p87971428326"></a>CPU consumed by the monitored object</p>
<p id="p611203623618"><a name="p611203623618"></a><a name="p611203623618"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p911211362367"><a name="p911211362367"></a><a name="p911211362367"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p690411121682"><a name="p690411121682"></a><a name="p690411121682"></a>Measured object:</p>
<p id="p4904612288"><a name="p4904612288"></a><a name="p4904612288"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p590418126817"><a name="p590418126817"></a><a name="p590418126817"></a>Dimension:</p>
<p id="p79041012783"><a name="p79041012783"></a><a name="p79041012783"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p727210510464"><a name="p727210510464"></a><a name="p727210510464"></a>1 minute</p>
</td>
</tr>
<tr id="row181121436173610"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p911223643611"><a name="p911223643611"></a><a name="p911223643611"></a>memory_usage</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p911220362361"><a name="p911220362361"></a><a name="p911220362361"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p131124362363"><a name="p131124362363"></a><a name="p131124362363"></a>Memory consumed by the monitored object</p>
<p id="p483619613316"><a name="p483619613316"></a><a name="p483619613316"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p9113113663615"><a name="p9113113663615"></a><a name="p9113113663615"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p1384132819"><a name="p1384132819"></a><a name="p1384132819"></a>Measured object:</p>
<p id="p9891318810"><a name="p9891318810"></a><a name="p9891318810"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p20801317814"><a name="p20801317814"></a><a name="p20801317814"></a>Dimension:</p>
<p id="p289137814"><a name="p289137814"></a><a name="p289137814"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p1127218516469"><a name="p1127218516469"></a><a name="p1127218516469"></a>1 minute</p>
</td>
</tr>
<tr id="row15113163617366"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p2011318366361"><a name="p2011318366361"></a><a name="p2011318366361"></a>net_in_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p181131736153615"><a name="p181131736153615"></a><a name="p181131736153615"></a>Network Input Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p1711315366366"><a name="p1711315366366"></a><a name="p1711315366366"></a>Inbound throughput per second on a port</p>
<p id="p57403541844"><a name="p57403541844"></a><a name="p57403541844"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p10113183616368"><a name="p10113183616368"></a><a name="p10113183616368"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p75171273812"><a name="p75171273812"></a><a name="p75171273812"></a>Measured object:</p>
<p id="p75171278816"><a name="p75171278816"></a><a name="p75171278816"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p2051777984"><a name="p2051777984"></a><a name="p2051777984"></a>Dimension:</p>
<p id="p145173713814"><a name="p145173713814"></a><a name="p145173713814"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p72727512464"><a name="p72727512464"></a><a name="p72727512464"></a>1 minute</p>
</td>
</tr>
<tr id="row13113236193616"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p111313613363"><a name="p111313613363"></a><a name="p111313613363"></a>net_out_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p7113133612361"><a name="p7113133612361"></a><a name="p7113133612361"></a>Network Output Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p19114336193613"><a name="p19114336193613"></a><a name="p19114336193613"></a>Outbound throughput per second on a port</p>
<p id="p179455171558"><a name="p179455171558"></a><a name="p179455171558"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p1111411369369"><a name="p1111411369369"></a><a name="p1111411369369"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p1869587488"><a name="p1869587488"></a><a name="p1869587488"></a>Measured object:</p>
<p id="p36951271182"><a name="p36951271182"></a><a name="p36951271182"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p1969519716811"><a name="p1969519716811"></a><a name="p1969519716811"></a>Dimension:</p>
<p id="p14696171817"><a name="p14696171817"></a><a name="p14696171817"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p0272115184610"><a name="p0272115184610"></a><a name="p0272115184610"></a>1 minute</p>
</td>
</tr>
<tr id="row511473617369"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p711413673610"><a name="p711413673610"></a><a name="p711413673610"></a>connected_clients</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p14114153633613"><a name="p14114153633613"></a><a name="p14114153633613"></a>Connected Clients</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p13114203693620"><a name="p13114203693620"></a><a name="p13114203693620"></a>Number of connected clients, including connections established by the DCS server (a management service in the background) to monitor DCS instances and excluding connections from standby nodes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p111141536143613"><a name="p111141536143613"></a><a name="p111141536143613"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p210189889"><a name="p210189889"></a><a name="p210189889"></a>Measured object:</p>
<p id="p5101591681"><a name="p5101591681"></a><a name="p5101591681"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p16101399813"><a name="p16101399813"></a><a name="p16101399813"></a>Dimension:</p>
<p id="p19101794812"><a name="p19101794812"></a><a name="p19101794812"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p1427213514463"><a name="p1427213514463"></a><a name="p1427213514463"></a>1 minute</p>
</td>
</tr>
<tr id="row2114193673612"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p20114173663616"><a name="p20114173663616"></a><a name="p20114173663616"></a>client_longest_out_list</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p311433673615"><a name="p311433673615"></a><a name="p311433673615"></a>Client Longest Output List</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p6114236163620"><a name="p6114236163620"></a><a name="p6114236163620"></a>Longest output list among current client connections</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p13114113618368"><a name="p13114113618368"></a><a name="p13114113618368"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p158918214816"><a name="p158918214816"></a><a name="p158918214816"></a>Measured object:</p>
<p id="p168911725818"><a name="p168911725818"></a><a name="p168911725818"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p0891122182"><a name="p0891122182"></a><a name="p0891122182"></a>Dimension:</p>
<p id="p14891221886"><a name="p14891221886"></a><a name="p14891221886"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p1327275110461"><a name="p1327275110461"></a><a name="p1327275110461"></a>1 minute</p>
</td>
</tr>
<tr id="row11114123613364"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p4114183615363"><a name="p4114183615363"></a><a name="p4114183615363"></a>client_biggest_in_buf</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p8115163613365"><a name="p8115163613365"></a><a name="p8115163613365"></a>Client Biggest Input Buf</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p41792818611"><a name="p41792818611"></a><a name="p41792818611"></a>Maximum input data length among current client connections</p>
<p id="p51152364363"><a name="p51152364363"></a><a name="p51152364363"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p2115113610361"><a name="p2115113610361"></a><a name="p2115113610361"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p898842182"><a name="p898842182"></a><a name="p898842182"></a>Measured object:</p>
<p id="p59881218810"><a name="p59881218810"></a><a name="p59881218810"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p159892021485"><a name="p159892021485"></a><a name="p159892021485"></a>Dimension:</p>
<p id="p3989162881"><a name="p3989162881"></a><a name="p3989162881"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p12272451104615"><a name="p12272451104615"></a><a name="p12272451104615"></a>1 minute</p>
</td>
</tr>
<tr id="row1115183617361"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p0115236103615"><a name="p0115236103615"></a><a name="p0115236103615"></a>blocked_clients</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p181153367367"><a name="p181153367367"></a><a name="p181153367367"></a>Blocked Clients</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p2011513362364"><a name="p2011513362364"></a><a name="p2011513362364"></a>Number of clients suspended by block operations, such as BLPOP, BRPOP, and BRPOPLPUSH</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p31151436173616"><a name="p31151436173616"></a><a name="p31151436173616"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p14881037810"><a name="p14881037810"></a><a name="p14881037810"></a>Measured object:</p>
<p id="p3881531812"><a name="p3881531812"></a><a name="p3881531812"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p288103383"><a name="p288103383"></a><a name="p288103383"></a>Dimension:</p>
<p id="p68816313817"><a name="p68816313817"></a><a name="p68816313817"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p172732051194618"><a name="p172732051194618"></a><a name="p172732051194618"></a>1 minute</p>
</td>
</tr>
<tr id="row1911523693620"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p161157362366"><a name="p161157362366"></a><a name="p161157362366"></a>used_memory</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p7115153623611"><a name="p7115153623611"></a><a name="p7115153623611"></a>Used Memory</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p201153363362"><a name="p201153363362"></a><a name="p201153363362"></a>Number of bytes used by the Redis server</p>
<p id="p194001381264"><a name="p194001381264"></a><a name="p194001381264"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p9115183611364"><a name="p9115183611364"></a><a name="p9115183611364"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p147839571575"><a name="p147839571575"></a><a name="p147839571575"></a>Measured object:</p>
<p id="p578385715713"><a name="p578385715713"></a><a name="p578385715713"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p107836571176"><a name="p107836571176"></a><a name="p107836571176"></a>Dimension:</p>
<p id="p1178425716720"><a name="p1178425716720"></a><a name="p1178425716720"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p1527395174613"><a name="p1527395174613"></a><a name="p1527395174613"></a>1 minute</p>
</td>
</tr>
<tr id="row811673673612"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p5116153603619"><a name="p5116153603619"></a><a name="p5116153603619"></a>used_memory_rss</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p01162036143619"><a name="p01162036143619"></a><a name="p01162036143619"></a>Used Memory RSS</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p811613614366"><a name="p811613614366"></a><a name="p811613614366"></a>Resident set size (RSS) memory that the Redis server has used, which is the memory that actually resides in the memory, including all stack and heap memory but not swapped-out memory</p>
<p id="p87726481061"><a name="p87726481061"></a><a name="p87726481061"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p51164365369"><a name="p51164365369"></a><a name="p51164365369"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p38878571275"><a name="p38878571275"></a><a name="p38878571275"></a>Measured object:</p>
<p id="p158876576718"><a name="p158876576718"></a><a name="p158876576718"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p118870571076"><a name="p118870571076"></a><a name="p118870571076"></a>Dimension:</p>
<p id="p08871571679"><a name="p08871571679"></a><a name="p08871571679"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p82731751114615"><a name="p82731751114615"></a><a name="p82731751114615"></a>1 minute</p>
</td>
</tr>
<tr id="row101161336163610"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p6116173673616"><a name="p6116173673616"></a><a name="p6116173673616"></a>used_memory_peak</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p1011612369360"><a name="p1011612369360"></a><a name="p1011612369360"></a>Used Memory Peak</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p31168367365"><a name="p31168367365"></a><a name="p31168367365"></a>Peak memory consumed by Redis since the Redis server last started</p>
<p id="p1730312166121"><a name="p1730312166121"></a><a name="p1730312166121"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p151168368364"><a name="p151168368364"></a><a name="p151168368364"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p16988105720710"><a name="p16988105720710"></a><a name="p16988105720710"></a>Measured object:</p>
<p id="p89885572717"><a name="p89885572717"></a><a name="p89885572717"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p1398885716716"><a name="p1398885716716"></a><a name="p1398885716716"></a>Dimension:</p>
<p id="p39880571975"><a name="p39880571975"></a><a name="p39880571975"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p2273145118463"><a name="p2273145118463"></a><a name="p2273145118463"></a>1 minute</p>
</td>
</tr>
<tr id="row5117173615366"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p1911733611365"><a name="p1911733611365"></a><a name="p1911733611365"></a>used_memory_lua</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p9117193617361"><a name="p9117193617361"></a><a name="p9117193617361"></a>Used Memory Lua</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p11171236123610"><a name="p11171236123610"></a><a name="p11171236123610"></a>Number of bytes used by the Lua engine</p>
<p id="p1045332061217"><a name="p1045332061217"></a><a name="p1045332061217"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p101171136123617"><a name="p101171136123617"></a><a name="p101171136123617"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p118655461579"><a name="p118655461579"></a><a name="p118655461579"></a>Measured object:</p>
<p id="p164803432499"><a name="p164803432499"></a><a name="p164803432499"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p2865146479"><a name="p2865146479"></a><a name="p2865146479"></a>Dimension:</p>
<p id="p348012436495"><a name="p348012436495"></a><a name="p348012436495"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p182735517462"><a name="p182735517462"></a><a name="p182735517462"></a>1 minute</p>
</td>
</tr>
<tr id="row131171336163610"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p8117636123618"><a name="p8117636123618"></a><a name="p8117636123618"></a>memory_frag_ratio</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p1311753619368"><a name="p1311753619368"></a><a name="p1311753619368"></a>Memory Fragmentation Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p1011743633617"><a name="p1011743633617"></a><a name="p1011743633617"></a>Ratio between Used Memory RSS and Used Memory Its value is the same as that of <strong id="b211024121152859"><a name="b211024121152859"></a><a name="b211024121152859"></a>used_memory_rss</strong>/<strong id="b1953536021152859"><a name="b1953536021152859"></a><a name="b1953536021152859"></a>used_memory</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p17118183618365"><a name="p17118183618365"></a><a name="p17118183618365"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p8218193710718"><a name="p8218193710718"></a><a name="p8218193710718"></a>Measured object:</p>
<p id="p05633439493"><a name="p05633439493"></a><a name="p05633439493"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p5219123712713"><a name="p5219123712713"></a><a name="p5219123712713"></a>Dimension:</p>
<p id="p5563184324910"><a name="p5563184324910"></a><a name="p5563184324910"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p8273115144616"><a name="p8273115144616"></a><a name="p8273115144616"></a>1 minute</p>
</td>
</tr>
<tr id="row111803613366"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p1118103617368"><a name="p1118103617368"></a><a name="p1118103617368"></a>total_connections_received</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p13118336163620"><a name="p13118336163620"></a><a name="p13118336163620"></a>New Connections</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p911815361363"><a name="p911815361363"></a><a name="p911815361363"></a>Number of new connections established during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p8118136143611"><a name="p8118136143611"></a><a name="p8118136143611"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p499418331718"><a name="p499418331718"></a><a name="p499418331718"></a>Measured object:</p>
<p id="p515565044913"><a name="p515565044913"></a><a name="p515565044913"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p59947331171"><a name="p59947331171"></a><a name="p59947331171"></a>Dimension:</p>
<p id="p515575024917"><a name="p515575024917"></a><a name="p515575024917"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p427311516469"><a name="p427311516469"></a><a name="p427311516469"></a>1 minute</p>
</td>
</tr>
<tr id="row12118133633611"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p1011893653618"><a name="p1011893653618"></a><a name="p1011893653618"></a>total_commands_processed</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p121181736173611"><a name="p121181736173611"></a><a name="p121181736173611"></a>Commands Processed</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p711815369361"><a name="p711815369361"></a><a name="p711815369361"></a>Number of commands processed during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p2118436183619"><a name="p2118436183619"></a><a name="p2118436183619"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p1810019266714"><a name="p1810019266714"></a><a name="p1810019266714"></a>Measured object:</p>
<p id="p02404509493"><a name="p02404509493"></a><a name="p02404509493"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p141001261774"><a name="p141001261774"></a><a name="p141001261774"></a>Dimension:</p>
<p id="p02401150124919"><a name="p02401150124919"></a><a name="p02401150124919"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p11273451124615"><a name="p11273451124615"></a><a name="p11273451124615"></a>1 minute</p>
</td>
</tr>
<tr id="row12118163623617"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p13118436123615"><a name="p13118436123615"></a><a name="p13118436123615"></a>instantaneous_ops</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p3119163615368"><a name="p3119163615368"></a><a name="p3119163615368"></a>Instantaneous Ops Per Second</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p111910369360"><a name="p111910369360"></a><a name="p111910369360"></a>Number of processed commands per second</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p3119163653614"><a name="p3119163653614"></a><a name="p3119163653614"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p27826201578"><a name="p27826201578"></a><a name="p27826201578"></a>Measured object:</p>
<p id="p183311850184910"><a name="p183311850184910"></a><a name="p183311850184910"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p167829203711"><a name="p167829203711"></a><a name="p167829203711"></a>Dimension:</p>
<p id="p9331115074910"><a name="p9331115074910"></a><a name="p9331115074910"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p627395144617"><a name="p627395144617"></a><a name="p627395144617"></a>1 minute</p>
</td>
</tr>
<tr id="row1111910368369"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p14119736113618"><a name="p14119736113618"></a><a name="p14119736113618"></a>total_net_input_bytes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p12119103633617"><a name="p12119103633617"></a><a name="p12119103633617"></a>Net Input Bytes</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p171191036123620"><a name="p171191036123620"></a><a name="p171191036123620"></a>Number of bytes received during the monitoring period</p>
<p id="p2191112538"><a name="p2191112538"></a><a name="p2191112538"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p311912361360"><a name="p311912361360"></a><a name="p311912361360"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p20609131616715"><a name="p20609131616715"></a><a name="p20609131616715"></a>Measured object:</p>
<p id="p1141745010493"><a name="p1141745010493"></a><a name="p1141745010493"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p176093164711"><a name="p176093164711"></a><a name="p176093164711"></a>Dimension:</p>
<p id="p2041795013496"><a name="p2041795013496"></a><a name="p2041795013496"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p12273195184616"><a name="p12273195184616"></a><a name="p12273195184616"></a>1 minute</p>
</td>
</tr>
<tr id="row91191236123613"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p4119193673615"><a name="p4119193673615"></a><a name="p4119193673615"></a>total_net_output_bytes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p911916361362"><a name="p911916361362"></a><a name="p911916361362"></a>Net Output Bytes</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p17119736143612"><a name="p17119736143612"></a><a name="p17119736143612"></a>Number of bytes sent during the monitoring period</p>
<p id="p57401231632"><a name="p57401231632"></a><a name="p57401231632"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p131194365369"><a name="p131194365369"></a><a name="p131194365369"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p186309121779"><a name="p186309121779"></a><a name="p186309121779"></a>Measured object:</p>
<p id="p15091850104918"><a name="p15091850104918"></a><a name="p15091850104918"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p1863171214716"><a name="p1863171214716"></a><a name="p1863171214716"></a>Dimension:</p>
<p id="p1750945064917"><a name="p1750945064917"></a><a name="p1750945064917"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p12731151184614"><a name="p12731151184614"></a><a name="p12731151184614"></a>1 minute</p>
</td>
</tr>
<tr id="row1911917369369"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p17119836193615"><a name="p17119836193615"></a><a name="p17119836193615"></a>instantaneous_input_kbps</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p141204369363"><a name="p141204369363"></a><a name="p141204369363"></a>Instantaneous Input Kbps</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p945315107148"><a name="p945315107148"></a><a name="p945315107148"></a>Instantaneous input traffic</p>
<p id="p01204365368"><a name="p01204365368"></a><a name="p01204365368"></a>Unit: kbit/s</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p191205363361"><a name="p191205363361"></a><a name="p191205363361"></a>≥ 0 kbits/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p12229871975"><a name="p12229871975"></a><a name="p12229871975"></a>Measured object:</p>
<p id="p11591205010497"><a name="p11591205010497"></a><a name="p11591205010497"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p152301771579"><a name="p152301771579"></a><a name="p152301771579"></a>Dimension:</p>
<p id="p10591150154911"><a name="p10591150154911"></a><a name="p10591150154911"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p122731251104610"><a name="p122731251104610"></a><a name="p122731251104610"></a>1 minute</p>
</td>
</tr>
<tr id="row121201236183613"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p71201236143613"><a name="p71201236143613"></a><a name="p71201236143613"></a>instantaneous_output_kbps</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p1312023653610"><a name="p1312023653610"></a><a name="p1312023653610"></a>Instantaneous Output Kbps</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p1112053614364"><a name="p1112053614364"></a><a name="p1112053614364"></a>Instantaneous output traffic</p>
<p id="p101211220111416"><a name="p101211220111416"></a><a name="p101211220111416"></a>Unit: kbit/s</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p1312063633614"><a name="p1312063633614"></a><a name="p1312063633614"></a>≥ 0 kbits/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p798013117713"><a name="p798013117713"></a><a name="p798013117713"></a>Measured object:</p>
<p id="p126811050144918"><a name="p126811050144918"></a><a name="p126811050144918"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p18980131574"><a name="p18980131574"></a><a name="p18980131574"></a>Dimension:</p>
<p id="p13681155018497"><a name="p13681155018497"></a><a name="p13681155018497"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p19273195104617"><a name="p19273195104617"></a><a name="p19273195104617"></a>1 minute</p>
</td>
</tr>
<tr id="row161219361363"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p171211336143614"><a name="p171211336143614"></a><a name="p171211336143614"></a>rejected_connections</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p131217360366"><a name="p131217360366"></a><a name="p131217360366"></a>Rejected Connections</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p19121193653620"><a name="p19121193653620"></a><a name="p19121193653620"></a>Number of connections that have exceeded maxclients and been rejected during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p11217367367"><a name="p11217367367"></a><a name="p11217367367"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p176843563613"><a name="p176843563613"></a><a name="p176843563613"></a>Measured object:</p>
<p id="p8770135013492"><a name="p8770135013492"></a><a name="p8770135013492"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p1068475620617"><a name="p1068475620617"></a><a name="p1068475620617"></a>Dimension:</p>
<p id="p1277025020492"><a name="p1277025020492"></a><a name="p1277025020492"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p42731851184610"><a name="p42731851184610"></a><a name="p42731851184610"></a>1 minute</p>
</td>
</tr>
<tr id="row912113633615"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p71211736183615"><a name="p71211736183615"></a><a name="p71211736183615"></a>expired_keys</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p712119361361"><a name="p712119361361"></a><a name="p712119361361"></a>Expired Keys</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p1912118365365"><a name="p1912118365365"></a><a name="p1912118365365"></a>Number of keys that have expired and been deleted during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p1912117364361"><a name="p1912117364361"></a><a name="p1912117364361"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p5411452767"><a name="p5411452767"></a><a name="p5411452767"></a>Measured object:</p>
<p id="p128621750134914"><a name="p128621750134914"></a><a name="p128621750134914"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p841105212614"><a name="p841105212614"></a><a name="p841105212614"></a>Dimension:</p>
<p id="p7862125044913"><a name="p7862125044913"></a><a name="p7862125044913"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p12731551174619"><a name="p12731551174619"></a><a name="p12731551174619"></a>1 minute</p>
</td>
</tr>
<tr id="row2121236123614"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p5121036133617"><a name="p5121036133617"></a><a name="p5121036133617"></a>evicted_keys</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p3434191811717"><a name="p3434191811717"></a><a name="p3434191811717"></a>Evicted Keys</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p19121193614367"><a name="p19121193614367"></a><a name="p19121193614367"></a>Number of keys that have been evicted and deleted during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p912193653618"><a name="p912193653618"></a><a name="p912193653618"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p046174817613"><a name="p046174817613"></a><a name="p046174817613"></a>Measured object:</p>
<p id="p159501050154917"><a name="p159501050154917"></a><a name="p159501050154917"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p174694820610"><a name="p174694820610"></a><a name="p174694820610"></a>Dimension:</p>
<p id="p1695015504491"><a name="p1695015504491"></a><a name="p1695015504491"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p14273185114614"><a name="p14273185114614"></a><a name="p14273185114614"></a>1 minute</p>
</td>
</tr>
<tr id="row912223613614"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p16122436173614"><a name="p16122436173614"></a><a name="p16122436173614"></a>keyspace_hits</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p191221136193613"><a name="p191221136193613"></a><a name="p191221136193613"></a>Keyspace Hits</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p1912283693612"><a name="p1912283693612"></a><a name="p1912283693612"></a>Number of successful lookups of keys in the main dictionary during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p412293603611"><a name="p412293603611"></a><a name="p412293603611"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p108261425618"><a name="p108261425618"></a><a name="p108261425618"></a>Measured object:</p>
<p id="p8380517491"><a name="p8380517491"></a><a name="p8380517491"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p78267421069"><a name="p78267421069"></a><a name="p78267421069"></a>Dimension:</p>
<p id="p338165116494"><a name="p338165116494"></a><a name="p338165116494"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p6274155113465"><a name="p6274155113465"></a><a name="p6274155113465"></a>1 minute</p>
</td>
</tr>
<tr id="row3122193618364"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p91221036203616"><a name="p91221036203616"></a><a name="p91221036203616"></a>keyspace_misses</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p6122133683611"><a name="p6122133683611"></a><a name="p6122133683611"></a>Keyspace Misses</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p8122163643619"><a name="p8122163643619"></a><a name="p8122163643619"></a>Number of failed lookups of keys in the main dictionary during the monitoring period</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p17122036173612"><a name="p17122036173612"></a><a name="p17122036173612"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p1694113012616"><a name="p1694113012616"></a><a name="p1694113012616"></a>Measured object:</p>
<p id="p69482564498"><a name="p69482564498"></a><a name="p69482564498"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p1894193018614"><a name="p1894193018614"></a><a name="p1894193018614"></a>Dimension:</p>
<p id="p179491156124910"><a name="p179491156124910"></a><a name="p179491156124910"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p1827495144611"><a name="p1827495144611"></a><a name="p1827495144611"></a>1 minute</p>
</td>
</tr>
<tr id="row1012219366366"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p8122193611363"><a name="p8122193611363"></a><a name="p8122193611363"></a>pubsub_channels</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p012223613368"><a name="p012223613368"></a><a name="p012223613368"></a>PubSub Channels</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p121238367362"><a name="p121238367362"></a><a name="p121238367362"></a>Number of Pub/Sub channels</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p1212343673618"><a name="p1212343673618"></a><a name="p1212343673618"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p1723832612615"><a name="p1723832612615"></a><a name="p1723832612615"></a>Measured object:</p>
<p id="p84114578498"><a name="p84114578498"></a><a name="p84114578498"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p323811260620"><a name="p323811260620"></a><a name="p323811260620"></a>Dimension:</p>
<p id="p1541165704914"><a name="p1541165704914"></a><a name="p1541165704914"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p9274175113469"><a name="p9274175113469"></a><a name="p9274175113469"></a>1 minute</p>
</td>
</tr>
<tr id="row1312333617361"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p912313617363"><a name="p912313617363"></a><a name="p912313617363"></a>pubsub_patterns</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p712343615364"><a name="p712343615364"></a><a name="p712343615364"></a>PubSub Patterns</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p612383618364"><a name="p612383618364"></a><a name="p612383618364"></a>Number of Pub/Sub patterns</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p1612363633619"><a name="p1612363633619"></a><a name="p1612363633619"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p131403231862"><a name="p131403231862"></a><a name="p131403231862"></a>Measured object:</p>
<p id="p121341457194912"><a name="p121341457194912"></a><a name="p121341457194912"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p11140152320611"><a name="p11140152320611"></a><a name="p11140152320611"></a>Dimension:</p>
<p id="p19134857154918"><a name="p19134857154918"></a><a name="p19134857154918"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p182741351164613"><a name="p182741351164613"></a><a name="p182741351164613"></a>1 minute</p>
</td>
</tr>
<tr id="row212511368364"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p1125836123610"><a name="p1125836123610"></a><a name="p1125836123610"></a>keyspace_hits_perc</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p3125143603612"><a name="p3125143603612"></a><a name="p3125143603612"></a>Percentage of Keyspace Hits</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p1212593633610"><a name="p1212593633610"></a><a name="p1212593633610"></a>Ratio of the number of Redis cache hits to the number of lookups</p>
<p id="p1836416013615"><a name="p1836416013615"></a><a name="p1836416013615"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p912563623620"><a name="p912563623620"></a><a name="p912563623620"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p487921513616"><a name="p487921513616"></a><a name="p487921513616"></a>Measured object:</p>
<p id="p112271157154918"><a name="p112271157154918"></a><a name="p112271157154918"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p88801615062"><a name="p88801615062"></a><a name="p88801615062"></a>Dimension:</p>
<p id="p722775754913"><a name="p722775754913"></a><a name="p722775754913"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p92741351164618"><a name="p92741351164618"></a><a name="p92741351164618"></a>1 minute</p>
</td>
</tr>
<tr id="row38091491681"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p19127183613369"><a name="p19127183613369"></a><a name="p19127183613369"></a>command_max_delay</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p10127163610362"><a name="p10127163610362"></a><a name="p10127163610362"></a>Maximum Command Latency </p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p54271741519"><a name="p54271741519"></a><a name="p54271741519"></a>Maximum latency of commands</p>
<p id="p151272361369"><a name="p151272361369"></a><a name="p151272361369"></a>Unit: ms</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p1512743663612"><a name="p1512743663612"></a><a name="p1512743663612"></a>≥ 0 ms</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p15921148364"><a name="p15921148364"></a><a name="p15921148364"></a>Measured object:</p>
<p id="p1232385714498"><a name="p1232385714498"></a><a name="p1232385714498"></a>Redis instance (single-node, active/standby, or cluster)</p>
<p id="p1592118360"><a name="p1592118360"></a><a name="p1592118360"></a>Dimension:</p>
<p id="p15323145774915"><a name="p15323145774915"></a><a name="p15323145774915"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p162741751184612"><a name="p162741751184612"></a><a name="p162741751184612"></a>1 minute</p>
</td>
</tr>
<tr id="row1012653614364"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p512610363369"><a name="p512610363369"></a><a name="p512610363369"></a>auth_errors</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p112541756201714"><a name="p112541756201714"></a><a name="p112541756201714"></a>Authentication Failures</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p20126203653610"><a name="p20126203653610"></a><a name="p20126203653610"></a>Number of authentication failures on an instance</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p6126736183619"><a name="p6126736183619"></a><a name="p6126736183619"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p28282031612"><a name="p28282031612"></a><a name="p28282031612"></a>Measured object:</p>
<p id="p69662024506"><a name="p69662024506"></a><a name="p69662024506"></a>Redis instance (single-node or active/standby)</p>
<p id="p18828531963"><a name="p18828531963"></a><a name="p18828531963"></a>Dimension:</p>
<p id="p596662175011"><a name="p596662175011"></a><a name="p596662175011"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p327435144610"><a name="p327435144610"></a><a name="p327435144610"></a>1 minute</p>
</td>
</tr>
<tr id="row612733612369"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p1712715365363"><a name="p1712715365363"></a><a name="p1712715365363"></a>is_slow_log_exist</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p0127936183617"><a name="p0127936183617"></a><a name="p0127936183617"></a>Slow Query Logs</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p19127113613364"><a name="p19127113613364"></a><a name="p19127113613364"></a>Existence of slow query logs in the instance</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><a name="ul1612723614365"></a><a name="ul1612723614365"></a><ul id="ul1612723614365"><li>1 minute indicates yes.</li><li>0 indicates no.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p132389571452"><a name="p132389571452"></a><a name="p132389571452"></a>Measured object:</p>
<p id="p13671831504"><a name="p13671831504"></a><a name="p13671831504"></a>Redis instance (single-node or active/standby)</p>
<p id="p1123812571054"><a name="p1123812571054"></a><a name="p1123812571054"></a>Dimension:</p>
<p id="p967103185012"><a name="p967103185012"></a><a name="p967103185012"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p1927425110468"><a name="p1927425110468"></a><a name="p1927425110468"></a>1 minute</p>
</td>
</tr>
<tr id="row206711438145812"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p7272540165820"><a name="p7272540165820"></a><a name="p7272540165820"></a>keys</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.2 "><p id="p0272104025812"><a name="p0272104025812"></a><a name="p0272104025812"></a>Keys</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.7.1.3 "><p id="p132721640185814"><a name="p132721640185814"></a><a name="p132721640185814"></a>Number of keys in Redis</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p327234015584"><a name="p327234015584"></a><a name="p327234015584"></a>&gt;=0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.5 "><p id="p13538552052"><a name="p13538552052"></a><a name="p13538552052"></a>Measured object:</p>
<p id="p1615818317505"><a name="p1615818317505"></a><a name="p1615818317505"></a>Redis instance (single-node or active/standby)</p>
<p id="p13510155015513"><a name="p13510155015513"></a><a name="p13510155015513"></a>Dimension:</p>
<p id="p141587318507"><a name="p141587318507"></a><a name="p141587318507"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p72741551174612"><a name="p72741551174612"></a><a name="p72741551174612"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="section10507421184117"></a>

<a name="table850711216413"></a>
<table><thead align="left"><tr id="row1650814216415"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p6508621194118"><a name="p6508621194118"></a><a name="p6508621194118"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p9509172120416"><a name="p9509172120416"></a><a name="p9509172120416"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row1550910213415"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p17510721104113"><a name="p17510721104113"></a><a name="p17510721104113"></a>dcs_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p175107217410"><a name="p175107217410"></a><a name="p175107217410"></a>Redis instance</p>
</td>
</tr>
</tbody>
</table>

