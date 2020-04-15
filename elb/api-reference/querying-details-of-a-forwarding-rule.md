# Querying Details of a Forwarding Rule<a name="EN-US_TOPIC_0116649235"></a>

## Function<a name="en-us_topic_0082661926_section3977498515419"></a>

This API is used to query details about a forwarding rule using its ID.

## URI<a name="section493496615419"></a>

GET /v2.0/lbaas/l7policies/\{l7policy\_id\}/rules/\{l7rule\_id\}

**Table  1**  Parameter description

<a name="table1344812955613"></a>
<table><thead align="left"><tr id="row12492129155610"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p549215914564"><a name="p549215914564"></a><a name="p549215914564"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p27256578102"><a name="p27256578102"></a><a name="p27256578102"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="p1949259185618"><a name="p1949259185618"></a><a name="p1949259185618"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.5.1.4"><p id="p14492129165617"><a name="p14492129165617"></a><a name="p14492129165617"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row249219195618"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p14929911564"><a name="p14929911564"></a><a name="p14929911564"></a>l7policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p127264576101"><a name="p127264576101"></a><a name="p127264576101"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p14921914569"><a name="p14921914569"></a><a name="p14921914569"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p10492179145620"><a name="p10492179145620"></a><a name="p10492179145620"></a>Specifies the forwarding policy ID.</p>
</td>
</tr>
<tr id="row15492199125618"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p1449212915560"><a name="p1449212915560"></a><a name="p1449212915560"></a>l7rule_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p12726125720105"><a name="p12726125720105"></a><a name="p12726125720105"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p134928925620"><a name="p134928925620"></a><a name="p134928925620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p144922913566"><a name="p144922913566"></a><a name="p144922913566"></a>Specifies the forwarding rule ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0082661926_section999145115419"></a>

None

## Response<a name="section134822533120"></a>

**Table  2**  Response parameters

<a name="table33929591566"></a>
<table><thead align="left"><tr id="row1157945913569"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p20579145975614"><a name="p20579145975614"></a><a name="p20579145975614"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="p175790594566"><a name="p175790594566"></a><a name="p175790594566"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.4.1.3"><p id="p2057913599561"><a name="p2057913599561"></a><a name="p2057913599561"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1157935917568"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p957965912569"><a name="p957965912569"></a><a name="p957965912569"></a>rule</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p157985914567"><a name="p157985914567"></a><a name="p157985914567"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p145791259175615"><a name="p145791259175615"></a><a name="p145791259175615"></a>Specifies the forwarding rule. For details, see <a href="#table239892725716">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **rule**  parameter description

