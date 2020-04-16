# RDS Metrics<a name="EN-US_TOPIC_0171212543"></a>

## Function<a name="s5bef70b523b7497589c9e05f0571674e"></a>

This section describes metrics reported by Cloud Eye to the Relational Database Service \(RDS\) as well as their namespaces and dimensions. You can use APIs provided by Cloud Eye to query the metrics of the monitored object and alarms generated for RDS.

## Namespace<a name="seb67a3c3c7674640a799cdb3c27cb0b8"></a>

SYS.RDS

## Metrics<a name="sc7cedca808a44d8c8885149adf1c648e"></a>

**Table  1**  MySQL metrics

<a name="table735516925913"></a>
<table><thead align="left"><tr id="row635612945920"><th class="cellrowborder" valign="top" width="15.229999999999999%" id="mcps1.2.6.1.1"><p id="p13356139145915"><a name="p13356139145915"></a><a name="p13356139145915"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="12.370000000000001%" id="mcps1.2.6.1.2"><p id="p1735612915914"><a name="p1735612915914"></a><a name="p1735612915914"></a><strong id="b1623493124"><a name="b1623493124"></a><a name="b1623493124"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.709999999999997%" id="mcps1.2.6.1.3"><p id="p1635612919593"><a name="p1635612919593"></a><a name="p1635612919593"></a><strong id="b1072480847"><a name="b1072480847"></a><a name="b1072480847"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.99%" id="mcps1.2.6.1.4"><p id="p123566995916"><a name="p123566995916"></a><a name="p123566995916"></a><strong id="b2065713119"><a name="b2065713119"></a><a name="b2065713119"></a>Value Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.7%" id="mcps1.2.6.1.5"><p id="p1635610915599"><a name="p1635610915599"></a><a name="p1635610915599"></a><strong id="b1171129984"><a name="b1171129984"></a><a name="b1171129984"></a>Remarks</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row193568925913"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p835614914591"><a name="p835614914591"></a><a name="p835614914591"></a>rds001_cpu_usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p163564925917"><a name="p163564925917"></a><a name="p163564925917"></a>CPU Usage (deprecated)</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p335615914592"><a name="p335615914592"></a><a name="p335615914592"></a>CPU usage of the monitored object</p>
<p id="p462362262"><a name="p462362262"></a><a name="p462362262"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p435610945912"><a name="p435610945912"></a><a name="p435610945912"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p13356109105913"><a name="p13356109105913"></a><a name="p13356109105913"></a>Monitored object: ECS</p>
<p id="p13356497591"><a name="p13356497591"></a><a name="p13356497591"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row23562913599"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p10356199105918"><a name="p10356199105918"></a><a name="p10356199105918"></a>rds001_cpu_util</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p53564920594"><a name="p53564920594"></a><a name="p53564920594"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p935616945910"><a name="p935616945910"></a><a name="p935616945910"></a>CPU usage of the monitored object</p>
<p id="p111391329268"><a name="p111391329268"></a><a name="p111391329268"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p235659105918"><a name="p235659105918"></a><a name="p235659105918"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p43561291590"><a name="p43561291590"></a><a name="p43561291590"></a>Monitored object: ECS</p>
<p id="p564421763612"><a name="p564421763612"></a><a name="p564421763612"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row6356189185915"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p14357149135913"><a name="p14357149135913"></a><a name="p14357149135913"></a>rds002_mem_usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1435719911594"><a name="p1435719911594"></a><a name="p1435719911594"></a>Memory Usage (deprecated)</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p7357899592"><a name="p7357899592"></a><a name="p7357899592"></a>Memory usage of the monitored object</p>
<p id="p13736619202616"><a name="p13736619202616"></a><a name="p13736619202616"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p173571955912"><a name="p173571955912"></a><a name="p173571955912"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p17357195591"><a name="p17357195591"></a><a name="p17357195591"></a>Monitored object: ECS</p>
<p id="p19528121173620"><a name="p19528121173620"></a><a name="p19528121173620"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row12357109145911"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p163573925916"><a name="p163573925916"></a><a name="p163573925916"></a>rds002_mem_util</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p53578985914"><a name="p53578985914"></a><a name="p53578985914"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p035712955913"><a name="p035712955913"></a><a name="p035712955913"></a>Memory usage of the monitored object</p>
<p id="p1177054716262"><a name="p1177054716262"></a><a name="p1177054716262"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1835715985912"><a name="p1835715985912"></a><a name="p1835715985912"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1935710965916"><a name="p1935710965916"></a><a name="p1935710965916"></a>Monitored object: ECS</p>
<p id="p1638719254369"><a name="p1638719254369"></a><a name="p1638719254369"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row14357119105911"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1735739185918"><a name="p1735739185918"></a><a name="p1735739185918"></a>rds003_iops</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1435714965911"><a name="p1435714965911"></a><a name="p1435714965911"></a>IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1235711913595"><a name="p1235711913595"></a><a name="p1235711913595"></a>Average rate at which I/O requests are processed during a specified period</p>
<p id="p2112259172110"><a name="p2112259172110"></a><a name="p2112259172110"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p4357199165916"><a name="p4357199165916"></a><a name="p4357199165916"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p103574905912"><a name="p103574905912"></a><a name="p103574905912"></a>Monitored object: ECS</p>
<p id="p1932612814369"><a name="p1932612814369"></a><a name="p1932612814369"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row43589935914"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p11358994595"><a name="p11358994595"></a><a name="p11358994595"></a>rds004_bytes_in</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p13582914598"><a name="p13582914598"></a><a name="p13582914598"></a>Network Input Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p63581792597"><a name="p63581792597"></a><a name="p63581792597"></a>Rate at which all incoming traffic passes through the network adapter</p>
<p id="p1888317439215"><a name="p1888317439215"></a><a name="p1888317439215"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p335819145911"><a name="p335819145911"></a><a name="p335819145911"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p73588910597"><a name="p73588910597"></a><a name="p73588910597"></a>Monitored object: ECS</p>
<p id="p2346113217367"><a name="p2346113217367"></a><a name="p2346113217367"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row73589985912"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1235849185914"><a name="p1235849185914"></a><a name="p1235849185914"></a>rds005_bytes_out</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p2035814920592"><a name="p2035814920592"></a><a name="p2035814920592"></a>Network Output Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p93582915592"><a name="p93582915592"></a><a name="p93582915592"></a>Rate at which all outgoing traffic passes through the network adapter</p>
<p id="p42991031192115"><a name="p42991031192115"></a><a name="p42991031192115"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p535920917598"><a name="p535920917598"></a><a name="p535920917598"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p143595915914"><a name="p143595915914"></a><a name="p143595915914"></a>Monitored object: ECS</p>
<p id="p1208405369"><a name="p1208405369"></a><a name="p1208405369"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row235910935915"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p18359149115914"><a name="p18359149115914"></a><a name="p18359149115914"></a>rds006_conn_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p133594935913"><a name="p133594935913"></a><a name="p133594935913"></a>Total Connections</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p73590912590"><a name="p73590912590"></a><a name="p73590912590"></a>Total number of connection attempts to the MySQL server</p>
<p id="p1350015558209"><a name="p1350015558209"></a><a name="p1350015558209"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p535914955917"><a name="p535914955917"></a><a name="p535914955917"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p53591298594"><a name="p53591298594"></a><a name="p53591298594"></a>Monitored object: database</p>
<p id="p135912965911"><a name="p135912965911"></a><a name="p135912965911"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row735915915594"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p4359199205919"><a name="p4359199205919"></a><a name="p4359199205919"></a>rds007_conn_active_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1935910915591"><a name="p1935910915591"></a><a name="p1935910915591"></a>Current Active Connections</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p53597917594"><a name="p53597917594"></a><a name="p53597917594"></a>Number of current active connections</p>
<p id="p8675151517215"><a name="p8675151517215"></a><a name="p8675151517215"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p143596918599"><a name="p143596918599"></a><a name="p143596918599"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p73591498591"><a name="p73591498591"></a><a name="p73591498591"></a>Monitored object: database</p>
<p id="p5359396592"><a name="p5359396592"></a><a name="p5359396592"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row103591910598"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1236014975912"><a name="p1236014975912"></a><a name="p1236014975912"></a>rds008_qps</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p8360195594"><a name="p8360195594"></a><a name="p8360195594"></a>QPS</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p113602913590"><a name="p113602913590"></a><a name="p113602913590"></a>Rate at which SQL statement queries (including the stored procedure) are executed</p>
<p id="p11167101511205"><a name="p11167101511205"></a><a name="p11167101511205"></a>Unit: Query/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p12360129165912"><a name="p12360129165912"></a><a name="p12360129165912"></a>≥ 0 queries/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1536089155914"><a name="p1536089155914"></a><a name="p1536089155914"></a>Monitored object: database</p>
<p id="p13601917594"><a name="p13601917594"></a><a name="p13601917594"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row1536015918599"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p43601920598"><a name="p43601920598"></a><a name="p43601920598"></a>rds009_tps</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p163601393598"><a name="p163601393598"></a><a name="p163601393598"></a>TPS</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1836016914592"><a name="p1836016914592"></a><a name="p1836016914592"></a>Rate at which transactions (including those submitted and rolled back) are executed</p>
<p id="p109601310112011"><a name="p109601310112011"></a><a name="p109601310112011"></a>Unit: Transaction/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p536017985912"><a name="p536017985912"></a><a name="p536017985912"></a>≥ 0 transactions/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1136015965916"><a name="p1136015965916"></a><a name="p1136015965916"></a>Monitored object: database</p>
<p id="p6360129205910"><a name="p6360129205910"></a><a name="p6360129205910"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row1336019165916"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p16360149115918"><a name="p16360149115918"></a><a name="p16360149115918"></a>rds010_innodb_buf_usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p936013975917"><a name="p936013975917"></a><a name="p936013975917"></a>Buffer Pool Usage</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1636017925910"><a name="p1636017925910"></a><a name="p1636017925910"></a>Ratio of dirty data from all data in the InnoDB buffer</p>
<p id="p1964982317197"><a name="p1964982317197"></a><a name="p1964982317197"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p736014910591"><a name="p736014910591"></a><a name="p736014910591"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1536099185919"><a name="p1536099185919"></a><a name="p1536099185919"></a>Monitored object: database</p>
<p id="p93606915910"><a name="p93606915910"></a><a name="p93606915910"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row7360109165910"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p93610995915"><a name="p93610995915"></a><a name="p93610995915"></a>rds011_innodb_buf_hit</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p3361197595"><a name="p3361197595"></a><a name="p3361197595"></a>Buffer Pool Hit Rate</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p163616905915"><a name="p163616905915"></a><a name="p163616905915"></a>Ratio of read hits to read requests in the InnoDB buffer</p>
<p id="p96437119192"><a name="p96437119192"></a><a name="p96437119192"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p636189105911"><a name="p636189105911"></a><a name="p636189105911"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p736115910597"><a name="p736115910597"></a><a name="p736115910597"></a>Monitored object: database</p>
<p id="p53611910596"><a name="p53611910596"></a><a name="p53611910596"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row836169195912"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p8361189205913"><a name="p8361189205913"></a><a name="p8361189205913"></a>rds012_innodb_buf_dirty</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1636115918598"><a name="p1636115918598"></a><a name="p1636115918598"></a>Buffer Pool Dirty Block Rate</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1236119185918"><a name="p1236119185918"></a><a name="p1236119185918"></a>Ratio of used pages to total data in the InnoDB buffer</p>
<p id="p1269819951910"><a name="p1269819951910"></a><a name="p1269819951910"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1136189135914"><a name="p1136189135914"></a><a name="p1136189135914"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p33615915919"><a name="p33615915919"></a><a name="p33615915919"></a>Monitored object: database</p>
<p id="p1436199175912"><a name="p1436199175912"></a><a name="p1436199175912"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row1036120919597"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p16361169175912"><a name="p16361169175912"></a><a name="p16361169175912"></a>rds013_innodb_reads</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1336111935916"><a name="p1336111935916"></a><a name="p1336111935916"></a>InnoDB Read Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p13361119125919"><a name="p13361119125919"></a><a name="p13361119125919"></a>Average rate at which data is read by the InnoDB buffer</p>
<p id="p1263417375193"><a name="p1263417375193"></a><a name="p1263417375193"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p03619975910"><a name="p03619975910"></a><a name="p03619975910"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p9361139175910"><a name="p9361139175910"></a><a name="p9361139175910"></a>Monitored object: database</p>
<p id="p6361129195915"><a name="p6361129195915"></a><a name="p6361129195915"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row153617925915"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p103616910594"><a name="p103616910594"></a><a name="p103616910594"></a>rds014_innodb_writes</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p16361393590"><a name="p16361393590"></a><a name="p16361393590"></a>InnoDB Write Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p136111911597"><a name="p136111911597"></a><a name="p136111911597"></a>Average rate at which data is written by the InnoDB buffer</p>
<p id="p1575314315187"><a name="p1575314315187"></a><a name="p1575314315187"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p163611925911"><a name="p163611925911"></a><a name="p163611925911"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1136218913591"><a name="p1136218913591"></a><a name="p1136218913591"></a>Monitored object: database</p>
<p id="p3362179185911"><a name="p3362179185911"></a><a name="p3362179185911"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row163621997595"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1336212912599"><a name="p1336212912599"></a><a name="p1336212912599"></a>rds015_innodb_read_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p193624955910"><a name="p193624955910"></a><a name="p193624955910"></a>InnoDB File Read Frequency</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p636219913594"><a name="p636219913594"></a><a name="p636219913594"></a>Average rate at which the InnoDB reads files</p>
<p id="p2711937191817"><a name="p2711937191817"></a><a name="p2711937191817"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p33621091594"><a name="p33621091594"></a><a name="p33621091594"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1836218920599"><a name="p1836218920599"></a><a name="p1836218920599"></a>Monitored object: database</p>
<p id="p1436218919595"><a name="p1436218919595"></a><a name="p1436218919595"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row93621195590"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p123621913591"><a name="p123621913591"></a><a name="p123621913591"></a>rds016_innodb_write_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p163621995918"><a name="p163621995918"></a><a name="p163621995918"></a>InnoDB File Write Frequency</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p336216911598"><a name="p336216911598"></a><a name="p336216911598"></a>Average rate at which the InnoDB writes data</p>
<p id="p523635131819"><a name="p523635131819"></a><a name="p523635131819"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p336211911599"><a name="p336211911599"></a><a name="p336211911599"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1836212913592"><a name="p1836212913592"></a><a name="p1836212913592"></a>Monitored object: database</p>
<p id="p336212918597"><a name="p336212918597"></a><a name="p336212918597"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row33621195592"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p836216935913"><a name="p836216935913"></a><a name="p836216935913"></a>rds017_innodb_log_write_req_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p153628955918"><a name="p153628955918"></a><a name="p153628955918"></a>InnoDB Log Write Request Frequency</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p33628920593"><a name="p33628920593"></a><a name="p33628920593"></a>Average rate at which log write requests are received</p>
<p id="p1913218328186"><a name="p1913218328186"></a><a name="p1913218328186"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p113624925912"><a name="p113624925912"></a><a name="p113624925912"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p153621797591"><a name="p153621797591"></a><a name="p153621797591"></a>Monitored object: database</p>
<p id="p1536218975912"><a name="p1536218975912"></a><a name="p1536218975912"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row143624995912"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p183627945919"><a name="p183627945919"></a><a name="p183627945919"></a>rds018_innodb_log_write_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1736214920594"><a name="p1736214920594"></a><a name="p1736214920594"></a>InnoDB Log Physical Write Frequency</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p93626912593"><a name="p93626912593"></a><a name="p93626912593"></a>Average rate at which log write requests are received</p>
<p id="p2576202311812"><a name="p2576202311812"></a><a name="p2576202311812"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p13624945918"><a name="p13624945918"></a><a name="p13624945918"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p123629911593"><a name="p123629911593"></a><a name="p123629911593"></a>Monitored object: database</p>
<p id="p13625919595"><a name="p13625919595"></a><a name="p13625919595"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row1136389135917"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p17363179165917"><a name="p17363179165917"></a><a name="p17363179165917"></a>rds019_innodb_log_fsync_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p19363999595"><a name="p19363999595"></a><a name="p19363999595"></a>InnoDB Log fsync() Write Frequency</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p133631492596"><a name="p133631492596"></a><a name="p133631492596"></a>Average rate at which fsync() write requests on log files are received</p>
<p id="p34661949111617"><a name="p34661949111617"></a><a name="p34661949111617"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p036314975910"><a name="p036314975910"></a><a name="p036314975910"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p336318911599"><a name="p336318911599"></a><a name="p336318911599"></a>Monitored object: database</p>
<p id="p63631199594"><a name="p63631199594"></a><a name="p63631199594"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row336314912593"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p53638915592"><a name="p53638915592"></a><a name="p53638915592"></a>rds020_temp_tbl_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p236311912595"><a name="p236311912595"></a><a name="p236311912595"></a>Temporary Tables Qty</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p10363894594"><a name="p10363894594"></a><a name="p10363894594"></a>Number of temporary tables automatically created on hard disks when MySQL statements are executed</p>
<p id="p146181827101610"><a name="p146181827101610"></a><a name="p146181827101610"></a>Unit: Table</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1036320913591"><a name="p1036320913591"></a><a name="p1036320913591"></a>≥ 0 tables</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1436359115914"><a name="p1436359115914"></a><a name="p1436359115914"></a>Monitored object: database</p>
<p id="p1836319955914"><a name="p1836319955914"></a><a name="p1836319955914"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row03637945918"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p163630925912"><a name="p163630925912"></a><a name="p163630925912"></a>rds021_myisam_buf_usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1236316911593"><a name="p1236316911593"></a><a name="p1236316911593"></a>Key Buffer Usage</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p113634985914"><a name="p113634985914"></a><a name="p113634985914"></a>MyISAM key buffer usage ratio</p>
<p id="p19113445101418"><a name="p19113445101418"></a><a name="p19113445101418"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p236318919599"><a name="p236318919599"></a><a name="p236318919599"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1136309145916"><a name="p1136309145916"></a><a name="p1136309145916"></a>Monitored object: database</p>
<p id="p4363194592"><a name="p4363194592"></a><a name="p4363194592"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row436311914590"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p18363895599"><a name="p18363895599"></a><a name="p18363895599"></a>rds022_myisam_buf_write_hit</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p14363129105918"><a name="p14363129105918"></a><a name="p14363129105918"></a>Key Buffer Write Hit Rate</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p113634918598"><a name="p113634918598"></a><a name="p113634918598"></a>MyISAM Key buffer write hit ratio of the monitored object</p>
<p id="p1080323620141"><a name="p1080323620141"></a><a name="p1080323620141"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p3363694595"><a name="p3363694595"></a><a name="p3363694595"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p123648910594"><a name="p123648910594"></a><a name="p123648910594"></a>Monitored object: database</p>
<p id="p93644913596"><a name="p93644913596"></a><a name="p93644913596"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row13364129135915"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p15364179105911"><a name="p15364179105911"></a><a name="p15364179105911"></a>rds023_myisam_buf_read_hit</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p183641396597"><a name="p183641396597"></a><a name="p183641396597"></a>Key Buffer Read Hit Rate</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1336415925918"><a name="p1336415925918"></a><a name="p1336415925918"></a>MyISAM Key buffer read hit ratio of the monitored object</p>
<p id="p028422031418"><a name="p028422031418"></a><a name="p028422031418"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p19364179155912"><a name="p19364179155912"></a><a name="p19364179155912"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p18364109185910"><a name="p18364109185910"></a><a name="p18364109185910"></a>Monitored object: database</p>
<p id="p163641493599"><a name="p163641493599"></a><a name="p163641493599"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row93641910592"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p03641399592"><a name="p03641399592"></a><a name="p03641399592"></a>rds024_myisam_disk_write_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p11364095599"><a name="p11364095599"></a><a name="p11364095599"></a>MyISAM Disk Write Frequency</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p16364198590"><a name="p16364198590"></a><a name="p16364198590"></a>Rate at which indexes are written into disks</p>
<p id="p13891164012138"><a name="p13891164012138"></a><a name="p13891164012138"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1336411911594"><a name="p1336411911594"></a><a name="p1336411911594"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p183643914590"><a name="p183643914590"></a><a name="p183643914590"></a>Monitored object: database</p>
<p id="p7364139185912"><a name="p7364139185912"></a><a name="p7364139185912"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row23644915597"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p143641399598"><a name="p143641399598"></a><a name="p143641399598"></a>rds025_myisam_disk_read_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p836499155916"><a name="p836499155916"></a><a name="p836499155916"></a>MyISAM Disk Read Frequency</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p43641097599"><a name="p43641097599"></a><a name="p43641097599"></a>Rate at which indexes are read from disks</p>
<p id="p137663416139"><a name="p137663416139"></a><a name="p137663416139"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p173641596596"><a name="p173641596596"></a><a name="p173641596596"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p153645925912"><a name="p153645925912"></a><a name="p153645925912"></a>Monitored object: database</p>
<p id="p18364391597"><a name="p18364391597"></a><a name="p18364391597"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row1836479135916"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p836429115912"><a name="p836429115912"></a><a name="p836429115912"></a>rds026_myisam_buf_write_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p8364109145919"><a name="p8364109145919"></a><a name="p8364109145919"></a>MyISAM Buffer Pool Write Frequency</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p19365149185910"><a name="p19365149185910"></a><a name="p19365149185910"></a>Rate at which requests on writing indexes into the MyISAM buffer pool are received</p>
<p id="p141967287138"><a name="p141967287138"></a><a name="p141967287138"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p136514925912"><a name="p136514925912"></a><a name="p136514925912"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p736539165914"><a name="p736539165914"></a><a name="p736539165914"></a>Monitored object: database</p>
<p id="p19365139105913"><a name="p19365139105913"></a><a name="p19365139105913"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row19365594592"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1336513918596"><a name="p1336513918596"></a><a name="p1336513918596"></a>rds027_myisam_buf_read_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p53651595599"><a name="p53651595599"></a><a name="p53651595599"></a>MyISAM Buffer Pool Read Frequency</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p03651991597"><a name="p03651991597"></a><a name="p03651991597"></a>Rate at which requests on reading indexes from the MyISAM buffer pool are received</p>
<p id="p17634610161116"><a name="p17634610161116"></a><a name="p17634610161116"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p133653918598"><a name="p133653918598"></a><a name="p133653918598"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p236512945920"><a name="p236512945920"></a><a name="p236512945920"></a>Monitored object: database</p>
<p id="p7365149145913"><a name="p7365149145913"></a><a name="p7365149145913"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row183655925916"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p13651395594"><a name="p13651395594"></a><a name="p13651395594"></a>rds028_comdml_del_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p236599205918"><a name="p236599205918"></a><a name="p236599205918"></a>Delete Operations per Second</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p53651293599"><a name="p53651293599"></a><a name="p53651293599"></a>Average rate at which Delete statements are executed</p>
<p id="p33471828396"><a name="p33471828396"></a><a name="p33471828396"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p20932170131014"><a name="p20932170131014"></a><a name="p20932170131014"></a>≥ 0 executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p736509135913"><a name="p736509135913"></a><a name="p736509135913"></a>Monitored object: database</p>
<p id="p1365697597"><a name="p1365697597"></a><a name="p1365697597"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row53655919592"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p736589195913"><a name="p736589195913"></a><a name="p736589195913"></a>rds029_comdml_ins_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p15365149105916"><a name="p15365149105916"></a><a name="p15365149105916"></a>Insert Operations per Second</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1136511915596"><a name="p1136511915596"></a><a name="p1136511915596"></a>Average rate at which Insert statements are executed</p>
<p id="p9171646101111"><a name="p9171646101111"></a><a name="p9171646101111"></a>Unit: Execution/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p18409147151020"><a name="p18409147151020"></a><a name="p18409147151020"></a>≥ 0 executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p2036518975910"><a name="p2036518975910"></a><a name="p2036518975910"></a>Monitored object: database</p>
<p id="p63650985910"><a name="p63650985910"></a><a name="p63650985910"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row1536510985912"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1736614975910"><a name="p1736614975910"></a><a name="p1736614975910"></a>rds030_comdml_ins_sel_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p6366596598"><a name="p6366596598"></a><a name="p6366596598"></a>Insert_Select Operations per Second</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p17366169125915"><a name="p17366169125915"></a><a name="p17366169125915"></a>Average rate at which Insert-Select statements are executed</p>
<p id="p1384518191791"><a name="p1384518191791"></a><a name="p1384518191791"></a>Unit: Execution/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p86138951015"><a name="p86138951015"></a><a name="p86138951015"></a>≥ 0 executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p43669920596"><a name="p43669920596"></a><a name="p43669920596"></a>Monitored object: database</p>
<p id="p193661893594"><a name="p193661893594"></a><a name="p193661893594"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row936614920593"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p13366494598"><a name="p13366494598"></a><a name="p13366494598"></a>rds031_comdml_rep_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p153664985916"><a name="p153664985916"></a><a name="p153664985916"></a>Replace Operations per Second</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p8366097595"><a name="p8366097595"></a><a name="p8366097595"></a>Average rate at which Replace statements are executed</p>
<p id="p1912945161117"><a name="p1912945161117"></a><a name="p1912945161117"></a>Unit: Execution/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1661349181012"><a name="p1661349181012"></a><a name="p1661349181012"></a>≥ 0 executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p036610919598"><a name="p036610919598"></a><a name="p036610919598"></a>Monitored object: database</p>
<p id="p53662985914"><a name="p53662985914"></a><a name="p53662985914"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row73661296599"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p436611912591"><a name="p436611912591"></a><a name="p436611912591"></a>rds032_comdml_rep_sel_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p236611911595"><a name="p236611911595"></a><a name="p236611911595"></a>Replace_Selection Operations per Second</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1336669155916"><a name="p1336669155916"></a><a name="p1336669155916"></a>Average rate at which Replace_Selection statements are executed</p>
<p id="p1453919394406"><a name="p1453919394406"></a><a name="p1453919394406"></a>Unit: Execution/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1096614112102"><a name="p1096614112102"></a><a name="p1096614112102"></a>≥ 0 executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1136613985914"><a name="p1136613985914"></a><a name="p1136613985914"></a>Monitored object: database</p>
<p id="p16366149105911"><a name="p16366149105911"></a><a name="p16366149105911"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row33661192593"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p5366399599"><a name="p5366399599"></a><a name="p5366399599"></a>rds033_comdml_sel_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1636609125916"><a name="p1636609125916"></a><a name="p1636609125916"></a>Select Operations per Second</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p113679975912"><a name="p113679975912"></a><a name="p113679975912"></a>Average rate at which Select statements are executed</p>
<p id="p633112864019"><a name="p633112864019"></a><a name="p633112864019"></a>Unit: Execution/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p16966151119107"><a name="p16966151119107"></a><a name="p16966151119107"></a>≥ 0 executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p4367199205912"><a name="p4367199205912"></a><a name="p4367199205912"></a>Monitored object: database</p>
<p id="p133676925917"><a name="p133676925917"></a><a name="p133676925917"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row536714915920"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p8367694595"><a name="p8367694595"></a><a name="p8367694595"></a>rds034_comdml_upd_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p636710913597"><a name="p636710913597"></a><a name="p636710913597"></a>Update Operations per Second</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1336719145916"><a name="p1336719145916"></a><a name="p1336719145916"></a>Average rate at which Update statements are executed</p>
<p id="p132481414184019"><a name="p132481414184019"></a><a name="p132481414184019"></a>Unit: Execution/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p144819816129"><a name="p144819816129"></a><a name="p144819816129"></a>≥ 0 executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p4367159165919"><a name="p4367159165919"></a><a name="p4367159165919"></a>Monitored object: database</p>
<p id="p736710916591"><a name="p736710916591"></a><a name="p736710916591"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row036769115913"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1336717975916"><a name="p1336717975916"></a><a name="p1336717975916"></a>rds035_innodb_del_row_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p536719185913"><a name="p536719185913"></a><a name="p536719185913"></a>Row Delete Speed</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p2367594591"><a name="p2367594591"></a><a name="p2367594591"></a>Average rate at which rows are deleted from the InnoDB table</p>
<p id="p53681853143410"><a name="p53681853143410"></a><a name="p53681853143410"></a>Unit: Row/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p193676913599"><a name="p193676913599"></a><a name="p193676913599"></a>≥ 0 rows/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1636710919592"><a name="p1636710919592"></a><a name="p1636710919592"></a>Monitored object: database</p>
<p id="p836711915594"><a name="p836711915594"></a><a name="p836711915594"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row83673965914"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1436769105913"><a name="p1436769105913"></a><a name="p1436769105913"></a>rds036_innodb_ins_row_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p9367199195912"><a name="p9367199195912"></a><a name="p9367199195912"></a>Row Insert Speed</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p9367149185917"><a name="p9367149185917"></a><a name="p9367149185917"></a>Average rate at which rows are inserted into the InnoDB table</p>
<p id="p324894814344"><a name="p324894814344"></a><a name="p324894814344"></a>Unit: Row/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p836720975912"><a name="p836720975912"></a><a name="p836720975912"></a>≥ 0 rows/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p193682919593"><a name="p193682919593"></a><a name="p193682919593"></a>Monitored object: database</p>
<p id="p836811925915"><a name="p836811925915"></a><a name="p836811925915"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row936813995915"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p336819912594"><a name="p336819912594"></a><a name="p336819912594"></a>rds037_innodb_read_row_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p17368209115913"><a name="p17368209115913"></a><a name="p17368209115913"></a>Row Read Speed</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p136820955910"><a name="p136820955910"></a><a name="p136820955910"></a>Average rate at which rows are read from the InnoDB table</p>
<p id="p114031532193414"><a name="p114031532193414"></a><a name="p114031532193414"></a>Unit: Row/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p63681398594"><a name="p63681398594"></a><a name="p63681398594"></a>≥ 0 rows/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p8368169175910"><a name="p8368169175910"></a><a name="p8368169175910"></a>Monitored object: database</p>
<p id="p73681893593"><a name="p73681893593"></a><a name="p73681893593"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row136817918599"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p836815912597"><a name="p836815912597"></a><a name="p836815912597"></a>rds038_innodb_upd_row_count</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1536869115911"><a name="p1536869115911"></a><a name="p1536869115911"></a>Row Update Speed</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p736814919591"><a name="p736814919591"></a><a name="p736814919591"></a>Average rate at which rows are updated in the InnoDB table</p>
<p id="p19274121353414"><a name="p19274121353414"></a><a name="p19274121353414"></a>Unit: Row/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p836829135915"><a name="p836829135915"></a><a name="p836829135915"></a>≥ 0 rows/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1536899105914"><a name="p1536899105914"></a><a name="p1536899105914"></a>Monitored object: database</p>
<p id="p43682945910"><a name="p43682945910"></a><a name="p43682945910"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row183683912598"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p19368696591"><a name="p19368696591"></a><a name="p19368696591"></a>rds039_disk_usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p136889185917"><a name="p136889185917"></a><a name="p136889185917"></a>Disk Utilization </p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p183688945911"><a name="p183688945911"></a><a name="p183688945911"></a>Disk usage of the monitored object</p>
<p id="p261714265333"><a name="p261714265333"></a><a name="p261714265333"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1036810935913"><a name="p1036810935913"></a><a name="p1036810935913"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p8368291593"><a name="p8368291593"></a><a name="p8368291593"></a>Monitored object: ECS</p>
<p id="p1325018114541"><a name="p1325018114541"></a><a name="p1325018114541"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row103699912593"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p436917916599"><a name="p436917916599"></a><a name="p436917916599"></a>rds039_disk_util</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p236919965910"><a name="p236919965910"></a><a name="p236919965910"></a>Disk Utilization</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p7369798594"><a name="p7369798594"></a><a name="p7369798594"></a>Disk usage of the monitored object</p>
<p id="p8896641193318"><a name="p8896641193318"></a><a name="p8896641193318"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p5369189185911"><a name="p5369189185911"></a><a name="p5369189185911"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1836914915594"><a name="p1836914915594"></a><a name="p1836914915594"></a>Monitored object: ECS</p>
<p id="p189408712549"><a name="p189408712549"></a><a name="p189408712549"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row23690910591"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p73702919591"><a name="p73702919591"></a><a name="p73702919591"></a>rds047_disk_total_size</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p2370179105919"><a name="p2370179105919"></a><a name="p2370179105919"></a>Total Disk Size</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p153705915917"><a name="p153705915917"></a><a name="p153705915917"></a>Total disk size of the monitored object</p>
<p id="p15370591598"><a name="p15370591598"></a><a name="p15370591598"></a>Unit: GB</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1937069175911"><a name="p1937069175911"></a><a name="p1937069175911"></a>40-2000 GB</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p93701698597"><a name="p93701698597"></a><a name="p93701698597"></a>Monitored object: ECS</p>
<p id="p7240173117539"><a name="p7240173117539"></a><a name="p7240173117539"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row143701596596"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1370199155919"><a name="p1370199155919"></a><a name="p1370199155919"></a>rds048_disk_used_size</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p11370391595"><a name="p11370391595"></a><a name="p11370391595"></a>Storage Space Used</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1937016911592"><a name="p1937016911592"></a><a name="p1937016911592"></a>Amount of used storage space size of the monitored object</p>
<p id="p1437015917597"><a name="p1437015917597"></a><a name="p1437015917597"></a>Unit: GB</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p13701994593"><a name="p13701994593"></a><a name="p13701994593"></a>0-2000 GB</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p03711993594"><a name="p03711993594"></a><a name="p03711993594"></a>Monitored object: ECS</p>
<p id="p012612240531"><a name="p012612240531"></a><a name="p012612240531"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row13711915598"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p163715925911"><a name="p163715925911"></a><a name="p163715925911"></a>rds049_disk_read_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p23717985920"><a name="p23717985920"></a><a name="p23717985920"></a>Disk Read Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1337129155910"><a name="p1337129155910"></a><a name="p1337129155910"></a>Rate at which data is read from a disk</p>
<p id="p1237139135913"><a name="p1237139135913"></a><a name="p1237139135913"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p123719918598"><a name="p123719918598"></a><a name="p123719918598"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p19371119195915"><a name="p19371119195915"></a><a name="p19371119195915"></a>Monitored object: ECS</p>
<p id="p1221802025318"><a name="p1221802025318"></a><a name="p1221802025318"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row1837115919592"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1937111995914"><a name="p1937111995914"></a><a name="p1937111995914"></a>rds050_disk_write_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p337118914599"><a name="p337118914599"></a><a name="p337118914599"></a>Disk Write Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p5372491599"><a name="p5372491599"></a><a name="p5372491599"></a>Rate at which data is written to a disk</p>
<p id="p133721193599"><a name="p133721193599"></a><a name="p133721193599"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p537214945914"><a name="p537214945914"></a><a name="p537214945914"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p143720925914"><a name="p143720925914"></a><a name="p143720925914"></a>Monitored object: ECS</p>
<p id="p15557131555314"><a name="p15557131555314"></a><a name="p15557131555314"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row53723945917"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p103727965911"><a name="p103727965911"></a><a name="p103727965911"></a>rds051_avg_disk_sec_per_read</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1537259125916"><a name="p1537259125916"></a><a name="p1537259125916"></a>Average Time per Disk Read</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p33721913590"><a name="p33721913590"></a><a name="p33721913590"></a>Time required for reading 1 KB disk data</p>
<p id="p10372697597"><a name="p10372697597"></a><a name="p10372697597"></a>Unit: Second</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p837219145920"><a name="p837219145920"></a><a name="p837219145920"></a>&gt; 0s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p103731999598"><a name="p103731999598"></a><a name="p103731999598"></a>Monitored object: ECS</p>
<p id="p66721512135317"><a name="p66721512135317"></a><a name="p66721512135317"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row17373139185920"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p437319911598"><a name="p437319911598"></a><a name="p437319911598"></a>rds052_avg_disk_sec_per_write</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p2037319965917"><a name="p2037319965917"></a><a name="p2037319965917"></a>Average Time per Disk Write</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p93736955912"><a name="p93736955912"></a><a name="p93736955912"></a>Time required for writing 1 KB data to a disk</p>
<p id="p63735935912"><a name="p63735935912"></a><a name="p63735935912"></a>Unit: Second</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1937316911596"><a name="p1937316911596"></a><a name="p1937316911596"></a>&gt; 0s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1373799594"><a name="p1373799594"></a><a name="p1373799594"></a>Monitored object: ECS</p>
<p id="p1015115910534"><a name="p1015115910534"></a><a name="p1015115910534"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
<tr id="row237399195913"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p937339165913"><a name="p937339165913"></a><a name="p937339165913"></a>rds053_avg_disk_queue_length</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1237320915592"><a name="p1237320915592"></a><a name="p1237320915592"></a>Average Disk Queue Length</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p4373129155919"><a name="p4373129155919"></a><a name="p4373129155919"></a>Number of processes waiting to be written to the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p937311905916"><a name="p937311905916"></a><a name="p937311905916"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p937418995914"><a name="p937418995914"></a><a name="p937418995914"></a>Monitored object: ECS</p>
<p id="p96171165537"><a name="p96171165537"></a><a name="p96171165537"></a>Monitored instance type: MySQL instance</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  PostgreSQL metrics

