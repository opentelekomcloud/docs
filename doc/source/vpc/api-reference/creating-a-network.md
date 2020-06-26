# Creating a Network<a name="vpc_network_0003"></a>

## Function<a name="section6414416120507"></a>

This API is used to create a network.

## URI<a name="section5332460720507"></a>

POST /v2.0/networks

## Request Message<a name="section4437514120507"></a>

**Table  1**  Request parameter

<a name="table3761670020507"></a>
<table><thead align="left"><tr id="row4177733320507"><th class="cellrowborder" valign="top" width="16.5%" id="mcps1.2.5.1.1"><p id="p2852081420507"><a name="p2852081420507"></a><a name="p2852081420507"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="10.51%" id="mcps1.2.5.1.2"><p id="p2848463220507"><a name="p2848463220507"></a><a name="p2848463220507"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.21%" id="mcps1.2.5.1.3"><p id="p2555388320507"><a name="p2555388320507"></a><a name="p2555388320507"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="54.779999999999994%" id="mcps1.2.5.1.4"><p id="p5659862220507"><a name="p5659862220507"></a><a name="p5659862220507"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2108564120507"><td class="cellrowborder" valign="top" width="16.5%" headers="mcps1.2.5.1.1 "><p id="p3021536520507"><a name="p3021536520507"></a><a name="p3021536520507"></a>network</p>
</td>
<td class="cellrowborder" valign="top" width="10.51%" headers="mcps1.2.5.1.2 "><p id="p3152549720507"><a name="p3152549720507"></a><a name="p3152549720507"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="18.21%" headers="mcps1.2.5.1.3 "><p id="p342849420507"><a name="p342849420507"></a><a name="p342849420507"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="54.779999999999994%" headers="mcps1.2.5.1.4 "><p id="p3740541204921"><a name="p3740541204921"></a><a name="p3740541204921"></a>Specifies the network list. For details, see <a href="#table49902238182444">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **network**  objects

