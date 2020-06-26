# Querying CC Attack Protection Rules<a name="EN-US_TOPIC_0193631170"></a>

## Function Description<a name="section727444"></a>

This API is used to query all CC attack protection rules in a policy.

## URI<a name="section58923012"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/cc?offset=\{offset\}&limit=\{limit\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table30453955"></a>
    <table><thead align="left"><tr id="row66019173"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p45952776"><a name="p45952776"></a><a name="p45952776"></a><strong id="b149068539305"><a name="b149068539305"></a><a name="b149068539305"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p31187347"><a name="p31187347"></a><a name="p31187347"></a><strong id="b1249213284295"><a name="b1249213284295"></a><a name="b1249213284295"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p43147183"><a name="p43147183"></a><a name="p43147183"></a><strong id="b780011364291"><a name="b780011364291"></a><a name="b780011364291"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p5260931"><a name="p5260931"></a><a name="p5260931"></a><strong id="b379313381291"><a name="b379313381291"></a><a name="b379313381291"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23482296"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p23017846"><a name="p23017846"></a><a name="p23017846"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p52506212"><a name="p52506212"></a><a name="p52506212"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p25144746"><a name="p25144746"></a><a name="p25144746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p23458545"><a name="p23458545"></a><a name="p23458545"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row9800316"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p55628135"><a name="p55628135"></a><a name="p55628135"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p9585062"><a name="p9585062"></a><a name="p9585062"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p38192546"><a name="p38192546"></a><a name="p38192546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p6588482"><a name="p6588482"></a><a name="p6588482"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row59296339"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p38274149"><a name="p38274149"></a><a name="p38274149"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p13198351"><a name="p13198351"></a><a name="p13198351"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p62433530"><a name="p62433530"></a><a name="p62433530"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p21617533"><a name="p21617533"></a><a name="p21617533"></a>Specifies the number of returned pages. Its value ranges from <strong id="b14950253113319"><a name="b14950253113319"></a><a name="b14950253113319"></a>0</strong> to <strong id="b20950165363317"><a name="b20950165363317"></a><a name="b20950165363317"></a>65535</strong>. The default value is <strong id="b1795019536338"><a name="b1795019536338"></a><a name="b1795019536338"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row14234046"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p12107073"><a name="p12107073"></a><a name="p12107073"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p41148865"><a name="p41148865"></a><a name="p41148865"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p44723749"><a name="p44723749"></a><a name="p44723749"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p25357967"><a name="p25357967"></a><a name="p25357967"></a>Specifies the maximum number of records displayed on each page. Its value ranges from <strong id="b15826145517335"><a name="b15826145517335"></a><a name="b15826145517335"></a>0</strong> to <strong id="b7826135523314"><a name="b7826135523314"></a><a name="b7826135523314"></a>50</strong>. The default value is <strong id="b15826755153314"><a name="b15826755153314"></a><a name="b15826755153314"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section60545062"></a>

Request parameters

None

## Response<a name="section8034648"></a>

Response parameters

**Table  2**  Parameter description

<a name="table61024835"></a>
<table><thead align="left"><tr id="row2629376"><th class="cellrowborder" valign="top" width="33.2966703329667%" id="mcps1.2.4.1.1"><p id="p11652904"><a name="p11652904"></a><a name="p11652904"></a><strong id="b73157016351"><a name="b73157016351"></a><a name="b73157016351"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.90730926907309%" id="mcps1.2.4.1.2"><p id="p4361181"><a name="p4361181"></a><a name="p4361181"></a><strong id="b13411175183510"><a name="b13411175183510"></a><a name="b13411175183510"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p17711366"><a name="p17711366"></a><a name="p17711366"></a><strong id="b018010718357"><a name="b018010718357"></a><a name="b018010718357"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row25184570"><td class="cellrowborder" valign="top" width="33.2966703329667%" headers="mcps1.2.4.1.1 "><p id="p26684269"><a name="p26684269"></a><a name="p26684269"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="26.90730926907309%" headers="mcps1.2.4.1.2 "><p id="p13942152"><a name="p13942152"></a><a name="p13942152"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p55572532"><a name="p55572532"></a><a name="p55572532"></a>Specifies the total number of CC attack protection rules in a policy.</p>
</td>
</tr>
<tr id="row30390744"><td class="cellrowborder" valign="top" width="33.2966703329667%" headers="mcps1.2.4.1.1 "><p id="p45731167"><a name="p45731167"></a><a name="p45731167"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="26.90730926907309%" headers="mcps1.2.4.1.2 "><p id="p13237067"><a name="p13237067"></a><a name="p13237067"></a><a href="#table16394183011019">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1603648"><a name="p1603648"></a><a name="p1603648"></a>Specifies the CC attack protection rule objects.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **items**

