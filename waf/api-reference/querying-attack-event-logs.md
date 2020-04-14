# Querying Attack Event Logs<a name="EN-US_TOPIC_0193631150"></a>

## Function Description<a name="section41061312"></a>

This API is used to query attack event logs.

## URI<a name="section34007492"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/event?from=\{from\}&to=\{to\}&hosts=\{hostname\}&attacks=\{attack\}&sips=\{sip\}&offset=\{offset\}&limit=\{limit\}

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >An example of a URI is as follows:  
    >GET  /v1/3ac26c59e15a4a11bb680a103a29ddb6/waf/event/attack/type?from=1543976973635&to=1563976973635&hosts=3211757cafa3437aae24d760022e79ba&hosts=93029844064b43739b51ca63036fbc4b&hosts=34fe5f5c60ef4e43a9975296765d1217  

-   Parameter description

    **Table  1**  Path parameters

    <a name="table62758145"></a>
    <table><thead align="left"><tr id="row33430159"><th class="cellrowborder" valign="top" width="24.447555244475552%" id="mcps1.2.5.1.1"><p id="p23488320"><a name="p23488320"></a><a name="p23488320"></a><strong id="b154011010354"><a name="b154011010354"></a><a name="b154011010354"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.408159184081594%" id="mcps1.2.5.1.2"><p id="p23505762"><a name="p23505762"></a><a name="p23505762"></a><strong id="b15553102193519"><a name="b15553102193519"></a><a name="b15553102193519"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p24918556"><a name="p24918556"></a><a name="p24918556"></a><strong id="b1659484133517"><a name="b1659484133517"></a><a name="b1659484133517"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p5137175"><a name="p5137175"></a><a name="p5137175"></a><strong id="b126918623518"><a name="b126918623518"></a><a name="b126918623518"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13458043"><td class="cellrowborder" valign="top" width="24.447555244475552%" headers="mcps1.2.5.1.1 "><p id="p16359662"><a name="p16359662"></a><a name="p16359662"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.2 "><p id="p50064283"><a name="p50064283"></a><a name="p50064283"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p28675112"><a name="p28675112"></a><a name="p28675112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p40982717"><a name="p40982717"></a><a name="p40982717"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row35495584"><td class="cellrowborder" valign="top" width="24.447555244475552%" headers="mcps1.2.5.1.1 "><p id="p56570032"><a name="p56570032"></a><a name="p56570032"></a>from</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.2 "><p id="p18769889"><a name="p18769889"></a><a name="p18769889"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p43966042"><a name="p43966042"></a><a name="p43966042"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p4479684"><a name="p4479684"></a><a name="p4479684"></a>Specifies the start time (UTC) in milliseconds. For example, <strong id="b67431836173512"><a name="b67431836173512"></a><a name="b67431836173512"></a>1548172800000</strong>.</p>
    </td>
    </tr>
    <tr id="row40317163"><td class="cellrowborder" valign="top" width="24.447555244475552%" headers="mcps1.2.5.1.1 "><p id="p44464769"><a name="p44464769"></a><a name="p44464769"></a>to</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.2 "><p id="p44876507"><a name="p44876507"></a><a name="p44876507"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p11118433"><a name="p11118433"></a><a name="p11118433"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p28177917"><a name="p28177917"></a><a name="p28177917"></a>Specifies the end time (UTC) in milliseconds. For example, <strong id="b12562739173514"><a name="b12562739173514"></a><a name="b12562739173514"></a>1548431999000</strong>.</p>
    </td>
    </tr>
    <tr id="row52274661"><td class="cellrowborder" valign="top" width="24.447555244475552%" headers="mcps1.2.5.1.1 "><p id="p6389178"><a name="p6389178"></a><a name="p6389178"></a>hosts</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.2 "><p id="p47761432"><a name="p47761432"></a><a name="p47761432"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p43470758"><a name="p43470758"></a><a name="p43470758"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p31470476"><a name="p31470476"></a><a name="p31470476"></a>Specifies the domain IDs.</p>
    </td>
    </tr>
    <tr id="row14798832"><td class="cellrowborder" valign="top" width="24.447555244475552%" headers="mcps1.2.5.1.1 "><p id="p57854734"><a name="p57854734"></a><a name="p57854734"></a>attacks</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.2 "><p id="p55721881"><a name="p55721881"></a><a name="p55721881"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p17178488"><a name="p17178488"></a><a name="p17178488"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p49280276"><a name="p49280276"></a><a name="p49280276"></a>Specifies the list of attack types. For example, <strong id="b7498113122210"><a name="b7498113122210"></a><a name="b7498113122210"></a>sqli</strong> and <strong id="b193771534132219"><a name="b193771534132219"></a><a name="b193771534132219"></a>xss</strong>.</p>
    </td>
    </tr>
    <tr id="row40869300"><td class="cellrowborder" valign="top" width="24.447555244475552%" headers="mcps1.2.5.1.1 "><p id="p22078965"><a name="p22078965"></a><a name="p22078965"></a>sips</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.2 "><p id="p43565735"><a name="p43565735"></a><a name="p43565735"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p39163633"><a name="p39163633"></a><a name="p39163633"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p18137724"><a name="p18137724"></a><a name="p18137724"></a>Specifies the attack source IP addresses. For example, <em id="i15533730193410"><a name="i15533730193410"></a><a name="i15533730193410"></a>X.X.</em><strong id="b156111133143413"><a name="b156111133143413"></a><a name="b156111133143413"></a>12.23</strong> and <em id="i1029885783419"><a name="i1029885783419"></a><a name="i1029885783419"></a>X.X.</em><strong id="b42981853153412"><a name="b42981853153412"></a><a name="b42981853153412"></a>20.85</strong>.</p>
    </td>
    </tr>
    <tr id="row5445144516815"><td class="cellrowborder" valign="top" width="24.447555244475552%" headers="mcps1.2.5.1.1 "><p id="p16445845388"><a name="p16445845388"></a><a name="p16445845388"></a>nsips</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.2 "><p id="p204451645381"><a name="p204451645381"></a><a name="p204451645381"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p744544516820"><a name="p744544516820"></a><a name="p744544516820"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p24454451986"><a name="p24454451986"></a><a name="p24454451986"></a>Specifies the excluded attack source IP addresses. For example, <em id="i1284321123511"><a name="i1284321123511"></a><a name="i1284321123511"></a>X.X.</em><strong id="b83415258355"><a name="b83415258355"></a><a name="b83415258355"></a>12.1</strong> and <em id="i9393114015359"><a name="i9393114015359"></a><a name="i9393114015359"></a>X.X.</em><strong id="b17549144319356"><a name="b17549144319356"></a><a name="b17549144319356"></a>20.2</strong>.</p>
    </td>
    </tr>
    <tr id="row25233394"><td class="cellrowborder" valign="top" width="24.447555244475552%" headers="mcps1.2.5.1.1 "><p id="p30639048"><a name="p30639048"></a><a name="p30639048"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.2 "><p id="p65843830"><a name="p65843830"></a><a name="p65843830"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p31750053"><a name="p31750053"></a><a name="p31750053"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p21617533"><a name="p21617533"></a><a name="p21617533"></a>Specifies the number of returned pages. Its value ranges from <strong id="b2584046145217"><a name="b2584046145217"></a><a name="b2584046145217"></a>0</strong> to <strong id="b195841146155214"><a name="b195841146155214"></a><a name="b195841146155214"></a>65535</strong>. The default value is <strong id="b158412465528"><a name="b158412465528"></a><a name="b158412465528"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row60340071"><td class="cellrowborder" valign="top" width="24.447555244475552%" headers="mcps1.2.5.1.1 "><p id="p55707598"><a name="p55707598"></a><a name="p55707598"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.2 "><p id="p16021618"><a name="p16021618"></a><a name="p16021618"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p22682682"><a name="p22682682"></a><a name="p22682682"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p25357967"><a name="p25357967"></a><a name="p25357967"></a>Specifies the maximum number of records displayed on each page. Its value ranges from <strong id="b147277816352"><a name="b147277816352"></a><a name="b147277816352"></a>0</strong> to <strong id="b9727148203520"><a name="b9727148203520"></a><a name="b9727148203520"></a>50</strong>. The default value is <strong id="b97276819359"><a name="b97276819359"></a><a name="b97276819359"></a>10</strong>.</p>
    </td>
    </tr>
    <tr id="row137226276511"><td class="cellrowborder" valign="top" width="24.447555244475552%" headers="mcps1.2.5.1.1 "><p id="p127229274514"><a name="p127229274514"></a><a name="p127229274514"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.2 "><p id="p197224276511"><a name="p197224276511"></a><a name="p197224276511"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p17722152714514"><a name="p17722152714514"></a><a name="p17722152714514"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p372219271655"><a name="p372219271655"></a><a name="p372219271655"></a>Specifies the ID of the last event record on the previous page.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section37631980"></a>

