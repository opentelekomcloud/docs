# Querying a Precise Protection Rule<a name="EN-US_TOPIC_0193631123"></a>

## Function Description<a name="section21481960"></a>

This API is used to query details about a precise protection rule.

## URI<a name="section59119916"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/custom/\{custom\_rule\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table24845830"></a>
    <table><thead align="left"><tr id="row58718317"><th class="cellrowborder" valign="top" width="30.91%" id="mcps1.2.5.1.1"><p id="p58563217"><a name="p58563217"></a><a name="p58563217"></a><strong id="b84917498919"><a name="b84917498919"></a><a name="b84917498919"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p46000130"><a name="p46000130"></a><a name="p46000130"></a><strong id="b14704105013917"><a name="b14704105013917"></a><a name="b14704105013917"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.45%" id="mcps1.2.5.1.3"><p id="p35023015"><a name="p35023015"></a><a name="p35023015"></a><strong id="b196881652391"><a name="b196881652391"></a><a name="b196881652391"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p18291944"><a name="p18291944"></a><a name="p18291944"></a><strong id="b5487135415915"><a name="b5487135415915"></a><a name="b5487135415915"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5252527"><td class="cellrowborder" valign="top" width="30.91%" headers="mcps1.2.5.1.1 "><p id="p22801505"><a name="p22801505"></a><a name="p22801505"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p34982632"><a name="p34982632"></a><a name="p34982632"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.3 "><p id="p15020972"><a name="p15020972"></a><a name="p15020972"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p8739220"><a name="p8739220"></a><a name="p8739220"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row11544121"><td class="cellrowborder" valign="top" width="30.91%" headers="mcps1.2.5.1.1 "><p id="p62658643"><a name="p62658643"></a><a name="p62658643"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p42185350"><a name="p42185350"></a><a name="p42185350"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.3 "><p id="p61570169"><a name="p61570169"></a><a name="p61570169"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p21127764"><a name="p21127764"></a><a name="p21127764"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row55932152"><td class="cellrowborder" valign="top" width="30.91%" headers="mcps1.2.5.1.1 "><p id="p34210500"><a name="p34210500"></a><a name="p34210500"></a>custom_rule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p19587083"><a name="p19587083"></a><a name="p19587083"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.45%" headers="mcps1.2.5.1.3 "><p id="p43049911"><a name="p43049911"></a><a name="p43049911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p64490800"><a name="p64490800"></a><a name="p64490800"></a>Specifies the ID of a precise protection rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section62317203"></a>

Request parameters

None

## Response<a name="section23983916"></a>

Response parameters

**Table  2**  Parameter description

<a name="table21827061"></a>
<table><thead align="left"><tr id="row28265867"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p7833851"><a name="p7833851"></a><a name="p7833851"></a><strong id="b7961684177"><a name="b7961684177"></a><a name="b7961684177"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p30562167"><a name="p30562167"></a><a name="p30562167"></a><strong id="b15625111091710"><a name="b15625111091710"></a><a name="b15625111091710"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p59616488"><a name="p59616488"></a><a name="p59616488"></a><strong id="b4657121220172"><a name="b4657121220172"></a><a name="b4657121220172"></a>Description</strong></p>
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
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p126191914204"><a name="p126191914204"></a><a name="p126191914204"></a>Specifies the effect time of the precise protection rule.</p>
<a name="ul52563885311"></a><a name="ul52563885311"></a><ul id="ul52563885311"><li><span class="parmvalue" id="parmvalue19835124515359"><a name="parmvalue19835124515359"></a><a name="parmvalue19835124515359"></a><b>false</b></span>: The rule takes effect immediately.</li><li><span class="parmvalue" id="parmvalue1981124853520"><a name="parmvalue1981124853520"></a><a name="parmvalue1981124853520"></a><b>true</b></span>: The rule takes effect at the scheduled time.</li></ul>
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
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p58752378"><a name="p58752378"></a><a name="p58752378"></a><a href="#table15795105212399">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p61322144"><a name="p61322144"></a><a name="p61322144"></a>Specifies the condition parameters.</p>
</td>
</tr>
<tr id="row5087387"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p9425218"><a name="p9425218"></a><a name="p9425218"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p25245222"><a name="p25245222"></a><a name="p25245222"></a><a href="#table11869252183917">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p31597102"><a name="p31597102"></a><a name="p31597102"></a>Specifies the protective action after the precise protection rule is matched.</p>
</td>
</tr>
<tr id="row11511132"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p59986482"><a name="p59986482"></a><a name="p59986482"></a>priority</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p27066910"><a name="p27066910"></a><a name="p27066910"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p44936069"><a name="p44936069"></a><a name="p44936069"></a>Specifies the priority of a rule being executed. Smaller values correspond to higher priorities. If two rules are assigned with the same priority, the rule added earlier has higher priority. The value ranges from <strong id="b5870577417"><a name="b5870577417"></a><a name="b5870577417"></a>0</strong> to <strong id="b1587657542"><a name="b1587657542"></a><a name="b1587657542"></a>65535</strong>.</p>
</td>
</tr>
<tr id="row1771443"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p9269217"><a name="p9269217"></a><a name="p9269217"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p12609087"><a name="p12609087"></a><a name="p12609087"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p48098095"><a name="p48098095"></a><a name="p48098095"></a>Specifies the time when a precise protection rule is added.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **conditions**

