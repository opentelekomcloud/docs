# DMS Metrics<a name="EN-US_TOPIC_0143117152"></a>

## Function<a name="section337847172818"></a>

This section describes DMS metrics reported to Cloud Eye as well as their namespace and dimensions. You can use the Cloud Eye console to query the DMS metrics and alarms.

For more information about the namespace and dimensions, see the "Querying Monitoring Data" section in the  _Cloud Eye API Reference_.

## Namespace<a name="section6441231194316"></a>

SYS.DMS

## Standard Queue Metrics<a name="section16253740145310"></a>

**Table  1**  Standard queue metrics

<a name="table196122331719"></a>
<table><thead align="left"><tr id="row96152033215"><th class="cellrowborder" valign="top" width="11.42%" id="mcps1.2.7.1.1"><p id="p11644154112118"><a name="p11644154112118"></a><a name="p11644154112118"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="11.14%" id="mcps1.2.7.1.2"><p id="p1061818334114"><a name="p1061818334114"></a><a name="p1061818334114"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="39.82%" id="mcps1.2.7.1.3"><p id="p18619203317114"><a name="p18619203317114"></a><a name="p18619203317114"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="15.06%" id="mcps1.2.7.1.4"><p id="p134404318212"><a name="p134404318212"></a><a name="p134404318212"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="14.32%" id="mcps1.2.7.1.5"><p id="p459214820316"><a name="p459214820316"></a><a name="p459214820316"></a>Monitored Objects and Dimensions</p>
</th>
<th class="cellrowborder" valign="top" width="8.24%" id="mcps1.2.7.1.6"><p id="p212119231536"><a name="p212119231536"></a><a name="p212119231536"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row562043317112"><td class="cellrowborder" valign="top" width="11.42%" headers="mcps1.2.7.1.1 "><p id="p1644134118118"><a name="p1644134118118"></a><a name="p1644134118118"></a>queued_messages</p>
</td>
<td class="cellrowborder" valign="top" width="11.14%" headers="mcps1.2.7.1.2 "><p id="p76211233812"><a name="p76211233812"></a><a name="p76211233812"></a>Queued Messages</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.7.1.3 "><p id="p96211233213"><a name="p96211233213"></a><a name="p96211233213"></a>The current number of messages in a queue.</p>
<p id="p1217575005215"><a name="p1217575005215"></a><a name="p1217575005215"></a>Messages older than 72 hours will be deleted from a queue and deleted messages are not counted into the metric.</p>
<p id="p96221334118"><a name="p96221334118"></a><a name="p96221334118"></a>Dead letter messages are specific to consumer groups and stored in dead letter queues. Therefore, generation and expiry of dead letter messages do not affect the metric.</p>
<p id="p1137713118446"><a name="p1137713118446"></a><a name="p1137713118446"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.06%" headers="mcps1.2.7.1.4 "><p id="p244104318211"><a name="p244104318211"></a><a name="p244104318211"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.32%" headers="mcps1.2.7.1.5 "><p id="p19789195131814"><a name="p19789195131814"></a><a name="p19789195131814"></a>Monitored object: DMS</p>
<p id="p1378985131815"><a name="p1378985131815"></a><a name="p1378985131815"></a>Dimension:</p>
<p id="p17789135121817"><a name="p17789135121817"></a><a name="p17789135121817"></a>queue_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.24%" headers="mcps1.2.7.1.6 "><p id="p19121823635"><a name="p19121823635"></a><a name="p19121823635"></a>1 minute</p>
</td>
</tr>
<tr id="row11623173314110"><td class="cellrowborder" valign="top" width="11.42%" headers="mcps1.2.7.1.1 "><p id="p764516417112"><a name="p764516417112"></a><a name="p764516417112"></a>message_size</p>
</td>
<td class="cellrowborder" valign="top" width="11.14%" headers="mcps1.2.7.1.2 "><p id="p1262310331618"><a name="p1262310331618"></a><a name="p1262310331618"></a>Message Size</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.7.1.3 "><p id="p18625183315119"><a name="p18625183315119"></a><a name="p18625183315119"></a>Total size of messages sent to a queue during the previous one minute.</p>
<p id="p13625933214"><a name="p13625933214"></a><a name="p13625933214"></a>This metric gives you an overview of the message load flowing into a queue.</p>
<p id="p19301105113448"><a name="p19301105113448"></a><a name="p19301105113448"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="15.06%" headers="mcps1.2.7.1.4 "><p id="p154410431826"><a name="p154410431826"></a><a name="p154410431826"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.32%" headers="mcps1.2.7.1.5 "><p id="p1282310227193"><a name="p1282310227193"></a><a name="p1282310227193"></a>Monitored object: DMS</p>
<p id="p382352217194"><a name="p382352217194"></a><a name="p382352217194"></a>Dimension:</p>
<p id="p1823172281919"><a name="p1823172281919"></a><a name="p1823172281919"></a>queue_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.24%" headers="mcps1.2.7.1.6 "><p id="p1812117231332"><a name="p1812117231332"></a><a name="p1812117231332"></a>1 minute</p>
</td>
</tr>
<tr id="row1462619334118"><td class="cellrowborder" valign="top" width="11.42%" headers="mcps1.2.7.1.1 "><p id="p16645941710"><a name="p16645941710"></a><a name="p16645941710"></a>request_count</p>
</td>
<td class="cellrowborder" valign="top" width="11.14%" headers="mcps1.2.7.1.2 "><p id="p9626833515"><a name="p9626833515"></a><a name="p9626833515"></a>Request Count</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.7.1.3 "><p id="p362716339118"><a name="p362716339118"></a><a name="p362716339118"></a>The total number of requests sent to a queue during the previous one minute.</p>
<p id="p16382816104511"><a name="p16382816104511"></a><a name="p16382816104511"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.06%" headers="mcps1.2.7.1.4 "><p id="p5762202014514"><a name="p5762202014514"></a><a name="p5762202014514"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.32%" headers="mcps1.2.7.1.5 "><p id="p9166625183416"><a name="p9166625183416"></a><a name="p9166625183416"></a>Monitored object: DMS</p>
<p id="p11166925143413"><a name="p11166925143413"></a><a name="p11166925143413"></a>Dimension:</p>
<p id="p5166162583417"><a name="p5166162583417"></a><a name="p5166162583417"></a>queue_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.24%" headers="mcps1.2.7.1.6 "><p id="p15121162317312"><a name="p15121162317312"></a><a name="p15121162317312"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Metrics of consumer groups in standard queues

