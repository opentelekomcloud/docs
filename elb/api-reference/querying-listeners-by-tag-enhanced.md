# Querying Listeners by Tag<a name="EN-US_TOPIC_0109852832"></a>

## Function<a name="en-us_topic_0094115926_section33422852114539"></a>

This API is used to query listeners by tag.

## URI<a name="en-us_topic_0094115926_section4741864114539"></a>

POST /v2.0/\{project\_id\}/listeners/resource\_instances/action

**Table  1**  Parameter description

<a name="table33323423"></a>
<table><thead align="left"><tr id="row8420641"><th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.1"><p id="p10983320"><a name="p10983320"></a><a name="p10983320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p17233719"><a name="p17233719"></a><a name="p17233719"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p4164548117122"><a name="p4164548117122"></a><a name="p4164548117122"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.5.1.4"><p id="p53754023"><a name="p53754023"></a><a name="p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53906008171138"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p16126074171144"><a name="p16126074171144"></a><a name="p16126074171144"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p31143627171144"><a name="p31143627171144"></a><a name="p31143627171144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p39605860171144"><a name="p39605860171144"></a><a name="p39605860171144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the tag is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0094115926_section4877123114539"></a>

None

## Request<a name="en-us_topic_0094115926_section65761899114539"></a>

**Table  2**  Request parameters

