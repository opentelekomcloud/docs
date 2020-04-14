# Querying a Policy<a name="EN-US_TOPIC_0193631142"></a>

## Function Description<a name="section15319872"></a>

This API is used to query details about a policy.

## URI<a name="section3661125"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/policy/\{policy\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table50793543"></a>
    <table><thead align="left"><tr id="row57499042"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p26910830"><a name="p26910830"></a><a name="p26910830"></a><strong id="b167314917478"><a name="b167314917478"></a><a name="b167314917478"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p32293618"><a name="p32293618"></a><a name="p32293618"></a><strong id="b10590161516460"><a name="b10590161516460"></a><a name="b10590161516460"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p65646295"><a name="p65646295"></a><a name="p65646295"></a><strong id="b1864101284716"><a name="b1864101284716"></a><a name="b1864101284716"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p15749701"><a name="p15749701"></a><a name="p15749701"></a><strong id="b3626141224714"><a name="b3626141224714"></a><a name="b3626141224714"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row657379"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p53247705"><a name="p53247705"></a><a name="p53247705"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p18096848"><a name="p18096848"></a><a name="p18096848"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p56558575"><a name="p56558575"></a><a name="p56558575"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p17841887"><a name="p17841887"></a><a name="p17841887"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row26359261"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p54725385"><a name="p54725385"></a><a name="p54725385"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p3571161"><a name="p3571161"></a><a name="p3571161"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p20828597"><a name="p20828597"></a><a name="p20828597"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p9394822"><a name="p9394822"></a><a name="p9394822"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section32950126"></a>

Request parameters

None

## Response<a name="section28115686"></a>

Response parameters

**Table  2**  Parameter description

