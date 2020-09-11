# DB Instance Specifications<a name="rds_10_0004"></a>

For details about single DB instance specifications, see  [Table 1](#ted9b9d433c8a4c52884e199e17f94479).  The specifications vary according to actual situations.

For primary/standby DB instances and read replicas, the specifications are displayed based on the following rules:

-   For primary/standby DB instances: the suffix  **.ha**  needs to be added to the DB instance name, for example, rds.mysql.s1.xlarge.ha.
-   For read replicas: the suffix  **.rr**  needs to be added to the DB instance name, for example, rds.mysql.s1.xlarge.rr.

## Constraints<a name="section1399014431471"></a>

**Table  1**  Single DB instance specifications

<a name="ted9b9d433c8a4c52884e199e17f94479"></a>
<table><thead align="left"><tr id="r495c7487f7d545cfad43ba7ca29a4b5d"><th class="cellrowborder" valign="top" width="11.12%" id="mcps1.2.6.1.1"><p id="af7477395c96c4da580be96a7483d0da3"><a name="af7477395c96c4da580be96a7483d0da3"></a><a name="af7477395c96c4da580be96a7483d0da3"></a><strong id="b1414215423506"><a name="b1414215423506"></a><a name="b1414215423506"></a>Instance Class</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.93%" id="mcps1.2.6.1.2"><p id="p183721423195015"><a name="p183721423195015"></a><a name="p183721423195015"></a><strong id="b3597135213508"><a name="b3597135213508"></a><a name="b3597135213508"></a>DB Engine</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.11%" id="mcps1.2.6.1.3"><p id="p113108391561"><a name="p113108391561"></a><a name="p113108391561"></a><strong id="b3930113614540"><a name="b3930113614540"></a><a name="b3930113614540"></a>Spec Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.869999999999997%" id="mcps1.2.6.1.4"><p id="en-us_topic_0086557098_p488424159258"><a name="en-us_topic_0086557098_p488424159258"></a><a name="en-us_topic_0086557098_p488424159258"></a><strong id="b47998572126"><a name="b47998572126"></a><a name="b47998572126"></a>vCPUs</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.97%" id="mcps1.2.6.1.5"><p id="en-us_topic_0086557098_p639215769258"><a name="en-us_topic_0086557098_p639215769258"></a><a name="en-us_topic_0086557098_p639215769258"></a><strong id="b91709447502"><a name="b91709447502"></a><a name="b91709447502"></a>Memory (GB)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r2e862e85f4da4ef59f2cb64b6c1e8a28"><td class="cellrowborder" rowspan="58" valign="top" width="11.12%" headers="mcps1.2.6.1.1 "><p id="p122081415115115"><a name="p122081415115115"></a><a name="p122081415115115"></a>General computing-plus</p>
</td>
<td class="cellrowborder" rowspan="20" valign="top" width="19.93%" headers="mcps1.2.6.1.2 "><p id="p1128551155517"><a name="p1128551155517"></a><a name="p1128551155517"></a>MySQL</p>
</td>
<td class="cellrowborder" valign="top" width="33.11%" headers="mcps1.2.6.1.3 "><p id="p19533626264"><a name="p19533626264"></a><a name="p19533626264"></a>rds.mysql.c2.medium</p>
</td>
<td class="cellrowborder" valign="top" width="19.869999999999997%" headers="mcps1.2.6.1.4 "><p id="p1410181045211"><a name="p1410181045211"></a><a name="p1410181045211"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="15.97%" headers="mcps1.2.6.1.5 "><p id="p18751010522"><a name="p18751010522"></a><a name="p18751010522"></a>2</p>
</td>
</tr>
<tr id="r1a699d99e9c54e3e837d583f56f1590d"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p175695842311"><a name="p175695842311"></a><a name="p175695842311"></a>rds.mysql.s1.medium</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p89972975216"><a name="p89972975216"></a><a name="p89972975216"></a>1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1599389205219"><a name="p1599389205219"></a><a name="p1599389205219"></a>4</p>
</td>
</tr>
<tr id="r41644dd0109840a49d6909885f2d0d65"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p86301284249"><a name="p86301284249"></a><a name="p86301284249"></a>rds.mysql.c2.large</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p17982199155216"><a name="p17982199155216"></a><a name="p17982199155216"></a>2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p59784905213"><a name="p59784905213"></a><a name="p59784905213"></a>4</p>
</td>
</tr>
<tr id="r1b4077c456af477fa3d552723fa832d3"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1153362614618"><a name="p1153362614618"></a><a name="p1153362614618"></a>rds.mysql.s1.large</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p17944393522"><a name="p17944393522"></a><a name="p17944393522"></a>2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p093915910522"><a name="p093915910522"></a><a name="p093915910522"></a>8</p>
</td>
</tr>
<tr id="ra2ccbc6c7cc24b9fabaae73742b22f4e"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1053312617620"><a name="p1053312617620"></a><a name="p1053312617620"></a>rds.mysql.m1.large</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p591819918520"><a name="p591819918520"></a><a name="p591819918520"></a>2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p15912209135214"><a name="p15912209135214"></a><a name="p15912209135214"></a>16</p>
</td>
</tr>
<tr id="r64ba627d7e284a09a42573f43bbb0970"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p19533172613613"><a name="p19533172613613"></a><a name="p19533172613613"></a>rds.mysql.c2.xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p178971913526"><a name="p178971913526"></a><a name="p178971913526"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1189213945218"><a name="p1189213945218"></a><a name="p1189213945218"></a>8</p>
</td>
</tr>
<tr id="rb5102f233af34d318828b3ac1162f9a1"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p32847125270"><a name="p32847125270"></a><a name="p32847125270"></a>rds.mysql.s1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p887813975216"><a name="p887813975216"></a><a name="p887813975216"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p7875129145211"><a name="p7875129145211"></a><a name="p7875129145211"></a>16</p>
</td>
</tr>
<tr id="r8072b6079c1b40f89e93ed9c4636fdeb"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p20211218202719"><a name="p20211218202719"></a><a name="p20211218202719"></a>rds.mysql.m1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p15861159185217"><a name="p15861159185217"></a><a name="p15861159185217"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p0858119125216"><a name="p0858119125216"></a><a name="p0858119125216"></a>32</p>
</td>
</tr>
<tr id="row194852039131116"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1549642682719"><a name="p1549642682719"></a><a name="p1549642682719"></a>rds.mysql.c2.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p548563913115"><a name="p548563913115"></a><a name="p548563913115"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p8485339131111"><a name="p8485339131111"></a><a name="p8485339131111"></a>16</p>
</td>
</tr>
<tr id="r6da1f7a3005c43a9af198cee0941c560"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p23956395279"><a name="p23956395279"></a><a name="p23956395279"></a>rds.mysql.s1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p78480995216"><a name="p78480995216"></a><a name="p78480995216"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p184417905212"><a name="p184417905212"></a><a name="p184417905212"></a>32</p>
</td>
</tr>
<tr id="rcb7d13c56a914b0a8cac1d6d62b185d2"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p6533926765"><a name="p6533926765"></a><a name="p6533926765"></a>rds.mysql.m1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p28269925211"><a name="p28269925211"></a><a name="p28269925211"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p12822109205212"><a name="p12822109205212"></a><a name="p12822109205212"></a>64</p>
</td>
</tr>
<tr id="row176113162122"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p195337261767"><a name="p195337261767"></a><a name="p195337261767"></a>rds.mysql.c2.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p116381611124"><a name="p116381611124"></a><a name="p116381611124"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p156381661214"><a name="p156381661214"></a><a name="p156381661214"></a>32</p>
</td>
</tr>
<tr id="row1773819151219"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p65347268620"><a name="p65347268620"></a><a name="p65347268620"></a>rds.mysql.s1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p9742194122"><a name="p9742194122"></a><a name="p9742194122"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p2074181911212"><a name="p2074181911212"></a><a name="p2074181911212"></a>64</p>
</td>
</tr>
<tr id="row65846238171141"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p2047104172814"><a name="p2047104172814"></a><a name="p2047104172814"></a>rds.mysql.m1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p68031697526"><a name="p68031697526"></a><a name="p68031697526"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p117981396522"><a name="p117981396522"></a><a name="p117981396522"></a>128</p>
</td>
</tr>
<tr id="row104491410197"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p85531447142817"><a name="p85531447142817"></a><a name="p85531447142817"></a>rds.mysql.c2.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p8450910993"><a name="p8450910993"></a><a name="p8450910993"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p6450510398"><a name="p6450510398"></a><a name="p6450510398"></a>64</p>
</td>
</tr>
<tr id="row32217715910"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1830188290"><a name="p1830188290"></a><a name="p1830188290"></a>rds.mysql.s1.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p152211671794"><a name="p152211671794"></a><a name="p152211671794"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p102211175914"><a name="p102211175914"></a><a name="p102211175914"></a>128</p>
</td>
</tr>
<tr id="row1239413511525"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p5345131752911"><a name="p5345131752911"></a><a name="p5345131752911"></a>rds.mysql.m1.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p117841935219"><a name="p117841935219"></a><a name="p117841935219"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p87780975216"><a name="p87780975216"></a><a name="p87780975216"></a>256</p>
</td>
</tr>
<tr id="row15741347111920"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p23771337142913"><a name="p23771337142913"></a><a name="p23771337142913"></a>rds.mysql.c3.15xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p44695511914"><a name="p44695511914"></a><a name="p44695511914"></a>60</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p3471655121914"><a name="p3471655121914"></a><a name="p3471655121914"></a>128</p>
</td>
</tr>
<tr id="row127014519197"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p25343266616"><a name="p25343266616"></a><a name="p25343266616"></a>rds.mysql.c3.15xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p16472055201912"><a name="p16472055201912"></a><a name="p16472055201912"></a>60</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p154719557197"><a name="p154719557197"></a><a name="p154719557197"></a>256</p>
</td>
</tr>
<tr id="row5444135341919"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p8534102616613"><a name="p8534102616613"></a><a name="p8534102616613"></a>rds.mysql.m3.15xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p204765521910"><a name="p204765521910"></a><a name="p204765521910"></a>60</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p547155510198"><a name="p547155510198"></a><a name="p547155510198"></a>512</p>
</td>
</tr>
<tr id="row8701193316524"><td class="cellrowborder" rowspan="20" valign="top" headers="mcps1.2.6.1.1 "><p id="p5320181110566"><a name="p5320181110566"></a><a name="p5320181110566"></a>PostgreSQL</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1767713285345"><a name="p1767713285345"></a><a name="p1767713285345"></a>rds.pg.c2.medium</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p17287156105414"><a name="p17287156105414"></a><a name="p17287156105414"></a>1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p6287856205413"><a name="p6287856205413"></a><a name="p6287856205413"></a>2</p>
</td>
</tr>
<tr id="row1465615016528"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1667712286349"><a name="p1667712286349"></a><a name="p1667712286349"></a>rds.pg.s1.medium</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p172875567542"><a name="p172875567542"></a><a name="p172875567542"></a>1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1328711566541"><a name="p1328711566541"></a><a name="p1328711566541"></a>4</p>
</td>
</tr>
<tr id="row168485453522"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p36771928123414"><a name="p36771928123414"></a><a name="p36771928123414"></a>rds.pg.c2.large</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1028785645420"><a name="p1028785645420"></a><a name="p1028785645420"></a>2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p82872565543"><a name="p82872565543"></a><a name="p82872565543"></a>4</p>
</td>
</tr>
<tr id="row133351248175210"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p196771928143419"><a name="p196771928143419"></a><a name="p196771928143419"></a>rds.pg.s1.large</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p828845655411"><a name="p828845655411"></a><a name="p828845655411"></a>2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1328835611549"><a name="p1328835611549"></a><a name="p1328835611549"></a>8</p>
</td>
</tr>
<tr id="row102741117115311"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1567722819342"><a name="p1567722819342"></a><a name="p1567722819342"></a>rds.pg.m1.large</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p128811568546"><a name="p128811568546"></a><a name="p128811568546"></a>2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p5288656145416"><a name="p5288656145416"></a><a name="p5288656145416"></a>16</p>
</td>
</tr>
<tr id="row33009159537"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p2067712282342"><a name="p2067712282342"></a><a name="p2067712282342"></a>rds.pg.c2.xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1028995618547"><a name="p1028995618547"></a><a name="p1028995618547"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p142891656205417"><a name="p142891656205417"></a><a name="p142891656205417"></a>8</p>
</td>
</tr>
<tr id="row3473312175316"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p7677228163414"><a name="p7677228163414"></a><a name="p7677228163414"></a>rds.pg.s1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p728925685410"><a name="p728925685410"></a><a name="p728925685410"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p828965614541"><a name="p828965614541"></a><a name="p828965614541"></a>16</p>
</td>
</tr>
<tr id="row1374910109539"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p767818282344"><a name="p767818282344"></a><a name="p767818282344"></a>rds.pg.m1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p19289165615413"><a name="p19289165615413"></a><a name="p19289165615413"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p20289185618546"><a name="p20289185618546"></a><a name="p20289185618546"></a>32</p>
</td>
</tr>
<tr id="row209821183538"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p136781928153413"><a name="p136781928153413"></a><a name="p136781928153413"></a>rds.pg.c2.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p729055685417"><a name="p729055685417"></a><a name="p729055685417"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p14290155645418"><a name="p14290155645418"></a><a name="p14290155645418"></a>16</p>
</td>
</tr>
<tr id="row2828133565215"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p19678128103414"><a name="p19678128103414"></a><a name="p19678128103414"></a>rds.pg.s1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p15290856145411"><a name="p15290856145411"></a><a name="p15290856145411"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p8290195615416"><a name="p8290195615416"></a><a name="p8290195615416"></a>32</p>
</td>
</tr>
<tr id="row099310695320"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p767862883412"><a name="p767862883412"></a><a name="p767862883412"></a>rds.pg.m1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1029135625414"><a name="p1029135625414"></a><a name="p1029135625414"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p8291135655412"><a name="p8291135655412"></a><a name="p8291135655412"></a>64</p>
</td>
</tr>
<tr id="row17752143155212"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p867810285343"><a name="p867810285343"></a><a name="p867810285343"></a>rds.pg.c2.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p112911561542"><a name="p112911561542"></a><a name="p112911561542"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1529115564549"><a name="p1529115564549"></a><a name="p1529115564549"></a>32</p>
</td>
</tr>
<tr id="row13304115685218"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p36789285340"><a name="p36789285340"></a><a name="p36789285340"></a>rds.pg.s1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p0291756185416"><a name="p0291756185416"></a><a name="p0291756185416"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p2291956115412"><a name="p2291956115412"></a><a name="p2291956115412"></a>64</p>
</td>
</tr>
<tr id="row71811341185211"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p12678152833412"><a name="p12678152833412"></a><a name="p12678152833412"></a>rds.pg.m1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1729219565541"><a name="p1729219565541"></a><a name="p1729219565541"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1292256195414"><a name="p1292256195414"></a><a name="p1292256195414"></a>128</p>
</td>
</tr>
<tr id="row2010055405219"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1367842820343"><a name="p1367842820343"></a><a name="p1367842820343"></a>rds.pg.c2.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p17292556165411"><a name="p17292556165411"></a><a name="p17292556165411"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p7292105618542"><a name="p7292105618542"></a><a name="p7292105618542"></a>64</p>
</td>
</tr>
<tr id="row138392038195214"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p106781328173414"><a name="p106781328173414"></a><a name="p106781328173414"></a>rds.pg.s1.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p192939562541"><a name="p192939562541"></a><a name="p192939562541"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1129325625417"><a name="p1129325625417"></a><a name="p1129325625417"></a>128</p>
</td>
</tr>
<tr id="row15673831115210"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1067812863411"><a name="p1067812863411"></a><a name="p1067812863411"></a>rds.pg.m1.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1329325625412"><a name="p1329325625412"></a><a name="p1329325625412"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p10293135695416"><a name="p10293135695416"></a><a name="p10293135695416"></a>256</p>
</td>
</tr>
<tr id="row9143253538"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p76784284349"><a name="p76784284349"></a><a name="p76784284349"></a>rds.pg.c3.15xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1129335617544"><a name="p1129335617544"></a><a name="p1129335617544"></a>60</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p72937563549"><a name="p72937563549"></a><a name="p72937563549"></a>128</p>
</td>
</tr>
<tr id="row812872517525"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p6678112813419"><a name="p6678112813419"></a><a name="p6678112813419"></a>rds.pg.c3.15xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p3294356105417"><a name="p3294356105417"></a><a name="p3294356105417"></a>60</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p10294185615542"><a name="p10294185615542"></a><a name="p10294185615542"></a>256</p>
</td>
</tr>
<tr id="row2034362914522"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p3678928113410"><a name="p3678928113410"></a><a name="p3678928113410"></a>rds.pg.m3.15xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p0294195675412"><a name="p0294195675412"></a><a name="p0294195675412"></a>60</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p9294165625411"><a name="p9294165625411"></a><a name="p9294165625411"></a>512</p>
</td>
</tr>
<tr id="row1981844212564"><td class="cellrowborder" rowspan="18" valign="top" headers="mcps1.2.6.1.1 "><p id="p1643682619010"><a name="p1643682619010"></a><a name="p1643682619010"></a>Microsoft SQL Server</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p579443133714"><a name="p579443133714"></a><a name="p579443133714"></a>rds.mssql.c2.large</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p16244917703"><a name="p16244917703"></a><a name="p16244917703"></a>2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p1624417175011"><a name="p1624417175011"></a><a name="p1624417175011"></a>4</p>
</td>
</tr>
<tr id="row99731051205617"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p10791643103715"><a name="p10791643103715"></a><a name="p10791643103715"></a>rds.mssql.s1.large</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1924541717019"><a name="p1924541717019"></a><a name="p1924541717019"></a>2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p152451917605"><a name="p152451917605"></a><a name="p152451917605"></a>8</p>
</td>
</tr>
<tr id="row19288606577"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p187913431374"><a name="p187913431374"></a><a name="p187913431374"></a>rds.mssql.m1.large</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p12478171702"><a name="p12478171702"></a><a name="p12478171702"></a>2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1524710171503"><a name="p1524710171503"></a><a name="p1524710171503"></a>16</p>
</td>
</tr>
<tr id="row1558013245712"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p279174320372"><a name="p279174320372"></a><a name="p279174320372"></a>rds.mssql.c2.xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1924710174015"><a name="p1924710174015"></a><a name="p1924710174015"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p102473171017"><a name="p102473171017"></a><a name="p102473171017"></a>8</p>
</td>
</tr>
<tr id="row8275058125611"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p157912432372"><a name="p157912432372"></a><a name="p157912432372"></a>rds.mssql.s1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p122488171609"><a name="p122488171609"></a><a name="p122488171609"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p192488171014"><a name="p192488171014"></a><a name="p192488171014"></a>16</p>
</td>
</tr>
<tr id="row347285495613"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p17791435378"><a name="p17791435378"></a><a name="p17791435378"></a>rds.mssql.m1.xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p18248917707"><a name="p18248917707"></a><a name="p18248917707"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p172488173020"><a name="p172488173020"></a><a name="p172488173020"></a>32</p>
</td>
</tr>
<tr id="row175231456145619"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1279194313718"><a name="p1279194313718"></a><a name="p1279194313718"></a>rds.mssql.c2.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1524815170018"><a name="p1524815170018"></a><a name="p1524815170018"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p192484171401"><a name="p192484171401"></a><a name="p192484171401"></a>16</p>
</td>
</tr>
<tr id="row594254965619"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1779194314376"><a name="p1779194314376"></a><a name="p1779194314376"></a>rds.mssql.s1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p6249201711017"><a name="p6249201711017"></a><a name="p6249201711017"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p224918171103"><a name="p224918171103"></a><a name="p224918171103"></a>32</p>
</td>
</tr>
<tr id="row4110124825619"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1379144316371"><a name="p1379144316371"></a><a name="p1379144316371"></a>rds.mssql.m1.2xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p324914171501"><a name="p324914171501"></a><a name="p324914171501"></a>8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1524912172013"><a name="p1524912172013"></a><a name="p1524912172013"></a>64</p>
</td>
</tr>
<tr id="row2027054611565"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p3792043183714"><a name="p3792043183714"></a><a name="p3792043183714"></a>rds.mssql.c2.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p11249101715017"><a name="p11249101715017"></a><a name="p11249101715017"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p824921715018"><a name="p824921715018"></a><a name="p824921715018"></a>32</p>
</td>
</tr>
<tr id="row9505244125617"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p179104373713"><a name="p179104373713"></a><a name="p179104373713"></a>rds.mssql.s1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p112501217202"><a name="p112501217202"></a><a name="p112501217202"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p172503171302"><a name="p172503171302"></a><a name="p172503171302"></a>64</p>
</td>
</tr>
<tr id="row16212836135614"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p10796433379"><a name="p10796433379"></a><a name="p10796433379"></a>rds.mssql.m1.4xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p52501179015"><a name="p52501179015"></a><a name="p52501179015"></a>16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p42503171604"><a name="p42503171604"></a><a name="p42503171604"></a>128</p>
</td>
</tr>
<tr id="row151051440125619"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p13791843153719"><a name="p13791843153719"></a><a name="p13791843153719"></a>rds.mssql.c2.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1725011719012"><a name="p1725011719012"></a><a name="p1725011719012"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p14250111720015"><a name="p14250111720015"></a><a name="p14250111720015"></a>64</p>
</td>
</tr>
<tr id="row823813815562"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p079134393715"><a name="p079134393715"></a><a name="p079134393715"></a>rds.mssql.s1.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1225151711010"><a name="p1225151711010"></a><a name="p1225151711010"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p10251141713019"><a name="p10251141713019"></a><a name="p10251141713019"></a>128</p>
</td>
</tr>
<tr id="row82031534165615"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1080143113713"><a name="p1080143113713"></a><a name="p1080143113713"></a>rds.mssql.m1.8xlarge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p12251141718017"><a name="p12251141718017"></a><a name="p12251141718017"></a>32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p725111718010"><a name="p725111718010"></a><a name="p725111718010"></a>256</p>
</td>
</tr>
<tr id="row13718183135615"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p17801943153712"><a name="p17801943153712"></a><a name="p17801943153712"></a>rds.mssql.c3.15xlarge.2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1725121719018"><a name="p1725121719018"></a><a name="p1725121719018"></a>60</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1525291713013"><a name="p1525291713013"></a><a name="p1525291713013"></a>128</p>
</td>
</tr>
<tr id="row124796298565"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p7801143133719"><a name="p7801143133719"></a><a name="p7801143133719"></a>rds.mssql.c3.15xlarge.4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p5252161720017"><a name="p5252161720017"></a><a name="p5252161720017"></a>60</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p192527174018"><a name="p192527174018"></a><a name="p192527174018"></a>256</p>
</td>
</tr>
<tr id="row15972152615566"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p138020430379"><a name="p138020430379"></a><a name="p138020430379"></a>rds.mssql.m3.15xlarge.8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p10252217907"><a name="p10252217907"></a><a name="p10252217907"></a>60</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p20252161717013"><a name="p20252161717013"></a><a name="p20252161717013"></a>512</p>
</td>
</tr>
</tbody>
</table>

