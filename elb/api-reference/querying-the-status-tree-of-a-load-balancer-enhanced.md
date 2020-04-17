# Querying the Status Tree of a Load Balancer<a name="EN-US_TOPIC_0141008272"></a>

## Function<a name="en-us_topic_0096561533_en-us_topic_0049139633_section21536161"></a>

This API is used to query the status tree of a load balancer. You can use this API to query information about the associated listeners, backend server groups, backend servers, health checks, forwarding policies, and forwarding rules and understand the topology of resources associated with the load balancer.

## URI<a name="en-us_topic_0096561533_en-us_topic_0049139633_section59607724"></a>

GET /v2.0/lbaas/loadbalancers/\{loadbalancer\_id\}/statuses

**Table  1**  Parameter description

<a name="en-us_topic_0096561533_table8859516183710"></a>
<table><thead align="left"><tr id="en-us_topic_0096561533_row1189415166379"><th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.1"><p id="en-us_topic_0096561533_p148945161379"><a name="en-us_topic_0096561533_p148945161379"></a><a name="en-us_topic_0096561533_p148945161379"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.2"><p id="p12397022203011"><a name="p12397022203011"></a><a name="p12397022203011"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.5.1.3"><p id="en-us_topic_0096561533_p16894816103712"><a name="en-us_topic_0096561533_p16894816103712"></a><a name="en-us_topic_0096561533_p16894816103712"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.60606060606061%" id="mcps1.2.5.1.4"><p id="en-us_topic_0096561533_p16894816113718"><a name="en-us_topic_0096561533_p16894816113718"></a><a name="en-us_topic_0096561533_p16894816113718"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561533_row1089431611376"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561533_p989461633718"><a name="en-us_topic_0096561533_p989461633718"></a><a name="en-us_topic_0096561533_p989461633718"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561533_p1889491623711"><a name="en-us_topic_0096561533_p1889491623711"></a><a name="en-us_topic_0096561533_p1889491623711"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096561533_p108947162378"><a name="en-us_topic_0096561533_p108947162378"></a><a name="en-us_topic_0096561533_p108947162378"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096561533_p1789471633719"><a name="en-us_topic_0096561533_p1789471633719"></a><a name="en-us_topic_0096561533_p1789471633719"></a>Specifies the load balancer ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0096561533_section144381854113611"></a>

None

## Response<a name="en-us_topic_0096561533_section998913218376"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0096561533_table55131118111415"></a>
<table><thead align="left"><tr id="en-us_topic_0096561533_row45132185142"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561533_p55136183141"><a name="en-us_topic_0096561533_p55136183141"></a><a name="en-us_topic_0096561533_p55136183141"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561533_p1351381841417"><a name="en-us_topic_0096561533_p1351381841417"></a><a name="en-us_topic_0096561533_p1351381841417"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="73%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561533_p1751351820147"><a name="en-us_topic_0096561533_p1751351820147"></a><a name="en-us_topic_0096561533_p1751351820147"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561533_row1851431841417"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561533_p951413181144"><a name="en-us_topic_0096561533_p951413181144"></a><a name="en-us_topic_0096561533_p951413181144"></a>statuses</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.2 "><p id="p15758559163013"><a name="p15758559163013"></a><a name="p15758559163013"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561533_p18514171861420"><a name="en-us_topic_0096561533_p18514171861420"></a><a name="en-us_topic_0096561533_p18514171861420"></a>Specifies the status tree of a load balancer. For details, see <a href="#en-us_topic_0096561533_table1112044734716">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **statuses**  parameter description

<a name="en-us_topic_0096561533_table1112044734716"></a>
<table><thead align="left"><tr id="en-us_topic_0096561533_row51584479473"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561533_p615874718471"><a name="en-us_topic_0096561533_p615874718471"></a><a name="en-us_topic_0096561533_p615874718471"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561533_p1158134720471"><a name="en-us_topic_0096561533_p1158134720471"></a><a name="en-us_topic_0096561533_p1158134720471"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="73%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561533_p61581247104718"><a name="en-us_topic_0096561533_p61581247104718"></a><a name="en-us_topic_0096561533_p61581247104718"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561533_row2015874754710"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561533_p1015834710470"><a name="en-us_topic_0096561533_p1015834710470"></a><a name="en-us_topic_0096561533_p1015834710470"></a>loadbalancer</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.2 "><p id="p159081065310"><a name="p159081065310"></a><a name="p159081065310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561533_p121589470473"><a name="en-us_topic_0096561533_p121589470473"></a><a name="en-us_topic_0096561533_p121589470473"></a>Specifies the load balancer. For details, see <a href="#en-us_topic_0096561533_table712410117487">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **loadbalancer**  parameter description