<a name="table16394183011019"></a>
<table><thead align="left"><tr id="row939613301015"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p039873016013"><a name="p039873016013"></a><a name="p039873016013"></a><strong id="b191193914421"><a name="b191193914421"></a><a name="b191193914421"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p183997301406"><a name="p183997301406"></a><a name="p183997301406"></a><strong id="b194141142174212"><a name="b194141142174212"></a><a name="b194141142174212"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p839973013010"><a name="p839973013010"></a><a name="p839973013010"></a><strong id="b05921943204220"><a name="b05921943204220"></a><a name="b05921943204220"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row3521132912545"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1550711285549"><a name="p1550711285549"></a><a name="p1550711285549"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p12511152855417"><a name="p12511152855417"></a><a name="p12511152855417"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p851272816548"><a name="p851272816548"></a><a name="p851272816548"></a>Specifies the ID of a CC attack protection rule.</p>
</td>
</tr>
<tr id="row1152119292547"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p16515142865410"><a name="p16515142865410"></a><a name="p16515142865410"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p651882835414"><a name="p651882835414"></a><a name="p651882835414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p18520162895410"><a name="p18520162895410"></a><a name="p18520162895410"></a>Specifies the ID of the policy to which the rule belongs.</p>
</td>
</tr>
<tr id="row652142915419"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p15221228115415"><a name="p15221228115415"></a><a name="p15221228115415"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p752312814546"><a name="p752312814546"></a><a name="p752312814546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p13524152875412"><a name="p13524152875412"></a><a name="p13524152875412"></a>Specifies the URL to which the rule applies, excluding a domain name.</p>
<a name="ul20810143683616"></a><a name="ul20810143683616"></a><ul id="ul20810143683616"><li>Prefix match: The path ending with * indicates that the path is used as a prefix.<p id="li315614594312p0"><a name="li315614594312p0"></a><a name="li315614594312p0"></a>For example, if the path to be protected is <strong id="b1620175592313"><a name="b1620175592313"></a><a name="b1620175592313"></a>/admin/test.php</strong> or <strong id="b1662055542315"><a name="b1662055542315"></a><a name="b1662055542315"></a>/adminabc</strong>, set <strong id="b1062010551237"><a name="b1062010551237"></a><a name="b1062010551237"></a>Path</strong> to <span class="parmvalue" id="parmvalue4620105513234"><a name="parmvalue4620105513234"></a><a name="parmvalue4620105513234"></a><b>/admin*</b></span>.</p>
</li><li>Exact match: The path to be entered must match the path to be protected.<p id="p1285333620361"><a name="p1285333620361"></a><a name="p1285333620361"></a>If the path to be protected is <span class="parmvalue" id="parmvalue8970171414552"><a name="parmvalue8970171414552"></a><a name="parmvalue8970171414552"></a><b>/admin</b></span>, set <strong id="b1697081419556"><a name="b1697081419556"></a><a name="b1697081419556"></a>url</strong> to <span class="parmvalue" id="parmvalue7970151414550"><a name="parmvalue7970151414550"></a><a name="parmvalue7970151414550"></a><b>/admin</b></span>.</p>
</li></ul>
</td>
</tr>
<tr id="row55211629115411"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p185271828155419"><a name="p185271828155419"></a><a name="p185271828155419"></a>limit_num</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p135281286547"><a name="p135281286547"></a><a name="p135281286547"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p11530228185415"><a name="p11530228185415"></a><a name="p11530228185415"></a>Specifies the number of requests allowed from a web visitor in a rate limiting period.</p>
</td>
</tr>
<tr id="row11521529165419"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1953319288548"><a name="p1953319288548"></a><a name="p1953319288548"></a>limit_period</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p13535152875415"><a name="p13535152875415"></a><a name="p13535152875415"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p853642817546"><a name="p853642817546"></a><a name="p853642817546"></a>Specifies the rate limiting period.</p>
</td>
</tr>
<tr id="row65211529175417"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p115391228205410"><a name="p115391228205410"></a><a name="p115391228205410"></a>lock_time</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1254142865411"><a name="p1254142865411"></a><a name="p1254142865411"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p154452819543"><a name="p154452819543"></a><a name="p154452819543"></a>Specifies the lock duration. The value ranges from <strong id="b4469437151015"><a name="b4469437151015"></a><a name="b4469437151015"></a>0</strong> seconds to <strong id="b846973771011"><a name="b846973771011"></a><a name="b846973771011"></a>2<sup id="sup104771137131015"><a name="sup104771137131015"></a><a name="sup104771137131015"></a>32</sup></strong> seconds.</p>
</td>
</tr>
<tr id="row2052110298543"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p654722885416"><a name="p654722885416"></a><a name="p654722885416"></a>tag_type</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p554952835413"><a name="p554952835413"></a><a name="p554952835413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p71571255171014"><a name="p71571255171014"></a><a name="p71571255171014"></a>Specifies the rate limit mode.</p>
<a name="ul555831610497"></a><a name="ul555831610497"></a><ul id="ul555831610497"><li><span class="parmvalue" id="parmvalue20113112417553"><a name="parmvalue20113112417553"></a><a name="parmvalue20113112417553"></a><b>ip</b></span>: A web visitor is identified by the IP address.</li><li><span class="parmvalue" id="parmvalue797704317587"><a name="parmvalue797704317587"></a><a name="parmvalue797704317587"></a><b>cookie</b></span>: A web visitor is identified by the cookie key value.</li><li><span class="parmvalue" id="parmvalue9409202895518"><a name="parmvalue9409202895518"></a><a name="parmvalue9409202895518"></a><b>other</b></span>: A web visitor is identified by the Referer field (user-defined request source).</li></ul>
</td>
</tr>
<tr id="row1352142911542"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p1355482885412"><a name="p1355482885412"></a><a name="p1355482885412"></a>tag_index</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p755522845411"><a name="p755522845411"></a><a name="p755522845411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p16557142835414"><a name="p16557142835414"></a><a name="p16557142835414"></a>If <span class="parmvalue" id="parmvalue940418231916"><a name="parmvalue940418231916"></a><a name="parmvalue940418231916"></a><b>tag_type</b></span> is set to <strong id="b144041523214"><a name="b144041523214"></a><a name="b144041523214"></a>cookie</strong>, this parameter indicates cookie name.</p>
</td>
</tr>
<tr id="row2521192975413"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p195608285544"><a name="p195608285544"></a><a name="p195608285544"></a>tag_condition</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p4562102810547"><a name="p4562102810547"></a><a name="p4562102810547"></a><a href="#table1897210413559">Table 4</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p155661828165416"><a name="p155661828165416"></a><a name="p155661828165416"></a>Specifies the <strong id="b1185818219215"><a name="b1185818219215"></a><a name="b1185818219215"></a>Referer</strong> (customized request source) field. This field is returned when <span class="parmvalue" id="parmvalue118581429213"><a name="parmvalue118581429213"></a><a name="parmvalue118581429213"></a><b>tag_type</b></span> is set to <span class="parmvalue" id="parmvalue1185872172115"><a name="parmvalue1185872172115"></a><a name="parmvalue1185872172115"></a><b>other</b></span>.</p>
</td>
</tr>
<tr id="row4521229135413"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p25843288546"><a name="p25843288546"></a><a name="p25843288546"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p658672815413"><a name="p658672815413"></a><a name="p658672815413"></a><a href="#table3660351175718">Table 5</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p11588142825415"><a name="p11588142825415"></a><a name="p11588142825415"></a>Specifies the action taken when the number of requests reaches the upper limit.</p>
</td>
</tr>
<tr id="row14520182920540"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p463052825418"><a name="p463052825418"></a><a name="p463052825418"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1863182820543"><a name="p1863182820543"></a><a name="p1863182820543"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p4632202885411"><a name="p4632202885411"></a><a name="p4632202885411"></a>Specifies the time when a CC attack protection rule is added.</p>
</td>
</tr>
<tr id="row1331174518134"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p13111845101314"><a name="p13111845101314"></a><a name="p13111845101314"></a>default</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1311245121318"><a name="p1311245121318"></a><a name="p1311245121318"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p153111545121310"><a name="p153111545121310"></a><a name="p153111545121310"></a>Specifies whether the rule is the default CC attack protection rule.</p>
<a name="ul1248751619599"></a><a name="ul1248751619599"></a><ul id="ul1248751619599"><li><strong id="b86402025123619"><a name="b86402025123619"></a><a name="b86402025123619"></a>true</strong>: The rule is the default CC attack protection rule created by the system when creating a domain name.</li><li><strong id="b1248153224120"><a name="b1248153224120"></a><a name="b1248153224120"></a>false</strong>: The rule is created by users.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  4** **tag\_condition**

