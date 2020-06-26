# Querying a CC Attack Protection Rule<a name="EN-US_TOPIC_0193631146"></a>

## Function Description<a name="section50234597"></a>

This API is used to query details about a CC attack protection rule.

## URI<a name="section42470594"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/cc/\{ccrule\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table26564439"></a>
    <table><thead align="left"><tr id="row14496474"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p33363744"><a name="p33363744"></a><a name="p33363744"></a><strong id="b155951659171913"><a name="b155951659171913"></a><a name="b155951659171913"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p18108714"><a name="p18108714"></a><a name="p18108714"></a><strong id="b1254118192018"><a name="b1254118192018"></a><a name="b1254118192018"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p57519712"><a name="p57519712"></a><a name="p57519712"></a><strong id="b1782114716209"><a name="b1782114716209"></a><a name="b1782114716209"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p28585132"><a name="p28585132"></a><a name="p28585132"></a><strong id="b18433798207"><a name="b18433798207"></a><a name="b18433798207"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33694323"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p44885663"><a name="p44885663"></a><a name="p44885663"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p11860120"><a name="p11860120"></a><a name="p11860120"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p21145669"><a name="p21145669"></a><a name="p21145669"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p35077647"><a name="p35077647"></a><a name="p35077647"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row47263370"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p3127753"><a name="p3127753"></a><a name="p3127753"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p52021465"><a name="p52021465"></a><a name="p52021465"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p52989154"><a name="p52989154"></a><a name="p52989154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p64263051"><a name="p64263051"></a><a name="p64263051"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row41496547"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p5777119"><a name="p5777119"></a><a name="p5777119"></a>ccrule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p65293520"><a name="p65293520"></a><a name="p65293520"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p54283806"><a name="p54283806"></a><a name="p54283806"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p34912176"><a name="p34912176"></a><a name="p34912176"></a>Specifies the ID of a CC attack protection rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section46691029"></a>

Request parameters

None

## Response<a name="section17566079"></a>

Response parameters

**Table  2**  Parameter description

<a name="table40294034"></a>
<table><thead align="left"><tr id="row225404"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p18257741"><a name="p18257741"></a><a name="p18257741"></a><strong id="b388812523219"><a name="b388812523219"></a><a name="b388812523219"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p2482084"><a name="p2482084"></a><a name="p2482084"></a><strong id="b115381554152120"><a name="b115381554152120"></a><a name="b115381554152120"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p66831078"><a name="p66831078"></a><a name="p66831078"></a><strong id="b688245818213"><a name="b688245818213"></a><a name="b688245818213"></a>Description</strong></p>
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
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p5699133"><a name="p5699133"></a><a name="p5699133"></a>Specifies the lock duration. The value ranges from <strong id="b1322912813320"><a name="b1322912813320"></a><a name="b1322912813320"></a>0</strong> seconds to <strong id="b19229681534"><a name="b19229681534"></a><a name="b19229681534"></a>2<sup id="sup6229481313"><a name="sup6229481313"></a><a name="sup6229481313"></a>32</sup></strong> seconds.</p>
</td>
</tr>
<tr id="row51292205"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p61027960"><a name="p61027960"></a><a name="p61027960"></a>tag_type</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p44317740"><a name="p44317740"></a><a name="p44317740"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p71571255171014"><a name="p71571255171014"></a><a name="p71571255171014"></a>Specifies the rate limit mode.</p>
<a name="ul555831610497"></a><a name="ul555831610497"></a><ul id="ul555831610497"><li><span class="parmvalue" id="parmvalue05012225817"><a name="parmvalue05012225817"></a><a name="parmvalue05012225817"></a><b>ip</b></span>: A web visitor is identified by the IP address.</li><li><span class="parmvalue" id="parmvalue6293168142413"><a name="parmvalue6293168142413"></a><a name="parmvalue6293168142413"></a><b>cookie</b></span>: A web visitor is identified by the cookie key value.</li><li><span class="parmvalue" id="parmvalue189581648102617"><a name="parmvalue189581648102617"></a><a name="parmvalue189581648102617"></a><b>other</b></span>: A web visitor is identified by the Referer field (user-defined request source).</li></ul>
</td>
</tr>
<tr id="row28268911"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p8080463"><a name="p8080463"></a><a name="p8080463"></a>tag_index</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p50537747"><a name="p50537747"></a><a name="p50537747"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p16557142835414"><a name="p16557142835414"></a><a name="p16557142835414"></a>If <span class="parmname" id="parmname798914116483"><a name="parmname798914116483"></a><a name="parmname798914116483"></a><b>tag_type</b></span> is set to <strong id="b18990151144814"><a name="b18990151144814"></a><a name="b18990151144814"></a>cookie</strong>, this parameter indicates cookie name.</p>
</td>
</tr>
<tr id="row66360388"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p6482354"><a name="p6482354"></a><a name="p6482354"></a>tag_condition</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p55308705"><a name="p55308705"></a><a name="p55308705"></a><a href="#table2115782102">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p155661828165416"><a name="p155661828165416"></a><a name="p155661828165416"></a>Specifies the <strong id="b790994314221"><a name="b790994314221"></a><a name="b790994314221"></a>Referer</strong> (customized request source) field. This field is returned when <span class="parmvalue" id="parmvalue12909184318222"><a name="parmvalue12909184318222"></a><a name="parmvalue12909184318222"></a><b>tag_type</b></span> is set to <span class="parmvalue" id="parmvalue2909443122213"><a name="parmvalue2909443122213"></a><a name="parmvalue2909443122213"></a><b>other</b></span>.</p>
</td>
</tr>
<tr id="row13663579"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p33008137"><a name="p33008137"></a><a name="p33008137"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p56413415"><a name="p56413415"></a><a name="p56413415"></a><a href="#table191681818102">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p6083869"><a name="p6083869"></a><a name="p6083869"></a>Specifies the action taken when the number of requests reaches the upper limit.</p>
</td>
</tr>
<tr id="row26058851"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p30392200"><a name="p30392200"></a><a name="p30392200"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p45849121"><a name="p45849121"></a><a name="p45849121"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p22791319"><a name="p22791319"></a><a name="p22791319"></a>Specifies the time when a CC attack protection rule is added.</p>
</td>
</tr>
<tr id="row198481743151816"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p13111845101314"><a name="p13111845101314"></a><a name="p13111845101314"></a>default</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p1311245121318"><a name="p1311245121318"></a><a name="p1311245121318"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p8552015163214"><a name="p8552015163214"></a><a name="p8552015163214"></a>Specifies whether the rule is the default CC attack protection rule.</p>
<a name="ul1248751619599"></a><a name="ul1248751619599"></a><ul id="ul1248751619599"><li><strong id="en-us_topic_0193631170_b86402025123619"><a name="en-us_topic_0193631170_b86402025123619"></a><a name="en-us_topic_0193631170_b86402025123619"></a>true</strong>: The rule is the default CC attack protection rule created by the system when creating a domain name.</li><li><strong id="en-us_topic_0193631170_b1248153224120"><a name="en-us_topic_0193631170_b1248153224120"></a><a name="en-us_topic_0193631170_b1248153224120"></a>false</strong>: The rule is created by users.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  3** **tag\_condition**