<a name="en-us_topic_0096561533_table712410117487"></a>
<table><thead align="left"><tr id="en-us_topic_0096561533_row622413115489"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561533_p182247110482"><a name="en-us_topic_0096561533_p182247110482"></a><a name="en-us_topic_0096561533_p182247110482"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561533_p20224111114819"><a name="en-us_topic_0096561533_p20224111114819"></a><a name="en-us_topic_0096561533_p20224111114819"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="73%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561533_p0225161116489"><a name="en-us_topic_0096561533_p0225161116489"></a><a name="en-us_topic_0096561533_p0225161116489"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561533_row6225511164819"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561533_p20225131117489"><a name="en-us_topic_0096561533_p20225131117489"></a><a name="en-us_topic_0096561533_p20225131117489"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p19954143318312"><a name="p19954143318312"></a><a name="p19954143318312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561533_p2225511104811"><a name="en-us_topic_0096561533_p2225511104811"></a><a name="en-us_topic_0096561533_p2225511104811"></a>Specifies the load balancer ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096561533_row122541154816"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561533_p0225181154814"><a name="en-us_topic_0096561533_p0225181154814"></a><a name="en-us_topic_0096561533_p0225181154814"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p169305358314"><a name="p169305358314"></a><a name="p169305358314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561533_p182251711174818"><a name="en-us_topic_0096561533_p182251711174818"></a><a name="en-us_topic_0096561533_p182251711174818"></a>Specifies the load balancer name.</p>
<p id="p1986711136011"><a name="p1986711136011"></a><a name="p1986711136011"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561533_row122251111104817"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561533_p8225101115483"><a name="en-us_topic_0096561533_p8225101115483"></a><a name="en-us_topic_0096561533_p8225101115483"></a>listeners</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561533_p422512115486"><a name="en-us_topic_0096561533_p422512115486"></a><a name="en-us_topic_0096561533_p422512115486"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561533_p1225131112487"><a name="en-us_topic_0096561533_p1225131112487"></a><a name="en-us_topic_0096561533_p1225131112487"></a>Lists the listeners added to the load balancer. For details of this parameter, see <a href="#d0e1809">Table 5</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561533_row10225131110487"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561533_p1422591194819"><a name="en-us_topic_0096561533_p1422591194819"></a><a name="en-us_topic_0096561533_p1422591194819"></a>pools</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1153239191113"><a name="p1153239191113"></a><a name="p1153239191113"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.4.1.3 "><p id="p29157296305"><a name="p29157296305"></a><a name="p29157296305"></a>Lists the backend server groups associated with the load balancer. For details of this parameter, see <a href="#table99441432133413">Table 6</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561533_row1722512117481"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p727217358477"><a name="p727217358477"></a><a name="p727217358477"></a>operating_status</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p82761735124717"><a name="p82761735124717"></a><a name="p82761735124717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.4.1.3 "><a name="ul132852353472"></a><a name="ul132852353472"></a><ul id="ul132852353472"><li>Specifies the operating status of the load balancer.</li><li>The value can be <strong id="b842352706165847"><a name="b842352706165847"></a><a name="b842352706165847"></a>ONLINE</strong>, <strong id="b842352706165850"><a name="b842352706165850"></a><a name="b842352706165850"></a>OFFLINE</strong>, <strong id="b842352706165852"><a name="b842352706165852"></a><a name="b842352706165852"></a>DEGRADED</strong>, <strong id="b842352706165855"><a name="b842352706165855"></a><a name="b842352706165855"></a>DISABLED</strong>, or <strong id="b842352706165859"><a name="b842352706165859"></a><a name="b842352706165859"></a>NO_MONITOR</strong>.</li><li>This parameter is reserved. The default value is <strong id="b842352706145855"><a name="b842352706145855"></a><a name="b842352706145855"></a>ONLINE</strong>.</li><li>The value contains a maximum of 16 characters.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0096561533_row1222671120487"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p930113351475"><a name="p930113351475"></a><a name="p930113351475"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p7305153534717"><a name="p7305153534717"></a><a name="p7305153534717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.4.1.3 "><a name="ul631316357476"></a><a name="ul631316357476"></a><ul id="ul631316357476"><li>Specifies the provisioning status of the load balancer.</li><li>The value can be <strong id="b842352706165943"><a name="b842352706165943"></a><a name="b842352706165943"></a>ACTIVE</strong>, <strong id="b842352706165947"><a name="b842352706165947"></a><a name="b842352706165947"></a>PENDING_CREATE</strong>, or <strong id="b842352706165951"><a name="b842352706165951"></a><a name="b842352706165951"></a>ERROR</strong>.</li><li>This parameter is reserved. The default value is <strong id="b1099445437"><a name="b1099445437"></a><a name="b1099445437"></a>ACTIVE</strong>.</li><li>The value contains a maximum of 16 characters.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  5** **listeners**  parameter description