Request parameters

None

## Response<a name="section3143504"></a>

Response parameters

**Table  2**  Parameter description

<a name="table65418856"></a>
<table><thead align="left"><tr id="row45644753"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p6237533"><a name="p6237533"></a><a name="p6237533"></a><strong id="b118902290376"><a name="b118902290376"></a><a name="b118902290376"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p35478198"><a name="p35478198"></a><a name="p35478198"></a><strong id="b653418913383"><a name="b653418913383"></a><a name="b653418913383"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p55161795"><a name="p55161795"></a><a name="p55161795"></a><strong id="b911271123819"><a name="b911271123819"></a><a name="b911271123819"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row26694113"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p14739544"><a name="p14739544"></a><a name="p14739544"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p53052407"><a name="p53052407"></a><a name="p53052407"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p2277735"><a name="p2277735"></a><a name="p2277735"></a>Specifies the total number of event logs.</p>
</td>
</tr>
<tr id="row20499621"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p49856593"><a name="p49856593"></a><a name="p49856593"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p11852193"><a name="p11852193"></a><a name="p11852193"></a><a href="#table8472209123418">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p20503549"><a name="p20503549"></a><a name="p20503549"></a>Specifies the event log objects.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **items**

<a name="table8472209123418"></a>
<table><thead align="left"><tr id="row114721298347"><th class="cellrowborder" valign="top" width="34.77347734773477%" id="mcps1.2.4.1.1"><p id="p3540175514347"><a name="p3540175514347"></a><a name="p3540175514347"></a><strong id="b84708559510"><a name="b84708559510"></a><a name="b84708559510"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.69246924692469%" id="mcps1.2.4.1.2"><p id="p15542185543412"><a name="p15542185543412"></a><a name="p15542185543412"></a><strong id="b135873729"><a name="b135873729"></a><a name="b135873729"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.53405340534053%" id="mcps1.2.4.1.3"><p id="p14545555143412"><a name="p14545555143412"></a><a name="p14545555143412"></a><strong id="b11380152015454"><a name="b11380152015454"></a><a name="b11380152015454"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6472994344"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p37701141203417"><a name="p37701141203417"></a><a name="p37701141203417"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p9773164114346"><a name="p9773164114346"></a><a name="p9773164114346"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p977524116342"><a name="p977524116342"></a><a name="p977524116342"></a>Specifies the event ID.</p>
</td>
</tr>
<tr id="row4472094342"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p177910414341"><a name="p177910414341"></a><a name="p177910414341"></a>time</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p15783154113347"><a name="p15783154113347"></a><a name="p15783154113347"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p97851241203416"><a name="p97851241203416"></a><a name="p97851241203416"></a>Specifies the attack time since Unix Epoch in milliseconds.</p>
</td>
</tr>
<tr id="row7473159143415"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p97886412348"><a name="p97886412348"></a><a name="p97886412348"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p87901541173413"><a name="p87901541173413"></a><a name="p87901541173413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p1793174153412"><a name="p1793174153412"></a><a name="p1793174153412"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row94739915343"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p15811181014367"><a name="p15811181014367"></a><a name="p15811181014367"></a>sip</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p1681331010367"><a name="p1681331010367"></a><a name="p1681331010367"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p1181791016366"><a name="p1181791016366"></a><a name="p1181791016366"></a>Specifies an attack source IP address.</p>
</td>
</tr>
<tr id="row1859064418356"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p2821121010365"><a name="p2821121010365"></a><a name="p2821121010365"></a>host</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p1582516104369"><a name="p1582516104369"></a><a name="p1582516104369"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p18829141014361"><a name="p18829141014361"></a><a name="p18829141014361"></a>Specifies an attacked domain name.</p>
</td>
</tr>
<tr id="row978110198718"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p11781319674"><a name="p11781319674"></a><a name="p11781319674"></a>host_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p1978211914713"><a name="p1978211914713"></a><a name="p1978211914713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p7782111915711"><a name="p7782111915711"></a><a name="p7782111915711"></a>Specifies a domain name ID.</p>
</td>
</tr>
<tr id="row742095011354"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p88367106361"><a name="p88367106361"></a><a name="p88367106361"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p208391110153615"><a name="p208391110153615"></a><a name="p208391110153615"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p1984161011369"><a name="p1984161011369"></a><a name="p1984161011369"></a>Specifies the attacked URL, excluding a domain name.</p>
</td>
</tr>
<tr id="row9765105117356"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p1784531053618"><a name="p1784531053618"></a><a name="p1784531053618"></a>attack</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p1684811014367"><a name="p1684811014367"></a><a name="p1684811014367"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p18525107365"><a name="p18525107365"></a><a name="p18525107365"></a>Specifies the attack type.</p>
<a name="ul285317105364"></a><a name="ul285317105364"></a><ul id="ul285317105364"><li><span class="parmvalue" id="parmvalue12108252133310"><a name="parmvalue12108252133310"></a><a name="parmvalue12108252133310"></a><b>cc</b></span> refers to CC attack.</li><li><span class="parmvalue" id="parmvalue7543858183320"><a name="parmvalue7543858183320"></a><a name="parmvalue7543858183320"></a><b>cmdi</b></span> refers to command injection.</li><li><span class="parmvalue" id="parmvalue2155727195117"><a name="parmvalue2155727195117"></a><a name="parmvalue2155727195117"></a><b>custom</b></span> refers to Precise Protection events.</li><li><span class="parmvalue" id="parmvalue1240819181169"><a name="parmvalue1240819181169"></a><a name="parmvalue1240819181169"></a><b>illegal</b></span> refers to invalid requests.</li><li><span class="parmvalue" id="parmvalue6831171813413"><a name="parmvalue6831171813413"></a><a name="parmvalue6831171813413"></a><b>sqli</b></span> refers to SQL injection.</li><li><span class="parmvalue" id="parmvalue1890312258340"><a name="parmvalue1890312258340"></a><a name="parmvalue1890312258340"></a><b>lfi</b></span> refers to local file inclusion.</li><li><strong id="b366411121563"><a name="b366411121563"></a><a name="b366411121563"></a>robot</strong> refers to malicious crawlers.</li><li><span class="parmvalue" id="parmvalue128201348519"><a name="parmvalue128201348519"></a><a name="parmvalue128201348519"></a><b>antitamper</b></span> refers to Web Tamper Protection events.</li><li><span class="parmvalue" id="parmvalue16677105211341"><a name="parmvalue16677105211341"></a><a name="parmvalue16677105211341"></a><b>rfi</b></span> refers to remote file inclusion.</li><li><span class="parmvalue" id="parmvalue4708175873413"><a name="parmvalue4708175873413"></a><a name="parmvalue4708175873413"></a><b>vuln</b></span> refers to other types of attacks.</li><li><span class="parmvalue" id="parmvalue158411665354"><a name="parmvalue158411665354"></a><a name="parmvalue158411665354"></a><b>xss</b></span> refers to XSS attack.</li><li><span class="parmvalue" id="parmvalue9149174020511"><a name="parmvalue9149174020511"></a><a name="parmvalue9149174020511"></a><b>whiteblackip</b></span> refers to Blacklist and Whitelist events.</li><li><span class="parmvalue" id="parmvalue3180202023517"><a name="parmvalue3180202023517"></a><a name="parmvalue3180202023517"></a><b>webshell</b></span> refers to webshells.</li></ul>
</td>
</tr>
<tr id="row3703125223519"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p14931910103612"><a name="p14931910103612"></a><a name="p14931910103612"></a>rule</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p1893451083613"><a name="p1893451083613"></a><a name="p1893451083613"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p29374102363"><a name="p29374102363"></a><a name="p29374102363"></a>Specifies the matched rule ID that consists of six digits.</p>
</td>
</tr>
<tr id="row1557010537353"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p10941610163618"><a name="p10941610163618"></a><a name="p10941610163618"></a>payload</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p159459107364"><a name="p159459107364"></a><a name="p159459107364"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p209484106363"><a name="p209484106363"></a><a name="p209484106363"></a>Specifies the hit load.</p>
</td>
</tr>
<tr id="row5378195483516"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p14952151023611"><a name="p14952151023611"></a><a name="p14952151023611"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p129551510123612"><a name="p129551510123612"></a><a name="p129551510123612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p189576106363"><a name="p189576106363"></a><a name="p189576106363"></a>Specifies the protective action.</p>
<a name="ul69591710163615"></a><a name="ul69591710163615"></a><ul id="ul69591710163615"><li><strong id="b10363317105115"><a name="b10363317105115"></a><a name="b10363317105115"></a>Block</strong>: WAF blocks and logs detected attacks.</li><li><span class="parmvalue" id="parmvalue16793129105115"><a name="parmvalue16793129105115"></a><a name="parmvalue16793129105115"></a><b>Log only</b></span>: WAF logs detected attacks only.</li><li><strong id="b177322101588"><a name="b177322101588"></a><a name="b177322101588"></a>Allow</strong>: WAF allows the requests that meet the specified conditions.</li><li><strong id="b193186146811"><a name="b193186146811"></a><a name="b193186146811"></a>Verification code</strong>: A verification code is displayed when the number of requests reaches the maximum limit in a CC attack protection rule. Upon completing the verification, you are no longer restricted by the maximum number of requests allowed.</li><li><strong id="b122724642416"><a name="b122724642416"></a><a name="b122724642416"></a>Filter</strong>: WAF implements data masking.</li><li><span class="parmvalue" id="parmvalue177251243154914"><a name="parmvalue177251243154914"></a><a name="parmvalue177251243154914"></a><b>Mismatch</b></span>: The cached web page in the WAF engine does not match the original web page.</li></ul>
</td>
</tr>
<tr id="row02185553354"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p997401010364"><a name="p997401010364"></a><a name="p997401010364"></a>payload_location</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p11978161012365"><a name="p11978161012365"></a><a name="p11978161012365"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p2981151015363"><a name="p2981151015363"></a><a name="p2981151015363"></a>Specifies the location in the request packet where the attack occurs. The options are as follows: <strong id="b66997587508"><a name="b66997587508"></a><a name="b66997587508"></a>body</strong>, <strong id="b7916191165113"><a name="b7916191165113"></a><a name="b7916191165113"></a>url</strong>, <strong id="b20890617511"><a name="b20890617511"></a><a name="b20890617511"></a>params</strong>, and <strong id="b12849105517"><a name="b12849105517"></a><a name="b12849105517"></a>header</strong>.</p>
</td>
</tr>
<tr id="row5199115643518"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p20985710123616"><a name="p20985710123616"></a><a name="p20985710123616"></a>request_line</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p179875109364"><a name="p179875109364"></a><a name="p179875109364"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p3989181043619"><a name="p3989181043619"></a><a name="p3989181043619"></a>Specifies the attack request method.</p>
</td>
</tr>
<tr id="row651825713358"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p7993111011362"><a name="p7993111011362"></a><a name="p7993111011362"></a>headers</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p199671063615"><a name="p199671063615"></a><a name="p199671063615"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p10999201063616"><a name="p10999201063616"></a><a name="p10999201063616"></a>Specifies the attack request header.</p>
</td>
</tr>
<tr id="row4192591355"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p1757115367"><a name="p1757115367"></a><a name="p1757115367"></a>cookie</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p19801113362"><a name="p19801113362"></a><a name="p19801113362"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p1211131117365"><a name="p1211131117365"></a><a name="p1211131117365"></a>Specifies the cookie.</p>
</td>
</tr>
<tr id="row188941859133511"><td class="cellrowborder" valign="top" width="34.77347734773477%" headers="mcps1.2.4.1.1 "><p id="p12158117367"><a name="p12158117367"></a><a name="p12158117367"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="24.69246924692469%" headers="mcps1.2.4.1.2 "><p id="p7182011103616"><a name="p7182011103616"></a><a name="p7182011103616"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.2.4.1.3 "><p id="p122121114368"><a name="p122121114368"></a><a name="p122121114368"></a>Specifies the body of an attack request.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section192451843181018"></a>