<a name="table45361916161515"></a>
<table><thead align="left"><tr id="row25361166157"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="p1195855641516"><a name="p1195855641516"></a><a name="p1195855641516"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p15958155671520"><a name="p15958155671520"></a><a name="p15958155671520"></a><strong id="b1486653138"><a name="b1486653138"></a><a name="b1486653138"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p1958756161512"><a name="p1958756161512"></a><a name="p1958756161512"></a><strong id="b1851374365"><a name="b1851374365"></a><a name="b1851374365"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.5.1.4"><p id="p1595885611514"><a name="p1595885611514"></a><a name="p1595885611514"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17537131615157"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p1641271415168"><a name="p1641271415168"></a><a name="p1641271415168"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p16412181411616"><a name="p16412181411616"></a><a name="p16412181411616"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101983303_p4459890810595"><a name="en-us_topic_0101983303_p4459890810595"></a><a name="en-us_topic_0101983303_p4459890810595"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p7413131471620"><a name="p7413131471620"></a><a name="p7413131471620"></a>Specifies the included tags. A maximum of 10 tag keys are allowed for each query operation. Each tag key can have up to 10 tag values. The structure body must be included. The tag key cannot be left blank or set to an empty string. Each tag key and each tag value of the same tag key must be unique. For details, see <a href="#table202620276214">Table 3</a>.</p>
</td>
</tr>
<tr id="row1253771619151"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p18413814131611"><a name="p18413814131611"></a><a name="p18413814131611"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p9413181421618"><a name="p9413181421618"></a><a name="p9413181421618"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p1541311141169"><a name="p1541311141169"></a><a name="p1541311141169"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p174135147169"><a name="p174135147169"></a><a name="p174135147169"></a>Sets the page size. This parameter is available when <strong id="b842352706112419"><a name="b842352706112419"></a><a name="b842352706112419"></a>action</strong> is set to <strong id="b842352706112428"><a name="b842352706112428"></a><a name="b842352706112428"></a>filter</strong>. Both the default value and maximum value are <strong id="b842352706112658"><a name="b842352706112658"></a><a name="b842352706112658"></a>1000</strong>, and the minimum value is <strong id="b842352706112710"><a name="b842352706112710"></a><a name="b842352706112710"></a>1</strong>. The value cannot be a negative integer.</p>
</td>
</tr>
<tr id="row55371416101510"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p10413161410165"><a name="p10413161410165"></a><a name="p10413161410165"></a>offset</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p441319149167"><a name="p441319149167"></a><a name="p441319149167"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p1041315146163"><a name="p1041315146163"></a><a name="p1041315146163"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p441321461612"><a name="p441321461612"></a><a name="p441321461612"></a>Specifies the index position. The query starts from the next listener indexed by this parameter. This parameter is not required when you query listeners on the first page. The value in the response returned for querying the listeners on the previous page will be included in this parameter for querying the listeners on subsequent pages. This parameter is not available when <strong id="b1124678678165222"><a name="b1124678678165222"></a><a name="b1124678678165222"></a>action</strong> is set to <strong id="b492491814165222"><a name="b492491814165222"></a><a name="b492491814165222"></a>count</strong>. If <strong id="b1521445588165222"><a name="b1521445588165222"></a><a name="b1521445588165222"></a>action</strong> is set to <strong id="b1990372348165222"><a name="b1990372348165222"></a><a name="b1990372348165222"></a>filter</strong>, the value must be a positive integer, and the default value is <strong id="b1833821991165222"><a name="b1833821991165222"></a><a name="b1833821991165222"></a>0</strong>.</p>
</td>
</tr>
<tr id="row6537316201518"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p104136141162"><a name="p104136141162"></a><a name="p104136141162"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p14413914121616"><a name="p14413914121616"></a><a name="p14413914121616"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p2413121415169"><a name="p2413121415169"></a><a name="p2413121415169"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p922174894318"><a name="p922174894318"></a><a name="p922174894318"></a>Identifies the operation. The value can be <strong id="b11221548164310"><a name="b11221548164310"></a><a name="b11221548164310"></a>filter</strong> or <strong id="b522948184315"><a name="b522948184315"></a><a name="b522948184315"></a>count</strong>.</p>
<a name="ul161291572439"></a><a name="ul161291572439"></a><ul id="ul161291572439"><li><strong id="b1712825704311"><a name="b1712825704311"></a><a name="b1712825704311"></a>filter</strong>: indicates pagination query.</li><li><strong id="b114084596432"><a name="b114084596432"></a><a name="b114084596432"></a>count</strong>: indicates that all listeners meeting the search criteria will be returned.</li></ul>
</td>
</tr>
<tr id="row12537616151510"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p1841315149165"><a name="p1841315149165"></a><a name="p1841315149165"></a>matches</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1641311471616"><a name="p1641311471616"></a><a name="p1641311471616"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p1041371441613"><a name="p1041371441613"></a><a name="p1041371441613"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p141391419169"><a name="p141391419169"></a><a name="p141391419169"></a>Specifies the search criteria. The tag key is the parameter to match, for example, <strong id="b84235270615351"><a name="b84235270615351"></a><a name="b84235270615351"></a>resource_name</strong>. <strong id="b201314374336"><a name="b201314374336"></a><a name="b201314374336"></a>value</strong> indicates the value of the match content. The key is a fixed dictionary value.</p>
<p id="p2413514131614"><a name="p2413514131614"></a><a name="p2413514131614"></a>Determine whether fuzzy match is required based on different parameters. For example, if the <strong id="b8423527062245"><a name="b8423527062245"></a><a name="b8423527062245"></a>key</strong> is <strong id="b842352706123028"><a name="b842352706123028"></a><a name="b842352706123028"></a>resource_name</strong>, fuzzy search is used by default. If <strong id="b842352706123110"><a name="b842352706123110"></a><a name="b842352706123110"></a>value</strong> is an empty string, exact match is used. If the key is <strong id="b842352706104855"><a name="b842352706104855"></a><a name="b842352706104855"></a>resource_id</strong>, exact match is used. Currently, only <strong id="b84235270615520"><a name="b84235270615520"></a><a name="b84235270615520"></a>resource_name</strong> can be used for search. For details, see <a href="#table5401017132210">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tags**  parameter description

<a name="table202620276214"></a>
<table><thead align="left"><tr id="row72713274217"><th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.1"><p id="p12459548182120"><a name="p12459548182120"></a><a name="p12459548182120"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p17459174813215"><a name="p17459174813215"></a><a name="p17459174813215"></a><strong id="b1597273864"><a name="b1597273864"></a><a name="b1597273864"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p134601048102118"><a name="p134601048102118"></a><a name="p134601048102118"></a><strong id="b1327668137"><a name="b1327668137"></a><a name="b1327668137"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.5.1.4"><p id="p246016488214"><a name="p246016488214"></a><a name="p246016488214"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1276279216"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p5460248152117"><a name="p5460248152117"></a><a name="p5460248152117"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p194601648202120"><a name="p194601648202120"></a><a name="p194601648202120"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p5460104812219"><a name="p5460104812219"></a><a name="p5460104812219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p7460104842119"><a name="p7460104842119"></a><a name="p7460104842119"></a>Specifies the tag key. It contains a maximum of 127 Unicode characters and cannot be left blank. (This parameter is not verified in the search process.)</p>
</td>
</tr>
<tr id="row162720275211"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p164601848102117"><a name="p164601848102117"></a><a name="p164601848102117"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1146044832118"><a name="p1146044832118"></a><a name="p1146044832118"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p1471110311293"><a name="p1471110311293"></a><a name="p1471110311293"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p446018484216"><a name="p446018484216"></a><a name="p446018484216"></a>Lists the tag values. Each tag value can contain a maximum of 255 Unicode characters. The values are in the OR relationship.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **matches**  parameter description

