# Related Services<a name="EN-US_TOPIC_0237964710"></a>

## Virtual Private Cloud \(VPC\)<a name="section18389930"></a>

The VPC service enables users to create private, isolated virtual networks. DCS instances run in VPCs and use the IP addresses and bandwidths of VPCs. VPCs are based on security groups. A security group is a set of access control rules that implements access control for mutually trusted ECSs with the same security protection requirements in the same VPC.

## Elastic Cloud Server \(ECS\)<a name="section31291646"></a>

The ECS service provides scalable, on-demand cloud servers for secure, flexible, and efficient application environments, ensuring service reliability. After you create DCS instances, you can connect to them through ECSs.

## Cloud Trace Service \(CTS\)<a name="section13189358"></a>

CTS provides a history of operations performed on cloud service resources. With CTS, you can query, audit, and review operations. Traces include operation time, resource objects, resource IDs, requesters' IP addresses, resource operation requests, and responses.

Currently, CTS records the following operations on DCS instances:

-   Creating, starting, stopping, restarting, and deleting DCS instances
-   Configuring Redis-specific parameters
-   Changing instance passwords
-   Modifying basic information

## Identity and Access Management \(IAM\)<a name="section51595365"></a>

IAM provides identity authentication and permission management. It is used to authenticate access to DCS.

## Cloud Eye<a name="section61705107"></a>

Cloud Eye is a secure, scalable monitoring platform. It monitors DCS service metrics and sends notifications if alarms or events occur.

**Table  1**  DCS monitoring metrics displayed on the Cloud Eye console

