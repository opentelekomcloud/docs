# Updating an IKE Policy<a name="en_topic_0093011513"></a>

## **Function**<a name="section59206997"></a>

This interface is used to update an IKE policy.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the IKE policy is updated, the IPsec VPN connection also needs to be updated.  

## URI<a name="section63100926"></a>

PUT /v2.0/vpn/ikepolicies/\{ikepolicy\_id\}

**Table  1**  Parameter description

<a name="table492018108144"></a>
<table><thead align="left"><tr id="row29285105141"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p3928151019147"><a name="p3928151019147"></a><a name="p3928151019147"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p69359101144"><a name="p69359101144"></a><a name="p69359101144"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p7935510111417"><a name="p7935510111417"></a><a name="p7935510111417"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p893571013140"><a name="p893571013140"></a><a name="p893571013140"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1294311103147"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1943141015146"><a name="p1943141015146"></a><a name="p1943141015146"></a>ikepolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p69514103140"><a name="p69514103140"></a><a name="p69514103140"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p179517108141"><a name="p179517108141"></a><a name="p179517108141"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1595131020148"><a name="p1595131020148"></a><a name="p1595131020148"></a>Specifies the IKE policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section10901353"></a>

[Table 2](#table9467673)  describes the request parameters.

**Table  2**  Request parameters

<a name="table9467673"></a>
<table><thead align="left"><tr id="row5698118"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p58894414"><a name="p58894414"></a><a name="p58894414"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p5718243"><a name="p5718243"></a><a name="p5718243"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p60524524"><a name="p60524524"></a><a name="p60524524"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p3539410"><a name="p3539410"></a><a name="p3539410"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61306625"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p66889567"><a name="p66889567"></a><a name="p66889567"></a>auth_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p49345813"><a name="p49345813"></a><a name="p49345813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p37587916"><a name="p37587916"></a><a name="p37587916"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p24722347"><a name="p24722347"></a><a name="p24722347"></a>Specifies the authentication hash algorithm. The value can be <strong id="b842352706165820"><a name="b842352706165820"></a><a name="b842352706165820"></a>md5</strong>, <strong id="b842352706165823"><a name="b842352706165823"></a><a name="b842352706165823"></a>sha1</strong>, <strong id="b842352706165833"><a name="b842352706165833"></a><a name="b842352706165833"></a>sha2-256</strong>, <strong id="b842352706165840"><a name="b842352706165840"></a><a name="b842352706165840"></a>sha2-384</strong>, or <strong id="b842352706165851"><a name="b842352706165851"></a><a name="b842352706165851"></a>sha2-512</strong>.</p>
</td>
</tr>
<tr id="row21174538"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p37415993"><a name="p37415993"></a><a name="p37415993"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p10796581"><a name="p10796581"></a><a name="p10796581"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p2107829"><a name="p2107829"></a><a name="p2107829"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p36516433"><a name="p36516433"></a><a name="p36516433"></a>Provides supplementary information about the IKE policy.</p>
</td>
</tr>
<tr id="row60212448"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p45370106"><a name="p45370106"></a><a name="p45370106"></a>encryption_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p51099989"><a name="p51099989"></a><a name="p51099989"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p45458457"><a name="p45458457"></a><a name="p45458457"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p58256364"><a name="p58256364"></a><a name="p58256364"></a>Specifies the encryption algorithm. The value can be <strong id="b8423527061721"><a name="b8423527061721"></a><a name="b8423527061721"></a>3des</strong>, <strong id="b84235270617211"><a name="b84235270617211"></a><a name="b84235270617211"></a>aes-128</strong>, <strong id="b84235270617219"><a name="b84235270617219"></a><a name="b84235270617219"></a>aes-192</strong>, or <strong id="b84235270617227"><a name="b84235270617227"></a><a name="b84235270617227"></a>aes-256</strong>. The default value is <strong id="b84235270617239"><a name="b84235270617239"></a><a name="b84235270617239"></a>aes-128</strong>.</p>
</td>
</tr>
<tr id="row54545236"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p56088004"><a name="p56088004"></a><a name="p56088004"></a>ike_version</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p46834456"><a name="p46834456"></a><a name="p46834456"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p35494585"><a name="p35494585"></a><a name="p35494585"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p56489102"><a name="p56489102"></a><a name="p56489102"></a>Specifies the IKE version. The value can be <strong id="b2123880768213834"><a name="b2123880768213834"></a><a name="b2123880768213834"></a>v1</strong> or <strong id="b499525058213834"><a name="b499525058213834"></a><a name="b499525058213834"></a>v2</strong>. The default value is <strong id="b842352706213844"><a name="b842352706213844"></a><a name="b842352706213844"></a>v1</strong>.</p>
</td>
</tr>
<tr id="row38639871"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p42821886"><a name="p42821886"></a><a name="p42821886"></a>ikepolicy</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p46020774"><a name="p46020774"></a><a name="p46020774"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p36695198"><a name="p36695198"></a><a name="p36695198"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p19521038"><a name="p19521038"></a><a name="p19521038"></a>Specifies the IKE policy object.</p>
</td>
</tr>
<tr id="row41471619"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p3757979"><a name="p3757979"></a><a name="p3757979"></a>lifetime</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p35960896"><a name="p35960896"></a><a name="p35960896"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p27151449"><a name="p27151449"></a><a name="p27151449"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p51783759"><a name="p51783759"></a><a name="p51783759"></a>Specifies the lifetime object of SA.</p>
</td>
</tr>
<tr id="row63400648"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p35178835"><a name="p35178835"></a><a name="p35178835"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p30913391"><a name="p30913391"></a><a name="p30913391"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p20956739"><a name="p20956739"></a><a name="p20956739"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p19774328"><a name="p19774328"></a><a name="p19774328"></a>Specifies the IKE policy name.</p>
</td>
</tr>
<tr id="row43751230"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p54188775"><a name="p54188775"></a><a name="p54188775"></a>pfs</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p27214660"><a name="p27214660"></a><a name="p27214660"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p56903870"><a name="p56903870"></a><a name="p56903870"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p6588145672511"><a name="p6588145672511"></a><a name="p6588145672511"></a>Specifies the PFS. The value can be <strong id="b15233116153619"><a name="b15233116153619"></a><a name="b15233116153619"></a>group1</strong>, <strong id="b72332633619"><a name="b72332633619"></a><a name="b72332633619"></a>group2</strong>, <strong id="b1523510653611"><a name="b1523510653611"></a><a name="b1523510653611"></a>group5</strong>, <strong id="b202357618364"><a name="b202357618364"></a><a name="b202357618364"></a>group14</strong>, <strong id="b32364633616"><a name="b32364633616"></a><a name="b32364633616"></a>group15</strong>, <strong id="b16236767365"><a name="b16236767365"></a><a name="b16236767365"></a>group16</strong>, <strong id="b18237126123615"><a name="b18237126123615"></a><a name="b18237126123615"></a>group19</strong>, <strong id="b1923714633614"><a name="b1923714633614"></a><a name="b1923714633614"></a>group20</strong>, <strong id="b1923813683611"><a name="b1923813683611"></a><a name="b1923813683611"></a>group21</strong>, or <strong id="b1023811619367"><a name="b1023811619367"></a><a name="b1023811619367"></a>disable</strong>.</p>
<p id="p489023122614"><a name="p489023122614"></a><a name="p489023122614"></a>The default value is <strong id="b20367157163618"><a name="b20367157163618"></a><a name="b20367157163618"></a>group5</strong>.</p>
</td>
</tr>
<tr id="row9643552"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p42930272"><a name="p42930272"></a><a name="p42930272"></a>phase1_negotiation_mode</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p54800025"><a name="p54800025"></a><a name="p54800025"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p9617010"><a name="p9617010"></a><a name="p9617010"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p40780307"><a name="p40780307"></a><a name="p40780307"></a>Specifies the IKE mode The default value is <strong id="b842352706213613"><a name="b842352706213613"></a><a name="b842352706213613"></a>main</strong>.</p>
</td>
</tr>
<tr id="row31478446"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p66726223"><a name="p66726223"></a><a name="p66726223"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p36115021"><a name="p36115021"></a><a name="p36115021"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p39635599"><a name="p39635599"></a><a name="p39635599"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p56366974"><a name="p56366974"></a><a name="p56366974"></a>Specifies the lifetime value of the SA. The default unit is <strong id="b842352706101653"><a name="b842352706101653"></a><a name="b842352706101653"></a>seconds</strong>. The default value is <strong id="b842352706101657"><a name="b842352706101657"></a><a name="b842352706101657"></a>3600</strong>.</p>
</td>
</tr>
<tr id="row37540721"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p20899598"><a name="p20899598"></a><a name="p20899598"></a>units</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p15145867"><a name="p15145867"></a><a name="p15145867"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p18855696"><a name="p18855696"></a><a name="p18855696"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p50916422"><a name="p50916422"></a><a name="p50916422"></a>Specifies the lifecycle unit. The default value is <strong id="b8423527061079"><a name="b8423527061079"></a><a name="b8423527061079"></a>seconds</strong>.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>1.  The  **ikepolicy\_id**  parameter must be specified.  
>2.  The value of  **name**  can contain 1 to 64 characters.  
>3.  The value of  **description**  can contain a maximum of 255 characters.  
>4.  The value of  **auth\_algorithm**  can only be  **md5**,  **sha1**,  **sha2-256**,  **sha2-384**, or  **sha2-512**.  
>5.  The value of  **encryption\_algorithm**  can only be  **3des**,  **aes-128**,  **aes-192**, or  **aes-256**.  
>6.  The value of  **phase1\_negotiation\_mode**  can only be  **main**  and  **aggressive**.  
>7.  The value of  **units**  can only be in seconds.  
>8.  The value of  **value**  can only be an integer ranging from 60 to 604,800.  
>9.  The value of  **ike\_version**  can only be  **v1**  or  **v2**.  
>10. The  **project\_id**  parameter is not supported.  

## Response Message<a name="section31003317"></a>

[Table 3](#table30589524)  describes the response parameters.

**Table  3**  Response parameters

<a name="table30589524"></a>
<table><thead align="left"><tr id="row17707452"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p25017536"><a name="p25017536"></a><a name="p25017536"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p13154536"><a name="p13154536"></a><a name="p13154536"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p4915910"><a name="p4915910"></a><a name="p4915910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row62644428"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p41033878"><a name="p41033878"></a><a name="p41033878"></a>auth_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p35409804"><a name="p35409804"></a><a name="p35409804"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p59951903"><a name="p59951903"></a><a name="p59951903"></a>Specifies the authentication hash algorithm. The value can be <strong id="b1058970326"><a name="b1058970326"></a><a name="b1058970326"></a>md5</strong>, <strong id="b799313540"><a name="b799313540"></a><a name="b799313540"></a>sha1</strong>, <strong id="b1989756512"><a name="b1989756512"></a><a name="b1989756512"></a>sha2-256</strong>, <strong id="b728910706"><a name="b728910706"></a><a name="b728910706"></a>sha2-384</strong>, or <strong id="b1843698762"><a name="b1843698762"></a><a name="b1843698762"></a>sha2-512</strong>.</p>
</td>
</tr>
<tr id="row2696221"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p17067371"><a name="p17067371"></a><a name="p17067371"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p40279785"><a name="p40279785"></a><a name="p40279785"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p963478"><a name="p963478"></a><a name="p963478"></a>Provides supplementary information about the IKE policy.</p>
</td>
</tr>
<tr id="row8671305"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p31287108"><a name="p31287108"></a><a name="p31287108"></a>encryption_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p51227795"><a name="p51227795"></a><a name="p51227795"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p24374351"><a name="p24374351"></a><a name="p24374351"></a>Specifies the encryption algorithm. The value can be <strong id="b605702229"><a name="b605702229"></a><a name="b605702229"></a>3des</strong>, <strong id="b1927999648"><a name="b1927999648"></a><a name="b1927999648"></a>aes-128</strong>, <strong id="b470192939"><a name="b470192939"></a><a name="b470192939"></a>aes-192</strong>, or <strong id="b358467858"><a name="b358467858"></a><a name="b358467858"></a>aes-256</strong>. The default value is <strong id="b731547647"><a name="b731547647"></a><a name="b731547647"></a>aes-128</strong>.</p>
</td>
</tr>
<tr id="row18042568"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p52161898"><a name="p52161898"></a><a name="p52161898"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p64364196"><a name="p64364196"></a><a name="p64364196"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p44522499"><a name="p44522499"></a><a name="p44522499"></a>Specifies the IKE policy ID.</p>
</td>
</tr>
<tr id="row65158171"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p43320494"><a name="p43320494"></a><a name="p43320494"></a>ike_version</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p19299134"><a name="p19299134"></a><a name="p19299134"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p54302323"><a name="p54302323"></a><a name="p54302323"></a>Specifies the IKE version. The value can be <strong id="b472173104"><a name="b472173104"></a><a name="b472173104"></a>v1</strong> or <strong id="b815504622"><a name="b815504622"></a><a name="b815504622"></a>v2</strong>. The default value is <strong id="b1412719502"><a name="b1412719502"></a><a name="b1412719502"></a>v1</strong>.</p>
</td>
</tr>
<tr id="row18958859"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p59272617"><a name="p59272617"></a><a name="p59272617"></a>lifetime</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p36352712"><a name="p36352712"></a><a name="p36352712"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5246632"><a name="p5246632"></a><a name="p5246632"></a>Specifies the lifetime object of SA.</p>
</td>
</tr>
<tr id="row47219689"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p66698493"><a name="p66698493"></a><a name="p66698493"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p33868853"><a name="p33868853"></a><a name="p33868853"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p16100147"><a name="p16100147"></a><a name="p16100147"></a>Specifies the IKE policy name.</p>
</td>
</tr>
<tr id="row10683599"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p60065170"><a name="p60065170"></a><a name="p60065170"></a>pfs</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p33440573"><a name="p33440573"></a><a name="p33440573"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8545646381"><a name="p8545646381"></a><a name="p8545646381"></a>Specifies the PFS. The value can be <strong id="b157916843618"><a name="b157916843618"></a><a name="b157916843618"></a>group1</strong>, <strong id="b358028203618"><a name="b358028203618"></a><a name="b358028203618"></a>group2</strong>, <strong id="b1058010817361"><a name="b1058010817361"></a><a name="b1058010817361"></a>group5</strong>, <strong id="b185811810361"><a name="b185811810361"></a><a name="b185811810361"></a>group14</strong>, <strong id="b45814883617"><a name="b45814883617"></a><a name="b45814883617"></a>group15</strong>, <strong id="b5582281363"><a name="b5582281363"></a><a name="b5582281363"></a>group16</strong>, <strong id="b2582118123618"><a name="b2582118123618"></a><a name="b2582118123618"></a>group19</strong>, <strong id="b135827814366"><a name="b135827814366"></a><a name="b135827814366"></a>group20</strong>, <strong id="b358318853619"><a name="b358318853619"></a><a name="b358318853619"></a>group21</strong>, or <strong id="b175835819368"><a name="b175835819368"></a><a name="b175835819368"></a>disable</strong>.</p>
<p id="p11546104619817"><a name="p11546104619817"></a><a name="p11546104619817"></a>The default value is <strong id="b22765111365"><a name="b22765111365"></a><a name="b22765111365"></a>group5</strong>.</p>
</td>
</tr>
<tr id="row21213148"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p40543448"><a name="p40543448"></a><a name="p40543448"></a>phase1_negotiation_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p62793889"><a name="p62793889"></a><a name="p62793889"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p9393336"><a name="p9393336"></a><a name="p9393336"></a>Specifies the IKE mode The default value is <strong id="b1136061932"><a name="b1136061932"></a><a name="b1136061932"></a>main</strong>.</p>
</td>
</tr>
<tr id="row17431163"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2638090"><a name="p2638090"></a><a name="p2638090"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p12358762"><a name="p12358762"></a><a name="p12358762"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p18334396"><a name="p18334396"></a><a name="p18334396"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row55991032"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p38979707"><a name="p38979707"></a><a name="p38979707"></a>ikepolicy</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p3239736"><a name="p3239736"></a><a name="p3239736"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p49509242"><a name="p49509242"></a><a name="p49509242"></a>Specifies the IKE policy object.</p>
</td>
</tr>
<tr id="row2405037"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p60590285"><a name="p60590285"></a><a name="p60590285"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p8866062"><a name="p8866062"></a><a name="p8866062"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p53959953"><a name="p53959953"></a><a name="p53959953"></a>Specifies the lifetime value of the SA. The default unit is <strong id="b842352706101729"><a name="b842352706101729"></a><a name="b842352706101729"></a>seconds</strong>. The default value is <strong id="b842352706101736"><a name="b842352706101736"></a><a name="b842352706101736"></a>3600</strong>.</p>
</td>
</tr>
<tr id="row15877536"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p11012038"><a name="p11012038"></a><a name="p11012038"></a>units</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p19559856"><a name="p19559856"></a><a name="p19559856"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p20069106"><a name="p20069106"></a><a name="p20069106"></a>Specifies the lifetime unit of the SA. The default unit is <strong id="b842352706101812"><a name="b842352706101812"></a><a name="b842352706101812"></a>seconds</strong>. The default value is <strong id="b842352706101817"><a name="b842352706101817"></a><a name="b842352706101817"></a>3600</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section10594405"></a>

-   Example Request

    ```
    {
      "ikepolicy" : {
        "encryption_algorithm" : "aes-256"
      }
    }
    ```


-   Example Response

    ```
    {
      "ikepolicy" : {
        "name" : "ikepolicy1",
        "tenant_id" : "ccb81365fe36411a9011e90491fe1330",
        "auth_algorithm" : "sha1",
        "encryption_algorithm" : "aes-256",
        "pfs" : "group5",
        "phase1_negotiation_mode" : "main",
        "lifetime" : {
          "units" : "seconds",
          "value" : 3600
        },
        "ike_version" : "v1",
        "id" : "5522aff7-1b3c-48dd-9c3c-b50f016b73db",
        "description" : ""
      }
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

