# Updating a CC Attack Protection Rule<a name="EN-US_TOPIC_0193631101"></a>

## Function Description<a name="section25190616"></a>

This API is used to update a CC attack protection rule.

## URI<a name="section25388955"></a>

-   URI format

    PUT  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/cc/\{ccrule\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table49821820"></a>
    <table><thead align="left"><tr id="row29493317"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p40148466"><a name="p40148466"></a><a name="p40148466"></a><strong id="b1372610544293"><a name="b1372610544293"></a><a name="b1372610544293"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p30800295"><a name="p30800295"></a><a name="p30800295"></a><strong id="b10324145614294_1"><a name="b10324145614294_1"></a><a name="b10324145614294_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p11795981"><a name="p11795981"></a><a name="p11795981"></a><strong id="b035917586297_1"><a name="b035917586297_1"></a><a name="b035917586297_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p15950411"><a name="p15950411"></a><a name="p15950411"></a><strong id="b5756115914298"><a name="b5756115914298"></a><a name="b5756115914298"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16914954"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p27934066"><a name="p27934066"></a><a name="p27934066"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p48066858"><a name="p48066858"></a><a name="p48066858"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p1101402"><a name="p1101402"></a><a name="p1101402"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p22104747"><a name="p22104747"></a><a name="p22104747"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row64724999"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p8233580"><a name="p8233580"></a><a name="p8233580"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p62940229"><a name="p62940229"></a><a name="p62940229"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p64993787"><a name="p64993787"></a><a name="p64993787"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p30005365"><a name="p30005365"></a><a name="p30005365"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row1612831"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p63530491"><a name="p63530491"></a><a name="p63530491"></a>ccrule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p45696143"><a name="p45696143"></a><a name="p45696143"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p10400132"><a name="p10400132"></a><a name="p10400132"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p37104386"><a name="p37104386"></a><a name="p37104386"></a>Specifies the ID of a CC attack protection rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section27174007"></a>

Request parameters

**Table  2**  Parameter description

<a name="table38027958"></a>
<table><thead align="left"><tr id="row50296914"><th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.2.5.1.1"><p id="p47518222"><a name="p47518222"></a><a name="p47518222"></a><strong id="b02471827103116"><a name="b02471827103116"></a><a name="b02471827103116"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.2"><p id="p23770734"><a name="p23770734"></a><a name="p23770734"></a><strong id="b86481280319"><a name="b86481280319"></a><a name="b86481280319"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="p46381274"><a name="p46381274"></a><a name="p46381274"></a><strong id="b151925302315"><a name="b151925302315"></a><a name="b151925302315"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.5.1.4"><p id="p65895739"><a name="p65895739"></a><a name="p65895739"></a><strong id="b15781113214311"><a name="b15781113214311"></a><a name="b15781113214311"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row56190747"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p55156678"><a name="p55156678"></a><a name="p55156678"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p38505946"><a name="p38505946"></a><a name="p38505946"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p31973885"><a name="p31973885"></a><a name="p31973885"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p39747930"><a name="p39747930"></a><a name="p39747930"></a>Specifies the URL to which the rule applies, excluding a domain name. </p>
</td>
</tr>
<tr id="row22187053"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p52320849"><a name="p52320849"></a><a name="p52320849"></a>limit_num</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p10130370"><a name="p10130370"></a><a name="p10130370"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p15253607"><a name="p15253607"></a><a name="p15253607"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p27582632"><a name="p27582632"></a><a name="p27582632"></a>Specifies the number of requests allowed from a web visitor in a rate limiting period. The value ranges from <strong id="b5636131117105"><a name="b5636131117105"></a><a name="b5636131117105"></a>0</strong> to <strong id="b1563601117104"><a name="b1563601117104"></a><a name="b1563601117104"></a>2<sup id="sup116361311101018"><a name="sup116361311101018"></a><a name="sup116361311101018"></a>32</sup></strong>.</p>
</td>
</tr>
<tr id="row46917103"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p42189031"><a name="p42189031"></a><a name="p42189031"></a>limit_period</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p61868335"><a name="p61868335"></a><a name="p61868335"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p45279215"><a name="p45279215"></a><a name="p45279215"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p43737808"><a name="p43737808"></a><a name="p43737808"></a>Specifies the rate limiting period. The value ranges from <strong id="b28317200102"><a name="b28317200102"></a><a name="b28317200102"></a>0</strong> seconds to <strong id="b208392061018"><a name="b208392061018"></a><a name="b208392061018"></a>2<sup id="sup1583420121014"><a name="sup1583420121014"></a><a name="sup1583420121014"></a>32</sup></strong> seconds.</p>
</td>
</tr>
<tr id="row58095956"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p8152009"><a name="p8152009"></a><a name="p8152009"></a>lock_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p56332978"><a name="p56332978"></a><a name="p56332978"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p66677368"><a name="p66677368"></a><a name="p66677368"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p32157698"><a name="p32157698"></a><a name="p32157698"></a>Specifies the lock duration. The value ranges from <strong id="b4469437151015_1"><a name="b4469437151015_1"></a><a name="b4469437151015_1"></a>0</strong> seconds to <strong id="b846973771011_1"><a name="b846973771011_1"></a><a name="b846973771011_1"></a>2<sup id="sup104771137131015_1"><a name="sup104771137131015_1"></a><a name="sup104771137131015_1"></a>32</sup></strong> seconds.</p>
</td>
</tr>
<tr id="row20983828"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p21968512"><a name="p21968512"></a><a name="p21968512"></a>tag_type</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p34619044"><a name="p34619044"></a><a name="p34619044"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p52679209"><a name="p52679209"></a><a name="p52679209"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p71571255171014"><a name="p71571255171014"></a><a name="p71571255171014"></a>Specifies the rate limit mode.</p>
<a name="ul555831610497"></a><a name="ul555831610497"></a><ul id="ul555831610497"><li><span class="parmvalue" id="parmvalue102056106130"><a name="parmvalue102056106130"></a><a name="parmvalue102056106130"></a><b>ip</b></span>: A web visitor is identified by the IP address.</li><li><span class="parmvalue" id="parmvalue19822135092819"><a name="parmvalue19822135092819"></a><a name="parmvalue19822135092819"></a><b>cookie</b></span>: A web visitor is identified by the cookie key value.</li><li><span class="parmvalue" id="parmvalue1380814330278"><a name="parmvalue1380814330278"></a><a name="parmvalue1380814330278"></a><b>other</b></span>: A web visitor is identified by the Referer field (user-defined request source).</li></ul>
</td>
</tr>
<tr id="row16873712"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p24593437"><a name="p24593437"></a><a name="p24593437"></a>tag_index</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p45911399"><a name="p45911399"></a><a name="p45911399"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p27835829"><a name="p27835829"></a><a name="p27835829"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p16557142835414"><a name="p16557142835414"></a><a name="p16557142835414"></a>If <span class="parmname" id="parmname5941525124816"><a name="parmname5941525124816"></a><a name="parmname5941525124816"></a><b>tag_type</b></span> is set to <strong id="b12941425204815"><a name="b12941425204815"></a><a name="b12941425204815"></a>cookie</strong>, this parameter indicates cookie name.</p>
</td>
</tr>
<tr id="row25442801"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p47601018"><a name="p47601018"></a><a name="p47601018"></a>tag_condition</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p30477219"><a name="p30477219"></a><a name="p30477219"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p52735636"><a name="p52735636"></a><a name="p52735636"></a><a href="#table1897210413559">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p155661828165416"><a name="p155661828165416"></a><a name="p155661828165416"></a>Specifies the <strong id="b1310131714256"><a name="b1310131714256"></a><a name="b1310131714256"></a>Referer</strong> (customized request source) field. This field is mandatory when <span class="parmvalue" id="parmvalue12106017142520"><a name="parmvalue12106017142520"></a><a name="parmvalue12106017142520"></a><b>tag_type</b></span> is set to <span class="parmvalue" id="parmvalue10107141715255"><a name="parmvalue10107141715255"></a><a name="parmvalue10107141715255"></a><b>other</b></span>.</p>
</td>
</tr>
<tr id="row12918005"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p39725486"><a name="p39725486"></a><a name="p39725486"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p63647832"><a name="p63647832"></a><a name="p63647832"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p55200795"><a name="p55200795"></a><a name="p55200795"></a><a href="#table3660351175718">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p42079390"><a name="p42079390"></a><a name="p42079390"></a>Specifies the action taken when the number of requests reaches the upper limit.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tag\_condition**

<a name="table1897210413559"></a>
<table><thead align="left"><tr id="row498264125512"><th class="cellrowborder" valign="top" width="30.010000000000005%" id="mcps1.2.5.1.1"><p id="p179858412553"><a name="p179858412553"></a><a name="p179858412553"></a><strong id="b109251511154213"><a name="b109251511154213"></a><a name="b109251511154213"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.55%" id="mcps1.2.5.1.2"><p id="p3506142418818"><a name="p3506142418818"></a><a name="p3506142418818"></a><strong id="b10324145614294_3"><a name="b10324145614294_3"></a><a name="b10324145614294_3"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.640000000000004%" id="mcps1.2.5.1.3"><p id="p20987841105519"><a name="p20987841105519"></a><a name="p20987841105519"></a><strong id="b8548111404210"><a name="b8548111404210"></a><a name="b8548111404210"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.800000000000004%" id="mcps1.2.5.1.4"><p id="p18992541175512"><a name="p18992541175512"></a><a name="p18992541175512"></a><strong id="b20338216144212"><a name="b20338216144212"></a><a name="b20338216144212"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row316718559556"><td class="cellrowborder" valign="top" width="30.010000000000005%" headers="mcps1.2.5.1.1 "><p id="p129251153125517"><a name="p129251153125517"></a><a name="p129251153125517"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="20.55%" headers="mcps1.2.5.1.2 "><p id="p05066243817"><a name="p05066243817"></a><a name="p05066243817"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.640000000000004%" headers="mcps1.2.5.1.3 "><p id="p18928155325515"><a name="p18928155325515"></a><a name="p18928155325515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.800000000000004%" headers="mcps1.2.5.1.4 "><p id="p976814616116"><a name="p976814616116"></a><a name="p976814616116"></a>Specifies the category. The value is <strong id="b479314264486"><a name="b479314264486"></a><a name="b479314264486"></a>Referer</strong>.</p>
<p id="p67691946516"><a name="p67691946516"></a><a name="p67691946516"></a>This parameter is mandatory when the <strong id="b1229453318443"><a name="b1229453318443"></a><a name="b1229453318443"></a>tag_condition</strong> field is transferred.</p>
</td>
</tr>
<tr id="row816515556552"><td class="cellrowborder" valign="top" width="30.010000000000005%" headers="mcps1.2.5.1.1 "><p id="p159555533556"><a name="p159555533556"></a><a name="p159555533556"></a>contents</p>
</td>
<td class="cellrowborder" valign="top" width="20.55%" headers="mcps1.2.5.1.2 "><p id="p150617241883"><a name="p150617241883"></a><a name="p150617241883"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.640000000000004%" headers="mcps1.2.5.1.3 "><p id="p1895915385512"><a name="p1895915385512"></a><a name="p1895915385512"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="36.800000000000004%" headers="mcps1.2.5.1.4 "><p id="p29649538557"><a name="p29649538557"></a><a name="p29649538557"></a>Specifies the category content.</p>
<p id="p195393569110"><a name="p195393569110"></a><a name="p195393569110"></a>The format is as follows: <strong id="b177054316299"><a name="b177054316299"></a><a name="b177054316299"></a>http://www.example.com/path</strong>.</p>
<p id="p145413566113"><a name="p145413566113"></a><a name="p145413566113"></a>This parameter is mandatory when the <strong id="b8132124017515"><a name="b8132124017515"></a><a name="b8132124017515"></a>tag_condition</strong> field is transferred. Currently, only one value is accepted. </p>
</td>
</tr>
</tbody>
</table>

**Table  4** **action**

<a name="table3660351175718"></a>
<table><thead align="left"><tr id="row13670125155718"><th class="cellrowborder" valign="top" width="34.29%" id="mcps1.2.5.1.1"><p id="p166741051165714"><a name="p166741051165714"></a><a name="p166741051165714"></a><strong id="b342414416514"><a name="b342414416514"></a><a name="b342414416514"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.91%" id="mcps1.2.5.1.2"><p id="p122672012482"><a name="p122672012482"></a><a name="p122672012482"></a><strong id="b10324145614294_5"><a name="b10324145614294_5"></a><a name="b10324145614294_5"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.3"><p id="p1868015111574"><a name="p1868015111574"></a><a name="p1868015111574"></a><strong id="b1341144815117"><a name="b1341144815117"></a><a name="b1341144815117"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.8%" id="mcps1.2.5.1.4"><p id="p16684751165717"><a name="p16684751165717"></a><a name="p16684751165717"></a><strong id="b1796784912513"><a name="b1796784912513"></a><a name="b1796784912513"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row487919825816"><td class="cellrowborder" valign="top" width="34.29%" headers="mcps1.2.5.1.1 "><p id="p9786157105816"><a name="p9786157105816"></a><a name="p9786157105816"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.2.5.1.2 "><p id="p026701194814"><a name="p026701194814"></a><a name="p026701194814"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p0791171581"><a name="p0791171581"></a><a name="p0791171581"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p154031329171813"><a name="p154031329171813"></a><a name="p154031329171813"></a>Specifies the action. The default value is <span class="parmvalue" id="parmvalue8808821161015"><a name="parmvalue8808821161015"></a><a name="parmvalue8808821161015"></a><b>block</b></span>.</p>
<a name="ul661483971811"></a><a name="ul661483971811"></a><ul id="ul661483971811"><li><strong id="b1843463134514"><a name="b1843463134514"></a><a name="b1843463134514"></a>block</strong>: block the requests.</li><li><span class="parmvalue" id="parmvalue14833818184116"><a name="parmvalue14833818184116"></a><a name="parmvalue14833818184116"></a><b>captcha</b></span>: Verification code. The user needs to enter the correct verification code after blocking to restore the correct access page.</li></ul>
<p id="p1716414522309"><a name="p1716414522309"></a><a name="p1716414522309"></a>The default value is <strong id="b63647164518"><a name="b63647164518"></a><a name="b63647164518"></a>block</strong>.</p>
<p id="p26661424422"><a name="p26661424422"></a><a name="p26661424422"></a>If <strong id="b14508284486"><a name="b14508284486"></a><a name="b14508284486"></a>tag_type</strong> is set to <strong id="b950172811486"><a name="b950172811486"></a><a name="b950172811486"></a>other</strong>, this parameter value can only be <strong id="b1552928154811"><a name="b1552928154811"></a><a name="b1552928154811"></a>block</strong>.</p>
</td>
</tr>
<tr id="row15877178135818"><td class="cellrowborder" valign="top" width="34.29%" headers="mcps1.2.5.1.1 "><p id="p2799197175818"><a name="p2799197175818"></a><a name="p2799197175818"></a>detail</p>
</td>
<td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.2.5.1.2 "><p id="p82672117485"><a name="p82672117485"></a><a name="p82672117485"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p178031872584"><a name="p178031872584"></a><a name="p178031872584"></a><a href="#table1060217107105">Table 5</a></p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p880513714586"><a name="p880513714586"></a><a name="p880513714586"></a>Specifies the action details. If <strong id="b10522102910489"><a name="b10522102910489"></a><a name="b10522102910489"></a>detail</strong> is <strong id="b1052212297483"><a name="b1052212297483"></a><a name="b1052212297483"></a>null</strong>, the default block page is displayed by default.</p>
<p id="p63755381215"><a name="p63755381215"></a><a name="p63755381215"></a>This parameter is not required if <strong id="b156851230184820"><a name="b156851230184820"></a><a name="b156851230184820"></a>category</strong> is set to <strong id="b6686830164817"><a name="b6686830164817"></a><a name="b6686830164817"></a>captcha</strong>.</p>
<p id="p163782389220"><a name="p163782389220"></a><a name="p163782389220"></a>This parameter is required if <strong id="b19411031104814"><a name="b19411031104814"></a><a name="b19411031104814"></a>category</strong> is set to <strong id="b6941931194820"><a name="b6941931194820"></a><a name="b6941931194820"></a>block</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **detail**

<a name="table1060217107105"></a>
<table><thead align="left"><tr id="row1861251018106"><th class="cellrowborder" valign="top" width="34.61%" id="mcps1.2.5.1.1"><p id="p14615101021017"><a name="p14615101021017"></a><a name="p14615101021017"></a><strong id="b7731164345512"><a name="b7731164345512"></a><a name="b7731164345512"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.02%" id="mcps1.2.5.1.2"><p id="p712037099"><a name="p712037099"></a><a name="p712037099"></a><strong id="b10324145614294_7"><a name="b10324145614294_7"></a><a name="b10324145614294_7"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.57%" id="mcps1.2.5.1.3"><p id="p2619141061016"><a name="p2619141061016"></a><a name="p2619141061016"></a><strong id="b7533945165510"><a name="b7533945165510"></a><a name="b7533945165510"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.8%" id="mcps1.2.5.1.4"><p id="p10622171001012"><a name="p10622171001012"></a><a name="p10622171001012"></a><strong id="b21404477556_1"><a name="b21404477556_1"></a><a name="b21404477556_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1142418101020"><td class="cellrowborder" valign="top" width="34.61%" headers="mcps1.2.5.1.1 "><p id="p159981716141015"><a name="p159981716141015"></a><a name="p159981716141015"></a>response</p>
</td>
<td class="cellrowborder" valign="top" width="18.02%" headers="mcps1.2.5.1.2 "><p id="p51201479910"><a name="p51201479910"></a><a name="p51201479910"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="10.57%" headers="mcps1.2.5.1.3 "><p id="p62517141010"><a name="p62517141010"></a><a name="p62517141010"></a><a href="#table671153413914">Table 6</a></p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p651517191019"><a name="p651517191019"></a><a name="p651517191019"></a>Specifies the returned page.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **response**

<a name="table671153413914"></a>
<table><thead align="left"><tr id="row87235341695"><th class="cellrowborder" valign="top" width="35.010000000000005%" id="mcps1.2.5.1.1"><p id="p117313341294"><a name="p117313341294"></a><a name="p117313341294"></a><strong id="b458925111574"><a name="b458925111574"></a><a name="b458925111574"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.94%" id="mcps1.2.5.1.2"><p id="p32997211392"><a name="p32997211392"></a><a name="p32997211392"></a><strong id="b10324145614294_9"><a name="b10324145614294_9"></a><a name="b10324145614294_9"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.25%" id="mcps1.2.5.1.3"><p id="p107346349917"><a name="p107346349917"></a><a name="p107346349917"></a><strong id="b1931413546575"><a name="b1931413546575"></a><a name="b1931413546575"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.8%" id="mcps1.2.5.1.4"><p id="p773818346918"><a name="p773818346918"></a><a name="p773818346918"></a><strong id="b1382815525710"><a name="b1382815525710"></a><a name="b1382815525710"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row46995451391"><td class="cellrowborder" valign="top" width="35.010000000000005%" headers="mcps1.2.5.1.1 "><p id="p26435443911"><a name="p26435443911"></a><a name="p26435443911"></a>content_type</p>
</td>
<td class="cellrowborder" valign="top" width="17.94%" headers="mcps1.2.5.1.2 "><p id="p1129972111915"><a name="p1129972111915"></a><a name="p1129972111915"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="10.25%" headers="mcps1.2.5.1.3 "><p id="p76471144794"><a name="p76471144794"></a><a name="p76471144794"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p1265017441999"><a name="p1265017441999"></a><a name="p1265017441999"></a>Specifies the type of the returned page.</p>
<p id="p6652244595"><a name="p6652244595"></a><a name="p6652244595"></a>The options are <strong id="b5811123314482"><a name="b5811123314482"></a><a name="b5811123314482"></a>application/json</strong>, <strong id="b7812163324813"><a name="b7812163324813"></a><a name="b7812163324813"></a>text/html</strong>, and <strong id="b13812123313486"><a name="b13812123313486"></a><a name="b13812123313486"></a>text/xml</strong>.</p>
<p id="p2665132172918"><a name="p2665132172918"></a><a name="p2665132172918"></a>The default value is <strong id="b1861818363482"><a name="b1861818363482"></a><a name="b1861818363482"></a>application/json</strong>.</p>
</td>
</tr>
<tr id="row1669964520912"><td class="cellrowborder" valign="top" width="35.010000000000005%" headers="mcps1.2.5.1.1 "><p id="p86555442914"><a name="p86555442914"></a><a name="p86555442914"></a>content</p>
</td>
<td class="cellrowborder" valign="top" width="17.94%" headers="mcps1.2.5.1.2 "><p id="p18299182119910"><a name="p18299182119910"></a><a name="p18299182119910"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="10.25%" headers="mcps1.2.5.1.3 "><p id="p1365811441899"><a name="p1365811441899"></a><a name="p1365811441899"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p186601448918"><a name="p186601448918"></a><a name="p186601448918"></a>Specifies the content of the returned page.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section43239478"></a>

Response parameters

**Table  7**  Parameter description

<a name="table40294034"></a>
<table><thead align="left"><tr id="row225404"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p18257741"><a name="p18257741"></a><a name="p18257741"></a><strong id="b584914547594"><a name="b584914547594"></a><a name="b584914547594"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p2482084"><a name="p2482084"></a><a name="p2482084"></a><strong id="b1930235618599"><a name="b1930235618599"></a><a name="b1930235618599"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p66831078"><a name="p66831078"></a><a name="p66831078"></a><strong id="b11769257115919"><a name="b11769257115919"></a><a name="b11769257115919"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row64608796"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p65929964"><a name="p65929964"></a><a name="p65929964"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p38726877"><a name="p38726877"></a><a name="p38726877"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p49869334"><a name="p49869334"></a><a name="p49869334"></a>Specifies the ID of a CC attack protection rule.</p>
</td>
</tr>
<tr id="row46170830"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p48849735"><a name="p48849735"></a><a name="p48849735"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p64514461"><a name="p64514461"></a><a name="p64514461"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p58288823"><a name="p58288823"></a><a name="p58288823"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row54837361"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p12641261"><a name="p12641261"></a><a name="p12641261"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p17309217"><a name="p17309217"></a><a name="p17309217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p59869366"><a name="p59869366"></a><a name="p59869366"></a>Specifies the URL to which the rule applies, excluding a domain name.</p>
</td>
</tr>
<tr id="row1953388"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p24006773"><a name="p24006773"></a><a name="p24006773"></a>limit_num</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p65500466"><a name="p65500466"></a><a name="p65500466"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p3937548"><a name="p3937548"></a><a name="p3937548"></a>Specifies the number of requests allowed from a web visitor in a rate limiting period.</p>
</td>
</tr>
<tr id="row35437935"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p51900478"><a name="p51900478"></a><a name="p51900478"></a>limit_period</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p43189214"><a name="p43189214"></a><a name="p43189214"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p8665463"><a name="p8665463"></a><a name="p8665463"></a>Specifies the rate limiting period.</p>
</td>
</tr>
<tr id="row10880304"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p8889392"><a name="p8889392"></a><a name="p8889392"></a>lock_time</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p48952124"><a name="p48952124"></a><a name="p48952124"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p5699133"><a name="p5699133"></a><a name="p5699133"></a>Specifies the lock duration. The value ranges from <strong id="b4469437151015_3"><a name="b4469437151015_3"></a><a name="b4469437151015_3"></a>0</strong> seconds to <strong id="b846973771011_3"><a name="b846973771011_3"></a><a name="b846973771011_3"></a>2<sup id="sup104771137131015_3"><a name="sup104771137131015_3"></a><a name="sup104771137131015_3"></a>32</sup></strong> seconds.</p>
</td>
</tr>
<tr id="row51292205"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p61027960"><a name="p61027960"></a><a name="p61027960"></a>tag_type</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p44317740"><a name="p44317740"></a><a name="p44317740"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p32967151"><a name="p32967151"></a><a name="p32967151"></a>Specifies the tag object type. The value can be <strong id="b22651513742"><a name="b22651513742"></a><a name="b22651513742"></a>cookie</strong>, <strong id="b358610181148"><a name="b358610181148"></a><a name="b358610181148"></a>ip</strong>, or <strong id="b156261425447"><a name="b156261425447"></a><a name="b156261425447"></a>other</strong>.</p>
</td>
</tr>
<tr id="row28268911"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p8080463"><a name="p8080463"></a><a name="p8080463"></a>tag_index</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p50537747"><a name="p50537747"></a><a name="p50537747"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p67025700"><a name="p67025700"></a><a name="p67025700"></a>If <strong id="b15432136112"><a name="b15432136112"></a><a name="b15432136112"></a>tag_type</strong> is set to <strong id="b144483315119"><a name="b144483315119"></a><a name="b144483315119"></a>cookie</strong>, <strong id="b174486311119"><a name="b174486311119"></a><a name="b174486311119"></a>index</strong> indicates cookie name.</p>
</td>
</tr>
<tr id="row66360388"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p6482354"><a name="p6482354"></a><a name="p6482354"></a>tag_condition</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p55308705"><a name="p55308705"></a><a name="p55308705"></a><a href="#table2115782102">Table 8</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p50820153"><a name="p50820153"></a><a name="p50820153"></a>This field is valid only when <strong id="b16925852201619"><a name="b16925852201619"></a><a name="b16925852201619"></a>tag_type</strong> is set to <strong id="b247513451544"><a name="b247513451544"></a><a name="b247513451544"></a>other</strong>.</p>
</td>
</tr>
<tr id="row13663579"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p33008137"><a name="p33008137"></a><a name="p33008137"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p56413415"><a name="p56413415"></a><a name="p56413415"></a><a href="#table191681818102">Table 9</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p6083869"><a name="p6083869"></a><a name="p6083869"></a>Specifies the action taken when the number of requests reaches the upper limit.</p>
</td>
</tr>
<tr id="row26058851"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p30392200"><a name="p30392200"></a><a name="p30392200"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p45849121"><a name="p45849121"></a><a name="p45849121"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p6250841"><a name="p6250841"></a><a name="p6250841"></a>Specifies the time when a CC attack protection rule is added.</p>
</td>
</tr>
<tr id="row1980831209"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p13111845101314"><a name="p13111845101314"></a><a name="p13111845101314"></a>default</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p1311245121318"><a name="p1311245121318"></a><a name="p1311245121318"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p8552015163214"><a name="p8552015163214"></a><a name="p8552015163214"></a>Specifies whether the rule is the default CC attack protection rule.</p>
<a name="ul1248751619599"></a><a name="ul1248751619599"></a><ul id="ul1248751619599"><li><strong id="en-us_topic_0193631170_b86402025123619"><a name="en-us_topic_0193631170_b86402025123619"></a><a name="en-us_topic_0193631170_b86402025123619"></a>true</strong>: The rule is the default CC attack protection rule created by the system when creating a domain name.</li><li><strong id="en-us_topic_0193631170_b1248153224120"><a name="en-us_topic_0193631170_b1248153224120"></a><a name="en-us_topic_0193631170_b1248153224120"></a>false</strong>: The rule is created by users.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  8** **tag\_condition**

<a name="table2115782102"></a>
<table><thead align="left"><tr id="row41268816100"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p121301861010"><a name="p121301861010"></a><a name="p121301861010"></a><strong id="b76373221776"><a name="b76373221776"></a><a name="b76373221776"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p101341485102"><a name="p101341485102"></a><a name="p101341485102"></a><strong id="b4171324373"><a name="b4171324373"></a><a name="b4171324373"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p11378851012"><a name="p11378851012"></a><a name="p11378851012"></a><strong id="b148831251718"><a name="b148831251718"></a><a name="b148831251718"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6140148141013"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p414218141013"><a name="p414218141013"></a><a name="p414218141013"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p121451586106"><a name="p121451586106"></a><a name="p121451586106"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1014916851017"><a name="p1014916851017"></a><a name="p1014916851017"></a>Specifies the category. The value is <strong id="b912994224814"><a name="b912994224814"></a><a name="b912994224814"></a>Referer</strong>.</p>
</td>
</tr>
<tr id="row18151118161015"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p015411861014"><a name="p015411861014"></a><a name="p015411861014"></a>contents</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1915812813106"><a name="p1915812813106"></a><a name="p1915812813106"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1416011851010"><a name="p1416011851010"></a><a name="p1416011851010"></a>Specifies the category content.</p>
</td>
</tr>
</tbody>
</table>

**Table  9** **action**

<a name="table191681818102"></a>
<table><thead align="left"><tr id="row121755812102"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p1417815817101"><a name="p1417815817101"></a><a name="p1417815817101"></a><strong id="b617717108810"><a name="b617717108810"></a><a name="b617717108810"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p14181783102"><a name="p14181783102"></a><a name="p14181783102"></a><strong id="b16114112982"><a name="b16114112982"></a><a name="b16114112982"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p1018516818105"><a name="p1018516818105"></a><a name="p1018516818105"></a><strong id="b1343114131389"><a name="b1343114131389"></a><a name="b1343114131389"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1518717871011"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1018878131019"><a name="p1018878131019"></a><a name="p1018878131019"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1519115815103"><a name="p1519115815103"></a><a name="p1519115815103"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p865312311309"><a name="p865312311309"></a><a name="p865312311309"></a>Specifies the action. The default value is <span class="parmvalue" id="parmvalue1294195515172"><a name="parmvalue1294195515172"></a><a name="parmvalue1294195515172"></a><b>block</b></span>.</p>
<a name="ul106561931103010"></a><a name="ul106561931103010"></a><ul id="ul106561931103010"><li><strong id="b19924183519569"><a name="b19924183519569"></a><a name="b19924183519569"></a>block</strong>: block the requests.</li><li><span class="parmvalue" id="parmvalue1277944413211"><a name="parmvalue1277944413211"></a><a name="parmvalue1277944413211"></a><b>captcha</b></span>: Verification code. The user needs to enter the correct verification code after blocking to restore the correct access page.</li></ul>
<p id="p6523943317"><a name="p6523943317"></a><a name="p6523943317"></a>The default value is <strong id="b14981767456"><a name="b14981767456"></a><a name="b14981767456"></a>block</strong>.</p>
<p id="p2196148191019"><a name="p2196148191019"></a><a name="p2196148191019"></a>If <strong id="b67631943184817"><a name="b67631943184817"></a><a name="b67631943184817"></a>tag_type</strong> is set to <strong id="b18763124313483"><a name="b18763124313483"></a><a name="b18763124313483"></a>other</strong>, this parameter value can only be <strong id="b167631243194817"><a name="b167631243194817"></a><a name="b167631243194817"></a>block</strong>.</p>
</td>
</tr>
<tr id="row719668141011"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p820148101013"><a name="p820148101013"></a><a name="p820148101013"></a>detail</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p142035816105"><a name="p142035816105"></a><a name="p142035816105"></a><a href="#table4421441182116">Table 10</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1207138141010"><a name="p1207138141010"></a><a name="p1207138141010"></a>Specifies the action details. If <strong id="b1918924614811"><a name="b1918924614811"></a><a name="b1918924614811"></a>detail</strong> is <strong id="b818915462484"><a name="b818915462484"></a><a name="b818915462484"></a>null</strong>, the default block page is displayed by default.</p>
</td>
</tr>
</tbody>
</table>

**Table  10** **detail**

<a name="table4421441182116"></a>
<table><thead align="left"><tr id="row056104110213"><th class="cellrowborder" valign="top" width="32.96%" id="mcps1.2.5.1.1"><p id="p159134182113"><a name="p159134182113"></a><a name="p159134182113"></a><strong id="b87111834113313"><a name="b87111834113313"></a><a name="b87111834113313"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.439999999999998%" id="mcps1.2.5.1.2"><p id="p36114122116"><a name="p36114122116"></a><a name="p36114122116"></a><strong id="b10324145614294_11"><a name="b10324145614294_11"></a><a name="b10324145614294_11"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.5.1.3"><p id="p76616416215"><a name="p76616416215"></a><a name="p76616416215"></a><strong id="b035917586297_3"><a name="b035917586297_3"></a><a name="b035917586297_3"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.25%" id="mcps1.2.5.1.4"><p id="p769114172111"><a name="p769114172111"></a><a name="p769114172111"></a><strong id="b21404477556_3"><a name="b21404477556_3"></a><a name="b21404477556_3"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row117454142116"><td class="cellrowborder" valign="top" width="32.96%" headers="mcps1.2.5.1.1 "><p id="p107934162119"><a name="p107934162119"></a><a name="p107934162119"></a>response</p>
</td>
<td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="p18394172117"><a name="p18394172117"></a><a name="p18394172117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.3 "><p id="p38964162119"><a name="p38964162119"></a><a name="p38964162119"></a><a href="#table26606224461">Table 11</a></p>
</td>
<td class="cellrowborder" valign="top" width="30.25%" headers="mcps1.2.5.1.4 "><p id="p19614114219"><a name="p19614114219"></a><a name="p19614114219"></a>Specifies the returned page.</p>
</td>
</tr>
</tbody>
</table>

**Table  11** **response**

<a name="table26606224461"></a>
<table><thead align="left"><tr id="row5674522154620"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p206809222462"><a name="p206809222462"></a><a name="p206809222462"></a><strong id="b19963226111115"><a name="b19963226111115"></a><a name="b19963226111115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p146851122134613"><a name="p146851122134613"></a><a name="p146851122134613"></a><strong id="b19657228131116"><a name="b19657228131116"></a><a name="b19657228131116"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p186885225463"><a name="p186885225463"></a><a name="p186885225463"></a><strong id="b19791329121111"><a name="b19791329121111"></a><a name="b19791329121111"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row14691172244614"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1669210224468"><a name="p1669210224468"></a><a name="p1669210224468"></a>content_type</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p769718225468"><a name="p769718225468"></a><a name="p769718225468"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p470132274618"><a name="p470132274618"></a><a name="p470132274618"></a>Specifies the type of the returned page.</p>
<p id="p19703132284613"><a name="p19703132284613"></a><a name="p19703132284613"></a>The options are <strong id="b12889144711483"><a name="b12889144711483"></a><a name="b12889144711483"></a>application/json</strong>, <strong id="b1890247134816"><a name="b1890247134816"></a><a name="b1890247134816"></a>text/html</strong>, and <strong id="b989024718488"><a name="b989024718488"></a><a name="b989024718488"></a>text/xml</strong>.</p>
</td>
</tr>
<tr id="row770552264619"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p107121822184612"><a name="p107121822184612"></a><a name="p107121822184612"></a>content</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p871532216464"><a name="p871532216464"></a><a name="p871532216464"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p207195228469"><a name="p207195228469"></a><a name="p207195228469"></a>Specifies the content of the returned page.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section1457985113518"></a>

-   Request example

    ```
    {
      "path": "/abc1",
      "limit_num": 10,
      "limit_period": 60,
      "lock_time": "",
      "tag_type": "cookie",
      "tag_index": "sesssionid",
      "action": {
        "category": "block",
        "detail": {
          "response": {
            "content_type": "application/json",
            "content": "{\'error\':\'forbidden\}"
          }
        }
      }
    }
    ```


-   Response example

    ```
    {
      "id": "3a9b5c0f96784ec8abd8ba61a98064ef",
      "policy_id": "9tre832yf96784ec8abd8ba61a98064ef",
      "path": "/abc1",
      "limit_num": 10,
      "limit_period": 60,
      "lock_time": "",
      "tag_type": "cookie",
      "tag_index": "sesssionid",
      "action": {
        "category": "block",
        "detail": {
          "response": {
            "content_type": "application/json",
            "content": "{\"error\":\"forbidden\"}"
          }
        }
    },
      "timestamp": 1499817600,
       "default": false
    }
    ```


## Status Code<a name="section53610983"></a>

[Table 12](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  12**  Status code

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

