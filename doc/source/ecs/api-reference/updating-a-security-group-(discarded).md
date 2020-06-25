# Updating a Security Group \(Discarded\)<a name="EN-US_TOPIC_0065817700"></a>

## Function<a name="en-us_topic_0057972664_section65665194"></a>

This API is used to update a security group.

## Constraints<a name="en-us_topic_0057972664_section17280459"></a>

This API will be discarded. 

You are advised to use the desired network API. For details, see "Security Group \(Native OpenStack API\) \> Updating a Security Group" in  _Virtual Private Network API Reference_.

## URI<a name="en-us_topic_0057972664_section54115834"></a>

PUT /v2/\{project\_id\}/os-security-groups/\{security\_group\_id\}

PUT /v2.1/\{project\_id\}/os-security-groups/\{security\_group\_id\}

[Table 1](#en-us_topic_0057972664_table55945983)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972664_table55945983"></a>
<table><thead align="left"><tr id="en-us_topic_0057972664_row11302482"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972664_row49888896"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972664_p14468758"><a name="en-us_topic_0057972664_p14468758"></a><a name="en-us_topic_0057972664_p14468758"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972664_p31118786"><a name="en-us_topic_0057972664_p31118786"></a><a name="en-us_topic_0057972664_p31118786"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972664_row3928161611210"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972664_p4928516101217"><a name="en-us_topic_0057972664_p4928516101217"></a><a name="en-us_topic_0057972664_p4928516101217"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972664_p18928816181213"><a name="en-us_topic_0057972664_p18928816181213"></a><a name="en-us_topic_0057972664_p18928816181213"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972664_p292821613128"><a name="en-us_topic_0057972664_p292821613128"></a><a name="en-us_topic_0057972664_p292821613128"></a>Specifies the security group ID, which is specified in the URI.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972664_section21306406"></a>

[Table 2](#en-us_topic_0057972664_table52078514)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0057972664_table52078514"></a>
<table><thead align="left"><tr id="en-us_topic_0057972664_row2492560"><th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.2.5.1.1"><p id="en-us_topic_0058745339_p39560242204918"><a name="en-us_topic_0058745339_p39560242204918"></a><a name="en-us_topic_0058745339_p39560242204918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.5.1.2"><p id="p125971723123015"><a name="p125971723123015"></a><a name="p125971723123015"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.3"><p id="en-us_topic_0058745339_p50263001204918"><a name="en-us_topic_0058745339_p50263001204918"></a><a name="en-us_topic_0058745339_p50263001204918"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.5.1.4"><p id="en-us_topic_0058745339_p2596798204918"><a name="en-us_topic_0058745339_p2596798204918"></a><a name="en-us_topic_0058745339_p2596798204918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972664_row30749271"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p7663035"><a name="en-us_topic_0057972664_p7663035"></a><a name="en-us_topic_0057972664_p7663035"></a>security_group</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="p5597172311304"><a name="p5597172311304"></a><a name="p5597172311304"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p16726062"><a name="en-us_topic_0057972664_p16726062"></a><a name="en-us_topic_0057972664_p16726062"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p16706408"><a name="en-us_topic_0057972664_p16706408"></a><a name="en-us_topic_0057972664_p16706408"></a>Specifies the security group in the message body. For details, see <a href="#en-us_topic_0057972664_table11041789">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Objects of request parameter  **security\_group**

<a name="en-us_topic_0057972664_table11041789"></a>
<table><thead align="left"><tr id="en-us_topic_0057972664_row9230088"><th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.2.5.1.1"><p id="p14601427201219"><a name="p14601427201219"></a><a name="p14601427201219"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.5.1.2"><p id="p67171626153010"><a name="p67171626153010"></a><a name="p67171626153010"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.3"><p id="p146052771212"><a name="p146052771212"></a><a name="p146052771212"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.5.1.4"><p id="p20601027181211"><a name="p20601027181211"></a><a name="p20601027181211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972664_row7414170"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p63676932"><a name="en-us_topic_0057972664_p63676932"></a><a name="en-us_topic_0057972664_p63676932"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="p57171626103012"><a name="p57171626103012"></a><a name="p57171626103012"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p57557895"><a name="en-us_topic_0057972664_p57557895"></a><a name="en-us_topic_0057972664_p57557895"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p15772917"><a name="en-us_topic_0057972664_p15772917"></a><a name="en-us_topic_0057972664_p15772917"></a>Specifies the security group name.</p>
<p id="en-us_topic_0057972664_p9152184911574"><a name="en-us_topic_0057972664_p9152184911574"></a><a name="en-us_topic_0057972664_p9152184911574"></a>The value cannot exceed 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0057972664_row7738529"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p22841149"><a name="en-us_topic_0057972664_p22841149"></a><a name="en-us_topic_0057972664_p22841149"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="p4717926203010"><a name="p4717926203010"></a><a name="p4717926203010"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p38193748"><a name="en-us_topic_0057972664_p38193748"></a><a name="en-us_topic_0057972664_p38193748"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p4687385"><a name="en-us_topic_0057972664_p4687385"></a><a name="en-us_topic_0057972664_p4687385"></a>Specifies information about a security group.</p>
<p id="en-us_topic_0057972664_p1733534185813"><a name="en-us_topic_0057972664_p1733534185813"></a><a name="en-us_topic_0057972664_p1733534185813"></a>The value cannot exceed 255 characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057972664_section57539933"></a>

[Table 4](#en-us_topic_0057972664_table44133910)  describes the response parameters.

**Table  4**  Response parameters

<a name="en-us_topic_0057972664_table44133910"></a>
<table><thead align="left"><tr id="en-us_topic_0057972664_row60896162"><th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.2.5.1.1"><p id="p875863061217"><a name="p875863061217"></a><a name="p875863061217"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.5.1.2"><p id="p45394474304"><a name="p45394474304"></a><a name="p45394474304"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.3"><p id="p1875853061210"><a name="p1875853061210"></a><a name="p1875853061210"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.5.1.4"><p id="p197581530181210"><a name="p197581530181210"></a><a name="p197581530181210"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972664_row17602849"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p16544703"><a name="en-us_topic_0057972664_p16544703"></a><a name="en-us_topic_0057972664_p16544703"></a>security_group</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.2 "><p id="p2539147153014"><a name="p2539147153014"></a><a name="p2539147153014"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p65052577"><a name="en-us_topic_0057972664_p65052577"></a><a name="en-us_topic_0057972664_p65052577"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p64696659"><a name="en-us_topic_0057972664_p64696659"></a><a name="en-us_topic_0057972664_p64696659"></a>Specifies the security group. For details, see <a href="#en-us_topic_0057972664_table5938035">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  Objects of response parameter  **security\_group**

<a name="en-us_topic_0057972664_table5938035"></a>
<table><thead align="left"><tr id="en-us_topic_0057972664_row27762102"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.1"><p id="p13502533121212"><a name="p13502533121212"></a><a name="p13502533121212"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.2"><p id="p730821283112"><a name="p730821283112"></a><a name="p730821283112"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.3"><p id="p155181933111211"><a name="p155181933111211"></a><a name="p155181933111211"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.45454545454546%" id="mcps1.2.5.1.4"><p id="p125181533171211"><a name="p125181533171211"></a><a name="p125181533171211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972664_row21024178"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p25236858"><a name="en-us_topic_0057972664_p25236858"></a><a name="en-us_topic_0057972664_p25236858"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p1308191263113"><a name="p1308191263113"></a><a name="p1308191263113"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p8741693161834"><a name="en-us_topic_0057972664_p8741693161834"></a><a name="en-us_topic_0057972664_p8741693161834"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p4222112625811"><a name="en-us_topic_0057972664_p4222112625811"></a><a name="en-us_topic_0057972664_p4222112625811"></a>Specifies information about a security group.</p>
<p id="en-us_topic_0057972664_p60714046"><a name="en-us_topic_0057972664_p60714046"></a><a name="en-us_topic_0057972664_p60714046"></a>The value cannot exceed 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0057972664_row9555503"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p35798250"><a name="en-us_topic_0057972664_p35798250"></a><a name="en-us_topic_0057972664_p35798250"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p9308101253120"><a name="p9308101253120"></a><a name="p9308101253120"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p58105597161834"><a name="en-us_topic_0057972664_p58105597161834"></a><a name="en-us_topic_0057972664_p58105597161834"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p33323423"><a name="en-us_topic_0057972664_p33323423"></a><a name="en-us_topic_0057972664_p33323423"></a>Specifies the security group ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972664_row31475357"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p66476022"><a name="en-us_topic_0057972664_p66476022"></a><a name="en-us_topic_0057972664_p66476022"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p14308191211315"><a name="p14308191211315"></a><a name="p14308191211315"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p66138500161834"><a name="en-us_topic_0057972664_p66138500161834"></a><a name="en-us_topic_0057972664_p66138500161834"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p31741019"><a name="en-us_topic_0057972664_p31741019"></a><a name="en-us_topic_0057972664_p31741019"></a>Specifies the security group name.</p>
<p id="en-us_topic_0057972664_p49657545587"><a name="en-us_topic_0057972664_p49657545587"></a><a name="en-us_topic_0057972664_p49657545587"></a>The value cannot exceed 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0057972664_row17233719"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p53754023"><a name="en-us_topic_0057972664_p53754023"></a><a name="en-us_topic_0057972664_p53754023"></a>rules</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p15308191293111"><a name="p15308191293111"></a><a name="p15308191293111"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p61314810161834"><a name="en-us_topic_0057972664_p61314810161834"></a><a name="en-us_topic_0057972664_p61314810161834"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p56666602"><a name="en-us_topic_0057972664_p56666602"></a><a name="en-us_topic_0057972664_p56666602"></a>Specifies the security group rule list. For details, see <a href="#en-us_topic_0057972664_table64215808">Table 6</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0057972664_row40237373"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p38001806"><a name="en-us_topic_0057972664_p38001806"></a><a name="en-us_topic_0057972664_p38001806"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p830819125312"><a name="p830819125312"></a><a name="p830819125312"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p8281316161834"><a name="en-us_topic_0057972664_p8281316161834"></a><a name="en-us_topic_0057972664_p8281316161834"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p43875021"><a name="en-us_topic_0057972664_p43875021"></a><a name="en-us_topic_0057972664_p43875021"></a>Specifies the tenant or project ID.</p>
<p id="en-us_topic_0057972664_p209451415910"><a name="en-us_topic_0057972664_p209451415910"></a><a name="en-us_topic_0057972664_p209451415910"></a>The value cannot exceed 255 characters.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **security\_group\_rule**  objects

<a name="en-us_topic_0057972664_table64215808"></a>
<table><thead align="left"><tr id="en-us_topic_0057972664_row50789581"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.1"><p id="p14934193631220"><a name="p14934193631220"></a><a name="p14934193631220"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.2"><p id="p839243119312"><a name="p839243119312"></a><a name="p839243119312"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.5.1.3"><p id="p1593416362121"><a name="p1593416362121"></a><a name="p1593416362121"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.554455445544555%" id="mcps1.2.5.1.4"><p id="p10934636101219"><a name="p10934636101219"></a><a name="p10934636101219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972664_row16670523"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p2523549416194"><a name="en-us_topic_0057972664_p2523549416194"></a><a name="en-us_topic_0057972664_p2523549416194"></a>parent_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p1392183173116"><a name="p1392183173116"></a><a name="p1392183173116"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p2351847316194"><a name="en-us_topic_0057972664_p2351847316194"></a><a name="en-us_topic_0057972664_p2351847316194"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p3955312816194"><a name="en-us_topic_0057972664_p3955312816194"></a><a name="en-us_topic_0057972664_p3955312816194"></a>Specifies the associated security group ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972664_row55443761"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p5606438216194"><a name="en-us_topic_0057972664_p5606438216194"></a><a name="en-us_topic_0057972664_p5606438216194"></a>ip_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p8393133163114"><a name="p8393133163114"></a><a name="p8393133163114"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p6351133316194"><a name="en-us_topic_0057972664_p6351133316194"></a><a name="en-us_topic_0057972664_p6351133316194"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p4556843916194"><a name="en-us_topic_0057972664_p4556843916194"></a><a name="en-us_topic_0057972664_p4556843916194"></a>Specifies the protocol type or the IP protocol number. The value can be <strong id="en-us_topic_0057972664_b84235270618469"><a name="en-us_topic_0057972664_b84235270618469"></a><a name="en-us_topic_0057972664_b84235270618469"></a>icmp</strong>, <strong id="en-us_topic_0057972664_b84235270619548"><a name="en-us_topic_0057972664_b84235270619548"></a><a name="en-us_topic_0057972664_b84235270619548"></a>tcp</strong>, <strong id="en-us_topic_0057972664_b842352706184613"><a name="en-us_topic_0057972664_b842352706184613"></a><a name="en-us_topic_0057972664_b842352706184613"></a>udp</strong>, or the IP protocol number.</p>
</td>
</tr>
<tr id="en-us_topic_0057972664_row63384014"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p3850893516194"><a name="en-us_topic_0057972664_p3850893516194"></a><a name="en-us_topic_0057972664_p3850893516194"></a>from_port</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p153935313314"><a name="p153935313314"></a><a name="p153935313314"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p138869916194"><a name="en-us_topic_0057972664_p138869916194"></a><a name="en-us_topic_0057972664_p138869916194"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p2078843616194"><a name="en-us_topic_0057972664_p2078843616194"></a><a name="en-us_topic_0057972664_p2078843616194"></a>Specifies the start port. The value ranges from 1 to 65,535 and cannot be greater than <strong id="en-us_topic_0057972664_b842352706192235"><a name="en-us_topic_0057972664_b842352706192235"></a><a name="en-us_topic_0057972664_b842352706192235"></a>to_port</strong>. When <strong id="en-us_topic_0057972664_b84235270619236"><a name="en-us_topic_0057972664_b84235270619236"></a><a name="en-us_topic_0057972664_b84235270619236"></a>ip_protocol</strong> is <strong id="en-us_topic_0057972664_b842352706192316"><a name="en-us_topic_0057972664_b842352706192316"></a><a name="en-us_topic_0057972664_b842352706192316"></a>icmp</strong>, this parameter specifies a port type with a length from 0 to 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0057972664_row56087165"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p2893204816194"><a name="en-us_topic_0057972664_p2893204816194"></a><a name="en-us_topic_0057972664_p2893204816194"></a>to_port</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p43932313319"><a name="p43932313319"></a><a name="p43932313319"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p5065329216194"><a name="en-us_topic_0057972664_p5065329216194"></a><a name="en-us_topic_0057972664_p5065329216194"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p2803062516194"><a name="en-us_topic_0057972664_p2803062516194"></a><a name="en-us_topic_0057972664_p2803062516194"></a>Specifies the end port. The value ranges from 1 to 65,535 and cannot be less than <strong id="en-us_topic_0057972664_b842352706162914"><a name="en-us_topic_0057972664_b842352706162914"></a><a name="en-us_topic_0057972664_b842352706162914"></a>from_port</strong>. When <strong id="en-us_topic_0057972664_b842352706162939"><a name="en-us_topic_0057972664_b842352706162939"></a><a name="en-us_topic_0057972664_b842352706162939"></a>ip_protocol</strong> is <strong id="en-us_topic_0057972664_b842352706162947"><a name="en-us_topic_0057972664_b842352706162947"></a><a name="en-us_topic_0057972664_b842352706162947"></a>icmp</strong>, it specifies the code. The value ranges from 0 to 255. If both <strong id="en-us_topic_0057972664_b842352706163018"><a name="en-us_topic_0057972664_b842352706163018"></a><a name="en-us_topic_0057972664_b842352706163018"></a>from_port</strong> and <strong id="en-us_topic_0057972664_b842352706163116"><a name="en-us_topic_0057972664_b842352706163116"></a><a name="en-us_topic_0057972664_b842352706163116"></a>to_port</strong> are <strong id="en-us_topic_0057972664_b842352706163025"><a name="en-us_topic_0057972664_b842352706163025"></a><a name="en-us_topic_0057972664_b842352706163025"></a>-1</strong>, any ICMP packet can be transmitted.</p>
</td>
</tr>
<tr id="en-us_topic_0057972664_row59740974"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p5271149216194"><a name="en-us_topic_0057972664_p5271149216194"></a><a name="en-us_topic_0057972664_p5271149216194"></a>ip_range</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p639323103118"><a name="p639323103118"></a><a name="p639323103118"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p6042635416194"><a name="en-us_topic_0057972664_p6042635416194"></a><a name="en-us_topic_0057972664_p6042635416194"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p5897723816194"><a name="en-us_topic_0057972664_p5897723816194"></a><a name="en-us_topic_0057972664_p5897723816194"></a>Specifies the peer IP segment in CIDR format. For details, see <a href="#en-us_topic_0057972664_table4101480163218">Table 7</a>. The value of <strong id="en-us_topic_0057972664_b84235270618494"><a name="en-us_topic_0057972664_b84235270618494"></a><a name="en-us_topic_0057972664_b84235270618494"></a>ip_range</strong> or <strong id="en-us_topic_0057972664_b84235270618498"><a name="en-us_topic_0057972664_b84235270618498"></a><a name="en-us_topic_0057972664_b84235270618498"></a>group</strong> must be empty.</p>
</td>
</tr>
<tr id="en-us_topic_0057972664_row18301082"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p3354966816194"><a name="en-us_topic_0057972664_p3354966816194"></a><a name="en-us_topic_0057972664_p3354966816194"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p18393153115317"><a name="p18393153115317"></a><a name="p18393153115317"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p6004111716194"><a name="en-us_topic_0057972664_p6004111716194"></a><a name="en-us_topic_0057972664_p6004111716194"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p5918086916194"><a name="en-us_topic_0057972664_p5918086916194"></a><a name="en-us_topic_0057972664_p5918086916194"></a>Specifies the name of the peer security group and the ID of the tenant in the peer security group. For details, see <a href="#en-us_topic_0057972664_table9527961163416">Table 8</a>. The value of <strong id="en-us_topic_0057972664_b1152282663192924"><a name="en-us_topic_0057972664_b1152282663192924"></a><a name="en-us_topic_0057972664_b1152282663192924"></a>ip_range</strong> or <strong id="en-us_topic_0057972664_b506241931192924"><a name="en-us_topic_0057972664_b506241931192924"></a><a name="en-us_topic_0057972664_b506241931192924"></a>group</strong> must be empty.</p>
</td>
</tr>
<tr id="en-us_topic_0057972664_row3099778"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p2717504716194"><a name="en-us_topic_0057972664_p2717504716194"></a><a name="en-us_topic_0057972664_p2717504716194"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p1239333183111"><a name="p1239333183111"></a><a name="p1239333183111"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p3013279116194"><a name="en-us_topic_0057972664_p3013279116194"></a><a name="en-us_topic_0057972664_p3013279116194"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p5953487016194"><a name="en-us_topic_0057972664_p5953487016194"></a><a name="en-us_topic_0057972664_p5953487016194"></a>Specifies the security group rule ID in UUID format.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **ip\_range**  objects

<a name="en-us_topic_0057972664_table4101480163218"></a>
<table><thead align="left"><tr id="en-us_topic_0057972664_row55642344163218"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.1"><p id="p17249416128"><a name="p17249416128"></a><a name="p17249416128"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.2"><p id="p12695115783116"><a name="p12695115783116"></a><a name="p12695115783116"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.5.1.3"><p id="p272414151210"><a name="p272414151210"></a><a name="p272414151210"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.554455445544555%" id="mcps1.2.5.1.4"><p id="p47247419120"><a name="p47247419120"></a><a name="p47247419120"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972664_row5649056163218"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p54920430163218"><a name="en-us_topic_0057972664_p54920430163218"></a><a name="en-us_topic_0057972664_p54920430163218"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p196951557143110"><a name="p196951557143110"></a><a name="p196951557143110"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p19369856163218"><a name="en-us_topic_0057972664_p19369856163218"></a><a name="en-us_topic_0057972664_p19369856163218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p48550802163218"><a name="en-us_topic_0057972664_p48550802163218"></a><a name="en-us_topic_0057972664_p48550802163218"></a>Specifies the peer IP segment in CIDR format.</p>
<p id="en-us_topic_0057972664_p9404201915595"><a name="en-us_topic_0057972664_p9404201915595"></a><a name="en-us_topic_0057972664_p9404201915595"></a>The value cannot exceed 255 characters.</p>
</td>
</tr>
</tbody>
</table>

**Table  8** **group**  objects

<a name="en-us_topic_0057972664_table9527961163416"></a>
<table><thead align="left"><tr id="en-us_topic_0057972664_row57542164163416"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.1"><p id="p44391448122"><a name="p44391448122"></a><a name="p44391448122"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.2"><p id="p1914510120324"><a name="p1914510120324"></a><a name="p1914510120324"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.5.1.3"><p id="p3439134412128"><a name="p3439134412128"></a><a name="p3439134412128"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.554455445544555%" id="mcps1.2.5.1.4"><p id="p24391044131213"><a name="p24391044131213"></a><a name="p24391044131213"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972664_row46600064163416"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p16508853163416"><a name="en-us_topic_0057972664_p16508853163416"></a><a name="en-us_topic_0057972664_p16508853163416"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p214619118324"><a name="p214619118324"></a><a name="p214619118324"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p62148702163416"><a name="en-us_topic_0057972664_p62148702163416"></a><a name="en-us_topic_0057972664_p62148702163416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p4179246163416"><a name="en-us_topic_0057972664_p4179246163416"></a><a name="en-us_topic_0057972664_p4179246163416"></a>Specifies the ID of the tenant of the peer security group.</p>
</td>
</tr>
<tr id="en-us_topic_0057972664_row37613216163416"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972664_p26771660163416"><a name="en-us_topic_0057972664_p26771660163416"></a><a name="en-us_topic_0057972664_p26771660163416"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p61462173213"><a name="p61462173213"></a><a name="p61462173213"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972664_p21020848163416"><a name="en-us_topic_0057972664_p21020848163416"></a><a name="en-us_topic_0057972664_p21020848163416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972664_p9073859163416"><a name="en-us_topic_0057972664_p9073859163416"></a><a name="en-us_topic_0057972664_p9073859163416"></a>Specifies the name of the peer security group.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057972664_section48097351"></a>

```
PUT https://{endpoint}/v2/bb1118612ba64af3a6ea63a1bdcaa5ae/os-security-groups/3d02312d-0764-49c9-8244-2368ddce0045
PUT https://{endpoint}/v2.1/bb1118612ba64af3a6ea63a1bdcaa5ae/os-security-groups/3d02312d-0764-49c9-8244-2368ddce0045
```

```
{
    "security_group": {
        "name": "test",
        "description": "description"
    }
}
```

## Example Response<a name="section435415620273"></a>

```
{
  "security_group": {
    "rules": [
      {
        "from_port": null,
        "group": {
          "tenant_id": "bb1118612ba64af3a6ea63a1bdcaa5ae",
          "name": "test"
        },
        "ip_protocol": null,
        "to_port": null,
        "parent_group_id": "3d02312d-0764-49c9-8244-2368ddce0045",
        "ip_range": {},
        "id": "00dec0b6-8e96-4906-aadf-46cfe54cf5ef"
      }
    ],
    "tenant_id": "bb1118612ba64af3a6ea63a1bdcaa5ae",
    "id": "3d02312d-0764-49c9-8244-2368ddce0045",
    "name": "test",
    "description": "description"
  }
}
```

## Returned Values<a name="en-us_topic_0057972664_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

