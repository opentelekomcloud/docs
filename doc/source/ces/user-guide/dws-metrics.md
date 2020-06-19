# DWS Metrics<a name="EN-US_TOPIC_0102700161"></a>

**Table  1**  DWS metrics

<a name="table681604142420"></a>
<table><thead align="left"><tr id="row8817043243"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.7.1.1"><p id="p191792920453"><a name="p191792920453"></a><a name="p191792920453"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.7.1.2"><p id="p7817144112420"><a name="p7817144112420"></a><a name="p7817144112420"></a><strong id="b158171492419"><a name="b158171492419"></a><a name="b158171492419"></a>Metric</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.7.1.3"><p id="p9818174142410"><a name="p9818174142410"></a><a name="p9818174142410"></a><strong id="b148181042245"><a name="b148181042245"></a><a name="b148181042245"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.7.1.4"><p id="p11818444242"><a name="p11818444242"></a><a name="p11818444242"></a><strong id="b2818104182415"><a name="b2818104182415"></a><a name="b2818104182415"></a>Value Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.7.1.5"><p id="p58182442413"><a name="p58182442413"></a><a name="p58182442413"></a><strong id="b3727331210"><a name="b3727331210"></a><a name="b3727331210"></a>Monitored Object</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.7.1.6"><p id="p151120813416"><a name="p151120813416"></a><a name="p151120813416"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row138291346247"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.1 "><p id="p174766031820"><a name="p174766031820"></a><a name="p174766031820"></a>dws001_shared_buffer_hit_ratio</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.2 "><p id="p182910442419"><a name="p182910442419"></a><a name="p182910442419"></a>Shared Memory Hit Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p982913413249"><a name="p982913413249"></a><a name="p982913413249"></a>Percentage of data volume obtained from memory</p>
<p id="p09681328104517"><a name="p09681328104517"></a><a name="p09681328104517"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p108296419249"><a name="p108296419249"></a><a name="p108296419249"></a>0-100%</p>
</td>
<td class="cellrowborder" rowspan="9" valign="top" width="11%" headers="mcps1.2.7.1.5 "><p id="p178298411243"><a name="p178298411243"></a><a name="p178298411243"></a>Data warehouse clusters</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.6 "><p id="p64951124154515"><a name="p64951124154515"></a><a name="p64951124154515"></a>1 minute</p>
</td>
</tr>
<tr id="row198297418243"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p49450901820"><a name="p49450901820"></a><a name="p49450901820"></a>dws002_in_memory_sort_ratio</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1882914410242"><a name="p1882914410242"></a><a name="p1882914410242"></a>In-memory Sort Ratio</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p3829204162412"><a name="p3829204162412"></a><a name="p3829204162412"></a>Percentage of data volume that is sorted in memory</p>
<p id="p123694212460"><a name="p123694212460"></a><a name="p123694212460"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1182994112410"><a name="p1182994112410"></a><a name="p1182994112410"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p17553162454513"><a name="p17553162454513"></a><a name="p17553162454513"></a>1 minute</p>
</td>
</tr>
<tr id="row08306452418"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p472550131820"><a name="p472550131820"></a><a name="p472550131820"></a>dws003_physical_reads</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p4830046246"><a name="p4830046246"></a><a name="p4830046246"></a>File Reads</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1883016420241"><a name="p1883016420241"></a><a name="p1883016420241"></a>Total number of database file reads</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1483034142416"><a name="p1483034142416"></a><a name="p1483034142416"></a>&gt; 0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p12851780469"><a name="p12851780469"></a><a name="p12851780469"></a>1 minute</p>
</td>
</tr>
<tr id="row1283210410247"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p326223181820"><a name="p326223181820"></a><a name="p326223181820"></a>dws004_physical_writes</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p28322452414"><a name="p28322452414"></a><a name="p28322452414"></a>File Writes</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p208326452413"><a name="p208326452413"></a><a name="p208326452413"></a>Total number of database file writes</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p8832114192415"><a name="p8832114192415"></a><a name="p8832114192415"></a>&gt; 0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p122871389465"><a name="p122871389465"></a><a name="p122871389465"></a>1 minute</p>
</td>
</tr>
<tr id="row883319482417"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p192707691820"><a name="p192707691820"></a><a name="p192707691820"></a>dws005_physical_reads_per_second</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p78335492416"><a name="p78335492416"></a><a name="p78335492416"></a>File Reads per Second</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p38331540247"><a name="p38331540247"></a><a name="p38331540247"></a>Number of database file reads per second</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p18331740245"><a name="p18331740245"></a><a name="p18331740245"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p14267636204710"><a name="p14267636204710"></a><a name="p14267636204710"></a>1 minute</p>
</td>
</tr>
<tr id="row383304122414"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p164415431820"><a name="p164415431820"></a><a name="p164415431820"></a>dws006_physical_writes_per_second</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p138335422415"><a name="p138335422415"></a><a name="p138335422415"></a>File Writes per Second</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p28331348241"><a name="p28331348241"></a><a name="p28331348241"></a>Number of database file writes per second</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p8833114132419"><a name="p8833114132419"></a><a name="p8833114132419"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p6269163618474"><a name="p6269163618474"></a><a name="p6269163618474"></a>1 minute</p>
</td>
</tr>
<tr id="row883317413242"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p121668681820"><a name="p121668681820"></a><a name="p121668681820"></a>dws007_db_size</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p683310442410"><a name="p683310442410"></a><a name="p683310442410"></a>Data Volume</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p883316462410"><a name="p883316462410"></a><a name="p883316462410"></a>Total data volume of the database</p>
<p id="p8569174510476"><a name="p8569174510476"></a><a name="p8569174510476"></a>Unit: MB</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p14834164112415"><a name="p14834164112415"></a><a name="p14834164112415"></a>0-36000 MB</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p726983614715"><a name="p726983614715"></a><a name="p726983614715"></a>1 minute</p>
</td>
</tr>
<tr id="row1683413472411"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p538006441820"><a name="p538006441820"></a><a name="p538006441820"></a>dws008_active_sql_count</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p168401242248"><a name="p168401242248"></a><a name="p168401242248"></a>Active SQL Count</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p984015413244"><a name="p984015413244"></a><a name="p984015413244"></a>Number of active SQLs in the database</p>
<p id="p675552114502"><a name="p675552114502"></a><a name="p675552114502"></a>Unit: None</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p18840144142410"><a name="p18840144142410"></a><a name="p18840144142410"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p8273836184718"><a name="p8273836184718"></a><a name="p8273836184718"></a>1 minute</p>
</td>
</tr>
<tr id="row1484116414245"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p22581211820"><a name="p22581211820"></a><a name="p22581211820"></a>dws009_session_count</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1284404172414"><a name="p1284404172414"></a><a name="p1284404172414"></a>Session Count</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1084412416240"><a name="p1084412416240"></a><a name="p1084412416240"></a>Number of sessions that access the database</p>
<p id="p1867693217506"><a name="p1867693217506"></a><a name="p1867693217506"></a>Unit: None</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p78441745243"><a name="p78441745243"></a><a name="p78441745243"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1350134116473"><a name="p1350134116473"></a><a name="p1350134116473"></a>1 minute</p>
</td>
</tr>
<tr id="row16844245246"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.1 "><p id="p618009251820"><a name="p618009251820"></a><a name="p618009251820"></a>dws010_cpu_usage</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.7.1.2 "><p id="p1884513492419"><a name="p1884513492419"></a><a name="p1884513492419"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="p28456452420"><a name="p28456452420"></a><a name="p28456452420"></a>CPU Usage of each node in the cluster</p>
<p id="p1834101884617"><a name="p1834101884617"></a><a name="p1834101884617"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.7.1.4 "><p id="p10317114144511"><a name="p10317114144511"></a><a name="p10317114144511"></a>0-100%</p>
</td>
<td class="cellrowborder" rowspan="13" valign="top" width="11%" headers="mcps1.2.7.1.5 "><p id="p084517482416"><a name="p084517482416"></a><a name="p084517482416"></a>Nodes in the cluster</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.6 "><p id="p1352154184718"><a name="p1352154184718"></a><a name="p1352154184718"></a>1 minute</p>
</td>
</tr>
<tr id="row118461946245"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p110997811820"><a name="p110997811820"></a><a name="p110997811820"></a>dws011_mem_usage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1884615416242"><a name="p1884615416242"></a><a name="p1884615416242"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p6846184112410"><a name="p6846184112410"></a><a name="p6846184112410"></a>Memory Usage of each node in the cluster</p>
<p id="p12802208465"><a name="p12802208465"></a><a name="p12802208465"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p13192014114517"><a name="p13192014114517"></a><a name="p13192014114517"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p2035418418472"><a name="p2035418418472"></a><a name="p2035418418472"></a>1 minute</p>
</td>
</tr>
<tr id="row1784619417243"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p145509231820"><a name="p145509231820"></a><a name="p145509231820"></a>dws012_iops</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1484615492420"><a name="p1484615492420"></a><a name="p1484615492420"></a>IOPS</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p38461648241"><a name="p38461648241"></a><a name="p38461648241"></a>Number of I/O requests processed by each node in the cluster per second</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p138461943243"><a name="p138461943243"></a><a name="p138461943243"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p133552041114717"><a name="p133552041114717"></a><a name="p133552041114717"></a>1 minute</p>
</td>
</tr>
<tr id="row4848246244"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p24792981820"><a name="p24792981820"></a><a name="p24792981820"></a>dws013_bytes_in</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1184816418241"><a name="p1184816418241"></a><a name="p1184816418241"></a>Network Input Throughput</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p98485472411"><a name="p98485472411"></a><a name="p98485472411"></a>Data input to each node in the cluster per second over the network</p>
<p id="p23390140480"><a name="p23390140480"></a><a name="p23390140480"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p58481645245"><a name="p58481645245"></a><a name="p58481645245"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p203571241154716"><a name="p203571241154716"></a><a name="p203571241154716"></a>1 minute</p>
</td>
</tr>
<tr id="row1784804182419"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p229544381820"><a name="p229544381820"></a><a name="p229544381820"></a>dws014_bytes_out</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p108486419248"><a name="p108486419248"></a><a name="p108486419248"></a>Network Output Throughput</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p6848134132414"><a name="p6848134132414"></a><a name="p6848134132414"></a>Data sent to the network per second from each node in the cluster</p>
<p id="p160363312485"><a name="p160363312485"></a><a name="p160363312485"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p138502412415"><a name="p138502412415"></a><a name="p138502412415"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1136084194716"><a name="p1136084194716"></a><a name="p1136084194716"></a>1 minute</p>
</td>
</tr>
<tr id="row128506422415"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p22632241820"><a name="p22632241820"></a><a name="p22632241820"></a>dws015_disk_usage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p108505418243"><a name="p108505418243"></a><a name="p108505418243"></a>Disk Usage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p985014419243"><a name="p985014419243"></a><a name="p985014419243"></a>Disk Usage of each node in the cluster</p>
<p id="p2090883318460"><a name="p2090883318460"></a><a name="p2090883318460"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p885024112416"><a name="p885024112416"></a><a name="p885024112416"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p193627417475"><a name="p193627417475"></a><a name="p193627417475"></a>1 minute</p>
</td>
</tr>
<tr id="row118526417246"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p131888691820"><a name="p131888691820"></a><a name="p131888691820"></a>dws016_disk_total_size</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p685244152418"><a name="p685244152418"></a><a name="p685244152418"></a>Total Disk Size</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p16852114172411"><a name="p16852114172411"></a><a name="p16852114172411"></a>Total disk space of each node in the cluster</p>
<p id="p1356144465019"><a name="p1356144465019"></a><a name="p1356144465019"></a>Unit: GB</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p385219462412"><a name="p385219462412"></a><a name="p385219462412"></a>100-2000 GB</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p13365541194717"><a name="p13365541194717"></a><a name="p13365541194717"></a>1 minute</p>
</td>
</tr>
<tr id="row188521414246"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p505047341820"><a name="p505047341820"></a><a name="p505047341820"></a>dws017_disk_used_size</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p9852641240"><a name="p9852641240"></a><a name="p9852641240"></a>Disk Usage</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p188521948247"><a name="p188521948247"></a><a name="p188521948247"></a>Used disk space of each node in the cluster</p>
<p id="p134476575507"><a name="p134476575507"></a><a name="p134476575507"></a>Unit: GB</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p14852348248"><a name="p14852348248"></a><a name="p14852348248"></a>0-3600 GB</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1783164313478"><a name="p1783164313478"></a><a name="p1783164313478"></a>1 minute</p>
</td>
</tr>
<tr id="row13852134142418"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p435369601820"><a name="p435369601820"></a><a name="p435369601820"></a>dws018_disk_read_throughput</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1985216472414"><a name="p1985216472414"></a><a name="p1985216472414"></a>Disk Read Throughput</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p128525412412"><a name="p128525412412"></a><a name="p128525412412"></a>Data volume read from each disk in the cluster per second</p>
<p id="p20752105144815"><a name="p20752105144815"></a><a name="p20752105144815"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p138522411242"><a name="p138522411242"></a><a name="p138522411242"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p0851543144715"><a name="p0851543144715"></a><a name="p0851543144715"></a>1 minute</p>
</td>
</tr>
<tr id="row3853541245"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p62589891820"><a name="p62589891820"></a><a name="p62589891820"></a>dws019_disk_write_throughput</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p285312415247"><a name="p285312415247"></a><a name="p285312415247"></a>Disk Write Throughput</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p58533417248"><a name="p58533417248"></a><a name="p58533417248"></a>Data volume written to each disk in the cluster per second</p>
<p id="p674694915480"><a name="p674694915480"></a><a name="p674694915480"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p12853144102419"><a name="p12853144102419"></a><a name="p12853144102419"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1589124317474"><a name="p1589124317474"></a><a name="p1589124317474"></a>1 minute</p>
</td>
</tr>
<tr id="row38531247247"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p259222881820"><a name="p259222881820"></a><a name="p259222881820"></a>dws020_avg_disk_sec_per_read</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p68531445244"><a name="p68531445244"></a><a name="p68531445244"></a>Average Time per Disk Read</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p15853114132410"><a name="p15853114132410"></a><a name="p15853114132410"></a>Average time used each time when a disk reads data</p>
<p id="p24541114134911"><a name="p24541114134911"></a><a name="p24541114134911"></a>Unit: Second</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p118551643247"><a name="p118551643247"></a><a name="p118551643247"></a>&gt; 0s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p13911343154719"><a name="p13911343154719"></a><a name="p13911343154719"></a>1 minute</p>
</td>
</tr>
<tr id="row685513410246"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p392485401820"><a name="p392485401820"></a><a name="p392485401820"></a>dws021_avg_disk_sec_per_write</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p38553415247"><a name="p38553415247"></a><a name="p38553415247"></a>Average Time per Disk Write</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p15855343246"><a name="p15855343246"></a><a name="p15855343246"></a>Average time used each time when data is written to a disk</p>
<p id="p421734164915"><a name="p421734164915"></a><a name="p421734164915"></a>Unit: Second</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p58556418245"><a name="p58556418245"></a><a name="p58556418245"></a>&gt; 0s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p189414316479"><a name="p189414316479"></a><a name="p189414316479"></a>1 minute</p>
</td>
</tr>
<tr id="row108552419248"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p428065411820"><a name="p428065411820"></a><a name="p428065411820"></a>dws022_avg_disk_queue_length</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p185544172411"><a name="p185544172411"></a><a name="p185544172411"></a>Average Disk Queue Length</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1285624182414"><a name="p1285624182414"></a><a name="p1285624182414"></a>Average I/O queue length of a disk</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p48561432419"><a name="p48561432419"></a><a name="p48561432419"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1951243104719"><a name="p1951243104719"></a><a name="p1951243104719"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