<a name="table49902238182444"></a>
<table><thead align="left"><tr id="row27727643182444"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.5.1.1"><p id="p31346634182444"><a name="p31346634182444"></a><a name="p31346634182444"></a><strong id="b19584020732"><a name="b19584020732"></a><a name="b19584020732"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.66%" id="mcps1.2.5.1.2"><p id="p4702855164210"><a name="p4702855164210"></a><a name="p4702855164210"></a><strong id="b13928211635"><a name="b13928211635"></a><a name="b13928211635"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.28%" id="mcps1.2.5.1.3"><p id="p56049421182444"><a name="p56049421182444"></a><a name="p56049421182444"></a><strong id="b154372418310"><a name="b154372418310"></a><a name="b154372418310"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44.89%" id="mcps1.2.5.1.4"><p id="p32650631182444"><a name="p32650631182444"></a><a name="p32650631182444"></a><strong id="b1257814251634"><a name="b1257814251634"></a><a name="b1257814251634"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row64801111182444"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.5.1.1 "><p id="p14398613182444"><a name="p14398613182444"></a><a name="p14398613182444"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11.66%" headers="mcps1.2.5.1.2 "><p id="p070215513423"><a name="p070215513423"></a><a name="p070215513423"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.2.5.1.3 "><p id="p25436971182444"><a name="p25436971182444"></a><a name="p25436971182444"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.89%" headers="mcps1.2.5.1.4 "><p id="p59079578182444"><a name="p59079578182444"></a><a name="p59079578182444"></a>Specifies the network name.</p>
<p id="p4388171561813"><a name="p4388171561813"></a><a name="p4388171561813"></a>The name cannot be the same as the <strong id="b1959112318315"><a name="b1959112318315"></a><a name="b1959112318315"></a>admin_external_net</strong> value.</p>
</td>
</tr>
<tr id="row48951951182444"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.5.1.1 "><p id="p5685084182444"><a name="p5685084182444"></a><a name="p5685084182444"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="11.66%" headers="mcps1.2.5.1.2 "><p id="p1702155104218"><a name="p1702155104218"></a><a name="p1702155104218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.2.5.1.3 "><p id="p57838641182444"><a name="p57838641182444"></a><a name="p57838641182444"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="44.89%" headers="mcps1.2.5.1.4 "><p id="p52254844182444"><a name="p52254844182444"></a><a name="p52254844182444"></a>Specifies the administrative status.</p>
<p id="p06091419141817"><a name="p06091419141817"></a><a name="p06091419141817"></a>The value can only be <strong id="b20234617131917"><a name="b20234617131917"></a><a name="b20234617131917"></a>true</strong>.</p>
</td>
</tr>
<tr id="row62882662182444"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.5.1.1 "><p id="p60330876182444"><a name="p60330876182444"></a><a name="p60330876182444"></a>provider:network_type</p>
</td>
<td class="cellrowborder" valign="top" width="11.66%" headers="mcps1.2.5.1.2 "><p id="p870218554422"><a name="p870218554422"></a><a name="p870218554422"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.2.5.1.3 "><p id="p54962794182444"><a name="p54962794182444"></a><a name="p54962794182444"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.89%" headers="mcps1.2.5.1.4 "><p id="p3680057182444"><a name="p3680057182444"></a><a name="p3680057182444"></a>Specifies the network type. Only the VXLAN and GENEVE networks are supported. This is an extended attribute.</p>
<p id="p33120518182444"><a name="p33120518182444"></a><a name="p33120518182444"></a>Tenants can create only networks whose type is <strong id="b0860132412198"><a name="b0860132412198"></a><a name="b0860132412198"></a>geneve</strong>.</p>
</td>
</tr>
<tr id="row25641034212156"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.5.1.1 "><p id="p53737204212156"><a name="p53737204212156"></a><a name="p53737204212156"></a>port_security_enabled</p>
</td>
<td class="cellrowborder" valign="top" width="11.66%" headers="mcps1.2.5.1.2 "><p id="p17040552426"><a name="p17040552426"></a><a name="p17040552426"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.2.5.1.3 "><p id="p31320715212156"><a name="p31320715212156"></a><a name="p31320715212156"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="44.89%" headers="mcps1.2.5.1.4 "><p id="p34506445212156"><a name="p34506445212156"></a><a name="p34506445212156"></a>Specifies whether the security option is enabled for the port. If the option is not enabled, the security group and DHCP snooping settings of all VMs in the network do not take effect.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section1288473020507"></a>

**Table  3**  Response parameter

<a name="table3703017620507"></a>
<table><thead align="left"><tr id="row256778820507"><th class="cellrowborder" valign="top" width="21.59%" id="mcps1.2.4.1.1"><p id="p666426420507"><a name="p666426420507"></a><a name="p666426420507"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.63%" id="mcps1.2.4.1.2"><p id="p293447220507"><a name="p293447220507"></a><a name="p293447220507"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.78%" id="mcps1.2.4.1.3"><p id="p5993672520507"><a name="p5993672520507"></a><a name="p5993672520507"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2303659520507"><td class="cellrowborder" valign="top" width="21.59%" headers="mcps1.2.4.1.1 "><p id="p5402491720507"><a name="p5402491720507"></a><a name="p5402491720507"></a>network</p>
</td>
<td class="cellrowborder" valign="top" width="13.63%" headers="mcps1.2.4.1.2 "><p id="p1394218020507"><a name="p1394218020507"></a><a name="p1394218020507"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="64.78%" headers="mcps1.2.4.1.3 "><p id="p526423120507"><a name="p526423120507"></a><a name="p526423120507"></a>Specifies the network list. For details, see <a href="#table6247102344219">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **network**  objects

