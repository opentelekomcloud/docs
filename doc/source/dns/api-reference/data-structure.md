# Data Structure<a name="dns_api_80006"></a>

**Table  1**  Description of the  **links**  field

<a name="table0172144213344"></a>
<table><thead align="left"><tr id="row917304253418"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p101731742153416"><a name="p101731742153416"></a><a name="p101731742153416"></a><strong id="b1272512714015"><a name="b1272512714015"></a><a name="b1272512714015"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.25%" id="mcps1.2.4.1.2"><p id="p0174542163418"><a name="p0174542163418"></a><a name="p0174542163418"></a><strong id="b474282814011"><a name="b474282814011"></a><a name="b474282814011"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="62.74999999999999%" id="mcps1.2.4.1.3"><p id="p7174194243414"><a name="p7174194243414"></a><a name="p7174194243414"></a><strong id="b1356514305010"><a name="b1356514305010"></a><a name="b1356514305010"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1390694871216"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p8907184881217"><a name="p8907184881217"></a><a name="p8907184881217"></a>self</p>
</td>
<td class="cellrowborder" valign="top" width="19.25%" headers="mcps1.2.4.1.2 "><p id="p9907184891219"><a name="p9907184891219"></a><a name="p9907184891219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.74999999999999%" headers="mcps1.2.4.1.3 "><p id="p1890754813127"><a name="p1890754813127"></a><a name="p1890754813127"></a>Link to the current resource</p>
</td>
</tr>
<tr id="row15778204719370"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p136561245153620"><a name="p136561245153620"></a><a name="p136561245153620"></a>next</p>
</td>
<td class="cellrowborder" valign="top" width="19.25%" headers="mcps1.2.4.1.2 "><p id="p19656144517367"><a name="p19656144517367"></a><a name="p19656144517367"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.74999999999999%" headers="mcps1.2.4.1.3 "><p id="p76567451365"><a name="p76567451365"></a><a name="p76567451365"></a>Link to the next page</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Description of the  **tag**  field

<a name="table19530794112436"></a>
<table><thead align="left"><tr id="row15361836112436"><th class="cellrowborder" valign="top" width="18.011801180118013%" id="mcps1.2.4.1.1"><p id="p58707511112436"><a name="p58707511112436"></a><a name="p58707511112436"></a><strong id="b129171645401"><a name="b129171645401"></a><a name="b129171645401"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.28192819281928%" id="mcps1.2.4.1.2"><p id="p42210623112436"><a name="p42210623112436"></a><a name="p42210623112436"></a><strong id="b117891464017"><a name="b117891464017"></a><a name="b117891464017"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="62.70627062706271%" id="mcps1.2.4.1.3"><p id="p63617265112436"><a name="p63617265112436"></a><a name="p63617265112436"></a><strong id="b15591647504"><a name="b15591647504"></a><a name="b15591647504"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row35684479112436"><td class="cellrowborder" valign="top" width="18.011801180118013%" headers="mcps1.2.4.1.1 "><p id="p13313439112530"><a name="p13313439112530"></a><a name="p13313439112530"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="19.28192819281928%" headers="mcps1.2.4.1.2 "><p id="p35653193112436"><a name="p35653193112436"></a><a name="p35653193112436"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.70627062706271%" headers="mcps1.2.4.1.3 "><p id="p48921437201850"><a name="p48921437201850"></a><a name="p48921437201850"></a>Tag key. The key contains 36 Unicode characters at most and cannot be blank. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
</td>
</tr>
<tr id="row20048002112436"><td class="cellrowborder" valign="top" width="18.011801180118013%" headers="mcps1.2.4.1.1 "><p id="p66095544112533"><a name="p66095544112533"></a><a name="p66095544112533"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="19.28192819281928%" headers="mcps1.2.4.1.2 "><p id="p60123528112436"><a name="p60123528112436"></a><a name="p60123528112436"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.70627062706271%" headers="mcps1.2.4.1.3 "><p id="p61714725112922"><a name="p61714725112922"></a><a name="p61714725112922"></a>Tag value. Each value contains 43 Unicode characters at most and can be an empty string. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Description of the  **router**  field

