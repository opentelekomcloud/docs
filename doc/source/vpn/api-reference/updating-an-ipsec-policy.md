# Updating an IPsec Policy<a name="en_topic_0093011507"></a>

## **Function**<a name="section45521706"></a>

This interface is used to update an IPsec policy.

>![](/images/icon-note.gif) **NOTE:**   
>If the IPsec policy is updated, the IPsec VPN connection also needs to be updated.  

## URI<a name="section7042173"></a>

PUT /v2.0/vpn/ipsecpolicies/\{ipsecpolicy\_id\}

**Table  1**  Parameter description

<a name="table44973181017"></a>
<table><thead align="left"><tr id="row15504918204"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p1550413181805"><a name="p1550413181805"></a><a name="p1550413181805"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p135113181904"><a name="p135113181904"></a><a name="p135113181904"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p45111018804"><a name="p45111018804"></a><a name="p45111018804"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p125111818109"><a name="p125111818109"></a><a name="p125111818109"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1151910188014"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p11519418808"><a name="p11519418808"></a><a name="p11519418808"></a>ipsecpolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p051911182003"><a name="p051911182003"></a><a name="p051911182003"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p125198181109"><a name="p125198181109"></a><a name="p125198181109"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1651921810014"><a name="p1651921810014"></a><a name="p1651921810014"></a>Specifies the IPsec policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section33545144"></a>

