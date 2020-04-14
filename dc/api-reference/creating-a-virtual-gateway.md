# Creating a Virtual Gateway<a name="en-dc_topic_0055025322"></a>

## Function<a name="section17487184"></a>

This API is used to create a virtual gateway.

## URI<a name="section853188092910"></a>

POST /v2.0/dcaas/virtual-gateways

**Table  1**  Parameter description

<a name="table116196219413"></a>
<table><thead align="left"><tr id="row1162611216418"><th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.1"><p id="p3628921415"><a name="p3628921415"></a><a name="p3628921415"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.25%" id="mcps1.2.5.1.2"><p id="p126302264110"><a name="p126302264110"></a><a name="p126302264110"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="8.25%" id="mcps1.2.5.1.3"><p id="p1463272144111"><a name="p1463272144111"></a><a name="p1463272144111"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="69.07%" id="mcps1.2.5.1.4"><p id="p66345214415"><a name="p66345214415"></a><a name="p66345214415"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row463615254119"><td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.1 "><p id="p16638723418"><a name="p16638723418"></a><a name="p16638723418"></a>virtual_gateway</p>
</td>
<td class="cellrowborder" valign="top" width="8.25%" headers="mcps1.2.5.1.2 "><p id="p1263922194115"><a name="p1263922194115"></a><a name="p1263922194115"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="8.25%" headers="mcps1.2.5.1.3 "><p id="p1642721414"><a name="p1642721414"></a><a name="p1642721414"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="69.07%" headers="mcps1.2.5.1.4 "><p id="p14646152154117"><a name="p14646152154117"></a><a name="p14646152154117"></a>Specifies the <strong id="b8423527061905"><a name="b8423527061905"></a><a name="b8423527061905"></a>virtual_gateway</strong> object.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section2281784192910"></a>