<a name="table2115782102"></a>
<table><thead align="left"><tr id="row41268816100"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p121301861010"><a name="p121301861010"></a><a name="p121301861010"></a><strong id="b899171342417"><a name="b899171342417"></a><a name="b899171342417"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p101341485102"><a name="p101341485102"></a><a name="p101341485102"></a><strong id="b858621582417"><a name="b858621582417"></a><a name="b858621582417"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p11378851012"><a name="p11378851012"></a><a name="p11378851012"></a><strong id="b7427222142416"><a name="b7427222142416"></a><a name="b7427222142416"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6140148141013"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p414218141013"><a name="p414218141013"></a><a name="p414218141013"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p121451586106"><a name="p121451586106"></a><a name="p121451586106"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1014916851017"><a name="p1014916851017"></a><a name="p1014916851017"></a>Specifies the category. The value is <strong id="b1909843488"><a name="b1909843488"></a><a name="b1909843488"></a>Referer</strong>.</p>
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

**Table  4** **action**

<a name="table191681818102"></a>
<table><thead align="left"><tr id="row121755812102"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p1417815817101"><a name="p1417815817101"></a><a name="p1417815817101"></a><strong id="b18432113815244"><a name="b18432113815244"></a><a name="b18432113815244"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p14181783102"><a name="p14181783102"></a><a name="p14181783102"></a><strong id="b1691915416242"><a name="b1691915416242"></a><a name="b1691915416242"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p1018516818105"><a name="p1018516818105"></a><a name="p1018516818105"></a><strong id="b208501043132419"><a name="b208501043132419"></a><a name="b208501043132419"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1518717871011"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1018878131019"><a name="p1018878131019"></a><a name="p1018878131019"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1519115815103"><a name="p1519115815103"></a><a name="p1519115815103"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p154031329171813"><a name="p154031329171813"></a><a name="p154031329171813"></a>Specifies the action. The default value is <span class="parmvalue" id="parmvalue485112018915"><a name="parmvalue485112018915"></a><a name="parmvalue485112018915"></a><b>block</b></span>.</p>
<a name="ul661483971811"></a><a name="ul661483971811"></a><ul id="ul661483971811"><li><strong id="b1242288145818"><a name="b1242288145818"></a><a name="b1242288145818"></a>block</strong>: block the requests.</li><li><span class="parmvalue" id="parmvalue1749805751815"><a name="parmvalue1749805751815"></a><a name="parmvalue1749805751815"></a><b>captcha</b></span>: Verification code. The user needs to enter the correct verification code after blocking to restore the correct access page.</li></ul>
<p id="p15900183312309"><a name="p15900183312309"></a><a name="p15900183312309"></a>The default value is <strong id="b765844611443"><a name="b765844611443"></a><a name="b765844611443"></a>block</strong>.</p>
<p id="p2196148191019"><a name="p2196148191019"></a><a name="p2196148191019"></a>If <strong id="b6970763488"><a name="b6970763488"></a><a name="b6970763488"></a>tag_type</strong> is set to <strong id="b4971262484"><a name="b4971262484"></a><a name="b4971262484"></a>other</strong>, this parameter value can only be <strong id="b697119614480"><a name="b697119614480"></a><a name="b697119614480"></a>block</strong>.</p>
</td>
</tr>
<tr id="row719668141011"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p820148101013"><a name="p820148101013"></a><a name="p820148101013"></a>detail</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p142035816105"><a name="p142035816105"></a><a name="p142035816105"></a><a href="#table1060217107105">Table 5</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1207138141010"><a name="p1207138141010"></a><a name="p1207138141010"></a>Specifies the action details. If <strong id="b66561087484"><a name="b66561087484"></a><a name="b66561087484"></a>detail</strong> is <strong id="b0656686489"><a name="b0656686489"></a><a name="b0656686489"></a>null</strong>, the default block page is displayed by default.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **detail**

