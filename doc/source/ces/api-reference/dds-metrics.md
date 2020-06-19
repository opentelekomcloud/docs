# DDS Metrics<a name="EN-US_TOPIC_0171212626"></a>

## Function<a name="section59820001153251"></a>

This section describes metrics reported by the Document Database Service \(DDS\) to Cloud Eye as well as their namespaces and dimensions. You can use APIs provided by Cloud Eye to query the metrics of the monitored object and alarms generated for DDS.

## Namespace<a name="section55128484153251"></a>

SYS.DDS

## Metrics<a name="section57564324153251"></a>

<a name="table32198700153251"></a>
<table><thead align="left"><tr id="row43554686153251"><th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.1.6.1.1"><p id="p38268712153251"><a name="p38268712153251"></a><a name="p38268712153251"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.6.1.2"><p id="p12757995153251"><a name="p12757995153251"></a><a name="p12757995153251"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="32.32323232323232%" id="mcps1.1.6.1.3"><p id="p26764654153251"><a name="p26764654153251"></a><a name="p26764654153251"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.1.6.1.4"><p id="p20453337153251"><a name="p20453337153251"></a><a name="p20453337153251"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.6.1.5"><p id="p46107605153251"><a name="p46107605153251"></a><a name="p46107605153251"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row1671192211720"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1945442218710"><a name="p1945442218710"></a><a name="p1945442218710"></a>mongo001_command_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p204541822072"><a name="p204541822072"></a><a name="p204541822072"></a>Commands per Second</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p7454192214710"><a name="p7454192214710"></a><a name="p7454192214710"></a>Average number of the command statement execution times on nodes per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p136515555163"><a name="p136515555163"></a><a name="p136515555163"></a>≥ 0 executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p154551322677"><a name="p154551322677"></a><a name="p154551322677"></a>Monitored object: database</p>
<p id="p16519141713317"><a name="p16519141713317"></a><a name="p16519141713317"></a>Monitored instance type:</p>
<a name="ul255431916318"></a><a name="ul255431916318"></a><ul id="ul255431916318"><li>DDS DB instance</li><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row867172217718"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1645512214717"><a name="p1645512214717"></a><a name="p1645512214717"></a>mongo002_delete_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p6455202210718"><a name="p6455202210718"></a><a name="p6455202210718"></a>Delete Operations per Second</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p1455132215714"><a name="p1455132215714"></a><a name="p1455132215714"></a>Average number of the delete statement execution times on nodes per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p171165561614"><a name="p171165561614"></a><a name="p171165561614"></a>≥ 0 executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1645515221374"><a name="p1645515221374"></a><a name="p1645515221374"></a>Monitored object: database</p>
<p id="p1642413199323"><a name="p1642413199323"></a><a name="p1642413199323"></a>Monitored instance type:</p>
<a name="ul81787223328"></a><a name="ul81787223328"></a><ul id="ul81787223328"><li>DDS DB instance</li><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row2067014221779"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p184551222773"><a name="p184551222773"></a><a name="p184551222773"></a>mongo003_insert_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p13455822371"><a name="p13455822371"></a><a name="p13455822371"></a>Insert Operations per Second</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p11455622272"><a name="p11455622272"></a><a name="p11455622272"></a>Average number of the insert statement execution times on nodes per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p98501751121620"><a name="p98501751121620"></a><a name="p98501751121620"></a>≥ 0 executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p14562221275"><a name="p14562221275"></a><a name="p14562221275"></a>Monitored object: database</p>
<p id="p1045616223710"><a name="p1045616223710"></a><a name="p1045616223710"></a>Monitored instance type:</p>
<a name="ul3294627123213"></a><a name="ul3294627123213"></a><ul id="ul3294627123213"><li>DDS DB instance</li><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row966917227714"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p945612213713"><a name="p945612213713"></a><a name="p945612213713"></a>mongo004_query_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p44562022471"><a name="p44562022471"></a><a name="p44562022471"></a>Query Operations per Second</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p1945622213718"><a name="p1945622213718"></a><a name="p1945622213718"></a>Average number of the query statement execution times on nodes per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p4856105191617"><a name="p4856105191617"></a><a name="p4856105191617"></a>≥ 0 executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p134563221375"><a name="p134563221375"></a><a name="p134563221375"></a>Monitored object: database</p>
<p id="p845613226713"><a name="p845613226713"></a><a name="p845613226713"></a>Monitored instance type:</p>
<a name="ul67661329173213"></a><a name="ul67661329173213"></a><ul id="ul67661329173213"><li>DDS DB instance</li><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row766812229712"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p9456162217710"><a name="p9456162217710"></a><a name="p9456162217710"></a>mongo005_update_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p645642213718"><a name="p645642213718"></a><a name="p645642213718"></a>Update Operations per Second</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p1345620222719"><a name="p1345620222719"></a><a name="p1345620222719"></a>Average number of the update statement execution times on nodes per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p108142465168"><a name="p108142465168"></a><a name="p108142465168"></a>≥ 0 executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1445612214712"><a name="p1445612214712"></a><a name="p1445612214712"></a>Monitored object: database</p>
<p id="p645610221375"><a name="p645610221375"></a><a name="p645610221375"></a>Monitored instance type:</p>
<a name="ul96203313218"></a><a name="ul96203313218"></a><ul id="ul96203313218"><li>DDS DB instance</li><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1666819221174"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p245620223714"><a name="p245620223714"></a><a name="p245620223714"></a>mongo006_getmore_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p345662215714"><a name="p345662215714"></a><a name="p345662215714"></a>Getmore Operations per Second</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p545616221779"><a name="p545616221779"></a><a name="p545616221779"></a>Average number of the getmore statement execution times on nodes per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p345622213716"><a name="p345622213716"></a><a name="p345622213716"></a>≥ 0 executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p14567221071"><a name="p14567221071"></a><a name="p14567221071"></a>Monitored object: database</p>
<p id="p1456102219713"><a name="p1456102219713"></a><a name="p1456102219713"></a>Monitored instance type:</p>
<a name="ul1454383593220"></a><a name="ul1454383593220"></a><ul id="ul1454383593220"><li>DDS DB instance</li><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row966814221718"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p134561221173"><a name="p134561221173"></a><a name="p134561221173"></a>mongo007_chunk_num1</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p84571022675"><a name="p84571022675"></a><a name="p84571022675"></a>Number of Chunks of Shard 1</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p2457132219718"><a name="p2457132219718"></a><a name="p2457132219718"></a>Number of chunks in shard 1</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p103841535171614"><a name="p103841535171614"></a><a name="p103841535171614"></a>0-64 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p13457422970"><a name="p13457422970"></a><a name="p13457422970"></a>Monitored object: database</p>
<p id="p74576221718"><a name="p74576221718"></a><a name="p74576221718"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row16681227710"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p845719221375"><a name="p845719221375"></a><a name="p845719221375"></a>mongo007_chunk_num2</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1145712213720"><a name="p1145712213720"></a><a name="p1145712213720"></a>Number of Chunks of Shard 2</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p15457162215716"><a name="p15457162215716"></a><a name="p15457162215716"></a>Number of chunks in shard 2</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p143918354161"><a name="p143918354161"></a><a name="p143918354161"></a>0-64 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p6458122470"><a name="p6458122470"></a><a name="p6458122470"></a>Monitored object: database</p>
<p id="p1445816227711"><a name="p1445816227711"></a><a name="p1445816227711"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row1366715221072"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p9458192211711"><a name="p9458192211711"></a><a name="p9458192211711"></a>mongo007_chunk_num3</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p204581822171"><a name="p204581822171"></a><a name="p204581822171"></a>Number of Chunks of Shard 3</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p1945872213717"><a name="p1945872213717"></a><a name="p1945872213717"></a>Number of chunks in shard 3</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p1445812222714"><a name="p1445812222714"></a><a name="p1445812222714"></a>0-64 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p645972213719"><a name="p645972213719"></a><a name="p645972213719"></a>Monitored object: database</p>
<p id="p74591227714"><a name="p74591227714"></a><a name="p74591227714"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row26677227715"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p745916222074"><a name="p745916222074"></a><a name="p745916222074"></a>mongo007_chunk_num4</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p145915221573"><a name="p145915221573"></a><a name="p145915221573"></a>Number of Chunks of Shard 4</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p3459522178"><a name="p3459522178"></a><a name="p3459522178"></a>Number of chunks in shard 4</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p1645910221971"><a name="p1645910221971"></a><a name="p1645910221971"></a>0-64 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1845918222718"><a name="p1845918222718"></a><a name="p1845918222718"></a>Monitored object: database</p>
<p id="p1446017221176"><a name="p1446017221176"></a><a name="p1446017221176"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row866732220710"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p18460112213716"><a name="p18460112213716"></a><a name="p18460112213716"></a>mongo007_chunk_num5</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p8460112215716"><a name="p8460112215716"></a><a name="p8460112215716"></a>Number of Chunks of Shard 5</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p154601222470"><a name="p154601222470"></a><a name="p154601222470"></a>Number of chunks in shard 5</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p164605221173"><a name="p164605221173"></a><a name="p164605221173"></a>0-64 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p14460172220716"><a name="p14460172220716"></a><a name="p14460172220716"></a>Monitored object: database</p>
<p id="p1046014221672"><a name="p1046014221672"></a><a name="p1046014221672"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row196666221079"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1246016221575"><a name="p1246016221575"></a><a name="p1246016221575"></a>mongo007_chunk_num6</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1946016221978"><a name="p1946016221978"></a><a name="p1946016221978"></a>Number of Chunks of Shard 6</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p11460522171"><a name="p11460522171"></a><a name="p11460522171"></a>Number of chunks in shard 6</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p134605223710"><a name="p134605223710"></a><a name="p134605223710"></a>0-64 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p94608226710"><a name="p94608226710"></a><a name="p94608226710"></a>Monitored object: database</p>
<p id="p1946012210710"><a name="p1946012210710"></a><a name="p1946012210710"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row166616223711"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1746082211717"><a name="p1746082211717"></a><a name="p1746082211717"></a>mongo007_chunk_num7</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p154609222719"><a name="p154609222719"></a><a name="p154609222719"></a>Number of Chunks of Shard 7</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p3460222979"><a name="p3460222979"></a><a name="p3460222979"></a>Number of chunks in shard 7</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p194602221976"><a name="p194602221976"></a><a name="p194602221976"></a>0-64 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p04602223719"><a name="p04602223719"></a><a name="p04602223719"></a>Monitored object: database</p>
<p id="p746116221578"><a name="p746116221578"></a><a name="p746116221578"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row66665221715"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p134611422675"><a name="p134611422675"></a><a name="p134611422675"></a>mongo007_chunk_num8</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1946182211716"><a name="p1946182211716"></a><a name="p1946182211716"></a>Number of Chunks of Shard 8</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p1146114222715"><a name="p1146114222715"></a><a name="p1146114222715"></a>Number of chunks in shard 8</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p94614224720"><a name="p94614224720"></a><a name="p94614224720"></a>0-64 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p144611222712"><a name="p144611222712"></a><a name="p144611222712"></a>Monitored object: database</p>
<p id="p446115221271"><a name="p446115221271"></a><a name="p446115221271"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row96661622673"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1246116221073"><a name="p1246116221073"></a><a name="p1246116221073"></a>mongo007_chunk_num9</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p12461202220711"><a name="p12461202220711"></a><a name="p12461202220711"></a>Number of Chunks of Shard 9</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p746113221873"><a name="p746113221873"></a><a name="p746113221873"></a>Number of chunks in shard 9</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p14612227712"><a name="p14612227712"></a><a name="p14612227712"></a>0-64 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p24615222719"><a name="p24615222719"></a><a name="p24615222719"></a>Monitored object: database</p>
<p id="p7461182212715"><a name="p7461182212715"></a><a name="p7461182212715"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row8666422972"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p54614224713"><a name="p54614224713"></a><a name="p54614224713"></a>mongo007_chunk_num10</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1946119229712"><a name="p1946119229712"></a><a name="p1946119229712"></a>Number of Chunks of Shard 10</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p134614221876"><a name="p134614221876"></a><a name="p134614221876"></a>Number of chunks in shard 10</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p846114221777"><a name="p846114221777"></a><a name="p846114221777"></a>0-64 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p134619226718"><a name="p134619226718"></a><a name="p134619226718"></a>Monitored object: database</p>
<p id="p84619221372"><a name="p84619221372"></a><a name="p84619221372"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row186661222774"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p164614221972"><a name="p164614221972"></a><a name="p164614221972"></a>mongo007_chunk_num11</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1046192211720"><a name="p1046192211720"></a><a name="p1046192211720"></a>Number of Chunks of Shard 11</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p164615221771"><a name="p164615221771"></a><a name="p164615221771"></a>Number of chunks in shard 11</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p746111221575"><a name="p746111221575"></a><a name="p746111221575"></a>0-64 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p2046216223712"><a name="p2046216223712"></a><a name="p2046216223712"></a>Monitored object: database</p>
<p id="p246242215716"><a name="p246242215716"></a><a name="p246242215716"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row2665822979"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1146218222710"><a name="p1146218222710"></a><a name="p1146218222710"></a>mongo007_chunk_num12</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1346210221974"><a name="p1346210221974"></a><a name="p1346210221974"></a>Number of Chunks of Shard 12</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p146202212720"><a name="p146202212720"></a><a name="p146202212720"></a>Number of chunks in shard 12</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p9462522278"><a name="p9462522278"></a><a name="p9462522278"></a>0-64 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p84621221872"><a name="p84621221872"></a><a name="p84621221872"></a>Monitored object: database</p>
<p id="p346218228714"><a name="p346218228714"></a><a name="p346218228714"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row26654223711"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1746219221074"><a name="p1746219221074"></a><a name="p1746219221074"></a>mongo008_connections</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p194621522171"><a name="p194621522171"></a><a name="p194621522171"></a>Current DB Instance Active Connections</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p846210221175"><a name="p846210221175"></a><a name="p846210221175"></a>Total number of connections attempting to connect to DDS DB instances</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p18462202215716"><a name="p18462202215716"></a><a name="p18462202215716"></a>0-200 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p114621522577"><a name="p114621522577"></a><a name="p114621522577"></a>Monitored object: database</p>
<p id="p144621722977"><a name="p144621722977"></a><a name="p144621722977"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row26656221475"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p94622221577"><a name="p94622221577"></a><a name="p94622221577"></a>mongo009_migFail_num</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p9462112215713"><a name="p9462112215713"></a><a name="p9462112215713"></a>Chunk Migration Failures in Last 24 hrs</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p164626221071"><a name="p164626221071"></a><a name="p164626221071"></a>Number of chunk migration failures in the last 24 hours</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p204623224719"><a name="p204623224719"></a><a name="p204623224719"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1946282214715"><a name="p1946282214715"></a><a name="p1946282214715"></a>Monitored object: database</p>
<p id="p846282210719"><a name="p846282210719"></a><a name="p846282210719"></a>Monitored instance type: DDS DB instance</p>
</td>
</tr>
<tr id="row9664182214719"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p12464222971"><a name="p12464222971"></a><a name="p12464222971"></a>mongo007_connections</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p104641922474"><a name="p104641922474"></a><a name="p104641922474"></a>Current Active Connections</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p10464182215719"><a name="p10464182215719"></a><a name="p10464182215719"></a>Total number of connections attempting to connect to DDS DB instance nodes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p2046472212716"><a name="p2046472212716"></a><a name="p2046472212716"></a>0-200 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1746472213716"><a name="p1746472213716"></a><a name="p1746472213716"></a>Monitored object: database</p>
<p id="p55050233392"><a name="p55050233392"></a><a name="p55050233392"></a>Monitored instance type:</p>
<a name="ul14281152663915"></a><a name="ul14281152663915"></a><ul id="ul14281152663915"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row116644229718"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p194644221873"><a name="p194644221873"></a><a name="p194644221873"></a>mongo008_mem_resident</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p18464922571"><a name="p18464922571"></a><a name="p18464922571"></a>Resident Memory</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p104653226719"><a name="p104653226719"></a><a name="p104653226719"></a>Size of resident memory in MB</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p24651422275"><a name="p24651422275"></a><a name="p24651422275"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p44651229713"><a name="p44651229713"></a><a name="p44651229713"></a>Monitored object: database</p>
<p id="p1538714509391"><a name="p1538714509391"></a><a name="p1538714509391"></a>Monitored instance type:</p>
<a name="ul111553103914"></a><a name="ul111553103914"></a><ul id="ul111553103914"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row5664522874"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p104652221073"><a name="p104652221073"></a><a name="p104652221073"></a>mongo009_mem_virtual</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p13465172213714"><a name="p13465172213714"></a><a name="p13465172213714"></a>Virtual Memory</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p8465422379"><a name="p8465422379"></a><a name="p8465422379"></a>Size of virtual memory in MB</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p7465142218720"><a name="p7465142218720"></a><a name="p7465142218720"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p16465122217710"><a name="p16465122217710"></a><a name="p16465122217710"></a>Monitored object: database</p>
<p id="p2597144718516"><a name="p2597144718516"></a><a name="p2597144718516"></a>Monitored instance type:</p>
<a name="ul101861448453"></a><a name="ul101861448453"></a><ul id="ul101861448453"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1766382220715"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1946510221476"><a name="p1946510221476"></a><a name="p1946510221476"></a>mongo010_regular_asserts_ps</p>
<p id="p164651221775"><a name="p164651221775"></a><a name="p164651221775"></a></p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p246510221576"><a name="p246510221576"></a><a name="p246510221576"></a>Regular Asserts per Second</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p14465112215715"><a name="p14465112215715"></a><a name="p14465112215715"></a>Number of regular asserts per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p1346552218716"><a name="p1346552218716"></a><a name="p1346552218716"></a>≥ 0 asserts/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p11465152213716"><a name="p11465152213716"></a><a name="p11465152213716"></a>Monitored object: database</p>
<p id="p723311569393"><a name="p723311569393"></a><a name="p723311569393"></a>Monitored instance type:</p>
<a name="ul068345815393"></a><a name="ul068345815393"></a><ul id="ul068345815393"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1566372212716"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p16465192211710"><a name="p16465192211710"></a><a name="p16465192211710"></a>mongo011_warning_asserts_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p114658223720"><a name="p114658223720"></a><a name="p114658223720"></a>Warning Asserts per Second</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p7465152210716"><a name="p7465152210716"></a><a name="p7465152210716"></a>Number of warning asserts per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p17466322478"><a name="p17466322478"></a><a name="p17466322478"></a>≥ 0 asserts/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p346682218714"><a name="p346682218714"></a><a name="p346682218714"></a>Monitored object: database</p>
<p id="p192071415174017"><a name="p192071415174017"></a><a name="p192071415174017"></a>Monitored instance type:</p>
<a name="ul84803191408"></a><a name="ul84803191408"></a><ul id="ul84803191408"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row15663172217711"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p546692210713"><a name="p546692210713"></a><a name="p546692210713"></a>mongo012_msg_asserts_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p15466142214715"><a name="p15466142214715"></a><a name="p15466142214715"></a>Message Asserts per Second</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p146615223718"><a name="p146615223718"></a><a name="p146615223718"></a>Number of message asserts per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p995812811151"><a name="p995812811151"></a><a name="p995812811151"></a>≥ 0 asserts/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p64671022477"><a name="p64671022477"></a><a name="p64671022477"></a>Monitored object: database</p>
<p id="p28323299400"><a name="p28323299400"></a><a name="p28323299400"></a>Monitored instance type:</p>
<a name="ul165411932104016"></a><a name="ul165411932104016"></a><ul id="ul165411932104016"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row166322211711"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p204678223717"><a name="p204678223717"></a><a name="p204678223717"></a>mongo013_user_asserts_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1946702211718"><a name="p1946702211718"></a><a name="p1946702211718"></a>User Asserts per Second</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p846742210710"><a name="p846742210710"></a><a name="p846742210710"></a>Number of user asserts per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p1646717221474"><a name="p1646717221474"></a><a name="p1646717221474"></a>≥ 0 asserts/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p546742216711"><a name="p546742216711"></a><a name="p546742216711"></a>Monitored object: database</p>
<p id="p178953919408"><a name="p178953919408"></a><a name="p178953919408"></a>Monitored instance type:</p>
<a name="ul68441041144013"></a><a name="ul68441041144013"></a><ul id="ul68441041144013"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row96639227712"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p0467162217714"><a name="p0467162217714"></a><a name="p0467162217714"></a>mongo031_cpu_usage</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p134676226713"><a name="p134676226713"></a><a name="p134676226713"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p746842214713"><a name="p746842214713"></a><a name="p746842214713"></a>CPU usage of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p1546812222079"><a name="p1546812222079"></a><a name="p1546812222079"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p947118221278"><a name="p947118221278"></a><a name="p947118221278"></a>Monitored object: ECS</p>
<p id="p56621213154116"><a name="p56621213154116"></a><a name="p56621213154116"></a>Monitored instance type:</p>
<a name="ul118757155417"></a><a name="ul118757155417"></a><ul id="ul118757155417"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row5662182220719"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1847110221276"><a name="p1847110221276"></a><a name="p1847110221276"></a>mongo032_mem_usage</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p147115221177"><a name="p147115221177"></a><a name="p147115221177"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p104712223713"><a name="p104712223713"></a><a name="p104712223713"></a>Memory usage of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p147152217715"><a name="p147152217715"></a><a name="p147152217715"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p74717228713"><a name="p74717228713"></a><a name="p74717228713"></a>Monitored object: ECS</p>
<p id="p7872141744116"><a name="p7872141744116"></a><a name="p7872141744116"></a>Monitored instance type:</p>
<a name="ul3992191984119"></a><a name="ul3992191984119"></a><ul id="ul3992191984119"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row14662192210712"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1147142213711"><a name="p1147142213711"></a><a name="p1147142213711"></a>mongo033_bytes_out</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1647162219710"><a name="p1647162219710"></a><a name="p1647162219710"></a>Network Output Throughput</p>
<p id="p194711822976"><a name="p194711822976"></a><a name="p194711822976"></a></p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p12471102213716"><a name="p12471102213716"></a><a name="p12471102213716"></a>Outgoing traffic in bytes per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p104716222076"><a name="p104716222076"></a><a name="p104716222076"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p15472162220711"><a name="p15472162220711"></a><a name="p15472162220711"></a>Monitored object: ECS</p>
<p id="p47591022164114"><a name="p47591022164114"></a><a name="p47591022164114"></a>Monitored instance type:</p>
<a name="ul85878254416"></a><a name="ul85878254416"></a><ul id="ul85878254416"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row116627227714"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p0472102214720"><a name="p0472102214720"></a><a name="p0472102214720"></a>mongo034_bytes_in</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p18472022075"><a name="p18472022075"></a><a name="p18472022075"></a>Network Input Throughput</p>
<p id="p6472112215711"><a name="p6472112215711"></a><a name="p6472112215711"></a></p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p9472142210712"><a name="p9472142210712"></a><a name="p9472142210712"></a>Incoming traffic in bytes per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p847216225713"><a name="p847216225713"></a><a name="p847216225713"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p134724226717"><a name="p134724226717"></a><a name="p134724226717"></a>Monitored object: ECS</p>
<p id="p92362819411"><a name="p92362819411"></a><a name="p92362819411"></a>Monitored instance type:</p>
<a name="ul346613307416"></a><a name="ul346613307416"></a><ul id="ul346613307416"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row56628223712"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1147220225711"><a name="p1147220225711"></a><a name="p1147220225711"></a>mongo014_queues_total</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1147272213717"><a name="p1147272213717"></a><a name="p1147272213717"></a>Number of Operations Queued Waiting for the Lock</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p10472122215710"><a name="p10472122215710"></a><a name="p10472122215710"></a>Number of operations queued waiting for the lock</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p19472162214720"><a name="p19472162214720"></a><a name="p19472162214720"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p16472142215718"><a name="p16472142215718"></a><a name="p16472142215718"></a>Monitored object: database</p>
<p id="p169301148204315"><a name="p169301148204315"></a><a name="p169301148204315"></a>Monitored instance type:</p>
<a name="ul2437105211437"></a><a name="ul2437105211437"></a><ul id="ul2437105211437"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row106619222715"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p104722022770"><a name="p104722022770"></a><a name="p104722022770"></a>mongo015_queues_readers</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1847213229711"><a name="p1847213229711"></a><a name="p1847213229711"></a>Number of Operations Queued Waiting for the Read Lock</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p44728221774"><a name="p44728221774"></a><a name="p44728221774"></a>Number of operations queued waiting for the read lock</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p247272217711"><a name="p247272217711"></a><a name="p247272217711"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p13472142214718"><a name="p13472142214718"></a><a name="p13472142214718"></a>Monitored object: database</p>
<p id="p4472222973"><a name="p4472222973"></a><a name="p4472222973"></a>Monitored instance type:</p>
<a name="ul183794577433"></a><a name="ul183794577433"></a><ul id="ul183794577433"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1566113221714"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p7472022374"><a name="p7472022374"></a><a name="p7472022374"></a>mongo016_queues_writers</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1647212221677"><a name="p1647212221677"></a><a name="p1647212221677"></a>Number of Operations Queued Waiting for the Write Lock</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p1047219221879"><a name="p1047219221879"></a><a name="p1047219221879"></a>Number of operations queued waiting for the write lock</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p74726221974"><a name="p74726221974"></a><a name="p74726221974"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p047282217719"><a name="p047282217719"></a><a name="p047282217719"></a>Monitored object: database</p>
<p id="p94721522776"><a name="p94721522776"></a><a name="p94721522776"></a>Monitored instance type:</p>
<a name="ul153923634420"></a><a name="ul153923634420"></a><ul id="ul153923634420"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row176612222714"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1147252211718"><a name="p1147252211718"></a><a name="p1147252211718"></a>mongo017_page_faults</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1472172213714"><a name="p1472172213714"></a><a name="p1472172213714"></a>Number of Page Faults</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p74725221275"><a name="p74725221275"></a><a name="p74725221275"></a>Number of page faults on the monitored nodes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p14733221875"><a name="p14733221875"></a><a name="p14733221875"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p14473522873"><a name="p14473522873"></a><a name="p14473522873"></a>Monitored object: database</p>
<p id="p1447310228715"><a name="p1447310228715"></a><a name="p1447310228715"></a>Monitored instance type:</p>
<a name="ul1886610934412"></a><a name="ul1886610934412"></a><ul id="ul1886610934412"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row13660172210712"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p34736221173"><a name="p34736221173"></a><a name="p34736221173"></a>mongo018_porfling_num</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p24734221972"><a name="p24734221972"></a><a name="p24734221972"></a>Number of Slow Queries</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p24731221714"><a name="p24731221714"></a><a name="p24731221714"></a>Number of slow queries on the monitored nodes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p7473422176"><a name="p7473422176"></a><a name="p7473422176"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p204735221079"><a name="p204735221079"></a><a name="p204735221079"></a>Monitored object: database</p>
<p id="p74730221072"><a name="p74730221072"></a><a name="p74730221072"></a>Monitored instance type:</p>
<a name="ul14199151312442"></a><a name="ul14199151312442"></a><ul id="ul14199151312442"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row66604221374"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p124736221378"><a name="p124736221378"></a><a name="p124736221378"></a>mongo019_cursors_open</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p114735225715"><a name="p114735225715"></a><a name="p114735225715"></a>Number of Current Maintained Cursors</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p14473522374"><a name="p14473522374"></a><a name="p14473522374"></a>Number of maintained cursors on the monitored nodes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p1347332218712"><a name="p1347332218712"></a><a name="p1347332218712"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p64737221874"><a name="p64737221874"></a><a name="p64737221874"></a>Monitored object: database</p>
<p id="p124739224715"><a name="p124739224715"></a><a name="p124739224715"></a>Monitored instance type:</p>
<a name="ul169541616144414"></a><a name="ul169541616144414"></a><ul id="ul169541616144414"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1766022211717"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1747482214719"><a name="p1747482214719"></a><a name="p1747482214719"></a>mongo020_cursors_timeOut</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p947420221714"><a name="p947420221714"></a><a name="p947420221714"></a>Number of Timed Out Cursors</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p94749220718"><a name="p94749220718"></a><a name="p94749220718"></a>Number of timed out cursors on the monitored nodes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p5474132213713"><a name="p5474132213713"></a><a name="p5474132213713"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p147413221076"><a name="p147413221076"></a><a name="p147413221076"></a>Monitored object: database</p>
<p id="p84741422171"><a name="p84741422171"></a><a name="p84741422171"></a>Monitored instance type:</p>
<a name="ul14582122018448"></a><a name="ul14582122018448"></a><ul id="ul14582122018448"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row156591322671"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1947415221572"><a name="p1947415221572"></a><a name="p1947415221572"></a>mongo021_wt_cahe_usage</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p124741221575"><a name="p124741221575"></a><a name="p124741221575"></a>Bytes in Cache When Using WiredTiger</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p114748221712"><a name="p114748221712"></a><a name="p114748221712"></a>Size of data in cache in MB when WiredTiger is used</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p19474622973"><a name="p19474622973"></a><a name="p19474622973"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p34747221678"><a name="p34747221678"></a><a name="p34747221678"></a>Monitored object: database</p>
<p id="p1347432213710"><a name="p1347432213710"></a><a name="p1347432213710"></a>Monitored instance type:</p>
<a name="ul247372517445"></a><a name="ul247372517445"></a><ul id="ul247372517445"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row6659422676"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p11474422572"><a name="p11474422572"></a><a name="p11474422572"></a>mongo022_wt_cahe_dirty</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1447418221577"><a name="p1447418221577"></a><a name="p1447418221577"></a>Tracked Dirty Bytes in Cache When Using WiredTiger</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p6474182212713"><a name="p6474182212713"></a><a name="p6474182212713"></a>Size of dirty data in cache in MB when WiredTiger is used</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p20475622177"><a name="p20475622177"></a><a name="p20475622177"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p147518222714"><a name="p147518222714"></a><a name="p147518222714"></a>Monitored object: database</p>
<p id="p16475222873"><a name="p16475222873"></a><a name="p16475222873"></a>Monitored instance type:</p>
<a name="ul962392913442"></a><a name="ul962392913442"></a><ul id="ul962392913442"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row26580221579"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p114751322476"><a name="p114751322476"></a><a name="p114751322476"></a>mongo023_wInto_wtCache</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p947518224716"><a name="p947518224716"></a><a name="p947518224716"></a>Bytes Written into WiredTiger Cache per Second</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p447562219720"><a name="p447562219720"></a><a name="p447562219720"></a>Bytes written into WiredTiger cache per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p247519221575"><a name="p247519221575"></a><a name="p247519221575"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p5475142213711"><a name="p5475142213711"></a><a name="p5475142213711"></a>Monitored object: database</p>
<p id="p147517221879"><a name="p147517221879"></a><a name="p147517221879"></a>Monitored instance type:</p>
<a name="ul831863354420"></a><a name="ul831863354420"></a><ul id="ul831863354420"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row36582221717"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p14475112219717"><a name="p14475112219717"></a><a name="p14475112219717"></a>mongo024_wFrom_wtCache</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p847582215714"><a name="p847582215714"></a><a name="p847582215714"></a>Bytes Written into Disks from WiredTiger Cache per Second</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p12475172213717"><a name="p12475172213717"></a><a name="p12475172213717"></a>Bytes written into disks from WiredTiger cache per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p147542219710"><a name="p147542219710"></a><a name="p147542219710"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p10476132217719"><a name="p10476132217719"></a><a name="p10476132217719"></a>Monitored object: database</p>
<p id="p1947632219719"><a name="p1947632219719"></a><a name="p1947632219719"></a>Monitored instance type:</p>
<a name="ul24069373449"></a><a name="ul24069373449"></a><ul id="ul24069373449"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1465817221476"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p104761022170"><a name="p104761022170"></a><a name="p104761022170"></a>mongo025_repl_oplog_win</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1247614221178"><a name="p1247614221178"></a><a name="p1247614221178"></a>Oplog Available Time on Primary Node</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p12476122212711"><a name="p12476122212711"></a><a name="p12476122212711"></a>Oplog available time in hours on the monitored primary node</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p347616221577"><a name="p347616221577"></a><a name="p347616221577"></a>≥ 0 Hours</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p144766221673"><a name="p144766221673"></a><a name="p144766221673"></a>Monitored object: database</p>
<p id="p1847611220710"><a name="p1847611220710"></a><a name="p1847611220710"></a>Monitored instance type: primary node</p>
</td>
</tr>
<tr id="row1265722214717"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1947611221277"><a name="p1947611221277"></a><a name="p1947611221277"></a>mongo026_oplog_size_ph</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p134762221271"><a name="p134762221271"></a><a name="p134762221271"></a>Oplog Generation Speed on Primary Node</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p2047692215714"><a name="p2047692215714"></a><a name="p2047692215714"></a>Speed in MB/hour at which Oplog is generated on the monitored primary node</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p16476522278"><a name="p16476522278"></a><a name="p16476522278"></a>≥ 0 MB/Hour</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p194765221573"><a name="p194765221573"></a><a name="p194765221573"></a>Monitored object: database</p>
<p id="p147615221174"><a name="p147615221174"></a><a name="p147615221174"></a>Monitored instance type: primary node</p>
</td>
</tr>
<tr id="row46542222079"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p184789228718"><a name="p184789228718"></a><a name="p184789228718"></a>mongo035_disk_usage</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p12478192210718"><a name="p12478192210718"></a><a name="p12478192210718"></a>Disk Utilization</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p184781722976"><a name="p184781722976"></a><a name="p184781722976"></a>Disk usage of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p1747811221975"><a name="p1747811221975"></a><a name="p1747811221975"></a>0-1</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p154791922475"><a name="p154791922475"></a><a name="p154791922475"></a>Monitored object: ECS</p>
<p id="p412416333469"><a name="p412416333469"></a><a name="p412416333469"></a>Monitored instance type:</p>
<a name="ul46159369469"></a><a name="ul46159369469"></a><ul id="ul46159369469"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row196541221878"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p134791022671"><a name="p134791022671"></a><a name="p134791022671"></a>mongo036_iops</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p947915229716"><a name="p947915229716"></a><a name="p947915229716"></a>IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p14479162212716"><a name="p14479162212716"></a><a name="p14479162212716"></a>Average number of I/O requests processed by the system per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p2479922372"><a name="p2479922372"></a><a name="p2479922372"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p124791225719"><a name="p124791225719"></a><a name="p124791225719"></a>Monitored object: ECS</p>
<p id="p94798227710"><a name="p94798227710"></a><a name="p94798227710"></a>Monitored instance type:</p>
<a name="ul12970163815462"></a><a name="ul12970163815462"></a><ul id="ul12970163815462"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row19654022675"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p134791221774"><a name="p134791221774"></a><a name="p134791221774"></a>mongo037_read_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p144791722478"><a name="p144791722478"></a><a name="p144791722478"></a>Disk Read Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p24791222374"><a name="p24791222374"></a><a name="p24791222374"></a>Average number of read bytes per second for disks</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p647962215710"><a name="p647962215710"></a><a name="p647962215710"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p147922211719"><a name="p147922211719"></a><a name="p147922211719"></a>Monitored object: ECS</p>
<p id="p1747913221720"><a name="p1747913221720"></a><a name="p1747913221720"></a>Monitored instance type:</p>
<a name="ul192682504466"></a><a name="ul192682504466"></a><ul id="ul192682504466"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row4653722978"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p74791122978"><a name="p74791122978"></a><a name="p74791122978"></a>mongo038_write_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p247962218711"><a name="p247962218711"></a><a name="p247962218711"></a>Disk Read Throughput</p>
<p id="p1747920221374"><a name="p1747920221374"></a><a name="p1747920221374"></a></p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p947919225717"><a name="p947919225717"></a><a name="p947919225717"></a>Average number of write bytes per second for disks</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p0479142220710"><a name="p0479142220710"></a><a name="p0479142220710"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1648016227710"><a name="p1648016227710"></a><a name="p1648016227710"></a>Monitored object: ECS</p>
<p id="p154807221714"><a name="p154807221714"></a><a name="p154807221714"></a>Monitored instance type:</p>
<a name="ul18271753104611"></a><a name="ul18271753104611"></a><ul id="ul18271753104611"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row665242219716"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p948019221876"><a name="p948019221876"></a><a name="p948019221876"></a>mongo039_avg_disk_sec_per_read</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1548020226712"><a name="p1548020226712"></a><a name="p1548020226712"></a>Average Time per Disk Read</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p174802022675"><a name="p174802022675"></a><a name="p174802022675"></a>Average time per disk read operation during a specified period</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p1548011221175"><a name="p1548011221175"></a><a name="p1548011221175"></a>≥ 0 Seconds</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1248052214719"><a name="p1248052214719"></a><a name="p1248052214719"></a>Monitored object: ECS</p>
<p id="p1648012221178"><a name="p1648012221178"></a><a name="p1648012221178"></a>Monitored instance type:</p>
<a name="ul1994145694611"></a><a name="ul1994145694611"></a><ul id="ul1994145694611"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row665215221713"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p24801227719"><a name="p24801227719"></a><a name="p24801227719"></a>mongo040_avg_disk_sec_per_write</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p184807221870"><a name="p184807221870"></a><a name="p184807221870"></a>Average Time per Disk Write</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p1248012215717"><a name="p1248012215717"></a><a name="p1248012215717"></a>Average time per disk write operation during a specified period</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p1148018221678"><a name="p1148018221678"></a><a name="p1148018221678"></a>≥ 0 Seconds</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1648014226710"><a name="p1648014226710"></a><a name="p1648014226710"></a>Monitored object: ECS</p>
<p id="p1048011221718"><a name="p1048011221718"></a><a name="p1048011221718"></a>Monitored instance type:</p>
<a name="ul98563012475"></a><a name="ul98563012475"></a><ul id="ul98563012475"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row86522022774"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p448010226713"><a name="p448010226713"></a><a name="p448010226713"></a>mongo041_avg_disk_queue_length</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p5480152210715"><a name="p5480152210715"></a><a name="p5480152210715"></a>Average Disk Queue Length</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p5480722779"><a name="p5480722779"></a><a name="p5480722779"></a>Number of processes waiting to be written to the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p1348042210710"><a name="p1348042210710"></a><a name="p1348042210710"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p74801222570"><a name="p74801222570"></a><a name="p74801222570"></a>Monitored object: ECS</p>
<p id="p8480122219717"><a name="p8480122219717"></a><a name="p8480122219717"></a>Monitored instance type:</p>
<a name="ul36026411471"></a><a name="ul36026411471"></a><ul id="ul36026411471"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row3651132214718"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p184804226716"><a name="p184804226716"></a><a name="p184804226716"></a>mongo042_disk_total_size</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p6480152218718"><a name="p6480152218718"></a><a name="p6480152218718"></a>Total Disk Size</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p11480122212710"><a name="p11480122212710"></a><a name="p11480122212710"></a>Total disk size of the monitored object in GB</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p348011221674"><a name="p348011221674"></a><a name="p348011221674"></a>0–1000 GB</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1348072210715"><a name="p1348072210715"></a><a name="p1348072210715"></a>Monitored object: ECS</p>
<p id="p1148018229719"><a name="p1148018229719"></a><a name="p1148018229719"></a>Monitored instance type:</p>
<a name="ul0721106174713"></a><a name="ul0721106174713"></a><ul id="ul0721106174713"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1665112217712"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p348013226711"><a name="p348013226711"></a><a name="p348013226711"></a>mongo043_disk_used_size</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p9480722579"><a name="p9480722579"></a><a name="p9480722579"></a>Disk Usage</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p18480122372"><a name="p18480122372"></a><a name="p18480122372"></a>Total size of the disk usage of the monitored object in GB</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p54811221716"><a name="p54811221716"></a><a name="p54811221716"></a>0–1000 GB</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1748192213718"><a name="p1748192213718"></a><a name="p1748192213718"></a>Monitored object: ECS</p>
<p id="p24812221271"><a name="p24812221271"></a><a name="p24812221271"></a>Monitored instance type:</p>
<a name="ul13868395477"></a><a name="ul13868395477"></a><ul id="ul13868395477"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row12626307124"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p647610220714"><a name="p647610220714"></a><a name="p647610220714"></a>mongo025_repl_headroom</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p114763221074"><a name="p114763221074"></a><a name="p114763221074"></a>Oplog Overlapping Time Between Primary and Secondary Nodes</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p164761322574"><a name="p164761322574"></a><a name="p164761322574"></a>Oplog overlapping time in seconds between the primary and secondary nodes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p6476322772"><a name="p6476322772"></a><a name="p6476322772"></a>≥ 0 Seconds</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1247615222720"><a name="p1247615222720"></a><a name="p1247615222720"></a>Monitored object: database</p>
<p id="p184761622579"><a name="p184761622579"></a><a name="p184761622579"></a>Monitored instance type: secondary node</p>
</td>
</tr>
<tr id="row5610307120"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1047716221716"><a name="p1047716221716"></a><a name="p1047716221716"></a>mongo026_repl_lag</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p14477822177"><a name="p14477822177"></a><a name="p14477822177"></a>Delay Between Primary and Secondary Nodes</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p194773222718"><a name="p194773222718"></a><a name="p194773222718"></a>Replication delay between the primary and secondary nodes in seconds</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p15477122171"><a name="p15477122171"></a><a name="p15477122171"></a>≥ 0 Seconds</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1447792212711"><a name="p1447792212711"></a><a name="p1447792212711"></a>Monitored object: database</p>
<p id="p1547710224710"><a name="p1547710224710"></a><a name="p1547710224710"></a>Monitored instance type: secondary node</p>
</td>
</tr>
<tr id="row176018309126"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p1247712213715"><a name="p1247712213715"></a><a name="p1247712213715"></a>mongo027_repl_command_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p1147716221674"><a name="p1147716221674"></a><a name="p1147716221674"></a>Command Operations per Second for Secondary Node Replication</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p84774221178"><a name="p84774221178"></a><a name="p84774221178"></a>Average number of the command statement execution times for secondary node replication per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p1447720221772"><a name="p1447720221772"></a><a name="p1447720221772"></a>≥ 0</p>
<p id="p1647716221875"><a name="p1647716221875"></a><a name="p1647716221875"></a>commands/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1247711221876"><a name="p1247711221876"></a><a name="p1247711221876"></a>Monitored object: database</p>
<p id="p8477162216710"><a name="p8477162216710"></a><a name="p8477162216710"></a>Monitored instance type: secondary node</p>
</td>
</tr>
<tr id="row0591130201219"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p19477162210715"><a name="p19477162210715"></a><a name="p19477162210715"></a>mongo028_repl_update_ps</p>
<p id="p19477202214717"><a name="p19477202214717"></a><a name="p19477202214717"></a></p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p104771221577"><a name="p104771221577"></a><a name="p104771221577"></a>Update Operations per Second for Secondary Node Replication</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p147710226715"><a name="p147710226715"></a><a name="p147710226715"></a>Average number of the update statement execution times for secondary node replication per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p947712221379"><a name="p947712221379"></a><a name="p947712221379"></a>≥ 0</p>
<p id="p11478112216714"><a name="p11478112216714"></a><a name="p11478112216714"></a>executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p747817222710"><a name="p747817222710"></a><a name="p747817222710"></a>Monitored object: database</p>
<p id="p15478122270"><a name="p15478122270"></a><a name="p15478122270"></a>Monitored instance type: secondary node</p>
</td>
</tr>
<tr id="row159930101218"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p154781422778"><a name="p154781422778"></a><a name="p154781422778"></a>mongo029_repl_delete_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p347814222713"><a name="p347814222713"></a><a name="p347814222713"></a>Delete Operations per Second for Secondary Node Replication</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p64785228715"><a name="p64785228715"></a><a name="p64785228715"></a>Average number of the delete statement execution times for secondary node replication per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p194784222712"><a name="p194784222712"></a><a name="p194784222712"></a>≥ 0</p>
<p id="p194787229713"><a name="p194787229713"></a><a name="p194787229713"></a>executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p7478102212710"><a name="p7478102212710"></a><a name="p7478102212710"></a>Monitored object: database</p>
<p id="p13478132220712"><a name="p13478132220712"></a><a name="p13478132220712"></a>Monitored instance type: secondary node</p>
</td>
</tr>
<tr id="row195716300123"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p147802211719"><a name="p147802211719"></a><a name="p147802211719"></a>mongo030_repl_insert_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.6.1.2 "><p id="p24781722279"><a name="p24781722279"></a><a name="p24781722279"></a>Insert Operations per Second for Secondary Node Replication</p>
</td>
<td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.1.6.1.3 "><p id="p9478922875"><a name="p9478922875"></a><a name="p9478922875"></a>Average number of the insert statement execution times for secondary node replication per second</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.4 "><p id="p647816228715"><a name="p647816228715"></a><a name="p647816228715"></a>≥ 0</p>
<p id="p17478192216715"><a name="p17478192216715"></a><a name="p17478192216715"></a>executions/s</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p6478102211719"><a name="p6478102211719"></a><a name="p6478102211719"></a>Monitored object: database</p>
<p id="p447814221378"><a name="p447814221378"></a><a name="p447814221378"></a>Monitored instance type: secondary node</p>
</td>
</tr>
</tbody>
</table>