**total**  with a value of  **2**  is used as an example.

Response example

```
{
  "total": 2,
  "items": [
    {
      "id": "0000-0000-0000-13-56ef71f5745764348192f844658dd144",
      "time": 1499817600,
      "policy_id": "xxx",
      "sip": "X.X.1.1",
      "host": "a.com",
      "host_id": "123",
      "url": "/login",
      "attack": "sqli",
      "rule": "20001",
      "payload": "1 or 1=1",
      "action": "block",
      "payload_location": "params",
      "request_line": "GET / ",
      "headers": {
        "Connection": "keep-alive",
        "User-Agent": "curl"
      },
      "cookie": "sid=123; uid=456",
      "body": "user=admin&pass=abc123"
    },
   {
      "id": "0000-0000-0000-13-56ef71f5745764348192f844658dd144",
      "time": 1499817600,
      "host": "a.com",
      "host_id": "a",
      "policy_id": "xxx",
      "sip": "X.X.1.2",
      "url": "/login",
      "attack": "sqli",
      "rule": "20001",
      "payload": "1 or 1=1",
      "action": "log",
      "payload_location": "params",
      "request_line": "GET / ",
      "headers": {
        "Connection": "keep-alive",
        "User-Agent": "curl"
      },
      "cookie": "sid=123; uid=456",
      "body": "user=admin&pass=abc123"
    }
  ]
}
```

## Status Code<a name="section28291536"></a>

[Table 4](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  4**  Status code

<a name="en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0"></a>
<table><thead align="left"><tr id="en-us_topic_0193631139_r3d6e2f205c444705bdbb9daaac74e575"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="19.41%" id="mcps1.2.4.1.2"><p id="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a>Meaning</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0193631139_rc7b2adc390904a1ba79e303017797786"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="19.41%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a>The request has succeeded.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

