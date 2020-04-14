# Monitoring a Cluster<a name="dws_01_0022"></a>

## Function<a name="section43782126162722"></a>

This section describes how to check cluster metrics on Cloud Eye. By monitoring cluster running metrics, you can identify the time when the database cluster is abnormal and analyze potential activity problems based on the database logs, improving database performance. This section describes the metrics that can be monitored by Cloud Eye as well as their namespaces and dimensions. You can use the management console or APIs provided by Cloud Eye to query the metrics of the monitored objects and alarms generated for DWS. For details, see the user guide and API reference of .

This section is organized as follows:

-   [Namespace](#section54481685355)
-   [Monitoring Metrics of a Cluster](#section185715586432)
-   [Dimension](#section6596194111819)
-   [Viewing Monitoring Information of a Cluster](#section26007147165750)
-   [Comparing the Monitoring Metrics of Multiple Nodes](#section20548025153518)
-   [Creating Alarm Rules](#section76461040113)

## Namespace<a name="section54481685355"></a>

SYS.DWS

## Monitoring Metrics of a Cluster<a name="section185715586432"></a>

With the DWS monitoring metrics provided by Cloud Eye, you can obtain information about the cluster running status and performance. This information will provide a better understanding of the node-level information.

[Table 1](#table1114714531724)  describes DWS monitoring metrics.

**Table  1**  DWS monitoring metrics

<a name="table1114714531724"></a>
<table><thead align="left"><tr id="row01475535216"><th class="cellrowborder" valign="top" width="19.56%" id="mcps1.2.7.1.1"><p id="p6381131419376"><a name="p6381131419376"></a><a name="p6381131419376"></a><strong id="b229978125117"><a name="b229978125117"></a><a name="b229978125117"></a>Metric ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.9%" id="mcps1.2.7.1.2"><p id="p113074120310"><a name="p113074120310"></a><a name="p113074120310"></a><strong id="b3200496162920"><a name="b3200496162920"></a><a name="b3200496162920"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.46%" id="mcps1.2.7.1.3"><p id="p766414199311"><a name="p766414199311"></a><a name="p766414199311"></a><strong id="b691751211511"><a name="b691751211511"></a><a name="b691751211511"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.709999999999999%" id="mcps1.2.7.1.4"><p id="p51483538214"><a name="p51483538214"></a><a name="p51483538214"></a><strong id="b25306395184919_1"><a name="b25306395184919_1"></a><a name="b25306395184919_1"></a>Value Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.790000000000001%" id="mcps1.2.7.1.5"><p id="p1384520586435"><a name="p1384520586435"></a><a name="p1384520586435"></a><strong id="b1611641615511"><a name="b1611641615511"></a><a name="b1611641615511"></a>Measurement Object &amp; Dimension</strong></p>
</th>
<th class="cellrowborder" valign="top" width="8.58%" id="mcps1.2.7.1.6"><p id="p181431935163611"><a name="p181431935163611"></a><a name="p181431935163611"></a><strong id="b18672111711518"><a name="b18672111711518"></a><a name="b18672111711518"></a>Monitoring Period (Raw Data)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row111489531726"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p76691855553"><a name="p76691855553"></a><a name="p76691855553"></a>dws001_shared_buffer_hit_ratio</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p131483531821"><a name="p131483531821"></a><a name="p131483531821"></a>Shared Memory Hit Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p121481953628"><a name="p121481953628"></a><a name="p121481953628"></a>Percentage of data volume obtained from memory, expressed in percentage</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p814817531527"><a name="p814817531527"></a><a name="p814817531527"></a>0% to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p5349161716"><a name="p5349161716"></a><a name="p5349161716"></a>Monitored object: data warehouse cluster</p>
<p id="p248971710"><a name="p248971710"></a><a name="p248971710"></a>Dimension: datastore_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p3575101521010"><a name="p3575101521010"></a><a name="p3575101521010"></a>4 minutes</p>
</td>
</tr>
<tr id="row1114816533218"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p1366912514552"><a name="p1366912514552"></a><a name="p1366912514552"></a>dws002_in_memory_sort_ratio</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p1814815532217"><a name="p1814815532217"></a><a name="p1814815532217"></a>In-memory Sort Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p7148135314217"><a name="p7148135314217"></a><a name="p7148135314217"></a>Percentage of data volume that is sorted in memory, expressed in percentage</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p1314814531726"><a name="p1314814531726"></a><a name="p1314814531726"></a>0% to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p1741193174"><a name="p1741193174"></a><a name="p1741193174"></a>Monitored object: data warehouse cluster</p>
<p id="p7418915174"><a name="p7418915174"></a><a name="p7418915174"></a>Dimension: datastore_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p10575515171020"><a name="p10575515171020"></a><a name="p10575515171020"></a>4 minutes</p>
</td>
</tr>
<tr id="row51481953625"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p1766916585513"><a name="p1766916585513"></a><a name="p1766916585513"></a>dws003_physical_reads</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p151481453526"><a name="p151481453526"></a><a name="p151481453526"></a>File Reads</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p614813536216"><a name="p614813536216"></a><a name="p614813536216"></a>Total number of database file reads</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p21498531920"><a name="p21498531920"></a><a name="p21498531920"></a>&gt; 0</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p18469141713"><a name="p18469141713"></a><a name="p18469141713"></a>Monitored object: data warehouse cluster</p>
<p id="p2479111711"><a name="p2479111711"></a><a name="p2479111711"></a>Dimension: datastore_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p1757513158108"><a name="p1757513158108"></a><a name="p1757513158108"></a>4 minutes</p>
</td>
</tr>
<tr id="row8149353321"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p10669654555"><a name="p10669654555"></a><a name="p10669654555"></a>dws004_physical_writes</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p81499533214"><a name="p81499533214"></a><a name="p81499533214"></a>File Writes</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p514916537213"><a name="p514916537213"></a><a name="p514916537213"></a>Total number of database file writes</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p17149175312214"><a name="p17149175312214"></a><a name="p17149175312214"></a>&gt; 0</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p2469121717"><a name="p2469121717"></a><a name="p2469121717"></a>Monitored object: data warehouse cluster</p>
<p id="p164149141714"><a name="p164149141714"></a><a name="p164149141714"></a>Dimension: datastore_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p125759158107"><a name="p125759158107"></a><a name="p125759158107"></a>4 minutes</p>
</td>
</tr>
<tr id="row131496531423"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p166694513557"><a name="p166694513557"></a><a name="p166694513557"></a>dws006_physical_writes_per_second</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p6149753021"><a name="p6149753021"></a><a name="p6149753021"></a>File Reads per Second</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p114915531726"><a name="p114915531726"></a><a name="p114915531726"></a>Number of database file reads per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p11491532021"><a name="p11491532021"></a><a name="p11491532021"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p645916171"><a name="p645916171"></a><a name="p645916171"></a>Monitored object: data warehouse cluster</p>
<p id="p11410916170"><a name="p11410916170"></a><a name="p11410916170"></a>Dimension: datastore_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p0576315101019"><a name="p0576315101019"></a><a name="p0576315101019"></a>4 minutes</p>
</td>
</tr>
<tr id="row1814917531022"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p96691751559"><a name="p96691751559"></a><a name="p96691751559"></a>dws005_physical_reads_per_second</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p131491953320"><a name="p131491953320"></a><a name="p131491953320"></a>File Writes per Second</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p31491753223"><a name="p31491753223"></a><a name="p31491753223"></a>Number of database file writes per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p614910531222"><a name="p614910531222"></a><a name="p614910531222"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p1444941710"><a name="p1444941710"></a><a name="p1444941710"></a>Monitored object: data warehouse cluster</p>
<p id="p1941914171"><a name="p1941914171"></a><a name="p1941914171"></a>Dimension: datastore_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p20576171516103"><a name="p20576171516103"></a><a name="p20576171516103"></a>4 minutes</p>
</td>
</tr>
<tr id="row181502531526"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p1367012519551"><a name="p1367012519551"></a><a name="p1367012519551"></a>dws007_db_size</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p8150195318218"><a name="p8150195318218"></a><a name="p8150195318218"></a>Data Volume</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p4150165311219"><a name="p4150165311219"></a><a name="p4150165311219"></a>Total data volume of the database</p>
<p id="p114082057131917"><a name="p114082057131917"></a><a name="p114082057131917"></a>Unit: MB</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p151508531723"><a name="p151508531723"></a><a name="p151508531723"></a>0 to 36,000 MB</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p44491173"><a name="p44491173"></a><a name="p44491173"></a>Monitored object: data warehouse cluster</p>
<p id="p18449181718"><a name="p18449181718"></a><a name="p18449181718"></a>Dimension: datastore_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p1757661518107"><a name="p1757661518107"></a><a name="p1757661518107"></a>4 minutes</p>
</td>
</tr>
<tr id="row2150753720"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p36705545516"><a name="p36705545516"></a><a name="p36705545516"></a>dws008_active_sql_count</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p91501253324"><a name="p91501253324"></a><a name="p91501253324"></a>Active SQL Count</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p1815017538214"><a name="p1815017538214"></a><a name="p1815017538214"></a>Number of active SQLs in the database</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p515012533210"><a name="p515012533210"></a><a name="p515012533210"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p1413914171"><a name="p1413914171"></a><a name="p1413914171"></a>Monitored object: data warehouse cluster</p>
<p id="p1941692174"><a name="p1941692174"></a><a name="p1941692174"></a>Dimension: datastore_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p1257613153102"><a name="p1257613153102"></a><a name="p1257613153102"></a>4 minutes</p>
</td>
</tr>
<tr id="row151508531125"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p12670175155514"><a name="p12670175155514"></a><a name="p12670175155514"></a>dws009_session_count</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p31501753621"><a name="p31501753621"></a><a name="p31501753621"></a>Session Count</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p61503539216"><a name="p61503539216"></a><a name="p61503539216"></a>Number of sessions that access the database</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p815055311212"><a name="p815055311212"></a><a name="p815055311212"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p16511911174"><a name="p16511911174"></a><a name="p16511911174"></a>Monitored object: data warehouse cluster</p>
<p id="p155129101716"><a name="p155129101716"></a><a name="p155129101716"></a>Dimension: datastore_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p157621512108"><a name="p157621512108"></a><a name="p157621512108"></a>4 minutes</p>
</td>
</tr>
<tr id="row131519538215"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p26701457553"><a name="p26701457553"></a><a name="p26701457553"></a>dws010_cpu_usage</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p171519532215"><a name="p171519532215"></a><a name="p171519532215"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p61511353227"><a name="p61511353227"></a><a name="p61511353227"></a>CPU usages of each node in the cluster, expressed in percentage</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p18151753021"><a name="p18151753021"></a><a name="p18151753021"></a>0% to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p256910177"><a name="p256910177"></a><a name="p256910177"></a>Monitored object: data warehouse</p>
<p id="p195139181710"><a name="p195139181710"></a><a name="p195139181710"></a>Dimension: dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p157661521017"><a name="p157661521017"></a><a name="p157661521017"></a>1 minute</p>
</td>
</tr>
<tr id="row101511653827"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p146709595513"><a name="p146709595513"></a><a name="p146709595513"></a>dws011_mem_usage</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p141511753922"><a name="p141511753922"></a><a name="p141511753922"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p8152053424"><a name="p8152053424"></a><a name="p8152053424"></a>Memory usages of each node in the cluster, expressed in percentage</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p131527535217"><a name="p131527535217"></a><a name="p131527535217"></a>0% to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p55798178"><a name="p55798178"></a><a name="p55798178"></a>Monitored object: data warehouse</p>
<p id="p1855991712"><a name="p1855991712"></a><a name="p1855991712"></a>Dimension: dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p125761154107"><a name="p125761154107"></a><a name="p125761154107"></a>1 minute</p>
</td>
</tr>
<tr id="row215212532022"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p11670145145519"><a name="p11670145145519"></a><a name="p11670145145519"></a>dws012_iops</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p13152175313215"><a name="p13152175313215"></a><a name="p13152175313215"></a>IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p111522053921"><a name="p111522053921"></a><a name="p111522053921"></a>Number of I/O requests processed by each node in the cluster per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p51521053924"><a name="p51521053924"></a><a name="p51521053924"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p059981717"><a name="p059981717"></a><a name="p059981717"></a>Monitored object: data warehouse</p>
<p id="p1756981714"><a name="p1756981714"></a><a name="p1756981714"></a>Dimension: dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p9576141511015"><a name="p9576141511015"></a><a name="p9576141511015"></a>1 minute</p>
</td>
</tr>
<tr id="row131521053028"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p967015575519"><a name="p967015575519"></a><a name="p967015575519"></a>dws013_bytes_in</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p115214538211"><a name="p115214538211"></a><a name="p115214538211"></a>Network Input Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p131531531329"><a name="p131531531329"></a><a name="p131531531329"></a>Data input to each node in the cluster per second over the network</p>
<p id="p26183389267"><a name="p26183389267"></a><a name="p26183389267"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p815312531423"><a name="p815312531423"></a><a name="p815312531423"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p105149171711"><a name="p105149171711"></a><a name="p105149171711"></a>Monitored object: data warehouse</p>
<p id="p14589191716"><a name="p14589191716"></a><a name="p14589191716"></a>Dimension: dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p17576115131019"><a name="p17576115131019"></a><a name="p17576115131019"></a>1 minute</p>
</td>
</tr>
<tr id="row51530538211"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p867110515555"><a name="p867110515555"></a><a name="p867110515555"></a>dws014_bytes_out</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p181535536210"><a name="p181535536210"></a><a name="p181535536210"></a>Network Output Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p20153135314217"><a name="p20153135314217"></a><a name="p20153135314217"></a>Data sent to the network per second from each node in the cluster</p>
<p id="p9205949112614"><a name="p9205949112614"></a><a name="p9205949112614"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p1415318531522"><a name="p1415318531522"></a><a name="p1415318531522"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p4519121711"><a name="p4519121711"></a><a name="p4519121711"></a>Monitored object: data warehouse</p>
<p id="p753931715"><a name="p753931715"></a><a name="p753931715"></a>Dimension: dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p2576111513108"><a name="p2576111513108"></a><a name="p2576111513108"></a>1 minute</p>
</td>
</tr>
<tr id="row715325310220"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p2067111517552"><a name="p2067111517552"></a><a name="p2067111517552"></a>dws015_disk_usage</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p1115355316216"><a name="p1115355316216"></a><a name="p1115355316216"></a>Disk Usage</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p7153195316217"><a name="p7153195316217"></a><a name="p7153195316217"></a>Disk usages of each node in the cluster, expressed in percentage</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p12153453724"><a name="p12153453724"></a><a name="p12153453724"></a>0% to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p1451491175"><a name="p1451491175"></a><a name="p1451491175"></a>Monitored object: data warehouse</p>
<p id="p10510931711"><a name="p10510931711"></a><a name="p10510931711"></a>Dimension: dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p195777157107"><a name="p195777157107"></a><a name="p195777157107"></a>1 minute</p>
</td>
</tr>
<tr id="row31530531621"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p867116510552"><a name="p867116510552"></a><a name="p867116510552"></a>dws016_disk_total_size</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p1153125315211"><a name="p1153125315211"></a><a name="p1153125315211"></a>Total Disk Size</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p1515416538210"><a name="p1515416538210"></a><a name="p1515416538210"></a>Total disk space of each node in the cluster</p>
<p id="p1357833219201"><a name="p1357833219201"></a><a name="p1357833219201"></a>Unit: GB</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p1315475312220"><a name="p1315475312220"></a><a name="p1315475312220"></a>100 to 2,000 GB</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p155490174"><a name="p155490174"></a><a name="p155490174"></a>Monitored object: data warehouse</p>
<p id="p7515951712"><a name="p7515951712"></a><a name="p7515951712"></a>Dimension: dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p3577181517107"><a name="p3577181517107"></a><a name="p3577181517107"></a>1 minute</p>
</td>
</tr>
<tr id="row71541531227"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p467113595515"><a name="p467113595515"></a><a name="p467113595515"></a>dws017_disk_used_size</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p1154115316212"><a name="p1154115316212"></a><a name="p1154115316212"></a>Used Disk Space</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p131541153723"><a name="p131541153723"></a><a name="p131541153723"></a>Used disk space of each node in the cluster</p>
<p id="p4281553202014"><a name="p4281553202014"></a><a name="p4281553202014"></a>Unit: GB</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p71546536212"><a name="p71546536212"></a><a name="p71546536212"></a>0 to 3,600 GB</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p766911174"><a name="p766911174"></a><a name="p766911174"></a>Monitored object: data warehouse</p>
<p id="p1261595172"><a name="p1261595172"></a><a name="p1261595172"></a>Dimension: dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p13577161581011"><a name="p13577161581011"></a><a name="p13577161581011"></a>1 minute</p>
</td>
</tr>
<tr id="row11541531526"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p767112515520"><a name="p767112515520"></a><a name="p767112515520"></a>dws018_disk_read_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p415410531827"><a name="p415410531827"></a><a name="p415410531827"></a>Disk Read Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p115445311213"><a name="p115445311213"></a><a name="p115445311213"></a>Data volume read from each disk in the cluster per second</p>
<p id="p1161515152114"><a name="p1161515152114"></a><a name="p1161515152114"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p1215425317217"><a name="p1215425317217"></a><a name="p1215425317217"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p569961711"><a name="p569961711"></a><a name="p569961711"></a>Monitored object: data warehouse</p>
<p id="p186159111720"><a name="p186159111720"></a><a name="p186159111720"></a>Dimension: dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p16577115101017"><a name="p16577115101017"></a><a name="p16577115101017"></a>1 minute</p>
</td>
</tr>
<tr id="row1715418531426"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p13671185145512"><a name="p13671185145512"></a><a name="p13671185145512"></a>dws019_disk_write_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p11155155318219"><a name="p11155155318219"></a><a name="p11155155318219"></a>Disk Write Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p1015545320210"><a name="p1015545320210"></a><a name="p1015545320210"></a>Data volume written to each disk in the cluster per second</p>
<p id="p2612173432111"><a name="p2612173432111"></a><a name="p2612173432111"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p715512535219"><a name="p715512535219"></a><a name="p715512535219"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p86139101718"><a name="p86139101718"></a><a name="p86139101718"></a>Monitored object: data warehouse</p>
<p id="p0669171717"><a name="p0669171717"></a><a name="p0669171717"></a>Dimension: dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p1957751501020"><a name="p1957751501020"></a><a name="p1957751501020"></a>1 minute</p>
</td>
</tr>
<tr id="row91551539210"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p1567215525512"><a name="p1567215525512"></a><a name="p1567215525512"></a>dws020_avg_disk_sec_per_read</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p61556532220"><a name="p61556532220"></a><a name="p61556532220"></a>Average Time per Disk Read</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p91551531925"><a name="p91551531925"></a><a name="p91551531925"></a>Average time used each time when a disk reads data</p>
<p id="p14291337182116"><a name="p14291337182116"></a><a name="p14291337182116"></a>Unit: second</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p111559535217"><a name="p111559535217"></a><a name="p111559535217"></a>&gt; 0s</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p1610910177"><a name="p1610910177"></a><a name="p1610910177"></a>Monitored object: data warehouse</p>
<p id="p368911178"><a name="p368911178"></a><a name="p368911178"></a>Dimension: dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p157713158103"><a name="p157713158103"></a><a name="p157713158103"></a>1 minute</p>
</td>
</tr>
<tr id="row161552053528"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p186727555519"><a name="p186727555519"></a><a name="p186727555519"></a>dws021_avg_disk_sec_per_write</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p101551353628"><a name="p101551353628"></a><a name="p101551353628"></a>Average Time per Disk Write</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p315518531428"><a name="p315518531428"></a><a name="p315518531428"></a>Average time used each time when data is written to a disk</p>
<p id="p564415496218"><a name="p564415496218"></a><a name="p564415496218"></a>Unit: second</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p2155153123"><a name="p2155153123"></a><a name="p2155153123"></a>&gt; 0s</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p12619141716"><a name="p12619141716"></a><a name="p12619141716"></a>Monitored object: data warehouse</p>
<p id="p367981716"><a name="p367981716"></a><a name="p367981716"></a>Dimension: dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p1757721519102"><a name="p1757721519102"></a><a name="p1757721519102"></a>1 minute</p>
</td>
</tr>
<tr id="row3155353624"><td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.2.7.1.1 "><p id="p166724517551"><a name="p166724517551"></a><a name="p166724517551"></a>dws022_avg_disk_queue_length</p>
</td>
<td class="cellrowborder" valign="top" width="15.9%" headers="mcps1.2.7.1.2 "><p id="p31564530215"><a name="p31564530215"></a><a name="p31564530215"></a>Average Disk Queue Length</p>
</td>
<td class="cellrowborder" valign="top" width="28.46%" headers="mcps1.2.7.1.3 "><p id="p1615617535210"><a name="p1615617535210"></a><a name="p1615617535210"></a>Average I/O queue length of a disk</p>
</td>
<td class="cellrowborder" valign="top" width="11.709999999999999%" headers="mcps1.2.7.1.4 "><p id="p181561153328"><a name="p181561153328"></a><a name="p181561153328"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15.790000000000001%" headers="mcps1.2.7.1.5 "><p id="p76092171"><a name="p76092171"></a><a name="p76092171"></a>Monitored object: data warehouse</p>
<p id="p14669121715"><a name="p14669121715"></a><a name="p14669121715"></a>Dimension: dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.58%" headers="mcps1.2.7.1.6 "><p id="p19578101514104"><a name="p19578101514104"></a><a name="p19578101514104"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="section6596194111819"></a>

<a name="table6596541121814"></a>
<table><thead align="left"><tr id="row15596641121813"><th class="cellrowborder" valign="top" width="45.22%" id="mcps1.1.3.1.1"><p id="p19596154131811"><a name="p19596154131811"></a><a name="p19596154131811"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="54.779999999999994%" id="mcps1.1.3.1.2"><p id="p11596174117181"><a name="p11596174117181"></a><a name="p11596174117181"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row1359614113186"><td class="cellrowborder" valign="top" width="45.22%" headers="mcps1.1.3.1.1 "><p id="p1559664191815"><a name="p1559664191815"></a><a name="p1559664191815"></a>datastore_id</p>
</td>
<td class="cellrowborder" valign="top" width="54.779999999999994%" headers="mcps1.1.3.1.2 "><p id="p1959618414187"><a name="p1959618414187"></a><a name="p1959618414187"></a>Data warehouse cluster</p>
</td>
</tr>
<tr id="row165971241201816"><td class="cellrowborder" valign="top" width="45.22%" headers="mcps1.1.3.1.1 "><p id="p17597134112186"><a name="p17597134112186"></a><a name="p17597134112186"></a>dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="54.779999999999994%" headers="mcps1.1.3.1.2 "><p id="p659712418183"><a name="p659712418183"></a><a name="p659712418183"></a>Data warehouse node</p>
</td>
</tr>
</tbody>
</table>

## Viewing Monitoring Information of a Cluster<a name="section26007147165750"></a>

1.  Log in to the DWS management console.
2.  Click  **Cluster Management**.
3.  In the cluster list, click  **View Metric**  in the  **Operation**  column where a specific cluster resides. The Cloud Eye management console is displayed.

    On Cloud Eye, you can view monitoring metrics of data warehouse clusters and monitoring information about each node in the cluster. Additionally, you can specify a specific monitoring metric and the time range to view the performance curve.

    Cloud Eye also supports the ability to compare the monitoring metrics of multiple nodes. For details, see  [Comparing the Monitoring Metrics of Multiple Nodes](#section20548025153518).


## Comparing the Monitoring Metrics of Multiple Nodes<a name="section20548025153518"></a>

1.  In the navigation tree on the left of the Cloud Eye management console, choose  **Dashboard**  \>  **Monitoring Panels**.
2.  On the  **Monitoring Panels**  page, click  **Create Panel**. In the displayed dialog box, enter the  **Name**  and click  **OK**.
3.  On the  **Monitoring Panels**  page, click  **Add Graph**  in the upper right corner.
4.  In the  **Add Graph**  window, configure the title and monitoring metrics.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can add multiple monitoring metrics by clicking  **Add Metric**.  

    The following describes how to set parameters if you want to compare CPU usage of two nodes.

    **Figure  1**  Add Graph<a name="fig5653161610242"></a>  
    ![](figures/add-graph.png "add-graph")

    **Table  2**  Configuration example

    <a name="table531634516736"></a>
    <table><thead align="left"><tr id="row4060451616736"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p568376716736"><a name="p568376716736"></a><a name="p568376716736"></a><strong id="b84235270692541"><a name="b84235270692541"></a><a name="b84235270692541"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p5773201616736"><a name="p5773201616736"></a><a name="p5773201616736"></a><strong id="b60793810112357_1"><a name="b60793810112357_1"></a><a name="b60793810112357_1"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4982610116736"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p2261359816417"><a name="p2261359816417"></a><a name="p2261359816417"></a>Resource Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p2177264216736"><a name="p2177264216736"></a><a name="p2177264216736"></a>DWS</p>
    </td>
    </tr>
    <tr id="row6173605316736"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3456440016736"><a name="p3456440016736"></a><a name="p3456440016736"></a>Dimension</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p52128907161035"><a name="p52128907161035"></a><a name="p52128907161035"></a>Data Warehouse Node</p>
    </td>
    </tr>
    <tr id="row3162373816736"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1138595516736"><a name="p1138595516736"></a><a name="p1138595516736"></a>Monitored Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p4984712416736"><a name="p4984712416736"></a><a name="p4984712416736"></a>dws-64a3-dws-dn-1-1</p>
    <p id="p50143521161249"><a name="p50143521161249"></a><a name="p50143521161249"></a>dws-64a3-dws-cn-cn-1-1</p>
    </td>
    </tr>
    <tr id="row4150216216921"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p623199316921"><a name="p623199316921"></a><a name="p623199316921"></a>Metric</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p3502938716921"><a name="p3502938716921"></a><a name="p3502938716921"></a>CPU Usage</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **OK**.

    After the monitoring metrics are added successfully, you can view the corresponding monitoring graph on the  **Monitoring Panels**  page. Move the cursor to the graph and click  ![](figures/icon_dws_monitor_detail.png)  in the upper right corner to zoom in the graph and view detailed metric comparison data.


## Creating Alarm Rules<a name="section76461040113"></a>

Setting DWS alarm rules allows you to customize the monitored objects and notification policies and determine the running status of your DWS at any time.

A DWS alarm rule includes the alarm rule name, monitored object, metric, threshold, monitoring interval, and whether to send a notification. This section describes how to set DWS alarm rules.

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  In the navigation tree on the left, click  **Cluster Management**.
3.  Locate the row containing the target cluster, click  **View Metric**  in the  **Operation**  column to enter the Cloud Eye management console and view the DWS monitoring information.

    The status of the target cluster must be  **Available**. Otherwise, you cannot create alarm rules.

4.  In the left navigation pane of the Cloud Eye management console, choose  **Alarm Management**  \>  **Alarm Rules**.
5.  On the  **Alarm Rules**  page, click  **Create Alarm Rule**  in the upper right corner.
6.  On the  **Create Alarm Rule**  page, set parameters as prompted.
    1.  Select the object to be monitored, set the parameters, and click  **Next**.

        **Figure  2**  Selecting the object to be monitored<a name="fig12111616112412"></a>  
        ![](figures/selecting-the-object-to-be-monitored.png "selecting-the-object-to-be-monitored")

        **Table  3**  Selecting the object to be monitored

        <a name="table161785409115"></a>
        <table><thead align="left"><tr id="row191782040141114"><th class="cellrowborder" valign="top" width="16.36163616361636%" id="mcps1.2.4.1.1"><p id="p7178114021113"><a name="p7178114021113"></a><a name="p7178114021113"></a><strong id="b1993131717811"><a name="b1993131717811"></a><a name="b1993131717811"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="50.305030503050304%" id="mcps1.2.4.1.2"><p id="p2017816401114"><a name="p2017816401114"></a><a name="p2017816401114"></a><strong id="b972392910133"><a name="b972392910133"></a><a name="b972392910133"></a>Description</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p16178184011114"><a name="p16178184011114"></a><a name="p16178184011114"></a><strong id="b3176675391910"><a name="b3176675391910"></a><a name="b3176675391910"></a>Example Value</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row10178144021113"><td class="cellrowborder" valign="top" width="16.36163616361636%" headers="mcps1.2.4.1.1 "><p id="p29586526115"><a name="p29586526115"></a><a name="p29586526115"></a>Resource Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="50.305030503050304%" headers="mcps1.2.4.1.2 "><p id="p49637525114"><a name="p49637525114"></a><a name="p49637525114"></a>Name of the cloud service resource for which the alarm rule is configured</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2967155231119"><a name="p2967155231119"></a><a name="p2967155231119"></a>Data Warehouse Service</p>
        </td>
        </tr>
        <tr id="row17179184031110"><td class="cellrowborder" valign="top" width="16.36163616361636%" headers="mcps1.2.4.1.1 "><p id="p8977155221111"><a name="p8977155221111"></a><a name="p8977155221111"></a>Dimension</p>
        </td>
        <td class="cellrowborder" valign="top" width="50.305030503050304%" headers="mcps1.2.4.1.2 "><p id="p17989552131113"><a name="p17989552131113"></a><a name="p17989552131113"></a>Metric dimension of the alarm rule. You can select <strong id="b484222919369"><a name="b484222919369"></a><a name="b484222919369"></a>Data Warehouse Nodes</strong> or <strong id="b18842122914367"><a name="b18842122914367"></a><a name="b18842122914367"></a>Data Warehouses</strong>.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p179951852151112"><a name="p179951852151112"></a><a name="p179951852151112"></a>Data Warehouses</p>
        </td>
        </tr>
        <tr id="row131791440101112"><td class="cellrowborder" valign="top" width="16.36163616361636%" headers="mcps1.2.4.1.1 "><p id="p823205351117"><a name="p823205351117"></a><a name="p823205351117"></a>Monitored Object</p>
        </td>
        <td class="cellrowborder" valign="top" width="50.305030503050304%" headers="mcps1.2.4.1.2 "><p id="p82835351118"><a name="p82835351118"></a><a name="p82835351118"></a>Specific resources monitored by the alarm rule. You can specify one or more resources for monitoring. Select the ID of the cluster instance or node you have created.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p431205381114"><a name="p431205381114"></a><a name="p431205381114"></a>-</p>
        </td>
        </tr>
        </tbody>
        </table>

    2.  Select the monitoring metric. You can select either of the following methods and set parameters as prompted.
        -   **Create Manually**

            If no alarm template is available, set  **Method**  to  **Create manually**  and configure related parameters to create an alarm rule.

            **Figure  3**  Selecting the metric<a name="fig7965229132511"></a>  
            ![](figures/selecting-the-metric.png "selecting-the-metric")

              

            **Table  4**  Related parameters

            <a name="table15471215125717"></a>
            <table><thead align="left"><tr id="row1047141585716"><th class="cellrowborder" valign="top" width="14.881488148814881%" id="mcps1.2.4.1.1"><p id="p84721514574"><a name="p84721514574"></a><a name="p84721514574"></a><strong id="b421211011503"><a name="b421211011503"></a><a name="b421211011503"></a>Parameter</strong></p>
            </th>
            <th class="cellrowborder" valign="top" width="66.07660766076607%" id="mcps1.2.4.1.2"><p id="p1347191518576"><a name="p1347191518576"></a><a name="p1347191518576"></a><strong id="b132755120504"><a name="b132755120504"></a><a name="b132755120504"></a>Description</strong></p>
            </th>
            <th class="cellrowborder" valign="top" width="19.041904190419046%" id="mcps1.2.4.1.3"><p id="p5471215175714"><a name="p5471215175714"></a><a name="p5471215175714"></a><strong id="b9571823508"><a name="b9571823508"></a><a name="b9571823508"></a>Example Value</strong></p>
            </th>
            </tr>
            </thead>
            <tbody><tr id="row13471315145711"><td class="cellrowborder" valign="top" width="14.881488148814881%" headers="mcps1.2.4.1.1 "><p id="p16862955155719"><a name="p16862955155719"></a><a name="p16862955155719"></a>Method</p>
            </td>
            <td class="cellrowborder" valign="top" width="66.07660766076607%" headers="mcps1.2.4.1.2 "><p id="p2866135525716"><a name="p2866135525716"></a><a name="p2866135525716"></a>Select <span class="parmname" id="parmname16962173145815"><a name="parmname16962173145815"></a><a name="parmname16962173145815"></a><b>Create manually</b></span>.</p>
            </td>
            <td class="cellrowborder" valign="top" width="19.041904190419046%" headers="mcps1.2.4.1.3 "><p id="p6875135510574"><a name="p6875135510574"></a><a name="p6875135510574"></a>Create manually</p>
            </td>
            </tr>
            <tr id="row94761525715"><td class="cellrowborder" valign="top" width="14.881488148814881%" headers="mcps1.2.4.1.1 "><p id="p7883955125710"><a name="p7883955125710"></a><a name="p7883955125710"></a>Metric</p>
            </td>
            <td class="cellrowborder" valign="top" width="66.07660766076607%" headers="mcps1.2.4.1.2 "><p id="p16887955155710"><a name="p16887955155710"></a><a name="p16887955155710"></a>Select a metric supported by DWS. For details, see section <a href="#section185715586432">Monitoring Metrics of a Cluster</a>.</p>
            <p id="p589165535715"><a name="p589165535715"></a><a name="p589165535715"></a>For example:</p>
            <a name="ul18921055175712"></a><a name="ul18921055175712"></a><ul id="ul18921055175712"><li>CPU Usage<p id="p2090011552572"><a name="p2090011552572"></a><a name="p2090011552572"></a>CPU usage of the monitored object, expressed in percentage</p>
            </li></ul>
            <a name="ul18902165575710"></a><a name="ul18902165575710"></a><ul id="ul18902165575710"><li>Data Volume<p id="p2217115507"><a name="p2217115507"></a><a name="p2217115507"></a>Total data volume of the database, expressed in MB</p>
            </li></ul>
            </td>
            <td class="cellrowborder" valign="top" width="19.041904190419046%" headers="mcps1.2.4.1.3 "><p id="p37831319144519"><a name="p37831319144519"></a><a name="p37831319144519"></a>Data Volumn</p>
            </td>
            </tr>
            <tr id="row114771595719"><td class="cellrowborder" valign="top" width="14.881488148814881%" headers="mcps1.2.4.1.1 "><p id="p7920555105711"><a name="p7920555105711"></a><a name="p7920555105711"></a>Alarm Policy</p>
            </td>
            <td class="cellrowborder" valign="top" width="66.07660766076607%" headers="mcps1.2.4.1.2 "><p id="p19924105525718"><a name="p19924105525718"></a><a name="p19924105525718"></a>Policy that triggers an alarm</p>
            <p id="p49261055165717"><a name="p49261055165717"></a><a name="p49261055165717"></a>For example, trigger an alarm if the metric raw data equals to or is greater than 80% for 3 consecutive periods of 5 minutes.</p>
            </td>
            <td class="cellrowborder" valign="top" width="19.041904190419046%" headers="mcps1.2.4.1.3 "><p id="p17958255125710"><a name="p17958255125710"></a><a name="p17958255125710"></a>-</p>
            </td>
            </tr>
            <tr id="row14721520572"><td class="cellrowborder" valign="top" width="14.881488148814881%" headers="mcps1.2.4.1.1 "><p id="p149631255135719"><a name="p149631255135719"></a><a name="p149631255135719"></a>Alarm Severity</p>
            </td>
            <td class="cellrowborder" valign="top" width="66.07660766076607%" headers="mcps1.2.4.1.2 "><p id="p12968165515570"><a name="p12968165515570"></a><a name="p12968165515570"></a>Severity of an alarm. Valid values are <strong id="b1178119286141"><a name="b1178119286141"></a><a name="b1178119286141"></a>Critical</strong>, <strong id="b1678162816146"><a name="b1678162816146"></a><a name="b1678162816146"></a>Major</strong>, <strong id="b7781828101419"><a name="b7781828101419"></a><a name="b7781828101419"></a>Minor</strong>, and <strong id="b9781628131415"><a name="b9781628131415"></a><a name="b9781628131415"></a>Informational</strong>.</p>
            </td>
            <td class="cellrowborder" valign="top" width="19.041904190419046%" headers="mcps1.2.4.1.3 "><p id="p9972205513578"><a name="p9972205513578"></a><a name="p9972205513578"></a>Major</p>
            </td>
            </tr>
            <tr id="row194813156573"><td class="cellrowborder" valign="top" width="14.881488148814881%" headers="mcps1.2.4.1.1 "><p id="p11980205565712"><a name="p11980205565712"></a><a name="p11980205565712"></a>Alarm Notification</p>
            </td>
            <td class="cellrowborder" valign="top" width="66.07660766076607%" headers="mcps1.2.4.1.2 "><p id="p18984125595714"><a name="p18984125595714"></a><a name="p18984125595714"></a>Whether to notify users when alarms are triggered. Notifications can be sent as emails or text messages, or HTTP/HTTPS requests sent to the servers.</p>
            <p id="p1298711556579"><a name="p1298711556579"></a><a name="p1298711556579"></a>You can enable (recommended) or disable <strong id="b139733275171"><a name="b139733275171"></a><a name="b139733275171"></a>Alarm Notification</strong>.</p>
            </td>
            <td class="cellrowborder" valign="top" width="19.041904190419046%" headers="mcps1.2.4.1.3 "><p id="p5991185515577"><a name="p5991185515577"></a><a name="p5991185515577"></a>Enable</p>
            </td>
            </tr>
            <tr id="row6486158574"><td class="cellrowborder" valign="top" width="14.881488148814881%" headers="mcps1.2.4.1.1 "><p id="p412195635711"><a name="p412195635711"></a><a name="p412195635711"></a>Topic</p>
            </td>
            <td class="cellrowborder" valign="top" width="66.07660766076607%" headers="mcps1.2.4.1.2 "><p id="p1616135612572"><a name="p1616135612572"></a><a name="p1616135612572"></a>Name of the topic to which the alarm notification is sent</p>
            <p id="p7191569572"><a name="p7191569572"></a><a name="p7191569572"></a>If you enable <strong id="b10718265216"><a name="b10718265216"></a><a name="b10718265216"></a>Alarm Notification</strong>, you need to select a topic. If no desired topics are available, create one first, whereupon the SMN service is invoked. For details about how to create a topic, see the <em id="i152117526217"><a name="i152117526217"></a><a name="i152117526217"></a>Simple Message Notification User Guide</em>.</p>
            </td>
            <td class="cellrowborder" valign="top" width="19.041904190419046%" headers="mcps1.2.4.1.3 "><p id="p15299568576"><a name="p15299568576"></a><a name="p15299568576"></a>-</p>
            </td>
            </tr>
            <tr id="row19471222155719"><td class="cellrowborder" valign="top" width="14.881488148814881%" headers="mcps1.2.4.1.1 "><p id="p104112562578"><a name="p104112562578"></a><a name="p104112562578"></a>Trigger Condition</p>
            </td>
            <td class="cellrowborder" valign="top" width="66.07660766076607%" headers="mcps1.2.4.1.2 "><p id="p14461756145711"><a name="p14461756145711"></a><a name="p14461756145711"></a>Condition for triggering the alarm. You can select <strong id="b76667522313"><a name="b76667522313"></a><a name="b76667522313"></a>Generated alarm</strong>, <strong id="b042810132319"><a name="b042810132319"></a><a name="b042810132319"></a>Cleared alarm</strong>, or both.</p>
            </td>
            <td class="cellrowborder" valign="top" width="19.041904190419046%" headers="mcps1.2.4.1.3 "><p id="p45018563576"><a name="p45018563576"></a><a name="p45018563576"></a>-</p>
            </td>
            </tr>
            </tbody>
            </table>

        -   **Use template**

            If you have available alarm rule templates, Set  **Method**  to  **Use Template**, so that you can use a template to quickly create alarm rules.

            **Figure  4**  Using an alarm rule template<a name="fig17135622192320"></a>  
            ![](figures/using-an-alarm-rule-template.png "using-an-alarm-rule-template")

            **Table  5**  Related parameters

            <a name="table62791540103"></a>
            <table><thead align="left"><tr id="row9292740707"><th class="cellrowborder" valign="top" width="14.879999999999999%" id="mcps1.2.4.1.1"><p id="p122978401803"><a name="p122978401803"></a><a name="p122978401803"></a><strong id="b550713293313"><a name="b550713293313"></a><a name="b550713293313"></a>Parameter</strong></p>
            </th>
            <th class="cellrowborder" valign="top" width="66.08000000000001%" id="mcps1.2.4.1.2"><p id="p029912405013"><a name="p029912405013"></a><a name="p029912405013"></a><strong id="b19413173153319"><a name="b19413173153319"></a><a name="b19413173153319"></a>Description</strong></p>
            </th>
            <th class="cellrowborder" valign="top" width="19.040000000000003%" id="mcps1.2.4.1.3"><p id="p1303104017011"><a name="p1303104017011"></a><a name="p1303104017011"></a><strong id="b14398115133314"><a name="b14398115133314"></a><a name="b14398115133314"></a>Example Value</strong></p>
            </th>
            </tr>
            </thead>
            <tbody><tr id="row2030784017018"><td class="cellrowborder" valign="top" width="14.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p1131194017018"><a name="p1131194017018"></a><a name="p1131194017018"></a>Method</p>
            </td>
            <td class="cellrowborder" valign="top" width="66.08000000000001%" headers="mcps1.2.4.1.2 "><p id="p031417403010"><a name="p031417403010"></a><a name="p031417403010"></a>Select <strong id="b112431715183317"><a name="b112431715183317"></a><a name="b112431715183317"></a>Use template</strong>.</p>
            </td>
            <td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.4.1.3 "><p id="p1320144014017"><a name="p1320144014017"></a><a name="p1320144014017"></a>Use template</p>
            </td>
            </tr>
            <tr id="row33219409015"><td class="cellrowborder" valign="top" width="14.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p18672471116"><a name="p18672471116"></a><a name="p18672471116"></a>Template</p>
            </td>
            <td class="cellrowborder" valign="top" width="66.08000000000001%" headers="mcps1.2.4.1.2 "><p id="p56704710116"><a name="p56704710116"></a><a name="p56704710116"></a>Select the template to be imported.</p>
            </td>
            <td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.4.1.3 "><p id="p46631755207"><a name="p46631755207"></a><a name="p46631755207"></a>-</p>
            </td>
            </tr>
            <tr id="row84041340302"><td class="cellrowborder" valign="top" width="14.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p144111240801"><a name="p144111240801"></a><a name="p144111240801"></a>Alarm Notification</p>
            </td>
            <td class="cellrowborder" valign="top" width="66.08000000000001%" headers="mcps1.2.4.1.2 "><p id="p12414124013016"><a name="p12414124013016"></a><a name="p12414124013016"></a>Whether to notify users when alarms are triggered. Notifications can be sent as emails or text messages, or HTTP/HTTPS requests sent to the servers.</p>
            <p id="p64161240805"><a name="p64161240805"></a><a name="p64161240805"></a>You can enable (recommended) or disable <strong id="b1338411492332"><a name="b1338411492332"></a><a name="b1338411492332"></a>Alarm Notification</strong>.</p>
            </td>
            <td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.4.1.3 "><p id="p124194401903"><a name="p124194401903"></a><a name="p124194401903"></a>Enable</p>
            </td>
            </tr>
            <tr id="row144335407019"><td class="cellrowborder" valign="top" width="14.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p1943694017015"><a name="p1943694017015"></a><a name="p1943694017015"></a>Topic</p>
            </td>
            <td class="cellrowborder" valign="top" width="66.08000000000001%" headers="mcps1.2.4.1.2 "><p id="p9440154017013"><a name="p9440154017013"></a><a name="p9440154017013"></a>Name of the topic to which the alarm notification is sent</p>
            <p id="p184423401703"><a name="p184423401703"></a><a name="p184423401703"></a>If you enable <strong id="b15617186133413"><a name="b15617186133413"></a><a name="b15617186133413"></a>Alarm Notification</strong>, you need to select a topic. If no desired topics are available, create one first, whereupon the SMN service is invoked. For details about how to create a topic, see the <em id="i17617166103414"><a name="i17617166103414"></a><a name="i17617166103414"></a>Simple Message Notification User Guide</em>.</p>
            </td>
            <td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.4.1.3 "><p id="p14445134014012"><a name="p14445134014012"></a><a name="p14445134014012"></a>-</p>
            </td>
            </tr>
            <tr id="row19446740107"><td class="cellrowborder" valign="top" width="14.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p114501440903"><a name="p114501440903"></a><a name="p114501440903"></a>Trigger Condition</p>
            </td>
            <td class="cellrowborder" valign="top" width="66.08000000000001%" headers="mcps1.2.4.1.2 "><p id="p7452104010013"><a name="p7452104010013"></a><a name="p7452104010013"></a>Condition for triggering the alarm. You can select <strong id="b435251313411"><a name="b435251313411"></a><a name="b435251313411"></a>Generated alarm</strong>, <strong id="b153524132343"><a name="b153524132343"></a><a name="b153524132343"></a>Cleared alarm</strong>, or both.</p>
            </td>
            <td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.4.1.3 "><p id="p19455104018020"><a name="p19455104018020"></a><a name="p19455104018020"></a>-</p>
            </td>
            </tr>
            </tbody>
            </table>

    3.  On the  **Specify Rule Name**  page shown in  [Table 6](#table178061044145), add the alarm rule details. After the configuration is complete, click  **Finish**. The alarm rule is added.

        **Table  6**  Rule details

        <a name="table178061044145"></a>
        <table><thead align="left"><tr id="row158061444940"><th class="cellrowborder" valign="top" width="14.941494149414941%" id="mcps1.2.4.1.1"><p id="p58061441549"><a name="p58061441549"></a><a name="p58061441549"></a><strong id="b1887501310388"><a name="b1887501310388"></a><a name="b1887501310388"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="68.70687068706872%" id="mcps1.2.4.1.2"><p id="p280718441141"><a name="p280718441141"></a><a name="p280718441141"></a><strong id="b142745501728"><a name="b142745501728"></a><a name="b142745501728"></a>Description</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="16.351635163516352%" id="mcps1.2.4.1.3"><p id="p138072441848"><a name="p138072441848"></a><a name="p138072441848"></a><strong id="b60793810112357_3"><a name="b60793810112357_3"></a><a name="b60793810112357_3"></a>Example Value</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row1680714443419"><td class="cellrowborder" valign="top" width="14.941494149414941%" headers="mcps1.2.4.1.1 "><p id="p1148710521043"><a name="p1148710521043"></a><a name="p1148710521043"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="68.70687068706872%" headers="mcps1.2.4.1.2 "><p id="p154921752249"><a name="p154921752249"></a><a name="p154921752249"></a>Name of the alarm rule. The system generates a name randomly but you can change it.</p>
        </td>
        <td class="cellrowborder" valign="top" width="16.351635163516352%" headers="mcps1.2.4.1.3 "><p id="p1549645214419"><a name="p1549645214419"></a><a name="p1549645214419"></a>alarm-fk0k</p>
        </td>
        </tr>
        <tr id="row1880724410418"><td class="cellrowborder" valign="top" width="14.941494149414941%" headers="mcps1.2.4.1.1 "><p id="p1050217521247"><a name="p1050217521247"></a><a name="p1050217521247"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="68.70687068706872%" headers="mcps1.2.4.1.2 "><p id="p125062529410"><a name="p125062529410"></a><a name="p125062529410"></a>Alarm rule description. This parameter is optional.</p>
        </td>
        <td class="cellrowborder" valign="top" width="16.351635163516352%" headers="mcps1.2.4.1.3 "><p id="p115101521946"><a name="p115101521946"></a><a name="p115101521946"></a>-</p>
        </td>
        </tr>
        </tbody>
        </table>



