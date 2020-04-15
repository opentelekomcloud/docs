# ECS Metrics<a name="EN-US_TOPIC_0022067719"></a>

## Function<a name="section25901060112133"></a>

This section describes monitoring metrics reported by ECS to Cloud Eye as well as their namespaces and dimensions. You can use APIs provided by Cloud Eye to view the monitoring metrics of the monitored object and alarms generated for ECS.

## Namespace<a name="section24282572112133"></a>

SYS.ECS

## Metrics<a name="section52364133112133"></a>

<a name="table13636366112133"></a>
<table><thead align="left"><tr id="row32163296112133"><th class="cellrowborder" valign="top" width="15.150000000000002%" id="mcps1.1.6.1.1"><p id="p55090151112133"><a name="p55090151112133"></a><a name="p55090151112133"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="16.020000000000003%" id="mcps1.1.6.1.2"><p id="p33117267112133"><a name="p33117267112133"></a><a name="p33117267112133"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25.420000000000005%" id="mcps1.1.6.1.3"><p id="p65253004112133"><a name="p65253004112133"></a><a name="p65253004112133"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="18.980000000000004%" id="mcps1.1.6.1.4"><p id="p51001977112133"><a name="p51001977112133"></a><a name="p51001977112133"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="24.430000000000003%" id="mcps1.1.6.1.5"><p id="p37519491112133"><a name="p37519491112133"></a><a name="p37519491112133"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row19179921112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="p10069772112133"><a name="p10069772112133"></a><a name="p10069772112133"></a>cpu_util</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="p10345179112133"><a name="p10345179112133"></a><a name="p10345179112133"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="p32653159112133"><a name="p32653159112133"></a><a name="p32653159112133"></a>This metric is used to show CPU usages (%) of monitored objects.</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="p31614322112133"><a name="p31614322112133"></a><a name="p31614322112133"></a>0% to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="p10623276112133"><a name="p10623276112133"></a><a name="p10623276112133"></a>Monitored object: ECS</p>
<div class="note" id="note609891291230"><a name="note609891291230"></a><a name="note609891291230"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p120312521230"><a name="p120312521230"></a><a name="p120312521230"></a>The metrics collected using OTC tools are accurate.</p>
</div></div>
</td>
</tr>
<tr id="row55179047112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="p40317835112133"><a name="p40317835112133"></a><a name="p40317835112133"></a>mem_util</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="p44519166112133"><a name="p44519166112133"></a><a name="p44519166112133"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="p49282731112133"><a name="p49282731112133"></a><a name="p49282731112133"></a>This metric is used to show memory usages (%) of monitored objects.</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="p13493709112133"><a name="p13493709112133"></a><a name="p13493709112133"></a>0% to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="p19248659112133"><a name="p19248659112133"></a><a name="p19248659112133"></a>Monitored object: ECS</p>
<div class="note" id="note1851305616219"><a name="note1851305616219"></a><a name="note1851305616219"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p3239978216219"><a name="p3239978216219"></a><a name="p3239978216219"></a>This metric is unavailable if the image has no OTC Tools installed.</p>
</div></div>
</td>
</tr>
<tr id="row15637553112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="p58682320112133"><a name="p58682320112133"></a><a name="p58682320112133"></a>disk_util_inband</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="p55647512112133"><a name="p55647512112133"></a><a name="p55647512112133"></a>Disks Usage</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="p11154608112133"><a name="p11154608112133"></a><a name="p11154608112133"></a>This metric is used to show disk usages (%) of monitored objects.</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="p11536837112133"><a name="p11536837112133"></a><a name="p11536837112133"></a>0% to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="p62068605112133"><a name="p62068605112133"></a><a name="p62068605112133"></a>Monitored object: ECS</p>
<div class="note" id="note1022149416225"><a name="note1022149416225"></a><a name="note1022149416225"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p2488458916225"><a name="p2488458916225"></a><a name="p2488458916225"></a>This metric is unavailable if the image has no OTC Tools installed.</p>
</div></div>
</td>
</tr>
<tr id="row61501122112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="p15534971112133"><a name="p15534971112133"></a><a name="p15534971112133"></a>disk_read_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="p292712452495"><a name="p292712452495"></a><a name="p292712452495"></a>Disk Read Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="p53692267112133"><a name="p53692267112133"></a><a name="p53692267112133"></a>This metric is used to show the number of bytes read from the monitored object per second (byte/s).</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="p20538509112133"><a name="p20538509112133"></a><a name="p20538509112133"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="p53006500112133"><a name="p53006500112133"></a><a name="p53006500112133"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="row65668128112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="p17518185112133"><a name="p17518185112133"></a><a name="p17518185112133"></a>disk_write_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="p18939164514497"><a name="p18939164514497"></a><a name="p18939164514497"></a>Disk Write Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="p46440320112133"><a name="p46440320112133"></a><a name="p46440320112133"></a>This metric is used to show the number of bytes written to the monitored object per second (byte/s).</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="p66041352112133"><a name="p66041352112133"></a><a name="p66041352112133"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="p47749284112133"><a name="p47749284112133"></a><a name="p47749284112133"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="row42486756112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="p18875184112133"><a name="p18875184112133"></a><a name="p18875184112133"></a>disk_read_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="p59508458491"><a name="p59508458491"></a><a name="p59508458491"></a>Disk Read IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="p2615947105641"><a name="p2615947105641"></a><a name="p2615947105641"></a>This metric is used to show the number of read requests sent to the monitored object per second (requests/second).</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="p8134307112133"><a name="p8134307112133"></a><a name="p8134307112133"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="p54899139112133"><a name="p54899139112133"></a><a name="p54899139112133"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="row17645255112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="p19979544112133"><a name="p19979544112133"></a><a name="p19979544112133"></a>disk_write_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="p11969114513496"><a name="p11969114513496"></a><a name="p11969114513496"></a>Disk Write IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="p22177214112133"><a name="p22177214112133"></a><a name="p22177214112133"></a>This metric is used to show the number of write requests sent to the monitored object per second (requests/second).</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="p21229150112133"><a name="p21229150112133"></a><a name="p21229150112133"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="p41839618112133"><a name="p41839618112133"></a><a name="p41839618112133"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="row33565898112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="p34483231112133"><a name="p34483231112133"></a><a name="p34483231112133"></a>network_incoming_bytes_rate_inband</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="p41678312112133"><a name="p41678312112133"></a><a name="p41678312112133"></a>Inband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="p20500110112133"><a name="p20500110112133"></a><a name="p20500110112133"></a>This metric is used to show the number of incoming bytes received by the monitored object per second (byte/s).</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="p1314054112133"><a name="p1314054112133"></a><a name="p1314054112133"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="p39329546112133"><a name="p39329546112133"></a><a name="p39329546112133"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="row31576687112133"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="p7574877112133"><a name="p7574877112133"></a><a name="p7574877112133"></a>network_outgoing_bytes_rate_inband</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="p9585275112133"><a name="p9585275112133"></a><a name="p9585275112133"></a>Inband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="p38209777112133"><a name="p38209777112133"></a><a name="p38209777112133"></a>This metric is used to show the number of outgoing bytes sent by the monitored object per second (byte/s).</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="p49143110112133"><a name="p49143110112133"></a><a name="p49143110112133"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="p21168949112133"><a name="p21168949112133"></a><a name="p21168949112133"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="row40758280115945"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="p31280203115945"><a name="p31280203115945"></a><a name="p31280203115945"></a>network_incoming_bytes_aggregate_rate</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="p50668540115945"><a name="p50668540115945"></a><a name="p50668540115945"></a>Outband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="p10511114115945"><a name="p10511114115945"></a><a name="p10511114115945"></a>This metric is used to show the number of incoming bytes received by the monitored object per second (byte/s) at the virtualization layer.</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="p46093916115945"><a name="p46093916115945"></a><a name="p46093916115945"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="p42619739115945"><a name="p42619739115945"></a><a name="p42619739115945"></a>Monitored object: ECS</p>
<div class="note" id="note79003289217"><a name="note79003289217"></a><a name="note79003289217"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p39940969217"><a name="p39940969217"></a><a name="p39940969217"></a>This metric is unavailable if SR-IOV is enabled.</p>
</div></div>
</td>
</tr>
<tr id="row55227643115945"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="p27286742115945"><a name="p27286742115945"></a><a name="p27286742115945"></a>network_outgoing_bytes_ aggregate_rate</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="p62742485115945"><a name="p62742485115945"></a><a name="p62742485115945"></a>Outband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="p48976549115945"><a name="p48976549115945"></a><a name="p48976549115945"></a>This metric is used to show the number of outgoing bytes sent by the monitored object per second (byte/s) at the virtualization layer.</p>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="p7677550115945"><a name="p7677550115945"></a><a name="p7677550115945"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="p17901783115945"><a name="p17901783115945"></a><a name="p17901783115945"></a>Monitored object: ECS</p>
<div class="note" id="note3360037392113"><a name="note3360037392113"></a><a name="note3360037392113"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p3396790292113"><a name="p3396790292113"></a><a name="p3396790292113"></a>This metric is unavailable if SR-IOV is enabled.</p>
</div></div>
</td>
</tr>
<tr id="row6070168616270"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="p944426716270"><a name="p944426716270"></a><a name="p944426716270"></a>inst_sys_status_error</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="p2678816316270"><a name="p2678816316270"></a><a name="p2678816316270"></a>System Status Check Failed</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="p2235760816270"><a name="p2235760816270"></a><a name="p2235760816270"></a>This metric is used to monitor the cloud platform on which ECSs run.</p>
<p id="p31381019115520"><a name="p31381019115520"></a><a name="p31381019115520"></a>The system periodically checks the system status and returns check results using value <strong id="b842352706192323"><a name="b842352706192323"></a><a name="b842352706192323"></a>0</strong> or <strong id="b842352706192327"><a name="b842352706192327"></a><a name="b842352706192327"></a>1</strong>.</p>
<a name="ul13993718115520"></a><a name="ul13993718115520"></a><ul id="ul13993718115520"><li><strong id="b171676334619247"><a name="b171676334619247"></a><a name="b171676334619247"></a>0</strong>: The system is running properly. All check items are normal.</li><li><strong id="b1087511831192613"><a name="b1087511831192613"></a><a name="b1087511831192613"></a>1</strong>: The system is not running properly. One or more check items are abnormal.<p id="p2678038715835"><a name="p2678038715835"></a><a name="p2678038715835"></a>When the power source of the physical host fails or the hardware/software becomes faulty, the check result is <strong id="b842352706201616"><a name="b842352706201616"></a><a name="b842352706201616"></a>1</strong>.</p>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="p6613580916270"><a name="p6613580916270"></a><a name="p6613580916270"></a>0 or 1</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="p5540031116270"><a name="p5540031116270"></a><a name="p5540031116270"></a>Monitored object: ECS</p>
</td>
</tr>
<tr id="row22568644142859"><td class="cellrowborder" valign="top" width="15.150000000000002%" headers="mcps1.1.6.1.1 "><p id="p1791210142859"><a name="p1791210142859"></a><a name="p1791210142859"></a>ib_card_state</p>
</td>
<td class="cellrowborder" valign="top" width="16.020000000000003%" headers="mcps1.1.6.1.2 "><p id="p10870298142859"><a name="p10870298142859"></a><a name="p10870298142859"></a>InfiniBand NIC status</p>
</td>
<td class="cellrowborder" valign="top" width="25.420000000000005%" headers="mcps1.1.6.1.3 "><p id="p8078955142859"><a name="p8078955142859"></a><a name="p8078955142859"></a>This metric is used to monitor the status of an InfiniBand NIC on a high-performance h2 ECS to ensure proper InfiniBand NIC running.</p>
<p id="p1325610141717"><a name="p1325610141717"></a><a name="p1325610141717"></a>The system periodically checks the NIC status and returns check results using value <strong id="b2096629246"><a name="b2096629246"></a><a name="b2096629246"></a>0</strong> or <strong id="b1443560621"><a name="b1443560621"></a><a name="b1443560621"></a>1</strong>.</p>
<a name="ul28823487141959"></a><a name="ul28823487141959"></a><ul id="ul28823487141959"><li><strong id="b1101849494"><a name="b1101849494"></a><a name="b1101849494"></a>0</strong>: The system is running properly. That is, the InfiniBand NIC is functional.</li><li><strong id="b133791155"><a name="b133791155"></a><a name="b133791155"></a>1</strong>: The system is not running properly. That is, the InfiniBand NIC malfunctions.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="18.980000000000004%" headers="mcps1.1.6.1.4 "><p id="p50415620142859"><a name="p50415620142859"></a><a name="p50415620142859"></a>0 or 1</p>
</td>
<td class="cellrowborder" valign="top" width="24.430000000000003%" headers="mcps1.1.6.1.5 "><p id="p57133454142859"><a name="p57133454142859"></a><a name="p57133454142859"></a>Monitored object: ECS</p>
<div class="note" id="note14324438161653"><a name="note14324438161653"></a><a name="note14324438161653"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p61811084161653"><a name="p61811084161653"></a><a name="p61811084161653"></a>Only Mellanox EDR 100 GB single-port InfiniBand NICs are supported.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The image based on which the target ECS is created must have OTC Tools installed. Otherwise, the  **Memory Usage**  and  **Disk Usage**  metrics are unavailable. For details about how to install the OTC Tools, visit  [https://github.com/UVP-Tools/UVP-Tools/](https://github.com/UVP-Tools/UVP-Tools/).  

## Dimension<a name="section36963297112133"></a>

<a name="table41237041112133"></a>
<table><thead align="left"><tr id="row28021974112133"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p55187441112133"><a name="p55187441112133"></a><a name="p55187441112133"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p40997749112133"><a name="p40997749112133"></a><a name="p40997749112133"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row32483336112133"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p13904597112133"><a name="p13904597112133"></a><a name="p13904597112133"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p52530562112133"><a name="p52530562112133"></a><a name="p52530562112133"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

