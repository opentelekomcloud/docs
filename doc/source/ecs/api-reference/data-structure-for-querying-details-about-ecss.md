# Data Structure for Querying Details About ECSs<a name="EN-US_TOPIC_0169494074"></a>

**Table  1** **addresses**  parameters

<a name="en-us_topic_0057972887_table32893262"></a>
<table><thead align="left"><tr id="en-us_topic_0094148849_en-us_topic_0057972887_row1712624"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="en-us_topic_0094148849_p491416463113"><a name="en-us_topic_0094148849_p491416463113"></a><a name="en-us_topic_0094148849_p491416463113"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.4.1.2"><p id="en-us_topic_0094148849_p691414466112"><a name="en-us_topic_0094148849_p691414466112"></a><a name="en-us_topic_0094148849_p691414466112"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.59595959595959%" id="mcps1.2.4.1.3"><p id="en-us_topic_0094148849_p1931154611117"><a name="en-us_topic_0094148849_p1931154611117"></a><a name="en-us_topic_0094148849_p1931154611117"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094148849_en-us_topic_0057972887_row49962103"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p20398553"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p20398553"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p20398553"></a>Network information</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p1701193815159"><a name="p1701193815159"></a><a name="p1701193815159"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p34056575716"><a name="en-us_topic_0094148849_p34056575716"></a><a name="en-us_topic_0094148849_p34056575716"></a>Specifies the network information of the ECS.</p>
<a name="en-us_topic_0094148849_ul124201235982"></a><a name="en-us_topic_0094148849_ul124201235982"></a><ul id="en-us_topic_0094148849_ul124201235982"><li><strong id="b842352706214237"><a name="b842352706214237"></a><a name="b842352706214237"></a>key</strong> indicates the network name, for example, <strong id="b842352706214248"><a name="b842352706214248"></a><a name="b842352706214248"></a>demo_net</strong>.</li><li><strong id="b84235270615178"><a name="b84235270615178"></a><a name="b84235270615178"></a>value</strong> specifies detailed network information. For details, see <a href="#en-us_topic_0057972887_table23553967">Table 2</a>.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  2** **address**  parameters

<a name="en-us_topic_0057972887_table23553967"></a>
<table><thead align="left"><tr id="en-us_topic_0094148849_en-us_topic_0057972887_row13724749"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="en-us_topic_0094148849_p87136551517"><a name="en-us_topic_0094148849_p87136551517"></a><a name="en-us_topic_0094148849_p87136551517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.4.1.2"><p id="en-us_topic_0094148849_p9713155210"><a name="en-us_topic_0094148849_p9713155210"></a><a name="en-us_topic_0094148849_p9713155210"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.59595959595959%" id="mcps1.2.4.1.3"><p id="en-us_topic_0094148849_p1272913555114"><a name="en-us_topic_0094148849_p1272913555114"></a><a name="en-us_topic_0094148849_p1272913555114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094148849_en-us_topic_0057972887_row12502855"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p6098369"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p6098369"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p6098369"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p24205908"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p24205908"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p24205908"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p122951645487"><a name="en-us_topic_0094148849_p122951645487"></a><a name="en-us_topic_0094148849_p122951645487"></a>Specifies the IP address version.</p>
<a name="en-us_topic_0094148849_ul18833294914"></a><a name="en-us_topic_0094148849_ul18833294914"></a><ul id="en-us_topic_0094148849_ul18833294914"><li><strong id="b842352706152447"><a name="b842352706152447"></a><a name="b842352706152447"></a>4</strong>: indicates IPv4.</li><li><strong id="b1340524992232832"><a name="b1340524992232832"></a><a name="b1340524992232832"></a>6</strong>: indicates IPv6.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0094148849_en-us_topic_0057972887_row50089974"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p30756130"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p30756130"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p30756130"></a>addr</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p8218569"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p8218569"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p8218569"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p33618350"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p33618350"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p33618350"></a>Specifies the IP address.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_en-us_topic_0057972887_row34129699"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p13042201"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p13042201"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p13042201"></a>OS-EXT-IPS:type</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p49785360"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p49785360"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p49785360"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p112831815141110"><a name="en-us_topic_0094148849_p112831815141110"></a><a name="en-us_topic_0094148849_p112831815141110"></a>Specifies the IP address type.</p>
<a name="en-us_topic_0094148849_ul3596123318119"></a><a name="en-us_topic_0094148849_ul3596123318119"></a><ul id="en-us_topic_0094148849_ul3596123318119"><li><strong id="b842352706152629"><a name="b842352706152629"></a><a name="b842352706152629"></a>fixed</strong>: indicates the private IP address.</li><li><strong id="b842352706152642"><a name="b842352706152642"></a><a name="b842352706152642"></a>floating</strong>: indicates the floating IP address.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0094148849_en-us_topic_0057972887_row4849437"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p57260105"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p57260105"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p57260105"></a>OS-EXT-IPS-MAC:mac_addr</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p7556889"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p7556889"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p7556889"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p54408134"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p54408134"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p54408134"></a>Specifies the MAC address.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row17508182373712"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p850932318373"><a name="en-us_topic_0094148849_p850932318373"></a><a name="en-us_topic_0094148849_p850932318373"></a>OS-EXT-IPS:port_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p850942393715"><a name="en-us_topic_0094148849_p850942393715"></a><a name="en-us_topic_0094148849_p850942393715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p14509192313375"><a name="en-us_topic_0094148849_p14509192313375"></a><a name="en-us_topic_0094148849_p14509192313375"></a>Specifies the port ID corresponding to the IP address.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **flavor**  parameters