<a name="d0e1809"></a>
<table><thead align="left"><tr id="row20334451"><th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.4.1.1"><p id="p36477860"><a name="p36477860"></a><a name="p36477860"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.4.1.2"><p id="p1916722"><a name="p1916722"></a><a name="p1916722"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71.28712871287128%" id="mcps1.2.4.1.3"><p id="p46651798"><a name="p46651798"></a><a name="p46651798"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20699302"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.1 "><p id="p66030746"><a name="p66030746"></a><a name="p66030746"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="p12616125515318"><a name="p12616125515318"></a><a name="p12616125515318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71.28712871287128%" headers="mcps1.2.4.1.3 "><p id="p43264248"><a name="p43264248"></a><a name="p43264248"></a>Specifies the listener ID.</p>
</td>
</tr>
<tr id="row53833912"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.1 "><p id="p65579600"><a name="p65579600"></a><a name="p65579600"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="p10347360"><a name="p10347360"></a><a name="p10347360"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71.28712871287128%" headers="mcps1.2.4.1.3 "><p id="p44245620"><a name="p44245620"></a><a name="p44245620"></a>Specifies the listener name.</p>
</td>
</tr>
<tr id="row62666267"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.1 "><p id="p42802865"><a name="p42802865"></a><a name="p42802865"></a>l7policies</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="p44480011"><a name="p44480011"></a><a name="p44480011"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="71.28712871287128%" headers="mcps1.2.4.1.3 "><p id="p8312132"><a name="p8312132"></a><a name="p8312132"></a>Lists associated forwarding policies. For details of this parameter, see <a href="#table129151528185512">Table 9</a>.</p>
</td>
</tr>
<tr id="row7700330"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.1 "><p id="p19747016"><a name="p19747016"></a><a name="p19747016"></a>pools</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="p56004438"><a name="p56004438"></a><a name="p56004438"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="71.28712871287128%" headers="mcps1.2.4.1.3 "><p id="p4958258"><a name="p4958258"></a><a name="p4958258"></a>Lists the backend server groups associated with the listener. For details of this parameter, see <a href="#table99441432133413">Table 6</a>.</p>
</td>
</tr>
<tr id="row66074642"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.1 "><p id="p19591840114414"><a name="p19591840114414"></a><a name="p19591840114414"></a>operating_status</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="p2963240164412"><a name="p2963240164412"></a><a name="p2963240164412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71.28712871287128%" headers="mcps1.2.4.1.3 "><a name="ul1796424012448"></a><a name="ul1796424012448"></a><ul id="ul1796424012448"><li>Specifies the operating status of the listener.</li><li>The value can be <strong id="b1244745394"><a name="b1244745394"></a><a name="b1244745394"></a>ONLINE</strong>, <strong id="b434550772"><a name="b434550772"></a><a name="b434550772"></a>OFFLINE</strong>, <strong id="b2143120354"><a name="b2143120354"></a><a name="b2143120354"></a>DEGRADED</strong>, <strong id="b895918977"><a name="b895918977"></a><a name="b895918977"></a>DISABLED</strong>, or <strong id="b291599533"><a name="b291599533"></a><a name="b291599533"></a>NO_MONITOR</strong>.</li><li>This parameter is reserved. The default value is <strong id="b1037190960"><a name="b1037190960"></a><a name="b1037190960"></a>ONLINE</strong>.</li></ul>
</td>
</tr>
<tr id="row62939823"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.1 "><p id="p1197744013447"><a name="p1197744013447"></a><a name="p1197744013447"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="p1398120403443"><a name="p1398120403443"></a><a name="p1398120403443"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71.28712871287128%" headers="mcps1.2.4.1.3 "><a name="ul298320402441"></a><a name="ul298320402441"></a><ul id="ul298320402441"><li>Specifies the provisioning status of the listener.</li><li>The value can be <strong id="b186687581"><a name="b186687581"></a><a name="b186687581"></a>ACTIVE</strong>, <strong id="b2077873532"><a name="b2077873532"></a><a name="b2077873532"></a>PENDING_CREATE</strong>, or <strong id="b550954697"><a name="b550954697"></a><a name="b550954697"></a>ERROR</strong>.</li><li>This parameter is reserved. The default value is <strong id="b1482750197"><a name="b1482750197"></a><a name="b1482750197"></a>ACTIVE</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  6** **pools**  parameter description

