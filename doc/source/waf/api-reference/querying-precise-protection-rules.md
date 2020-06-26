# Querying Precise Protection Rules<a name="EN-US_TOPIC_0193631102"></a>

## Function Description<a name="section25506372"></a>

This API is used to query all precise protection rules in a policy.

## URI<a name="section28230758"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/custom?offset=\{offset\}&limit=\{limit\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table56418417"></a>
    <table><thead align="left"><tr id="row48333475"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p22697382"><a name="p22697382"></a><a name="p22697382"></a><strong id="b84235270616223"><a name="b84235270616223"></a><a name="b84235270616223"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p26548625"><a name="p26548625"></a><a name="p26548625"></a><strong id="b7811258121310"><a name="b7811258121310"></a><a name="b7811258121310"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p2955021"><a name="p2955021"></a><a name="p2955021"></a><strong id="b48520201417"><a name="b48520201417"></a><a name="b48520201417"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p38030145"><a name="p38030145"></a><a name="p38030145"></a><strong id="b77904482571"><a name="b77904482571"></a><a name="b77904482571"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60542934"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p5030644"><a name="p5030644"></a><a name="p5030644"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p4828994"><a name="p4828994"></a><a name="p4828994"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p55604200"><a name="p55604200"></a><a name="p55604200"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p7646351"><a name="p7646351"></a><a name="p7646351"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row1708298"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p4154453"><a name="p4154453"></a><a name="p4154453"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p966388"><a name="p966388"></a><a name="p966388"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p11168592"><a name="p11168592"></a><a name="p11168592"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p32240720"><a name="p32240720"></a><a name="p32240720"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row21731025"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p15382595"><a name="p15382595"></a><a name="p15382595"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p38030669"><a name="p38030669"></a><a name="p38030669"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p60585368"><a name="p60585368"></a><a name="p60585368"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p21617533"><a name="p21617533"></a><a name="p21617533"></a>Specifies the number of returned pages. Its value ranges from <strong id="b14761918203419"><a name="b14761918203419"></a><a name="b14761918203419"></a>0</strong> to <strong id="b07661813419"><a name="b07661813419"></a><a name="b07661813419"></a>65535</strong>. The default value is <strong id="b476151811346"><a name="b476151811346"></a><a name="b476151811346"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row9101228"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p16861445171214"><a name="p16861445171214"></a><a name="p16861445171214"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p53379695"><a name="p53379695"></a><a name="p53379695"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p28788019"><a name="p28788019"></a><a name="p28788019"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p25357967"><a name="p25357967"></a><a name="p25357967"></a>Specifies the maximum number of records displayed on each page. Its value ranges from <strong id="b877941915344"><a name="b877941915344"></a><a name="b877941915344"></a>0</strong> to <strong id="b57797196346"><a name="b57797196346"></a><a name="b57797196346"></a>50</strong>. The default value is <strong id="b2779111913349"><a name="b2779111913349"></a><a name="b2779111913349"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section52750233"></a>

Request parameters

None

## Response<a name="section4990055"></a>

Response parameters

**Table  2**  Parameter description

<a name="table40011473"></a>
<table><thead align="left"><tr id="row25246382"><th class="cellrowborder" valign="top" width="31.716828317168282%" id="mcps1.2.4.1.1"><p id="p31691062"><a name="p31691062"></a><a name="p31691062"></a><strong id="b1311836676"><a name="b1311836676"></a><a name="b1311836676"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.48715128487151%" id="mcps1.2.4.1.2"><p id="p16839243"><a name="p16839243"></a><a name="p16839243"></a><strong id="b1439190096"><a name="b1439190096"></a><a name="b1439190096"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p21801428"><a name="p21801428"></a><a name="p21801428"></a><strong id="b106721609814"><a name="b106721609814"></a><a name="b106721609814"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row61995128"><td class="cellrowborder" valign="top" width="31.716828317168282%" headers="mcps1.2.4.1.1 "><p id="p55549451"><a name="p55549451"></a><a name="p55549451"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="28.48715128487151%" headers="mcps1.2.4.1.2 "><p id="p3211654"><a name="p3211654"></a><a name="p3211654"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p58817426"><a name="p58817426"></a><a name="p58817426"></a>Specifies the total number of precise protection rules in a policy.</p>
</td>
</tr>
<tr id="row59594790"><td class="cellrowborder" valign="top" width="31.716828317168282%" headers="mcps1.2.4.1.1 "><p id="p62448653"><a name="p62448653"></a><a name="p62448653"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="28.48715128487151%" headers="mcps1.2.4.1.2 "><p id="p25176153"><a name="p25176153"></a><a name="p25176153"></a><a href="#table16394183011019">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p460610183342"><a name="p460610183342"></a><a name="p460610183342"></a>Specifies the precise protection rule objects.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **items**