<a name="table054516146361"></a>
<table><thead align="left"><tr id="row45451143365"><th class="cellrowborder" valign="top" width="11.86%" id="mcps1.2.7.1.1"><p id="p15545131433617"><a name="p15545131433617"></a><a name="p15545131433617"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="10.7%" id="mcps1.2.7.1.2"><p id="p1546101413365"><a name="p1546101413365"></a><a name="p1546101413365"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="39.82%" id="mcps1.2.7.1.3"><p id="p16546161443618"><a name="p16546161443618"></a><a name="p16546161443618"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="15.06%" id="mcps1.2.7.1.4"><p id="p10546314183615"><a name="p10546314183615"></a><a name="p10546314183615"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="14.32%" id="mcps1.2.7.1.5"><p id="p125461614123611"><a name="p125461614123611"></a><a name="p125461614123611"></a>Monitored Objects and Dimensions</p>
</th>
<th class="cellrowborder" valign="top" width="8.24%" id="mcps1.2.7.1.6"><p id="p185461414153617"><a name="p185461414153617"></a><a name="p185461414153617"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row1054741453619"><td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.2.7.1.1 "><p id="p1054731419361"><a name="p1054731419361"></a><a name="p1054731419361"></a>dead_avail_messages</p>
</td>
<td class="cellrowborder" valign="top" width="10.7%" headers="mcps1.2.7.1.2 "><p id="p654715147368"><a name="p654715147368"></a><a name="p654715147368"></a>Accumulated Messages</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.7.1.3 "><p id="p254716141365"><a name="p254716141365"></a><a name="p254716141365"></a>The current number of messages that are not retrieved by a consumer group.</p>
<p id="p254717144360"><a name="p254717144360"></a><a name="p254717144360"></a>Messages older than 72 hours will be deleted from a queue. Deleted messages can no longer be retrieved by a consumer group and therefore are not included in the count.</p>
<p id="p1454721410366"><a name="p1454721410366"></a><a name="p1454721410366"></a>Dead letter messages are flagged as retrieved messages and therefore are not included in the count.</p>
<p id="p1754575864516"><a name="p1754575864516"></a><a name="p1754575864516"></a>Unit: Count</p>
<p id="p15879203144512"><a name="p15879203144512"></a><a name="p15879203144512"></a></p>
</td>
<td class="cellrowborder" valign="top" width="15.06%" headers="mcps1.2.7.1.4 "><p id="p0258936104519"><a name="p0258936104519"></a><a name="p0258936104519"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.32%" headers="mcps1.2.7.1.5 "><p id="p65477144368"><a name="p65477144368"></a><a name="p65477144368"></a>Monitored object: DMS</p>
<p id="p9547114133614"><a name="p9547114133614"></a><a name="p9547114133614"></a>Dimension:</p>
<p id="p13547121453620"><a name="p13547121453620"></a><a name="p13547121453620"></a>group_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.24%" headers="mcps1.2.7.1.6 "><p id="p15547914123616"><a name="p15547914123616"></a><a name="p15547914123616"></a>1 minute</p>
</td>
</tr>
<tr id="row14547101412369"><td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.2.7.1.1 "><p id="p1547161420366"><a name="p1547161420366"></a><a name="p1547161420366"></a>consumed_messages</p>
</td>
<td class="cellrowborder" valign="top" width="10.7%" headers="mcps1.2.7.1.2 "><p id="p18547314183616"><a name="p18547314183616"></a><a name="p18547314183616"></a>Retrieved Messages</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.7.1.3 "><p id="p105480140362"><a name="p105480140362"></a><a name="p105480140362"></a>The accumulated number of messages retrieved by a consumer group.</p>
<p id="p2548111423613"><a name="p2548111423613"></a><a name="p2548111423613"></a>The count is accumulated since a consumer group is created.</p>
<p id="p195480147360"><a name="p195480147360"></a><a name="p195480147360"></a>Dead letter messages are counted into the metric because dead letter messages are flagged as retrieved messages.</p>
<p id="p1752318294618"><a name="p1752318294618"></a><a name="p1752318294618"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.06%" headers="mcps1.2.7.1.4 "><p id="p33211243114510"><a name="p33211243114510"></a><a name="p33211243114510"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.32%" headers="mcps1.2.7.1.5 "><p id="p15548101483616"><a name="p15548101483616"></a><a name="p15548101483616"></a>Monitored object: DMS</p>
<p id="p3548514113619"><a name="p3548514113619"></a><a name="p3548514113619"></a>Dimension:</p>
<p id="p1454811149369"><a name="p1454811149369"></a><a name="p1454811149369"></a>group_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.24%" headers="mcps1.2.7.1.6 "><p id="p135481514103611"><a name="p135481514103611"></a><a name="p135481514103611"></a>1 minute</p>
</td>
</tr>
<tr id="row145481814133620"><td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.2.7.1.1 "><p id="p054851403620"><a name="p054851403620"></a><a name="p054851403620"></a>skipped_messages</p>
</td>
<td class="cellrowborder" valign="top" width="10.7%" headers="mcps1.2.7.1.2 "><p id="p10548614183612"><a name="p10548614183612"></a><a name="p10548614183612"></a>Skipped Messages</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.7.1.3 "><p id="p17548181413619"><a name="p17548181413619"></a><a name="p17548181413619"></a>Accumulated number of messages that have been deleted and never retrieved.</p>
<p id="p1554831463618"><a name="p1554831463618"></a><a name="p1554831463618"></a>The count is accumulated since a consumer group is created.</p>
<p id="p05481614153612"><a name="p05481614153612"></a><a name="p05481614153612"></a>Messages are stored for at least 72 hours. Messages older than 72 hours will be deleted from the queue. Deleted messages can no longer be retrieved by a consumer group.</p>
<p id="p12359719465"><a name="p12359719465"></a><a name="p12359719465"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.06%" headers="mcps1.2.7.1.4 "><p id="p173368475452"><a name="p173368475452"></a><a name="p173368475452"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.32%" headers="mcps1.2.7.1.5 "><p id="p75481914133611"><a name="p75481914133611"></a><a name="p75481914133611"></a>Monitored object: DMS</p>
<p id="p1054821463613"><a name="p1054821463613"></a><a name="p1054821463613"></a>Dimension:</p>
<p id="p154841483611"><a name="p154841483611"></a><a name="p154841483611"></a>group_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.24%" headers="mcps1.2.7.1.6 "><p id="p1954811143361"><a name="p1954811143361"></a><a name="p1954811143361"></a>1 minute</p>
</td>
</tr>
<tr id="row65489145369"><td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.2.7.1.1 "><p id="p75481114103610"><a name="p75481114103610"></a><a name="p75481114103610"></a>dead_avail_messages</p>
</td>
<td class="cellrowborder" valign="top" width="10.7%" headers="mcps1.2.7.1.2 "><p id="p14548151419367"><a name="p14548151419367"></a><a name="p14548151419367"></a>Available Dead Letter Messages</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.7.1.3 "><p id="p95481014173612"><a name="p95481014173612"></a><a name="p95481014173612"></a>The current number of dead letter messages that are not retrieved by a consumer group.</p>
<p id="p954841413610"><a name="p954841413610"></a><a name="p954841413610"></a>Messages older than 72 hours will be deleted from a queue. Deleted messages can no longer be retrieved by a consumer group and therefore are not included in the count.</p>
<p id="p17884974616"><a name="p17884974616"></a><a name="p17884974616"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.06%" headers="mcps1.2.7.1.4 "><p id="p2536124917457"><a name="p2536124917457"></a><a name="p2536124917457"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.32%" headers="mcps1.2.7.1.5 "><p id="p8548131413369"><a name="p8548131413369"></a><a name="p8548131413369"></a>Monitored object: DMS</p>
<p id="p13548171463613"><a name="p13548171463613"></a><a name="p13548171463613"></a>Dimension:</p>
<p id="p17548121483614"><a name="p17548121483614"></a><a name="p17548121483614"></a>group_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.24%" headers="mcps1.2.7.1.6 "><p id="p35483140365"><a name="p35483140365"></a><a name="p35483140365"></a>1 minute</p>
</td>
</tr>
<tr id="row35487146364"><td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.2.7.1.1 "><p id="p13549614133612"><a name="p13549614133612"></a><a name="p13549614133612"></a>dead_his_messages</p>
</td>
<td class="cellrowborder" valign="top" width="10.7%" headers="mcps1.2.7.1.2 "><p id="p7549171463617"><a name="p7549171463617"></a><a name="p7549171463617"></a>Historical Dead Letter Messages</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.7.1.3 "><p id="p154971412363"><a name="p154971412363"></a><a name="p154971412363"></a>The accumulated number of dead letter messages generated for a consumer group since the consumer group is created. The count of historical dead letter messages includes the retrieved dead letter messages, remaining dead letter messages, and expired dead letter messages.</p>
<p id="p6388101218468"><a name="p6388101218468"></a><a name="p6388101218468"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.06%" headers="mcps1.2.7.1.4 "><p id="p1166715184515"><a name="p1166715184515"></a><a name="p1166715184515"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.32%" headers="mcps1.2.7.1.5 "><p id="p7549121433612"><a name="p7549121433612"></a><a name="p7549121433612"></a>Monitored object: DMS</p>
<p id="p25495141369"><a name="p25495141369"></a><a name="p25495141369"></a>Dimension:</p>
<p id="p175499146363"><a name="p175499146363"></a><a name="p175499146363"></a>group_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.24%" headers="mcps1.2.7.1.6 "><p id="p654981415366"><a name="p654981415366"></a><a name="p654981415366"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

