# Adding a Precise Protection Rule<a name="EN-US_TOPIC_0193631136"></a>

## Function Description<a name="section17318397"></a>

This API is used to add a precise protection rule.

## URI<a name="section21647845"></a>

-   URI format

    POST  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/custom

-   Parameter description

    **Table  1**  Path parameters

    <a name="table41506548"></a>
    <table><thead align="left"><tr id="row5093551"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p9924526"><a name="p9924526"></a><a name="p9924526"></a><strong id="b133601937201412"><a name="b133601937201412"></a><a name="b133601937201412"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p65689174"><a name="p65689174"></a><a name="p65689174"></a><strong id="b1752894181410"><a name="b1752894181410"></a><a name="b1752894181410"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p19222862"><a name="p19222862"></a><a name="p19222862"></a><strong id="b1219111445143"><a name="b1219111445143"></a><a name="b1219111445143"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p13547966"><a name="p13547966"></a><a name="p13547966"></a><strong id="b13813164618144"><a name="b13813164618144"></a><a name="b13813164618144"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23643471"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p36073000"><a name="p36073000"></a><a name="p36073000"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p36231922"><a name="p36231922"></a><a name="p36231922"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p49104597"><a name="p49104597"></a><a name="p49104597"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p18049400"><a name="p18049400"></a><a name="p18049400"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row28226873"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p4675359"><a name="p4675359"></a><a name="p4675359"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p43159835"><a name="p43159835"></a><a name="p43159835"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p6285714"><a name="p6285714"></a><a name="p6285714"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p39380846"><a name="p39380846"></a><a name="p39380846"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section60612878"></a>

Request parameters

**Table  2**  Parameter description

