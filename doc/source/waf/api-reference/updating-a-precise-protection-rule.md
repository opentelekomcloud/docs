# Updating a Precise Protection Rule<a name="EN-US_TOPIC_0193631155"></a>

## Function Description<a name="section4351957"></a>

This API is used to update a precise protection rule.

## URI<a name="section39167615"></a>

-   URI format

    PUT  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/custom/\{custom\_rule\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table12378624"></a>
    <table><thead align="left"><tr id="row49380663"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p40410789"><a name="p40410789"></a><a name="p40410789"></a><strong id="b19891141317274"><a name="b19891141317274"></a><a name="b19891141317274"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p52048451"><a name="p52048451"></a><a name="p52048451"></a><strong id="b1691541492716"><a name="b1691541492716"></a><a name="b1691541492716"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p55174969"><a name="p55174969"></a><a name="p55174969"></a><strong id="b5378151612272"><a name="b5378151612272"></a><a name="b5378151612272"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p39987504"><a name="p39987504"></a><a name="p39987504"></a><strong id="b153272018152712"><a name="b153272018152712"></a><a name="b153272018152712"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17762383"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p29466943"><a name="p29466943"></a><a name="p29466943"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p38012200"><a name="p38012200"></a><a name="p38012200"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p59089329"><a name="p59089329"></a><a name="p59089329"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p21506306"><a name="p21506306"></a><a name="p21506306"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row59339029"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p41732070"><a name="p41732070"></a><a name="p41732070"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p24854548"><a name="p24854548"></a><a name="p24854548"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p67061382"><a name="p67061382"></a><a name="p67061382"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p63262885"><a name="p63262885"></a><a name="p63262885"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row32495056"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p14853917"><a name="p14853917"></a><a name="p14853917"></a>custom_rule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p62316618"><a name="p62316618"></a><a name="p62316618"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p14481279"><a name="p14481279"></a><a name="p14481279"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p32132965"><a name="p32132965"></a><a name="p32132965"></a>Specifies the ID of a precise protection rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section16964221"></a>

Request parameters

**Table  2**  Parameter description

<a name="table35445346"></a>
<table><thead align="left"><tr id="row26374855"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p55988511"><a name="p55988511"></a><a name="p55988511"></a><strong id="b105970616286"><a name="b105970616286"></a><a name="b105970616286"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p38775556"><a name="p38775556"></a><a name="p38775556"></a><strong id="b1957617972815"><a name="b1957617972815"></a><a name="b1957617972815"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p53812317"><a name="p53812317"></a><a name="p53812317"></a><strong id="b20465161212820"><a name="b20465161212820"></a><a name="b20465161212820"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p63830419"><a name="p63830419"></a><a name="p63830419"></a><strong id="b18154101416282"><a name="b18154101416282"></a><a name="b18154101416282"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2881421"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p32068531"><a name="p32068531"></a><a name="p32068531"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p47414255"><a name="p47414255"></a><a name="p47414255"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p15349414"><a name="p15349414"></a><a name="p15349414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p35343042"><a name="p35343042"></a><a name="p35343042"></a>Specifies the rule name.</p>
</td>
</tr>
<tr id="row49651930"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p62383368"><a name="p62383368"></a><a name="p62383368"></a>time</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p19888014"><a name="p19888014"></a><a name="p19888014"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p316437"><a name="p316437"></a><a name="p316437"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p126191914204"><a name="p126191914204"></a><a name="p126191914204"></a>Specifies the effect time of the precise protection rule.</p>
<a name="ul52563885311"></a><a name="ul52563885311"></a><ul id="ul52563885311"><li><span class="parmvalue" id="parmvalue119412044113720"><a name="parmvalue119412044113720"></a><a name="parmvalue119412044113720"></a><b>false</b></span>: The rule takes effect immediately.</li><li><span class="parmvalue" id="parmvalue9488850133711"><a name="parmvalue9488850133711"></a><a name="parmvalue9488850133711"></a><b>true</b></span>: The rule takes effect at the scheduled time.</li></ul>
</td>
</tr>
<tr id="row29356267"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p29047402"><a name="p29047402"></a><a name="p29047402"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p4029350"><a name="p4029350"></a><a name="p4029350"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p57941894"><a name="p57941894"></a><a name="p57941894"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p62781810"><a name="p62781810"></a><a name="p62781810"></a>Specifies the time when the precise protection rule takes effect. If <strong id="b1029093715229"><a name="b1029093715229"></a><a name="b1029093715229"></a>time</strong> is set to <strong id="b829143719225"><a name="b829143719225"></a><a name="b829143719225"></a>true</strong>, either the start time or the end time must be set.</p>
</td>
</tr>
<tr id="row28165385"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p66803699"><a name="p66803699"></a><a name="p66803699"></a>end</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p42390558"><a name="p42390558"></a><a name="p42390558"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p11083186"><a name="p11083186"></a><a name="p11083186"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p25322837"><a name="p25322837"></a><a name="p25322837"></a>Specifies the time when the precise protection rule expires. If <strong id="b4434134718226"><a name="b4434134718226"></a><a name="b4434134718226"></a>time</strong> is set to <strong id="b1643424702219"><a name="b1643424702219"></a><a name="b1643424702219"></a>true</strong>, either the start time or the end time must be set.</p>
</td>
</tr>
<tr id="row1057314103473"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p5574810114714"><a name="p5574810114714"></a><a name="p5574810114714"></a>conditions</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p1657491010475"><a name="p1657491010475"></a><a name="p1657491010475"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p105745103478"><a name="p105745103478"></a><a name="p105745103478"></a><a href="#table15795105212399">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p7574810154711"><a name="p7574810154711"></a><a name="p7574810154711"></a>Specifies the condition parameters.</p>
</td>
</tr>
<tr id="row13873481"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p50010194"><a name="p50010194"></a><a name="p50010194"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p24293883"><a name="p24293883"></a><a name="p24293883"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p21647468"><a name="p21647468"></a><a name="p21647468"></a><a href="#table11869252183917">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p8614478"><a name="p8614478"></a><a name="p8614478"></a>Specifies the protective action after the precise protection rule is matched.</p>
</td>
</tr>
<tr id="row1490572204917"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p41583556"><a name="p41583556"></a><a name="p41583556"></a>priority</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p12824875"><a name="p12824875"></a><a name="p12824875"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p32181946"><a name="p32181946"></a><a name="p32181946"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p56600858"><a name="p56600858"></a><a name="p56600858"></a>Specifies the rule priority. The value ranges from <strong id="b226115715010"><a name="b226115715010"></a><a name="b226115715010"></a>0</strong> to <strong id="b72628573503"><a name="b72628573503"></a><a name="b72628573503"></a>65535</strong>. The default value is <strong id="b4908123172315"><a name="b4908123172315"></a><a name="b4908123172315"></a>50</strong>. Smaller values correspond to higher priorities.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **conditions**

<a name="table15795105212399"></a>
<table><thead align="left"><tr id="row18801155273910"><th class="cellrowborder" valign="top" width="26.16%" id="mcps1.2.5.1.1"><p id="p680445263913"><a name="p680445263913"></a><a name="p680445263913"></a><strong id="b17376511182313"><a name="b17376511182313"></a><a name="b17376511182313"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.53%" id="mcps1.2.5.1.2"><p id="p982910912357"><a name="p982910912357"></a><a name="p982910912357"></a><strong id="b926170532"><a name="b926170532"></a><a name="b926170532"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.509999999999998%" id="mcps1.2.5.1.3"><p id="p8807552173910"><a name="p8807552173910"></a><a name="p8807552173910"></a><strong id="b64851838125713"><a name="b64851838125713"></a><a name="b64851838125713"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.8%" id="mcps1.2.5.1.4"><p id="p11809552173910"><a name="p11809552173910"></a><a name="p11809552173910"></a><strong id="b10828913142318"><a name="b10828913142318"></a><a name="b10828913142318"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1981275223913"><td class="cellrowborder" valign="top" width="26.16%" headers="mcps1.2.5.1.1 "><p id="p1481416526399"><a name="p1481416526399"></a><a name="p1481416526399"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.5.1.2 "><p id="p8896173833419"><a name="p8896173833419"></a><a name="p8896173833419"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p181717528397"><a name="p181717528397"></a><a name="p181717528397"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p78191552193916"><a name="p78191552193916"></a><a name="p78191552193916"></a>Specifies the condition type. The value can be <strong id="b799045075111"><a name="b799045075111"></a><a name="b799045075111"></a>path</strong>, <strong id="b8990135065110"><a name="b8990135065110"></a><a name="b8990135065110"></a>user-agent</strong>, <strong id="b999115018512"><a name="b999115018512"></a><a name="b999115018512"></a>ip</strong>, <strong id="b16991750175118"><a name="b16991750175118"></a><a name="b16991750175118"></a>params</strong>, <strong id="b4991115015517"><a name="b4991115015517"></a><a name="b4991115015517"></a>cookie</strong>, <strong id="b3992650105114"><a name="b3992650105114"></a><a name="b3992650105114"></a>referer</strong>, or <strong id="b109921150125114"><a name="b109921150125114"></a><a name="b109921150125114"></a>header</strong>.</p>
</td>
</tr>
<tr id="row198208522393"><td class="cellrowborder" valign="top" width="26.16%" headers="mcps1.2.5.1.1 "><p id="p6823135213395"><a name="p6823135213395"></a><a name="p6823135213395"></a>index</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.5.1.2 "><p id="p48971338133418"><a name="p48971338133418"></a><a name="p48971338133418"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p882745213392"><a name="p882745213392"></a><a name="p882745213392"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><a name="ul47389508420"></a><a name="ul47389508420"></a><ul id="ul47389508420"><li>If <strong id="b799283912416"><a name="b799283912416"></a><a name="b799283912416"></a>category</strong> is set to <strong id="b3992173914249"><a name="b3992173914249"></a><a name="b3992173914249"></a>cookie</strong>, <strong id="b89929390243"><a name="b89929390243"></a><a name="b89929390243"></a>index</strong> indicates cookie name.</li><li>If <strong id="b16857144712417"><a name="b16857144712417"></a><a name="b16857144712417"></a>category</strong> is set to <strong id="b3857134742411"><a name="b3857134742411"></a><a name="b3857134742411"></a>params</strong>, <strong id="b28571947162418"><a name="b28571947162418"></a><a name="b28571947162418"></a>index</strong> indicates param name.</li><li>If <strong id="b7658162010484"><a name="b7658162010484"></a><a name="b7658162010484"></a>category </strong>is set to <strong id="b1658152074816"><a name="b1658152074816"></a><a name="b1658152074816"></a>header</strong>, <strong id="b14658102094812"><a name="b14658102094812"></a><a name="b14658102094812"></a>index</strong> indicates an option in the header.</li></ul>
</td>
</tr>
<tr id="row88321852153910"><td class="cellrowborder" valign="top" width="26.16%" headers="mcps1.2.5.1.1 "><p id="p983495273920"><a name="p983495273920"></a><a name="p983495273920"></a>logic</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.5.1.2 "><p id="p17897103873415"><a name="p17897103873415"></a><a name="p17897103873415"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p128381352133914"><a name="p128381352133914"></a><a name="p128381352133914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p17842105216390"><a name="p17842105216390"></a><a name="p17842105216390"></a><span class="parmvalue" id="parmvalue166187152233"><a name="parmvalue166187152233"></a><a name="parmvalue166187152233"></a><b>contain</b></span>, <span class="parmvalue" id="parmvalue16181015172316"><a name="parmvalue16181015172316"></a><a name="parmvalue16181015172316"></a><b>not_contain</b></span>, <span class="parmvalue" id="parmvalue16619615122318"><a name="parmvalue16619615122318"></a><a name="parmvalue16619615122318"></a><b>equal</b></span>, <span class="parmvalue" id="parmvalue146201515202319"><a name="parmvalue146201515202319"></a><a name="parmvalue146201515202319"></a><b>not_equal</b></span>, <span class="parmvalue" id="parmvalue3620131572313"><a name="parmvalue3620131572313"></a><a name="parmvalue3620131572313"></a><b>prefix</b></span>, <span class="parmvalue" id="parmvalue15621131516235"><a name="parmvalue15621131516235"></a><a name="parmvalue15621131516235"></a><b>not_prefix</b></span>, <span class="parmvalue" id="parmvalue36211159236"><a name="parmvalue36211159236"></a><a name="parmvalue36211159236"></a><b>suffix</b></span>, and <span class="parmvalue" id="parmvalue462261592315"><a name="parmvalue462261592315"></a><a name="parmvalue462261592315"></a><b>not_suffix</b></span> indicate <strong id="b462251512310"><a name="b462251512310"></a><a name="b462251512310"></a>Include</strong>, <strong id="b176231615182319"><a name="b176231615182319"></a><a name="b176231615182319"></a>Exclude</strong>, <strong id="b116239152239"><a name="b116239152239"></a><a name="b116239152239"></a>Equal to</strong>, <strong id="b19624615172313"><a name="b19624615172313"></a><a name="b19624615172313"></a>Not equal to</strong>, <strong id="b262441592311"><a name="b262441592311"></a><a name="b262441592311"></a>Prefix is</strong>, <strong id="b9625181552318"><a name="b9625181552318"></a><a name="b9625181552318"></a>Prefix is not</strong>, <strong id="b11626115172318"><a name="b11626115172318"></a><a name="b11626115172318"></a>Suffix is</strong>, and <strong id="b14626111515235"><a name="b14626111515235"></a><a name="b14626111515235"></a>Suffix is not</strong> respectively.</p>
<p id="p181434344213"><a name="p181434344213"></a><a name="p181434344213"></a>If <span class="parmname" id="parmname1723205417519"><a name="parmname1723205417519"></a><a name="parmname1723205417519"></a><b>category</b></span> is set to <strong id="b572411547510"><a name="b572411547510"></a><a name="b572411547510"></a>ip</strong>, <span class="parmname" id="parmname1972475419518"><a name="parmname1972475419518"></a><a name="parmname1972475419518"></a><b>logic</b></span> can only be <span class="parmvalue" id="parmvalue1672512543516"><a name="parmvalue1672512543516"></a><a name="parmvalue1672512543516"></a><b>equal</b></span> or <span class="parmvalue" id="parmvalue18725454155112"><a name="parmvalue18725454155112"></a><a name="parmvalue18725454155112"></a><b>not_equal</b></span>.</p>
</td>
</tr>
<tr id="row7844115211397"><td class="cellrowborder" valign="top" width="26.16%" headers="mcps1.2.5.1.1 "><p id="p198482052183915"><a name="p198482052183915"></a><a name="p198482052183915"></a>contents</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.5.1.2 "><p id="p68976382348"><a name="p68976382348"></a><a name="p68976382348"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p8852155293920"><a name="p8852155293920"></a><a name="p8852155293920"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p3856135214398"><a name="p3856135214398"></a><a name="p3856135214398"></a>Specifies content matching the condition. Currently, only one value is accepted. </p>
</td>
</tr>
</tbody>
</table>

**Table  4** **action**

<a name="table11869252183917"></a>
<table><thead align="left"><tr id="row108771152153912"><th class="cellrowborder" valign="top" width="26.88%" id="mcps1.2.5.1.1"><p id="p1088015522391"><a name="p1088015522391"></a><a name="p1088015522391"></a><strong id="b126469390235"><a name="b126469390235"></a><a name="b126469390235"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.06%" id="mcps1.2.5.1.2"><p id="p1061735942013"><a name="p1061735942013"></a><a name="p1061735942013"></a><strong id="b1406445785"><a name="b1406445785"></a><a name="b1406445785"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.259999999999998%" id="mcps1.2.5.1.3"><p id="p788305283914"><a name="p788305283914"></a><a name="p788305283914"></a><strong id="b1789775562"><a name="b1789775562"></a><a name="b1789775562"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.8%" id="mcps1.2.5.1.4"><p id="p888585219398"><a name="p888585219398"></a><a name="p888585219398"></a><strong id="b1395341192311"><a name="b1395341192311"></a><a name="b1395341192311"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row208859523396"><td class="cellrowborder" valign="top" width="26.88%" headers="mcps1.2.5.1.1 "><p id="p888817523397"><a name="p888817523397"></a><a name="p888817523397"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="17.06%" headers="mcps1.2.5.1.2 "><p id="p361725910206"><a name="p361725910206"></a><a name="p361725910206"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.259999999999998%" headers="mcps1.2.5.1.3 "><p id="p3890165216399"><a name="p3890165216399"></a><a name="p3890165216399"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p94858282213"><a name="p94858282213"></a><a name="p94858282213"></a>Specifies the protective action.</p>
<a name="ul1491712301523"></a><a name="ul1491712301523"></a><ul id="ul1491712301523"><li><span class="parmvalue" id="parmvalue956117191172"><a name="parmvalue956117191172"></a><a name="parmvalue956117191172"></a><b>block</b></span>: block.</li><li><span class="parmvalue" id="parmvalue974116227172"><a name="parmvalue974116227172"></a><a name="parmvalue974116227172"></a><b>pass</b></span>: allow.</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section18460262"></a>

Response parameters

**Table  5**  Parameter description

<a name="table21827061"></a>
<table><thead align="left"><tr id="row28265867"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p7833851"><a name="p7833851"></a><a name="p7833851"></a><strong id="b44889334578"><a name="b44889334578"></a><a name="b44889334578"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p30562167"><a name="p30562167"></a><a name="p30562167"></a><strong id="b60923830"><a name="b60923830"></a><a name="b60923830"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p59616488"><a name="p59616488"></a><a name="p59616488"></a><strong id="b15645414578"><a name="b15645414578"></a><a name="b15645414578"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row66786352"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p40985451"><a name="p40985451"></a><a name="p40985451"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p31487247"><a name="p31487247"></a><a name="p31487247"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p330178"><a name="p330178"></a><a name="p330178"></a>Specifies the ID of a precise protection rule.</p>
</td>
</tr>
<tr id="row2971610"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p39373866"><a name="p39373866"></a><a name="p39373866"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p35166558"><a name="p35166558"></a><a name="p35166558"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p29918943"><a name="p29918943"></a><a name="p29918943"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row835031"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p528693"><a name="p528693"></a><a name="p528693"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p42824212"><a name="p42824212"></a><a name="p42824212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p46209180"><a name="p46209180"></a><a name="p46209180"></a>Specifies the rule name.</p>
</td>
</tr>
<tr id="row13229438"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p64951573"><a name="p64951573"></a><a name="p64951573"></a>time</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p26586089"><a name="p26586089"></a><a name="p26586089"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p1116816397587"><a name="p1116816397587"></a><a name="p1116816397587"></a>Specifies the effect time of the precise protection rule.</p>
<a name="ul71711939145810"></a><a name="ul71711939145810"></a><ul id="ul71711939145810"><li><span class="parmvalue" id="parmvalue20681103018384"><a name="parmvalue20681103018384"></a><a name="parmvalue20681103018384"></a><b>false</b></span>: The rule takes effect immediately.</li><li><span class="parmvalue" id="parmvalue1634133410383"><a name="parmvalue1634133410383"></a><a name="parmvalue1634133410383"></a><b>true</b></span>: The rule takes effect at the scheduled time.</li></ul>
</td>
</tr>
<tr id="row53906414"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p4343448"><a name="p4343448"></a><a name="p4343448"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p16275035"><a name="p16275035"></a><a name="p16275035"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p43209438"><a name="p43209438"></a><a name="p43209438"></a>Specifies the time when the precise protection rule takes effect.</p>
</td>
</tr>
<tr id="row53340623"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p25623189"><a name="p25623189"></a><a name="p25623189"></a>end</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p62212465"><a name="p62212465"></a><a name="p62212465"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p6044872"><a name="p6044872"></a><a name="p6044872"></a>Specifies the time when the precise protection rule expires.</p>
</td>
</tr>
<tr id="row54403854"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p44636076"><a name="p44636076"></a><a name="p44636076"></a>conditions</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p58752378"><a name="p58752378"></a><a name="p58752378"></a><a href="#table19870529184915">Table 6</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p61322144"><a name="p61322144"></a><a name="p61322144"></a>Specifies the condition parameters.</p>
</td>
</tr>
<tr id="row5087387"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p9425218"><a name="p9425218"></a><a name="p9425218"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p25245222"><a name="p25245222"></a><a name="p25245222"></a><a href="#table19952132917491">Table 7</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p31597102"><a name="p31597102"></a><a name="p31597102"></a>Specifies the protective action after the precise protection rule is matched.</p>
</td>
</tr>
<tr id="row11511132"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p59986482"><a name="p59986482"></a><a name="p59986482"></a>priority</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p27066910"><a name="p27066910"></a><a name="p27066910"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p5282171915206"><a name="p5282171915206"></a><a name="p5282171915206"></a>Specifies the priority of a rule being executed. Smaller values correspond to higher priorities. If two rules are assigned with the same priority, the rule added earlier has higher priority. The value ranges from <strong id="b914418156"><a name="b914418156"></a><a name="b914418156"></a>0</strong> to <strong id="b1144198855"><a name="b1144198855"></a><a name="b1144198855"></a>65535</strong>.</p>
</td>
</tr>
<tr id="row1771443"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p9269217"><a name="p9269217"></a><a name="p9269217"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p12609087"><a name="p12609087"></a><a name="p12609087"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p1749462202016"><a name="p1749462202016"></a><a name="p1749462202016"></a>Specifies the time when a precise protection rule is added.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **conditions**

<a name="table19870529184915"></a>
<table><thead align="left"><tr id="row158795297497"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p2881122954910"><a name="p2881122954910"></a><a name="p2881122954910"></a><strong id="b6503184320247"><a name="b6503184320247"></a><a name="b6503184320247"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p7884192994917"><a name="p7884192994917"></a><a name="p7884192994917"></a><strong id="b1566197401"><a name="b1566197401"></a><a name="b1566197401"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p288715299496"><a name="p288715299496"></a><a name="p288715299496"></a><strong id="b4321447142420"><a name="b4321447142420"></a><a name="b4321447142420"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1989032916497"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1489316299496"><a name="p1489316299496"></a><a name="p1489316299496"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p16895142918491"><a name="p16895142918491"></a><a name="p16895142918491"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p4901112934918"><a name="p4901112934918"></a><a name="p4901112934918"></a>Specifies the condition type. The value can be <strong id="b12526165813510"><a name="b12526165813510"></a><a name="b12526165813510"></a>path</strong>, <strong id="b752785814519"><a name="b752785814519"></a><a name="b752785814519"></a>user-agent</strong>, <strong id="b2528185814517"><a name="b2528185814517"></a><a name="b2528185814517"></a>ip</strong>, <strong id="b185281258155113"><a name="b185281258155113"></a><a name="b185281258155113"></a>params</strong>, <strong id="b452914585519"><a name="b452914585519"></a><a name="b452914585519"></a>cookie</strong>, <strong id="b18530185813518"><a name="b18530185813518"></a><a name="b18530185813518"></a>referer</strong>, or <strong id="b16530558105112"><a name="b16530558105112"></a><a name="b16530558105112"></a>header</strong>.</p>
</td>
</tr>
<tr id="row199031629184917"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p99061529134916"><a name="p99061529134916"></a><a name="p99061529134916"></a>index</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1909112913497"><a name="p1909112913497"></a><a name="p1909112913497"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><a name="ul11271761838"></a><a name="ul11271761838"></a><ul id="ul11271761838"><li>If <strong id="b15911309251"><a name="b15911309251"></a><a name="b15911309251"></a>category</strong> is set to <strong id="b05981503259"><a name="b05981503259"></a><a name="b05981503259"></a>cookie</strong>, <strong id="b459840112520"><a name="b459840112520"></a><a name="b459840112520"></a>index</strong> indicates cookie name.</li><li>If <strong id="b17716103142515"><a name="b17716103142515"></a><a name="b17716103142515"></a>category</strong> is set to <strong id="b10716730254"><a name="b10716730254"></a><a name="b10716730254"></a>params</strong>, <strong id="b157167342513"><a name="b157167342513"></a><a name="b157167342513"></a>index</strong> indicates param name.</li><li>If <strong id="b63372384814"><a name="b63372384814"></a><a name="b63372384814"></a>category </strong>is set to <strong id="b1933223104817"><a name="b1933223104817"></a><a name="b1933223104817"></a>header</strong>, <strong id="b933102319482"><a name="b933102319482"></a><a name="b933102319482"></a>index</strong> indicates an option in the header.</li></ul>
</td>
</tr>
<tr id="row391312915495"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p17917112934914"><a name="p17917112934914"></a><a name="p17917112934914"></a>logic</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1492013291493"><a name="p1492013291493"></a><a name="p1492013291493"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p10922929194916"><a name="p10922929194916"></a><a name="p10922929194916"></a><span class="parmvalue" id="parmvalue17711111914237"><a name="parmvalue17711111914237"></a><a name="parmvalue17711111914237"></a><b>contain</b></span>, <span class="parmvalue" id="parmvalue571221982310"><a name="parmvalue571221982310"></a><a name="parmvalue571221982310"></a><b>not_contain</b></span>, <span class="parmvalue" id="parmvalue177121199236"><a name="parmvalue177121199236"></a><a name="parmvalue177121199236"></a><b>equal</b></span>, <span class="parmvalue" id="parmvalue8713719202319"><a name="parmvalue8713719202319"></a><a name="parmvalue8713719202319"></a><b>not_equal</b></span>, <span class="parmvalue" id="parmvalue17714161982314"><a name="parmvalue17714161982314"></a><a name="parmvalue17714161982314"></a><b>prefix</b></span>, <span class="parmvalue" id="parmvalue19714181942314"><a name="parmvalue19714181942314"></a><a name="parmvalue19714181942314"></a><b>not_prefix</b></span>, <span class="parmvalue" id="parmvalue17715181922313"><a name="parmvalue17715181922313"></a><a name="parmvalue17715181922313"></a><b>suffix</b></span>, and <span class="parmvalue" id="parmvalue6716919162312"><a name="parmvalue6716919162312"></a><a name="parmvalue6716919162312"></a><b>not_suffix</b></span> indicate <strong id="b18716171915231"><a name="b18716171915231"></a><a name="b18716171915231"></a>Include</strong>, <strong id="b13717111922317"><a name="b13717111922317"></a><a name="b13717111922317"></a>Exclude</strong>, <strong id="b571719195237"><a name="b571719195237"></a><a name="b571719195237"></a>Equal to</strong>, <strong id="b1871721962314"><a name="b1871721962314"></a><a name="b1871721962314"></a>Not equal to</strong>, <strong id="b5718141982314"><a name="b5718141982314"></a><a name="b5718141982314"></a>Prefix is</strong>, <strong id="b147197193231"><a name="b147197193231"></a><a name="b147197193231"></a>Prefix is not</strong>, <strong id="b1971991972310"><a name="b1971991972310"></a><a name="b1971991972310"></a>Suffix is</strong>, and <strong id="b117207193230"><a name="b117207193230"></a><a name="b117207193230"></a>Suffix is not</strong> respectively.</p>
<p id="p12211115324210"><a name="p12211115324210"></a><a name="p12211115324210"></a>If <span class="parmname" id="parmname156514220527"><a name="parmname156514220527"></a><a name="parmname156514220527"></a><b>category</b></span> is set to <strong id="b656612214525"><a name="b656612214525"></a><a name="b656612214525"></a>ip</strong>, <span class="parmname" id="parmname05678265214"><a name="parmname05678265214"></a><a name="parmname05678265214"></a><b>logic</b></span> can only be <span class="parmvalue" id="parmvalue165677215529"><a name="parmvalue165677215529"></a><a name="parmvalue165677215529"></a><b>equal</b></span> or <span class="parmvalue" id="parmvalue2056713225214"><a name="parmvalue2056713225214"></a><a name="parmvalue2056713225214"></a><b>not_equal</b></span>.</p>
</td>
</tr>
<tr id="row11927329174917"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1393018293495"><a name="p1393018293495"></a><a name="p1393018293495"></a>contents</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p14933429134919"><a name="p14933429134919"></a><a name="p14933429134919"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p129361729164910"><a name="p129361729164910"></a><a name="p129361729164910"></a>Specifies content matching the condition.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **action**

<a name="table19952132917491"></a>
<table><thead align="left"><tr id="row796182924920"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p11963162910493"><a name="p11963162910493"></a><a name="p11963162910493"></a><strong id="b01202922518"><a name="b01202922518"></a><a name="b01202922518"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p12967182920493"><a name="p12967182920493"></a><a name="p12967182920493"></a><strong id="b84845752"><a name="b84845752"></a><a name="b84845752"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p297116295496"><a name="p297116295496"></a><a name="p297116295496"></a><strong id="b149751100259"><a name="b149751100259"></a><a name="b149751100259"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row16971829164910"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1597482912494"><a name="p1597482912494"></a><a name="p1597482912494"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p697714299496"><a name="p697714299496"></a><a name="p697714299496"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1222611101546"><a name="p1222611101546"></a><a name="p1222611101546"></a>Specifies the protective action.</p>
<a name="ul1522911106417"></a><a name="ul1522911106417"></a><ul id="ul1522911106417"><li><span class="parmvalue" id="parmvalue1202136201714"><a name="parmvalue1202136201714"></a><a name="parmvalue1202136201714"></a><b>block</b></span>: block.</li><li><span class="parmvalue" id="parmvalue1480204017175"><a name="parmvalue1480204017175"></a><a name="parmvalue1480204017175"></a><b>pass</b></span>: allow.</li></ul>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section498844755617"></a>

A rule named  **rule1**  is used as an example.

-   Request example

    ```
    {
          "name": "rule1",
          "time": true,
          "start": 1499817600,
          "end": 1567817600,
          "conditions": [{
              "category": "path",
              "contents": ["/login"],
              "logic": "contain"
            },{
              "category": "ip",
               "logic": "equal",
               "contents": ["X.X.1.1"]
            }
          ],
          "action": {
            "category": "block"
          },
         "priority": 10
    }
    ```


-   Response example

    ```
    {
          "id": "7374ad99c6c448e9a9ca35cb46660a39",
          "policy_id": "9tre832yf96784ec8abd8ba61a98064ef",
          "name": "rule1",
          "time": true,
          "start": 1499817600,
          "end": 1567817600,
          "conditions": [{
              "category": "path",
              "contents": ["/login"],
              "logic": "contain"
            },{
              "category": "ip",
               "logic": "equal",
               "contents": ["X.X.1.1"]
            }
          ],
          "action": {
            "category": "block"
          },
         
         "priority": 10,
         "timestamp": 1499817600
    }
    ```


## Status Code<a name="section31924637"></a>

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

