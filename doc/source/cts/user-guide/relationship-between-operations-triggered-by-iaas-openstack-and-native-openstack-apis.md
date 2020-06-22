# Relationship Between Operations Triggered by IaaS OpenStack and Native OpenStack APIs<a name="en-us_topic_0100366885"></a>

**Table  1**  Relationship between operations triggered by IaaS OpenStack and native OpenStack APIs

<a name="tea6c26156b1e4e689e1ce31b394ea1e7"></a>
<table><thead align="left"><tr id="r2e5c54c099674eaeb61aba2d8bd47db6"><th class="cellrowborder" valign="top" width="20.840000000000003%" id="mcps1.2.6.1.1"><p id="acffbdd884f584691af9e7f9c4985dc6a"><a name="acffbdd884f584691af9e7f9c4985dc6a"></a><a name="acffbdd884f584691af9e7f9c4985dc6a"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.17%" id="mcps1.2.6.1.2"><p id="ace86727c52e0443ba1b382433ff06240"><a name="ace86727c52e0443ba1b382433ff06240"></a><a name="ace86727c52e0443ba1b382433ff06240"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.47%" id="mcps1.2.6.1.3"><p id="a737772654f92464f9f5897aca69b0954"><a name="a737772654f92464f9f5897aca69b0954"></a><a name="a737772654f92464f9f5897aca69b0954"></a><strong id="b842352706183338"><a name="b842352706183338"></a><a name="b842352706183338"></a>Service Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.990000000000006%" id="mcps1.2.6.1.4"><p id="aba9bf84b4cbb44c9a028336ec256777f"><a name="aba9bf84b4cbb44c9a028336ec256777f"></a><a name="aba9bf84b4cbb44c9a028336ec256777f"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.530000000000005%" id="mcps1.2.6.1.5"><p id="a25e1e20328864611ae4d7c2655a6d61a"><a name="a25e1e20328864611ae4d7c2655a6d61a"></a><a name="a25e1e20328864611ae4d7c2655a6d61a"></a>OpenStack Component</p>
</th>
</tr>
</thead>
<tbody><tr id="r55f7cb6b8dde48f98cf85187bc16d520"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p30581715183117"><a name="p30581715183117"></a><a name="p30581715183117"></a>Enabling an ECS</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p33415641183135"><a name="p33415641183135"></a><a name="p33415641183135"></a>enableService</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p21725460183241"><a name="p21725460183241"></a><a name="p21725460183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p60920134183252"><a name="p60920134183252"></a><a name="p60920134183252"></a>computeService</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p3816603218332"><a name="p3816603218332"></a><a name="p3816603218332"></a>nova</p>
</td>
</tr>
<tr id="r59f2bd3d4d5a4e9d90b22856fecaa5b0"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p13927433183117"><a name="p13927433183117"></a><a name="p13927433183117"></a>Disabling an ECS</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p66593704183135"><a name="p66593704183135"></a><a name="p66593704183135"></a>disableService</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p168984183241"><a name="p168984183241"></a><a name="p168984183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p51818959183252"><a name="p51818959183252"></a><a name="p51818959183252"></a>computeService</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p3996833918332"><a name="p3996833918332"></a><a name="p3996833918332"></a>nova</p>
</td>
</tr>
<tr id="r58fb90efaf4b45f3876e2f30748256ad"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p19660912183117"><a name="p19660912183117"></a><a name="p19660912183117"></a>Adding the cause of disabling an ECS</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p27102035183135"><a name="p27102035183135"></a><a name="p27102035183135"></a>logDisabledInfo</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p56080598183241"><a name="p56080598183241"></a><a name="p56080598183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p60839772183252"><a name="p60839772183252"></a><a name="p60839772183252"></a>computeService</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p1167262318332"><a name="p1167262318332"></a><a name="p1167262318332"></a>nova</p>
</td>
</tr>
<tr id="r48b6f08c3ffb4f82bd4af9c4d3db97f6"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p38616840183117"><a name="p38616840183117"></a><a name="p38616840183117"></a>Deleting an ECS</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p27377659183135"><a name="p27377659183135"></a><a name="p27377659183135"></a>deleteService</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p13458291183241"><a name="p13458291183241"></a><a name="p13458291183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p60343720183252"><a name="p60343720183252"></a><a name="p60343720183252"></a>computeService</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p5362562318332"><a name="p5362562318332"></a><a name="p5362562318332"></a>nova</p>
</td>
</tr>
<tr id="rfb783c9454414dcf821d01a9758177f0"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p33062493183117"><a name="p33062493183117"></a><a name="p33062493183117"></a>Creating a flavor</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p26981453183135"><a name="p26981453183135"></a><a name="p26981453183135"></a>createFlavor</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p13200281183241"><a name="p13200281183241"></a><a name="p13200281183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p34266166183252"><a name="p34266166183252"></a><a name="p34266166183252"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p3572058218332"><a name="p3572058218332"></a><a name="p3572058218332"></a>nova</p>
</td>
</tr>
<tr id="r5d3e04ac2d3b4337a4bca9c6d14c6057"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p10475586183117"><a name="p10475586183117"></a><a name="p10475586183117"></a>Deleting a flavor</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p6582587183135"><a name="p6582587183135"></a><a name="p6582587183135"></a>deleteFlavor</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p26437435183241"><a name="p26437435183241"></a><a name="p26437435183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p15537937183252"><a name="p15537937183252"></a><a name="p15537937183252"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p206534318332"><a name="p206534318332"></a><a name="p206534318332"></a>nova</p>
</td>
</tr>
<tr id="r1e315010bc3945908c67f7857a1f68fd"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p53401235183117"><a name="p53401235183117"></a><a name="p53401235183117"></a>Adding/Deleting permissions of a tenant to access specifications</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p33977024183135"><a name="p33977024183135"></a><a name="p33977024183135"></a>operateFlavorAccess</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p12646228183241"><a name="p12646228183241"></a><a name="p12646228183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p52867469183252"><a name="p52867469183252"></a><a name="p52867469183252"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p2924046118332"><a name="p2924046118332"></a><a name="p2924046118332"></a>nova</p>
</td>
</tr>
<tr id="ra14460f3337043fa9c5bef1048038395"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p6359538183117"><a name="p6359538183117"></a><a name="p6359538183117"></a>Creating extra specifications</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p6080159183135"><a name="p6080159183135"></a><a name="p6080159183135"></a>createExtraSpecs</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p25185959183241"><a name="p25185959183241"></a><a name="p25185959183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p19897091183252"><a name="p19897091183252"></a><a name="p19897091183252"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p4278682018332"><a name="p4278682018332"></a><a name="p4278682018332"></a>nova</p>
</td>
</tr>
<tr id="rd2000b102f734d12935d4f3b299daa5d"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p5591689183117"><a name="p5591689183117"></a><a name="p5591689183117"></a>Updating specified extra specifications</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p3251492183135"><a name="p3251492183135"></a><a name="p3251492183135"></a>updateExtraSpec</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p39844479183241"><a name="p39844479183241"></a><a name="p39844479183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p9465240183252"><a name="p9465240183252"></a><a name="p9465240183252"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p5307910118332"><a name="p5307910118332"></a><a name="p5307910118332"></a>nova</p>
</td>
</tr>
<tr id="r16279a2c637242b6867f5eabc4cd5a31"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p49810125183117"><a name="p49810125183117"></a><a name="p49810125183117"></a>Deleting specified extra specifications</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p21527520183135"><a name="p21527520183135"></a><a name="p21527520183135"></a>deleteExtraSpec</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p55596400183241"><a name="p55596400183241"></a><a name="p55596400183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p55056118183252"><a name="p55056118183252"></a><a name="p55056118183252"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p3995958118332"><a name="p3995958118332"></a><a name="p3995958118332"></a>nova</p>
</td>
</tr>
<tr id="rca17fec9b0264ca291c046a398f9e8b8"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p5686328183117"><a name="p5686328183117"></a><a name="p5686328183117"></a>Creating a host group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p57197168183135"><a name="p57197168183135"></a><a name="p57197168183135"></a>createAggregate</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p63130643183241"><a name="p63130643183241"></a><a name="p63130643183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p4809488183252"><a name="p4809488183252"></a><a name="p4809488183252"></a>hostAggregates</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p528795018332"><a name="p528795018332"></a><a name="p528795018332"></a>nova</p>
</td>
</tr>
<tr id="ra2bd4cab907f427e91d292e8aaa3b5d3"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p51693070183117"><a name="p51693070183117"></a><a name="p51693070183117"></a>Updating a host group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p22130997183135"><a name="p22130997183135"></a><a name="p22130997183135"></a>updateAggregate</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p52667341183241"><a name="p52667341183241"></a><a name="p52667341183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p16455905183252"><a name="p16455905183252"></a><a name="p16455905183252"></a>hostAggregates</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p2971053118332"><a name="p2971053118332"></a><a name="p2971053118332"></a>nova</p>
</td>
</tr>
<tr id="r3e842246497f48f998c035e0622ef2f4"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p36175384183117"><a name="p36175384183117"></a><a name="p36175384183117"></a>Deleting a host group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p27370012183135"><a name="p27370012183135"></a><a name="p27370012183135"></a>deleteAggregate</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p8221576183241"><a name="p8221576183241"></a><a name="p8221576183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p50977068183252"><a name="p50977068183252"></a><a name="p50977068183252"></a>hostAggregates</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p4992306318332"><a name="p4992306318332"></a><a name="p4992306318332"></a>nova</p>
</td>
</tr>
<tr id="re8989836c4e445adbe77b52c77a46b9d"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p65180522183117"><a name="p65180522183117"></a><a name="p65180522183117"></a>Adding a host to a host group/Removing a host from a host group/Setting metadata of a host group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p21406551183135"><a name="p21406551183135"></a><a name="p21406551183135"></a>operateAggregate</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p20840054183241"><a name="p20840054183241"></a><a name="p20840054183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p51081020183252"><a name="p51081020183252"></a><a name="p51081020183252"></a>hostAggregates</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p2090884518332"><a name="p2090884518332"></a><a name="p2090884518332"></a>nova</p>
</td>
</tr>
<tr id="r91ea3ecb71e54363ae0461ae410f2dcd"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p3525408183117"><a name="p3525408183117"></a><a name="p3525408183117"></a>Creating a key pair</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p36119585183135"><a name="p36119585183135"></a><a name="p36119585183135"></a>createKeypair</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p25796821183241"><a name="p25796821183241"></a><a name="p25796821183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p59753381183252"><a name="p59753381183252"></a><a name="p59753381183252"></a>keypair</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p883620818332"><a name="p883620818332"></a><a name="p883620818332"></a>nova</p>
</td>
</tr>
<tr id="r48687098eab0427aa2d2f4983c2b98b0"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p19885852183117"><a name="p19885852183117"></a><a name="p19885852183117"></a>Deleting a key pair</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p24503165183135"><a name="p24503165183135"></a><a name="p24503165183135"></a>deleteKeypair</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p15400613183241"><a name="p15400613183241"></a><a name="p15400613183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p6562048183252"><a name="p6562048183252"></a><a name="p6562048183252"></a>keypair</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p6625410018332"><a name="p6625410018332"></a><a name="p6625410018332"></a>nova</p>
</td>
</tr>
<tr id="r02fdb9449de14af1ae255dd44a0c3d40"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p1271496183117"><a name="p1271496183117"></a><a name="p1271496183117"></a>Updating the quota</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p11849975183135"><a name="p11849975183135"></a><a name="p11849975183135"></a>updateQuotas</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p19866738183241"><a name="p19866738183241"></a><a name="p19866738183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p19004082183252"><a name="p19004082183252"></a><a name="p19004082183252"></a>quotaSets</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p4796581018332"><a name="p4796581018332"></a><a name="p4796581018332"></a>nova</p>
</td>
</tr>
<tr id="r76eb3d23c6b644d6bd0a7948c55f4345"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p54505945183117"><a name="p54505945183117"></a><a name="p54505945183117"></a>Deleting the quota</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p48697184183135"><a name="p48697184183135"></a><a name="p48697184183135"></a>revertQuotasToDefaults</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p54446607183241"><a name="p54446607183241"></a><a name="p54446607183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p29549989183252"><a name="p29549989183252"></a><a name="p29549989183252"></a>quotaSets</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p335787118332"><a name="p335787118332"></a><a name="p335787118332"></a>nova</p>
</td>
</tr>
<tr id="rdf23f70fd0d8453da486dd06d80064c1"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p6386953183117"><a name="p6386953183117"></a><a name="p6386953183117"></a>Creating a VM</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p66767252183135"><a name="p66767252183135"></a><a name="p66767252183135"></a>createServer</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p30238552183241"><a name="p30238552183241"></a><a name="p30238552183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p67105547183252"><a name="p67105547183252"></a><a name="p67105547183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p3196914118332"><a name="p3196914118332"></a><a name="p3196914118332"></a>nova</p>
</td>
</tr>
<tr id="r22ae42bed3df442aafbab3b27ac1880c"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p25577691183117"><a name="p25577691183117"></a><a name="p25577691183117"></a>Updating a VM</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p19401015183135"><a name="p19401015183135"></a><a name="p19401015183135"></a>updateServer</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p32197359183241"><a name="p32197359183241"></a><a name="p32197359183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p64691490183252"><a name="p64691490183252"></a><a name="p64691490183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p1872811918332"><a name="p1872811918332"></a><a name="p1872811918332"></a>nova</p>
</td>
</tr>
<tr id="r70975478997f4943a6d8d105e98c0a99"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p56982107183117"><a name="p56982107183117"></a><a name="p56982107183117"></a>Deleting a VM</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p50478963183135"><a name="p50478963183135"></a><a name="p50478963183135"></a>deleteServer</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p50881278183241"><a name="p50881278183241"></a><a name="p50881278183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p49673706183252"><a name="p49673706183252"></a><a name="p49673706183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p2969944018332"><a name="p2969944018332"></a><a name="p2969944018332"></a>nova</p>
</td>
</tr>
<tr id="r5a55f22147d24c11b5f1c0ed586d3f26"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p66678234183117"><a name="p66678234183117"></a><a name="p66678234183117"></a>Operating a VM</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p23506875183135"><a name="p23506875183135"></a><a name="p23506875183135"></a>operateServer</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p48359418183241"><a name="p48359418183241"></a><a name="p48359418183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p40454127183252"><a name="p40454127183252"></a><a name="p40454127183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p4183766718332"><a name="p4183766718332"></a><a name="p4183766718332"></a>nova</p>
</td>
</tr>
<tr id="rcd73d3c51b7d420e9729380a9dbdd509"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p21615541183117"><a name="p21615541183117"></a><a name="p21615541183117"></a>Setting metadata</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p23751818183135"><a name="p23751818183135"></a><a name="p23751818183135"></a>setMetadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p21862749183241"><a name="p21862749183241"></a><a name="p21862749183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p30267652183252"><a name="p30267652183252"></a><a name="p30267652183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p3223522718332"><a name="p3223522718332"></a><a name="p3223522718332"></a>nova</p>
</td>
</tr>
<tr id="r8908def3544d4108a15302d01ca9fe4b"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p54255373183117"><a name="p54255373183117"></a><a name="p54255373183117"></a>Updating metadata/Setting metadata of a specified key</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p988707183135"><a name="p988707183135"></a><a name="p988707183135"></a>updateMetadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p33143915183241"><a name="p33143915183241"></a><a name="p33143915183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p53411589183252"><a name="p53411589183252"></a><a name="p53411589183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p1137854018332"><a name="p1137854018332"></a><a name="p1137854018332"></a>nova</p>
</td>
</tr>
<tr id="r6c2c4ca326aa4817a234765e7cb7a0c9"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p25046671183117"><a name="p25046671183117"></a><a name="p25046671183117"></a>Deleting metadata of a specified key</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p49679185183135"><a name="p49679185183135"></a><a name="p49679185183135"></a>deleteMetadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2723053183241"><a name="p2723053183241"></a><a name="p2723053183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p13907604183252"><a name="p13907604183252"></a><a name="p13907604183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p4056542318332"><a name="p4056542318332"></a><a name="p4056542318332"></a>nova</p>
</td>
</tr>
<tr id="r6fdd05e5be9d42e7b1e2f16a99bb89a0"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p5412653183117"><a name="p5412653183117"></a><a name="p5412653183117"></a>Adding an NIC to a VM</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p44448808183135"><a name="p44448808183135"></a><a name="p44448808183135"></a>createInterface</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p38948855183241"><a name="p38948855183241"></a><a name="p38948855183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p5204955183252"><a name="p5204955183252"></a><a name="p5204955183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p4429364118332"><a name="p4429364118332"></a><a name="p4429364118332"></a>nova</p>
</td>
</tr>
<tr id="r0abff2bff97342f182cc370c4513dff7"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p53510370183117"><a name="p53510370183117"></a><a name="p53510370183117"></a>Detaching an NIC from a VM</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p56708801183135"><a name="p56708801183135"></a><a name="p56708801183135"></a>detachInterface</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6666405183241"><a name="p6666405183241"></a><a name="p6666405183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p36316495183252"><a name="p36316495183252"></a><a name="p36316495183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p1070090018332"><a name="p1070090018332"></a><a name="p1070090018332"></a>nova</p>
</td>
</tr>
<tr id="r1e9e8299f0d64979990b00e8158ddb75"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p18810225183117"><a name="p18810225183117"></a><a name="p18810225183117"></a>Clearing the password (DB) of a specified VM</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p1656321183135"><a name="p1656321183135"></a><a name="p1656321183135"></a>clearAdminPassword</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p27971289183241"><a name="p27971289183241"></a><a name="p27971289183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p33833066183252"><a name="p33833066183252"></a><a name="p33833066183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p1632792218332"><a name="p1632792218332"></a><a name="p1632792218332"></a>nova</p>
</td>
</tr>
<tr id="r19d748ef70a442ae9c568fbd5c291b10"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p22446374183117"><a name="p22446374183117"></a><a name="p22446374183117"></a>Attaching a volume to a VM</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p66607698183135"><a name="p66607698183135"></a><a name="p66607698183135"></a>attachVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p57083901183241"><a name="p57083901183241"></a><a name="p57083901183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p35352688183252"><a name="p35352688183252"></a><a name="p35352688183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p2478692918332"><a name="p2478692918332"></a><a name="p2478692918332"></a>nova</p>
</td>
</tr>
<tr id="r9659b2d922074a6ea4f81495269b76ee"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p55952786183117"><a name="p55952786183117"></a><a name="p55952786183117"></a>Detaching a volume from a VM</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p37303399183135"><a name="p37303399183135"></a><a name="p37303399183135"></a>detachVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6668742183241"><a name="p6668742183241"></a><a name="p6668742183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p2305834183252"><a name="p2305834183252"></a><a name="p2305834183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p1738684918332"><a name="p1738684918332"></a><a name="p1738684918332"></a>nova</p>
</td>
</tr>
<tr id="r1c7a7acf955a4eb58185489d0d77d9be"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p54500946183117"><a name="p54500946183117"></a><a name="p54500946183117"></a>Creating a VM group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p15088123183135"><a name="p15088123183135"></a><a name="p15088123183135"></a>createServerGroup</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p29675246183241"><a name="p29675246183241"></a><a name="p29675246183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p3231660183252"><a name="p3231660183252"></a><a name="p3231660183252"></a>serverGroup</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p5854663818332"><a name="p5854663818332"></a><a name="p5854663818332"></a>nova</p>
</td>
</tr>
<tr id="r504097ea854f4c92836ccbc73e26b529"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p2742215183117"><a name="p2742215183117"></a><a name="p2742215183117"></a>Deleting a VM group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p60497041183135"><a name="p60497041183135"></a><a name="p60497041183135"></a>deleteServerGroup</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p24200696183241"><a name="p24200696183241"></a><a name="p24200696183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p7070482183252"><a name="p7070482183252"></a><a name="p7070482183252"></a>serverGroup</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p6637082718332"><a name="p6637082718332"></a><a name="p6637082718332"></a>nova</p>
</td>
</tr>
<tr id="r5ebb449827d741d3879e5e80c74a88e5"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p52918238183117"><a name="p52918238183117"></a><a name="p52918238183117"></a>Creating a VM</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p11819572183135"><a name="p11819572183135"></a><a name="p11819572183135"></a>createServerVolumesBoot</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p59785712183241"><a name="p59785712183241"></a><a name="p59785712183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p54107966183252"><a name="p54107966183252"></a><a name="p54107966183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p6595147618332"><a name="p6595147618332"></a><a name="p6595147618332"></a>nova</p>
</td>
</tr>
<tr id="rb0e6b19947bb48d19fa19ae8ff844945"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p56907977183117"><a name="p56907977183117"></a><a name="p56907977183117"></a>Creating a console</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p26533944183135"><a name="p26533944183135"></a><a name="p26533944183135"></a>createServerRemoteConsoles</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p30131495183241"><a name="p30131495183241"></a><a name="p30131495183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p51804058183252"><a name="p51804058183252"></a><a name="p51804058183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p2867972318332"><a name="p2867972318332"></a><a name="p2867972318332"></a>nova</p>
</td>
</tr>
<tr id="r01c36c6c684f4cfb84ac78dbb9f57a03"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p12637635183117"><a name="p12637635183117"></a><a name="p12637635183117"></a>Resetting the password</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p15892470183135"><a name="p15892470183135"></a><a name="p15892470183135"></a>resetServerPassword</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p21261818183241"><a name="p21261818183241"></a><a name="p21261818183241"></a>ECS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p49977307183252"><a name="p49977307183252"></a><a name="p49977307183252"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p3666146618332"><a name="p3666146618332"></a><a name="p3666146618332"></a>nova</p>
</td>
</tr>
<tr id="rc9dd7b7b0af6438a98989eb0d47c6f7b"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p43329111183318"><a name="p43329111183318"></a><a name="p43329111183318"></a>Creating a floating IP address</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p41327539183334"><a name="p41327539183334"></a><a name="p41327539183334"></a>createFloatingip</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2314286218343"><a name="p2314286218343"></a><a name="p2314286218343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p40301250183417"><a name="p40301250183417"></a><a name="p40301250183417"></a>floatingips</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p59493595183431"><a name="p59493595183431"></a><a name="p59493595183431"></a>neutron</p>
</td>
</tr>
<tr id="r984ab805e71748a4ac9af3c90333ed05"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p45756501183318"><a name="p45756501183318"></a><a name="p45756501183318"></a>Updating a floating IP address</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p63005054183334"><a name="p63005054183334"></a><a name="p63005054183334"></a>updateFloatingip</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2682201318343"><a name="p2682201318343"></a><a name="p2682201318343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p53038036183417"><a name="p53038036183417"></a><a name="p53038036183417"></a>floatingips</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p18505330183431"><a name="p18505330183431"></a><a name="p18505330183431"></a>neutron</p>
</td>
</tr>
<tr id="r55fcb6e53bc74f90b9c3c4aa40a6cbc3"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p3383879183318"><a name="p3383879183318"></a><a name="p3383879183318"></a>Deleting a floating IP address</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p28221436183334"><a name="p28221436183334"></a><a name="p28221436183334"></a>deleteFloatingip</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2456865818343"><a name="p2456865818343"></a><a name="p2456865818343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p10022968183417"><a name="p10022968183417"></a><a name="p10022968183417"></a>floatingips</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p1503930183431"><a name="p1503930183431"></a><a name="p1503930183431"></a>neutron</p>
</td>
</tr>
<tr id="r1f9e9d2133b240508d12f6508a0a3fe8"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p50928961183318"><a name="p50928961183318"></a><a name="p50928961183318"></a>Creating a firewall group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p38115179183334"><a name="p38115179183334"></a><a name="p38115179183334"></a>createFirewallGroup</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p5959395018343"><a name="p5959395018343"></a><a name="p5959395018343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p58986874183417"><a name="p58986874183417"></a><a name="p58986874183417"></a>FWaaS v2</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p22623295183431"><a name="p22623295183431"></a><a name="p22623295183431"></a>neutron</p>
</td>
</tr>
<tr id="rda92404f24f74fb3b8774d865062f4cb"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p16011359183318"><a name="p16011359183318"></a><a name="p16011359183318"></a>Updating a firewall group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p2895819183334"><a name="p2895819183334"></a><a name="p2895819183334"></a>updateFirewallGroup</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2455494218343"><a name="p2455494218343"></a><a name="p2455494218343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p51758187183417"><a name="p51758187183417"></a><a name="p51758187183417"></a>FWaaS v2</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p50710740183431"><a name="p50710740183431"></a><a name="p50710740183431"></a>neutron</p>
</td>
</tr>
<tr id="rae270fefc63d4799b590bc07bf0b4151"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p62447491183318"><a name="p62447491183318"></a><a name="p62447491183318"></a>Deleting a firewall group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p30677416183334"><a name="p30677416183334"></a><a name="p30677416183334"></a>deleteFirewallGroup</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p4959496318343"><a name="p4959496318343"></a><a name="p4959496318343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p16537063183417"><a name="p16537063183417"></a><a name="p16537063183417"></a>FWaaS v2</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p58254933183431"><a name="p58254933183431"></a><a name="p58254933183431"></a>neutron</p>
</td>
</tr>
<tr id="rea61d0d8edc64e128a2c8f520ac57f98"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p24411159183318"><a name="p24411159183318"></a><a name="p24411159183318"></a>Creating a firewall policy</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p16584917183334"><a name="p16584917183334"></a><a name="p16584917183334"></a>createFirewallPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p5015975418343"><a name="p5015975418343"></a><a name="p5015975418343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p43032978183417"><a name="p43032978183417"></a><a name="p43032978183417"></a>FWaaS v2</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p55044452183431"><a name="p55044452183431"></a><a name="p55044452183431"></a>neutron</p>
</td>
</tr>
<tr id="r46fb1cd4d3be42dd8435421e5eb3c4c2"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p11886544183318"><a name="p11886544183318"></a><a name="p11886544183318"></a>Updating a firewall policy</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p10809646183334"><a name="p10809646183334"></a><a name="p10809646183334"></a>updateFirewallPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p5923906118343"><a name="p5923906118343"></a><a name="p5923906118343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p31201942183417"><a name="p31201942183417"></a><a name="p31201942183417"></a>FWaaS v2</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p63413803183431"><a name="p63413803183431"></a><a name="p63413803183431"></a>neutron</p>
</td>
</tr>
<tr id="rfae297cd6dfa41d9a167373b777e4fd3"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p8247656183318"><a name="p8247656183318"></a><a name="p8247656183318"></a>Deleting a firewall policy</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p28495189183334"><a name="p28495189183334"></a><a name="p28495189183334"></a>deleteFirewallPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p3427627118343"><a name="p3427627118343"></a><a name="p3427627118343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p63420006183417"><a name="p63420006183417"></a><a name="p63420006183417"></a>FWaaS v2</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p57764639183431"><a name="p57764639183431"></a><a name="p57764639183431"></a>neutron</p>
</td>
</tr>
<tr id="r59713401d82b459c9ade667c4b970a12"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p39852898183318"><a name="p39852898183318"></a><a name="p39852898183318"></a>Inserting a firewall rule into a firewall policy</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p36353908183334"><a name="p36353908183334"></a><a name="p36353908183334"></a>insertFirewallPolicyRule</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2290453918343"><a name="p2290453918343"></a><a name="p2290453918343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p62286205183417"><a name="p62286205183417"></a><a name="p62286205183417"></a>FWaaS v2</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p33164730183431"><a name="p33164730183431"></a><a name="p33164730183431"></a>neutron</p>
</td>
</tr>
<tr id="r9d4de9ab4cc742a9bb42e9967b407a25"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p61734090183318"><a name="p61734090183318"></a><a name="p61734090183318"></a>Removing a firewall rule from a firewall policy</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p61107200183334"><a name="p61107200183334"></a><a name="p61107200183334"></a>removeFirewallPolicyRule</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p5441117318343"><a name="p5441117318343"></a><a name="p5441117318343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p41051678183417"><a name="p41051678183417"></a><a name="p41051678183417"></a>FWaaS v2</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p17897792183431"><a name="p17897792183431"></a><a name="p17897792183431"></a>neutron</p>
</td>
</tr>
<tr id="r45e8e1284b754c859ff232cfd4dc44ff"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p41212913183318"><a name="p41212913183318"></a><a name="p41212913183318"></a>Creating a firewall rule</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p53972595183334"><a name="p53972595183334"></a><a name="p53972595183334"></a>createFirewallRule</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p440649418343"><a name="p440649418343"></a><a name="p440649418343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p63229204183417"><a name="p63229204183417"></a><a name="p63229204183417"></a>FWaaS v2</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p28370810183431"><a name="p28370810183431"></a><a name="p28370810183431"></a>neutron</p>
</td>
</tr>
<tr id="ref37d881edf545f19a669485689172e6"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p46551860183318"><a name="p46551860183318"></a><a name="p46551860183318"></a>Updating a firewall rule</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p20228113183334"><a name="p20228113183334"></a><a name="p20228113183334"></a>updateFirewallRule</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p5821782618343"><a name="p5821782618343"></a><a name="p5821782618343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p57409651183417"><a name="p57409651183417"></a><a name="p57409651183417"></a>FWaaS v2</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p12790652183431"><a name="p12790652183431"></a><a name="p12790652183431"></a>neutron</p>
</td>
</tr>
<tr id="rbcd9aa17a94a4ea29fc0a13194e36289"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p46329780183318"><a name="p46329780183318"></a><a name="p46329780183318"></a>Deleting a firewall rule</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p49453219183334"><a name="p49453219183334"></a><a name="p49453219183334"></a>deleteFirewallRule</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2799381318343"><a name="p2799381318343"></a><a name="p2799381318343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p42813524183417"><a name="p42813524183417"></a><a name="p42813524183417"></a>FWaaS v2</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p63362658183431"><a name="p63362658183431"></a><a name="p63362658183431"></a>neutron</p>
</td>
</tr>
<tr id="row501529174545"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p2743731217465"><a name="p2743731217465"></a><a name="p2743731217465"></a>Creating a NAT gateway</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p24962923174619"><a name="p24962923174619"></a><a name="p24962923174619"></a>createNatGateway</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p19806536174545"><a name="p19806536174545"></a><a name="p19806536174545"></a>VPC-OpenStack</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p65280981174651"><a name="p65280981174651"></a><a name="p65280981174651"></a>natgateways</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p4024374317475"><a name="p4024374317475"></a><a name="p4024374317475"></a>neutron</p>
</td>
</tr>
<tr id="row27572359174545"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p335956917465"><a name="p335956917465"></a><a name="p335956917465"></a>Updating a NAT gateway</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p11468781174619"><a name="p11468781174619"></a><a name="p11468781174619"></a>updateNatGateway</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p27056388174635"><a name="p27056388174635"></a><a name="p27056388174635"></a>VPC-OpenStack</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p9651280174651"><a name="p9651280174651"></a><a name="p9651280174651"></a>natgateways</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p1111508017475"><a name="p1111508017475"></a><a name="p1111508017475"></a>neutron</p>
</td>
</tr>
<tr id="row20473080174545"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p3320723317465"><a name="p3320723317465"></a><a name="p3320723317465"></a>Deleting a NAT gateway</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p39242487174619"><a name="p39242487174619"></a><a name="p39242487174619"></a>deleteNatGateway</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p26960494174635"><a name="p26960494174635"></a><a name="p26960494174635"></a>VPC-OpenStack</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p56461732174651"><a name="p56461732174651"></a><a name="p56461732174651"></a>natgateways</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p4982994817475"><a name="p4982994817475"></a><a name="p4982994817475"></a>neutron</p>
</td>
</tr>
<tr id="row61042026174545"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p4888238717465"><a name="p4888238717465"></a><a name="p4888238717465"></a>Creating an SNAT rule</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p19397541174619"><a name="p19397541174619"></a><a name="p19397541174619"></a>createSnatRule</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p40814269174635"><a name="p40814269174635"></a><a name="p40814269174635"></a>VPC-OpenStack</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p22869316174651"><a name="p22869316174651"></a><a name="p22869316174651"></a>snatrules</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p12702462181426"><a name="p12702462181426"></a><a name="p12702462181426"></a>neutron</p>
</td>
</tr>
<tr id="row55316064174545"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p45403517465"><a name="p45403517465"></a><a name="p45403517465"></a>Deleting an SNAT rule</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p47946201174619"><a name="p47946201174619"></a><a name="p47946201174619"></a>deleteSnatRule</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p54663832174635"><a name="p54663832174635"></a><a name="p54663832174635"></a>VPC-OpenStack</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p28733355174651"><a name="p28733355174651"></a><a name="p28733355174651"></a>snatrules</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p66180864181426"><a name="p66180864181426"></a><a name="p66180864181426"></a>neutron</p>
</td>
</tr>
<tr id="row65957161174545"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p6255624217465"><a name="p6255624217465"></a><a name="p6255624217465"></a>Creating a DNAT rule</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p56171261174619"><a name="p56171261174619"></a><a name="p56171261174619"></a>createDnatRule</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p56830760174635"><a name="p56830760174635"></a><a name="p56830760174635"></a>VPC-OpenStack</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p8650524174651"><a name="p8650524174651"></a><a name="p8650524174651"></a>dnatrules</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p61685699181426"><a name="p61685699181426"></a><a name="p61685699181426"></a>neutron</p>
</td>
</tr>
<tr id="row30086936174545"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p3658225317465"><a name="p3658225317465"></a><a name="p3658225317465"></a>Deleting a DNAT rule</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p12442822174619"><a name="p12442822174619"></a><a name="p12442822174619"></a>deleteDnatRule</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p28010005174635"><a name="p28010005174635"></a><a name="p28010005174635"></a>VPC-OpenStack</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p65108066174651"><a name="p65108066174651"></a><a name="p65108066174651"></a>dnatrules</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p28154934174545"><a name="p28154934174545"></a><a name="p28154934174545"></a>neutron</p>
</td>
</tr>
<tr id="r58a89784a999488bae757ecb13edb2de"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p18165608183318"><a name="p18165608183318"></a><a name="p18165608183318"></a>Creating a VPC</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p55972576183334"><a name="p55972576183334"></a><a name="p55972576183334"></a>createNetwork</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2206768218343"><a name="p2206768218343"></a><a name="p2206768218343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p10820418183417"><a name="p10820418183417"></a><a name="p10820418183417"></a>networks</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p32503715183431"><a name="p32503715183431"></a><a name="p32503715183431"></a>neutron</p>
</td>
</tr>
<tr id="r0f0bc222002d441ebfbca1abaa093999"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p22282025183318"><a name="p22282025183318"></a><a name="p22282025183318"></a>Updating a VPC</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p1819037183334"><a name="p1819037183334"></a><a name="p1819037183334"></a>updateNetwork</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p4832223018343"><a name="p4832223018343"></a><a name="p4832223018343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p36347874183417"><a name="p36347874183417"></a><a name="p36347874183417"></a>networks</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p5779848183431"><a name="p5779848183431"></a><a name="p5779848183431"></a>neutron</p>
</td>
</tr>
<tr id="r6a049138627d46f58db91288aee8c907"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p3251445183318"><a name="p3251445183318"></a><a name="p3251445183318"></a>Deleting a VPC</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p51010036183334"><a name="p51010036183334"></a><a name="p51010036183334"></a>deleteNetwork</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6186106018343"><a name="p6186106018343"></a><a name="p6186106018343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p56708187183417"><a name="p56708187183417"></a><a name="p56708187183417"></a>networks</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p52759716183431"><a name="p52759716183431"></a><a name="p52759716183431"></a>neutron</p>
</td>
</tr>
<tr id="r6e5281a777fd43b6ad522360c53bed01"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p35908811183318"><a name="p35908811183318"></a><a name="p35908811183318"></a>Creating a virtual port</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p17909482183334"><a name="p17909482183334"></a><a name="p17909482183334"></a>createPort</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2737241818343"><a name="p2737241818343"></a><a name="p2737241818343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p22276865183417"><a name="p22276865183417"></a><a name="p22276865183417"></a>ports</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p27180955183431"><a name="p27180955183431"></a><a name="p27180955183431"></a>neutron</p>
</td>
</tr>
<tr id="rabdaa1d1fc8a49eea6568428b18c2da2"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p5066556183318"><a name="p5066556183318"></a><a name="p5066556183318"></a>Updating a virtual port</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p36893321183334"><a name="p36893321183334"></a><a name="p36893321183334"></a>updatePort</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2316022918343"><a name="p2316022918343"></a><a name="p2316022918343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p66599080183417"><a name="p66599080183417"></a><a name="p66599080183417"></a>ports</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p17801669183431"><a name="p17801669183431"></a><a name="p17801669183431"></a>neutron</p>
</td>
</tr>
<tr id="r92a5c71006ec4461882fd40e4125abd4"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p2532226183318"><a name="p2532226183318"></a><a name="p2532226183318"></a>Deleting a virtual port</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p51685820183334"><a name="p51685820183334"></a><a name="p51685820183334"></a>deletePort</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p3948231718343"><a name="p3948231718343"></a><a name="p3948231718343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p31020672183417"><a name="p31020672183417"></a><a name="p31020672183417"></a>ports</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p25406337183431"><a name="p25406337183431"></a><a name="p25406337183431"></a>neutron</p>
</td>
</tr>
<tr id="rc6d30b9952c84994a52b5f2065882f98"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p34054065183318"><a name="p34054065183318"></a><a name="p34054065183318"></a>Creating a vRouter</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p30890430183334"><a name="p30890430183334"></a><a name="p30890430183334"></a>createRouter</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6001575818343"><a name="p6001575818343"></a><a name="p6001575818343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p65491733183417"><a name="p65491733183417"></a><a name="p65491733183417"></a>routes</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p66282587183431"><a name="p66282587183431"></a><a name="p66282587183431"></a>neutron</p>
</td>
</tr>
<tr id="rc8fd9d8b502d44cda2bfa2c8d68926e9"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p62242786183318"><a name="p62242786183318"></a><a name="p62242786183318"></a>Updating a vRouter</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p37654418183334"><a name="p37654418183334"></a><a name="p37654418183334"></a>updateRouter</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6361715318343"><a name="p6361715318343"></a><a name="p6361715318343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p29071418183417"><a name="p29071418183417"></a><a name="p29071418183417"></a>routes</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p1623844183431"><a name="p1623844183431"></a><a name="p1623844183431"></a>neutron</p>
</td>
</tr>
<tr id="r4627930fd14a49fba730e0abfaaebe7a"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p9399546183318"><a name="p9399546183318"></a><a name="p9399546183318"></a>Deleting a vRouter</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p2545860183334"><a name="p2545860183334"></a><a name="p2545860183334"></a>deleteRouter</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p467994718343"><a name="p467994718343"></a><a name="p467994718343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p53772235183417"><a name="p53772235183417"></a><a name="p53772235183417"></a>routes</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p42931896183431"><a name="p42931896183431"></a><a name="p42931896183431"></a>neutron</p>
</td>
</tr>
<tr id="r38b5f77df2e640a697ee9d062762c84f"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p7165283183318"><a name="p7165283183318"></a><a name="p7165283183318"></a>Adding a vRouter API</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p43992613183334"><a name="p43992613183334"></a><a name="p43992613183334"></a>addRouterInterface</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p5623835818343"><a name="p5623835818343"></a><a name="p5623835818343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p8383082183417"><a name="p8383082183417"></a><a name="p8383082183417"></a>routes</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p24622267183431"><a name="p24622267183431"></a><a name="p24622267183431"></a>neutron</p>
</td>
</tr>
<tr id="reb864d9b61294562baadda216eedfbe2"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p56109008183318"><a name="p56109008183318"></a><a name="p56109008183318"></a>Deleting a vRouter API</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p59687057183334"><a name="p59687057183334"></a><a name="p59687057183334"></a>removeRouterInterface</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6135598818343"><a name="p6135598818343"></a><a name="p6135598818343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p4360257183417"><a name="p4360257183417"></a><a name="p4360257183417"></a>routes</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p31566423183431"><a name="p31566423183431"></a><a name="p31566423183431"></a>neutron</p>
</td>
</tr>
<tr id="ra5fedfdb0b8345409a38444f9c646677"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p34168828183318"><a name="p34168828183318"></a><a name="p34168828183318"></a>Adding an extra route to the current vRouter</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p25321388183334"><a name="p25321388183334"></a><a name="p25321388183334"></a>addExtraRoute</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p3401254718343"><a name="p3401254718343"></a><a name="p3401254718343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p24511429183417"><a name="p24511429183417"></a><a name="p24511429183417"></a>routes</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p60691199183431"><a name="p60691199183431"></a><a name="p60691199183431"></a>neutron</p>
</td>
</tr>
<tr id="r683a3f8fe31042de9955ef11456d6cfc"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p11687274183318"><a name="p11687274183318"></a><a name="p11687274183318"></a>Deleting a specified extra route from the current vRouter</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p4354720183334"><a name="p4354720183334"></a><a name="p4354720183334"></a>removeExtraRoute</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p3197597118343"><a name="p3197597118343"></a><a name="p3197597118343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p17874544183417"><a name="p17874544183417"></a><a name="p17874544183417"></a>routes</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p19142958183431"><a name="p19142958183431"></a><a name="p19142958183431"></a>neutron</p>
</td>
</tr>
<tr id="r42c236c43f6d44f6b07ff656ff9ba93e"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p64306213183318"><a name="p64306213183318"></a><a name="p64306213183318"></a>Creating a security group rule</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p20474592183334"><a name="p20474592183334"></a><a name="p20474592183334"></a>createSecurity-group-rule</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2370720018343"><a name="p2370720018343"></a><a name="p2370720018343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p11423622183417"><a name="p11423622183417"></a><a name="p11423622183417"></a>security-group-rules</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p63681831183431"><a name="p63681831183431"></a><a name="p63681831183431"></a>neutron</p>
</td>
</tr>
<tr id="rd14d67831617441da5358f11b482bc8f"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p37242753183318"><a name="p37242753183318"></a><a name="p37242753183318"></a>Deleting a security group rule</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p27810023183334"><a name="p27810023183334"></a><a name="p27810023183334"></a>deleteSecurity-group-rule</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p3557111718343"><a name="p3557111718343"></a><a name="p3557111718343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p6321360183417"><a name="p6321360183417"></a><a name="p6321360183417"></a>security-group-rules</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p51830197183431"><a name="p51830197183431"></a><a name="p51830197183431"></a>neutron</p>
</td>
</tr>
<tr id="r887e1604739a47d58834d5fa31806f3f"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p37986007183318"><a name="p37986007183318"></a><a name="p37986007183318"></a>Creating a security group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p6630136183334"><a name="p6630136183334"></a><a name="p6630136183334"></a>createSecurity-group</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2732346218343"><a name="p2732346218343"></a><a name="p2732346218343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p44868962183417"><a name="p44868962183417"></a><a name="p44868962183417"></a>security-groups</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p1923820183431"><a name="p1923820183431"></a><a name="p1923820183431"></a>neutron</p>
</td>
</tr>
<tr id="r91a0638808184e069ba70d6067d3dbea"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p42947660183318"><a name="p42947660183318"></a><a name="p42947660183318"></a>Deleting a security group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p1531358183334"><a name="p1531358183334"></a><a name="p1531358183334"></a>deleteSecurity-group</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p5458039718343"><a name="p5458039718343"></a><a name="p5458039718343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p27457112183417"><a name="p27457112183417"></a><a name="p27457112183417"></a>security-groups</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p60287717183431"><a name="p60287717183431"></a><a name="p60287717183431"></a>neutron</p>
</td>
</tr>
<tr id="rc966efe7c4b94d9bb1d9f803e5863aae"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p36113802183318"><a name="p36113802183318"></a><a name="p36113802183318"></a>Updating a security group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p42618797183334"><a name="p42618797183334"></a><a name="p42618797183334"></a>updateSecurity-group</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6066202818343"><a name="p6066202818343"></a><a name="p6066202818343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p17793428183417"><a name="p17793428183417"></a><a name="p17793428183417"></a>security-groups</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p60549253183431"><a name="p60549253183431"></a><a name="p60549253183431"></a>neutron</p>
</td>
</tr>
<tr id="r2405196b2b6c4ed098207f720c7e366a"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p20287108183318"><a name="p20287108183318"></a><a name="p20287108183318"></a>Creating a virtual subnet</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p64808062183334"><a name="p64808062183334"></a><a name="p64808062183334"></a>createSubnet</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6498658418343"><a name="p6498658418343"></a><a name="p6498658418343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p19398272183417"><a name="p19398272183417"></a><a name="p19398272183417"></a>subnets</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p49882166183431"><a name="p49882166183431"></a><a name="p49882166183431"></a>neutron</p>
</td>
</tr>
<tr id="r646cf5c42003468380e9a80564d66b64"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p25351733183318"><a name="p25351733183318"></a><a name="p25351733183318"></a>Updating a virtual subnet</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p437558183334"><a name="p437558183334"></a><a name="p437558183334"></a>updateSubnet</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6347124318343"><a name="p6347124318343"></a><a name="p6347124318343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p48479441183417"><a name="p48479441183417"></a><a name="p48479441183417"></a>subnets</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p58203819183431"><a name="p58203819183431"></a><a name="p58203819183431"></a>neutron</p>
</td>
</tr>
<tr id="r03de56946f7e45ccb21ab471f6595d2c"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p26475872183318"><a name="p26475872183318"></a><a name="p26475872183318"></a>Deleting a virtual subnet</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p50544703183334"><a name="p50544703183334"></a><a name="p50544703183334"></a>deleteSubnet</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p3252951318343"><a name="p3252951318343"></a><a name="p3252951318343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p42250561183417"><a name="p42250561183417"></a><a name="p42250561183417"></a>subnets</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p17782175183431"><a name="p17782175183431"></a><a name="p17782175183431"></a>neutron</p>
</td>
</tr>
<tr id="r2a393ee2624b4dc3bfa586825d42061f"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p40666960183318"><a name="p40666960183318"></a><a name="p40666960183318"></a>Creating a VPN</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p4322380183334"><a name="p4322380183334"></a><a name="p4322380183334"></a>createVpnService</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2458604318343"><a name="p2458604318343"></a><a name="p2458604318343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p64799827183417"><a name="p64799827183417"></a><a name="p64799827183417"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p11195029183431"><a name="p11195029183431"></a><a name="p11195029183431"></a>neutron</p>
</td>
</tr>
<tr id="r99d027e2cd6c4a1eb1576aac8148ad5d"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p51205273183318"><a name="p51205273183318"></a><a name="p51205273183318"></a>Updating a VPN</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p64007448183334"><a name="p64007448183334"></a><a name="p64007448183334"></a>updateVpnService</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p515893318343"><a name="p515893318343"></a><a name="p515893318343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p61543187183417"><a name="p61543187183417"></a><a name="p61543187183417"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p41003928183431"><a name="p41003928183431"></a><a name="p41003928183431"></a>neutron</p>
</td>
</tr>
<tr id="r40ec1555fad741718848cffd06ac35e1"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p16115668183318"><a name="p16115668183318"></a><a name="p16115668183318"></a>Deleting a VPN</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p20769318183334"><a name="p20769318183334"></a><a name="p20769318183334"></a>deleteVpnService</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p276635518343"><a name="p276635518343"></a><a name="p276635518343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p36262354183417"><a name="p36262354183417"></a><a name="p36262354183417"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p28419580183431"><a name="p28419580183431"></a><a name="p28419580183431"></a>neutron</p>
</td>
</tr>
<tr id="r5fb034ca80b64164804283b5fab38f74"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p4271206183318"><a name="p4271206183318"></a><a name="p4271206183318"></a>Creating a private key exchange policy</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p41338753183334"><a name="p41338753183334"></a><a name="p41338753183334"></a>createVpnIkepolicy</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p340712718343"><a name="p340712718343"></a><a name="p340712718343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p61473005183417"><a name="p61473005183417"></a><a name="p61473005183417"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p48343834183431"><a name="p48343834183431"></a><a name="p48343834183431"></a>neutron</p>
</td>
</tr>
<tr id="rc8764d9e20c04bf997643057e5b3e6eb"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p26701625183318"><a name="p26701625183318"></a><a name="p26701625183318"></a>Updating a private key exchange policy</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p4071549183334"><a name="p4071549183334"></a><a name="p4071549183334"></a>updateVpnIkepolicy</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p76762718343"><a name="p76762718343"></a><a name="p76762718343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p52208517183417"><a name="p52208517183417"></a><a name="p52208517183417"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p10501911183431"><a name="p10501911183431"></a><a name="p10501911183431"></a>neutron</p>
</td>
</tr>
<tr id="r0a09049f1447471b84694521c069ae3c"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p3914111183318"><a name="p3914111183318"></a><a name="p3914111183318"></a>Deleting an IKE policy specified by the tenant</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p15369331183334"><a name="p15369331183334"></a><a name="p15369331183334"></a>deleteVpnIkepolicy</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2272976418343"><a name="p2272976418343"></a><a name="p2272976418343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p9283655183417"><a name="p9283655183417"></a><a name="p9283655183417"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p5482909183431"><a name="p5482909183431"></a><a name="p5482909183431"></a>neutron</p>
</td>
</tr>
<tr id="r0f576fff66494cc288c9583e41088cd9"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p34815350183318"><a name="p34815350183318"></a><a name="p34815350183318"></a>Creating an IKE policy</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p64171400183334"><a name="p64171400183334"></a><a name="p64171400183334"></a>createVpnIpsecpolicy</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6121794818343"><a name="p6121794818343"></a><a name="p6121794818343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p56898597183417"><a name="p56898597183417"></a><a name="p56898597183417"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p37617823183431"><a name="p37617823183431"></a><a name="p37617823183431"></a>neutron</p>
</td>
</tr>
<tr id="r618b0e4dff0a4d70b41d565cdfb419b6"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p13239582183318"><a name="p13239582183318"></a><a name="p13239582183318"></a>Updating a specified IPsec policy</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p6072678183334"><a name="p6072678183334"></a><a name="p6072678183334"></a>updateVpnIpsecpolicy</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p49010218343"><a name="p49010218343"></a><a name="p49010218343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p5799706183417"><a name="p5799706183417"></a><a name="p5799706183417"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p42976536183431"><a name="p42976536183431"></a><a name="p42976536183431"></a>neutron</p>
</td>
</tr>
<tr id="rb01b2ba9fe6c450c91a85b660d6e00f6"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p55087875183318"><a name="p55087875183318"></a><a name="p55087875183318"></a>Deleting a specified IPsec policy</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p64906240183334"><a name="p64906240183334"></a><a name="p64906240183334"></a>deleteVpnIpsecpolicy</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2174073418343"><a name="p2174073418343"></a><a name="p2174073418343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p127721183417"><a name="p127721183417"></a><a name="p127721183417"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p57164235183431"><a name="p57164235183431"></a><a name="p57164235183431"></a>neutron</p>
</td>
</tr>
<tr id="rc1b5a70512fb4cefab47a3720d3d813a"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p27960568183318"><a name="p27960568183318"></a><a name="p27960568183318"></a>Creating an IPsec connection</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p4899921183334"><a name="p4899921183334"></a><a name="p4899921183334"></a>createVpnIpsec-site-connection</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p1130336518343"><a name="p1130336518343"></a><a name="p1130336518343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p26000350183417"><a name="p26000350183417"></a><a name="p26000350183417"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p65231875183431"><a name="p65231875183431"></a><a name="p65231875183431"></a>neutron</p>
</td>
</tr>
<tr id="rd4b183de162f420a9c7ec23830520ce6"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p49268953183318"><a name="p49268953183318"></a><a name="p49268953183318"></a>Updating an IPsec connection</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p15272732183334"><a name="p15272732183334"></a><a name="p15272732183334"></a>updateVpnIpsec-site-connection</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p5287216818343"><a name="p5287216818343"></a><a name="p5287216818343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p29555594183417"><a name="p29555594183417"></a><a name="p29555594183417"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p40961620183431"><a name="p40961620183431"></a><a name="p40961620183431"></a>neutron</p>
</td>
</tr>
<tr id="rf40174f8be4d415faaf4b68cc7c8d803"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p13824840183318"><a name="p13824840183318"></a><a name="p13824840183318"></a>Deleting a specified IPsec connection</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p60859308183334"><a name="p60859308183334"></a><a name="p60859308183334"></a>deleteVpnIpsec-site-connection</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2332269618343"><a name="p2332269618343"></a><a name="p2332269618343"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p4083082183417"><a name="p4083082183417"></a><a name="p4083082183417"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p64685399183431"><a name="p64685399183431"></a><a name="p64685399183431"></a>neutron</p>
</td>
</tr>
<tr id="r87a556a706ea419797ea30195cbd6ac0"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p6728844183457"><a name="p6728844183457"></a><a name="p6728844183457"></a>Creating an image</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p3994376318353"><a name="p3994376318353"></a><a name="p3994376318353"></a>createImage</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p999088818359"><a name="p999088818359"></a><a name="p999088818359"></a>IMS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p395558418359"><a name="p395558418359"></a><a name="p395558418359"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p57557186183515"><a name="p57557186183515"></a><a name="p57557186183515"></a>glance</p>
</td>
</tr>
<tr id="re148a84d49c44c41ad47fb3e409be78e"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p6380433183457"><a name="p6380433183457"></a><a name="p6380433183457"></a>Modifying information about an image/Uploading an image</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p6086554918353"><a name="p6086554918353"></a><a name="p6086554918353"></a>updateImage</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6504859718359"><a name="p6504859718359"></a><a name="p6504859718359"></a>IMS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p3444500518359"><a name="p3444500518359"></a><a name="p3444500518359"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p16148640183515"><a name="p16148640183515"></a><a name="p16148640183515"></a>glance</p>
</td>
</tr>
<tr id="red3cb70a22844455a6212f80fee267ac"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p20824213183457"><a name="p20824213183457"></a><a name="p20824213183457"></a>Deleting an image</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p1202631218353"><a name="p1202631218353"></a><a name="p1202631218353"></a>deleteImage</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p1169398818359"><a name="p1169398818359"></a><a name="p1169398818359"></a>IMS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p768899918359"><a name="p768899918359"></a><a name="p768899918359"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p28308079183515"><a name="p28308079183515"></a><a name="p28308079183515"></a>glance</p>
</td>
</tr>
<tr id="rc22930c46f0840ba967dcf8d54804040"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p14248219183457"><a name="p14248219183457"></a><a name="p14248219183457"></a>Adding a tag</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p4302917418353"><a name="p4302917418353"></a><a name="p4302917418353"></a>addTag</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p3524473118359"><a name="p3524473118359"></a><a name="p3524473118359"></a>IMS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p3625094518359"><a name="p3625094518359"></a><a name="p3625094518359"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p34168367183515"><a name="p34168367183515"></a><a name="p34168367183515"></a>glance</p>
</td>
</tr>
<tr id="r090d737e2d024cd98d66b9400f7d8051"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p52186926183457"><a name="p52186926183457"></a><a name="p52186926183457"></a>Deleting a tag</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p2842907718353"><a name="p2842907718353"></a><a name="p2842907718353"></a>deleteTag</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p5315603718359"><a name="p5315603718359"></a><a name="p5315603718359"></a>IMS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p1067177018359"><a name="p1067177018359"></a><a name="p1067177018359"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p11351148183515"><a name="p11351148183515"></a><a name="p11351148183515"></a>glance</p>
</td>
</tr>
<tr id="r1380d900d125470fbc43d5ae939afb13"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p60652578183457"><a name="p60652578183457"></a><a name="p60652578183457"></a>Adding an image member</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p5526704518353"><a name="p5526704518353"></a><a name="p5526704518353"></a>addMember</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6220152918359"><a name="p6220152918359"></a><a name="p6220152918359"></a>IMS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p515909418359"><a name="p515909418359"></a><a name="p515909418359"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p20596985183515"><a name="p20596985183515"></a><a name="p20596985183515"></a>glance</p>
</td>
</tr>
<tr id="re370b20fe57a464dbc4728589000e16a"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p58096976183457"><a name="p58096976183457"></a><a name="p58096976183457"></a>Modifying information about an image member</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p2435755418353"><a name="p2435755418353"></a><a name="p2435755418353"></a>updateMember</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p288366718359"><a name="p288366718359"></a><a name="p288366718359"></a>IMS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p3225046618359"><a name="p3225046618359"></a><a name="p3225046618359"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p49926066183515"><a name="p49926066183515"></a><a name="p49926066183515"></a>glance</p>
</td>
</tr>
<tr id="rd7ca5735ca644a3cbc6de1258ced170b"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p7002845183457"><a name="p7002845183457"></a><a name="p7002845183457"></a>Deleting an image member</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p3991713518353"><a name="p3991713518353"></a><a name="p3991713518353"></a>deleteMember</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p2248789618359"><a name="p2248789618359"></a><a name="p2248789618359"></a>IMS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p958027618359"><a name="p958027618359"></a><a name="p958027618359"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p23098169183515"><a name="p23098169183515"></a><a name="p23098169183515"></a>glance</p>
</td>
</tr>
<tr id="r478349bdcf9c455985f989a0013a6ff4"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p33580995183526"><a name="p33580995183526"></a><a name="p33580995183526"></a>Creating a configuration</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p34325781183559"><a name="p34325781183559"></a><a name="p34325781183559"></a>createSoftwareConfigs</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p16571327183549"><a name="p16571327183549"></a><a name="p16571327183549"></a>RTS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p100265183549"><a name="p100265183549"></a><a name="p100265183549"></a>software_configs</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p29745683183611"><a name="p29745683183611"></a><a name="p29745683183611"></a>heat</p>
</td>
</tr>
<tr id="rc06040e11231493db219bb2552446ebd"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p52919190183526"><a name="p52919190183526"></a><a name="p52919190183526"></a>Deleting a configuration</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p58997489183559"><a name="p58997489183559"></a><a name="p58997489183559"></a>deleteSoftwareConfigs</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p5984595183549"><a name="p5984595183549"></a><a name="p5984595183549"></a>RTS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p14990211183549"><a name="p14990211183549"></a><a name="p14990211183549"></a>software_configs</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p8439859183611"><a name="p8439859183611"></a><a name="p8439859183611"></a>heat</p>
</td>
</tr>
<tr id="r8c98ec4a9b4745d8a2f9a3888306b6c2"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p57602122183526"><a name="p57602122183526"></a><a name="p57602122183526"></a>Creating a deployment</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p59496647183559"><a name="p59496647183559"></a><a name="p59496647183559"></a>createSoftwareDeployments</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p56228365183549"><a name="p56228365183549"></a><a name="p56228365183549"></a>RTS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p58203677183549"><a name="p58203677183549"></a><a name="p58203677183549"></a>software_deployments</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p45750736183611"><a name="p45750736183611"></a><a name="p45750736183611"></a>heat</p>
</td>
</tr>
<tr id="rdb0eebde3efb4904a1eced1d22d22cda"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p48907064183526"><a name="p48907064183526"></a><a name="p48907064183526"></a>Deleting a deployment</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p20730044183559"><a name="p20730044183559"></a><a name="p20730044183559"></a>deleteSoftwareDeployments</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p17678600183549"><a name="p17678600183549"></a><a name="p17678600183549"></a>RTS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p22680482183549"><a name="p22680482183549"></a><a name="p22680482183549"></a>software_deployments</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p66290365183611"><a name="p66290365183611"></a><a name="p66290365183611"></a>heat</p>
</td>
</tr>
<tr id="r2fafe801d2444fdabdc33bdc1907c459"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p18443397183526"><a name="p18443397183526"></a><a name="p18443397183526"></a>Updating a deployment</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p12707962183559"><a name="p12707962183559"></a><a name="p12707962183559"></a>updateSoftwareDeployments</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p25291370183549"><a name="p25291370183549"></a><a name="p25291370183549"></a>RTS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p35335113183549"><a name="p35335113183549"></a><a name="p35335113183549"></a>software_deployments</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p7294678183611"><a name="p7294678183611"></a><a name="p7294678183611"></a>heat</p>
</td>
</tr>
<tr id="r9cc827047e7841bfb1578fbac2d0dfe5"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p23463899183526"><a name="p23463899183526"></a><a name="p23463899183526"></a>Stack management actions, such as canceling stack update or checking stack resources</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p3081204183559"><a name="p3081204183559"></a><a name="p3081204183559"></a>createStacksActions</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p56602785183549"><a name="p56602785183549"></a><a name="p56602785183549"></a>RTS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p21422862183549"><a name="p21422862183549"></a><a name="p21422862183549"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p16220349183611"><a name="p16220349183611"></a><a name="p16220349183611"></a>heat</p>
</td>
</tr>
<tr id="ref87009eead2448d8af469de90f2c3f9"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p59531053183526"><a name="p59531053183526"></a><a name="p59531053183526"></a>Sending a signal to resources in a stack</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p31605285183559"><a name="p31605285183559"></a><a name="p31605285183559"></a>createStacksResourcesSignal</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p48010145183549"><a name="p48010145183549"></a><a name="p48010145183549"></a>RTS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p63616502183549"><a name="p63616502183549"></a><a name="p63616502183549"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p13474460183611"><a name="p13474460183611"></a><a name="p13474460183611"></a>heat</p>
</td>
</tr>
<tr id="r0c9220d638044049a199f98b57266f0b"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p45811574183526"><a name="p45811574183526"></a><a name="p45811574183526"></a>Creating a stack</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p21912528183559"><a name="p21912528183559"></a><a name="p21912528183559"></a>createStacks</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p4205094183549"><a name="p4205094183549"></a><a name="p4205094183549"></a>RTS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p5068366183549"><a name="p5068366183549"></a><a name="p5068366183549"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p24987880183611"><a name="p24987880183611"></a><a name="p24987880183611"></a>heat</p>
</td>
</tr>
<tr id="rf479d5767e0043af8959f4883706147d"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p43532153183526"><a name="p43532153183526"></a><a name="p43532153183526"></a>Deleting a stack</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p2323520183559"><a name="p2323520183559"></a><a name="p2323520183559"></a>deleteStacks</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p3851511183549"><a name="p3851511183549"></a><a name="p3851511183549"></a>RTS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p43537003183549"><a name="p43537003183549"></a><a name="p43537003183549"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p29663003183611"><a name="p29663003183611"></a><a name="p29663003183611"></a>heat</p>
</td>
</tr>
<tr id="r6c958a7ba08e4ababefb6120af91d8bb"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p59555969183526"><a name="p59555969183526"></a><a name="p59555969183526"></a>Updating a stack</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p16124937183559"><a name="p16124937183559"></a><a name="p16124937183559"></a>updateStacks</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p63091744183549"><a name="p63091744183549"></a><a name="p63091744183549"></a>RTS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p10157674183549"><a name="p10157674183549"></a><a name="p10157674183549"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p15275641183611"><a name="p15275641183611"></a><a name="p15275641183611"></a>heat</p>
</td>
</tr>
<tr id="r248e5bc248a544fdb34ef08843e11d7f"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p63975714183526"><a name="p63975714183526"></a><a name="p63975714183526"></a>Previewing a stack</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p11027908183559"><a name="p11027908183559"></a><a name="p11027908183559"></a>createStacksPreview</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p22969911183549"><a name="p22969911183549"></a><a name="p22969911183549"></a>RTS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p48623473183549"><a name="p48623473183549"></a><a name="p48623473183549"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p62979787183611"><a name="p62979787183611"></a><a name="p62979787183611"></a>heat</p>
</td>
</tr>
<tr id="r31d1fa5e715742cdabdc9294a1cfa889"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p64743925183526"><a name="p64743925183526"></a><a name="p64743925183526"></a>Identifying a resource as unhealthy</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p53390550183559"><a name="p53390550183559"></a><a name="p53390550183559"></a>patchStacksResource</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p13031831183549"><a name="p13031831183549"></a><a name="p13031831183549"></a>RTS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p48945387183549"><a name="p48945387183549"></a><a name="p48945387183549"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p9802021183611"><a name="p9802021183611"></a><a name="p9802021183611"></a>heat</p>
</td>
</tr>
<tr id="r97348ef3bfb2402b9f9df6499ee959ff"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p20790367183526"><a name="p20790367183526"></a><a name="p20790367183526"></a>Validating a template</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p65678889183559"><a name="p65678889183559"></a><a name="p65678889183559"></a>createValidate</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p46380966183549"><a name="p46380966183549"></a><a name="p46380966183549"></a>RTS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p65870799183549"><a name="p65870799183549"></a><a name="p65870799183549"></a>validate</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p32134307183611"><a name="p32134307183611"></a><a name="p32134307183611"></a>heat</p>
</td>
</tr>
<tr id="raa1069af63ac407284946e15be7493ac"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p39521842183659"><a name="p39521842183659"></a><a name="p39521842183659"></a>Creating a backup</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p14046159183955"><a name="p14046159183955"></a><a name="p14046159183955"></a>createBackup</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p60325865184017"><a name="p60325865184017"></a><a name="p60325865184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p36356653184051"><a name="p36356653184051"></a><a name="p36356653184051"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p39654770184115"><a name="p39654770184115"></a><a name="p39654770184115"></a>Cinder</p>
</td>
</tr>
<tr id="r6f2cafb0b03240cf98cf826afd16adfe"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p21720607183659"><a name="p21720607183659"></a><a name="p21720607183659"></a>Importing volume backup information</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p39102812183955"><a name="p39102812183955"></a><a name="p39102812183955"></a>import_recordBackup</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p21250087184017"><a name="p21250087184017"></a><a name="p21250087184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p63108180184051"><a name="p63108180184051"></a><a name="p63108180184051"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p51516335184115"><a name="p51516335184115"></a><a name="p51516335184115"></a>Cinder</p>
</td>
</tr>
<tr id="rf59ab8b429114c9e8c5ff7eb72e1cd0f"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p63739942183659"><a name="p63739942183659"></a><a name="p63739942183659"></a>Restoring a volume backup</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p51791784183955"><a name="p51791784183955"></a><a name="p51791784183955"></a>restoreBackup</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p56275342184017"><a name="p56275342184017"></a><a name="p56275342184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p36291791184051"><a name="p36291791184051"></a><a name="p36291791184051"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p41553525184115"><a name="p41553525184115"></a><a name="p41553525184115"></a>Cinder</p>
</td>
</tr>
<tr id="r10e9bd64595e420cafe6637e3fa31f2e"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p27084435183659"><a name="p27084435183659"></a><a name="p27084435183659"></a>Deleting a backup</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p41029174183955"><a name="p41029174183955"></a><a name="p41029174183955"></a>deleteBackup</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p21208631184017"><a name="p21208631184017"></a><a name="p21208631184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p15823577184051"><a name="p15823577184051"></a><a name="p15823577184051"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p26422199184115"><a name="p26422199184115"></a><a name="p26422199184115"></a>Cinder</p>
</td>
</tr>
<tr id="r03e8581b70a54e489747d80fa96fe51c"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p14547191183659"><a name="p14547191183659"></a><a name="p14547191183659"></a>Deleting a consistent group of snapshots</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p46823697183955"><a name="p46823697183955"></a><a name="p46823697183955"></a>deleteCgsnapshot</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p26053895184017"><a name="p26053895184017"></a><a name="p26053895184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p59772277184051"><a name="p59772277184051"></a><a name="p59772277184051"></a>cgsnapshot</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p1539184184115"><a name="p1539184184115"></a><a name="p1539184184115"></a>Cinder</p>
</td>
</tr>
<tr id="r819f92c66f8641e8a9d12cc550597302"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p1702127183659"><a name="p1702127183659"></a><a name="p1702127183659"></a>Creating a consistent group of snapshots</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p43172749183955"><a name="p43172749183955"></a><a name="p43172749183955"></a>createCgsnapshot</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p1481320184017"><a name="p1481320184017"></a><a name="p1481320184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p20337711184051"><a name="p20337711184051"></a><a name="p20337711184051"></a>cgsnapshot</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p48323427184115"><a name="p48323427184115"></a><a name="p48323427184115"></a>Cinder</p>
</td>
</tr>
<tr id="r4d7c000cb34142e2bcdc23d0074fbf49"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p32891100183659"><a name="p32891100183659"></a><a name="p32891100183659"></a>Creating a consistent group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p65985795183955"><a name="p65985795183955"></a><a name="p65985795183955"></a>createConsistencygroup</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6140685184017"><a name="p6140685184017"></a><a name="p6140685184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p62241240184051"><a name="p62241240184051"></a><a name="p62241240184051"></a>consistencygroup</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p62733787184115"><a name="p62733787184115"></a><a name="p62733787184115"></a>Cinder</p>
</td>
</tr>
<tr id="r30ba69266fe14e798ad275eedc84da86"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p19748011183659"><a name="p19748011183659"></a><a name="p19748011183659"></a>Deleting a consistent group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p53698456183955"><a name="p53698456183955"></a><a name="p53698456183955"></a>deleteConsistencygroup</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p47374513184017"><a name="p47374513184017"></a><a name="p47374513184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p8272204184051"><a name="p8272204184051"></a><a name="p8272204184051"></a>consistencygroup</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p31794796184115"><a name="p31794796184115"></a><a name="p31794796184115"></a>Cinder</p>
</td>
</tr>
<tr id="r1dbee01921bf4ba1931a7ebf07a16362"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p35003534183659"><a name="p35003534183659"></a><a name="p35003534183659"></a>Updating a consistent group</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p21706998183955"><a name="p21706998183955"></a><a name="p21706998183955"></a>updateConsistencygroup</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p42064087184017"><a name="p42064087184017"></a><a name="p42064087184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p57748527184051"><a name="p57748527184051"></a><a name="p57748527184051"></a>consistencygroup</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p25848239184115"><a name="p25848239184115"></a><a name="p25848239184115"></a>Cinder</p>
</td>
</tr>
<tr id="r954876cd16f94a1d9df0f4ee6ddd4b99"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p16208320183659"><a name="p16208320183659"></a><a name="p16208320183659"></a>Updating the quota level of a tenant</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p53818640183955"><a name="p53818640183955"></a><a name="p53818640183955"></a>updateQuota-class</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p63077770184017"><a name="p63077770184017"></a><a name="p63077770184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p21418923184051"><a name="p21418923184051"></a><a name="p21418923184051"></a>quota-class</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p52884745184115"><a name="p52884745184115"></a><a name="p52884745184115"></a>Cinder</p>
</td>
</tr>
<tr id="rb4b0c26e3135485e87b75ea5e51c1d8e"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p4705604183659"><a name="p4705604183659"></a><a name="p4705604183659"></a>Updating the quota of a tenant</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p42212065183955"><a name="p42212065183955"></a><a name="p42212065183955"></a>updateQuota</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p14123038184017"><a name="p14123038184017"></a><a name="p14123038184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p45138739184051"><a name="p45138739184051"></a><a name="p45138739184051"></a>quota</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p32491364184115"><a name="p32491364184115"></a><a name="p32491364184115"></a>Cinder</p>
</td>
</tr>
<tr id="r02bb3b3b62584cfba1f0181f45bb9ff2"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p7833766183659"><a name="p7833766183659"></a><a name="p7833766183659"></a>Creating a volume transfer</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p36735788183955"><a name="p36735788183955"></a><a name="p36735788183955"></a>createVolume-transfer</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p28038636184017"><a name="p28038636184017"></a><a name="p28038636184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p22797634184051"><a name="p22797634184051"></a><a name="p22797634184051"></a>volume-transfer</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p63884274184115"><a name="p63884274184115"></a><a name="p63884274184115"></a>Cinder</p>
</td>
</tr>
<tr id="rc095daecb69044faa160142b71c78eb5"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p6561975183659"><a name="p6561975183659"></a><a name="p6561975183659"></a>Deleting a volume transfer</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p3952956183955"><a name="p3952956183955"></a><a name="p3952956183955"></a>deleteVolume-transfer</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p39071513184017"><a name="p39071513184017"></a><a name="p39071513184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p43586075184051"><a name="p43586075184051"></a><a name="p43586075184051"></a>volume-transfer</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p65193713184115"><a name="p65193713184115"></a><a name="p65193713184115"></a>Cinder</p>
</td>
</tr>
<tr id="rabfb8cfa774c4774b435b803078360ab"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p18950739183659"><a name="p18950739183659"></a><a name="p18950739183659"></a>Accepting a volume transfer</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p63133093183955"><a name="p63133093183955"></a><a name="p63133093183955"></a>acceptVolume-transfer</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p28974927184017"><a name="p28974927184017"></a><a name="p28974927184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p31756425184051"><a name="p31756425184051"></a><a name="p31756425184051"></a>volume-transfer</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p13141089184115"><a name="p13141089184115"></a><a name="p13141089184115"></a>Cinder</p>
</td>
</tr>
<tr id="rfdd6901487664098bd65916cf2825fa5"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p57772318183659"><a name="p57772318183659"></a><a name="p57772318183659"></a>Creating qos-specs</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p54452992183955"><a name="p54452992183955"></a><a name="p54452992183955"></a>createQos-specs</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p50538625184017"><a name="p50538625184017"></a><a name="p50538625184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p64985248184051"><a name="p64985248184051"></a><a name="p64985248184051"></a>qos-specs</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p50395342184115"><a name="p50395342184115"></a><a name="p50395342184115"></a>Cinder</p>
</td>
</tr>
<tr id="rda9b560007c64c6ca30924a71b0f7b72"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p38762562183659"><a name="p38762562183659"></a><a name="p38762562183659"></a>Deleting qos-specs</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p34892978183955"><a name="p34892978183955"></a><a name="p34892978183955"></a>deleteQos-specs</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p67000234184017"><a name="p67000234184017"></a><a name="p67000234184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p62496889184051"><a name="p62496889184051"></a><a name="p62496889184051"></a>qos-specs</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p29656075184115"><a name="p29656075184115"></a><a name="p29656075184115"></a>Cinder</p>
</td>
</tr>
<tr id="r5f205e00735d4cef84a6615f5d0df34c"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p5076274183659"><a name="p5076274183659"></a><a name="p5076274183659"></a>Creating a snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p2721701183955"><a name="p2721701183955"></a><a name="p2721701183955"></a>createSnapshot</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p55026573184017"><a name="p55026573184017"></a><a name="p55026573184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p60422905184051"><a name="p60422905184051"></a><a name="p60422905184051"></a>snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p10225140184115"><a name="p10225140184115"></a><a name="p10225140184115"></a>Cinder</p>
</td>
</tr>
<tr id="r2be44893f4c44a07878d7c625f750b50"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p9616489183659"><a name="p9616489183659"></a><a name="p9616489183659"></a>Adding pieces of snapshot metadata</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p37963019183955"><a name="p37963019183955"></a><a name="p37963019183955"></a>createSnapshotMetadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p50380149184017"><a name="p50380149184017"></a><a name="p50380149184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p24883338184051"><a name="p24883338184051"></a><a name="p24883338184051"></a>snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p5043499184115"><a name="p5043499184115"></a><a name="p5043499184115"></a>Cinder</p>
</td>
</tr>
<tr id="rac366a361aec4f59a1ad3ed57b625ca8"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p31098922183659"><a name="p31098922183659"></a><a name="p31098922183659"></a>Forcibly deleting a snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p26189602183955"><a name="p26189602183955"></a><a name="p26189602183955"></a>force_deleteSnapshot</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p18580470184017"><a name="p18580470184017"></a><a name="p18580470184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p20560351184051"><a name="p20560351184051"></a><a name="p20560351184051"></a>snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p52832218184115"><a name="p52832218184115"></a><a name="p52832218184115"></a>Cinder</p>
</td>
</tr>
<tr id="rc4f67a63afb748779b75f2a072dfa5df"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p55427392183659"><a name="p55427392183659"></a><a name="p55427392183659"></a>Deleting a snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p33302506183955"><a name="p33302506183955"></a><a name="p33302506183955"></a>deleteSnapshot</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p56281001184017"><a name="p56281001184017"></a><a name="p56281001184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p23219379184051"><a name="p23219379184051"></a><a name="p23219379184051"></a>snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p61308534184115"><a name="p61308534184115"></a><a name="p61308534184115"></a>Cinder</p>
</td>
</tr>
<tr id="r155f6fbc6fa04ffe8b5523ed6083b0c5"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p7033279183659"><a name="p7033279183659"></a><a name="p7033279183659"></a>Deleting a single piece of snapshot metadata</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p51227119183955"><a name="p51227119183955"></a><a name="p51227119183955"></a>deleteSnapshotSingleMetadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p25334259184017"><a name="p25334259184017"></a><a name="p25334259184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p15493769184051"><a name="p15493769184051"></a><a name="p15493769184051"></a>snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p66527353184115"><a name="p66527353184115"></a><a name="p66527353184115"></a>Cinder</p>
</td>
</tr>
<tr id="r9a17cf925d244178ae8f9b1fceab99c8"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p26986944183659"><a name="p26986944183659"></a><a name="p26986944183659"></a>Updating snapshot information</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p32041732183955"><a name="p32041732183955"></a><a name="p32041732183955"></a>updateSnapshot</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p13737406184017"><a name="p13737406184017"></a><a name="p13737406184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p20668780184051"><a name="p20668780184051"></a><a name="p20668780184051"></a>snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p45841191184115"><a name="p45841191184115"></a><a name="p45841191184115"></a>Cinder</p>
</td>
</tr>
<tr id="rd7cfdb8213fd4e8aa56dfbee0bbc5496"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p10585640183659"><a name="p10585640183659"></a><a name="p10585640183659"></a>Replacing pieces of snapshot metadata</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p4538629183955"><a name="p4538629183955"></a><a name="p4538629183955"></a>updateSnapshotMetadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p15348284184017"><a name="p15348284184017"></a><a name="p15348284184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p35155632184051"><a name="p35155632184051"></a><a name="p35155632184051"></a>snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p65122889184115"><a name="p65122889184115"></a><a name="p65122889184115"></a>Cinder</p>
</td>
</tr>
<tr id="r58463d8f4d404556a8bd6d4a029c513d"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p66521441183659"><a name="p66521441183659"></a><a name="p66521441183659"></a>Updating a single piece of snapshot metadata</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p20326548183955"><a name="p20326548183955"></a><a name="p20326548183955"></a>updateSnapshotSingleMetadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p48828331184017"><a name="p48828331184017"></a><a name="p48828331184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p59978670184051"><a name="p59978670184051"></a><a name="p59978670184051"></a>snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p28619507184115"><a name="p28619507184115"></a><a name="p28619507184115"></a>Cinder</p>
</td>
</tr>
<tr id="rb449da6fe68848b688798d85c6006e72"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p41530910183659"><a name="p41530910183659"></a><a name="p41530910183659"></a>Rolling back a snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p54103515183955"><a name="p54103515183955"></a><a name="p54103515183955"></a>rollbackSnapshot</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p28155403184017"><a name="p28155403184017"></a><a name="p28155403184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p36580491184051"><a name="p36580491184051"></a><a name="p36580491184051"></a>snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p59873345184115"><a name="p59873345184115"></a><a name="p59873345184115"></a>Cinder</p>
</td>
</tr>
<tr id="r92b40f3e71ac4469bdfffc81ab62e4ad"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p9935898183659"><a name="p9935898183659"></a><a name="p9935898183659"></a>Activating a snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p48559951183955"><a name="p48559951183955"></a><a name="p48559951183955"></a>activeSnapshot</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p57085416184017"><a name="p57085416184017"></a><a name="p57085416184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p24959217184051"><a name="p24959217184051"></a><a name="p24959217184051"></a>snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p26907157184115"><a name="p26907157184115"></a><a name="p26907157184115"></a>Cinder</p>
</td>
</tr>
<tr id="r3e49dc28f8634d35bc2eeb5e5207597e"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p62621400183659"><a name="p62621400183659"></a><a name="p62621400183659"></a>Creating a volume type</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p33833578183955"><a name="p33833578183955"></a><a name="p33833578183955"></a>createType</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p7772949184017"><a name="p7772949184017"></a><a name="p7772949184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p8767187184051"><a name="p8767187184051"></a><a name="p8767187184051"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p19529177184115"><a name="p19529177184115"></a><a name="p19529177184115"></a>Cinder</p>
</td>
</tr>
<tr id="r4bea206073ea4565b1bbd3d05ccee1e1"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p16973411183659"><a name="p16973411183659"></a><a name="p16973411183659"></a>Creating extra specifications for a volume type</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p35725936183955"><a name="p35725936183955"></a><a name="p35725936183955"></a>createTypeExtra-specs</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p29335918184017"><a name="p29335918184017"></a><a name="p29335918184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p15937324184051"><a name="p15937324184051"></a><a name="p15937324184051"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p9691458184115"><a name="p9691458184115"></a><a name="p9691458184115"></a>Cinder</p>
</td>
</tr>
<tr id="r0a9e2bcd66014d5fb2813b341b062894"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p25586191183659"><a name="p25586191183659"></a><a name="p25586191183659"></a>Deleting a volume type</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p5968170183955"><a name="p5968170183955"></a><a name="p5968170183955"></a>deleteType</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p45265813184017"><a name="p45265813184017"></a><a name="p45265813184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p8475839184051"><a name="p8475839184051"></a><a name="p8475839184051"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p18642698184115"><a name="p18642698184115"></a><a name="p18642698184115"></a>Cinder</p>
</td>
</tr>
<tr id="rc4205633d9734fd384c4dc49449317f1"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p63178037183659"><a name="p63178037183659"></a><a name="p63178037183659"></a>Creating a volume</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p55828908183955"><a name="p55828908183955"></a><a name="p55828908183955"></a>createVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p48325556184017"><a name="p48325556184017"></a><a name="p48325556184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p4871383184051"><a name="p4871383184051"></a><a name="p4871383184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p34536884184115"><a name="p34536884184115"></a><a name="p34536884184115"></a>Cinder</p>
</td>
</tr>
<tr id="r550cf0340a604774ba1099f9465db7cd"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p20108794183659"><a name="p20108794183659"></a><a name="p20108794183659"></a>Adding pieces of volume metadata</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p31302930183955"><a name="p31302930183955"></a><a name="p31302930183955"></a>createVolumeMetadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p64286272184017"><a name="p64286272184017"></a><a name="p64286272184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p61577736184051"><a name="p61577736184051"></a><a name="p61577736184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p11565132184115"><a name="p11565132184115"></a><a name="p11565132184115"></a>Cinder</p>
</td>
</tr>
<tr id="rab03852b9f664724addf8b597292428c"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p29578760183659"><a name="p29578760183659"></a><a name="p29578760183659"></a>Forcibly deleting a volume</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p2822462183955"><a name="p2822462183955"></a><a name="p2822462183955"></a>force_deleteVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p22705843184017"><a name="p22705843184017"></a><a name="p22705843184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p61448427184051"><a name="p61448427184051"></a><a name="p61448427184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p42373411184115"><a name="p42373411184115"></a><a name="p42373411184115"></a>Cinder</p>
</td>
</tr>
<tr id="rc9492fcc285d4df0921893a7d6534e8d"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p20970834183659"><a name="p20970834183659"></a><a name="p20970834183659"></a>Attaching a volume</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p44308890183955"><a name="p44308890183955"></a><a name="p44308890183955"></a>attachVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p43779665184017"><a name="p43779665184017"></a><a name="p43779665184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p34291429184051"><a name="p34291429184051"></a><a name="p34291429184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p20139670184115"><a name="p20139670184115"></a><a name="p20139670184115"></a>Cinder</p>
</td>
</tr>
<tr id="r76b2bf3faa34452d9de4ce2cf3d48b79"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p54025939183659"><a name="p54025939183659"></a><a name="p54025939183659"></a>Detaching a volume</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p21817819183955"><a name="p21817819183955"></a><a name="p21817819183955"></a>detachVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p38665443184017"><a name="p38665443184017"></a><a name="p38665443184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p33954528184051"><a name="p33954528184051"></a><a name="p33954528184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p52087238184115"><a name="p52087238184115"></a><a name="p52087238184115"></a>Cinder</p>
</td>
</tr>
<tr id="r03f633617a024ed18e10ba96055fc67d"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p59115342183659"><a name="p59115342183659"></a><a name="p59115342183659"></a>Reserving a volume</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p389819183955"><a name="p389819183955"></a><a name="p389819183955"></a>reserveVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p1385341184017"><a name="p1385341184017"></a><a name="p1385341184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p56789006184051"><a name="p56789006184051"></a><a name="p56789006184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p55088992184115"><a name="p55088992184115"></a><a name="p55088992184115"></a>Cinder</p>
</td>
</tr>
<tr id="rc412cf0ca8ee4581834591a0ab2621d2"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p11193870183659"><a name="p11193870183659"></a><a name="p11193870183659"></a>Pre-detaching a volume</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p15743165183955"><a name="p15743165183955"></a><a name="p15743165183955"></a>begin_detachingVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p3281211184017"><a name="p3281211184017"></a><a name="p3281211184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p60125869184051"><a name="p60125869184051"></a><a name="p60125869184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p28774998184115"><a name="p28774998184115"></a><a name="p28774998184115"></a>Cinder</p>
</td>
</tr>
<tr id="r33edf25a9ca04c508faee17bb615c6ef"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p40159143183659"><a name="p40159143183659"></a><a name="p40159143183659"></a>Rolling back the volume pre-detaching</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p1152237183955"><a name="p1152237183955"></a><a name="p1152237183955"></a>roll_detachingVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p43192831184017"><a name="p43192831184017"></a><a name="p43192831184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p9670333184051"><a name="p9670333184051"></a><a name="p9670333184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p39008419184115"><a name="p39008419184115"></a><a name="p39008419184115"></a>Cinder</p>
</td>
</tr>
<tr id="r511583c0dcdb4a8cb7f522210adbcb44"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p16550578183659"><a name="p16550578183659"></a><a name="p16550578183659"></a>Initializing the connection for attaching a volume</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p34674588183955"><a name="p34674588183955"></a><a name="p34674588183955"></a>initialize_connectionVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p13516595184017"><a name="p13516595184017"></a><a name="p13516595184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p3242186184051"><a name="p3242186184051"></a><a name="p3242186184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p50088458184115"><a name="p50088458184115"></a><a name="p50088458184115"></a>Cinder</p>
</td>
</tr>
<tr id="ra3b84e04546b4a36a2440bda9553acbe"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p52885140183659"><a name="p52885140183659"></a><a name="p52885140183659"></a>Terminating the connection for detaching a volume</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p44842279183955"><a name="p44842279183955"></a><a name="p44842279183955"></a>terminate_connectionVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p55704204184017"><a name="p55704204184017"></a><a name="p55704204184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p14743719184051"><a name="p14743719184051"></a><a name="p14743719184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p7264471184115"><a name="p7264471184115"></a><a name="p7264471184115"></a>Cinder</p>
</td>
</tr>
<tr id="r1f8df1bda938447b843ed7dd2e214518"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p32779319183659"><a name="p32779319183659"></a><a name="p32779319183659"></a>Uploading a volume image</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p8004783183955"><a name="p8004783183955"></a><a name="p8004783183955"></a>Upload_imageVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p7502532184017"><a name="p7502532184017"></a><a name="p7502532184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p10753584184051"><a name="p10753584184051"></a><a name="p10753584184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p61308059184115"><a name="p61308059184115"></a><a name="p61308059184115"></a>Cinder</p>
</td>
</tr>
<tr id="rf2585b68300c45958537925932a09e1f"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p5368013183659"><a name="p5368013183659"></a><a name="p5368013183659"></a>Expanding the capacity of a volume</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p64125153183955"><a name="p64125153183955"></a><a name="p64125153183955"></a>extendVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p33528414184017"><a name="p33528414184017"></a><a name="p33528414184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p54734855184051"><a name="p54734855184051"></a><a name="p54734855184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p66180851184115"><a name="p66180851184115"></a><a name="p66180851184115"></a>Cinder</p>
</td>
</tr>
<tr id="rc935099121124a769a54608c60244680"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p20968084183659"><a name="p20968084183659"></a><a name="p20968084183659"></a>Unreserving a volume</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p39467695183955"><a name="p39467695183955"></a><a name="p39467695183955"></a>unreserveVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p14588006184017"><a name="p14588006184017"></a><a name="p14588006184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p39044182184051"><a name="p39044182184051"></a><a name="p39044182184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p61676096184115"><a name="p61676096184115"></a><a name="p61676096184115"></a>Cinder</p>
</td>
</tr>
<tr id="r840707860fd94e3cb68536bacf0c2753"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p52021132183659"><a name="p52021132183659"></a><a name="p52021132183659"></a>Setting the state of a volume to read-only</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p49356308183955"><a name="p49356308183955"></a><a name="p49356308183955"></a>update_readonly_flagVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p31456045184017"><a name="p31456045184017"></a><a name="p31456045184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p9051026184051"><a name="p9051026184051"></a><a name="p9051026184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p66044527184115"><a name="p66044527184115"></a><a name="p66044527184115"></a>Cinder</p>
</td>
</tr>
<tr id="r7bf5990584d84d979f3db60c99522cdc"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p6897217183659"><a name="p6897217183659"></a><a name="p6897217183659"></a>Changing the type of a volume</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p10397907183955"><a name="p10397907183955"></a><a name="p10397907183955"></a>retypeVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p47334672184017"><a name="p47334672184017"></a><a name="p47334672184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p21529909184051"><a name="p21529909184051"></a><a name="p21529909184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p29405106184115"><a name="p29405106184115"></a><a name="p29405106184115"></a>Cinder</p>
</td>
</tr>
<tr id="r99a6051c8ea44135b53333aedcfb6232"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p62015622183659"><a name="p62015622183659"></a><a name="p62015622183659"></a>Setting the state of a volume to bootable</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p63882040183955"><a name="p63882040183955"></a><a name="p63882040183955"></a>set_bootableVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p13019952184017"><a name="p13019952184017"></a><a name="p13019952184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p58939011184051"><a name="p58939011184051"></a><a name="p58939011184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p28595012184115"><a name="p28595012184115"></a><a name="p28595012184115"></a>Cinder</p>
</td>
</tr>
<tr id="r6d1385d15aea4cd89b2f5b84ce233227"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p45123639183659"><a name="p45123639183659"></a><a name="p45123639183659"></a>Deleting a volume</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p63564500183955"><a name="p63564500183955"></a><a name="p63564500183955"></a>deleteVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p29195834184017"><a name="p29195834184017"></a><a name="p29195834184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p16866117184051"><a name="p16866117184051"></a><a name="p16866117184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p42016296184115"><a name="p42016296184115"></a><a name="p42016296184115"></a>Cinder</p>
</td>
</tr>
<tr id="ra8d3508cf20846cfae1f48bfcc067c5e"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p11789814183659"><a name="p11789814183659"></a><a name="p11789814183659"></a>Deleting a single piece of volume metadata</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p33404740183955"><a name="p33404740183955"></a><a name="p33404740183955"></a>deleteVolumeSingleMetadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p10253600184017"><a name="p10253600184017"></a><a name="p10253600184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p14477455184051"><a name="p14477455184051"></a><a name="p14477455184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p28238314184115"><a name="p28238314184115"></a><a name="p28238314184115"></a>Cinder</p>
</td>
</tr>
<tr id="r950e8d086d9849579aa8fffbe801bbfb"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p4839917183659"><a name="p4839917183659"></a><a name="p4839917183659"></a>Updating a volume</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p58646761183955"><a name="p58646761183955"></a><a name="p58646761183955"></a>updateVolume</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p25790941184017"><a name="p25790941184017"></a><a name="p25790941184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p17973629184051"><a name="p17973629184051"></a><a name="p17973629184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p50418523184115"><a name="p50418523184115"></a><a name="p50418523184115"></a>Cinder</p>
</td>
</tr>
<tr id="r124a2ecc9092430986db9f531530f4a8"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p38639249183659"><a name="p38639249183659"></a><a name="p38639249183659"></a>Replacing pieces of volume metadata</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p5142960183955"><a name="p5142960183955"></a><a name="p5142960183955"></a>updateVolumeMetadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p11114548184017"><a name="p11114548184017"></a><a name="p11114548184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p16547313184051"><a name="p16547313184051"></a><a name="p16547313184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p46554967184115"><a name="p46554967184115"></a><a name="p46554967184115"></a>Cinder</p>
</td>
</tr>
<tr id="r53deb3f113fd44659e20f06fec5c7978"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p49399132183659"><a name="p49399132183659"></a><a name="p49399132183659"></a>Updating a single piece of volume metadata</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p58230731183955"><a name="p58230731183955"></a><a name="p58230731183955"></a>updateVolumeSingleMetadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p49442417184017"><a name="p49442417184017"></a><a name="p49442417184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p50504533184051"><a name="p50504533184051"></a><a name="p50504533184051"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p48595330184115"><a name="p48595330184115"></a><a name="p48595330184115"></a>Cinder</p>
</td>
</tr>
<tr id="rbd8bb59d1ac1462e971603e7fa0a93e1"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p41616786183659"><a name="p41616786183659"></a><a name="p41616786183659"></a>Creating volume tags</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p37401205183955"><a name="p37401205183955"></a><a name="p37401205183955"></a>createVolume-tags</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p6062117184017"><a name="p6062117184017"></a><a name="p6062117184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p42147678184051"><a name="p42147678184051"></a><a name="p42147678184051"></a>volume-tags</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p59624710184115"><a name="p59624710184115"></a><a name="p59624710184115"></a>Cinder</p>
</td>
</tr>
<tr id="r4d6a00cad078451d9338278cd53df745"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p5430524183659"><a name="p5430524183659"></a><a name="p5430524183659"></a>Updating volume tags</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p19280049183955"><a name="p19280049183955"></a><a name="p19280049183955"></a>updateVolume-tags</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p57207533184017"><a name="p57207533184017"></a><a name="p57207533184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p56906950184051"><a name="p56906950184051"></a><a name="p56906950184051"></a>volume-tags</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p46978902184115"><a name="p46978902184115"></a><a name="p46978902184115"></a>Cinder</p>
</td>
</tr>
<tr id="r6a303e92b99c4788b544b0f0324170c1"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p66538158183659"><a name="p66538158183659"></a><a name="p66538158183659"></a>Batch deleting volume tags</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p29403659183955"><a name="p29403659183955"></a><a name="p29403659183955"></a>bulkDeleteVolume-tags</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p29687082184017"><a name="p29687082184017"></a><a name="p29687082184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p11889168184051"><a name="p11889168184051"></a><a name="p11889168184051"></a>volume-tags</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p22099181184115"><a name="p22099181184115"></a><a name="p22099181184115"></a>Cinder</p>
</td>
</tr>
<tr id="r6b35e712c1b745919b64a7b021f7658d"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p53717956183659"><a name="p53717956183659"></a><a name="p53717956183659"></a>Deleting a single volume tag</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p27539796183955"><a name="p27539796183955"></a><a name="p27539796183955"></a>deleteVolume-tagsSingleTag</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p32829129184017"><a name="p32829129184017"></a><a name="p32829129184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p10160712184051"><a name="p10160712184051"></a><a name="p10160712184051"></a>volume-tags</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p4175886184115"><a name="p4175886184115"></a><a name="p4175886184115"></a>Cinder</p>
</td>
</tr>
<tr id="r0553b7f4e68d4a3c856e19371e9fbde3"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p35922464183659"><a name="p35922464183659"></a><a name="p35922464183659"></a>Updating a single volume tag</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p10961256183955"><a name="p10961256183955"></a><a name="p10961256183955"></a>updateVolume-tagsSingleTag</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p41679868184017"><a name="p41679868184017"></a><a name="p41679868184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p25184191184051"><a name="p25184191184051"></a><a name="p25184191184051"></a>volume-tags</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p24322436184115"><a name="p24322436184115"></a><a name="p24322436184115"></a>Cinder</p>
</td>
</tr>
<tr id="r4d9078646d394ad4a301af0d449853f2"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p15019308183659"><a name="p15019308183659"></a><a name="p15019308183659"></a>Creating snapshot tags</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p4801515183955"><a name="p4801515183955"></a><a name="p4801515183955"></a>createSnapshot-tags</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p51417598184017"><a name="p51417598184017"></a><a name="p51417598184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p38555858184051"><a name="p38555858184051"></a><a name="p38555858184051"></a>snapshot-tags</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p14316387184115"><a name="p14316387184115"></a><a name="p14316387184115"></a>Cinder</p>
</td>
</tr>
<tr id="r7807393ca095489c8b516cf9deec8528"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p10331293183659"><a name="p10331293183659"></a><a name="p10331293183659"></a>Updating snapshot tags</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p10643975183955"><a name="p10643975183955"></a><a name="p10643975183955"></a>updateSnapshot-tags</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p36683218184017"><a name="p36683218184017"></a><a name="p36683218184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p55715490184051"><a name="p55715490184051"></a><a name="p55715490184051"></a>snapshot-tags</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p34772420184115"><a name="p34772420184115"></a><a name="p34772420184115"></a>Cinder</p>
</td>
</tr>
<tr id="rf4f2850446ff4ddab9341c602b72ea70"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p15320365183659"><a name="p15320365183659"></a><a name="p15320365183659"></a>Batch deleting snapshot tags</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p41938735183955"><a name="p41938735183955"></a><a name="p41938735183955"></a>bulkDeleteSnapshot-tags</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p32738564184017"><a name="p32738564184017"></a><a name="p32738564184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p15730140184051"><a name="p15730140184051"></a><a name="p15730140184051"></a>snapshot-tags</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p49053068184115"><a name="p49053068184115"></a><a name="p49053068184115"></a>Cinder</p>
</td>
</tr>
<tr id="r61be0cdae5be462ca8d8511cb270563c"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p28475231183659"><a name="p28475231183659"></a><a name="p28475231183659"></a>Deleting a single snapshot tag</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p38804958183955"><a name="p38804958183955"></a><a name="p38804958183955"></a>deleteSnapshot-tagsSingleTag</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p42766437184017"><a name="p42766437184017"></a><a name="p42766437184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p58765682184051"><a name="p58765682184051"></a><a name="p58765682184051"></a>snapshot-tags</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p57771301184115"><a name="p57771301184115"></a><a name="p57771301184115"></a>Cinder</p>
</td>
</tr>
<tr id="rdfeaa71679f34abe9844c1eaed5cd262"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p21805119183659"><a name="p21805119183659"></a><a name="p21805119183659"></a>Updating a single snapshot tag</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p35982935183955"><a name="p35982935183955"></a><a name="p35982935183955"></a>updateSnapshot-tagsSingleTag</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p38219985184017"><a name="p38219985184017"></a><a name="p38219985184017"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p24727391184051"><a name="p24727391184051"></a><a name="p24727391184051"></a>snapshot-tags</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p38020930184115"><a name="p38020930184115"></a><a name="p38020930184115"></a>Cinder</p>
</td>
</tr>
<tr id="row55216342184125"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p43338702184125"><a name="p43338702184125"></a><a name="p43338702184125"></a>Batch creating volume tags</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p20773950184125"><a name="p20773950184125"></a><a name="p20773950184125"></a>createVolume-tags</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p4968399184125"><a name="p4968399184125"></a><a name="p4968399184125"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p41092966184051"><a name="p41092966184051"></a><a name="p41092966184051"></a>volume-tags</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p24243871184131"><a name="p24243871184131"></a><a name="p24243871184131"></a>Cinder</p>
</td>
</tr>
<tr id="row29520772184122"><td class="cellrowborder" valign="top" width="20.840000000000003%" headers="mcps1.2.6.1.1 "><p id="p42372365184122"><a name="p42372365184122"></a><a name="p42372365184122"></a>Batch deleting volume tags</p>
</td>
<td class="cellrowborder" valign="top" width="20.17%" headers="mcps1.2.6.1.2 "><p id="p9609546184122"><a name="p9609546184122"></a><a name="p9609546184122"></a>deleteVolume-tags</p>
</td>
<td class="cellrowborder" valign="top" width="13.47%" headers="mcps1.2.6.1.3 "><p id="p40175780184122"><a name="p40175780184122"></a><a name="p40175780184122"></a>EVS</p>
</td>
<td class="cellrowborder" valign="top" width="18.990000000000006%" headers="mcps1.2.6.1.4 "><p id="p33012738184122"><a name="p33012738184122"></a><a name="p33012738184122"></a>volume-tags</p>
</td>
<td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.2.6.1.5 "><p id="p27670923184131"><a name="p27670923184131"></a><a name="p27670923184131"></a>Cinder</p>
</td>
</tr>
</tbody>
</table>