<a name="table8610164"></a>
<table><thead align="left"><tr id="row58352912"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p28965449"><a name="p28965449"></a><a name="p28965449"></a><strong id="b1672611517187"><a name="b1672611517187"></a><a name="b1672611517187"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p64500002"><a name="p64500002"></a><a name="p64500002"></a><strong id="b2101155141818"><a name="b2101155141818"></a><a name="b2101155141818"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.26827317268273%" id="mcps1.2.5.1.3"><p id="p57117635"><a name="p57117635"></a><a name="p57117635"></a><strong id="b189031657111817"><a name="b189031657111817"></a><a name="b189031657111817"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.876012398760125%" id="mcps1.2.5.1.4"><p id="p63125717"><a name="p63125717"></a><a name="p63125717"></a><strong id="b142911403191"><a name="b142911403191"></a><a name="b142911403191"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row12909439"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p39031658"><a name="p39031658"></a><a name="p39031658"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p7447742"><a name="p7447742"></a><a name="p7447742"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.26827317268273%" headers="mcps1.2.5.1.3 "><p id="p66396193"><a name="p66396193"></a><a name="p66396193"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.876012398760125%" headers="mcps1.2.5.1.4 "><p id="p9382590"><a name="p9382590"></a><a name="p9382590"></a>Specifies the name of a precise protection rule. The maximum length is 256 characters. Only digits, letters, underscores (_), and hyphens (-) are allowed.</p>
</td>
</tr>
<tr id="row17334449"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p61913109"><a name="p61913109"></a><a name="p61913109"></a>time</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p48905926"><a name="p48905926"></a><a name="p48905926"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.26827317268273%" headers="mcps1.2.5.1.3 "><p id="p1957035"><a name="p1957035"></a><a name="p1957035"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.876012398760125%" headers="mcps1.2.5.1.4 "><p id="p11288193815561"><a name="p11288193815561"></a><a name="p11288193815561"></a>Specifies the effect time of the precise protection rule.</p>
<a name="ul52563885311"></a><a name="ul52563885311"></a><ul id="ul52563885311"><li><span class="parmvalue" id="parmvalue125921355142818"><a name="parmvalue125921355142818"></a><a name="parmvalue125921355142818"></a><b>false</b></span>: The rule takes effect immediately.</li><li><span class="parmvalue" id="parmvalue1141418352075"><a name="parmvalue1141418352075"></a><a name="parmvalue1141418352075"></a><b>true</b></span>: The rule takes effect at the scheduled time.</li></ul>
</td>
</tr>
<tr id="row17392531"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p66617803"><a name="p66617803"></a><a name="p66617803"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p27332947"><a name="p27332947"></a><a name="p27332947"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.26827317268273%" headers="mcps1.2.5.1.3 "><p id="p66485075"><a name="p66485075"></a><a name="p66485075"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.876012398760125%" headers="mcps1.2.5.1.4 "><p id="p16582004"><a name="p16582004"></a><a name="p16582004"></a>Specifies the time when the precise protection rule takes effect. If <strong id="b1841431119596"><a name="b1841431119596"></a><a name="b1841431119596"></a>time</strong> is set to <strong id="b8227131615592"><a name="b8227131615592"></a><a name="b8227131615592"></a>true</strong>, either the start time or the end time must be set.</p>
</td>
</tr>
<tr id="row15020312"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p8685773"><a name="p8685773"></a><a name="p8685773"></a>end</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p32458998"><a name="p32458998"></a><a name="p32458998"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.26827317268273%" headers="mcps1.2.5.1.3 "><p id="p11933180"><a name="p11933180"></a><a name="p11933180"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.876012398760125%" headers="mcps1.2.5.1.4 "><p id="p27063494"><a name="p27063494"></a><a name="p27063494"></a>Specifies the time when the precise protection rule expires. If <strong id="b13805143955918"><a name="b13805143955918"></a><a name="b13805143955918"></a>time</strong> is set to <strong id="b1805539145916"><a name="b1805539145916"></a><a name="b1805539145916"></a>true</strong>, either the start time or the end time must be set.</p>
</td>
</tr>
<tr id="row42244856"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p66390180"><a name="p66390180"></a><a name="p66390180"></a>conditions</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p8895496"><a name="p8895496"></a><a name="p8895496"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.26827317268273%" headers="mcps1.2.5.1.3 "><p id="p8702162652812"><a name="p8702162652812"></a><a name="p8702162652812"></a><a href="#table8999745192019">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.876012398760125%" headers="mcps1.2.5.1.4 "><p id="p45752091"><a name="p45752091"></a><a name="p45752091"></a>Specifies the condition parameters.</p>
</td>
</tr>
<tr id="row13191058"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p61842812"><a name="p61842812"></a><a name="p61842812"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p43211903"><a name="p43211903"></a><a name="p43211903"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.26827317268273%" headers="mcps1.2.5.1.3 "><p id="p10503234"><a name="p10503234"></a><a name="p10503234"></a><a href="#table10607112511329">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.876012398760125%" headers="mcps1.2.5.1.4 "><p id="p45455597"><a name="p45455597"></a><a name="p45455597"></a>Specifies the protective action after the precise protection rule is matched.</p>
</td>
</tr>
<tr id="row22054494"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p41583556"><a name="p41583556"></a><a name="p41583556"></a>priority</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p12824875"><a name="p12824875"></a><a name="p12824875"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.26827317268273%" headers="mcps1.2.5.1.3 "><p id="p32181946"><a name="p32181946"></a><a name="p32181946"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.876012398760125%" headers="mcps1.2.5.1.4 "><p id="p5282171915206"><a name="p5282171915206"></a><a name="p5282171915206"></a>Specifies the priority of a rule being executed. Smaller values correspond to higher priorities. If two rules are assigned with the same priority, the rule added earlier has higher priority. The value ranges from <strong id="b13239114610197"><a name="b13239114610197"></a><a name="b13239114610197"></a>0</strong> to <strong id="b5340155031918"><a name="b5340155031918"></a><a name="b5340155031918"></a>65535</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **conditions**