<a name="table28850501"></a>
<table><thead align="left"><tr id="row44286268"><th class="cellrowborder" valign="top" width="24.3975602439756%" id="mcps1.2.4.1.1"><p id="p30417949"><a name="p30417949"></a><a name="p30417949"></a><strong id="b938353804716"><a name="b938353804716"></a><a name="b938353804716"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35.80641935806419%" id="mcps1.2.4.1.2"><p id="p47934770"><a name="p47934770"></a><a name="p47934770"></a><strong id="b1486203914474"><a name="b1486203914474"></a><a name="b1486203914474"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p57511139"><a name="p57511139"></a><a name="p57511139"></a><strong id="b55551739114716"><a name="b55551739114716"></a><a name="b55551739114716"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row191871841133512"><td class="cellrowborder" valign="top" width="24.3975602439756%" headers="mcps1.2.4.1.1 "><p id="p1718764153519"><a name="p1718764153519"></a><a name="p1718764153519"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="35.80641935806419%" headers="mcps1.2.4.1.2 "><p id="p21871641133513"><a name="p21871641133513"></a><a name="p21871641133513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p2187541103515"><a name="p2187541103515"></a><a name="p2187541103515"></a>Specifies the instance ID.</p>
</td>
</tr>
<tr id="row11851038203520"><td class="cellrowborder" valign="top" width="24.3975602439756%" headers="mcps1.2.4.1.1 "><p id="p151851738183511"><a name="p151851738183511"></a><a name="p151851738183511"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="35.80641935806419%" headers="mcps1.2.4.1.2 "><p id="p12185193812359"><a name="p12185193812359"></a><a name="p12185193812359"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p6185203816357"><a name="p6185203816357"></a><a name="p6185203816357"></a>Specifies the policy name.</p>
</td>
</tr>
<tr id="row47838210"><td class="cellrowborder" valign="top" width="24.3975602439756%" headers="mcps1.2.4.1.1 "><p id="p49689834"><a name="p49689834"></a><a name="p49689834"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="35.80641935806419%" headers="mcps1.2.4.1.2 "><p id="p65453602"><a name="p65453602"></a><a name="p65453602"></a><a href="#table1231716412312">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p141522"><a name="p141522"></a><a name="p141522"></a>Specifies the protective action after a rule is matched.</p>
<a name="ul796714441001"></a><a name="ul796714441001"></a><ul id="ul796714441001"><li><span class="parmvalue" id="parmvalue1312794717267"><a name="parmvalue1312794717267"></a><a name="parmvalue1312794717267"></a><b>block</b></span>: block and log detected attacks.</li><li><span class="parmvalue" id="parmvalue919319241583"><a name="parmvalue919319241583"></a><a name="parmvalue919319241583"></a><b>log</b></span>: only log detected attacks.</li></ul>
</td>
</tr>
<tr id="row12946355"><td class="cellrowborder" valign="top" width="24.3975602439756%" headers="mcps1.2.4.1.1 "><p id="p42021858"><a name="p42021858"></a><a name="p42021858"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="35.80641935806419%" headers="mcps1.2.4.1.2 "><p id="p48327333"><a name="p48327333"></a><a name="p48327333"></a><a href="#table1272813819259">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p22199909"><a name="p22199909"></a><a name="p22199909"></a>Specifies the protection switches.</p>
</td>
</tr>
<tr id="row50045227"><td class="cellrowborder" valign="top" width="24.3975602439756%" headers="mcps1.2.4.1.1 "><p id="p27131597"><a name="p27131597"></a><a name="p27131597"></a>level</p>
</td>
<td class="cellrowborder" valign="top" width="35.80641935806419%" headers="mcps1.2.4.1.2 "><p id="p50175772"><a name="p50175772"></a><a name="p50175772"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p8528528245"><a name="p8528528245"></a><a name="p8528528245"></a>Specifies the protection level.</p>
<a name="ul14533143918414"></a><a name="ul14533143918414"></a><ul id="ul14533143918414"><li><span class="parmvalue" id="parmvalue184661522103015"><a name="parmvalue184661522103015"></a><a name="parmvalue184661522103015"></a><b>1</b></span>: low</li><li><span class="parmvalue" id="parmvalue7311102603010"><a name="parmvalue7311102603010"></a><a name="parmvalue7311102603010"></a><b>2</b></span>: medium</li><li><span class="parmvalue" id="parmvalue8927429103012"><a name="parmvalue8927429103012"></a><a name="parmvalue8927429103012"></a><b>3</b></span>: high</li></ul>
</td>
</tr>
<tr id="row3807228"><td class="cellrowborder" valign="top" width="24.3975602439756%" headers="mcps1.2.4.1.1 "><p id="p39950041"><a name="p39950041"></a><a name="p39950041"></a>full_detection</p>
</td>
<td class="cellrowborder" valign="top" width="35.80641935806419%" headers="mcps1.2.4.1.2 "><p id="p14727870"><a name="p14727870"></a><a name="p14727870"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p68421843104420"><a name="p68421843104420"></a><a name="p68421843104420"></a>Specifies the detection mode in Precise Protection.</p>
<a name="ul02880554511"></a><a name="ul02880554511"></a><ul id="ul02880554511"><li><strong id="en-us_topic_0193631159_b1755019491619"><a name="en-us_topic_0193631159_b1755019491619"></a><a name="en-us_topic_0193631159_b1755019491619"></a>true</strong>: full detection. Full detection finishes all threat detections before blocking requests that meet Precise Protection specified conditions.</li><li><strong id="en-us_topic_0193631159_b17686122792016"><a name="en-us_topic_0193631159_b17686122792016"></a><a name="en-us_topic_0193631159_b17686122792016"></a>false</strong>: instant detection. Instant detection immediately ends threat detection after blocking a request that meets Precise Protection specified conditions.</li></ul>
</td>
</tr>
<tr id="row66308345"><td class="cellrowborder" valign="top" width="24.3975602439756%" headers="mcps1.2.4.1.1 "><p id="p2266842"><a name="p2266842"></a><a name="p2266842"></a>hosts</p>
</td>
<td class="cellrowborder" valign="top" width="35.80641935806419%" headers="mcps1.2.4.1.2 "><p id="p49396545"><a name="p49396545"></a><a name="p49396545"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p41697171"><a name="p41697171"></a><a name="p41697171"></a>Specifies the domain IDs.</p>
</td>
</tr>
<tr id="row39730225"><td class="cellrowborder" valign="top" width="24.3975602439756%" headers="mcps1.2.4.1.1 "><p id="p64031633"><a name="p64031633"></a><a name="p64031633"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="35.80641935806419%" headers="mcps1.2.4.1.2 "><p id="p19179794"><a name="p19179794"></a><a name="p19179794"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p10059483"><a name="p10059483"></a><a name="p10059483"></a>Specifies the time when a policy is created.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **action**

