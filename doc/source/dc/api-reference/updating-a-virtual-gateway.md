# Updating a Virtual Gateway<a name="en-dc_topic_0055025326"></a>

## Function<a name="section10267951"></a>

This API is used to update a virtual gateway.

## URI<a name="section25302698"></a>

PUT /v2.0/dcaas/virtual-gateways/\{virtual\_gateway\_id\}

**Table  1**  Parameter description

<a name="table78013327231"></a>
<table><thead align="left"><tr id="row128753217231"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p1587432182316"><a name="p1587432182316"></a><a name="p1587432182316"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.2"><p id="p1694123232312"><a name="p1694123232312"></a><a name="p1694123232312"></a><strong id="b842352706165439"><a name="b842352706165439"></a><a name="b842352706165439"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p894632182312"><a name="p894632182312"></a><a name="p894632182312"></a><strong id="b842352706192549"><a name="b842352706192549"></a><a name="b842352706192549"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="p7941332152315"><a name="p7941332152315"></a><a name="p7941332152315"></a><strong id="b84235270615331"><a name="b84235270615331"></a><a name="b84235270615331"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1994932152311"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p1594203215232"><a name="p1594203215232"></a><a name="p1594203215232"></a>virtual_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.2 "><p id="p794173252315"><a name="p794173252315"></a><a name="p794173252315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p2103173217239"><a name="p2103173217239"></a><a name="p2103173217239"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p010343252316"><a name="p010343252316"></a><a name="p010343252316"></a>Specifies the virtual gateway ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section36252627"></a>