<a name="table8999745192019"></a>
<table><thead align="left"><tr id="row187946192018"><th class="cellrowborder" valign="top" width="25.61%" id="mcps1.2.5.1.1"><p id="p1810114618208"><a name="p1810114618208"></a><a name="p1810114618208"></a><strong id="b18519164810111"><a name="b18519164810111"></a><a name="b18519164810111"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.09%" id="mcps1.2.5.1.2"><p id="p982910912357"><a name="p982910912357"></a><a name="p982910912357"></a><strong id="b1440206295"><a name="b1440206295"></a><a name="b1440206295"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21.36%" id="mcps1.2.5.1.3"><p id="p15129469208"><a name="p15129469208"></a><a name="p15129469208"></a><strong id="b1848933010498"><a name="b1848933010498"></a><a name="b1848933010498"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35.94%" id="mcps1.2.5.1.4"><p id="p1151846112017"><a name="p1151846112017"></a><a name="p1151846112017"></a><strong id="b362213502119"><a name="b362213502119"></a><a name="b362213502119"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row18193192042114"><td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.5.1.1 "><p id="p17915121882118"><a name="p17915121882118"></a><a name="p17915121882118"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.2 "><p id="p8896173833419"><a name="p8896173833419"></a><a name="p8896173833419"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.36%" headers="mcps1.2.5.1.3 "><p id="p13919121810219"><a name="p13919121810219"></a><a name="p13919121810219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35.94%" headers="mcps1.2.5.1.4 "><p id="p6922118172114"><a name="p6922118172114"></a><a name="p6922118172114"></a>Specifies the condition type. The value can be <strong id="b1617276204315"><a name="b1617276204315"></a><a name="b1617276204315"></a>path</strong>, <strong id="b15172116134318"><a name="b15172116134318"></a><a name="b15172116134318"></a>user-agent</strong>, <strong id="b1917214674313"><a name="b1917214674313"></a><a name="b1917214674313"></a>ip</strong>, <strong id="b3173136184315"><a name="b3173136184315"></a><a name="b3173136184315"></a>params</strong>, <strong id="b121737612431"><a name="b121737612431"></a><a name="b121737612431"></a>cookie</strong>, <strong id="b1117313618439"><a name="b1117313618439"></a><a name="b1117313618439"></a>referer</strong>, or <strong id="b111748694318"><a name="b111748694318"></a><a name="b111748694318"></a>header</strong>.</p>
</td>
</tr>
<tr id="row2191142014219"><td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.5.1.1 "><p id="p17927121862115"><a name="p17927121862115"></a><a name="p17927121862115"></a>index</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.2 "><p id="p48971338133418"><a name="p48971338133418"></a><a name="p48971338133418"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.36%" headers="mcps1.2.5.1.3 "><p id="p1793021892114"><a name="p1793021892114"></a><a name="p1793021892114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35.94%" headers="mcps1.2.5.1.4 "><a name="ul51027553113"></a><a name="ul51027553113"></a><ul id="ul51027553113"><li>If <strong id="b79561522192315"><a name="b79561522192315"></a><a name="b79561522192315"></a>category</strong> is set to <strong id="b595622282316"><a name="b595622282316"></a><a name="b595622282316"></a>cookie</strong>, <strong id="b16956172218233"><a name="b16956172218233"></a><a name="b16956172218233"></a>index</strong> indicates cookie name.</li><li>If <strong id="b1585252617239"><a name="b1585252617239"></a><a name="b1585252617239"></a>category</strong> is set to <strong id="b168521826122310"><a name="b168521826122310"></a><a name="b168521826122310"></a>params</strong>, <strong id="b14852192612236"><a name="b14852192612236"></a><a name="b14852192612236"></a>index</strong> indicates param name.</li><li>If <strong id="b13860101314471"><a name="b13860101314471"></a><a name="b13860101314471"></a>category </strong>is set to <strong id="b108602013164719"><a name="b108602013164719"></a><a name="b108602013164719"></a>header</strong>, <strong id="b188608132471"><a name="b188608132471"></a><a name="b188608132471"></a>index</strong> indicates an option in the header.</li></ul>
</td>
</tr>
<tr id="row1191112015214"><td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.5.1.1 "><p id="p1893714188211"><a name="p1893714188211"></a><a name="p1893714188211"></a>logic</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.2 "><p id="p17897103873415"><a name="p17897103873415"></a><a name="p17897103873415"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.36%" headers="mcps1.2.5.1.3 "><p id="p994051832118"><a name="p994051832118"></a><a name="p994051832118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35.94%" headers="mcps1.2.5.1.4 "><p id="p6249135565913"><a name="p6249135565913"></a><a name="p6249135565913"></a><span class="parmvalue" id="parmvalue6541735102217"><a name="parmvalue6541735102217"></a><a name="parmvalue6541735102217"></a><b>contain</b></span>, <span class="parmvalue" id="parmvalue1055193515227"><a name="parmvalue1055193515227"></a><a name="parmvalue1055193515227"></a><b>not_contain</b></span>, <span class="parmvalue" id="parmvalue1956103518228"><a name="parmvalue1956103518228"></a><a name="parmvalue1956103518228"></a><b>equal</b></span>, <span class="parmvalue" id="parmvalue1956113512211"><a name="parmvalue1956113512211"></a><a name="parmvalue1956113512211"></a><b>not_equal</b></span>, <span class="parmvalue" id="parmvalue1957535132213"><a name="parmvalue1957535132213"></a><a name="parmvalue1957535132213"></a><b>prefix</b></span>, <span class="parmvalue" id="parmvalue857113592220"><a name="parmvalue857113592220"></a><a name="parmvalue857113592220"></a><b>not_prefix</b></span>, <span class="parmvalue" id="parmvalue75743510226"><a name="parmvalue75743510226"></a><a name="parmvalue75743510226"></a><b>suffix</b></span>, and <span class="parmvalue" id="parmvalue12581635172218"><a name="parmvalue12581635172218"></a><a name="parmvalue12581635172218"></a><b>not_suffix</b></span> indicate <strong id="b659193515223"><a name="b659193515223"></a><a name="b659193515223"></a>Include</strong>, <strong id="b0601235152215"><a name="b0601235152215"></a><a name="b0601235152215"></a>Exclude</strong>, <strong id="b8605353220"><a name="b8605353220"></a><a name="b8605353220"></a>Equal to</strong>, <strong id="b14601935142214"><a name="b14601935142214"></a><a name="b14601935142214"></a>Not equal to</strong>, <strong id="b1261173582217"><a name="b1261173582217"></a><a name="b1261173582217"></a>Prefix is</strong>, <strong id="b1462113511222"><a name="b1462113511222"></a><a name="b1462113511222"></a>Prefix is not</strong>, <strong id="b96217354223"><a name="b96217354223"></a><a name="b96217354223"></a>Suffix is</strong>, and <strong id="b126315357226"><a name="b126315357226"></a><a name="b126315357226"></a>Suffix is not</strong> respectively.</p>
<p id="p072865520416"><a name="p072865520416"></a><a name="p072865520416"></a>If <span class="parmname" id="parmname1777281044316"><a name="parmname1777281044316"></a><a name="parmname1777281044316"></a><b>category</b></span> is set to <strong id="b1277417106439"><a name="b1277417106439"></a><a name="b1277417106439"></a>ip</strong>, <span class="parmname" id="parmname4774101094315"><a name="parmname4774101094315"></a><a name="parmname4774101094315"></a><b>logic</b></span> can only be <span class="parmvalue" id="parmvalue17775151014317"><a name="parmvalue17775151014317"></a><a name="parmvalue17775151014317"></a><b>equal</b></span> or <span class="parmvalue" id="parmvalue67750101438"><a name="parmvalue67750101438"></a><a name="parmvalue67750101438"></a><b>not_equal</b></span>.</p>
</td>
</tr>
<tr id="row17189620192110"><td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.5.1.1 "><p id="p139511118132116"><a name="p139511118132116"></a><a name="p139511118132116"></a>contents</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.2 "><p id="p68976382348"><a name="p68976382348"></a><a name="p68976382348"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.36%" headers="mcps1.2.5.1.3 "><p id="p14953818172112"><a name="p14953818172112"></a><a name="p14953818172112"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="35.94%" headers="mcps1.2.5.1.4 "><p id="p39551318112111"><a name="p39551318112111"></a><a name="p39551318112111"></a>Specifies content matching the condition. Currently, only one value is accepted. </p>
</td>
</tr>
</tbody>
</table>