<a name="table4448008117179"></a>
<table><thead align="left"><tr id="row6132935617179"><th class="cellrowborder" valign="top" width="18.099999999999998%" id="mcps1.2.4.1.1"><p id="p36588677171719"><a name="p36588677171719"></a><a name="p36588677171719"></a><strong id="b1852811451429"><a name="b1852811451429"></a><a name="b1852811451429"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.37%" id="mcps1.2.4.1.2"><p id="p9906869171719"><a name="p9906869171719"></a><a name="p9906869171719"></a><strong id="b344718467213"><a name="b344718467213"></a><a name="b344718467213"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="62.529999999999994%" id="mcps1.2.4.1.3"><p id="p64258954171719"><a name="p64258954171719"></a><a name="p64258954171719"></a><strong id="b928115474211"><a name="b928115474211"></a><a name="b928115474211"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row266872817179"><td class="cellrowborder" valign="top" width="18.099999999999998%" headers="mcps1.2.4.1.1 "><p id="p25118582171719"><a name="p25118582171719"></a><a name="p25118582171719"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.37%" headers="mcps1.2.4.1.2 "><p id="p50755907171719"><a name="p50755907171719"></a><a name="p50755907171719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.529999999999994%" headers="mcps1.2.4.1.3 "><p id="p17587794171719"><a name="p17587794171719"></a><a name="p17587794171719"></a>ID of the associated VPC</p>
<p id="p143411822947"><a name="p143411822947"></a><a name="p143411822947"></a>You can obtain the VPC ID using the following methods:</p>
<a name="ul1938314911411"></a><a name="ul1938314911411"></a><ul id="ul1938314911411"><li>On the VPC console, obtain the VPC ID on the VPC details page.</li><li>Obtain the VPC ID according to "Querying VPCs" in <em id="i571271913167"><a name="i571271913167"></a><a name="i571271913167"></a>Virtual Private Cloud User Guide</em>.</li></ul>
</td>
</tr>
<tr id="row6657832817179"><td class="cellrowborder" valign="top" width="18.099999999999998%" headers="mcps1.2.4.1.1 "><p id="p3709384171719"><a name="p3709384171719"></a><a name="p3709384171719"></a>router_region</p>
</td>
<td class="cellrowborder" valign="top" width="19.37%" headers="mcps1.2.4.1.2 "><p id="p43861924171719"><a name="p43861924171719"></a><a name="p43861924171719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.529999999999994%" headers="mcps1.2.4.1.3 "><p id="p63154928171719"><a name="p63154928171719"></a><a name="p63154928171719"></a>Region of the VPC</p>
<p id="p38645142171939"><a name="p38645142171939"></a><a name="p38645142171939"></a>If it is left blank, the region of the project in the token takes effect by default.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Description of the  **alias\_target**  field

<a name="table11888161342410"></a>
<table><thead align="left"><tr id="row18392181415485"><th class="cellrowborder" valign="top" width="18.011801180118013%" id="mcps1.2.4.1.1"><p id="p183921314184812"><a name="p183921314184812"></a><a name="p183921314184812"></a><strong id="b14552431318"><a name="b14552431318"></a><a name="b14552431318"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.28192819281928%" id="mcps1.2.4.1.2"><p id="p439210145483"><a name="p439210145483"></a><a name="p439210145483"></a><strong id="b119000431315"><a name="b119000431315"></a><a name="b119000431315"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="62.70627062706271%" id="mcps1.2.4.1.3"><p id="p23921149482"><a name="p23921149482"></a><a name="p23921149482"></a><strong id="b47765443312"><a name="b47765443312"></a><a name="b47765443312"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row11392714154811"><td class="cellrowborder" valign="top" width="18.011801180118013%" headers="mcps1.2.4.1.1 "><p id="p1939231417484"><a name="p1939231417484"></a><a name="p1939231417484"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="19.28192819281928%" headers="mcps1.2.4.1.2 "><p id="p163922014164812"><a name="p163922014164812"></a><a name="p163922014164812"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.70627062706271%" headers="mcps1.2.4.1.3 "><p id="p33931814104817"><a name="p33931814104817"></a><a name="p33931814104817"></a>Service that support domain name aliases</p>
<p id="p589419319282"><a name="p589419319282"></a><a name="p589419319282"></a>The value can be <strong id="b12478331544"><a name="b12478331544"></a><a name="b12478331544"></a>cloudsite</strong> or <strong id="b9693113618418"><a name="b9693113618418"></a><a name="b9693113618418"></a>waf</strong> (Web Application Firewall).</p>
</td>
</tr>
<tr id="row16393414184815"><td class="cellrowborder" valign="top" width="18.011801180118013%" headers="mcps1.2.4.1.1 "><p id="p5393181418489"><a name="p5393181418489"></a><a name="p5393181418489"></a>resource_domain_name</p>
</td>
<td class="cellrowborder" valign="top" width="19.28192819281928%" headers="mcps1.2.4.1.2 "><p id="p8393181414818"><a name="p8393181414818"></a><a name="p8393181414818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.70627062706271%" headers="mcps1.2.4.1.3 "><p id="p339318146487"><a name="p339318146487"></a><a name="p339318146487"></a>Domain name of the target service</p>
</td>
</tr>
</tbody>
</table>