<a name="table99441432133413"></a>
<table><thead align="left"><tr id="row69508326348"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.1"><p id="p1995243214346"><a name="p1995243214346"></a><a name="p1995243214346"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="p11955183293418"><a name="p11955183293418"></a><a name="p11955183293418"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="72%" id="mcps1.2.4.1.3"><p id="p29591532173414"><a name="p29591532173414"></a><a name="p29591532173414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6962193213342"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p1196393233413"><a name="p1196393233413"></a><a name="p1196393233413"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p5755131993219"><a name="p5755131993219"></a><a name="p5755131993219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p597213213348"><a name="p597213213348"></a><a name="p597213213348"></a>Specifies the ID of the backend server group.</p>
</td>
</tr>
<tr id="row16972163219349"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p5975173217344"><a name="p5975173217344"></a><a name="p5975173217344"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p209761032163418"><a name="p209761032163418"></a><a name="p209761032163418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p1097911327348"><a name="p1097911327348"></a><a name="p1097911327348"></a>Specifies the backend server group name.</p>
</td>
</tr>
<tr id="row1698173210346"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p20724741"><a name="p20724741"></a><a name="p20724741"></a>healthmonitor</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p982446"><a name="p982446"></a><a name="p982446"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p142523271642"><a name="p142523271642"></a><a name="p142523271642"></a>Provides health check details of the backend server group. For details of this parameter, see <a href="#table10522133654610">Table 7</a>.</p>
</td>
</tr>
<tr id="row49931032193418"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p19554439"><a name="p19554439"></a><a name="p19554439"></a>members</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p20167161741116"><a name="p20167161741116"></a><a name="p20167161741116"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="p4208190"><a name="p4208190"></a><a name="p4208190"></a>Lists the members contained in the backend server group. For details of this parameter, see <a href="#table1563417579480">Table 8</a>.</p>
</td>
</tr>
<tr id="row42133393416"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p32941855144513"><a name="p32941855144513"></a><a name="p32941855144513"></a>operating_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p9297145517453"><a name="p9297145517453"></a><a name="p9297145517453"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><a name="ul73006555458"></a><a name="ul73006555458"></a><ul id="ul73006555458"><li>Specifies the operating status of the backend server group.</li><li>The value can be <strong id="b380269669"><a name="b380269669"></a><a name="b380269669"></a>ONLINE</strong>, <strong id="b1618797377"><a name="b1618797377"></a><a name="b1618797377"></a>OFFLINE</strong>, <strong id="b1931624454"><a name="b1931624454"></a><a name="b1931624454"></a>DEGRADED</strong>, <strong id="b1738064316"><a name="b1738064316"></a><a name="b1738064316"></a>DISABLED</strong>, or <strong id="b970504453"><a name="b970504453"></a><a name="b970504453"></a>NO_MONITOR</strong>.</li><li>This parameter is reserved. The default value is <strong id="b1221994890"><a name="b1221994890"></a><a name="b1221994890"></a>ONLINE</strong>.</li></ul>
</td>
</tr>
<tr id="row210733113412"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p2031113556456"><a name="p2031113556456"></a><a name="p2031113556456"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p33181355134517"><a name="p33181355134517"></a><a name="p33181355134517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><a name="ul3320185515455"></a><a name="ul3320185515455"></a><ul id="ul3320185515455"><li>Specifies the provisioning status of the backend server group.</li><li>The value can be <strong id="b1060982249"><a name="b1060982249"></a><a name="b1060982249"></a>ACTIVE</strong>, <strong id="b1556711931"><a name="b1556711931"></a><a name="b1556711931"></a>PENDING_CREATE</strong>, or <strong id="b358359142"><a name="b358359142"></a><a name="b358359142"></a>ERROR</strong>.</li><li>This parameter is reserved. The default value is <strong id="b545309669"><a name="b545309669"></a><a name="b545309669"></a>ACTIVE</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  7** **healthmonitor**  parameter description