<a name="en-us_topic_0057972887_table41869715"></a>
<table><thead align="left"><tr id="en-us_topic_0094148849_en-us_topic_0057972887_row12766603"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="en-us_topic_0094148849_p1755513619211"><a name="en-us_topic_0094148849_p1755513619211"></a><a name="en-us_topic_0094148849_p1755513619211"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.4.1.2"><p id="en-us_topic_0094148849_p655516613217"><a name="en-us_topic_0094148849_p655516613217"></a><a name="en-us_topic_0094148849_p655516613217"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.59595959595959%" id="mcps1.2.4.1.3"><p id="en-us_topic_0094148849_p155516615214"><a name="en-us_topic_0094148849_p155516615214"></a><a name="en-us_topic_0094148849_p155516615214"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094148849_en-us_topic_0057972887_row57626186"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p37209478"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p37209478"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p37209478"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p61177702"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p61177702"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p61177702"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p8788275"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p8788275"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p8788275"></a>Specifies the ECS flavor ID.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row1387814161309"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p18782163307"><a name="en-us_topic_0094148849_p18782163307"></a><a name="en-us_topic_0094148849_p18782163307"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p178781416183015"><a name="en-us_topic_0094148849_p178781416183015"></a><a name="en-us_topic_0094148849_p178781416183015"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p587811615309"><a name="en-us_topic_0094148849_p587811615309"></a><a name="en-us_topic_0094148849_p587811615309"></a>Specifies the ECS flavor name.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row1247816451303"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p174781145103015"><a name="en-us_topic_0094148849_p174781145103015"></a><a name="en-us_topic_0094148849_p174781145103015"></a>disk</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p8478124516305"><a name="en-us_topic_0094148849_p8478124516305"></a><a name="en-us_topic_0094148849_p8478124516305"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p57975774173425"><a name="en-us_topic_0094148849_p57975774173425"></a><a name="en-us_topic_0094148849_p57975774173425"></a>Specifies the system disk size in the ECS flavor. The value <strong id="b71731215134611"><a name="b71731215134611"></a><a name="b71731215134611"></a>0</strong> indicates that the disk size is not limited.</p>
<p id="en-us_topic_0094148849_p52019925173425"><a name="en-us_topic_0094148849_p52019925173425"></a><a name="en-us_topic_0094148849_p52019925173425"></a>The field is invalid in this system.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row1052931914322"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p952919196325"><a name="en-us_topic_0094148849_p952919196325"></a><a name="en-us_topic_0094148849_p952919196325"></a>vcpus</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p3529101912324"><a name="en-us_topic_0094148849_p3529101912324"></a><a name="en-us_topic_0094148849_p3529101912324"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p57750575173425"><a name="en-us_topic_0094148849_p57750575173425"></a><a name="en-us_topic_0094148849_p57750575173425"></a>Specifies the number of vCPUs in the ECS flavor.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row2015565919321"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p3155165911323"><a name="en-us_topic_0094148849_p3155165911323"></a><a name="en-us_topic_0094148849_p3155165911323"></a>ram</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p2155115912322"><a name="en-us_topic_0094148849_p2155115912322"></a><a name="en-us_topic_0094148849_p2155115912322"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p10323939173425"><a name="en-us_topic_0094148849_p10323939173425"></a><a name="en-us_topic_0094148849_p10323939173425"></a>Specifies the memory size (MB) in the ECS flavor.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **security\_groups**  parameters