**Table  4** **action**

<a name="table10607112511329"></a>
<table><thead align="left"><tr id="row186151525163218"><th class="cellrowborder" valign="top" width="25.69%" id="mcps1.2.5.1.1"><p id="p1461816256324"><a name="p1461816256324"></a><a name="p1461816256324"></a><strong id="b03277161934"><a name="b03277161934"></a><a name="b03277161934"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.830000000000002%" id="mcps1.2.5.1.2"><p id="p177751119143610"><a name="p177751119143610"></a><a name="p177751119143610"></a><strong id="b1952857060"><a name="b1952857060"></a><a name="b1952857060"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.68%" id="mcps1.2.5.1.3"><p id="p116201025143210"><a name="p116201025143210"></a><a name="p116201025143210"></a><strong id="b422279724"><a name="b422279724"></a><a name="b422279724"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.8%" id="mcps1.2.5.1.4"><p id="p17625142533210"><a name="p17625142533210"></a><a name="p17625142533210"></a><strong id="b33210186311"><a name="b33210186311"></a><a name="b33210186311"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row34449423322"><td class="cellrowborder" valign="top" width="25.69%" headers="mcps1.2.5.1.1 "><p id="p173849415321"><a name="p173849415321"></a><a name="p173849415321"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.5.1.2 "><p id="p3775619133618"><a name="p3775619133618"></a><a name="p3775619133618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.68%" headers="mcps1.2.5.1.3 "><p id="p13387241113219"><a name="p13387241113219"></a><a name="p13387241113219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p94858282213"><a name="p94858282213"></a><a name="p94858282213"></a>Specifies the protective action.</p>
<a name="ul1491712301523"></a><a name="ul1491712301523"></a><ul id="ul1491712301523"><li><span class="parmvalue" id="parmvalue16530112781515"><a name="parmvalue16530112781515"></a><a name="parmvalue16530112781515"></a><b>block</b></span>: block.</li><li><span class="parmvalue" id="parmvalue1652183113155"><a name="parmvalue1652183113155"></a><a name="parmvalue1652183113155"></a><b>pass</b></span>: allow.</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section8644993"></a>

