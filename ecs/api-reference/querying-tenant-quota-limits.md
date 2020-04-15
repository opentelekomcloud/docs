# Querying Tenant Quota Limits<a name="EN-US_TOPIC_0065817717"></a>

## Function<a name="en-us_topic_0057973197_section23906465"></a>

This API is used to query tenant quota limits.

Tenants are only allowed to query their own quota limits.

## URI<a name="en-us_topic_0057973197_section13831595"></a>

GET /v2/\{project\_id\}/limits?project\_id=\{project\_id\}

GET /v2.1/\{project\_id\}/limits?project\_id=\{project\_id\}

[Table 1](#en-us_topic_0057973197_table258804192629)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973197_table258804192629"></a>
<table><thead align="left"><tr id="en-us_topic_0057973197_row33277594192629"><th class="cellrowborder" valign="top" width="16.46%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.61%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.93%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973197_row56232837192629"><td class="cellrowborder" valign="top" width="16.46%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p58565959192629"><a name="en-us_topic_0057973197_p58565959192629"></a><a name="en-us_topic_0057973197_p58565959192629"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p46222262192629"><a name="en-us_topic_0057973197_p46222262192629"></a><a name="en-us_topic_0057973197_p46222262192629"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.93%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973197_section16903657"></a>

None

## Response<a name="en-us_topic_0057973197_section17915190"></a>

[Table 2](#en-us_topic_0057973197_table62068690)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057973197_table62068690"></a>
<table><thead align="left"><tr id="en-us_topic_0057973197_row56098908"><th class="cellrowborder" valign="top" width="16.54%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973197_p47717737"><a name="en-us_topic_0057973197_p47717737"></a><a name="en-us_topic_0057973197_p47717737"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.35%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973197_p39931478"><a name="en-us_topic_0057973197_p39931478"></a><a name="en-us_topic_0057973197_p39931478"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="69.11%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973197_p64532721"><a name="en-us_topic_0057973197_p64532721"></a><a name="en-us_topic_0057973197_p64532721"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973197_row59767919"><td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p9363310"><a name="en-us_topic_0057973197_p9363310"></a><a name="en-us_topic_0057973197_p9363310"></a>limits</p>
</td>
<td class="cellrowborder" valign="top" width="14.35%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p20230678"><a name="en-us_topic_0057973197_p20230678"></a><a name="en-us_topic_0057973197_p20230678"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="69.11%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p59256190"><a name="en-us_topic_0057973197_p59256190"></a><a name="en-us_topic_0057973197_p59256190"></a>Specifies tenant limits.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **limits**  parameter information

<a name="en-us_topic_0057973197_table35022095"></a>
<table><thead align="left"><tr id="en-us_topic_0057973197_row34160447"><th class="cellrowborder" valign="top" width="16.439999999999998%" id="mcps1.2.4.1.1"><p id="p7699812193214"><a name="p7699812193214"></a><a name="p7699812193214"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.37%" id="mcps1.2.4.1.2"><p id="p1569931220327"><a name="p1569931220327"></a><a name="p1569931220327"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="69.19%" id="mcps1.2.4.1.3"><p id="p19715151203213"><a name="p19715151203213"></a><a name="p19715151203213"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973197_row7791918"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p27165655"><a name="en-us_topic_0057973197_p27165655"></a><a name="en-us_topic_0057973197_p27165655"></a>rate</p>
</td>
<td class="cellrowborder" valign="top" width="14.37%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p52934452"><a name="en-us_topic_0057973197_p52934452"></a><a name="en-us_topic_0057973197_p52934452"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="69.19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p14573100"><a name="en-us_topic_0057973197_p14573100"></a><a name="en-us_topic_0057973197_p14573100"></a>The value is empty.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row64049040"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p20589776"><a name="en-us_topic_0057973197_p20589776"></a><a name="en-us_topic_0057973197_p20589776"></a>absolute</p>
</td>
<td class="cellrowborder" valign="top" width="14.37%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p57159177"><a name="en-us_topic_0057973197_p57159177"></a><a name="en-us_topic_0057973197_p57159177"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="69.19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p17028995"><a name="en-us_topic_0057973197_p17028995"></a><a name="en-us_topic_0057973197_p17028995"></a>Specifies the tenant quota limits.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **absolute**  parameter information

<a name="en-us_topic_0057973197_table37171349"></a>
<table><thead align="left"><tr id="en-us_topic_0057973197_row45622382"><th class="cellrowborder" valign="top" width="20.44%" id="mcps1.2.4.1.1"><p id="p31891619163214"><a name="p31891619163214"></a><a name="p31891619163214"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.2.4.1.2"><p id="p1218921903213"><a name="p1218921903213"></a><a name="p1218921903213"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.44%" id="mcps1.2.4.1.3"><p id="p1920515197321"><a name="p1920515197321"></a><a name="p1920515197321"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973197_row43053675"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p64795628"><a name="en-us_topic_0057973197_p64795628"></a><a name="en-us_topic_0057973197_p64795628"></a>maxServerMeta</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p13954547"><a name="en-us_topic_0057973197_p13954547"></a><a name="en-us_topic_0057973197_p13954547"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p19292588"><a name="en-us_topic_0057973197_p19292588"></a><a name="en-us_topic_0057973197_p19292588"></a>Specifies the limit of ECS metadata quantity.</p>
<p id="en-us_topic_0057973197_p11146411125217"><a name="en-us_topic_0057973197_p11146411125217"></a><a name="en-us_topic_0057973197_p11146411125217"></a>If the value is <strong id="en-us_topic_0057973197_b3861153182516"><a name="en-us_topic_0057973197_b3861153182516"></a><a name="en-us_topic_0057973197_b3861153182516"></a>-1</strong>, there is no quantity limit.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row39415571"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p38544692"><a name="en-us_topic_0057973197_p38544692"></a><a name="en-us_topic_0057973197_p38544692"></a>maxPersonality</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p35112349"><a name="en-us_topic_0057973197_p35112349"></a><a name="en-us_topic_0057973197_p35112349"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p54506602"><a name="en-us_topic_0057973197_p54506602"></a><a name="en-us_topic_0057973197_p54506602"></a>Specifies the quantity limit of injected files.</p>
<p id="en-us_topic_0057973197_p19852033530"><a name="en-us_topic_0057973197_p19852033530"></a><a name="en-us_topic_0057973197_p19852033530"></a>If the value is <strong id="en-us_topic_0057973197_b82331287221"><a name="en-us_topic_0057973197_b82331287221"></a><a name="en-us_topic_0057973197_b82331287221"></a>-1</strong>, there is no quantity limit.</p>
<p id="p11469124194518"><a name="p11469124194518"></a><a name="p11469124194518"></a>This field is not supported in microversions later than 2.56.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row20797372"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p6865542"><a name="en-us_topic_0057973197_p6865542"></a><a name="en-us_topic_0057973197_p6865542"></a>totalServerGroupsUsed</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p19238012"><a name="en-us_topic_0057973197_p19238012"></a><a name="en-us_topic_0057973197_p19238012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p55938575"><a name="en-us_topic_0057973197_p55938575"></a><a name="en-us_topic_0057973197_p55938575"></a>Specifies the number of used ECS groups.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row33685133"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p44141275"><a name="en-us_topic_0057973197_p44141275"></a><a name="en-us_topic_0057973197_p44141275"></a>maxImageMeta</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p18673497"><a name="en-us_topic_0057973197_p18673497"></a><a name="en-us_topic_0057973197_p18673497"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p43137542"><a name="en-us_topic_0057973197_p43137542"></a><a name="en-us_topic_0057973197_p43137542"></a>Specifies the limit of the image metadata quantity.</p>
<p id="en-us_topic_0057973197_p12446181925314"><a name="en-us_topic_0057973197_p12446181925314"></a><a name="en-us_topic_0057973197_p12446181925314"></a>If the value is <strong id="en-us_topic_0057973197_b182335192112"><a name="en-us_topic_0057973197_b182335192112"></a><a name="en-us_topic_0057973197_b182335192112"></a>-1</strong>, there is no quantity limit.</p>
<p id="p18876174441"><a name="p18876174441"></a><a name="p18876174441"></a>This field is not supported in microversions later than 2.38.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row52693561"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p40320052"><a name="en-us_topic_0057973197_p40320052"></a><a name="en-us_topic_0057973197_p40320052"></a>maxPersonalitySize</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p44698755"><a name="en-us_topic_0057973197_p44698755"></a><a name="en-us_topic_0057973197_p44698755"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p2798143"><a name="en-us_topic_0057973197_p2798143"></a><a name="en-us_topic_0057973197_p2798143"></a>Specifies the size limit of injected files.</p>
<p id="en-us_topic_0057973197_p11479523115314"><a name="en-us_topic_0057973197_p11479523115314"></a><a name="en-us_topic_0057973197_p11479523115314"></a>If the value is <strong id="en-us_topic_0057973197_b6324195617713"><a name="en-us_topic_0057973197_b6324195617713"></a><a name="en-us_topic_0057973197_b6324195617713"></a>-1</strong>, there is no size limit.</p>
<p id="p967182117443"><a name="p967182117443"></a><a name="p967182117443"></a>This field is not supported in microversions later than 2.56.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row25183288"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p26580442"><a name="en-us_topic_0057973197_p26580442"></a><a name="en-us_topic_0057973197_p26580442"></a>maxTotalRAMSize</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p5532180"><a name="en-us_topic_0057973197_p5532180"></a><a name="en-us_topic_0057973197_p5532180"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p57851251"><a name="en-us_topic_0057973197_p57851251"></a><a name="en-us_topic_0057973197_p57851251"></a>Specifies the total memory size limit.</p>
<p id="en-us_topic_0057973197_p8694162635316"><a name="en-us_topic_0057973197_p8694162635316"></a><a name="en-us_topic_0057973197_p8694162635316"></a>If the value is <strong id="en-us_topic_0057973197_b157041347571"><a name="en-us_topic_0057973197_b157041347571"></a><a name="en-us_topic_0057973197_b157041347571"></a>-1</strong>, there is no size limit.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row50899211"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p29195422"><a name="en-us_topic_0057973197_p29195422"></a><a name="en-us_topic_0057973197_p29195422"></a>maxTotalKeypairs</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p16018990"><a name="en-us_topic_0057973197_p16018990"></a><a name="en-us_topic_0057973197_p16018990"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p8114019"><a name="en-us_topic_0057973197_p8114019"></a><a name="en-us_topic_0057973197_p8114019"></a>Specifies the limit of key pair quantity.</p>
<p id="en-us_topic_0057973197_p1550814298531"><a name="en-us_topic_0057973197_p1550814298531"></a><a name="en-us_topic_0057973197_p1550814298531"></a>If the value is <strong id="en-us_topic_0057973197_b1466715109266"><a name="en-us_topic_0057973197_b1466715109266"></a><a name="en-us_topic_0057973197_b1466715109266"></a>-1</strong>, there is no quantity limit.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row5917307"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p9539865"><a name="en-us_topic_0057973197_p9539865"></a><a name="en-us_topic_0057973197_p9539865"></a>maxSecurityGroupRules</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p34531640"><a name="en-us_topic_0057973197_p34531640"></a><a name="en-us_topic_0057973197_p34531640"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p2571032"><a name="en-us_topic_0057973197_p2571032"></a><a name="en-us_topic_0057973197_p2571032"></a>Specifies the maximum number of security group rules.</p>
<p id="en-us_topic_0057973197_p1559613510539"><a name="en-us_topic_0057973197_p1559613510539"></a><a name="en-us_topic_0057973197_p1559613510539"></a>If the value is <strong id="en-us_topic_0057973197_b1920910112278"><a name="en-us_topic_0057973197_b1920910112278"></a><a name="en-us_topic_0057973197_b1920910112278"></a>-1</strong>, there is no quantity limit.</p>
<p id="p10880112015455"><a name="p10880112015455"></a><a name="p10880112015455"></a>This field is not supported in microversions later than 2.35.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row23139289"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p62343149"><a name="en-us_topic_0057973197_p62343149"></a><a name="en-us_topic_0057973197_p62343149"></a>maxServerGroups</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p16630309"><a name="en-us_topic_0057973197_p16630309"></a><a name="en-us_topic_0057973197_p16630309"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p59557667"><a name="en-us_topic_0057973197_p59557667"></a><a name="en-us_topic_0057973197_p59557667"></a>Specifies the maximum number of ECS groups.</p>
<p id="en-us_topic_0057973197_p162641840115317"><a name="en-us_topic_0057973197_p162641840115317"></a><a name="en-us_topic_0057973197_p162641840115317"></a>If the value is <strong id="en-us_topic_0057973197_b226185302616"><a name="en-us_topic_0057973197_b226185302616"></a><a name="en-us_topic_0057973197_b226185302616"></a>-1</strong>, there is no quantity limit.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row66256959"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p65213442"><a name="en-us_topic_0057973197_p65213442"></a><a name="en-us_topic_0057973197_p65213442"></a>totalCoresUsed</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p47797421"><a name="en-us_topic_0057973197_p47797421"></a><a name="en-us_topic_0057973197_p47797421"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p66270173"><a name="en-us_topic_0057973197_p66270173"></a><a name="en-us_topic_0057973197_p66270173"></a>Specifies the number of used cores.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row59560652"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p59683528"><a name="en-us_topic_0057973197_p59683528"></a><a name="en-us_topic_0057973197_p59683528"></a>totalRAMUsed</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p2527633"><a name="en-us_topic_0057973197_p2527633"></a><a name="en-us_topic_0057973197_p2527633"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p7914408"><a name="en-us_topic_0057973197_p7914408"></a><a name="en-us_topic_0057973197_p7914408"></a>Specifies the size of used memory.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row4120811"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p65350266"><a name="en-us_topic_0057973197_p65350266"></a><a name="en-us_topic_0057973197_p65350266"></a>maxSecurityGroups</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p58880218"><a name="en-us_topic_0057973197_p58880218"></a><a name="en-us_topic_0057973197_p58880218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p34493740"><a name="en-us_topic_0057973197_p34493740"></a><a name="en-us_topic_0057973197_p34493740"></a>Specifies the maximum number of security groups.</p>
<p id="en-us_topic_0057973197_p1137175318536"><a name="en-us_topic_0057973197_p1137175318536"></a><a name="en-us_topic_0057973197_p1137175318536"></a>If the value is <strong id="en-us_topic_0057973197_b203121256102719"><a name="en-us_topic_0057973197_b203121256102719"></a><a name="en-us_topic_0057973197_b203121256102719"></a>-1</strong>, there is no quantity limit.</p>
<p id="p13630184813452"><a name="p13630184813452"></a><a name="p13630184813452"></a>This field is not supported in microversions later than 2.35.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row42008204"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p47221336"><a name="en-us_topic_0057973197_p47221336"></a><a name="en-us_topic_0057973197_p47221336"></a>totalFloatingIpsUsed</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p66831897"><a name="en-us_topic_0057973197_p66831897"></a><a name="en-us_topic_0057973197_p66831897"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p61874073"><a name="en-us_topic_0057973197_p61874073"></a><a name="en-us_topic_0057973197_p61874073"></a>Specifies the number of used floating IP addresses.</p>
<p id="p152301411124612"><a name="p152301411124612"></a><a name="p152301411124612"></a>This field is not supported in microversions later than 2.35.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row19995752"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p9043179"><a name="en-us_topic_0057973197_p9043179"></a><a name="en-us_topic_0057973197_p9043179"></a>totalInstancesUsed</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p61408936"><a name="en-us_topic_0057973197_p61408936"></a><a name="en-us_topic_0057973197_p61408936"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p49520874"><a name="en-us_topic_0057973197_p49520874"></a><a name="en-us_topic_0057973197_p49520874"></a>Specifies the number of used ECSs.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row43034688"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p63257669"><a name="en-us_topic_0057973197_p63257669"></a><a name="en-us_topic_0057973197_p63257669"></a>totalSecurityGroupsUsed</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p23597542"><a name="en-us_topic_0057973197_p23597542"></a><a name="en-us_topic_0057973197_p23597542"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p3329567"><a name="en-us_topic_0057973197_p3329567"></a><a name="en-us_topic_0057973197_p3329567"></a>Specifies the number of used security groups.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row29966109"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p11335741"><a name="en-us_topic_0057973197_p11335741"></a><a name="en-us_topic_0057973197_p11335741"></a>maxTotalFloatingIps</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p45779838"><a name="en-us_topic_0057973197_p45779838"></a><a name="en-us_topic_0057973197_p45779838"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p49354113"><a name="en-us_topic_0057973197_p49354113"></a><a name="en-us_topic_0057973197_p49354113"></a>Specifies the maximum number of floating IP addresses.</p>
<p id="en-us_topic_0057973197_p92491961540"><a name="en-us_topic_0057973197_p92491961540"></a><a name="en-us_topic_0057973197_p92491961540"></a>If the value is <strong id="en-us_topic_0057973197_b179193932814"><a name="en-us_topic_0057973197_b179193932814"></a><a name="en-us_topic_0057973197_b179193932814"></a>-1</strong>, there is no quantity limit.</p>
<p id="p114267721112"><a name="p114267721112"></a><a name="p114267721112"></a>This field is not supported in microversions later than 2.35.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row41533840"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p8797878"><a name="en-us_topic_0057973197_p8797878"></a><a name="en-us_topic_0057973197_p8797878"></a>maxTotalInstances</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p41539488"><a name="en-us_topic_0057973197_p41539488"></a><a name="en-us_topic_0057973197_p41539488"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p11485922"><a name="en-us_topic_0057973197_p11485922"></a><a name="en-us_topic_0057973197_p11485922"></a>Specifies the maximum number of ECSs.</p>
<p id="en-us_topic_0057973197_p54861412155419"><a name="en-us_topic_0057973197_p54861412155419"></a><a name="en-us_topic_0057973197_p54861412155419"></a>If the value is <strong id="en-us_topic_0057973197_b479424672816"><a name="en-us_topic_0057973197_b479424672816"></a><a name="en-us_topic_0057973197_b479424672816"></a>-1</strong>, there is no quantity limit.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row36264434"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p51738071"><a name="en-us_topic_0057973197_p51738071"></a><a name="en-us_topic_0057973197_p51738071"></a>maxTotalCores</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p30034245"><a name="en-us_topic_0057973197_p30034245"></a><a name="en-us_topic_0057973197_p30034245"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p23057881"><a name="en-us_topic_0057973197_p23057881"></a><a name="en-us_topic_0057973197_p23057881"></a>Specifies the maximum number of cores.</p>
<p id="en-us_topic_0057973197_p179025159542"><a name="en-us_topic_0057973197_p179025159542"></a><a name="en-us_topic_0057973197_p179025159542"></a>If the value is <strong id="en-us_topic_0057973197_b565095892814"><a name="en-us_topic_0057973197_b565095892814"></a><a name="en-us_topic_0057973197_b565095892814"></a>-1</strong>, there is no quantity limit.</p>
</td>
</tr>
<tr id="en-us_topic_0057973197_row6194341"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973197_p31979603"><a name="en-us_topic_0057973197_p31979603"></a><a name="en-us_topic_0057973197_p31979603"></a>maxServerGroupMembers</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973197_p40211054"><a name="en-us_topic_0057973197_p40211054"></a><a name="en-us_topic_0057973197_p40211054"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973197_p19782153"><a name="en-us_topic_0057973197_p19782153"></a><a name="en-us_topic_0057973197_p19782153"></a>Specifies the maximum number of members in an ECS group.</p>
<p id="en-us_topic_0057973197_p26221819185410"><a name="en-us_topic_0057973197_p26221819185410"></a><a name="en-us_topic_0057973197_p26221819185410"></a>If the value is <strong id="en-us_topic_0057973197_b165541111182915"><a name="en-us_topic_0057973197_b165541111182915"></a><a name="en-us_topic_0057973197_b165541111182915"></a>-1</strong>, there is no quantity limit.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973197_section27018986"></a>

```
GET https://{endpoint}/v2/d9ebe43510414ef590a4aa158605329e/limits
GET https://{endpoint}/v2.1/d9ebe43510414ef590a4aa158605329e/limits
```

## Example Response<a name="section692711188456"></a>

```
{
  "limits": {
    "rate": [],
    "absolute": {
      "maxServerMeta": 128,
      "maxPersonality": 5,
      "totalServerGroupsUsed": 0,
      "maxImageMeta": 128,
      "maxPersonalitySize": 10240,
      "maxTotalRAMSize": 25165824,
      "maxTotalKeypairs": -1,
      "maxSecurityGroupRules": 20,
      "maxServerGroups": -1,
      "totalCoresUsed": 0,
      "totalRAMUsed": 0,
      "maxSecurityGroups": 10,
      "totalFloatingIpsUsed": 0,
      "totalInstancesUsed": 0,
      "totalSecurityGroupsUsed": 0,
      "maxTotalFloatingIps": 10,
      "maxTotalInstances": 2048,
      "maxTotalCores": 20480,
      "maxServerGroupMembers": -1
    }
  }
}
```

## Returned Values<a name="en-us_topic_0057973197_section1642564"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

