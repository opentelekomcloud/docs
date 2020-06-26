# Configuring Displayed Metrics<a name="rds_pg_06_0001"></a>

## Description<a name="section3846020215313"></a>

This section describes namespaces, descriptions, and dimensions of monitoring metrics to be reported to Cloud Eye. Users can retrieve monitoring metrics and alarm information reported to Cloud Eye over its API.

## Namespace<a name="section1688213153437"></a>

SYS.RDS

## DB Instance Monitoring Metrics<a name="en-us_topic_0171122394_s1feb2fcf34ab4e88a61a1597e2ec8f06"></a>

[Table 1](#table46701376141844)  lists the performance metrics of PostgreSQL databases.

**Table  1**  Database performance metrics

<a name="table46701376141844"></a>
<table><thead align="left"><tr id="re01f141cc21347af98381c27e1a5d524"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.7.1.1"><p id="a807246cff23b44219a7b4ecb8436420f"><a name="a807246cff23b44219a7b4ecb8436420f"></a><a name="a807246cff23b44219a7b4ecb8436420f"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.7.1.2"><p id="en-us_topic_0029128243_p468860223835"><a name="en-us_topic_0029128243_p468860223835"></a><a name="en-us_topic_0029128243_p468860223835"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.7.1.3"><p id="a8bcd5efa9ee44b9ea636cef5aa688a8f"><a name="a8bcd5efa9ee44b9ea636cef5aa688a8f"></a><a name="a8bcd5efa9ee44b9ea636cef5aa688a8f"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.7.1.4"><p id="a8653133d56124b96a4e0fff4e8f62019"><a name="a8653133d56124b96a4e0fff4e8f62019"></a><a name="a8653133d56124b96a4e0fff4e8f62019"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.7.1.5"><p id="a762d63ea73c943f5977b57d80ca121d7"><a name="a762d63ea73c943f5977b57d80ca121d7"></a><a name="a762d63ea73c943f5977b57d80ca121d7"></a>Monitored Object</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.7.1.6"><p id="p285717216337"><a name="p285717216337"></a><a name="p285717216337"></a>Monitoring Interval (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="ra9c1d6eb3b56483d8a8838e74d31e642"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="aa1c7ecf3758444d4bc8e8f06b897fa96"><a name="aa1c7ecf3758444d4bc8e8f06b897fa96"></a><a name="aa1c7ecf3758444d4bc8e8f06b897fa96"></a>rds001_cpu_util</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="a47e9c5cfd53542d5ab746dd1f2cb090e"><a name="a47e9c5cfd53542d5ab746dd1f2cb090e"></a><a name="a47e9c5cfd53542d5ab746dd1f2cb090e"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="a8bbe05cb232b4427b2447d1fc478222e"><a name="a8bbe05cb232b4427b2447d1fc478222e"></a><a name="a8bbe05cb232b4427b2447d1fc478222e"></a>CPU usage of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="acc6eb79dd02047ffbc26cf17e20f38cb"><a name="acc6eb79dd02047ffbc26cf17e20f38cb"></a><a name="acc6eb79dd02047ffbc26cf17e20f38cb"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p228310199465"><a name="p228310199465"></a><a name="p228310199465"></a>Monitored object: ECS</p>
<p id="p45641326164812"><a name="p45641326164812"></a><a name="p45641326164812"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p118571924337"><a name="p118571924337"></a><a name="p118571924337"></a>1 minute</p>
</td>
</tr>
<tr id="rbf6d226456694af083a40de12dbb93cd"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="acfa39719774349a2b4be04f612b28e6e"><a name="acfa39719774349a2b4be04f612b28e6e"></a><a name="acfa39719774349a2b4be04f612b28e6e"></a>rds002_mem_util</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="a17120aa5ab7448629c4828548e9ff996"><a name="a17120aa5ab7448629c4828548e9ff996"></a><a name="a17120aa5ab7448629c4828548e9ff996"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="a775c60966f644266948c79c107fa37e8"><a name="a775c60966f644266948c79c107fa37e8"></a><a name="a775c60966f644266948c79c107fa37e8"></a>Memory usage of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p193641331101511"><a name="p193641331101511"></a><a name="p193641331101511"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p20304147134615"><a name="p20304147134615"></a><a name="p20304147134615"></a>Monitored object: ECS</p>
<p id="p9305247154611"><a name="p9305247154611"></a><a name="p9305247154611"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p1085718263311"><a name="p1085718263311"></a><a name="p1085718263311"></a>1 minute</p>
</td>
</tr>
<tr id="r3cea26498b3447b9a3ead17476c7c422"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="abe14ba68980e460183ba7bfe0f78f493"><a name="abe14ba68980e460183ba7bfe0f78f493"></a><a name="abe14ba68980e460183ba7bfe0f78f493"></a>rds003_iops</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="a8677e88f532e4667957cfe5c142c3eb4"><a name="a8677e88f532e4667957cfe5c142c3eb4"></a><a name="a8677e88f532e4667957cfe5c142c3eb4"></a>IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="adcfc613b104e4bbdb236107c7983f544"><a name="adcfc613b104e4bbdb236107c7983f544"></a><a name="adcfc613b104e4bbdb236107c7983f544"></a>Average number of I/O requests processed by the system in a specified period</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="a9bd3d08b7e79414c9b05faac03f0e760"><a name="a9bd3d08b7e79414c9b05faac03f0e760"></a><a name="a9bd3d08b7e79414c9b05faac03f0e760"></a>≥ 0 counts/s</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p1861975111463"><a name="p1861975111463"></a><a name="p1861975111463"></a>Monitored object: ECS</p>
<p id="p661915114619"><a name="p661915114619"></a><a name="p661915114619"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p98572213314"><a name="p98572213314"></a><a name="p98572213314"></a>1 minute</p>
</td>
</tr>
<tr id="r1069941e6a9b4463863c575cb9291d1e"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="ae6176ccfa03a4e18a930e91c5e463fff"><a name="ae6176ccfa03a4e18a930e91c5e463fff"></a><a name="ae6176ccfa03a4e18a930e91c5e463fff"></a>rds004_bytes_in</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="a065095b14e394d4b9d85d3b8d9006c0d"><a name="a065095b14e394d4b9d85d3b8d9006c0d"></a><a name="a065095b14e394d4b9d85d3b8d9006c0d"></a>Network Input Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="ae29cadcafee44fd284f88747e1bab9ea"><a name="ae29cadcafee44fd284f88747e1bab9ea"></a><a name="ae29cadcafee44fd284f88747e1bab9ea"></a>Incoming traffic in bytes per second</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="a3c8adbfbc01f412bb9b939d7cf4402b0"><a name="a3c8adbfbc01f412bb9b939d7cf4402b0"></a><a name="a3c8adbfbc01f412bb9b939d7cf4402b0"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p119230557463"><a name="p119230557463"></a><a name="p119230557463"></a>Monitored object: ECS</p>
<p id="p492310554461"><a name="p492310554461"></a><a name="p492310554461"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p78576219334"><a name="p78576219334"></a><a name="p78576219334"></a>1 minute</p>
</td>
</tr>
<tr id="r9fbd096305194e6b8fca4826a3b597cc"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="af9938a4483844a73b9ac48e277dff019"><a name="af9938a4483844a73b9ac48e277dff019"></a><a name="af9938a4483844a73b9ac48e277dff019"></a>rds005_bytes_out</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="a6850346c502e421eba00563c83bdc417"><a name="a6850346c502e421eba00563c83bdc417"></a><a name="a6850346c502e421eba00563c83bdc417"></a>Network Output Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="a8a416bbf839a442a857e6e647144ee09"><a name="a8a416bbf839a442a857e6e647144ee09"></a><a name="a8a416bbf839a442a857e6e647144ee09"></a>Outgoing traffic in bytes per second</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="abd516c021d294e9383dc76012e2a61bb"><a name="abd516c021d294e9383dc76012e2a61bb"></a><a name="abd516c021d294e9383dc76012e2a61bb"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p113513664715"><a name="p113513664715"></a><a name="p113513664715"></a>Monitored object: ECS</p>
<p id="p101359694713"><a name="p101359694713"></a><a name="p101359694713"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p14857626330"><a name="p14857626330"></a><a name="p14857626330"></a>1 minute</p>
</td>
</tr>
<tr id="r9f98434644aa4bb1bf05e67fdd90c7b2"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="a64be8ded9a174fc2b638a645164bb00b"><a name="a64be8ded9a174fc2b638a645164bb00b"></a><a name="a64be8ded9a174fc2b638a645164bb00b"></a>rds039_disk_util</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="ac056999825234a86aeb1bde58f13e3ac"><a name="ac056999825234a86aeb1bde58f13e3ac"></a><a name="ac056999825234a86aeb1bde58f13e3ac"></a>Storage Space Usage</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="a227244818c874d2bb5a6f63923d3a22b"><a name="a227244818c874d2bb5a6f63923d3a22b"></a><a name="a227244818c874d2bb5a6f63923d3a22b"></a>Storage space usage of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p28492171613"><a name="p28492171613"></a><a name="p28492171613"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p20575932174818"><a name="p20575932174818"></a><a name="p20575932174818"></a>Monitored object: ECS</p>
<p id="p55751432114818"><a name="p55751432114818"></a><a name="p55751432114818"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p985792113316"><a name="p985792113316"></a><a name="p985792113316"></a>1 minute</p>
</td>
</tr>
<tr id="row284059149835"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p461393659843"><a name="p461393659843"></a><a name="p461393659843"></a>rds040_transaction_logs_usage</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p8088335992"><a name="p8088335992"></a><a name="p8088335992"></a>Transaction Logs Usage</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p51175371992"><a name="p51175371992"></a><a name="p51175371992"></a>Storage space usage of transaction logs</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p51564412992"><a name="p51564412992"></a><a name="p51564412992"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p15967882992"><a name="p15967882992"></a><a name="p15967882992"></a>Monitored object: database</p>
<p id="p28614813185620"><a name="p28614813185620"></a><a name="p28614813185620"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p58579211334"><a name="p58579211334"></a><a name="p58579211334"></a>1 minute</p>
</td>
</tr>
<tr id="row31562129835"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p77229679843"><a name="p77229679843"></a><a name="p77229679843"></a>rds041_replication_slot_usage</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p30752963992"><a name="p30752963992"></a><a name="p30752963992"></a>Replication Slot Usage</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p7962038992"><a name="p7962038992"></a><a name="p7962038992"></a>Storage space usage of replication slot files</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p40945379992"><a name="p40945379992"></a><a name="p40945379992"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p28241392992"><a name="p28241392992"></a><a name="p28241392992"></a>Monitored object: database</p>
<p id="p20027222185615"><a name="p20027222185615"></a><a name="p20027222185615"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p1385742173316"><a name="p1385742173316"></a><a name="p1385742173316"></a>1 minute</p>
</td>
</tr>
<tr id="row450899329835"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p128130919843"><a name="p128130919843"></a><a name="p128130919843"></a>rds042_database_connections</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p52662579992"><a name="p52662579992"></a><a name="p52662579992"></a>Database Connections in Use</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p37810472992"><a name="p37810472992"></a><a name="p37810472992"></a>Number of database connections in use</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p42749369992"><a name="p42749369992"></a><a name="p42749369992"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p373704613543"><a name="p373704613543"></a><a name="p373704613543"></a>Monitored object: database</p>
<p id="p3363341713543"><a name="p3363341713543"></a><a name="p3363341713543"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p385716217338"><a name="p385716217338"></a><a name="p385716217338"></a>1 minute</p>
</td>
</tr>
<tr id="row348361549835"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p107309549843"><a name="p107309549843"></a><a name="p107309549843"></a>rds043_maximum_used_transaction_ids</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p7622504992"><a name="p7622504992"></a><a name="p7622504992"></a>Maximum Used Transaction IDs</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p13443064992"><a name="p13443064992"></a><a name="p13443064992"></a>Maximum number of transaction IDs that have been used</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p15146409992"><a name="p15146409992"></a><a name="p15146409992"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p2402571413543"><a name="p2402571413543"></a><a name="p2402571413543"></a>Monitored object: database</p>
<p id="p1490483513543"><a name="p1490483513543"></a><a name="p1490483513543"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p1585713223312"><a name="p1585713223312"></a><a name="p1585713223312"></a>1 minute</p>
</td>
</tr>
<tr id="row38706839835"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p94263939843"><a name="p94263939843"></a><a name="p94263939843"></a>rds044_transaction_logs_generations</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p20505075992"><a name="p20505075992"></a><a name="p20505075992"></a>Transaction Logs Generation</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p50298377992"><a name="p50298377992"></a><a name="p50298377992"></a>Size of transaction logs generated per second</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p47636707992"><a name="p47636707992"></a><a name="p47636707992"></a>≥ 0 MB/s</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p5016649135410"><a name="p5016649135410"></a><a name="p5016649135410"></a>Monitored object: database</p>
<p id="p45149841135410"><a name="p45149841135410"></a><a name="p45149841135410"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p12857122113317"><a name="p12857122113317"></a><a name="p12857122113317"></a>1 minute</p>
</td>
</tr>
<tr id="row78866169835"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p502820189843"><a name="p502820189843"></a><a name="p502820189843"></a>rds045_oldest_replication_slot_lag</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p31893805992"><a name="p31893805992"></a><a name="p31893805992"></a>Oldest Replication Slot Lag</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p33261442992"><a name="p33261442992"></a><a name="p33261442992"></a>Lagging size of the most lagging replica in terms of WAL data received</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p9822304992"><a name="p9822304992"></a><a name="p9822304992"></a>≥ 0 MB</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p3510764135411"><a name="p3510764135411"></a><a name="p3510764135411"></a>Monitored object: database</p>
<p id="p31596877135411"><a name="p31596877135411"></a><a name="p31596877135411"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p385710253313"><a name="p385710253313"></a><a name="p385710253313"></a>1 minute</p>
</td>
</tr>
<tr id="row83328319835"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p363752969843"><a name="p363752969843"></a><a name="p363752969843"></a>rds046_replication_lag</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p42436472992"><a name="p42436472992"></a><a name="p42436472992"></a>Replication Lag</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p14802198992"><a name="p14802198992"></a><a name="p14802198992"></a>Replication lag</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p58127393992"><a name="p58127393992"></a><a name="p58127393992"></a>≥ 0 ms</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p15783187135411"><a name="p15783187135411"></a><a name="p15783187135411"></a>Monitored object: database</p>
<p id="p7830959135411"><a name="p7830959135411"></a><a name="p7830959135411"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p17857426336"><a name="p17857426336"></a><a name="p17857426336"></a>1 minute</p>
</td>
</tr>
<tr id="row5950517415252"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p33965557151411"><a name="p33965557151411"></a><a name="p33965557151411"></a>rds047_disk_total_size</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p4325656715335"><a name="p4325656715335"></a><a name="p4325656715335"></a>Total Storage Space</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p1412103815335"><a name="p1412103815335"></a><a name="p1412103815335"></a>Total storage space of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p1878135135412"><a name="p1878135135412"></a><a name="p1878135135412"></a>40–4000 GB</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p4475175854814"><a name="p4475175854814"></a><a name="p4475175854814"></a>Monitored object: database</p>
<p id="p18475658134817"><a name="p18475658134817"></a><a name="p18475658134817"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p885712143311"><a name="p885712143311"></a><a name="p885712143311"></a>1 minute</p>
</td>
</tr>
<tr id="row661168615252"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p64829489151411"><a name="p64829489151411"></a><a name="p64829489151411"></a>rds048_disk_used_size</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p556084315335"><a name="p556084315335"></a><a name="p556084315335"></a>Used Storage Space</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p4777512715335"><a name="p4777512715335"></a><a name="p4777512715335"></a>Used storage space of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p119971303217"><a name="p119971303217"></a><a name="p119971303217"></a>0–4000 GB</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p10102103114918"><a name="p10102103114918"></a><a name="p10102103114918"></a>Monitored object: database</p>
<p id="p19102163194917"><a name="p19102163194917"></a><a name="p19102163194917"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p085711219335"><a name="p085711219335"></a><a name="p085711219335"></a>1 minute</p>
</td>
</tr>
<tr id="row73463115252"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p16057739151411"><a name="p16057739151411"></a><a name="p16057739151411"></a>rds049_disk_read_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p1815837015335"><a name="p1815837015335"></a><a name="p1815837015335"></a>Disk Read Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p6154185215335"><a name="p6154185215335"></a><a name="p6154185215335"></a>Number of bytes read from the disk per second</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p1883413515335"><a name="p1883413515335"></a><a name="p1883413515335"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p5201188184910"><a name="p5201188184910"></a><a name="p5201188184910"></a>Monitored object: database</p>
<p id="p1620138134911"><a name="p1620138134911"></a><a name="p1620138134911"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p18574203310"><a name="p18574203310"></a><a name="p18574203310"></a>1 minute</p>
</td>
</tr>
<tr id="row1499470615252"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p29149396151411"><a name="p29149396151411"></a><a name="p29149396151411"></a>rds050_disk_write_throughput</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p3987662715335"><a name="p3987662715335"></a><a name="p3987662715335"></a>Disk Write Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p878135015335"><a name="p878135015335"></a><a name="p878135015335"></a>Number of bytes written into the disk per second</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p4020075815335"><a name="p4020075815335"></a><a name="p4020075815335"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p187815211496"><a name="p187815211496"></a><a name="p187815211496"></a>Monitored object: database</p>
<p id="p11781182113494"><a name="p11781182113494"></a><a name="p11781182113494"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p2085752133311"><a name="p2085752133311"></a><a name="p2085752133311"></a>1 minute</p>
</td>
</tr>
<tr id="row5386186115252"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p43508968151411"><a name="p43508968151411"></a><a name="p43508968151411"></a>rds075_avg_disk_sec_per_read</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p4688806115335"><a name="p4688806115335"></a><a name="p4688806115335"></a>Disk Read Time</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p3983661115335"><a name="p3983661115335"></a><a name="p3983661115335"></a>Average time required for each disk read in a specified period</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p554006515335"><a name="p554006515335"></a><a name="p554006515335"></a>&gt; 0ms</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p4618826194911"><a name="p4618826194911"></a><a name="p4618826194911"></a>Monitored object: database</p>
<p id="p1761815269492"><a name="p1761815269492"></a><a name="p1761815269492"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p16857202113317"><a name="p16857202113317"></a><a name="p16857202113317"></a>1 minute</p>
</td>
</tr>
<tr id="row1344119115252"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p42654571151411"><a name="p42654571151411"></a><a name="p42654571151411"></a>rds052_avg_disk_sec_per_write</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p1217626415335"><a name="p1217626415335"></a><a name="p1217626415335"></a>Disk Write Time</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p4675329015335"><a name="p4675329015335"></a><a name="p4675329015335"></a>Average time required for each disk write in a specified period</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p2892016115335"><a name="p2892016115335"></a><a name="p2892016115335"></a>&gt; 0s</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p13932735164915"><a name="p13932735164915"></a><a name="p13932735164915"></a>Monitored object: database</p>
<p id="p493223564912"><a name="p493223564912"></a><a name="p493223564912"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p1785714263316"><a name="p1785714263316"></a><a name="p1785714263316"></a>1 minute</p>
</td>
</tr>
<tr id="row3877616715252"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.1 "><p id="p23778695151411"><a name="p23778695151411"></a><a name="p23778695151411"></a>rds053_avg_disk_queue_length</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.2 "><p id="p1061468915335"><a name="p1061468915335"></a><a name="p1061468915335"></a>Average Disk Queue Length</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.3 "><p id="p5448348215335"><a name="p5448348215335"></a><a name="p5448348215335"></a>Number of processes to be written into the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.4 "><p id="p5108595615335"><a name="p5108595615335"></a><a name="p5108595615335"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.7.1.5 "><p id="p4244740114914"><a name="p4244740114914"></a><a name="p4244740114914"></a>Monitored object: database</p>
<p id="p16244140114919"><a name="p16244140114919"></a><a name="p16244140114919"></a>Monitored instance type: PostgreSQL instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.7.1.6 "><p id="p385711273316"><a name="p385711273316"></a><a name="p385711273316"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="section137792512494"></a>

<a name="table1635911412509"></a>
<table><thead align="left"><tr id="row83591416507"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p8359547503"><a name="p8359547503"></a><a name="p8359547503"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p235984105013"><a name="p235984105013"></a><a name="p235984105013"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row153601641503"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1636013465020"><a name="p1636013465020"></a><a name="p1636013465020"></a>postgresql_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1536013465018"><a name="p1536013465018"></a><a name="p1536013465018"></a>PostgreSQL DB instance ID</p>
</td>
</tr>
</tbody>
</table>