[Table 2](#table3523051192910)  lists the  **virtual\_gateway**  parameters.

**Table  2**  Request parameters

<a name="table3523051192910"></a>
<table><thead align="left"><tr id="row1307920992910"><th class="cellrowborder" valign="top" width="21.007899210078993%" id="mcps1.2.5.1.1"><p id="p4450739192910"><a name="p4450739192910"></a><a name="p4450739192910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.23887611238876%" id="mcps1.2.5.1.2"><p id="p26394292910"><a name="p26394292910"></a><a name="p26394292910"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.04819518048195%" id="mcps1.2.5.1.3"><p id="p6472145192910"><a name="p6472145192910"></a><a name="p6472145192910"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="49.7050294970503%" id="mcps1.2.5.1.4"><p id="p6443764692910"><a name="p6443764692910"></a><a name="p6443764692910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2660185192910"><td class="cellrowborder" valign="top" width="21.007899210078993%" headers="mcps1.2.5.1.1 "><p id="p3605816293239"><a name="p3605816293239"></a><a name="p3605816293239"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.23887611238876%" headers="mcps1.2.5.1.2 "><p id="p6629905993311"><a name="p6629905993311"></a><a name="p6629905993311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.3 "><p id="p5941630693257"><a name="p5941630693257"></a><a name="p5941630693257"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.5.1.4 "><p id="p1074630693412"><a name="p1074630693412"></a><a name="p1074630693412"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row2405214492910"><td class="cellrowborder" valign="top" width="21.007899210078993%" headers="mcps1.2.5.1.1 "><p id="p1588715393239"><a name="p1588715393239"></a><a name="p1588715393239"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11.23887611238876%" headers="mcps1.2.5.1.2 "><p id="p2631109893311"><a name="p2631109893311"></a><a name="p2631109893311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.3 "><p id="p1210552293257"><a name="p1210552293257"></a><a name="p1210552293257"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.5.1.4 "><p id="p464917193412"><a name="p464917193412"></a><a name="p464917193412"></a>Specifies the virtual gateway name.</p>
</td>
</tr>
<tr id="row5264583392910"><td class="cellrowborder" valign="top" width="21.007899210078993%" headers="mcps1.2.5.1.1 "><p id="p4444139293239"><a name="p4444139293239"></a><a name="p4444139293239"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="11.23887611238876%" headers="mcps1.2.5.1.2 "><p id="p45532693311"><a name="p45532693311"></a><a name="p45532693311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.3 "><p id="p3573563593257"><a name="p3573563593257"></a><a name="p3573563593257"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.5.1.4 "><p id="p6458631593412"><a name="p6458631593412"></a><a name="p6458631593412"></a>Provides supplementary information about the virtual gateway.</p>
</td>
</tr>
<tr id="row677461492910"><td class="cellrowborder" valign="top" width="21.007899210078993%" headers="mcps1.2.5.1.1 "><p id="p3751344893239"><a name="p3751344893239"></a><a name="p3751344893239"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.23887611238876%" headers="mcps1.2.5.1.2 "><p id="p1832518793311"><a name="p1832518793311"></a><a name="p1832518793311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.3 "><p id="p3680570793257"><a name="p3680570793257"></a><a name="p3680570793257"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.5.1.4 "><p id="p4777447793412"><a name="p4777447793412"></a><a name="p4777447793412"></a>Specifies the ID of the VPC to be accessed.</p>
</td>
</tr>
<tr id="row2673906492910"><td class="cellrowborder" valign="top" width="21.007899210078993%" headers="mcps1.2.5.1.1 "><p id="p2167589193239"><a name="p2167589193239"></a><a name="p2167589193239"></a>local_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.23887611238876%" headers="mcps1.2.5.1.2 "><p id="p1287368693311"><a name="p1287368693311"></a><a name="p1287368693311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.3 "><p id="p2246540693257"><a name="p2246540693257"></a><a name="p2246540693257"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.5.1.4 "><p id="p3012004693412"><a name="p3012004693412"></a><a name="p3012004693412"></a>Specifies the ID of the local endpoint group that records CIDRs of the VPC.</p>
<p id="p5580254111215"><a name="p5580254111215"></a><a name="p5580254111215"></a>For details about how to obtain the ID, see section <a href="creating-an-endpoint-group.md">Creating an Endpoint Group</a>.</p>
</td>
</tr>
<tr id="row4354445992910"><td class="cellrowborder" valign="top" width="21.007899210078993%" headers="mcps1.2.5.1.1 "><p id="p40746793239"><a name="p40746793239"></a><a name="p40746793239"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.23887611238876%" headers="mcps1.2.5.1.2 "><p id="p5176382993311"><a name="p5176382993311"></a><a name="p5176382993311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.3 "><p id="p4979474293257"><a name="p4979474293257"></a><a name="p4979474293257"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.5.1.4 "><p id="p384989993412"><a name="p384989993412"></a><a name="p384989993412"></a>Specifies the ID of the physical device used by the virtual gateway.</p>
</td>
</tr>
<tr id="row4939414495544"><td class="cellrowborder" valign="top" width="21.007899210078993%" headers="mcps1.2.5.1.1 "><p id="p5641288995553"><a name="p5641288995553"></a><a name="p5641288995553"></a>redundant_device_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.23887611238876%" headers="mcps1.2.5.1.2 "><p id="p1681455295553"><a name="p1681455295553"></a><a name="p1681455295553"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.3 "><p id="p2527378495553"><a name="p2527378495553"></a><a name="p2527378495553"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.5.1.4 "><p id="p4245896095553"><a name="p4245896095553"></a><a name="p4245896095553"></a>Specifies the ID of the redundant physical device used by the virtual gateway.</p>
</td>
</tr>
<tr id="row43184565141256"><td class="cellrowborder" valign="top" width="21.007899210078993%" headers="mcps1.2.5.1.1 "><p id="p5942965514139"><a name="p5942965514139"></a><a name="p5942965514139"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="11.23887611238876%" headers="mcps1.2.5.1.2 "><p id="p4907275914139"><a name="p4907275914139"></a><a name="p4907275914139"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.3 "><p id="p30502401142656"><a name="p30502401142656"></a><a name="p30502401142656"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.5.1.4 "><p id="p4515284414139"><a name="p4515284414139"></a><a name="p4515284414139"></a>Specifies the virtual gateway type. The value can be <strong id="b842352706232310"><a name="b842352706232310"></a><a name="b842352706232310"></a>default</strong> or <strong id="b842352706232316"><a name="b842352706232316"></a><a name="b842352706232316"></a>double ipsec</strong>.</p>
</td>
</tr>
<tr id="row38240519104130"><td class="cellrowborder" valign="top" width="21.007899210078993%" headers="mcps1.2.5.1.1 "><p id="p26063336104152"><a name="p26063336104152"></a><a name="p26063336104152"></a>ipsec_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="11.23887611238876%" headers="mcps1.2.5.1.2 "><p id="p30755435104152"><a name="p30755435104152"></a><a name="p30755435104152"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.3 "><p id="p2573087104130"><a name="p2573087104130"></a><a name="p2573087104130"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.5.1.4 "><p id="p7093483104130"><a name="p7093483104130"></a><a name="p7093483104130"></a>Specifies the IPsec VPN access bandwidth in Mbit/s.</p>
</td>
</tr>
<tr id="row2117305145558"><td class="cellrowborder" valign="top" width="21.007899210078993%" headers="mcps1.2.5.1.1 "><p id="p18899583145634"><a name="p18899583145634"></a><a name="p18899583145634"></a>bgp_asn</p>
</td>
<td class="cellrowborder" valign="top" width="11.23887611238876%" headers="mcps1.2.5.1.2 "><p id="p55039507145634"><a name="p55039507145634"></a><a name="p55039507145634"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.3 "><p id="p50091417145634"><a name="p50091417145634"></a><a name="p50091417145634"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.5.1.4 "><p id="p47443661145634"><a name="p47443661145634"></a><a name="p47443661145634"></a>Specifies the AS number of the BGP peer.</p>
</td>
</tr>
<tr id="row6233967292910"><td class="cellrowborder" valign="top" width="21.007899210078993%" headers="mcps1.2.5.1.1 "><p id="p6228249193239"><a name="p6228249193239"></a><a name="p6228249193239"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="11.23887611238876%" headers="mcps1.2.5.1.2 "><p id="p682237893311"><a name="p682237893311"></a><a name="p682237893311"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.3 "><p id="p386476593257"><a name="p386476593257"></a><a name="p386476593257"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.5.1.4 "><p id="p5996447511383"><a name="p5996447511383"></a><a name="p5996447511383"></a>Specifies the virtual gateway administrative status.</p>
<p id="p5798730593412"><a name="p5798730593412"></a><a name="p5798730593412"></a>The value can be <strong id="b842352706154840"><a name="b842352706154840"></a><a name="b842352706154840"></a>true</strong> or <strong id="b842352706154844"><a name="b842352706154844"></a><a name="b842352706154844"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1915447592910"></a>

[Table 3](#table50992744154526)  lists the response parameter.

**Table  3**  Response parameter

<a name="table50992744154526"></a>
<table><thead align="left"><tr id="row20073554154526"><th class="cellrowborder" valign="top" width="29.000000000000004%" id="mcps1.2.4.1.1"><p id="p15345186154526"><a name="p15345186154526"></a><a name="p15345186154526"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="36.00000000000001%" id="mcps1.2.4.1.2"><p id="p35000534154526"><a name="p35000534154526"></a><a name="p35000534154526"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="35%" id="mcps1.2.4.1.3"><p id="p59082508154526"><a name="p59082508154526"></a><a name="p59082508154526"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20953821154526"><td class="cellrowborder" valign="top" width="29.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p19537972154526"><a name="p19537972154526"></a><a name="p19537972154526"></a>virtual_gateway</p>
</td>
<td class="cellrowborder" valign="top" width="36.00000000000001%" headers="mcps1.2.4.1.2 "><p id="p39071862154526"><a name="p39071862154526"></a><a name="p39071862154526"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.3 "><p id="p61739489154526"><a name="p61739489154526"></a><a name="p61739489154526"></a>Specifies the <strong id="b84235270619636"><a name="b84235270619636"></a><a name="b84235270619636"></a>virtual_gateway</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **virtual\_gateway**

<a name="table6599744292910"></a>
<table><thead align="left"><tr id="row1344591292910"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.4.1.1"><p id="p4888289392910"><a name="p4888289392910"></a><a name="p4888289392910"></a><strong id="b8423527069918"><a name="b8423527069918"></a><a name="b8423527069918"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33%" id="mcps1.1.4.1.2"><p id="p228436892910"><a name="p228436892910"></a><a name="p228436892910"></a><strong id="b842352706165439"><a name="b842352706165439"></a><a name="b842352706165439"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38%" id="mcps1.1.4.1.3"><p id="p1567805992910"><a name="p1567805992910"></a><a name="p1567805992910"></a><strong id="b84235270615331"><a name="b84235270615331"></a><a name="b84235270615331"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row557857592910"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.1 "><p id="p2232642692910"><a name="p2232642692910"></a><a name="p2232642692910"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.4.1.2 "><p id="p4674730592910"><a name="p4674730592910"></a><a name="p4674730592910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.4.1.3 "><p id="p5414758192910"><a name="p5414758192910"></a><a name="p5414758192910"></a>Specifies the virtual gateway ID.</p>
</td>
</tr>
<tr id="row2072208492910"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.1 "><p id="p6213532593429"><a name="p6213532593429"></a><a name="p6213532593429"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.4.1.2 "><p id="p6202319293429"><a name="p6202319293429"></a><a name="p6202319293429"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.4.1.3 "><p id="p4865392993429"><a name="p4865392993429"></a><a name="p4865392993429"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row2092257692910"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.1 "><p id="p4220277893429"><a name="p4220277893429"></a><a name="p4220277893429"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.4.1.2 "><p id="p3104281293429"><a name="p3104281293429"></a><a name="p3104281293429"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.4.1.3 "><p id="p2203472093429"><a name="p2203472093429"></a><a name="p2203472093429"></a>Specifies the virtual gateway name.</p>
</td>
</tr>
<tr id="row404465492910"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.1 "><p id="p1666196693429"><a name="p1666196693429"></a><a name="p1666196693429"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.4.1.2 "><p id="p5183306893429"><a name="p5183306893429"></a><a name="p5183306893429"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.4.1.3 "><p id="p4233879693429"><a name="p4233879693429"></a><a name="p4233879693429"></a>Provides supplementary information about the virtual gateway.</p>
</td>
</tr>
<tr id="row611136292910"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.1 "><p id="p3425966893429"><a name="p3425966893429"></a><a name="p3425966893429"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.4.1.2 "><p id="p5237210693429"><a name="p5237210693429"></a><a name="p5237210693429"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.4.1.3 "><p id="p436434393429"><a name="p436434393429"></a><a name="p436434393429"></a>Specifies the ID of the VPC to be accessed.</p>
</td>
</tr>
<tr id="row4800353492910"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.1 "><p id="p1364920093429"><a name="p1364920093429"></a><a name="p1364920093429"></a>local_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.4.1.2 "><p id="p5788847893429"><a name="p5788847893429"></a><a name="p5788847893429"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.4.1.3 "><p id="p6014873093429"><a name="p6014873093429"></a><a name="p6014873093429"></a>Specifies the ID of the local endpoint group that records CIDRs of the VPC.</p>
</td>
</tr>
<tr id="row4957271792910"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.1 "><p id="p374837693429"><a name="p374837693429"></a><a name="p374837693429"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.4.1.2 "><p id="p715986393429"><a name="p715986393429"></a><a name="p715986393429"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.4.1.3 "><p id="p5627825093429"><a name="p5627825093429"></a><a name="p5627825093429"></a>Specifies the ID of the physical device used by the virtual gateway.</p>
</td>
</tr>
<tr id="row467092395323"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.1 "><p id="p5631205595338"><a name="p5631205595338"></a><a name="p5631205595338"></a>redundant_device_id</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.4.1.2 "><p id="p1395232595338"><a name="p1395232595338"></a><a name="p1395232595338"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.4.1.3 "><p id="p6315446495338"><a name="p6315446495338"></a><a name="p6315446495338"></a>Specifies the ID of the redundant physical device used by the virtual gateway.</p>
</td>
</tr>
<tr id="row27709212142417"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.1 "><p id="p65101698142435"><a name="p65101698142435"></a><a name="p65101698142435"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.4.1.2 "><p id="p38746165142435"><a name="p38746165142435"></a><a name="p38746165142435"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.4.1.3 "><p id="p5212668142435"><a name="p5212668142435"></a><a name="p5212668142435"></a>Specifies the virtual gateway type. The value can be <strong id="b1168670605"><a name="b1168670605"></a><a name="b1168670605"></a>default</strong> or <strong id="b66334502"><a name="b66334502"></a><a name="b66334502"></a>double ipsec</strong>.</p>
</td>
</tr>
<tr id="row26313399104224"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.1 "><p id="p10207605104227"><a name="p10207605104227"></a><a name="p10207605104227"></a>ipsec_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.4.1.2 "><p id="p21509689104227"><a name="p21509689104227"></a><a name="p21509689104227"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.4.1.3 "><p id="p62237721104227"><a name="p62237721104227"></a><a name="p62237721104227"></a>Specifies the IPsec VPN access bandwidth in Mbit/s.</p>
</td>
</tr>
<tr id="row22969468145650"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.1 "><p id="p39548374145653"><a name="p39548374145653"></a><a name="p39548374145653"></a>bgp_asn</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.4.1.2 "><p id="p49445541145653"><a name="p49445541145653"></a><a name="p49445541145653"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.4.1.3 "><p id="p47334382145653"><a name="p47334382145653"></a><a name="p47334382145653"></a>Specifies the AS number of the BGP peer.</p>
</td>
</tr>
<tr id="row169233392910"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.1 "><p id="p772042793429"><a name="p772042793429"></a><a name="p772042793429"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.4.1.2 "><p id="p6460901893429"><a name="p6460901893429"></a><a name="p6460901893429"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.4.1.3 "><p id="p11396196113834"><a name="p11396196113834"></a><a name="p11396196113834"></a>Specifies the administrative state of the virtual gateway.</p>
<p id="p1809396693429"><a name="p1809396693429"></a><a name="p1809396693429"></a>The value can be <strong id="b17212656113625"><a name="b17212656113625"></a><a name="b17212656113625"></a>true</strong> or <strong id="b18750106113625"><a name="b18750106113625"></a><a name="b18750106113625"></a>false</strong>.</p>
</td>
</tr>
<tr id="row10232124744112"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.4.1.1 "><p id="p1223214715417"><a name="p1223214715417"></a><a name="p1223214715417"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.4.1.2 "><p id="p78651554413"><a name="p78651554413"></a><a name="p78651554413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.1.4.1.3 "><p id="p1286513554418"><a name="p1286513554418"></a><a name="p1286513554418"></a>Specifies the operating status. Possible values are: <strong id="b11729142384117"><a name="b11729142384117"></a><a name="b11729142384117"></a>ACTIVE</strong>, <strong id="b87382233419"><a name="b87382233419"></a><a name="b87382233419"></a>DOWN</strong>, <strong id="b1273972310413"><a name="b1273972310413"></a><a name="b1273972310413"></a>BUILD</strong>, <strong id="b574117234419"><a name="b574117234419"></a><a name="b574117234419"></a>ERROR</strong>, <strong id="b1674115235414"><a name="b1674115235414"></a><a name="b1674115235414"></a>PENDING_CREATE</strong>, <strong id="b157411923134111"><a name="b157411923134111"></a><a name="b157411923134111"></a>PENDING_UPDATE</strong>, and <strong id="b15742102394114"><a name="b15742102394114"></a><a name="b15742102394114"></a>PENDING_DELETE</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section5174176392910"></a>

-   Example request

    ```
    POST /v2.0/dcaas/virtual-gateways
    {
        "virtual_gateway" : {
            "name" : "virtual gateway1",
            "vpc_id" : "908d9cf3-da64-4acb-393f-e5eb6b9e838a",
            "local_ep_group_id" : "f8834cf1-5468-87c7-223d-56e78b9699ab",
            "device_id" : "aaa_01"
        }
    }
    ```


-   Example response

    ```
    {
        "virtual_gateway":{
            "status": "PENDING_CREATE",
            "redundant_device_id": "", 
            "description":"",
            "admin_state_up": true,
            "tenant_id": "6fbe9263116a4b68818cf1edce16bc4f",
            "name": "virtual gateway1",
            "local_ep_group_id":"011856d0-e1b0-4d78-b83a-edd67801764b",
            "vpc_id":"908d9cf3-da64-4acb-393f-e5eb6b9e838a",
            "device_id":"70.202.5.206",
            "type": "default",
            "id":"97b87776-49e3-44a4-ac4c-8f9156a360cd",
            "ipsec_bandwidth":1
        }
    }
    ```


## Returned Value<a name="sd936e658d4c44ad2b8ae55a74398fcd9"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