<a name="en-us_topic_0057972887_table38168783"></a>
<table><thead align="left"><tr id="en-us_topic_0094148849_en-us_topic_0057972887_row17184551"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="en-us_topic_0094148849_p1849312152027"><a name="en-us_topic_0094148849_p1849312152027"></a><a name="en-us_topic_0094148849_p1849312152027"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="en-us_topic_0094148849_p1051015154217"><a name="en-us_topic_0094148849_p1051015154217"></a><a name="en-us_topic_0094148849_p1051015154217"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="en-us_topic_0094148849_p1851019155217"><a name="en-us_topic_0094148849_p1851019155217"></a><a name="en-us_topic_0094148849_p1851019155217"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094148849_en-us_topic_0057972887_row52636849"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p35726411"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p35726411"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p35726411"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p8158206"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p8158206"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p8158206"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p40226508"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p40226508"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p40226508"></a>Specifies the security group name or UUID.</p>
</td>
</tr>
<tr id="row7752154019394"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p1175311408391"><a name="p1175311408391"></a><a name="p1175311408391"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p5753184023910"><a name="p5753184023910"></a><a name="p5753184023910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p7753184013916"><a name="p7753184013916"></a><a name="p7753184013916"></a>Specifies the security group ID.</p>
</td>
</tr>
</tbody>
</table>

The following table lists parameters involved in the fault information attribute.

**Table  5** **fault**  parameters

<a name="en-us_topic_0057972887_table37121720"></a>
<table><thead align="left"><tr id="en-us_topic_0094148849_en-us_topic_0057972887_row58298029"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="en-us_topic_0094148849_p16255251529"><a name="en-us_topic_0094148849_p16255251529"></a><a name="en-us_topic_0094148849_p16255251529"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="en-us_topic_0094148849_p10251225224"><a name="en-us_topic_0094148849_p10251225224"></a><a name="en-us_topic_0094148849_p10251225224"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.4.1.3"><p id="en-us_topic_0094148849_p141125127"><a name="en-us_topic_0094148849_p141125127"></a><a name="en-us_topic_0094148849_p141125127"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094148849_en-us_topic_0057972887_row13536050"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p22678235"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p22678235"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p22678235"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p24997708"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p24997708"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p24997708"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p63010216"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p63010216"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p63010216"></a>Specifies the fault information.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_en-us_topic_0057972887_row30221038"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p31985024"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p31985024"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p31985024"></a>code</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p40650175"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p40650175"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p40650175"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p15175522"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p15175522"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p15175522"></a>Specifies the error code.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_en-us_topic_0057972887_row2361972"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p57102025"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p57102025"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p57102025"></a>details</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p61861327"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p61861327"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p61861327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p64869644"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p64869644"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p64869644"></a>Specifies the fault details.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_en-us_topic_0057972887_row46955892"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p45330870"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p45330870"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p45330870"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p47921869"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p47921869"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p47921869"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p10360217"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p10360217"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p10360217"></a>Specifies the time when the fault occurred. The time is in ISO 8601 time format.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **os-extended-volumes:volumes\_attached**  parameters

