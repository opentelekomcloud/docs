# Adding a CC Attack Protection Rule<a name="EN-US_TOPIC_0193631135"></a>

## Function Description<a name="section326588"></a>

This API is used to add a CC attack protection rule.

## URI<a name="section2939295"></a>

-   URI format

    POST  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/cc

-   Parameter description

    **Table  1**  Path parameters

    <a name="table53523322"></a>
    <table><thead align="left"><tr id="row9120597"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p570920"><a name="p570920"></a><a name="p570920"></a><strong id="b165144145385"><a name="b165144145385"></a><a name="b165144145385"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p46244539"><a name="p46244539"></a><a name="p46244539"></a><strong id="b926571683814"><a name="b926571683814"></a><a name="b926571683814"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p54820150"><a name="p54820150"></a><a name="p54820150"></a><strong id="b781361715383"><a name="b781361715383"></a><a name="b781361715383"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p11247170"><a name="p11247170"></a><a name="p11247170"></a><strong id="b139819205384"><a name="b139819205384"></a><a name="b139819205384"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38605574"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p40043819"><a name="p40043819"></a><a name="p40043819"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p22323929"><a name="p22323929"></a><a name="p22323929"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p63407799"><a name="p63407799"></a><a name="p63407799"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p35758061"><a name="p35758061"></a><a name="p35758061"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row53387097"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p29387591"><a name="p29387591"></a><a name="p29387591"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p31584674"><a name="p31584674"></a><a name="p31584674"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p8221777"><a name="p8221777"></a><a name="p8221777"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p61984189"><a name="p61984189"></a><a name="p61984189"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section26453657"></a>

Request parameters

**Table  2**  Parameter description

