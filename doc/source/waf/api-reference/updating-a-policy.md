# Updating a Policy<a name="EN-US_TOPIC_0193631114"></a>

## Function Description<a name="section32903875"></a>

This API is used to update a policy.

## URI<a name="section27699421"></a>

-   URI format

    PUT  /v1/\{project\_id\}/waf/policy/\{policy\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table40881691"></a>
    <table><thead align="left"><tr id="row27363964"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p1888572"><a name="p1888572"></a><a name="p1888572"></a><strong id="b88125424517"><a name="b88125424517"></a><a name="b88125424517"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p18756616"><a name="p18756616"></a><a name="p18756616"></a><strong id="b5795643157"><a name="b5795643157"></a><a name="b5795643157"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p42890953"><a name="p42890953"></a><a name="p42890953"></a><strong id="b7156945354"><a name="b7156945354"></a><a name="b7156945354"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p51615207"><a name="p51615207"></a><a name="p51615207"></a><strong id="b87810458514"><a name="b87810458514"></a><a name="b87810458514"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20082249"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p16049496"><a name="p16049496"></a><a name="p16049496"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p24940795"><a name="p24940795"></a><a name="p24940795"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p6938523"><a name="p6938523"></a><a name="p6938523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p25149471"><a name="p25149471"></a><a name="p25149471"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row25018650"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p13244784"><a name="p13244784"></a><a name="p13244784"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p66194590"><a name="p66194590"></a><a name="p66194590"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p60161613"><a name="p60161613"></a><a name="p60161613"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p41252517"><a name="p41252517"></a><a name="p41252517"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section47968201"></a>

Request parameters

**Table  2**  Parameter description

<a name="table7717485"></a>
<table><thead align="left"><tr id="row1991232"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p27072102"><a name="p27072102"></a><a name="p27072102"></a><strong id="b79715323817"><a name="b79715323817"></a><a name="b79715323817"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p45356624"><a name="p45356624"></a><a name="p45356624"></a><strong id="b1162916349811"><a name="b1162916349811"></a><a name="b1162916349811"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p50007910"><a name="p50007910"></a><a name="p50007910"></a><strong id="b559711350810"><a name="b559711350810"></a><a name="b559711350810"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p24108946"><a name="p24108946"></a><a name="p24108946"></a><strong id="b15378173617816"><a name="b15378173617816"></a><a name="b15378173617816"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5609105717527"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p2609257205217"><a name="p2609257205217"></a><a name="p2609257205217"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p5609457105219"><a name="p5609457105219"></a><a name="p5609457105219"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1660975718525"><a name="p1660975718525"></a><a name="p1660975718525"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p196091757165214"><a name="p196091757165214"></a><a name="p196091757165214"></a>Specifies the policy name.</p>
</td>
</tr>
<tr id="row6667577"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p3202885"><a name="p3202885"></a><a name="p3202885"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p58107166"><a name="p58107166"></a><a name="p58107166"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p9060011"><a name="p9060011"></a><a name="p9060011"></a><a href="#table1231716412312">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p62772309"><a name="p62772309"></a><a name="p62772309"></a>Specifies the protective action after a rule is matched.</p>
<a name="ul796714441001"></a><a name="ul796714441001"></a><ul id="ul796714441001"><li><span class="parmvalue" id="parmvalue4611266336"><a name="parmvalue4611266336"></a><a name="parmvalue4611266336"></a><b>block</b></span>: WAF blocks and logs detected attacks.</li><li><span class="parmvalue" id="parmvalue998217444403"><a name="parmvalue998217444403"></a><a name="parmvalue998217444403"></a><b>log</b></span>: WAF logs detected attacks only.</li></ul>
</td>
</tr>
<tr id="row57926711"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p61552044"><a name="p61552044"></a><a name="p61552044"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p19659690"><a name="p19659690"></a><a name="p19659690"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p48931032"><a name="p48931032"></a><a name="p48931032"></a><a href="#table1272813819259">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p3990622"><a name="p3990622"></a><a name="p3990622"></a>Specifies the protection switches.</p>
</td>
</tr>
<tr id="row8101641"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p52253166"><a name="p52253166"></a><a name="p52253166"></a>level</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p4648068"><a name="p4648068"></a><a name="p4648068"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p40949234"><a name="p40949234"></a><a name="p40949234"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p8528528245"><a name="p8528528245"></a><a name="p8528528245"></a>Specifies the protection level.</p>
<a name="ul14533143918414"></a><a name="ul14533143918414"></a><ul id="ul14533143918414"><li><span class="parmvalue" id="parmvalue6295174817531"><a name="parmvalue6295174817531"></a><a name="parmvalue6295174817531"></a><b>1</b></span>: low</li><li><span class="parmvalue" id="parmvalue4199751195312"><a name="parmvalue4199751195312"></a><a name="parmvalue4199751195312"></a><b>2</b></span>: medium</li><li><span class="parmvalue" id="parmvalue161671854125317"><a name="parmvalue161671854125317"></a><a name="parmvalue161671854125317"></a><b>3</b></span>: high</li></ul>
</td>
</tr>
<tr id="row55656689"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p11897923"><a name="p11897923"></a><a name="p11897923"></a>full_detection</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p24207722"><a name="p24207722"></a><a name="p24207722"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p14668494"><a name="p14668494"></a><a name="p14668494"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p68421843104420"><a name="p68421843104420"></a><a name="p68421843104420"></a>Specifies the detection mode in Precise Protection.</p>
<a name="ul02880554511"></a><a name="ul02880554511"></a><ul id="ul02880554511"><li><strong id="en-us_topic_0193631159_b1755019491619"><a name="en-us_topic_0193631159_b1755019491619"></a><a name="en-us_topic_0193631159_b1755019491619"></a>true</strong>: full detection. Full detection finishes all threat detections before blocking requests that meet Precise Protection specified conditions.</li><li><strong id="en-us_topic_0193631159_b17686122792016"><a name="en-us_topic_0193631159_b17686122792016"></a><a name="en-us_topic_0193631159_b17686122792016"></a>false</strong>: instant detection. Instant detection immediately ends threat detection after blocking a request that meets Precise Protection specified conditions.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  3** **action**

<a name="table1231716412312"></a>
<table><thead align="left"><tr id="row153241848236"><th class="cellrowborder" valign="top" width="25.669999999999998%" id="mcps1.2.5.1.1"><p id="p1532615432319"><a name="p1532615432319"></a><a name="p1532615432319"></a><strong id="b1548171141020"><a name="b1548171141020"></a><a name="b1548171141020"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.11%" id="mcps1.2.5.1.2"><p id="p16443851111010"><a name="p16443851111010"></a><a name="p16443851111010"></a><strong id="b834323836"><a name="b834323836"></a><a name="b834323836"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.42%" id="mcps1.2.5.1.3"><p id="p333054192311"><a name="p333054192311"></a><a name="p333054192311"></a><strong id="b968631291016"><a name="b968631291016"></a><a name="b968631291016"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.8%" id="mcps1.2.5.1.4"><p id="p193322492311"><a name="p193322492311"></a><a name="p193322492311"></a><strong id="b731017134108"><a name="b731017134108"></a><a name="b731017134108"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19763216142319"><td class="cellrowborder" valign="top" width="25.669999999999998%" headers="mcps1.2.5.1.1 "><p id="p1576317163239"><a name="p1576317163239"></a><a name="p1576317163239"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.5.1.2 "><p id="p1744365101016"><a name="p1744365101016"></a><a name="p1744365101016"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.42%" headers="mcps1.2.5.1.3 "><p id="p117631516182318"><a name="p117631516182318"></a><a name="p117631516182318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p676312167234"><a name="p676312167234"></a><a name="p676312167234"></a>Specifies the protective action.</p>
<a name="ul16561652183712"></a><a name="ul16561652183712"></a><ul id="ul16561652183712"><li><span class="parmvalue" id="parmvalue4914141623313"><a name="parmvalue4914141623313"></a><a name="parmvalue4914141623313"></a><b>block</b></span>: WAF blocks and logs detected attacks.</li><li><span class="parmvalue" id="parmvalue19924192118429"><a name="parmvalue19924192118429"></a><a name="parmvalue19924192118429"></a><b>log</b></span>: WAF logs detected attacks only.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  4** **options**

<a name="table1272813819259"></a>
<table><thead align="left"><tr id="row14733082258"><th class="cellrowborder" valign="top" width="26.72%" id="mcps1.2.5.1.1"><p id="p873817812512"><a name="p873817812512"></a><a name="p873817812512"></a><strong id="b199151516191313"><a name="b199151516191313"></a><a name="b199151516191313"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.810000000000002%" id="mcps1.2.5.1.2"><p id="p1592724616121"><a name="p1592724616121"></a><a name="p1592724616121"></a><strong id="b79392066"><a name="b79392066"></a><a name="b79392066"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.67%" id="mcps1.2.5.1.3"><p id="p137404817256"><a name="p137404817256"></a><a name="p137404817256"></a><strong id="b2899151717133"><a name="b2899151717133"></a><a name="b2899151717133"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.8%" id="mcps1.2.5.1.4"><p id="p6742198152512"><a name="p6742198152512"></a><a name="p6742198152512"></a><strong id="b19617181812135"><a name="b19617181812135"></a><a name="b19617181812135"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1177747172812"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p33504133"><a name="p33504133"></a><a name="p33504133"></a>webattack</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p127091332111218"><a name="p127091332111218"></a><a name="p127091332111218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p29480242"><a name="p29480242"></a><a name="p29480242"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p2415193218263"><a name="p2415193218263"></a><a name="p2415193218263"></a>Specifies whether Basic Web Protection is enabled.</p>
<a name="ul1778444132612"></a><a name="ul1778444132612"></a><ul id="ul1778444132612"><li><strong id="b14855122575611"><a name="b14855122575611"></a><a name="b14855122575611"></a>true</strong>: enabled.</li><li><strong id="b918233015562"><a name="b918233015562"></a><a name="b918233015562"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1577720732819"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p42476939"><a name="p42476939"></a><a name="p42476939"></a>common</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p481055316127"><a name="p481055316127"></a><a name="p481055316127"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p18080074"><a name="p18080074"></a><a name="p18080074"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p8672433268"><a name="p8672433268"></a><a name="p8672433268"></a>Specifies whether General Check in Basic Web Protection is enabled.</p>
<a name="ul4842171218268"></a><a name="ul4842171218268"></a><ul id="ul4842171218268"><li><strong id="b280074120560"><a name="b280074120560"></a><a name="b280074120560"></a>true</strong>: enabled.</li><li><strong id="b19887154413560"><a name="b19887154413560"></a><a name="b19887154413560"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row8777157112811"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p47260058"><a name="p47260058"></a><a name="p47260058"></a>crawler</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p10721155171211"><a name="p10721155171211"></a><a name="p10721155171211"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p2859499"><a name="p2859499"></a><a name="p2859499"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p825744922615"><a name="p825744922615"></a><a name="p825744922615"></a>Specifies whether the master crawler detection switch in Basic Web Protection is enabled.</p>
<a name="ul2993535262"></a><a name="ul2993535262"></a><ul id="ul2993535262"><li><strong id="b1433425935617"><a name="b1433425935617"></a><a name="b1433425935617"></a>true</strong>: enabled.</li><li><strong id="b18741124572"><a name="b18741124572"></a><a name="b18741124572"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1177515762814"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p42166705"><a name="p42166705"></a><a name="p42166705"></a>crawler_engine</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p10709195512127"><a name="p10709195512127"></a><a name="p10709195512127"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p60059924"><a name="p60059924"></a><a name="p60059924"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p1718417589268"><a name="p1718417589268"></a><a name="p1718417589268"></a>Specifies whether the Search Engine switch in Basic Web Protection is enabled.</p>
<a name="ul172713111276"></a><a name="ul172713111276"></a><ul id="ul172713111276"><li><strong id="b12530111195715"><a name="b12530111195715"></a><a name="b12530111195715"></a>true</strong>: enabled.</li><li><strong id="b1930141717576"><a name="b1930141717576"></a><a name="b1930141717576"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row177751776289"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p55359439"><a name="p55359439"></a><a name="p55359439"></a>crawler_scanner</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p6716185620127"><a name="p6716185620127"></a><a name="p6716185620127"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p54929604"><a name="p54929604"></a><a name="p54929604"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p20112962"><a name="p20112962"></a><a name="p20112962"></a>Specifies whether the Scanner switch in Basic Web Protection is enabled.</p>
<a name="ul851114810278"></a><a name="ul851114810278"></a><ul id="ul851114810278"><li><strong id="b1896092417579"><a name="b1896092417579"></a><a name="b1896092417579"></a>true</strong>: enabled.</li><li><strong id="b8481228115711"><a name="b8481228115711"></a><a name="b8481228115711"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row177577172811"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p25118198"><a name="p25118198"></a><a name="p25118198"></a>crawler_script</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p1153565915127"><a name="p1153565915127"></a><a name="p1153565915127"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p21308157"><a name="p21308157"></a><a name="p21308157"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p48239148"><a name="p48239148"></a><a name="p48239148"></a>Specifies whether the Script Tool switch in Basic Web Protection is enabled.</p>
<a name="ul1296981219278"></a><a name="ul1296981219278"></a><ul id="ul1296981219278"><li><strong id="b1253593695719"><a name="b1253593695719"></a><a name="b1253593695719"></a>true</strong>: enabled.</li><li><strong id="b13949539145714"><a name="b13949539145714"></a><a name="b13949539145714"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1773576281"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p11652645"><a name="p11652645"></a><a name="p11652645"></a>crawler_other</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p6386110181311"><a name="p6386110181311"></a><a name="p6386110181311"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p4340158"><a name="p4340158"></a><a name="p4340158"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p16008479"><a name="p16008479"></a><a name="p16008479"></a>Specifies whether detection of other crawlers in Basic Web Protection is enabled.</p>
<a name="ul8824161782711"></a><a name="ul8824161782711"></a><ul id="ul8824161782711"><li><strong id="b1793419478579"><a name="b1793419478579"></a><a name="b1793419478579"></a>true</strong>: enabled.</li><li><strong id="b10645105019576"><a name="b10645105019576"></a><a name="b10645105019576"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1177357102817"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p6261339"><a name="p6261339"></a><a name="p6261339"></a>webshell</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p844471191314"><a name="p844471191314"></a><a name="p844471191314"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p37406470"><a name="p37406470"></a><a name="p37406470"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p10025242"><a name="p10025242"></a><a name="p10025242"></a>Specifies whether webshell detection in Basic Web Protection is enabled.</p>
<a name="ul20574202914279"></a><a name="ul20574202914279"></a><ul id="ul20574202914279"><li><strong id="b85062213588"><a name="b85062213588"></a><a name="b85062213588"></a>true</strong>: enabled.</li><li><strong id="b765618575810"><a name="b765618575810"></a><a name="b765618575810"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row47721722816"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p8926362"><a name="p8926362"></a><a name="p8926362"></a>cc</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p155063211311"><a name="p155063211311"></a><a name="p155063211311"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p51946711"><a name="p51946711"></a><a name="p51946711"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p46934044"><a name="p46934044"></a><a name="p46934044"></a>Specifies whether CC Attack Protection is enabled.</p>
<a name="ul8527033142710"></a><a name="ul8527033142710"></a><ul id="ul8527033142710"><li><strong id="b13132191615585"><a name="b13132191615585"></a><a name="b13132191615585"></a>true</strong>: enabled.</li><li><strong id="b174451719105815"><a name="b174451719105815"></a><a name="b174451719105815"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1977218711283"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p38799072"><a name="p38799072"></a><a name="p38799072"></a>custom</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p124401646138"><a name="p124401646138"></a><a name="p124401646138"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p55717167"><a name="p55717167"></a><a name="p55717167"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p16796711"><a name="p16796711"></a><a name="p16796711"></a>Specifies whether Precise Protection is enabled.</p>
<a name="ul1043194117270"></a><a name="ul1043194117270"></a><ul id="ul1043194117270"><li><strong id="b9234142915584"><a name="b9234142915584"></a><a name="b9234142915584"></a>true</strong>: enabled.</li><li><strong id="b621013216587"><a name="b621013216587"></a><a name="b621013216587"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row97728782819"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p10468143"><a name="p10468143"></a><a name="p10468143"></a>whiteblackip</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p27561239131"><a name="p27561239131"></a><a name="p27561239131"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p42613264"><a name="p42613264"></a><a name="p42613264"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p29122361"><a name="p29122361"></a><a name="p29122361"></a>Specifies whether Blacklist and Whitelist is enabled.</p>
<a name="ul1621718455274"></a><a name="ul1621718455274"></a><ul id="ul1621718455274"><li><strong id="b201417473597"><a name="b201417473597"></a><a name="b201417473597"></a>true</strong>: enabled.</li><li><strong id="b1814635014598"><a name="b1814635014598"></a><a name="b1814635014598"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row10772157172818"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p51392996"><a name="p51392996"></a><a name="p51392996"></a>privacy</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p148616614139"><a name="p148616614139"></a><a name="p148616614139"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p2083177"><a name="p2083177"></a><a name="p2083177"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p34519671"><a name="p34519671"></a><a name="p34519671"></a>Specifies whether Data Masking is enabled.</p>
<a name="ul2712175332710"></a><a name="ul2712175332710"></a><ul id="ul2712175332710"><li><strong id="b19471458195914"><a name="b19471458195914"></a><a name="b19471458195914"></a>true</strong>: enabled.</li><li><strong id="b1730613110018"><a name="b1730613110018"></a><a name="b1730613110018"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row14770678287"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p58255435"><a name="p58255435"></a><a name="p58255435"></a>Ignore</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p134123721310"><a name="p134123721310"></a><a name="p134123721310"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p21069794"><a name="p21069794"></a><a name="p21069794"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p28931745"><a name="p28931745"></a><a name="p28931745"></a>Specifies whether False Alarm Masking is enabled.</p>
<a name="ul1371357192720"></a><a name="ul1371357192720"></a><ul id="ul1371357192720"><li><strong id="b1899131016017"><a name="b1899131016017"></a><a name="b1899131016017"></a>true</strong>: enabled.</li><li><strong id="b16538241701"><a name="b16538241701"></a><a name="b16538241701"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row167707717287"><td class="cellrowborder" valign="top" width="26.72%" headers="mcps1.2.5.1.1 "><p id="p37316794"><a name="p37316794"></a><a name="p37316794"></a>antitamper</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.5.1.2 "><p id="p11474118151317"><a name="p11474118151317"></a><a name="p11474118151317"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.5.1.3 "><p id="p2761443"><a name="p2761443"></a><a name="p2761443"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p22350292"><a name="p22350292"></a><a name="p22350292"></a>Specifies whether Web Tamper Protection is enabled.</p>
<a name="ul5509133182819"></a><a name="ul5509133182819"></a><ul id="ul5509133182819"><li><strong id="b25131432708"><a name="b25131432708"></a><a name="b25131432708"></a>true</strong>: enabled.</li><li><strong id="b363743520010"><a name="b363743520010"></a><a name="b363743520010"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section29060633"></a>

Response parameters

**Table  5**  Parameter description

<a name="table9491078"></a>
<table><thead align="left"><tr id="row46156472"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.4.1.1"><p id="p47686789"><a name="p47686789"></a><a name="p47686789"></a><strong id="b1920825610171"><a name="b1920825610171"></a><a name="b1920825610171"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p37424690"><a name="p37424690"></a><a name="p37424690"></a><strong id="b08465771715"><a name="b08465771715"></a><a name="b08465771715"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="58.160000000000004%" id="mcps1.2.4.1.3"><p id="p11501031"><a name="p11501031"></a><a name="p11501031"></a><strong id="b33619581179"><a name="b33619581179"></a><a name="b33619581179"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row36400421"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p62752954"><a name="p62752954"></a><a name="p62752954"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p49824491"><a name="p49824491"></a><a name="p49824491"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p9252002"><a name="p9252002"></a><a name="p9252002"></a>Specifies the instance ID.</p>
</td>
</tr>
<tr id="row16159154"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p33823082"><a name="p33823082"></a><a name="p33823082"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p55315098"><a name="p55315098"></a><a name="p55315098"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p51337963"><a name="p51337963"></a><a name="p51337963"></a>Specifies the policy name.</p>
</td>
</tr>
<tr id="row59388487"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p45738156"><a name="p45738156"></a><a name="p45738156"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p13803141"><a name="p13803141"></a><a name="p13803141"></a><a href="#table11505121316253">Table 9</a></p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p998516155518"><a name="p998516155518"></a><a name="p998516155518"></a>Specifies the protection switches.</p>
</td>
</tr>
<tr id="row63269396"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p24547423"><a name="p24547423"></a><a name="p24547423"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p42184251"><a name="p42184251"></a><a name="p42184251"></a><a href="#table12302141319252">Table 6</a></p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p61481167"><a name="p61481167"></a><a name="p61481167"></a>Specifies the mode of Basic Web Protection.</p>
<a name="ul056915599376"></a><a name="ul056915599376"></a><ul id="ul056915599376"><li><span class="parmvalue" id="parmvalue196301326173315"><a name="parmvalue196301326173315"></a><a name="parmvalue196301326173315"></a><b>block</b></span>: WAF blocks and logs detected attacks.</li><li><span class="parmvalue" id="parmvalue36621156114210"><a name="parmvalue36621156114210"></a><a name="parmvalue36621156114210"></a><b>log</b></span>: WAF logs detected attacks only.</li></ul>
</td>
</tr>
<tr id="row16459598"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p58159082"><a name="p58159082"></a><a name="p58159082"></a>level</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p13265235"><a name="p13265235"></a><a name="p13265235"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p43632395506"><a name="p43632395506"></a><a name="p43632395506"></a>Specifies the protection level.</p>
<a name="ul1636483915508"></a><a name="ul1636483915508"></a><ul id="ul1636483915508"><li><span class="parmvalue" id="parmvalue9836141419111"><a name="parmvalue9836141419111"></a><a name="parmvalue9836141419111"></a><b>1</b></span>: low</li><li><span class="parmvalue" id="parmvalue25941617014"><a name="parmvalue25941617014"></a><a name="parmvalue25941617014"></a><b>2</b></span>: medium</li><li><span class="parmvalue" id="parmvalue389952012120"><a name="parmvalue389952012120"></a><a name="parmvalue389952012120"></a><b>3</b></span>: high</li></ul>
</td>
</tr>
<tr id="row6680310"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p4234237"><a name="p4234237"></a><a name="p4234237"></a>full_detection</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p7428908"><a name="p7428908"></a><a name="p7428908"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p9392123985013"><a name="p9392123985013"></a><a name="p9392123985013"></a>Specifies the detection mode in Precise Protection.</p>
<a name="ul193934396503"></a><a name="ul193934396503"></a><ul id="ul193934396503"><li><strong id="en-us_topic_0193631159_b1755019491619_1"><a name="en-us_topic_0193631159_b1755019491619_1"></a><a name="en-us_topic_0193631159_b1755019491619_1"></a>true</strong>: full detection. Full detection finishes all threat detections before blocking requests that meet Precise Protection specified conditions.</li><li><strong id="en-us_topic_0193631159_b17686122792016_1"><a name="en-us_topic_0193631159_b17686122792016_1"></a><a name="en-us_topic_0193631159_b17686122792016_1"></a>false</strong>: instant detection. Instant detection immediately ends threat detection after blocking a request that meets Precise Protection specified conditions.</li></ul>
</td>
</tr>
<tr id="row46965394"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p46100558"><a name="p46100558"></a><a name="p46100558"></a>hosts</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p43157678"><a name="p43157678"></a><a name="p43157678"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p6111002"><a name="p6111002"></a><a name="p6111002"></a>Specifies the domain IDs.</p>
</td>
</tr>
<tr id="row54999025"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p25736027"><a name="p25736027"></a><a name="p25736027"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p4243462"><a name="p4243462"></a><a name="p4243462"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p8925879"><a name="p8925879"></a><a name="p8925879"></a>Specifies the time when a policy is created.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **action**

<a name="table12302141319252"></a>
<table><thead align="left"><tr id="row2314171302517"><th class="cellrowborder" valign="top" width="25.947405259474053%" id="mcps1.2.4.1.1"><p id="p1032051318255"><a name="p1032051318255"></a><a name="p1032051318255"></a><strong id="b63501310112017"><a name="b63501310112017"></a><a name="b63501310112017"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.608239176082392%" id="mcps1.2.4.1.2"><p id="p73241113172512"><a name="p73241113172512"></a><a name="p73241113172512"></a><strong id="b2398413182017"><a name="b2398413182017"></a><a name="b2398413182017"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.44435556444356%" id="mcps1.2.4.1.3"><p id="p733011135258"><a name="p733011135258"></a><a name="p733011135258"></a><strong id="b1513212144201"><a name="b1513212144201"></a><a name="b1513212144201"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1233213135259"><td class="cellrowborder" valign="top" width="25.947405259474053%" headers="mcps1.2.4.1.1 "><p id="p1833781332518"><a name="p1833781332518"></a><a name="p1833781332518"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="17.608239176082392%" headers="mcps1.2.4.1.2 "><p id="p1342613132514"><a name="p1342613132514"></a><a name="p1342613132514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.44435556444356%" headers="mcps1.2.4.1.3 "><p id="p1934720136259"><a name="p1934720136259"></a><a name="p1934720136259"></a>Specifies the protective action.</p>
<a name="ul312751263814"></a><a name="ul312751263814"></a><ul id="ul312751263814"><li><span class="parmvalue" id="parmvalue14879635173313"><a name="parmvalue14879635173313"></a><a name="parmvalue14879635173313"></a><b>block</b></span>: WAF blocks and logs detected attacks.</li><li><span class="parmvalue" id="parmvalue21311819124310"><a name="parmvalue21311819124310"></a><a name="parmvalue21311819124310"></a><b>log</b></span>: WAF logs detected attacks only.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  7** **options**

<a name="table11505121316253"></a>
<table><thead align="left"><tr id="row2521713172519"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p185240130256"><a name="p185240130256"></a><a name="p185240130256"></a><strong id="b7232103042515"><a name="b7232103042515"></a><a name="b7232103042515"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p3529161322512"><a name="p3529161322512"></a><a name="p3529161322512"></a><strong id="b334214313259"><a name="b334214313259"></a><a name="b334214313259"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p11535141362514"><a name="p11535141362514"></a><a name="p11535141362514"></a><strong id="b229832132518"><a name="b229832132518"></a><a name="b229832132518"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1353713137259"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p15431213102519"><a name="p15431213102519"></a><a name="p15431213102519"></a>webattack</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p125481013152517"><a name="p125481013152517"></a><a name="p125481013152517"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p25532013152516"><a name="p25532013152516"></a><a name="p25532013152516"></a>Specifies whether Basic Web Protection is enabled.</p>
<a name="ul2556191311257"></a><a name="ul2556191311257"></a><ul id="ul2556191311257"><li><strong id="b44394151725"><a name="b44394151725"></a><a name="b44394151725"></a>true</strong>: enabled.</li><li><strong id="b11500151811211"><a name="b11500151811211"></a><a name="b11500151811211"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row75671313192512"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p9571131342518"><a name="p9571131342518"></a><a name="p9571131342518"></a>common</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p20576213202515"><a name="p20576213202515"></a><a name="p20576213202515"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1258012133259"><a name="p1258012133259"></a><a name="p1258012133259"></a>Specifies whether General Check in Basic Web Protection is enabled.</p>
<a name="ul1958241302519"></a><a name="ul1958241302519"></a><ul id="ul1958241302519"><li><strong id="b786715265220"><a name="b786715265220"></a><a name="b786715265220"></a>true</strong>: enabled.</li><li><strong id="b153597303220"><a name="b153597303220"></a><a name="b153597303220"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row45967139252"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1160061315251"><a name="p1160061315251"></a><a name="p1160061315251"></a>crawler</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p66041713182512"><a name="p66041713182512"></a><a name="p66041713182512"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p5608313162513"><a name="p5608313162513"></a><a name="p5608313162513"></a>Specifies whether the master crawler detection switch in Basic Web Protection is enabled.</p>
<a name="ul19610813112517"></a><a name="ul19610813112517"></a><ul id="ul19610813112517"><li><strong id="b6848840528"><a name="b6848840528"></a><a name="b6848840528"></a>true</strong>: enabled.</li><li><strong id="b790310431023"><a name="b790310431023"></a><a name="b790310431023"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row3622171318251"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p962641313258"><a name="p962641313258"></a><a name="p962641313258"></a>crawler_engine</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p166311113142520"><a name="p166311113142520"></a><a name="p166311113142520"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1463661313257"><a name="p1463661313257"></a><a name="p1463661313257"></a>Specifies whether the Search Engine switch in Basic Web Protection is enabled.</p>
<a name="ul7639201322516"></a><a name="ul7639201322516"></a><ul id="ul7639201322516"><li><strong id="b55681155228"><a name="b55681155228"></a><a name="b55681155228"></a>true</strong>: enabled.</li><li><strong id="b53991959722"><a name="b53991959722"></a><a name="b53991959722"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row19652713162519"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p16658101352515"><a name="p16658101352515"></a><a name="p16658101352515"></a>crawler_scanner</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p17664413112517"><a name="p17664413112517"></a><a name="p17664413112517"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p26671013142513"><a name="p26671013142513"></a><a name="p26671013142513"></a>Specifies whether the Scanner switch in Basic Web Protection is enabled.</p>
<a name="ul1767181332517"></a><a name="ul1767181332517"></a><ul id="ul1767181332517"><li><strong id="b518111157312"><a name="b518111157312"></a><a name="b518111157312"></a>true</strong>: enabled.</li><li><strong id="b4595111912319"><a name="b4595111912319"></a><a name="b4595111912319"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row16685191316259"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1668891302515"><a name="p1668891302515"></a><a name="p1668891302515"></a>crawler_script</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p206948136253"><a name="p206948136253"></a><a name="p206948136253"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1969851314256"><a name="p1969851314256"></a><a name="p1969851314256"></a>Specifies whether the Script Tool switch in Basic Web Protection is enabled.</p>
<a name="ul67001313202519"></a><a name="ul67001313202519"></a><ul id="ul67001313202519"><li><strong id="b10724281337"><a name="b10724281337"></a><a name="b10724281337"></a>true</strong>: enabled.</li><li><strong id="b5814633132"><a name="b5814633132"></a><a name="b5814633132"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row117121213112510"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p15718613162516"><a name="p15718613162516"></a><a name="p15718613162516"></a>crawler_other</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p072417138253"><a name="p072417138253"></a><a name="p072417138253"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p187292013162517"><a name="p187292013162517"></a><a name="p187292013162517"></a>Specifies whether detection of other crawlers in Basic Web Protection is enabled.</p>
<a name="ul1173221382514"></a><a name="ul1173221382514"></a><ul id="ul1173221382514"><li><strong id="b34701642334"><a name="b34701642334"></a><a name="b34701642334"></a>true</strong>: enabled.</li><li><strong id="b24995017314"><a name="b24995017314"></a><a name="b24995017314"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row77451413132517"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p67501713152511"><a name="p67501713152511"></a><a name="p67501713152511"></a>webshell</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1175511138259"><a name="p1175511138259"></a><a name="p1175511138259"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p137591913112511"><a name="p137591913112511"></a><a name="p137591913112511"></a>Specifies whether webshell detection in Basic Web Protection is enabled.</p>
<a name="ul676121320259"></a><a name="ul676121320259"></a><ul id="ul676121320259"><li><strong id="b92224583320"><a name="b92224583320"></a><a name="b92224583320"></a>true</strong>: enabled.</li><li><strong id="b4761918416"><a name="b4761918416"></a><a name="b4761918416"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row87735134252"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p17779813162510"><a name="p17779813162510"></a><a name="p17779813162510"></a>cc</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p978461352514"><a name="p978461352514"></a><a name="p978461352514"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p7788151312251"><a name="p7788151312251"></a><a name="p7788151312251"></a>Specifies whether CC Attack Protection is enabled.</p>
<a name="ul207901313152517"></a><a name="ul207901313152517"></a><ul id="ul207901313152517"><li><strong id="b20685191113416"><a name="b20685191113416"></a><a name="b20685191113416"></a>true</strong>: enabled.</li><li><strong id="b1277117171543"><a name="b1277117171543"></a><a name="b1277117171543"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row13802111332511"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1580961312517"><a name="p1580961312517"></a><a name="p1580961312517"></a>custom</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1681571314255"><a name="p1681571314255"></a><a name="p1681571314255"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p198222135251"><a name="p198222135251"></a><a name="p198222135251"></a>Specifies whether Precise Protection is enabled.</p>
<a name="ul082519136253"></a><a name="ul082519136253"></a><ul id="ul082519136253"><li><strong id="b104203381742"><a name="b104203381742"></a><a name="b104203381742"></a>true</strong>: enabled.</li><li><strong id="b356804219419"><a name="b356804219419"></a><a name="b356804219419"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row5840413142518"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p084571316258"><a name="p084571316258"></a><a name="p084571316258"></a>whiteblackip</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p584911392518"><a name="p584911392518"></a><a name="p584911392518"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p14853613132520"><a name="p14853613132520"></a><a name="p14853613132520"></a>Specifies whether Blacklist and Whitelist is enabled.</p>
<a name="ul885691362515"></a><a name="ul885691362515"></a><ul id="ul885691362515"><li><strong id="b102191072006"><a name="b102191072006"></a><a name="b102191072006"></a>true</strong>: enabled.</li><li><strong id="b20837111018020"><a name="b20837111018020"></a><a name="b20837111018020"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1786921352519"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p88751213132515"><a name="p88751213132515"></a><a name="p88751213132515"></a>privacy</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1587914130258"><a name="p1587914130258"></a><a name="p1587914130258"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p6884713202519"><a name="p6884713202519"></a><a name="p6884713202519"></a>Specifies whether Data Masking is enabled.</p>
<a name="ul19886111311257"></a><a name="ul19886111311257"></a><ul id="ul19886111311257"><li><strong id="b438114527411"><a name="b438114527411"></a><a name="b438114527411"></a>true</strong>: enabled.</li><li><strong id="b470919551344"><a name="b470919551344"></a><a name="b470919551344"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row1389841315256"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p690114136259"><a name="p690114136259"></a><a name="p690114136259"></a>Ignore</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p13905813172510"><a name="p13905813172510"></a><a name="p13905813172510"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p169091013182513"><a name="p169091013182513"></a><a name="p169091013182513"></a>Specifies whether False Alarm Masking is enabled.</p>
<a name="ul209121713122518"></a><a name="ul209121713122518"></a><ul id="ul209121713122518"><li><strong id="b1345620813512"><a name="b1345620813512"></a><a name="b1345620813512"></a>true</strong>: enabled.</li><li><strong id="b14683415456"><a name="b14683415456"></a><a name="b14683415456"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
<tr id="row49261313162514"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p109301113162513"><a name="p109301113162513"></a><a name="p109301113162513"></a>antitamper</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p139361713182517"><a name="p139361713182517"></a><a name="p139361713182517"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1094031313251"><a name="p1094031313251"></a><a name="p1094031313251"></a>Specifies whether Web Tamper Protection is enabled.</p>
<a name="ul1594215134253"></a><a name="ul1594215134253"></a><ul id="ul1594215134253"><li><strong id="b66121325459"><a name="b66121325459"></a><a name="b66121325459"></a>true</strong>: enabled.</li><li><strong id="b105251834155"><a name="b105251834155"></a><a name="b105251834155"></a>false</strong>: disabled.</li></ul>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section2039619368421"></a>

A policy named  **policy\_1**  is used as an example.

-   Request example

    ```
    {
              "name": "policy_1",
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
               "full_detection": false
    }
    ```


-   Response example

    ```
    {
              "id": "xxxxxxxxxxxxxxxxxxxxxxxxx",
              "name": "policy_1",
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
               "hosts": [],
               "timestamp": 1499817612
    }
    ```


## Status Code<a name="section60219109"></a>

[Table 8](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  8**  Status code

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

