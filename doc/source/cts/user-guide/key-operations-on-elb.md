# Key Operations on ELB<a name="en-us_topic_0100273727"></a>

Elastic Load Balancing \(ELB\) is a service that automatically distributes access traffic to multiple ECSs to balance their service load. ELB enables you to achieve higher levels of fault tolerance in your applications and expand application service capabilities.

With a web-based console, you can create load balancers, configure the ports required for listening, and add backend ECSs for load balancers. ELB helps eliminate single points of failure \(SPOFs\), improving availability of the whole system.

With CTS, you can record operations associated with ELB for future query, audit, and backtrack operations.

**Table  1**  ELB operations that can be recorded by CTS

<a name="table37577724194626"></a>
<table><thead align="left"><tr id="rfa95cb0587f848fa8875fd009e3c627e"><th class="cellrowborder" valign="top" width="31.630000000000003%" id="mcps1.2.4.1.1"><p id="a85dfb09ba34a4c40885391b3a1b6060c"><a name="a85dfb09ba34a4c40885391b3a1b6060c"></a><a name="a85dfb09ba34a4c40885391b3a1b6060c"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.57%" id="mcps1.2.4.1.2"><p id="a1e92918ca9b549589074db0f046248e4"><a name="a1e92918ca9b549589074db0f046248e4"></a><a name="a1e92918ca9b549589074db0f046248e4"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.800000000000004%" id="mcps1.2.4.1.3"><p id="a47ee44a828254911b5425dbc6f55dc8e"><a name="a47ee44a828254911b5425dbc6f55dc8e"></a><a name="a47ee44a828254911b5425dbc6f55dc8e"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rd5afffb742b84c5c8229a6e058c21c76"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p629593420475"><a name="p629593420475"></a><a name="p629593420475"></a>Adding a backend ECS group</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p10631194494914"><a name="p10631194494914"></a><a name="p10631194494914"></a>pool</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p16968414195013"><a name="p16968414195013"></a><a name="p16968414195013"></a>createPool</p>
</td>
</tr>
<tr id="r567db8d728fd49d1bd2fa36646db3afa"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p18295123434711"><a name="p18295123434711"></a><a name="p18295123434711"></a>Modifying a backend ECS group</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p66316441494"><a name="p66316441494"></a><a name="p66316441494"></a>pool</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p1996861415508"><a name="p1996861415508"></a><a name="p1996861415508"></a>updatePool</p>
</td>
</tr>
<tr id="r23fdaad92d6c4caeb36cdee95be72a96"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p529510348478"><a name="p529510348478"></a><a name="p529510348478"></a>Deleting a backend ECS group</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p106311344114913"><a name="p106311344114913"></a><a name="p106311344114913"></a>pool</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p8968111420505"><a name="p8968111420505"></a><a name="p8968111420505"></a>deletePool</p>
</td>
</tr>
<tr id="rc1dd5780cb4a4aee878e5bfca359f09d"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p1059184174718"><a name="p1059184174718"></a><a name="p1059184174718"></a>Configuring a forwarding policy</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p1631744134919"><a name="p1631744134919"></a><a name="p1631744134919"></a>l7policy</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p12968314145017"><a name="p12968314145017"></a><a name="p12968314145017"></a>createL7policy</p>
</td>
</tr>
<tr id="r2f4023484c5549feb6f207b3022d45fb"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p4591184114711"><a name="p4591184114711"></a><a name="p4591184114711"></a>Modifying a forwarding policy</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p2631194417498"><a name="p2631194417498"></a><a name="p2631194417498"></a>l7policy</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p199683140505"><a name="p199683140505"></a><a name="p199683140505"></a>updateL7policy</p>
</td>
</tr>
<tr id="r28cc860aa41a4a0ba061f055e5f83a10"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p859114112475"><a name="p859114112475"></a><a name="p859114112475"></a>Deleting a forwarding policy</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p146311644104911"><a name="p146311644104911"></a><a name="p146311644104911"></a>l7policy</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p10968514165019"><a name="p10968514165019"></a><a name="p10968514165019"></a>deleteL7policy</p>
</td>
</tr>
<tr id="r85e9052c91774dba91ac7ae792662522"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p145918419472"><a name="p145918419472"></a><a name="p145918419472"></a>Configuring a forwarding rule</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p1763174404912"><a name="p1763174404912"></a><a name="p1763174404912"></a>l7rule</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p39681014195010"><a name="p39681014195010"></a><a name="p39681014195010"></a>createL7rule</p>
</td>
</tr>
<tr id="r1a7fd544b8224384b485b0c22ddf5f8a"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p8591194164715"><a name="p8591194164715"></a><a name="p8591194164715"></a>Modifying a forwarding rule</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p1963144424910"><a name="p1963144424910"></a><a name="p1963144424910"></a>l7rule</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p9968181485011"><a name="p9968181485011"></a><a name="p9968181485011"></a>updateL7rule</p>
</td>
</tr>
<tr id="ra3ef76f6f10d449cadad8cb01b2ba2d5"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p459116419479"><a name="p459116419479"></a><a name="p459116419479"></a>Deleting a forwarding rule</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p96311144174915"><a name="p96311144174915"></a><a name="p96311144174915"></a>l7rule</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p11969161435013"><a name="p11969161435013"></a><a name="p11969161435013"></a>deleteL7rule</p>
</td>
</tr>
<tr id="rfb890c7ba77a4af199973364fa9cce5c"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p3690447144720"><a name="p3690447144720"></a><a name="p3690447144720"></a>Configuring a health check</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p7631154474918"><a name="p7631154474918"></a><a name="p7631154474918"></a>healthmonitor</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p1396918145505"><a name="p1396918145505"></a><a name="p1396918145505"></a>createHealthmonitor</p>
</td>
</tr>
<tr id="rbfdc35d7064e461fa45936bfd07cd994"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p1069034719478"><a name="p1069034719478"></a><a name="p1069034719478"></a>Deleting a health check</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p663118446493"><a name="p663118446493"></a><a name="p663118446493"></a>healthmonitor</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p3969614195020"><a name="p3969614195020"></a><a name="p3969614195020"></a>updateHealthmonitor</p>
</td>
</tr>
<tr id="rdf4ca2a9bba94d7a94ef0c6084d1d2c8"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p1569054712475"><a name="p1569054712475"></a><a name="p1569054712475"></a>Modifying a health check</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p46311044194918"><a name="p46311044194918"></a><a name="p46311044194918"></a>healthmonitor</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p139691714125015"><a name="p139691714125015"></a><a name="p139691714125015"></a>deleteHealthmonitor</p>
</td>
</tr>
<tr id="rd8d46d8825324529bdb5532737ad5370"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p19690147124716"><a name="p19690147124716"></a><a name="p19690147124716"></a>Creating a certificate</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p663154434917"><a name="p663154434917"></a><a name="p663154434917"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p1496991485019"><a name="p1496991485019"></a><a name="p1496991485019"></a>createCertificate</p>
</td>
</tr>
<tr id="r60a6508572cb45db9169958f0a081a1e"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p66902477473"><a name="p66902477473"></a><a name="p66902477473"></a>Modifying a certificate</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p2631944144911"><a name="p2631944144911"></a><a name="p2631944144911"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p9969514125010"><a name="p9969514125010"></a><a name="p9969514125010"></a>updateCertificate</p>
</td>
</tr>
<tr id="r51e04670452f47d1a3bf7aebcb51a959"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p1069015476470"><a name="p1069015476470"></a><a name="p1069015476470"></a>Deleting a certificate</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p126321344104919"><a name="p126321344104919"></a><a name="p126321344104919"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p3969191417504"><a name="p3969191417504"></a><a name="p3969191417504"></a>deleteCertificate</p>
</td>
</tr>
<tr id="rc22f0acef3644330a56420f3eba261f5"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p169019472473"><a name="p169019472473"></a><a name="p169019472473"></a>Adding a listener</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p13632844144916"><a name="p13632844144916"></a><a name="p13632844144916"></a>listener</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p49693142505"><a name="p49693142505"></a><a name="p49693142505"></a>createListener</p>
</td>
</tr>
<tr id="rfd95d8d3632947809bd64c8d75e0af28"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p8690194784712"><a name="p8690194784712"></a><a name="p8690194784712"></a>Modifying a listener</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p1663274414490"><a name="p1663274414490"></a><a name="p1663274414490"></a>listener</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p12969181413509"><a name="p12969181413509"></a><a name="p12969181413509"></a>updateListener</p>
</td>
</tr>
<tr id="row1861703194034"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p186908474476"><a name="p186908474476"></a><a name="p186908474476"></a>Deleting a listener</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p46325443496"><a name="p46325443496"></a><a name="p46325443496"></a>listener</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p296911414509"><a name="p296911414509"></a><a name="p296911414509"></a>deleteListener</p>
</td>
</tr>
<tr id="row3058864194034"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p2069015479473"><a name="p2069015479473"></a><a name="p2069015479473"></a>Creating a load balancer</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p1763284444920"><a name="p1763284444920"></a><a name="p1763284444920"></a>loadbalancer</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p2096941435013"><a name="p2096941435013"></a><a name="p2096941435013"></a>createLoadbalancer</p>
</td>
</tr>
<tr id="row5883113594034"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p1869054718472"><a name="p1869054718472"></a><a name="p1869054718472"></a>Modifying a load balancer</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p19632174454916"><a name="p19632174454916"></a><a name="p19632174454916"></a>loadbalancer</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p10969151415014"><a name="p10969151415014"></a><a name="p10969151415014"></a>updateLoadbalancer</p>
</td>
</tr>
<tr id="row1442546694034"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p56914472472"><a name="p56914472472"></a><a name="p56914472472"></a>Deleting a load balancer</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p263224419498"><a name="p263224419498"></a><a name="p263224419498"></a>loadbalancer</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p496951416508"><a name="p496951416508"></a><a name="p496951416508"></a>deleteLoadbalancer</p>
</td>
</tr>
<tr id="row2669784494034"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p136911447114717"><a name="p136911447114717"></a><a name="p136911447114717"></a>Adding a backend ECS</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p10632244174915"><a name="p10632244174915"></a><a name="p10632244174915"></a>member</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p19969171415018"><a name="p19969171415018"></a><a name="p19969171415018"></a>createMember</p>
</td>
</tr>
<tr id="row5384430994034"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p669174724715"><a name="p669174724715"></a><a name="p669174724715"></a>Removing a backend ECS</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p4632164444914"><a name="p4632164444914"></a><a name="p4632164444914"></a>member</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p18969151445020"><a name="p18969151445020"></a><a name="p18969151445020"></a>deleteMember</p>
</td>
</tr>
<tr id="row5480612594034"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p969124715476"><a name="p969124715476"></a><a name="p969124715476"></a>Configuring access logs</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.4.1.2 "><p id="p196321744184912"><a name="p196321744184912"></a><a name="p196321744184912"></a>accesslog</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p1696921411509"><a name="p1696921411509"></a><a name="p1696921411509"></a>createAccesslog</p>
</td>
</tr>
</tbody>
</table>

