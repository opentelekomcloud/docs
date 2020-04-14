# AS and Other Services<a name="EN-US_TOPIC_0192950176"></a>

In addition to scaling resources, AS can work with other cloud services to meet your requirements in various scenarios.

**Table  1**  Related services

<a name="en-us_topic_0190954097_table1856812418720"></a>
<table><thead align="left"><tr id="en-us_topic_0190954097_row156911244716"><th class="cellrowborder" valign="top" width="16.068393160683932%" id="mcps1.2.5.1.1"><p id="en-us_topic_0190954097_p102331346113311"><a name="en-us_topic_0190954097_p102331346113311"></a><a name="en-us_topic_0190954097_p102331346113311"></a>Service Name</p>
</th>
<th class="cellrowborder" valign="top" width="23.787621237876213%" id="mcps1.2.5.1.2"><p id="en-us_topic_0190954097_p826493615347"><a name="en-us_topic_0190954097_p826493615347"></a><a name="en-us_topic_0190954097_p826493615347"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="23.797620237976204%" id="mcps1.2.5.1.3"><p id="en-us_topic_0190954097_p156917241271"><a name="en-us_topic_0190954097_p156917241271"></a><a name="en-us_topic_0190954097_p156917241271"></a>Relationship</p>
</th>
<th class="cellrowborder" valign="top" width="36.34636536346365%" id="mcps1.2.5.1.4"><p id="en-us_topic_0190954097_p35697246715"><a name="en-us_topic_0190954097_p35697246715"></a><a name="en-us_topic_0190954097_p35697246715"></a>Reference</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0190954097_row165698242719"><td class="cellrowborder" valign="top" width="16.068393160683932%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954097_p956972414719"><a name="en-us_topic_0190954097_p956972414719"></a><a name="en-us_topic_0190954097_p956972414719"></a>Elastic Load Balancing (ELB)</p>
</td>
<td class="cellrowborder" valign="top" width="23.787621237876213%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954097_p11261836193416"><a name="en-us_topic_0190954097_p11261836193416"></a><a name="en-us_topic_0190954097_p11261836193416"></a>After ELB is configured, AS automatically binds ECSs to the load balancer when adding ECSs, and unbinds ECSs from the load balancer when removing ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="23.797620237976204%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954097_p256919241777"><a name="en-us_topic_0190954097_p256919241777"></a><a name="en-us_topic_0190954097_p256919241777"></a>The load balancer distributes traffic to all ECSs in an AS group.</p>
</td>
<td class="cellrowborder" valign="top" width="36.34636536346365%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0190954097_p1569132410711"><a name="en-us_topic_0190954097_p1569132410711"></a><a name="en-us_topic_0190954097_p1569132410711"></a><a href="(optional)-adding-a-load-balancer-to-an-as-group.md">(Optional) Adding a Load Balancer to an AS Group</a></p>
</td>
</tr>
<tr id="en-us_topic_0190954097_row187602196425"><td class="cellrowborder" valign="top" width="16.068393160683932%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954097_p77613196420"><a name="en-us_topic_0190954097_p77613196420"></a><a name="en-us_topic_0190954097_p77613196420"></a>Cloud Eye</p>
</td>
<td class="cellrowborder" valign="top" width="23.787621237876213%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954097_p2260113619349"><a name="en-us_topic_0190954097_p2260113619349"></a><a name="en-us_topic_0190954097_p2260113619349"></a>If an alarm-triggered policy is configured, AS triggers scaling actions when an alarm triggering condition specified in Cloud Eye is met.</p>
</td>
<td class="cellrowborder" valign="top" width="23.797620237976204%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954097_p0761181954215"><a name="en-us_topic_0190954097_p0761181954215"></a><a name="en-us_topic_0190954097_p0761181954215"></a>AS scales resources based on ECS status monitored by Cloud Eye.</p>
</td>
<td class="cellrowborder" valign="top" width="36.34636536346365%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0190954097_p27619196429"><a name="en-us_topic_0190954097_p27619196429"></a><a name="en-us_topic_0190954097_p27619196429"></a><a href="#en-us_topic_0190954097_table57136275115435">AS metrics</a></p>
</td>
</tr>
<tr id="en-us_topic_0190954097_row513291817259"><td class="cellrowborder" valign="top" width="16.068393160683932%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954097_p2183134722716"><a name="en-us_topic_0190954097_p2183134722716"></a><a name="en-us_topic_0190954097_p2183134722716"></a>Elastic Cloud Server (ECS)</p>
</td>
<td class="cellrowborder" valign="top" width="23.787621237876213%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954097_p2258936163413"><a name="en-us_topic_0190954097_p2258936163413"></a><a name="en-us_topic_0190954097_p2258936163413"></a>ECSs added in a scaling action can be managed and maintained on the ECS console.</p>
</td>
<td class="cellrowborder" valign="top" width="23.797620237976204%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954097_p13133191817254"><a name="en-us_topic_0190954097_p13133191817254"></a><a name="en-us_topic_0190954097_p13133191817254"></a>AS automatically adjusts the number of ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="36.34636536346365%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0190954097_p4133181815251"><a name="en-us_topic_0190954097_p4133181815251"></a><a name="en-us_topic_0190954097_p4133181815251"></a><a href="dynamically-expanding-resources.md">Dynamically Expanding Resources</a> and <a href="expanding-resources-as-planned.md">Expanding Resources as Planned</a></p>
</td>
</tr>
<tr id="en-us_topic_0190954097_row839202722510"><td class="cellrowborder" valign="top" width="16.068393160683932%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954097_p193931727192510"><a name="en-us_topic_0190954097_p193931727192510"></a><a name="en-us_topic_0190954097_p193931727192510"></a>Virtual Private Cloud (VPC)</p>
</td>
<td class="cellrowborder" valign="top" width="23.787621237876213%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954097_p4254136123413"><a name="en-us_topic_0190954097_p4254136123413"></a><a name="en-us_topic_0190954097_p4254136123413"></a>AS automatically adjusts the bandwidths of EIPs assigned in VPCs and also shared bandwidths.</p>
</td>
<td class="cellrowborder" valign="top" width="23.797620237976204%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954097_p3393132742512"><a name="en-us_topic_0190954097_p3393132742512"></a><a name="en-us_topic_0190954097_p3393132742512"></a>AS automatically adjusts the bandwidth.</p>
</td>
<td class="cellrowborder" valign="top" width="36.34636536346365%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0190954097_p16393132719256"><a name="en-us_topic_0190954097_p16393132719256"></a><a name="en-us_topic_0190954097_p16393132719256"></a><a href="creating-a-bandwidth-scaling-policy.md">Creating a Bandwidth Scaling Policy</a></p>
</td>
</tr>
<tr id="en-us_topic_0190954097_row155695241277"><td class="cellrowborder" valign="top" width="16.068393160683932%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954097_p65692241774"><a name="en-us_topic_0190954097_p65692241774"></a><a name="en-us_topic_0190954097_p65692241774"></a>Cloud Trace Service (CTS)</p>
</td>
<td class="cellrowborder" valign="top" width="23.787621237876213%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954097_p825073663418"><a name="en-us_topic_0190954097_p825073663418"></a><a name="en-us_topic_0190954097_p825073663418"></a>CTS records AS operation logs for view, audit, and backtracking.</p>
</td>
<td class="cellrowborder" valign="top" width="23.797620237976204%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954097_p656913241072"><a name="en-us_topic_0190954097_p656913241072"></a><a name="en-us_topic_0190954097_p656913241072"></a>Log audit</p>
</td>
<td class="cellrowborder" valign="top" width="36.34636536346365%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0190954097_p1956972416714"><a name="en-us_topic_0190954097_p1956972416714"></a><a name="en-us_topic_0190954097_p1956972416714"></a><a href="recording-as-resource-operations.md">Recording AS Resource Operations</a></p>
</td>
</tr>
<tr id="en-us_topic_0190954097_row185691424975"><td class="cellrowborder" valign="top" width="16.068393160683932%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0190954097_p1856982414716"><a name="en-us_topic_0190954097_p1856982414716"></a><a name="en-us_topic_0190954097_p1856982414716"></a>Tag Management Service (TMS)</p>
</td>
<td class="cellrowborder" valign="top" width="23.787621237876213%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0190954097_p31252699193054"><a name="en-us_topic_0190954097_p31252699193054"></a><a name="en-us_topic_0190954097_p31252699193054"></a>If you have multiple resources of the same type, TMS enables you to manage these resources easily.</p>
</td>
<td class="cellrowborder" valign="top" width="23.797620237976204%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0190954097_p1756910243712"><a name="en-us_topic_0190954097_p1756910243712"></a><a name="en-us_topic_0190954097_p1756910243712"></a>Tags</p>
</td>
<td class="cellrowborder" valign="top" width="36.34636536346365%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0190954097_p756918242716"><a name="en-us_topic_0190954097_p756918242716"></a><a name="en-us_topic_0190954097_p756918242716"></a><a href="marking-as-groups-and-instances.md">Marking AS Groups and ECSs</a></p>
</td>
</tr>
</tbody>
</table>

