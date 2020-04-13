# Creating a DNAT Rule<a name="nat_api_0011"></a>

## Function<a name="section2213133217038"></a>

This API is used to create a DNAT rule.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You can create a DNAT rule only when  **status**  of the NAT gateway is set to  **ACTIVE**  and  **admin\_state\_up**  of the NAT gateway administrator to  **True**. Either  **port\_id**  or  **private\_ip**  is used each time. If you create a rule that applies to all port types, set  **internal\_service\_port**  to  **0**,  **external\_service\_port**  to  **0**, and  **protocol**  to  **ANY**.  

## URI<a name="section2631225217131"></a>

POST /v2.0/dnat\_rules

## Request<a name="section1572764517510"></a>

[Table 1](#table19385203615518)  lists the request parameters.

**Table  1**  Request parameter

<a name="table19385203615518"></a>
<table><thead align="left"><tr id="row7697336175113"><th class="cellrowborder" valign="top" width="21.19%" id="mcps1.2.5.1.1"><p id="p969713363516"><a name="p969713363516"></a><a name="p969713363516"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.29%" id="mcps1.2.5.1.2"><p id="p1269717362514"><a name="p1269717362514"></a><a name="p1269717362514"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.02%" id="mcps1.2.5.1.3"><p id="p269717363519"><a name="p269717363519"></a><a name="p269717363519"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.5%" id="mcps1.2.5.1.4"><p id="p176971936105117"><a name="p176971936105117"></a><a name="p176971936105117"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4697436175118"><td class="cellrowborder" valign="top" width="21.19%" headers="mcps1.2.5.1.1 "><p id="p96971336105112"><a name="p96971336105112"></a><a name="p96971336105112"></a>dnat_rule</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.2 "><p id="p7697436175113"><a name="p7697436175113"></a><a name="p7697436175113"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.02%" headers="mcps1.2.5.1.3 "><p id="p1869713366514"><a name="p1869713366514"></a><a name="p1869713366514"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.5%" headers="mcps1.2.5.1.4 "><p id="p14697113614518"><a name="p14697113614518"></a><a name="p14697113614518"></a>Specifies the DNAT rule object. For details, see <a href="#table132796437212">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Description of the  **dnat\_rule**  field

<a name="table132796437212"></a>
<table><thead align="left"><tr id="row184049431027"><th class="cellrowborder" valign="top" width="20.919999999999998%" id="mcps1.2.5.1.1"><p id="p14043431726"><a name="p14043431726"></a><a name="p14043431726"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.29%" id="mcps1.2.5.1.2"><p id="p154049430210"><a name="p154049430210"></a><a name="p154049430210"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.02%" id="mcps1.2.5.1.3"><p id="p1740416433219"><a name="p1740416433219"></a><a name="p1740416433219"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.769999999999996%" id="mcps1.2.5.1.4"><p id="p240420437215"><a name="p240420437215"></a><a name="p240420437215"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row134041433214"><td class="cellrowborder" valign="top" width="20.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p164043431129"><a name="p164043431129"></a><a name="p164043431129"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.2 "><p id="p1140424312213"><a name="p1140424312213"></a><a name="p1140424312213"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.02%" headers="mcps1.2.5.1.3 "><p id="p8404443921"><a name="p8404443921"></a><a name="p8404443921"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.769999999999996%" headers="mcps1.2.5.1.4 "><p id="p1440494313213"><a name="p1440494313213"></a><a name="p1440494313213"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
<tr id="row040412436218"><td class="cellrowborder" valign="top" width="20.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p19404204314213"><a name="p19404204314213"></a><a name="p19404204314213"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.2 "><p id="p154048432027"><a name="p154048432027"></a><a name="p154048432027"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.02%" headers="mcps1.2.5.1.3 "><p id="p540414431823"><a name="p540414431823"></a><a name="p540414431823"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.769999999999996%" headers="mcps1.2.5.1.4 "><p id="p86078310224"><a name="p86078310224"></a><a name="p86078310224"></a>Specifies the port ID of an ECS or a BMS. This parameter and <strong id="b36401438161616"><a name="b36401438161616"></a><a name="b36401438161616"></a>private_ip</strong> are alternative.</p>
<p id="p19185113282111"><a name="p19185113282111"></a><a name="p19185113282111"></a>When the DNAT rule is used in the VPC scenario, use this parameter.</p>
<p id="p13404243429"><a name="p13404243429"></a><a name="p13404243429"></a></p>
</td>
</tr>
<tr id="row14041643528"><td class="cellrowborder" valign="top" width="20.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p740415432025"><a name="p740415432025"></a><a name="p740415432025"></a>private_ip</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.2 "><p id="p12404194314216"><a name="p12404194314216"></a><a name="p12404194314216"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.02%" headers="mcps1.2.5.1.3 "><p id="p184045434218"><a name="p184045434218"></a><a name="p184045434218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.769999999999996%" headers="mcps1.2.5.1.4 "><p id="p84041843221"><a name="p84041843221"></a><a name="p84041843221"></a>Specifies the private IP address, for example, the IP address of a Direct Connect connection. This parameter and <strong id="b1420810186186"><a name="b1420810186186"></a><a name="b1420810186186"></a>port_id</strong> are alternative.</p>
<p id="p675545942210"><a name="p675545942210"></a><a name="p675545942210"></a>When the DNAT rule is used in the Direct Connect scenario, use this parameter.</p>
</td>
</tr>
<tr id="row16404204313220"><td class="cellrowborder" valign="top" width="20.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p5404144313210"><a name="p5404144313210"></a><a name="p5404144313210"></a>internal_service_port</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.2 "><p id="p64041431726"><a name="p64041431726"></a><a name="p64041431726"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.02%" headers="mcps1.2.5.1.3 "><p id="p740413431823"><a name="p740413431823"></a><a name="p740413431823"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.769999999999996%" headers="mcps1.2.5.1.4 "><p id="p1740419431628"><a name="p1740419431628"></a><a name="p1740419431628"></a>Specifies the port used by ECSs or BMSs to provide services for external systems. In the VPC scenario, this parameter indicates the NIC port of the ECS or BMS associated with the DNAT rule. In the Direct Connect scenario, this parameter indicates the port of the private IP address of the DNAT rule.</p>
<p id="p223280102618"><a name="p223280102618"></a><a name="p223280102618"></a>The value ranges from 0 to 65535.</p>
</td>
</tr>
<tr id="row14404174310215"><td class="cellrowborder" valign="top" width="20.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p19404343926"><a name="p19404343926"></a><a name="p19404343926"></a>floating_ip_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.2 "><p id="p144048432217"><a name="p144048432217"></a><a name="p144048432217"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.02%" headers="mcps1.2.5.1.3 "><p id="p240484314213"><a name="p240484314213"></a><a name="p240484314213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.769999999999996%" headers="mcps1.2.5.1.4 "><p id="p1404343021"><a name="p1404343021"></a><a name="p1404343021"></a>Specifies the EIP ID. </p>
</td>
</tr>
<tr id="row74041243421"><td class="cellrowborder" valign="top" width="20.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p1440444312219"><a name="p1440444312219"></a><a name="p1440444312219"></a>external_service_port</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.2 "><p id="p1740404311216"><a name="p1740404311216"></a><a name="p1740404311216"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.02%" headers="mcps1.2.5.1.3 "><p id="p64041430217"><a name="p64041430217"></a><a name="p64041430217"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.769999999999996%" headers="mcps1.2.5.1.4 "><p id="p1140419436216"><a name="p1140419436216"></a><a name="p1140419436216"></a>Specifies the port for providing external services.</p>
<p id="p47430417266"><a name="p47430417266"></a><a name="p47430417266"></a>The value ranges from 0 to 65535.</p>
</td>
</tr>
<tr id="row1040494319212"><td class="cellrowborder" valign="top" width="20.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p740414312213"><a name="p740414312213"></a><a name="p740414312213"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="12.29%" headers="mcps1.2.5.1.2 "><p id="p34041343627"><a name="p34041343627"></a><a name="p34041343627"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.02%" headers="mcps1.2.5.1.3 "><p id="p1440414314215"><a name="p1440414314215"></a><a name="p1440414314215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.769999999999996%" headers="mcps1.2.5.1.4 "><p id="p1740415431329"><a name="p1740415431329"></a><a name="p1740415431329"></a>Specifies the protocol type. Currently, TCP, UDP, and ANY are supported.</p>
<p id="p2404114317211"><a name="p2404114317211"></a><a name="p2404114317211"></a>The protocol number of TCP, UDP, and ANY are 6, 17, and 0, respectively.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>To map all ports, set  **internal\_service\_port**  and  **external\_service\_port**  to  **0**  and  **protocol**  to  **ANY**  or  **0**.  

## Response<a name="section4576293817529"></a>

[Table 3](#table4946919917549)  lists response parameters.

**Table  3**  Response parameter

<a name="table4946919917549"></a>
<table><thead align="left"><tr id="row3265693817549"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p2796632617549"><a name="p2796632617549"></a><a name="p2796632617549"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.2"><p id="p5067993017549"><a name="p5067993017549"></a><a name="p5067993017549"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.4.1.3"><p id="p5371412517549"><a name="p5371412517549"></a><a name="p5371412517549"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5587684317549"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p2973040117549"><a name="p2973040117549"></a><a name="p2973040117549"></a>dnat_rule</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p5935228017549"><a name="p5935228017549"></a><a name="p5935228017549"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p4468272717549"><a name="p4468272717549"></a><a name="p4468272717549"></a>Specifies the DNAT rule object. For details, see <a href="#table1730611321529">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Description of the  **dnat\_rule**  field

<a name="table1730611321529"></a>
<table><thead align="left"><tr id="row1530623213215"><th class="cellrowborder" valign="top" width="24.152415241524153%" id="mcps1.2.4.1.1"><p id="p78428281539"><a name="p78428281539"></a><a name="p78428281539"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.072807280728075%" id="mcps1.2.4.1.2"><p id="p6842132819314"><a name="p6842132819314"></a><a name="p6842132819314"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.774777477747776%" id="mcps1.2.4.1.3"><p id="p1384232814313"><a name="p1384232814313"></a><a name="p1384232814313"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row183067321216"><td class="cellrowborder" valign="top" width="24.152415241524153%" headers="mcps1.2.4.1.1 "><p id="p1684216281036"><a name="p1684216281036"></a><a name="p1684216281036"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.072807280728075%" headers="mcps1.2.4.1.2 "><p id="p1884242812310"><a name="p1884242812310"></a><a name="p1884242812310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><p id="p08422281337"><a name="p08422281337"></a><a name="p08422281337"></a>Specifies the DNAT rule ID.</p>
</td>
</tr>
<tr id="row530610328215"><td class="cellrowborder" valign="top" width="24.152415241524153%" headers="mcps1.2.4.1.1 "><p id="p10842228633"><a name="p10842228633"></a><a name="p10842228633"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.072807280728075%" headers="mcps1.2.4.1.2 "><p id="p1284214286314"><a name="p1284214286314"></a><a name="p1284214286314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><p id="p1842172811317"><a name="p1842172811317"></a><a name="p1842172811317"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row1230612322216"><td class="cellrowborder" valign="top" width="24.152415241524153%" headers="mcps1.2.4.1.1 "><p id="p68422281533"><a name="p68422281533"></a><a name="p68422281533"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.072807280728075%" headers="mcps1.2.4.1.2 "><p id="p7842028439"><a name="p7842028439"></a><a name="p7842028439"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><p id="p188422286314"><a name="p188422286314"></a><a name="p188422286314"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
<tr id="row93061232920"><td class="cellrowborder" valign="top" width="24.152415241524153%" headers="mcps1.2.4.1.1 "><p id="p18429281134"><a name="p18429281134"></a><a name="p18429281134"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.072807280728075%" headers="mcps1.2.4.1.2 "><p id="p19842152810314"><a name="p19842152810314"></a><a name="p19842152810314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><p id="p145561716582"><a name="p145561716582"></a><a name="p145561716582"></a>Specifies the port ID of an ECS or a BMS. This parameter is used in the VPC scenario. This parameter and <strong id="b1597534911434"><a name="b1597534911434"></a><a name="b1597534911434"></a>private_ip</strong> are alternative.</p>
</td>
</tr>
<tr id="row93061325220"><td class="cellrowborder" valign="top" width="24.152415241524153%" headers="mcps1.2.4.1.1 "><p id="p384216281635"><a name="p384216281635"></a><a name="p384216281635"></a>private_ip</p>
</td>
<td class="cellrowborder" valign="top" width="28.072807280728075%" headers="mcps1.2.4.1.2 "><p id="p1384220280311"><a name="p1384220280311"></a><a name="p1384220280311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><p id="p1247121916108"><a name="p1247121916108"></a><a name="p1247121916108"></a>Specifies the IP address of a Direct Connect connection.</p>
<p id="p192471019141012"><a name="p192471019141012"></a><a name="p192471019141012"></a>This parameter is used in the Direct Connect scenario. This parameter and <strong id="b8607127593"><a name="b8607127593"></a><a name="b8607127593"></a>port_id</strong> are alternative.</p>
</td>
</tr>
<tr id="row930619322026"><td class="cellrowborder" valign="top" width="24.152415241524153%" headers="mcps1.2.4.1.1 "><p id="p1984218280319"><a name="p1984218280319"></a><a name="p1984218280319"></a>internal_service_port</p>
</td>
<td class="cellrowborder" valign="top" width="28.072807280728075%" headers="mcps1.2.4.1.2 "><p id="p11842928334"><a name="p11842928334"></a><a name="p11842928334"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><p id="p284210281312"><a name="p284210281312"></a><a name="p284210281312"></a>Specifies the port used by ECSs or BMSs to provide services for external systems.</p>
</td>
</tr>
<tr id="row0306133219211"><td class="cellrowborder" valign="top" width="24.152415241524153%" headers="mcps1.2.4.1.1 "><p id="p1184216281632"><a name="p1184216281632"></a><a name="p1184216281632"></a>floating_ip_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.072807280728075%" headers="mcps1.2.4.1.2 "><p id="p1484210288313"><a name="p1484210288313"></a><a name="p1484210288313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><p id="p384214281237"><a name="p384214281237"></a><a name="p384214281237"></a>Specifies the EIP ID.</p>
</td>
</tr>
<tr id="row1530611323214"><td class="cellrowborder" valign="top" width="24.152415241524153%" headers="mcps1.2.4.1.1 "><p id="p745117426320"><a name="p745117426320"></a><a name="p745117426320"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="28.072807280728075%" headers="mcps1.2.4.1.2 "><p id="p545119422037"><a name="p545119422037"></a><a name="p545119422037"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><p id="p12451642538"><a name="p12451642538"></a><a name="p12451642538"></a>Specifies the EIP.</p>
</td>
</tr>
<tr id="row1130693214212"><td class="cellrowborder" valign="top" width="24.152415241524153%" headers="mcps1.2.4.1.1 "><p id="p245164217314"><a name="p245164217314"></a><a name="p245164217314"></a>external_service_port</p>
</td>
<td class="cellrowborder" valign="top" width="28.072807280728075%" headers="mcps1.2.4.1.2 "><p id="p134512421939"><a name="p134512421939"></a><a name="p134512421939"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><p id="p16451144211314"><a name="p16451144211314"></a><a name="p16451144211314"></a>Specifies the port for providing external services.</p>
</td>
</tr>
<tr id="row530618321326"><td class="cellrowborder" valign="top" width="24.152415241524153%" headers="mcps1.2.4.1.1 "><p id="p12451342037"><a name="p12451342037"></a><a name="p12451342037"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="28.072807280728075%" headers="mcps1.2.4.1.2 "><p id="p74515424310"><a name="p74515424310"></a><a name="p74515424310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><p id="p74511242439"><a name="p74511242439"></a><a name="p74511242439"></a>Specifies the protocol type. Currently, TCP, UDP, and ANY are supported.</p>
<p id="p1445110421435"><a name="p1445110421435"></a><a name="p1445110421435"></a>The protocol number of TCP, UDP, and ANY are 6, 17, and 0, respectively.</p>
</td>
</tr>
<tr id="row1630620322219"><td class="cellrowborder" valign="top" width="24.152415241524153%" headers="mcps1.2.4.1.1 "><p id="p1445104217312"><a name="p1445104217312"></a><a name="p1445104217312"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="28.072807280728075%" headers="mcps1.2.4.1.2 "><p id="p124515425318"><a name="p124515425318"></a><a name="p124515425318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><a name="ul2045134211310"></a><a name="ul2045134211310"></a><ul id="ul2045134211310"><li>Specifies the status of the DNAT rule.</li><li>For details about all its values, see <a href="resource-status-description.md#table1390614366107">Table 1</a>.</li></ul>
</td>
</tr>
<tr id="row14306173212214"><td class="cellrowborder" valign="top" width="24.152415241524153%" headers="mcps1.2.4.1.1 "><p id="p945116428311"><a name="p945116428311"></a><a name="p945116428311"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="28.072807280728075%" headers="mcps1.2.4.1.2 "><p id="p1764614265487"><a name="p1764614265487"></a><a name="p1764614265487"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><a name="ul71858556358"></a><a name="ul71858556358"></a><ul id="ul71858556358"><li>Specifies whether the DNAT rule is enabled or disabled.</li><li>The value can be:<a name="ul16205638124410"></a><a name="ul16205638124410"></a><ul id="ul16205638124410"><li><strong id="b2017512911216"><a name="b2017512911216"></a><a name="b2017512911216"></a>true</strong>: The DNAT rule is enabled.</li><li><strong id="b8164810229"><a name="b8164810229"></a><a name="b8164810229"></a>false</strong>: The DNAT rule is disabled.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row143061032627"><td class="cellrowborder" valign="top" width="24.152415241524153%" headers="mcps1.2.4.1.1 "><p id="p184511342035"><a name="p184511342035"></a><a name="p184511342035"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.072807280728075%" headers="mcps1.2.4.1.2 "><p id="p145144217316"><a name="p145144217316"></a><a name="p145144217316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.774777477747776%" headers="mcps1.2.4.1.3 "><p id="p0948172916015"><a name="p0948172916015"></a><a name="p0948172916015"></a>Specifies when the DNAT rule is created (UTC time). Its value rounds to 6 decimal places for seconds. The format is yyyy-mm-dd hh:mm:ss.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section956164017620"></a>

-   Example request
    1.  Create a rule for a specified port.

        ```
        POST https://{Endpoint}/v2.0/dnat_rules
        {
            "dnat_rule": {
                "floating_ip_id": "bf99c679-9f41-4dac-8513-9c9228e713e1",
                "nat_gateway_id": "cda3a125-2406-456c-a11f-598e10578541",
                "port_id": "9a469561-daac-4c94-88f5-39366e5ea193",
                "internal_service_port": 993,
                "protocol": "tcp",
                "external_service_port": 242
            }
        }
        ```

    1.  Create a rule for all ports.

        ```
        POST https://{Endpoint}/v2.0/dnat_rules
        {
            "dnat_rule": {
                "floating_ip_id": "Cf99c679-9f41-4dac-8513-9c9228e713e1",
                "nat_gateway_id": "Dda3a125-2406-456c-a11f-598e10578541",
                "private_ip": "192.168.1.100",
                "internal_service_port": 0,
                "protocol": "any",
                "external_service_port": 0
            }
        }
        ```



-   Example response
    1.  Create a response for a specified port.

        ```
        {
            "dnat_rule": {
                "floating_ip_id": "bf99c679-9f41-4dac-8513-9c9228e713e1",
                "status": "ACTIVE",
                "nat_gateway_id": "cda3a125-2406-456c-a11f-598e10578541",
                "admin_state_up": true,
                "port_id": "9a469561-daac-4c94-88f5-39366e5ea193",
                "internal_service_port": 993,
                "protocol": "tcp",
                "tenant_id": "abc",
                "created_at": "2017-11-15 15:44:42.595173",
                "id": "79195d50-0271-41f1-bded-4c089b2502ff",
                "floating_ip_address": "5.21.11.226",
                "external_service_port": 242,
                "private_ip": ""
            }
        }
        ```

    2.  Create a response for all ports.

        ```
        {
            "dnat_rule": {
                "floating_ip_id": "cf99c679-9f41-4dac-8513-9c9228e713e1",
                "status": "ACTIVE",
                "nat_gateway_id": "dda3a125-2406-456c-a11f-598e10578541",
                "admin_state_up": true,
                "private_ip": "192.168.1.100",
                "internal_service_port": 0,
                "protocol": "any",
                "tenant_id": "abc",
                "created_at": "2017-11-15 15:44:42.595173",
                "id": "79195d50-0271-41f1-bded-4c089b2502ff",
                "floating_ip_address": "5.21.11.227",
                "external_service_port": 0
            }
        }
        ```



## Status Code<a name="section5446226317959"></a>

See  [Status Codes](status-codes.md).

