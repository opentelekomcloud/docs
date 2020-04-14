# Key Operations on VPC<a name="en-us_topic_0100273725"></a>

Virtual Private Cloud \(VPC\) enables you to provision logically isolated, configurable, and manageable virtual networks for ECSs, improving the security of resources in enterprise clouds and simplifying network deployment.

With CTS, you can record operations associated with VPC for future query, audit, and backtrack operations.

**Table  1**  VPC operations that can be recorded by CTS

<a name="table179312503310"></a>
<table><thead align="left"><tr id="row1679315013318"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p42878113339"><a name="p42878113339"></a><a name="p42878113339"></a><strong id="b039610381266"><a name="b039610381266"></a><a name="b039610381266"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p18287101143314"><a name="p18287101143314"></a><a name="p18287101143314"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p92871013333"><a name="p92871013333"></a><a name="p92871013333"></a><strong id="b891224772615"><a name="b891224772615"></a><a name="b891224772615"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2017020114337"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1591141414373"><a name="p1591141414373"></a><a name="p1591141414373"></a>Modifying the bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p14108182920371"><a name="p14108182920371"></a><a name="p14108182920371"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2882547153711"><a name="p2882547153711"></a><a name="p2882547153711"></a>modifyBandwidth</p>
</td>
</tr>
<tr id="row530933193620"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2911171412376"><a name="p2911171412376"></a><a name="p2911171412376"></a>Creating an EIP</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p161081229143718"><a name="p161081229143718"></a><a name="p161081229143718"></a>eip</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p28821247163717"><a name="p28821247163717"></a><a name="p28821247163717"></a>createEip</p>
</td>
</tr>
<tr id="row68574393711"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2911191453712"><a name="p2911191453712"></a><a name="p2911191453712"></a>Releasing an EIP</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p910872933711"><a name="p910872933711"></a><a name="p910872933711"></a>eip</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2882124793714"><a name="p2882124793714"></a><a name="p2882124793714"></a>deleteEip</p>
</td>
</tr>
<tr id="row58514438376"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p791191410370"><a name="p791191410370"></a><a name="p791191410370"></a>Binding an EIP</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p21081829113716"><a name="p21081829113716"></a><a name="p21081829113716"></a>eip</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10882747153711"><a name="p10882747153711"></a><a name="p10882747153711"></a>bindEip</p>
</td>
</tr>
<tr id="row286154313716"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p491141410375"><a name="p491141410375"></a><a name="p491141410375"></a>Unbinding an EIP</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p01081229173714"><a name="p01081229173714"></a><a name="p01081229173714"></a>eip</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p288214473379"><a name="p288214473379"></a><a name="p288214473379"></a>unbindEip</p>
</td>
</tr>
<tr id="row108654313718"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p129111414163719"><a name="p129111414163719"></a><a name="p129111414163719"></a>Assigning a private IP address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2108122911378"><a name="p2108122911378"></a><a name="p2108122911378"></a>privateIps</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p17882124793713"><a name="p17882124793713"></a><a name="p17882124793713"></a>createPrivateIp</p>
</td>
</tr>
<tr id="row198644314378"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p17911101415378"><a name="p17911101415378"></a><a name="p17911101415378"></a>Releasing a private IP address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11099295376"><a name="p11099295376"></a><a name="p11099295376"></a>privateIps</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p788234743713"><a name="p788234743713"></a><a name="p788234743713"></a>deletePrivateIp</p>
</td>
</tr>
<tr id="row986134313370"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p491111145373"><a name="p491111145373"></a><a name="p491111145373"></a>Creating a security group</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11093293373"><a name="p11093293373"></a><a name="p11093293373"></a>security_group</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14882164773714"><a name="p14882164773714"></a><a name="p14882164773714"></a>createSecurityGroup</p>
</td>
</tr>
<tr id="row0861243173713"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p0911141410371"><a name="p0911141410371"></a><a name="p0911141410371"></a>Modifying a security group</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11109132993714"><a name="p11109132993714"></a><a name="p11109132993714"></a>security_group</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18882164723712"><a name="p18882164723712"></a><a name="p18882164723712"></a>modifySecurityGroup</p>
</td>
</tr>
<tr id="row98684333716"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11911191483713"><a name="p11911191483713"></a><a name="p11911191483713"></a>Creating a subnet</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1310962914375"><a name="p1310962914375"></a><a name="p1310962914375"></a>subnet</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p988214733712"><a name="p988214733712"></a><a name="p988214733712"></a>createSubnet</p>
</td>
</tr>
<tr id="row12861043183714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p169118143378"><a name="p169118143378"></a><a name="p169118143378"></a>Deleting a subnet</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18109172923715"><a name="p18109172923715"></a><a name="p18109172923715"></a>subnet</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10882164713373"><a name="p10882164713373"></a><a name="p10882164713373"></a>deleteSubnet</p>
</td>
</tr>
<tr id="row1986154310370"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p19911171414373"><a name="p19911171414373"></a><a name="p19911171414373"></a>Modifying a subnet</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p13109629133718"><a name="p13109629133718"></a><a name="p13109629133718"></a>subnet</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1188264793714"><a name="p1188264793714"></a><a name="p1188264793714"></a>modifySubnet</p>
</td>
</tr>
<tr id="row88724310379"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5911151417376"><a name="p5911151417376"></a><a name="p5911151417376"></a>Creating a VPC</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p16109329193712"><a name="p16109329193712"></a><a name="p16109329193712"></a>vpc</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p138821347143720"><a name="p138821347143720"></a><a name="p138821347143720"></a>createVpc</p>
</td>
</tr>
<tr id="row1987204317379"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1591117148374"><a name="p1591117148374"></a><a name="p1591117148374"></a>Deleting a VPC</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5109629153711"><a name="p5109629153711"></a><a name="p5109629153711"></a>vpc</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p988274715370"><a name="p988274715370"></a><a name="p988274715370"></a>deleteVpc</p>
</td>
</tr>
<tr id="row387124363713"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p139121114193712"><a name="p139121114193712"></a><a name="p139121114193712"></a>Modifying a VPC</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11109122913717"><a name="p11109122913717"></a><a name="p11109122913717"></a>vpc</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10882184713719"><a name="p10882184713719"></a><a name="p10882184713719"></a>modifyVpc</p>
</td>
</tr>
<tr id="row18870434376"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16912314153713"><a name="p16912314153713"></a><a name="p16912314153713"></a>Creating a VPN</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5109162963714"><a name="p5109162963714"></a><a name="p5109162963714"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16882114723713"><a name="p16882114723713"></a><a name="p16882114723713"></a>createVpn</p>
</td>
</tr>
<tr id="row198764323713"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1891271419372"><a name="p1891271419372"></a><a name="p1891271419372"></a>Deleting a VPN</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12109142973717"><a name="p12109142973717"></a><a name="p12109142973717"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p68821047163716"><a name="p68821047163716"></a><a name="p68821047163716"></a>deleteVpn</p>
</td>
</tr>
<tr id="row168716438370"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1912111483719"><a name="p1912111483719"></a><a name="p1912111483719"></a>Modifying a VPN</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p310972915378"><a name="p310972915378"></a><a name="p310972915378"></a>vpn</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1788284713377"><a name="p1788284713377"></a><a name="p1788284713377"></a>modifyVpn</p>
</td>
</tr>
<tr id="row0878433372"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7912101415371"><a name="p7912101415371"></a><a name="p7912101415371"></a>Creating a NAT gateway</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p010982910374"><a name="p010982910374"></a><a name="p010982910374"></a>natgateway</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1883347113711"><a name="p1883347113711"></a><a name="p1883347113711"></a>createNatGateway</p>
</td>
</tr>
<tr id="row128716433377"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1291241493713"><a name="p1291241493713"></a><a name="p1291241493713"></a>Updating a NAT gateway</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6109192993714"><a name="p6109192993714"></a><a name="p6109192993714"></a>natgateway</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10883164719379"><a name="p10883164719379"></a><a name="p10883164719379"></a>updateNatGateway</p>
</td>
</tr>
<tr id="row17881843153716"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8912141417371"><a name="p8912141417371"></a><a name="p8912141417371"></a>Deleting a NAT gateway</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p81096296379"><a name="p81096296379"></a><a name="p81096296379"></a>natgateway</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2883447133720"><a name="p2883447133720"></a><a name="p2883447133720"></a>deleteNatGateway</p>
</td>
</tr>
<tr id="row4881043133718"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1691251413371"><a name="p1691251413371"></a><a name="p1691251413371"></a>Creating an SNAT rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p110932917371"><a name="p110932917371"></a><a name="p110932917371"></a>snatrule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14883047123710"><a name="p14883047123710"></a><a name="p14883047123710"></a>createSnatRule</p>
</td>
</tr>
<tr id="row1888154323716"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p129121314183712"><a name="p129121314183712"></a><a name="p129121314183712"></a>Deleting an SNAT rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p13109112917372"><a name="p13109112917372"></a><a name="p13109112917372"></a>snatrule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19883194720375"><a name="p19883194720375"></a><a name="p19883194720375"></a>deleteSnatRule</p>
</td>
</tr>
<tr id="row1012475273612"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p291251433720"><a name="p291251433720"></a><a name="p291251433720"></a>Creating a DNAT rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p210952910373"><a name="p210952910373"></a><a name="p210952910373"></a>dnatrule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p188839474374"><a name="p188839474374"></a><a name="p188839474374"></a>createDnatRule</p>
</td>
</tr>
<tr id="row1388843123715"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p20912214153714"><a name="p20912214153714"></a><a name="p20912214153714"></a>Deleting a DNAT rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p410952914379"><a name="p410952914379"></a><a name="p410952914379"></a>dnatrule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3883174712378"><a name="p3883174712378"></a><a name="p3883174712378"></a>deleteDnatRule</p>
</td>
</tr>
</tbody>
</table>

