# Creating a NAT Gateway<a name="nat_api_0061"></a>

## Function<a name="section19627306"></a>

This API is used to create a NAT gateway.

## URI<a name="section79426345357"></a>

POST /v2.0/nat\_gateways

## Request<a name="section14118316"></a>

[Table 1](#table531642713017)  describes the request parameters.

**Table  1**  Request parameter

<a name="table531642713017"></a>
<table><thead align="left"><tr id="row15519227163019"><th class="cellrowborder" valign="top" width="22.939999999999998%" id="mcps1.2.5.1.1"><p id="p1519927183015"><a name="p1519927183015"></a><a name="p1519927183015"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.23%" id="mcps1.2.5.1.2"><p id="p165191278302"><a name="p165191278302"></a><a name="p165191278302"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.77%" id="mcps1.2.5.1.3"><p id="p85191827133020"><a name="p85191827133020"></a><a name="p85191827133020"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.06%" id="mcps1.2.5.1.4"><p id="p10519027113020"><a name="p10519027113020"></a><a name="p10519027113020"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12519162773014"><td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.2.5.1.1 "><p id="p19519182710304"><a name="p19519182710304"></a><a name="p19519182710304"></a>nat_gateway</p>
</td>
<td class="cellrowborder" valign="top" width="8.23%" headers="mcps1.2.5.1.2 "><p id="p651913277303"><a name="p651913277303"></a><a name="p651913277303"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.77%" headers="mcps1.2.5.1.3 "><p id="p1836019108576"><a name="p1836019108576"></a><a name="p1836019108576"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50.06%" headers="mcps1.2.5.1.4 "><p id="p15519192743011"><a name="p15519192743011"></a><a name="p15519192743011"></a>Specifies the NAT gateway object. For details, see <a href="#table93481227153014">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Description of the  **nat\_gateway**  field

<a name="table93481227153014"></a>
<table><thead align="left"><tr id="row1051916278301"><th class="cellrowborder" valign="top" width="22.939999999999998%" id="mcps1.2.5.1.1"><p id="p10519132723015"><a name="p10519132723015"></a><a name="p10519132723015"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.23%" id="mcps1.2.5.1.2"><p id="p95191427163010"><a name="p95191427163010"></a><a name="p95191427163010"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.77%" id="mcps1.2.5.1.3"><p id="p195191927133019"><a name="p195191927133019"></a><a name="p195191927133019"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.06%" id="mcps1.2.5.1.4"><p id="p85191127143015"><a name="p85191127143015"></a><a name="p85191127143015"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13519162717309"><td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.2.5.1.1 "><p id="p8519142717306"><a name="p8519142717306"></a><a name="p8519142717306"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.23%" headers="mcps1.2.5.1.2 "><p id="p1519427203019"><a name="p1519427203019"></a><a name="p1519427203019"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.77%" headers="mcps1.2.5.1.3 "><p id="p7519227183020"><a name="p7519227183020"></a><a name="p7519227183020"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.06%" headers="mcps1.2.5.1.4 "><p id="p16519162711308"><a name="p16519162711308"></a><a name="p16519162711308"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row0519192793015"><td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.2.5.1.1 "><p id="p8519142711302"><a name="p8519142711302"></a><a name="p8519142711302"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="8.23%" headers="mcps1.2.5.1.2 "><p id="p1151962733014"><a name="p1151962733014"></a><a name="p1151962733014"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.77%" headers="mcps1.2.5.1.3 "><p id="p13519112753013"><a name="p13519112753013"></a><a name="p13519112753013"></a>String(64)</p>
</td>
<td class="cellrowborder" valign="top" width="50.06%" headers="mcps1.2.5.1.4 "><p id="p12519327113012"><a name="p12519327113012"></a><a name="p12519327113012"></a>Specifies the NAT gateway name.</p>
<p id="p15519227143015"><a name="p15519227143015"></a><a name="p15519227143015"></a>The name can contain only digits, letters, underscores (_), and hyphens (-).</p>
</td>
</tr>
<tr id="row1651920271306"><td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.2.5.1.1 "><p id="p65191327153018"><a name="p65191327153018"></a><a name="p65191327153018"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="8.23%" headers="mcps1.2.5.1.2 "><p id="p5519122733012"><a name="p5519122733012"></a><a name="p5519122733012"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.77%" headers="mcps1.2.5.1.3 "><p id="p125191227203016"><a name="p125191227203016"></a><a name="p125191227203016"></a>String(255)</p>
</td>
<td class="cellrowborder" valign="top" width="50.06%" headers="mcps1.2.5.1.4 "><p id="p6519152719306"><a name="p6519152719306"></a><a name="p6519152719306"></a>Provides supplementary information about the NAT gateway.</p>
</td>
</tr>
<tr id="row95191027143013"><td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.2.5.1.1 "><p id="p95190271307"><a name="p95190271307"></a><a name="p95190271307"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="8.23%" headers="mcps1.2.5.1.2 "><p id="p195191927143014"><a name="p195191927143014"></a><a name="p195191927143014"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.77%" headers="mcps1.2.5.1.3 "><p id="p12519172793015"><a name="p12519172793015"></a><a name="p12519172793015"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.06%" headers="mcps1.2.5.1.4 "><p id="p251962719307"><a name="p251962719307"></a><a name="p251962719307"></a>Specifies the NAT gateway type.</p>
<p id="p15191327183013"><a name="p15191327183013"></a><a name="p15191327183013"></a>The value can be:</p>
<a name="ul151911279307"></a><a name="ul151911279307"></a><ul id="ul151911279307"><li><strong id="b325113510558"><a name="b325113510558"></a><a name="b325113510558"></a>1</strong>: small type, which supports up to 10,000 SNAT connections.</li><li><strong id="b15436163935910"><a name="b15436163935910"></a><a name="b15436163935910"></a>2</strong>: medium type, which supports up to 50,000 SNAT connections.</li><li><strong id="b1139694119"><a name="b1139694119"></a><a name="b1139694119"></a>3</strong>: large type, which supports up to 200,000 SNAT connections.</li><li><strong id="b83552382110"><a name="b83552382110"></a><a name="b83552382110"></a>4</strong>: extra-large type, which supports up to 1,000,000 SNAT connections.</li></ul>
</td>
</tr>
<tr id="row35192277306"><td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.2.5.1.1 "><p id="p55191827103018"><a name="p55191827103018"></a><a name="p55191827103018"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.23%" headers="mcps1.2.5.1.2 "><p id="p1751942763015"><a name="p1751942763015"></a><a name="p1751942763015"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.77%" headers="mcps1.2.5.1.3 "><p id="p19519152720308"><a name="p19519152720308"></a><a name="p19519152720308"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.06%" headers="mcps1.2.5.1.4 "><p id="p151972713301"><a name="p151972713301"></a><a name="p151972713301"></a>Specifies the VPC ID. </p>
</td>
</tr>
<tr id="row10519172753011"><td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.2.5.1.1 "><p id="p45191127163011"><a name="p45191127163011"></a><a name="p45191127163011"></a>internal_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.23%" headers="mcps1.2.5.1.2 "><p id="p1051910279307"><a name="p1051910279307"></a><a name="p1051910279307"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.77%" headers="mcps1.2.5.1.3 "><p id="p85191527133017"><a name="p85191527133017"></a><a name="p85191527133017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.06%" headers="mcps1.2.5.1.4 "><p id="p1034195216414"><a name="p1034195216414"></a><a name="p1034195216414"></a>Specifies the network ID of the downstream interface (the next hop of the DVR) of the NAT gateway. </p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section59955987"></a>

[Table 3](#table1899835483516)  lists response parameters.

**Table  3**  Response parameters

<a name="table1899835483516"></a>
<table><thead align="left"><tr id="row7169955173518"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="p17169195519358"><a name="p17169195519358"></a><a name="p17169195519358"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.4.1.2"><p id="p5169105593518"><a name="p5169105593518"></a><a name="p5169105593518"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="p2169855193514"><a name="p2169855193514"></a><a name="p2169855193514"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row316945543510"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p161697551351"><a name="p161697551351"></a><a name="p161697551351"></a>nat_gateway</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.2 "><p id="p716916553359"><a name="p716916553359"></a><a name="p716916553359"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p141693558351"><a name="p141693558351"></a><a name="p141693558351"></a>Specifies the NAT gateway object. For details, see <a href="#table5998115418352">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Description of the  **nat\_gateway**  field

<a name="table5998115418352"></a>
<table><thead align="left"><tr id="row6169455113517"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p18169125533511"><a name="p18169125533511"></a><a name="p18169125533511"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.2"><p id="p11692559359"><a name="p11692559359"></a><a name="p11692559359"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="p15169165515355"><a name="p15169165515355"></a><a name="p15169165515355"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16169555143516"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p131697559351"><a name="p131697559351"></a><a name="p131697559351"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p11169115553519"><a name="p11169115553519"></a><a name="p11169115553519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p16169195593517"><a name="p16169195593517"></a><a name="p16169195593517"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
<tr id="row5169755193513"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p141694552355"><a name="p141694552355"></a><a name="p141694552355"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p816965583515"><a name="p816965583515"></a><a name="p816965583515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p201693557359"><a name="p201693557359"></a><a name="p201693557359"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row91691755183512"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p16169555143511"><a name="p16169555143511"></a><a name="p16169555143511"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p14169155513358"><a name="p14169155513358"></a><a name="p14169155513358"></a>String(64)</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p19169955183517"><a name="p19169955183517"></a><a name="p19169955183517"></a>Specifies the NAT gateway name.</p>
<p id="p15169055203514"><a name="p15169055203514"></a><a name="p15169055203514"></a>The name can contain only digits, letters, underscores (_), and hyphens (-).</p>
</td>
</tr>
<tr id="row191691855183511"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1616925533510"><a name="p1616925533510"></a><a name="p1616925533510"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p111692055193514"><a name="p111692055193514"></a><a name="p111692055193514"></a>String(255)</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p181694559355"><a name="p181694559355"></a><a name="p181694559355"></a>Provides supplementary information about the NAT gateway.</p>
</td>
</tr>
<tr id="row1169655103519"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p2016935510359"><a name="p2016935510359"></a><a name="p2016935510359"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p7169165511359"><a name="p7169165511359"></a><a name="p7169165511359"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p1216915518351"><a name="p1216915518351"></a><a name="p1216915518351"></a>Specifies the NAT gateway type.</p>
<p id="p19169115553517"><a name="p19169115553517"></a><a name="p19169115553517"></a>The value can be:</p>
<a name="ul1216911558358"></a><a name="ul1216911558358"></a><ul id="ul1216911558358"><li><strong id="b69605375103"><a name="b69605375103"></a><a name="b69605375103"></a>1</strong>: small type, which supports up to 10,000 SNAT connections.</li><li><strong id="b2085620429102"><a name="b2085620429102"></a><a name="b2085620429102"></a>2</strong>: medium type, which supports up to 50,000 SNAT connections.</li><li><strong id="b4885124519109"><a name="b4885124519109"></a><a name="b4885124519109"></a>3</strong>: large type, which supports up to 200,000 SNAT connections.</li><li><strong id="b1247834831015"><a name="b1247834831015"></a><a name="b1247834831015"></a>4</strong>: extra-large type, which supports up to 1,000,000 SNAT connections.</li></ul>
</td>
</tr>
<tr id="row1716985523510"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1016965563511"><a name="p1016965563511"></a><a name="p1016965563511"></a>router_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1616917554354"><a name="p1616917554354"></a><a name="p1616917554354"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p15169195517351"><a name="p15169195517351"></a><a name="p15169195517351"></a>Specifies the router ID.</p>
</td>
</tr>
<tr id="row10169355153512"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p17169135563513"><a name="p17169135563513"></a><a name="p17169135563513"></a>internal_network_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p10169125533515"><a name="p10169125533515"></a><a name="p10169125533515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p8169195593518"><a name="p8169195593518"></a><a name="p8169195593518"></a>Specifies the network ID of the downstream interface (the next hop of the DVR) of the NAT gateway.</p>
</td>
</tr>
<tr id="row2169755143512"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p121696555354"><a name="p121696555354"></a><a name="p121696555354"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p171691355173516"><a name="p171691355173516"></a><a name="p171691355173516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><a name="ul5169105563515"></a><a name="ul5169105563515"></a><ul id="ul5169105563515"><li>Specifies the status of the NAT gateway.</li><li>For details about all its values, see <a href="resource-status-description.md#table1390614366107">Table 1</a>.</li></ul>
</td>
</tr>
<tr id="row11169155517351"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p6169755103520"><a name="p6169755103520"></a><a name="p6169755103520"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1764614265487"><a name="p1764614265487"></a><a name="p1764614265487"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><a name="ul71858556358"></a><a name="ul71858556358"></a><ul id="ul71858556358"><li>Specifies whether the NAT gateway is up or down.</li><li>The value can be:<a name="ul16205638124410"></a><a name="ul16205638124410"></a><ul id="ul16205638124410"><li><strong id="b1135931618373"><a name="b1135931618373"></a><a name="b1135931618373"></a>true</strong>: The NAT gateway is up.</li><li><strong id="b8147172211385"><a name="b8147172211385"></a><a name="b8147172211385"></a>false</strong>: The NAT gateway is down.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row13185255183510"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1418525573515"><a name="p1418525573515"></a><a name="p1418525573515"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p101859557352"><a name="p101859557352"></a><a name="p101859557352"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p135382155910"><a name="p135382155910"></a><a name="p135382155910"></a>Specifies when the NAT gateway is created (UTC time). Its value rounds to 6 decimal places for seconds. The format is yyyy-mm-dd hh:mm:ss.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section2732972"></a>

-   Example request

    ```
    POST https://{Endpoint}/v2.0/nat_gateways
    {
        "nat_gateway": {
            "name": "nat_001",
            "description": "my nat gateway 01",
            "router_id": "d84f345c-80a1-4fa2-a39c-d0d397c3f09a",
            "internal_network_id": "89d66639-aacb-4929-969d-07080b0f9fd9",
            "spec": "1"
        }
    }
    ```


-   Example response

    ```
    {
        "nat_gateway": { 
             "router_id": "d84f345c-80a1-4fa2-a39c-d0d397c3f09a", 
             "status": "PENDING_CREATE", 
             "description": "my nat gateway 01", 
             "admin_state_up": true, 
             "tenant_id": "27e25061336f4af590faeabeb7fcd9a3", 
             "created_at": "2017-11-18 07:34:32.203044", 
             "spec": "1", 
             "internal_network_id": "89d66639-aacb-4929-969d-07080b0f9fd9", 
             "id": "a78fb3eb-1654-4710-8742-3fc49d5f04f8",
             "name": "nat_001" 
        }
    }
    ```


## Status Code<a name="section20044197"></a>

See  [Status Codes](status-codes.md).