## Kafka Queues \(Non-Premium\) Metrics<a name="section16277161107"></a>

**Table  3**  Metrics of Kafka queues \(non-premium\)

<a name="table26431938164819"></a>
<table><thead align="left"><tr id="row1643183815489"><th class="cellrowborder" valign="top" width="11.42%" id="mcps1.2.7.1.1"><p id="p564315384489"><a name="p564315384489"></a><a name="p564315384489"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="11.14%" id="mcps1.2.7.1.2"><p id="p11643143811481"><a name="p11643143811481"></a><a name="p11643143811481"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="39.82%" id="mcps1.2.7.1.3"><p id="p56431538194815"><a name="p56431538194815"></a><a name="p56431538194815"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="15.06%" id="mcps1.2.7.1.4"><p id="p1264312385486"><a name="p1264312385486"></a><a name="p1264312385486"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="14.32%" id="mcps1.2.7.1.5"><p id="p186432038114817"><a name="p186432038114817"></a><a name="p186432038114817"></a>Monitored Objects and Dimensions</p>
</th>
<th class="cellrowborder" valign="top" width="8.24%" id="mcps1.2.7.1.6"><p id="p116441388486"><a name="p116441388486"></a><a name="p116441388486"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row864433815483"><td class="cellrowborder" valign="top" width="11.42%" headers="mcps1.2.7.1.1 "><p id="p1164410383486"><a name="p1164410383486"></a><a name="p1164410383486"></a>queued_messages</p>
</td>
<td class="cellrowborder" valign="top" width="11.14%" headers="mcps1.2.7.1.2 "><p id="p764483817486"><a name="p764483817486"></a><a name="p764483817486"></a>Queued Messages</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.7.1.3 "><p id="p46441238104818"><a name="p46441238104818"></a><a name="p46441238104818"></a>The current number of messages in a queue.</p>
<p id="p186441838134812"><a name="p186441838134812"></a><a name="p186441838134812"></a>Messages older than 72 hours will be deleted from a queue and deleted messages are not counted into the metric.</p>
<p id="p2644538194812"><a name="p2644538194812"></a><a name="p2644538194812"></a>Dead letter messages are specific to consumer groups and stored in dead letter queues. Therefore, generation and expiry of dead letter messages do not affect the metric.</p>
<p id="p4644113864819"><a name="p4644113864819"></a><a name="p4644113864819"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.06%" headers="mcps1.2.7.1.4 "><p id="p156448381487"><a name="p156448381487"></a><a name="p156448381487"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.32%" headers="mcps1.2.7.1.5 "><p id="p12644438194811"><a name="p12644438194811"></a><a name="p12644438194811"></a>Monitored object: DMS</p>
<p id="p1644153811484"><a name="p1644153811484"></a><a name="p1644153811484"></a>Dimension:</p>
<p id="p16449385484"><a name="p16449385484"></a><a name="p16449385484"></a>queue_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.24%" headers="mcps1.2.7.1.6 "><p id="p1564410386489"><a name="p1564410386489"></a><a name="p1564410386489"></a>1 minute</p>
</td>
</tr>
<tr id="row16644238184818"><td class="cellrowborder" valign="top" width="11.42%" headers="mcps1.2.7.1.1 "><p id="p464417387482"><a name="p464417387482"></a><a name="p464417387482"></a>message_size</p>
</td>
<td class="cellrowborder" valign="top" width="11.14%" headers="mcps1.2.7.1.2 "><p id="p196451338184817"><a name="p196451338184817"></a><a name="p196451338184817"></a>Message Size</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.7.1.3 "><p id="p146455380488"><a name="p146455380488"></a><a name="p146455380488"></a>Total size of messages sent to a queue during the previous one minute</p>
<p id="p186451838194811"><a name="p186451838194811"></a><a name="p186451838194811"></a>This metric gives you an overview of the message load flowing into a queue.</p>
<p id="p364517386483"><a name="p364517386483"></a><a name="p364517386483"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="15.06%" headers="mcps1.2.7.1.4 "><p id="p1645173815485"><a name="p1645173815485"></a><a name="p1645173815485"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.32%" headers="mcps1.2.7.1.5 "><p id="p76451338194810"><a name="p76451338194810"></a><a name="p76451338194810"></a>Monitored object: DMS</p>
<p id="p9645173811486"><a name="p9645173811486"></a><a name="p9645173811486"></a>Dimension:</p>
<p id="p3645138144813"><a name="p3645138144813"></a><a name="p3645138144813"></a>queue_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.24%" headers="mcps1.2.7.1.6 "><p id="p1364553816487"><a name="p1364553816487"></a><a name="p1364553816487"></a>1 minute</p>
</td>
</tr>
<tr id="row1564573818485"><td class="cellrowborder" valign="top" width="11.42%" headers="mcps1.2.7.1.1 "><p id="p7645103811484"><a name="p7645103811484"></a><a name="p7645103811484"></a>request_count</p>
</td>
<td class="cellrowborder" valign="top" width="11.14%" headers="mcps1.2.7.1.2 "><p id="p15646133819480"><a name="p15646133819480"></a><a name="p15646133819480"></a>Request Count</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.7.1.3 "><p id="p13646338194819"><a name="p13646338194819"></a><a name="p13646338194819"></a>The total number of requests sent to a queue during the previous one minute.</p>
<p id="p4646153814482"><a name="p4646153814482"></a><a name="p4646153814482"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.06%" headers="mcps1.2.7.1.4 "><p id="p1664616380485"><a name="p1664616380485"></a><a name="p1664616380485"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.32%" headers="mcps1.2.7.1.5 "><p id="p126461238104810"><a name="p126461238104810"></a><a name="p126461238104810"></a>Monitored object: DMS</p>
<p id="p1964643844810"><a name="p1964643844810"></a><a name="p1964643844810"></a>Dimension:</p>
<p id="p364633824810"><a name="p364633824810"></a><a name="p364633824810"></a>queue_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.24%" headers="mcps1.2.7.1.6 "><p id="p19646638164816"><a name="p19646638164816"></a><a name="p19646638164816"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Metrics of consumer groups in Kafka queues \(non-premium\)