[Table 2](#table17322790)  describes the request parameters.

**Table  2**  Request parameters

<a name="table17322790"></a>
<table><thead align="left"><tr id="row19920592"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p2955276"><a name="p2955276"></a><a name="p2955276"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p38050837"><a name="p38050837"></a><a name="p38050837"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p62218962"><a name="p62218962"></a><a name="p62218962"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p6571180"><a name="p6571180"></a><a name="p6571180"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row55864401"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p28722627"><a name="p28722627"></a><a name="p28722627"></a>ipsecpolicy</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p44831437"><a name="p44831437"></a><a name="p44831437"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p7467800"><a name="p7467800"></a><a name="p7467800"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p912076"><a name="p912076"></a><a name="p912076"></a>Specifies the IPsec policy object.</p>
</td>
</tr>
<tr id="row8208684"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p60923663"><a name="p60923663"></a><a name="p60923663"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p35869679"><a name="p35869679"></a><a name="p35869679"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p19762867"><a name="p19762867"></a><a name="p19762867"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p57288388"><a name="p57288388"></a><a name="p57288388"></a>Provides supplementary information about the IPsec policy.</p>
</td>
</tr>
<tr id="row45833444"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p21521490"><a name="p21521490"></a><a name="p21521490"></a>transform_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p65519169"><a name="p65519169"></a><a name="p65519169"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p5452505"><a name="p5452505"></a><a name="p5452505"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p38999745"><a name="p38999745"></a><a name="p38999745"></a>Specifies the transform protocol used. The value can be <strong id="b842352706184452"><a name="b842352706184452"></a><a name="b842352706184452"></a>esp</strong>, <strong id="b842352706184456"><a name="b842352706184456"></a><a name="b842352706184456"></a>ah</strong>, or <strong id="b84235270618456"><a name="b84235270618456"></a><a name="b84235270618456"></a>ah-esp</strong>. The default value is <strong id="b842352706201018"><a name="b842352706201018"></a><a name="b842352706201018"></a>esp</strong>.</p>
</td>
</tr>
<tr id="row15453386"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p43764782"><a name="p43764782"></a><a name="p43764782"></a>auth_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p55286454"><a name="p55286454"></a><a name="p55286454"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p49017803"><a name="p49017803"></a><a name="p49017803"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p11019092"><a name="p11019092"></a><a name="p11019092"></a>Specifies the authentication hash algorithm. The value can be <strong id="b842352706165820"><a name="b842352706165820"></a><a name="b842352706165820"></a>md5</strong>, <strong id="b842352706165823"><a name="b842352706165823"></a><a name="b842352706165823"></a>sha1</strong>, <strong id="b842352706165833"><a name="b842352706165833"></a><a name="b842352706165833"></a>sha2-256</strong>, <strong id="b842352706165840"><a name="b842352706165840"></a><a name="b842352706165840"></a>sha2-384</strong>, or <strong id="b842352706165851"><a name="b842352706165851"></a><a name="b842352706165851"></a>sha2-512</strong>.</p>
</td>
</tr>
<tr id="row32062968"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p46963595"><a name="p46963595"></a><a name="p46963595"></a>encapsulation_mode</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p45954822"><a name="p45954822"></a><a name="p45954822"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p31353106"><a name="p31353106"></a><a name="p31353106"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p56573654"><a name="p56573654"></a><a name="p56573654"></a>Specifies the encapsulation mode. The default value is <strong id="b84235270617116"><a name="b84235270617116"></a><a name="b84235270617116"></a>tunnel</strong>.</p>
</td>
</tr>
<tr id="row39400845"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p37351897"><a name="p37351897"></a><a name="p37351897"></a>encryption_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p5604850"><a name="p5604850"></a><a name="p5604850"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p51339711"><a name="p51339711"></a><a name="p51339711"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p64875945"><a name="p64875945"></a><a name="p64875945"></a>Specifies the encryption algorithm. The value can be <strong id="b8423527061721"><a name="b8423527061721"></a><a name="b8423527061721"></a>3des</strong>, <strong id="b84235270617211"><a name="b84235270617211"></a><a name="b84235270617211"></a>aes-128</strong>, <strong id="b84235270617219"><a name="b84235270617219"></a><a name="b84235270617219"></a>aes-192</strong>, or <strong id="b84235270617227"><a name="b84235270617227"></a><a name="b84235270617227"></a>aes-256</strong>. The default value is <strong id="b84235270617239"><a name="b84235270617239"></a><a name="b84235270617239"></a>aes-128</strong>.</p>
</td>
</tr>
<tr id="row47012596"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49923923"><a name="p49923923"></a><a name="p49923923"></a>pfs</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p17305987"><a name="p17305987"></a><a name="p17305987"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p59607724"><a name="p59607724"></a><a name="p59607724"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p6588145672511"><a name="p6588145672511"></a><a name="p6588145672511"></a>Specifies the PFS. The value can be <strong id="b58067010359"><a name="b58067010359"></a><a name="b58067010359"></a>group1</strong>, <strong id="b108076063516"><a name="b108076063516"></a><a name="b108076063516"></a>group2</strong>, <strong id="b28081007355"><a name="b28081007355"></a><a name="b28081007355"></a>group5</strong>, <strong id="b78081909351"><a name="b78081909351"></a><a name="b78081909351"></a>group14</strong>, <strong id="b108101908350"><a name="b108101908350"></a><a name="b108101908350"></a>group15</strong>, <strong id="b1881080163517"><a name="b1881080163517"></a><a name="b1881080163517"></a>group16</strong>, <strong id="b118116093514"><a name="b118116093514"></a><a name="b118116093514"></a>group19</strong>, <strong id="b28113043510"><a name="b28113043510"></a><a name="b28113043510"></a>group20</strong>, <strong id="b2081214033510"><a name="b2081214033510"></a><a name="b2081214033510"></a>group21</strong>, or <strong id="b158135017357"><a name="b158135017357"></a><a name="b158135017357"></a>disable</strong>.</p>
<p id="p489023122614"><a name="p489023122614"></a><a name="p489023122614"></a>The default value is <strong id="b579329351"><a name="b579329351"></a><a name="b579329351"></a>group5</strong>.</p>
<p id="p89224267257"><a name="p89224267257"></a><a name="p89224267257"></a>The value <strong id="b129306212359"><a name="b129306212359"></a><a name="b129306212359"></a>disable</strong> indicates that the PFS function is disabled.</p>
</td>
</tr>
<tr id="row34595869"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p50801977"><a name="p50801977"></a><a name="p50801977"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p21319498"><a name="p21319498"></a><a name="p21319498"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p49157816"><a name="p49157816"></a><a name="p49157816"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p22360170"><a name="p22360170"></a><a name="p22360170"></a>Specifies the lifetime value of the SA. The default unit is <strong id="b842352706101111"><a name="b842352706101111"></a><a name="b842352706101111"></a>seconds</strong>. The default value is <strong id="b842352706101115"><a name="b842352706101115"></a><a name="b842352706101115"></a>3600</strong>.</p>
</td>
</tr>
<tr id="row67023809"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p60219412"><a name="p60219412"></a><a name="p60219412"></a>units</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p45934241"><a name="p45934241"></a><a name="p45934241"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p29686030"><a name="p29686030"></a><a name="p29686030"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p55758211"><a name="p55758211"></a><a name="p55758211"></a>Specifies the lifecycle unit. The default value is <strong id="b842352706101139"><a name="b842352706101139"></a><a name="b842352706101139"></a>seconds</strong>.</p>
</td>
</tr>
<tr id="row32061857"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p46873590"><a name="p46873590"></a><a name="p46873590"></a>lifetime</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p38664423"><a name="p38664423"></a><a name="p38664423"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p44810590"><a name="p44810590"></a><a name="p44810590"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p5779136"><a name="p5779136"></a><a name="p5779136"></a>Specifies the lifetime object of SA.</p>
</td>
</tr>
<tr id="row52012230"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p52241078"><a name="p52241078"></a><a name="p52241078"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p3668935"><a name="p3668935"></a><a name="p3668935"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p28748320"><a name="p28748320"></a><a name="p28748320"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p46912618"><a name="p46912618"></a><a name="p46912618"></a>Specifies the IPsec policy name.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>1.  The  **project\_id**  parameter is not supported.  
>2.  The value of  **name**  can contain 1 to 64 characters.  
>3.  The value of  **description**  can contain a maximum of 255 characters.  
>4.  The value of  **transform\_protocol**  can only be  **esp**,  **ah**, or  **ah-esp**.  
>5.  The value of  **auth\_algorithm**  can only be  **md5**,  **sha1**,  **sha2-256**,  **sha2-384**, or  **sha2-512**.  
>6.  The value of  **encapsulation\_mode**  can only be  **tunnel**.  
>7.  The value of  **units**  can only be in seconds.  
>8.  The value of  **value**  can only be an integer ranging from 60 to 604,800.  
>9.  The value of  **encryption\_algorithm**  can only be  **aes-192**,  **aes-256**,  **group2**,  **group5**, or  **group14**.  

## Response Message<a name="section33470841"></a>

[Table 3](#table41825741)  describes the response parameters.

**Table  3**  Response parameters

<a name="table41825741"></a>
<table><thead align="left"><tr id="row35695699"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p5670474"><a name="p5670474"></a><a name="p5670474"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p56655270"><a name="p56655270"></a><a name="p56655270"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p66343596"><a name="p66343596"></a><a name="p66343596"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5122214"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p12246180"><a name="p12246180"></a><a name="p12246180"></a>encryption_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p52416527"><a name="p52416527"></a><a name="p52416527"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p39015754"><a name="p39015754"></a><a name="p39015754"></a>Specifies the encryption algorithm. The value can be <strong id="b458331934"><a name="b458331934"></a><a name="b458331934"></a>3des</strong>, <strong id="b1422370126"><a name="b1422370126"></a><a name="b1422370126"></a>aes-128</strong>, <strong id="b723315459"><a name="b723315459"></a><a name="b723315459"></a>aes-192</strong>, or <strong id="b958515037"><a name="b958515037"></a><a name="b958515037"></a>aes-256</strong>. The default value is <strong id="b775604940"><a name="b775604940"></a><a name="b775604940"></a>aes-128</strong>.</p>
</td>
</tr>
<tr id="row15597466"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p55435195"><a name="p55435195"></a><a name="p55435195"></a>pfs</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p61065805"><a name="p61065805"></a><a name="p61065805"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1341342012274"><a name="p1341342012274"></a><a name="p1341342012274"></a>Specifies the PFS. The value can be <strong id="b111621446359"><a name="b111621446359"></a><a name="b111621446359"></a>group1</strong>, <strong id="b6162124183514"><a name="b6162124183514"></a><a name="b6162124183514"></a>group2</strong>, <strong id="b116217433517"><a name="b116217433517"></a><a name="b116217433517"></a>group5</strong>, <strong id="b1316214412356"><a name="b1316214412356"></a><a name="b1316214412356"></a>group14</strong>, <strong id="b2164194153510"><a name="b2164194153510"></a><a name="b2164194153510"></a>group15</strong>, <strong id="b2016414483518"><a name="b2016414483518"></a><a name="b2016414483518"></a>group16</strong>, <strong id="b11643416358"><a name="b11643416358"></a><a name="b11643416358"></a>group19</strong>, <strong id="b416513423512"><a name="b416513423512"></a><a name="b416513423512"></a>group20</strong>, <strong id="b141651844358"><a name="b141651844358"></a><a name="b141651844358"></a>group21</strong>, or <strong id="b11167134163518"><a name="b11167134163518"></a><a name="b11167134163518"></a>disable</strong>.</p>
<p id="p74161620162715"><a name="p74161620162715"></a><a name="p74161620162715"></a>The default value is <strong id="b71824516355"><a name="b71824516355"></a><a name="b71824516355"></a>group5</strong>.</p>
<p id="p14417122062713"><a name="p14417122062713"></a><a name="p14417122062713"></a>The value <strong id="b792615511351"><a name="b792615511351"></a><a name="b792615511351"></a>disable</strong> indicates that the PFS function is disabled.</p>
</td>
</tr>
<tr id="row48367351"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p25441382"><a name="p25441382"></a><a name="p25441382"></a>lifetime</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p47486057"><a name="p47486057"></a><a name="p47486057"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p36677197"><a name="p36677197"></a><a name="p36677197"></a>Specifies the lifetime object of SA.</p>
</td>
</tr>
<tr id="row61659320"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p28349038"><a name="p28349038"></a><a name="p28349038"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p14570748"><a name="p14570748"></a><a name="p14570748"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p35661763"><a name="p35661763"></a><a name="p35661763"></a>Specifies the IPsec policy name.</p>
</td>
</tr>
<tr id="row52520413"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p26295076"><a name="p26295076"></a><a name="p26295076"></a>transform_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p49526440"><a name="p49526440"></a><a name="p49526440"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1856645"><a name="p1856645"></a><a name="p1856645"></a>Specifies the transform protocol used. The value can be <strong id="b1060973911"><a name="b1060973911"></a><a name="b1060973911"></a>esp</strong>, <strong id="b1850442652"><a name="b1850442652"></a><a name="b1850442652"></a>ah</strong>, or <strong id="b575293144"><a name="b575293144"></a><a name="b575293144"></a>ah-esp</strong>. The default value is <strong id="b920655545"><a name="b920655545"></a><a name="b920655545"></a>esp</strong>.</p>
</td>
</tr>
<tr id="row16709807"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p11317154"><a name="p11317154"></a><a name="p11317154"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p44274261"><a name="p44274261"></a><a name="p44274261"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p36263964"><a name="p36263964"></a><a name="p36263964"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row57940224"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p62646535"><a name="p62646535"></a><a name="p62646535"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p41204595"><a name="p41204595"></a><a name="p41204595"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p28849561"><a name="p28849561"></a><a name="p28849561"></a>Specifies the IPsec policy ID.</p>
</td>
</tr>
<tr id="row58319463"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p26256062"><a name="p26256062"></a><a name="p26256062"></a>encapsulation_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p46366269"><a name="p46366269"></a><a name="p46366269"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p4615638"><a name="p4615638"></a><a name="p4615638"></a>Specifies the encapsulation mode. The default value is <strong id="b1973039499"><a name="b1973039499"></a><a name="b1973039499"></a>tunnel</strong>.</p>
</td>
</tr>
<tr id="row41540743"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p9356983"><a name="p9356983"></a><a name="p9356983"></a>auth_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p19718131"><a name="p19718131"></a><a name="p19718131"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p51881906"><a name="p51881906"></a><a name="p51881906"></a>Specifies the authentication hash algorithm. The value can be <strong id="b386339358"><a name="b386339358"></a><a name="b386339358"></a>md5</strong>, <strong id="b167959609"><a name="b167959609"></a><a name="b167959609"></a>sha1</strong>, <strong id="b1018329879"><a name="b1018329879"></a><a name="b1018329879"></a>sha2-256</strong>, <strong id="b692830195"><a name="b692830195"></a><a name="b692830195"></a>sha2-384</strong>, or <strong id="b1544948481"><a name="b1544948481"></a><a name="b1544948481"></a>sha2-512</strong>.</p>
</td>
</tr>
<tr id="row64283975"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39619499"><a name="p39619499"></a><a name="p39619499"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p55062814"><a name="p55062814"></a><a name="p55062814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p20114008"><a name="p20114008"></a><a name="p20114008"></a>Provides supplementary information about the IPsec policy.</p>
</td>
</tr>
<tr id="row17450296"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p4187856"><a name="p4187856"></a><a name="p4187856"></a>ipsecpolicy</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p3672032"><a name="p3672032"></a><a name="p3672032"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p123786"><a name="p123786"></a><a name="p123786"></a>Specifies the IPsec policy object.</p>
</td>
</tr>
<tr id="row5825185"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2077973"><a name="p2077973"></a><a name="p2077973"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p34098154"><a name="p34098154"></a><a name="p34098154"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p44149718"><a name="p44149718"></a><a name="p44149718"></a>Specifies the lifetime value of the SA. The default unit is <strong id="b842352706101322"><a name="b842352706101322"></a><a name="b842352706101322"></a>seconds</strong>. The default value is <strong id="b842352706101327"><a name="b842352706101327"></a><a name="b842352706101327"></a>3600</strong>.</p>
</td>
</tr>
<tr id="row61803142"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39998624"><a name="p39998624"></a><a name="p39998624"></a>units</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p18663102"><a name="p18663102"></a><a name="p18663102"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p42047784"><a name="p42047784"></a><a name="p42047784"></a>Specifies the lifecycle unit. The default value is <strong id="b8423527061079"><a name="b8423527061079"></a><a name="b8423527061079"></a>seconds</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section32802119"></a>

-   Example Request

```
PUT /v2.0/vpn/ipsecpolicies/{ipsecpolicy_id}
{
  "ipsecpolicy" : {
    "pfs" : "group14"
  }
}
```

-   Example Response

    ```
    {
        "ipsecpolicy": {
            "name": "ipsecpolicy1",
            "transform_protocol": "esp",
            "auth_algorithm": "sha1",
            "encapsulation_mode": "tunnel",
            "encryption_algorithm": "aes-128",
            "pfs": "group14",
            "project_id": "ccb81365fe36411a9011e90491fe1330",
            "tenant_id": "ccb81365fe36411a9011e90491fe1330",
            "lifetime": {
                "units": "seconds",
                "value": 3600
            },
            "id": "5291b189-fd84-46e5-84bd-78f40c05d69c",
            "description": ""
        }
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