<a name="table16394183011019"></a>
<table><thead align="left"><tr id="row939613301015"><th class="cellrowborder" valign="top" width="32.10678932106789%" id="mcps1.2.4.1.1"><p id="p039873016013"><a name="p039873016013"></a><a name="p039873016013"></a><strong id="b3190817104913"><a name="b3190817104913"></a><a name="b3190817104913"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.077192280771925%" id="mcps1.2.4.1.2"><p id="p183997301406"><a name="p183997301406"></a><a name="p183997301406"></a><strong id="b1015048624"><a name="b1015048624"></a><a name="b1015048624"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.81601839816019%" id="mcps1.2.4.1.3"><p id="p839973013010"><a name="p839973013010"></a><a name="p839973013010"></a><strong id="b31351819144920"><a name="b31351819144920"></a><a name="b31351819144920"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row3339122013205"><td class="cellrowborder" valign="top" width="32.10678932106789%" headers="mcps1.2.4.1.1 "><p id="p12178171962012"><a name="p12178171962012"></a><a name="p12178171962012"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.077192280771925%" headers="mcps1.2.4.1.2 "><p id="p15179151917207"><a name="p15179151917207"></a><a name="p15179151917207"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.81601839816019%" headers="mcps1.2.4.1.3 "><p id="p8182191922017"><a name="p8182191922017"></a><a name="p8182191922017"></a>Specifies the ID of a precise protection rule.</p>
</td>
</tr>
<tr id="row333932072017"><td class="cellrowborder" valign="top" width="32.10678932106789%" headers="mcps1.2.4.1.1 "><p id="p1118414196209"><a name="p1118414196209"></a><a name="p1118414196209"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.077192280771925%" headers="mcps1.2.4.1.2 "><p id="p10186101915204"><a name="p10186101915204"></a><a name="p10186101915204"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.81601839816019%" headers="mcps1.2.4.1.3 "><p id="p10189419102012"><a name="p10189419102012"></a><a name="p10189419102012"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row033712020207"><td class="cellrowborder" valign="top" width="32.10678932106789%" headers="mcps1.2.4.1.1 "><p id="p1119011197203"><a name="p1119011197203"></a><a name="p1119011197203"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="28.077192280771925%" headers="mcps1.2.4.1.2 "><p id="p1019361992020"><a name="p1019361992020"></a><a name="p1019361992020"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.81601839816019%" headers="mcps1.2.4.1.3 "><p id="p719431917209"><a name="p719431917209"></a><a name="p719431917209"></a>Specifies the rule name.</p>
</td>
</tr>
<tr id="row13337182016202"><td class="cellrowborder" valign="top" width="32.10678932106789%" headers="mcps1.2.4.1.1 "><p id="p18196101962013"><a name="p18196101962013"></a><a name="p18196101962013"></a>conditions</p>
</td>
<td class="cellrowborder" valign="top" width="28.077192280771925%" headers="mcps1.2.4.1.2 "><p id="p119921992020"><a name="p119921992020"></a><a name="p119921992020"></a><a href="#table8999745192019">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.81601839816019%" headers="mcps1.2.4.1.3 "><p id="p1220171902013"><a name="p1220171902013"></a><a name="p1220171902013"></a>Specifies the condition parameters. If there are multiple conditions, the conditions must be met at the same time.</p>
</td>
</tr>
<tr id="row833511201202"><td class="cellrowborder" valign="top" width="32.10678932106789%" headers="mcps1.2.4.1.1 "><p id="p0235419162012"><a name="p0235419162012"></a><a name="p0235419162012"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="28.077192280771925%" headers="mcps1.2.4.1.2 "><p id="p20237919182015"><a name="p20237919182015"></a><a name="p20237919182015"></a><a href="#table10607112511329">Table 5</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.81601839816019%" headers="mcps1.2.4.1.3 "><p id="p132401219102013"><a name="p132401219102013"></a><a name="p132401219102013"></a>Specifies the protective action after the precise protection rule is matched.</p>
</td>
</tr>
<tr id="row183331720132014"><td class="cellrowborder" valign="top" width="32.10678932106789%" headers="mcps1.2.4.1.1 "><p id="p18257131942020"><a name="p18257131942020"></a><a name="p18257131942020"></a>time</p>
</td>
<td class="cellrowborder" valign="top" width="28.077192280771925%" headers="mcps1.2.4.1.2 "><p id="p4259181962019"><a name="p4259181962019"></a><a name="p4259181962019"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.81601839816019%" headers="mcps1.2.4.1.3 "><p id="p126191914204"><a name="p126191914204"></a><a name="p126191914204"></a>Specifies the effect time of the precise protection rule.</p>
<a name="ul52563885311"></a><a name="ul52563885311"></a><ul id="ul52563885311"><li><span class="parmvalue" id="parmvalue156102348544"><a name="parmvalue156102348544"></a><a name="parmvalue156102348544"></a><b>false</b></span>: The rule takes effect immediately.</li><li><span class="parmvalue" id="parmvalue166311294112"><a name="parmvalue166311294112"></a><a name="parmvalue166311294112"></a><b>true</b></span>: The rule takes effect at the scheduled time.</li></ul>
</td>
</tr>
<tr id="row10333192022014"><td class="cellrowborder" valign="top" width="32.10678932106789%" headers="mcps1.2.4.1.1 "><p id="p10263101910202"><a name="p10263101910202"></a><a name="p10263101910202"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="28.077192280771925%" headers="mcps1.2.4.1.2 "><p id="p326581912203"><a name="p326581912203"></a><a name="p326581912203"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.81601839816019%" headers="mcps1.2.4.1.3 "><p id="p326741952016"><a name="p326741952016"></a><a name="p326741952016"></a>Specifies the time when the precise protection rule takes effect. This parameter is returned only when <strong id="b3373854154410"><a name="b3373854154410"></a><a name="b3373854154410"></a>time</strong> is <strong id="b1976115117445"><a name="b1976115117445"></a><a name="b1976115117445"></a>true</strong>.</p>
</td>
</tr>
<tr id="row833216201209"><td class="cellrowborder" valign="top" width="32.10678932106789%" headers="mcps1.2.4.1.1 "><p id="p19271131911205"><a name="p19271131911205"></a><a name="p19271131911205"></a>end</p>
</td>
<td class="cellrowborder" valign="top" width="28.077192280771925%" headers="mcps1.2.4.1.2 "><p id="p1727411190203"><a name="p1727411190203"></a><a name="p1727411190203"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.81601839816019%" headers="mcps1.2.4.1.3 "><p id="p15276919192012"><a name="p15276919192012"></a><a name="p15276919192012"></a>Specifies the time when the precise protection rule expires. This parameter is returned only when <strong id="b1848913513454"><a name="b1848913513454"></a><a name="b1848913513454"></a>time</strong> is <strong id="b3646181216454"><a name="b3646181216454"></a><a name="b3646181216454"></a>true</strong>.</p>
</td>
</tr>
<tr id="row9332820112017"><td class="cellrowborder" valign="top" width="32.10678932106789%" headers="mcps1.2.4.1.1 "><p id="p4278201912015"><a name="p4278201912015"></a><a name="p4278201912015"></a>priority</p>
</td>
<td class="cellrowborder" valign="top" width="28.077192280771925%" headers="mcps1.2.4.1.2 "><p id="p1228061972020"><a name="p1228061972020"></a><a name="p1228061972020"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.81601839816019%" headers="mcps1.2.4.1.3 "><p id="p5282171915206"><a name="p5282171915206"></a><a name="p5282171915206"></a>Specifies the priority of a rule being executed. Smaller values correspond to higher priorities. If two rules are assigned with the same priority, the rule added earlier has higher priority. The value ranges from <strong id="b13239114610197"><a name="b13239114610197"></a><a name="b13239114610197"></a>0</strong> to <strong id="b5340155031918"><a name="b5340155031918"></a><a name="b5340155031918"></a>65535</strong>.</p>
</td>
</tr>
<tr id="row123328208209"><td class="cellrowborder" valign="top" width="32.10678932106789%" headers="mcps1.2.4.1.1 "><p id="p02879196207"><a name="p02879196207"></a><a name="p02879196207"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="28.077192280771925%" headers="mcps1.2.4.1.2 "><p id="p8288131922016"><a name="p8288131922016"></a><a name="p8288131922016"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.81601839816019%" headers="mcps1.2.4.1.3 "><p id="p162921619162012"><a name="p162921619162012"></a><a name="p162921619162012"></a>Specifies the time when a precise protection rule is added.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **conditions**