<a name="table65657065"></a>
<table><thead align="left"><tr id="row49768945"><th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.2.5.1.1"><p id="p4752708"><a name="p4752708"></a><a name="p4752708"></a><strong id="b1227343811381"><a name="b1227343811381"></a><a name="b1227343811381"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.2"><p id="p49425105"><a name="p49425105"></a><a name="p49425105"></a><strong id="b131033407387"><a name="b131033407387"></a><a name="b131033407387"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="p44010558"><a name="p44010558"></a><a name="p44010558"></a><strong id="b165724273814"><a name="b165724273814"></a><a name="b165724273814"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.5.1.4"><p id="p8085427"><a name="p8085427"></a><a name="p8085427"></a><strong id="b17323154443814"><a name="b17323154443814"></a><a name="b17323154443814"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5659985"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p55805606"><a name="p55805606"></a><a name="p55805606"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p23960215"><a name="p23960215"></a><a name="p23960215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p61729294"><a name="p61729294"></a><a name="p61729294"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p13524152875412"><a name="p13524152875412"></a><a name="p13524152875412"></a>Specifies the URL to which the rule applies, excluding a domain name.</p>
<a name="ul20810143683616"></a><a name="ul20810143683616"></a><ul id="ul20810143683616"><li>Prefix match: The path ending with * indicates that the path is used as a prefix.<p id="li315614594312p0"><a name="li315614594312p0"></a><a name="li315614594312p0"></a>For example, if the path to be protected is <strong id="b346171102411"><a name="b346171102411"></a><a name="b346171102411"></a>/admin/test.php</strong> or <strong id="b1146311122411"><a name="b1146311122411"></a><a name="b1146311122411"></a>/adminabc</strong>, set <strong id="b1146171162414"><a name="b1146171162414"></a><a name="b1146171162414"></a>Path</strong> to <span class="parmvalue" id="parmvalue14671116240"><a name="parmvalue14671116240"></a><a name="parmvalue14671116240"></a><b>/admin*</b></span>.</p>
</li><li>Exact match: The path to be entered must match the path to be protected.<p id="p1285333620361"><a name="p1285333620361"></a><a name="p1285333620361"></a>If the path to be protected is <span class="parmvalue" id="parmvalue13116135814272"><a name="parmvalue13116135814272"></a><a name="parmvalue13116135814272"></a><b>/admin</b></span>, set <strong id="b911610585273"><a name="b911610585273"></a><a name="b911610585273"></a>url</strong> to <span class="parmvalue" id="parmvalue7116205892715"><a name="parmvalue7116205892715"></a><a name="parmvalue7116205892715"></a><b>/admin</b></span>.</p>
</li></ul>
</td>
</tr>
<tr id="row37716470"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p35135206"><a name="p35135206"></a><a name="p35135206"></a>limit_num</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p27379447"><a name="p27379447"></a><a name="p27379447"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p3142736"><a name="p3142736"></a><a name="p3142736"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p53235098"><a name="p53235098"></a><a name="p53235098"></a>Specifies the number of requests allowed from a web visitor in a rate limiting period. The value ranges from <strong id="b1534913774517"><a name="b1534913774517"></a><a name="b1534913774517"></a>0</strong> to <strong id="b19685134414455"><a name="b19685134414455"></a><a name="b19685134414455"></a>2<sup id="sup924844444417"><a name="sup924844444417"></a><a name="sup924844444417"></a>32</sup></strong>.</p>
</td>
</tr>
<tr id="row9353841"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p19463655"><a name="p19463655"></a><a name="p19463655"></a>limit_period</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p33052193"><a name="p33052193"></a><a name="p33052193"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p59981959"><a name="p59981959"></a><a name="p59981959"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p26700547"><a name="p26700547"></a><a name="p26700547"></a>Specifies the rate limiting period. The value ranges from <strong id="b187081010174513"><a name="b187081010174513"></a><a name="b187081010174513"></a>0</strong> seconds to <strong id="b193741414513"><a name="b193741414513"></a><a name="b193741414513"></a>2<sup id="sup177124118246"><a name="sup177124118246"></a><a name="sup177124118246"></a>32</sup></strong> seconds.</p>
</td>
</tr>
<tr id="row38978331"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p3128272"><a name="p3128272"></a><a name="p3128272"></a>lock_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p52063502"><a name="p52063502"></a><a name="p52063502"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p56394108"><a name="p56394108"></a><a name="p56394108"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p4520002"><a name="p4520002"></a><a name="p4520002"></a>Specifies the lock duration. The value ranges from <strong id="b15741020114620"><a name="b15741020114620"></a><a name="b15741020114620"></a>0</strong> seconds to <strong id="b1535112418464"><a name="b1535112418464"></a><a name="b1535112418464"></a>2<sup id="sup89298419460"><a name="sup89298419460"></a><a name="sup89298419460"></a>32</sup></strong> seconds.</p>
</td>
</tr>
<tr id="row40680022"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p6747476"><a name="p6747476"></a><a name="p6747476"></a>tag_type</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p9674687"><a name="p9674687"></a><a name="p9674687"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p45452158"><a name="p45452158"></a><a name="p45452158"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p71571255171014"><a name="p71571255171014"></a><a name="p71571255171014"></a>Specifies the rate limit mode.</p>
<a name="ul555831610497"></a><a name="ul555831610497"></a><ul id="ul555831610497"><li><span class="parmvalue" id="parmvalue1896344320463"><a name="parmvalue1896344320463"></a><a name="parmvalue1896344320463"></a><b>ip</b></span>: A web visitor is identified by the IP address.</li><li><span class="parmvalue" id="parmvalue0776947204610"><a name="parmvalue0776947204610"></a><a name="parmvalue0776947204610"></a><b>cookie</b></span>: A web visitor is identified by the cookie key value.</li><li><span class="parmvalue" id="parmvalue678165316251"><a name="parmvalue678165316251"></a><a name="parmvalue678165316251"></a><b>other</b></span>: A web visitor is identified by the Referer field (user-defined request source).</li></ul>
</td>
</tr>
<tr id="row49953482"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p19700203"><a name="p19700203"></a><a name="p19700203"></a>tag_index</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p52212605"><a name="p52212605"></a><a name="p52212605"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p1362599"><a name="p1362599"></a><a name="p1362599"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p16557142835414"><a name="p16557142835414"></a><a name="p16557142835414"></a>If <span class="parmname" id="parmname4122162862114"><a name="parmname4122162862114"></a><a name="parmname4122162862114"></a><b>tag_type</b></span> is set to <strong id="b4667334154614"><a name="b4667334154614"></a><a name="b4667334154614"></a>cookie</strong>, this parameter indicates cookie name.</p>
</td>
</tr>
<tr id="row53811111"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p63732758"><a name="p63732758"></a><a name="p63732758"></a>tag_condition</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p62079769"><a name="p62079769"></a><a name="p62079769"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p62405401"><a name="p62405401"></a><a name="p62405401"></a><a href="#table1897210413559">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p155661828165416"><a name="p155661828165416"></a><a name="p155661828165416"></a>Specifies the <strong id="b2032511128233"><a name="b2032511128233"></a><a name="b2032511128233"></a>Referer</strong> (customized request source) field. This field is mandatory when <span class="parmvalue" id="parmvalue123346128238"><a name="parmvalue123346128238"></a><a name="parmvalue123346128238"></a><b>tag_type</b></span> is set to <span class="parmvalue" id="parmvalue12335161212319"><a name="parmvalue12335161212319"></a><a name="parmvalue12335161212319"></a><b>other</b></span>.</p>
</td>
</tr>
<tr id="row32159664"><td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.1 "><p id="p54795959"><a name="p54795959"></a><a name="p54795959"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.2 "><p id="p9287715"><a name="p9287715"></a><a name="p9287715"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p14107484"><a name="p14107484"></a><a name="p14107484"></a><a href="#table3660351175718">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.4 "><p id="p1855561"><a name="p1855561"></a><a name="p1855561"></a>Specifies the action taken when the number of requests reaches the upper limit.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tag\_condition**

