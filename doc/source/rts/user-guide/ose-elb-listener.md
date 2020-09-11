# OSE::ELB::Listener<a name="EN-US_TOPIC_0088407146"></a>

A resource for ELB Listener.

## Required Properties<a name="section191915578476"></a>

<a name="table273094654810"></a>
<table><thead align="left"><tr id="row094254114525"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p127317468488"><a name="p127317468488"></a><a name="p127317468488"></a><strong id="b1728225205119"><a name="b1728225205119"></a><a name="b1728225205119"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p673134674818"><a name="p673134674818"></a><a name="p673134674818"></a><strong id="b102831510516"><a name="b102831510516"></a><a name="b102831510516"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10942941195214"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p157314465481"><a name="p157314465481"></a><a name="p157314465481"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p2114936"><a name="p2114936"></a><a name="p2114936"></a>The name of the listener.</p>
<p id="p19034430"><a name="p19034430"></a><a name="p19034430"></a>String value expected.</p>
<p id="p37092147"><a name="p37092147"></a><a name="p37092147"></a>Can be updated without replacement.</p>
<p id="p65393872"><a name="p65393872"></a><a name="p65393872"></a>It is allowed to start with <strong id="b616424474219"><a name="b616424474219"></a><a name="b616424474219"></a>numbers</strong>, <strong id="b10165164464218"><a name="b10165164464218"></a><a name="b10165164464218"></a>letters</strong>, _, and <strong id="b10166174444216"><a name="b10166174444216"></a><a name="b10166174444216"></a>-</strong> characters. It is allowed to include <strong id="b171661144114212"><a name="b171661144114212"></a><a name="b171661144114212"></a>numbers</strong>, <strong id="b11167134474213"><a name="b11167134474213"></a><a name="b11167134474213"></a>letters</strong>, _, and <strong id="b181676449424"><a name="b181676449424"></a><a name="b181676449424"></a>-</strong> characters, and the string length is <strong id="b131671744204214"><a name="b131671744204214"></a><a name="b131671744204214"></a>1</strong> to <strong id="b20417152194515"><a name="b20417152194515"></a><a name="b20417152194515"></a>64</strong>.</p>
</td>
</tr>
<tr id="row109423415528"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p87311946114820"><a name="p87311946114820"></a><a name="p87311946114820"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p62412303"><a name="p62412303"></a><a name="p62412303"></a>The ID of load balancer associated.</p>
<p id="p24839818"><a name="p24839818"></a><a name="p24839818"></a>String value expected.</p>
<p id="p22231778"><a name="p22231778"></a><a name="p22231778"></a>Updates cause replacement.</p>
<p id="p65868279"><a name="p65868279"></a><a name="p65868279"></a>Value must be of type elb.lb</p>
</td>
</tr>
<tr id="row12942124111525"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p4732946194811"><a name="p4732946194811"></a><a name="p4732946194811"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p47805593"><a name="p47805593"></a><a name="p47805593"></a>The protocol of the listener.</p>
<p id="p27597159"><a name="p27597159"></a><a name="p27597159"></a>String value expected.</p>
<p id="p47047839"><a name="p47047839"></a><a name="p47047839"></a>Updates cause replacement.</p>
<p id="p20777372"><a name="p20777372"></a><a name="p20777372"></a>Allowed values: HTTP, HTTPS, TCP</p>
<div class="note" id="note67662611019"><a name="note67662611019"></a><a name="note67662611019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p35137894"><a name="p35137894"></a><a name="p35137894"></a>Do not update this attribute. Otherwise, the listener update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row1194315417523"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1673274694811"><a name="p1673274694811"></a><a name="p1673274694811"></a>backend_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p22236356"><a name="p22236356"></a><a name="p22236356"></a>The backend protocol of the listener.</p>
<p id="p65909476"><a name="p65909476"></a><a name="p65909476"></a>String value expected.</p>
<p id="p56314374"><a name="p56314374"></a><a name="p56314374"></a>Updates cause replacement.</p>
<p id="p37067324"><a name="p37067324"></a><a name="p37067324"></a>Allowed values: HTTP, TCP</p>
<div class="note" id="note6681114304"><a name="note6681114304"></a><a name="note6681114304"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p47209948"><a name="p47209948"></a><a name="p47209948"></a>Do not update this attribute. Otherwise, the listener update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row3943204114529"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1073284610481"><a name="p1073284610481"></a><a name="p1073284610481"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p49663244"><a name="p49663244"></a><a name="p49663244"></a>The port of the listener.</p>
<p id="p44316017"><a name="p44316017"></a><a name="p44316017"></a>Integer value expected.</p>
<p id="p63299837"><a name="p63299837"></a><a name="p63299837"></a>Can be updated without replacement.</p>
<p id="p32827625"><a name="p32827625"></a><a name="p32827625"></a>Allowed values: from 1 to 65535, include 1 and 65535</p>
</td>
</tr>
<tr id="row18943641155220"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p473214466487"><a name="p473214466487"></a><a name="p473214466487"></a>backend_port</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p41791982"><a name="p41791982"></a><a name="p41791982"></a>The backend port of the listener.</p>
<p id="p40583520"><a name="p40583520"></a><a name="p40583520"></a>Integer value expected.</p>
<p id="p29707367"><a name="p29707367"></a><a name="p29707367"></a>Can be updated without replacement.</p>
<p id="p66039715"><a name="p66039715"></a><a name="p66039715"></a>Allowed values: from 1 to 65535, include 1 and 65535</p>
</td>
</tr>
<tr id="row1694315417529"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p16732144664810"><a name="p16732144664810"></a><a name="p16732144664810"></a>lb_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p47616678"><a name="p47616678"></a><a name="p47616678"></a>The algorithm used to distribute load.</p>
<p id="p25896919"><a name="p25896919"></a><a name="p25896919"></a>String value expected.</p>
<p id="p31745681"><a name="p31745681"></a><a name="p31745681"></a>Can be updated without replacement.</p>
<p id="p17275677"><a name="p17275677"></a><a name="p17275677"></a>Allowed values: roundrobin, leastconn, source</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section59499511488"></a>

