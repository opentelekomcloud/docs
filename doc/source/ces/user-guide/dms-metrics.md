# DMS Metrics<a name="EN-US_TOPIC_0084572339"></a>

**Table  1**  Queue metrics

<a name="table135911932131910"></a>
<table><thead align="left"><tr id="row15592732151913"><th class="cellrowborder" valign="top" width="15.79%" id="mcps1.2.7.1.1"><p id="p228715446230"><a name="p228715446230"></a><a name="p228715446230"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="11.179999999999996%" id="mcps1.2.7.1.2"><p id="p1592133251913"><a name="p1592133251913"></a><a name="p1592133251913"></a>Metric Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.67999999999999%" id="mcps1.2.7.1.3"><p id="p1559283210196"><a name="p1559283210196"></a><a name="p1559283210196"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="9.839999999999998%" id="mcps1.2.7.1.4"><p id="p1859283218193"><a name="p1859283218193"></a><a name="p1859283218193"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="19.099999999999994%" id="mcps1.2.7.1.5"><p id="p8592123214198"><a name="p8592123214198"></a><a name="p8592123214198"></a>Monitored Object</p>
</th>
<th class="cellrowborder" valign="top" width="10.409999999999997%" id="mcps1.2.7.1.6"><p id="p566053165"><a name="p566053165"></a><a name="p566053165"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row75921832181912"><td class="cellrowborder" valign="top" width="15.79%" headers="mcps1.2.7.1.1 "><p id="p759215321190"><a name="p759215321190"></a><a name="p759215321190"></a>queued_messages</p>
</td>
<td class="cellrowborder" valign="top" width="11.179999999999996%" headers="mcps1.2.7.1.2 "><p id="p3592113216198"><a name="p3592113216198"></a><a name="p3592113216198"></a>Queued Messages</p>
</td>
<td class="cellrowborder" valign="top" width="33.67999999999999%" headers="mcps1.2.7.1.3 "><p id="p059213211914"><a name="p059213211914"></a><a name="p059213211914"></a>Current number of messages in a queue</p>
<a name="ul1451235142818"></a><a name="ul1451235142818"></a><ul id="ul1451235142818"><li>The following messages are not counted into the metric: Messages older than 72 hours<p id="p013733917288"><a name="p013733917288"></a><a name="p013733917288"></a>Messages older than 72 hours will be deleted from a queue and deleted messages are not counted into the metric.</p>
</li><li>Dead letter messages<p id="p161392437284"><a name="p161392437284"></a><a name="p161392437284"></a>Dead letter messages are specific to consumer groups and stored in dead letter queues. Therefore, generation and expiry of dead letter messages do not affect the metric.</p>
</li></ul>
<p id="p9357123133815"><a name="p9357123133815"></a><a name="p9357123133815"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="9.839999999999998%" headers="mcps1.2.7.1.4 "><p id="p259283291918"><a name="p259283291918"></a><a name="p259283291918"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="19.099999999999994%" headers="mcps1.2.7.1.5 "><p id="p25924328193"><a name="p25924328193"></a><a name="p25924328193"></a>Monitored object: DMS</p>
<p id="p1959333217198"><a name="p1959333217198"></a><a name="p1959333217198"></a>Dimension: queue_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.409999999999997%" headers="mcps1.2.7.1.6 "><p id="p1266015312619"><a name="p1266015312619"></a><a name="p1266015312619"></a>1 minute</p>
</td>
</tr>
<tr id="row145935323195"><td class="cellrowborder" valign="top" width="15.79%" headers="mcps1.2.7.1.1 "><p id="p1859320320190"><a name="p1859320320190"></a><a name="p1859320320190"></a>message_size</p>
</td>
<td class="cellrowborder" valign="top" width="11.179999999999996%" headers="mcps1.2.7.1.2 "><p id="p85936324197"><a name="p85936324197"></a><a name="p85936324197"></a>Message Size</p>
</td>
<td class="cellrowborder" valign="top" width="33.67999999999999%" headers="mcps1.2.7.1.3 "><p id="p059303217197"><a name="p059303217197"></a><a name="p059303217197"></a>Total size of messages sent to a queue during the previous one minute</p>
<p id="p7593173201912"><a name="p7593173201912"></a><a name="p7593173201912"></a>This metric gives you an overview of message load flowing into a queue.</p>
<p id="p12593183210193"><a name="p12593183210193"></a><a name="p12593183210193"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="9.839999999999998%" headers="mcps1.2.7.1.4 "><p id="p2059393241914"><a name="p2059393241914"></a><a name="p2059393241914"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="19.099999999999994%" headers="mcps1.2.7.1.5 "><p id="p1859393212196"><a name="p1859393212196"></a><a name="p1859393212196"></a>Monitored object: DMS</p>
<p id="p1959311328193"><a name="p1959311328193"></a><a name="p1959311328193"></a>Dimension: queue_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.409999999999997%" headers="mcps1.2.7.1.6 "><p id="p13660839611"><a name="p13660839611"></a><a name="p13660839611"></a>1 minute</p>
</td>
</tr>
<tr id="row3593133217196"><td class="cellrowborder" valign="top" width="15.79%" headers="mcps1.2.7.1.1 "><p id="p155931532151920"><a name="p155931532151920"></a><a name="p155931532151920"></a>request_count</p>
</td>
<td class="cellrowborder" valign="top" width="11.179999999999996%" headers="mcps1.2.7.1.2 "><p id="p1259312320193"><a name="p1259312320193"></a><a name="p1259312320193"></a>Request Count</p>
</td>
<td class="cellrowborder" valign="top" width="33.67999999999999%" headers="mcps1.2.7.1.3 "><p id="p19593132141912"><a name="p19593132141912"></a><a name="p19593132141912"></a>Total number of requests sent to a queue during the previous one minute</p>
<p id="p661612269389"><a name="p661612269389"></a><a name="p661612269389"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="9.839999999999998%" headers="mcps1.2.7.1.4 "><p id="p13593163210190"><a name="p13593163210190"></a><a name="p13593163210190"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="19.099999999999994%" headers="mcps1.2.7.1.5 "><p id="p16593832151916"><a name="p16593832151916"></a><a name="p16593832151916"></a>Monitored object: DMS</p>
<p id="p11594732191914"><a name="p11594732191914"></a><a name="p11594732191914"></a>Dimension: queue_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.409999999999997%" headers="mcps1.2.7.1.6 "><p id="p196601931766"><a name="p196601931766"></a><a name="p196601931766"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Consumer group metrics