<a name="table1897210413559"></a>
<table><thead align="left"><tr id="row498264125512"><th class="cellrowborder" valign="top" width="33.32%" id="mcps1.2.5.1.1"><p id="p179858412553"><a name="p179858412553"></a><a name="p179858412553"></a><strong id="b12839135584412"><a name="b12839135584412"></a><a name="b12839135584412"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.84%" id="mcps1.2.5.1.2"><p id="p62393252474"><a name="p62393252474"></a><a name="p62393252474"></a><strong id="b2095894981"><a name="b2095894981"></a><a name="b2095894981"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11.04%" id="mcps1.2.5.1.3"><p id="p20987841105519"><a name="p20987841105519"></a><a name="p20987841105519"></a><strong id="b144218581446"><a name="b144218581446"></a><a name="b144218581446"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.8%" id="mcps1.2.5.1.4"><p id="p18992541175512"><a name="p18992541175512"></a><a name="p18992541175512"></a><strong id="b115761059174412"><a name="b115761059174412"></a><a name="b115761059174412"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row316718559556"><td class="cellrowborder" valign="top" width="33.32%" headers="mcps1.2.5.1.1 "><p id="p129251153125517"><a name="p129251153125517"></a><a name="p129251153125517"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.2.5.1.2 "><p id="p11680211174712"><a name="p11680211174712"></a><a name="p11680211174712"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.04%" headers="mcps1.2.5.1.3 "><p id="p18928155325515"><a name="p18928155325515"></a><a name="p18928155325515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p976814616116"><a name="p976814616116"></a><a name="p976814616116"></a>Specifies the category. The value is <strong id="b1193510218433"><a name="b1193510218433"></a><a name="b1193510218433"></a>Referer</strong>.</p>
<p id="p67691946516"><a name="p67691946516"></a><a name="p67691946516"></a>This parameter is mandatory when the <strong id="b9655181054511"><a name="b9655181054511"></a><a name="b9655181054511"></a>tag_condition</strong> field is transferred.</p>
</td>
</tr>
<tr id="row816515556552"><td class="cellrowborder" valign="top" width="33.32%" headers="mcps1.2.5.1.1 "><p id="p159555533556"><a name="p159555533556"></a><a name="p159555533556"></a>contents</p>
</td>
<td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.2.5.1.2 "><p id="p168011117475"><a name="p168011117475"></a><a name="p168011117475"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.04%" headers="mcps1.2.5.1.3 "><p id="p1895915385512"><a name="p1895915385512"></a><a name="p1895915385512"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p29649538557"><a name="p29649538557"></a><a name="p29649538557"></a>Specifies the category content.</p>
<p id="p195393569110"><a name="p195393569110"></a><a name="p195393569110"></a>The format is as follows: <strong id="b10710161617020"><a name="b10710161617020"></a><a name="b10710161617020"></a>http://www.example.com/path</strong>.</p>
<p id="p145413566113"><a name="p145413566113"></a><a name="p145413566113"></a>This parameter is mandatory when the <strong id="b353622914519"><a name="b353622914519"></a><a name="b353622914519"></a>tag_condition</strong> field is transferred. Currently, only one value is accepted. </p>
</td>
</tr>
</tbody>
</table>

**Table  4** **action**

