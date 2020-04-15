# Creating an IPsec Policy<a name="en_topic_0093011504"></a>

## **Function**<a name="section51184318"></a>

This interface is used to create an IPsec policy.

## URI<a name="section58005681"></a>

POST /v2.0/vpn/ipsecpolicies

## Request Message<a name="section839735"></a>

**Table  1**  Request parameters

<a name="table45459112"></a>
<table><thead align="left"><tr id="row26085680"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p32565348"><a name="p32565348"></a><a name="p32565348"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p20547495"><a name="p20547495"></a><a name="p20547495"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p53734436"><a name="p53734436"></a><a name="p53734436"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p57522049"><a name="p57522049"></a><a name="p57522049"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row28774374"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49022972"><a name="p49022972"></a><a name="p49022972"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p11437802"><a name="p11437802"></a><a name="p11437802"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p54046809"><a name="p54046809"></a><a name="p54046809"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p15715441"><a name="p15715441"></a><a name="p15715441"></a>Specifies the IPsec policy name.</p>
</td>
</tr>
<tr id="row7221243"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p48049826"><a name="p48049826"></a><a name="p48049826"></a>pfs</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p66830726"><a name="p66830726"></a><a name="p66830726"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p44579726"><a name="p44579726"></a><a name="p44579726"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1020312412913"><a name="p1020312412913"></a><a name="p1020312412913"></a>Specifies the PFS. The value can be <strong id="b488215063218"><a name="b488215063218"></a><a name="b488215063218"></a>group1</strong>, <strong id="b1895111102329"><a name="b1895111102329"></a><a name="b1895111102329"></a>group2</strong>, <strong id="b2527141953217"><a name="b2527141953217"></a><a name="b2527141953217"></a>group5</strong>, <strong id="b2653172453212"><a name="b2653172453212"></a><a name="b2653172453212"></a>group14</strong>, <strong id="b116523011322"><a name="b116523011322"></a><a name="b116523011322"></a>group15</strong>, <strong id="b207979452325"><a name="b207979452325"></a><a name="b207979452325"></a>group16</strong>, <strong id="b6866052193219"><a name="b6866052193219"></a><a name="b6866052193219"></a>group19</strong>, <strong id="b69228083313"><a name="b69228083313"></a><a name="b69228083313"></a>group20</strong>, <strong id="b48501778336"><a name="b48501778336"></a><a name="b48501778336"></a>group21</strong>, or <strong id="b644761513314"><a name="b644761513314"></a><a name="b644761513314"></a>disable</strong>.</p>
<p id="p32051440298"><a name="p32051440298"></a><a name="p32051440298"></a>The default value is <strong id="b842352706201018"><a name="b842352706201018"></a><a name="b842352706201018"></a>group5</strong>.</p>
<p id="p1206943292"><a name="p1206943292"></a><a name="p1206943292"></a>The value <strong id="b2626173812332"><a name="b2626173812332"></a><a name="b2626173812332"></a>disable</strong> indicates that the PFS function is disabled.</p>
</td>
</tr>
<tr id="row17930557"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p43089040"><a name="p43089040"></a><a name="p43089040"></a>auth_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p551331"><a name="p551331"></a><a name="p551331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p44657822"><a name="p44657822"></a><a name="p44657822"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p60513834"><a name="p60513834"></a><a name="p60513834"></a>Specifies the authentication hash algorithm. The value can be <strong id="b842352706165820"><a name="b842352706165820"></a><a name="b842352706165820"></a>md5</strong>, <strong id="b842352706165823"><a name="b842352706165823"></a><a name="b842352706165823"></a>sha1</strong>, <strong id="b842352706165833"><a name="b842352706165833"></a><a name="b842352706165833"></a>sha2-256</strong>, <strong id="b842352706165840"><a name="b842352706165840"></a><a name="b842352706165840"></a>sha2-384</strong>, or <strong id="b842352706165851"><a name="b842352706165851"></a><a name="b842352706165851"></a>sha2-512</strong>.</p>
</td>
</tr>
<tr id="row7753598"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p24061669"><a name="p24061669"></a><a name="p24061669"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p2838193"><a name="p2838193"></a><a name="p2838193"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p28567114"><a name="p28567114"></a><a name="p28567114"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p32234903"><a name="p32234903"></a><a name="p32234903"></a>Provides supplementary information about the IPsec policy.</p>
</td>
</tr>
<tr id="row21678677"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p11142412"><a name="p11142412"></a><a name="p11142412"></a>encapsulation_mode</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p30120171"><a name="p30120171"></a><a name="p30120171"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p23814811"><a name="p23814811"></a><a name="p23814811"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p49951556"><a name="p49951556"></a><a name="p49951556"></a>Specifies the encapsulation mode. The default value is <strong id="b84235270617116"><a name="b84235270617116"></a><a name="b84235270617116"></a>tunnel</strong>.</p>
</td>
</tr>
<tr id="row46910821"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p41680117"><a name="p41680117"></a><a name="p41680117"></a>encryption_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p20646289"><a name="p20646289"></a><a name="p20646289"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p61736738"><a name="p61736738"></a><a name="p61736738"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p34619920"><a name="p34619920"></a><a name="p34619920"></a>Specifies the encryption algorithm. The value can be <strong id="b8423527061721"><a name="b8423527061721"></a><a name="b8423527061721"></a>3des</strong>, <strong id="b84235270617211"><a name="b84235270617211"></a><a name="b84235270617211"></a>aes-128</strong>, <strong id="b84235270617219"><a name="b84235270617219"></a><a name="b84235270617219"></a>aes-192</strong>, or <strong id="b84235270617227"><a name="b84235270617227"></a><a name="b84235270617227"></a>aes-256</strong>. The default value is <strong id="b84235270617239"><a name="b84235270617239"></a><a name="b84235270617239"></a>aes-128</strong>.</p>
</td>
</tr>
<tr id="row43143829"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p4989273"><a name="p4989273"></a><a name="p4989273"></a>ipsecpolicy</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p1477932"><a name="p1477932"></a><a name="p1477932"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p52603705"><a name="p52603705"></a><a name="p52603705"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p33041702"><a name="p33041702"></a><a name="p33041702"></a>Specifies the IPsec policy object.</p>
</td>
</tr>
<tr id="row28939864"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p62427641"><a name="p62427641"></a><a name="p62427641"></a>lifetime</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p23474126"><a name="p23474126"></a><a name="p23474126"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p22356031"><a name="p22356031"></a><a name="p22356031"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p66008118"><a name="p66008118"></a><a name="p66008118"></a>Specifies the lifetime object of SA.</p>
</td>
</tr>
<tr id="row57202150"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p2862558"><a name="p2862558"></a><a name="p2862558"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p30540622"><a name="p30540622"></a><a name="p30540622"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p57871327"><a name="p57871327"></a><a name="p57871327"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p57065912"><a name="p57065912"></a><a name="p57065912"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row43831168"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p60663705"><a name="p60663705"></a><a name="p60663705"></a>transform_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p14813071"><a name="p14813071"></a><a name="p14813071"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p59008073"><a name="p59008073"></a><a name="p59008073"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p14924591"><a name="p14924591"></a><a name="p14924591"></a>Specifies the transform protocol used. The value can be <strong id="b842352706184452"><a name="b842352706184452"></a><a name="b842352706184452"></a>esp</strong>, <strong id="b842352706184456"><a name="b842352706184456"></a><a name="b842352706184456"></a>ah</strong>, or <strong id="b84235270618456"><a name="b84235270618456"></a><a name="b84235270618456"></a>ah-esp</strong>. The default value is <strong id="b1070371618"><a name="b1070371618"></a><a name="b1070371618"></a>esp</strong>.</p>
</td>
</tr>
<tr id="row15056516"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p11618302"><a name="p11618302"></a><a name="p11618302"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p1558396"><a name="p1558396"></a><a name="p1558396"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p59121255"><a name="p59121255"></a><a name="p59121255"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p24092326"><a name="p24092326"></a><a name="p24092326"></a>Specifies the lifetime value of the SA. The default unit is <strong id="b84235270610843"><a name="b84235270610843"></a><a name="b84235270610843"></a>seconds</strong>. The default value is <strong id="b84235270610838"><a name="b84235270610838"></a><a name="b84235270610838"></a>3600</strong>.</p>
</td>
</tr>
<tr id="row15504345"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p47892402"><a name="p47892402"></a><a name="p47892402"></a>units</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p54079315"><a name="p54079315"></a><a name="p54079315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p18348389"><a name="p18348389"></a><a name="p18348389"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p9824527"><a name="p9824527"></a><a name="p9824527"></a>Specifies the lifecycle unit. The default value is <strong id="b84235270610853"><a name="b84235270610853"></a><a name="b84235270610853"></a>seconds</strong>.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>1.  The  **project\_id**  parameter is not supported.  
>2.  The value of  **tenant\_id**  can contain a maximum of 255 characters.  
>3.  The value of  **name**  can contain 1 to 64 characters.  
>4.  The value of  **description**  can contain a maximum of 255 characters.  
>5.  The value of  **transform\_protocol**  can only be  **esp**,  **ah**, or  **ah-esp**.  
>6.  The value of  **auth\_algorithm**  can only be  **md5**,  **sha1**,  **sha2-256**,  **sha2-384**, or  **sha2-512**.  
>7.  The value of  **encapsulation\_mode**  can only be  **tunnel**.  
>8.  The value of  **units**  can only be in seconds.  
>9.  The value of  **value**  can only be an integer ranging from 60 to 604,800.  
>10. The value of  **encryption\_algorithm**  can only be  **aes-192**,  **aes-256**,  **group2**,  **group5**, or  **group14**.  