<a name="table10522133654610"></a>
<table><thead align="left"><tr id="row155317365461"><th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.4.1.1"><p id="p2053533644615"><a name="p2053533644615"></a><a name="p2053533644615"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.4.1.2"><p id="p20538136204612"><a name="p20538136204612"></a><a name="p20538136204612"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71.71717171717171%" id="mcps1.2.4.1.3"><p id="p1554113634618"><a name="p1554113634618"></a><a name="p1554113634618"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20543113614464"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.1 "><p id="p3500861"><a name="p3500861"></a><a name="p3500861"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="p195305643214"><a name="p195305643214"></a><a name="p195305643214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 "><p id="p3139116"><a name="p3139116"></a><a name="p3139116"></a>Specifies the health check ID.</p>
</td>
</tr>
<tr id="row2055363654611"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.1 "><p id="p6714269"><a name="p6714269"></a><a name="p6714269"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="p6984889"><a name="p6984889"></a><a name="p6984889"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 "><p id="p64233450"><a name="p64233450"></a><a name="p64233450"></a>Specifies the health check name.</p>
</td>
</tr>
<tr id="row556083620460"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.1 "><p id="p51307412"><a name="p51307412"></a><a name="p51307412"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="p62259745"><a name="p62259745"></a><a name="p62259745"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 "><a name="ul711834416471"></a><a name="ul711834416471"></a><ul id="ul711834416471"><li>Specifies the health check protocol.</li><li>The value can be <strong id="b37719544155919"><a name="b37719544155919"></a><a name="b37719544155919"></a>UDP_CONNECT</strong>, <strong id="b3931576155919"><a name="b3931576155919"></a><a name="b3931576155919"></a>TCP</strong>, or <strong id="b842352706155831"><a name="b842352706155831"></a><a name="b842352706155831"></a>HTTP</strong>.</li></ul>
</td>
</tr>
<tr id="row1560063614465"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.1 "><p id="p166041636104612"><a name="p166041636104612"></a><a name="p166041636104612"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="p16610143616463"><a name="p16610143616463"></a><a name="p16610143616463"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 "><a name="ul1761411362462"></a><a name="ul1761411362462"></a><ul id="ul1761411362462"><li>Specifies the provisioning status of the health check.</li><li>The value can be <strong id="b921361675"><a name="b921361675"></a><a name="b921361675"></a>ACTIVE</strong>, <strong id="b587070153"><a name="b587070153"></a><a name="b587070153"></a>PENDING_CREATE</strong>, or <strong id="b613170128"><a name="b613170128"></a><a name="b613170128"></a>ERROR</strong>.</li><li>This parameter is reserved. The default value is <strong id="b2105456964"><a name="b2105456964"></a><a name="b2105456964"></a>ACTIVE</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  8** **members**  parameter description