<a name="table9451145782618"></a>
<table><thead align="left"><tr id="row144511357162615"><th class="cellrowborder" valign="top" width="15.229999999999999%" id="mcps1.2.6.1.1"><p id="p2452185710269"><a name="p2452185710269"></a><a name="p2452185710269"></a><strong id="b1572366420"><a name="b1572366420"></a><a name="b1572366420"></a>Metric</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.370000000000001%" id="mcps1.2.6.1.2"><p id="p9452105762616"><a name="p9452105762616"></a><a name="p9452105762616"></a><strong id="b2072325305"><a name="b2072325305"></a><a name="b2072325305"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.709999999999997%" id="mcps1.2.6.1.3"><p id="p12452557122613"><a name="p12452557122613"></a><a name="p12452557122613"></a><strong id="b1130762412"><a name="b1130762412"></a><a name="b1130762412"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.99%" id="mcps1.2.6.1.4"><p id="p8452165782614"><a name="p8452165782614"></a><a name="p8452165782614"></a><strong id="b940335233"><a name="b940335233"></a><a name="b940335233"></a>Value Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.7%" id="mcps1.2.6.1.5"><p id="p1645213571262"><a name="p1645213571262"></a><a name="p1645213571262"></a><strong id="b1433912248"><a name="b1433912248"></a><a name="b1433912248"></a>Remarks</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row184521157192617"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p6452357202619"><a name="p6452357202619"></a><a name="p6452357202619"></a>rds001_cpu_usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p19452257132613"><a name="p19452257132613"></a><a name="p19452257132613"></a>CPU Usage (deprecated)</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p64522578262"><a name="p64522578262"></a><a name="p64522578262"></a>CPU usage of the monitored object</p>
<p id="p7353134662915"><a name="p7353134662915"></a><a name="p7353134662915"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p11452175716269"><a name="p11452175716269"></a><a name="p11452175716269"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1445255732617"><a name="p1445255732617"></a><a name="p1445255732617"></a>Monitored object: ECS</p>
<p id="p12452185752617"><a name="p12452185752617"></a><a name="p12452185752617"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row745205792617"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p345235720268"><a name="p345235720268"></a><a name="p345235720268"></a>rds001_cpu_util</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p2045212575263"><a name="p2045212575263"></a><a name="p2045212575263"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p12452457122612"><a name="p12452457122612"></a><a name="p12452457122612"></a>CPU usage of the monitored object</p>
<p id="p999316266305"><a name="p999316266305"></a><a name="p999316266305"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p19452657102613"><a name="p19452657102613"></a><a name="p19452657102613"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p3452115762613"><a name="p3452115762613"></a><a name="p3452115762613"></a>Monitored object: ECS</p>
<p id="p12453105718268"><a name="p12453105718268"></a><a name="p12453105718268"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row1445311570264"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1445305712616"><a name="p1445305712616"></a><a name="p1445305712616"></a>rds002_mem_usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1545316570265"><a name="p1545316570265"></a><a name="p1545316570265"></a>Memory Usage (deprecated)</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p14453175711262"><a name="p14453175711262"></a><a name="p14453175711262"></a>Memory usage of the monitored object</p>
<p id="p19414171316304"><a name="p19414171316304"></a><a name="p19414171316304"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1545345712262"><a name="p1545345712262"></a><a name="p1545345712262"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p145335712617"><a name="p145335712617"></a><a name="p145335712617"></a>Monitored object: ECS</p>
<p id="p34531357142617"><a name="p34531357142617"></a><a name="p34531357142617"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row0453457122612"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p11453155713261"><a name="p11453155713261"></a><a name="p11453155713261"></a>rds002_mem_util</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p64532057112614"><a name="p64532057112614"></a><a name="p64532057112614"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p645395712619"><a name="p645395712619"></a><a name="p645395712619"></a>Memory consumed by the monitored object</p>
<p id="p470317387308"><a name="p470317387308"></a><a name="p470317387308"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p18453357172615"><a name="p18453357172615"></a><a name="p18453357172615"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p94539575269"><a name="p94539575269"></a><a name="p94539575269"></a>Monitored object: ECS</p>
<p id="p134537577263"><a name="p134537577263"></a><a name="p134537577263"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row8453165792612"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p14453155792613"><a name="p14453155792613"></a><a name="p14453155792613"></a>rds003_iops</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1645345716265"><a name="p1645345716265"></a><a name="p1645345716265"></a>IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1845375762618"><a name="p1845375762618"></a><a name="p1845375762618"></a>Average rate at which I/O requests are processed during a specified period</p>
<p id="p15242145014308"><a name="p15242145014308"></a><a name="p15242145014308"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p10453155717269"><a name="p10453155717269"></a><a name="p10453155717269"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1045316572269"><a name="p1045316572269"></a><a name="p1045316572269"></a>Monitored object: ECS</p>
<p id="p12453175719265"><a name="p12453175719265"></a><a name="p12453175719265"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row12453105742613"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p18453057202620"><a name="p18453057202620"></a><a name="p18453057202620"></a>rds004_bytes_in</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p2453155710265"><a name="p2453155710265"></a><a name="p2453155710265"></a>Network Input Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p19453175719268"><a name="p19453175719268"></a><a name="p19453175719268"></a>Rate at which all incoming traffic passes through the network adapter</p>
<p id="p173203793110"><a name="p173203793110"></a><a name="p173203793110"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p745315579264"><a name="p745315579264"></a><a name="p745315579264"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p5453195732618"><a name="p5453195732618"></a><a name="p5453195732618"></a>Monitored object: ECS</p>
<p id="p94541457202616"><a name="p94541457202616"></a><a name="p94541457202616"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row4454195722615"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p174541057132611"><a name="p174541057132611"></a><a name="p174541057132611"></a>rds005_bytes_out</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p15454115712617"><a name="p15454115712617"></a><a name="p15454115712617"></a>Network Output Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1045475716268"><a name="p1045475716268"></a><a name="p1045475716268"></a>Rate at which all outgoing traffic passes through the network adapter</p>
<p id="p1452114293117"><a name="p1452114293117"></a><a name="p1452114293117"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p0454357142614"><a name="p0454357142614"></a><a name="p0454357142614"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p16454757162617"><a name="p16454757162617"></a><a name="p16454757162617"></a>Monitored object: ECS</p>
<p id="p19454257172610"><a name="p19454257172610"></a><a name="p19454257172610"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row1646318576269"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p6464857142610"><a name="p6464857142610"></a><a name="p6464857142610"></a>rds039_disk_usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p17464857112617"><a name="p17464857112617"></a><a name="p17464857112617"></a>Disk Utilization (deprecated)</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p154646577264"><a name="p154646577264"></a><a name="p154646577264"></a>Disk usage of the monitored object</p>
<p id="p1749112187302"><a name="p1749112187302"></a><a name="p1749112187302"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p15464115717261"><a name="p15464115717261"></a><a name="p15464115717261"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1346465710261"><a name="p1346465710261"></a><a name="p1346465710261"></a>Monitored object: ECS</p>
<p id="p16278161843610"><a name="p16278161843610"></a><a name="p16278161843610"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row8464175752612"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p046418571268"><a name="p046418571268"></a><a name="p046418571268"></a>rds039_disk_util</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p146415571262"><a name="p146415571262"></a><a name="p146415571262"></a>Disk Utilization</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p0464195715267"><a name="p0464195715267"></a><a name="p0464195715267"></a>Disk usage of the monitored object</p>
<p id="p587201334410"><a name="p587201334410"></a><a name="p587201334410"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p44643577267"><a name="p44643577267"></a><a name="p44643577267"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1146416578260"><a name="p1146416578260"></a><a name="p1146416578260"></a>Monitored object: ECS</p>
<p id="p717042219364"><a name="p717042219364"></a><a name="p717042219364"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row546555732619"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p3465135742610"><a name="p3465135742610"></a><a name="p3465135742610"></a>rds040_transaction_logs_usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p74650577265"><a name="p74650577265"></a><a name="p74650577265"></a>Transaction Logs Usage</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p446515742610"><a name="p446515742610"></a><a name="p446515742610"></a>Disk capacity used by transaction logs</p>
<p id="p19465145711261"><a name="p19465145711261"></a><a name="p19465145711261"></a>Unit: MB</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p16465165732615"><a name="p16465165732615"></a><a name="p16465165732615"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1646575717261"><a name="p1646575717261"></a><a name="p1646575717261"></a>Monitored object: database</p>
<p id="p8465457132618"><a name="p8465457132618"></a><a name="p8465457132618"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row7465125719264"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p346525710265"><a name="p346525710265"></a><a name="p346525710265"></a>rds041_replication_slot_usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1646512579269"><a name="p1646512579269"></a><a name="p1646512579269"></a>Replication Slot Usage</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p9465157152611"><a name="p9465157152611"></a><a name="p9465157152611"></a>Disk capacity used by replication slot files</p>
<p id="p646585792618"><a name="p646585792618"></a><a name="p646585792618"></a>Unit: MB</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p11465135712267"><a name="p11465135712267"></a><a name="p11465135712267"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p124658578260"><a name="p124658578260"></a><a name="p124658578260"></a>Monitored object: database</p>
<p id="p24650577266"><a name="p24650577266"></a><a name="p24650577266"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row114651657112620"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1346585713267"><a name="p1346585713267"></a><a name="p1346585713267"></a>rds042_database_connections</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p24651657162616"><a name="p24651657162616"></a><a name="p24651657162616"></a>Recommended Maximum Database Connections</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1846595732620"><a name="p1846595732620"></a><a name="p1846595732620"></a>Recommended maximum number of database connections</p>
<p id="p1746505732613"><a name="p1746505732613"></a><a name="p1746505732613"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p13465185792614"><a name="p13465185792614"></a><a name="p13465185792614"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p6465757192613"><a name="p6465757192613"></a><a name="p6465757192613"></a>Monitored object: database</p>
<p id="p146517576267"><a name="p146517576267"></a><a name="p146517576267"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row2046515715263"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1446518573265"><a name="p1446518573265"></a><a name="p1446518573265"></a>rds043_maximum_used_transaction_ids</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p5466145716267"><a name="p5466145716267"></a><a name="p5466145716267"></a>Maximum Used Transaction IDs</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p64667575263"><a name="p64667575263"></a><a name="p64667575263"></a>Maximum transaction IDs that have been used</p>
<p id="p204661757142610"><a name="p204661757142610"></a><a name="p204661757142610"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p194661357102619"><a name="p194661357102619"></a><a name="p194661357102619"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1446618574263"><a name="p1446618574263"></a><a name="p1446618574263"></a>Monitored object: database</p>
<p id="p144661257112610"><a name="p144661257112610"></a><a name="p144661257112610"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row184663575262"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p246695792612"><a name="p246695792612"></a><a name="p246695792612"></a>rds044_transaction_logs_generations</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p17466185716268"><a name="p17466185716268"></a><a name="p17466185716268"></a>Transaction Logs Generations</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p8466175719266"><a name="p8466175719266"></a><a name="p8466175719266"></a>Size of transaction logs generated per second</p>
<p id="p13466155722616"><a name="p13466155722616"></a><a name="p13466155722616"></a>Unit: MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p9466155752610"><a name="p9466155752610"></a><a name="p9466155752610"></a>≥ 0 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p9466145732616"><a name="p9466145732616"></a><a name="p9466145732616"></a>Monitored object: database</p>
<p id="p346615578260"><a name="p346615578260"></a><a name="p346615578260"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row14466957182614"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p154661357172612"><a name="p154661357172612"></a><a name="p154661357172612"></a>rds045_oldest_replication_slot_lag</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p7466125732610"><a name="p7466125732610"></a><a name="p7466125732610"></a>Oldest Replication Slot Lag</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p946665772615"><a name="p946665772615"></a><a name="p946665772615"></a>Lagging size of the most lagging replica in terms of WAL data received</p>
<p id="p94661576260"><a name="p94661576260"></a><a name="p94661576260"></a>Unit: MB</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1146645752618"><a name="p1146645752618"></a><a name="p1146645752618"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p10467165715264"><a name="p10467165715264"></a><a name="p10467165715264"></a>Monitored object: database</p>
<p id="p746765712618"><a name="p746765712618"></a><a name="p746765712618"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row54671757102610"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1446715732611"><a name="p1446715732611"></a><a name="p1446715732611"></a>rds046_replication_lag</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1146715573263"><a name="p1146715573263"></a><a name="p1146715573263"></a>Replication Lag</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p15467195762616"><a name="p15467195762616"></a><a name="p15467195762616"></a>Replication lag delay</p>
<p id="p946795716269"><a name="p946795716269"></a><a name="p946795716269"></a>Unit: ms</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p124674571265"><a name="p124674571265"></a><a name="p124674571265"></a>≥ 0 ms</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p94678578261"><a name="p94678578261"></a><a name="p94678578261"></a>Monitored object: database</p>
<p id="p12467195717264"><a name="p12467195717264"></a><a name="p12467195717264"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row194671757202617"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1246765732613"><a name="p1246765732613"></a><a name="p1246765732613"></a>rds047_disk_total_size</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p8467175715268"><a name="p8467175715268"></a><a name="p8467175715268"></a>Total Disk Size</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p11467195713268"><a name="p11467195713268"></a><a name="p11467195713268"></a>Total disk size of the monitored object</p>
<p id="p1546755713269"><a name="p1546755713269"></a><a name="p1546755713269"></a>Unit: GB</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p346755772617"><a name="p346755772617"></a><a name="p346755772617"></a>40-2000 GB</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p18468185742613"><a name="p18468185742613"></a><a name="p18468185742613"></a>Monitored object: ECS</p>
<p id="p6641330202212"><a name="p6641330202212"></a><a name="p6641330202212"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row14468145713266"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1468557152620"><a name="p1468557152620"></a><a name="p1468557152620"></a>rds048_disk_used_size</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p24683573262"><a name="p24683573262"></a><a name="p24683573262"></a>Storage Space Used</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p19468175718267"><a name="p19468175718267"></a><a name="p19468175718267"></a>Amount of used storage space size of the monitored object</p>
<p id="p446875722619"><a name="p446875722619"></a><a name="p446875722619"></a>Unit: GB</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p34681157182615"><a name="p34681157182615"></a><a name="p34681157182615"></a>0-2000 GB</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p11468175717267"><a name="p11468175717267"></a><a name="p11468175717267"></a>Monitored object: ECS</p>
<p id="p877793315226"><a name="p877793315226"></a><a name="p877793315226"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row2469757142614"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p646914575261"><a name="p646914575261"></a><a name="p646914575261"></a>rds049_disk_read_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p12469145792612"><a name="p12469145792612"></a><a name="p12469145792612"></a>Disk Read Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p346915720267"><a name="p346915720267"></a><a name="p346915720267"></a>Rate at which data is read from a disk</p>
<p id="p8469145712261"><a name="p8469145712261"></a><a name="p8469145712261"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p246905782615"><a name="p246905782615"></a><a name="p246905782615"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p164691157192612"><a name="p164691157192612"></a><a name="p164691157192612"></a>Monitored object: ECS</p>
<p id="p85251237182219"><a name="p85251237182219"></a><a name="p85251237182219"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row246915762613"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p14696579260"><a name="p14696579260"></a><a name="p14696579260"></a>rds050_disk_write_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p12469125752613"><a name="p12469125752613"></a><a name="p12469125752613"></a>Disk Write Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p13469257122613"><a name="p13469257122613"></a><a name="p13469257122613"></a>Rate at which data is written to a disk</p>
<p id="p04691579268"><a name="p04691579268"></a><a name="p04691579268"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1746965712260"><a name="p1746965712260"></a><a name="p1746965712260"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p134691057152617"><a name="p134691057152617"></a><a name="p134691057152617"></a>Monitored object: ECS</p>
<p id="p26174142217"><a name="p26174142217"></a><a name="p26174142217"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row114695572267"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p194693572269"><a name="p194693572269"></a><a name="p194693572269"></a>rds051_avg_disk_sec_per_read</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p2470125782619"><a name="p2470125782619"></a><a name="p2470125782619"></a>Average Time per Disk Read</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p64702057102617"><a name="p64702057102617"></a><a name="p64702057102617"></a>Time required for reading 1 KB disk data</p>
<p id="p19470657142612"><a name="p19470657142612"></a><a name="p19470657142612"></a>Unit: Second</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p18470957142611"><a name="p18470957142611"></a><a name="p18470957142611"></a>&gt; 0s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p947035752613"><a name="p947035752613"></a><a name="p947035752613"></a>Monitored object: ECS</p>
<p id="p64351044162210"><a name="p64351044162210"></a><a name="p64351044162210"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row4470155713267"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p447017571265"><a name="p447017571265"></a><a name="p447017571265"></a>rds052_avg_disk_sec_per_write</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1947016571269"><a name="p1947016571269"></a><a name="p1947016571269"></a>Average Time per Disk Write</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p4470145710266"><a name="p4470145710266"></a><a name="p4470145710266"></a>Time required for writing 1 KB data to a disk</p>
<p id="p194701572267"><a name="p194701572267"></a><a name="p194701572267"></a>Unit: Second</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p8470145772613"><a name="p8470145772613"></a><a name="p8470145772613"></a>&gt; 0s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p14702574260"><a name="p14702574260"></a><a name="p14702574260"></a>Monitored object: ECS</p>
<p id="p2498164719225"><a name="p2498164719225"></a><a name="p2498164719225"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
<tr id="row1047025792618"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p13470115711269"><a name="p13470115711269"></a><a name="p13470115711269"></a>rds053_avg_disk_queue_length</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p0470165714269"><a name="p0470165714269"></a><a name="p0470165714269"></a>Average Disk Queue Length</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p547119576263"><a name="p547119576263"></a><a name="p547119576263"></a>Number of processes waiting to be written to the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p647185772620"><a name="p647185772620"></a><a name="p647185772620"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1247145717268"><a name="p1247145717268"></a><a name="p1247145717268"></a>Monitored object: ECS</p>
<p id="p17471205717265"><a name="p17471205717265"></a><a name="p17471205717265"></a>Monitored instance type: PostgreSQL instance</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Microsoft SQL Server metrics

