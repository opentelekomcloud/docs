# ECS Metrics<a name="EN-US_TOPIC_0171212508"></a>

## Function<a name="en-us_topic_0022067719_section25901060112133"></a>

This section describes monitoring metrics reported by ECS to Cloud Eye as well as their namespaces and dimensions. You can use APIs provided by Cloud Eye to view the monitoring metrics of the monitored object and alarms generated for ECS.

## Namespace<a name="en-us_topic_0022067719_section24282572112133"></a>

SYS.ECS

## Metrics<a name="en-us_topic_0022067719_section52364133112133"></a>

<a name="en-us_topic_0022067719_table13636366112133"></a>
<table><thead align="left"><tr id="en-us_topic_0022067719_row32163296112133"><th class="cellrowborder" valign="top" width="15.150000000000002%" id="mcps1.1.6.1.1"><p id="en-us_topic_0022067719_p55090151112133"><a name="en-us_topic_0022067719_p55090151112133"></a><a name="en-us_topic_0022067719_p55090151112133"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="16.020000000000003%" id="mcps1.1.6.1.2"><p id="en-us_topic_0022067719_p33117267112133"><a name="en-us_topic_0022067719_p33117267112133"></a><a name="en-us_topic_0022067719_p33117267112133"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25.420000000000005%" id="mcps1.1.6.1.3"><p id="en-us_topic_0022067719_p65253004112133"><a name="en-us_topic_0022067719_p65253004112133"></a><a name="en-us_topic_0022067719_p65253004112133"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="18.980000000000004%" id="mcps1.1.6.1.4"><p id="en-us_topic_0022067719_p51001977112133"><a name="en-us_topic_0022067719_p51001977112133"></a><a name="en-us_topic_0022067719_p51001977112133"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="24.430000000000003%" id="mcps1.1.6.1.5"><p id="en-us_topic_0022067719_p37519491112133"><a name="en-us_topic_0022067719_p37519491112133"></a><a name="en-us_topic_0022067719_p37519491112133"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0022067719_row19179921112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0022067719_p10069772112133"><a name="en-us_topic_0022067719_p10069772112133"></a><a name="en-us_topic_0022067719_p10069772112133"></a>cpu_util</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0022067719_p10345179112133"><a name="en-us_topic_0022067719_p10345179112133"></a><a name="en-us_topic_0022067719_p10345179112133"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0022067719_p32653159112133"><a name="en-us_topic_0022067719_p32653159112133"></a><a name="en-us_topic_0022067719_p32653159112133"></a>This metric is used to show CPU usages (%) of monitored objects.</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0022067719_p31614322112133"><a name="en-us_topic_0022067719_p31614322112133"></a><a name="en-us_topic_0022067719_p31614322112133"></a>0% to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0022067719_p10623276112133"><a name="en-us_topic_0022067719_p10623276112133"></a><a name="en-us_topic_0022067719_p10623276112133"></a>Monitored object: ECS</p>
<div class="note" id="en-us_topic_0022067719_note609891291230"><a name="en-us_topic_0022067719_note609891291230"></a><a name="en-us_topic_0022067719_note609891291230"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0022067719_p120312521230"><a name="en-us_topic_0022067719_p120312521230"></a><a name="en-us_topic_0022067719_p120312521230"></a>The metrics collected using OTC tools are accurate.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0022067719_row55179047112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0022067719_p40317835112133"><a name="en-us_topic_0022067719_p40317835112133"></a><a name="en-us_topic_0022067719_p40317835112133"></a>mem_util</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0022067719_p44519166112133"><a name="en-us_topic_0022067719_p44519166112133"></a><a name="en-us_topic_0022067719_p44519166112133"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0022067719_p49282731112133"><a name="en-us_topic_0022067719_p49282731112133"></a><a name="en-us_topic_0022067719_p49282731112133"></a>This metric is used to show memory usages (%) of monitored objects.</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0022067719_p13493709112133"><a name="en-us_topic_0022067719_p13493709112133"></a><a name="en-us_topic_0022067719_p13493709112133"></a>0% to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0022067719_p19248659112133"><a name="en-us_topic_0022067719_p19248659112133"></a><a name="en-us_topic_0022067719_p19248659112133"></a>Monitored object: ECS</p>
<div class="note" id="en-us_topic_0022067719_note1851305616219"><a name="en-us_topic_0022067719_note1851305616219"></a><a name="en-us_topic_0022067719_note1851305616219"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0022067719_p3239978216219"><a name="en-us_topic_0022067719_p3239978216219"></a><a name="en-us_topic_0022067719_p3239978216219"></a>This metric is unavailable if the image has no OTC Tools installed.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0022067719_row15637553112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0022067719_p58682320112133"><a name="en-us_topic_0022067719_p58682320112133"></a><a name="en-us_topic_0022067719_p58682320112133"></a>disk_util_inband</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0022067719_p55647512112133"><a name="en-us_topic_0022067719_p55647512112133"></a><a name="en-us_topic_0022067719_p55647512112133"></a>Disks Usage</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0022067719_p11154608112133"><a name="en-us_topic_0022067719_p11154608112133"></a><a name="en-us_topic_0022067719_p11154608112133"></a>This metric is used to show disk usages (%) of monitored objects.</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0022067719_p11536837112133"><a name="en-us_topic_0022067719_p11536837112133"></a><a name="en-us_topic_0022067719_p11536837112133"></a>0% to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0022067719_p62068605112133"><a name="en-us_topic_0022067719_p62068605112133"></a><a name="en-us_topic_0022067719_p62068605112133"></a>Monitored object: ECS</p>
<div class="note" id="en-us_topic_0022067719_note1022149416225"><a name="en-us_topic_0022067719_note1022149416225"></a><a name="en-us_topic_0022067719_note1022149416225"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0022067719_p2488458916225"><a name="en-us_topic_0022067719_p2488458916225"></a><a name="en-us_topic_0022067719_p2488458916225"></a>This metric is unavailable if the image has no OTC Tools installed.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0022067719_row61501122112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0022067719_p15534971112133"><a name="en-us_topic_0022067719_p15534971112133"></a><a name="en-us_topic_0022067719_p15534971112133"></a>disk_read_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0022067719_p292712452495"><a name="en-us_topic_0022067719_p292712452495"></a><a name="en-us_topic_0022067719_p292712452495"></a>Disk Read Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0022067719_p53692267112133"><a name="en-us_topic_0022067719_p53692267112133"></a><a name="en-us_topic_0022067719_p53692267112133"></a>This metric is used to show the number of bytes read from the monitored object per second (byte/s).</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0022067719_p20538509112133"><a name="en-us_topic_0022067719_p20538509112133"></a><a name="en-us_topic_0022067719_p20538509112133"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0022067719_p53006500112133"><a name="en-us_topic_0022067719_p53006500112133"></a><a name="en-us_topic_0022067719_p53006500112133"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="en-us_topic_0022067719_row65668128112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0022067719_p17518185112133"><a name="en-us_topic_0022067719_p17518185112133"></a><a name="en-us_topic_0022067719_p17518185112133"></a>disk_write_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0022067719_p18939164514497"><a name="en-us_topic_0022067719_p18939164514497"></a><a name="en-us_topic_0022067719_p18939164514497"></a>Disk Write Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0022067719_p46440320112133"><a name="en-us_topic_0022067719_p46440320112133"></a><a name="en-us_topic_0022067719_p46440320112133"></a>This metric is used to show the number of bytes written to the monitored object per second (byte/s).</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0022067719_p66041352112133"><a name="en-us_topic_0022067719_p66041352112133"></a><a name="en-us_topic_0022067719_p66041352112133"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0022067719_p47749284112133"><a name="en-us_topic_0022067719_p47749284112133"></a><a name="en-us_topic_0022067719_p47749284112133"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="en-us_topic_0022067719_row42486756112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0022067719_p18875184112133"><a name="en-us_topic_0022067719_p18875184112133"></a><a name="en-us_topic_0022067719_p18875184112133"></a>disk_read_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0022067719_p59508458491"><a name="en-us_topic_0022067719_p59508458491"></a><a name="en-us_topic_0022067719_p59508458491"></a>Disk Read IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0022067719_p2615947105641"><a name="en-us_topic_0022067719_p2615947105641"></a><a name="en-us_topic_0022067719_p2615947105641"></a>This metric is used to show the number of read requests sent to the monitored object per second (requests/second).</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0022067719_p8134307112133"><a name="en-us_topic_0022067719_p8134307112133"></a><a name="en-us_topic_0022067719_p8134307112133"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0022067719_p54899139112133"><a name="en-us_topic_0022067719_p54899139112133"></a><a name="en-us_topic_0022067719_p54899139112133"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="en-us_topic_0022067719_row17645255112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0022067719_p19979544112133"><a name="en-us_topic_0022067719_p19979544112133"></a><a name="en-us_topic_0022067719_p19979544112133"></a>disk_write_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0022067719_p11969114513496"><a name="en-us_topic_0022067719_p11969114513496"></a><a name="en-us_topic_0022067719_p11969114513496"></a>Disk Write IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0022067719_p22177214112133"><a name="en-us_topic_0022067719_p22177214112133"></a><a name="en-us_topic_0022067719_p22177214112133"></a>This metric is used to show the number of write requests sent to the monitored object per second (requests/second).</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0022067719_p21229150112133"><a name="en-us_topic_0022067719_p21229150112133"></a><a name="en-us_topic_0022067719_p21229150112133"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0022067719_p41839618112133"><a name="en-us_topic_0022067719_p41839618112133"></a><a name="en-us_topic_0022067719_p41839618112133"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="en-us_topic_0022067719_row33565898112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0022067719_p34483231112133"><a name="en-us_topic_0022067719_p34483231112133"></a><a name="en-us_topic_0022067719_p34483231112133"></a>network_incoming_bytes_rate_inband</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0022067719_p41678312112133"><a name="en-us_topic_0022067719_p41678312112133"></a><a name="en-us_topic_0022067719_p41678312112133"></a>Inband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0022067719_p20500110112133"><a name="en-us_topic_0022067719_p20500110112133"></a><a name="en-us_topic_0022067719_p20500110112133"></a>This metric is used to show the number of incoming bytes received by the monitored object per second (byte/s).</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0022067719_p1314054112133"><a name="en-us_topic_0022067719_p1314054112133"></a><a name="en-us_topic_0022067719_p1314054112133"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0022067719_p39329546112133"><a name="en-us_topic_0022067719_p39329546112133"></a><a name="en-us_topic_0022067719_p39329546112133"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="en-us_topic_0022067719_row31576687112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0022067719_p7574877112133"><a name="en-us_topic_0022067719_p7574877112133"></a><a name="en-us_topic_0022067719_p7574877112133"></a>network_outgoing_bytes_rate_inband</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0022067719_p9585275112133"><a name="en-us_topic_0022067719_p9585275112133"></a><a name="en-us_topic_0022067719_p9585275112133"></a>Inband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0022067719_p38209777112133"><a name="en-us_topic_0022067719_p38209777112133"></a><a name="en-us_topic_0022067719_p38209777112133"></a>This metric is used to show the number of outgoing bytes sent by the monitored object per second (byte/s).</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0022067719_p49143110112133"><a name="en-us_topic_0022067719_p49143110112133"></a><a name="en-us_topic_0022067719_p49143110112133"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0022067719_p21168949112133"><a name="en-us_topic_0022067719_p21168949112133"></a><a name="en-us_topic_0022067719_p21168949112133"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="en-us_topic_0022067719_row40758280115945"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0022067719_p31280203115945"><a name="en-us_topic_0022067719_p31280203115945"></a><a name="en-us_topic_0022067719_p31280203115945"></a>network_incoming_bytes_aggregate_rate</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0022067719_p50668540115945"><a name="en-us_topic_0022067719_p50668540115945"></a><a name="en-us_topic_0022067719_p50668540115945"></a>Outband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0022067719_p10511114115945"><a name="en-us_topic_0022067719_p10511114115945"></a><a name="en-us_topic_0022067719_p10511114115945"></a>This metric is used to show the number of incoming bytes received by the monitored object per second (byte/s) at the virtualization layer.</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0022067719_p46093916115945"><a name="en-us_topic_0022067719_p46093916115945"></a><a name="en-us_topic_0022067719_p46093916115945"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0022067719_p42619739115945"><a name="en-us_topic_0022067719_p42619739115945"></a><a name="en-us_topic_0022067719_p42619739115945"></a>Monitored object: ECS</p>
<div class="note" id="en-us_topic_0022067719_note79003289217"><a name="en-us_topic_0022067719_note79003289217"></a><a name="en-us_topic_0022067719_note79003289217"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0022067719_p39940969217"><a name="en-us_topic_0022067719_p39940969217"></a><a name="en-us_topic_0022067719_p39940969217"></a>This metric is unavailable if SR-IOV is enabled.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0022067719_row55227643115945"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0022067719_p27286742115945"><a name="en-us_topic_0022067719_p27286742115945"></a><a name="en-us_topic_0022067719_p27286742115945"></a>network_outgoing_bytes_ aggregate_rate</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0022067719_p62742485115945"><a name="en-us_topic_0022067719_p62742485115945"></a><a name="en-us_topic_0022067719_p62742485115945"></a>Outband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0022067719_p48976549115945"><a name="en-us_topic_0022067719_p48976549115945"></a><a name="en-us_topic_0022067719_p48976549115945"></a>This metric is used to show the number of outgoing bytes sent by the monitored object per second (byte/s) at the virtualization layer.</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0022067719_p7677550115945"><a name="en-us_topic_0022067719_p7677550115945"></a><a name="en-us_topic_0022067719_p7677550115945"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0022067719_p17901783115945"><a name="en-us_topic_0022067719_p17901783115945"></a><a name="en-us_topic_0022067719_p17901783115945"></a>Monitored object: ECS</p>
<div class="note" id="en-us_topic_0022067719_note3360037392113"><a name="en-us_topic_0022067719_note3360037392113"></a><a name="en-us_topic_0022067719_note3360037392113"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0022067719_p3396790292113"><a name="en-us_topic_0022067719_p3396790292113"></a><a name="en-us_topic_0022067719_p3396790292113"></a>This metric is unavailable if SR-IOV is enabled.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0022067719_row6070168616270"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0022067719_p944426716270"><a name="en-us_topic_0022067719_p944426716270"></a><a name="en-us_topic_0022067719_p944426716270"></a>inst_sys_status_error</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0022067719_p2678816316270"><a name="en-us_topic_0022067719_p2678816316270"></a><a name="en-us_topic_0022067719_p2678816316270"></a>System Status Check Failed</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0022067719_p2235760816270"><a name="en-us_topic_0022067719_p2235760816270"></a><a name="en-us_topic_0022067719_p2235760816270"></a>This metric is used to monitor the cloud platform on which ECSs run.</p>
<p id="en-us_topic_0022067719_p31381019115520"><a name="en-us_topic_0022067719_p31381019115520"></a><a name="en-us_topic_0022067719_p31381019115520"></a>The system periodically checks the system status and returns check results using value <strong id="en-us_topic_0022067719_b842352706192323"><a name="en-us_topic_0022067719_b842352706192323"></a><a name="en-us_topic_0022067719_b842352706192323"></a>0</strong> or <strong id="en-us_topic_0022067719_b842352706192327"><a name="en-us_topic_0022067719_b842352706192327"></a><a name="en-us_topic_0022067719_b842352706192327"></a>1</strong>.</p>
<a name="en-us_topic_0022067719_ul13993718115520"></a><a name="en-us_topic_0022067719_ul13993718115520"></a><ul id="en-us_topic_0022067719_ul13993718115520"><li><strong id="en-us_topic_0022067719_b171676334619247"><a name="en-us_topic_0022067719_b171676334619247"></a><a name="en-us_topic_0022067719_b171676334619247"></a>0</strong>: The system is running properly. All check items are normal.</li><li><strong id="en-us_topic_0022067719_b1087511831192613"><a name="en-us_topic_0022067719_b1087511831192613"></a><a name="en-us_topic_0022067719_b1087511831192613"></a>1</strong>: The system is not running properly. One or more check items are abnormal.<p id="en-us_topic_0022067719_p2678038715835"><a name="en-us_topic_0022067719_p2678038715835"></a><a name="en-us_topic_0022067719_p2678038715835"></a>When the power source of the physical host fails or the hardware/software becomes faulty, the check result is <strong id="en-us_topic_0022067719_b842352706201616"><a name="en-us_topic_0022067719_b842352706201616"></a><a name="en-us_topic_0022067719_b842352706201616"></a>1</strong>.</p>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0022067719_p6613580916270"><a name="en-us_topic_0022067719_p6613580916270"></a><a name="en-us_topic_0022067719_p6613580916270"></a>0 or 1</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0022067719_p5540031116270"><a name="en-us_topic_0022067719_p5540031116270"></a><a name="en-us_topic_0022067719_p5540031116270"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="en-us_topic_0022067719_row22568644142859"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0022067719_p1791210142859"><a name="en-us_topic_0022067719_p1791210142859"></a><a name="en-us_topic_0022067719_p1791210142859"></a>ib_card_state</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="en-us_topic_0022067719_p10870298142859"><a name="en-us_topic_0022067719_p10870298142859"></a><a name="en-us_topic_0022067719_p10870298142859"></a>InfiniBand NIC status</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0022067719_p8078955142859"><a name="en-us_topic_0022067719_p8078955142859"></a><a name="en-us_topic_0022067719_p8078955142859"></a>This metric is used to monitor the status of an InfiniBand NIC on a high-performance h2 ECS to ensure proper InfiniBand NIC running.</p>
<p id="en-us_topic_0022067719_p1325610141717"><a name="en-us_topic_0022067719_p1325610141717"></a><a name="en-us_topic_0022067719_p1325610141717"></a>The system periodically checks the NIC status and returns check results using value <strong id="en-us_topic_0022067719_b2096629246"><a name="en-us_topic_0022067719_b2096629246"></a><a name="en-us_topic_0022067719_b2096629246"></a>0</strong> or <strong id="en-us_topic_0022067719_b1443560621"><a name="en-us_topic_0022067719_b1443560621"></a><a name="en-us_topic_0022067719_b1443560621"></a>1</strong>.</p>
<a name="en-us_topic_0022067719_ul28823487141959"></a><a name="en-us_topic_0022067719_ul28823487141959"></a><ul id="en-us_topic_0022067719_ul28823487141959"><li><strong id="en-us_topic_0022067719_b1101849494"><a name="en-us_topic_0022067719_b1101849494"></a><a name="en-us_topic_0022067719_b1101849494"></a>0</strong>: The system is running properly. That is, the InfiniBand NIC is functional.</li><li><strong id="en-us_topic_0022067719_b133791155"><a name="en-us_topic_0022067719_b133791155"></a><a name="en-us_topic_0022067719_b133791155"></a>1</strong>: The system is not running properly. That is, the InfiniBand NIC malfunctions.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0022067719_p50415620142859"><a name="en-us_topic_0022067719_p50415620142859"></a><a name="en-us_topic_0022067719_p50415620142859"></a>0 or 1</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0022067719_p57133454142859"><a name="en-us_topic_0022067719_p57133454142859"></a><a name="en-us_topic_0022067719_p57133454142859"></a>Monitored object: ECS</p>
<div class="note" id="en-us_topic_0022067719_note14324438161653"><a name="en-us_topic_0022067719_note14324438161653"></a><a name="en-us_topic_0022067719_note14324438161653"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0022067719_p61811084161653"><a name="en-us_topic_0022067719_p61811084161653"></a><a name="en-us_topic_0022067719_p61811084161653"></a>Only Mellanox EDR 100 GB single-port InfiniBand NICs are supported.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>The image based on which the target ECS is created must have OTC Tools installed. Otherwise, the  **Memory Usage**  and  **Disk Usage**  metrics are unavailable. For details about how to install the OTC Tools, visit  [https://github.com/UVP-Tools/UVP-Tools/](https://github.com/UVP-Tools/UVP-Tools/).  

## Dimension<a name="en-us_topic_0022067719_section36963297112133"></a>

<a name="en-us_topic_0022067719_table41237041112133"></a>
<table><thead align="left"><tr id="en-us_topic_0022067719_row28021974112133"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0022067719_p55187441112133"><a name="en-us_topic_0022067719_p55187441112133"></a><a name="en-us_topic_0022067719_p55187441112133"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0022067719_p40997749112133"><a name="en-us_topic_0022067719_p40997749112133"></a><a name="en-us_topic_0022067719_p40997749112133"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0022067719_row32483336112133"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0022067719_p13904597112133"><a name="en-us_topic_0022067719_p13904597112133"></a><a name="en-us_topic_0022067719_p13904597112133"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0022067719_p52530562112133"><a name="en-us_topic_0022067719_p52530562112133"></a><a name="en-us_topic_0022067719_p52530562112133"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