<a name="table1563417579480"></a>
<table><thead align="left"><tr id="row2064116573481"><th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.4.1.1"><p id="p964445794812"><a name="p964445794812"></a><a name="p964445794812"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.4.1.2"><p id="p46450576480"><a name="p46450576480"></a><a name="p46450576480"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71.71717171717171%" id="mcps1.2.4.1.3"><p id="p1664855774817"><a name="p1664855774817"></a><a name="p1664855774817"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row565215578482"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.1 "><p id="p14993"><a name="p14993"></a><a name="p14993"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="p348372016339"><a name="p348372016339"></a><a name="p348372016339"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 "><p id="p37168116"><a name="p37168116"></a><a name="p37168116"></a>Specifies the backend server ID.</p>
</td>
</tr>
<tr id="row966215764815"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.1 "><p id="p50684498"><a name="p50684498"></a><a name="p50684498"></a>address</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="p11803692"><a name="p11803692"></a><a name="p11803692"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 "><p id="p1125094518441"><a name="p1125094518441"></a><a name="p1125094518441"></a>Specifies the private IP address of the backend server, for example, 192.168.3.11.</p>
</td>
</tr>
<tr id="row146751572485"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.1 "><p id="p66672336"><a name="p66672336"></a><a name="p66672336"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="p31750097"><a name="p31750097"></a><a name="p31750097"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 "><p id="p938311819816"><a name="p938311819816"></a><a name="p938311819816"></a>Specifies the port used by the backend server. The port number ranges from 0 to 65535.</p>
</td>
</tr>
<tr id="row969685754810"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.1 "><p id="p6699165714811"><a name="p6699165714811"></a><a name="p6699165714811"></a>operating_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="p270619570489"><a name="p270619570489"></a><a name="p270619570489"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 "><a name="ul1671095734812"></a><a name="ul1671095734812"></a><ul id="ul1671095734812"><li>Specifies the health check result of the backend server.</li><li>The value can be <strong id="b82521617917"><a name="b82521617917"></a><a name="b82521617917"></a>ONLINE</strong>, <strong id="b122511163911"><a name="b122511163911"></a><a name="b122511163911"></a>OFFLINE</strong>, <strong id="b102517161599"><a name="b102517161599"></a><a name="b102517161599"></a>DEGRADED</strong>, <strong id="b15251416992"><a name="b15251416992"></a><a name="b15251416992"></a>DISABLED</strong>, or <strong id="b122571612915"><a name="b122571612915"></a><a name="b122571612915"></a>NO_MONITOR</strong>.<a name="ul1135719201915"></a><a name="ul1135719201915"></a><ul id="ul1135719201915"><li><strong id="b96808236915"><a name="b96808236915"></a><a name="b96808236915"></a>ONLINE</strong>: The backend server is healthy.</li><li><strong id="b119107316914"><a name="b119107316914"></a><a name="b119107316914"></a>OFFLINE</strong>: The backend server is unhealthy.</li><li><strong id="b167711918118"><a name="b167711918118"></a><a name="b167711918118"></a>DEGRADED</strong>: The backend server performance is deteriorating.</li><li><strong id="b195743419912"><a name="b195743419912"></a><a name="b195743419912"></a>DISABLED</strong>: The backend server does not exist.</li><li><strong id="b15356162010911"><a name="b15356162010911"></a><a name="b15356162010911"></a>NO_MONITOR</strong>: The health check is disabled.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row872245794817"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.1 "><p id="p20724457144816"><a name="p20724457144816"></a><a name="p20724457144816"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="p9727115710489"><a name="p9727115710489"></a><a name="p9727115710489"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 "><a name="ul16729257134816"></a><a name="ul16729257134816"></a><ul id="ul16729257134816"><li>Specifies the provisioning status of the backend server.</li><li>The value can be <strong id="b14324501"><a name="b14324501"></a><a name="b14324501"></a>ACTIVE</strong>, <strong id="b422022538"><a name="b422022538"></a><a name="b422022538"></a>PENDING_CREATE</strong>, or <strong id="b1034095884"><a name="b1034095884"></a><a name="b1034095884"></a>ERROR</strong>.</li><li>This parameter is reserved. The default value is <strong id="b1399201976"><a name="b1399201976"></a><a name="b1399201976"></a>ACTIVE</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  9** **l7policies**  parameter description