<a name="table15795105212399"></a>
<table><thead align="left"><tr id="row18801155273910"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p680445263913"><a name="p680445263913"></a><a name="p680445263913"></a><strong id="b5232102016189"><a name="b5232102016189"></a><a name="b5232102016189"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p8807552173910"><a name="p8807552173910"></a><a name="p8807552173910"></a><strong id="b1635554336"><a name="b1635554336"></a><a name="b1635554336"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p11809552173910"><a name="p11809552173910"></a><a name="p11809552173910"></a><strong id="b1979232191810"><a name="b1979232191810"></a><a name="b1979232191810"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1981275223913"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1481416526399"><a name="p1481416526399"></a><a name="p1481416526399"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p181717528397"><a name="p181717528397"></a><a name="p181717528397"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p78191552193916"><a name="p78191552193916"></a><a name="p78191552193916"></a>Specifies the condition type. The value can be <strong id="b26761226175110"><a name="b26761226175110"></a><a name="b26761226175110"></a>path</strong>, <strong id="b967632612519"><a name="b967632612519"></a><a name="b967632612519"></a>user-agent</strong>, <strong id="b16677026195111"><a name="b16677026195111"></a><a name="b16677026195111"></a>ip</strong>, <strong id="b8677226135117"><a name="b8677226135117"></a><a name="b8677226135117"></a>params</strong>, <strong id="b1567817267516"><a name="b1567817267516"></a><a name="b1567817267516"></a>cookie</strong>, <strong id="b267812615512"><a name="b267812615512"></a><a name="b267812615512"></a>referer</strong>, or <strong id="b206783265515"><a name="b206783265515"></a><a name="b206783265515"></a>header</strong>.</p>
</td>
</tr>
<tr id="row198208522393"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p6823135213395"><a name="p6823135213395"></a><a name="p6823135213395"></a>index</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p882745213392"><a name="p882745213392"></a><a name="p882745213392"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><a name="ul192591951241"></a><a name="ul192591951241"></a><ul id="ul192591951241"><li>If <strong id="b14728143241"><a name="b14728143241"></a><a name="b14728143241"></a>category</strong> is set to <strong id="b9724145245"><a name="b9724145245"></a><a name="b9724145245"></a>cookie</strong>, <strong id="b47251472411"><a name="b47251472411"></a><a name="b47251472411"></a>index</strong> indicates cookie name.</li><li>If <strong id="b3675116192415"><a name="b3675116192415"></a><a name="b3675116192415"></a>category</strong> is set to <strong id="b66759165241"><a name="b66759165241"></a><a name="b66759165241"></a>params</strong>, <strong id="b20675131622414"><a name="b20675131622414"></a><a name="b20675131622414"></a>index</strong> indicates param name.</li><li>If <strong id="b8186145644715"><a name="b8186145644715"></a><a name="b8186145644715"></a>category </strong>is set to <strong id="b17186656194715"><a name="b17186656194715"></a><a name="b17186656194715"></a>header</strong>, <strong id="b418675612478"><a name="b418675612478"></a><a name="b418675612478"></a>index</strong> indicates an option in the header.</li></ul>
</td>
</tr>
<tr id="row88321852153910"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p983495273920"><a name="p983495273920"></a><a name="p983495273920"></a>logic</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p128381352133914"><a name="p128381352133914"></a><a name="p128381352133914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p354910311212"><a name="p354910311212"></a><a name="p354910311212"></a><span class="parmvalue" id="parmvalue738915820221"><a name="parmvalue738915820221"></a><a name="parmvalue738915820221"></a><b>contain</b></span>, <span class="parmvalue" id="parmvalue143901758112213"><a name="parmvalue143901758112213"></a><a name="parmvalue143901758112213"></a><b>not_contain</b></span>, <span class="parmvalue" id="parmvalue12391205816226"><a name="parmvalue12391205816226"></a><a name="parmvalue12391205816226"></a><b>equal</b></span>, <span class="parmvalue" id="parmvalue12392758162219"><a name="parmvalue12392758162219"></a><a name="parmvalue12392758162219"></a><b>not_equal</b></span>, <span class="parmvalue" id="parmvalue4392758162212"><a name="parmvalue4392758162212"></a><a name="parmvalue4392758162212"></a><b>prefix</b></span>, <span class="parmvalue" id="parmvalue183932585229"><a name="parmvalue183932585229"></a><a name="parmvalue183932585229"></a><b>not_prefix</b></span>, <span class="parmvalue" id="parmvalue19394558132216"><a name="parmvalue19394558132216"></a><a name="parmvalue19394558132216"></a><b>suffix</b></span>, and <span class="parmvalue" id="parmvalue153941758152211"><a name="parmvalue153941758152211"></a><a name="parmvalue153941758152211"></a><b>not_suffix</b></span> indicate <strong id="b3395105819229"><a name="b3395105819229"></a><a name="b3395105819229"></a>Include</strong>, <strong id="b15396105812224"><a name="b15396105812224"></a><a name="b15396105812224"></a>Exclude</strong>, <strong id="b1739655822211"><a name="b1739655822211"></a><a name="b1739655822211"></a>Equal to</strong>, <strong id="b639714584228"><a name="b639714584228"></a><a name="b639714584228"></a>Not equal to</strong>, <strong id="b143984582227"><a name="b143984582227"></a><a name="b143984582227"></a>Prefix is</strong>, <strong id="b839820583228"><a name="b839820583228"></a><a name="b839820583228"></a>Prefix is not</strong>, <strong id="b10399958122216"><a name="b10399958122216"></a><a name="b10399958122216"></a>Suffix is</strong>, and <strong id="b2040055872218"><a name="b2040055872218"></a><a name="b2040055872218"></a>Suffix is not</strong> respectively.</p>
<p id="p15275833164210"><a name="p15275833164210"></a><a name="p15275833164210"></a>If <span class="parmname" id="parmname13573173220519"><a name="parmname13573173220519"></a><a name="parmname13573173220519"></a><b>category</b></span> is set to <strong id="b6574332115112"><a name="b6574332115112"></a><a name="b6574332115112"></a>ip</strong>, <span class="parmname" id="parmname1757514325517"><a name="parmname1757514325517"></a><a name="parmname1757514325517"></a><b>logic</b></span> can only be <span class="parmvalue" id="parmvalue105751132125117"><a name="parmvalue105751132125117"></a><a name="parmvalue105751132125117"></a><b>equal</b></span> or <span class="parmvalue" id="parmvalue0576173245116"><a name="parmvalue0576173245116"></a><a name="parmvalue0576173245116"></a><b>not_equal</b></span>.</p>
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