<a name="table3660351175718"></a>
<table><thead align="left"><tr id="row13670125155718"><th class="cellrowborder" valign="top" width="33.56%" id="mcps1.2.5.1.1"><p id="p166741051165714"><a name="p166741051165714"></a><a name="p166741051165714"></a><strong id="b8595737164512"><a name="b8595737164512"></a><a name="b8595737164512"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.93%" id="mcps1.2.5.1.2"><p id="p122672012482"><a name="p122672012482"></a><a name="p122672012482"></a><strong id="b62679161"><a name="b62679161"></a><a name="b62679161"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.71%" id="mcps1.2.5.1.3"><p id="p1868015111574"><a name="p1868015111574"></a><a name="p1868015111574"></a><strong id="b07721639124510"><a name="b07721639124510"></a><a name="b07721639124510"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.8%" id="mcps1.2.5.1.4"><p id="p16684751165717"><a name="p16684751165717"></a><a name="p16684751165717"></a><strong id="b5821743144514"><a name="b5821743144514"></a><a name="b5821743144514"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row487919825816"><td class="cellrowborder" valign="top" width="33.56%" headers="mcps1.2.5.1.1 "><p id="p9786157105816"><a name="p9786157105816"></a><a name="p9786157105816"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="18.93%" headers="mcps1.2.5.1.2 "><p id="p026701194814"><a name="p026701194814"></a><a name="p026701194814"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="10.71%" headers="mcps1.2.5.1.3 "><p id="p0791171581"><a name="p0791171581"></a><a name="p0791171581"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p154031329171813"><a name="p154031329171813"></a><a name="p154031329171813"></a>Specifies the action. The default value is <span class="parmvalue" id="parmvalue13790144324819"><a name="parmvalue13790144324819"></a><a name="parmvalue13790144324819"></a><b>block</b></span>.</p>
<a name="ul661483971811"></a><a name="ul661483971811"></a><ul id="ul661483971811"><li><strong id="b13237202818575"><a name="b13237202818575"></a><a name="b13237202818575"></a>block</strong>: block the requests.</li><li><span class="parmvalue" id="parmvalue196676212502"><a name="parmvalue196676212502"></a><a name="parmvalue196676212502"></a><b>captcha</b></span>: Verification code. The user needs to enter the correct verification code after blocking to restore the correct access page.</li></ul>
<p id="p077719328294"><a name="p077719328294"></a><a name="p077719328294"></a>The default value is <strong id="b1600125384316"><a name="b1600125384316"></a><a name="b1600125384316"></a>block</strong>.</p>
<p id="p552175163110"><a name="p552175163110"></a><a name="p552175163110"></a>If <strong id="b12153340101510"><a name="b12153340101510"></a><a name="b12153340101510"></a>tag_type</strong> is set to <strong id="b915374019150"><a name="b915374019150"></a><a name="b915374019150"></a>other</strong>, this parameter value can only be <strong id="b2153154071514"><a name="b2153154071514"></a><a name="b2153154071514"></a>block</strong>.</p>
</td>
</tr>
<tr id="row15877178135818"><td class="cellrowborder" valign="top" width="33.56%" headers="mcps1.2.5.1.1 "><p id="p2799197175818"><a name="p2799197175818"></a><a name="p2799197175818"></a>detail</p>
</td>
<td class="cellrowborder" valign="top" width="18.93%" headers="mcps1.2.5.1.2 "><p id="p82672117485"><a name="p82672117485"></a><a name="p82672117485"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="10.71%" headers="mcps1.2.5.1.3 "><p id="p178031872584"><a name="p178031872584"></a><a name="p178031872584"></a><a href="#table1060217107105">Table 5</a></p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p880513714586"><a name="p880513714586"></a><a name="p880513714586"></a>Specifies the action details. If <strong id="b73901957403"><a name="b73901957403"></a><a name="b73901957403"></a>detail</strong> is <strong id="b1939812571307"><a name="b1939812571307"></a><a name="b1939812571307"></a>null</strong>, the default block page is displayed by default.</p>
<p id="p63755381215"><a name="p63755381215"></a><a name="p63755381215"></a>This parameter is not required if <strong id="b13992181719151"><a name="b13992181719151"></a><a name="b13992181719151"></a>category</strong> is set to <strong id="b13992131771518"><a name="b13992131771518"></a><a name="b13992131771518"></a>captcha</strong>.</p>
<p id="p163782389220"><a name="p163782389220"></a><a name="p163782389220"></a>This parameter is required if <strong id="b839132221519"><a name="b839132221519"></a><a name="b839132221519"></a>category</strong> is set to <strong id="b1739172261514"><a name="b1739172261514"></a><a name="b1739172261514"></a>block</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **detail**

<a name="table1060217107105"></a>
<table><thead align="left"><tr id="row1861251018106"><th class="cellrowborder" valign="top" width="34.2%" id="mcps1.2.5.1.1"><p id="p14615101021017"><a name="p14615101021017"></a><a name="p14615101021017"></a><strong id="b7612742154611"><a name="b7612742154611"></a><a name="b7612742154611"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.02%" id="mcps1.2.5.1.2"><p id="p13498927551"><a name="p13498927551"></a><a name="p13498927551"></a><strong id="b413208824"><a name="b413208824"></a><a name="b413208824"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="9.98%" id="mcps1.2.5.1.3"><p id="p2619141061016"><a name="p2619141061016"></a><a name="p2619141061016"></a><strong id="b17992643114613"><a name="b17992643114613"></a><a name="b17992643114613"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.8%" id="mcps1.2.5.1.4"><p id="p10622171001012"><a name="p10622171001012"></a><a name="p10622171001012"></a><strong id="b1292845114619"><a name="b1292845114619"></a><a name="b1292845114619"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1142418101020"><td class="cellrowborder" valign="top" width="34.2%" headers="mcps1.2.5.1.1 "><p id="p159981716141015"><a name="p159981716141015"></a><a name="p159981716141015"></a>response</p>
</td>
<td class="cellrowborder" valign="top" width="19.02%" headers="mcps1.2.5.1.2 "><p id="p3498132175512"><a name="p3498132175512"></a><a name="p3498132175512"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="9.98%" headers="mcps1.2.5.1.3 "><p id="p62517141010"><a name="p62517141010"></a><a name="p62517141010"></a><a href="#table671153413914">Table 6</a></p>
</td>
<td class="cellrowborder" valign="top" width="36.8%" headers="mcps1.2.5.1.4 "><p id="p651517191019"><a name="p651517191019"></a><a name="p651517191019"></a>Specifies the returned page.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **response**

