# ELB Metrics<a name="EN-US_TOPIC_0123219861"></a>

## Classic load balancer metrics<a name="section13219833114416"></a>

<a name="en-us_topic_0107344474_table468720012438"></a>
<table><thead align="left"><tr id="en-us_topic_0107344474_row5687303436"><th class="cellrowborder" valign="top" width="12%" id="mcps1.1.7.1.1"><p id="en-us_topic_0107344474_p12433142065419"><a name="en-us_topic_0107344474_p12433142065419"></a><a name="en-us_topic_0107344474_p12433142065419"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.1.7.1.2"><p id="en-us_topic_0107344474_p86875019436"><a name="en-us_topic_0107344474_p86875019436"></a><a name="en-us_topic_0107344474_p86875019436"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.1.7.1.3"><p id="en-us_topic_0107344474_p116870017439"><a name="en-us_topic_0107344474_p116870017439"></a><a name="en-us_topic_0107344474_p116870017439"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.1.7.1.4"><p id="en-us_topic_0107344474_p1768713094319"><a name="en-us_topic_0107344474_p1768713094319"></a><a name="en-us_topic_0107344474_p1768713094319"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.1.7.1.5"><p id="en-us_topic_0107344474_p96881205431"><a name="en-us_topic_0107344474_p96881205431"></a><a name="en-us_topic_0107344474_p96881205431"></a>Measurement Object &amp; Dimension</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.7.1.6"><p id="en-us_topic_0107344474_p268830104318"><a name="en-us_topic_0107344474_p268830104318"></a><a name="en-us_topic_0107344474_p268830104318"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0107344474_row968819020436"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p12919153865612"><a name="en-us_topic_0107344474_p12919153865612"></a><a name="en-us_topic_0107344474_p12919153865612"></a>m1_cps</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p46888012436"><a name="en-us_topic_0107344474_p46888012436"></a><a name="en-us_topic_0107344474_p46888012436"></a>Concurrent Connections</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p1368812004314"><a name="en-us_topic_0107344474_p1368812004314"></a><a name="en-us_topic_0107344474_p1368812004314"></a>Total number of concurrent connections processed by the monitored object</p>
<p id="en-us_topic_0107344474_p168812034316"><a name="en-us_topic_0107344474_p168812034316"></a><a name="en-us_topic_0107344474_p168812034316"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p1688100184310"><a name="en-us_topic_0107344474_p1688100184310"></a><a name="en-us_topic_0107344474_p1688100184310"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p15852459192813"><a name="en-us_topic_0107344474_p15852459192813"></a><a name="en-us_topic_0107344474_p15852459192813"></a>Monitored object: a classic load balancer</p>
<p id="en-us_topic_0107344474_p19127341173418"><a name="en-us_topic_0107344474_p19127341173418"></a><a name="en-us_topic_0107344474_p19127341173418"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p968812034312"><a name="en-us_topic_0107344474_p968812034312"></a><a name="en-us_topic_0107344474_p968812034312"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row186885016438"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p1162812120577"><a name="en-us_topic_0107344474_p1162812120577"></a><a name="en-us_topic_0107344474_p1162812120577"></a>m2_act_conn</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p1068816044310"><a name="en-us_topic_0107344474_p1068816044310"></a><a name="en-us_topic_0107344474_p1068816044310"></a>Active Connections</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p76886014438"><a name="en-us_topic_0107344474_p76886014438"></a><a name="en-us_topic_0107344474_p76886014438"></a>Total number of active connections processed by the monitored object</p>
<p id="en-us_topic_0107344474_p56888094314"><a name="en-us_topic_0107344474_p56888094314"></a><a name="en-us_topic_0107344474_p56888094314"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p5688150164313"><a name="en-us_topic_0107344474_p5688150164313"></a><a name="en-us_topic_0107344474_p5688150164313"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p1874331182917"><a name="en-us_topic_0107344474_p1874331182917"></a><a name="en-us_topic_0107344474_p1874331182917"></a>Monitored object: a classic load balancer</p>
<p id="en-us_topic_0107344474_p12307172414719"><a name="en-us_topic_0107344474_p12307172414719"></a><a name="en-us_topic_0107344474_p12307172414719"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p1068811014316"><a name="en-us_topic_0107344474_p1068811014316"></a><a name="en-us_topic_0107344474_p1068811014316"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row16689160164320"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p14702831125717"><a name="en-us_topic_0107344474_p14702831125717"></a><a name="en-us_topic_0107344474_p14702831125717"></a>m3_inact_conn</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p1268980134313"><a name="en-us_topic_0107344474_p1268980134313"></a><a name="en-us_topic_0107344474_p1268980134313"></a>Inactive Connections</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p1768910064315"><a name="en-us_topic_0107344474_p1768910064315"></a><a name="en-us_topic_0107344474_p1768910064315"></a>Total number of non-active connections processed by the monitored object</p>
<p id="en-us_topic_0107344474_p168911016439"><a name="en-us_topic_0107344474_p168911016439"></a><a name="en-us_topic_0107344474_p168911016439"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p268918044311"><a name="en-us_topic_0107344474_p268918044311"></a><a name="en-us_topic_0107344474_p268918044311"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p5652139298"><a name="en-us_topic_0107344474_p5652139298"></a><a name="en-us_topic_0107344474_p5652139298"></a>Monitored object: a classic load balancer</p>
<p id="en-us_topic_0107344474_p33566245475"><a name="en-us_topic_0107344474_p33566245475"></a><a name="en-us_topic_0107344474_p33566245475"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p156893019433"><a name="en-us_topic_0107344474_p156893019433"></a><a name="en-us_topic_0107344474_p156893019433"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row668912084312"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p5702193115712"><a name="en-us_topic_0107344474_p5702193115712"></a><a name="en-us_topic_0107344474_p5702193115712"></a>m4_ncps</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p96898084319"><a name="en-us_topic_0107344474_p96898084319"></a><a name="en-us_topic_0107344474_p96898084319"></a>New Connections</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p1968917020434"><a name="en-us_topic_0107344474_p1968917020434"></a><a name="en-us_topic_0107344474_p1968917020434"></a>Total number of new connections processed by the monitored object</p>
<p id="en-us_topic_0107344474_p206891807431"><a name="en-us_topic_0107344474_p206891807431"></a><a name="en-us_topic_0107344474_p206891807431"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p176902016437"><a name="en-us_topic_0107344474_p176902016437"></a><a name="en-us_topic_0107344474_p176902016437"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p12520658293"><a name="en-us_topic_0107344474_p12520658293"></a><a name="en-us_topic_0107344474_p12520658293"></a>Monitored object: a classic load balancer</p>
<p id="en-us_topic_0107344474_p16401224164711"><a name="en-us_topic_0107344474_p16401224164711"></a><a name="en-us_topic_0107344474_p16401224164711"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p16901402433"><a name="en-us_topic_0107344474_p16901402433"></a><a name="en-us_topic_0107344474_p16901402433"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row36901708439"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p4773141118585"><a name="en-us_topic_0107344474_p4773141118585"></a><a name="en-us_topic_0107344474_p4773141118585"></a>m5_in_pps</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p16908010437"><a name="en-us_topic_0107344474_p16908010437"></a><a name="en-us_topic_0107344474_p16908010437"></a>Incoming Packets</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p156901807438"><a name="en-us_topic_0107344474_p156901807438"></a><a name="en-us_topic_0107344474_p156901807438"></a>Incoming packets received by the monitored object per second</p>
<p id="en-us_topic_0107344474_p146909034317"><a name="en-us_topic_0107344474_p146909034317"></a><a name="en-us_topic_0107344474_p146909034317"></a>Unit: Packet/s</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p769030194315"><a name="en-us_topic_0107344474_p769030194315"></a><a name="en-us_topic_0107344474_p769030194315"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p510913115334"><a name="en-us_topic_0107344474_p510913115334"></a><a name="en-us_topic_0107344474_p510913115334"></a>Monitored object: a classic load balancer</p>
<p id="en-us_topic_0107344474_p12449112417474"><a name="en-us_topic_0107344474_p12449112417474"></a><a name="en-us_topic_0107344474_p12449112417474"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p66906094312"><a name="en-us_topic_0107344474_p66906094312"></a><a name="en-us_topic_0107344474_p66906094312"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row166909024312"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p197739113581"><a name="en-us_topic_0107344474_p197739113581"></a><a name="en-us_topic_0107344474_p197739113581"></a>m6_out_pps</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p14690150134317"><a name="en-us_topic_0107344474_p14690150134317"></a><a name="en-us_topic_0107344474_p14690150134317"></a>Outgoing Packets</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p1869010019435"><a name="en-us_topic_0107344474_p1869010019435"></a><a name="en-us_topic_0107344474_p1869010019435"></a>Outgoing packets sent from the monitored object per second</p>
<p id="en-us_topic_0107344474_p269018012432"><a name="en-us_topic_0107344474_p269018012432"></a><a name="en-us_topic_0107344474_p269018012432"></a>Unit: Packet/s</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p116903013438"><a name="en-us_topic_0107344474_p116903013438"></a><a name="en-us_topic_0107344474_p116903013438"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p1803213173314"><a name="en-us_topic_0107344474_p1803213173314"></a><a name="en-us_topic_0107344474_p1803213173314"></a>Monitored object: a classic load balancer</p>
<p id="en-us_topic_0107344474_p549342494719"><a name="en-us_topic_0107344474_p549342494719"></a><a name="en-us_topic_0107344474_p549342494719"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p18690130194318"><a name="en-us_topic_0107344474_p18690130194318"></a><a name="en-us_topic_0107344474_p18690130194318"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row169016014311"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p8407132119581"><a name="en-us_topic_0107344474_p8407132119581"></a><a name="en-us_topic_0107344474_p8407132119581"></a>m7_in_Bps</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p126903014432"><a name="en-us_topic_0107344474_p126903014432"></a><a name="en-us_topic_0107344474_p126903014432"></a>Inbound Rate</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p869190184319"><a name="en-us_topic_0107344474_p869190184319"></a><a name="en-us_topic_0107344474_p869190184319"></a>Incoming bytes received by the monitored object per second</p>
<p id="en-us_topic_0107344474_p869111017438"><a name="en-us_topic_0107344474_p869111017438"></a><a name="en-us_topic_0107344474_p869111017438"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p16691703437"><a name="en-us_topic_0107344474_p16691703437"></a><a name="en-us_topic_0107344474_p16691703437"></a>≥ 1 byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p85671317112017"><a name="en-us_topic_0107344474_p85671317112017"></a><a name="en-us_topic_0107344474_p85671317112017"></a>Measurement object: classic load balancer</p>
<p id="en-us_topic_0107344474_p11647195132013"><a name="en-us_topic_0107344474_p11647195132013"></a><a name="en-us_topic_0107344474_p11647195132013"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p069115019435"><a name="en-us_topic_0107344474_p069115019435"></a><a name="en-us_topic_0107344474_p069115019435"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row1691180134319"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p64070218581"><a name="en-us_topic_0107344474_p64070218581"></a><a name="en-us_topic_0107344474_p64070218581"></a>m8_out_Bps</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p8691802439"><a name="en-us_topic_0107344474_p8691802439"></a><a name="en-us_topic_0107344474_p8691802439"></a>Outbound Rate</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p2069111094312"><a name="en-us_topic_0107344474_p2069111094312"></a><a name="en-us_topic_0107344474_p2069111094312"></a>Outgoing bytes sent from the monitored object per second</p>
<p id="en-us_topic_0107344474_p17691110114315"><a name="en-us_topic_0107344474_p17691110114315"></a><a name="en-us_topic_0107344474_p17691110114315"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p869117018435"><a name="en-us_topic_0107344474_p869117018435"></a><a name="en-us_topic_0107344474_p869117018435"></a>≥ 1 byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p202565415332"><a name="en-us_topic_0107344474_p202565415332"></a><a name="en-us_topic_0107344474_p202565415332"></a>Monitored object: a classic load balancer</p>
<p id="en-us_topic_0107344474_p1657572464717"><a name="en-us_topic_0107344474_p1657572464717"></a><a name="en-us_topic_0107344474_p1657572464717"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p06911102434"><a name="en-us_topic_0107344474_p06911102434"></a><a name="en-us_topic_0107344474_p06911102434"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row1269150154315"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p88291732185820"><a name="en-us_topic_0107344474_p88291732185820"></a><a name="en-us_topic_0107344474_p88291732185820"></a>m9_abnormal_servers</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p8691502439"><a name="en-us_topic_0107344474_p8691502439"></a><a name="en-us_topic_0107344474_p8691502439"></a>Unhealthy Servers</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p12691190104315"><a name="en-us_topic_0107344474_p12691190104315"></a><a name="en-us_topic_0107344474_p12691190104315"></a>Number of backend servers considered unhealthy</p>
<p id="en-us_topic_0107344474_p1969110104315"><a name="en-us_topic_0107344474_p1969110104315"></a><a name="en-us_topic_0107344474_p1969110104315"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p11692120154316"><a name="en-us_topic_0107344474_p11692120154316"></a><a name="en-us_topic_0107344474_p11692120154316"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p4890196343"><a name="en-us_topic_0107344474_p4890196343"></a><a name="en-us_topic_0107344474_p4890196343"></a>Monitored object: a classic load balancer</p>
<p id="en-us_topic_0107344474_p116137244471"><a name="en-us_topic_0107344474_p116137244471"></a><a name="en-us_topic_0107344474_p116137244471"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p869215064313"><a name="en-us_topic_0107344474_p869215064313"></a><a name="en-us_topic_0107344474_p869215064313"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row169214011439"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p48291932145815"><a name="en-us_topic_0107344474_p48291932145815"></a><a name="en-us_topic_0107344474_p48291932145815"></a>ma_normal_servers</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p136924034314"><a name="en-us_topic_0107344474_p136924034314"></a><a name="en-us_topic_0107344474_p136924034314"></a>Healthy Servers</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p1569260174312"><a name="en-us_topic_0107344474_p1569260174312"></a><a name="en-us_topic_0107344474_p1569260174312"></a>Number of backend servers considered healthy</p>
<p id="en-us_topic_0107344474_p969218016435"><a name="en-us_topic_0107344474_p969218016435"></a><a name="en-us_topic_0107344474_p969218016435"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p36921004318"><a name="en-us_topic_0107344474_p36921004318"></a><a name="en-us_topic_0107344474_p36921004318"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p1039615130342"><a name="en-us_topic_0107344474_p1039615130342"></a><a name="en-us_topic_0107344474_p1039615130342"></a>Monitored object: a classic load balancer</p>
<p id="en-us_topic_0107344474_p1765572412474"><a name="en-us_topic_0107344474_p1765572412474"></a><a name="en-us_topic_0107344474_p1765572412474"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p469216014312"><a name="en-us_topic_0107344474_p469216014312"></a><a name="en-us_topic_0107344474_p469216014312"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