<a name="table129151528185512"></a>
<table><thead align="left"><tr id="row11933172835514"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.1"><p id="p5939102865518"><a name="p5939102865518"></a><a name="p5939102865518"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="p794322835518"><a name="p794322835518"></a><a name="p794322835518"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.2.4.1.3"><p id="p159461128155514"><a name="p159461128155514"></a><a name="p159461128155514"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19509282550"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p1935143363913"><a name="p1935143363913"></a><a name="p1935143363913"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p19407184714339"><a name="p19407184714339"></a><a name="p19407184714339"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p11481033123916"><a name="p11481033123916"></a><a name="p11481033123916"></a>Specifies the forwarding policy ID.</p>
</td>
</tr>
<tr id="row129595287556"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p1664133312394"><a name="p1664133312394"></a><a name="p1664133312394"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p18701833123917"><a name="p18701833123917"></a><a name="p18701833123917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p207819333393"><a name="p207819333393"></a><a name="p207819333393"></a>Specifies the forwarding policy name.</p>
</td>
</tr>
<tr id="row49761289556"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p888633113917"><a name="p888633113917"></a><a name="p888633113917"></a>rules</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p159543303918"><a name="p159543303918"></a><a name="p159543303918"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p4104533143915"><a name="p4104533143915"></a><a name="p4104533143915"></a>Lists forwarding rules of the forwarding policy. For details of this parameter, see <a href="#table197162765814">Table 10</a>.</p>
</td>
</tr>
<tr id="row14996228175516"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p092371110147"><a name="p092371110147"></a><a name="p092371110147"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p59190112146"><a name="p59190112146"></a><a name="p59190112146"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><a name="ul284383855616"></a><a name="ul284383855616"></a><ul id="ul284383855616"><li>Specifies whether requests are forwarded to another backend server group or redirected to another HTTPS listener.</li><li>The value can be <strong id="b33816586104655"><a name="b33816586104655"></a><a name="b33816586104655"></a>REDIRECT_TO_POOL</strong> or <strong id="b35913821104655"><a name="b35913821104655"></a><a name="b35913821104655"></a>REDIRECT_TO_LISTENER</strong>.<a name="ul49734537104721"></a><a name="ul49734537104721"></a><ul id="ul49734537104721"><li><strong id="b43612444104736"><a name="b43612444104736"></a><a name="b43612444104736"></a>REDIRECT_TO_POOL</strong>: Requests are forwarded to another backend server group.</li><li><strong id="b842352706103440"><a name="b842352706103440"></a><a name="b842352706103440"></a>REDIRECT_TO_LISTENER</strong>: Requests are redirected to another HTTPS listener.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row181542975510"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p7187291557"><a name="p7187291557"></a><a name="p7187291557"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p4202297559"><a name="p4202297559"></a><a name="p4202297559"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><a name="ul1625172912552"></a><a name="ul1625172912552"></a><ul id="ul1625172912552"><li>Specifies the provisioning status of the forwarding policy.</li><li>The value can be <strong id="b1721304429"><a name="b1721304429"></a><a name="b1721304429"></a>ACTIVE</strong>, <strong id="b1931532219"><a name="b1931532219"></a><a name="b1931532219"></a>PENDING_CREATE</strong>, or <strong id="b530344059"><a name="b530344059"></a><a name="b530344059"></a>ERROR</strong>.</li><li>This parameter is reserved. The default value is <strong id="b1108456769"><a name="b1108456769"></a><a name="b1108456769"></a>ACTIVE</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  10** **rules**  parameter description