<a name="table671153413914"></a>
<table><thead align="left"><tr id="row87235341695"><th class="cellrowborder" valign="top" width="34.440000000000005%" id="mcps1.2.5.1.1"><p id="p117313341294"><a name="p117313341294"></a><a name="p117313341294"></a><strong id="b175419518468"><a name="b175419518468"></a><a name="b175419518468"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.330000000000002%" id="mcps1.2.5.1.2"><p id="p46641438125519"><a name="p46641438125519"></a><a name="p46641438125519"></a><strong id="b617189872"><a name="b617189872"></a><a name="b617189872"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="9.430000000000001%" id="mcps1.2.5.1.3"><p id="p107346349917"><a name="p107346349917"></a><a name="p107346349917"></a><strong id="b4650155384615"><a name="b4650155384615"></a><a name="b4650155384615"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.800000000000004%" id="mcps1.2.5.1.4"><p id="p773818346918"><a name="p773818346918"></a><a name="p773818346918"></a><strong id="b166601558467"><a name="b166601558467"></a><a name="b166601558467"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row46995451391"><td class="cellrowborder" valign="top" width="34.440000000000005%" headers="mcps1.2.5.1.1 "><p id="p26435443911"><a name="p26435443911"></a><a name="p26435443911"></a>content_type</p>
</td>
<td class="cellrowborder" valign="top" width="19.330000000000002%" headers="mcps1.2.5.1.2 "><p id="p1466453810554"><a name="p1466453810554"></a><a name="p1466453810554"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="9.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p76471144794"><a name="p76471144794"></a><a name="p76471144794"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.800000000000004%" headers="mcps1.2.5.1.4 "><p id="p1265017441999"><a name="p1265017441999"></a><a name="p1265017441999"></a>Specifies the type of the returned page.</p>
<p id="p6652244595"><a name="p6652244595"></a><a name="p6652244595"></a>The options are <strong id="b069217584713"><a name="b069217584713"></a><a name="b069217584713"></a>application/json</strong>, <strong id="b469310516479"><a name="b469310516479"></a><a name="b469310516479"></a>text/html</strong>, and <strong id="b146931518470"><a name="b146931518470"></a><a name="b146931518470"></a>text/xml</strong>.</p>
<p id="p8479161618275"><a name="p8479161618275"></a><a name="p8479161618275"></a>The default value is <strong id="b135161717113813"><a name="b135161717113813"></a><a name="b135161717113813"></a>application/json</strong>.</p>
</td>
</tr>
<tr id="row1669964520912"><td class="cellrowborder" valign="top" width="34.440000000000005%" headers="mcps1.2.5.1.1 "><p id="p86555442914"><a name="p86555442914"></a><a name="p86555442914"></a>content</p>
</td>
<td class="cellrowborder" valign="top" width="19.330000000000002%" headers="mcps1.2.5.1.2 "><p id="p10664103814553"><a name="p10664103814553"></a><a name="p10664103814553"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="9.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p1365811441899"><a name="p1365811441899"></a><a name="p1365811441899"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.800000000000004%" headers="mcps1.2.5.1.4 "><p id="p186601448918"><a name="p186601448918"></a><a name="p186601448918"></a>Specifies the content of the returned page.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section36756323"></a>

Response parameters

**Table  7**  Parameter description

