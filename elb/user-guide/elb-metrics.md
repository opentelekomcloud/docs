# ELB Metrics<a name="EN-US_TOPIC_0107344474"></a>

## Description<a name="en-us_topic_0021772779_en-us_topic_0021733202_section58478819162452"></a>

This topic describes monitoring metrics reported by ELB to Cloud Eye as well as their namespaces and dimensions. You can also use APIs provided by Cloud Eye to query metrics of the monitored objects and alarms generated by Cloud Eye.

## Namespace<a name="en-us_topic_0021772779_en-us_topic_0021733202_section40749874162521"></a>

SYS.ELB

## Classic load balancer metrics<a name="section161482219412"></a>

<a name="table468720012438"></a>
<table><thead align="left"><tr id="row5687303436"><th class="cellrowborder" valign="top" width="12%" id="mcps1.1.7.1.1"><p id="p12433142065419"><a name="p12433142065419"></a><a name="p12433142065419"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.1.7.1.2"><p id="p86875019436"><a name="p86875019436"></a><a name="p86875019436"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.1.7.1.3"><p id="p116870017439"><a name="p116870017439"></a><a name="p116870017439"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.1.7.1.4"><p id="p1768713094319"><a name="p1768713094319"></a><a name="p1768713094319"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.1.7.1.5"><p id="p96881205431"><a name="p96881205431"></a><a name="p96881205431"></a>Measurement Object &amp; Dimension</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.7.1.6"><p id="p268830104318"><a name="p268830104318"></a><a name="p268830104318"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row968819020436"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="p12919153865612"><a name="p12919153865612"></a><a name="p12919153865612"></a>m1_cps</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="p46888012436"><a name="p46888012436"></a><a name="p46888012436"></a>Concurrent Connections</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="p1368812004314"><a name="p1368812004314"></a><a name="p1368812004314"></a>Total number of concurrent connections processed by the monitored object</p>
<p id="p168812034316"><a name="p168812034316"></a><a name="p168812034316"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="p1688100184310"><a name="p1688100184310"></a><a name="p1688100184310"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="p15852459192813"><a name="p15852459192813"></a><a name="p15852459192813"></a>Monitored object: a classic load balancer</p>
<p id="p19127341173418"><a name="p19127341173418"></a><a name="p19127341173418"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="p968812034312"><a name="p968812034312"></a><a name="p968812034312"></a>1 minute</p>
</td>
</tr>
<tr id="row186885016438"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="p1162812120577"><a name="p1162812120577"></a><a name="p1162812120577"></a>m2_act_conn</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="p1068816044310"><a name="p1068816044310"></a><a name="p1068816044310"></a>Active Connections</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="p76886014438"><a name="p76886014438"></a><a name="p76886014438"></a>Total number of active connections processed by the monitored object</p>
<p id="p56888094314"><a name="p56888094314"></a><a name="p56888094314"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="p5688150164313"><a name="p5688150164313"></a><a name="p5688150164313"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="p1874331182917"><a name="p1874331182917"></a><a name="p1874331182917"></a>Monitored object: a classic load balancer</p>
<p id="p12307172414719"><a name="p12307172414719"></a><a name="p12307172414719"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="p1068811014316"><a name="p1068811014316"></a><a name="p1068811014316"></a>1 minute</p>
</td>
</tr>
<tr id="row16689160164320"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="p14702831125717"><a name="p14702831125717"></a><a name="p14702831125717"></a>m3_inact_conn</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="p1268980134313"><a name="p1268980134313"></a><a name="p1268980134313"></a>Inactive Connections</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="p1768910064315"><a name="p1768910064315"></a><a name="p1768910064315"></a>Total number of non-active connections processed by the monitored object</p>
<p id="p168911016439"><a name="p168911016439"></a><a name="p168911016439"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="p268918044311"><a name="p268918044311"></a><a name="p268918044311"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="p5652139298"><a name="p5652139298"></a><a name="p5652139298"></a>Monitored object: a classic load balancer</p>
<p id="p33566245475"><a name="p33566245475"></a><a name="p33566245475"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="p156893019433"><a name="p156893019433"></a><a name="p156893019433"></a>1 minute</p>
</td>
</tr>
<tr id="row668912084312"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="p5702193115712"><a name="p5702193115712"></a><a name="p5702193115712"></a>m4_ncps</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="p96898084319"><a name="p96898084319"></a><a name="p96898084319"></a>New Connections</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="p1968917020434"><a name="p1968917020434"></a><a name="p1968917020434"></a>Total number of new connections processed by the monitored object</p>
<p id="p206891807431"><a name="p206891807431"></a><a name="p206891807431"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="p176902016437"><a name="p176902016437"></a><a name="p176902016437"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="p12520658293"><a name="p12520658293"></a><a name="p12520658293"></a>Monitored object: a classic load balancer</p>
<p id="p16401224164711"><a name="p16401224164711"></a><a name="p16401224164711"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="p16901402433"><a name="p16901402433"></a><a name="p16901402433"></a>1 minute</p>
</td>
</tr>
<tr id="row36901708439"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="p4773141118585"><a name="p4773141118585"></a><a name="p4773141118585"></a>m5_in_pps</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="p16908010437"><a name="p16908010437"></a><a name="p16908010437"></a>Incoming Packets</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="p156901807438"><a name="p156901807438"></a><a name="p156901807438"></a>Incoming packets received by the monitored object per second</p>
<p id="p146909034317"><a name="p146909034317"></a><a name="p146909034317"></a>Unit: Packet/s</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="p769030194315"><a name="p769030194315"></a><a name="p769030194315"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="p510913115334"><a name="p510913115334"></a><a name="p510913115334"></a>Monitored object: a classic load balancer</p>
<p id="p12449112417474"><a name="p12449112417474"></a><a name="p12449112417474"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="p66906094312"><a name="p66906094312"></a><a name="p66906094312"></a>1 minute</p>
</td>
</tr>
<tr id="row166909024312"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="p197739113581"><a name="p197739113581"></a><a name="p197739113581"></a>m6_out_pps</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="p14690150134317"><a name="p14690150134317"></a><a name="p14690150134317"></a>Outgoing Packets</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="p1869010019435"><a name="p1869010019435"></a><a name="p1869010019435"></a>Outgoing packets sent from the monitored object per second</p>
<p id="p269018012432"><a name="p269018012432"></a><a name="p269018012432"></a>Unit: Packet/s</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="p116903013438"><a name="p116903013438"></a><a name="p116903013438"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="p1803213173314"><a name="p1803213173314"></a><a name="p1803213173314"></a>Monitored object: a classic load balancer</p>
<p id="p549342494719"><a name="p549342494719"></a><a name="p549342494719"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="p18690130194318"><a name="p18690130194318"></a><a name="p18690130194318"></a>1 minute</p>
</td>
</tr>
<tr id="row169016014311"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="p8407132119581"><a name="p8407132119581"></a><a name="p8407132119581"></a>m7_in_Bps</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="p126903014432"><a name="p126903014432"></a><a name="p126903014432"></a>Inbound Rate</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="p869190184319"><a name="p869190184319"></a><a name="p869190184319"></a>Incoming bytes received by the monitored object per second</p>
<p id="p869111017438"><a name="p869111017438"></a><a name="p869111017438"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="p16691703437"><a name="p16691703437"></a><a name="p16691703437"></a>≥ 1 byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="p85671317112017"><a name="p85671317112017"></a><a name="p85671317112017"></a>Measurement object: classic load balancer</p>
<p id="p11647195132013"><a name="p11647195132013"></a><a name="p11647195132013"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="p069115019435"><a name="p069115019435"></a><a name="p069115019435"></a>1 minute</p>
</td>
</tr>
<tr id="row1691180134319"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="p64070218581"><a name="p64070218581"></a><a name="p64070218581"></a>m8_out_Bps</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="p8691802439"><a name="p8691802439"></a><a name="p8691802439"></a>Outbound Rate</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="p2069111094312"><a name="p2069111094312"></a><a name="p2069111094312"></a>Outgoing bytes sent from the monitored object per second</p>
<p id="p17691110114315"><a name="p17691110114315"></a><a name="p17691110114315"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="p869117018435"><a name="p869117018435"></a><a name="p869117018435"></a>≥ 1 byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="p202565415332"><a name="p202565415332"></a><a name="p202565415332"></a>Monitored object: a classic load balancer</p>
<p id="p1657572464717"><a name="p1657572464717"></a><a name="p1657572464717"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="p06911102434"><a name="p06911102434"></a><a name="p06911102434"></a>1 minute</p>
</td>
</tr>
<tr id="row1269150154315"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="p88291732185820"><a name="p88291732185820"></a><a name="p88291732185820"></a>m9_abnormal_servers</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="p8691502439"><a name="p8691502439"></a><a name="p8691502439"></a>Unhealthy Servers</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="p12691190104315"><a name="p12691190104315"></a><a name="p12691190104315"></a>Number of backend servers considered unhealthy</p>
<p id="p1969110104315"><a name="p1969110104315"></a><a name="p1969110104315"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="p11692120154316"><a name="p11692120154316"></a><a name="p11692120154316"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="p4890196343"><a name="p4890196343"></a><a name="p4890196343"></a>Monitored object: a classic load balancer</p>
<p id="p116137244471"><a name="p116137244471"></a><a name="p116137244471"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="p869215064313"><a name="p869215064313"></a><a name="p869215064313"></a>1 minute</p>
</td>
</tr>
<tr id="row169214011439"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.1 "><p id="p48291932145815"><a name="p48291932145815"></a><a name="p48291932145815"></a>ma_normal_servers</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.7.1.2 "><p id="p136924034314"><a name="p136924034314"></a><a name="p136924034314"></a>Healthy Servers</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.7.1.3 "><p id="p1569260174312"><a name="p1569260174312"></a><a name="p1569260174312"></a>Number of backend servers considered healthy</p>
<p id="p969218016435"><a name="p969218016435"></a><a name="p969218016435"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.7.1.4 "><p id="p36921004318"><a name="p36921004318"></a><a name="p36921004318"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.7.1.5 "><p id="p1039615130342"><a name="p1039615130342"></a><a name="p1039615130342"></a>Monitored object: a classic load balancer</p>
<p id="p1765572412474"><a name="p1765572412474"></a><a name="p1765572412474"></a>Dimension: lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.7.1.6 "><p id="p469216014312"><a name="p469216014312"></a><a name="p469216014312"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