<a name="table8999745192019"></a>
<table><thead align="left"><tr id="row187946192018"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p1810114618208"><a name="p1810114618208"></a><a name="p1810114618208"></a><strong id="b1673845245220"><a name="b1673845245220"></a><a name="b1673845245220"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p15129469208"><a name="p15129469208"></a><a name="p15129469208"></a><strong id="b353709052"><a name="b353709052"></a><a name="b353709052"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p1151846112017"><a name="p1151846112017"></a><a name="p1151846112017"></a><strong id="b9991156185212"><a name="b9991156185212"></a><a name="b9991156185212"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row18193192042114"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p17915121882118"><a name="p17915121882118"></a><a name="p17915121882118"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p13919121810219"><a name="p13919121810219"></a><a name="p13919121810219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p6922118172114"><a name="p6922118172114"></a><a name="p6922118172114"></a>Specifies the condition type. The value can be <strong id="b17337318533"><a name="b17337318533"></a><a name="b17337318533"></a>path</strong>, <strong id="b103377125315"><a name="b103377125315"></a><a name="b103377125315"></a>user-agent</strong>, <strong id="b533901135320"><a name="b533901135320"></a><a name="b533901135320"></a>ip</strong>, <strong id="b143405155315"><a name="b143405155315"></a><a name="b143405155315"></a>params</strong>, <strong id="b12340151165311"><a name="b12340151165311"></a><a name="b12340151165311"></a>cookie</strong>, <strong id="b13401011538"><a name="b13401011538"></a><a name="b13401011538"></a>referer</strong>, or <strong id="b934214195317"><a name="b934214195317"></a><a name="b934214195317"></a>header</strong>.</p>
</td>
</tr>
<tr id="row2191142014219"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p17927121862115"><a name="p17927121862115"></a><a name="p17927121862115"></a>index</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1793021892114"><a name="p1793021892114"></a><a name="p1793021892114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><a name="ul67311349013"></a><a name="ul67311349013"></a><ul id="ul67311349013"><li>If <strong id="b11315124992016"><a name="b11315124992016"></a><a name="b11315124992016"></a>category</strong> is set to <strong id="b2031594922019"><a name="b2031594922019"></a><a name="b2031594922019"></a>cookie</strong>, <strong id="b7370125617226"><a name="b7370125617226"></a><a name="b7370125617226"></a>index</strong> indicates cookie name.</li><li>If <strong id="b1594016470209"><a name="b1594016470209"></a><a name="b1594016470209"></a>category</strong> is set to <strong id="b0948104713200"><a name="b0948104713200"></a><a name="b0948104713200"></a>params</strong>, <strong id="b131051603234"><a name="b131051603234"></a><a name="b131051603234"></a>index</strong> indicates param name.</li><li>If <strong id="b2642113472"><a name="b2642113472"></a><a name="b2642113472"></a>category </strong>is set to <strong id="b271611476"><a name="b271611476"></a><a name="b271611476"></a>header</strong>, <strong id="b207110154715"><a name="b207110154715"></a><a name="b207110154715"></a>index</strong> indicates an option in the header.</li></ul>
</td>
</tr>
<tr id="row1191112015214"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1893714188211"><a name="p1893714188211"></a><a name="p1893714188211"></a>logic</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p994051832118"><a name="p994051832118"></a><a name="p994051832118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p14612173720406"><a name="p14612173720406"></a><a name="p14612173720406"></a><span class="parmvalue" id="parmvalue56551145789"><a name="parmvalue56551145789"></a><a name="parmvalue56551145789"></a><b>contain</b></span>, <span class="parmvalue" id="parmvalue1963614566816"><a name="parmvalue1963614566816"></a><a name="parmvalue1963614566816"></a><b>not_contain</b></span>, <span class="parmvalue" id="parmvalue1781534796"><a name="parmvalue1781534796"></a><a name="parmvalue1781534796"></a><b>equal</b></span>, <span class="parmvalue" id="parmvalue13673644894"><a name="parmvalue13673644894"></a><a name="parmvalue13673644894"></a><b>not_equal</b></span>, <span class="parmvalue" id="parmvalue692017531911"><a name="parmvalue692017531911"></a><a name="parmvalue692017531911"></a><b>prefix</b></span>, <span class="parmvalue" id="parmvalue16743111641014"><a name="parmvalue16743111641014"></a><a name="parmvalue16743111641014"></a><b>not_prefix</b></span>, <span class="parmvalue" id="parmvalue082243751013"><a name="parmvalue082243751013"></a><a name="parmvalue082243751013"></a><b>suffix</b></span>, and <span class="parmvalue" id="parmvalue15701195091011"><a name="parmvalue15701195091011"></a><a name="parmvalue15701195091011"></a><b>not_suffix</b></span> indicate <strong id="b6464789519"><a name="b6464789519"></a><a name="b6464789519"></a>Include</strong>, <strong id="b74646825118"><a name="b74646825118"></a><a name="b74646825118"></a>Exclude</strong>, <strong id="b184651087519"><a name="b184651087519"></a><a name="b184651087519"></a>Equal to</strong>, <strong id="b946514845120"><a name="b946514845120"></a><a name="b946514845120"></a>Not equal to</strong>, <strong id="b1446578115115"><a name="b1446578115115"></a><a name="b1446578115115"></a>Prefix is</strong>, <strong id="b746638175111"><a name="b746638175111"></a><a name="b746638175111"></a>Prefix is not</strong>, <strong id="b11466108165110"><a name="b11466108165110"></a><a name="b11466108165110"></a>Suffix is</strong>, and <strong id="b4466884515"><a name="b4466884515"></a><a name="b4466884515"></a>Suffix is not</strong> respectively.</p>
<p id="p18942141814214"><a name="p18942141814214"></a><a name="p18942141814214"></a>If <span class="parmname" id="parmname1982002772915"><a name="parmname1982002772915"></a><a name="parmname1982002772915"></a><b>category</b></span> is set to <strong id="b17820112732911"><a name="b17820112732911"></a><a name="b17820112732911"></a>ip</strong>, <span class="parmname" id="parmname1682072714299"><a name="parmname1682072714299"></a><a name="parmname1682072714299"></a><b>logic</b></span> can only be <span class="parmvalue" id="parmvalue682012274292"><a name="parmvalue682012274292"></a><a name="parmvalue682012274292"></a><b>equal</b></span> or <span class="parmvalue" id="parmvalue168201427112919"><a name="parmvalue168201427112919"></a><a name="parmvalue168201427112919"></a><b>not_equal</b></span>.</p>
</td>
</tr>
<tr id="row17189620192110"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p139511118132116"><a name="p139511118132116"></a><a name="p139511118132116"></a>contents</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p14953818172112"><a name="p14953818172112"></a><a name="p14953818172112"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p39551318112111"><a name="p39551318112111"></a><a name="p39551318112111"></a>Specifies content matching the condition.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **action**

