# Updating a Virtual Interface<a name="en-dc_topic_0055025333"></a>

## Function<a name="section20784174143924"></a>

This API is used to update a virtual interface.

>![](/images/icon-note.gif) **NOTE:**   
>1.  You can only increase the bandwidth.  
>2.  Virtual interface bandwidths of hosted direct connections cannot be updated.  

## URI<a name="section11530146143924"></a>

PUT /v2.0/dcaas/virtual-interfaces/\{virtual\_interface\_id\}

**Table  1**  Parameter description

<a name="table1222245015813"></a>
<table><thead align="left"><tr id="row12230205015819"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p162305501281"><a name="p162305501281"></a><a name="p162305501281"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.2"><p id="p9230650285"><a name="p9230650285"></a><a name="p9230650285"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p19230450783"><a name="p19230450783"></a><a name="p19230450783"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="p152371550289"><a name="p152371550289"></a><a name="p152371550289"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row023735012814"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p2023716501788"><a name="p2023716501788"></a><a name="p2023716501788"></a>virtual_interface_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.2 "><p id="p123716501816"><a name="p123716501816"></a><a name="p123716501816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p4244175012817"><a name="p4244175012817"></a><a name="p4244175012817"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p1624475015815"><a name="p1624475015815"></a><a name="p1624475015815"></a>Specifies the virtual interface ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section17286486143924"></a>

