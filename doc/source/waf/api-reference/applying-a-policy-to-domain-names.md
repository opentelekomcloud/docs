# Applying a Policy to Domain Names<a name="EN-US_TOPIC_0193631176"></a>

## Function Description<a name="section53777129"></a>

This API is used to apply a policy to domain names.

## URI<a name="section14232118"></a>

-   URI format

    PUT  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/hosts

-   Parameter description

    **Table  1**  Path parameters

    <a name="table62466949"></a>
    <table><thead align="left"><tr id="row28829553"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p53492480"><a name="p53492480"></a><a name="p53492480"></a><strong id="b624512501175"><a name="b624512501175"></a><a name="b624512501175"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p37923619"><a name="p37923619"></a><a name="p37923619"></a><strong id="b87586468195"><a name="b87586468195"></a><a name="b87586468195"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p51914307"><a name="p51914307"></a><a name="p51914307"></a><strong id="b138226476199"><a name="b138226476199"></a><a name="b138226476199"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p44309319"><a name="p44309319"></a><a name="p44309319"></a><strong id="b13805144831918"><a name="b13805144831918"></a><a name="b13805144831918"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32285080"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p64954653"><a name="p64954653"></a><a name="p64954653"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p26835518"><a name="p26835518"></a><a name="p26835518"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p26193381"><a name="p26193381"></a><a name="p26193381"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p41289079"><a name="p41289079"></a><a name="p41289079"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row36057397"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p34968021"><a name="p34968021"></a><a name="p34968021"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p13837462"><a name="p13837462"></a><a name="p13837462"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p47092639"><a name="p47092639"></a><a name="p47092639"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p56407449"><a name="p56407449"></a><a name="p56407449"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section60980198"></a>

Request parameters

**Table  2**  Parameter description

<a name="table32705923"></a>
<table><thead align="left"><tr id="row51664566"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p24080287"><a name="p24080287"></a><a name="p24080287"></a><strong id="b1819036812"><a name="b1819036812"></a><a name="b1819036812"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p4346192"><a name="p4346192"></a><a name="p4346192"></a><strong id="b1712426265"><a name="b1712426265"></a><a name="b1712426265"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p16497266"><a name="p16497266"></a><a name="p16497266"></a><strong id="b754689166"><a name="b754689166"></a><a name="b754689166"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p61210156"><a name="p61210156"></a><a name="p61210156"></a><strong id="b1174883833"><a name="b1174883833"></a><a name="b1174883833"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row59075623"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p20396171"><a name="p20396171"></a><a name="p20396171"></a>hosts</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p41477118"><a name="p41477118"></a><a name="p41477118"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p4203435"><a name="p4203435"></a><a name="p4203435"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p4933944"><a name="p4933944"></a><a name="p4933944"></a>Specifies the domain IDs.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section11950876"></a>

Response parameters

**Table  3**  Parameter description