<a name="table37368736"></a>
<table><thead align="left"><tr id="row16468652"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p58892473"><a name="p58892473"></a><a name="p58892473"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="37%" id="mcps1.2.5.1.2"><p id="p5560998"><a name="p5560998"></a><a name="p5560998"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.3"><p id="p47787675"><a name="p47787675"></a><a name="p47787675"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.4"><p id="p45596481"><a name="p45596481"></a><a name="p45596481"></a>Monitored Object</p>
</th>
</tr>
</thead>
<tbody><tr id="row2327487"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p54308798"><a name="p54308798"></a><a name="p54308798"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p36936550"><a name="p36936550"></a><a name="p36936550"></a>CPU consumed by monitored objects</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p39070558"><a name="p39070558"></a><a name="p39070558"></a>0% to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p10598606"><a name="p10598606"></a><a name="p10598606"></a>ECS</p>
</td>
</tr>
<tr id="row28278595"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p8864859"><a name="p8864859"></a><a name="p8864859"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p46964992"><a name="p46964992"></a><a name="p46964992"></a>Memory consumed by monitored objects</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p46067993"><a name="p46067993"></a><a name="p46067993"></a>0% to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p40519951"><a name="p40519951"></a><a name="p40519951"></a>ECS</p>
</td>
</tr>
<tr id="row29135240"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p11144211"><a name="p11144211"></a><a name="p11144211"></a>Network Input Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p30265903"><a name="p30265903"></a><a name="p30265903"></a>Inbound throughput per second on a port</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p35619075"><a name="p35619075"></a><a name="p35619075"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p66572856"><a name="p66572856"></a><a name="p66572856"></a>ECS</p>
</td>
</tr>
<tr id="row62284798"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p11903911"><a name="p11903911"></a><a name="p11903911"></a>Network Output Throughput</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p24692740"><a name="p24692740"></a><a name="p24692740"></a>Outbound throughput per second on a port</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p53954942"><a name="p53954942"></a><a name="p53954942"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p8274172"><a name="p8274172"></a><a name="p8274172"></a>ECS</p>
</td>
</tr>
<tr id="row7358688"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p59182880"><a name="p59182880"></a><a name="p59182880"></a>Connected Clients</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p29083993"><a name="p29083993"></a><a name="p29083993"></a>Number of connected clients, including connections established by the DCS server (a management service in the background) to monitor DCS instances and excluding connections from standby nodes</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p6993202"><a name="p6993202"></a><a name="p6993202"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p29578451"><a name="p29578451"></a><a name="p29578451"></a>DCS</p>
</td>
</tr>
<tr id="row64879470"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p20745743"><a name="p20745743"></a><a name="p20745743"></a>Client Longest Output List</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p2683661"><a name="p2683661"></a><a name="p2683661"></a>Longest output list among current client connections</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p16049999"><a name="p16049999"></a><a name="p16049999"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p24981566"><a name="p24981566"></a><a name="p24981566"></a>DCS</p>
</td>
</tr>
<tr id="row23507505"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p25059790"><a name="p25059790"></a><a name="p25059790"></a>Client Biggest Input Buf</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p16577099"><a name="p16577099"></a><a name="p16577099"></a>Maximum input data length among current client connections</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p567760"><a name="p567760"></a><a name="p567760"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p45988614"><a name="p45988614"></a><a name="p45988614"></a>DCS</p>
</td>
</tr>
<tr id="row11244347"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p38376892"><a name="p38376892"></a><a name="p38376892"></a>Blocked Clients</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p21520579"><a name="p21520579"></a><a name="p21520579"></a>Number of clients suspended by block operations, such as BLPOP, BRPOP, and BRPOPLPUSH</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p65445301"><a name="p65445301"></a><a name="p65445301"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p66578044"><a name="p66578044"></a><a name="p66578044"></a>DCS</p>
</td>
</tr>
<tr id="row62331491"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p15686020"><a name="p15686020"></a><a name="p15686020"></a>Used Memory</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p62608109"><a name="p62608109"></a><a name="p62608109"></a>Total number of bytes allocated by Redis using its allocator</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p38092103"><a name="p38092103"></a><a name="p38092103"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p65561530"><a name="p65561530"></a><a name="p65561530"></a>DCS</p>
</td>
</tr>
<tr id="row53182860"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p12844374"><a name="p12844374"></a><a name="p12844374"></a>Used Memory RSS</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p33761356"><a name="p33761356"></a><a name="p33761356"></a>Number of bytes that Redis allocates as seen by the operating system (a.k.a resident set size).</p>
<p id="p35416756"><a name="p35416756"></a><a name="p35416756"></a>It includes all stack and heap memory but not swapped-out memory.</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p50184984"><a name="p50184984"></a><a name="p50184984"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p38451933"><a name="p38451933"></a><a name="p38451933"></a>DCS</p>
</td>
</tr>
<tr id="row10523083"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p47063428"><a name="p47063428"></a><a name="p47063428"></a>Used Memory Peak</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p54041329"><a name="p54041329"></a><a name="p54041329"></a>Peak memory consumed by Redis since the Redis server last started</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p15271547"><a name="p15271547"></a><a name="p15271547"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p29035785"><a name="p29035785"></a><a name="p29035785"></a>DCS</p>
</td>
</tr>
<tr id="row59995477"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p27795493"><a name="p27795493"></a><a name="p27795493"></a>Used Memory Lua</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p36842478"><a name="p36842478"></a><a name="p36842478"></a>Number of bytes used by the Lua engine</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p31450711"><a name="p31450711"></a><a name="p31450711"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p64479624"><a name="p64479624"></a><a name="p64479624"></a>DCS</p>
</td>
</tr>
<tr id="row43445707"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p29441404"><a name="p29441404"></a><a name="p29441404"></a>Memory Fragmentation Ratio</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p35943562"><a name="p35943562"></a><a name="p35943562"></a>Ratio between Used Memory RSS and Used Memory.</p>
<p id="p55056607"><a name="p55056607"></a><a name="p55056607"></a>Ideally, the Used Memory RSS should be only slightly higher than Used Memory. When Used Memory RSS is much greater than Used Memory, there is memory fragmentation (internal or external), which can be evaluated by checking Memory Fragmentation Ratio.</p>
<p id="p25747420"><a name="p25747420"></a><a name="p25747420"></a>When Used Memory is much greater than Used Memory RSS, part of Redis memory has been swapped out by the operating system. In this case, significant latency can be expected.</p>
<p id="p30400195"><a name="p30400195"></a><a name="p30400195"></a>Because Redis does not have control over how its allocations are mapped to memory pages, high Used Memory RSS is often the result of a spike in memory usage.</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p46496694"><a name="p46496694"></a><a name="p46496694"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p8135907"><a name="p8135907"></a><a name="p8135907"></a>DCS</p>
</td>
</tr>
<tr id="row6114302"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p25496434"><a name="p25496434"></a><a name="p25496434"></a>Total Connections Received</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p51945267"><a name="p51945267"></a><a name="p51945267"></a>Total number of connections the Redis server has received since it last started, including connections established by the DCS server (a management service in the background) to monitor DCS instances</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p46817064"><a name="p46817064"></a><a name="p46817064"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p34085817"><a name="p34085817"></a><a name="p34085817"></a>DCS</p>
</td>
</tr>
<tr id="row38336904"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p18281552"><a name="p18281552"></a><a name="p18281552"></a>Total Commands Processed</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p4410728"><a name="p4410728"></a><a name="p4410728"></a>Total number of commands the Redis server has processed since it last started, including commands issued by the DCS server (a management service in the background) to monitor DCS instances</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p21724664"><a name="p21724664"></a><a name="p21724664"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p14867369"><a name="p14867369"></a><a name="p14867369"></a>DCS</p>
</td>
</tr>
<tr id="row66697461"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p33785274"><a name="p33785274"></a><a name="p33785274"></a>Instantaneous Ops per Second</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p52252659"><a name="p52252659"></a><a name="p52252659"></a>Number of commands processed per second</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p4606985"><a name="p4606985"></a><a name="p4606985"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p37621475"><a name="p37621475"></a><a name="p37621475"></a>DCS</p>
</td>
</tr>
<tr id="row3048957"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p45638969"><a name="p45638969"></a><a name="p45638969"></a>Total Net Input Bytes</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p5769005"><a name="p5769005"></a><a name="p5769005"></a>Total number of bytes the Redis server has received since it last started</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p64636290"><a name="p64636290"></a><a name="p64636290"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p1048160"><a name="p1048160"></a><a name="p1048160"></a>DCS</p>
</td>
</tr>
<tr id="row9433441"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p25911262"><a name="p25911262"></a><a name="p25911262"></a>Total Net Output Bytes</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p18437496"><a name="p18437496"></a><a name="p18437496"></a>Total number of bytes the Redis server has sent since it last started</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p17042198"><a name="p17042198"></a><a name="p17042198"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p38240801"><a name="p38240801"></a><a name="p38240801"></a>DCS</p>
</td>
</tr>
<tr id="row8622890"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p27365507"><a name="p27365507"></a><a name="p27365507"></a>Instantaneous Input Kbps</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p2013564"><a name="p2013564"></a><a name="p2013564"></a>Instantaneous input traffic</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p28880957"><a name="p28880957"></a><a name="p28880957"></a>≥ 0 kbit/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p57656175"><a name="p57656175"></a><a name="p57656175"></a>DCS</p>
</td>
</tr>
<tr id="row49143529"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p21202951"><a name="p21202951"></a><a name="p21202951"></a>Instantaneous Output Kbps</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p39717481"><a name="p39717481"></a><a name="p39717481"></a>Instantaneous output traffic</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p62999416"><a name="p62999416"></a><a name="p62999416"></a>≥ 0 kbit/s</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p2679067"><a name="p2679067"></a><a name="p2679067"></a>DCS</p>
</td>
</tr>
<tr id="row24111608"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p6883221"><a name="p6883221"></a><a name="p6883221"></a>Rejected Connections</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p20670010"><a name="p20670010"></a><a name="p20670010"></a>Number of connections that have exceeded maxclients and been rejected by the Redis server since it last started</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p63658128"><a name="p63658128"></a><a name="p63658128"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p56034750"><a name="p56034750"></a><a name="p56034750"></a>DCS</p>
</td>
</tr>
<tr id="row34550710"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p47144157"><a name="p47144157"></a><a name="p47144157"></a>Sync Full</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p60580335"><a name="p60580335"></a><a name="p60580335"></a>Total number of full synchronizations since the Redis server last started</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p8060118"><a name="p8060118"></a><a name="p8060118"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p48889850"><a name="p48889850"></a><a name="p48889850"></a>DCS</p>
</td>
</tr>
<tr id="row37355470"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p5894231"><a name="p5894231"></a><a name="p5894231"></a>Sync Partial OK</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p7670737"><a name="p7670737"></a><a name="p7670737"></a>Total number of successful incremental synchronizations since the Redis server last started</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p17349988"><a name="p17349988"></a><a name="p17349988"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p63171767"><a name="p63171767"></a><a name="p63171767"></a>DCS</p>
</td>
</tr>
<tr id="row31674992"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p15537542"><a name="p15537542"></a><a name="p15537542"></a>Sync Partial Err</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p50581426"><a name="p50581426"></a><a name="p50581426"></a>Total number of failed incremental synchronizations since the Redis server last started</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p3454809"><a name="p3454809"></a><a name="p3454809"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p11404133"><a name="p11404133"></a><a name="p11404133"></a>DCS</p>
</td>
</tr>
<tr id="row35528341"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p59223347"><a name="p59223347"></a><a name="p59223347"></a>Expired Keys</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p32361769"><a name="p32361769"></a><a name="p32361769"></a>Total number of keys that have expired since the Redis server last started</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p4057632"><a name="p4057632"></a><a name="p4057632"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p60232767"><a name="p60232767"></a><a name="p60232767"></a>DCS</p>
</td>
</tr>
<tr id="row5223998"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p20490669"><a name="p20490669"></a><a name="p20490669"></a>Evicted Keys</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p49131481"><a name="p49131481"></a><a name="p49131481"></a>Number of keys that have been evicted due to insufficient memory since the Redis server last started</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p20226985"><a name="p20226985"></a><a name="p20226985"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p27773061"><a name="p27773061"></a><a name="p27773061"></a>DCS</p>
</td>
</tr>
<tr id="row48630964"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p46793998"><a name="p46793998"></a><a name="p46793998"></a>Keyspace Hits</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p32217513"><a name="p32217513"></a><a name="p32217513"></a>Total number of query hits in the master dictionary since the Redis server last started</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p59481773"><a name="p59481773"></a><a name="p59481773"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p53294272"><a name="p53294272"></a><a name="p53294272"></a>DCS</p>
</td>
</tr>
<tr id="row9886408"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p62601592"><a name="p62601592"></a><a name="p62601592"></a>Keyspace Misses</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p37564172"><a name="p37564172"></a><a name="p37564172"></a>Total number of query misses in the master dictionary since the Redis server last started</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p22799085"><a name="p22799085"></a><a name="p22799085"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p34786562"><a name="p34786562"></a><a name="p34786562"></a>DCS</p>
</td>
</tr>
<tr id="row44643603"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p59362130"><a name="p59362130"></a><a name="p59362130"></a>PubSub Channels</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p43603258"><a name="p43603258"></a><a name="p43603258"></a>Number of Pub/Sub channels</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p42202994"><a name="p42202994"></a><a name="p42202994"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p62999330"><a name="p62999330"></a><a name="p62999330"></a>DCS</p>
</td>
</tr>
<tr id="row30123063"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p24049039"><a name="p24049039"></a><a name="p24049039"></a>PubSub Patterns</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p1815156"><a name="p1815156"></a><a name="p1815156"></a>Number of Pub/Sub patterns</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p12809933"><a name="p12809933"></a><a name="p12809933"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p30971651"><a name="p30971651"></a><a name="p30971651"></a>DCS</p>
</td>
</tr>
<tr id="row10309404"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p29755367"><a name="p29755367"></a><a name="p29755367"></a>Aof Current Size</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p61374531"><a name="p61374531"></a><a name="p61374531"></a>AOF file size</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p5281111"><a name="p5281111"></a><a name="p5281111"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p25116876"><a name="p25116876"></a><a name="p25116876"></a>DCS</p>
</td>
</tr>
<tr id="row24725298"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p56592155"><a name="p56592155"></a><a name="p56592155"></a>Latest Fork usec</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.5.1.2 "><p id="p20561848"><a name="p20561848"></a><a name="p20561848"></a>Duration of the latest fork operation</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p54897010"><a name="p54897010"></a><a name="p54897010"></a>≥ 0 ms</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.4 "><p id="p17472816"><a name="p17472816"></a><a name="p17472816"></a>DCS</p>
</td>
</tr>
</tbody>
</table>

