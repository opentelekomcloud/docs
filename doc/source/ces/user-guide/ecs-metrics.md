# ECS Metrics<a name="EN-US_TOPIC_0084572206"></a>

You do not need to install the Agent on an ECS to check basic monitoring metrics. The monitoring data is available in minutes after an ECS starts running.

Basic monitoring metric data is reported every 5 minutes.

ECS metrics vary depending on ECS OSs and types. For details, see  [Table 1](#table1037217573240). √ indicates that the metric is supported, and x indicates that the metric is not supported.

**Table  1**  Supported ECS metrics

<a name="table1037217573240"></a>
<table><thead align="left"><tr id="row17373205718243"><th class="cellrowborder" valign="top" id="mcps1.2.6.1.1"><p id="p9373135712419"><a name="p9373135712419"></a><a name="p9373135712419"></a>Metric</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.6.1.2"><p id="p93738573243"><a name="p93738573243"></a><a name="p93738573243"></a>Windows ECS</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.6.1.3"><p id="p93741157102418"><a name="p93741157102418"></a><a name="p93741157102418"></a>Linux ECS</p>
</th>
</tr>
</thead>
<tbody><tr id="row1377165742410"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p12378105772413"><a name="p12378105772413"></a><a name="p12378105772413"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p5621621911122"><a name="p5621621911122"></a><a name="p5621621911122"></a>XEN</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p19378657142411"><a name="p19378657142411"></a><a name="p19378657142411"></a>KVM</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p14878195116811"><a name="p14878195116811"></a><a name="p14878195116811"></a>XEN</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p1245823211122"><a name="p1245823211122"></a><a name="p1245823211122"></a>KVM</p>
</td>
</tr>
<tr id="row183781057122416"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p0378657142410"><a name="p0378657142410"></a><a name="p0378657142410"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p14378145714241"><a name="p14378145714241"></a><a name="p14378145714241"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p18378857192420"><a name="p18378857192420"></a><a name="p18378857192420"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p23791557172411"><a name="p23791557172411"></a><a name="p23791557172411"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p1537975718247"><a name="p1537975718247"></a><a name="p1537975718247"></a>√</p>
</td>
</tr>
<tr id="row1837911572249"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p537911578249"><a name="p537911578249"></a><a name="p537911578249"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p43791857192417"><a name="p43791857192417"></a><a name="p43791857192417"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p3379257192417"><a name="p3379257192417"></a><a name="p3379257192417"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p2379205792411"><a name="p2379205792411"></a><a name="p2379205792411"></a>√ (The OTC Tools must be installed on the image. Otherwise, this metric is unavailable.)</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p1637935722414"><a name="p1637935722414"></a><a name="p1637935722414"></a>x (Not supported)</p>
</td>
</tr>
<tr id="row838075712248"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p1538095762417"><a name="p1538095762417"></a><a name="p1538095762417"></a>Disk Usage</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p18380857122416"><a name="p18380857122416"></a><a name="p18380857122416"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p14380135713244"><a name="p14380135713244"></a><a name="p14380135713244"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p4380115742419"><a name="p4380115742419"></a><a name="p4380115742419"></a>√ (The OTC Tools must be installed on the image. Otherwise, this metric is unavailable.)</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p133841857182410"><a name="p133841857182410"></a><a name="p133841857182410"></a>x (Not supported)</p>
</td>
</tr>
<tr id="row73547541549"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p14452195555420"><a name="p14452195555420"></a><a name="p14452195555420"></a>Disk Read Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p34562558541"><a name="p34562558541"></a><a name="p34562558541"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p1946016558542"><a name="p1946016558542"></a><a name="p1946016558542"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p44651955115413"><a name="p44651955115413"></a><a name="p44651955115413"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p20468955115416"><a name="p20468955115416"></a><a name="p20468955115416"></a>√</p>
</td>
</tr>
<tr id="row139958595541"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p138222016555"><a name="p138222016555"></a><a name="p138222016555"></a>Disk Write Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p6826909559"><a name="p6826909559"></a><a name="p6826909559"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p1830120135513"><a name="p1830120135513"></a><a name="p1830120135513"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p19835808556"><a name="p19835808556"></a><a name="p19835808556"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p48382005554"><a name="p48382005554"></a><a name="p48382005554"></a>√</p>
</td>
</tr>
<tr id="row184731953557"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p1655576135515"><a name="p1655576135515"></a><a name="p1655576135515"></a>Disk Read IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p1055915635512"><a name="p1055915635512"></a><a name="p1055915635512"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p85636605520"><a name="p85636605520"></a><a name="p85636605520"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p1656586105519"><a name="p1656586105519"></a><a name="p1656586105519"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p1556911645511"><a name="p1556911645511"></a><a name="p1556911645511"></a>√</p>
</td>
</tr>
<tr id="row19682410145510"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p8644161210552"><a name="p8644161210552"></a><a name="p8644161210552"></a>Disk Write IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p1864813126550"><a name="p1864813126550"></a><a name="p1864813126550"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p06519125551"><a name="p06519125551"></a><a name="p06519125551"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p17658012195512"><a name="p17658012195512"></a><a name="p17658012195512"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p36611412105515"><a name="p36611412105515"></a><a name="p36611412105515"></a>√</p>
</td>
</tr>
<tr id="row20389105742419"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p3389357162420"><a name="p3389357162420"></a><a name="p3389357162420"></a>Inband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p10390157102414"><a name="p10390157102414"></a><a name="p10390157102414"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p1139065714241"><a name="p1139065714241"></a><a name="p1139065714241"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p539010576249"><a name="p539010576249"></a><a name="p539010576249"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p139017573245"><a name="p139017573245"></a><a name="p139017573245"></a>x (Not supported)</p>
</td>
</tr>
<tr id="row8391195716245"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p3391135715241"><a name="p3391135715241"></a><a name="p3391135715241"></a>Inband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p10391357142410"><a name="p10391357142410"></a><a name="p10391357142410"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p93911573244"><a name="p93911573244"></a><a name="p93911573244"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p939175732414"><a name="p939175732414"></a><a name="p939175732414"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p1239165742417"><a name="p1239165742417"></a><a name="p1239165742417"></a>x (Not supported)</p>
</td>
</tr>
<tr id="row1039265712416"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p83921857122418"><a name="p83921857122418"></a><a name="p83921857122418"></a>Outband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p113921757202419"><a name="p113921757202419"></a><a name="p113921757202419"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p1039218574242"><a name="p1039218574242"></a><a name="p1039218574242"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p153921157162412"><a name="p153921157162412"></a><a name="p153921157162412"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p03921257122413"><a name="p03921257122413"></a><a name="p03921257122413"></a>√</p>
</td>
</tr>
<tr id="row19393657182416"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p43931857192411"><a name="p43931857192411"></a><a name="p43931857192411"></a>Outband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p143931057102414"><a name="p143931057102414"></a><a name="p143931057102414"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p143930577246"><a name="p143930577246"></a><a name="p143930577246"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p53937574243"><a name="p53937574243"></a><a name="p53937574243"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p1339310577241"><a name="p1339310577241"></a><a name="p1339310577241"></a>√</p>
</td>
</tr>
<tr id="row13393105712413"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p33931257152419"><a name="p33931257152419"></a><a name="p33931257152419"></a>System Status Check Failed</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p19393125752411"><a name="p19393125752411"></a><a name="p19393125752411"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p163935576240"><a name="p163935576240"></a><a name="p163935576240"></a>×</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p739395715243"><a name="p739395715243"></a><a name="p739395715243"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p183941857162415"><a name="p183941857162415"></a><a name="p183941857162415"></a>×</p>
</td>
</tr>
<tr id="row173943575246"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.6.1.1 "><p id="p14394757132415"><a name="p14394757132415"></a><a name="p14394757132415"></a>InfiniBand NIC status</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.2 "><p id="p16395657162413"><a name="p16395657162413"></a><a name="p16395657162413"></a>×</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.2 "><p id="p43950572244"><a name="p43950572244"></a><a name="p43950572244"></a>√ (only for H2 ECSs)</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p43951257152414"><a name="p43951257152414"></a><a name="p43951257152414"></a>×</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.6.1.3 "><p id="p0395457152414"><a name="p0395457152414"></a><a name="p0395457152414"></a>√ (only for H2 ECSs)</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>For  **Memory Usage**  and  **Disk Usage**, the OTC Tools must be installed for the images used by ECSs. Otherwise, the metrics cannot be obtained. For details about how to install the OTC Tools, visit  [https://github.com/UVP-Tools/UVP-Tools/](https://github.com/UVP-Tools/UVP-Tools/).  

[Table 2](#table2442018718425)  describes these ECS metrics.

**Table  2**  Metric description

<a name="table2442018718425"></a>
<table><thead align="left"><tr id="en-us_topic_0030911465_row15175257222846"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.7.1.1"><p id="en-us_topic_0030911465_p55090151112133"><a name="en-us_topic_0030911465_p55090151112133"></a><a name="en-us_topic_0030911465_p55090151112133"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.7.1.2"><p id="en-us_topic_0030911465_p21236279222846"><a name="en-us_topic_0030911465_p21236279222846"></a><a name="en-us_topic_0030911465_p21236279222846"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.7.1.3"><p id="en-us_topic_0030911465_p42417005222846"><a name="en-us_topic_0030911465_p42417005222846"></a><a name="en-us_topic_0030911465_p42417005222846"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.7.1.4"><p id="en-us_topic_0030911465_p64622851222846"><a name="en-us_topic_0030911465_p64622851222846"></a><a name="en-us_topic_0030911465_p64622851222846"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.7.1.5"><p id="en-us_topic_0030911465_p67068467222846"><a name="en-us_topic_0030911465_p67068467222846"></a><a name="en-us_topic_0030911465_p67068467222846"></a>Monitored Object</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.7.1.6"><p id="en-us_topic_0030911465_p92927044715"><a name="en-us_topic_0030911465_p92927044715"></a><a name="en-us_topic_0030911465_p92927044715"></a>Monitoring Interval (Raw Metrics and KVM Only)</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0030911465_row63836764222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0030911465_p10069772112133"><a name="en-us_topic_0030911465_p10069772112133"></a><a name="en-us_topic_0030911465_p10069772112133"></a>cpu_util</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0030911465_p3395365222846"><a name="en-us_topic_0030911465_p3395365222846"></a><a name="en-us_topic_0030911465_p3395365222846"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0030911465_p6589110222846"><a name="en-us_topic_0030911465_p6589110222846"></a><a name="en-us_topic_0030911465_p6589110222846"></a>CPU usage of an ECS</p>
<p id="en-us_topic_0030911465_p370229193114"><a name="en-us_topic_0030911465_p370229193114"></a><a name="en-us_topic_0030911465_p370229193114"></a>Unit: Percent</p>
<p id="en-us_topic_0030911465_p11196181114376"><a name="en-us_topic_0030911465_p11196181114376"></a><a name="en-us_topic_0030911465_p11196181114376"></a>Formula: CPU usage of an ECS/Number of vCPUs in the ECS</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0030911465_p13045074222846"><a name="en-us_topic_0030911465_p13045074222846"></a><a name="en-us_topic_0030911465_p13045074222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0030911465_p18876142014717"><a name="en-us_topic_0030911465_p18876142014717"></a><a name="en-us_topic_0030911465_p18876142014717"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0030911465_p162937034720"><a name="en-us_topic_0030911465_p162937034720"></a><a name="en-us_topic_0030911465_p162937034720"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0030911465_row47509658222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0030911465_p124210503017"><a name="en-us_topic_0030911465_p124210503017"></a><a name="en-us_topic_0030911465_p124210503017"></a>mem_util</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0030911465_p23077113222846"><a name="en-us_topic_0030911465_p23077113222846"></a><a name="en-us_topic_0030911465_p23077113222846"></a>Memory Usage</p>
<p id="en-us_topic_0030911465_p6367428222846"><a name="en-us_topic_0030911465_p6367428222846"></a><a name="en-us_topic_0030911465_p6367428222846"></a></p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0030911465_p88761115174313"><a name="en-us_topic_0030911465_p88761115174313"></a><a name="en-us_topic_0030911465_p88761115174313"></a>Memory usage of an ECS</p>
<p id="en-us_topic_0030911465_p9514173893717"><a name="en-us_topic_0030911465_p9514173893717"></a><a name="en-us_topic_0030911465_p9514173893717"></a>This metric is unavailable if the image has no OTC Tools installed.</p>
<p id="en-us_topic_0030911465_p740255511317"><a name="en-us_topic_0030911465_p740255511317"></a><a name="en-us_topic_0030911465_p740255511317"></a>Unit: Percent</p>
<p id="en-us_topic_0030911465_p45999697222846"><a name="en-us_topic_0030911465_p45999697222846"></a><a name="en-us_topic_0030911465_p45999697222846"></a>Formula: Used memory of an ECS/Total memory of the ECS</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0030911465_p15452979222846"><a name="en-us_topic_0030911465_p15452979222846"></a><a name="en-us_topic_0030911465_p15452979222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0030911465_p43731801222846"><a name="en-us_topic_0030911465_p43731801222846"></a><a name="en-us_topic_0030911465_p43731801222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0030911465_p1529314019473"><a name="en-us_topic_0030911465_p1529314019473"></a><a name="en-us_topic_0030911465_p1529314019473"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0030911465_row58041894222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0030911465_p1924275153012"><a name="en-us_topic_0030911465_p1924275153012"></a><a name="en-us_topic_0030911465_p1924275153012"></a>disk_util_inband</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0030911465_p3772951222846"><a name="en-us_topic_0030911465_p3772951222846"></a><a name="en-us_topic_0030911465_p3772951222846"></a>Disk Usage</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0030911465_p661521494312"><a name="en-us_topic_0030911465_p661521494312"></a><a name="en-us_topic_0030911465_p661521494312"></a>Disk usage of an ECS</p>
<p id="en-us_topic_0030911465_p37173646222846"><a name="en-us_topic_0030911465_p37173646222846"></a><a name="en-us_topic_0030911465_p37173646222846"></a>This metric is unavailable if the image has no OTC Tools installed.</p>
<p id="en-us_topic_0030911465_p499211413328"><a name="en-us_topic_0030911465_p499211413328"></a><a name="en-us_topic_0030911465_p499211413328"></a>Unit: Percent</p>
<p id="en-us_topic_0030911465_p16310184093713"><a name="en-us_topic_0030911465_p16310184093713"></a><a name="en-us_topic_0030911465_p16310184093713"></a>Formula: Used capacity of an ECS disk/Total capacity of the ECS disk</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0030911465_p22679847222846"><a name="en-us_topic_0030911465_p22679847222846"></a><a name="en-us_topic_0030911465_p22679847222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0030911465_p25128347222846"><a name="en-us_topic_0030911465_p25128347222846"></a><a name="en-us_topic_0030911465_p25128347222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0030911465_p72931703474"><a name="en-us_topic_0030911465_p72931703474"></a><a name="en-us_topic_0030911465_p72931703474"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0030911465_row24828535222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0030911465_p15534971112133"><a name="en-us_topic_0030911465_p15534971112133"></a><a name="en-us_topic_0030911465_p15534971112133"></a>disk_read_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0030911465_p292712452495"><a name="en-us_topic_0030911465_p292712452495"></a><a name="en-us_topic_0030911465_p292712452495"></a>Disk Read Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0030911465_p26808602222846"><a name="en-us_topic_0030911465_p26808602222846"></a><a name="en-us_topic_0030911465_p26808602222846"></a>Number of bytes read from an ECS disk per second</p>
<p id="en-us_topic_0030911465_p1428281363215"><a name="en-us_topic_0030911465_p1428281363215"></a><a name="en-us_topic_0030911465_p1428281363215"></a>Unit: byte/s</p>
<p id="en-us_topic_0030911465_p139664438371"><a name="en-us_topic_0030911465_p139664438371"></a><a name="en-us_topic_0030911465_p139664438371"></a>Formula: Total number of bytes read from an ECS disk/Monitoring interval</p>
<p id="en-us_topic_0030911465_p13259851114311"><a name="en-us_topic_0030911465_p13259851114311"></a><a name="en-us_topic_0030911465_p13259851114311"></a>byte_out = (rd_bytes - last_rd_bytes)/Time difference</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0030911465_p66019488222846"><a name="en-us_topic_0030911465_p66019488222846"></a><a name="en-us_topic_0030911465_p66019488222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0030911465_p45978283222846"><a name="en-us_topic_0030911465_p45978283222846"></a><a name="en-us_topic_0030911465_p45978283222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0030911465_p1929370154718"><a name="en-us_topic_0030911465_p1929370154718"></a><a name="en-us_topic_0030911465_p1929370154718"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0030911465_row11151367222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0030911465_p17518185112133"><a name="en-us_topic_0030911465_p17518185112133"></a><a name="en-us_topic_0030911465_p17518185112133"></a>disk_write_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0030911465_p18939164514497"><a name="en-us_topic_0030911465_p18939164514497"></a><a name="en-us_topic_0030911465_p18939164514497"></a>Disk Write Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0030911465_p15463290222846"><a name="en-us_topic_0030911465_p15463290222846"></a><a name="en-us_topic_0030911465_p15463290222846"></a>Number of bytes written to an ECS disk per second</p>
<p id="en-us_topic_0030911465_p67319380323"><a name="en-us_topic_0030911465_p67319380323"></a><a name="en-us_topic_0030911465_p67319380323"></a>Unit: byte/s</p>
<p id="en-us_topic_0030911465_p13629649103720"><a name="en-us_topic_0030911465_p13629649103720"></a><a name="en-us_topic_0030911465_p13629649103720"></a>Formula: Total number of bytes written to an ECS disk/Monitoring interval</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0030911465_p53157119222846"><a name="en-us_topic_0030911465_p53157119222846"></a><a name="en-us_topic_0030911465_p53157119222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0030911465_p10759388222846"><a name="en-us_topic_0030911465_p10759388222846"></a><a name="en-us_topic_0030911465_p10759388222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0030911465_p3293130104711"><a name="en-us_topic_0030911465_p3293130104711"></a><a name="en-us_topic_0030911465_p3293130104711"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0030911465_row29725634222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0030911465_p18875184112133"><a name="en-us_topic_0030911465_p18875184112133"></a><a name="en-us_topic_0030911465_p18875184112133"></a>disk_read_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0030911465_p59508458491"><a name="en-us_topic_0030911465_p59508458491"></a><a name="en-us_topic_0030911465_p59508458491"></a>Disk Read IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0030911465_p11529080222846"><a name="en-us_topic_0030911465_p11529080222846"></a><a name="en-us_topic_0030911465_p11529080222846"></a>Number of read requests sent to an ECS disk per second</p>
<p id="en-us_topic_0030911465_p04261505333"><a name="en-us_topic_0030911465_p04261505333"></a><a name="en-us_topic_0030911465_p04261505333"></a>Unit: request/s</p>
<p id="en-us_topic_0030911465_p15021352143711"><a name="en-us_topic_0030911465_p15021352143711"></a><a name="en-us_topic_0030911465_p15021352143711"></a>Formula: Total number of read requests sent to an ECS disk/Monitoring interval</p>
<p id="en-us_topic_0030911465_p19923180174416"><a name="en-us_topic_0030911465_p19923180174416"></a><a name="en-us_topic_0030911465_p19923180174416"></a>req_out = (rd_req - last_rd_req)/Time difference</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0030911465_p10609393222846"><a name="en-us_topic_0030911465_p10609393222846"></a><a name="en-us_topic_0030911465_p10609393222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0030911465_p54054474222846"><a name="en-us_topic_0030911465_p54054474222846"></a><a name="en-us_topic_0030911465_p54054474222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0030911465_p32931706476"><a name="en-us_topic_0030911465_p32931706476"></a><a name="en-us_topic_0030911465_p32931706476"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0030911465_row16728218222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0030911465_p19979544112133"><a name="en-us_topic_0030911465_p19979544112133"></a><a name="en-us_topic_0030911465_p19979544112133"></a>disk_write_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0030911465_p11969114513496"><a name="en-us_topic_0030911465_p11969114513496"></a><a name="en-us_topic_0030911465_p11969114513496"></a>Disk Write IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0030911465_p30846695222846"><a name="en-us_topic_0030911465_p30846695222846"></a><a name="en-us_topic_0030911465_p30846695222846"></a>Number of write requests sent to an ECS disk per second</p>
<p id="en-us_topic_0030911465_p116931923173320"><a name="en-us_topic_0030911465_p116931923173320"></a><a name="en-us_topic_0030911465_p116931923173320"></a>Unit: request/s</p>
<p id="en-us_topic_0030911465_p21821655103712"><a name="en-us_topic_0030911465_p21821655103712"></a><a name="en-us_topic_0030911465_p21821655103712"></a>Formula: Total number of write requests sent to an ECS disk/Monitoring interval</p>
<p id="en-us_topic_0030911465_p1357557164413"><a name="en-us_topic_0030911465_p1357557164413"></a><a name="en-us_topic_0030911465_p1357557164413"></a>req_in = (wr_req - last_wr_req)/Time difference</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0030911465_p51947303222846"><a name="en-us_topic_0030911465_p51947303222846"></a><a name="en-us_topic_0030911465_p51947303222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0030911465_p46982038222846"><a name="en-us_topic_0030911465_p46982038222846"></a><a name="en-us_topic_0030911465_p46982038222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0030911465_p18293105476"><a name="en-us_topic_0030911465_p18293105476"></a><a name="en-us_topic_0030911465_p18293105476"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0030911465_row20185161222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0030911465_p34483231112133"><a name="en-us_topic_0030911465_p34483231112133"></a><a name="en-us_topic_0030911465_p34483231112133"></a>network_incoming_bytes_rate_inband</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0030911465_p24385382222846"><a name="en-us_topic_0030911465_p24385382222846"></a><a name="en-us_topic_0030911465_p24385382222846"></a>Inband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0030911465_p29058915222846"><a name="en-us_topic_0030911465_p29058915222846"></a><a name="en-us_topic_0030911465_p29058915222846"></a>Number of incoming bytes on an ECS per second</p>
<p id="en-us_topic_0030911465_p14765153917334"><a name="en-us_topic_0030911465_p14765153917334"></a><a name="en-us_topic_0030911465_p14765153917334"></a>Unit: byte/s</p>
<p id="en-us_topic_0030911465_p6126135893715"><a name="en-us_topic_0030911465_p6126135893715"></a><a name="en-us_topic_0030911465_p6126135893715"></a>Formula: Total number of inband incoming bytes on an ECS/Monitoring interval</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0030911465_p66369310222846"><a name="en-us_topic_0030911465_p66369310222846"></a><a name="en-us_topic_0030911465_p66369310222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0030911465_p7205036222846"><a name="en-us_topic_0030911465_p7205036222846"></a><a name="en-us_topic_0030911465_p7205036222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0030911465_p82931008478"><a name="en-us_topic_0030911465_p82931008478"></a><a name="en-us_topic_0030911465_p82931008478"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0030911465_row64845332222846"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0030911465_p7574877112133"><a name="en-us_topic_0030911465_p7574877112133"></a><a name="en-us_topic_0030911465_p7574877112133"></a>network_outgoing_bytes_rate_inband</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0030911465_p17980571222846"><a name="en-us_topic_0030911465_p17980571222846"></a><a name="en-us_topic_0030911465_p17980571222846"></a>Inband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0030911465_p47140109222846"><a name="en-us_topic_0030911465_p47140109222846"></a><a name="en-us_topic_0030911465_p47140109222846"></a>Number of outgoing bytes on an ECS per second</p>
<p id="en-us_topic_0030911465_p372019126349"><a name="en-us_topic_0030911465_p372019126349"></a><a name="en-us_topic_0030911465_p372019126349"></a>Unit: byte/s</p>
<p id="en-us_topic_0030911465_p2336161163817"><a name="en-us_topic_0030911465_p2336161163817"></a><a name="en-us_topic_0030911465_p2336161163817"></a>Formula: Total number of inband outgoing bytes on an ECS/Monitoring interval</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0030911465_p48614360222846"><a name="en-us_topic_0030911465_p48614360222846"></a><a name="en-us_topic_0030911465_p48614360222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0030911465_p45449088222846"><a name="en-us_topic_0030911465_p45449088222846"></a><a name="en-us_topic_0030911465_p45449088222846"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0030911465_p1429311044718"><a name="en-us_topic_0030911465_p1429311044718"></a><a name="en-us_topic_0030911465_p1429311044718"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0030911465_row22492419121215"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0030911465_p31280203115945"><a name="en-us_topic_0030911465_p31280203115945"></a><a name="en-us_topic_0030911465_p31280203115945"></a>network_incoming_bytes_aggregate_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0030911465_p1105187121215"><a name="en-us_topic_0030911465_p1105187121215"></a><a name="en-us_topic_0030911465_p1105187121215"></a>Outband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0030911465_p22411285121215"><a name="en-us_topic_0030911465_p22411285121215"></a><a name="en-us_topic_0030911465_p22411285121215"></a>Number of incoming bytes on an ECS per second on the hypervisor</p>
<p id="en-us_topic_0030911465_p727510295345"><a name="en-us_topic_0030911465_p727510295345"></a><a name="en-us_topic_0030911465_p727510295345"></a>Unit: byte/s</p>
<p id="en-us_topic_0030911465_p157791355389"><a name="en-us_topic_0030911465_p157791355389"></a><a name="en-us_topic_0030911465_p157791355389"></a>Formula: Total number of outband incoming bytes on an ECS/Monitoring interval</p>
<p id="en-us_topic_0030911465_p542192819444"><a name="en-us_topic_0030911465_p542192819444"></a><a name="en-us_topic_0030911465_p542192819444"></a>This metric is unavailable if SR-IOV is enabled.</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0030911465_p4924384121215"><a name="en-us_topic_0030911465_p4924384121215"></a><a name="en-us_topic_0030911465_p4924384121215"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0030911465_p63330824121215"><a name="en-us_topic_0030911465_p63330824121215"></a><a name="en-us_topic_0030911465_p63330824121215"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0030911465_p132931016476"><a name="en-us_topic_0030911465_p132931016476"></a><a name="en-us_topic_0030911465_p132931016476"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0030911465_row62680097121215"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0030911465_p27286742115945"><a name="en-us_topic_0030911465_p27286742115945"></a><a name="en-us_topic_0030911465_p27286742115945"></a>network_outgoing_bytes_ aggregate_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0030911465_p27249966121215"><a name="en-us_topic_0030911465_p27249966121215"></a><a name="en-us_topic_0030911465_p27249966121215"></a>Outband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0030911465_p59763627121215"><a name="en-us_topic_0030911465_p59763627121215"></a><a name="en-us_topic_0030911465_p59763627121215"></a>Number of outgoing bytes on an ECS per second on the hypervisor</p>
<p id="en-us_topic_0030911465_p10272498343"><a name="en-us_topic_0030911465_p10272498343"></a><a name="en-us_topic_0030911465_p10272498343"></a>Unit: byte/s</p>
<p id="en-us_topic_0030911465_p1112031083818"><a name="en-us_topic_0030911465_p1112031083818"></a><a name="en-us_topic_0030911465_p1112031083818"></a>Formula: Total number of outband outgoing bytes on an ECS/Monitoring interval</p>
<p id="en-us_topic_0030911465_p17183383445"><a name="en-us_topic_0030911465_p17183383445"></a><a name="en-us_topic_0030911465_p17183383445"></a>This metric is unavailable if SR-IOV is enabled.</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0030911465_p59175014121215"><a name="en-us_topic_0030911465_p59175014121215"></a><a name="en-us_topic_0030911465_p59175014121215"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0030911465_p28446836121215"><a name="en-us_topic_0030911465_p28446836121215"></a><a name="en-us_topic_0030911465_p28446836121215"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0030911465_p182931501478"><a name="en-us_topic_0030911465_p182931501478"></a><a name="en-us_topic_0030911465_p182931501478"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0030911465_row2605901916337"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0030911465_p324211523017"><a name="en-us_topic_0030911465_p324211523017"></a><a name="en-us_topic_0030911465_p324211523017"></a>inst_sys_status_error</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0030911465_p3320458516337"><a name="en-us_topic_0030911465_p3320458516337"></a><a name="en-us_topic_0030911465_p3320458516337"></a>System Status Check Failed</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0030911465_p521685316337"><a name="en-us_topic_0030911465_p521685316337"></a><a name="en-us_topic_0030911465_p521685316337"></a>Status of the cloud platform for running ECSs, which can be <strong id="en-us_topic_0030911465_b1565424293203310"><a name="en-us_topic_0030911465_b1565424293203310"></a><a name="en-us_topic_0030911465_b1565424293203310"></a>0</strong> or <strong id="en-us_topic_0030911465_b1229152802203310"><a name="en-us_topic_0030911465_b1229152802203310"></a><a name="en-us_topic_0030911465_b1229152802203310"></a>1</strong></p>
<a name="en-us_topic_0030911465_ul13348182820394"></a><a name="en-us_topic_0030911465_ul13348182820394"></a><ul id="en-us_topic_0030911465_ul13348182820394"><li><strong id="en-us_topic_0030911465_b171676334619247"><a name="en-us_topic_0030911465_b171676334619247"></a><a name="en-us_topic_0030911465_b171676334619247"></a>0</strong>: The system is running properly. All check items are normal.</li><li><strong id="en-us_topic_0030911465_b1087511831192613"><a name="en-us_topic_0030911465_b1087511831192613"></a><a name="en-us_topic_0030911465_b1087511831192613"></a>1</strong>: The system is not running properly. At least one check item failed. When the power source of the physical host fails or the hardware/software becomes faulty, the check result is <strong id="en-us_topic_0030911465_b842352706201616"><a name="en-us_topic_0030911465_b842352706201616"></a><a name="en-us_topic_0030911465_b842352706201616"></a>1</strong>.</li></ul>
<p id="en-us_topic_0030911465_p5086914416723"><a name="en-us_topic_0030911465_p5086914416723"></a><a name="en-us_topic_0030911465_p5086914416723"></a>The system periodically checks the status and returns check results using value <strong id="en-us_topic_0030911465_b842352706192323"><a name="en-us_topic_0030911465_b842352706192323"></a><a name="en-us_topic_0030911465_b842352706192323"></a>0</strong> or <strong id="en-us_topic_0030911465_b842352706192327"><a name="en-us_topic_0030911465_b842352706192327"></a><a name="en-us_topic_0030911465_b842352706192327"></a>1</strong>.</p>
<a name="en-us_topic_0030911465_ul3386195716122"></a><a name="en-us_topic_0030911465_ul3386195716122"></a><ul id="en-us_topic_0030911465_ul3386195716122"><li>If the detected fault does not affect ECS functions, certain management operations performed on the ECS, such as starting, stopping, or specifications modifications, may be affected.</li><li>If the detected fault affects ECS functions, such as a host power supply failure, the system will recover the ECS as soon as possible. </li></ul>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0030911465_p72621040193911"><a name="en-us_topic_0030911465_p72621040193911"></a><a name="en-us_topic_0030911465_p72621040193911"></a><strong>0</strong> or <strong>1</strong></p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0030911465_p225190516337"><a name="en-us_topic_0030911465_p225190516337"></a><a name="en-us_topic_0030911465_p225190516337"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0030911465_p20293206479"><a name="en-us_topic_0030911465_p20293206479"></a><a name="en-us_topic_0030911465_p20293206479"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0030911465_row44572200141717"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0030911465_p024210514305"><a name="en-us_topic_0030911465_p024210514305"></a><a name="en-us_topic_0030911465_p024210514305"></a>ib_card_state</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0030911465_p65605483141717"><a name="en-us_topic_0030911465_p65605483141717"></a><a name="en-us_topic_0030911465_p65605483141717"></a>InfiniBand NIC status</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0030911465_p12443932141717"><a name="en-us_topic_0030911465_p12443932141717"></a><a name="en-us_topic_0030911465_p12443932141717"></a>Status of an InfiniBand NIC on an H2 ECS</p>
<p id="en-us_topic_0030911465_p1325610141717"><a name="en-us_topic_0030911465_p1325610141717"></a><a name="en-us_topic_0030911465_p1325610141717"></a>The system periodically checks the status and returns check results using value <strong id="en-us_topic_0030911465_b1226863769"><a name="en-us_topic_0030911465_b1226863769"></a><a name="en-us_topic_0030911465_b1226863769"></a>0</strong> or <strong id="en-us_topic_0030911465_b686144398"><a name="en-us_topic_0030911465_b686144398"></a><a name="en-us_topic_0030911465_b686144398"></a>1</strong>.</p>
<a name="en-us_topic_0030911465_ul94245295397"></a><a name="en-us_topic_0030911465_ul94245295397"></a><ul id="en-us_topic_0030911465_ul94245295397"><li><strong id="en-us_topic_0030911465_b1295345995"><a name="en-us_topic_0030911465_b1295345995"></a><a name="en-us_topic_0030911465_b1295345995"></a>0</strong>: The system is running properly. That is, the InfiniBand NIC is functional.</li><li><strong id="en-us_topic_0030911465_b1157944315"><a name="en-us_topic_0030911465_b1157944315"></a><a name="en-us_topic_0030911465_b1157944315"></a>1</strong>: The system is not running properly. That is, the InfiniBand NIC malfunctions. When the physical NIC corresponding to a virtual NIC becomes faulty, for example, the network cable is not securely connected to the NIC, the switch or adapter is incompatible with the InfiniBand NIC, or the NIC is disabled, the returned value is <strong id="en-us_topic_0030911465_b842352706174428"><a name="en-us_topic_0030911465_b842352706174428"></a><a name="en-us_topic_0030911465_b842352706174428"></a>1</strong>.</li></ul>
<div class="note" id="en-us_topic_0030911465_note14324438161653"><a name="en-us_topic_0030911465_note14324438161653"></a><a name="en-us_topic_0030911465_note14324438161653"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0030911465_p61811084161653"><a name="en-us_topic_0030911465_p61811084161653"></a><a name="en-us_topic_0030911465_p61811084161653"></a>Only Mellanox EDR 100 GB single-port InfiniBand NICs are supported.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0030911465_p1139153311398"><a name="en-us_topic_0030911465_p1139153311398"></a><a name="en-us_topic_0030911465_p1139153311398"></a><strong>0</strong> or <strong>1</strong></p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0030911465_p40265596141717"><a name="en-us_topic_0030911465_p40265596141717"></a><a name="en-us_topic_0030911465_p40265596141717"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0030911465_p1429319013473"><a name="en-us_topic_0030911465_p1429319013473"></a><a name="en-us_topic_0030911465_p1429319013473"></a>5 minutes</p>
</td>
</tr>
</tbody>
</table>

