# DDS Metrics<a name="dds_metrics"></a>

## Function<a name="section59820001153251"></a>

This section describes metrics reported by Document Database Service \(DDS\) to Cloud Eye as well as their namespaces and dimensions. You can use APIs provided by Cloud Eye to query the metrics of the monitored object and alarms generated for DDS.

## Namespace<a name="section55128484153251"></a>

SYS.DDS

## Monitoring Metrics<a name="section57564324153251"></a>

<a name="table32198700153251"></a>
<table><thead align="left"><tr id="row43554686153251"><th class="cellrowborder" valign="top" width="13.717171717171716%" id="mcps1.1.6.1.1"><p id="p38268712153251"><a name="p38268712153251"></a><a name="p38268712153251"></a><strong id="b842352706112935"><a name="b842352706112935"></a><a name="b842352706112935"></a>Metrics</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.606060606060606%" id="mcps1.1.6.1.2"><p id="p12757995153251"><a name="p12757995153251"></a><a name="p12757995153251"></a><strong id="b842352706112940"><a name="b842352706112940"></a><a name="b842352706112940"></a>Metrics Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35.58585858585858%" id="mcps1.1.6.1.3"><p id="p26764654153251"><a name="p26764654153251"></a><a name="p26764654153251"></a><strong id="b842352706112944"><a name="b842352706112944"></a><a name="b842352706112944"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.15151515151515%" id="mcps1.1.6.1.4"><p id="p20453337153251"><a name="p20453337153251"></a><a name="p20453337153251"></a><strong id="b842352706112947"><a name="b842352706112947"></a><a name="b842352706112947"></a>Value Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.939393939393938%" id="mcps1.1.6.1.5"><p id="p46107605153251"><a name="p46107605153251"></a><a name="p46107605153251"></a><strong id="b842352706112951"><a name="b842352706112951"></a><a name="b842352706112951"></a>Remarks</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1671192211720"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1945442218710"><a name="p1945442218710"></a><a name="p1945442218710"></a>mongo001_command_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p204541822072"><a name="p204541822072"></a><a name="p204541822072"></a>COMMAND Statements per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p7454192214710"><a name="p7454192214710"></a><a name="p7454192214710"></a>Number of COMMAND statements executed per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p136515555163"><a name="p136515555163"></a><a name="p136515555163"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p154551322677"><a name="p154551322677"></a><a name="p154551322677"></a>Monitored object: database</p>
<p id="p339352616263"><a name="p339352616263"></a><a name="p339352616263"></a>Monitored object type:</p>
<a name="ul1978618331265"></a><a name="ul1978618331265"></a><ul id="ul1978618331265"><li>DDS DB instance</li><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row867172217718"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1645512214717"><a name="p1645512214717"></a><a name="p1645512214717"></a>mongo002_delete_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p6455202210718"><a name="p6455202210718"></a><a name="p6455202210718"></a>DELETE Statements per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p1455132215714"><a name="p1455132215714"></a><a name="p1455132215714"></a>Number of DELETE statements executed per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p171165561614"><a name="p171165561614"></a><a name="p171165561614"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p1645515221374"><a name="p1645515221374"></a><a name="p1645515221374"></a>Monitored object: database</p>
<p id="p145582210716"><a name="p145582210716"></a><a name="p145582210716"></a>Monitored object type:</p>
<a name="ul265514219262"></a><a name="ul265514219262"></a><ul id="ul265514219262"><li>DDS DB instance</li><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row2067014221779"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p184551222773"><a name="p184551222773"></a><a name="p184551222773"></a>mongo003_insert_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p13455822371"><a name="p13455822371"></a><a name="p13455822371"></a>INSERT Statements per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p11455622272"><a name="p11455622272"></a><a name="p11455622272"></a>Number of INSERT statements executed per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p98501751121620"><a name="p98501751121620"></a><a name="p98501751121620"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p14562221275"><a name="p14562221275"></a><a name="p14562221275"></a>Monitored object: database</p>
<p id="p1045616223710"><a name="p1045616223710"></a><a name="p1045616223710"></a>Monitored object type:</p>
<a name="ul7776924182718"></a><a name="ul7776924182718"></a><ul id="ul7776924182718"><li>DDS DB instance</li><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row966917227714"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p945612213713"><a name="p945612213713"></a><a name="p945612213713"></a>mongo004_query_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p44562022471"><a name="p44562022471"></a><a name="p44562022471"></a>QUERY Statements per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p1945622213718"><a name="p1945622213718"></a><a name="p1945622213718"></a>Number of QUERY statements executed per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p4856105191617"><a name="p4856105191617"></a><a name="p4856105191617"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p134563221375"><a name="p134563221375"></a><a name="p134563221375"></a>Monitored object: database</p>
<p id="p845613226713"><a name="p845613226713"></a><a name="p845613226713"></a>Monitored object type:</p>
<a name="ul1529182822711"></a><a name="ul1529182822711"></a><ul id="ul1529182822711"><li>DDS DB instance</li><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row766812229712"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p9456162217710"><a name="p9456162217710"></a><a name="p9456162217710"></a>mongo005_update_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p645642213718"><a name="p645642213718"></a><a name="p645642213718"></a>UPDATE Statements per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p1345620222719"><a name="p1345620222719"></a><a name="p1345620222719"></a>Number of UPDATE statements executed per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p108142465168"><a name="p108142465168"></a><a name="p108142465168"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p1445612214712"><a name="p1445612214712"></a><a name="p1445612214712"></a>Monitored object: database</p>
<p id="p645610221375"><a name="p645610221375"></a><a name="p645610221375"></a>Monitored object type:</p>
<a name="ul1432553322717"></a><a name="ul1432553322717"></a><ul id="ul1432553322717"><li>DDS DB instance</li><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1666819221174"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p245620223714"><a name="p245620223714"></a><a name="p245620223714"></a>mongo006_getmore_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p345662215714"><a name="p345662215714"></a><a name="p345662215714"></a>GETMORE Statements per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p545616221779"><a name="p545616221779"></a><a name="p545616221779"></a>Number of GETMORE statements executed per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p345622213716"><a name="p345622213716"></a><a name="p345622213716"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p14567221071"><a name="p14567221071"></a><a name="p14567221071"></a>Monitored object: database</p>
<p id="p1456102219713"><a name="p1456102219713"></a><a name="p1456102219713"></a>Monitored object type:</p>
<a name="ul1224917354276"></a><a name="ul1224917354276"></a><ul id="ul1224917354276"><li>DDS DB instance</li><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row966814221718"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p134561221173"><a name="p134561221173"></a><a name="p134561221173"></a>mongo007_chunk_num1</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p84571022675"><a name="p84571022675"></a><a name="p84571022675"></a>Chunks of Shard 1</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p2457132219718"><a name="p2457132219718"></a><a name="p2457132219718"></a>Number of chunks in shard 1</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p103841535171614"><a name="p103841535171614"></a><a name="p103841535171614"></a>0–64 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p13457422970"><a name="p13457422970"></a><a name="p13457422970"></a>Monitored object: database</p>
<p id="p74576221718"><a name="p74576221718"></a><a name="p74576221718"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row16681227710"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p845719221375"><a name="p845719221375"></a><a name="p845719221375"></a>mongo007_chunk_num2</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1145712213720"><a name="p1145712213720"></a><a name="p1145712213720"></a>Chunks of Shard 2</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p15457162215716"><a name="p15457162215716"></a><a name="p15457162215716"></a>Number of chunks in shard 2</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p143918354161"><a name="p143918354161"></a><a name="p143918354161"></a>0–64 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p6458122470"><a name="p6458122470"></a><a name="p6458122470"></a>Monitored object: database</p>
<p id="p1445816227711"><a name="p1445816227711"></a><a name="p1445816227711"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row1366715221072"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p9458192211711"><a name="p9458192211711"></a><a name="p9458192211711"></a>mongo007_chunk_num3</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p204581822171"><a name="p204581822171"></a><a name="p204581822171"></a>Chunks of Shard 3</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p1945872213717"><a name="p1945872213717"></a><a name="p1945872213717"></a>Number of chunks in shard 3</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p1445812222714"><a name="p1445812222714"></a><a name="p1445812222714"></a>0–64 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p645972213719"><a name="p645972213719"></a><a name="p645972213719"></a>Monitored object: database</p>
<p id="p74591227714"><a name="p74591227714"></a><a name="p74591227714"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row26677227715"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p745916222074"><a name="p745916222074"></a><a name="p745916222074"></a>mongo007_chunk_num4</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p145915221573"><a name="p145915221573"></a><a name="p145915221573"></a>Chunks of Shard 4</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p3459522178"><a name="p3459522178"></a><a name="p3459522178"></a>Number of chunks in shard 4</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p1645910221971"><a name="p1645910221971"></a><a name="p1645910221971"></a>0–64 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p1845918222718"><a name="p1845918222718"></a><a name="p1845918222718"></a>Monitored object: database</p>
<p id="p1446017221176"><a name="p1446017221176"></a><a name="p1446017221176"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row866732220710"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p18460112213716"><a name="p18460112213716"></a><a name="p18460112213716"></a>mongo007_chunk_num5</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p8460112215716"><a name="p8460112215716"></a><a name="p8460112215716"></a>Chunks of Shard 5</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p154601222470"><a name="p154601222470"></a><a name="p154601222470"></a>Number of chunks in shard 5</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p164605221173"><a name="p164605221173"></a><a name="p164605221173"></a>0–64 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p14460172220716"><a name="p14460172220716"></a><a name="p14460172220716"></a>Monitored object: database</p>
<p id="p1046014221672"><a name="p1046014221672"></a><a name="p1046014221672"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row196666221079"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1246016221575"><a name="p1246016221575"></a><a name="p1246016221575"></a>mongo007_chunk_num6</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1946016221978"><a name="p1946016221978"></a><a name="p1946016221978"></a>Chunks of Shard 6</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p11460522171"><a name="p11460522171"></a><a name="p11460522171"></a>Number of chunks in shard 6</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p134605223710"><a name="p134605223710"></a><a name="p134605223710"></a>0–64 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p94608226710"><a name="p94608226710"></a><a name="p94608226710"></a>Monitored object: database</p>
<p id="p1946012210710"><a name="p1946012210710"></a><a name="p1946012210710"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row166616223711"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1746082211717"><a name="p1746082211717"></a><a name="p1746082211717"></a>mongo007_chunk_num7</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p154609222719"><a name="p154609222719"></a><a name="p154609222719"></a>Chunks of Shard 7</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p3460222979"><a name="p3460222979"></a><a name="p3460222979"></a>Number of chunks in shard 7</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p194602221976"><a name="p194602221976"></a><a name="p194602221976"></a>0–64 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p04602223719"><a name="p04602223719"></a><a name="p04602223719"></a>Monitored object: database</p>
<p id="p746116221578"><a name="p746116221578"></a><a name="p746116221578"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row66665221715"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p134611422675"><a name="p134611422675"></a><a name="p134611422675"></a>mongo007_chunk_num8</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1946182211716"><a name="p1946182211716"></a><a name="p1946182211716"></a>Chunks of Shard 8</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p1146114222715"><a name="p1146114222715"></a><a name="p1146114222715"></a>Number of chunks in shard 8</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p94614224720"><a name="p94614224720"></a><a name="p94614224720"></a>0–64 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p144611222712"><a name="p144611222712"></a><a name="p144611222712"></a>Monitored object: database</p>
<p id="p446115221271"><a name="p446115221271"></a><a name="p446115221271"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row96661622673"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1246116221073"><a name="p1246116221073"></a><a name="p1246116221073"></a>mongo007_chunk_num9</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p12461202220711"><a name="p12461202220711"></a><a name="p12461202220711"></a>Chunks of Shard 9</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p746113221873"><a name="p746113221873"></a><a name="p746113221873"></a>Number of chunks in shard 9</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p14612227712"><a name="p14612227712"></a><a name="p14612227712"></a>0–64 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p24615222719"><a name="p24615222719"></a><a name="p24615222719"></a>Monitored object: database</p>
<p id="p7461182212715"><a name="p7461182212715"></a><a name="p7461182212715"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row8666422972"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p54614224713"><a name="p54614224713"></a><a name="p54614224713"></a>mongo007_chunk_num10</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1946119229712"><a name="p1946119229712"></a><a name="p1946119229712"></a>Chunks of Shard 10</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p134614221876"><a name="p134614221876"></a><a name="p134614221876"></a>Number of chunks in shard 10</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p846114221777"><a name="p846114221777"></a><a name="p846114221777"></a>0–64 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p134619226718"><a name="p134619226718"></a><a name="p134619226718"></a>Monitored object: database</p>
<p id="p84619221372"><a name="p84619221372"></a><a name="p84619221372"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row186661222774"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p164614221972"><a name="p164614221972"></a><a name="p164614221972"></a>mongo007_chunk_num11</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1046192211720"><a name="p1046192211720"></a><a name="p1046192211720"></a>Chunks of Shard 11</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p164615221771"><a name="p164615221771"></a><a name="p164615221771"></a>Number of chunks in shard 11</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p746111221575"><a name="p746111221575"></a><a name="p746111221575"></a>0–64 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p2046216223712"><a name="p2046216223712"></a><a name="p2046216223712"></a>Monitored object: database</p>
<p id="p246242215716"><a name="p246242215716"></a><a name="p246242215716"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row2665822979"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1146218222710"><a name="p1146218222710"></a><a name="p1146218222710"></a>mongo007_chunk_num12</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1346210221974"><a name="p1346210221974"></a><a name="p1346210221974"></a>Chunks of Shard 12</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p146202212720"><a name="p146202212720"></a><a name="p146202212720"></a>Number of chunks in shard 12</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p9462522278"><a name="p9462522278"></a><a name="p9462522278"></a>0–64 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p84621221872"><a name="p84621221872"></a><a name="p84621221872"></a>Monitored object: database</p>
<p id="p346218228714"><a name="p346218228714"></a><a name="p346218228714"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row26654223711"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1746219221074"><a name="p1746219221074"></a><a name="p1746219221074"></a>mongo008_connections</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p194621522171"><a name="p194621522171"></a><a name="p194621522171"></a>Active Instance Connections</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p846210221175"><a name="p846210221175"></a><a name="p846210221175"></a>Total number of connections attempting to connect to a DDS DB instance</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p18462202215716"><a name="p18462202215716"></a><a name="p18462202215716"></a>0–200 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p114621522577"><a name="p114621522577"></a><a name="p114621522577"></a>Monitored object: database</p>
<p id="p144621722977"><a name="p144621722977"></a><a name="p144621722977"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row26656221475"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p94622221577"><a name="p94622221577"></a><a name="p94622221577"></a>mongo009_migFail_num</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p9462112215713"><a name="p9462112215713"></a><a name="p9462112215713"></a>Chunk Migration Failures in Last 24 hrs</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p164626221071"><a name="p164626221071"></a><a name="p164626221071"></a>Number of chunk migration failures in the last 24 hours</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p204623224719"><a name="p204623224719"></a><a name="p204623224719"></a>≥ 0 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p1946282214715"><a name="p1946282214715"></a><a name="p1946282214715"></a>Monitored object: database</p>
<p id="p846282210719"><a name="p846282210719"></a><a name="p846282210719"></a>Monitored object type: DDS DB instance</p>
</td>
</tr>
<tr id="row9664182214719"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p12464222971"><a name="p12464222971"></a><a name="p12464222971"></a>mongo007_connections</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p104641922474"><a name="p104641922474"></a><a name="p104641922474"></a>Active Node Connections</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p10464182215719"><a name="p10464182215719"></a><a name="p10464182215719"></a>Total number of connections attempting to connect to a DDS DB instance node</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p2046472212716"><a name="p2046472212716"></a><a name="p2046472212716"></a>0–200 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p1746472213716"><a name="p1746472213716"></a><a name="p1746472213716"></a>Monitored object: database</p>
<p id="p1471622202813"><a name="p1471622202813"></a><a name="p1471622202813"></a>Monitored object type:</p>
<a name="ul844833732819"></a><a name="ul844833732819"></a><ul id="ul844833732819"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row116644229718"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p194644221873"><a name="p194644221873"></a><a name="p194644221873"></a>mongo008_mem_resident</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p18464922571"><a name="p18464922571"></a><a name="p18464922571"></a>Resident Memory</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p104653226719"><a name="p104653226719"></a><a name="p104653226719"></a>Size of resident memory in MB</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p24651422275"><a name="p24651422275"></a><a name="p24651422275"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p44651229713"><a name="p44651229713"></a><a name="p44651229713"></a>Monitored object: database</p>
<p id="p5734181122915"><a name="p5734181122915"></a><a name="p5734181122915"></a>Monitored object type:</p>
<a name="ul063381452918"></a><a name="ul063381452918"></a><ul id="ul063381452918"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row5664522874"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p104652221073"><a name="p104652221073"></a><a name="p104652221073"></a>mongo009_mem_virtual</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p13465172213714"><a name="p13465172213714"></a><a name="p13465172213714"></a>Virtual Memory</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p8465422379"><a name="p8465422379"></a><a name="p8465422379"></a>Size of virtual memory in MB</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p7465142218720"><a name="p7465142218720"></a><a name="p7465142218720"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p16465122217710"><a name="p16465122217710"></a><a name="p16465122217710"></a>Monitored object: database</p>
<p id="p3465622576"><a name="p3465622576"></a><a name="p3465622576"></a>Monitored object type:</p>
<a name="ul1557972442913"></a><a name="ul1557972442913"></a><ul id="ul1557972442913"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1766382220715"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1946510221476"><a name="p1946510221476"></a><a name="p1946510221476"></a>mongo010_regular_asserts_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p246510221576"><a name="p246510221576"></a><a name="p246510221576"></a>Regular Asserts per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p14465112215715"><a name="p14465112215715"></a><a name="p14465112215715"></a>Number of regular asserts per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p1346552218716"><a name="p1346552218716"></a><a name="p1346552218716"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p11465152213716"><a name="p11465152213716"></a><a name="p11465152213716"></a>Monitored object: database</p>
<p id="p174656221714"><a name="p174656221714"></a><a name="p174656221714"></a>Monitored object type:</p>
<a name="ul1095214336291"></a><a name="ul1095214336291"></a><ul id="ul1095214336291"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1566372212716"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p16465192211710"><a name="p16465192211710"></a><a name="p16465192211710"></a>mongo011_warning_asserts_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p114658223720"><a name="p114658223720"></a><a name="p114658223720"></a>Warning Asserts per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p7465152210716"><a name="p7465152210716"></a><a name="p7465152210716"></a>Number of warning asserts per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p17466322478"><a name="p17466322478"></a><a name="p17466322478"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p346682218714"><a name="p346682218714"></a><a name="p346682218714"></a>Monitored object: database</p>
<p id="p144661022574"><a name="p144661022574"></a><a name="p144661022574"></a>Monitored object type:</p>
<a name="ul699210443291"></a><a name="ul699210443291"></a><ul id="ul699210443291"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row15663172217711"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p546692210713"><a name="p546692210713"></a><a name="p546692210713"></a>mongo012_msg_asserts_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p15466142214715"><a name="p15466142214715"></a><a name="p15466142214715"></a>Message Asserts per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p146615223718"><a name="p146615223718"></a><a name="p146615223718"></a>Number of message asserts per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p995812811151"><a name="p995812811151"></a><a name="p995812811151"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p64671022477"><a name="p64671022477"></a><a name="p64671022477"></a>Monitored object: database</p>
<p id="p124670220714"><a name="p124670220714"></a><a name="p124670220714"></a>Monitored object type:</p>
<a name="ul7335124912298"></a><a name="ul7335124912298"></a><ul id="ul7335124912298"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row166322211711"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p204678223717"><a name="p204678223717"></a><a name="p204678223717"></a>mongo013_user_asserts_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1946702211718"><a name="p1946702211718"></a><a name="p1946702211718"></a>User Asserts per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p846742210710"><a name="p846742210710"></a><a name="p846742210710"></a>Number of user asserts per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p1646717221474"><a name="p1646717221474"></a><a name="p1646717221474"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p546742216711"><a name="p546742216711"></a><a name="p546742216711"></a>Monitored object: database</p>
<p id="p13467132217712"><a name="p13467132217712"></a><a name="p13467132217712"></a>Monitored object type:</p>
<a name="ul14838145862916"></a><a name="ul14838145862916"></a><ul id="ul14838145862916"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row56628223712"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1147220225711"><a name="p1147220225711"></a><a name="p1147220225711"></a>mongo014_queues_total</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1147272213717"><a name="p1147272213717"></a><a name="p1147272213717"></a>Operations Queued Waiting for a Lock</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p10472122215710"><a name="p10472122215710"></a><a name="p10472122215710"></a>Number of operations queued waiting for a lock</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p19472162214720"><a name="p19472162214720"></a><a name="p19472162214720"></a>≥ 0 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p16472142215718"><a name="p16472142215718"></a><a name="p16472142215718"></a>Monitored object: database</p>
<p id="p34721622971"><a name="p34721622971"></a><a name="p34721622971"></a>Monitored object type:</p>
<a name="ul186529193013"></a><a name="ul186529193013"></a><ul id="ul186529193013"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row106619222715"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p104722022770"><a name="p104722022770"></a><a name="p104722022770"></a>mongo015_queues_readers</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1847213229711"><a name="p1847213229711"></a><a name="p1847213229711"></a>Operations Queued Waiting for a Read Lock</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p44728221774"><a name="p44728221774"></a><a name="p44728221774"></a>Number of operations queued waiting for a read lock</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p247272217711"><a name="p247272217711"></a><a name="p247272217711"></a>≥ 0 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p13472142214718"><a name="p13472142214718"></a><a name="p13472142214718"></a>Monitored object: database</p>
<p id="p4472222973"><a name="p4472222973"></a><a name="p4472222973"></a>Monitored object type:</p>
<a name="ul157938156307"></a><a name="ul157938156307"></a><ul id="ul157938156307"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1566113221714"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p7472022374"><a name="p7472022374"></a><a name="p7472022374"></a>mongo016_queues_writers</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1647212221677"><a name="p1647212221677"></a><a name="p1647212221677"></a>Operations Queued Waiting for a Write Lock</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p1047219221879"><a name="p1047219221879"></a><a name="p1047219221879"></a>Number of operations queued waiting for a write lock</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p74726221974"><a name="p74726221974"></a><a name="p74726221974"></a>≥ 0 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p047282217719"><a name="p047282217719"></a><a name="p047282217719"></a>Monitored object: database</p>
<p id="p94721522776"><a name="p94721522776"></a><a name="p94721522776"></a>Monitored object type:</p>
<a name="ul16980151853018"></a><a name="ul16980151853018"></a><ul id="ul16980151853018"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row176612222714"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1147252211718"><a name="p1147252211718"></a><a name="p1147252211718"></a>mongo017_page_faults</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1472172213714"><a name="p1472172213714"></a><a name="p1472172213714"></a>Page Faults</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p74725221275"><a name="p74725221275"></a><a name="p74725221275"></a>Number of page faults on the monitored nodes</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p14733221875"><a name="p14733221875"></a><a name="p14733221875"></a>≥ 0 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p14473522873"><a name="p14473522873"></a><a name="p14473522873"></a>Monitored object: database</p>
<p id="p1447310228715"><a name="p1447310228715"></a><a name="p1447310228715"></a>Monitored object type:</p>
<a name="ul141311127153018"></a><a name="ul141311127153018"></a><ul id="ul141311127153018"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row13660172210712"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p34736221173"><a name="p34736221173"></a><a name="p34736221173"></a>mongo018_porfling_num</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p24734221972"><a name="p24734221972"></a><a name="p24734221972"></a>Slow Queries</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p24731221714"><a name="p24731221714"></a><a name="p24731221714"></a>Number of slow queries on the monitored nodes</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p7473422176"><a name="p7473422176"></a><a name="p7473422176"></a>≥ 0 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p204735221079"><a name="p204735221079"></a><a name="p204735221079"></a>Monitored object: database</p>
<p id="p74730221072"><a name="p74730221072"></a><a name="p74730221072"></a>Monitored object type:</p>
<a name="ul1663223618306"></a><a name="ul1663223618306"></a><ul id="ul1663223618306"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row66604221374"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p124736221378"><a name="p124736221378"></a><a name="p124736221378"></a>mongo019_cursors_open</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p114735225715"><a name="p114735225715"></a><a name="p114735225715"></a>Current Maintained Cursors</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p14473522374"><a name="p14473522374"></a><a name="p14473522374"></a>Number of maintained cursors on the monitored nodes</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p1347332218712"><a name="p1347332218712"></a><a name="p1347332218712"></a>≥ 0 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p64737221874"><a name="p64737221874"></a><a name="p64737221874"></a>Monitored object: database</p>
<p id="p124739224715"><a name="p124739224715"></a><a name="p124739224715"></a>Monitored object type:</p>
<a name="ul14179241123011"></a><a name="ul14179241123011"></a><ul id="ul14179241123011"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1766022211717"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1747482214719"><a name="p1747482214719"></a><a name="p1747482214719"></a>mongo020_cursors_timeOut</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p947420221714"><a name="p947420221714"></a><a name="p947420221714"></a>Timeout Cursors</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p94749220718"><a name="p94749220718"></a><a name="p94749220718"></a>Number of timed out cursors on the monitored nodes</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p5474132213713"><a name="p5474132213713"></a><a name="p5474132213713"></a>≥ 0 Counts</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p147413221076"><a name="p147413221076"></a><a name="p147413221076"></a>Monitored object: database</p>
<p id="p84741422171"><a name="p84741422171"></a><a name="p84741422171"></a>Monitored object type:</p>
<a name="ul1761484733015"></a><a name="ul1761484733015"></a><ul id="ul1761484733015"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row156591322671"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1947415221572"><a name="p1947415221572"></a><a name="p1947415221572"></a>mongo021_wt_cahe_usage</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p124741221575"><a name="p124741221575"></a><a name="p124741221575"></a>Bytes in WiredTiger Cache</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p114748221712"><a name="p114748221712"></a><a name="p114748221712"></a>Size of data in the WiredTiger cache in MB</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p19474622973"><a name="p19474622973"></a><a name="p19474622973"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p34747221678"><a name="p34747221678"></a><a name="p34747221678"></a>Monitored object: database</p>
<p id="p1347432213710"><a name="p1347432213710"></a><a name="p1347432213710"></a>Monitored object type:</p>
<a name="ul487825823014"></a><a name="ul487825823014"></a><ul id="ul487825823014"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row6659422676"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p11474422572"><a name="p11474422572"></a><a name="p11474422572"></a>mongo022_wt_cahe_dirty</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1447418221577"><a name="p1447418221577"></a><a name="p1447418221577"></a>Tracked Dirty Bytes in WiredTiger Cache</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p6474182212713"><a name="p6474182212713"></a><a name="p6474182212713"></a>Size of tracked dirty data in the WiredTiger cache in MB</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p20475622177"><a name="p20475622177"></a><a name="p20475622177"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p147518222714"><a name="p147518222714"></a><a name="p147518222714"></a>Monitored object: database</p>
<p id="p16475222873"><a name="p16475222873"></a><a name="p16475222873"></a>Monitored object type:</p>
<a name="ul642931483119"></a><a name="ul642931483119"></a><ul id="ul642931483119"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row26580221579"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p114751322476"><a name="p114751322476"></a><a name="p114751322476"></a>mongo023_wInto_wtCache</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p947518224716"><a name="p947518224716"></a><a name="p947518224716"></a>Bytes Written Into Cache per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p447562219720"><a name="p447562219720"></a><a name="p447562219720"></a>Bytes written into WiredTiger cache per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p247519221575"><a name="p247519221575"></a><a name="p247519221575"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p5475142213711"><a name="p5475142213711"></a><a name="p5475142213711"></a>Monitored object: database</p>
<p id="p147517221879"><a name="p147517221879"></a><a name="p147517221879"></a>Monitored object type:</p>
<a name="ul18495112063112"></a><a name="ul18495112063112"></a><ul id="ul18495112063112"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row36582221717"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p14475112219717"><a name="p14475112219717"></a><a name="p14475112219717"></a>mongo024_wFrom_wtCache</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p847582215714"><a name="p847582215714"></a><a name="p847582215714"></a>Bytes Written From Cache per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p12475172213717"><a name="p12475172213717"></a><a name="p12475172213717"></a>Bytes written from the WiredTiger cache to the disk per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p147542219710"><a name="p147542219710"></a><a name="p147542219710"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p10476132217719"><a name="p10476132217719"></a><a name="p10476132217719"></a>Monitored object: database</p>
<p id="p1947632219719"><a name="p1947632219719"></a><a name="p1947632219719"></a>Monitored object type:</p>
<a name="ul4955162217313"></a><a name="ul4955162217313"></a><ul id="ul4955162217313"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1465817221476"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p104761022170"><a name="p104761022170"></a><a name="p104761022170"></a>mongo025_repl_oplog_win</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1247614221178"><a name="p1247614221178"></a><a name="p1247614221178"></a>Oplog Window</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p12476122212711"><a name="p12476122212711"></a><a name="p12476122212711"></a>Available time in hour in the monitored primary node's oplog</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p347616221577"><a name="p347616221577"></a><a name="p347616221577"></a>≥ 0 Hours</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p144766221673"><a name="p144766221673"></a><a name="p144766221673"></a>Monitored object: database</p>
<p id="p1847611220710"><a name="p1847611220710"></a><a name="p1847611220710"></a>Monitored object type: primary node</p>
</td>
</tr>
<tr id="row1265722214717"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1947611221277"><a name="p1947611221277"></a><a name="p1947611221277"></a>mongo026_oplog_size_ph</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p134762221271"><a name="p134762221271"></a><a name="p134762221271"></a>Oplog Growth Rate</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p2047692215714"><a name="p2047692215714"></a><a name="p2047692215714"></a>Speed in MB/hour at which oplogs are generated on the monitored primary node</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p16476522278"><a name="p16476522278"></a><a name="p16476522278"></a>≥ 0 MB/Hour</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p194765221573"><a name="p194765221573"></a><a name="p194765221573"></a>Monitored object: database</p>
<p id="p147615221174"><a name="p147615221174"></a><a name="p147615221174"></a>Monitored object type: primary node</p>
</td>
</tr>
<tr id="row9731164874620"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p17684541461"><a name="p17684541461"></a><a name="p17684541461"></a>mongo025_repl_headroom</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p5774541467"><a name="p5774541467"></a><a name="p5774541467"></a>Replication Headroom</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p1683135444612"><a name="p1683135444612"></a><a name="p1683135444612"></a>Time difference in seconds between the primary's oplog window and the replication lag of the secondary</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p15861954154610"><a name="p15861954154610"></a><a name="p15861954154610"></a>≥ 0 Seconds</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p2091154154616"><a name="p2091154154616"></a><a name="p2091154154616"></a>Monitored object: database</p>
<p id="p13951654164611"><a name="p13951654164611"></a><a name="p13951654164611"></a>Monitored object type: secondary node</p>
</td>
</tr>
<tr id="row1863374619466"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p6113954184618"><a name="p6113954184618"></a><a name="p6113954184618"></a>mongo026_repl_lag</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p11192542468"><a name="p11192542468"></a><a name="p11192542468"></a>Replication Lag</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p6125155454613"><a name="p6125155454613"></a><a name="p6125155454613"></a>A delay in seconds between an operation on the primary and the application of that operation from the oplog to the secondary</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p1512945424613"><a name="p1512945424613"></a><a name="p1512945424613"></a>≥ 0 Seconds</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p11341354124612"><a name="p11341354124612"></a><a name="p11341354124612"></a>Monitored object: database</p>
<p id="p1413745413461"><a name="p1413745413461"></a><a name="p1413745413461"></a>Monitored object type: secondary node</p>
</td>
</tr>
<tr id="row172941744164611"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p181561554194612"><a name="p181561554194612"></a><a name="p181561554194612"></a>mongo027_repl_command_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p2163145415460"><a name="p2163145415460"></a><a name="p2163145415460"></a>Replicated COMMAND Statements per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p141681954124616"><a name="p141681954124616"></a><a name="p141681954124616"></a>Number of replicated COMMAND statements executed on the secondary node per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p21731054154615"><a name="p21731054154615"></a><a name="p21731054154615"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p1918215543466"><a name="p1918215543466"></a><a name="p1918215543466"></a>Monitored object: database</p>
<p id="p1718455464618"><a name="p1718455464618"></a><a name="p1718455464618"></a>Monitored object type: secondary node</p>
</td>
</tr>
<tr id="row164609411468"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1620513549465"><a name="p1620513549465"></a><a name="p1620513549465"></a>mongo028_repl_update_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p9214254154612"><a name="p9214254154612"></a><a name="p9214254154612"></a>Replicated UPDATE Statements per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p20220145412469"><a name="p20220145412469"></a><a name="p20220145412469"></a>Number of replicated UPDATE statements executed on the secondary node per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p5225154194614"><a name="p5225154194614"></a><a name="p5225154194614"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p2023613546469"><a name="p2023613546469"></a><a name="p2023613546469"></a>Monitored object: database</p>
<p id="p1223995454617"><a name="p1223995454617"></a><a name="p1223995454617"></a>Monitored object type: secondary node</p>
</td>
</tr>
<tr id="row19568112714473"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p7608631104717"><a name="p7608631104717"></a><a name="p7608631104717"></a>mongo029_repl_delete_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1161510313478"><a name="p1161510313478"></a><a name="p1161510313478"></a>Replicated DELETE Statements per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p1621143164719"><a name="p1621143164719"></a><a name="p1621143164719"></a>Number of replicated DELETE statements executed on the secondary node per second </p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p136271131194715"><a name="p136271131194715"></a><a name="p136271131194715"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p1663633115475"><a name="p1663633115475"></a><a name="p1663633115475"></a>Monitored object: database</p>
<p id="p2063863115470"><a name="p2063863115470"></a><a name="p2063863115470"></a>Monitored object type: secondary node</p>
</td>
</tr>
<tr id="row184386253479"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p765723194714"><a name="p765723194714"></a><a name="p765723194714"></a>mongo030_repl_insert_ps</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p16611531184715"><a name="p16611531184715"></a><a name="p16611531184715"></a>Replicated INSERT Statements per Second</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p266663184712"><a name="p266663184712"></a><a name="p266663184712"></a>Number of replicated INSERT statements executed on the secondary node per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p11671163174719"><a name="p11671163174719"></a><a name="p11671163174719"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p10680153154718"><a name="p10680153154718"></a><a name="p10680153154718"></a>Monitored object: database</p>
<p id="p17683731174720"><a name="p17683731174720"></a><a name="p17683731174720"></a>Monitored object type: secondary node</p>
</td>
</tr>
<tr id="row17409182019321"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p1689142443215"><a name="p1689142443215"></a><a name="p1689142443215"></a>mongo031_cpu_usage</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p137069249328"><a name="p137069249328"></a><a name="p137069249328"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p11715142414323"><a name="p11715142414323"></a><a name="p11715142414323"></a>CPU usage of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p0723024153217"><a name="p0723024153217"></a><a name="p0723024153217"></a>0–1</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p8733162413321"><a name="p8733162413321"></a><a name="p8733162413321"></a>Monitored object: ECS</p>
<p id="p197371024143217"><a name="p197371024143217"></a><a name="p197371024143217"></a>Monitored object type:</p>
<a name="ul17597103783418"></a><a name="ul17597103783418"></a><ul id="ul17597103783418"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row197626176320"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p187521246328"><a name="p187521246328"></a><a name="p187521246328"></a>mongo032_mem_usage</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p57601124103213"><a name="p57601124103213"></a><a name="p57601124103213"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p14767172420325"><a name="p14767172420325"></a><a name="p14767172420325"></a>Memory usage of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p1977612419326"><a name="p1977612419326"></a><a name="p1977612419326"></a>0–1</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p11782102453211"><a name="p11782102453211"></a><a name="p11782102453211"></a>Monitored object: ECS</p>
<div class="p" id="p1678713240327"><a name="p1678713240327"></a><a name="p1678713240327"></a>Monitored object type:<a name="ul3741257134914"></a><a name="ul3741257134914"></a><ul id="ul3741257134914"><li>mongos node</li></ul>
</div>
<a name="ul189433395345"></a><a name="ul189433395345"></a><ul id="ul189433395345"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row18316141543211"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p8799724203213"><a name="p8799724203213"></a><a name="p8799724203213"></a>mongo033_bytes_out</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p168056243327"><a name="p168056243327"></a><a name="p168056243327"></a>Network Output Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p1581720241322"><a name="p1581720241322"></a><a name="p1581720241322"></a>Outgoing traffic in bytes per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p1682482423213"><a name="p1682482423213"></a><a name="p1682482423213"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p1983213249328"><a name="p1983213249328"></a><a name="p1983213249328"></a>Monitored object: ECS</p>
<p id="p1883662417325"><a name="p1883662417325"></a><a name="p1883662417325"></a>Monitored object type:</p>
<a name="ul427819423346"></a><a name="ul427819423346"></a><ul id="ul427819423346"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row15782181215322"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p158502245328"><a name="p158502245328"></a><a name="p158502245328"></a>mongo034_bytes_in</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p2858124173220"><a name="p2858124173220"></a><a name="p2858124173220"></a>Network Input Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p1886416249328"><a name="p1886416249328"></a><a name="p1886416249328"></a>Incoming traffic in bytes per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p28702024103210"><a name="p28702024103210"></a><a name="p28702024103210"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p208771024133217"><a name="p208771024133217"></a><a name="p208771024133217"></a>Monitored object: ECS</p>
<p id="p388232443217"><a name="p388232443217"></a><a name="p388232443217"></a>Monitored object type:</p>
<a name="ul104151145113413"></a><a name="ul104151145113413"></a><ul id="ul104151145113413"><li>mongos node</li><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row46542222079"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p184789228718"><a name="p184789228718"></a><a name="p184789228718"></a>mongo035_disk_usage</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p12478192210718"><a name="p12478192210718"></a><a name="p12478192210718"></a>Disk Utilization</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p184781722976"><a name="p184781722976"></a><a name="p184781722976"></a>Disk usage of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p1747811221975"><a name="p1747811221975"></a><a name="p1747811221975"></a>0–1</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p154791922475"><a name="p154791922475"></a><a name="p154791922475"></a>Monitored object: ECS</p>
<p id="p164791221777"><a name="p164791221777"></a><a name="p164791221777"></a>Monitored object type:</p>
<a name="ul15719194711345"></a><a name="ul15719194711345"></a><ul id="ul15719194711345"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row196541221878"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p134791022671"><a name="p134791022671"></a><a name="p134791022671"></a>mongo036_iops</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p947915229716"><a name="p947915229716"></a><a name="p947915229716"></a>IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p14479162212716"><a name="p14479162212716"></a><a name="p14479162212716"></a>Average number of I/O requests processed by the system in a specified period</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p2479922372"><a name="p2479922372"></a><a name="p2479922372"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p124791225719"><a name="p124791225719"></a><a name="p124791225719"></a>Monitored object: ECS</p>
<p id="p94798227710"><a name="p94798227710"></a><a name="p94798227710"></a>Monitored object type:</p>
<a name="ul49901749143411"></a><a name="ul49901749143411"></a><ul id="ul49901749143411"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row19654022675"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p134791221774"><a name="p134791221774"></a><a name="p134791221774"></a>mongo037_read_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p144791722478"><a name="p144791722478"></a><a name="p144791722478"></a>Disk Read Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p24791222374"><a name="p24791222374"></a><a name="p24791222374"></a>Number of bytes read from the disk per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p647962215710"><a name="p647962215710"></a><a name="p647962215710"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p147922211719"><a name="p147922211719"></a><a name="p147922211719"></a>Monitored object: ECS</p>
<p id="p1747913221720"><a name="p1747913221720"></a><a name="p1747913221720"></a>Monitored object type:</p>
<a name="ul997175313348"></a><a name="ul997175313348"></a><ul id="ul997175313348"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row4653722978"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p74791122978"><a name="p74791122978"></a><a name="p74791122978"></a>mongo038_write_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p247962218711"><a name="p247962218711"></a><a name="p247962218711"></a>Disk Write Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p947919225717"><a name="p947919225717"></a><a name="p947919225717"></a>Number of bytes written into the disk per second</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p0479142220710"><a name="p0479142220710"></a><a name="p0479142220710"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p1648016227710"><a name="p1648016227710"></a><a name="p1648016227710"></a>Monitored object: ECS</p>
<p id="p154807221714"><a name="p154807221714"></a><a name="p154807221714"></a>Monitored object type:</p>
<a name="ul38353552343"></a><a name="ul38353552343"></a><ul id="ul38353552343"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row665242219716"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p948019221876"><a name="p948019221876"></a><a name="p948019221876"></a>mongo039_avg_disk_sec_per_read</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p1548020226712"><a name="p1548020226712"></a><a name="p1548020226712"></a>Disk Read Time</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p174802022675"><a name="p174802022675"></a><a name="p174802022675"></a>Average time required for each disk read in a specified period</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p1548011221175"><a name="p1548011221175"></a><a name="p1548011221175"></a>≥ 0 Seconds</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p1248052214719"><a name="p1248052214719"></a><a name="p1248052214719"></a>Monitored object: ECS</p>
<p id="p1648012221178"><a name="p1648012221178"></a><a name="p1648012221178"></a>Monitored object type:</p>
<a name="ul17682175783410"></a><a name="ul17682175783410"></a><ul id="ul17682175783410"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row665215221713"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p24801227719"><a name="p24801227719"></a><a name="p24801227719"></a>mongo040_avg_disk_sec_per_write</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p184807221870"><a name="p184807221870"></a><a name="p184807221870"></a>Disk Write Time</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p1248012215717"><a name="p1248012215717"></a><a name="p1248012215717"></a>Average time required for each disk write in a specified period</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p1148018221678"><a name="p1148018221678"></a><a name="p1148018221678"></a>≥ 0 Seconds</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p1648014226710"><a name="p1648014226710"></a><a name="p1648014226710"></a>Monitored object: ECS</p>
<p id="p1048011221718"><a name="p1048011221718"></a><a name="p1048011221718"></a>Monitored object type:</p>
<a name="ul919919173511"></a><a name="ul919919173511"></a><ul id="ul919919173511"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row3651132214718"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p184804226716"><a name="p184804226716"></a><a name="p184804226716"></a>mongo042_disk_total_size</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p6480152218718"><a name="p6480152218718"></a><a name="p6480152218718"></a>Total Storage Space</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p11480122212710"><a name="p11480122212710"></a><a name="p11480122212710"></a>Total storage space of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p348011221674"><a name="p348011221674"></a><a name="p348011221674"></a>0–1000 GB</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p1348072210715"><a name="p1348072210715"></a><a name="p1348072210715"></a>Monitored object: ECS</p>
<p id="p1148018229719"><a name="p1148018229719"></a><a name="p1148018229719"></a>Monitored object type:</p>
<a name="ul183041773355"></a><a name="ul183041773355"></a><ul id="ul183041773355"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
<tr id="row1665112217712"><td class="cellrowborder" valign="top" width="13.717171717171716%" headers="mcps1.1.6.1.1 "><p id="p348013226711"><a name="p348013226711"></a><a name="p348013226711"></a>mongo043_disk_used_size</p>
</td>
<td class="cellrowborder" valign="top" width="16.606060606060606%" headers="mcps1.1.6.1.2 "><p id="p9480722579"><a name="p9480722579"></a><a name="p9480722579"></a>Used Storage Space</p>
</td>
<td class="cellrowborder" valign="top" width="35.58585858585858%" headers="mcps1.1.6.1.3 "><p id="p18480122372"><a name="p18480122372"></a><a name="p18480122372"></a>Used storage space of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="11.15151515151515%" headers="mcps1.1.6.1.4 "><p id="p54811221716"><a name="p54811221716"></a><a name="p54811221716"></a>0–1000 GB</p>
</td>
<td class="cellrowborder" valign="top" width="22.939393939393938%" headers="mcps1.1.6.1.5 "><p id="p1748192213718"><a name="p1748192213718"></a><a name="p1748192213718"></a>Monitored object: ECS</p>
<p id="p24812221271"><a name="p24812221271"></a><a name="p24812221271"></a>Monitored object type:</p>
<a name="ul467121583511"></a><a name="ul467121583511"></a><ul id="ul467121583511"><li>Primary node</li><li>Secondary node</li></ul>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="section45895235153251"></a>