<a name="en-us_topic_0057972887_table33871262"></a>
<table><thead align="left"><tr id="en-us_topic_0094148849_en-us_topic_0057972887_row5274317"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="en-us_topic_0094148849_p05289331529"><a name="en-us_topic_0094148849_p05289331529"></a><a name="en-us_topic_0094148849_p05289331529"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="en-us_topic_0094148849_p852818331627"><a name="en-us_topic_0094148849_p852818331627"></a><a name="en-us_topic_0094148849_p852818331627"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.4.1.3"><p id="en-us_topic_0094148849_p1352811334213"><a name="en-us_topic_0094148849_p1352811334213"></a><a name="en-us_topic_0094148849_p1352811334213"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094148849_en-us_topic_0057972887_row42725634"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p38224348"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p38224348"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p38224348"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p9164474"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p9164474"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p9164474"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p65684132"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p65684132"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p65684132"></a>Specifies the disk ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_en-us_topic_0057972887_row54286279"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p35112448"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p35112448"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p35112448"></a>delete_on_termination</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p25536001"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p25536001"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p25536001"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_en-us_topic_0057972887_p37980797"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p37980797"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p37980797"></a>Specifies whether the disk is deleted with the ECS.</p>
<a name="en-us_topic_0094148849_en-us_topic_0057972887_ul6282859"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_ul6282859"></a><ul id="en-us_topic_0094148849_en-us_topic_0057972887_ul6282859"><li><strong id="en-us_topic_0057972887_b809566892144429"><a name="en-us_topic_0057972887_b809566892144429"></a><a name="en-us_topic_0057972887_b809566892144429"></a>true</strong>: indicates that the disk is deleted with the ECS.</li><li><strong id="b15443849105714"><a name="b15443849105714"></a><a name="b15443849105714"></a>false</strong>: indicates that the disk is not deleted with the ECS.</li></ul>
<p id="en-us_topic_0094148849_en-us_topic_0057972887_p16801916"><a name="en-us_topic_0094148849_en-us_topic_0057972887_p16801916"></a><a name="en-us_topic_0094148849_en-us_topic_0057972887_p16801916"></a>This parameter is newly added in microversion 2.3.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row10694188445"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p2695189447"><a name="en-us_topic_0094148849_p2695189447"></a><a name="en-us_topic_0094148849_p2695189447"></a>bootIndex</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p669121810449"><a name="en-us_topic_0094148849_p669121810449"></a><a name="en-us_topic_0094148849_p669121810449"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p174792192520"><a name="p174792192520"></a><a name="p174792192520"></a>Specifies the EVS disk boot sequence.</p>
<a name="ul1147102112513"></a><a name="ul1147102112513"></a><ul id="ul1147102112513"><li><strong id="b842352706181942"><a name="b842352706181942"></a><a name="b842352706181942"></a>0</strong> indicates the system disk.</li><li>Non-<strong id="b842352706193244"><a name="b842352706193244"></a><a name="b842352706193244"></a>0</strong> indicates a data disk.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0094148849_row398716920453"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p7989159154510"><a name="en-us_topic_0094148849_p7989159154510"></a><a name="en-us_topic_0094148849_p7989159154510"></a>device</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p1898914916452"><a name="en-us_topic_0094148849_p1898914916452"></a><a name="en-us_topic_0094148849_p1898914916452"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_en-us_topic_0101860613_p1462819"><a name="en-us_topic_0094148849_en-us_topic_0101860613_p1462819"></a><a name="en-us_topic_0094148849_en-us_topic_0101860613_p1462819"></a>Specifies the drive letter of the EVS disk, which is the device name of the EVS disk.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **metadata**  parameters