## Metrics of enhanced load balancer and enhanced load balancer listeners<a name="section1153447455"></a>

<a name="en-us_topic_0107344474_table173712719019"></a>
<table><thead align="left"><tr id="en-us_topic_0107344474_row4378277012"><th class="cellrowborder" valign="top" width="9.090909090909092%" id="mcps1.1.7.1.1"><p id="en-us_topic_0107344474_p21500591400"><a name="en-us_topic_0107344474_p21500591400"></a><a name="en-us_topic_0107344474_p21500591400"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.1.7.1.2"><p id="en-us_topic_0107344474_p11507599016"><a name="en-us_topic_0107344474_p11507599016"></a><a name="en-us_topic_0107344474_p11507599016"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.1.7.1.3"><p id="en-us_topic_0107344474_p17150145915010"><a name="en-us_topic_0107344474_p17150145915010"></a><a name="en-us_topic_0107344474_p17150145915010"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.1.7.1.4"><p id="en-us_topic_0107344474_p1115015592000"><a name="en-us_topic_0107344474_p1115015592000"></a><a name="en-us_topic_0107344474_p1115015592000"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.1.7.1.5"><p id="en-us_topic_0107344474_p14150859706"><a name="en-us_topic_0107344474_p14150859706"></a><a name="en-us_topic_0107344474_p14150859706"></a>Measurement Object &amp; Dimension</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.1.7.1.6"><p id="en-us_topic_0107344474_p81501859405"><a name="en-us_topic_0107344474_p81501859405"></a><a name="en-us_topic_0107344474_p81501859405"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0107344474_row1381271805"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p847416411252"><a name="en-us_topic_0107344474_p847416411252"></a><a name="en-us_topic_0107344474_p847416411252"></a>m1_cps</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p838727303"><a name="en-us_topic_0107344474_p838727303"></a><a name="en-us_topic_0107344474_p838727303"></a>Concurrent Connections</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p638202716013"><a name="en-us_topic_0107344474_p638202716013"></a><a name="en-us_topic_0107344474_p638202716013"></a>Total number of concurrent connections processed by the monitored object</p>
<p id="en-us_topic_0107344474_p83822713017"><a name="en-us_topic_0107344474_p83822713017"></a><a name="en-us_topic_0107344474_p83822713017"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p1438142710018"><a name="en-us_topic_0107344474_p1438142710018"></a><a name="en-us_topic_0107344474_p1438142710018"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p13882711010"><a name="en-us_topic_0107344474_p13882711010"></a><a name="en-us_topic_0107344474_p13882711010"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="en-us_topic_0107344474_p34567242116"><a name="en-us_topic_0107344474_p34567242116"></a><a name="en-us_topic_0107344474_p34567242116"></a>Dimensions<sup id="en-us_topic_0107344474_sup1245616247117"><a name="en-us_topic_0107344474_sup1245616247117"></a><a name="en-us_topic_0107344474_sup1245616247117"></a>a</sup>: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p16382275017"><a name="en-us_topic_0107344474_p16382275017"></a><a name="en-us_topic_0107344474_p16382275017"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row15388271010"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p14741441358"><a name="en-us_topic_0107344474_p14741441358"></a><a name="en-us_topic_0107344474_p14741441358"></a>m2_act_conn</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p3383278014"><a name="en-us_topic_0107344474_p3383278014"></a><a name="en-us_topic_0107344474_p3383278014"></a>Active Connections</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p1538427605"><a name="en-us_topic_0107344474_p1538427605"></a><a name="en-us_topic_0107344474_p1538427605"></a>Total number of active connections processed by the monitored object</p>
<p id="en-us_topic_0107344474_p1038227308"><a name="en-us_topic_0107344474_p1038227308"></a><a name="en-us_topic_0107344474_p1038227308"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p1138727605"><a name="en-us_topic_0107344474_p1138727605"></a><a name="en-us_topic_0107344474_p1138727605"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p1438132717013"><a name="en-us_topic_0107344474_p1438132717013"></a><a name="en-us_topic_0107344474_p1438132717013"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="en-us_topic_0107344474_p12408029259"><a name="en-us_topic_0107344474_p12408029259"></a><a name="en-us_topic_0107344474_p12408029259"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p123812271808"><a name="en-us_topic_0107344474_p123812271808"></a><a name="en-us_topic_0107344474_p123812271808"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row123814271407"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p9475114113520"><a name="en-us_topic_0107344474_p9475114113520"></a><a name="en-us_topic_0107344474_p9475114113520"></a>m3_inact_conn</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p7391027203"><a name="en-us_topic_0107344474_p7391027203"></a><a name="en-us_topic_0107344474_p7391027203"></a>Inactive Connections</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p19396272011"><a name="en-us_topic_0107344474_p19396272011"></a><a name="en-us_topic_0107344474_p19396272011"></a>Total number of non-active connections processed by the monitored object</p>
<p id="en-us_topic_0107344474_p203914271014"><a name="en-us_topic_0107344474_p203914271014"></a><a name="en-us_topic_0107344474_p203914271014"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p4393271907"><a name="en-us_topic_0107344474_p4393271907"></a><a name="en-us_topic_0107344474_p4393271907"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p14391271206"><a name="en-us_topic_0107344474_p14391271206"></a><a name="en-us_topic_0107344474_p14391271206"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="en-us_topic_0107344474_p1753172518818"><a name="en-us_topic_0107344474_p1753172518818"></a><a name="en-us_topic_0107344474_p1753172518818"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p83912720015"><a name="en-us_topic_0107344474_p83912720015"></a><a name="en-us_topic_0107344474_p83912720015"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row939102719012"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p10475114119519"><a name="en-us_topic_0107344474_p10475114119519"></a><a name="en-us_topic_0107344474_p10475114119519"></a>m4_ncps</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p13398271406"><a name="en-us_topic_0107344474_p13398271406"></a><a name="en-us_topic_0107344474_p13398271406"></a>New Connections</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p11391327003"><a name="en-us_topic_0107344474_p11391327003"></a><a name="en-us_topic_0107344474_p11391327003"></a>Total number of new connections processed by the monitored object</p>
<p id="en-us_topic_0107344474_p0397272017"><a name="en-us_topic_0107344474_p0397272017"></a><a name="en-us_topic_0107344474_p0397272017"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p33910271703"><a name="en-us_topic_0107344474_p33910271703"></a><a name="en-us_topic_0107344474_p33910271703"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p53910271709"><a name="en-us_topic_0107344474_p53910271709"></a><a name="en-us_topic_0107344474_p53910271709"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="en-us_topic_0107344474_p189546311780"><a name="en-us_topic_0107344474_p189546311780"></a><a name="en-us_topic_0107344474_p189546311780"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p9394271304"><a name="en-us_topic_0107344474_p9394271304"></a><a name="en-us_topic_0107344474_p9394271304"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row639527908"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p447544118511"><a name="en-us_topic_0107344474_p447544118511"></a><a name="en-us_topic_0107344474_p447544118511"></a>m5_in_pps</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p43992712015"><a name="en-us_topic_0107344474_p43992712015"></a><a name="en-us_topic_0107344474_p43992712015"></a>Incoming Packets</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p2040627607"><a name="en-us_topic_0107344474_p2040627607"></a><a name="en-us_topic_0107344474_p2040627607"></a>Incoming packets received by the monitored object per second</p>
<p id="en-us_topic_0107344474_p114012272003"><a name="en-us_topic_0107344474_p114012272003"></a><a name="en-us_topic_0107344474_p114012272003"></a>Unit: Packet/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p640527402"><a name="en-us_topic_0107344474_p640527402"></a><a name="en-us_topic_0107344474_p640527402"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p12401271900"><a name="en-us_topic_0107344474_p12401271900"></a><a name="en-us_topic_0107344474_p12401271900"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="en-us_topic_0107344474_p1773114913819"><a name="en-us_topic_0107344474_p1773114913819"></a><a name="en-us_topic_0107344474_p1773114913819"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p174020270014"><a name="en-us_topic_0107344474_p174020270014"></a><a name="en-us_topic_0107344474_p174020270014"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row8407271908"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p747516411659"><a name="en-us_topic_0107344474_p747516411659"></a><a name="en-us_topic_0107344474_p747516411659"></a>m6_out_pps</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p54011271606"><a name="en-us_topic_0107344474_p54011271606"></a><a name="en-us_topic_0107344474_p54011271606"></a>Outgoing Packets</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p1940527102"><a name="en-us_topic_0107344474_p1940527102"></a><a name="en-us_topic_0107344474_p1940527102"></a>Outgoing packets sent from the monitored object per second</p>
<p id="en-us_topic_0107344474_p194015278012"><a name="en-us_topic_0107344474_p194015278012"></a><a name="en-us_topic_0107344474_p194015278012"></a>Unit: Packet/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p134011278011"><a name="en-us_topic_0107344474_p134011278011"></a><a name="en-us_topic_0107344474_p134011278011"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p154082715019"><a name="en-us_topic_0107344474_p154082715019"></a><a name="en-us_topic_0107344474_p154082715019"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="en-us_topic_0107344474_p17411115812814"><a name="en-us_topic_0107344474_p17411115812814"></a><a name="en-us_topic_0107344474_p17411115812814"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p64072713012"><a name="en-us_topic_0107344474_p64072713012"></a><a name="en-us_topic_0107344474_p64072713012"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row17401727203"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p247514115516"><a name="en-us_topic_0107344474_p247514115516"></a><a name="en-us_topic_0107344474_p247514115516"></a>m7_in_Bps</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p14011277010"><a name="en-us_topic_0107344474_p14011277010"></a><a name="en-us_topic_0107344474_p14011277010"></a>Inbound Rate</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p44011275017"><a name="en-us_topic_0107344474_p44011275017"></a><a name="en-us_topic_0107344474_p44011275017"></a>Incoming bytes received by the monitored object per second</p>
<p id="en-us_topic_0107344474_p124013273016"><a name="en-us_topic_0107344474_p124013273016"></a><a name="en-us_topic_0107344474_p124013273016"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p64192712019"><a name="en-us_topic_0107344474_p64192712019"></a><a name="en-us_topic_0107344474_p64192712019"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p041112711017"><a name="en-us_topic_0107344474_p041112711017"></a><a name="en-us_topic_0107344474_p041112711017"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="en-us_topic_0107344474_p7911967913"><a name="en-us_topic_0107344474_p7911967913"></a><a name="en-us_topic_0107344474_p7911967913"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p64118270012"><a name="en-us_topic_0107344474_p64118270012"></a><a name="en-us_topic_0107344474_p64118270012"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row12411276015"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p1147520415511"><a name="en-us_topic_0107344474_p1147520415511"></a><a name="en-us_topic_0107344474_p1147520415511"></a>m8_out_Bps</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p24111271013"><a name="en-us_topic_0107344474_p24111271013"></a><a name="en-us_topic_0107344474_p24111271013"></a>Outbound Rate</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p941162717012"><a name="en-us_topic_0107344474_p941162717012"></a><a name="en-us_topic_0107344474_p941162717012"></a>Outgoing bytes sent from the monitored object per second</p>
<p id="en-us_topic_0107344474_p114110279019"><a name="en-us_topic_0107344474_p114110279019"></a><a name="en-us_topic_0107344474_p114110279019"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p6414270019"><a name="en-us_topic_0107344474_p6414270019"></a><a name="en-us_topic_0107344474_p6414270019"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p44119277018"><a name="en-us_topic_0107344474_p44119277018"></a><a name="en-us_topic_0107344474_p44119277018"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="en-us_topic_0107344474_p104551620793"><a name="en-us_topic_0107344474_p104551620793"></a><a name="en-us_topic_0107344474_p104551620793"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p10413276013"><a name="en-us_topic_0107344474_p10413276013"></a><a name="en-us_topic_0107344474_p10413276013"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row441152710011"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p114758411551"><a name="en-us_topic_0107344474_p114758411551"></a><a name="en-us_topic_0107344474_p114758411551"></a>m9_abnormal_servers</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p184118277017"><a name="en-us_topic_0107344474_p184118277017"></a><a name="en-us_topic_0107344474_p184118277017"></a>Unhealthy Servers</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p64117278012"><a name="en-us_topic_0107344474_p64117278012"></a><a name="en-us_topic_0107344474_p64117278012"></a>Number of backend servers considered unhealthy</p>
<p id="en-us_topic_0107344474_p34111276011"><a name="en-us_topic_0107344474_p34111276011"></a><a name="en-us_topic_0107344474_p34111276011"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p20421827404"><a name="en-us_topic_0107344474_p20421827404"></a><a name="en-us_topic_0107344474_p20421827404"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p54232718017"><a name="en-us_topic_0107344474_p54232718017"></a><a name="en-us_topic_0107344474_p54232718017"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="en-us_topic_0107344474_p1052123815118"><a name="en-us_topic_0107344474_p1052123815118"></a><a name="en-us_topic_0107344474_p1052123815118"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p34219271209"><a name="en-us_topic_0107344474_p34219271209"></a><a name="en-us_topic_0107344474_p34219271209"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0107344474_row4420271009"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0107344474_p0475114111514"><a name="en-us_topic_0107344474_p0475114111514"></a><a name="en-us_topic_0107344474_p0475114111514"></a>ma_normal_servers</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0107344474_p15425271805"><a name="en-us_topic_0107344474_p15425271805"></a><a name="en-us_topic_0107344474_p15425271805"></a>Healthy Servers</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0107344474_p1742627702"><a name="en-us_topic_0107344474_p1742627702"></a><a name="en-us_topic_0107344474_p1742627702"></a>Number of backend servers considered healthy</p>
<p id="en-us_topic_0107344474_p84220271019"><a name="en-us_topic_0107344474_p84220271019"></a><a name="en-us_topic_0107344474_p84220271019"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0107344474_p184212717016"><a name="en-us_topic_0107344474_p184212717016"></a><a name="en-us_topic_0107344474_p184212717016"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0107344474_p74215271202"><a name="en-us_topic_0107344474_p74215271202"></a><a name="en-us_topic_0107344474_p74215271202"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="en-us_topic_0107344474_p1034312920111"><a name="en-us_topic_0107344474_p1034312920111"></a><a name="en-us_topic_0107344474_p1034312920111"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0107344474_p11421927101"><a name="en-us_topic_0107344474_p11421927101"></a><a name="en-us_topic_0107344474_p11421927101"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

**a**: If a service has multiple dimensions, all dimensions are mandatory when you use APIs to query the metrics.

-   Example of querying a single metric from both the enhanced load balancer and listener dimensions: dim.0=lbaas\_instance\_id,223e9eed-2b02-4ed2-a126-7e806a6fee1f&dim.1=lbaas\_listener\_id,3baa7335-8886-4867-8481-7cbba967a917
-   Example of querying metrics in batches from both the enhanced load balancer and listener dimensions:

    ```
    "dimensions": [
    {
    "name": "lbaas_instance_id",
    "value": "223e9eed-2b02-4ed2-a126-7e806a6fee1f"
    }
    {
    "name": "lbaas_listener_id",
    "value": "3baa7335-8886-4867-8481-7cbba967a917"
    }
    ],
    ```


