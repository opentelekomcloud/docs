# Updating a Forwarding Rule<a name="EN-US_TOPIC_0116649237"></a>

## Function<a name="en-us_topic_0082661928_section605674515130"></a>

This API is used to update a forwarding rule. You can change the mode that how traffic is distributed by updating the forwarding rule.

## URI<a name="section5329110515130"></a>

PUT /v2.0/lbaas/l7policies/\{l7policy\_id\}/rules/\{l7rule\_id\}

**Table  1**  Parameter description

<a name="table0551852175911"></a>
<table><thead align="left"><tr id="row1158845275910"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p18588175220590"><a name="p18588175220590"></a><a name="p18588175220590"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="p1489717461210"><a name="p1489717461210"></a><a name="p1489717461210"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p4588452185917"><a name="p4588452185917"></a><a name="p4588452185917"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.5.1.4"><p id="p958955225911"><a name="p958955225911"></a><a name="p958955225911"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4589105211591"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p1958916525596"><a name="p1958916525596"></a><a name="p1958916525596"></a>l7policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p135891452105910"><a name="p135891452105910"></a><a name="p135891452105910"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1130920370128"><a name="p1130920370128"></a><a name="p1130920370128"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p7589185215914"><a name="p7589185215914"></a><a name="p7589185215914"></a>Specifies the forwarding policy ID.</p>
</td>
</tr>
<tr id="row2058919521598"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p155897527599"><a name="p155897527599"></a><a name="p155897527599"></a>l7rule_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p1131612621212"><a name="p1131612621212"></a><a name="p1131612621212"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p0658139101219"><a name="p0658139101219"></a><a name="p0658139101219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p18589175205918"><a name="p18589175205918"></a><a name="p18589175205918"></a>Specifies the forwarding rule ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section147898232323"></a>

**Table  2**  Request parameters

<a name="table19789132373218"></a>
<table><thead align="left"><tr id="row1478910234323"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p478962313325"><a name="p478962313325"></a><a name="p478962313325"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p12780184118120"><a name="p12780184118120"></a><a name="p12780184118120"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p137896233326"><a name="p137896233326"></a><a name="p137896233326"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.5.1.4"><p id="p1273911018135"><a name="p1273911018135"></a><a name="p1273911018135"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2078919230322"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p6789723153212"><a name="p6789723153212"></a><a name="p6789723153212"></a>rule</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p20789423183216"><a name="p20789423183216"></a><a name="p20789423183216"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p127601314819"><a name="p127601314819"></a><a name="p127601314819"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p1378918232324"><a name="p1378918232324"></a><a name="p1378918232324"></a>Specifies the forwarding rule. For details, see <a href="#table01635270010">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **rule**  parameter description