<a name="table12775632"></a>
<table><thead align="left"><tr id="row23791917"><th class="cellrowborder" valign="top" width="35.27647235276473%" id="mcps1.2.4.1.1"><p id="p48097106"><a name="p48097106"></a><a name="p48097106"></a><strong id="b148591516154711"><a name="b148591516154711"></a><a name="b148591516154711"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.92750724927507%" id="mcps1.2.4.1.2"><p id="p3551528"><a name="p3551528"></a><a name="p3551528"></a><strong id="b334881964719"><a name="b334881964719"></a><a name="b334881964719"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p19238358"><a name="p19238358"></a><a name="p19238358"></a><strong id="b139719216476"><a name="b139719216476"></a><a name="b139719216476"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row18416568"><td class="cellrowborder" valign="top" width="35.27647235276473%" headers="mcps1.2.4.1.1 "><p id="p15347038"><a name="p15347038"></a><a name="p15347038"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="24.92750724927507%" headers="mcps1.2.4.1.2 "><p id="p35150536"><a name="p35150536"></a><a name="p35150536"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p28621150"><a name="p28621150"></a><a name="p28621150"></a>Specifies the ID of a CC attack protection rule.</p>
</td>
</tr>
<tr id="row56263766"><td class="cellrowborder" valign="top" width="35.27647235276473%" headers="mcps1.2.4.1.1 "><p id="p61071194"><a name="p61071194"></a><a name="p61071194"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.92750724927507%" headers="mcps1.2.4.1.2 "><p id="p47819711"><a name="p47819711"></a><a name="p47819711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p48191405"><a name="p48191405"></a><a name="p48191405"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row31069462"><td class="cellrowborder" valign="top" width="35.27647235276473%" headers="mcps1.2.4.1.1 "><p id="p33598499"><a name="p33598499"></a><a name="p33598499"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="24.92750724927507%" headers="mcps1.2.4.1.2 "><p id="p37123917"><a name="p37123917"></a><a name="p37123917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p9691986224"><a name="p9691986224"></a><a name="p9691986224"></a>Specifies the URL to which the rule applies.</p>
</td>
</tr>
<tr id="row18463575"><td class="cellrowborder" valign="top" width="35.27647235276473%" headers="mcps1.2.4.1.1 "><p id="p19154631"><a name="p19154631"></a><a name="p19154631"></a>limit_num</p>
</td>
<td class="cellrowborder" valign="top" width="24.92750724927507%" headers="mcps1.2.4.1.2 "><p id="p8021296"><a name="p8021296"></a><a name="p8021296"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p45745209"><a name="p45745209"></a><a name="p45745209"></a>Specifies the number of requests allowed from a web visitor in a rate limiting period.</p>
</td>
</tr>
<tr id="row9053697"><td class="cellrowborder" valign="top" width="35.27647235276473%" headers="mcps1.2.4.1.1 "><p id="p62260829"><a name="p62260829"></a><a name="p62260829"></a>limit_period</p>
</td>
<td class="cellrowborder" valign="top" width="24.92750724927507%" headers="mcps1.2.4.1.2 "><p id="p9962414"><a name="p9962414"></a><a name="p9962414"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p1649244"><a name="p1649244"></a><a name="p1649244"></a>Specifies the rate limiting period.</p>
</td>
</tr>
<tr id="row14843201"><td class="cellrowborder" valign="top" width="35.27647235276473%" headers="mcps1.2.4.1.1 "><p id="p61448645"><a name="p61448645"></a><a name="p61448645"></a>lock_time</p>
</td>
<td class="cellrowborder" valign="top" width="24.92750724927507%" headers="mcps1.2.4.1.2 "><p id="p11284312"><a name="p11284312"></a><a name="p11284312"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p41614117"><a name="p41614117"></a><a name="p41614117"></a>Specifies the lock duration. The value ranges from <strong id="b17741145323"><a name="b17741145323"></a><a name="b17741145323"></a>0</strong> seconds to <strong id="b117481353213"><a name="b117481353213"></a><a name="b117481353213"></a>2<sup id="sup107484511217"><a name="sup107484511217"></a><a name="sup107484511217"></a>32</sup></strong> seconds.</p>
</td>
</tr>
<tr id="row38982736"><td class="cellrowborder" valign="top" width="35.27647235276473%" headers="mcps1.2.4.1.1 "><p id="p3485028"><a name="p3485028"></a><a name="p3485028"></a>tag_type</p>
</td>
<td class="cellrowborder" valign="top" width="24.92750724927507%" headers="mcps1.2.4.1.2 "><p id="p13851845"><a name="p13851845"></a><a name="p13851845"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p294271602612"><a name="p294271602612"></a><a name="p294271602612"></a>Specifies the rate limit mode.</p>
<a name="ul20943116192616"></a><a name="ul20943116192616"></a><ul id="ul20943116192616"><li><span class="parmvalue" id="parmvalue43831357165312"><a name="parmvalue43831357165312"></a><a name="parmvalue43831357165312"></a><b>ip</b></span>: A web visitor is identified by the IP address.</li><li><span class="parmvalue" id="parmvalue2085960115417"><a name="parmvalue2085960115417"></a><a name="parmvalue2085960115417"></a><b>cookie</b></span>: A web visitor is identified by the cookie key value.</li><li><span class="parmvalue" id="parmvalue6922115914914"><a name="parmvalue6922115914914"></a><a name="parmvalue6922115914914"></a><b>other</b></span>: A web visitor is identified by the Referer field (user-defined request source).</li></ul>
</td>
</tr>
<tr id="row31665451"><td class="cellrowborder" valign="top" width="35.27647235276473%" headers="mcps1.2.4.1.1 "><p id="p14764778"><a name="p14764778"></a><a name="p14764778"></a>tag_index</p>
</td>
<td class="cellrowborder" valign="top" width="24.92750724927507%" headers="mcps1.2.4.1.2 "><p id="p55096402"><a name="p55096402"></a><a name="p55096402"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p143021136202715"><a name="p143021136202715"></a><a name="p143021136202715"></a>If <span class="parmname" id="parmname16787108184717"><a name="parmname16787108184717"></a><a name="parmname16787108184717"></a><b>tag_type</b></span> is set to <strong id="b27877864716"><a name="b27877864716"></a><a name="b27877864716"></a>cookie</strong>, this parameter indicates cookie name.</p>
</td>
</tr>
<tr id="row34176603"><td class="cellrowborder" valign="top" width="35.27647235276473%" headers="mcps1.2.4.1.1 "><p id="p16841487"><a name="p16841487"></a><a name="p16841487"></a>tag_condition</p>
</td>
<td class="cellrowborder" valign="top" width="24.92750724927507%" headers="mcps1.2.4.1.2 "><p id="p21983207"><a name="p21983207"></a><a name="p21983207"></a><a href="#table2115782102">Table 8</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p13308143614277"><a name="p13308143614277"></a><a name="p13308143614277"></a>Specifies the <strong id="b102982573216"><a name="b102982573216"></a><a name="b102982573216"></a>Referer</strong> (customized request source) field. This field is returned when <span class="parmname" id="parmname8369183532219"><a name="parmname8369183532219"></a><a name="parmname8369183532219"></a><b>tag_type</b></span> is set to <span class="parmvalue" id="parmvalue229816570211"><a name="parmvalue229816570211"></a><a name="parmvalue229816570211"></a><b>other</b></span>.</p>
</td>
</tr>
<tr id="row54202760"><td class="cellrowborder" valign="top" width="35.27647235276473%" headers="mcps1.2.4.1.1 "><p id="p28347443"><a name="p28347443"></a><a name="p28347443"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="24.92750724927507%" headers="mcps1.2.4.1.2 "><p id="p14441522"><a name="p14441522"></a><a name="p14441522"></a><a href="#table191681818102">Table 9</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p28912622"><a name="p28912622"></a><a name="p28912622"></a>Specifies the action taken when the number of requests reaches the upper limit.</p>
</td>
</tr>
<tr id="row15406836"><td class="cellrowborder" valign="top" width="35.27647235276473%" headers="mcps1.2.4.1.1 "><p id="p39994208"><a name="p39994208"></a><a name="p39994208"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="24.92750724927507%" headers="mcps1.2.4.1.2 "><p id="p18305412"><a name="p18305412"></a><a name="p18305412"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p6343433"><a name="p6343433"></a><a name="p6343433"></a>Specifies the time when a CC attack protection rule is added.</p>
</td>
</tr>
<tr id="row189505580158"><td class="cellrowborder" valign="top" width="35.27647235276473%" headers="mcps1.2.4.1.1 "><p id="p13111845101314"><a name="p13111845101314"></a><a name="p13111845101314"></a>default</p>
</td>
<td class="cellrowborder" valign="top" width="24.92750724927507%" headers="mcps1.2.4.1.2 "><p id="p1311245121318"><a name="p1311245121318"></a><a name="p1311245121318"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p8552015163214"><a name="p8552015163214"></a><a name="p8552015163214"></a>Specifies whether the rule is the default CC attack protection rule.</p>
<a name="ul1248751619599"></a><a name="ul1248751619599"></a><ul id="ul1248751619599"><li><strong id="en-us_topic_0193631170_b86402025123619"><a name="en-us_topic_0193631170_b86402025123619"></a><a name="en-us_topic_0193631170_b86402025123619"></a>true</strong>: The rule is the default CC attack protection rule created by the system when creating a domain name.</li><li><strong id="en-us_topic_0193631170_b1248153224120"><a name="en-us_topic_0193631170_b1248153224120"></a><a name="en-us_topic_0193631170_b1248153224120"></a>false</strong>: The rule is created by users.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  8** **tag\_condition**

