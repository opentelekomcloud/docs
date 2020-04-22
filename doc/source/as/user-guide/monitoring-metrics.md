# Monitoring Metrics<a name="EN-US_TOPIC_0108337598"></a>

[Table 1](#en-us_topic_0042018317_table57136275115435)  lists the AS metrics supported by Cloud Eye.

**Table  1**  AS metrics

<a name="en-us_topic_0042018317_table57136275115435"></a>
<table><thead align="left"><tr id="en-us_topic_0042018317_row26323242"><th class="cellrowborder" valign="top" width="13.858614138586143%" id="mcps1.2.7.1.1"><p id="p9460135411424"><a name="p9460135411424"></a><a name="p9460135411424"></a><strong id="b19884145812613"><a name="b19884145812613"></a><a name="b19884145812613"></a>Metric ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.148585141485851%" id="mcps1.2.7.1.2"><p id="en-us_topic_0042018317_p51807830"><a name="en-us_topic_0042018317_p51807830"></a><a name="en-us_topic_0042018317_p51807830"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="32.736726327367265%" id="mcps1.2.7.1.3"><p id="en-us_topic_0042018317_p35684727"><a name="en-us_topic_0042018317_p35684727"></a><a name="en-us_topic_0042018317_p35684727"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="11.6988301169883%" id="mcps1.2.7.1.4"><p id="p13478947195214"><a name="p13478947195214"></a><a name="p13478947195214"></a><strong id="b18541936163312"><a name="b18541936163312"></a><a name="b18541936163312"></a>Value Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.608539146085391%" id="mcps1.2.7.1.5"><p id="en-us_topic_0042018317_p51782583"><a name="en-us_topic_0042018317_p51782583"></a><a name="en-us_topic_0042018317_p51782583"></a><strong id="b276983816338"><a name="b276983816338"></a><a name="b276983816338"></a>Monitored Object &amp; Dimension</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.94870512948705%" id="mcps1.2.7.1.6"><p id="en-us_topic_0042018317_p47235721105619"><a name="en-us_topic_0042018317_p47235721105619"></a><a name="en-us_topic_0042018317_p47235721105619"></a>Monitoring Interval (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0042018317_row33639718"><td class="cellrowborder" valign="top" width="13.858614138586143%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0043063076_p26463451162545"><a name="en-us_topic_0043063076_p26463451162545"></a><a name="en-us_topic_0043063076_p26463451162545"></a>cpu_util</p>
</td>
<td class="cellrowborder" valign="top" width="14.148585141485851%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0042018317_p40462633"><a name="en-us_topic_0042018317_p40462633"></a><a name="en-us_topic_0042018317_p40462633"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="32.736726327367265%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0042018317_p106912192911"><a name="en-us_topic_0042018317_p106912192911"></a><a name="en-us_topic_0042018317_p106912192911"></a>CPU usage of an AS group</p>
<p id="en-us_topic_0042018317_p5508516122917"><a name="en-us_topic_0042018317_p5508516122917"></a><a name="en-us_topic_0042018317_p5508516122917"></a>Formula: Total CPU usage of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0042018317_p56247849"><a name="en-us_topic_0042018317_p56247849"></a><a name="en-us_topic_0042018317_p56247849"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="11.6988301169883%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0043063076_p39523811162614"><a name="en-us_topic_0043063076_p39523811162614"></a><a name="en-us_topic_0043063076_p39523811162614"></a>≥0%</p>
</td>
<td class="cellrowborder" valign="top" width="14.608539146085391%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0042018317_en-us_topic_0030911465_p13045074222846"><a name="en-us_topic_0042018317_en-us_topic_0030911465_p13045074222846"></a><a name="en-us_topic_0042018317_en-us_topic_0030911465_p13045074222846"></a>Object: AS group</p>
<p id="p484410613498"><a name="p484410613498"></a><a name="p484410613498"></a>Dimension:</p>
<p id="p198441165499"><a name="p198441165499"></a><a name="p198441165499"></a>AutoScalingGroup</p>
</td>
<td class="cellrowborder" valign="top" width="12.94870512948705%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0042018317_p888164105619"><a name="en-us_topic_0042018317_p888164105619"></a><a name="en-us_topic_0042018317_p888164105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0042018317_row27353390"><td class="cellrowborder" valign="top" width="13.858614138586143%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0043063076_p10426432162545"><a name="en-us_topic_0043063076_p10426432162545"></a><a name="en-us_topic_0043063076_p10426432162545"></a>mem_util</p>
</td>
<td class="cellrowborder" valign="top" width="14.148585141485851%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0042018317_p1032124"><a name="en-us_topic_0042018317_p1032124"></a><a name="en-us_topic_0042018317_p1032124"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="32.736726327367265%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0042018317_p16493259"><a name="en-us_topic_0042018317_p16493259"></a><a name="en-us_topic_0042018317_p16493259"></a>Memory usage of an AS group</p>
<p id="en-us_topic_0042018317_p3415225303"><a name="en-us_topic_0042018317_p3415225303"></a><a name="en-us_topic_0042018317_p3415225303"></a>Formula: Total memory usage of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0042018317_p12329122213307"><a name="en-us_topic_0042018317_p12329122213307"></a><a name="en-us_topic_0042018317_p12329122213307"></a>Unit: Percent</p>
<div class="note" id="en-us_topic_0042018317_note193017546365"><a name="en-us_topic_0042018317_note193017546365"></a><a name="en-us_topic_0042018317_note193017546365"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0042018317_p1130265414365"><a name="en-us_topic_0042018317_p1130265414365"></a><a name="en-us_topic_0042018317_p1130265414365"></a>This metric is unavailable if the image has no OTC Tools installed.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="11.6988301169883%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0043063076_p47312124162614"><a name="en-us_topic_0043063076_p47312124162614"></a><a name="en-us_topic_0043063076_p47312124162614"></a>≥0%</p>
</td>
<td class="cellrowborder" valign="top" width="14.608539146085391%" headers="mcps1.2.7.1.5 "><p id="p08093589532"><a name="p08093589532"></a><a name="p08093589532"></a>Object: AS group</p>
<p id="p20810958125315"><a name="p20810958125315"></a><a name="p20810958125315"></a>Dimension:</p>
<p id="p1481045814533"><a name="p1481045814533"></a><a name="p1481045814533"></a>AutoScalingGroup</p>
</td>
<td class="cellrowborder" valign="top" width="12.94870512948705%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0042018317_p4832464105619"><a name="en-us_topic_0042018317_p4832464105619"></a><a name="en-us_topic_0042018317_p4832464105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0042018317_row26669028"><td class="cellrowborder" valign="top" width="13.858614138586143%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0043063076_p13712924162545"><a name="en-us_topic_0043063076_p13712924162545"></a><a name="en-us_topic_0043063076_p13712924162545"></a>network_incoming_bytes_rate_inband</p>
</td>
<td class="cellrowborder" valign="top" width="14.148585141485851%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0042018317_p63671394104552"><a name="en-us_topic_0042018317_p63671394104552"></a><a name="en-us_topic_0042018317_p63671394104552"></a>Number of Instances</p>
</td>
<td class="cellrowborder" valign="top" width="32.736726327367265%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0042018317_p30149174143433"><a name="en-us_topic_0042018317_p30149174143433"></a><a name="en-us_topic_0042018317_p30149174143433"></a>Number of available ECSs in an AS group</p>
<p id="en-us_topic_0042018317_p1954317478339"><a name="en-us_topic_0042018317_p1954317478339"></a><a name="en-us_topic_0042018317_p1954317478339"></a>Formula: Total number of ECSs in <strong id="b7513363348"><a name="b7513363348"></a><a name="b7513363348"></a>Enabled</strong> state in the AS group</p>
</td>
<td class="cellrowborder" valign="top" width="11.6988301169883%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0043063076_p7076870162614"><a name="en-us_topic_0043063076_p7076870162614"></a><a name="en-us_topic_0043063076_p7076870162614"></a>≥0 Byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.608539146085391%" headers="mcps1.2.7.1.5 "><p id="p15463102105419"><a name="p15463102105419"></a><a name="p15463102105419"></a>Object: AS group</p>
<p id="p2046313245418"><a name="p2046313245418"></a><a name="p2046313245418"></a>Dimension:</p>
<p id="p194633210542"><a name="p194633210542"></a><a name="p194633210542"></a>AutoScalingGroup</p>
</td>
<td class="cellrowborder" valign="top" width="12.94870512948705%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0042018317_p55885300105619"><a name="en-us_topic_0042018317_p55885300105619"></a><a name="en-us_topic_0042018317_p55885300105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0042018317_row49150562"><td class="cellrowborder" valign="top" width="13.858614138586143%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0043063076_p66043059162545"><a name="en-us_topic_0043063076_p66043059162545"></a><a name="en-us_topic_0043063076_p66043059162545"></a>network_outgoing_bytes_rate_inband</p>
</td>
<td class="cellrowborder" valign="top" width="14.148585141485851%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0042018317_p21772565"><a name="en-us_topic_0042018317_p21772565"></a><a name="en-us_topic_0042018317_p21772565"></a>Inband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="32.736726327367265%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0042018317_p18747312"><a name="en-us_topic_0042018317_p18747312"></a><a name="en-us_topic_0042018317_p18747312"></a>Number of incoming bytes per second on an ECS in an AS group</p>
<p id="en-us_topic_0042018317_p11415571347"><a name="en-us_topic_0042018317_p11415571347"></a><a name="en-us_topic_0042018317_p11415571347"></a>Formula: Total inband incoming rates of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0042018317_p1573177133411"><a name="en-us_topic_0042018317_p1573177133411"></a><a name="en-us_topic_0042018317_p1573177133411"></a>Unit: Byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.6988301169883%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0043063076_p834095511437"><a name="en-us_topic_0043063076_p834095511437"></a><a name="en-us_topic_0043063076_p834095511437"></a>≥0 Byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.608539146085391%" headers="mcps1.2.7.1.5 "><p id="p1812414142549"><a name="p1812414142549"></a><a name="p1812414142549"></a>Object: AS group</p>
<p id="p51241214155418"><a name="p51241214155418"></a><a name="p51241214155418"></a>Dimension:</p>
<p id="p1312441418546"><a name="p1312441418546"></a><a name="p1312441418546"></a>AutoScalingGroup</p>
</td>
<td class="cellrowborder" valign="top" width="12.94870512948705%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0042018317_p30415481105619"><a name="en-us_topic_0042018317_p30415481105619"></a><a name="en-us_topic_0042018317_p30415481105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0042018317_row49347015"><td class="cellrowborder" valign="top" width="13.858614138586143%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0043063076_p14042138104552"><a name="en-us_topic_0043063076_p14042138104552"></a><a name="en-us_topic_0043063076_p14042138104552"></a>instance_num</p>
</td>
<td class="cellrowborder" valign="top" width="14.148585141485851%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0042018317_p37685299"><a name="en-us_topic_0042018317_p37685299"></a><a name="en-us_topic_0042018317_p37685299"></a>Inband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="32.736726327367265%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0042018317_p32610412"><a name="en-us_topic_0042018317_p32610412"></a><a name="en-us_topic_0042018317_p32610412"></a>Number of outgoing bytes per second on an ECS in an AS group</p>
<p id="en-us_topic_0042018317_p91607516343"><a name="en-us_topic_0042018317_p91607516343"></a><a name="en-us_topic_0042018317_p91607516343"></a>Formula: Total inband outgoing rates of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0042018317_p1949715114340"><a name="en-us_topic_0042018317_p1949715114340"></a><a name="en-us_topic_0042018317_p1949715114340"></a>Unit: Byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.6988301169883%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0043063076_p62450816104552"><a name="en-us_topic_0043063076_p62450816104552"></a><a name="en-us_topic_0043063076_p62450816104552"></a>≥0</p>
</td>
<td class="cellrowborder" valign="top" width="14.608539146085391%" headers="mcps1.2.7.1.5 "><p id="p4129131425418"><a name="p4129131425418"></a><a name="p4129131425418"></a>Object: AS group</p>
<p id="p6129111417542"><a name="p6129111417542"></a><a name="p6129111417542"></a>Dimension:</p>
<p id="p1129101405415"><a name="p1129101405415"></a><a name="p1129101405415"></a>AutoScalingGroup</p>
</td>
<td class="cellrowborder" valign="top" width="12.94870512948705%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0042018317_p47734919105619"><a name="en-us_topic_0042018317_p47734919105619"></a><a name="en-us_topic_0042018317_p47734919105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0042018317_row49585291175830"><td class="cellrowborder" valign="top" width="13.858614138586143%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0043063076_p52067206164320"><a name="en-us_topic_0043063076_p52067206164320"></a><a name="en-us_topic_0043063076_p52067206164320"></a>disk_read_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="14.148585141485851%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0042018317_p1411176318214"><a name="en-us_topic_0042018317_p1411176318214"></a><a name="en-us_topic_0042018317_p1411176318214"></a>Disks Read Rate</p>
</td>
<td class="cellrowborder" valign="top" width="32.736726327367265%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0042018317_p220213918214"><a name="en-us_topic_0042018317_p220213918214"></a><a name="en-us_topic_0042018317_p220213918214"></a>Number of bytes read from an AS group per second</p>
<p id="en-us_topic_0042018317_p16302131413351"><a name="en-us_topic_0042018317_p16302131413351"></a><a name="en-us_topic_0042018317_p16302131413351"></a>Formula: Total disks read rates of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0042018317_p1053317144359"><a name="en-us_topic_0042018317_p1053317144359"></a><a name="en-us_topic_0042018317_p1053317144359"></a>Unit: Byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.6988301169883%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0043063076_p438577111428"><a name="en-us_topic_0043063076_p438577111428"></a><a name="en-us_topic_0043063076_p438577111428"></a>≥0 Byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.608539146085391%" headers="mcps1.2.7.1.5 "><p id="p3137191417540"><a name="p3137191417540"></a><a name="p3137191417540"></a>Object: AS group</p>
<p id="p13137181435414"><a name="p13137181435414"></a><a name="p13137181435414"></a>Dimension:</p>
<p id="p1613751445411"><a name="p1613751445411"></a><a name="p1613751445411"></a>AutoScalingGroup</p>
</td>
<td class="cellrowborder" valign="top" width="12.94870512948705%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0042018317_p41323205105619"><a name="en-us_topic_0042018317_p41323205105619"></a><a name="en-us_topic_0042018317_p41323205105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0042018317_row34742176175835"><td class="cellrowborder" valign="top" width="13.858614138586143%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0043063076_p4535684164320"><a name="en-us_topic_0043063076_p4535684164320"></a><a name="en-us_topic_0043063076_p4535684164320"></a>disk_write_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="14.148585141485851%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0042018317_p4424835218214"><a name="en-us_topic_0042018317_p4424835218214"></a><a name="en-us_topic_0042018317_p4424835218214"></a>Disks Write Rate</p>
</td>
<td class="cellrowborder" valign="top" width="32.736726327367265%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0042018317_p10694175583519"><a name="en-us_topic_0042018317_p10694175583519"></a><a name="en-us_topic_0042018317_p10694175583519"></a>Number of bytes written to an AS group per second</p>
<p id="en-us_topic_0042018317_p2734677318214"><a name="en-us_topic_0042018317_p2734677318214"></a><a name="en-us_topic_0042018317_p2734677318214"></a>Formula: Total disks write rates of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0042018317_p555217291353"><a name="en-us_topic_0042018317_p555217291353"></a><a name="en-us_topic_0042018317_p555217291353"></a>Unit: Byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.6988301169883%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0043063076_p41383251164320"><a name="en-us_topic_0043063076_p41383251164320"></a><a name="en-us_topic_0043063076_p41383251164320"></a>≥0 Byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.608539146085391%" headers="mcps1.2.7.1.5 "><p id="p1214361495411"><a name="p1214361495411"></a><a name="p1214361495411"></a>Object: AS group</p>
<p id="p21431414195417"><a name="p21431414195417"></a><a name="p21431414195417"></a>Dimension:</p>
<p id="p121431214105413"><a name="p121431214105413"></a><a name="p121431214105413"></a>AutoScalingGroup</p>
</td>
<td class="cellrowborder" valign="top" width="12.94870512948705%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0042018317_p58845275105619"><a name="en-us_topic_0042018317_p58845275105619"></a><a name="en-us_topic_0042018317_p58845275105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0042018317_row18531428175847"><td class="cellrowborder" valign="top" width="13.858614138586143%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0043063076_p40894923164320"><a name="en-us_topic_0043063076_p40894923164320"></a><a name="en-us_topic_0043063076_p40894923164320"></a>disk_read_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="14.148585141485851%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0042018317_p3630726418214"><a name="en-us_topic_0042018317_p3630726418214"></a><a name="en-us_topic_0042018317_p3630726418214"></a>Disks Read Requests</p>
</td>
<td class="cellrowborder" valign="top" width="32.736726327367265%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0042018317_p5520727618214"><a name="en-us_topic_0042018317_p5520727618214"></a><a name="en-us_topic_0042018317_p5520727618214"></a>Number of read requests per second sent to an ECS disk in an AS group</p>
<p id="en-us_topic_0042018317_p32533663612"><a name="en-us_topic_0042018317_p32533663612"></a><a name="en-us_topic_0042018317_p32533663612"></a>Formula: Total disks read rates of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0042018317_p363319663618"><a name="en-us_topic_0042018317_p363319663618"></a><a name="en-us_topic_0042018317_p363319663618"></a>Unit: Request/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.6988301169883%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0043063076_p33600476164320"><a name="en-us_topic_0043063076_p33600476164320"></a><a name="en-us_topic_0043063076_p33600476164320"></a>≥0 request/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.608539146085391%" headers="mcps1.2.7.1.5 "><p id="p14149141414546"><a name="p14149141414546"></a><a name="p14149141414546"></a>Object: AS group</p>
<p id="p1114915142541"><a name="p1114915142541"></a><a name="p1114915142541"></a>Dimension:</p>
<p id="p15149171415541"><a name="p15149171415541"></a><a name="p15149171415541"></a>AutoScalingGroup</p>
</td>
<td class="cellrowborder" valign="top" width="12.94870512948705%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0042018317_p1737970105619"><a name="en-us_topic_0042018317_p1737970105619"></a><a name="en-us_topic_0042018317_p1737970105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0042018317_row32523856175914"><td class="cellrowborder" valign="top" width="13.858614138586143%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0043063076_p8904702164320"><a name="en-us_topic_0043063076_p8904702164320"></a><a name="en-us_topic_0043063076_p8904702164320"></a>disk_write_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="14.148585141485851%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0042018317_p4789499918214"><a name="en-us_topic_0042018317_p4789499918214"></a><a name="en-us_topic_0042018317_p4789499918214"></a>Disks Write Requests</p>
</td>
<td class="cellrowborder" valign="top" width="32.736726327367265%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0042018317_p5428973118214"><a name="en-us_topic_0042018317_p5428973118214"></a><a name="en-us_topic_0042018317_p5428973118214"></a>Number of write requests per second sent to an ECS disk in an AS group</p>
<p id="en-us_topic_0042018317_p10201517123617"><a name="en-us_topic_0042018317_p10201517123617"></a><a name="en-us_topic_0042018317_p10201517123617"></a>Formula: Total disks write rates of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0042018317_p13201617163613"><a name="en-us_topic_0042018317_p13201617163613"></a><a name="en-us_topic_0042018317_p13201617163613"></a>Unit: Request/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.6988301169883%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0043063076_p8106792164320"><a name="en-us_topic_0043063076_p8106792164320"></a><a name="en-us_topic_0043063076_p8106792164320"></a>≥0 request/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.608539146085391%" headers="mcps1.2.7.1.5 "><p id="p14155914195420"><a name="p14155914195420"></a><a name="p14155914195420"></a>Object: AS group</p>
<p id="p151551314185413"><a name="p151551314185413"></a><a name="p151551314185413"></a>Dimension:</p>
<p id="p61556144544"><a name="p61556144544"></a><a name="p61556144544"></a>AutoScalingGroup</p>
</td>
<td class="cellrowborder" valign="top" width="12.94870512948705%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0042018317_p6557873105619"><a name="en-us_topic_0042018317_p6557873105619"></a><a name="en-us_topic_0042018317_p6557873105619"></a>5 minutes</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   The image based on which the target ECS is created must have OTC Tools installed. Otherwise,  **Memory Usage**  will be unavailable. For details about how to install the OTC Tools, visit  [https://github.com/UVP-Tools/UVP-Tools/](https://github.com/UVP-Tools/UVP-Tools/).  
>-   OSs determine whether the  **Memory Usage**,  **Inband Outgoing Rate**, and  **Inband Incoming Rate**  metrics are supported. For details, see  _[Elastic Cloud Server User Guide](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0030911465.html)_.  