<a name="table01635270010"></a>
<table><thead align="left"><tr id="row1925572711010"><th class="cellrowborder" valign="top" width="21.372137213721373%" id="mcps1.2.5.1.1"><p id="p192555271308"><a name="p192555271308"></a><a name="p192555271308"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.79127912791279%" id="mcps1.2.5.1.2"><p id="p72551927902"><a name="p72551927902"></a><a name="p72551927902"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.861286128612862%" id="mcps1.2.5.1.3"><p id="p3255192718016"><a name="p3255192718016"></a><a name="p3255192718016"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.97529752975297%" id="mcps1.2.5.1.4"><p id="p1378144620139"><a name="p1378144620139"></a><a name="p1378144620139"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1025510278015"><td class="cellrowborder" valign="top" width="21.372137213721373%" headers="mcps1.2.5.1.1 "><p id="p725719271906"><a name="p725719271906"></a><a name="p725719271906"></a>compare_type</p>
</td>
<td class="cellrowborder" valign="top" width="12.79127912791279%" headers="mcps1.2.5.1.2 "><p id="p12571727303"><a name="p12571727303"></a><a name="p12571727303"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.861286128612862%" headers="mcps1.2.5.1.3 "><p id="p225715276012"><a name="p225715276012"></a><a name="p225715276012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.97529752975297%" headers="mcps1.2.5.1.4 "><p id="p42720683610"><a name="p42720683610"></a><a name="p42720683610"></a>Specifies the match mode. The options are as follows:</p>
<p id="p10794420115116"><a name="p10794420115116"></a><a name="p10794420115116"></a>When <strong id="b296325975415"><a name="b296325975415"></a><a name="b296325975415"></a>type</strong> is set to <strong id="b59659597546"><a name="b59659597546"></a><a name="b59659597546"></a>HOST_NAME</strong>, the value of this parameter can only be the following:</p>
<a name="ul15305619145114"></a><a name="ul15305619145114"></a><ul id="ul15305619145114"><li><strong id="b513111195518"><a name="b513111195518"></a><a name="b513111195518"></a>EQUAL_TO</strong>: indicates exact match.</li></ul>
<p id="p13663103020517"><a name="p13663103020517"></a><a name="p13663103020517"></a>When <strong id="b57012417556"><a name="b57012417556"></a><a name="b57012417556"></a>type</strong> is set to <strong id="b0729413556"><a name="b0729413556"></a><a name="b0729413556"></a>PATH</strong>, the value of this parameter can be one of the following:</p>
<a name="ul17531436125112"></a><a name="ul17531436125112"></a><ul id="ul17531436125112"><li><strong id="b669016510559"><a name="b669016510559"></a><a name="b669016510559"></a>REGEX</strong>: indicates regular expression match.</li><li><strong id="b21799716550"><a name="b21799716550"></a><a name="b21799716550"></a>STARTS_WITH</strong>: indicates prefix match.</li><li><strong id="b71511289551"><a name="b71511289551"></a><a name="b71511289551"></a>EQUAL_TO</strong>: indicates exact match.</li></ul>
</td>
</tr>
<tr id="row82572272001"><td class="cellrowborder" valign="top" width="21.372137213721373%" headers="mcps1.2.5.1.1 "><p id="p725714271508"><a name="p725714271508"></a><a name="p725714271508"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="12.79127912791279%" headers="mcps1.2.5.1.2 "><p id="p725702710018"><a name="p725702710018"></a><a name="p725702710018"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.861286128612862%" headers="mcps1.2.5.1.3 "><p id="p16257327502"><a name="p16257327502"></a><a name="p16257327502"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="52.97529752975297%" headers="mcps1.2.5.1.4 "><p id="p189741017613"><a name="p189741017613"></a><a name="p189741017613"></a>Specifies the administrative status of the forwarding rule.</p>
<p id="p189052592020"><a name="p189052592020"></a><a name="p189052592020"></a>The value can be <strong id="b6381181112557"><a name="b6381181112557"></a><a name="b6381181112557"></a>true</strong> or <strong id="b123821311145516"><a name="b123821311145516"></a><a name="b123821311145516"></a>false</strong>.</p>
<p id="p1610904293213"><a name="p1610904293213"></a><a name="p1610904293213"></a>This parameter is reserved. The default value is <strong id="b495435074619"><a name="b495435074619"></a><a name="b495435074619"></a>true</strong>.</p>
</td>
</tr>
<tr id="row72181712141716"><td class="cellrowborder" valign="top" width="21.372137213721373%" headers="mcps1.2.5.1.1 "><p id="p1087782119244"><a name="p1087782119244"></a><a name="p1087782119244"></a>invert</p>
</td>
<td class="cellrowborder" valign="top" width="12.79127912791279%" headers="mcps1.2.5.1.2 "><p id="p977412062416"><a name="p977412062416"></a><a name="p977412062416"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.861286128612862%" headers="mcps1.2.5.1.3 "><p id="p988032152413"><a name="p988032152413"></a><a name="p988032152413"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="52.97529752975297%" headers="mcps1.2.5.1.4 "><p id="p1238515351377"><a name="p1238515351377"></a><a name="p1238515351377"></a>Specifies whether reverse match is supported.</p>
<p id="p1938543553715"><a name="p1938543553715"></a><a name="p1938543553715"></a>The value can be <strong id="b17762101495510"><a name="b17762101495510"></a><a name="b17762101495510"></a>true</strong> or <strong id="b16763131418555"><a name="b16763131418555"></a><a name="b16763131418555"></a>false</strong>. The default value is <strong id="b82728162558"><a name="b82728162558"></a><a name="b82728162558"></a>false</strong>.</p>
<p id="p183851435173713"><a name="p183851435173713"></a><a name="p183851435173713"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="row98306710179"><td class="cellrowborder" valign="top" width="21.372137213721373%" headers="mcps1.2.5.1.1 "><p id="p163041927161418"><a name="p163041927161418"></a><a name="p163041927161418"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="12.79127912791279%" headers="mcps1.2.5.1.2 "><p id="p1518714313147"><a name="p1518714313147"></a><a name="p1518714313147"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.861286128612862%" headers="mcps1.2.5.1.3 "><p id="p193051427151417"><a name="p193051427151417"></a><a name="p193051427151417"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.97529752975297%" headers="mcps1.2.5.1.4 "><p id="p82048119202"><a name="p82048119202"></a><a name="p82048119202"></a>Specifies the key of the match content. The default value is <strong id="b393222018554"><a name="b393222018554"></a><a name="b393222018554"></a>null</strong>.</p>
<p id="p1747128122016"><a name="p1747128122016"></a><a name="p1747128122016"></a>This parameter is reserved.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row1257162717015"><td class="cellrowborder" valign="top" width="21.372137213721373%" headers="mcps1.2.5.1.1 "><p id="p1025717271504"><a name="p1025717271504"></a><a name="p1025717271504"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="12.79127912791279%" headers="mcps1.2.5.1.2 "><p id="p3257202715019"><a name="p3257202715019"></a><a name="p3257202715019"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.861286128612862%" headers="mcps1.2.5.1.3 "><p id="p13257127403"><a name="p13257127403"></a><a name="p13257127403"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.97529752975297%" headers="mcps1.2.5.1.4 "><p id="p16872195212010"><a name="p16872195212010"></a><a name="p16872195212010"></a>Specifies the value of the match content. The value cannot contain spaces.</p>
<p id="p1577253223314"><a name="p1577253223314"></a><a name="p1577253223314"></a>The value contains a maximum of 128 characters.</p>
<a name="ul75251828131120"></a><a name="ul75251828131120"></a><ul id="ul75251828131120"><li>When <strong id="b7605132745519"><a name="b7605132745519"></a><a name="b7605132745519"></a>type</strong> is set to <strong id="b15606172785516"><a name="b15606172785516"></a><a name="b15606172785516"></a>HOST_NAME</strong>, the value is a string of a maximum of 100 characters, contains only letters, digits, hyphens (-), and periods (.), and must start with a letter or digit.</li><li>When <strong id="b1480252925510"><a name="b1480252925510"></a><a name="b1480252925510"></a>type</strong> is set to <strong id="b880312291557"><a name="b880312291557"></a><a name="b880312291557"></a>PATH</strong>, the value is a string of a maximum of 128 characters. When the value of <strong id="b1468323118554"><a name="b1468323118554"></a><a name="b1468323118554"></a>compare_type</strong> is set to <strong id="b13684431185513"><a name="b13684431185513"></a><a name="b13684431185513"></a>STARTS_WITH</strong> or <strong id="b10684153112559"><a name="b10684153112559"></a><a name="b10684153112559"></a>EQUAL_TO</strong>, the string must start with a slash (/) and can contain only letters, digits, and special characters _~';@^-%#&amp;$.*+?,=!:| \/()[]{}</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0082661928_section27729415130"></a>