<a name="table2115782102"></a>
<table><thead align="left"><tr id="row41268816100"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p121301861010"><a name="p121301861010"></a><a name="p121301861010"></a><strong id="b13951132454915"><a name="b13951132454915"></a><a name="b13951132454915"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p101341485102"><a name="p101341485102"></a><a name="p101341485102"></a><strong id="b148449264493"><a name="b148449264493"></a><a name="b148449264493"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p11378851012"><a name="p11378851012"></a><a name="p11378851012"></a><strong id="b1742202814495"><a name="b1742202814495"></a><a name="b1742202814495"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6140148141013"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p414218141013"><a name="p414218141013"></a><a name="p414218141013"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p121451586106"><a name="p121451586106"></a><a name="p121451586106"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1014916851017"><a name="p1014916851017"></a><a name="p1014916851017"></a>Specifies the category. The value is <strong id="b1087931712473"><a name="b1087931712473"></a><a name="b1087931712473"></a>Referer</strong>.</p>
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
<table><thead align="left"><tr id="row121755812102"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p1417815817101"><a name="p1417815817101"></a><a name="p1417815817101"></a><strong id="b48720453491"><a name="b48720453491"></a><a name="b48720453491"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p14181783102"><a name="p14181783102"></a><a name="p14181783102"></a><strong id="b1341174620492"><a name="b1341174620492"></a><a name="b1341174620492"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p1018516818105"><a name="p1018516818105"></a><a name="p1018516818105"></a><strong id="b9108134814912"><a name="b9108134814912"></a><a name="b9108134814912"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1518717871011"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1018878131019"><a name="p1018878131019"></a><a name="p1018878131019"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1519115815103"><a name="p1519115815103"></a><a name="p1519115815103"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p14193788102"><a name="p14193788102"></a><a name="p14193788102"></a>Specifies the action. The default value is <span class="parmvalue" id="parmvalue343613556542"><a name="parmvalue343613556542"></a><a name="parmvalue343613556542"></a><b>block</b></span>.</p>
<a name="ul20449173612297"></a><a name="ul20449173612297"></a><ul id="ul20449173612297"><li><strong id="b1978244335717"><a name="b1978244335717"></a><a name="b1978244335717"></a>block</strong>: block the requests.</li><li><span class="parmvalue" id="parmvalue174001532164712"><a name="parmvalue174001532164712"></a><a name="parmvalue174001532164712"></a><b>captcha</b></span>: Verification code. The user needs to enter the correct verification code after blocking to restore the correct access page.</li></ul>
<p id="p169913477299"><a name="p169913477299"></a><a name="p169913477299"></a>The default value is <strong id="b1961556154311"><a name="b1961556154311"></a><a name="b1961556154311"></a>block</strong>.</p>
<p id="p596559152913"><a name="p596559152913"></a><a name="p596559152913"></a>If <strong id="b14881021194716"><a name="b14881021194716"></a><a name="b14881021194716"></a>tag_type</strong> is set to <strong id="b1590182112473"><a name="b1590182112473"></a><a name="b1590182112473"></a>other</strong>, this parameter value can only be <strong id="b9901321184717"><a name="b9901321184717"></a><a name="b9901321184717"></a>block</strong>.</p>
</td>
</tr>
<tr id="row719668141011"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p820148101013"><a name="p820148101013"></a><a name="p820148101013"></a>detail</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p142035816105"><a name="p142035816105"></a><a name="p142035816105"></a><a href="#table994172920135">Table 10</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1207138141010"><a name="p1207138141010"></a><a name="p1207138141010"></a>Specifies the action details. If <strong id="b3471626124711"><a name="b3471626124711"></a><a name="b3471626124711"></a>detail</strong> is <strong id="b114852634717"><a name="b114852634717"></a><a name="b114852634717"></a>null</strong>, the default block page is displayed by default.</p>
</td>
</tr>
</tbody>
</table>