<a name="table1231716412312"></a>
<table><thead align="left"><tr id="row153241848236"><th class="cellrowborder" valign="top" width="25.407459254074595%" id="mcps1.2.4.1.1"><p id="p1532615432319"><a name="p1532615432319"></a><a name="p1532615432319"></a><strong id="b1603906441"><a name="b1603906441"></a><a name="b1603906441"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34.796520347965206%" id="mcps1.2.4.1.2"><p id="p333054192311"><a name="p333054192311"></a><a name="p333054192311"></a><strong id="b1626761878"><a name="b1626761878"></a><a name="b1626761878"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p193322492311"><a name="p193322492311"></a><a name="p193322492311"></a><strong id="b2045989521"><a name="b2045989521"></a><a name="b2045989521"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19763216142319"><td class="cellrowborder" valign="top" width="25.407459254074595%" headers="mcps1.2.4.1.1 "><p id="p1576317163239"><a name="p1576317163239"></a><a name="p1576317163239"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="34.796520347965206%" headers="mcps1.2.4.1.2 "><p id="p117631516182318"><a name="p117631516182318"></a><a name="p117631516182318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p676312167234"><a name="p676312167234"></a><a name="p676312167234"></a>Specifies the protective action.</p>
<a name="ul1392521423713"></a><a name="ul1392521423713"></a><ul id="ul1392521423713"><li><span class="parmvalue" id="parmvalue438075817288"><a name="parmvalue438075817288"></a><a name="parmvalue438075817288"></a><b>block</b></span>: WAF blocks and logs detected attacks.</li><li><span class="parmvalue" id="parmvalue224561115327"><a name="parmvalue224561115327"></a><a name="parmvalue224561115327"></a><b>log</b></span>: WAF logs detected attacks only.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  4** **options**