<a name="table1897210413559"></a>
<table><thead align="left"><tr id="row498264125512"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p179858412553"><a name="p179858412553"></a><a name="p179858412553"></a><strong id="b12793177195613"><a name="b12793177195613"></a><a name="b12793177195613"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p20987841105519"><a name="p20987841105519"></a><a name="p20987841105519"></a><strong id="b1192686788"><a name="b1192686788"></a><a name="b1192686788"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p18992541175512"><a name="p18992541175512"></a><a name="p18992541175512"></a><strong id="b1651416917561"><a name="b1651416917561"></a><a name="b1651416917561"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row316718559556"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p129251153125517"><a name="p129251153125517"></a><a name="p129251153125517"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p18928155325515"><a name="p18928155325515"></a><a name="p18928155325515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p169331053205518"><a name="p169331053205518"></a><a name="p169331053205518"></a>Specifies the category. The value is <strong id="b128891959461"><a name="b128891959461"></a><a name="b128891959461"></a>Referer</strong>.</p>
</td>
</tr>
<tr id="row816515556552"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p159555533556"><a name="p159555533556"></a><a name="p159555533556"></a>contents</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p1895915385512"><a name="p1895915385512"></a><a name="p1895915385512"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p29649538557"><a name="p29649538557"></a><a name="p29649538557"></a>Specifies the category content. For example, <strong id="b1435138144117"><a name="b1435138144117"></a><a name="b1435138144117"></a>http://www.</strong><em id="i11685154224119"><a name="i11685154224119"></a><a name="i11685154224119"></a>xxx</em><strong id="b203331247194110"><a name="b203331247194110"></a><a name="b203331247194110"></a>.com</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **action**

