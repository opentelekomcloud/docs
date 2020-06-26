# Querying Security Groups<a name="vpc_sg02_0001"></a>

## Function<a name="section1170323616037"></a>

This API is used to query all security groups accessible to the tenant submitting the request. 

## URI<a name="section2797834416037"></a>

GET /v2.0/security-groups

Example of querying security groups by page

```
GET https://{Endpoint}/v2.0/security-groups?limit=2&marker=0431c9c5-1660-42e0-8a00-134bec7f03e2&page_reverse=False
```

[Table 1](#table1687161718223)  describes the parameters.

**Table  1**  Parameter description

<a name="table1687161718223"></a>
<table><thead align="left"><tr id="row396316178224"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.1"><p id="p14963617122211"><a name="p14963617122211"></a><a name="p14963617122211"></a><strong id="b795715382317"><a name="b795715382317"></a><a name="b795715382317"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.2"><p id="p19964161752210"><a name="p19964161752210"></a><a name="p19964161752210"></a><strong id="b146961839153118"><a name="b146961839153118"></a><a name="b146961839153118"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.54175417541754%" id="mcps1.2.5.1.3"><p id="p1396481772212"><a name="p1396481772212"></a><a name="p1396481772212"></a><strong id="b372134017317"><a name="b372134017317"></a><a name="b372134017317"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46.09460946094609%" id="mcps1.2.5.1.4"><p id="p796421711226"><a name="p796421711226"></a><a name="p796421711226"></a><strong id="b105381041173112"><a name="b105381041173112"></a><a name="b105381041173112"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row17964117122212"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1396481719225"><a name="p1396481719225"></a><a name="p1396481719225"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p17964717142210"><a name="p17964717142210"></a><a name="p17964717142210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.54175417541754%" headers="mcps1.2.5.1.3 "><p id="p8964417192215"><a name="p8964417192215"></a><a name="p8964417192215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.09460946094609%" headers="mcps1.2.5.1.4 "><p id="p169644177228"><a name="p169644177228"></a><a name="p169644177228"></a>Specifies that the ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row69646172222"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p89647174229"><a name="p89647174229"></a><a name="p89647174229"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p6964111702216"><a name="p6964111702216"></a><a name="p6964111702216"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.54175417541754%" headers="mcps1.2.5.1.3 "><p id="p296421782217"><a name="p296421782217"></a><a name="p296421782217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.09460946094609%" headers="mcps1.2.5.1.4 "><p id="p11964717192216"><a name="p11964717192216"></a><a name="p11964717192216"></a>Specifies that the name is used as the filtering condition.</p>
</td>
</tr>
<tr id="row1996419172225"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p2096413173223"><a name="p2096413173223"></a><a name="p2096413173223"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p596421732212"><a name="p596421732212"></a><a name="p596421732212"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.54175417541754%" headers="mcps1.2.5.1.3 "><p id="p10964131710228"><a name="p10964131710228"></a><a name="p10964131710228"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.09460946094609%" headers="mcps1.2.5.1.4 "><p id="p2096421719225"><a name="p2096421719225"></a><a name="p2096421719225"></a>Specifies that the description is used as the filtering condition.</p>
</td>
</tr>
<tr id="row396451752217"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p179648172225"><a name="p179648172225"></a><a name="p179648172225"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p196411752220"><a name="p196411752220"></a><a name="p196411752220"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.54175417541754%" headers="mcps1.2.5.1.3 "><p id="p11964181772212"><a name="p11964181772212"></a><a name="p11964181772212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.09460946094609%" headers="mcps1.2.5.1.4 "><p id="p5964217162211"><a name="p5964217162211"></a><a name="p5964217162211"></a>Specifies that the project ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row39646172224"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p109641217162215"><a name="p109641217162215"></a><a name="p109641217162215"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p199641717112219"><a name="p199641717112219"></a><a name="p199641717112219"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.54175417541754%" headers="mcps1.2.5.1.3 "><p id="p796412174223"><a name="p796412174223"></a><a name="p796412174223"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.09460946094609%" headers="mcps1.2.5.1.4 "><p id="p496412171223"><a name="p496412171223"></a><a name="p496412171223"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row10964201702215"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p10964111722211"><a name="p10964111722211"></a><a name="p10964111722211"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p896421742213"><a name="p896421742213"></a><a name="p896421742213"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.54175417541754%" headers="mcps1.2.5.1.3 "><p id="p18965161732218"><a name="p18965161732218"></a><a name="p18965161732218"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="46.09460946094609%" headers="mcps1.2.5.1.4 "><p id="p96971524162214"><a name="p96971524162214"></a><a name="p96971524162214"></a>Specifies the number of records on each page.</p>
<p id="p1496571772219"><a name="p1496571772219"></a><a name="p1496571772219"></a>The value ranges from 0 to intmax.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section3834086716037"></a>

None

## Response Message<a name="section6006230416037"></a>

**Table  2**  Response parameter

<a name="table1547016516037"></a>
<table><thead align="left"><tr id="row2546099716037"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.4.1.1"><p id="p3614026216037"><a name="p3614026216037"></a><a name="p3614026216037"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.61%" id="mcps1.2.4.1.2"><p id="p3446060616037"><a name="p3446060616037"></a><a name="p3446060616037"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p3726817816037"><a name="p3726817816037"></a><a name="p3726817816037"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row841863916037"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p5631571516037"><a name="p5631571516037"></a><a name="p5631571516037"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p86066502616"><a name="p86066502616"></a><a name="p86066502616"></a>Array of <a href="#table513726041607">Security Group</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p6079210416037"><a name="p6079210416037"></a><a name="p6079210416037"></a>Specifies the security group list. For details, see <a href="#table513726041607">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **Security Group**  objects

<a name="table513726041607"></a>
<table><thead align="left"><tr id="row72893461607"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p647825491607"><a name="p647825491607"></a><a name="p647825491607"></a><strong id="b74664312719"><a name="b74664312719"></a><a name="b74664312719"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.2"><p id="p245230881607"><a name="p245230881607"></a><a name="p245230881607"></a><strong id="b7275337576"><a name="b7275337576"></a><a name="b7275337576"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p4542071607"><a name="p4542071607"></a><a name="p4542071607"></a><strong id="b10119113816711"><a name="b10119113816711"></a><a name="b10119113816711"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row284118681607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p6322881607"><a name="p6322881607"></a><a name="p6322881607"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p206339641607"><a name="p206339641607"></a><a name="p206339641607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p538811831607"><a name="p538811831607"></a><a name="p538811831607"></a>Specifies the security group ID.</p>
<p id="p7631141813810"><a name="p7631141813810"></a><a name="p7631141813810"></a>This parameter is not mandatory when you query security groups.</p>
</td>
</tr>
<tr id="row487759591607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p499705331607"><a name="p499705331607"></a><a name="p499705331607"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p26621541607"><a name="p26621541607"></a><a name="p26621541607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row356666781607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p270644691607"><a name="p270644691607"></a><a name="p270644691607"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p426717071607"><a name="p426717071607"></a><a name="p426717071607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p29740751607"><a name="p29740751607"></a><a name="p29740751607"></a>Specifies the security group name.</p>
</td>
</tr>
<tr id="row5261561607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p76095411607"><a name="p76095411607"></a><a name="p76095411607"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p597100051607"><a name="p597100051607"></a><a name="p597100051607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p40269061607"><a name="p40269061607"></a><a name="p40269061607"></a>Provides supplementary information about the security group.</p>
</td>
</tr>
<tr id="row141788771607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p574773991607"><a name="p574773991607"></a><a name="p574773991607"></a>security_group_rules</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p263715271607"><a name="p263715271607"></a><a name="p263715271607"></a>Array of <a href="#table655457801607">Security Group Rule</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p577222241607"><a name="p577222241607"></a><a name="p577222241607"></a>Specifies the security group rule list. For details, see <a href="#table655457801607">Table 4</a>.</p>
</td>
</tr>
<tr id="row19560720141817"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p15700614790"><a name="p15700614790"></a><a name="p15700614790"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p8746620183014"><a name="p8746620183014"></a><a name="p8746620183014"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row5768162761818"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Specifies the time (UTC) when the security group is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i175318119108"><a name="i175318119108"></a><a name="i175318119108"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row4242824111816"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the security group is updated.</p>
<p id="p15297192516128"><a name="p15297192516128"></a><a name="p15297192516128"></a>Format: <em id="i122011254101"><a name="i122011254101"></a><a name="i122011254101"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

**Table  4** **Security Group Rule**  objects

<a name="table655457801607"></a>
<table><thead align="left"><tr id="vpc_sg02_0006_row54478641607"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="vpc_sg02_0006_p389969021607"><a name="vpc_sg02_0006_p389969021607"></a><a name="vpc_sg02_0006_p389969021607"></a><strong id="vpc_sg02_0006_b195868418291"><a name="vpc_sg02_0006_b195868418291"></a><a name="vpc_sg02_0006_b195868418291"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.2"><p id="vpc_sg02_0006_p36789391607"><a name="vpc_sg02_0006_p36789391607"></a><a name="vpc_sg02_0006_p36789391607"></a><strong id="vpc_sg02_0006_b582815515290"><a name="vpc_sg02_0006_b582815515290"></a><a name="vpc_sg02_0006_b582815515290"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="vpc_sg02_0006_p433861031607"><a name="vpc_sg02_0006_p433861031607"></a><a name="vpc_sg02_0006_p433861031607"></a><strong id="vpc_sg02_0006_b198338642916"><a name="vpc_sg02_0006_b198338642916"></a><a name="vpc_sg02_0006_b198338642916"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="vpc_sg02_0006_row134774871607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p269083981607"><a name="vpc_sg02_0006_p269083981607"></a><a name="vpc_sg02_0006_p269083981607"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p630670281607"><a name="vpc_sg02_0006_p630670281607"></a><a name="vpc_sg02_0006_p630670281607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p334792201607"><a name="vpc_sg02_0006_p334792201607"></a><a name="vpc_sg02_0006_p334792201607"></a>Specifies the security group rule ID.</p>
<p id="vpc_sg02_0006_p529374054010"><a name="vpc_sg02_0006_p529374054010"></a><a name="vpc_sg02_0006_p529374054010"></a>This parameter is not mandatory when you query security group rules.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row250554771607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p254411021607"><a name="vpc_sg02_0006_p254411021607"></a><a name="vpc_sg02_0006_p254411021607"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p505368621607"><a name="vpc_sg02_0006_p505368621607"></a><a name="vpc_sg02_0006_p505368621607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p480145951607"><a name="vpc_sg02_0006_p480145951607"></a><a name="vpc_sg02_0006_p480145951607"></a>Provides supplementary information about the security group rule.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row569401671607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p115724181607"><a name="vpc_sg02_0006_p115724181607"></a><a name="vpc_sg02_0006_p115724181607"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p615991711607"><a name="vpc_sg02_0006_p615991711607"></a><a name="vpc_sg02_0006_p615991711607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p587796621607"><a name="vpc_sg02_0006_p587796621607"></a><a name="vpc_sg02_0006_p587796621607"></a>Specifies the ID of the belonged security group.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row654332091607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p113008931607"><a name="vpc_sg02_0006_p113008931607"></a><a name="vpc_sg02_0006_p113008931607"></a>remote_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p170542961607"><a name="vpc_sg02_0006_p170542961607"></a><a name="vpc_sg02_0006_p170542961607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p141218971607"><a name="vpc_sg02_0006_p141218971607"></a><a name="vpc_sg02_0006_p141218971607"></a>Specifies the peer ID of the belonged security group.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row9932071607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p657989401607"><a name="vpc_sg02_0006_p657989401607"></a><a name="vpc_sg02_0006_p657989401607"></a>direction</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p507988391607"><a name="vpc_sg02_0006_p507988391607"></a><a name="vpc_sg02_0006_p507988391607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p570991491607"><a name="vpc_sg02_0006_p570991491607"></a><a name="vpc_sg02_0006_p570991491607"></a>Specifies the direction of the traffic for which the security group rule takes effect.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row97529031607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p478834691607"><a name="vpc_sg02_0006_p478834691607"></a><a name="vpc_sg02_0006_p478834691607"></a>remote_ip_prefix</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p622759951607"><a name="vpc_sg02_0006_p622759951607"></a><a name="vpc_sg02_0006_p622759951607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p146708701607"><a name="vpc_sg02_0006_p146708701607"></a><a name="vpc_sg02_0006_p146708701607"></a>Specifies the peer IP address segment.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row315033981607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p163656291607"><a name="vpc_sg02_0006_p163656291607"></a><a name="vpc_sg02_0006_p163656291607"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p628340441607"><a name="vpc_sg02_0006_p628340441607"></a><a name="vpc_sg02_0006_p628340441607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p99902671607"><a name="vpc_sg02_0006_p99902671607"></a><a name="vpc_sg02_0006_p99902671607"></a>Specifies the protocol type or the IP protocol number.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row551583771607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p97886331607"><a name="vpc_sg02_0006_p97886331607"></a><a name="vpc_sg02_0006_p97886331607"></a>port_range_max</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p343603851607"><a name="vpc_sg02_0006_p343603851607"></a><a name="vpc_sg02_0006_p343603851607"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p188144701607"><a name="vpc_sg02_0006_p188144701607"></a><a name="vpc_sg02_0006_p188144701607"></a>Specifies the maximum port number. When ICMP is used, the value is the ICMP code.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row456604071607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p630384091607"><a name="vpc_sg02_0006_p630384091607"></a><a name="vpc_sg02_0006_p630384091607"></a>port_range_min</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p337362901607"><a name="vpc_sg02_0006_p337362901607"></a><a name="vpc_sg02_0006_p337362901607"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p258562691607"><a name="vpc_sg02_0006_p258562691607"></a><a name="vpc_sg02_0006_p258562691607"></a>Specifies the minimum port number. If the ICMP protocol is used, this parameter indicates the ICMP type.</p>
<p id="vpc_sg02_0006_p5690808615417"><a name="vpc_sg02_0006_p5690808615417"></a><a name="vpc_sg02_0006_p5690808615417"></a>When the TCP or UDP protocol is used, both <strong id="vpc_sg02_0006_b84235270621055"><a name="vpc_sg02_0006_b84235270621055"></a><a name="vpc_sg02_0006_b84235270621055"></a>port_range_max</strong> and <strong id="vpc_sg02_0006_b8423527062112"><a name="vpc_sg02_0006_b8423527062112"></a><a name="vpc_sg02_0006_b8423527062112"></a>port_range_min</strong> must be specified, and the <strong id="vpc_sg02_0006_b43870256421149"><a name="vpc_sg02_0006_b43870256421149"></a><a name="vpc_sg02_0006_b43870256421149"></a>port_range_max</strong> value must be greater than the <strong id="vpc_sg02_0006_b70589128621159"><a name="vpc_sg02_0006_b70589128621159"></a><a name="vpc_sg02_0006_b70589128621159"></a>port_range_min</strong> value.</p>
<p id="vpc_sg02_0006_p4241072615417"><a name="vpc_sg02_0006_p4241072615417"></a><a name="vpc_sg02_0006_p4241072615417"></a>When the ICMP protocol is used, if you specify the ICMP code (<strong id="vpc_sg02_0006_b84235270621317"><a name="vpc_sg02_0006_b84235270621317"></a><a name="vpc_sg02_0006_b84235270621317"></a>port_range_max</strong>), you must also specify the ICMP type (<strong id="vpc_sg02_0006_b84235270621326"><a name="vpc_sg02_0006_b84235270621326"></a><a name="vpc_sg02_0006_b84235270621326"></a>port_range_min</strong>).</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row360773491607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p364292801607"><a name="vpc_sg02_0006_p364292801607"></a><a name="vpc_sg02_0006_p364292801607"></a>ethertype</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p339523071607"><a name="vpc_sg02_0006_p339523071607"></a><a name="vpc_sg02_0006_p339523071607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p34728681607"><a name="vpc_sg02_0006_p34728681607"></a><a name="vpc_sg02_0006_p34728681607"></a>Specifies the network type.</p>
<p id="vpc_sg02_0006_p568898621607"><a name="vpc_sg02_0006_p568898621607"></a><a name="vpc_sg02_0006_p568898621607"></a>Only IPv4 is supported.</p>
</td>
</tr>
<tr id="vpc_sg02_0006_row532124261607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p593368391607"><a name="vpc_sg02_0006_p593368391607"></a><a name="vpc_sg02_0006_p593368391607"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p130282191607"><a name="vpc_sg02_0006_p130282191607"></a><a name="vpc_sg02_0006_p130282191607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p10487112"><a name="vpc_sg02_0006_p10487112"></a><a name="vpc_sg02_0006_p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="vpc_sg02_0006_row11992111863317"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p169261732143314"><a name="vpc_sg02_0006_p169261732143314"></a><a name="vpc_sg02_0006_p169261732143314"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p69311132153317"><a name="vpc_sg02_0006_p69311132153317"></a><a name="vpc_sg02_0006_p69311132153317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p13646103310"><a name="vpc_sg02_0006_p13646103310"></a><a name="vpc_sg02_0006_p13646103310"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="vpc_sg02_0006_row10903153923318"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p6634195714335"><a name="vpc_sg02_0006_p6634195714335"></a><a name="vpc_sg02_0006_p6634195714335"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p12638157153319"><a name="vpc_sg02_0006_p12638157153319"></a><a name="vpc_sg02_0006_p12638157153319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p1364635713332"><a name="vpc_sg02_0006_p1364635713332"></a><a name="vpc_sg02_0006_p1364635713332"></a>Specifies the time (UTC) when the security group rule is created.</p>
<p id="vpc_sg02_0006_p65980291419"><a name="vpc_sg02_0006_p65980291419"></a><a name="vpc_sg02_0006_p65980291419"></a>Format: <em id="vpc_sg02_0006_i1034411227245"><a name="vpc_sg02_0006_i1034411227245"></a><a name="vpc_sg02_0006_i1034411227245"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="vpc_sg02_0006_row1797311427338"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="vpc_sg02_0006_p1725445103416"><a name="vpc_sg02_0006_p1725445103416"></a><a name="vpc_sg02_0006_p1725445103416"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="vpc_sg02_0006_p192601514345"><a name="vpc_sg02_0006_p192601514345"></a><a name="vpc_sg02_0006_p192601514345"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="vpc_sg02_0006_p1127018513343"><a name="vpc_sg02_0006_p1127018513343"></a><a name="vpc_sg02_0006_p1127018513343"></a>Specifies the time (UTC) when the security group rule is updated.</p>
<p id="vpc_sg02_0006_p19850105451210"><a name="vpc_sg02_0006_p19850105451210"></a><a name="vpc_sg02_0006_p19850105451210"></a>Format: <em id="vpc_sg02_0006_i1647183316242"><a name="vpc_sg02_0006_i1647183316242"></a><a name="vpc_sg02_0006_i1647183316242"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section2440368716037"></a>

Example request

```
GET https://{Endpoint}/v2.0/security-groups?limit=1
```

Example response

```
{
    "security_groups": [
        {
            "id": "0431c9c5-1660-42e0-8a00-134bec7f03e2",
            "name": "sg-ad3f",
            "description": "",
            "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
            "project_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
            "security_group_rules": [
                {
                    "id": "d90e55ba-23bd-4d97-b722-8cb6fb485d69",
                    "direction": "ingress",
                    "protocol": null,
                    "ethertype": "IPv4",
                    "description": null,
                    "remote_group_id": "0431c9c5-1660-42e0-8a00-134bec7f03e2",
                    "remote_ip_prefix": null,
                    "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
                    "port_range_max": null,
                    "port_range_min": null,
                    "security_group_id": "0431c9c5-1660-42e0-8a00-134bec7f03e2"
                    
                },
                {
                    "id": "aecff4d4-9ce9-489c-86a3-803aedec65f7",
                    "direction": "egress",
                    "protocol": null,
                    "ethertype": "IPv4",
                    "description": null,
                    "remote_group_id": null,
                    "remote_ip_prefix": null,
                    "tenant_id": "bbfe8c41dd034a07bebd592bf03b4b0c",
                    "port_range_max": null,
                    "port_range_min": null,
                    "security_group_id": "0431c9c5-1660-42e0-8a00-134bec7f03e2"
                }
            ],
            "created_at": "2018-09-12T08:24:14",
            "updated_at": "2018-09-12T08:24:14"
        }
    ]
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