<a name="table5401017132210"></a>
<table><thead align="left"><tr id="row0401217152213"><th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.5.1.1"><p id="p15349101932318"><a name="p15349101932318"></a><a name="p15349101932318"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.2"><p id="p434991918236"><a name="p434991918236"></a><a name="p434991918236"></a><strong id="b919222919"><a name="b919222919"></a><a name="b919222919"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.3"><p id="p203491719112319"><a name="p203491719112319"></a><a name="p203491719112319"></a><strong id="b9577274"><a name="b9577274"></a><a name="b9577274"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="60.60606060606061%" id="mcps1.2.5.1.4"><p id="p63494194233"><a name="p63494194233"></a><a name="p63494194233"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1640161710227"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.1 "><p id="p9349131912315"><a name="p9349131912315"></a><a name="p9349131912315"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.2 "><p id="p16349119122310"><a name="p16349119122310"></a><a name="p16349119122310"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p1034981914239"><a name="p1034981914239"></a><a name="p1034981914239"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.5.1.4 "><p id="p1663653761117"><a name="p1663653761117"></a><a name="p1663653761117"></a>Specifies the tag key.</p>
<p id="p2749183921115"><a name="p2749183921115"></a><a name="p2749183921115"></a>The value can be one of the following:</p>
<a name="ul1413954313116"></a><a name="ul1413954313116"></a><ul id="ul1413954313116"><li><strong id="b181901216154817"><a name="b181901216154817"></a><a name="b181901216154817"></a>resource_name</strong>: indicates the resource name.</li></ul>
</td>
</tr>
<tr id="row5401111722214"><td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.1 "><p id="p17349719122311"><a name="p17349719122311"></a><a name="p17349719122311"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.2 "><p id="p73491519152311"><a name="p73491519152311"></a><a name="p73491519152311"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p8349219172319"><a name="p8349219172319"></a><a name="p8349219172319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.5.1.4 "><p id="p183491919132316"><a name="p183491919132316"></a><a name="p183491919132316"></a>Specifies the tag value. Each tag value can contain a maximum of 255 Unicode characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0094115926_section24696125114539"></a>

**Table  5**  Response parameters

<a name="table5837112592520"></a>
<table><thead align="left"><tr id="row18838132515253"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p597873482514"><a name="p597873482514"></a><a name="p597873482514"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p18978183420259"><a name="p18978183420259"></a><a name="p18978183420259"></a><strong id="b1726450967"><a name="b1726450967"></a><a name="b1726450967"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.4.1.3"><p id="p097893432512"><a name="p097893432512"></a><a name="p097893432512"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1683862519250"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p1978534142519"><a name="p1978534142519"></a><a name="p1978534142519"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p19691062298"><a name="p19691062298"></a><a name="p19691062298"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0101985068_p12131870113812"><a name="en-us_topic_0101985068_p12131870113812"></a><a name="en-us_topic_0101985068_p12131870113812"></a>Lists the listeners. For details, see <a href="#table2019842119305">Table 6</a>.</p>
</td>
</tr>
<tr id="row1683832510255"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p8978193419253"><a name="p8978193419253"></a><a name="p8978193419253"></a>total_count</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p59782346259"><a name="p59782346259"></a><a name="p59782346259"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p2097817343255"><a name="p2097817343255"></a><a name="p2097817343255"></a>Specifies the total number of queried records.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **resource**  parameter description