**Table  2**  AS metrics

<a name="en-us_topic_0190954097_table57136275115435"></a>
<table><thead align="left"><tr id="en-us_topic_0190954097_row26323242"><th class="cellrowborder" valign="top" width="15.348465153484646%" id="mcps1.2.6.1.1"><p id="en-us_topic_0190954097_p51807830"><a name="en-us_topic_0190954097_p51807830"></a><a name="en-us_topic_0190954097_p51807830"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="41.65583441655834%" id="mcps1.2.6.1.2"><p id="en-us_topic_0190954097_p35684727"><a name="en-us_topic_0190954097_p35684727"></a><a name="en-us_topic_0190954097_p35684727"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="14.90850914908509%" id="mcps1.2.6.1.3"><p id="en-us_topic_0190954097_p51782583"><a name="en-us_topic_0190954097_p51782583"></a><a name="en-us_topic_0190954097_p51782583"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="14.868513148685128%" id="mcps1.2.6.1.4"><p id="en-us_topic_0190954097_p1437619553263"><a name="en-us_topic_0190954097_p1437619553263"></a><a name="en-us_topic_0190954097_p1437619553263"></a>Monitored Object</p>
</th>
<th class="cellrowborder" valign="top" width="13.218678132186778%" id="mcps1.2.6.1.5"><p id="en-us_topic_0190954097_p47235721105619"><a name="en-us_topic_0190954097_p47235721105619"></a><a name="en-us_topic_0190954097_p47235721105619"></a>Monitoring Interval (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0190954097_row33639718"><td class="cellrowborder" valign="top" width="15.348465153484646%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0190954097_p40462633"><a name="en-us_topic_0190954097_p40462633"></a><a name="en-us_topic_0190954097_p40462633"></a>CPU Usage</p>
</td>
<td class="cellrowborder" valign="top" width="41.65583441655834%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0190954097_p106912192911"><a name="en-us_topic_0190954097_p106912192911"></a><a name="en-us_topic_0190954097_p106912192911"></a>CPU usage of an AS group</p>
<p id="en-us_topic_0190954097_p5508516122917"><a name="en-us_topic_0190954097_p5508516122917"></a><a name="en-us_topic_0190954097_p5508516122917"></a>Formula: Total CPU usage of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0190954097_p56247849"><a name="en-us_topic_0190954097_p56247849"></a><a name="en-us_topic_0190954097_p56247849"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="14.90850914908509%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0190954097_en-us_topic_0030911465_p13045074222846"><a name="en-us_topic_0190954097_en-us_topic_0030911465_p13045074222846"></a><a name="en-us_topic_0190954097_en-us_topic_0030911465_p13045074222846"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.868513148685128%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0190954097_p153761455112614"><a name="en-us_topic_0190954097_p153761455112614"></a><a name="en-us_topic_0190954097_p153761455112614"></a>AS group</p>
</td>
<td class="cellrowborder" valign="top" width="13.218678132186778%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0190954097_p888164105619"><a name="en-us_topic_0190954097_p888164105619"></a><a name="en-us_topic_0190954097_p888164105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0190954097_row27353390"><td class="cellrowborder" valign="top" width="15.348465153484646%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0190954097_p1032124"><a name="en-us_topic_0190954097_p1032124"></a><a name="en-us_topic_0190954097_p1032124"></a>Memory Usage</p>
</td>
<td class="cellrowborder" valign="top" width="41.65583441655834%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0190954097_p16493259"><a name="en-us_topic_0190954097_p16493259"></a><a name="en-us_topic_0190954097_p16493259"></a>Memory usage of an AS group</p>
<p id="en-us_topic_0190954097_p3415225303"><a name="en-us_topic_0190954097_p3415225303"></a><a name="en-us_topic_0190954097_p3415225303"></a>Formula: Total memory usage of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0190954097_p12329122213307"><a name="en-us_topic_0190954097_p12329122213307"></a><a name="en-us_topic_0190954097_p12329122213307"></a>Unit: Percent</p>
<div class="note" id="en-us_topic_0190954097_note193017546365"><a name="en-us_topic_0190954097_note193017546365"></a><a name="en-us_topic_0190954097_note193017546365"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0190954097_p1130265414365"><a name="en-us_topic_0190954097_p1130265414365"></a><a name="en-us_topic_0190954097_p1130265414365"></a>This metric is unavailable if the image has no OTC Tools installed.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="14.90850914908509%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0190954097_p16491755171320"><a name="en-us_topic_0190954097_p16491755171320"></a><a name="en-us_topic_0190954097_p16491755171320"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.868513148685128%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0190954097_p18660202119150"><a name="en-us_topic_0190954097_p18660202119150"></a><a name="en-us_topic_0190954097_p18660202119150"></a>AS group</p>
</td>
<td class="cellrowborder" valign="top" width="13.218678132186778%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0190954097_p4832464105619"><a name="en-us_topic_0190954097_p4832464105619"></a><a name="en-us_topic_0190954097_p4832464105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0190954097_row26669028"><td class="cellrowborder" valign="top" width="15.348465153484646%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0190954097_p63671394104552"><a name="en-us_topic_0190954097_p63671394104552"></a><a name="en-us_topic_0190954097_p63671394104552"></a>Number of Instances</p>
</td>
<td class="cellrowborder" valign="top" width="41.65583441655834%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0190954097_p30149174143433"><a name="en-us_topic_0190954097_p30149174143433"></a><a name="en-us_topic_0190954097_p30149174143433"></a>Number of available ECSs in an AS group</p>
<p id="en-us_topic_0190954097_p1954317478339"><a name="en-us_topic_0190954097_p1954317478339"></a><a name="en-us_topic_0190954097_p1954317478339"></a>Formula: Total number of ECSs in <strong id="en-us_topic_0190954097_b7513363348"><a name="en-us_topic_0190954097_b7513363348"></a><a name="en-us_topic_0190954097_b7513363348"></a>Enabled</strong> state in the AS group</p>
</td>
<td class="cellrowborder" valign="top" width="14.90850914908509%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0190954097_p20374254"><a name="en-us_topic_0190954097_p20374254"></a><a name="en-us_topic_0190954097_p20374254"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.868513148685128%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0190954097_p8204183341518"><a name="en-us_topic_0190954097_p8204183341518"></a><a name="en-us_topic_0190954097_p8204183341518"></a>AS group</p>
</td>
<td class="cellrowborder" valign="top" width="13.218678132186778%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0190954097_p55885300105619"><a name="en-us_topic_0190954097_p55885300105619"></a><a name="en-us_topic_0190954097_p55885300105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0190954097_row49150562"><td class="cellrowborder" valign="top" width="15.348465153484646%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0190954097_p21772565"><a name="en-us_topic_0190954097_p21772565"></a><a name="en-us_topic_0190954097_p21772565"></a>Inband Incoming Rate</p>
</td>
<td class="cellrowborder" valign="top" width="41.65583441655834%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0190954097_p18747312"><a name="en-us_topic_0190954097_p18747312"></a><a name="en-us_topic_0190954097_p18747312"></a>Number of incoming bytes per second on an ECS in an AS group</p>
<p id="en-us_topic_0190954097_p11415571347"><a name="en-us_topic_0190954097_p11415571347"></a><a name="en-us_topic_0190954097_p11415571347"></a>Formula: Total inband incoming rates of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0190954097_p1573177133411"><a name="en-us_topic_0190954097_p1573177133411"></a><a name="en-us_topic_0190954097_p1573177133411"></a>Unit: Byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.90850914908509%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0190954097_p6656179173"><a name="en-us_topic_0190954097_p6656179173"></a><a name="en-us_topic_0190954097_p6656179173"></a>≥ 0 </p>
</td>
<td class="cellrowborder" valign="top" width="14.868513148685128%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0190954097_p1209433141515"><a name="en-us_topic_0190954097_p1209433141515"></a><a name="en-us_topic_0190954097_p1209433141515"></a>AS group</p>
</td>
<td class="cellrowborder" valign="top" width="13.218678132186778%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0190954097_p30415481105619"><a name="en-us_topic_0190954097_p30415481105619"></a><a name="en-us_topic_0190954097_p30415481105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0190954097_row49347015"><td class="cellrowborder" valign="top" width="15.348465153484646%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0190954097_p37685299"><a name="en-us_topic_0190954097_p37685299"></a><a name="en-us_topic_0190954097_p37685299"></a>Inband Outgoing Rate</p>
</td>
<td class="cellrowborder" valign="top" width="41.65583441655834%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0190954097_p32610412"><a name="en-us_topic_0190954097_p32610412"></a><a name="en-us_topic_0190954097_p32610412"></a>Number of outgoing bytes per second on an ECS in an AS group</p>
<p id="en-us_topic_0190954097_p91607516343"><a name="en-us_topic_0190954097_p91607516343"></a><a name="en-us_topic_0190954097_p91607516343"></a>Formula: Total inband outgoing rates of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0190954097_p1949715114340"><a name="en-us_topic_0190954097_p1949715114340"></a><a name="en-us_topic_0190954097_p1949715114340"></a>Unit: Byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.90850914908509%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0190954097_p18524192071718"><a name="en-us_topic_0190954097_p18524192071718"></a><a name="en-us_topic_0190954097_p18524192071718"></a>≥ 0 </p>
</td>
<td class="cellrowborder" valign="top" width="14.868513148685128%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0190954097_p2021523313150"><a name="en-us_topic_0190954097_p2021523313150"></a><a name="en-us_topic_0190954097_p2021523313150"></a>AS group</p>
</td>
<td class="cellrowborder" valign="top" width="13.218678132186778%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0190954097_p47734919105619"><a name="en-us_topic_0190954097_p47734919105619"></a><a name="en-us_topic_0190954097_p47734919105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0190954097_row49585291175830"><td class="cellrowborder" valign="top" width="15.348465153484646%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0190954097_p1411176318214"><a name="en-us_topic_0190954097_p1411176318214"></a><a name="en-us_topic_0190954097_p1411176318214"></a>Disks Read Rate</p>
</td>
<td class="cellrowborder" valign="top" width="41.65583441655834%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0190954097_p220213918214"><a name="en-us_topic_0190954097_p220213918214"></a><a name="en-us_topic_0190954097_p220213918214"></a>Number of bytes read from an AS group per second</p>
<p id="en-us_topic_0190954097_p16302131413351"><a name="en-us_topic_0190954097_p16302131413351"></a><a name="en-us_topic_0190954097_p16302131413351"></a>Formula: Total disks read rates of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0190954097_p1053317144359"><a name="en-us_topic_0190954097_p1053317144359"></a><a name="en-us_topic_0190954097_p1053317144359"></a>Unit: Byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.90850914908509%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0190954097_p13671465175830"><a name="en-us_topic_0190954097_p13671465175830"></a><a name="en-us_topic_0190954097_p13671465175830"></a>≥ 0 </p>
</td>
<td class="cellrowborder" valign="top" width="14.868513148685128%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0190954097_p8846113012155"><a name="en-us_topic_0190954097_p8846113012155"></a><a name="en-us_topic_0190954097_p8846113012155"></a>AS group</p>
</td>
<td class="cellrowborder" valign="top" width="13.218678132186778%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0190954097_p41323205105619"><a name="en-us_topic_0190954097_p41323205105619"></a><a name="en-us_topic_0190954097_p41323205105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0190954097_row34742176175835"><td class="cellrowborder" valign="top" width="15.348465153484646%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0190954097_p4424835218214"><a name="en-us_topic_0190954097_p4424835218214"></a><a name="en-us_topic_0190954097_p4424835218214"></a>Disks Write Rate</p>
</td>
<td class="cellrowborder" valign="top" width="41.65583441655834%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0190954097_p10694175583519"><a name="en-us_topic_0190954097_p10694175583519"></a><a name="en-us_topic_0190954097_p10694175583519"></a>Number of bytes written to an AS group per second</p>
<p id="en-us_topic_0190954097_p2734677318214"><a name="en-us_topic_0190954097_p2734677318214"></a><a name="en-us_topic_0190954097_p2734677318214"></a>Formula: Total disks write rates of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0190954097_p555217291353"><a name="en-us_topic_0190954097_p555217291353"></a><a name="en-us_topic_0190954097_p555217291353"></a>Unit: Byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.90850914908509%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0190954097_p40425551175835"><a name="en-us_topic_0190954097_p40425551175835"></a><a name="en-us_topic_0190954097_p40425551175835"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="14.868513148685128%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0190954097_p18522306155"><a name="en-us_topic_0190954097_p18522306155"></a><a name="en-us_topic_0190954097_p18522306155"></a>AS group</p>
</td>
<td class="cellrowborder" valign="top" width="13.218678132186778%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0190954097_p58845275105619"><a name="en-us_topic_0190954097_p58845275105619"></a><a name="en-us_topic_0190954097_p58845275105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0190954097_row18531428175847"><td class="cellrowborder" valign="top" width="15.348465153484646%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0190954097_p3630726418214"><a name="en-us_topic_0190954097_p3630726418214"></a><a name="en-us_topic_0190954097_p3630726418214"></a>Disks Read Requests</p>
</td>
<td class="cellrowborder" valign="top" width="41.65583441655834%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0190954097_p5520727618214"><a name="en-us_topic_0190954097_p5520727618214"></a><a name="en-us_topic_0190954097_p5520727618214"></a>Number of read requests per second sent to an ECS disk in an AS group</p>
<p id="en-us_topic_0190954097_p32533663612"><a name="en-us_topic_0190954097_p32533663612"></a><a name="en-us_topic_0190954097_p32533663612"></a>Formula: Total disks read rates of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0190954097_p363319663618"><a name="en-us_topic_0190954097_p363319663618"></a><a name="en-us_topic_0190954097_p363319663618"></a>Unit: Request/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.90850914908509%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0190954097_en-us_topic_0030911465_p51947303222846"><a name="en-us_topic_0190954097_en-us_topic_0030911465_p51947303222846"></a><a name="en-us_topic_0190954097_en-us_topic_0030911465_p51947303222846"></a>≥ 0 </p>
</td>
<td class="cellrowborder" valign="top" width="14.868513148685128%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0190954097_p385810309156"><a name="en-us_topic_0190954097_p385810309156"></a><a name="en-us_topic_0190954097_p385810309156"></a>AS group</p>
</td>
<td class="cellrowborder" valign="top" width="13.218678132186778%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0190954097_p1737970105619"><a name="en-us_topic_0190954097_p1737970105619"></a><a name="en-us_topic_0190954097_p1737970105619"></a>5 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0190954097_row32523856175914"><td class="cellrowborder" valign="top" width="15.348465153484646%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0190954097_p4789499918214"><a name="en-us_topic_0190954097_p4789499918214"></a><a name="en-us_topic_0190954097_p4789499918214"></a>Disks Write Requests</p>
</td>
<td class="cellrowborder" valign="top" width="41.65583441655834%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0190954097_p5428973118214"><a name="en-us_topic_0190954097_p5428973118214"></a><a name="en-us_topic_0190954097_p5428973118214"></a>Number of write requests per second sent to an ECS disk in an AS group</p>
<p id="en-us_topic_0190954097_p10201517123617"><a name="en-us_topic_0190954097_p10201517123617"></a><a name="en-us_topic_0190954097_p10201517123617"></a>Formula: Total disks write rates of all ECSs in an AS group/Number of ECSs in the AS group</p>
<p id="en-us_topic_0190954097_p13201617163613"><a name="en-us_topic_0190954097_p13201617163613"></a><a name="en-us_topic_0190954097_p13201617163613"></a>Unit: Request/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.90850914908509%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0190954097_p15652145181"><a name="en-us_topic_0190954097_p15652145181"></a><a name="en-us_topic_0190954097_p15652145181"></a>≥ 0 </p>
</td>
<td class="cellrowborder" valign="top" width="14.868513148685128%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0190954097_p786333041517"><a name="en-us_topic_0190954097_p786333041517"></a><a name="en-us_topic_0190954097_p786333041517"></a>AS group</p>
</td>
<td class="cellrowborder" valign="top" width="13.218678132186778%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0190954097_p6557873105619"><a name="en-us_topic_0190954097_p6557873105619"></a><a name="en-us_topic_0190954097_p6557873105619"></a>5 minutes</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   The image based on which the target ECS is created must have OTC Tools installed. Otherwise,  **Memory Usage**  will be unavailable. For details about how to install the OTC Tools, visit  [https://github.com/UVP-Tools/UVP-Tools/](https://github.com/UVP-Tools/UVP-Tools/).  
>-   OSs determine whether the  **Memory Usage**,  **Inband Outgoing Rate**, and  **Inband Incoming Rate**  metrics are supported. For details, see  _[Elastic Cloud Server User Guide](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0030911465.html)_.  