<a name="table6247102344219"></a>
<table><thead align="left"><tr id="row14248162384210"><th class="cellrowborder" valign="top" width="26.22737726227377%" id="mcps1.2.4.1.1"><p id="p2248523164214"><a name="p2248523164214"></a><a name="p2248523164214"></a><strong id="b46844120190"><a name="b46844120190"></a><a name="b46844120190"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.957704229577043%" id="mcps1.2.4.1.2"><p id="p17248823144212"><a name="p17248823144212"></a><a name="p17248823144212"></a><strong id="b18880114114197"><a name="b18880114114197"></a><a name="b18880114114197"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50.81491850814919%" id="mcps1.2.4.1.3"><p id="p424812319424"><a name="p424812319424"></a><a name="p424812319424"></a><strong id="b11700194231913"><a name="b11700194231913"></a><a name="b11700194231913"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row27455432182444"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p9297551182444"><a name="p9297551182444"></a><a name="p9297551182444"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p14904129182444"><a name="p14904129182444"></a><a name="p14904129182444"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p19312361182444"><a name="p19312361182444"></a><a name="p19312361182444"></a>Specifies the network status. The value can be <strong id="b223164541911"><a name="b223164541911"></a><a name="b223164541911"></a>ACTIVE</strong>, <strong id="b152424512193"><a name="b152424512193"></a><a name="b152424512193"></a>BUILD</strong>, <strong id="b1325114513191"><a name="b1325114513191"></a><a name="b1325114513191"></a>DOWN</strong>, or <strong id="b42744511194"><a name="b42744511194"></a><a name="b42744511194"></a>ERROR</strong>.</p>
</td>
</tr>
<tr id="row9248623114212"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p162482239429"><a name="p162482239429"></a><a name="p162482239429"></a>subnets</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p99761211840"><a name="p99761211840"></a><a name="p99761211840"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p024842334212"><a name="p024842334212"></a><a name="p024842334212"></a>Specifies IDs of the subnets associated with this network. The IDs are in a list.</p>
<p id="p14248172310421"><a name="p14248172310421"></a><a name="p14248172310421"></a>Only one subnet can be associated with each network.</p>
</td>
</tr>
<tr id="row13248152364216"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p32481523204218"><a name="p32481523204218"></a><a name="p32481523204218"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p152484235424"><a name="p152484235424"></a><a name="p152484235424"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p1924812236425"><a name="p1924812236425"></a><a name="p1924812236425"></a>Specifies the network name.</p>
<p id="p1024882310429"><a name="p1024882310429"></a><a name="p1024882310429"></a>The name cannot be <strong id="b885716546198"><a name="b885716546198"></a><a name="b885716546198"></a>admin_external_net</strong>.</p>
</td>
</tr>
<tr id="row12248172319421"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p1024820237420"><a name="p1024820237420"></a><a name="p1024820237420"></a>router:external</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p1224818233429"><a name="p1224818233429"></a><a name="p1224818233429"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p524892316421"><a name="p524892316421"></a><a name="p524892316421"></a>Specifies whether the network is an external network. This is an extended attribute.</p>
</td>
</tr>
<tr id="row1224892334218"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p624922324214"><a name="p624922324214"></a><a name="p624922324214"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p112495230424"><a name="p112495230424"></a><a name="p112495230424"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p1224915239422"><a name="p1224915239422"></a><a name="p1224915239422"></a>Specifies the administrative status.</p>
<p id="p1249123124216"><a name="p1249123124216"></a><a name="p1249123124216"></a>The value can only be <strong id="b1671174912194"><a name="b1671174912194"></a><a name="b1671174912194"></a>true</strong>.</p>
</td>
</tr>
<tr id="row19249162311423"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p1824952318429"><a name="p1824952318429"></a><a name="p1824952318429"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p1624982334213"><a name="p1624982334213"></a><a name="p1624982334213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row112491923134217"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p324952384219"><a name="p324952384219"></a><a name="p324952384219"></a>shared</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p324982313422"><a name="p324982313422"></a><a name="p324982313422"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p8249182374211"><a name="p8249182374211"></a><a name="p8249182374211"></a>Specifies whether the firewall rule can be shared by different tenants.</p>
</td>
</tr>
<tr id="row31409028182444"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p61103330182444"><a name="p61103330182444"></a><a name="p61103330182444"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p50422701182444"><a name="p50422701182444"></a><a name="p50422701182444"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p31263412182444"><a name="p31263412182444"></a><a name="p31263412182444"></a>Specifies the network ID.</p>
<p id="p311313148445"><a name="p311313148445"></a><a name="p311313148445"></a>This parameter is not mandatory when you query networks.</p>
</td>
</tr>
<tr id="row925022315429"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p17250102320423"><a name="p17250102320423"></a><a name="p17250102320423"></a>provider:network_type</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p225015239424"><a name="p225015239424"></a><a name="p225015239424"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p92506237428"><a name="p92506237428"></a><a name="p92506237428"></a>Specifies the network type. Only the VXLAN and GENEVE networks are supported. This is an extended attribute.</p>
<p id="p16250923104212"><a name="p16250923104212"></a><a name="p16250923104212"></a>Tenants can create only networks whose type is <strong id="b10181194382014"><a name="b10181194382014"></a><a name="b10181194382014"></a>geneve</strong>.</p>
</td>
</tr>
<tr id="row1325022310421"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p525082310429"><a name="p525082310429"></a><a name="p525082310429"></a>availability_zone_hints</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p1225017233429"><a name="p1225017233429"></a><a name="p1225017233429"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p125016235427"><a name="p125016235427"></a><a name="p125016235427"></a>Specifies the availability zones available to this network. The current version does not support cross-availability-zone network scheduling.</p>
</td>
</tr>
<tr id="row425010232428"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p10250192394215"><a name="p10250192394215"></a><a name="p10250192394215"></a>availability_zones</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p42509234421"><a name="p42509234421"></a><a name="p42509234421"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p3250152312424"><a name="p3250152312424"></a><a name="p3250152312424"></a>Specifies the availability zone of this network.</p>
</td>
</tr>
<tr id="row172501323104212"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p2025042313422"><a name="p2025042313422"></a><a name="p2025042313422"></a>port_security_enabled</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p1025082354210"><a name="p1025082354210"></a><a name="p1025082354210"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p9250172394214"><a name="p9250172394214"></a><a name="p9250172394214"></a>Specifies whether the security option is enabled for the port. If the option is not enabled, the security group and DHCP snooping settings of all VMs in the network do not take effect.</p>
</td>
</tr>
<tr id="row421706155213"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p14217767523"><a name="p14217767523"></a><a name="p14217767523"></a>dns_domain</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p22172685219"><a name="p22172685219"></a><a name="p22172685219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p021812614525"><a name="p021812614525"></a><a name="p021812614525"></a>Specifies the default private network DNS domain address. The system automatically sets this parameter, and you are not allowed to configure or change the parameter value.</p>
</td>
</tr>
<tr id="row1312882941114"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p15700614790"><a name="p15700614790"></a><a name="p15700614790"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p337222914248"><a name="p337222914248"></a><a name="p337222914248"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row9120034101119"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the network is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i1401135542110"><a name="i1401135542110"></a><a name="i1401135542110"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1542863714112"><td class="cellrowborder" valign="top" width="26.22737726227377%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="22.957704229577043%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.81491850814919%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the network is updated.</p>
<p id="p071214111465"><a name="p071214111465"></a><a name="p071214111465"></a>Format: <em id="i149301059152112"><a name="i149301059152112"></a><a name="i149301059152112"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section4737808120507"></a>

Example request

```
POST https://{Endpoint}/v2.0/networks 

{
    "network": {
           "name": "network-test",
           "shared": false,
           "admin_state_up": true
    }
}
```

Example response

```
{
    "network": {
        "id": "c360322d-5315-45d7-b7d2-481f98c56edb",
        "name": "network-test",
        "status": "ACTIVE",
        "shared": false,
        "subnets": [],
        "availability_zone_hints": [],
        "availability_zones": [
            "az2.dc2",
            "az5.dc5"
        ],
        "admin_state_up": true,
        "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
        "provider:network_type": "vxlan",
        "router:external": false,
        "port_security_enabled": true,
        "created_at": "2018-09-20T01:53:18",
        "updated_at": "2018-09-20T01:53:20"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