<a name="table17716193335119"></a>
<table><thead align="left"><tr id="row1999638135711"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p671620334516"><a name="p671620334516"></a><a name="p671620334516"></a><strong id="b87320214577"><a name="b87320214577"></a><a name="b87320214577"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p12716123318515"><a name="p12716123318515"></a><a name="p12716123318515"></a><strong id="b1573417215579"><a name="b1573417215579"></a><a name="b1573417215579"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row8996118195716"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p14716103312511"><a name="p14716103312511"></a><a name="p14716103312511"></a>certificate_id</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p35007262"><a name="p35007262"></a><a name="p35007262"></a>The ID of certificate.</p>
<p id="p46629906"><a name="p46629906"></a><a name="p46629906"></a>String value expected.</p>
<p id="p17015974"><a name="p17015974"></a><a name="p17015974"></a>Updates cause replacement.</p>
<div class="note" id="note118582515015"><a name="note118582515015"></a><a name="note118582515015"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p33715857"><a name="p33715857"></a><a name="p33715857"></a>Do not update this attribute. Otherwise, the listener update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row599619818570"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1771673385114"><a name="p1771673385114"></a><a name="p1771673385114"></a>cookie_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p39768900"><a name="p39768900"></a><a name="p39768900"></a>The timeout of cookie in minute.</p>
<p id="p22375784"><a name="p22375784"></a><a name="p22375784"></a>Integer value expected.</p>
<p id="p55466"><a name="p55466"></a><a name="p55466"></a>Updates cause replacement.</p>
<p id="p499195"><a name="p499195"></a><a name="p499195"></a>Allowed values: from 1 to 1440, include 1 and 1440</p>
<div class="note" id="note1011018311706"><a name="note1011018311706"></a><a name="note1011018311706"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p56614549"><a name="p56614549"></a><a name="p56614549"></a>Do not update this attribute. Otherwise, the listener update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row1599688195710"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p871619330513"><a name="p871619330513"></a><a name="p871619330513"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p40434806"><a name="p40434806"></a><a name="p40434806"></a>The description of the listener.</p>
<p id="p28368938"><a name="p28368938"></a><a name="p28368938"></a>String value expected.</p>
<p id="p53993858"><a name="p53993858"></a><a name="p53993858"></a>Can be updated without replacement.</p>
<p id="p16182678"><a name="p16182678"></a><a name="p16182678"></a>It is not allowed to start with the <strong id="b10442124413476"><a name="b10442124413476"></a><a name="b10442124413476"></a>&lt;&gt;</strong> character. The <strong id="b5192154910474"><a name="b5192154910474"></a><a name="b5192154910474"></a>&lt;&gt;</strong> character is not allowed and the string length is <strong id="b1619910586488"><a name="b1619910586488"></a><a name="b1619910586488"></a>1</strong> to <strong id="b46589194910"><a name="b46589194910"></a><a name="b46589194910"></a>128</strong>.</p>
</td>
</tr>
<tr id="row119962815572"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1671643375113"><a name="p1671643375113"></a><a name="p1671643375113"></a>session_sticky</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p8328137"><a name="p8328137"></a><a name="p8328137"></a>Whether to keep the session.</p>
<p id="p7844377"><a name="p7844377"></a><a name="p7844377"></a>Boolean value expected.</p>
<p id="p3490530"><a name="p3490530"></a><a name="p3490530"></a>Updates cause replacement.</p>
<div class="note" id="note1558504112010"><a name="note1558504112010"></a><a name="note1558504112010"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p53121131"><a name="p53121131"></a><a name="p53121131"></a>Do not update this attribute. Otherwise, the listener update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row13996183572"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p771611338517"><a name="p771611338517"></a><a name="p771611338517"></a>sticky_session_type</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p17248409"><a name="p17248409"></a><a name="p17248409"></a>The way of handing cookie.</p>
<p id="p21017956"><a name="p21017956"></a><a name="p21017956"></a>String value expected.</p>
<p id="p54943879"><a name="p54943879"></a><a name="p54943879"></a>Updates cause replacement.</p>
<p id="p24732867"><a name="p24732867"></a><a name="p24732867"></a>Allowed values: insert</p>
<div class="note" id="note827310477016"><a name="note827310477016"></a><a name="note827310477016"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p61568813"><a name="p61568813"></a><a name="p61568813"></a>Do not update this attribute. Otherwise, the listener update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row109961819579"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p571615335510"><a name="p571615335510"></a><a name="p571615335510"></a>tcp_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p3112476"><a name="p3112476"></a><a name="p3112476"></a>The timeout of TCP session in minute.</p>
<p id="p28012285"><a name="p28012285"></a><a name="p28012285"></a>Integer value expected.</p>
<p id="p50783973"><a name="p50783973"></a><a name="p50783973"></a>Updates cause replacement.</p>
<p id="p54402573"><a name="p54402573"></a><a name="p54402573"></a>Allowed values: from 1 to 5, include 1 and 5. The default value is <strong id="b1415154513755"><a name="b1415154513755"></a><a name="b1415154513755"></a>5</strong>.</p>
<div class="note" id="note690535618019"><a name="note690535618019"></a><a name="note690535618019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p45085073"><a name="p45085073"></a><a name="p45085073"></a>Do not update this attribute. Otherwise, the listener update will fail.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section1178017165486"></a>

<a name="table189121339115412"></a>
<table><thead align="left"><tr id="row18540371212"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p4912639185418"><a name="p4912639185418"></a><a name="p4912639185418"></a><strong id="b15421252715"><a name="b15421252715"></a><a name="b15421252715"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p149121339125410"><a name="p149121339125410"></a><a name="p149121339125410"></a><strong id="b135430525116"><a name="b135430525116"></a><a name="b135430525116"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row285413371911"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p9912939195412"><a name="p9912939195412"></a><a name="p9912939195412"></a>member_number</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p89128398541"><a name="p89128398541"></a><a name="p89128398541"></a>The number of the members listened by this listener.</p>
</td>
</tr>
<tr id="row12854103716118"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1691315394544"><a name="p1691315394544"></a><a name="p1691315394544"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p17913133995414"><a name="p17913133995414"></a><a name="p17913133995414"></a>The status of the listener.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section779242654812"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OSE::ELB::Listener
    properties:
      backend_port: Integer
      backend_protocol: Integer
      certificate_id: String
      cookie_timeout: Integer
      description: String
      lb_algorithm: String
      loadbalancer_id: String
      name: String
      port: Integer
      protocol: String
      session_sticky: Boolean
      sticky_session_type
      tcp_timeout: Integer
```