## Metrics of enhanced load balancer and enhanced load balancer listeners<a name="section12348155465819"></a>

<a name="table173712719019"></a>
<table><thead align="left"><tr id="row4378277012"><th class="cellrowborder" valign="top" width="9.090909090909092%" id="mcps1.1.7.1.1"><p id="p21500591400"><a name="p21500591400"></a><a name="p21500591400"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.1.7.1.2"><p id="p11507599016"><a name="p11507599016"></a><a name="p11507599016"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.1.7.1.3"><p id="p17150145915010"><a name="p17150145915010"></a><a name="p17150145915010"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.1.7.1.4"><p id="p1115015592000"><a name="p1115015592000"></a><a name="p1115015592000"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.1.7.1.5"><p id="p14150859706"><a name="p14150859706"></a><a name="p14150859706"></a>Measurement Object &amp; Dimension</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.1.7.1.6"><p id="p81501859405"><a name="p81501859405"></a><a name="p81501859405"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row1381271805"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="p847416411252"><a name="p847416411252"></a><a name="p847416411252"></a>m1_cps</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="p838727303"><a name="p838727303"></a><a name="p838727303"></a>Concurrent Connections</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="p638202716013"><a name="p638202716013"></a><a name="p638202716013"></a>Total number of concurrent connections processed by the monitored object</p>
<p id="p83822713017"><a name="p83822713017"></a><a name="p83822713017"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="p1438142710018"><a name="p1438142710018"></a><a name="p1438142710018"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="p13882711010"><a name="p13882711010"></a><a name="p13882711010"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="p34567242116"><a name="p34567242116"></a><a name="p34567242116"></a>Dimensions<sup id="sup1245616247117"><a name="sup1245616247117"></a><a name="sup1245616247117"></a>a</sup>: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="p16382275017"><a name="p16382275017"></a><a name="p16382275017"></a>1 minute</p>
</td>
</tr>
<tr id="row15388271010"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="p14741441358"><a name="p14741441358"></a><a name="p14741441358"></a>m2_act_conn</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="p3383278014"><a name="p3383278014"></a><a name="p3383278014"></a>Active Connections</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="p1538427605"><a name="p1538427605"></a><a name="p1538427605"></a>Total number of active connections processed by the monitored object</p>
<p id="p1038227308"><a name="p1038227308"></a><a name="p1038227308"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="p1138727605"><a name="p1138727605"></a><a name="p1138727605"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="p1438132717013"><a name="p1438132717013"></a><a name="p1438132717013"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="p12408029259"><a name="p12408029259"></a><a name="p12408029259"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="p123812271808"><a name="p123812271808"></a><a name="p123812271808"></a>1 minute</p>
</td>
</tr>
<tr id="row123814271407"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="p9475114113520"><a name="p9475114113520"></a><a name="p9475114113520"></a>m3_inact_conn</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="p7391027203"><a name="p7391027203"></a><a name="p7391027203"></a>Inactive Connections</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="p19396272011"><a name="p19396272011"></a><a name="p19396272011"></a>Total number of non-active connections processed by the monitored object</p>
<p id="p203914271014"><a name="p203914271014"></a><a name="p203914271014"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="p4393271907"><a name="p4393271907"></a><a name="p4393271907"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="p14391271206"><a name="p14391271206"></a><a name="p14391271206"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="p1753172518818"><a name="p1753172518818"></a><a name="p1753172518818"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="p83912720015"><a name="p83912720015"></a><a name="p83912720015"></a>1 minute</p>
</td>
</tr>
<tr id="row939102719012"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="p10475114119519"><a name="p10475114119519"></a><a name="p10475114119519"></a>m4_ncps</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="p13398271406"><a name="p13398271406"></a><a name="p13398271406"></a>New Connections</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="p11391327003"><a name="p11391327003"></a><a name="p11391327003"></a>Total number of new connections processed by the monitored object</p>
<p id="p0397272017"><a name="p0397272017"></a><a name="p0397272017"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="p33910271703"><a name="p33910271703"></a><a name="p33910271703"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="p53910271709"><a name="p53910271709"></a><a name="p53910271709"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="p189546311780"><a name="p189546311780"></a><a name="p189546311780"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="p9394271304"><a name="p9394271304"></a><a name="p9394271304"></a>1 minute</p>
</td>
</tr>
<tr id="row639527908"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="p447544118511"><a name="p447544118511"></a><a name="p447544118511"></a>m5_in_pps</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="p43992712015"><a name="p43992712015"></a><a name="p43992712015"></a>Incoming Packets</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="p2040627607"><a name="p2040627607"></a><a name="p2040627607"></a>Incoming packets received by the monitored object per second</p>
<p id="p114012272003"><a name="p114012272003"></a><a name="p114012272003"></a>Unit: Packet/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="p640527402"><a name="p640527402"></a><a name="p640527402"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="p12401271900"><a name="p12401271900"></a><a name="p12401271900"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="p1773114913819"><a name="p1773114913819"></a><a name="p1773114913819"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="p174020270014"><a name="p174020270014"></a><a name="p174020270014"></a>1 minute</p>
</td>
</tr>
<tr id="row8407271908"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="p747516411659"><a name="p747516411659"></a><a name="p747516411659"></a>m6_out_pps</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="p54011271606"><a name="p54011271606"></a><a name="p54011271606"></a>Outgoing Packets</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="p1940527102"><a name="p1940527102"></a><a name="p1940527102"></a>Outgoing packets sent from the monitored object per second</p>
<p id="p194015278012"><a name="p194015278012"></a><a name="p194015278012"></a>Unit: Packet/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="p134011278011"><a name="p134011278011"></a><a name="p134011278011"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="p154082715019"><a name="p154082715019"></a><a name="p154082715019"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="p17411115812814"><a name="p17411115812814"></a><a name="p17411115812814"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="p64072713012"><a name="p64072713012"></a><a name="p64072713012"></a>1 minute</p>
</td>
</tr>
<tr id="row17401727203"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="p247514115516"><a name="p247514115516"></a><a name="p247514115516"></a>m7_in_Bps</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="p14011277010"><a name="p14011277010"></a><a name="p14011277010"></a>Inbound Rate</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="p44011275017"><a name="p44011275017"></a><a name="p44011275017"></a>Incoming bytes received by the monitored object per second</p>
<p id="p124013273016"><a name="p124013273016"></a><a name="p124013273016"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="p64192712019"><a name="p64192712019"></a><a name="p64192712019"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="p041112711017"><a name="p041112711017"></a><a name="p041112711017"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="p7911967913"><a name="p7911967913"></a><a name="p7911967913"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="p64118270012"><a name="p64118270012"></a><a name="p64118270012"></a>1 minute</p>
</td>
</tr>
<tr id="row12411276015"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="p1147520415511"><a name="p1147520415511"></a><a name="p1147520415511"></a>m8_out_Bps</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="p24111271013"><a name="p24111271013"></a><a name="p24111271013"></a>Outbound Rate</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="p941162717012"><a name="p941162717012"></a><a name="p941162717012"></a>Outgoing bytes sent from the monitored object per second</p>
<p id="p114110279019"><a name="p114110279019"></a><a name="p114110279019"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="p6414270019"><a name="p6414270019"></a><a name="p6414270019"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="p44119277018"><a name="p44119277018"></a><a name="p44119277018"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="p104551620793"><a name="p104551620793"></a><a name="p104551620793"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="p10413276013"><a name="p10413276013"></a><a name="p10413276013"></a>1 minute</p>
</td>
</tr>
<tr id="row441152710011"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="p114758411551"><a name="p114758411551"></a><a name="p114758411551"></a>m9_abnormal_servers</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="p184118277017"><a name="p184118277017"></a><a name="p184118277017"></a>Unhealthy Servers</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="p64117278012"><a name="p64117278012"></a><a name="p64117278012"></a>Number of backend servers considered unhealthy</p>
<p id="p34111276011"><a name="p34111276011"></a><a name="p34111276011"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="p20421827404"><a name="p20421827404"></a><a name="p20421827404"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="p54232718017"><a name="p54232718017"></a><a name="p54232718017"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="p1052123815118"><a name="p1052123815118"></a><a name="p1052123815118"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="p34219271209"><a name="p34219271209"></a><a name="p34219271209"></a>1 minute</p>
</td>
</tr>
<tr id="row4420271009"><td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.1 "><p id="p0475114111514"><a name="p0475114111514"></a><a name="p0475114111514"></a>ma_normal_servers</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.2 "><p id="p15425271805"><a name="p15425271805"></a><a name="p15425271805"></a>Healthy Servers</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.1.7.1.3 "><p id="p1742627702"><a name="p1742627702"></a><a name="p1742627702"></a>Number of backend servers considered healthy</p>
<p id="p84220271019"><a name="p84220271019"></a><a name="p84220271019"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.7.1.4 "><p id="p184212717016"><a name="p184212717016"></a><a name="p184212717016"></a>≥ 1</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.7.1.5 "><p id="p74215271202"><a name="p74215271202"></a><a name="p74215271202"></a>Monitored object: an enhanced load balancer or enhanced load balancer listener</p>
<p id="p1034312920111"><a name="p1034312920111"></a><a name="p1034312920111"></a>Dimensions: lbaas_instance_id and lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.7.1.6 "><p id="p11421927101"><a name="p11421927101"></a><a name="p11421927101"></a>1 minute</p>
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


## Dimensions<a name="en-us_topic_0021772779_en-us_topic_0021733202_section25639464162814"></a>

<a name="table262063515438"></a>
<table><thead align="left"><tr id="row17620163515436"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p462012358431"><a name="p462012358431"></a><a name="p462012358431"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p14620235194314"><a name="p14620235194314"></a><a name="p14620235194314"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row8620103517438"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p56207352436"><a name="p56207352436"></a><a name="p56207352436"></a>lb_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1062073584312"><a name="p1062073584312"></a><a name="p1062073584312"></a>ID of a classic load balancer</p>
</td>
</tr>
<tr id="row062010350437"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p462014358431"><a name="p462014358431"></a><a name="p462014358431"></a>lbaas_instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p17621173519434"><a name="p17621173519434"></a><a name="p17621173519434"></a>ID of an enhanced load balancer</p>
</td>
</tr>
<tr id="row1621163514436"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1862110353435"><a name="p1862110353435"></a><a name="p1862110353435"></a>lbaas_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p12621103520435"><a name="p12621103520435"></a><a name="p12621103520435"></a>ID of an enhanced load balancer listener</p>
</td>
</tr>
</tbody>
</table>