<a name="table3660351175718"></a>
<table><thead align="left"><tr id="row13670125155718"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p166741051165714"><a name="p166741051165714"></a><a name="p166741051165714"></a><strong id="b15441388113"><a name="b15441388113"></a><a name="b15441388113"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p1868015111574"><a name="p1868015111574"></a><a name="p1868015111574"></a><strong id="b1230373929"><a name="b1230373929"></a><a name="b1230373929"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p16684751165717"><a name="p16684751165717"></a><a name="p16684751165717"></a><strong id="b13264591562"><a name="b13264591562"></a><a name="b13264591562"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row487919825816"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p9786157105816"><a name="p9786157105816"></a><a name="p9786157105816"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p0791171581"><a name="p0791171581"></a><a name="p0791171581"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p154031329171813"><a name="p154031329171813"></a><a name="p154031329171813"></a>Specifies the action. The default value is <span class="parmvalue" id="parmvalue1419013502810"><a name="parmvalue1419013502810"></a><a name="parmvalue1419013502810"></a><b>block</b></span>.</p>
<a name="ul661483971811"></a><a name="ul661483971811"></a><ul id="ul661483971811"><li><strong id="b2080181405715"><a name="b2080181405715"></a><a name="b2080181405715"></a>block</strong>: block the requests.</li><li><span class="parmvalue" id="parmvalue10306151065715"><a name="parmvalue10306151065715"></a><a name="parmvalue10306151065715"></a><b>captcha</b></span>: Verification code. The user needs to enter the correct verification code after blocking to restore the correct access page.</li></ul>
<p id="p2139345162813"><a name="p2139345162813"></a><a name="p2139345162813"></a>The default value is <strong id="b842352706102157_1"><a name="b842352706102157_1"></a><a name="b842352706102157_1"></a>block</strong>.</p>
</td>
</tr>
<tr id="row15877178135818"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p2799197175818"><a name="p2799197175818"></a><a name="p2799197175818"></a>detail</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p178031872584"><a name="p178031872584"></a><a name="p178031872584"></a><a href="#table1060217107105">Table 6</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p880513714586"><a name="p880513714586"></a><a name="p880513714586"></a>Specifies the action details. If <strong id="b163751012194614"><a name="b163751012194614"></a><a name="b163751012194614"></a>detail</strong> is <strong id="b143758126467"><a name="b143758126467"></a><a name="b143758126467"></a>null</strong>, the default block page is displayed by default.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **detail**