<a name="table10607112511329"></a>
<table><thead align="left"><tr id="row186151525163218"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p1461816256324"><a name="p1461816256324"></a><a name="p1461816256324"></a><strong id="b11242172011547"><a name="b11242172011547"></a><a name="b11242172011547"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p116201025143210"><a name="p116201025143210"></a><a name="p116201025143210"></a><strong id="b1789958615"><a name="b1789958615"></a><a name="b1789958615"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p17625142533210"><a name="p17625142533210"></a><a name="p17625142533210"></a><strong id="b799692313549"><a name="b799692313549"></a><a name="b799692313549"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row34449423322"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p173849415321"><a name="p173849415321"></a><a name="p173849415321"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p13387241113219"><a name="p13387241113219"></a><a name="p13387241113219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p94858282213"><a name="p94858282213"></a><a name="p94858282213"></a>Specifies the protective action.</p>
<a name="ul1491712301523"></a><a name="ul1491712301523"></a><ul id="ul1491712301523"><li><span class="parmvalue" id="parmvalue522312429540"><a name="parmvalue522312429540"></a><a name="parmvalue522312429540"></a><b>block</b></span>: block.</li><li><span class="parmvalue" id="parmvalue1755775815212"><a name="parmvalue1755775815212"></a><a name="parmvalue1755775815212"></a><b>pass</b></span>: allow.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1177017287527"></a>

**total**  with a value of  **2**  is used as an example.

Response example

```
{
  "total": 2,
  "items": [{
      "id": "7374ad99c6c448e9a9ca35cb46660a39",
      "policy_id": "9tre832yf96784ec8abd8ba61a98064ef",
      "name": "rule1",
      "time": true,
      "start": 1499817600,
      "end": 1567817600,
      "conditions": [{
          "category": "path",
          "contents": ["/login"],
          "logic": "containi"
        },{
          "category": "ip",
           "logic": "equal",
           "contents": ["X.X.1.1"]
        }
      ],
      "action": {
        "category": "block"
      },
     
     "priority": 1,
     "timestamp": 1499817600
    }, {
      "id": "7374ad99c6c448e9a9ca35cb46660a39",
      "policy_id": "9tre832yf96784ec8abd8ba61a98064ef",
      "name": "rule2",
      "time": false,
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
     
     "priority": 1,
     "timestamp": 1499817600
    }
  ]
}

```

## Status Code<a name="section44910495"></a>

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

