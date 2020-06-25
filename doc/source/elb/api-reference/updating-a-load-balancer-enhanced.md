# Updating a Load Balancer<a name="EN-US_TOPIC_0141008274"></a>

## Function<a name="en-us_topic_0096561536_en-us_topic_0049139635_section53558972"></a>

This API is used to update the name or description of a load balancer.

## URI<a name="en-us_topic_0096561536_en-us_topic_0049139635_section12268704"></a>

PUT /v2.0/lbaas/loadbalancers/\{loadbalancer\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0096561536_table758513315356"></a>
<table><thead align="left"><tr id="en-us_topic_0096561536_row9719153143511"><th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.1"><p id="en-us_topic_0096561536_p1271943123520"><a name="en-us_topic_0096561536_p1271943123520"></a><a name="en-us_topic_0096561536_p1271943123520"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.2.5.1.2"><p id="en-us_topic_0096561536_p117192317355"><a name="en-us_topic_0096561536_p117192317355"></a><a name="en-us_topic_0096561536_p117192317355"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="p13521733113410"><a name="p13521733113410"></a><a name="p13521733113410"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.59595959595959%" id="mcps1.2.5.1.4"><p id="en-us_topic_0096561536_p2072010311352"><a name="en-us_topic_0096561536_p2072010311352"></a><a name="en-us_topic_0096561536_p2072010311352"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561536_row107201323518"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561536_p672019343513"><a name="en-us_topic_0096561536_p672019343513"></a><a name="en-us_topic_0096561536_p672019343513"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.5.1.2 "><p id="p1234364311348"><a name="p1234364311348"></a><a name="p1234364311348"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096561536_p072013333518"><a name="en-us_topic_0096561536_p072013333518"></a><a name="en-us_topic_0096561536_p072013333518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096561536_p6720334350"><a name="en-us_topic_0096561536_p6720334350"></a><a name="en-us_topic_0096561536_p6720334350"></a>Specifies the load balancer ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0096561536_section1268101171716"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0096561536_table10681911171714"></a>
<table><thead align="left"><tr id="en-us_topic_0096561536_row969911191714"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="en-us_topic_0096561536_p12692116178"><a name="en-us_topic_0096561536_p12692116178"></a><a name="en-us_topic_0096561536_p12692116178"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="en-us_topic_0096561536_p116918114179"><a name="en-us_topic_0096561536_p116918114179"></a><a name="en-us_topic_0096561536_p116918114179"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p94903217354"><a name="p94903217354"></a><a name="p94903217354"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="en-us_topic_0096561536_p569111141717"><a name="en-us_topic_0096561536_p569111141717"></a><a name="en-us_topic_0096561536_p569111141717"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561536_row107017115174"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561536_p177061120174"><a name="en-us_topic_0096561536_p177061120174"></a><a name="en-us_topic_0096561536_p177061120174"></a>loadbalancer</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561536_p970131131711"><a name="en-us_topic_0096561536_p970131131711"></a><a name="en-us_topic_0096561536_p970131131711"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p124904218358"><a name="p124904218358"></a><a name="p124904218358"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096561536_p167017113179"><a name="en-us_topic_0096561536_p167017113179"></a><a name="en-us_topic_0096561536_p167017113179"></a>Specifies the load balancer. For details, see <a href="#en-us_topic_0096561536_table153641232163710">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **loadbalancer**  parameter description

<a name="en-us_topic_0096561536_table153641232163710"></a>
<table><thead align="left"><tr id="en-us_topic_0096561536_row5424532203711"><th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.1"><p id="en-us_topic_0096561536_p242443214376"><a name="en-us_topic_0096561536_p242443214376"></a><a name="en-us_topic_0096561536_p242443214376"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.2"><p id="en-us_topic_0096561536_p2042414329378"><a name="en-us_topic_0096561536_p2042414329378"></a><a name="en-us_topic_0096561536_p2042414329378"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="en-us_topic_0096561536_p74241732103713"><a name="en-us_topic_0096561536_p74241732103713"></a><a name="en-us_topic_0096561536_p74241732103713"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.58585858585859%" id="mcps1.2.5.1.4"><p id="en-us_topic_0096561536_p1742411321370"><a name="en-us_topic_0096561536_p1742411321370"></a><a name="en-us_topic_0096561536_p1742411321370"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561536_row1742413210379"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561536_p7424193253715"><a name="en-us_topic_0096561536_p7424193253715"></a><a name="en-us_topic_0096561536_p7424193253715"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561536_p242413213713"><a name="en-us_topic_0096561536_p242413213713"></a><a name="en-us_topic_0096561536_p242413213713"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p332771714378"><a name="p332771714378"></a><a name="p332771714378"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096561536_p10424103213375"><a name="en-us_topic_0096561536_p10424103213375"></a><a name="en-us_topic_0096561536_p10424103213375"></a>Specifies the load balancer name.</p>
<p id="p0553043304"><a name="p0553043304"></a><a name="p0553043304"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561536_row04244326371"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561536_p4424143215377"><a name="en-us_topic_0096561536_p4424143215377"></a><a name="en-us_topic_0096561536_p4424143215377"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561536_p842411321376"><a name="en-us_topic_0096561536_p842411321376"></a><a name="en-us_topic_0096561536_p842411321376"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p185060183372"><a name="p185060183372"></a><a name="p185060183372"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096561536_p1242418328373"><a name="en-us_topic_0096561536_p1242418328373"></a><a name="en-us_topic_0096561536_p1242418328373"></a>Provides supplementary information about the load balancer.</p>
<p id="p758520471103"><a name="p758520471103"></a><a name="p758520471103"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561536_row3424173223711"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561536_p5424123220379"><a name="en-us_topic_0096561536_p5424123220379"></a><a name="en-us_topic_0096561536_p5424123220379"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561536_p1542413212375"><a name="en-us_topic_0096561536_p1542413212375"></a><a name="en-us_topic_0096561536_p1542413212375"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p83151224113718"><a name="p83151224113718"></a><a name="p83151224113718"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p72201616133215"><a name="p72201616133215"></a><a name="p72201616133215"></a>Specifies the administrative status of the load balancer.</p>
<p id="p14892813103216"><a name="p14892813103216"></a><a name="p14892813103216"></a>This parameter is reserved. The default value is <strong id="b1115313544210"><a name="b1115313544210"></a><a name="b1115313544210"></a>true</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0096561536_section16203682429"></a>

**Table  4**  Response parameters

<a name="en-us_topic_0096561536_table8517103103818"></a>
<table><thead align="left"><tr id="en-us_topic_0096561536_row7554193143812"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561536_p1447519610387"><a name="en-us_topic_0096561536_p1447519610387"></a><a name="en-us_topic_0096561536_p1447519610387"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561536_p1355443153816"><a name="en-us_topic_0096561536_p1355443153816"></a><a name="en-us_topic_0096561536_p1355443153816"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.2.4.1.3"><p id="p740472617382"><a name="p740472617382"></a><a name="p740472617382"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561536_row35541332385"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561536_p1355420316382"><a name="en-us_topic_0096561536_p1355420316382"></a><a name="en-us_topic_0096561536_p1355420316382"></a>loadbalancer</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561536_p14554334389"><a name="en-us_topic_0096561536_p14554334389"></a><a name="en-us_topic_0096561536_p14554334389"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561536_p145541036382"><a name="en-us_topic_0096561536_p145541036382"></a><a name="en-us_topic_0096561536_p145541036382"></a>Specifies the load balancer. For details, see <a href="#en-us_topic_0096561536_table555616231383">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **loadbalancer**  parameter description

<a name="en-us_topic_0096561536_table555616231383"></a>
<table><thead align="left"><tr id="en-us_topic_0141008271_en-us_topic_0096561532_row6659133533816"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="en-us_topic_0141008271_en-us_topic_0096561532_p96591835173819"><a name="en-us_topic_0141008271_en-us_topic_0096561532_p96591835173819"></a><a name="en-us_topic_0141008271_en-us_topic_0096561532_p96591835173819"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="en-us_topic_0141008271_en-us_topic_0096561532_p17660123513386"><a name="en-us_topic_0141008271_en-us_topic_0096561532_p17660123513386"></a><a name="en-us_topic_0141008271_en-us_topic_0096561532_p17660123513386"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.2.4.1.3"><p id="en-us_topic_0141008271_en-us_topic_0096561532_p4660183515387"><a name="en-us_topic_0141008271_en-us_topic_0096561532_p4660183515387"></a><a name="en-us_topic_0141008271_en-us_topic_0096561532_p4660183515387"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0141008271_en-us_topic_0096561532_row156601235133818"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p10415829113311"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p10415829113311"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p10415829113311"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p155784252919"><a name="en-us_topic_0141008271_p155784252919"></a><a name="en-us_topic_0141008271_p155784252919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1941513297339"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1941513297339"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1941513297339"></a>Specifies the load balancer ID.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_row1758616126181"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p20415229113312"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p20415229113312"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p20415229113312"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p741592933318"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p741592933318"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p741592933318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1341519295331"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1341519295331"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1341519295331"></a>Specifies the ID of the project where the load balancer is used.</p>
<p id="en-us_topic_0141008271_p77281547155311"><a name="en-us_topic_0141008271_p77281547155311"></a><a name="en-us_topic_0141008271_p77281547155311"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row76601535193815"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1041552912332"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1041552912332"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1041552912332"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p241692918331"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p241692918331"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p241692918331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p17416152919332"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p17416152919332"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p17416152919332"></a>Specifies the load balancer name.</p>
<p id="en-us_topic_0141008271_p076212535532"><a name="en-us_topic_0141008271_p076212535532"></a><a name="en-us_topic_0141008271_p076212535532"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row66605355385"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p4416102918335"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p4416102918335"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p4416102918335"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p24161129143314"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p24161129143314"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p24161129143314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p5416142912334"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p5416142912334"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p5416142912334"></a>Provides supplementary information about the load balancer.</p>
<p id="en-us_topic_0141008271_p157105551532"><a name="en-us_topic_0141008271_p157105551532"></a><a name="en-us_topic_0141008271_p157105551532"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row1166020352385"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1541618299335"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1541618299335"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1541618299335"></a>vip_subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p135272044182910"><a name="en-us_topic_0141008271_p135272044182910"></a><a name="en-us_topic_0141008271_p135272044182910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_p4335125124117"><a name="en-us_topic_0141008271_p4335125124117"></a><a name="en-us_topic_0141008271_p4335125124117"></a>Specifies the ID of the subnet where the load balancer works.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row36601435103818"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1041622923320"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1041622923320"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1041622923320"></a>vip_port_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p19102164614291"><a name="en-us_topic_0141008271_p19102164614291"></a><a name="en-us_topic_0141008271_p19102164614291"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_p173334177415"><a name="en-us_topic_0141008271_p173334177415"></a><a name="en-us_topic_0141008271_p173334177415"></a>Specifies the ID of the port bound to the private IP address of the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row1866173519389"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p174164295334"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p174164295334"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p174164295334"></a>provider</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p541611290339"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p541611290339"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p541611290339"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_p43391417194120"><a name="en-us_topic_0141008271_p43391417194120"></a><a name="en-us_topic_0141008271_p43391417194120"></a>Specifies the provider of the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row6661203510387"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1416829143318"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1416829143318"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1416829143318"></a>vip_address</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p341672912338"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p341672912338"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p341672912338"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p64178297334"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p64178297334"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p64178297334"></a>Specifies the private IP address of the load balancer.</p>
<p id="en-us_topic_0141008271_p832917316544"><a name="en-us_topic_0141008271_p832917316544"></a><a name="en-us_topic_0141008271_p832917316544"></a>The value contains a maximum of 64 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row16611235163814"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1841715293336"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1841715293336"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1841715293336"></a>listeners</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p10662124818106"><a name="en-us_topic_0141008271_p10662124818106"></a><a name="en-us_topic_0141008271_p10662124818106"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p7417112963311"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p7417112963311"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p7417112963311"></a>Lists the IDs of listeners added to the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row8661143513384"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1441712910330"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1441712910330"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1441712910330"></a>pools</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p563318509102"><a name="en-us_topic_0141008271_p563318509102"></a><a name="en-us_topic_0141008271_p563318509102"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p104171229123313"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p104171229123313"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p104171229123313"></a>Lists the IDs of backend server groups associated with the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row566114352387"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_p727217358477"><a name="en-us_topic_0141008271_p727217358477"></a><a name="en-us_topic_0141008271_p727217358477"></a>operating_status</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p82761735124717"><a name="en-us_topic_0141008271_p82761735124717"></a><a name="en-us_topic_0141008271_p82761735124717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_p9800291619"><a name="en-us_topic_0141008271_p9800291619"></a><a name="en-us_topic_0141008271_p9800291619"></a>Specifies the operating status of the load balancer.</p>
<p id="en-us_topic_0141008271_p75131031164"><a name="en-us_topic_0141008271_p75131031164"></a><a name="en-us_topic_0141008271_p75131031164"></a>The value can be <strong id="en-us_topic_0141008271_b842352706165847"><a name="en-us_topic_0141008271_b842352706165847"></a><a name="en-us_topic_0141008271_b842352706165847"></a>ONLINE</strong>, <strong id="en-us_topic_0141008271_b842352706165850"><a name="en-us_topic_0141008271_b842352706165850"></a><a name="en-us_topic_0141008271_b842352706165850"></a>OFFLINE</strong>, <strong id="en-us_topic_0141008271_b842352706165852"><a name="en-us_topic_0141008271_b842352706165852"></a><a name="en-us_topic_0141008271_b842352706165852"></a>DEGRADED</strong>, <strong id="en-us_topic_0141008271_b842352706165855"><a name="en-us_topic_0141008271_b842352706165855"></a><a name="en-us_topic_0141008271_b842352706165855"></a>DISABLED</strong>, or <strong id="en-us_topic_0141008271_b842352706165859"><a name="en-us_topic_0141008271_b842352706165859"></a><a name="en-us_topic_0141008271_b842352706165859"></a>NO_MONITOR</strong>.</p>
<p id="en-us_topic_0141008271_p58611733561"><a name="en-us_topic_0141008271_p58611733561"></a><a name="en-us_topic_0141008271_p58611733561"></a>This parameter is reserved. The default value is <strong id="en-us_topic_0141008271_b842352706145855"><a name="en-us_topic_0141008271_b842352706145855"></a><a name="en-us_topic_0141008271_b842352706145855"></a>ONLINE</strong>.</p>
<p id="en-us_topic_0141008271_p71718156545"><a name="en-us_topic_0141008271_p71718156545"></a><a name="en-us_topic_0141008271_p71718156545"></a>The value contains a maximum of 16 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row2661123514384"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_p930113351475"><a name="en-us_topic_0141008271_p930113351475"></a><a name="en-us_topic_0141008271_p930113351475"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p7305153534717"><a name="en-us_topic_0141008271_p7305153534717"></a><a name="en-us_topic_0141008271_p7305153534717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_p4255836060"><a name="en-us_topic_0141008271_p4255836060"></a><a name="en-us_topic_0141008271_p4255836060"></a>Specifies the provisioning status of the load balancer.</p>
<p id="en-us_topic_0141008271_p9469138261"><a name="en-us_topic_0141008271_p9469138261"></a><a name="en-us_topic_0141008271_p9469138261"></a>The value can be <strong id="en-us_topic_0141008271_b842352706165943"><a name="en-us_topic_0141008271_b842352706165943"></a><a name="en-us_topic_0141008271_b842352706165943"></a>ACTIVE</strong>, <strong id="en-us_topic_0141008271_b842352706165947"><a name="en-us_topic_0141008271_b842352706165947"></a><a name="en-us_topic_0141008271_b842352706165947"></a>PENDING_CREATE</strong>, or <strong id="en-us_topic_0141008271_b842352706165951"><a name="en-us_topic_0141008271_b842352706165951"></a><a name="en-us_topic_0141008271_b842352706165951"></a>ERROR</strong>.</p>
<p id="en-us_topic_0141008271_p15614144018617"><a name="en-us_topic_0141008271_p15614144018617"></a><a name="en-us_topic_0141008271_p15614144018617"></a>This parameter is reserved. The default value is <strong id="en-us_topic_0141008271_b1402670288"><a name="en-us_topic_0141008271_b1402670288"></a><a name="en-us_topic_0141008271_b1402670288"></a>ACTIVE</strong>.</p>
<p id="en-us_topic_0141008271_p18722348205910"><a name="en-us_topic_0141008271_p18722348205910"></a><a name="en-us_topic_0141008271_p18722348205910"></a>The value contains a maximum of 16 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row16662935103816"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p114181329133314"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p114181329133314"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p114181329133314"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p10418172913319"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p10418172913319"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p10418172913319"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_p14847443611"><a name="en-us_topic_0141008271_p14847443611"></a><a name="en-us_topic_0141008271_p14847443611"></a>Specifies the administrative status of the load balancer.</p>
<p id="en-us_topic_0141008271_p114911046864"><a name="en-us_topic_0141008271_p114911046864"></a><a name="en-us_topic_0141008271_p114911046864"></a>This parameter is reserved. The default value is <strong id="en-us_topic_0141008271_b1291373994"><a name="en-us_topic_0141008271_b1291373994"></a><a name="en-us_topic_0141008271_b1291373994"></a>true</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row866215358384"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p74181229133310"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p74181229133310"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p74181229133310"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p71551954161018"><a name="en-us_topic_0141008271_p71551954161018"></a><a name="en-us_topic_0141008271_p71551954161018"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p4418112919333"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p4418112919333"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p4418112919333"></a>Lists load balancer tags.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row13900164817511"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p18781627124910"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p18781627124910"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p18781627124910"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p18781627204916"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p18781627204916"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p18781627204916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p578162719490"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p578162719490"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p578162719490"></a>Specifies the time when the load balancer was created.</p>
<p id="en-us_topic_0141008271_p3462240292"><a name="en-us_topic_0141008271_p3462240292"></a><a name="en-us_topic_0141008271_p3462240292"></a>The UTC time is in <em id="en-us_topic_0141008271_i155506367247"><a name="en-us_topic_0141008271_i155506367247"></a><a name="en-us_topic_0141008271_i155506367247"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
<p id="en-us_topic_0141008271_p415795413546"><a name="en-us_topic_0141008271_p415795413546"></a><a name="en-us_topic_0141008271_p415795413546"></a>The value contains a maximum of 19 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row4521952195114"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1541843114495"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1541843114495"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1541843114495"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1810172112506"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1810172112506"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1810172112506"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p341843144919"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p341843144919"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p341843144919"></a>Specifies the time when the load balancer was updated.</p>
<p id="en-us_topic_0141008271_p52901417154816"><a name="en-us_topic_0141008271_p52901417154816"></a><a name="en-us_topic_0141008271_p52901417154816"></a>The UTC time is in <em id="en-us_topic_0141008271_i185028407247"><a name="en-us_topic_0141008271_i185028407247"></a><a name="en-us_topic_0141008271_i185028407247"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
<p id="en-us_topic_0141008271_p3844185817544"><a name="en-us_topic_0141008271_p3844185817544"></a><a name="en-us_topic_0141008271_p3844185817544"></a>The value contains a maximum of 19 characters.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section10121011882"></a>

-   Example request: Modifying the load balancer name and description

    ```
    PUT https://{Endpoint}/v2.0/lbaas/loadbalancers/1e11b74e-30b7-4b78-b09b-84aec4a04487
    
    {
        "loadbalancer": {
            "name": "lb_update_test", 
            "description": "lb update test"
        }
    }
    ```


-   Example response

    ```
    {
      "loadbalancer": {
        "description": "simple lb2",
        "admin_state_up": true,
        "tenant_id": "145483a5107745e9b3d80f956713e6a3",
     
        "provisioning_status": "ACTIVE",
        "vip_subnet_id": "823d5866-6e30-45c2-9b1a-a1ebc3757fdb",
        "listeners": [
          {
            "id": "37ffe679-08ef-436e-b6bd-cf66fb4c3de2"
          }
        ],
        "vip_address": "192.172.1.68",
        "vip_port_id": "f42e3019-67f7-4d2a-8d1c-af49e7c22fa6",
        "tags": [],
        "provider": "vlb",
        "pools": [
          {
            "id": "75c4f2d4-a213-4408-9fa8-d64708e8d1df"
          }
        ],
        "id": "c32a9f9a-0cc6-4f38-bb9c-cde79a533c19",
        "operating_status": "ONLINE",
        "name": "loadbalancer-test2",
        "created_at": "2018-07-25T01:54:13", 
        "updated_at": "2018-07-25T01:54:14"
      }
    } 
    ```


## Status Code<a name="en-us_topic_0096561536_section64372710310"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