Response parameters

**Table  5**  Parameter description

<a name="table30555213"></a>
<table><thead align="left"><tr id="row28256362"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p7063986"><a name="p7063986"></a><a name="p7063986"></a><strong id="b15739221497"><a name="b15739221497"></a><a name="b15739221497"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p35312007"><a name="p35312007"></a><a name="p35312007"></a><strong id="b1067791273"><a name="b1067791273"></a><a name="b1067791273"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p41700304"><a name="p41700304"></a><a name="p41700304"></a><strong id="b7500183884913"><a name="b7500183884913"></a><a name="b7500183884913"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row39758420"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p66315431"><a name="p66315431"></a><a name="p66315431"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p2840802"><a name="p2840802"></a><a name="p2840802"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p28778414"><a name="p28778414"></a><a name="p28778414"></a>Specifies the ID of a precise protection rule.</p>
</td>
</tr>
<tr id="row57679138"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p41498569"><a name="p41498569"></a><a name="p41498569"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p5940949"><a name="p5940949"></a><a name="p5940949"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p11454894"><a name="p11454894"></a><a name="p11454894"></a>Specifies the ID of the policy to which the rule belongs.</p>
</td>
</tr>
<tr id="row35985187"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p29119001"><a name="p29119001"></a><a name="p29119001"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p9828880"><a name="p9828880"></a><a name="p9828880"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p57941807"><a name="p57941807"></a><a name="p57941807"></a>Specifies the rule name.</p>
</td>
</tr>
<tr id="row51714222"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p28102429"><a name="p28102429"></a><a name="p28102429"></a>conditions</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p61704265"><a name="p61704265"></a><a name="p61704265"></a><a href="#table15795105212399">Table 6</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p31989529"><a name="p31989529"></a><a name="p31989529"></a>Specifies the condition parameters in the precise protection rule.</p>
</td>
</tr>
<tr id="row53590077"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p45828979"><a name="p45828979"></a><a name="p45828979"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p21159789"><a name="p21159789"></a><a name="p21159789"></a><a href="#table11869252183917">Table 7</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p36221331"><a name="p36221331"></a><a name="p36221331"></a>Specifies the protective action after the precise protection rule is matched.</p>
</td>
</tr>
<tr id="row9477515"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p29481256"><a name="p29481256"></a><a name="p29481256"></a>priority</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p39171554"><a name="p39171554"></a><a name="p39171554"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p175201816103813"><a name="p175201816103813"></a><a name="p175201816103813"></a>Specifies the priority of a rule being executed. Smaller values correspond to higher priorities. If two rules are assigned with the same priority, the rule added earlier has higher priority. The value ranges from <strong id="b8461337047"><a name="b8461337047"></a><a name="b8461337047"></a>0</strong> to <strong id="b10466372415"><a name="b10466372415"></a><a name="b10466372415"></a>65535</strong>.</p>
</td>
</tr>
<tr id="row19630814152611"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p18257131942020"><a name="p18257131942020"></a><a name="p18257131942020"></a>time</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p4259181962019"><a name="p4259181962019"></a><a name="p4259181962019"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p618124395719"><a name="p618124395719"></a><a name="p618124395719"></a>Specifies the effect time of the precise protection rule.</p>
<a name="ul132111451508"></a><a name="ul132111451508"></a><ul id="ul132111451508"><li><span class="parmvalue" id="parmvalue139731422173118"><a name="parmvalue139731422173118"></a><a name="parmvalue139731422173118"></a><b>false</b></span>: The rule takes effect immediately.</li><li><span class="parmvalue" id="parmvalue181926531872"><a name="parmvalue181926531872"></a><a name="parmvalue181926531872"></a><b>true</b></span>: The rule takes effect at the scheduled time.</li></ul>
</td>
</tr>
<tr id="row172872583236"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p1828985872315"><a name="p1828985872315"></a><a name="p1828985872315"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p1928925872320"><a name="p1928925872320"></a><a name="p1928925872320"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p3289658102318"><a name="p3289658102318"></a><a name="p3289658102318"></a>Specifies the time when the precise protection rule takes effect.</p>
</td>
</tr>
<tr id="row184061547240"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p134063413241"><a name="p134063413241"></a><a name="p134063413241"></a>end</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p140610415249"><a name="p140610415249"></a><a name="p140610415249"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p12406114142419"><a name="p12406114142419"></a><a name="p12406114142419"></a>Specifies the time when the precise protection rule expires.</p>
</td>
</tr>
<tr id="row89941720172515"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p11994182062511"><a name="p11994182062511"></a><a name="p11994182062511"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p799417209254"><a name="p799417209254"></a><a name="p799417209254"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p15994102012255"><a name="p15994102012255"></a><a name="p15994102012255"></a>Specifies the time when a precise protection rule is added.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **conditions**