<a name="table537485761711"></a>
<table><thead align="left"><tr id="en-us_topic_0094148849_row837535716176"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="en-us_topic_0094148849_p8463204610218"><a name="en-us_topic_0094148849_p8463204610218"></a><a name="en-us_topic_0094148849_p8463204610218"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="en-us_topic_0094148849_p94778464218"><a name="en-us_topic_0094148849_p94778464218"></a><a name="en-us_topic_0094148849_p94778464218"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.4.1.3"><p id="en-us_topic_0094148849_p7477446320"><a name="en-us_topic_0094148849_p7477446320"></a><a name="en-us_topic_0094148849_p7477446320"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094148849_row143751557161716"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p19375145713174"><a name="en-us_topic_0094148849_p19375145713174"></a><a name="en-us_topic_0094148849_p19375145713174"></a>charging_mode</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p17375115771713"><a name="en-us_topic_0094148849_p17375115771713"></a><a name="en-us_topic_0094148849_p17375115771713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p12375757181712"><a name="en-us_topic_0094148849_p12375757181712"></a><a name="en-us_topic_0094148849_p12375757181712"></a>Specifies the ECS billing mode.</p>
<a name="en-us_topic_0094148849_ul8337219192011"></a><a name="en-us_topic_0094148849_ul8337219192011"></a><ul id="en-us_topic_0094148849_ul8337219192011"><li><strong id="b8423527061775"><a name="b8423527061775"></a><a name="b8423527061775"></a>0</strong>: pay-per-use payment (postpaid)</li></ul>
</td>
</tr>
<tr id="en-us_topic_0094148849_row184449173712"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p44469173713"><a name="en-us_topic_0094148849_p44469173713"></a><a name="en-us_topic_0094148849_p44469173713"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p6441923711"><a name="en-us_topic_0094148849_p6441923711"></a><a name="en-us_topic_0094148849_p6441923711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p54411913713"><a name="en-us_topic_0094148849_p54411913713"></a><a name="en-us_topic_0094148849_p54411913713"></a>Specifies the ID of the VPC where an ECS is located.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row16375135761710"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p33751757151717"><a name="en-us_topic_0094148849_p33751757151717"></a><a name="en-us_topic_0094148849_p33751757151717"></a>EcmResStatus</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p937516577179"><a name="en-us_topic_0094148849_p937516577179"></a><a name="en-us_topic_0094148849_p937516577179"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p93751457191714"><a name="en-us_topic_0094148849_p93751457191714"></a><a name="en-us_topic_0094148849_p93751457191714"></a>Specifies the ECS frozen status.</p>
<a name="en-us_topic_0094148849_ul19491750191212"></a><a name="en-us_topic_0094148849_ul19491750191212"></a><ul id="en-us_topic_0094148849_ul19491750191212"><li><strong id="b84235270617117"><a name="b84235270617117"></a><a name="b84235270617117"></a>normal</strong>: The ECS is not frozen.</li><li><strong id="b842352706171139"><a name="b842352706171139"></a><a name="b842352706171139"></a>freeze</strong>: The ECS is frozen.</li></ul>
<div class="note" id="en-us_topic_0094148849_note858016558456"><a name="en-us_topic_0094148849_note858016558456"></a><a name="en-us_topic_0094148849_note858016558456"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0094148849_p2058217556458"><a name="en-us_topic_0094148849_p2058217556458"></a><a name="en-us_topic_0094148849_p2058217556458"></a>The system automatically adds this field, which is mandatory, after an ECS is frozen or unfrozen.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0094148849_row5767181932716"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p17767141922718"><a name="en-us_topic_0094148849_p17767141922718"></a><a name="en-us_topic_0094148849_p17767141922718"></a>metering.image_id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p47671319112715"><a name="en-us_topic_0094148849_p47671319112715"></a><a name="en-us_topic_0094148849_p47671319112715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p11767131942713"><a name="en-us_topic_0094148849_p11767131942713"></a><a name="en-us_topic_0094148849_p11767131942713"></a>Specifies the image ID of the ECS.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row77801029142717"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p5780629112713"><a name="en-us_topic_0094148849_p5780629112713"></a><a name="en-us_topic_0094148849_p5780629112713"></a>metering.imagetype</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p93301647102814"><a name="en-us_topic_0094148849_p93301647102814"></a><a name="en-us_topic_0094148849_p93301647102814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_en-us_topic_0020091567_p2572734285718"><a name="en-us_topic_0094148849_en-us_topic_0020091567_p2572734285718"></a><a name="en-us_topic_0094148849_en-us_topic_0020091567_p2572734285718"></a>Specifies the image type. The following types are supported:</p>
<a name="en-us_topic_0094148849_en-us_topic_0020091567_ul6291210685828"></a><a name="en-us_topic_0094148849_en-us_topic_0020091567_ul6291210685828"></a><ul id="en-us_topic_0094148849_en-us_topic_0020091567_ul6291210685828"><li>Public image: The value is <strong id="b842352706163515"><a name="b842352706163515"></a><a name="b842352706163515"></a>gold</strong>.</li><li>Private image: The value is <strong id="b1762610292163524"><a name="b1762610292163524"></a><a name="b1762610292163524"></a>private</strong>.</li><li>Shared image: The value is <strong id="b298092137163545"><a name="b298092137163545"></a><a name="b298092137163545"></a>shared</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0094148849_row1455173842715"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p75511838202716"><a name="en-us_topic_0094148849_p75511838202716"></a><a name="en-us_topic_0094148849_p75511838202716"></a>metering.resourcespeccode</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p1054493282"><a name="en-us_topic_0094148849_p1054493282"></a><a name="en-us_topic_0094148849_p1054493282"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p165519382274"><a name="en-us_topic_0094148849_p165519382274"></a><a name="en-us_topic_0094148849_p165519382274"></a>Specifies the resource specifications of the ECS.</p>
</td>
</tr>
<tr id="row15495156134810"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p194956654816"><a name="p194956654816"></a><a name="p194956654816"></a>metering.resourcetype</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p649516615483"><a name="p649516615483"></a><a name="p649516615483"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p16495146104819"><a name="p16495146104819"></a><a name="p16495146104819"></a>Specifies the resource type of the ECS.</p>
</td>
</tr>
<tr id="row027315675519"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p162733610555"><a name="p162733610555"></a><a name="p162733610555"></a>cascaded.instance_extrainfo</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p327317675511"><a name="p327317675511"></a><a name="p327317675511"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p727314611552"><a name="p727314611552"></a><a name="p727314611552"></a>Specifies the extended information about the internal ECSs.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row4296856102711"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p1729612561276"><a name="en-us_topic_0094148849_p1729612561276"></a><a name="en-us_topic_0094148849_p1729612561276"></a>image_name</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p197645332810"><a name="en-us_topic_0094148849_p197645332810"></a><a name="en-us_topic_0094148849_p197645332810"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p197232344210"><a name="en-us_topic_0094148849_p197232344210"></a><a name="en-us_topic_0094148849_p197232344210"></a>Specifies the image name of the ECS.</p>
</td>
</tr>
<tr id="row414413517513"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p8144155145110"><a name="p8144155145110"></a><a name="p8144155145110"></a>agency_name</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p201449510518"><a name="p201449510518"></a><a name="p201449510518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p0842044134818"><a name="p0842044134818"></a><a name="p0842044134818"></a>Specifies the IAM agency name.</p>
<p id="p9821153514191"><a name="p9821153514191"></a><a name="p9821153514191"></a>An agency is created by a tenant administrator on IAM to provide temporary credentials for ECSs to access cloud services.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row2066170288"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p15681722813"><a name="en-us_topic_0094148849_p15681722813"></a><a name="en-us_topic_0094148849_p15681722813"></a>os_bit</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p144731557162816"><a name="en-us_topic_0094148849_p144731557162816"></a><a name="en-us_topic_0094148849_p144731557162816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p66111720288"><a name="en-us_topic_0094148849_p66111720288"></a><a name="en-us_topic_0094148849_p66111720288"></a>Specifies the number of bits in the operating system: <strong id="b40089937144822"><a name="b40089937144822"></a><a name="b40089937144822"></a>32</strong> or <strong id="b25265115144822"><a name="b25265115144822"></a><a name="b25265115144822"></a>64</strong>.</p>
</td>
</tr>
<tr id="row1632761935919"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p43271919145918"><a name="p43271919145918"></a><a name="p43271919145918"></a>os_type</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p203276194595"><a name="p203276194595"></a><a name="p203276194595"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p8327319155914"><a name="p8327319155914"></a><a name="p8327319155914"></a>Specifies the OS type. The value can be <strong id="b198791036144120"><a name="b198791036144120"></a><a name="b198791036144120"></a>Linux</strong> or <strong id="b17885143684119"><a name="b17885143684119"></a><a name="b17885143684119"></a>Windows</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row2094193023412"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p5941330113415"><a name="en-us_topic_0094148849_p5941330113415"></a><a name="en-us_topic_0094148849_p5941330113415"></a>lockCheckEndpoint</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p994153010344"><a name="en-us_topic_0094148849_p994153010344"></a><a name="en-us_topic_0094148849_p994153010344"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p15790555145619"><a name="en-us_topic_0094148849_p15790555145619"></a><a name="en-us_topic_0094148849_p15790555145619"></a>Specifies the callback URL for checking whether ECS locking is enabled.</p>
<a name="en-us_topic_0094148849_ul758318166597"></a><a name="en-us_topic_0094148849_ul758318166597"></a><ul id="en-us_topic_0094148849_ul758318166597"><li>If ECS locking is enabled, the ECS is locked.</li><li>If ECS locking is disabled, the ECS is unlocked, and invalid locks are deleted.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0094148849_row56991916103513"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p2069971643513"><a name="en-us_topic_0094148849_p2069971643513"></a><a name="en-us_topic_0094148849_p2069971643513"></a>lockSource</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p1969910162358"><a name="en-us_topic_0094148849_p1969910162358"></a><a name="en-us_topic_0094148849_p1969910162358"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p76998167357"><a name="en-us_topic_0094148849_p76998167357"></a><a name="en-us_topic_0094148849_p76998167357"></a>Specifies the lock source.</p>
<a name="en-us_topic_0094148849_ul102341810125015"></a><a name="en-us_topic_0094148849_ul102341810125015"></a><ul id="en-us_topic_0094148849_ul102341810125015"><li>Order lock (<strong id="b842352706105517"><a name="b842352706105517"></a><a name="b842352706105517"></a>ORDER</strong>)</li></ul>
</td>
</tr>
<tr id="en-us_topic_0094148849_row349632173519"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p1849123243518"><a name="en-us_topic_0094148849_p1849123243518"></a><a name="en-us_topic_0094148849_p1849123243518"></a>lockSourceId</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p1049153253519"><a name="en-us_topic_0094148849_p1049153253519"></a><a name="en-us_topic_0094148849_p1049153253519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p204913273511"><a name="en-us_topic_0094148849_p204913273511"></a><a name="en-us_topic_0094148849_p204913273511"></a>Specifies the ECS lock source ID.</p>
<p id="en-us_topic_0094148849_p1422432714505"><a name="en-us_topic_0094148849_p1422432714505"></a><a name="en-us_topic_0094148849_p1422432714505"></a>If <strong id="b842352706105652"><a name="b842352706105652"></a><a name="b842352706105652"></a>lockSource</strong> is set to <strong id="b84235270610570"><a name="b84235270610570"></a><a name="b84235270610570"></a>ORDER</strong>, <strong id="b842352706105719"><a name="b842352706105719"></a><a name="b842352706105719"></a>lockSourceId</strong> is the order ID.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row28541251143515"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p158541510357"><a name="en-us_topic_0094148849_p158541510357"></a><a name="en-us_topic_0094148849_p158541510357"></a>lockScene</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p2854151133516"><a name="en-us_topic_0094148849_p2854151133516"></a><a name="en-us_topic_0094148849_p2854151133516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p118547517350"><a name="en-us_topic_0094148849_p118547517350"></a><a name="en-us_topic_0094148849_p118547517350"></a>Specifies the ECS lock type.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row98431053435"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p208441753132"><a name="en-us_topic_0094148849_p208441753132"></a><a name="en-us_topic_0094148849_p208441753132"></a>virtual_env_type</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p1844753337"><a name="en-us_topic_0094148849_p1844753337"></a><a name="en-us_topic_0094148849_p1844753337"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0094148849_ul526316514513"></a><a name="en-us_topic_0094148849_ul526316514513"></a><ul id="en-us_topic_0094148849_ul526316514513"><li>If an ECS is created using an iOS image, the value of this parameter is <strong id="b842352706184954"><a name="b842352706184954"></a><a name="b842352706184954"></a>IsoImage</strong>.</li><li>If an ECS is created using a non-iOS image, the value of this parameter is <strong id="b200790646618512"><a name="b200790646618512"></a><a name="b200790646618512"></a>FusionCompute</strong> in versions earlier than 19.5.0, and this parameter will be unavailable in versions later than 19.5.0.</li></ul>
<div class="note" id="en-us_topic_0094148849_note198629531362"><a name="en-us_topic_0094148849_note198629531362"></a><a name="en-us_topic_0094148849_note198629531362"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul1588823185411"></a><a name="ul1588823185411"></a><ul id="ul1588823185411"><li>The <strong id="b842352706185220"><a name="b842352706185220"></a><a name="b842352706185220"></a>virtual_env_type</strong> cannot be added, deleted, or modified.</li></ul>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  8** **sys\_tags**  parameters