<a name="table239892725716"></a>
<table><thead align="left"><tr id="en-us_topic_0116649236_row18222814135918"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="en-us_topic_0116649236_p102227144592"><a name="en-us_topic_0116649236_p102227144592"></a><a name="en-us_topic_0116649236_p102227144592"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="en-us_topic_0116649236_p922291411591"><a name="en-us_topic_0116649236_p922291411591"></a><a name="en-us_topic_0116649236_p922291411591"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="en-us_topic_0116649236_p98675571208"><a name="en-us_topic_0116649236_p98675571208"></a><a name="en-us_topic_0116649236_p98675571208"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0116649236_row102221114205912"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0116649236_p122261415596"><a name="en-us_topic_0116649236_p122261415596"></a><a name="en-us_topic_0116649236_p122261415596"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0116649236_p923119572119"><a name="en-us_topic_0116649236_p923119572119"></a><a name="en-us_topic_0116649236_p923119572119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0116649236_p52228141594"><a name="en-us_topic_0116649236_p52228141594"></a><a name="en-us_topic_0116649236_p52228141594"></a>Specifies the forwarding rule ID.</p>
</td>
</tr>
<tr id="en-us_topic_0116649236_row202222146591"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0116649236_p11222111412593"><a name="en-us_topic_0116649236_p11222111412593"></a><a name="en-us_topic_0116649236_p11222111412593"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0116649236_p4222914145911"><a name="en-us_topic_0116649236_p4222914145911"></a><a name="en-us_topic_0116649236_p4222914145911"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0116649236_p1266711718204"><a name="en-us_topic_0116649236_p1266711718204"></a><a name="en-us_topic_0116649236_p1266711718204"></a>Specifies the ID of the project where the forwarding rule is used.</p>
<p id="en-us_topic_0116649236_p54077531303"><a name="en-us_topic_0116649236_p54077531303"></a><a name="en-us_topic_0116649236_p54077531303"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0116649236_row722213149597"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0116649236_p1622251465915"><a name="en-us_topic_0116649236_p1622251465915"></a><a name="en-us_topic_0116649236_p1622251465915"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0116649236_p19222111414597"><a name="en-us_topic_0116649236_p19222111414597"></a><a name="en-us_topic_0116649236_p19222111414597"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0116649236_p1979757131619"><a name="en-us_topic_0116649236_p1979757131619"></a><a name="en-us_topic_0116649236_p1979757131619"></a>Specifies the administrative status of the forwarding rule.</p>
<p id="en-us_topic_0116649236_p179812717162"><a name="en-us_topic_0116649236_p179812717162"></a><a name="en-us_topic_0116649236_p179812717162"></a>The value can be <strong id="en-us_topic_0116649236_b194855147820"><a name="en-us_topic_0116649236_b194855147820"></a><a name="en-us_topic_0116649236_b194855147820"></a>true</strong> or <strong id="en-us_topic_0116649236_b1248715141382"><a name="en-us_topic_0116649236_b1248715141382"></a><a name="en-us_topic_0116649236_b1248715141382"></a>false</strong>.</p>
<p id="en-us_topic_0116649236_p159731852204013"><a name="en-us_topic_0116649236_p159731852204013"></a><a name="en-us_topic_0116649236_p159731852204013"></a>This parameter is reserved. The default value is <strong id="en-us_topic_0116649236_b136295564412"><a name="en-us_topic_0116649236_b136295564412"></a><a name="en-us_topic_0116649236_b136295564412"></a>true</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0116649236_row4224114155917"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0116649236_p92241147592"><a name="en-us_topic_0116649236_p92241147592"></a><a name="en-us_topic_0116649236_p92241147592"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0116649236_p222481475913"><a name="en-us_topic_0116649236_p222481475913"></a><a name="en-us_topic_0116649236_p222481475913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0116649236_p199311319151611"><a name="en-us_topic_0116649236_p199311319151611"></a><a name="en-us_topic_0116649236_p199311319151611"></a>Specifies the match type of a forwarding rule.</p>
<p id="en-us_topic_0116649236_p293131991615"><a name="en-us_topic_0116649236_p293131991615"></a><a name="en-us_topic_0116649236_p293131991615"></a>The value can be one of the following:</p>
<a name="en-us_topic_0116649236_ul13931161917169"></a><a name="en-us_topic_0116649236_ul13931161917169"></a><ul id="en-us_topic_0116649236_ul13931161917169"><li><strong id="en-us_topic_0116649236_b142851011164818"><a name="en-us_topic_0116649236_b142851011164818"></a><a name="en-us_topic_0116649236_b142851011164818"></a>HOST_NAME</strong>: matches the domain name in the request.</li><li><strong id="en-us_topic_0116649236_b11681722194812"><a name="en-us_topic_0116649236_b11681722194812"></a><a name="en-us_topic_0116649236_b11681722194812"></a>PATH</strong>: matches the path in the request.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0116649236_row622461465910"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0116649236_p162241814165916"><a name="en-us_topic_0116649236_p162241814165916"></a><a name="en-us_topic_0116649236_p162241814165916"></a>compare_type</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0116649236_p12241214105911"><a name="en-us_topic_0116649236_p12241214105911"></a><a name="en-us_topic_0116649236_p12241214105911"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0116649236_p928234417166"><a name="en-us_topic_0116649236_p928234417166"></a><a name="en-us_topic_0116649236_p928234417166"></a>Specifies the match mode. The options are as follows:</p>
<p id="en-us_topic_0116649236_p112828447167"><a name="en-us_topic_0116649236_p112828447167"></a><a name="en-us_topic_0116649236_p112828447167"></a>When <strong id="en-us_topic_0116649236_b164379297485"><a name="en-us_topic_0116649236_b164379297485"></a><a name="en-us_topic_0116649236_b164379297485"></a>type</strong> is set to <strong id="en-us_topic_0116649236_b2043819291487"><a name="en-us_topic_0116649236_b2043819291487"></a><a name="en-us_topic_0116649236_b2043819291487"></a>HOST_NAME</strong>, the value of this parameter can only be the following:</p>
<a name="en-us_topic_0116649236_ul128264412167"></a><a name="en-us_topic_0116649236_ul128264412167"></a><ul id="en-us_topic_0116649236_ul128264412167"><li><strong id="en-us_topic_0116649236_b16405014151016"><a name="en-us_topic_0116649236_b16405014151016"></a><a name="en-us_topic_0116649236_b16405014151016"></a>EQUAL_TO</strong>: indicates exact match.</li></ul>
<p id="en-us_topic_0116649236_p2028224451611"><a name="en-us_topic_0116649236_p2028224451611"></a><a name="en-us_topic_0116649236_p2028224451611"></a>When <strong id="en-us_topic_0116649236_b18170829496"><a name="en-us_topic_0116649236_b18170829496"></a><a name="en-us_topic_0116649236_b18170829496"></a>type</strong> is set to <strong id="en-us_topic_0116649236_b517115211498"><a name="en-us_topic_0116649236_b517115211498"></a><a name="en-us_topic_0116649236_b517115211498"></a>PATH</strong>, the value of this parameter can be one of the following:</p>
<a name="en-us_topic_0116649236_ul162821144131610"></a><a name="en-us_topic_0116649236_ul162821144131610"></a><ul id="en-us_topic_0116649236_ul162821144131610"><li><strong id="en-us_topic_0116649236_b1628118511493"><a name="en-us_topic_0116649236_b1628118511493"></a><a name="en-us_topic_0116649236_b1628118511493"></a>REGEX</strong>: indicates regular expression match.</li><li><strong id="en-us_topic_0116649236_b8539988491"><a name="en-us_topic_0116649236_b8539988491"></a><a name="en-us_topic_0116649236_b8539988491"></a>STARTS_WITH</strong>: indicates prefix match.</li><li><strong id="en-us_topic_0116649236_b39271823111019"><a name="en-us_topic_0116649236_b39271823111019"></a><a name="en-us_topic_0116649236_b39271823111019"></a>EQUAL_TO</strong>: indicates exact match.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0116649236_row322461410591"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0116649236_p622481485911"><a name="en-us_topic_0116649236_p622481485911"></a><a name="en-us_topic_0116649236_p622481485911"></a>invert</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0116649236_p1622411412594"><a name="en-us_topic_0116649236_p1622411412594"></a><a name="en-us_topic_0116649236_p1622411412594"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0116649236_p1837110431511"><a name="en-us_topic_0116649236_p1837110431511"></a><a name="en-us_topic_0116649236_p1837110431511"></a>Specifies whether reverse match is supported.</p>
<p id="en-us_topic_0116649236_p1497849152414"><a name="en-us_topic_0116649236_p1497849152414"></a><a name="en-us_topic_0116649236_p1497849152414"></a>The value can be <strong id="en-us_topic_0116649236_b27267458912"><a name="en-us_topic_0116649236_b27267458912"></a><a name="en-us_topic_0116649236_b27267458912"></a>true</strong> or <strong id="en-us_topic_0116649236_b27281845194"><a name="en-us_topic_0116649236_b27281845194"></a><a name="en-us_topic_0116649236_b27281845194"></a>false</strong>. The default value is <strong id="en-us_topic_0116649236_b189421423910"><a name="en-us_topic_0116649236_b189421423910"></a><a name="en-us_topic_0116649236_b189421423910"></a>false</strong>.</p>
<p id="en-us_topic_0116649236_p1828957181510"><a name="en-us_topic_0116649236_p1828957181510"></a><a name="en-us_topic_0116649236_p1828957181510"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="en-us_topic_0116649236_row19224714125916"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0116649236_p172241014165910"><a name="en-us_topic_0116649236_p172241014165910"></a><a name="en-us_topic_0116649236_p172241014165910"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0116649236_p922415146591"><a name="en-us_topic_0116649236_p922415146591"></a><a name="en-us_topic_0116649236_p922415146591"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0116649236_p781771561717"><a name="en-us_topic_0116649236_p781771561717"></a><a name="en-us_topic_0116649236_p781771561717"></a>Specifies the key of the match content. The default value is <strong id="en-us_topic_0116649236_b485293415910"><a name="en-us_topic_0116649236_b485293415910"></a><a name="en-us_topic_0116649236_b485293415910"></a>null</strong>.</p>
<p id="en-us_topic_0116649236_p198171615161716"><a name="en-us_topic_0116649236_p198171615161716"></a><a name="en-us_topic_0116649236_p198171615161716"></a>This parameter is reserved.</p>
<p id="en-us_topic_0116649236_p463514574308"><a name="en-us_topic_0116649236_p463514574308"></a><a name="en-us_topic_0116649236_p463514574308"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0116649236_row622481417593"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0116649236_p15224151413595"><a name="en-us_topic_0116649236_p15224151413595"></a><a name="en-us_topic_0116649236_p15224151413595"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0116649236_p622413146591"><a name="en-us_topic_0116649236_p622413146591"></a><a name="en-us_topic_0116649236_p622413146591"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0116649236_p19314172610176"><a name="en-us_topic_0116649236_p19314172610176"></a><a name="en-us_topic_0116649236_p19314172610176"></a>Specifies the value of the match content.</p>
<p id="en-us_topic_0116649236_p162351209317"><a name="en-us_topic_0116649236_p162351209317"></a><a name="en-us_topic_0116649236_p162351209317"></a>The value contains a maximum of 128 characters.</p>
<a name="en-us_topic_0116649236_ul731432621713"></a><a name="en-us_topic_0116649236_ul731432621713"></a><ul id="en-us_topic_0116649236_ul731432621713"><li>When <strong id="en-us_topic_0116649236_b1980151018456"><a name="en-us_topic_0116649236_b1980151018456"></a><a name="en-us_topic_0116649236_b1980151018456"></a>type</strong> is set to <strong id="en-us_topic_0116649236_b128101044518"><a name="en-us_topic_0116649236_b128101044518"></a><a name="en-us_topic_0116649236_b128101044518"></a>HOST_NAME</strong>, the value is a string of a maximum of 100 characters, contains only letters, digits, hyphens (-), and periods (.), and must start with a letter or digit.</li><li>When <strong id="en-us_topic_0116649236_b6358111534519"><a name="en-us_topic_0116649236_b6358111534519"></a><a name="en-us_topic_0116649236_b6358111534519"></a>type</strong> is set to <strong id="en-us_topic_0116649236_b1835881514459"><a name="en-us_topic_0116649236_b1835881514459"></a><a name="en-us_topic_0116649236_b1835881514459"></a>PATH</strong>, the value is a string of a maximum of 128 characters. When the value of <strong id="en-us_topic_0116649236_b17222517692"><a name="en-us_topic_0116649236_b17222517692"></a><a name="en-us_topic_0116649236_b17222517692"></a>compare_type</strong> is set to <strong id="en-us_topic_0116649236_b522313171592"><a name="en-us_topic_0116649236_b522313171592"></a><a name="en-us_topic_0116649236_b522313171592"></a>STARTS_WITH</strong> or <strong id="en-us_topic_0116649236_b102253171193"><a name="en-us_topic_0116649236_b102253171193"></a><a name="en-us_topic_0116649236_b102253171193"></a>EQUAL_TO</strong>, the string must start with a slash (/) and can contain only letters, digits, and special characters _~';@^-%#&amp;$.*+?,=!:| \/()[]{}</li></ul>
</td>
</tr>
<tr id="en-us_topic_0116649236_row2224191419593"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0116649236_p2022412148597"><a name="en-us_topic_0116649236_p2022412148597"></a><a name="en-us_topic_0116649236_p2022412148597"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0116649236_p622431415599"><a name="en-us_topic_0116649236_p622431415599"></a><a name="en-us_topic_0116649236_p622431415599"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0116649236_p14704205693714"><a name="en-us_topic_0116649236_p14704205693714"></a><a name="en-us_topic_0116649236_p14704205693714"></a>Specifies the provisioning status of the forwarding rule. The value can be <strong id="en-us_topic_0116649236_b931816301281"><a name="en-us_topic_0116649236_b931816301281"></a><a name="en-us_topic_0116649236_b931816301281"></a>ACTIVE</strong>, <strong id="en-us_topic_0116649236_b331911301289"><a name="en-us_topic_0116649236_b331911301289"></a><a name="en-us_topic_0116649236_b331911301289"></a>PENDING_CREATE</strong>, or <strong id="en-us_topic_0116649236_b2320630687"><a name="en-us_topic_0116649236_b2320630687"></a><a name="en-us_topic_0116649236_b2320630687"></a>ERROR</strong>.</p>
<p id="en-us_topic_0116649236_p178421832011"><a name="en-us_topic_0116649236_p178421832011"></a><a name="en-us_topic_0116649236_p178421832011"></a>The default value is <strong id="en-us_topic_0116649236_b134024270811"><a name="en-us_topic_0116649236_b134024270811"></a><a name="en-us_topic_0116649236_b134024270811"></a>ACTIVE</strong>.</p>
<p id="en-us_topic_0116649236_p210952312206"><a name="en-us_topic_0116649236_p210952312206"></a><a name="en-us_topic_0116649236_p210952312206"></a>This parameter is reserved.</p>
<p id="en-us_topic_0116649236_p81819140317"><a name="en-us_topic_0116649236_p81819140317"></a><a name="en-us_topic_0116649236_p81819140317"></a>The value contains a maximum of 16 characters.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section897413116011"></a>

-   Example request: Querying details of a forwarding rule

    ```
    GET https://{Endpoint}/v2.0/lbaas/l7policies/5ae0e1e7-5f0f-47a1-b39f-5d4c428a1586/rules/67d8a8fa-b0dd-4bd4-a85b-671db19b2ef3
    ```

-   Example response

    ```
    {
        "rule": {
            "compare_type": "EQUAL_TO",
            "provisioning_status": "ACTIVE", 
            "admin_state_up": true, 
            "tenant_id": "a31d2bdcf7604c0faaddb058e1e08819", 
      
            "invert": false, 
            "value": "/index.html", 
            "key": null, 
            "type": "PATH", 
            "id": "67d8a8fa-b0dd-4bd4-a85b-671db19b2ef3"
        }
    }
    ```


## Status Code<a name="section9234125402119"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