**Table  4**  Response parameters

<a name="en-us_topic_0082661928_table2246083515130"></a>
<table><thead align="left"><tr id="en-us_topic_0082661928_row63807815130"><th class="cellrowborder" valign="top" width="23.34%" id="mcps1.2.4.1.1"><p id="en-us_topic_0082661928_p5168432015130"><a name="en-us_topic_0082661928_p5168432015130"></a><a name="en-us_topic_0082661928_p5168432015130"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.060000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0082661928_p2568040715130"><a name="en-us_topic_0082661928_p2568040715130"></a><a name="en-us_topic_0082661928_p2568040715130"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.599999999999994%" id="mcps1.2.4.1.3"><p id="en-us_topic_0082661928_p4590723515130"><a name="en-us_topic_0082661928_p4590723515130"></a><a name="en-us_topic_0082661928_p4590723515130"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0082661928_row2749856815130"><td class="cellrowborder" valign="top" width="23.34%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0082661928_p1279152115130"><a name="en-us_topic_0082661928_p1279152115130"></a><a name="en-us_topic_0082661928_p1279152115130"></a>rule</p>
</td>
<td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0082661928_p2948027915130"><a name="en-us_topic_0082661928_p2948027915130"></a><a name="en-us_topic_0082661928_p2948027915130"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="58.599999999999994%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0082661928_p1236530315130"><a name="en-us_topic_0082661928_p1236530315130"></a><a name="en-us_topic_0082661928_p1236530315130"></a>Specifies the forwarding rule. For details, see <a href="#table08840481403">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **rule**  parameter description

<a name="table08840481403"></a>
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

## Example<a name="section132814449312"></a>

-   Example request: Updating a forwarding rule

    ```
    PUT https://{Endpoint}/v2.0/lbaas/l7policies/5ae0e1e7-5f0f-47a1-b39f-5d4c428a1586/rules/c6f457b8-bf6f-45d7-be5c-a3226945b7b1
    
    {
        "rule": {
            "compare_type": "STARTS_WITH", 
            "value": "/ccc.html"
        }
    }
    ```

-   Example response

    ```
    {
        "rule": {
            "compare_type": "STARTS_WITH", 
            "provisioning_status": "ACTIVE",
            "admin_state_up": true, 
            "tenant_id": "a31d2bdcf7604c0faaddb058e1e08819",
     
            "invert": false, 
            "value": "/ccc.html", 
            "key": null, 
            "type": "PATH", 
            "id": "c6f457b8-bf6f-45d7-be5c-a3226945b7b1"
        }
    }
    ```


## Status Code<a name="section7214357142819"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