<a name="table764673816484"></a>
<table><thead align="left"><tr id="row1164717382487"><th class="cellrowborder" valign="top" width="11.86%" id="mcps1.2.7.1.1"><p id="p146471038144813"><a name="p146471038144813"></a><a name="p146471038144813"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="10.7%" id="mcps1.2.7.1.2"><p id="p26471238144819"><a name="p26471238144819"></a><a name="p26471238144819"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="39.82%" id="mcps1.2.7.1.3"><p id="p146476382487"><a name="p146476382487"></a><a name="p146476382487"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="15.06%" id="mcps1.2.7.1.4"><p id="p1364717385488"><a name="p1364717385488"></a><a name="p1364717385488"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="14.32%" id="mcps1.2.7.1.5"><p id="p1564783884811"><a name="p1564783884811"></a><a name="p1564783884811"></a>Monitored Objects and Dimensions</p>
</th>
<th class="cellrowborder" valign="top" width="8.24%" id="mcps1.2.7.1.6"><p id="p66471038174810"><a name="p66471038174810"></a><a name="p66471038174810"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row46478382488"><td class="cellrowborder" valign="top" width="11.86%" headers="mcps1.2.7.1.1 "><p id="p6647113810487"><a name="p6647113810487"></a><a name="p6647113810487"></a>dead_avail_messages</p>
</td>
<td class="cellrowborder" valign="top" width="10.7%" headers="mcps1.2.7.1.2 "><p id="p4647138134820"><a name="p4647138134820"></a><a name="p4647138134820"></a>Accumulated Messages</p>
</td>
<td class="cellrowborder" valign="top" width="39.82%" headers="mcps1.2.7.1.3 "><p id="p5647133817483"><a name="p5647133817483"></a><a name="p5647133817483"></a>The current number of messages that are not retrieved by a consumer group.</p>
<p id="p464743824816"><a name="p464743824816"></a><a name="p464743824816"></a>Messages older than 72 hours will be deleted from a queue. Deleted messages can no longer be retrieved by a consumer group and therefore are not included in the count.</p>
<p id="p1264713864819"><a name="p1264713864819"></a><a name="p1264713864819"></a>Dead letter messages are flagged as retrieved messages and therefore are not included in the count.</p>
<p id="p76471938164811"><a name="p76471938164811"></a><a name="p76471938164811"></a>Unit: Count</p>
<p id="p176471838194819"><a name="p176471838194819"></a><a name="p176471838194819"></a></p>
</td>
<td class="cellrowborder" valign="top" width="15.06%" headers="mcps1.2.7.1.4 "><p id="p1364873824811"><a name="p1364873824811"></a><a name="p1364873824811"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.32%" headers="mcps1.2.7.1.5 "><p id="p764863814481"><a name="p764863814481"></a><a name="p764863814481"></a>Monitored object: DMS</p>
<p id="p1764812383486"><a name="p1764812383486"></a><a name="p1764812383486"></a>Dimension:</p>
<p id="p26487380488"><a name="p26487380488"></a><a name="p26487380488"></a>group_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.24%" headers="mcps1.2.7.1.6 "><p id="p11648133813487"><a name="p11648133813487"></a><a name="p11648133813487"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

## Kafka Premium Instance Metrics<a name="section127571016334"></a>

**Table  5**  Monitoring metrics of Kafka premium instances