<a name="table26526577153251"></a>
<table><thead align="left"><tr id="row46969777153251"><th class="cellrowborder" valign="top" width="32.75%" id="mcps1.1.3.1.1"><p id="p46455583153251"><a name="p46455583153251"></a><a name="p46455583153251"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="67.25%" id="mcps1.1.3.1.2"><p id="p4805882153251"><a name="p4805882153251"></a><a name="p4805882153251"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row768992811619"><td class="cellrowborder" valign="top" width="32.75%" headers="mcps1.1.3.1.1 "><p id="p267914281617"><a name="p267914281617"></a><a name="p267914281617"></a>mongodb_cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="67.25%" headers="mcps1.1.3.1.2 "><p id="p13754191919570"><a name="p13754191919570"></a><a name="p13754191919570"></a>DDS DB instance ID</p>
<p id="p486754718574"><a name="p486754718574"></a><a name="p486754718574"></a>Supports cluster and replica set instances.</p>
</td>
</tr>
<tr id="row166894287616"><td class="cellrowborder" valign="top" width="32.75%" headers="mcps1.1.3.1.1 "><p id="p66791928161"><a name="p66791928161"></a><a name="p66791928161"></a>mongos_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="67.25%" headers="mcps1.1.3.1.2 "><p id="p186791428467"><a name="p186791428467"></a><a name="p186791428467"></a>mongos node ID</p>
</td>
</tr>
<tr id="row468932820618"><td class="cellrowborder" valign="top" width="32.75%" headers="mcps1.1.3.1.1 "><p id="p1367914285617"><a name="p1367914285617"></a><a name="p1367914285617"></a>mongod_primary_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="67.25%" headers="mcps1.1.3.1.2 "><p id="p13679102814616"><a name="p13679102814616"></a><a name="p13679102814616"></a>Primary node ID</p>
<p id="p1178942610311"><a name="p1178942610311"></a><a name="p1178942610311"></a>Includes the config and shard primary nodes of cluster instances and the primary nodes of replica set instances.</p>
</td>
</tr>
<tr id="row168782818613"><td class="cellrowborder" valign="top" width="32.75%" headers="mcps1.1.3.1.1 "><p id="p167911288618"><a name="p167911288618"></a><a name="p167911288618"></a>mongod_secondary_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="67.25%" headers="mcps1.1.3.1.2 "><p id="p3679028961"><a name="p3679028961"></a><a name="p3679028961"></a>Secondary node ID</p>
<p id="p132831831996"><a name="p132831831996"></a><a name="p132831831996"></a>Includes the config and shard secondary nodes of cluster instances and the secondary nodes of replica set instances.</p>
</td>
</tr>
</tbody>
</table>

