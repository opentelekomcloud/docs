# Querying ECSs by Tag <a name="EN-US_TOPIC_0102606095"></a>

## Function<a name="section192222559445"></a>

This API is used to filter ECSs by tag and obtain all tags of an ECS.

## URI<a name="section222245513448"></a>

POST /v1/\{project\_id\}/servers/resource\_instances/action

[Table 1](#table10820175118131)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table10820175118131"></a>
<table><thead align="left"><tr id="row6820451111313"><th class="cellrowborder" valign="top" width="17.03%" id="mcps1.2.4.1.1"><p id="p7707213"><a name="p7707213"></a><a name="p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.37%" id="mcps1.2.4.1.2"><p id="p20304554"><a name="p20304554"></a><a name="p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.60000000000001%" id="mcps1.2.4.1.3"><p id="p34056167"><a name="p34056167"></a><a name="p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8820105181314"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.4.1.1 "><p id="p13820135131314"><a name="p13820135131314"></a><a name="p13820135131314"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.4.1.2 "><p id="p1582019513134"><a name="p1582019513134"></a><a name="p1582019513134"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.60000000000001%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section625475584419"></a>

[Table 2](#table195321356132718)  describes the request parameters.

**Table  2**  Request parameters

<a name="table195321356132718"></a>
<table><thead align="left"><tr id="row853265613272"><th class="cellrowborder" valign="top" width="17.16%" id="mcps1.2.5.1.1"><p id="p1056061015287"><a name="p1056061015287"></a><a name="p1056061015287"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.26%" id="mcps1.2.5.1.2"><p id="p1560121010281"><a name="p1560121010281"></a><a name="p1560121010281"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.55%" id="mcps1.2.5.1.3"><p id="p7560111010289"><a name="p7560111010289"></a><a name="p7560111010289"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.03%" id="mcps1.2.5.1.4"><p id="p155602108289"><a name="p155602108289"></a><a name="p155602108289"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row253218562271"><td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.5.1.1 "><p id="p2935154611287"><a name="p2935154611287"></a><a name="p2935154611287"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.26%" headers="mcps1.2.5.1.2 "><p id="p15935104652818"><a name="p15935104652818"></a><a name="p15935104652818"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.3 "><p id="p1393513463287"><a name="p1393513463287"></a><a name="p1393513463287"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="49.03%" headers="mcps1.2.5.1.4 "><p id="p195139416412"><a name="p195139416412"></a><a name="p195139416412"></a>Displays the ECSs with all the specified tags. For details, see <a href="#table8638721112919">Table 3</a>.</p>
<a name="ul729224164518"></a><a name="ul729224164518"></a><ul id="ul729224164518"><li>A maximum of 10 keys are included. Each key can have a maximum of 10 values.</li><li>The structure body must be included.</li><li>This field cannot be left blank.</li><li>A key must be unique.</li><li>Values of the same key must be unique.</li></ul>
</td>
</tr>
<tr id="row16532105622710"><td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.5.1.1 "><p id="p39350465287"><a name="p39350465287"></a><a name="p39350465287"></a>not_tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.26%" headers="mcps1.2.5.1.2 "><p id="p1293594692811"><a name="p1293594692811"></a><a name="p1293594692811"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.3 "><p id="p4935104652820"><a name="p4935104652820"></a><a name="p4935104652820"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="49.03%" headers="mcps1.2.5.1.4 "><p id="p381210017461"><a name="p381210017461"></a><a name="p381210017461"></a>Displays the ECSs with none of specified tags.</p>
<a name="ul7618171794619"></a><a name="ul7618171794619"></a><ul id="ul7618171794619"><li>A maximum of 10 keys are included. Each key can have a maximum of 10 values.</li><li>The structure body must be included.</li><li>This field cannot be left blank.</li><li>Keys must be unique.</li><li>Values of the same key must be unique.</li></ul>
</td>
</tr>
<tr id="row353275611277"><td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.5.1.1 "><p id="p7935104619282"><a name="p7935104619282"></a><a name="p7935104619282"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="17.26%" headers="mcps1.2.5.1.2 "><p id="p99356465280"><a name="p99356465280"></a><a name="p99356465280"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.3 "><p id="p209356461287"><a name="p209356461287"></a><a name="p209356461287"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.03%" headers="mcps1.2.5.1.4 "><p id="p9200250164913"><a name="p9200250164913"></a><a name="p9200250164913"></a>Limits the maximum number of queried ECSs. The value cannot be a negative number. The maximum value is 1000.</p>
<a name="ul1965214204415"></a><a name="ul1965214204415"></a><ul id="ul1965214204415"><li>If the <strong id="b842352706152943"><a name="b842352706152943"></a><a name="b842352706152943"></a>action</strong> value is <strong id="b842352706152951"><a name="b842352706152951"></a><a name="b842352706152951"></a>count</strong>, this parameter is invalid.</li><li>If the <strong id="b12873725315307"><a name="b12873725315307"></a><a name="b12873725315307"></a>action</strong> value is <strong id="b842352706153013"><a name="b842352706153013"></a><a name="b842352706153013"></a>filter</strong>, the default value is <strong id="b842352706153021"><a name="b842352706153021"></a><a name="b842352706153021"></a>1000</strong>.</li></ul>
</td>
</tr>
<tr id="row11532135672711"><td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.5.1.1 "><p id="p13935134652817"><a name="p13935134652817"></a><a name="p13935134652817"></a>offset</p>
</td>
<td class="cellrowborder" valign="top" width="17.26%" headers="mcps1.2.5.1.2 "><p id="p1193504662816"><a name="p1193504662816"></a><a name="p1193504662816"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.3 "><p id="p149356468287"><a name="p149356468287"></a><a name="p149356468287"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.03%" headers="mcps1.2.5.1.4 "><p id="p983884517508"><a name="p983884517508"></a><a name="p983884517508"></a>Specifies index position. The query starts from the next piece of data indexed by this parameter. The value must be a number and cannot be a negative number.</p>
<p id="p17231571749"><a name="p17231571749"></a><a name="p17231571749"></a>This parameter is not required when data on the first page is queried. When you query the subsequent page data, the value in the response body for the query of the data on the previous page is contained in this parameter.</p>
<a name="ul129511127259"></a><a name="ul129511127259"></a><ul id="ul129511127259"><li>If the <strong id="b842352706152943_1"><a name="b842352706152943_1"></a><a name="b842352706152943_1"></a>action</strong> value is <strong id="b842352706152951_1"><a name="b842352706152951_1"></a><a name="b842352706152951_1"></a>count</strong>, this parameter is invalid.</li><li>If the <strong id="b12873725315307_1"><a name="b12873725315307_1"></a><a name="b12873725315307_1"></a>action</strong> value is <strong id="b842352706153013_1"><a name="b842352706153013_1"></a><a name="b842352706153013_1"></a>filter</strong>, the default value is <strong id="b842352706153021_1"><a name="b842352706153021_1"></a><a name="b842352706153021_1"></a>0</strong>.</li></ul>
</td>
</tr>
<tr id="row1753216566272"><td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.5.1.1 "><p id="p119356466289"><a name="p119356466289"></a><a name="p119356466289"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.26%" headers="mcps1.2.5.1.2 "><p id="p1693564642816"><a name="p1693564642816"></a><a name="p1693564642816"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.3 "><p id="p18935946142810"><a name="p18935946142810"></a><a name="p18935946142810"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.03%" headers="mcps1.2.5.1.4 "><p id="p1059442911610"><a name="p1059442911610"></a><a name="p1059442911610"></a>Specifies the operation, which can be <strong id="b842352706154359"><a name="b842352706154359"></a><a name="b842352706154359"></a>filter</strong> or <strong id="b84235270615449"><a name="b84235270615449"></a><a name="b84235270615449"></a>count</strong>.</p>
<a name="ul535538994"></a><a name="ul535538994"></a><ul id="ul535538994"><li><strong id="b842352706154442"><a name="b842352706154442"></a><a name="b842352706154442"></a>filter</strong>: filters ECSs by tag. The ECSs that meet the filter criteria are displayed on pages.</li><li><strong id="b842352706154442_1"><a name="b842352706154442_1"></a><a name="b842352706154442_1"></a>count</strong>: searches ECSs by tag. The number of ECSs that meet the search criteria is displayed.</li></ul>
</td>
</tr>
<tr id="row13532105610278"><td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.5.1.1 "><p id="p119351146112813"><a name="p119351146112813"></a><a name="p119351146112813"></a>matches</p>
</td>
<td class="cellrowborder" valign="top" width="17.26%" headers="mcps1.2.5.1.2 "><p id="p1793524611285"><a name="p1793524611285"></a><a name="p1793524611285"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.3 "><p id="p1935154617285"><a name="p1935154617285"></a><a name="p1935154617285"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="49.03%" headers="mcps1.2.5.1.4 "><p id="p1551843115315"><a name="p1551843115315"></a><a name="p1551843115315"></a>Specifies the search field, which is used to search for ECSs.</p>
<p id="p282282115537"><a name="p282282115537"></a><a name="p282282115537"></a>Currently, only <strong id="b842352706154915"><a name="b842352706154915"></a><a name="b842352706154915"></a>resource_name</strong> can be used for search. For more information, see <a href="#table2075564419352">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tag**  field description

<a name="table8638721112919"></a>
<table><thead align="left"><tr id="row9638182192913"><th class="cellrowborder" valign="top" width="17.07%" id="mcps1.2.5.1.1"><p id="p204899510491"><a name="p204899510491"></a><a name="p204899510491"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.5.1.2"><p id="p1248914564918"><a name="p1248914564918"></a><a name="p1248914564918"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.41%" id="mcps1.2.5.1.3"><p id="p1489951499"><a name="p1489951499"></a><a name="p1489951499"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.08%" id="mcps1.2.5.1.4"><p id="p1748911534916"><a name="p1748911534916"></a><a name="p1748911534916"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9638192152914"><td class="cellrowborder" valign="top" width="17.07%" headers="mcps1.2.5.1.1 "><p id="p116841114123415"><a name="p116841114123415"></a><a name="p116841114123415"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.5.1.2 "><p id="p1468491415348"><a name="p1468491415348"></a><a name="p1468491415348"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.5.1.3 "><p id="p1768410144344"><a name="p1768410144344"></a><a name="p1768410144344"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.2.5.1.4 "><p id="p10615125010247"><a name="p10615125010247"></a><a name="p10615125010247"></a>Specifies the tag key.</p>
<a name="ul936813598244"></a><a name="ul936813598244"></a><ul id="ul936813598244"><li>A key contains a maximum of 127 Unicode characters.</li><li>This field cannot be left blank.</li></ul>
</td>
</tr>
<tr id="row46381021162912"><td class="cellrowborder" valign="top" width="17.07%" headers="mcps1.2.5.1.1 "><p id="p186841314123420"><a name="p186841314123420"></a><a name="p186841314123420"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.5.1.2 "><p id="p1868481433415"><a name="p1868481433415"></a><a name="p1868481433415"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.5.1.3 "><p id="p068416140344"><a name="p068416140344"></a><a name="p068416140344"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.2.5.1.4 "><p id="p28141320102512"><a name="p28141320102512"></a><a name="p28141320102512"></a>Specifies the tag value.</p>
<a name="ul122717438253"></a><a name="ul122717438253"></a><ul id="ul122717438253"><li>Each tag contains a maximum of 10 values.</li><li>Values of the same tag must be unique.</li><li>Each value contains a maximum of 255 Unicode characters.</li><li>If this parameter is not specified, any value can be used.</li><li>The values are in the OR relationship.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  4** **match**  field description

<a name="table2075564419352"></a>
<table><thead align="left"><tr id="row475516447358"><th class="cellrowborder" valign="top" width="17.07%" id="mcps1.2.5.1.1"><p id="p12281103495"><a name="p12281103495"></a><a name="p12281103495"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.630000000000003%" id="mcps1.2.5.1.2"><p id="p544210184910"><a name="p544210184910"></a><a name="p544210184910"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.23%" id="mcps1.2.5.1.3"><p id="p174410100492"><a name="p174410100492"></a><a name="p174410100492"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.07%" id="mcps1.2.5.1.4"><p id="p844161094910"><a name="p844161094910"></a><a name="p844161094910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row075574413352"><td class="cellrowborder" valign="top" width="17.07%" headers="mcps1.2.5.1.1 "><p id="p17380257143511"><a name="p17380257143511"></a><a name="p17380257143511"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="17.630000000000003%" headers="mcps1.2.5.1.2 "><p id="p16380115718352"><a name="p16380115718352"></a><a name="p16380115718352"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.5.1.3 "><p id="p193801579351"><a name="p193801579351"></a><a name="p193801579351"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.07%" headers="mcps1.2.5.1.4 "><p id="p23438378275"><a name="p23438378275"></a><a name="p23438378275"></a>Specifies the key field to be matched.</p>
<p id="p1047715257337"><a name="p1047715257337"></a><a name="p1047715257337"></a>The tag key can only be <strong id="b842352706172034"><a name="b842352706172034"></a><a name="b842352706172034"></a>resource_name</strong>. In such a case, the tag value is the ECS name.</p>
<a name="ul1846525352715"></a><a name="ul1846525352715"></a><ul id="ul1846525352715"><li>The key must be unique, and the value is used for matching.</li><li>This field is a fixed dictionary value.</li><li>This field cannot be left blank.</li></ul>
</td>
</tr>
<tr id="row19755194423519"><td class="cellrowborder" valign="top" width="17.07%" headers="mcps1.2.5.1.1 "><p id="p9380145713514"><a name="p9380145713514"></a><a name="p9380145713514"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="17.630000000000003%" headers="mcps1.2.5.1.2 "><p id="p1380145711359"><a name="p1380145711359"></a><a name="p1380145711359"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.5.1.3 "><p id="p43801857183518"><a name="p43801857183518"></a><a name="p43801857183518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.07%" headers="mcps1.2.5.1.4 "><p id="p1214175622714"><a name="p1214175622714"></a><a name="p1214175622714"></a>Specifies the tag value.</p>
<p id="p14759181015343"><a name="p14759181015343"></a><a name="p14759181015343"></a>The tag key can only be <strong id="b842352706172034_1"><a name="b842352706172034_1"></a><a name="b842352706172034_1"></a>resource_name</strong>. In such a case, the tag value is the ECS name.</p>
<a name="ul167323292812"></a><a name="ul167323292812"></a><ul id="ul167323292812"><li>Each value contains a maximum of 255 Unicode characters.</li><li>This field cannot be left blank.</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1825415515447"></a>

[Table 5](#table725495518449)  describes the response parameters.

**Table  5**  Response parameters

<a name="table725495518449"></a>
<table><thead align="left"><tr id="row3363185511442"><th class="cellrowborder" valign="top" width="17.408259174082595%" id="mcps1.2.4.1.1"><p id="p15806308"><a name="p15806308"></a><a name="p15806308"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.61793820617938%" id="mcps1.2.4.1.2"><p id="p21995508"><a name="p21995508"></a><a name="p21995508"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61.97380261973803%" id="mcps1.2.4.1.3"><p id="p36805753"><a name="p36805753"></a><a name="p36805753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4363105574411"><td class="cellrowborder" valign="top" width="17.408259174082595%" headers="mcps1.2.4.1.1 "><p id="p13910142415446"><a name="p13910142415446"></a><a name="p13910142415446"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="20.61793820617938%" headers="mcps1.2.4.1.2 "><p id="p17910924114410"><a name="p17910924114410"></a><a name="p17910924114410"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="61.97380261973803%" headers="mcps1.2.4.1.3 "><p id="p17910202454413"><a name="p17910202454413"></a><a name="p17910202454413"></a>Specifies returned ECSs. For details, see <a href="#table790793515528">Table 6</a>.</p>
</td>
</tr>
<tr id="row13254131794410"><td class="cellrowborder" valign="top" width="17.408259174082595%" headers="mcps1.2.4.1.1 "><p id="p189108241448"><a name="p189108241448"></a><a name="p189108241448"></a>total_count</p>
</td>
<td class="cellrowborder" valign="top" width="20.61793820617938%" headers="mcps1.2.4.1.2 "><p id="p3910224134420"><a name="p3910224134420"></a><a name="p3910224134420"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="61.97380261973803%" headers="mcps1.2.4.1.3 "><p id="p1891052414418"><a name="p1891052414418"></a><a name="p1891052414418"></a>Specifies the total number of queried ECSs.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **resource**  field description

<a name="table790793515528"></a>
<table><thead align="left"><tr id="row1790773517524"><th class="cellrowborder" valign="top" width="20.549999999999997%" id="mcps1.2.4.1.1"><p id="p163537196379"><a name="p163537196379"></a><a name="p163537196379"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.4%" id="mcps1.2.4.1.2"><p id="p4367119113715"><a name="p4367119113715"></a><a name="p4367119113715"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62.050000000000004%" id="mcps1.2.4.1.3"><p id="p143671019113713"><a name="p143671019113713"></a><a name="p143671019113713"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row189071535205220"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p74711505311"><a name="p74711505311"></a><a name="p74711505311"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.4%" headers="mcps1.2.4.1.2 "><p id="p12476517531"><a name="p12476517531"></a><a name="p12476517531"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.050000000000004%" headers="mcps1.2.4.1.3 "><p id="p134795115319"><a name="p134795115319"></a><a name="p134795115319"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="row690773585214"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p84715165315"><a name="p84715165315"></a><a name="p84715165315"></a>resource_detail</p>
</td>
<td class="cellrowborder" valign="top" width="17.4%" headers="mcps1.2.4.1.2 "><p id="p15475545313"><a name="p15475545313"></a><a name="p15475545313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.050000000000004%" headers="mcps1.2.4.1.3 "><p id="p2473535313"><a name="p2473535313"></a><a name="p2473535313"></a>Queries ECS details.</p>
</td>
</tr>
<tr id="row1907113516524"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p1647195105319"><a name="p1647195105319"></a><a name="p1647195105319"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.4%" headers="mcps1.2.4.1.2 "><p id="p154765195313"><a name="p154765195313"></a><a name="p154765195313"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="62.050000000000004%" headers="mcps1.2.4.1.3 "><p id="p447205175313"><a name="p447205175313"></a><a name="p447205175313"></a>Specifies tags.</p>
</td>
</tr>
<tr id="row129076356521"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p64735205317"><a name="p64735205317"></a><a name="p64735205317"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.4%" headers="mcps1.2.4.1.2 "><p id="p194725135314"><a name="p194725135314"></a><a name="p194725135314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.050000000000004%" headers="mcps1.2.4.1.3 "><p id="p1847205115317"><a name="p1847205115317"></a><a name="p1847205115317"></a>Specifies the resource name, which is the ECS name.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **resource\_tag**  field description

<a name="table173144214534"></a>
<table><thead align="left"><tr id="row3314621125312"><th class="cellrowborder" valign="top" width="20.4%" id="mcps1.2.4.1.1"><p id="p1265913224374"><a name="p1265913224374"></a><a name="p1265913224374"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.61%" id="mcps1.2.4.1.2"><p id="p186591522143716"><a name="p186591522143716"></a><a name="p186591522143716"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61.99%" id="mcps1.2.4.1.3"><p id="p2659182283715"><a name="p2659182283715"></a><a name="p2659182283715"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1431416211537"><td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.1 "><p id="p159081145185319"><a name="p159081145185319"></a><a name="p159081145185319"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.2 "><p id="p1290844513537"><a name="p1290844513537"></a><a name="p1290844513537"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.99%" headers="mcps1.2.4.1.3 "><p id="p789502782812"><a name="p789502782812"></a><a name="p789502782812"></a>Specifies the tag key.</p>
<a name="ul5216143772810"></a><a name="ul5216143772810"></a><ul id="ul5216143772810"><li>It contains a maximum of 36 Unicode characters.</li><li>This field cannot be left blank.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li></ul>
</td>
</tr>
<tr id="row931452113533"><td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.2.4.1.1 "><p id="p09082453534"><a name="p09082453534"></a><a name="p09082453534"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.2 "><p id="p1790854513539"><a name="p1790854513539"></a><a name="p1790854513539"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.99%" headers="mcps1.2.4.1.3 "><p id="p9585104018283"><a name="p9585104018283"></a><a name="p9585104018283"></a>Specifies the tag value.</p>
<a name="ul1285455122812"></a><a name="ul1285455122812"></a><ul id="ul1285455122812"><li>Each value contains a maximum of 43 Unicode characters.</li><li>This field can be left blank.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li></ul>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section192136383502"></a>

```
POST https://{endpoint}/v1/{project_id}/servers/resource_instances/action
```

```
{
    "offset": "100", 
    "limit": "100", 
    "action": "filter", 
    "matches":[
    {
        "key": "resource_name", 
        "value": "ecs_test"
     }], 
    "tags": [
    {
        "key": "key1", 
        "values": [
            "value1", 
            "value2"
        ]
    }]
}
```

## Example Response<a name="section116031944014"></a>

-   Response body when  **action**  is set to  **filter**

    ```
    {
          "resources": [
             {
                "resource_detail": null, 
                "resource_id": "cdfs_cefs_wesas_12_dsad", 
                "resource_name": "ecs_test", 
                "tags": [
                    {
                       "key": "key1",
                       "value": "value1"
                    }
                 ]
             }
           ], 
          "total_count": 1000
    }
    ```


-   Response body when  **action**  is set to  **count**

    ```
    {
           "total_count": 1000
    }
    ```


## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).