<a name="table194401611352"></a>
<table><thead align="left"><tr id="row245314120513"><th class="cellrowborder" valign="top" width="12.092418483696738%" id="mcps1.2.7.1.1"><p id="p2265449134015"><a name="p2265449134015"></a><a name="p2265449134015"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="11.89237847569514%" id="mcps1.2.7.1.2"><p id="p645711654"><a name="p645711654"></a><a name="p645711654"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="38.44768953790758%" id="mcps1.2.7.1.3"><p id="p64587116519"><a name="p64587116519"></a><a name="p64587116519"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="15.923184636927386%" id="mcps1.2.7.1.4"><p id="p377410426417"><a name="p377410426417"></a><a name="p377410426417"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="13.552710542108423%" id="mcps1.2.7.1.5"><p id="p57741342154110"><a name="p57741342154110"></a><a name="p57741342154110"></a>Monitored Objects and Dimensions</p>
</th>
<th class="cellrowborder" valign="top" width="8.091618323664733%" id="mcps1.2.7.1.6"><p id="p3774184224114"><a name="p3774184224114"></a><a name="p3774184224114"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row14618115517"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p32659490407"><a name="p32659490407"></a><a name="p32659490407"></a>current_partitions</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p8328857887"><a name="p8328857887"></a><a name="p8328857887"></a>Partitions</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p183261257385"><a name="p183261257385"></a><a name="p183261257385"></a>Number of used partitions in the instance.</p>
<p id="p106762444436"><a name="p106762444436"></a><a name="p106762444436"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p19419102219415"><a name="p19419102219415"></a><a name="p19419102219415"></a>0–18,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p04851034184414"><a name="p04851034184414"></a><a name="p04851034184414"></a>Monitored object: DMS</p>
<p id="p13486143454420"><a name="p13486143454420"></a><a name="p13486143454420"></a>Dimension:</p>
<p id="p1448618346447"><a name="p1448618346447"></a><a name="p1448618346447"></a>kafka_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p057853364112"><a name="p057853364112"></a><a name="p057853364112"></a>1 minute</p>
</td>
</tr>
<tr id="row12671105019258"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p1826644954016"><a name="p1826644954016"></a><a name="p1826644954016"></a>current_topics</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p43227571885"><a name="p43227571885"></a><a name="p43227571885"></a>Topics</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p1032018571788"><a name="p1032018571788"></a><a name="p1032018571788"></a>Number of created topics in the instance.</p>
<p id="p9353145504311"><a name="p9353145504311"></a><a name="p9353145504311"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p04191822194119"><a name="p04191822194119"></a><a name="p04191822194119"></a>0–600</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p385165494418"><a name="p385165494418"></a><a name="p385165494418"></a>Monitored object: DMS</p>
<p id="p10851125413447"><a name="p10851125413447"></a><a name="p10851125413447"></a>Dimension:</p>
<p id="p2851165424420"><a name="p2851165424420"></a><a name="p2851165424420"></a>kafka_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p957943304113"><a name="p957943304113"></a><a name="p957943304113"></a>1 minute</p>
</td>
</tr>
<tr id="row1348615815272"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p6266174911406"><a name="p6266174911406"></a><a name="p6266174911406"></a>group_msgs</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p124211415324"><a name="p124211415324"></a><a name="p124211415324"></a>Accumulated Messages</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p173944113321"><a name="p173944113321"></a><a name="p173944113321"></a>Total number of accumulated messages in all consumer groups of the instance.</p>
<p id="p97820581435"><a name="p97820581435"></a><a name="p97820581435"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p1041962215411"><a name="p1041962215411"></a><a name="p1041962215411"></a>0–1,000,000,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p10719556134410"><a name="p10719556134410"></a><a name="p10719556134410"></a>Monitored object: DMS</p>
<p id="p16719135611442"><a name="p16719135611442"></a><a name="p16719135611442"></a>Dimension:</p>
<p id="p471955694416"><a name="p471955694416"></a><a name="p471955694416"></a>kafka_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p1157923364113"><a name="p1157923364113"></a><a name="p1157923364113"></a>1 minute</p>
</td>
</tr>
<tr id="row332854018250"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p526604954012"><a name="p526604954012"></a><a name="p526604954012"></a>broker_bytes_in_rate</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p1636544412329"><a name="p1636544412329"></a><a name="p1636544412329"></a>Message Creation</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p14364644193215"><a name="p14364644193215"></a><a name="p14364644193215"></a>Number of bytes created per second.</p>
<p id="p1618213373255"><a name="p1618213373255"></a><a name="p1618213373255"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p1341942212418"><a name="p1341942212418"></a><a name="p1341942212418"></a>0–500,000,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p1723917410183"><a name="p1723917410183"></a><a name="p1723917410183"></a>Monitored object: DMS</p>
<p id="p19240114113182"><a name="p19240114113182"></a><a name="p19240114113182"></a>Dimension:</p>
<p id="p16240941151810"><a name="p16240941151810"></a><a name="p16240941151810"></a>kafka_broker</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p11579143314415"><a name="p11579143314415"></a><a name="p11579143314415"></a>1 minute</p>
</td>
</tr>
<tr id="row2477117518"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p3266114916402"><a name="p3266114916402"></a><a name="p3266114916402"></a>broker_bytes_out_rate</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p153641445320"><a name="p153641445320"></a><a name="p153641445320"></a>Message Retrieval</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p1036384418321"><a name="p1036384418321"></a><a name="p1036384418321"></a>Number of bytes retrieved per second.</p>
<p id="p655471019252"><a name="p655471019252"></a><a name="p655471019252"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p1741942244116"><a name="p1741942244116"></a><a name="p1741942244116"></a>0–500,000,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p13394135813185"><a name="p13394135813185"></a><a name="p13394135813185"></a>Monitored object: DMS</p>
<p id="p83951058201819"><a name="p83951058201819"></a><a name="p83951058201819"></a>Dimension:</p>
<p id="p83951858121816"><a name="p83951858121816"></a><a name="p83951858121816"></a>kafka_broker</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p2057943324118"><a name="p2057943324118"></a><a name="p2057943324118"></a>1 minute</p>
</td>
</tr>
<tr id="row20513192192919"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p1626634917409"><a name="p1626634917409"></a><a name="p1626634917409"></a>broker_data_size</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p12361444133210"><a name="p12361444133210"></a><a name="p12361444133210"></a>Message Size</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p12360114418325"><a name="p12360114418325"></a><a name="p12360114418325"></a>Total size of messages in the node.</p>
<p id="p1948353618244"><a name="p1948353618244"></a><a name="p1948353618244"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p17419182212415"><a name="p17419182212415"></a><a name="p17419182212415"></a>0–5,000,000,000,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p3350131193"><a name="p3350131193"></a><a name="p3350131193"></a>Monitored object: DMS</p>
<p id="p103502315196"><a name="p103502315196"></a><a name="p103502315196"></a>Dimension:</p>
<p id="p235015331919"><a name="p235015331919"></a><a name="p235015331919"></a>kafka_broker</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p195797338412"><a name="p195797338412"></a><a name="p195797338412"></a>1 minute</p>
</td>
</tr>
<tr id="row1561493874718"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p173428111488"><a name="p173428111488"></a><a name="p173428111488"></a>broker_fetch_mean</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p15615153811475"><a name="p15615153811475"></a><a name="p15615153811475"></a>Average Message Retrieval Processing Duration</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p16151638154711"><a name="p16151638154711"></a><a name="p16151638154711"></a>Average time that the broker spends processing message retrieval requests</p>
<p id="p2860838134810"><a name="p2860838134810"></a><a name="p2860838134810"></a>Unit: ms</p>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p961510384478"><a name="p961510384478"></a><a name="p961510384478"></a>0–10,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p11454154720272"><a name="p11454154720272"></a><a name="p11454154720272"></a>Monitored object: DMS</p>
<p id="p1545574717274"><a name="p1545574717274"></a><a name="p1545574717274"></a>Dimension:</p>
<p id="p15455184722712"><a name="p15455184722712"></a><a name="p15455184722712"></a>kafka_broker</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p186152388474"><a name="p186152388474"></a><a name="p186152388474"></a>1 minute</p>
</td>
</tr>
<tr id="row461512381477"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p18615138174712"><a name="p18615138174712"></a><a name="p18615138174712"></a>broker_produce_mean</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p19615203854720"><a name="p19615203854720"></a><a name="p19615203854720"></a>Average Message Creation Processing Duration</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p0615838154713"><a name="p0615838154713"></a><a name="p0615838154713"></a>Average time that the broker spends processing message creation requests</p>
<p id="p423254616489"><a name="p423254616489"></a><a name="p423254616489"></a>Unit: ms</p>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p116154381475"><a name="p116154381475"></a><a name="p116154381475"></a>0–10,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p146261851112717"><a name="p146261851112717"></a><a name="p146261851112717"></a>Monitored object: DMS</p>
<p id="p1162719514276"><a name="p1162719514276"></a><a name="p1162719514276"></a>Dimension:</p>
<p id="p10627155132717"><a name="p10627155132717"></a><a name="p10627155132717"></a>kafka_broker</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p16151238144718"><a name="p16151238144718"></a><a name="p16151238144718"></a>1 minute</p>
</td>
</tr>
<tr id="row169381215163518"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p6266449144013"><a name="p6266449144013"></a><a name="p6266449144013"></a>broker_messages_in_rate</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p3938141516353"><a name="p3938141516353"></a><a name="p3938141516353"></a>Message Creation Rate</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p8938101533514"><a name="p8938101533514"></a><a name="p8938101533514"></a>Number of messages created per second.</p>
<p id="p1136932342616"><a name="p1136932342616"></a><a name="p1136932342616"></a>Unit: count/s</p>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p54192022124113"><a name="p54192022124113"></a><a name="p54192022124113"></a>0–500,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p11976915194"><a name="p11976915194"></a><a name="p11976915194"></a>Monitored object: DMS</p>
<p id="p1498792197"><a name="p1498792197"></a><a name="p1498792197"></a>Dimension:</p>
<p id="p129819111911"><a name="p129819111911"></a><a name="p129819111911"></a>kafka_broker</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p125791333204118"><a name="p125791333204118"></a><a name="p125791333204118"></a>1 minute</p>
</td>
</tr>
<tr id="row157314272486"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p674142764815"><a name="p674142764815"></a><a name="p674142764815"></a>broker_public_bytes_in_rate</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p8744279486"><a name="p8744279486"></a><a name="p8744279486"></a>Public Inbound Traffic</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p1974172719482"><a name="p1974172719482"></a><a name="p1974172719482"></a>Inbound traffic over public networks per second</p>
<p id="p9231163510494"><a name="p9231163510494"></a><a name="p9231163510494"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p167410279485"><a name="p167410279485"></a><a name="p167410279485"></a>0–500,000,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p022333742719"><a name="p022333742719"></a><a name="p022333742719"></a>Monitored object: DMS</p>
<p id="p5223437172710"><a name="p5223437172710"></a><a name="p5223437172710"></a>Dimension:</p>
<p id="p1922316378275"><a name="p1922316378275"></a><a name="p1922316378275"></a>kafka_broker</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p67417275489"><a name="p67417275489"></a><a name="p67417275489"></a>1 minute</p>
</td>
</tr>
<tr id="row107413271488"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p97442714817"><a name="p97442714817"></a><a name="p97442714817"></a>broker_public_bytes_out_rate</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p177522716489"><a name="p177522716489"></a><a name="p177522716489"></a>Public Outbound Traffic</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p11751427164820"><a name="p11751427164820"></a><a name="p11751427164820"></a>Outbound traffic over public networks per second</p>
<p id="p489512459490"><a name="p489512459490"></a><a name="p489512459490"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p9751127114813"><a name="p9751127114813"></a><a name="p9751127114813"></a>0–500,000,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p19455193910278"><a name="p19455193910278"></a><a name="p19455193910278"></a>Monitored object: DMS</p>
<p id="p645518392277"><a name="p645518392277"></a><a name="p645518392277"></a>Dimension:</p>
<p id="p1545593912711"><a name="p1545593912711"></a><a name="p1545593912711"></a>kafka_broker</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p375202724814"><a name="p375202724814"></a><a name="p375202724814"></a>1 minute</p>
</td>
</tr>
<tr id="row17206131442919"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p52661949184017"><a name="p52661949184017"></a><a name="p52661949184017"></a>topic_bytes_in_rate</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p888013083618"><a name="p888013083618"></a><a name="p888013083618"></a>Message Creation</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p15207201462916"><a name="p15207201462916"></a><a name="p15207201462916"></a>Number of bytes created per second.</p>
<p id="p537462712198"><a name="p537462712198"></a><a name="p537462712198"></a>Unit: byte/s</p>
<div class="note" id="note1497052921911"><a name="note1497052921911"></a><a name="note1497052921911"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1097052911915"><a name="p1097052911915"></a><a name="p1097052911915"></a>This metric is available only when <strong id="b28671679582"><a name="b28671679582"></a><a name="b28671679582"></a>Scope</strong> is set to <strong id="b5713612125814"><a name="b5713612125814"></a><a name="b5713612125814"></a>Basic monitoring</strong> on the <strong id="b9616111510582"><a name="b9616111510582"></a><a name="b9616111510582"></a>Queues</strong> tab page on the Cloud Eye console. For details, see <a href="viewing-metrics.md">Viewing Metrics</a>.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p18419722174116"><a name="p18419722174116"></a><a name="p18419722174116"></a>0–500,000,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p2497154513168"><a name="p2497154513168"></a><a name="p2497154513168"></a>Monitored object: DMS</p>
<p id="p14971645101617"><a name="p14971645101617"></a><a name="p14971645101617"></a>Dimension:</p>
<p id="p164989450161"><a name="p164989450161"></a><a name="p164989450161"></a>kafka_topics</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p857943311419"><a name="p857943311419"></a><a name="p857943311419"></a>1 minute</p>
</td>
</tr>
<tr id="row1837264042918"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p12266204994012"><a name="p12266204994012"></a><a name="p12266204994012"></a>topic_bytes_out_rate</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p988613093610"><a name="p988613093610"></a><a name="p988613093610"></a>Message Retrieval</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p1537284092918"><a name="p1537284092918"></a><a name="p1537284092918"></a>Number of bytes retrieved per second.</p>
<p id="p653710310296"><a name="p653710310296"></a><a name="p653710310296"></a>Unit: byte/s</p>
<div class="note" id="note8229955141916"><a name="note8229955141916"></a><a name="note8229955141916"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p2229115581913"><a name="p2229115581913"></a><a name="p2229115581913"></a>This metric is available only when <strong id="b1054494685814"><a name="b1054494685814"></a><a name="b1054494685814"></a>Scope</strong> is set to <strong id="b175441846185815"><a name="b175441846185815"></a><a name="b175441846185815"></a>Basic monitoring</strong> on the <strong id="b165449465582"><a name="b165449465582"></a><a name="b165449465582"></a>Queues</strong> tab page on the Cloud Eye console. For details, see <a href="viewing-metrics.md">Viewing Metrics</a>.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p8419522174112"><a name="p8419522174112"></a><a name="p8419522174112"></a>0–500,000,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p8146156171716"><a name="p8146156171716"></a><a name="p8146156171716"></a>Monitored object: DMS</p>
<p id="p1146186131710"><a name="p1146186131710"></a><a name="p1146186131710"></a>Dimension:</p>
<p id="p71461762175"><a name="p71461762175"></a><a name="p71461762175"></a>kafka_topics</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p8579173364119"><a name="p8579173364119"></a><a name="p8579173364119"></a>1 minute</p>
</td>
</tr>
<tr id="row14614183303617"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p12266749194012"><a name="p12266749194012"></a><a name="p12266749194012"></a>topic_data_size</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p8614163314362"><a name="p8614163314362"></a><a name="p8614163314362"></a>Message Size</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p16142033103618"><a name="p16142033103618"></a><a name="p16142033103618"></a>Total size of messages in the queue.</p>
<p id="p12422185831918"><a name="p12422185831918"></a><a name="p12422185831918"></a>Unit: byte</p>
<div class="note" id="note781150202013"><a name="note781150202013"></a><a name="note781150202013"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p68127018209"><a name="p68127018209"></a><a name="p68127018209"></a>This metric is available only when <strong id="b101791047105816"><a name="b101791047105816"></a><a name="b101791047105816"></a>Scope</strong> is set to <strong id="b317914477584"><a name="b317914477584"></a><a name="b317914477584"></a>Basic monitoring</strong> on the <strong id="b218094718583"><a name="b218094718583"></a><a name="b218094718583"></a>Queues</strong> tab page on the Cloud Eye console. For details, see <a href="viewing-metrics.md">Viewing Metrics</a>.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p1741918221419"><a name="p1741918221419"></a><a name="p1741918221419"></a>0–5,000,000,000,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p14237181061718"><a name="p14237181061718"></a><a name="p14237181061718"></a>Monitored object: DMS</p>
<p id="p523721012173"><a name="p523721012173"></a><a name="p523721012173"></a>Dimension:</p>
<p id="p12237151051712"><a name="p12237151051712"></a><a name="p12237151051712"></a>kafka_topics</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p16579233174114"><a name="p16579233174114"></a><a name="p16579233174114"></a>1 minute</p>
</td>
</tr>
<tr id="row780873553617"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p15266174910407"><a name="p15266174910407"></a><a name="p15266174910407"></a>topic_messages</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p98097353368"><a name="p98097353368"></a><a name="p98097353368"></a>Total Messages</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p3809133515369"><a name="p3809133515369"></a><a name="p3809133515369"></a>Total number of messages in the queue.</p>
<p id="p1464818317204"><a name="p1464818317204"></a><a name="p1464818317204"></a>Unit: Count</p>
<div class="note" id="note166479515200"><a name="note166479515200"></a><a name="note166479515200"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p4647205162018"><a name="p4647205162018"></a><a name="p4647205162018"></a>This metric is available only when <strong id="b7155144875814"><a name="b7155144875814"></a><a name="b7155144875814"></a>Scope</strong> is set to <strong id="b1815513483583"><a name="b1815513483583"></a><a name="b1815513483583"></a>Basic monitoring</strong> on the <strong id="b315674845818"><a name="b315674845818"></a><a name="b315674845818"></a>Queues</strong> tab page on the Cloud Eye console. For details, see <a href="viewing-metrics.md">Viewing Metrics</a>.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p14419722134115"><a name="p14419722134115"></a><a name="p14419722134115"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p1758415145176"><a name="p1758415145176"></a><a name="p1758415145176"></a>Monitored object: DMS</p>
<p id="p358413142176"><a name="p358413142176"></a><a name="p358413142176"></a>Dimension:</p>
<p id="p1858421451713"><a name="p1858421451713"></a><a name="p1858421451713"></a>kafka_topics</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p25799338417"><a name="p25799338417"></a><a name="p25799338417"></a>1 minute</p>
</td>
</tr>
<tr id="row016551383716"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p72661491408"><a name="p72661491408"></a><a name="p72661491408"></a>topic_messages_in_rate</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p516671353714"><a name="p516671353714"></a><a name="p516671353714"></a>Message Creation Rate</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p1616621317375"><a name="p1616621317375"></a><a name="p1616621317375"></a>Number of messages created per second.</p>
<p id="p8281783206"><a name="p8281783206"></a><a name="p8281783206"></a>Unit: count/s</p>
<div class="note" id="note1479141019200"><a name="note1479141019200"></a><a name="note1479141019200"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p44801910132015"><a name="p44801910132015"></a><a name="p44801910132015"></a>This metric is available only when <strong id="b99014914585"><a name="b99014914585"></a><a name="b99014914585"></a>Scope</strong> is set to <strong id="b590114918581"><a name="b590114918581"></a><a name="b590114918581"></a>Basic monitoring</strong> on the <strong id="b59017493588"><a name="b59017493588"></a><a name="b59017493588"></a>Queues</strong> tab page on the Cloud Eye console. For details, see <a href="viewing-metrics.md">Viewing Metrics</a>.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p1041982219412"><a name="p1041982219412"></a><a name="p1041982219412"></a>0–500,000</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p32401921161714"><a name="p32401921161714"></a><a name="p32401921161714"></a>Monitored object: DMS</p>
<p id="p1924092115170"><a name="p1924092115170"></a><a name="p1924092115170"></a>Dimension:</p>
<p id="p132401921181715"><a name="p132401921181715"></a><a name="p132401921181715"></a>kafka_topics</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p185791933124111"><a name="p185791933124111"></a><a name="p185791933124111"></a>1 minute</p>
</td>
</tr>
<tr id="row58231058142311"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p01365388129"><a name="p01365388129"></a><a name="p01365388129"></a>produced_messages</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p1823105832317"><a name="p1823105832317"></a><a name="p1823105832317"></a>Partition Messages</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p148241558132315"><a name="p148241558132315"></a><a name="p148241558132315"></a>Total number of messages in the partition.</p>
<p id="p27963223129"><a name="p27963223129"></a><a name="p27963223129"></a>Unit: Count</p>
<div class="note" id="note4113121221311"><a name="note4113121221311"></a><a name="note4113121221311"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p16114111215139"><a name="p16114111215139"></a><a name="p16114111215139"></a>This metric is available only when <strong id="b273004916581"><a name="b273004916581"></a><a name="b273004916581"></a>Scope</strong> is set to <strong id="b273084915812"><a name="b273084915812"></a><a name="b273084915812"></a>Partition monitoring</strong> on the <strong id="b573019499585"><a name="b573019499585"></a><a name="b573019499585"></a>Queues</strong> tab page on the Cloud Eye console. For details, see <a href="viewing-metrics.md">Viewing Metrics</a>.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p5419162216415"><a name="p5419162216415"></a><a name="p5419162216415"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p055724851110"><a name="p055724851110"></a><a name="p055724851110"></a>Monitored object: DMS</p>
<p id="p8557164891112"><a name="p8557164891112"></a><a name="p8557164891112"></a>Dimension:</p>
<p id="p255744821112"><a name="p255744821112"></a><a name="p255744821112"></a>kafka_partitions</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p175791833144110"><a name="p175791833144110"></a><a name="p175791833144110"></a>1 minute</p>
</td>
</tr>
<tr id="row1382175611233"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p21361938191210"><a name="p21361938191210"></a><a name="p21361938191210"></a>partition_messages</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p98210561234"><a name="p98210561234"></a><a name="p98210561234"></a>Created Messages</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p38320568231"><a name="p38320568231"></a><a name="p38320568231"></a>Number of messages that have been created.</p>
<p id="p1759422851211"><a name="p1759422851211"></a><a name="p1759422851211"></a>Unit: Count</p>
<div class="note" id="note1283019452143"><a name="note1283019452143"></a><a name="note1283019452143"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1083024521412"><a name="p1083024521412"></a><a name="p1083024521412"></a>This metric is available only when <strong id="b73571950185817"><a name="b73571950185817"></a><a name="b73571950185817"></a>Scope</strong> is set to <strong id="b183571150175816"><a name="b183571150175816"></a><a name="b183571150175816"></a>Partition monitoring</strong> on the <strong id="b635710500587"><a name="b635710500587"></a><a name="b635710500587"></a>Queues</strong> tab page on the Cloud Eye console. For details, see <a href="viewing-metrics.md">Viewing Metrics</a>.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p74199228411"><a name="p74199228411"></a><a name="p74199228411"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p58748911215"><a name="p58748911215"></a><a name="p58748911215"></a>Monitored object: DMS</p>
<p id="p78746981216"><a name="p78746981216"></a><a name="p78746981216"></a>Dimension:</p>
<p id="p13874119171211"><a name="p13874119171211"></a><a name="p13874119171211"></a>kafka_partitions</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p10579193384117"><a name="p10579193384117"></a><a name="p10579193384117"></a>1 minute</p>
</td>
</tr>
<tr id="row148992293716"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p203741753598"><a name="p203741753598"></a><a name="p203741753598"></a>messages_consumed</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p549015227376"><a name="p549015227376"></a><a name="p549015227376"></a>Retrieved Messages</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p1749032220372"><a name="p1749032220372"></a><a name="p1749032220372"></a>Number of messages that have been retrieved in the consumer group.</p>
<p id="p159251501692"><a name="p159251501692"></a><a name="p159251501692"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p3419922124118"><a name="p3419922124118"></a><a name="p3419922124118"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p51101344816"><a name="p51101344816"></a><a name="p51101344816"></a>Monitored object: DMS</p>
<p id="p111015341582"><a name="p111015341582"></a><a name="p111015341582"></a>Dimension:</p>
<p id="p31101534380"><a name="p31101534380"></a><a name="p31101534380"></a>kafka_groups-partitions</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p15579203311412"><a name="p15579203311412"></a><a name="p15579203311412"></a>1 minute</p>
</td>
</tr>
<tr id="row14343327163816"><td class="cellrowborder" valign="top" width="12.092418483696738%" headers="mcps1.2.7.1.1 "><p id="p17374165320913"><a name="p17374165320913"></a><a name="p17374165320913"></a>messages_remained</p>
</td>
<td class="cellrowborder" valign="top" width="11.89237847569514%" headers="mcps1.2.7.1.2 "><p id="p11343527103814"><a name="p11343527103814"></a><a name="p11343527103814"></a>Available Messages</p>
</td>
<td class="cellrowborder" valign="top" width="38.44768953790758%" headers="mcps1.2.7.1.3 "><p id="p9343627153814"><a name="p9343627153814"></a><a name="p9343627153814"></a>Number of remaining messages that can be retrieved in the consumer group.</p>
<p id="p192101067910"><a name="p192101067910"></a><a name="p192101067910"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.923184636927386%" headers="mcps1.2.7.1.4 "><p id="p5419192274110"><a name="p5419192274110"></a><a name="p5419192274110"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="13.552710542108423%" headers="mcps1.2.7.1.5 "><p id="p722735115815"><a name="p722735115815"></a><a name="p722735115815"></a>Monitored object: DMS</p>
<p id="p62272518819"><a name="p62272518819"></a><a name="p62272518819"></a>Dimension:</p>
<p id="p12227851389"><a name="p12227851389"></a><a name="p12227851389"></a>kafka_groups-partitions</p>
</td>
<td class="cellrowborder" valign="top" width="8.091618323664733%" headers="mcps1.2.7.1.6 "><p id="p1257933317414"><a name="p1257933317414"></a><a name="p1257933317414"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

