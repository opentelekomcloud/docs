# Error Codes<a name="en_topic_0093011523"></a>

<a name="table181291039195511"></a>
<table><tbody><tr id="row83958397552"><td class="cellrowborder" valign="top" width="10.85%"><p id="p2395193925511"><a name="p2395193925511"></a><a name="p2395193925511"></a><strong id="b842352706183013"><a name="b842352706183013"></a><a name="b842352706183013"></a>Service</strong></p>
</td>
<td class="cellrowborder" valign="top" width="14.91%"><p id="p203951439125511"><a name="p203951439125511"></a><a name="p203951439125511"></a><strong id="b84235270614475"><a name="b84235270614475"></a><a name="b84235270614475"></a>Error Code</strong></p>
</td>
<td class="cellrowborder" valign="top" width="14.19%"><p id="p7395103919554"><a name="p7395103919554"></a><a name="p7395103919554"></a><strong id="b170187709114474"><a name="b170187709114474"></a><a name="b170187709114474"></a>HTTP Status Code</strong></p>
</td>
<td class="cellrowborder" valign="top" width="16.63%"><p id="p133950397555"><a name="p133950397555"></a><a name="p133950397555"></a><strong id="b842352706151625"><a name="b842352706151625"></a><a name="b842352706151625"></a>Description</strong></p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%"><p id="p339543914556"><a name="p339543914556"></a><a name="p339543914556"></a><strong id="b84235270616428"><a name="b84235270616428"></a><a name="b84235270616428"></a>Handling Measure</strong></p>
</td>
</tr>
<tr id="row43953395555"><td class="cellrowborder" rowspan="18" valign="top" width="10.85%"><p id="p3395123915519"><a name="p3395123915519"></a><a name="p3395123915519"></a>VPN</p>
</td>
<td class="cellrowborder" valign="top" width="14.91%"><p id="p18395113975515"><a name="p18395113975515"></a><a name="p18395113975515"></a>VPC.1001</p>
</td>
<td class="cellrowborder" valign="top" width="14.19%"><p id="p1939519396554"><a name="p1939519396554"></a><a name="p1939519396554"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.63%"><p id="p123951839145515"><a name="p123951839145515"></a><a name="p123951839145515"></a>Invalid VPN parameters.</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%"><p id="p1639553945519"><a name="p1639553945519"></a><a name="p1639553945519"></a>Correct the parameter settings and send the request again.</p>
</td>
</tr>
<tr id="row183951639165511"><td class="cellrowborder" valign="top"><p id="p19395139165518"><a name="p19395139165518"></a><a name="p19395139165518"></a>VPC.1002</p>
</td>
<td class="cellrowborder" valign="top"><p id="p839533925519"><a name="p839533925519"></a><a name="p839533925519"></a>500</p>
</td>
<td class="cellrowborder" valign="top"><p id="p17395153915518"><a name="p17395153915518"></a><a name="p17395153915518"></a>Internal server error.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p16395143911553"><a name="p16395143911553"></a><a name="p16395143911553"></a>System exception. Try again later.</p>
</td>
</tr>
<tr id="row93956399554"><td class="cellrowborder" valign="top"><p id="p1539583995515"><a name="p1539583995515"></a><a name="p1539583995515"></a>VPC.1003</p>
</td>
<td class="cellrowborder" valign="top"><p id="p639516392553"><a name="p639516392553"></a><a name="p639516392553"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p17395939165514"><a name="p17395939165514"></a><a name="p17395939165514"></a>The quota limit has been reached.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p1939518398557"><a name="p1939518398557"></a><a name="p1939518398557"></a>Increase the VPN connection quota.</p>
</td>
</tr>
<tr id="row1439513399556"><td class="cellrowborder" valign="top"><p id="p33956398551"><a name="p33956398551"></a><a name="p33956398551"></a>VPC.1004</p>
</td>
<td class="cellrowborder" valign="top"><p id="p4395103925515"><a name="p4395103925515"></a><a name="p4395103925515"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p239518396555"><a name="p239518396555"></a><a name="p239518396555"></a>The remote gateway is being used by another VPN connection.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p039519397559"><a name="p039519397559"></a><a name="p039519397559"></a>Change the IP address and then create the connection.</p>
</td>
</tr>
<tr id="row1539510397553"><td class="cellrowborder" valign="top"><p id="p1939563911558"><a name="p1939563911558"></a><a name="p1939563911558"></a>VPC.1016</p>
</td>
<td class="cellrowborder" valign="top"><p id="p439523914552"><a name="p439523914552"></a><a name="p439523914552"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p17395113965515"><a name="p17395113965515"></a><a name="p17395113965515"></a>The VPN remote subnet is the same as the local subnet.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p439516393554"><a name="p439516393554"></a><a name="p439516393554"></a>Change the subnet to ensure that the local and remote subnets are different.</p>
</td>
</tr>
<tr id="row439503919551"><td class="cellrowborder" valign="top"><p id="p11395103925518"><a name="p11395103925518"></a><a name="p11395103925518"></a>VPC.1017</p>
</td>
<td class="cellrowborder" valign="top"><p id="p11395183955513"><a name="p11395183955513"></a><a name="p11395183955513"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p5395133916559"><a name="p5395133916559"></a><a name="p5395133916559"></a>You do not have permission to perform this operation.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p8498134314312"><a name="p8498134314312"></a><a name="p8498134314312"></a>Perform another operation, or obtain the required permission and try again.</p>
</td>
</tr>
<tr id="row34031239185512"><td class="cellrowborder" valign="top"><p id="p1540312393551"><a name="p1540312393551"></a><a name="p1540312393551"></a>VPC.1018</p>
</td>
<td class="cellrowborder" valign="top"><p id="p16403173917557"><a name="p16403173917557"></a><a name="p16403173917557"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p174038394557"><a name="p174038394557"></a><a name="p174038394557"></a>Both the local and remote subnets are being used by other VPNs.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p12403139155519"><a name="p12403139155519"></a><a name="p12403139155519"></a>Change the subnets or delete existing VPN subnets.</p>
</td>
</tr>
<tr id="row3403113945513"><td class="cellrowborder" valign="top"><p id="p0403539125514"><a name="p0403539125514"></a><a name="p0403539125514"></a>VPC.1019</p>
</td>
<td class="cellrowborder" valign="top"><p id="p18403183918551"><a name="p18403183918551"></a><a name="p18403183918551"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p8403239105513"><a name="p8403239105513"></a><a name="p8403239105513"></a>The local gateway IP address you specified is in use.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p18834423337"><a name="p18834423337"></a><a name="p18834423337"></a>Specify another local gateway IP address.</p>
</td>
</tr>
<tr id="row64034396558"><td class="cellrowborder" valign="top"><p id="p15403103965515"><a name="p15403103965515"></a><a name="p15403103965515"></a>VPC.1020</p>
</td>
<td class="cellrowborder" valign="top"><p id="p6403839165517"><a name="p6403839165517"></a><a name="p6403839165517"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p44035393553"><a name="p44035393553"></a><a name="p44035393553"></a>Failed to create the VPN connection.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p1640314398550"><a name="p1640314398550"></a><a name="p1640314398550"></a>System error. Contact technical support.</p>
</td>
</tr>
<tr id="row640353925511"><td class="cellrowborder" valign="top"><p id="p9403163935510"><a name="p9403163935510"></a><a name="p9403163935510"></a>VPC.1021</p>
</td>
<td class="cellrowborder" valign="top"><p id="p1740383905518"><a name="p1740383905518"></a><a name="p1740383905518"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p040318399557"><a name="p040318399557"></a><a name="p040318399557"></a>The remote subnet of the VPN is in use.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p14403103913556"><a name="p14403103913556"></a><a name="p14403103913556"></a>Select another remote subnet for the VPN.</p>
</td>
</tr>
<tr id="row740311398550"><td class="cellrowborder" valign="top"><p id="p1340373965511"><a name="p1340373965511"></a><a name="p1340373965511"></a>VPC.1023</p>
</td>
<td class="cellrowborder" valign="top"><p id="p64038393552"><a name="p64038393552"></a><a name="p64038393552"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p11403103985510"><a name="p11403103985510"></a><a name="p11403103985510"></a>Failed to query the VPN gateway.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p128471845811"><a name="p128471845811"></a><a name="p128471845811"></a>System error. Contact technical support.</p>
</td>
</tr>
<tr id="row9403133918558"><td class="cellrowborder" valign="top"><p id="p1640363985510"><a name="p1640363985510"></a><a name="p1640363985510"></a>VPC.1024</p>
</td>
<td class="cellrowborder" valign="top"><p id="p124030390553"><a name="p124030390553"></a><a name="p124030390553"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p18403163919554"><a name="p18403163919554"></a><a name="p18403163919554"></a>Failed to create the VPN gateway.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p1615232213411"><a name="p1615232213411"></a><a name="p1615232213411"></a>System error. Contact technical support.</p>
</td>
</tr>
<tr id="row1403123916551"><td class="cellrowborder" valign="top"><p id="p1840310394554"><a name="p1840310394554"></a><a name="p1840310394554"></a>VPC.1025</p>
</td>
<td class="cellrowborder" valign="top"><p id="p14403153955516"><a name="p14403153955516"></a><a name="p14403153955516"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p13403133919557"><a name="p13403133919557"></a><a name="p13403133919557"></a>Failed to update the VPN gateway.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p1230214239415"><a name="p1230214239415"></a><a name="p1230214239415"></a>System error. Contact technical support.</p>
</td>
</tr>
<tr id="row040323914558"><td class="cellrowborder" valign="top"><p id="p240319395558"><a name="p240319395558"></a><a name="p240319395558"></a>VPC.1026</p>
</td>
<td class="cellrowborder" valign="top"><p id="p04031139205520"><a name="p04031139205520"></a><a name="p04031139205520"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p1140317399552"><a name="p1140317399552"></a><a name="p1140317399552"></a>The VPN gateway already exists.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p18352024643"><a name="p18352024643"></a><a name="p18352024643"></a>System error. Contact technical support.</p>
</td>
</tr>
<tr id="row24038391551"><td class="cellrowborder" valign="top"><p id="p1240313913557"><a name="p1240313913557"></a><a name="p1240313913557"></a>VPC.1027</p>
</td>
<td class="cellrowborder" valign="top"><p id="p1840319396553"><a name="p1840319396553"></a><a name="p1840319396553"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p1240363914551"><a name="p1240363914551"></a><a name="p1240363914551"></a>Failed to create the VPN gateway.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p13403113916552"><a name="p13403113916552"></a><a name="p13403113916552"></a>System error. Contact technical support.</p>
</td>
</tr>
<tr id="row19403193913558"><td class="cellrowborder" valign="top"><p id="p940316391552"><a name="p940316391552"></a><a name="p940316391552"></a>VPC.1028</p>
</td>
<td class="cellrowborder" valign="top"><p id="p114031639135516"><a name="p114031639135516"></a><a name="p114031639135516"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p54031739205516"><a name="p54031739205516"></a><a name="p54031739205516"></a>Failed to create the VPN gateway.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p154021825445"><a name="p154021825445"></a><a name="p154021825445"></a>System error. Contact technical support.</p>
</td>
</tr>
<tr id="row740318398555"><td class="cellrowborder" valign="top"><p id="p1740393913556"><a name="p1740393913556"></a><a name="p1740393913556"></a>VPC.1029</p>
</td>
<td class="cellrowborder" valign="top"><p id="p240373910553"><a name="p240373910553"></a><a name="p240373910553"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p174031339125510"><a name="p174031339125510"></a><a name="p174031339125510"></a>Failed to allocate bandwidth to the VPN gateway.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p59115261241"><a name="p59115261241"></a><a name="p59115261241"></a>System error. Contact technical support.</p>
</td>
</tr>
<tr id="row14403163918552"><td class="cellrowborder" valign="top"><p id="p14403153910557"><a name="p14403153910557"></a><a name="p14403153910557"></a>VPC.1030</p>
</td>
<td class="cellrowborder" valign="top"><p id="p13403123925510"><a name="p13403123925510"></a><a name="p13403123925510"></a>400</p>
</td>
<td class="cellrowborder" valign="top"><p id="p15403193965518"><a name="p15403193965518"></a><a name="p15403193965518"></a>Failed to allocate bandwidth to the VPN gateway.</p>
</td>
<td class="cellrowborder" valign="top"><p id="p5770122615414"><a name="p5770122615414"></a><a name="p5770122615414"></a>System error. Contact technical support.</p>
</td>
</tr>
</tbody>
</table>