<a name="table356581171510"></a>
<table><thead align="left"><tr id="row17565201121517"><th class="cellrowborder" valign="top" width="15.559999999999995%" id="mcps1.2.7.1.1"><p id="p11367371249"><a name="p11367371249"></a><a name="p11367371249"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="12.209999999999997%" id="mcps1.2.7.1.2"><p id="p1656617113152"><a name="p1656617113152"></a><a name="p1656617113152"></a>Metric Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.199999999999996%" id="mcps1.2.7.1.3"><p id="p10566161181517"><a name="p10566161181517"></a><a name="p10566161181517"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="9.519999999999998%" id="mcps1.2.7.1.4"><p id="p13566011151518"><a name="p13566011151518"></a><a name="p13566011151518"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="18.709999999999997%" id="mcps1.2.7.1.5"><p id="p6566201113151"><a name="p6566201113151"></a><a name="p6566201113151"></a>Monitored Object</p>
</th>
<th class="cellrowborder" valign="top" width="10.799999999999997%" id="mcps1.2.7.1.6"><p id="p19405747453"><a name="p19405747453"></a><a name="p19405747453"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row15671911101519"><td class="cellrowborder" valign="top" width="15.559999999999995%" headers="mcps1.2.7.1.1 "><p id="p13567911101514"><a name="p13567911101514"></a><a name="p13567911101514"></a>accumulated_messages</p>
</td>
<td class="cellrowborder" valign="top" width="12.209999999999997%" headers="mcps1.2.7.1.2 "><p id="p456731115151"><a name="p456731115151"></a><a name="p456731115151"></a>Accumulated Messages</p>
</td>
<td class="cellrowborder" valign="top" width="33.199999999999996%" headers="mcps1.2.7.1.3 "><p id="p7567611131520"><a name="p7567611131520"></a><a name="p7567611131520"></a>Current number of messages that are not retrieved by a consumer group</p>
<p id="p38201223141919"><a name="p38201223141919"></a><a name="p38201223141919"></a>The following messages are not counted into the metric:</p>
<a name="ul35351934181917"></a><a name="ul35351934181917"></a><ul id="ul35351934181917"><li><p id="p553573411913"><a name="p553573411913"></a><a name="p553573411913"></a>Messages older than 72 hours</p>
<p id="p1453519348198"><a name="p1453519348198"></a><a name="p1453519348198"></a>Messages older than 72 hours will be deleted from a queue. Deleted messages can no longer be retrieved by a consumer group and therefore they are not counted into the metric.</p>
</li><li><p id="p2535434151913"><a name="p2535434151913"></a><a name="p2535434151913"></a>Dead letter messages</p>
<p id="p65350347191"><a name="p65350347191"></a><a name="p65350347191"></a>Dead letter messages are flagged as retrieved messages and therefore not counted into the metric.</p>
</li></ul>
<p id="p13593174873614"><a name="p13593174873614"></a><a name="p13593174873614"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="9.519999999999998%" headers="mcps1.2.7.1.4 "><p id="p3568011141515"><a name="p3568011141515"></a><a name="p3568011141515"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="18.709999999999997%" headers="mcps1.2.7.1.5 "><p id="p3568611121518"><a name="p3568611121518"></a><a name="p3568611121518"></a>Monitored object: DMS</p>
<p id="p7568111115158"><a name="p7568111115158"></a><a name="p7568111115158"></a>Dimension: group_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.799999999999997%" headers="mcps1.2.7.1.6 "><p id="p464444216414"><a name="p464444216414"></a><a name="p464444216414"></a>1 minute</p>
</td>
</tr>
<tr id="row175681511131520"><td class="cellrowborder" valign="top" width="15.559999999999995%" headers="mcps1.2.7.1.1 "><p id="p14568141111517"><a name="p14568141111517"></a><a name="p14568141111517"></a>consumed_messages</p>
</td>
<td class="cellrowborder" valign="top" width="12.209999999999997%" headers="mcps1.2.7.1.2 "><p id="p17568191116153"><a name="p17568191116153"></a><a name="p17568191116153"></a>Retrieved Messages</p>
</td>
<td class="cellrowborder" valign="top" width="33.199999999999996%" headers="mcps1.2.7.1.3 "><p id="p1256801114151"><a name="p1256801114151"></a><a name="p1256801114151"></a>Accumulated number of messages retrieved by a consumer group since the consumer group is created</p>
<p id="p456819113152"><a name="p456819113152"></a><a name="p456819113152"></a>Dead letter messages are counted into the metric because dead letter messages are flagged as retrieved messages.</p>
<p id="p1156871181511"><a name="p1156871181511"></a><a name="p1156871181511"></a>The count of skipped messages is accumulated since a consumer group is created.</p>
<p id="p194927572365"><a name="p194927572365"></a><a name="p194927572365"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="9.519999999999998%" headers="mcps1.2.7.1.4 "><p id="p1556851117154"><a name="p1556851117154"></a><a name="p1556851117154"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="18.709999999999997%" headers="mcps1.2.7.1.5 "><p id="p356810115158"><a name="p356810115158"></a><a name="p356810115158"></a>Monitored object: DMS</p>
<p id="p165685114156"><a name="p165685114156"></a><a name="p165685114156"></a>Dimension: group_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.799999999999997%" headers="mcps1.2.7.1.6 "><p id="p26449422411"><a name="p26449422411"></a><a name="p26449422411"></a>1 minute</p>
</td>
</tr>
<tr id="row1156841111154"><td class="cellrowborder" valign="top" width="15.559999999999995%" headers="mcps1.2.7.1.1 "><p id="p115686111151"><a name="p115686111151"></a><a name="p115686111151"></a>skipped_messages</p>
</td>
<td class="cellrowborder" valign="top" width="12.209999999999997%" headers="mcps1.2.7.1.2 "><p id="p1456871117150"><a name="p1456871117150"></a><a name="p1456871117150"></a>Skipped Messages</p>
</td>
<td class="cellrowborder" valign="top" width="33.199999999999996%" headers="mcps1.2.7.1.3 "><p id="p17568141111159"><a name="p17568141111159"></a><a name="p17568141111159"></a>Accumulated number of messages that are deleted and never retrieved</p>
<p id="p35681111121516"><a name="p35681111121516"></a><a name="p35681111121516"></a>The count of skipped messages is accumulated since a consumer group is created.</p>
<p id="p135681111158"><a name="p135681111158"></a><a name="p135681111158"></a>Messages older than 72 hours will be deleted from a queue. Deleted messages can no longer be retrieved by a consumer group.</p>
<p id="p1476210013719"><a name="p1476210013719"></a><a name="p1476210013719"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="9.519999999999998%" headers="mcps1.2.7.1.4 "><p id="p1056435015377"><a name="p1056435015377"></a><a name="p1056435015377"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="18.709999999999997%" headers="mcps1.2.7.1.5 "><p id="p656871113155"><a name="p656871113155"></a><a name="p656871113155"></a>Monitored object: DMS</p>
<p id="p0569201112150"><a name="p0569201112150"></a><a name="p0569201112150"></a>Dimension: group_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.799999999999997%" headers="mcps1.2.7.1.6 "><p id="p15644174215411"><a name="p15644174215411"></a><a name="p15644174215411"></a>1 minute</p>
</td>
</tr>
<tr id="row11569911131511"><td class="cellrowborder" valign="top" width="15.559999999999995%" headers="mcps1.2.7.1.1 "><p id="p1556911111153"><a name="p1556911111153"></a><a name="p1556911111153"></a>dead_avail_messages</p>
</td>
<td class="cellrowborder" valign="top" width="12.209999999999997%" headers="mcps1.2.7.1.2 "><p id="p15691011101513"><a name="p15691011101513"></a><a name="p15691011101513"></a>Available Dead Letter Messages</p>
</td>
<td class="cellrowborder" valign="top" width="33.199999999999996%" headers="mcps1.2.7.1.3 "><p id="p456931116156"><a name="p456931116156"></a><a name="p456931116156"></a>Current number of dead letter messages that are not retrieved by a consumer group</p>
<p id="p16569121111153"><a name="p16569121111153"></a><a name="p16569121111153"></a>Dead letter messages older than 72 hours will be deleted from a queue. Once deleted, dead letter messages can no longer be retrieved by a consumer group and therefore they are not counted into the metric.</p>
<p id="p153596713718"><a name="p153596713718"></a><a name="p153596713718"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="9.519999999999998%" headers="mcps1.2.7.1.4 "><p id="p19569151121510"><a name="p19569151121510"></a><a name="p19569151121510"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="18.709999999999997%" headers="mcps1.2.7.1.5 "><p id="p1656981118152"><a name="p1656981118152"></a><a name="p1656981118152"></a>Monitored object: DMS</p>
<p id="p125699119156"><a name="p125699119156"></a><a name="p125699119156"></a>Dimension: group_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.799999999999997%" headers="mcps1.2.7.1.6 "><p id="p264420424419"><a name="p264420424419"></a><a name="p264420424419"></a>1 minute</p>
</td>
</tr>
<tr id="row7569411151517"><td class="cellrowborder" valign="top" width="15.559999999999995%" headers="mcps1.2.7.1.1 "><p id="p135691011151513"><a name="p135691011151513"></a><a name="p135691011151513"></a>dead_his_messages</p>
</td>
<td class="cellrowborder" valign="top" width="12.209999999999997%" headers="mcps1.2.7.1.2 "><p id="p6569201121520"><a name="p6569201121520"></a><a name="p6569201121520"></a>Historical Dead Letter Messages</p>
</td>
<td class="cellrowborder" valign="top" width="33.199999999999996%" headers="mcps1.2.7.1.3 "><p id="p6682131262510"><a name="p6682131262510"></a><a name="p6682131262510"></a>Accumulated number of dead letter messages that have been generated for a consumer group since the consumer group is created</p>
<p id="p55696119158"><a name="p55696119158"></a><a name="p55696119158"></a>The count of historical dead letter messages includes the retrieved dead letter messages, remaining dead letter messages, and expired dead letter messages.</p>
<p id="p47367993712"><a name="p47367993712"></a><a name="p47367993712"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="9.519999999999998%" headers="mcps1.2.7.1.4 "><p id="p145691911111513"><a name="p145691911111513"></a><a name="p145691911111513"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="18.709999999999997%" headers="mcps1.2.7.1.5 "><p id="p556912112158"><a name="p556912112158"></a><a name="p556912112158"></a>Monitored object: DMS</p>
<p id="p7569511111512"><a name="p7569511111512"></a><a name="p7569511111512"></a>Dimension: group_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.799999999999997%" headers="mcps1.2.7.1.6 "><p id="p764434216417"><a name="p764434216417"></a><a name="p764434216417"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