**Table  4** **action**

<a name="table11869252183917"></a>
<table><thead align="left"><tr id="row108771152153912"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p1088015522391"><a name="p1088015522391"></a><a name="p1088015522391"></a><strong id="b554205913189"><a name="b554205913189"></a><a name="b554205913189"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p788305283914"><a name="p788305283914"></a><a name="p788305283914"></a><strong id="b1608462298"><a name="b1608462298"></a><a name="b1608462298"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p888585219398"><a name="p888585219398"></a><a name="p888585219398"></a><strong id="b1176818117192"><a name="b1176818117192"></a><a name="b1176818117192"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row208859523396"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p888817523397"><a name="p888817523397"></a><a name="p888817523397"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p3890165216399"><a name="p3890165216399"></a><a name="p3890165216399"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p94858282213"><a name="p94858282213"></a><a name="p94858282213"></a>Specifies the protective action.</p>
<a name="ul1491712301523"></a><a name="ul1491712301523"></a><ul id="ul1491712301523"><li><span class="parmvalue" id="parmvalue17406748111619"><a name="parmvalue17406748111619"></a><a name="parmvalue17406748111619"></a><b>block</b></span>: block.</li><li><span class="parmvalue" id="parmvalue1489065120161"><a name="parmvalue1489065120161"></a><a name="parmvalue1489065120161"></a><b>pass</b></span>: allow.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section74205045519"></a>

Rule ID  **7374ad99c6c448e9a9ca35cb46660a39**  is used as an example.

Response example

```
{ 
      "id": "7374ad99c6c448e9a9ca35cb46660a39", 
      "policy_id": "9tre832yf96784ec8abd8ba61a98064ef", 
      "name": "rule1", 
      "time": true, 
      "start": 1499817600, 
      "end": 1567817600, 
      "conditions": [{ 
          "category ": "path", 
          "contents": ["/login"], 
          "logic": "contain"
        },{ 
          "category": "ip", 
          "logic": "equal", 
          "contents": ["X.X.1.1"]
        }, { 
          "category": "referer", 
          "logic": "prefix", 
          "contents": ["https://www.waf.com/xxx"]
        }, { 
          "category": "user-agent", 
          "logic": "contain", 
          "contents": ["Mozilla/5.0"]
        }, { 
          "category": "cookie",
		  "index": "SID",
          "logic": 3, 
          "contents": ["234SDFASR4R32412FSR325S"]
        }, { 
          "category": "header",
		  "index": "x-language",
          "logic": "equal", 
          "contents": ["en-us"]
        }, { 
          "category": "params",
		  "index": "name",
          "logic": "equal", 
          "contents": ["abc"]
        }
      ], 
      "action": { 
        "category": "block" 
      }, 
     "priority": 10, 
     "timestamp": 1499817600 
}
```

## Status Code<a name="section14528658"></a>

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