<a name="table15795105212399"></a>
<table><thead align="left"><tr id="row18801155273910"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p680445263913"><a name="p680445263913"></a><a name="p680445263913"></a><strong id="b85681642510"><a name="b85681642510"></a><a name="b85681642510"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p8807552173910"><a name="p8807552173910"></a><a name="p8807552173910"></a><strong id="b1796991050"><a name="b1796991050"></a><a name="b1796991050"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p11809552173910"><a name="p11809552173910"></a><a name="p11809552173910"></a><strong id="b36481468512"><a name="b36481468512"></a><a name="b36481468512"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1981275223913"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1481416526399"><a name="p1481416526399"></a><a name="p1481416526399"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p181717528397"><a name="p181717528397"></a><a name="p181717528397"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p78191552193916"><a name="p78191552193916"></a><a name="p78191552193916"></a>Specifies the condition type. The value can be <strong id="b106121320164312"><a name="b106121320164312"></a><a name="b106121320164312"></a>path</strong>, <strong id="b16138202433"><a name="b16138202433"></a><a name="b16138202433"></a>user-agent</strong>, <strong id="b196139208431"><a name="b196139208431"></a><a name="b196139208431"></a>ip</strong>, <strong id="b12614172017435"><a name="b12614172017435"></a><a name="b12614172017435"></a>params</strong>, <strong id="b16614720164316"><a name="b16614720164316"></a><a name="b16614720164316"></a>cookie</strong>, <strong id="b06158202434"><a name="b06158202434"></a><a name="b06158202434"></a>referer</strong>, or <strong id="b761512024310"><a name="b761512024310"></a><a name="b761512024310"></a>header</strong>.</p>
</td>
</tr>
<tr id="row198208522393"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p6823135213395"><a name="p6823135213395"></a><a name="p6823135213395"></a>index</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p882745213392"><a name="p882745213392"></a><a name="p882745213392"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><a name="ul5824161113"></a><a name="ul5824161113"></a><ul id="ul5824161113"><li>If <strong id="b53114532232"><a name="b53114532232"></a><a name="b53114532232"></a>category</strong> is set to <strong id="b11319539230"><a name="b11319539230"></a><a name="b11319539230"></a>cookie</strong>, <strong id="b631125319236"><a name="b631125319236"></a><a name="b631125319236"></a>index</strong> indicates cookie name.</li><li>If <strong id="b18195195612237"><a name="b18195195612237"></a><a name="b18195195612237"></a>category</strong> is set to <strong id="b419565622310"><a name="b419565622310"></a><a name="b419565622310"></a>params</strong>, <strong id="b161951856182313"><a name="b161951856182313"></a><a name="b161951856182313"></a>index</strong> indicates param name.</li><li>If <strong id="b71031017154715"><a name="b71031017154715"></a><a name="b71031017154715"></a>category </strong>is set to <strong id="b141031917174718"><a name="b141031917174718"></a><a name="b141031917174718"></a>header</strong>, <strong id="b8103191714713"><a name="b8103191714713"></a><a name="b8103191714713"></a>index</strong> indicates an option in the header.</li></ul>
</td>
</tr>
<tr id="row88321852153910"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p983495273920"><a name="p983495273920"></a><a name="p983495273920"></a>logic</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p128381352133914"><a name="p128381352133914"></a><a name="p128381352133914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p17842105216390"><a name="p17842105216390"></a><a name="p17842105216390"></a><span class="parmvalue" id="parmvalue178384020229"><a name="parmvalue178384020229"></a><a name="parmvalue178384020229"></a><b>contain</b></span>, <span class="parmvalue" id="parmvalue57842040162215"><a name="parmvalue57842040162215"></a><a name="parmvalue57842040162215"></a><b>not_contain</b></span>, <span class="parmvalue" id="parmvalue1578411409220"><a name="parmvalue1578411409220"></a><a name="parmvalue1578411409220"></a><b>equal</b></span>, <span class="parmvalue" id="parmvalue15785154012227"><a name="parmvalue15785154012227"></a><a name="parmvalue15785154012227"></a><b>not_equal</b></span>, <span class="parmvalue" id="parmvalue97851640162216"><a name="parmvalue97851640162216"></a><a name="parmvalue97851640162216"></a><b>prefix</b></span>, <span class="parmvalue" id="parmvalue778616404222"><a name="parmvalue778616404222"></a><a name="parmvalue778616404222"></a><b>not_prefix</b></span>, <span class="parmvalue" id="parmvalue8786240192213"><a name="parmvalue8786240192213"></a><a name="parmvalue8786240192213"></a><b>suffix</b></span>, and <span class="parmvalue" id="parmvalue14787194072218"><a name="parmvalue14787194072218"></a><a name="parmvalue14787194072218"></a><b>not_suffix</b></span> indicate <strong id="b19788194062214"><a name="b19788194062214"></a><a name="b19788194062214"></a>Include</strong>, <strong id="b4789340182218"><a name="b4789340182218"></a><a name="b4789340182218"></a>Exclude</strong>, <strong id="b107894409222"><a name="b107894409222"></a><a name="b107894409222"></a>Equal to</strong>, <strong id="b7789184062215"><a name="b7789184062215"></a><a name="b7789184062215"></a>Not equal to</strong>, <strong id="b1679024082211"><a name="b1679024082211"></a><a name="b1679024082211"></a>Prefix is</strong>, <strong id="b11790144022215"><a name="b11790144022215"></a><a name="b11790144022215"></a>Prefix is not</strong>, <strong id="b379114405227"><a name="b379114405227"></a><a name="b379114405227"></a>Suffix is</strong>, and <strong id="b07910402225"><a name="b07910402225"></a><a name="b07910402225"></a>Suffix is not</strong> respectively.</p>
<p id="p98653711425"><a name="p98653711425"></a><a name="p98653711425"></a>If <span class="parmname" id="parmname79312519439"><a name="parmname79312519439"></a><a name="parmname79312519439"></a><b>category</b></span> is set to <strong id="b189442524313"><a name="b189442524313"></a><a name="b189442524313"></a>ip</strong>, <span class="parmname" id="parmname294112504314"><a name="parmname294112504314"></a><a name="parmname294112504314"></a><b>logic</b></span> can only be <span class="parmvalue" id="parmvalue5956256431"><a name="parmvalue5956256431"></a><a name="parmvalue5956256431"></a><b>equal</b></span> or <span class="parmvalue" id="parmvalue1995172519431"><a name="parmvalue1995172519431"></a><a name="parmvalue1995172519431"></a><b>not_equal</b></span>.</p>
</td>
</tr>
<tr id="row7844115211397"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p198482052183915"><a name="p198482052183915"></a><a name="p198482052183915"></a>contents</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p8852155293920"><a name="p8852155293920"></a><a name="p8852155293920"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p3856135214398"><a name="p3856135214398"></a><a name="p3856135214398"></a>Specifies content matching the condition.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **action**

