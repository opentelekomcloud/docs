# Querying Subnets<a name="vpc_subnet02_0001"></a>

## Function<a name="section47928120"></a>

This API is used to query all subnets accessible to the tenant submitting the request. 

## URI<a name="section28699899"></a>

GET /v2.0/subnets

Example:

```
GET https://{Endpoint}/v2.0/subnets?name={subnet_name}&ip_version={ip_version}&network_id={network_id}&cidr={subnet_cidr_address}&gateway_ip={subnet_gateway}&tenant_id={tenant_id}&enable_dhcp={is_enable_dhcp}
```

Example of querying networks by page

```
GET https://{Endpoint}/v2.0/subnets?limit=2&marker=011fc878-5521-4654-a1ad-f5b0b5820302&page_reverse=False
```

[Table 1](#table3825412149)  describes the parameters.

**Table  1**  Parameter description

<a name="table3825412149"></a>
<table><thead align="left"><tr id="row72051741191419"><th class="cellrowborder" valign="top" width="17.091709170917092%" id="mcps1.2.5.1.1"><p id="p11205114113148"><a name="p11205114113148"></a><a name="p11205114113148"></a><strong id="b820313302017"><a name="b820313302017"></a><a name="b820313302017"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.271927192719275%" id="mcps1.2.5.1.2"><p id="p1205124171417"><a name="p1205124171417"></a><a name="p1205124171417"></a><strong id="b98531533801"><a name="b98531533801"></a><a name="b98531533801"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.63166316631663%" id="mcps1.2.5.1.3"><p id="p4205124191411"><a name="p4205124191411"></a><a name="p4205124191411"></a><strong id="b162142035502"><a name="b162142035502"></a><a name="b162142035502"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.004700470047%" id="mcps1.2.5.1.4"><p id="p3205144151413"><a name="p3205144151413"></a><a name="p3205144151413"></a><strong id="b20283936204"><a name="b20283936204"></a><a name="b20283936204"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row8205041111418"><td class="cellrowborder" valign="top" width="17.091709170917092%" headers="mcps1.2.5.1.1 "><p id="p92051641151419"><a name="p92051641151419"></a><a name="p92051641151419"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19.271927192719275%" headers="mcps1.2.5.1.2 "><p id="p220544113147"><a name="p220544113147"></a><a name="p220544113147"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.63166316631663%" headers="mcps1.2.5.1.3 "><p id="p162059412145"><a name="p162059412145"></a><a name="p162059412145"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.004700470047%" headers="mcps1.2.5.1.4 "><p id="p1205841111418"><a name="p1205841111418"></a><a name="p1205841111418"></a>Specifies that the ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row192054417143"><td class="cellrowborder" valign="top" width="17.091709170917092%" headers="mcps1.2.5.1.1 "><p id="p620694131411"><a name="p620694131411"></a><a name="p620694131411"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="19.271927192719275%" headers="mcps1.2.5.1.2 "><p id="p820619412149"><a name="p820619412149"></a><a name="p820619412149"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.63166316631663%" headers="mcps1.2.5.1.3 "><p id="p18206114120146"><a name="p18206114120146"></a><a name="p18206114120146"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.004700470047%" headers="mcps1.2.5.1.4 "><p id="p920612418149"><a name="p920612418149"></a><a name="p920612418149"></a>Specifies that the subnet name is used as the filtering condition.</p>
</td>
</tr>
<tr id="row520664131419"><td class="cellrowborder" valign="top" width="17.091709170917092%" headers="mcps1.2.5.1.1 "><p id="p1206441191420"><a name="p1206441191420"></a><a name="p1206441191420"></a>enable_dhcp</p>
</td>
<td class="cellrowborder" valign="top" width="19.271927192719275%" headers="mcps1.2.5.1.2 "><p id="p16206104131414"><a name="p16206104131414"></a><a name="p16206104131414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.63166316631663%" headers="mcps1.2.5.1.3 "><p id="p1206104119142"><a name="p1206104119142"></a><a name="p1206104119142"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="47.004700470047%" headers="mcps1.2.5.1.4 "><p id="p144291518141512"><a name="p144291518141512"></a><a name="p144291518141512"></a>Specifies whether DHCP is enabled is used as the filtering condition.</p>
<p id="p142063410146"><a name="p142063410146"></a><a name="p142063410146"></a>The value can be <strong id="b3420201714115"><a name="b3420201714115"></a><a name="b3420201714115"></a>true</strong> or <strong id="b842061715118"><a name="b842061715118"></a><a name="b842061715118"></a>false</strong>.</p>
</td>
</tr>
<tr id="row4206441171415"><td class="cellrowborder" valign="top" width="17.091709170917092%" headers="mcps1.2.5.1.1 "><p id="p4206174161415"><a name="p4206174161415"></a><a name="p4206174161415"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="19.271927192719275%" headers="mcps1.2.5.1.2 "><p id="p16206104111145"><a name="p16206104111145"></a><a name="p16206104111145"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.63166316631663%" headers="mcps1.2.5.1.3 "><p id="p0206541121416"><a name="p0206541121416"></a><a name="p0206541121416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.004700470047%" headers="mcps1.2.5.1.4 "><p id="p3206164161418"><a name="p3206164161418"></a><a name="p3206164161418"></a>Specifies that the CIDR block is used as the filtering condition.</p>
</td>
</tr>
<tr id="row720664119147"><td class="cellrowborder" valign="top" width="17.091709170917092%" headers="mcps1.2.5.1.1 "><p id="p120684191415"><a name="p120684191415"></a><a name="p120684191415"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.271927192719275%" headers="mcps1.2.5.1.2 "><p id="p020604117141"><a name="p020604117141"></a><a name="p020604117141"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.63166316631663%" headers="mcps1.2.5.1.3 "><p id="p10206204131416"><a name="p10206204131416"></a><a name="p10206204131416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.004700470047%" headers="mcps1.2.5.1.4 "><p id="p192061641131415"><a name="p192061641131415"></a><a name="p192061641131415"></a>Specifies that the network ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row1120614111148"><td class="cellrowborder" valign="top" width="17.091709170917092%" headers="mcps1.2.5.1.1 "><p id="p13206641111413"><a name="p13206641111413"></a><a name="p13206641111413"></a>ip_version</p>
</td>
<td class="cellrowborder" valign="top" width="19.271927192719275%" headers="mcps1.2.5.1.2 "><p id="p14206154181414"><a name="p14206154181414"></a><a name="p14206154181414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.63166316631663%" headers="mcps1.2.5.1.3 "><p id="p11206184161418"><a name="p11206184161418"></a><a name="p11206184161418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.004700470047%" headers="mcps1.2.5.1.4 "><p id="p17206134120140"><a name="p17206134120140"></a><a name="p17206134120140"></a>Specifies that the IP address version is used as the filtering condition.</p>
</td>
</tr>
<tr id="row122065416145"><td class="cellrowborder" valign="top" width="17.091709170917092%" headers="mcps1.2.5.1.1 "><p id="p16206114181418"><a name="p16206114181418"></a><a name="p16206114181418"></a>gateway_ip</p>
</td>
<td class="cellrowborder" valign="top" width="19.271927192719275%" headers="mcps1.2.5.1.2 "><p id="p11206941191418"><a name="p11206941191418"></a><a name="p11206941191418"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.63166316631663%" headers="mcps1.2.5.1.3 "><p id="p6206141191413"><a name="p6206141191413"></a><a name="p6206141191413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.004700470047%" headers="mcps1.2.5.1.4 "><p id="p92061741171417"><a name="p92061741171417"></a><a name="p92061741171417"></a>Specifies that the gateway IP address is used as the filtering condition.</p>
</td>
</tr>
<tr id="row10206174112140"><td class="cellrowborder" valign="top" width="17.091709170917092%" headers="mcps1.2.5.1.1 "><p id="p420620416149"><a name="p420620416149"></a><a name="p420620416149"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.271927192719275%" headers="mcps1.2.5.1.2 "><p id="p1620612416148"><a name="p1620612416148"></a><a name="p1620612416148"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.63166316631663%" headers="mcps1.2.5.1.3 "><p id="p1420620410148"><a name="p1420620410148"></a><a name="p1420620410148"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.004700470047%" headers="mcps1.2.5.1.4 "><p id="p72071941181420"><a name="p72071941181420"></a><a name="p72071941181420"></a>Specifies that the project ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row1720744110145"><td class="cellrowborder" valign="top" width="17.091709170917092%" headers="mcps1.2.5.1.1 "><p id="p112071541201414"><a name="p112071541201414"></a><a name="p112071541201414"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="19.271927192719275%" headers="mcps1.2.5.1.2 "><p id="p7207841141412"><a name="p7207841141412"></a><a name="p7207841141412"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.63166316631663%" headers="mcps1.2.5.1.3 "><p id="p1207114117140"><a name="p1207114117140"></a><a name="p1207114117140"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.004700470047%" headers="mcps1.2.5.1.4 "><p id="p20207341121416"><a name="p20207341121416"></a><a name="p20207341121416"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row220774110141"><td class="cellrowborder" valign="top" width="17.091709170917092%" headers="mcps1.2.5.1.1 "><p id="p82075416148"><a name="p82075416148"></a><a name="p82075416148"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="19.271927192719275%" headers="mcps1.2.5.1.2 "><p id="p1720714413143"><a name="p1720714413143"></a><a name="p1720714413143"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.63166316631663%" headers="mcps1.2.5.1.3 "><p id="p1620714117148"><a name="p1620714117148"></a><a name="p1620714117148"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47.004700470047%" headers="mcps1.2.5.1.4 "><p id="p2518132611514"><a name="p2518132611514"></a><a name="p2518132611514"></a>Specifies the number of records on each page.</p>
<p id="p1420704119149"><a name="p1420704119149"></a><a name="p1420704119149"></a>The value ranges from 0 to intmax.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section42990474"></a>

None

## Response Message<a name="section51369953"></a>

**Table  2**  Response parameter

<a name="table51277242"></a>
<table><thead align="left"><tr id="row64740644"><th class="cellrowborder" valign="top" width="23.122312231223123%" id="mcps1.2.4.1.1"><p id="p9500791"><a name="p9500791"></a><a name="p9500791"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.552555255525554%" id="mcps1.2.4.1.2"><p id="p31366578"><a name="p31366578"></a><a name="p31366578"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.325132513251326%" id="mcps1.2.4.1.3"><p id="p40344834"><a name="p40344834"></a><a name="p40344834"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row46706151"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="p25101909"><a name="p25101909"></a><a name="p25101909"></a>subnets</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="p21426146239"><a name="p21426146239"></a><a name="p21426146239"></a>Array of <a href="#table176735992713">subnet</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="p15291872"><a name="p15291872"></a><a name="p15291872"></a>Specifies the subnet list. For details, see <a href="#table176735992713">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **subnet**  objects

<a name="table176735992713"></a>
<table><thead align="left"><tr id="row176713593276"><th class="cellrowborder" valign="top" width="28.332833283328334%" id="mcps1.2.4.1.1"><p id="p136755912715"><a name="p136755912715"></a><a name="p136755912715"></a><strong id="b18205124462718"><a name="b18205124462718"></a><a name="b18205124462718"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.292829282928288%" id="mcps1.2.4.1.2"><p id="p667105912718"><a name="p667105912718"></a><a name="p667105912718"></a><strong id="b14231124510275"><a name="b14231124510275"></a><a name="b14231124510275"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.37433743374337%" id="mcps1.2.4.1.3"><p id="p26855915275"><a name="p26855915275"></a><a name="p26855915275"></a><strong id="b22102046192715"><a name="b22102046192715"></a><a name="b22102046192715"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row28303131105515"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p2014344105614"><a name="p2014344105614"></a><a name="p2014344105614"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p28944191105614"><a name="p28944191105614"></a><a name="p28944191105614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p53796361105614"><a name="p53796361105614"></a><a name="p53796361105614"></a>Specifies the subnet ID.</p>
<p id="p2677113954519"><a name="p2677113954519"></a><a name="p2677113954519"></a>This parameter is not mandatory when you query subnets.</p>
</td>
</tr>
<tr id="row1868135972719"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p37015595272"><a name="p37015595272"></a><a name="p37015595272"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p18706591271"><a name="p18706591271"></a><a name="p18706591271"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p1870259172715"><a name="p1870259172715"></a><a name="p1870259172715"></a>Specifies the subnet name.</p>
</td>
</tr>
<tr id="row670165910271"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p187012596279"><a name="p187012596279"></a><a name="p187012596279"></a>ip_version</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p137095922720"><a name="p137095922720"></a><a name="p137095922720"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p870155932715"><a name="p870155932715"></a><a name="p870155932715"></a>Specifies the IP address version.</p>
<p id="p10708598273"><a name="p10708598273"></a><a name="p10708598273"></a>Only IPv4 address is supported.</p>
</td>
</tr>
<tr id="row1270135915274"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p1770105919271"><a name="p1770105919271"></a><a name="p1770105919271"></a>ipv6_address_mode</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p1370205912279"><a name="p1370205912279"></a><a name="p1370205912279"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p5701759142713"><a name="p5701759142713"></a><a name="p5701759142713"></a>Specifies the IPv6 addressing mode.</p>
</td>
</tr>
<tr id="row57075913279"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p070195972715"><a name="p070195972715"></a><a name="p070195972715"></a>ipv6_ra_mode</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p1970559102716"><a name="p1970559102716"></a><a name="p1970559102716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p19701959152712"><a name="p19701959152712"></a><a name="p19701959152712"></a>Specifies the IPv6 route broadcast mode.</p>
</td>
</tr>
<tr id="row970185911274"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p5719599271"><a name="p5719599271"></a><a name="p5719599271"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p1671105982710"><a name="p1671105982710"></a><a name="p1671105982710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p1071259102716"><a name="p1071259102716"></a><a name="p1071259102716"></a>Specifies the ID of the network to which the subnet belongs.</p>
</td>
</tr>
<tr id="row9711659142718"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p1471155922712"><a name="p1471155922712"></a><a name="p1471155922712"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p1871155912279"><a name="p1871155912279"></a><a name="p1871155912279"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p471115972720"><a name="p471115972720"></a><a name="p471115972720"></a>Specifies the CIDR format.</p>
<p id="p171105952717"><a name="p171105952717"></a><a name="p171105952717"></a>Only the addresses in the 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 network segments are supported. In addition, the subnet mask cannot be greater than 28. </p>
</td>
</tr>
<tr id="row373659122718"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p173195914274"><a name="p173195914274"></a><a name="p173195914274"></a>gateway_ip</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p16733594272"><a name="p16733594272"></a><a name="p16733594272"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p167319597276"><a name="p167319597276"></a><a name="p167319597276"></a>The gateway IP address cannot conflict with IP addresses configured for <strong id="b842352706101449"><a name="b842352706101449"></a><a name="b842352706101449"></a>allocation_pools</strong>.</p>
<p id="p1773175918271"><a name="p1773175918271"></a><a name="p1773175918271"></a>This attribute cannot be modified. </p>
</td>
</tr>
<tr id="row6733598278"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p37325918273"><a name="p37325918273"></a><a name="p37325918273"></a>allocation_pools</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p166911588244"><a name="p166911588244"></a><a name="p166911588244"></a>Array of <a href="#table1777145918276">allocation_pool</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p13740597271"><a name="p13740597271"></a><a name="p13740597271"></a>Specifies available IP address pools. For details, see <a href="#table1777145918276">Table 4</a>.</p>
<p id="p137415915279"><a name="p137415915279"></a><a name="p137415915279"></a>Example: [ { "start": "10.0.0.2", "end": "10.0.0.251"} ]</p>
<p id="p167414592279"><a name="p167414592279"></a><a name="p167414592279"></a>The last three and the first IP addresses in each subnet are the ones reserved by the system. For example, in subnet <strong id="b84235270612913"><a name="b84235270612913"></a><a name="b84235270612913"></a>192.168.1.0/24</strong>, IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved by the system. By default, the IP addresses reserved by the system are not in the IP address pool specified by <strong id="b842352706121042"><a name="b842352706121042"></a><a name="b842352706121042"></a>allocation_pool</strong>.</p>
<p id="p074359192720"><a name="p074359192720"></a><a name="p074359192720"></a>When updating an IP address pool, the <strong id="b280215131523"><a name="b280215131523"></a><a name="b280215131523"></a>allocation_pool</strong> value can contain neither gateway nor broadcast IP addresses. </p>
</td>
</tr>
<tr id="row474205911270"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p774105972720"><a name="p774105972720"></a><a name="p774105972720"></a>dns_nameservers</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p1474155952710"><a name="p1474155952710"></a><a name="p1474155952710"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p10743593273"><a name="p10743593273"></a><a name="p10743593273"></a>Specifies the DNS server address.</p>
<p id="p97485912712"><a name="p97485912712"></a><a name="p97485912712"></a>Example: "dns_nameservers": ["8.xx.xx.8","8.xx.xx.4"]</p>
</td>
</tr>
<tr id="row6741659182714"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p574959122713"><a name="p574959122713"></a><a name="p574959122713"></a>host_routes</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p18246193118245"><a name="p18246193118245"></a><a name="p18246193118245"></a>Array of <a href="#table177865912715">host_route</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p2074459132712"><a name="p2074459132712"></a><a name="p2074459132712"></a>Specifies the static VM routes. For details, see <a href="#table177865912715">Table 5</a>.</p>
<p id="p1674359172717"><a name="p1674359172717"></a><a name="p1674359172717"></a>Static routes are not supported, and entered information will be ignored.</p>
</td>
</tr>
<tr id="row42017779105653"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p5182838910577"><a name="p5182838910577"></a><a name="p5182838910577"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p3734998010577"><a name="p3734998010577"></a><a name="p3734998010577"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row97535914274"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p475959202718"><a name="p475959202718"></a><a name="p475959202718"></a>enable_dhcp</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p2755596279"><a name="p2755596279"></a><a name="p2755596279"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p47595962710"><a name="p47595962710"></a><a name="p47595962710"></a>Specifies whether to enable the DHCP function. Value <strong id="b842352706155341"><a name="b842352706155341"></a><a name="b842352706155341"></a>false</strong> indicates that the DHCP function is not enabled.</p>
<p id="p57535914276"><a name="p57535914276"></a><a name="p57535914276"></a>The value can only be <strong id="b193171228153711"><a name="b193171228153711"></a><a name="b193171228153711"></a>true</strong>.</p>
</td>
</tr>
<tr id="row63315321123"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p45641422124917"><a name="p45641422124917"></a><a name="p45641422124917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p113781259182412"><a name="p113781259182412"></a><a name="p113781259182412"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row126291040191211"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the subnet is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i1328416545374"><a name="i1328416545374"></a><a name="i1328416545374"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1084513362123"><td class="cellrowborder" valign="top" width="28.332833283328334%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.292829282928288%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.37433743374337%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the subnet is updated.</p>
<p id="p10406183916467"><a name="p10406183916467"></a><a name="p10406183916467"></a>Format: <em id="i11061673819"><a name="i11061673819"></a><a name="i11061673819"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

**Table  4** **allocation\_pool**  objects

<a name="table1777145918276"></a>
<table><thead align="left"><tr id="row11772597275"><th class="cellrowborder" valign="top" width="23.65%" id="mcps1.2.4.1.1"><p id="p1477155962713"><a name="p1477155962713"></a><a name="p1477155962713"></a><strong id="b88338814011"><a name="b88338814011"></a><a name="b88338814011"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.610000000000003%" id="mcps1.2.4.1.2"><p id="p1077859162717"><a name="p1077859162717"></a><a name="p1077859162717"></a><strong id="b18138164613815"><a name="b18138164613815"></a><a name="b18138164613815"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.739999999999995%" id="mcps1.2.4.1.3"><p id="p5771159182718"><a name="p5771159182718"></a><a name="p5771159182718"></a><strong id="b1554718148327"><a name="b1554718148327"></a><a name="b1554718148327"></a>Remarks</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row167785982711"><td class="cellrowborder" valign="top" width="23.65%" headers="mcps1.2.4.1.1 "><p id="p1077159182720"><a name="p1077159182720"></a><a name="p1077159182720"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="24.610000000000003%" headers="mcps1.2.4.1.2 "><p id="p2077125912718"><a name="p2077125912718"></a><a name="p2077125912718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p2078205910275"><a name="p2078205910275"></a><a name="p2078205910275"></a>Specifies the start IP address of a network pool.</p>
</td>
</tr>
<tr id="row1782594271"><td class="cellrowborder" valign="top" width="23.65%" headers="mcps1.2.4.1.1 "><p id="p9781459162717"><a name="p9781459162717"></a><a name="p9781459162717"></a>end</p>
</td>
<td class="cellrowborder" valign="top" width="24.610000000000003%" headers="mcps1.2.4.1.2 "><p id="p1778115952719"><a name="p1778115952719"></a><a name="p1778115952719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.739999999999995%" headers="mcps1.2.4.1.3 "><p id="p187825911271"><a name="p187825911271"></a><a name="p187825911271"></a>Specifies the end IP address of a network pool.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **host\_route**  objects

<a name="table177865912715"></a>
<table><thead align="left"><tr id="row1779145992719"><th class="cellrowborder" valign="top" width="23.712371237123715%" id="mcps1.2.4.1.1"><p id="p2794593271"><a name="p2794593271"></a><a name="p2794593271"></a><strong id="b11963213911"><a name="b11963213911"></a><a name="b11963213911"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.4024402440244%" id="mcps1.2.4.1.2"><p id="p14791594271"><a name="p14791594271"></a><a name="p14791594271"></a><strong id="b1048518314398"><a name="b1048518314398"></a><a name="b1048518314398"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.88518851885189%" id="mcps1.2.4.1.3"><p id="p14791459172716"><a name="p14791459172716"></a><a name="p14791459172716"></a><strong id="b979524193916"><a name="b979524193916"></a><a name="b979524193916"></a>Remarks</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1379165919277"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.2.4.1.1 "><p id="p979165972710"><a name="p979165972710"></a><a name="p979165972710"></a>destination</p>
</td>
<td class="cellrowborder" valign="top" width="24.4024402440244%" headers="mcps1.2.4.1.2 "><p id="p37995952710"><a name="p37995952710"></a><a name="p37995952710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.88518851885189%" headers="mcps1.2.4.1.3 "><p id="p10791559172714"><a name="p10791559172714"></a><a name="p10791559172714"></a>Specifies the destination subnet of a route.</p>
</td>
</tr>
<tr id="row1779185915279"><td class="cellrowborder" valign="top" width="23.712371237123715%" headers="mcps1.2.4.1.1 "><p id="p6791359102719"><a name="p6791359102719"></a><a name="p6791359102719"></a>nexthop</p>
</td>
<td class="cellrowborder" valign="top" width="24.4024402440244%" headers="mcps1.2.4.1.2 "><p id="p107935942717"><a name="p107935942717"></a><a name="p107935942717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.88518851885189%" headers="mcps1.2.4.1.3 "><p id="p87975920278"><a name="p87975920278"></a><a name="p87975920278"></a>Specifies the next-hop IP address of a route.</p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section64320104111236"></a>

Example request

```
GET https://{Endpoint}/v2.0/subnets?limit=1
```

Example response

```
{
    "subnets": [
        {
            "name": "kesmdemeet",
            "cidr": "172.16.236.0/24",
            "id": "011fc878-5521-4654-a1ad-f5b0b5820302",
            "enable_dhcp": true,
            "network_id": "48efad0c-079d-4cc8-ace0-dce35d584124",
            "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
            "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
            "dns_nameservers": [],
            "allocation_pools": [
                {
                    "start": "172.16.236.2",
                    "end": "172.16.236.251"
                }
            ],
            "host_routes": [],
            "ip_version": 4,
            "gateway_ip": "172.16.236.1",
            "created_at": "2018-03-26T08:23:43",
            "updated_at": "2018-03-26T08:23:44"
        }
    ]
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