<a name="table1272813819259"></a>
<table><thead align="left"><tr id="row14733082258"><th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.1"><p id="p873817812512"><a name="p873817812512"></a><a name="p873817812512"></a><strong id="b1428562748"><a name="b1428562748"></a><a name="b1428562748"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.2"><p id="p137404817256"><a name="p137404817256"></a><a name="p137404817256"></a><strong id="b1784827860"><a name="b1784827860"></a><a name="b1784827860"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p6742198152512"><a name="p6742198152512"></a><a name="p6742198152512"></a><strong id="b965611029"><a name="b965611029"></a><a name="b965611029"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1177747172812"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p33504133"><a name="p33504133"></a><a name="p33504133"></a>webattack</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p29480242"><a name="p29480242"></a><a name="p29480242"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p2415193218263"><a name="p2415193218263"></a><a name="p2415193218263"></a>Specifies whether Basic Web Protection is enabled.</p>
<a name="ul1778444132612"></a><a name="ul1778444132612"></a><ul id="ul1778444132612"><li><strong id="b2400155093115"><a name="b2400155093115"></a><a name="b2400155093115"></a>true</strong>: enabled.</li><li><strong id="b936485615312"><a name="b936485615312"></a><a name="b936485615312"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1577720732819"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p42476939"><a name="p42476939"></a><a name="p42476939"></a>common</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p18080074"><a name="p18080074"></a><a name="p18080074"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p8672433268"><a name="p8672433268"></a><a name="p8672433268"></a>Specifies whether General Check in Basic Web Protection is enabled.</p>
<a name="ul4842171218268"></a><a name="ul4842171218268"></a><ul id="ul4842171218268"><li><strong id="b846711493217"><a name="b846711493217"></a><a name="b846711493217"></a>true</strong>: enabled.</li><li><strong id="b09811697321"><a name="b09811697321"></a><a name="b09811697321"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row8777157112811"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p47260058"><a name="p47260058"></a><a name="p47260058"></a>crawler</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p2859499"><a name="p2859499"></a><a name="p2859499"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p825744922615"><a name="p825744922615"></a><a name="p825744922615"></a>Specifies whether the master crawler detection switch in Basic Web Protection is enabled.</p>
<a name="ul2993535262"></a><a name="ul2993535262"></a><ul id="ul2993535262"><li><strong id="b6200201818328"><a name="b6200201818328"></a><a name="b6200201818328"></a>true</strong>: enabled.</li><li><strong id="b1077992123215"><a name="b1077992123215"></a><a name="b1077992123215"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1177515762814"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p42166705"><a name="p42166705"></a><a name="p42166705"></a>crawler_engine</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p60059924"><a name="p60059924"></a><a name="p60059924"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1718417589268"><a name="p1718417589268"></a><a name="p1718417589268"></a>Specifies whether the Search Engine switch in Basic Web Protection is enabled.</p>
<a name="ul172713111276"></a><a name="ul172713111276"></a><ul id="ul172713111276"><li><strong id="b1627815296323"><a name="b1627815296323"></a><a name="b1627815296323"></a>true</strong>: enabled.</li><li><strong id="b126696328326"><a name="b126696328326"></a><a name="b126696328326"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row177751776289"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p55359439"><a name="p55359439"></a><a name="p55359439"></a>crawler_scanner</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p54929604"><a name="p54929604"></a><a name="p54929604"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p20112962"><a name="p20112962"></a><a name="p20112962"></a>Specifies whether the Scanner switch in Basic Web Protection is enabled.</p>
<a name="ul851114810278"></a><a name="ul851114810278"></a><ul id="ul851114810278"><li><strong id="b19895154973215"><a name="b19895154973215"></a><a name="b19895154973215"></a>true</strong>: enabled.</li><li><strong id="b1949353153214"><a name="b1949353153214"></a><a name="b1949353153214"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row177577172811"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p25118198"><a name="p25118198"></a><a name="p25118198"></a>crawler_script</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p21308157"><a name="p21308157"></a><a name="p21308157"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p48239148"><a name="p48239148"></a><a name="p48239148"></a>Specifies whether the Script Tool switch in Basic Web Protection is enabled.</p>
<a name="ul1296981219278"></a><a name="ul1296981219278"></a><ul id="ul1296981219278"><li><strong id="b39783017338"><a name="b39783017338"></a><a name="b39783017338"></a>true</strong>: enabled.</li><li><strong id="b6111174203311"><a name="b6111174203311"></a><a name="b6111174203311"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1773576281"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p11652645"><a name="p11652645"></a><a name="p11652645"></a>crawler_other</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p4340158"><a name="p4340158"></a><a name="p4340158"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p16008479"><a name="p16008479"></a><a name="p16008479"></a>Specifies whether detection of other crawlers in Basic Web Protection is enabled.</p>
<a name="ul8824161782711"></a><a name="ul8824161782711"></a><ul id="ul8824161782711"><li><strong id="b19432191315334"><a name="b19432191315334"></a><a name="b19432191315334"></a>true</strong>: enabled.</li><li><strong id="b455117177338"><a name="b455117177338"></a><a name="b455117177338"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1177357102817"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p6261339"><a name="p6261339"></a><a name="p6261339"></a>webshell</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p37406470"><a name="p37406470"></a><a name="p37406470"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p10025242"><a name="p10025242"></a><a name="p10025242"></a>Specifies whether webshell detection in Basic Web Protection is enabled.</p>
<a name="ul20574202914279"></a><a name="ul20574202914279"></a><ul id="ul20574202914279"><li><strong id="b149031527193313"><a name="b149031527193313"></a><a name="b149031527193313"></a>true</strong>: enabled.</li><li><strong id="b199571730153317"><a name="b199571730153317"></a><a name="b199571730153317"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row47721722816"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p8926362"><a name="p8926362"></a><a name="p8926362"></a>cc</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p51946711"><a name="p51946711"></a><a name="p51946711"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p46934044"><a name="p46934044"></a><a name="p46934044"></a>Specifies whether CC Attack Protection is enabled.</p>
<a name="ul8527033142710"></a><a name="ul8527033142710"></a><ul id="ul8527033142710"><li><strong id="b165911138113318"><a name="b165911138113318"></a><a name="b165911138113318"></a>true</strong>: enabled.</li><li><strong id="b8536134183315"><a name="b8536134183315"></a><a name="b8536134183315"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1977218711283"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p38799072"><a name="p38799072"></a><a name="p38799072"></a>custom</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p55717167"><a name="p55717167"></a><a name="p55717167"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p16796711"><a name="p16796711"></a><a name="p16796711"></a>Specifies whether Precise Protection is enabled.</p>
<a name="ul1043194117270"></a><a name="ul1043194117270"></a><ul id="ul1043194117270"><li><strong id="b17653164912339"><a name="b17653164912339"></a><a name="b17653164912339"></a>true</strong>: enabled.</li><li><strong id="b288885220337"><a name="b288885220337"></a><a name="b288885220337"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row97728782819"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p10468143"><a name="p10468143"></a><a name="p10468143"></a>whiteblackip</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p42613264"><a name="p42613264"></a><a name="p42613264"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p29122361"><a name="p29122361"></a><a name="p29122361"></a>Specifies whether Blacklist and Whitelist is enabled.</p>
<a name="ul1621718455274"></a><a name="ul1621718455274"></a><ul id="ul1621718455274"><li><strong id="b5651140173415"><a name="b5651140173415"></a><a name="b5651140173415"></a>true</strong>: enabled.</li><li><strong id="b1460512318345"><a name="b1460512318345"></a><a name="b1460512318345"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row10772157172818"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p51392996"><a name="p51392996"></a><a name="p51392996"></a>privacy</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p2083177"><a name="p2083177"></a><a name="p2083177"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p34519671"><a name="p34519671"></a><a name="p34519671"></a>Specifies whether Data Masking is enabled.</p>
<a name="ul2712175332710"></a><a name="ul2712175332710"></a><ul id="ul2712175332710"><li><strong id="b796511108344"><a name="b796511108344"></a><a name="b796511108344"></a>true</strong>: enabled.</li><li><strong id="b109481713173419"><a name="b109481713173419"></a><a name="b109481713173419"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row14770678287"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p58255435"><a name="p58255435"></a><a name="p58255435"></a>Ignore</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p21069794"><a name="p21069794"></a><a name="p21069794"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p28931745"><a name="p28931745"></a><a name="p28931745"></a>Specifies whether False Alarm Masking is enabled.</p>
<a name="ul1371357192720"></a><a name="ul1371357192720"></a><ul id="ul1371357192720"><li><strong id="b9722423193416"><a name="b9722423193416"></a><a name="b9722423193416"></a>true</strong>: enabled.</li><li><strong id="b18784123017347"><a name="b18784123017347"></a><a name="b18784123017347"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row167707717287"><td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.1 "><p id="p37316794"><a name="p37316794"></a><a name="p37316794"></a>antitamper</p>
</td>
<td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.2 "><p id="p2761443"><a name="p2761443"></a><a name="p2761443"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p22350292"><a name="p22350292"></a><a name="p22350292"></a>Specifies whether Web Tamper Protection is enabled.</p>
<a name="ul5509133182819"></a><a name="ul5509133182819"></a><ul id="ul5509133182819"><li><strong id="b6387173913349"><a name="b6387173913349"></a><a name="b6387173913349"></a>true</strong>: enabled.</li><li><strong id="b2085513425344"><a name="b2085513425344"></a><a name="b2085513425344"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1904124824012"></a>

A policy named  **policy\_2**  is used as an example.

Response example

```
{
          "id": "xxxxxxxxxxxxxxxxxxxxxxxxx",
          "name": "policy_2",
          "action": {
              "category": "block"
           },
           "options": {
               "webattack": true,
               "common": true,
               "crawler": true,
               "crawler_engine": true,
               "crawler_scanner": true,
               "crawler_script": true,
               "crawler_other": true,
               "webshell": true,
               "cc": true,
               "custom": true,
               "whiteblackip": true,
               "ignore": true,
               "privacy": true,
               "antitamper": true
            },
           "level": 1,
           "full_detection": false,
           "hosts": ["11111111111111111", "2222222222222222222"],
           "timestamp": 1499817612
}
```

## Status Code<a name="section51714589"></a>

[Table 5](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  5**  Status code

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