## Dimensions<a name="section10507421184117"></a>

<a name="table850711216413"></a>
<table><thead align="left"><tr id="row1650814216415"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p6508621194118"><a name="p6508621194118"></a><a name="p6508621194118"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p9509172120416"><a name="p9509172120416"></a><a name="p9509172120416"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1550910213415"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5524633105419"><a name="p5524633105419"></a><a name="p5524633105419"></a>queue_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p129922236522"><a name="p129922236522"></a><a name="p129922236522"></a>Queue ID</p>
</td>
</tr>
<tr id="row155101721174113"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2525433125414"><a name="p2525433125414"></a><a name="p2525433125414"></a>group_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p6989112310522"><a name="p6989112310522"></a><a name="p6989112310522"></a>Consumer group ID</p>
</td>
</tr>
<tr id="row561792013547"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1452510330544"><a name="p1452510330544"></a><a name="p1452510330544"></a>kafka_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p461711200546"><a name="p461711200546"></a><a name="p461711200546"></a>Kafka premium instance ID</p>
</td>
</tr>
<tr id="row166171620185417"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p165251433185417"><a name="p165251433185417"></a><a name="p165251433185417"></a>kafka_broker</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p496513459563"><a name="p496513459563"></a><a name="p496513459563"></a>Kafka premium instance brokers</p>
</td>
</tr>
<tr id="row96171620145412"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p115257331545"><a name="p115257331545"></a><a name="p115257331545"></a>kafka_topics</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1411785417567"><a name="p1411785417567"></a><a name="p1411785417567"></a>Topics in Kafka premium instances</p>
</td>
</tr>
<tr id="row10251726105418"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1852512332545"><a name="p1852512332545"></a><a name="p1852512332545"></a>kafka_partitions</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p19434120574"><a name="p19434120574"></a><a name="p19434120574"></a>Partitions in Kafka premium instances</p>
</td>
</tr>
<tr id="row1225726105414"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p8591342554"><a name="p8591342554"></a><a name="p8591342554"></a>kafka_groups-partitions</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p32853920572"><a name="p32853920572"></a><a name="p32853920572"></a>Consumer groups in Kafka premium instances</p>
</td>
</tr>
</tbody>
</table>