## Response Message<a name="section7557620"></a>

[Table 2](#table57589242)  describes the response parameters.

**Table  2**  Response parameters

<a name="table57589242"></a>
<table><thead align="left"><tr id="row35311297"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p41642789"><a name="p41642789"></a><a name="p41642789"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p17622742"><a name="p17622742"></a><a name="p17622742"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p61346876"><a name="p61346876"></a><a name="p61346876"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3041091"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p45001781"><a name="p45001781"></a><a name="p45001781"></a>auth_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p21265660"><a name="p21265660"></a><a name="p21265660"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p4672552"><a name="p4672552"></a><a name="p4672552"></a>Specifies the authentication hash algorithm. The value can be <strong id="b156386238"><a name="b156386238"></a><a name="b156386238"></a>md5</strong>, <strong id="b1612457743"><a name="b1612457743"></a><a name="b1612457743"></a>sha1</strong>, <strong id="b913520395"><a name="b913520395"></a><a name="b913520395"></a>sha2-256</strong>, <strong id="b849778651"><a name="b849778651"></a><a name="b849778651"></a>sha2-384</strong>, or <strong id="b823164186"><a name="b823164186"></a><a name="b823164186"></a>sha2-512</strong>.</p>
</td>
</tr>
<tr id="row42052973"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p50847687"><a name="p50847687"></a><a name="p50847687"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p25022010"><a name="p25022010"></a><a name="p25022010"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p21127816"><a name="p21127816"></a><a name="p21127816"></a>Provides supplementary information about the IPsec policy.</p>
</td>
</tr>
<tr id="row55932620"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p34248408"><a name="p34248408"></a><a name="p34248408"></a>encapsulation_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p22657631"><a name="p22657631"></a><a name="p22657631"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p10588164"><a name="p10588164"></a><a name="p10588164"></a>Specifies the encapsulation mode. The default value is <strong id="b1697058608"><a name="b1697058608"></a><a name="b1697058608"></a>tunnel</strong>.</p>
</td>
</tr>
<tr id="row28184617"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1252607"><a name="p1252607"></a><a name="p1252607"></a>encryption_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p34352342"><a name="p34352342"></a><a name="p34352342"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p34153125"><a name="p34153125"></a><a name="p34153125"></a>Specifies the encryption algorithm. The value can be <strong id="b1223398365"><a name="b1223398365"></a><a name="b1223398365"></a>3des</strong>, <strong id="b1629299840"><a name="b1629299840"></a><a name="b1629299840"></a>aes-128</strong>, <strong id="b1192961710"><a name="b1192961710"></a><a name="b1192961710"></a>aes-192</strong>, or <strong id="b538777431"><a name="b538777431"></a><a name="b538777431"></a>aes-256</strong>. The default value is <strong id="b734798645"><a name="b734798645"></a><a name="b734798645"></a>aes-128</strong>.</p>
</td>
</tr>
<tr id="row38942675"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p240095"><a name="p240095"></a><a name="p240095"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p19447695"><a name="p19447695"></a><a name="p19447695"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p22377468"><a name="p22377468"></a><a name="p22377468"></a>Specifies the IPsec policy ID.</p>
</td>
</tr>
<tr id="row51358334"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p66384370"><a name="p66384370"></a><a name="p66384370"></a>ipsecpolicy</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p8424883"><a name="p8424883"></a><a name="p8424883"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45062713"><a name="p45062713"></a><a name="p45062713"></a>Specifies the IPsec policy object.</p>
</td>
</tr>
<tr id="row2911240"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p34483920"><a name="p34483920"></a><a name="p34483920"></a>lifetime</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p41734120"><a name="p41734120"></a><a name="p41734120"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p13397545"><a name="p13397545"></a><a name="p13397545"></a>Specifies the lifetime object of SA.</p>
</td>
</tr>
<tr id="row53469045"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p36025402"><a name="p36025402"></a><a name="p36025402"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p32376435"><a name="p32376435"></a><a name="p32376435"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p22238563"><a name="p22238563"></a><a name="p22238563"></a>Specifies the IPsec policy name.</p>
</td>
</tr>
<tr id="row65929341"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p38676409"><a name="p38676409"></a><a name="p38676409"></a>pfs</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p45781421"><a name="p45781421"></a><a name="p45781421"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p6588145672511"><a name="p6588145672511"></a><a name="p6588145672511"></a>Specifies the PFS. The value can be <strong id="b12346651183314"><a name="b12346651183314"></a><a name="b12346651183314"></a>group1</strong>, <strong id="b8348351193317"><a name="b8348351193317"></a><a name="b8348351193317"></a>group2</strong>, <strong id="b135125143320"><a name="b135125143320"></a><a name="b135125143320"></a>group5</strong>, <strong id="b1935375117331"><a name="b1935375117331"></a><a name="b1935375117331"></a>group14</strong>, <strong id="b5355145163316"><a name="b5355145163316"></a><a name="b5355145163316"></a>group15</strong>, <strong id="b13356135113317"><a name="b13356135113317"></a><a name="b13356135113317"></a>group16</strong>, <strong id="b193588513336"><a name="b193588513336"></a><a name="b193588513336"></a>group19</strong>, <strong id="b1360051163319"><a name="b1360051163319"></a><a name="b1360051163319"></a>group20</strong>, <strong id="b73621551163316"><a name="b73621551163316"></a><a name="b73621551163316"></a>group21</strong>, or <strong id="b43643516332"><a name="b43643516332"></a><a name="b43643516332"></a>disable</strong>.</p>
<p id="p489023122614"><a name="p489023122614"></a><a name="p489023122614"></a>The default value is <strong id="b1687911520349"><a name="b1687911520349"></a><a name="b1687911520349"></a>group5</strong>.</p>
<p id="p89224267257"><a name="p89224267257"></a><a name="p89224267257"></a>The value <strong id="b1758510613343"><a name="b1758510613343"></a><a name="b1758510613343"></a>disable</strong> indicates that the PFS function is disabled.</p>
</td>
</tr>
<tr id="row810977"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p65689182"><a name="p65689182"></a><a name="p65689182"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p19223544"><a name="p19223544"></a><a name="p19223544"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p28119201"><a name="p28119201"></a><a name="p28119201"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row51746218"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p30694147"><a name="p30694147"></a><a name="p30694147"></a>transform_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p3197948"><a name="p3197948"></a><a name="p3197948"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p43771375"><a name="p43771375"></a><a name="p43771375"></a>Specifies the transform protocol used. The value can be <strong id="b495038905"><a name="b495038905"></a><a name="b495038905"></a>esp</strong>, <strong id="b669159008"><a name="b669159008"></a><a name="b669159008"></a>ah</strong>, or <strong id="b1802917355"><a name="b1802917355"></a><a name="b1802917355"></a>ah-esp</strong>. The default value is <strong id="b1966648559"><a name="b1966648559"></a><a name="b1966648559"></a>esp</strong>.</p>
</td>
</tr>
<tr id="row51573880"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p16734741"><a name="p16734741"></a><a name="p16734741"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p13336762"><a name="p13336762"></a><a name="p13336762"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p59650110"><a name="p59650110"></a><a name="p59650110"></a>Specifies the lifetime value of the SA. The default unit is <strong id="b842352706101248"><a name="b842352706101248"></a><a name="b842352706101248"></a>seconds</strong>. The default value is <strong id="b842352706101252"><a name="b842352706101252"></a><a name="b842352706101252"></a>3600</strong>.</p>
</td>
</tr>
<tr id="row67088950"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p65495901"><a name="p65495901"></a><a name="p65495901"></a>units</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p3567727"><a name="p3567727"></a><a name="p3567727"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p53976698"><a name="p53976698"></a><a name="p53976698"></a>Specifies the lifecycle unit. The default value is <strong id="b84235270610132"><a name="b84235270610132"></a><a name="b84235270610132"></a>seconds</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section909717"></a>

-   Request Example

    ```
    POST /v2.0/vpn/ipsecpolicies
    {
      "ipsecpolicy" : {
        "name" : "ipsecpolicy1",
        "transform_protocol" : "esp",
        "auth_algorithm" : "sha1",
        "encapsulation_mode" : "tunnel",
        "encryption_algorithm" : "aes-128",
        "pfs" : "group5",
        "lifetime" : {
          "units" : "seconds",
          "value" : 7200
        }
      }
    }
    ```


-   Example Response

    ```
    {
      "ipsecpolicy" : {
        "name" : "ipsecpolicy1",
        "transform_protocol" : "esp",
        "auth_algorithm" : "sha1",
        "encapsulation_mode" : "tunnel",
        "encryption_algorithm" : "aes-128",
        "pfs" : "group5",
        "project_id" : "ccb81365fe36411a9011e90491fe1330",
        "tenant_id" : "ccb81365fe36411a9011e90491fe1330",
        "lifetime" : {
          "units" : "seconds",
          "value" : 7200
        },
        "id" : "5291b189-fd84-46e5-84bd-78f40c05d69c",
        "description" : ""
      }
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

