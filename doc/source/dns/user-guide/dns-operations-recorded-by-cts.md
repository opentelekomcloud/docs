# DNS Operations Recorded by CTS<a name="EN-US_TOPIC_0109830566"></a>

CTS is interconnected with the DNS service to record operations performed by users in real time. Actions and results of the operations are stored in OBS buckets in the form the traces.

After you enable CTS, whenever a DNS API is called, the operation is recorded in a log file, which is then delivered to a specified OBS bucket for storage.

[Table 1](#table149110413017) and [Table 2](#table155718451405) list the DNS operations that will be recorded by CTS.

> ![](/images/icon-note.gif) **NOTE:** 

> The DNS service involves resources both at the global and region levels. [Table 1](#table149110413017) lists DNS operations at the global level. Traces of these operations are displayed only in the primary region.

> [Table 2](#table155718451405) lists DNS operations at the region level. Traces of these operations are displayed in the regions where the operations are performed.

**Table 1** Global-level DNS operations that can be recorded by CTS

<a name="table149110413017"></a><table><thead align="left"><tr id="row159216411903"><th class="cellrowborder" valign="top" width="35.23%" id="mcps1.2.4.1.1"><p id="p892144117015"><a name="p892144117015"></a><a name="p892144117015"></a><strong id="b89210411409"><a name="b89210411409"></a><a name="b89210411409"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.97%" id="mcps1.2.4.1.2"><p id="p1194104112010"><a name="p1194104112010"></a><a name="p1194104112010"></a><strong id="b19419411400"><a name="b19419411400"></a><a name="b19419411400"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.800000000000004%" id="mcps1.2.4.1.3"><p id="p11946413018"><a name="p11946413018"></a><a name="p11946413018"></a><strong id="b79614414016"><a name="b79614414016"></a><a name="b79614414016"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row51023413013"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p9102741704"><a name="p9102741704"></a><a name="p9102741704"></a>Creating a record set in a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p161029416011"><a name="p161029416011"></a><a name="p161029416011"></a>publicRecordSet</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p210274111018"><a name="p210274111018"></a><a name="p210274111018"></a>createPublicRecordSet</p>
</td>
</tr>
<tr id="row1102174119011"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p710218418018"><a name="p710218418018"></a><a name="p710218418018"></a>Deleting a record set in a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p4103114115020"><a name="p4103114115020"></a><a name="p4103114115020"></a>publicRecordSet</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p81034418014"><a name="p81034418014"></a><a name="p81034418014"></a>deletePublicRecordSet</p>
</td>
</tr>
<tr id="row131032411107"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p1710310410019"><a name="p1710310410019"></a><a name="p1710310410019"></a>Modifying a record set in a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p11038414014"><a name="p11038414014"></a><a name="p11038414014"></a>publicRecordSet</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p13103164117019"><a name="p13103164117019"></a><a name="p13103164117019"></a>updatePublicRecordSet</p>
</td>
</tr>
<tr id="row910416414014"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p12104541301"><a name="p12104541301"></a><a name="p12104541301"></a>Creating a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p110474116014"><a name="p110474116014"></a><a name="p110474116014"></a>publicZone</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p71073411306"><a name="p71073411306"></a><a name="p71073411306"></a>createPublicZone</p>
</td>
</tr>
<tr id="row1010716411403"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p151073411406"><a name="p151073411406"></a><a name="p151073411406"></a>Modifying a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p1110734118018"><a name="p1110734118018"></a><a name="p1110734118018"></a>publicZone</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p151071141605"><a name="p151071141605"></a><a name="p151071141605"></a>updatePublicZone</p>
</td>
</tr>
<tr id="row611294117013"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p12112154114013"><a name="p12112154114013"></a><a name="p12112154114013"></a>Deleting a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p151124417013"><a name="p151124417013"></a><a name="p151124417013"></a>publicZone</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p11112174113017"><a name="p11112174113017"></a><a name="p11112174113017"></a>deletePublicZone</p>
</td>
</tr>
<tr id="row131130416012"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p131139415016"><a name="p131139415016"></a><a name="p131139415016"></a>Adding tags to a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p91130412018"><a name="p91130412018"></a><a name="p91130412018"></a>publicZoneTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p311314413019"><a name="p311314413019"></a><a name="p311314413019"></a>createPublicZoneTag</p>
</td>
</tr>
<tr id="row191131041803"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p171134411203"><a name="p171134411203"></a><a name="p171134411203"></a>Deleting tags of a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p1211316411506"><a name="p1211316411506"></a><a name="p1211316411506"></a>publicZoneTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p91139418015"><a name="p91139418015"></a><a name="p91139418015"></a>deletePublicZoneTag</p>
</td>
</tr>
<tr id="row1311420419012"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p1811410411308"><a name="p1811410411308"></a><a name="p1811410411308"></a>Adding tags to a record set in a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p411410415020"><a name="p411410415020"></a><a name="p411410415020"></a>publicRecordSetTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p181141841603"><a name="p181141841603"></a><a name="p181141841603"></a>createPublicRecordSetTag</p>
</td>
</tr>
<tr id="row14115184120014"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p011517411008"><a name="p011517411008"></a><a name="p011517411008"></a>Deleting tags of a record set in a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p911554113010"><a name="p911554113010"></a><a name="p911554113010"></a>publicRecordSetTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p41150411102"><a name="p41150411102"></a><a name="p41150411102"></a>deletePublicRecordSetTag</p>
</td>
</tr>
<tr id="row91179411607"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p1011719417015"><a name="p1011719417015"></a><a name="p1011719417015"></a>Adding tags to a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p1911712416011"><a name="p1911712416011"></a><a name="p1911712416011"></a>privateZoneTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p10118174116012"><a name="p10118174116012"></a><a name="p10118174116012"></a>createPrivateZoneTag</p>
</td>
</tr>
<tr id="row101189411807"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p411844115011"><a name="p411844115011"></a><a name="p411844115011"></a>Deleting tags of a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p6118241303"><a name="p6118241303"></a><a name="p6118241303"></a>privateZoneTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p191182411503"><a name="p191182411503"></a><a name="p191182411503"></a>deletePrivateZoneTag</p>
</td>
</tr>
<tr id="row11118141303"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p111913416010"><a name="p111913416010"></a><a name="p111913416010"></a>Adding tags to a record set in a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p911919414013"><a name="p911919414013"></a><a name="p911919414013"></a>privateRecordSetTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p21192415010"><a name="p21192415010"></a><a name="p21192415010"></a>createPrivateRecordSetTag</p>
</td>
</tr>
<tr id="row41216411201"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p512124111013"><a name="p512124111013"></a><a name="p512124111013"></a>Deleting tags of a record set in a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p181211741400"><a name="p181211741400"></a><a name="p181211741400"></a>privateRecordSetTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p2121154119017"><a name="p2121154119017"></a><a name="p2121154119017"></a>deletePrivateRecordSetTag</p>
</td>
</tr>
<tr id="row11121124111016"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p171211641306"><a name="p171211641306"></a><a name="p171211641306"></a>Adding tags to a PTR record</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p181211941801"><a name="p181211941801"></a><a name="p181211941801"></a>ptrRecordTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p51234411303"><a name="p51234411303"></a><a name="p51234411303"></a>createPTRRecordSetTag</p>
</td>
</tr>
<tr id="row312317413013"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="p1312354114013"><a name="p1312354114013"></a><a name="p1312354114013"></a>Deleting tags of a PTR record</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="p81238411402"><a name="p81238411402"></a><a name="p81238411402"></a>ptrRecordTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="p41232411502"><a name="p41232411502"></a><a name="p41232411502"></a>deletePTRRecordTag</p>
</td>
</tr>
</tbody>
</table>

**Table 2** Region-level DNS operations that can be recorded by CTS

<a name="table155718451405"></a><table><thead align="left"><tr id="row155774513015"><th class="cellrowborder" valign="top" width="31.069999999999997%" id="mcps1.2.4.1.1"><p id="p19558104516010"><a name="p19558104516010"></a><a name="p19558104516010"></a><strong id="b125581445301"><a name="b125581445301"></a><a name="b125581445301"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.189999999999998%" id="mcps1.2.4.1.2"><p id="p1655815457011"><a name="p1655815457011"></a><a name="p1655815457011"></a><strong id="b75588451107"><a name="b75588451107"></a><a name="b75588451107"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.739999999999995%" id="mcps1.2.4.1.3"><p id="p135581045200"><a name="p135581045200"></a><a name="p135581045200"></a><strong id="b65582045301"><a name="b65582045301"></a><a name="b65582045301"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row125605451701"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="p856019451504"><a name="p856019451504"></a><a name="p856019451504"></a>Creating a record set in a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p1560114511012"><a name="p1560114511012"></a><a name="p1560114511012"></a>privateRecordSet</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p1156014451501"><a name="p1156014451501"></a><a name="p1156014451501"></a>createPrivateRecordSet</p>
</td>
</tr>
<tr id="row125609459014"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="p75601745709"><a name="p75601745709"></a><a name="p75601745709"></a>Deleting a record set in a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p956219451003"><a name="p956219451003"></a><a name="p956219451003"></a>privateRecordSet</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p25621245809"><a name="p25621245809"></a><a name="p25621245809"></a>deletePrivateRecordSet</p>
</td>
</tr>
<tr id="row1556213451002"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="p13562114514013"><a name="p13562114514013"></a><a name="p13562114514013"></a>Modifying a record set in a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p456214516014"><a name="p456214516014"></a><a name="p456214516014"></a>privateRecordSet</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p1756234513020"><a name="p1756234513020"></a><a name="p1756234513020"></a>updatePrivateRecordSet</p>
</td>
</tr>
<tr id="row1756224514019"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="p756214455020"><a name="p756214455020"></a><a name="p756214455020"></a>Creating a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p15562745909"><a name="p15562745909"></a><a name="p15562745909"></a>privateZone</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p1356212455014"><a name="p1356212455014"></a><a name="p1356212455014"></a>createPrivateZone</p>
</td>
</tr>
<tr id="row2056264519016"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="p1456311456020"><a name="p1456311456020"></a><a name="p1456311456020"></a>Modifying a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p256319451408"><a name="p256319451408"></a><a name="p256319451408"></a>privateZone</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p75634451509"><a name="p75634451509"></a><a name="p75634451509"></a>updatePrivateZone</p>
</td>
</tr>
<tr id="row656315451703"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="p556317451301"><a name="p556317451301"></a><a name="p556317451301"></a>Deleting a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p756424514014"><a name="p756424514014"></a><a name="p756424514014"></a>privateZone</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p12564174520020"><a name="p12564174520020"></a><a name="p12564174520020"></a>deletePrivateZone</p>
</td>
</tr>
<tr id="row1456418457016"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="p25648451403"><a name="p25648451403"></a><a name="p25648451403"></a>Associating a VPC with a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p1565134513013"><a name="p1565134513013"></a><a name="p1565134513013"></a>privateZone</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p1356534512018"><a name="p1356534512018"></a><a name="p1356534512018"></a>associateRouter</p>
</td>
</tr>
<tr id="row45652045506"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="p15653451706"><a name="p15653451706"></a><a name="p15653451706"></a>Disassociating a VPC from a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p456620451002"><a name="p456620451002"></a><a name="p456620451002"></a>privateZone</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p17566144511013"><a name="p17566144511013"></a><a name="p17566144511013"></a>disassociateRouter</p>
</td>
</tr>
<tr id="row0566945604"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="p156634515019"><a name="p156634515019"></a><a name="p156634515019"></a>Configuring a PTR record</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p1256612452007"><a name="p1256612452007"></a><a name="p1256612452007"></a>ptrRecord</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p85671845404"><a name="p85671845404"></a><a name="p85671845404"></a>setPTRRecord</p>
</td>
</tr>
<tr id="row135671445207"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="p18567745501"><a name="p18567745501"></a><a name="p18567745501"></a>Deleting a PTR record</p>
</td>
<td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p456854512013"><a name="p456854512013"></a><a name="p456854512013"></a>ptrRecord</p>
</td>
<td class="cellrowborder" valign="top" width="40.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p1856816459018"><a name="p1856816459018"></a><a name="p1856816459018"></a>resetPTRRecord</p>
</td>
</tr>
</tbody>
</table>