<a name="table6690227839"></a>
<table><thead align="left"><tr id="en-us_topic_0094148849_row569012713315"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="en-us_topic_0094148849_p15534586216"><a name="en-us_topic_0094148849_p15534586216"></a><a name="en-us_topic_0094148849_p15534586216"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.4.1.2"><p id="en-us_topic_0094148849_p1055311581724"><a name="en-us_topic_0094148849_p1055311581724"></a><a name="en-us_topic_0094148849_p1055311581724"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.57575757575757%" id="mcps1.2.4.1.3"><p id="en-us_topic_0094148849_p556816581724"><a name="en-us_topic_0094148849_p556816581724"></a><a name="en-us_topic_0094148849_p556816581724"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094148849_row16690152710311"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p106901027938"><a name="en-us_topic_0094148849_p106901027938"></a><a name="en-us_topic_0094148849_p106901027938"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p156906275313"><a name="en-us_topic_0094148849_p156906275313"></a><a name="en-us_topic_0094148849_p156906275313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p1169012277310"><a name="en-us_topic_0094148849_p1169012277310"></a><a name="en-us_topic_0094148849_p1169012277310"></a>Specifies the system tag key.</p>
</td>
</tr>
<tr id="en-us_topic_0094148849_row206908271832"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p36906274317"><a name="en-us_topic_0094148849_p36906274317"></a><a name="en-us_topic_0094148849_p36906274317"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p10690112711311"><a name="en-us_topic_0094148849_p10690112711311"></a><a name="en-us_topic_0094148849_p10690112711311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p56913271231"><a name="en-us_topic_0094148849_p56913271231"></a><a name="en-us_topic_0094148849_p56913271231"></a>Specifies the system tag value.</p>
</td>
</tr>
</tbody>
</table>

**Table  9** **image**  parameters

<a name="table173259974818"></a>
<table><thead align="left"><tr id="en-us_topic_0094148849_row10326199174815"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="en-us_topic_0094148849_p0326796485"><a name="en-us_topic_0094148849_p0326796485"></a><a name="en-us_topic_0094148849_p0326796485"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="en-us_topic_0094148849_p203269914811"><a name="en-us_topic_0094148849_p203269914811"></a><a name="en-us_topic_0094148849_p203269914811"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.4.1.3"><p id="en-us_topic_0094148849_p232712912486"><a name="en-us_topic_0094148849_p232712912486"></a><a name="en-us_topic_0094148849_p232712912486"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094148849_row232716914481"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094148849_p3327189174818"><a name="en-us_topic_0094148849_p3327189174818"></a><a name="en-us_topic_0094148849_p3327189174818"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094148849_p18327129164817"><a name="en-us_topic_0094148849_p18327129164817"></a><a name="en-us_topic_0094148849_p18327129164817"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094148849_p16867106104914"><a name="en-us_topic_0094148849_p16867106104914"></a><a name="en-us_topic_0094148849_p16867106104914"></a>Specifies the image ID.</p>
</td>
</tr>
</tbody>
</table>

