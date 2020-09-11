# DWS Metrics<a name="EN-US_TOPIC_0171212549"></a>

## Function<a name="section288632411820"></a>

This section describes metrics reported by the Data Warehouse Service \(DWS\) to Cloud Eye as well as their namespaces and dimensions. You can use APIs provided by Cloud Eye to query the metrics of the monitored object and alarms generated for DWS.

## Namespace<a name="section362284861820"></a>

SYS.DWS

## Metrics<a name="section367829141820"></a>

<a name="table266260401820"></a>
<table><thead align="left"><tr id="row588923361820"><th class="cellrowborder" valign="top" width="17.530000000000005%" id="mcps1.1.6.1.1"><p id="p55499171820"><a name="p55499171820"></a><a name="p55499171820"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="17.530000000000005%" id="mcps1.1.6.1.2"><p id="p468901511820"><a name="p468901511820"></a><a name="p468901511820"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="28.680000000000007%" id="mcps1.1.6.1.3"><p id="p400058771820"><a name="p400058771820"></a><a name="p400058771820"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="15.170000000000003%" id="mcps1.1.6.1.4"><p id="p192506081820"><a name="p192506081820"></a><a name="p192506081820"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="21.090000000000003%" id="mcps1.1.6.1.5"><p id="p157953911820"><a name="p157953911820"></a><a name="p157953911820"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row43582831820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p174766031820"><a name="p174766031820"></a><a name="p174766031820"></a>dws001_shared_buffer_hit_ratio</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p63187111820"><a name="p63187111820"></a><a name="p63187111820"></a>Cache Hit Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p420536081820"><a name="p420536081820"></a><a name="p420536081820"></a>Percentage of data volume obtained from memory</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p508991261820"><a name="p508991261820"></a><a name="p508991261820"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p291885521820"><a name="p291885521820"></a><a name="p291885521820"></a>Monitored object: data warehouse</p>
<p id="p9510676113640"><a name="p9510676113640"></a><a name="p9510676113640"></a>Dimension: </p>
<p id="p49893264113652"><a name="p49893264113652"></a><a name="p49893264113652"></a>datastore_id</p>
</td>
</tr>
<tr id="row613703831820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p49450901820"><a name="p49450901820"></a><a name="p49450901820"></a>dws002_in_memory_sort_ratio</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p650080471820"><a name="p650080471820"></a><a name="p650080471820"></a>In-memory Sort Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p311604441820"><a name="p311604441820"></a><a name="p311604441820"></a>Percentage of data volume that is sorted in memory</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p409680171820"><a name="p409680171820"></a><a name="p409680171820"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p300750951820"><a name="p300750951820"></a><a name="p300750951820"></a>Monitored object: data warehouse</p>
<p id="p18576899114058"><a name="p18576899114058"></a><a name="p18576899114058"></a>Dimension: </p>
<p id="p32974368114058"><a name="p32974368114058"></a><a name="p32974368114058"></a>datastore_id</p>
</td>
</tr>
<tr id="row22404041820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p472550131820"><a name="p472550131820"></a><a name="p472550131820"></a>dws003_physical_reads</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p24508761820"><a name="p24508761820"></a><a name="p24508761820"></a>File Reads</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p643032301820"><a name="p643032301820"></a><a name="p643032301820"></a>Total number of database file reads</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p411791571820"><a name="p411791571820"></a><a name="p411791571820"></a>≥ 0 times</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p471774491820"><a name="p471774491820"></a><a name="p471774491820"></a>Monitored object: data warehouse</p>
<p id="p2545403911411"><a name="p2545403911411"></a><a name="p2545403911411"></a>Dimension: </p>
<p id="p2775976111411"><a name="p2775976111411"></a><a name="p2775976111411"></a>datastore_id</p>
</td>
</tr>
<tr id="row219438611820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p326223181820"><a name="p326223181820"></a><a name="p326223181820"></a>dws004_physical_writes</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p251621361820"><a name="p251621361820"></a><a name="p251621361820"></a>File Writes</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p248671631820"><a name="p248671631820"></a><a name="p248671631820"></a>Total number of database file writes</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p9743021820"><a name="p9743021820"></a><a name="p9743021820"></a>≥ 0 times</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p118096091820"><a name="p118096091820"></a><a name="p118096091820"></a>Monitored object: data warehouse</p>
<p id="p4812806211413"><a name="p4812806211413"></a><a name="p4812806211413"></a>Dimension: </p>
<p id="p3049937611413"><a name="p3049937611413"></a><a name="p3049937611413"></a>datastore_id</p>
</td>
</tr>
<tr id="row391776211820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p192707691820"><a name="p192707691820"></a><a name="p192707691820"></a>dws005_physical_reads_per_second</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p174284241820"><a name="p174284241820"></a><a name="p174284241820"></a>File Reads per Second</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p24162601820"><a name="p24162601820"></a><a name="p24162601820"></a>Number of database file reads per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p614994051820"><a name="p614994051820"></a><a name="p614994051820"></a>≥ 0 times/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p153959141820"><a name="p153959141820"></a><a name="p153959141820"></a>Monitored object: data warehouse</p>
<p id="p1260566011417"><a name="p1260566011417"></a><a name="p1260566011417"></a>Dimension: </p>
<p id="p4634208211417"><a name="p4634208211417"></a><a name="p4634208211417"></a>datastore_id</p>
</td>
</tr>
<tr id="row43455041820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p164415431820"><a name="p164415431820"></a><a name="p164415431820"></a>dws006_physical_writes_per_second</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p566965981820"><a name="p566965981820"></a><a name="p566965981820"></a>File Writes per Second</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p290217501820"><a name="p290217501820"></a><a name="p290217501820"></a>Number of database file writes per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p19515671820"><a name="p19515671820"></a><a name="p19515671820"></a>≥ 0 times/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p238592081820"><a name="p238592081820"></a><a name="p238592081820"></a>Monitored object: data warehouse</p>
<p id="p3520819511419"><a name="p3520819511419"></a><a name="p3520819511419"></a>Dimension: </p>
<p id="p4843830311419"><a name="p4843830311419"></a><a name="p4843830311419"></a>datastore_id</p>
</td>
</tr>
<tr id="row134062801820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p121668681820"><a name="p121668681820"></a><a name="p121668681820"></a>dws007_db_size</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p459922771820"><a name="p459922771820"></a><a name="p459922771820"></a>Data Volume</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p343869951820"><a name="p343869951820"></a><a name="p343869951820"></a>Total data volume of the database</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p338832211820"><a name="p338832211820"></a><a name="p338832211820"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p601864041820"><a name="p601864041820"></a><a name="p601864041820"></a>Monitored object: data warehouse</p>
<p id="p24239331114113"><a name="p24239331114113"></a><a name="p24239331114113"></a>Dimension: </p>
<p id="p16827392114113"><a name="p16827392114113"></a><a name="p16827392114113"></a>datastore_id</p>
</td>
</tr>
<tr id="row48067271820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p538006441820"><a name="p538006441820"></a><a name="p538006441820"></a>dws008_active_sql_count</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p628848971820"><a name="p628848971820"></a><a name="p628848971820"></a>Active SQL Count</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p605118781820"><a name="p605118781820"></a><a name="p605118781820"></a>Number of active SQLs in the database</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p25151001820"><a name="p25151001820"></a><a name="p25151001820"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p23965541820"><a name="p23965541820"></a><a name="p23965541820"></a>Monitored object: data warehouse</p>
<p id="p15484654114116"><a name="p15484654114116"></a><a name="p15484654114116"></a>Dimension: </p>
<p id="p5144166114116"><a name="p5144166114116"></a><a name="p5144166114116"></a>datastore_id</p>
</td>
</tr>
<tr id="row215689941820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p22581211820"><a name="p22581211820"></a><a name="p22581211820"></a>dws009_session_count</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p486900751820"><a name="p486900751820"></a><a name="p486900751820"></a>Session Count</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p515820181820"><a name="p515820181820"></a><a name="p515820181820"></a>Number of sessions that access the database</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p173939581820"><a name="p173939581820"></a><a name="p173939581820"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p667333581820"><a name="p667333581820"></a><a name="p667333581820"></a>Monitored object: data warehouse</p>
<p id="p19719445114123"><a name="p19719445114123"></a><a name="p19719445114123"></a>Dimension: </p>
<p id="p43257277114123"><a name="p43257277114123"></a><a name="p43257277114123"></a>datastore_id</p>
</td>
</tr>
<tr id="row637293151820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p618009251820"><a name="p618009251820"></a><a name="p618009251820"></a>dws010_cpu_usage</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p398190561820"><a name="p398190561820"></a><a name="p398190561820"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p41180831820"><a name="p41180831820"></a><a name="p41180831820"></a>CPU usages of each node in the cluster</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p651292781820"><a name="p651292781820"></a><a name="p651292781820"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p409801701820"><a name="p409801701820"></a><a name="p409801701820"></a>Monitored object: data warehouse</p>
<p id="p34693831114130"><a name="p34693831114130"></a><a name="p34693831114130"></a>Dimension: </p>
<p id="p43809023114130"><a name="p43809023114130"></a><a name="p43809023114130"></a>dws_instance_id</p>
</td>
</tr>
<tr id="row332772141820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p110997811820"><a name="p110997811820"></a><a name="p110997811820"></a>dws011_mem_usage</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p266670891820"><a name="p266670891820"></a><a name="p266670891820"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p125506341820"><a name="p125506341820"></a><a name="p125506341820"></a>Memory usages of each node in the cluster</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p99684391820"><a name="p99684391820"></a><a name="p99684391820"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p21372491820"><a name="p21372491820"></a><a name="p21372491820"></a>Monitored object: data warehouse</p>
<p id="p3160250611421"><a name="p3160250611421"></a><a name="p3160250611421"></a>Dimension: </p>
<p id="p1598710311421"><a name="p1598710311421"></a><a name="p1598710311421"></a>dws_instance_id</p>
</td>
</tr>
<tr id="row192352441820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p145509231820"><a name="p145509231820"></a><a name="p145509231820"></a>dws012_iops</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p377741391820"><a name="p377741391820"></a><a name="p377741391820"></a>IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p398064361820"><a name="p398064361820"></a><a name="p398064361820"></a>Number of I/O requests processed by each node in the cluster per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p30958531820"><a name="p30958531820"></a><a name="p30958531820"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p494375021820"><a name="p494375021820"></a><a name="p494375021820"></a>Monitored object: data warehouse</p>
<p id="p4227380011425"><a name="p4227380011425"></a><a name="p4227380011425"></a>Dimension: </p>
<p id="p4491988011425"><a name="p4491988011425"></a><a name="p4491988011425"></a>dws_instance_id</p>
</td>
</tr>
<tr id="row422843371820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p24792981820"><a name="p24792981820"></a><a name="p24792981820"></a>dws013_bytes_in</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p666054881820"><a name="p666054881820"></a><a name="p666054881820"></a>Network Input Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p263354581820"><a name="p263354581820"></a><a name="p263354581820"></a>Data input to each node in the cluster per second over the network</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p527973771820"><a name="p527973771820"></a><a name="p527973771820"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p487291401820"><a name="p487291401820"></a><a name="p487291401820"></a>Monitored object: data warehouse</p>
<p id="p4077838411428"><a name="p4077838411428"></a><a name="p4077838411428"></a>Dimension: </p>
<p id="p3146114411428"><a name="p3146114411428"></a><a name="p3146114411428"></a>dws_instance_id</p>
</td>
</tr>
<tr id="row359090811820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p229544381820"><a name="p229544381820"></a><a name="p229544381820"></a>dws014_bytes_out</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p473701711820"><a name="p473701711820"></a><a name="p473701711820"></a>Network Output Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p117786571820"><a name="p117786571820"></a><a name="p117786571820"></a>Data sent to the network per second from each node in the cluster</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p145471671820"><a name="p145471671820"></a><a name="p145471671820"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p374699181820"><a name="p374699181820"></a><a name="p374699181820"></a>Monitored object: data warehouse</p>
<p id="p47585865114211"><a name="p47585865114211"></a><a name="p47585865114211"></a>Dimension: </p>
<p id="p25619609114211"><a name="p25619609114211"></a><a name="p25619609114211"></a>dws_instance_id</p>
</td>
</tr>
<tr id="row16849501820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p22632241820"><a name="p22632241820"></a><a name="p22632241820"></a>dws015_disk_usage</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p491034711820"><a name="p491034711820"></a><a name="p491034711820"></a>Disk Utilization</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p179582431820"><a name="p179582431820"></a><a name="p179582431820"></a>Disk usages of each node in the cluster</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p453315791820"><a name="p453315791820"></a><a name="p453315791820"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p479792961820"><a name="p479792961820"></a><a name="p479792961820"></a>Monitored object: data warehouse</p>
<p id="p34198202114213"><a name="p34198202114213"></a><a name="p34198202114213"></a>Dimension: </p>
<p id="p39348362114213"><a name="p39348362114213"></a><a name="p39348362114213"></a>dws_instance_id</p>
</td>
</tr>
<tr id="row291604821820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p131888691820"><a name="p131888691820"></a><a name="p131888691820"></a>dws016_disk_total_size</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p616654481820"><a name="p616654481820"></a><a name="p616654481820"></a>Total Disk Size</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p288453631820"><a name="p288453631820"></a><a name="p288453631820"></a>Total disk space of each cluster node</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p547730711820"><a name="p547730711820"></a><a name="p547730711820"></a>≥ 0 GB</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p74337631820"><a name="p74337631820"></a><a name="p74337631820"></a>Monitored object: data warehouse</p>
<p id="p889315114216"><a name="p889315114216"></a><a name="p889315114216"></a>Dimension: </p>
<p id="p8003835114216"><a name="p8003835114216"></a><a name="p8003835114216"></a>dws_instance_id</p>
</td>
</tr>
<tr id="row669038741820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p505047341820"><a name="p505047341820"></a><a name="p505047341820"></a>dws017_disk_used_size</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p643516871820"><a name="p643516871820"></a><a name="p643516871820"></a>Disk Usage</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p451041641820"><a name="p451041641820"></a><a name="p451041641820"></a>Used disk space of each node in the cluster</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p295586861820"><a name="p295586861820"></a><a name="p295586861820"></a>≥ 0 GB</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p454433561820"><a name="p454433561820"></a><a name="p454433561820"></a>Monitored object: data warehouse</p>
<p id="p61890117114218"><a name="p61890117114218"></a><a name="p61890117114218"></a>Dimension: </p>
<p id="p20140149114218"><a name="p20140149114218"></a><a name="p20140149114218"></a>dws_instance_id</p>
</td>
</tr>
<tr id="row63370241820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p435369601820"><a name="p435369601820"></a><a name="p435369601820"></a>dws018_disk_read_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p368328891820"><a name="p368328891820"></a><a name="p368328891820"></a>Disk Read Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p306740021820"><a name="p306740021820"></a><a name="p306740021820"></a>Data volume read by each disk in the cluster per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p15661951820"><a name="p15661951820"></a><a name="p15661951820"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p597529651820"><a name="p597529651820"></a><a name="p597529651820"></a>Monitored object: data warehouse</p>
<p id="p18011561114221"><a name="p18011561114221"></a><a name="p18011561114221"></a>Dimension: </p>
<p id="p27886321114221"><a name="p27886321114221"></a><a name="p27886321114221"></a>dws_instance_id</p>
</td>
</tr>
<tr id="row9057751820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p62589891820"><a name="p62589891820"></a><a name="p62589891820"></a>dws019_disk_write_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p372161111820"><a name="p372161111820"></a><a name="p372161111820"></a>Disk Read Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p617150381820"><a name="p617150381820"></a><a name="p617150381820"></a>Data volume written to each disk per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p328621771820"><a name="p328621771820"></a><a name="p328621771820"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p445906891820"><a name="p445906891820"></a><a name="p445906891820"></a>Monitored object: data warehouse</p>
<p id="p27720157114224"><a name="p27720157114224"></a><a name="p27720157114224"></a>Dimension: </p>
<p id="p48154822114224"><a name="p48154822114224"></a><a name="p48154822114224"></a>dws_instance_id</p>
</td>
</tr>
<tr id="row657718831820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p259222881820"><a name="p259222881820"></a><a name="p259222881820"></a>dws020_avg_disk_sec_per_read</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p193305981820"><a name="p193305981820"></a><a name="p193305981820"></a>Average Time per Disk Read</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p222746121820"><a name="p222746121820"></a><a name="p222746121820"></a>Average time used each time when a disk reads data</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p594131871820"><a name="p594131871820"></a><a name="p594131871820"></a>≥ 0s</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p477388751820"><a name="p477388751820"></a><a name="p477388751820"></a>Monitored object: data warehouse</p>
<p id="p26879206114230"><a name="p26879206114230"></a><a name="p26879206114230"></a>Dimension: </p>
<p id="p40586266114230"><a name="p40586266114230"></a><a name="p40586266114230"></a>dws_instance_id</p>
</td>
</tr>
<tr id="row269966931820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p392485401820"><a name="p392485401820"></a><a name="p392485401820"></a>dws021_avg_disk_sec_per_write</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p250152001820"><a name="p250152001820"></a><a name="p250152001820"></a>Average Time per Disk Write</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p129653201820"><a name="p129653201820"></a><a name="p129653201820"></a>Average time consumed by the disk to write data on cluster nodes</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p435580131820"><a name="p435580131820"></a><a name="p435580131820"></a>≥ 0s</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p385381501820"><a name="p385381501820"></a><a name="p385381501820"></a>Monitored object: data warehouse</p>
<p id="p64116167114232"><a name="p64116167114232"></a><a name="p64116167114232"></a>Dimension: </p>
<p id="p40174592114232"><a name="p40174592114232"></a><a name="p40174592114232"></a>dws_instance_id</p>
</td>
</tr>
<tr id="row112990341820"><td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.1 "><p id="p428065411820"><a name="p428065411820"></a><a name="p428065411820"></a>dws022_avg_disk_queue_length</p>
</td>
<td class="cellrowborder" valign="top" width="17.530000000000005%" headers="mcps1.1.6.1.2 "><p id="p447777681820"><a name="p447777681820"></a><a name="p447777681820"></a>Average Disk Queue Length</p>
</td>
<td class="cellrowborder" valign="top" width="28.680000000000007%" headers="mcps1.1.6.1.3 "><p id="p31205961820"><a name="p31205961820"></a><a name="p31205961820"></a>Average time used each time when data is written to a disk</p>
</td>
<td class="cellrowborder" valign="top" width="15.170000000000003%" headers="mcps1.1.6.1.4 "><p id="p514417201820"><a name="p514417201820"></a><a name="p514417201820"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="21.090000000000003%" headers="mcps1.1.6.1.5 "><p id="p60298211820"><a name="p60298211820"></a><a name="p60298211820"></a>Monitored object: data warehouse</p>
<p id="p52227848114235"><a name="p52227848114235"></a><a name="p52227848114235"></a>Dimension: </p>
<p id="p288585114235"><a name="p288585114235"></a><a name="p288585114235"></a>dws_instance_id</p>
</td>
</tr>
</tbody>
</table>

## **Dimension**<a name="section475962021820"></a>

<a name="table300871641820"></a>
<table><thead align="left"><tr id="row440366111820"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p101957281820"><a name="p101957281820"></a><a name="p101957281820"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p205476211820"><a name="p205476211820"></a><a name="p205476211820"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row537446191820"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p583468891820"><a name="p583468891820"></a><a name="p583468891820"></a>datastore_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p284776081820"><a name="p284776081820"></a><a name="p284776081820"></a>Data Warehouse Service</p>
</td>
</tr>
<tr id="row549718881820"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p235379061820"><a name="p235379061820"></a><a name="p235379061820"></a>dws_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p275222491820"><a name="p275222491820"></a><a name="p275222491820"></a>Data warehouse node</p>
</td>
</tr>
</tbody>
</table>