<a name="table11393103513397"></a>
<table><thead align="left"><tr id="row153942357392"><th class="cellrowborder" valign="top" width="15.229999999999999%" id="mcps1.2.6.1.1"><p id="p53941357397"><a name="p53941357397"></a><a name="p53941357397"></a><strong id="b1710092385"><a name="b1710092385"></a><a name="b1710092385"></a>Metric</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.370000000000001%" id="mcps1.2.6.1.2"><p id="p6394103511399"><a name="p6394103511399"></a><a name="p6394103511399"></a><strong id="b2107832571"><a name="b2107832571"></a><a name="b2107832571"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.709999999999997%" id="mcps1.2.6.1.3"><p id="p11394173543915"><a name="p11394173543915"></a><a name="p11394173543915"></a><strong id="b1635723876"><a name="b1635723876"></a><a name="b1635723876"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.99%" id="mcps1.2.6.1.4"><p id="p2039412357395"><a name="p2039412357395"></a><a name="p2039412357395"></a><strong id="b1111829171"><a name="b1111829171"></a><a name="b1111829171"></a>Value Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.7%" id="mcps1.2.6.1.5"><p id="p12394163512397"><a name="p12394163512397"></a><a name="p12394163512397"></a><strong id="b2051897553"><a name="b2051897553"></a><a name="b2051897553"></a>Remarks</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row3394173511397"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p99146336432"><a name="p99146336432"></a><a name="p99146336432"></a>rds001_cpu_usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1491443344310"><a name="p1491443344310"></a><a name="p1491443344310"></a>CPU Usage (deprecated)</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p159141633124319"><a name="p159141633124319"></a><a name="p159141633124319"></a>CPU usage of the monitored object</p>
<p id="p12692175311160"><a name="p12692175311160"></a><a name="p12692175311160"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p7914133144317"><a name="p7914133144317"></a><a name="p7914133144317"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p691413334436"><a name="p691413334436"></a><a name="p691413334436"></a>Monitored object: ECS</p>
<p id="p6915233174311"><a name="p6915233174311"></a><a name="p6915233174311"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row53951735103913"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1091510336431"><a name="p1091510336431"></a><a name="p1091510336431"></a>rds001_cpu_util</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p169152033154312"><a name="p169152033154312"></a><a name="p169152033154312"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p159151333174311"><a name="p159151333174311"></a><a name="p159151333174311"></a>CPU usage of the monitored object</p>
<p id="p175601921151719"><a name="p175601921151719"></a><a name="p175601921151719"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p3915173304311"><a name="p3915173304311"></a><a name="p3915173304311"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p691515339435"><a name="p691515339435"></a><a name="p691515339435"></a>Monitored object: ECS</p>
<p id="p174041350182418"><a name="p174041350182418"></a><a name="p174041350182418"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row5395173583917"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p18916233184318"><a name="p18916233184318"></a><a name="p18916233184318"></a>rds002_mem_usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p16916203384317"><a name="p16916203384317"></a><a name="p16916203384317"></a>Memory Usage (deprecated)</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1791663313436"><a name="p1791663313436"></a><a name="p1791663313436"></a>Memory usage of the monitored object</p>
<p id="p18348161615175"><a name="p18348161615175"></a><a name="p18348161615175"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1891723318433"><a name="p1891723318433"></a><a name="p1891723318433"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p89171733114310"><a name="p89171733114310"></a><a name="p89171733114310"></a>Monitored object: ECS</p>
<p id="p19917233194317"><a name="p19917233194317"></a><a name="p19917233194317"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row12396103533911"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p15917193313439"><a name="p15917193313439"></a><a name="p15917193313439"></a>rds002_mem_util</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p19917163394314"><a name="p19917163394314"></a><a name="p19917163394314"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p15917123314312"><a name="p15917123314312"></a><a name="p15917123314312"></a>Memory usage of the monitored object</p>
<p id="p7525642161719"><a name="p7525642161719"></a><a name="p7525642161719"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p18917133184319"><a name="p18917133184319"></a><a name="p18917133184319"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p3917203364318"><a name="p3917203364318"></a><a name="p3917203364318"></a>Monitored object: ECS</p>
<p id="p14866124742419"><a name="p14866124742419"></a><a name="p14866124742419"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row1739633573912"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p6918113304311"><a name="p6918113304311"></a><a name="p6918113304311"></a>rds003_iops</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1091817339430"><a name="p1091817339430"></a><a name="p1091817339430"></a>IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p991843314436"><a name="p991843314436"></a><a name="p991843314436"></a>Average rate at which I/O requests are processed during a specified period</p>
<p id="p121414622216"><a name="p121414622216"></a><a name="p121414622216"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p209186334436"><a name="p209186334436"></a><a name="p209186334436"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p491813338431"><a name="p491813338431"></a><a name="p491813338431"></a>Monitored object: ECS</p>
<p id="p191816334431"><a name="p191816334431"></a><a name="p191816334431"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row133965354392"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p10919233134313"><a name="p10919233134313"></a><a name="p10919233134313"></a>rds004_bytes_in</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p291933311435"><a name="p291933311435"></a><a name="p291933311435"></a>Network Input Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p16919333164312"><a name="p16919333164312"></a><a name="p16919333164312"></a>Rate at which all incoming traffic passes through the network adapter</p>
<p id="p165234182217"><a name="p165234182217"></a><a name="p165234182217"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p11919133317438"><a name="p11919133317438"></a><a name="p11919133317438"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p19919933174311"><a name="p19919933174311"></a><a name="p19919933174311"></a>Monitored object: ECS</p>
<p id="p591933314430"><a name="p591933314430"></a><a name="p591933314430"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row13397113517396"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p15919203384318"><a name="p15919203384318"></a><a name="p15919203384318"></a>rds005_bytes_out</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p992018331431"><a name="p992018331431"></a><a name="p992018331431"></a>Network Output Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1992033315433"><a name="p1992033315433"></a><a name="p1992033315433"></a>Rate at which all outgoing traffic passes through the network adapter</p>
<p id="p14384355112211"><a name="p14384355112211"></a><a name="p14384355112211"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p15920123384320"><a name="p15920123384320"></a><a name="p15920123384320"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p189201633164314"><a name="p189201633164314"></a><a name="p189201633164314"></a>Monitored object: ECS</p>
<p id="p11920633164315"><a name="p11920633164315"></a><a name="p11920633164315"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row03977354395"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p8921153364315"><a name="p8921153364315"></a><a name="p8921153364315"></a>rds039_disk_usage</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p3921163374313"><a name="p3921163374313"></a><a name="p3921163374313"></a>Disk Utilization (deprecated)</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p5921143314436"><a name="p5921143314436"></a><a name="p5921143314436"></a>Disk usage of the monitored object</p>
<p id="p14912155192318"><a name="p14912155192318"></a><a name="p14912155192318"></a>Unit: Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p292163344314"><a name="p292163344314"></a><a name="p292163344314"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1192113314318"><a name="p1192113314318"></a><a name="p1192113314318"></a>Monitored object: ECS</p>
<p id="p1992220333435"><a name="p1992220333435"></a><a name="p1992220333435"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row4397335193919"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p14922173315434"><a name="p14922173315434"></a><a name="p14922173315434"></a>rds039_disk_util</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p89221333154312"><a name="p89221333154312"></a><a name="p89221333154312"></a>Disk Utilization</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p192219339436"><a name="p192219339436"></a><a name="p192219339436"></a>Disk usage of the monitored object</p>
<p id="p15627320102315"><a name="p15627320102315"></a><a name="p15627320102315"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1092253312432"><a name="p1092253312432"></a><a name="p1092253312432"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1992223314434"><a name="p1992223314434"></a><a name="p1992223314434"></a>Monitored object: ECS</p>
<p id="p4923103324314"><a name="p4923103324314"></a><a name="p4923103324314"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row1641613543914"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p3416635193914"><a name="p3416635193914"></a><a name="p3416635193914"></a>rds047_disk_total_size</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p184161635153917"><a name="p184161635153917"></a><a name="p184161635153917"></a>Total Disk Size</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p10416203593910"><a name="p10416203593910"></a><a name="p10416203593910"></a>Total disk size of the monitored object</p>
<p id="p13416153510396"><a name="p13416153510396"></a><a name="p13416153510396"></a>Unit: GB</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p7416635123920"><a name="p7416635123920"></a><a name="p7416635123920"></a>40-2000 GB</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p15417435113910"><a name="p15417435113910"></a><a name="p15417435113910"></a>Monitored object: ECS</p>
<p id="p7417133593912"><a name="p7417133593912"></a><a name="p7417133593912"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row0417123573913"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p10417835133919"><a name="p10417835133919"></a><a name="p10417835133919"></a>rds048_disk_used_size</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p1841716358393"><a name="p1841716358393"></a><a name="p1841716358393"></a>Storage Space Used</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p124171135123910"><a name="p124171135123910"></a><a name="p124171135123910"></a>Amount of used storage space size of the monitored object</p>
<p id="p164171035103919"><a name="p164171035103919"></a><a name="p164171035103919"></a>Unit: GB</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p74173356398"><a name="p74173356398"></a><a name="p74173356398"></a>0-2000 GB</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p8417153511399"><a name="p8417153511399"></a><a name="p8417153511399"></a>Monitored object: ECS</p>
<p id="p15200193210246"><a name="p15200193210246"></a><a name="p15200193210246"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row20417835143915"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1141710359393"><a name="p1141710359393"></a><a name="p1141710359393"></a>rds049_disk_read_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p741873593913"><a name="p741873593913"></a><a name="p741873593913"></a>Disk Read Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p2418153512399"><a name="p2418153512399"></a><a name="p2418153512399"></a>Rate at which data is read from a disk</p>
<p id="p7436945192311"><a name="p7436945192311"></a><a name="p7436945192311"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p14418143515397"><a name="p14418143515397"></a><a name="p14418143515397"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1041812358397"><a name="p1041812358397"></a><a name="p1041812358397"></a>Monitored object: ECS</p>
<p id="p29382296240"><a name="p29382296240"></a><a name="p29382296240"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row24181235163913"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p7418103503916"><a name="p7418103503916"></a><a name="p7418103503916"></a>rds050_disk_write_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p74181535143918"><a name="p74181535143918"></a><a name="p74181535143918"></a>Disk Write Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p14418123513910"><a name="p14418123513910"></a><a name="p14418123513910"></a>Rate at which data is written to a disk</p>
<p id="p2418133516398"><a name="p2418133516398"></a><a name="p2418133516398"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p34181335143910"><a name="p34181335143910"></a><a name="p34181335143910"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p2041853523914"><a name="p2041853523914"></a><a name="p2041853523914"></a>Monitored object: ECS</p>
<p id="p634652515245"><a name="p634652515245"></a><a name="p634652515245"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row18418435163917"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p2418123573917"><a name="p2418123573917"></a><a name="p2418123573917"></a>rds051_avg_disk_sec_per_read</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p17418123514392"><a name="p17418123514392"></a><a name="p17418123514392"></a>Average Time per Disk Read</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p154181835193911"><a name="p154181835193911"></a><a name="p154181835193911"></a>Time required for reading 1 KB disk data</p>
<p id="p7418163519392"><a name="p7418163519392"></a><a name="p7418163519392"></a>Unit: Second</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p641943511397"><a name="p641943511397"></a><a name="p641943511397"></a>&gt; 0s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1641963533913"><a name="p1641963533913"></a><a name="p1641963533913"></a>Monitored object: ECS</p>
<p id="p164493221244"><a name="p164493221244"></a><a name="p164493221244"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row24196350398"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p2419135103917"><a name="p2419135103917"></a><a name="p2419135103917"></a>rds052_avg_disk_sec_per_write</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p5419153583916"><a name="p5419153583916"></a><a name="p5419153583916"></a>Average Time per Disk Write</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p1419153503917"><a name="p1419153503917"></a><a name="p1419153503917"></a>Time required for writing 1 KB data to a disk</p>
<p id="p241973513917"><a name="p241973513917"></a><a name="p241973513917"></a>Unit: Second</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p84190359397"><a name="p84190359397"></a><a name="p84190359397"></a>&gt; 0s</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p1541983573910"><a name="p1541983573910"></a><a name="p1541983573910"></a>Monitored object: ECS</p>
<p id="p113709195241"><a name="p113709195241"></a><a name="p113709195241"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row84201435143918"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p1642013359394"><a name="p1642013359394"></a><a name="p1642013359394"></a>rds053_avg_disk_queue_length</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p18420035113911"><a name="p18420035113911"></a><a name="p18420035113911"></a>Average Disk Queue Length</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p17420123512391"><a name="p17420123512391"></a><a name="p17420123512391"></a>Number of processes waiting to be written to the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p1342013517391"><a name="p1342013517391"></a><a name="p1342013517391"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p8420173533914"><a name="p8420173533914"></a><a name="p8420173533914"></a>Monitored object: ECS</p>
<p id="p13420193517395"><a name="p13420193517395"></a><a name="p13420193517395"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
<tr id="row1042116352399"><td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.6.1.1 "><p id="p542120357394"><a name="p542120357394"></a><a name="p542120357394"></a>rds054_db_connections_in_use</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.6.1.2 "><p id="p144211735133912"><a name="p144211735133912"></a><a name="p144211735133912"></a>Database Connections in Use</p>
</td>
<td class="cellrowborder" valign="top" width="30.709999999999997%" headers="mcps1.2.6.1.3 "><p id="p44215353392"><a name="p44215353392"></a><a name="p44215353392"></a>Number of database connections in use</p>
<p id="p442133503912"><a name="p442133503912"></a><a name="p442133503912"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="11.99%" headers="mcps1.2.6.1.4 "><p id="p14421203510393"><a name="p14421203510393"></a><a name="p14421203510393"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.6.1.5 "><p id="p5421735103917"><a name="p5421735103917"></a><a name="p5421735103917"></a>Monitored object: database</p>
<p id="p1642163533913"><a name="p1642163533913"></a><a name="p1642163533913"></a>Monitored instance type: Microsoft SQL Server instance</p>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="se9f8728f21d7422a92d38ca7cb65bcc0"></a>