<a name="table11869252183917"></a>
<table><thead align="left"><tr id="row108771152153912"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p1088015522391"><a name="p1088015522391"></a><a name="p1088015522391"></a><strong id="b44061821169"><a name="b44061821169"></a><a name="b44061821169"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p788305283914"><a name="p788305283914"></a><a name="p788305283914"></a><strong id="b1196187592"><a name="b1196187592"></a><a name="b1196187592"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p888585219398"><a name="p888585219398"></a><a name="p888585219398"></a><strong id="b10513271166"><a name="b10513271166"></a><a name="b10513271166"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row208859523396"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p888817523397"><a name="p888817523397"></a><a name="p888817523397"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p3890165216399"><a name="p3890165216399"></a><a name="p3890165216399"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p98611530733"><a name="p98611530733"></a><a name="p98611530733"></a>Specifies the protective action.</p>
<a name="ul1186323013318"></a><a name="ul1186323013318"></a><ul id="ul1186323013318"><li><span class="parmvalue" id="parmvalue16644175520155"><a name="parmvalue16644175520155"></a><a name="parmvalue16644175520155"></a><b>block</b></span>: block.</li><li><span class="parmvalue" id="parmvalue13011559161517"><a name="parmvalue13011559161517"></a><a name="parmvalue13011559161517"></a><b>pass</b></span>: allow.</li></ul>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section9395143112535"></a>

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


## Status Code<a name="section10696080"></a>

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