<a name="table64914630"></a>
<table><thead align="left"><tr id="row45118507"><th class="cellrowborder" valign="top" width="26.657334266573336%" id="mcps1.2.4.1.1"><p id="p30720454"><a name="p30720454"></a><a name="p30720454"></a><strong id="b629335564915"><a name="b629335564915"></a><a name="b629335564915"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.546645335466444%" id="mcps1.2.4.1.2"><p id="p5328821"><a name="p5328821"></a><a name="p5328821"></a><strong id="b1296555610495"><a name="b1296555610495"></a><a name="b1296555610495"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p28981345"><a name="p28981345"></a><a name="p28981345"></a><strong id="b73002586498"><a name="b73002586498"></a><a name="b73002586498"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row59505513"><td class="cellrowborder" valign="top" width="26.657334266573336%" headers="mcps1.2.4.1.1 "><p id="p55217210"><a name="p55217210"></a><a name="p55217210"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="33.546645335466444%" headers="mcps1.2.4.1.2 "><p id="p43409020"><a name="p43409020"></a><a name="p43409020"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p26469718"><a name="p26469718"></a><a name="p26469718"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row36900876"><td class="cellrowborder" valign="top" width="26.657334266573336%" headers="mcps1.2.4.1.1 "><p id="p36180990"><a name="p36180990"></a><a name="p36180990"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.546645335466444%" headers="mcps1.2.4.1.2 "><p id="p44979101"><a name="p44979101"></a><a name="p44979101"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p19428560"><a name="p19428560"></a><a name="p19428560"></a>Specifies the policy name.</p>
</td>
</tr>
<tr id="row40639317"><td class="cellrowborder" valign="top" width="26.657334266573336%" headers="mcps1.2.4.1.1 "><p id="p3450370"><a name="p3450370"></a><a name="p3450370"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="33.546645335466444%" headers="mcps1.2.4.1.2 "><p id="p11044535"><a name="p11044535"></a><a name="p11044535"></a><a href="#table1231716412312">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p22192157"><a name="p22192157"></a><a name="p22192157"></a>Specifies the protective action after a rule is matched.</p>
<a name="ul796714441001"></a><a name="ul796714441001"></a><ul id="ul796714441001"><li><span class="parmvalue" id="parmvalue153416405295"><a name="parmvalue153416405295"></a><a name="parmvalue153416405295"></a><b>block</b></span>: WAF blocks and logs detected attacks.</li><li><span class="parmvalue" id="parmvalue12873191210349"><a name="parmvalue12873191210349"></a><a name="parmvalue12873191210349"></a><b>log</b></span>: WAF logs detected attacks only.</li></ul>
</td>
</tr>
<tr id="row35894686"><td class="cellrowborder" valign="top" width="26.657334266573336%" headers="mcps1.2.4.1.1 "><p id="p21788414"><a name="p21788414"></a><a name="p21788414"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="33.546645335466444%" headers="mcps1.2.4.1.2 "><p id="p20031082"><a name="p20031082"></a><a name="p20031082"></a><a href="#table1272813819259">Table 5</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p11904971"><a name="p11904971"></a><a name="p11904971"></a>Specifies the protection switches.</p>
</td>
</tr>
<tr id="row66773820"><td class="cellrowborder" valign="top" width="26.657334266573336%" headers="mcps1.2.4.1.1 "><p id="p39970328"><a name="p39970328"></a><a name="p39970328"></a>level</p>
</td>
<td class="cellrowborder" valign="top" width="33.546645335466444%" headers="mcps1.2.4.1.2 "><p id="p16371096"><a name="p16371096"></a><a name="p16371096"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p8528528245"><a name="p8528528245"></a><a name="p8528528245"></a>Specifies the protection level.</p>
<a name="ul14533143918414"></a><a name="ul14533143918414"></a><ul id="ul14533143918414"><li><span class="parmvalue" id="parmvalue9145185104513"><a name="parmvalue9145185104513"></a><a name="parmvalue9145185104513"></a><b>1</b></span>: low</li><li><span class="parmvalue" id="parmvalue2770185614459"><a name="parmvalue2770185614459"></a><a name="parmvalue2770185614459"></a><b>2</b></span>: medium</li><li><span class="parmvalue" id="parmvalue1779365984517"><a name="parmvalue1779365984517"></a><a name="parmvalue1779365984517"></a><b>3</b></span>: high</li></ul>
</td>
</tr>
<tr id="row56260171"><td class="cellrowborder" valign="top" width="26.657334266573336%" headers="mcps1.2.4.1.1 "><p id="p60779989"><a name="p60779989"></a><a name="p60779989"></a>full_detection</p>
</td>
<td class="cellrowborder" valign="top" width="33.546645335466444%" headers="mcps1.2.4.1.2 "><p id="p24232096"><a name="p24232096"></a><a name="p24232096"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p68421843104420"><a name="p68421843104420"></a><a name="p68421843104420"></a>Specifies the detection mode in Precise Protection.</p>
<a name="ul02880554511"></a><a name="ul02880554511"></a><ul id="ul02880554511"><li><strong id="en-us_topic_0193631159_b1755019491619"><a name="en-us_topic_0193631159_b1755019491619"></a><a name="en-us_topic_0193631159_b1755019491619"></a>true</strong>: full detection. Full detection finishes all threat detections before blocking requests that meet Precise Protection specified conditions.</li><li><strong id="en-us_topic_0193631159_b17686122792016"><a name="en-us_topic_0193631159_b17686122792016"></a><a name="en-us_topic_0193631159_b17686122792016"></a>false</strong>: instant detection. Instant detection immediately ends threat detection after blocking a request that meets Precise Protection specified conditions.</li></ul>
</td>
</tr>
<tr id="row15567220"><td class="cellrowborder" valign="top" width="26.657334266573336%" headers="mcps1.2.4.1.1 "><p id="p52985303"><a name="p52985303"></a><a name="p52985303"></a>hosts</p>
</td>
<td class="cellrowborder" valign="top" width="33.546645335466444%" headers="mcps1.2.4.1.2 "><p id="p63951159"><a name="p63951159"></a><a name="p63951159"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p12661371"><a name="p12661371"></a><a name="p12661371"></a>Specifies the domain IDs.</p>
</td>
</tr>
<tr id="row46843478"><td class="cellrowborder" valign="top" width="26.657334266573336%" headers="mcps1.2.4.1.1 "><p id="p36225388"><a name="p36225388"></a><a name="p36225388"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="33.546645335466444%" headers="mcps1.2.4.1.2 "><p id="p48575322"><a name="p48575322"></a><a name="p48575322"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p42287049"><a name="p42287049"></a><a name="p42287049"></a>Specifies the time when a policy is created.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **action**