<a name="table197162765814"></a>
<table><thead align="left"><tr id="row1972617735812"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.1"><p id="p1873111785814"><a name="p1873111785814"></a><a name="p1873111785814"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="p57371476581"><a name="p57371476581"></a><a name="p57371476581"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.2.4.1.3"><p id="p37417719589"><a name="p37417719589"></a><a name="p37417719589"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row27461674582"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p1026672483412"><a name="p1026672483412"></a><a name="p1026672483412"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p024416556337"><a name="p024416556337"></a><a name="p024416556337"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p162661524153414"><a name="p162661524153414"></a><a name="p162661524153414"></a>Specifies the forwarding rule ID.</p>
</td>
</tr>
<tr id="row6760571587"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p17266122413414"><a name="p17266122413414"></a><a name="p17266122413414"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p1726616240348"><a name="p1726616240348"></a><a name="p1726616240348"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><a name="ul16514508013"></a><a name="ul16514508013"></a><ul id="ul16514508013"><li>Specifies the match type of a forwarding rule.</li><li>The value can be <strong id="b5705430310484"><a name="b5705430310484"></a><a name="b5705430310484"></a>PATH</strong> or <strong id="b4372668510484"><a name="b4372668510484"></a><a name="b4372668510484"></a>HOST_NAME</strong>.<a name="ul878084010488"></a><a name="ul878084010488"></a><ul id="ul878084010488"><li><strong id="b12331385104827"><a name="b12331385104827"></a><a name="b12331385104827"></a>PATH</strong>: matches the path in the request.</li><li><strong id="b842352706103223"><a name="b842352706103223"></a><a name="b842352706103223"></a>HOST_NAME</strong>: matches the domain name in the request.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row177958775820"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p107987720582"><a name="p107987720582"></a><a name="p107987720582"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p118025719582"><a name="p118025719582"></a><a name="p118025719582"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><a name="ul68061478581"></a><a name="ul68061478581"></a><ul id="ul68061478581"><li>Specifies the provisioning status of the forwarding rule.</li><li>The value can be <strong id="b1120770777"><a name="b1120770777"></a><a name="b1120770777"></a>ACTIVE</strong>, <strong id="b2132391268"><a name="b2132391268"></a><a name="b2132391268"></a>PENDING_CREATE</strong>, or <strong id="b1850905994"><a name="b1850905994"></a><a name="b1850905994"></a>ERROR</strong>.</li><li>This parameter is reserved. The default value is <strong id="b1543630885"><a name="b1543630885"></a><a name="b1543630885"></a>ACTIVE</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section16752112462"></a>

-   Example request

    ```
    GET https://{Endpoint}/v2.0/lbaas/loadbalancers/38278031-cfca-44be-81be-a412f618773b/statuses
    ```


-   Example response

    ```
    {
        "statuses": {
            "loadbalancer": {
                "name": "lb-jy",
                "provisioning_status": "ACTIVE",
                "listeners": [
                    {
                        "name": "listener-jy-1",
                        "provisioning_status": "ACTIVE",
                        "pools": [
                            {
                                "name": "pool-jy-1",
                                "provisioning_status": "ACTIVE",
                                "healthmonitor": {
                                    "type": "TCP",
                                    "id": "7422b51a-0ed2-4702-9429-4f88349276c6",
                                    "name": "",
                                    "provisioning_status": "ACTIVE"
                                },
                                "members": [
                                    {
                                        "protocol_port": 80,
                                        "address": "192.168.44.11",
                                        "id": "7bbf7151-0dce-4087-b316-06c7fa17b894",
                                        "operating_status": "ONLINE",
                                        "provisioning_status": "ACTIVE"
                                    }
                                ],
                                "id": "c54b3286-2349-4c5c-ade1-e6bb0b26ad18",
                                "operating_status": "ONLINE"
                            }
                        ],
                        "l7policies": [],
                        "id": "eb84c5b4-9bc5-4bee-939d-3900fb05dc7b",
                        "operating_status": "ONLINE"
                    }
                ],
                "pools": [
                    {
                        "name": "pool-jy-1",
                        "provisioning_status": "ACTIVE",
                        "healthmonitor": {
                            "type": "TCP",
                            "id": "7422b51a-0ed2-4702-9429-4f88349276c6",
                            "name": "",
                            "provisioning_status": "ACTIVE"
                        },
                        "members": [
                            {
                                "protocol_port": 80,
                                "address": "192.168.44.11",
                                "id": "7bbf7151-0dce-4087-b316-06c7fa17b894",
                                "operating_status": "ONLINE",
                                "provisioning_status": "ACTIVE"
                            }
                        ],
                        "id": "c54b3286-2349-4c5c-ade1-e6bb0b26ad18",
                        "operating_status": "ONLINE"
                    }
                ],
                "id": "38278031-cfca-44be-81be-a412f618773b",
                "operating_status": "ONLINE"
            }
        }
    }
    ```


## Status Code<a name="en-us_topic_0096561533_en-us_topic_0049139632_section15511864"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