<a name="table1060217107105"></a>
<table><thead align="left"><tr id="row1861251018106"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p14615101021017"><a name="p14615101021017"></a><a name="p14615101021017"></a><strong id="b282820160251"><a name="b282820160251"></a><a name="b282820160251"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p2619141061016"><a name="p2619141061016"></a><a name="p2619141061016"></a><strong id="b1513721916252"><a name="b1513721916252"></a><a name="b1513721916252"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p10622171001012"><a name="p10622171001012"></a><a name="p10622171001012"></a><strong id="b1927912219253"><a name="b1927912219253"></a><a name="b1927912219253"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1142418101020"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p159981716141015"><a name="p159981716141015"></a><a name="p159981716141015"></a>response</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p62517141010"><a name="p62517141010"></a><a name="p62517141010"></a><a href="#table671153413914">Table 6</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p651517191019"><a name="p651517191019"></a><a name="p651517191019"></a>Specifies the returned page.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **response**

<a name="table671153413914"></a>
<table><thead align="left"><tr id="row87235341695"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p117313341294"><a name="p117313341294"></a><a name="p117313341294"></a><strong id="b184641728122513"><a name="b184641728122513"></a><a name="b184641728122513"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p107346349917"><a name="p107346349917"></a><a name="p107346349917"></a><strong id="b1758610305254"><a name="b1758610305254"></a><a name="b1758610305254"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p773818346918"><a name="p773818346918"></a><a name="p773818346918"></a><strong id="b959032112515"><a name="b959032112515"></a><a name="b959032112515"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row46995451391"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p26435443911"><a name="p26435443911"></a><a name="p26435443911"></a>content_type</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p76471144794"><a name="p76471144794"></a><a name="p76471144794"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1265017441999"><a name="p1265017441999"></a><a name="p1265017441999"></a>Specifies the type of the returned page.</p>
<p id="p6652244595"><a name="p6652244595"></a><a name="p6652244595"></a>The options are <strong id="b1558511157482"><a name="b1558511157482"></a><a name="b1558511157482"></a>application/json</strong>, <strong id="b758551514812"><a name="b758551514812"></a><a name="b758551514812"></a>text/html</strong>, and <strong id="b15866150481"><a name="b15866150481"></a><a name="b15866150481"></a>text/xml</strong>.</p>
</td>
</tr>
<tr id="row1669964520912"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p86555442914"><a name="p86555442914"></a><a name="p86555442914"></a>content</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1365811441899"><a name="p1365811441899"></a><a name="p1365811441899"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p186601448918"><a name="p186601448918"></a><a name="p186601448918"></a>Specifies the content of the returned page.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section104851652195015"></a>

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
    ..},
      "timestamp": 1499817600,
       "default": false
    }
    ```


## Status Code<a name="section23876985"></a>

[Table 7](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  7**  Status code

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