<a name="table1231716412312"></a>
<table><thead align="left"><tr id="row153241848236"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p1532615432319"><a name="p1532615432319"></a><a name="p1532615432319"></a><strong id="b1242335045"><a name="b1242335045"></a><a name="b1242335045"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p333054192311"><a name="p333054192311"></a><a name="p333054192311"></a><strong id="b606394206"><a name="b606394206"></a><a name="b606394206"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p193322492311"><a name="p193322492311"></a><a name="p193322492311"></a><strong id="b1244499594"><a name="b1244499594"></a><a name="b1244499594"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19763216142319"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1576317163239"><a name="p1576317163239"></a><a name="p1576317163239"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p117631516182318"><a name="p117631516182318"></a><a name="p117631516182318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p676312167234"><a name="p676312167234"></a><a name="p676312167234"></a>Specifies the protective action.</p>
<a name="ul6757153383716"></a><a name="ul6757153383716"></a><ul id="ul6757153383716"><li><span class="parmvalue" id="parmvalue95611462322"><a name="parmvalue95611462322"></a><a name="parmvalue95611462322"></a><b>block</b></span>: block and log detected attacks.</li><li><span class="parmvalue" id="parmvalue7859193618341"><a name="parmvalue7859193618341"></a><a name="parmvalue7859193618341"></a><b>log</b></span>: only log detected attacks.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  5** **options**