[Table 2](#table50992744154526)  lists the request parameter.

**Table  2**  Request parameter

<a name="table50992744154526"></a>
<table><thead align="left"><tr id="row20073554154526"><th class="cellrowborder" valign="top" width="22.3%" id="mcps1.2.5.1.1"><p id="p15345186154526"><a name="p15345186154526"></a><a name="p15345186154526"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.62%" id="mcps1.2.5.1.2"><p id="p35000534154526"><a name="p35000534154526"></a><a name="p35000534154526"></a><strong id="b939254756"><a name="b939254756"></a><a name="b939254756"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.45%" id="mcps1.2.5.1.3"><p id="p16470999154526"><a name="p16470999154526"></a><a name="p16470999154526"></a><strong id="b1608738349"><a name="b1608738349"></a><a name="b1608738349"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41.63%" id="mcps1.2.5.1.4"><p id="p59082508154526"><a name="p59082508154526"></a><a name="p59082508154526"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20953821154526"><td class="cellrowborder" valign="top" width="22.3%" headers="mcps1.2.5.1.1 "><p id="p19537972154526"><a name="p19537972154526"></a><a name="p19537972154526"></a>virtual_gateway</p>
</td>
<td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.5.1.2 "><p id="p39071862154526"><a name="p39071862154526"></a><a name="p39071862154526"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="17.45%" headers="mcps1.2.5.1.3 "><p id="p10704269154526"><a name="p10704269154526"></a><a name="p10704269154526"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.2.5.1.4 "><p id="p61739489154526"><a name="p61739489154526"></a><a name="p61739489154526"></a>Specifies the <strong id="b842352706191940"><a name="b842352706191940"></a><a name="b842352706191940"></a>virtual_gateway</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **virtual\_gateway**

<a name="table125648759846"></a>
<table><thead align="left"><tr id="row265942339846"><th class="cellrowborder" valign="top" width="25.21%" id="mcps1.1.5.1.1"><p id="p351661709915"><a name="p351661709915"></a><a name="p351661709915"></a><strong id="b8423527069918"><a name="b8423527069918"></a><a name="b8423527069918"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.469999999999999%" id="mcps1.1.5.1.2"><p id="p89913189915"><a name="p89913189915"></a><a name="p89913189915"></a><strong id="b2080908666"><a name="b2080908666"></a><a name="b2080908666"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.02%" id="mcps1.1.5.1.3"><p id="p209180099915"><a name="p209180099915"></a><a name="p209180099915"></a><strong id="b389873230"><a name="b389873230"></a><a name="b389873230"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="45.300000000000004%" id="mcps1.1.5.1.4"><p id="p132751689915"><a name="p132751689915"></a><a name="p132751689915"></a><strong id="b800842364"><a name="b800842364"></a><a name="b800842364"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row66033117145224"><td class="cellrowborder" valign="top" width="25.21%" headers="mcps1.1.5.1.1 "><p id="p15341960145224"><a name="p15341960145224"></a><a name="p15341960145224"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.1.5.1.2 "><p id="p34739281145224"><a name="p34739281145224"></a><a name="p34739281145224"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.02%" headers="mcps1.1.5.1.3 "><p id="p62418382145224"><a name="p62418382145224"></a><a name="p62418382145224"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.300000000000004%" headers="mcps1.1.5.1.4 "><p id="p22724200145224"><a name="p22724200145224"></a><a name="p22724200145224"></a>Provides supplementary information about the virtual gateway.</p>
</td>
</tr>
<tr id="row52076255145224"><td class="cellrowborder" valign="top" width="25.21%" headers="mcps1.1.5.1.1 "><p id="p57161530145224"><a name="p57161530145224"></a><a name="p57161530145224"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.1.5.1.2 "><p id="p66681242145224"><a name="p66681242145224"></a><a name="p66681242145224"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.02%" headers="mcps1.1.5.1.3 "><p id="p32471539145224"><a name="p32471539145224"></a><a name="p32471539145224"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.300000000000004%" headers="mcps1.1.5.1.4 "><p id="p12948972145224"><a name="p12948972145224"></a><a name="p12948972145224"></a>Specifies the virtual gateway name.</p>
</td>
</tr>
<tr id="row22650581145251"><td class="cellrowborder" valign="top" width="25.21%" headers="mcps1.1.5.1.1 "><p id="p38440998145251"><a name="p38440998145251"></a><a name="p38440998145251"></a>local_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.1.5.1.2 "><p id="p26713113145251"><a name="p26713113145251"></a><a name="p26713113145251"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.02%" headers="mcps1.1.5.1.3 "><p id="p16278516145251"><a name="p16278516145251"></a><a name="p16278516145251"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.300000000000004%" headers="mcps1.1.5.1.4 "><p id="p43491424145251"><a name="p43491424145251"></a><a name="p43491424145251"></a>Specifies the ID of the local endpoint group that records CIDRs of the VPC.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section57838187"></a>

[Table 3](#table4284712915501)  lists the response parameter.

**Table  3**  Response parameter

<a name="table4284712915501"></a>
<table><thead align="left"><tr id="row4552452315501"><th class="cellrowborder" valign="top" width="31%" id="mcps1.2.4.1.1"><p id="p6360776715501"><a name="p6360776715501"></a><a name="p6360776715501"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.2"><p id="p5195553615501"><a name="p5195553615501"></a><a name="p5195553615501"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42%" id="mcps1.2.4.1.3"><p id="p3435514315501"><a name="p3435514315501"></a><a name="p3435514315501"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3130318915501"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.1 "><p id="p5253038415501"><a name="p5253038415501"></a><a name="p5253038415501"></a>virtual_gateway</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p2710268715501"><a name="p2710268715501"></a><a name="p2710268715501"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="p4935093915501"><a name="p4935093915501"></a><a name="p4935093915501"></a>Specifies the <strong id="b842352706192031"><a name="b842352706192031"></a><a name="b842352706192031"></a>virtual_gateway</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **virtual\_gateway**

<a name="table49261880"></a>
<table><thead align="left"><tr id="row31386613"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.4.1.1"><p id="p59287744"><a name="p59287744"></a><a name="p59287744"></a><strong id="b75907813"><a name="b75907813"></a><a name="b75907813"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.1.4.1.2"><p id="p37577972"><a name="p37577972"></a><a name="p37577972"></a><strong id="b958788138"><a name="b958788138"></a><a name="b958788138"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.1.4.1.3"><p id="p58217140"><a name="p58217140"></a><a name="p58217140"></a><strong id="b2105260469"><a name="b2105260469"></a><a name="b2105260469"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row22166934145242"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p14291132145242"><a name="p14291132145242"></a><a name="p14291132145242"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p16731007145242"><a name="p16731007145242"></a><a name="p16731007145242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p49150553145242"><a name="p49150553145242"></a><a name="p49150553145242"></a>Specifies the virtual gateway ID.</p>
</td>
</tr>
<tr id="row9919533145242"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p61728820145242"><a name="p61728820145242"></a><a name="p61728820145242"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p33978489145242"><a name="p33978489145242"></a><a name="p33978489145242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p64330433145242"><a name="p64330433145242"></a><a name="p64330433145242"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row8558710145242"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p54898609145242"><a name="p54898609145242"></a><a name="p54898609145242"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p17602321145242"><a name="p17602321145242"></a><a name="p17602321145242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p61586011145242"><a name="p61586011145242"></a><a name="p61586011145242"></a>Specifies the virtual gateway name.</p>
</td>
</tr>
<tr id="row45690210145242"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p372676145242"><a name="p372676145242"></a><a name="p372676145242"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p30186794145242"><a name="p30186794145242"></a><a name="p30186794145242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p17298602145242"><a name="p17298602145242"></a><a name="p17298602145242"></a>Provides supplementary information about the virtual gateway.</p>
</td>
</tr>
<tr id="row27446311145242"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p61323974145242"><a name="p61323974145242"></a><a name="p61323974145242"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p1186027145242"><a name="p1186027145242"></a><a name="p1186027145242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p64008823145242"><a name="p64008823145242"></a><a name="p64008823145242"></a>Specifies the ID of the VPC to be accessed.</p>
</td>
</tr>
<tr id="row40332292145242"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p21771545145242"><a name="p21771545145242"></a><a name="p21771545145242"></a>local_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p18664711145242"><a name="p18664711145242"></a><a name="p18664711145242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p52604433145242"><a name="p52604433145242"></a><a name="p52604433145242"></a>Specifies the ID of the local endpoint group that records CIDRs of the VPC.</p>
</td>
</tr>
<tr id="row49220608145242"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p29470565145242"><a name="p29470565145242"></a><a name="p29470565145242"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p38305526145242"><a name="p38305526145242"></a><a name="p38305526145242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p66972050145242"><a name="p66972050145242"></a><a name="p66972050145242"></a>Specifies the ID of the physical device used by the virtual gateway.</p>
</td>
</tr>
<tr id="row42751658145242"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p34480858145242"><a name="p34480858145242"></a><a name="p34480858145242"></a>redundant_device_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p41486137145242"><a name="p41486137145242"></a><a name="p41486137145242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p64104220145242"><a name="p64104220145242"></a><a name="p64104220145242"></a>Specifies the ID of the redundant physical device used by the virtual gateway.</p>
</td>
</tr>
<tr id="row59091091142819"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p60721963142822"><a name="p60721963142822"></a><a name="p60721963142822"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p19531943142822"><a name="p19531943142822"></a><a name="p19531943142822"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p38261990142822"><a name="p38261990142822"></a><a name="p38261990142822"></a>Specifies the virtual gateway type. The value can be <strong id="b842352706232310"><a name="b842352706232310"></a><a name="b842352706232310"></a>default</strong> or <strong id="b842352706232316"><a name="b842352706232316"></a><a name="b842352706232316"></a>double ipsec</strong>.</p>
</td>
</tr>
<tr id="row36208475104314"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p53182731104317"><a name="p53182731104317"></a><a name="p53182731104317"></a>ipsec_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p12833936104317"><a name="p12833936104317"></a><a name="p12833936104317"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p48943060104317"><a name="p48943060104317"></a><a name="p48943060104317"></a>Specifies the IPsec VPN access bandwidth in Mbit/s.</p>
</td>
</tr>
<tr id="row30049902163617"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p49030808163620"><a name="p49030808163620"></a><a name="p49030808163620"></a>bgp_asn</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p12072537163620"><a name="p12072537163620"></a><a name="p12072537163620"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p38351479163620"><a name="p38351479163620"></a><a name="p38351479163620"></a>Specifies the AS number of the BGP peer.</p>
</td>
</tr>
<tr id="row34576346145242"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p24207219145242"><a name="p24207219145242"></a><a name="p24207219145242"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p14627737145242"><a name="p14627737145242"></a><a name="p14627737145242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p36429021144551"><a name="p36429021144551"></a><a name="p36429021144551"></a>Specifies the virtual gateway status.</p>
<p id="p6910742145242"><a name="p6910742145242"></a><a name="p6910742145242"></a>The value can be <strong id="b84235270617169"><a name="b84235270617169"></a><a name="b84235270617169"></a>ACTIVE</strong>, <strong id="b842352706171613"><a name="b842352706171613"></a><a name="b842352706171613"></a>DOWN</strong>, <strong id="b842352706171618"><a name="b842352706171618"></a><a name="b842352706171618"></a>BUILD</strong>, <strong id="b842352706171622"><a name="b842352706171622"></a><a name="b842352706171622"></a>ERROR</strong>, <strong id="b842352706171626"><a name="b842352706171626"></a><a name="b842352706171626"></a>PENDING_CREATE</strong>, <strong id="b842352706171630"><a name="b842352706171630"></a><a name="b842352706171630"></a>PENDING_UPDATE</strong>, or <strong id="b842352706171633"><a name="b842352706171633"></a><a name="b842352706171633"></a>PENDING_DELETE</strong>.</p>
</td>
</tr>
<tr id="row26211437145242"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p4766768145242"><a name="p4766768145242"></a><a name="p4766768145242"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p50563943145242"><a name="p50563943145242"></a><a name="p50563943145242"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.4.1.3 "><p id="p20943989144556"><a name="p20943989144556"></a><a name="p20943989144556"></a>Specifies the administrative state of the virtual gateway.</p>
<p id="p30920819145242"><a name="p30920819145242"></a><a name="p30920819145242"></a>The value can be <strong id="b842352706154840"><a name="b842352706154840"></a><a name="b842352706154840"></a>true</strong> or <strong id="b842352706154844"><a name="b842352706154844"></a><a name="b842352706154844"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section5055526711495"></a>

-   Example request

    ```
    PUT /v2.0/dcaas/virtual-gateways/{virtual_gateway_id}
    {
        "virtual_gateway" : {
            "name" : "virtual gateway1",
            "description" : "New description"
        }
    }
    ```


-   Example response

    ```
    {        
         "virtual_gateway" : {
            "id" : "7ec892f3-ca64-46c7-863f-a2eb1b9e8389",
            "tenant_id" : "6fbe9263116a4b68818cf1edce16bc4f",
            "name" : "virtual gateway1",
            "description" : "New description",
            "vpc_id" : "908d9cf3-da64-4acb-393f-e5eb6b9e838a",
            "local_ep_group_id" : "f8834cf1-5468-87c7-223d-56e78b9699ab",
            "device_id" : "aaa_01"
        }
    }
    ```


## Returned Value<a name="section1374333103913"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