## **Dimension**<a name="section45895235153251"></a>

<a name="table26526577153251"></a>
<table><thead align="left"><tr id="row46969777153251"><th class="cellrowborder" valign="top" width="40.400000000000006%" id="mcps1.1.3.1.1"><p id="p46455583153251"><a name="p46455583153251"></a><a name="p46455583153251"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="59.599999999999994%" id="mcps1.1.3.1.2"><p id="p4805882153251"><a name="p4805882153251"></a><a name="p4805882153251"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row768992811619"><td class="cellrowborder" valign="top" width="40.400000000000006%" headers="mcps1.1.3.1.1 "><p id="p267914281617"><a name="p267914281617"></a><a name="p267914281617"></a>mongodb_cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.1.3.1.2 "><p id="p156791928264"><a name="p156791928264"></a><a name="p156791928264"></a>DDS DB instance ID</p>
</td>
</tr>
<tr id="row166894287616"><td class="cellrowborder" valign="top" width="40.400000000000006%" headers="mcps1.1.3.1.1 "><p id="p66791928161"><a name="p66791928161"></a><a name="p66791928161"></a>mongos_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.1.3.1.2 "><p id="p186791428467"><a name="p186791428467"></a><a name="p186791428467"></a>mongos node ID</p>
</td>
</tr>
<tr id="row468932820618"><td class="cellrowborder" valign="top" width="40.400000000000006%" headers="mcps1.1.3.1.1 "><p id="p1367914285617"><a name="p1367914285617"></a><a name="p1367914285617"></a>mongod_primary_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.1.3.1.2 "><p id="p13679102814616"><a name="p13679102814616"></a><a name="p13679102814616"></a>Primary node ID</p>
</td>
</tr>
<tr id="row168782818613"><td class="cellrowborder" valign="top" width="40.400000000000006%" headers="mcps1.1.3.1.1 "><p id="p167911288618"><a name="p167911288618"></a><a name="p167911288618"></a>mongod_secondary_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.1.3.1.2 "><p id="p3679028961"><a name="p3679028961"></a><a name="p3679028961"></a>Secondary node ID</p>
</td>
</tr>
</tbody>
</table>

