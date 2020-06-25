# Creating an IKE Policy<a name="en_topic_0093011510"></a>

## **Function**<a name="section1108643"></a>

This interface is used to create an IKE policy.

## URI<a name="section9977790"></a>

POST /v2.0/vpn/ikepolicies

## Request Message<a name="section2894687"></a>

[Table 1](#table59280891)  describes the request parameters.

**Table  1**  Request parameters

<a name="table59280891"></a>
<table><thead align="left"><tr id="row23389273"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p15482964"><a name="p15482964"></a><a name="p15482964"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p46160547"><a name="p46160547"></a><a name="p46160547"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p48016815"><a name="p48016815"></a><a name="p48016815"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p64156767"><a name="p64156767"></a><a name="p64156767"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row29315611"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p25754316"><a name="p25754316"></a><a name="p25754316"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p5724890"><a name="p5724890"></a><a name="p5724890"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p61062956"><a name="p61062956"></a><a name="p61062956"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p47152427"><a name="p47152427"></a><a name="p47152427"></a>Specifies the IKE policy name.</p>
</td>
</tr>
<tr id="row21718662"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p14381235"><a name="p14381235"></a><a name="p14381235"></a>auth_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p24029376"><a name="p24029376"></a><a name="p24029376"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p222421"><a name="p222421"></a><a name="p222421"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p18016155"><a name="p18016155"></a><a name="p18016155"></a>Specifies the authentication hash algorithm. The value can be <strong id="b842352706165820"><a name="b842352706165820"></a><a name="b842352706165820"></a>md5</strong>, <strong id="b842352706165823"><a name="b842352706165823"></a><a name="b842352706165823"></a>sha1</strong>, <strong id="b842352706165833"><a name="b842352706165833"></a><a name="b842352706165833"></a>sha2-256</strong>, <strong id="b842352706165840"><a name="b842352706165840"></a><a name="b842352706165840"></a>sha2-384</strong>, or <strong id="b842352706165851"><a name="b842352706165851"></a><a name="b842352706165851"></a>sha2-512</strong>.</p>
</td>
</tr>
<tr id="row27927672"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p47548937"><a name="p47548937"></a><a name="p47548937"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p26258720"><a name="p26258720"></a><a name="p26258720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p46581538"><a name="p46581538"></a><a name="p46581538"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p15008249"><a name="p15008249"></a><a name="p15008249"></a>Provides supplementary information about the IKE policy.</p>
</td>
</tr>
<tr id="row856520"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p2269305"><a name="p2269305"></a><a name="p2269305"></a>encryption_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p49596018"><a name="p49596018"></a><a name="p49596018"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p57854556"><a name="p57854556"></a><a name="p57854556"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p55707487"><a name="p55707487"></a><a name="p55707487"></a>Specifies the encryption algorithm. The value can be <strong id="b8423527061721"><a name="b8423527061721"></a><a name="b8423527061721"></a>3des</strong>, <strong id="b84235270617211"><a name="b84235270617211"></a><a name="b84235270617211"></a>aes-128</strong>, <strong id="b84235270617219"><a name="b84235270617219"></a><a name="b84235270617219"></a>aes-192</strong>, or <strong id="b84235270617227"><a name="b84235270617227"></a><a name="b84235270617227"></a>aes-256</strong>. The default value is <strong id="b84235270617239"><a name="b84235270617239"></a><a name="b84235270617239"></a>aes-128</strong>.</p>
</td>
</tr>
<tr id="row31605337"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p9895475"><a name="p9895475"></a><a name="p9895475"></a>ike_version</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p63335993"><a name="p63335993"></a><a name="p63335993"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p29941845"><a name="p29941845"></a><a name="p29941845"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p9370348"><a name="p9370348"></a><a name="p9370348"></a>Specifies the IKE version. The value can be <strong id="b842352706212526"><a name="b842352706212526"></a><a name="b842352706212526"></a>v1</strong> or <strong id="b842352706212529"><a name="b842352706212529"></a><a name="b842352706212529"></a>v2</strong>. The default value is <strong id="b842352706212533"><a name="b842352706212533"></a><a name="b842352706212533"></a>v1</strong>.</p>
</td>
</tr>
<tr id="row17224274"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p52988976"><a name="p52988976"></a><a name="p52988976"></a>lifetime</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p64248638"><a name="p64248638"></a><a name="p64248638"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p36757156"><a name="p36757156"></a><a name="p36757156"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p24539659"><a name="p24539659"></a><a name="p24539659"></a>Specifies the lifetime object of SA.</p>
</td>
</tr>
<tr id="row19530342"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p38453873"><a name="p38453873"></a><a name="p38453873"></a>pfs</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p27755984"><a name="p27755984"></a><a name="p27755984"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p33642220"><a name="p33642220"></a><a name="p33642220"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p6588145672511"><a name="p6588145672511"></a><a name="p6588145672511"></a>Specifies the PFS. The value can be <strong id="b85524134353"><a name="b85524134353"></a><a name="b85524134353"></a>group1</strong>, <strong id="b65521130351"><a name="b65521130351"></a><a name="b65521130351"></a>group2</strong>, <strong id="b6553713133512"><a name="b6553713133512"></a><a name="b6553713133512"></a>group5</strong>, <strong id="b1355351353518"><a name="b1355351353518"></a><a name="b1355351353518"></a>group14</strong>, <strong id="b16553111311357"><a name="b16553111311357"></a><a name="b16553111311357"></a>group15</strong>, <strong id="b6553613103510"><a name="b6553613103510"></a><a name="b6553613103510"></a>group16</strong>, <strong id="b11553181314358"><a name="b11553181314358"></a><a name="b11553181314358"></a>group19</strong>, <strong id="b05551313173510"><a name="b05551313173510"></a><a name="b05551313173510"></a>group20</strong>, <strong id="b55551313163511"><a name="b55551313163511"></a><a name="b55551313163511"></a>group21</strong>, or <strong id="b5555113143514"><a name="b5555113143514"></a><a name="b5555113143514"></a>disable</strong>.</p>
<p id="p489023122614"><a name="p489023122614"></a><a name="p489023122614"></a>The default value is <strong id="b769615123514"><a name="b769615123514"></a><a name="b769615123514"></a>group5</strong>.</p>
</td>
</tr>
<tr id="row30443021"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49965631"><a name="p49965631"></a><a name="p49965631"></a>phase1_negotiation_mode</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p20684297"><a name="p20684297"></a><a name="p20684297"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p64815380"><a name="p64815380"></a><a name="p64815380"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p15554440"><a name="p15554440"></a><a name="p15554440"></a>Specifies the IKE mode The default value is <strong id="b842352706213613"><a name="b842352706213613"></a><a name="b842352706213613"></a>main</strong>.</p>
</td>
</tr>
<tr id="row5772232"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p64897643"><a name="p64897643"></a><a name="p64897643"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p22217739"><a name="p22217739"></a><a name="p22217739"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p54806415"><a name="p54806415"></a><a name="p54806415"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p10134624"><a name="p10134624"></a><a name="p10134624"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row24102752"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p6165902"><a name="p6165902"></a><a name="p6165902"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p29676093"><a name="p29676093"></a><a name="p29676093"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p54953365"><a name="p54953365"></a><a name="p54953365"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p22037565"><a name="p22037565"></a><a name="p22037565"></a>Specifies the lifetime value of the SA. The default unit is <strong id="b84235270610146"><a name="b84235270610146"></a><a name="b84235270610146"></a>seconds</strong>. The default value is <strong id="b84235270610149"><a name="b84235270610149"></a><a name="b84235270610149"></a>3600</strong>.</p>
</td>
</tr>
<tr id="row64120358"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p26366538"><a name="p26366538"></a><a name="p26366538"></a>units</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p55314834"><a name="p55314834"></a><a name="p55314834"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p51316583"><a name="p51316583"></a><a name="p51316583"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p63002544"><a name="p63002544"></a><a name="p63002544"></a>Specifies the lifecycle unit. The default value is <strong id="b84235270610658"><a name="b84235270610658"></a><a name="b84235270610658"></a>seconds</strong>.</p>
</td>
</tr>
<tr id="row5607849"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p51582645"><a name="p51582645"></a><a name="p51582645"></a>ikepolicy</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p17444750"><a name="p17444750"></a><a name="p17444750"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p3738651"><a name="p3738651"></a><a name="p3738651"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p34395333"><a name="p34395333"></a><a name="p34395333"></a>Specifies the IKE policy object.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>1.  The  **project\_id**  parameter is not supported.  
>2.  The value of  **tenant\_id**  can contain a maximum of 255 characters.  
>3.  The value of  **name**  can contain 1 to 64 characters.  
>4.  The value of  **description**  can contain a maximum of 255 characters.  
>5.  The value of  **auth\_algorithm**  can only be  **md5**,  **sha1**,  **sha2-256**,  **sha2-384**, or  **sha2-512**.  
>6.  The value of  **encryption\_algorithm**  can only be  **3des**,  **aes-128**,  **aes-192**, or  **aes-256**.  
>7.  The value of  **phase1\_negotiation\_mode**  can only be  **main**  and  **aggressive**.  
>8.  The value of  **units**  can only be in seconds.  
>9.  The value of  **value**  can only be an integer ranging from 60 to 604,800.  
>10. The value of  **ike\_version**  can only be  **v1**  or  **v2**.  

## Response Message<a name="section26052191"></a>

[Table 2](#table34558579)  describes the response parameters.

**Table  2**  Response parameters

<a name="table34558579"></a>
<table><thead align="left"><tr id="row60007281"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p28751554"><a name="p28751554"></a><a name="p28751554"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18331773"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="_Hlk477540336"><a name="_Hlk477540336"></a><a name="_Hlk477540336"></a>auth_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p15678685"><a name="p15678685"></a><a name="p15678685"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p57075007"><a name="p57075007"></a><a name="p57075007"></a>Specifies the authentication hash algorithm. The value can be <strong id="b1689083915"><a name="b1689083915"></a><a name="b1689083915"></a>md5</strong>, <strong id="b1735216430"><a name="b1735216430"></a><a name="b1735216430"></a>sha1</strong>, <strong id="b1435088847"><a name="b1435088847"></a><a name="b1435088847"></a>sha2-256</strong>, <strong id="b1322707641"><a name="b1322707641"></a><a name="b1322707641"></a>sha2-384</strong>, or <strong id="b531797142"><a name="b531797142"></a><a name="b531797142"></a>sha2-512</strong>.</p>
</td>
</tr>
<tr id="row43913021"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p184914"><a name="p184914"></a><a name="p184914"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p14978051"><a name="p14978051"></a><a name="p14978051"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p23621468"><a name="p23621468"></a><a name="p23621468"></a>Provides supplementary information about the IKE policy.</p>
</td>
</tr>
<tr id="row11266626"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p40181490"><a name="p40181490"></a><a name="p40181490"></a>encryption_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p33475267"><a name="p33475267"></a><a name="p33475267"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p51027174"><a name="p51027174"></a><a name="p51027174"></a>Specifies the encryption algorithm. The value can be <strong id="b807489213"><a name="b807489213"></a><a name="b807489213"></a>3des</strong>, <strong id="b2057029087"><a name="b2057029087"></a><a name="b2057029087"></a>aes-128</strong>, <strong id="b101339829"><a name="b101339829"></a><a name="b101339829"></a>aes-192</strong>, or <strong id="b306520159"><a name="b306520159"></a><a name="b306520159"></a>aes-256</strong>. The default value is <strong id="b1074746446"><a name="b1074746446"></a><a name="b1074746446"></a>aes-128</strong>.</p>
</td>
</tr>
<tr id="row56591389"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p20499795"><a name="p20499795"></a><a name="p20499795"></a>lifetime</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p49870669"><a name="p49870669"></a><a name="p49870669"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45749167"><a name="p45749167"></a><a name="p45749167"></a>Specifies the lifetime object of SA.</p>
</td>
</tr>
<tr id="row9089319"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p65146268"><a name="p65146268"></a><a name="p65146268"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p42356378"><a name="p42356378"></a><a name="p42356378"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p2391374"><a name="p2391374"></a><a name="p2391374"></a>Specifies the IKE policy name.</p>
</td>
</tr>
<tr id="row21522370"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p65590400"><a name="p65590400"></a><a name="p65590400"></a>pfs</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p11222187"><a name="p11222187"></a><a name="p11222187"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1581194113275"><a name="p1581194113275"></a><a name="p1581194113275"></a>Specifies the PFS. The value can be <strong id="b21116168356"><a name="b21116168356"></a><a name="b21116168356"></a>group1</strong>, <strong id="b411215162358"><a name="b411215162358"></a><a name="b411215162358"></a>group2</strong>, <strong id="b1711221633514"><a name="b1711221633514"></a><a name="b1711221633514"></a>group5</strong>, <strong id="b1911411673510"><a name="b1911411673510"></a><a name="b1911411673510"></a>group14</strong>, <strong id="b51148165354"><a name="b51148165354"></a><a name="b51148165354"></a>group15</strong>, <strong id="b1111511166357"><a name="b1111511166357"></a><a name="b1111511166357"></a>group16</strong>, <strong id="b7115141623520"><a name="b7115141623520"></a><a name="b7115141623520"></a>group19</strong>, <strong id="b131165162352"><a name="b131165162352"></a><a name="b131165162352"></a>group20</strong>, <strong id="b511614167351"><a name="b511614167351"></a><a name="b511614167351"></a>group21</strong>, or <strong id="b10116141643514"><a name="b10116141643514"></a><a name="b10116141643514"></a>disable</strong>.</p>
<p id="p38111841102710"><a name="p38111841102710"></a><a name="p38111841102710"></a>The default value is <strong id="b16151121715354"><a name="b16151121715354"></a><a name="b16151121715354"></a>group5</strong>.</p>
</td>
</tr>
<tr id="row26008214"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p26290551"><a name="p26290551"></a><a name="p26290551"></a>phase1_negotiation_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p49159881"><a name="p49159881"></a><a name="p49159881"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p12781022"><a name="p12781022"></a><a name="p12781022"></a>Specifies the IKE mode The default value is <strong id="b1067143855"><a name="b1067143855"></a><a name="b1067143855"></a>main</strong>.</p>
</td>
</tr>
<tr id="row47920339"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p56342274"><a name="p56342274"></a><a name="p56342274"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p321477"><a name="p321477"></a><a name="p321477"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p28839721"><a name="p28839721"></a><a name="p28839721"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row58230900"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p19082474"><a name="p19082474"></a><a name="p19082474"></a>ikepolicy</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p2176568"><a name="p2176568"></a><a name="p2176568"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p53389951"><a name="p53389951"></a><a name="p53389951"></a>Specifies the IKE policy object.</p>
</td>
</tr>
<tr id="row24598620"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p46331171"><a name="p46331171"></a><a name="p46331171"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p61837391"><a name="p61837391"></a><a name="p61837391"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p42045429"><a name="p42045429"></a><a name="p42045429"></a>Specifies the lifetime value of the SA. The default unit is <strong id="b842352706101517"><a name="b842352706101517"></a><a name="b842352706101517"></a>seconds</strong>. The default value is <strong id="b842352706101522"><a name="b842352706101522"></a><a name="b842352706101522"></a>3600</strong>.</p>
</td>
</tr>
<tr id="row42864547"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p49476282"><a name="p49476282"></a><a name="p49476282"></a>units</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p48155897"><a name="p48155897"></a><a name="p48155897"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p2313746"><a name="p2313746"></a><a name="p2313746"></a>Specifies the lifecycle unit. The default value is <strong id="b8423527061079"><a name="b8423527061079"></a><a name="b8423527061079"></a>seconds</strong>.</p>
</td>
</tr>
<tr id="row20823715"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p8999315"><a name="p8999315"></a><a name="p8999315"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p57855887"><a name="p57855887"></a><a name="p57855887"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p24745166"><a name="p24745166"></a><a name="p24745166"></a>Specifies the IKE policy ID.</p>
</td>
</tr>
<tr id="row21379907"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p54050919"><a name="p54050919"></a><a name="p54050919"></a>ike_version</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p16048282"><a name="p16048282"></a><a name="p16048282"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p66085716"><a name="p66085716"></a><a name="p66085716"></a>Specifies the IKE version. The value can be <strong id="b2123880768213834"><a name="b2123880768213834"></a><a name="b2123880768213834"></a>v1</strong> or <strong id="b499525058213834"><a name="b499525058213834"></a><a name="b499525058213834"></a>v2</strong>. The default value is <strong id="b842352706213844"><a name="b842352706213844"></a><a name="b842352706213844"></a>v1</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section33143133"></a>

-   Example Request

    ```
    POST /v2.0/vpn/ikepolicies
    {
      "ikepolicy" : {
        "phase1_negotiation_mode" : "main",
        "auth_algorithm" : "sha1",
        "encryption_algorithm" : "aes-128",
        "pfs" : "group5",
        "lifetime" : {
          "units" : "seconds",
          "value" : 7200
        },
        "ike_version" : "v1",
        "name" : "ikepolicy1"
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
        "encryption_algorithm" : "aes-128",
        "pfs" : "group5",
        "phase1_negotiation_mode" : "main",
        "lifetime" : {
          "units" : "seconds",
          "value" : 7200
        },
        "ike_version" : "v1",
        "id" : "5522aff7-1b3c-48dd-9c3c-b50f016b73db",
        "description" : ""
      }
    }
    ```


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