[Table 2](#table10476506155243)  lists the request parameter.

**Table  2**  Request parameter

<a name="table10476506155243"></a>
<table><thead align="left"><tr id="row28606500155243"><th class="cellrowborder" valign="top" width="29.299999999999997%" id="mcps1.2.5.1.1"><p id="p28732152155335"><a name="p28732152155335"></a><a name="p28732152155335"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.060000000000002%" id="mcps1.2.5.1.2"><p id="p45602971155335"><a name="p45602971155335"></a><a name="p45602971155335"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.310000000000002%" id="mcps1.2.5.1.3"><p id="p2853179155335"><a name="p2853179155335"></a><a name="p2853179155335"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="31.330000000000002%" id="mcps1.2.5.1.4"><p id="p29780927155335"><a name="p29780927155335"></a><a name="p29780927155335"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17724599155243"><td class="cellrowborder" valign="top" width="29.299999999999997%" headers="mcps1.2.5.1.1 "><p id="p26406454155243"><a name="p26406454155243"></a><a name="p26406454155243"></a>virtual_interface</p>
</td>
<td class="cellrowborder" valign="top" width="21.060000000000002%" headers="mcps1.2.5.1.2 "><p id="p58548062155243"><a name="p58548062155243"></a><a name="p58548062155243"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="18.310000000000002%" headers="mcps1.2.5.1.3 "><p id="p44772566155243"><a name="p44772566155243"></a><a name="p44772566155243"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="31.330000000000002%" headers="mcps1.2.5.1.4 "><p id="p2699206155243"><a name="p2699206155243"></a><a name="p2699206155243"></a>Specifies the <strong id="b842352706194219"><a name="b842352706194219"></a><a name="b842352706194219"></a>virtual_interface</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **virtual\_interface**

<a name="table41417936143924"></a>
<table><thead align="left"><tr id="row60831409143924"><th class="cellrowborder" valign="top" width="29.590000000000003%" id="mcps1.1.5.1.1"><p id="p38838355143924"><a name="p38838355143924"></a><a name="p38838355143924"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.35%" id="mcps1.1.5.1.2"><p id="p63189637143924"><a name="p63189637143924"></a><a name="p63189637143924"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.09%" id="mcps1.1.5.1.3"><p id="p49522103143924"><a name="p49522103143924"></a><a name="p49522103143924"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="30.970000000000002%" id="mcps1.1.5.1.4"><p id="p21616645143924"><a name="p21616645143924"></a><a name="p21616645143924"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18728126143924"><td class="cellrowborder" valign="top" width="29.590000000000003%" headers="mcps1.1.5.1.1 "><p id="p7948256143924"><a name="p7948256143924"></a><a name="p7948256143924"></a>virtual_interface_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.35%" headers="mcps1.1.5.1.2 "><p id="p56200600143924"><a name="p56200600143924"></a><a name="p56200600143924"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.1.5.1.3 "><p id="p56692166143924"><a name="p56692166143924"></a><a name="p56692166143924"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.970000000000002%" headers="mcps1.1.5.1.4 "><p id="p45478774143924"><a name="p45478774143924"></a><a name="p45478774143924"></a>Specifies the virtual interface ID.</p>
</td>
</tr>
<tr id="row22103264145316"><td class="cellrowborder" valign="top" width="29.590000000000003%" headers="mcps1.1.5.1.1 "><p id="p949640145316"><a name="p949640145316"></a><a name="p949640145316"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="20.35%" headers="mcps1.1.5.1.2 "><p id="p9812033145316"><a name="p9812033145316"></a><a name="p9812033145316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.1.5.1.3 "><p id="p56577178145316"><a name="p56577178145316"></a><a name="p56577178145316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="30.970000000000002%" headers="mcps1.1.5.1.4 "><p id="p19348667145316"><a name="p19348667145316"></a><a name="p19348667145316"></a>Provides supplementary information about the virtual interface.</p>
</td>
</tr>
<tr id="row62108241145316"><td class="cellrowborder" valign="top" width="29.590000000000003%" headers="mcps1.1.5.1.1 "><p id="p12317111145316"><a name="p12317111145316"></a><a name="p12317111145316"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20.35%" headers="mcps1.1.5.1.2 "><p id="p58161973145316"><a name="p58161973145316"></a><a name="p58161973145316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.1.5.1.3 "><p id="p13499383145316"><a name="p13499383145316"></a><a name="p13499383145316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="30.970000000000002%" headers="mcps1.1.5.1.4 "><p id="p19708262145316"><a name="p19708262145316"></a><a name="p19708262145316"></a>Specifies the virtual interface name.</p>
</td>
</tr>
<tr id="row25467370204329"><td class="cellrowborder" valign="top" width="29.590000000000003%" headers="mcps1.1.5.1.1 "><p id="p9417538204337"><a name="p9417538204337"></a><a name="p9417538204337"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="20.35%" headers="mcps1.1.5.1.2 "><p id="p24623126204337"><a name="p24623126204337"></a><a name="p24623126204337"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.1.5.1.3 "><p id="p48316153204337"><a name="p48316153204337"></a><a name="p48316153204337"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="30.970000000000002%" headers="mcps1.1.5.1.4 "><p id="p21294358204337"><a name="p21294358204337"></a><a name="p21294358204337"></a>Specifies the virtual interface bandwidth.</p>
</td>
</tr>
<tr id="row15734375145352"><td class="cellrowborder" valign="top" width="29.590000000000003%" headers="mcps1.1.5.1.1 "><p id="p5702622145352"><a name="p5702622145352"></a><a name="p5702622145352"></a>remote_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.35%" headers="mcps1.1.5.1.2 "><p id="p59259247145352"><a name="p59259247145352"></a><a name="p59259247145352"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.1.5.1.3 "><p id="p35269704145352"><a name="p35269704145352"></a><a name="p35269704145352"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="30.970000000000002%" headers="mcps1.1.5.1.4 "><p id="p38273810145352"><a name="p38273810145352"></a><a name="p38273810145352"></a>Specifies the ID of the remote endpoint group that records the tenant CIDRs.</p>
</td>
</tr>
<tr id="row53944047145352"><td class="cellrowborder" valign="top" width="29.590000000000003%" headers="mcps1.1.5.1.1 "><p id="p51429535145352"><a name="p51429535145352"></a><a name="p51429535145352"></a>service_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.35%" headers="mcps1.1.5.1.2 "><p id="p5042777145352"><a name="p5042777145352"></a><a name="p5042777145352"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.1.5.1.3 "><p id="p5811775145352"><a name="p5811775145352"></a><a name="p5811775145352"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="30.970000000000002%" headers="mcps1.1.5.1.4 "><p id="p991803145352"><a name="p991803145352"></a><a name="p991803145352"></a>Specifies the ID of the service endpoint group that records the public service CIDRs.</p>
</td>
</tr>
<tr id="row27476943164116"><td class="cellrowborder" valign="top" width="29.590000000000003%" headers="mcps1.1.5.1.1 "><p id="p45959087164119"><a name="p45959087164119"></a><a name="p45959087164119"></a>rate_limit</p>
</td>
<td class="cellrowborder" valign="top" width="20.35%" headers="mcps1.1.5.1.2 "><p id="p31698555164119"><a name="p31698555164119"></a><a name="p31698555164119"></a>Boalean</p>
</td>
<td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.1.5.1.3 "><p id="p17446123164119"><a name="p17446123164119"></a><a name="p17446123164119"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="30.970000000000002%" headers="mcps1.1.5.1.4 "><p id="p3849831164119"><a name="p3849831164119"></a><a name="p3849831164119"></a>Specifies whether to limit the traffic rate. The value can be <strong id="b15280145145111"><a name="b15280145145111"></a><a name="b15280145145111"></a>true</strong> or <strong id="b11281185118517"><a name="b11281185118517"></a><a name="b11281185118517"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section33278910143924"></a>

[Table 3](#table2216502815556)  lists the response parameter.

**Table  3**  Response parameter

<a name="table2216502815556"></a>
<table><thead align="left"><tr id="row2118154015556"><th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.1"><p id="p3798321415556"><a name="p3798321415556"></a><a name="p3798321415556"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p5674152115556"><a name="p5674152115556"></a><a name="p5674152115556"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.4.1.3"><p id="p2825222315556"><a name="p2825222315556"></a><a name="p2825222315556"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row672873115556"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.1 "><p id="p815633515556"><a name="p815633515556"></a><a name="p815633515556"></a>virtual_interface</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p5668342815556"><a name="p5668342815556"></a><a name="p5668342815556"></a>Dictionary data structure</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p4976072015556"><a name="p4976072015556"></a><a name="p4976072015556"></a>Specifies the <strong id="b842352706194240"><a name="b842352706194240"></a><a name="b842352706194240"></a>virtual_interface</strong> object.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **virtual\_interface**

<a name="table12493326143924"></a>
<table><thead align="left"><tr id="row6524313143924"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.4.1.1"><p id="p58396671143924"><a name="p58396671143924"></a><a name="p58396671143924"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.2"><p id="p7441546143924"><a name="p7441546143924"></a><a name="p7441546143924"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.1.4.1.3"><p id="p55439607143924"><a name="p55439607143924"></a><a name="p55439607143924"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row40598305145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p46868244145335"><a name="p46868244145335"></a><a name="p46868244145335"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p38231421145335"><a name="p38231421145335"></a><a name="p38231421145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p50534474145335"><a name="p50534474145335"></a><a name="p50534474145335"></a>Specifies the virtual interface ID.</p>
</td>
</tr>
<tr id="row41793625145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p63974246145335"><a name="p63974246145335"></a><a name="p63974246145335"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p14531420145335"><a name="p14531420145335"></a><a name="p14531420145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p46065903145335"><a name="p46065903145335"></a><a name="p46065903145335"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row64296059145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p27611835145335"><a name="p27611835145335"></a><a name="p27611835145335"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p21966137145335"><a name="p21966137145335"></a><a name="p21966137145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p37094374145335"><a name="p37094374145335"></a><a name="p37094374145335"></a>Specifies the virtual interface name.</p>
</td>
</tr>
<tr id="row36970168145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p64035604145335"><a name="p64035604145335"></a><a name="p64035604145335"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p19501411145335"><a name="p19501411145335"></a><a name="p19501411145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p39265055145335"><a name="p39265055145335"></a><a name="p39265055145335"></a>Provides supplementary information about the virtual interface.</p>
</td>
</tr>
<tr id="row33933958145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p35849146145335"><a name="p35849146145335"></a><a name="p35849146145335"></a>direct_connect_id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p18099700145335"><a name="p18099700145335"></a><a name="p18099700145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p36556115145335"><a name="p36556115145335"></a><a name="p36556115145335"></a>Specifies the connection ID.</p>
</td>
</tr>
<tr id="row11226980145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p7188862145335"><a name="p7188862145335"></a><a name="p7188862145335"></a>vgw_ id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p45426958145335"><a name="p45426958145335"></a><a name="p45426958145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p15808067145335"><a name="p15808067145335"></a><a name="p15808067145335"></a>Specifies the virtual gateway ID.</p>
</td>
</tr>
<tr id="row53443225145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p48465145145335"><a name="p48465145145335"></a><a name="p48465145145335"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p33362712145335"><a name="p33362712145335"></a><a name="p33362712145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p50753784145335"><a name="p50753784145335"></a><a name="p50753784145335"></a>Specifies the interface type. The value can be <strong id="b842352706142157"><a name="b842352706142157"></a><a name="b842352706142157"></a>public</strong> or <strong id="b84235270614220"><a name="b84235270614220"></a><a name="b84235270614220"></a>private</strong>.</p>
</td>
</tr>
<tr id="row13394676145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p22524621145335"><a name="p22524621145335"></a><a name="p22524621145335"></a>service_type</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p12555013145335"><a name="p12555013145335"></a><a name="p12555013145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p30868483145335"><a name="p30868483145335"></a><a name="p30868483145335"></a>Specifies the access service type. The value can be <strong id="b1650500527142036"><a name="b1650500527142036"></a><a name="b1650500527142036"></a>vpc</strong>, <strong id="b26378606142036"><a name="b26378606142036"></a><a name="b26378606142036"></a>public service</strong>, or <strong id="b1032837367142036"><a name="b1032837367142036"></a><a name="b1032837367142036"></a>vpc and public service</strong>.</p>
</td>
</tr>
<tr id="row61140620145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p21655010145335"><a name="p21655010145335"></a><a name="p21655010145335"></a>vlan</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p15690831212825"><a name="p15690831212825"></a><a name="p15690831212825"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p62484413145335"><a name="p62484413145335"></a><a name="p62484413145335"></a>Specifies the VLAN used by the local gateway to communicate with the remote gateway.</p>
</td>
</tr>
<tr id="row58989185145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p51327912145335"><a name="p51327912145335"></a><a name="p51327912145335"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p5156695419451"><a name="p5156695419451"></a><a name="p5156695419451"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p17413768145335"><a name="p17413768145335"></a><a name="p17413768145335"></a>Specifies the virtual interface bandwidth.</p>
</td>
</tr>
<tr id="row58750137145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p11061850145335"><a name="p11061850145335"></a><a name="p11061850145335"></a>local_gateway_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p23594682145335"><a name="p23594682145335"></a><a name="p23594682145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p51672844145335"><a name="p51672844145335"></a><a name="p51672844145335"></a>Specifies the IPv4 address of the local gateway.</p>
</td>
</tr>
<tr id="row36353954145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p21430584145335"><a name="p21430584145335"></a><a name="p21430584145335"></a>remote_gateway_v4_ip</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p58155769145335"><a name="p58155769145335"></a><a name="p58155769145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p46114937145335"><a name="p46114937145335"></a><a name="p46114937145335"></a>Specifies the IPv4 address of the remote gateway.</p>
</td>
</tr>
<tr id="row26408949145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p63357643145335"><a name="p63357643145335"></a><a name="p63357643145335"></a>route_mode</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p31695496145335"><a name="p31695496145335"></a><a name="p31695496145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p50890954145335"><a name="p50890954145335"></a><a name="p50890954145335"></a>Specifies the routing mode. The value can be <strong id="b84235270614653"><a name="b84235270614653"></a><a name="b84235270614653"></a>static</strong> or <strong id="b84235270614655"><a name="b84235270614655"></a><a name="b84235270614655"></a>bgp</strong>.</p>
</td>
</tr>
<tr id="row17847408145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p55413029145335"><a name="p55413029145335"></a><a name="p55413029145335"></a>bgp_asn</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p59270342145335"><a name="p59270342145335"></a><a name="p59270342145335"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p43961599145335"><a name="p43961599145335"></a><a name="p43961599145335"></a>Specifies the AS number of the BGP peer.</p>
</td>
</tr>
<tr id="row24352666145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p37078045145335"><a name="p37078045145335"></a><a name="p37078045145335"></a>bgp_md5</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p50531678145335"><a name="p50531678145335"></a><a name="p50531678145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p20554593145335"><a name="p20554593145335"></a><a name="p20554593145335"></a>Specifies the MD5 password of the BGP peer.</p>
</td>
</tr>
<tr id="row54901634145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p19022230145335"><a name="p19022230145335"></a><a name="p19022230145335"></a>remote_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p64405632145335"><a name="p64405632145335"></a><a name="p64405632145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p47945666145335"><a name="p47945666145335"></a><a name="p47945666145335"></a>Specifies the ID of the remote endpoint group that records the tenant CIDRs.</p>
</td>
</tr>
<tr id="row50839424145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p55781303145335"><a name="p55781303145335"></a><a name="p55781303145335"></a>service_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p21991717145335"><a name="p21991717145335"></a><a name="p21991717145335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p3598777145335"><a name="p3598777145335"></a><a name="p3598777145335"></a>Specifies the ID of the service endpoint group that records the public service CIDRs.</p>
</td>
</tr>
<tr id="row41472724161653"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p14881030161656"><a name="p14881030161656"></a><a name="p14881030161656"></a>create_time</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p52974842161656"><a name="p52974842161656"></a><a name="p52974842161656"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p47576540161656"><a name="p47576540161656"></a><a name="p47576540161656"></a>Specifies the time when the virtual interface is created.</p>
</td>
</tr>
<tr id="row27939490171634"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p50962070171640"><a name="p50962070171640"></a><a name="p50962070171640"></a>delete_time</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p34287015171640"><a name="p34287015171640"></a><a name="p34287015171640"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p8196682171640"><a name="p8196682171640"></a><a name="p8196682171640"></a>Specifies the time when the virtual interface is deleted.</p>
</td>
</tr>
<tr id="row4406922419459"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p632259461952"><a name="p632259461952"></a><a name="p632259461952"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p210279641952"><a name="p210279641952"></a><a name="p210279641952"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p1999411815217"><a name="p1999411815217"></a><a name="p1999411815217"></a>Specifies the virtual interface status.</p>
<p id="p557608071952"><a name="p557608071952"></a><a name="p557608071952"></a>The value can be <strong id="b84235270617169"><a name="b84235270617169"></a><a name="b84235270617169"></a>ACTIVE</strong>, <strong id="b842352706171613"><a name="b842352706171613"></a><a name="b842352706171613"></a>DOWN</strong>, <strong id="b842352706171618"><a name="b842352706171618"></a><a name="b842352706171618"></a>BUILD</strong>, <strong id="b842352706171622"><a name="b842352706171622"></a><a name="b842352706171622"></a>ERROR</strong>, <strong id="b842352706171626"><a name="b842352706171626"></a><a name="b842352706171626"></a>PENDING_CREATE</strong>, <strong id="b842352706171630"><a name="b842352706171630"></a><a name="b842352706171630"></a>PENDING_UPDATE</strong>, <strong id="b842352706171633"><a name="b842352706171633"></a><a name="b842352706171633"></a>PENDING_DELETE</strong>, <strong id="b255042327233226"><a name="b255042327233226"></a><a name="b255042327233226"></a>DELETED</strong>, <strong id="b901715572233226"><a name="b901715572233226"></a><a name="b901715572233226"></a>AUTHORIZATION</strong>, or <strong id="b1624075844233226"><a name="b1624075844233226"></a><a name="b1624075844233226"></a>REJECTED</strong>.</p>
</td>
</tr>
<tr id="row20561905145335"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p6263091145335"><a name="p6263091145335"></a><a name="p6263091145335"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p37548366145335"><a name="p37548366145335"></a><a name="p37548366145335"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p2320543515223"><a name="p2320543515223"></a><a name="p2320543515223"></a>Specifies the administrative state of the virtual interface.</p>
<p id="p65299689145335"><a name="p65299689145335"></a><a name="p65299689145335"></a>The value can be <strong id="b842352706154840"><a name="b842352706154840"></a><a name="b842352706154840"></a>true</strong> or <strong id="b842352706154844"><a name="b842352706154844"></a><a name="b842352706154844"></a>false</strong>.</p>
</td>
</tr>
<tr id="row13946133405114"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p6570194316514"><a name="p6570194316514"></a><a name="p6570194316514"></a>rate_limit</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.2 "><p id="p1357015439512"><a name="p1357015439512"></a><a name="p1357015439512"></a>Boalean</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.4.1.3 "><p id="p15708434514"><a name="p15708434514"></a><a name="p15708434514"></a>Specifies whether to limit the traffic rate. The value can be <strong id="b15457452105112"><a name="b15457452105112"></a><a name="b15457452105112"></a>true</strong> or <strong id="b04572052185115"><a name="b04572052185115"></a><a name="b04572052185115"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section9931099143924"></a>

-   Example request

    ```
    PUT /v2.0/dcaas/virtual-interfaces/{virtual_interface_id}
    {
        "virtual_interface" : {
            "name" : "virtual interface1",
            "description" : "New description"
        }
    }
    ```


-   Example response

    ```
    {       
        "virtual_interface" : {
            "id" : "67c59cf4-1a64-46c7-763f-22eb1b9e8986",  
            "tenant_id" : "6fbe9263116a4b68818cf1edce16bc4f",
            "name" : "virtual interface1",
            "description" : "New description",
            "direct_connect_id" : "6ecd9cf3-ca64-46c7-863f-f2eb1b9e838a",
            "vgw_id" : "7ec892f3-ca64-46c7-863f-a2eb1b9e8389",
            "type" : "private",
            "service_type" : "vpc",
            "vlan" : 100,
            "bandwidth" : 10,
            "local_gateway_v4_ip" : "180.1.1.1/24",
            "remote_gateway_v4_ip"  : "180.1.1.2/24",
            "route_mode"  : "static",
            "remote_ep_group_id" : "78e34cf1-5468-87c7-223d-56e78b9699ef"
        }
    }
    ```


## Returned Value<a name="section38874431173428"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