<a name="table1060217107105"></a>
<table><thead align="left"><tr id="row1861251018106"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p14615101021017"><a name="p14615101021017"></a><a name="p14615101021017"></a><strong id="b126344184572"><a name="b126344184572"></a><a name="b126344184572"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p2619141061016"><a name="p2619141061016"></a><a name="p2619141061016"></a><strong id="b72110472"><a name="b72110472"></a><a name="b72110472"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p10622171001012"><a name="p10622171001012"></a><a name="p10622171001012"></a><strong id="b1795352114576"><a name="b1795352114576"></a><a name="b1795352114576"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1142418101020"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p159981716141015"><a name="p159981716141015"></a><a name="p159981716141015"></a>response</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p62517141010"><a name="p62517141010"></a><a name="p62517141010"></a><a href="#table671153413914">Table 7</a></p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p651517191019"><a name="p651517191019"></a><a name="p651517191019"></a>Specifies the returned page.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **response**

<a name="table671153413914"></a>
<table><thead align="left"><tr id="row87235341695"><th class="cellrowborder" valign="top" width="33.086691330866906%" id="mcps1.2.4.1.1"><p id="p117313341294"><a name="p117313341294"></a><a name="p117313341294"></a><strong id="b2775142818579"><a name="b2775142818579"></a><a name="b2775142818579"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.117288271172878%" id="mcps1.2.4.1.2"><p id="p107346349917"><a name="p107346349917"></a><a name="p107346349917"></a><strong id="b1045200888"><a name="b1045200888"></a><a name="b1045200888"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.4.1.3"><p id="p773818346918"><a name="p773818346918"></a><a name="p773818346918"></a><strong id="b19673183018570"><a name="b19673183018570"></a><a name="b19673183018570"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row46995451391"><td class="cellrowborder" valign="top" width="33.086691330866906%" headers="mcps1.2.4.1.1 "><p id="p26435443911"><a name="p26435443911"></a><a name="p26435443911"></a>content_type</p>
</td>
<td class="cellrowborder" valign="top" width="27.117288271172878%" headers="mcps1.2.4.1.2 "><p id="p76471144794"><a name="p76471144794"></a><a name="p76471144794"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.4.1.3 "><p id="p1265017441999"><a name="p1265017441999"></a><a name="p1265017441999"></a>Specifies the type of the returned page.</p>
<p id="p6652244595"><a name="p6652244595"></a><a name="p6652244595"></a>The options are <strong id="b3140104598"><a name="b3140104598"></a><a name="b3140104598"></a>application/json</strong>, <strong id="b7121171313593"><a name="b7121171313593"></a><a name="b7121171313593"></a>text/html</strong>, and <strong id="b193898189599"><a name="b193898189599"></a><a name="b193898189599"></a>text/xml</strong>.</p>
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

## Example<a name="section23104218489"></a>

**total**  with a value of  **2**  is used as an example.

Response example

```
{
  "total": 2,
  "items": [{
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
      "default": true
    }, {
      "id": "3d7bea768b10480984f98c6b69d43d0f",
      "policy_id": "9tre832yf96784ec8abd8ba61a98064ef",
      "path": "/efgh",
      "limit_num": 10,
      "limit_period": 60,
      "lock_time": 5,
      "tag_type": "other",
      "tag_condition":{
          "category": "referer",
         "contents": ["http://www.example.com"]
       }
      "action": {
        "category": "block",
      },
      "timestamp": 1499817600,
      "default": true
    }
  ]
}
```

## Status Code<a name="section5202971"></a>

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