**Table  10** **detail**

<a name="table994172920135"></a>
<table><thead align="left"><tr id="row161078297139"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p1611112296136"><a name="p1611112296136"></a><a name="p1611112296136"></a><strong id="b13306101375011"><a name="b13306101375011"></a><a name="b13306101375011"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p10115529101313"><a name="p10115529101313"></a><a name="p10115529101313"></a><strong id="b68821314115015"><a name="b68821314115015"></a><a name="b68821314115015"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p4118152914135"><a name="p4118152914135"></a><a name="p4118152914135"></a><strong id="b1922491615017"><a name="b1922491615017"></a><a name="b1922491615017"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1112013297131"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1312319291137"><a name="p1312319291137"></a><a name="p1312319291137"></a>response</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p6128172991319"><a name="p6128172991319"></a><a name="p6128172991319"></a><a href="#table614022951312">Table 11</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p413432919131"><a name="p413432919131"></a><a name="p413432919131"></a>Specifies the returned page.</p>
</td>
</tr>
</tbody>
</table>

**Table  11** **response**

<a name="table614022951312"></a>
<table><thead align="left"><tr id="row151501229151318"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p1315416291134"><a name="p1315416291134"></a><a name="p1315416291134"></a><strong id="b074920268505"><a name="b074920268505"></a><a name="b074920268505"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p1515852919136"><a name="p1515852919136"></a><a name="p1515852919136"></a><strong id="b12435428125019"><a name="b12435428125019"></a><a name="b12435428125019"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p11625293134"><a name="p11625293134"></a><a name="p11625293134"></a><strong id="b1233183112500"><a name="b1233183112500"></a><a name="b1233183112500"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row201641029141319"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p17169112919133"><a name="p17169112919133"></a><a name="p17169112919133"></a>content_type</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p15172729111316"><a name="p15172729111316"></a><a name="p15172729111316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p12176829131310"><a name="p12176829131310"></a><a name="p12176829131310"></a>Specifies the type of the returned page.</p>
<p id="p41774295138"><a name="p41774295138"></a><a name="p41774295138"></a>The options are <strong id="b11824122944716"><a name="b11824122944716"></a><a name="b11824122944716"></a>application/json</strong>, <strong id="b2825132919478"><a name="b2825132919478"></a><a name="b2825132919478"></a>text/html</strong>, and <strong id="b1282592964713"><a name="b1282592964713"></a><a name="b1282592964713"></a>text/xml</strong>.</p>
</td>
</tr>
<tr id="row1517952971310"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p13184162901317"><a name="p13184162901317"></a><a name="p13184162901317"></a>content</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p21881029121317"><a name="p21881029121317"></a><a name="p21881029121317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p191911129141320"><a name="p191911129141320"></a><a name="p191911129141320"></a>Specifies the content of the returned page.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section198571148154819"></a>

-   Request example

    ```
    {
          "path": "/abc1",
          "limit_num": 10,
          "limit_period": 60,
          "lock_time": 10,
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
          "lock_time": 10,
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


## Status Code<a name="section62371454"></a>

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