<a name="table2019842119305"></a>
<table><thead align="left"><tr id="row7199921173020"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p138175295308"><a name="p138175295308"></a><a name="p138175295308"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p5818182918305"><a name="p5818182918305"></a><a name="p5818182918305"></a><strong id="b1966778441"><a name="b1966778441"></a><a name="b1966778441"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.4.1.3"><p id="p16818102914302"><a name="p16818102914302"></a><a name="p16818102914302"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row41991021193013"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p381882915306"><a name="p381882915306"></a><a name="p381882915306"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p0818229113014"><a name="p0818229113014"></a><a name="p0818229113014"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p17818142983014"><a name="p17818142983014"></a><a name="p17818142983014"></a>Specifies the resource ID.</p>
</td>
</tr>
<tr id="row1919914214302"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p7818929163011"><a name="p7818929163011"></a><a name="p7818929163011"></a>resource_detail</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p8818132913307"><a name="p8818132913307"></a><a name="p8818132913307"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p13818029113013"><a name="p13818029113013"></a><a name="p13818029113013"></a>Specifies the resource details. The value is a resource object, used for extension. The value is left blank by default.</p>
</td>
</tr>
<tr id="row1319962143011"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p68181429193013"><a name="p68181429193013"></a><a name="p68181429193013"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p61283902916"><a name="p61283902916"></a><a name="p61283902916"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p4818122923012"><a name="p4818122923012"></a><a name="p4818122923012"></a>Lists the tags. If there is no tag, an empty array is used by default. For details, see <a href="#table15683233145412">Table 7</a>.</p>
</td>
</tr>
<tr id="row1719962117305"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p181882918304"><a name="p181882918304"></a><a name="p181882918304"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p1481882916302"><a name="p1481882916302"></a><a name="p1481882916302"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p38183292304"><a name="p38183292304"></a><a name="p38183292304"></a>Specifies the resource name. This parameter is an empty string by default if there is no resource name.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **tags**  parameter description

<a name="table15683233145412"></a>
<table><thead align="left"><tr id="row12684733125410"><th class="cellrowborder" valign="top" width="22.772277227722775%" id="mcps1.2.4.1.1"><p id="p5684933185414"><a name="p5684933185414"></a><a name="p5684933185414"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.4.1.2"><p id="p36841533155417"><a name="p36841533155417"></a><a name="p36841533155417"></a><strong id="b437765163"><a name="b437765163"></a><a name="b437765163"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.42574257425742%" id="mcps1.2.4.1.3"><p id="p3684153320546"><a name="p3684153320546"></a><a name="p3684153320546"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1668411338548"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.4.1.1 "><p id="p1684193355413"><a name="p1684193355413"></a><a name="p1684193355413"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.4.1.2 "><p id="p9684173325410"><a name="p9684173325410"></a><a name="p9684173325410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.4.1.3 "><p id="p13684143310547"><a name="p13684143310547"></a><a name="p13684143310547"></a>Specifies the tag key. It contains a maximum of 127 Unicode characters and cannot be left blank. (This parameter is not verified in the search process.)</p>
</td>
</tr>
<tr id="row26849339548"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.4.1.1 "><p id="p2684183316545"><a name="p2684183316545"></a><a name="p2684183316545"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.4.1.2 "><p id="p4684433185412"><a name="p4684433185412"></a><a name="p4684433185412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.4.1.3 "><p id="p9684173316541"><a name="p9684173316541"></a><a name="p9684173316541"></a>Specifies the tag value. Each tag value can contain a maximum of 255 Unicode characters.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section2495193617305"></a>

-   Example request 1 \(when  **action**  is set to  **filter**\)

    ```
    POST https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/listeners/resource_instances/action
    
    {
        "offset": "100", 
        "limit": "100", 
        "action": "filter", 
        "matches": [
            {
                "key": "resource_name", 
                "value": "resource1"
            }
        ], 
        "tags": [
            {
                "key": "key1", 
                "values": [
                    "*value1", 
                    "value2"
                ]
            }
        ]
    }
    ```


-   Example response 1

    ```
    {
        "resources": [
            {
                "resource_detail":"", 
                "resource_id": "154d135b-3a89-4e89-8023-06efb9acdc05", 
                "resource_name": "resouece1", 
                "tags": [
                    {
                        "key": "key1", 
                        "value": "value1"
                    }, 
                    {
                        "key": "key2", 
                        "value": "value1"
                    }
                ]
            }
        ], 
        "total_count": 1000
    }
    ```

-   Example request 2 \(when  **action**  is set to  **count**\)

    ```
    POST https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/listeners/resource_instances/action
    
    {
        "action": "count", 
        "tags": [
            {
                "key": "key1", 
                "values": [
                    "value1", 
                    "value2"
                ]
            }, 
            {
                "key": "key2", 
                "values": [
                    "value1", 
                    "value2"
                ]
            }
        ], 
        "matches": [
            {
                "key": "resource_name", 
                "value": "resource1"
            }
        ]
    }
    ```

-   Example response 2

    ```
    {
        "total_count": 1000
    }
    ```


## Status Code<a name="en-us_topic_0094115926_section1030264817164"></a>

For details, see  [Status Codes](status-codes-enhanced.md).