<a name="table1272813819259"></a>
<table><thead align="left"><tr id="row14733082258"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p873817812512"><a name="p873817812512"></a><a name="p873817812512"></a><strong id="b82863102"><a name="b82863102"></a><a name="b82863102"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p137404817256"><a name="p137404817256"></a><a name="p137404817256"></a><strong id="b1425684832"><a name="b1425684832"></a><a name="b1425684832"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p6742198152512"><a name="p6742198152512"></a><a name="p6742198152512"></a><strong id="b597130664"><a name="b597130664"></a><a name="b597130664"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1177747172812"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p33504133"><a name="p33504133"></a><a name="p33504133"></a>webattack</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p29480242"><a name="p29480242"></a><a name="p29480242"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p2415193218263"><a name="p2415193218263"></a><a name="p2415193218263"></a>Specifies whether Basic Web Protection is enabled.</p>
<a name="ul1778444132612"></a><a name="ul1778444132612"></a><ul id="ul1778444132612"><li><strong id="b0688110134713"><a name="b0688110134713"></a><a name="b0688110134713"></a>true</strong>: enabled.</li><li><strong id="b1732894114718"><a name="b1732894114718"></a><a name="b1732894114718"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1577720732819"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p42476939"><a name="p42476939"></a><a name="p42476939"></a>common</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p18080074"><a name="p18080074"></a><a name="p18080074"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p8672433268"><a name="p8672433268"></a><a name="p8672433268"></a>Specifies whether General Check in Basic Web Protection is enabled.</p>
<a name="ul4842171218268"></a><a name="ul4842171218268"></a><ul id="ul4842171218268"><li><strong id="b117141354714"><a name="b117141354714"></a><a name="b117141354714"></a>true</strong>: enabled.</li><li><strong id="b196027199470"><a name="b196027199470"></a><a name="b196027199470"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row8777157112811"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p47260058"><a name="p47260058"></a><a name="p47260058"></a>crawler</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p2859499"><a name="p2859499"></a><a name="p2859499"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p825744922615"><a name="p825744922615"></a><a name="p825744922615"></a>Specifies whether the master crawler detection switch in Basic Web Protection is enabled.</p>
<a name="ul2993535262"></a><a name="ul2993535262"></a><ul id="ul2993535262"><li><strong id="b1723562854719"><a name="b1723562854719"></a><a name="b1723562854719"></a>true</strong>: enabled.</li><li><strong id="b4552323471"><a name="b4552323471"></a><a name="b4552323471"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1177515762814"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p42166705"><a name="p42166705"></a><a name="p42166705"></a>crawler_engine</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p60059924"><a name="p60059924"></a><a name="p60059924"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1718417589268"><a name="p1718417589268"></a><a name="p1718417589268"></a>Specifies whether the Search Engine switch in Basic Web Protection is enabled.</p>
<a name="ul172713111276"></a><a name="ul172713111276"></a><ul id="ul172713111276"><li><strong id="b9762640134712"><a name="b9762640134712"></a><a name="b9762640134712"></a>true</strong>: enabled.</li><li><strong id="b1316684464720"><a name="b1316684464720"></a><a name="b1316684464720"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row177751776289"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p55359439"><a name="p55359439"></a><a name="p55359439"></a>crawler_scanner</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p54929604"><a name="p54929604"></a><a name="p54929604"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p20112962"><a name="p20112962"></a><a name="p20112962"></a>Specifies whether the Scanner switch in Basic Web Protection is enabled.</p>
<a name="ul851114810278"></a><a name="ul851114810278"></a><ul id="ul851114810278"><li><strong id="b1241713616489"><a name="b1241713616489"></a><a name="b1241713616489"></a>true</strong>: enabled.</li><li><strong id="b755820125489"><a name="b755820125489"></a><a name="b755820125489"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row177577172811"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p25118198"><a name="p25118198"></a><a name="p25118198"></a>crawler_script</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p21308157"><a name="p21308157"></a><a name="p21308157"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p48239148"><a name="p48239148"></a><a name="p48239148"></a>Specifies whether the Script Tool switch in Basic Web Protection is enabled.</p>
<a name="ul1296981219278"></a><a name="ul1296981219278"></a><ul id="ul1296981219278"><li><strong id="b1279110205485"><a name="b1279110205485"></a><a name="b1279110205485"></a>true</strong>: enabled.</li><li><strong id="b37111244486"><a name="b37111244486"></a><a name="b37111244486"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1773576281"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p11652645"><a name="p11652645"></a><a name="p11652645"></a>crawler_other</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p4340158"><a name="p4340158"></a><a name="p4340158"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p16008479"><a name="p16008479"></a><a name="p16008479"></a>Specifies whether detection of other crawlers in Basic Web Protection is enabled.</p>
<a name="ul8824161782711"></a><a name="ul8824161782711"></a><ul id="ul8824161782711"><li><strong id="b1646113406488"><a name="b1646113406488"></a><a name="b1646113406488"></a>true</strong>: enabled.</li><li><strong id="b20727443194819"><a name="b20727443194819"></a><a name="b20727443194819"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1177357102817"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p6261339"><a name="p6261339"></a><a name="p6261339"></a>webshell</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p37406470"><a name="p37406470"></a><a name="p37406470"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p10025242"><a name="p10025242"></a><a name="p10025242"></a>Specifies whether webshell detection in Basic Web Protection is enabled.</p>
<a name="ul20574202914279"></a><a name="ul20574202914279"></a><ul id="ul20574202914279"><li><strong id="b521617118491"><a name="b521617118491"></a><a name="b521617118491"></a>true</strong>: enabled.</li><li><strong id="b141456496"><a name="b141456496"></a><a name="b141456496"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row47721722816"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p8926362"><a name="p8926362"></a><a name="p8926362"></a>cc</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p51946711"><a name="p51946711"></a><a name="p51946711"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p46934044"><a name="p46934044"></a><a name="p46934044"></a>Specifies whether CC Attack Protection is enabled.</p>
<a name="ul8527033142710"></a><a name="ul8527033142710"></a><ul id="ul8527033142710"><li><strong id="b1346591612490"><a name="b1346591612490"></a><a name="b1346591612490"></a>true</strong>: enabled.</li><li><strong id="b14832111964917"><a name="b14832111964917"></a><a name="b14832111964917"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1977218711283"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p38799072"><a name="p38799072"></a><a name="p38799072"></a>custom</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p55717167"><a name="p55717167"></a><a name="p55717167"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p16796711"><a name="p16796711"></a><a name="p16796711"></a>Specifies whether Precise Protection is enabled.</p>
<a name="ul1043194117270"></a><a name="ul1043194117270"></a><ul id="ul1043194117270"><li><strong id="b1567133764912"><a name="b1567133764912"></a><a name="b1567133764912"></a>true</strong>: enabled.</li><li><strong id="b36291640104917"><a name="b36291640104917"></a><a name="b36291640104917"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row97728782819"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p10468143"><a name="p10468143"></a><a name="p10468143"></a>whiteblackip</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p42613264"><a name="p42613264"></a><a name="p42613264"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p29122361"><a name="p29122361"></a><a name="p29122361"></a>Specifies whether Blacklist and Whitelist is enabled.</p>
<a name="ul1621718455274"></a><a name="ul1621718455274"></a><ul id="ul1621718455274"><li><strong id="b420048194913"><a name="b420048194913"></a><a name="b420048194913"></a>true</strong>: enabled.</li><li><strong id="b15200451124911"><a name="b15200451124911"></a><a name="b15200451124911"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row10772157172818"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p51392996"><a name="p51392996"></a><a name="p51392996"></a>privacy</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p2083177"><a name="p2083177"></a><a name="p2083177"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p34519671"><a name="p34519671"></a><a name="p34519671"></a>Specifies whether Data Masking is enabled.</p>
<a name="ul2712175332710"></a><a name="ul2712175332710"></a><ul id="ul2712175332710"><li><strong id="b5656115944913"><a name="b5656115944913"></a><a name="b5656115944913"></a>true</strong>: enabled.</li><li><strong id="b98677215012"><a name="b98677215012"></a><a name="b98677215012"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row14770678287"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p58255435"><a name="p58255435"></a><a name="p58255435"></a>Ignore</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p21069794"><a name="p21069794"></a><a name="p21069794"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p28931745"><a name="p28931745"></a><a name="p28931745"></a>Specifies whether False Alarm Masking is enabled.</p>
<a name="ul1371357192720"></a><a name="ul1371357192720"></a><ul id="ul1371357192720"><li><strong id="b1632313175016"><a name="b1632313175016"></a><a name="b1632313175016"></a>true</strong>: enabled.</li><li><strong id="b1799271612508"><a name="b1799271612508"></a><a name="b1799271612508"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row167707717287"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p37316794"><a name="p37316794"></a><a name="p37316794"></a>antitamper</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p2761443"><a name="p2761443"></a><a name="p2761443"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p22350292"><a name="p22350292"></a><a name="p22350292"></a>Specifies whether Web Tamper Protection is enabled.</p>
<a name="ul5509133182819"></a><a name="ul5509133182819"></a><ul id="ul5509133182819"><li><strong id="b09161829155116"><a name="b09161829155116"></a><a name="b09161829155116"></a>true</strong>: enabled.</li><li><strong id="b149788329514"><a name="b149788329514"></a><a name="b149788329514"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section11561926164114"></a>

**policy\_2**  applying to domain IDs  **de06e61829494691b51979b9a03d5dcb**  and  **563972cc974b43848c73ed1a86268136**  is used as an example.

-   Request example

    ```
    {
      "hosts": [
          "de06e61829494691b51979b9a03d5dcb",
          "563972cc974b43848c73ed1a86268136"
       ]
    }
    ```


-   Response example

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
               "hosts": ["de06e61829494691b51979b9a03d5dcb", "563972cc974b43848c73ed1a86268136"],
               "timestamp": 1499817612
    }
    ```


## Status Code<a name="section40449024"></a>

[Table 6](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  6**  Status code

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