<a name="t955709aa786b4e3982ee24082d963191"></a>
<table><thead align="left"><tr id="rec5236eb711b4b678f5e17c5a8e3e2f0"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a2a45466ae642456c8ba6f01b5b0fd0c4"><a name="a2a45466ae642456c8ba6f01b5b0fd0c4"></a><a name="a2a45466ae642456c8ba6f01b5b0fd0c4"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="ab531e8bc7bff44a7aac9a7d6e9a9bbde"><a name="ab531e8bc7bff44a7aac9a7d6e9a9bbde"></a><a name="ab531e8bc7bff44a7aac9a7d6e9a9bbde"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="ra35ecb63bb3f496c86fcde8f86b9246e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a9dd6d9ed3abc4e7dbf310aeb13ef3e2d"><a name="a9dd6d9ed3abc4e7dbf310aeb13ef3e2d"></a><a name="a9dd6d9ed3abc4e7dbf310aeb13ef3e2d"></a>rds_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aee8f71df30d34743b1d48e6ea4544cd3"><a name="aee8f71df30d34743b1d48e6ea4544cd3"></a><a name="aee8f71df30d34743b1d48e6ea4544cd3"></a>MySQL instance ID</p>
</td>
</tr>
<tr id="row2309218511552"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p54303026115518"><a name="p54303026115518"></a><a name="p54303026115518"></a>postgresql_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p36468953115518"><a name="p36468953115518"></a><a name="p36468953115518"></a>PostgreSQL instance ID</p>
</td>
</tr>
<tr id="row811808211558"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p10757141115518"><a name="p10757141115518"></a><a name="p10757141115518"></a>rds_instance_sqlserver_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p66022067115518"><a name="p66022067115518"></a><a name="p66022067115518"></a>Microsoft SQL Server instance ID</p>
</td>
</tr>
</tbody>
</table>

