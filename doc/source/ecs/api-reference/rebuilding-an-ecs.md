# Rebuilding an ECS<a name="EN-US_TOPIC_0065817688"></a>

## Function<a name="en-us_topic_0058745339_section59295179204041"></a>

This API is used to rebuild an ECS.

You can use the original image or another image to rebuild an ECS. This API supports different OSs.

This API is native from the community for defcore tests. 

If you are required to reinstall or change an ECS OS, ECS APIs are recommended. For details, see "Reinstalling an ECS OS \(Using an Image with Cloud-Init Installed\)" and "Changing an ECS OS \(Using an Image with Cloud-Init Installed\)".

## Constraints<a name="en-us_topic_0058745339_section7529181132617"></a>

-   ECSs in the error state cannot be rebuilt.
-   The password cannot be set during the rebuilding.

## URI<a name="en-us_topic_0058745339_section50411366204518"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/action

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#en-us_topic_0058745339_table46110007)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0058745339_table46110007"></a>
<table><thead align="left"><tr id="en-us_topic_0058745339_row14148614"><th class="cellrowborder" valign="top" width="17.73%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.73%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="64.53999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0058745339_row17201924"><td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p51178607"><a name="en-us_topic_0058745339_p51178607"></a><a name="en-us_topic_0058745339_p51178607"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p51826478"><a name="en-us_topic_0058745339_p51826478"></a><a name="en-us_topic_0058745339_p51826478"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.53999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row615338831654"><td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p519996316521"><a name="en-us_topic_0058745339_p519996316521"></a><a name="en-us_topic_0058745339_p519996316521"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p5588153816521"><a name="en-us_topic_0058745339_p5588153816521"></a><a name="en-us_topic_0058745339_p5588153816521"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.53999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p1719074216521"><a name="en-us_topic_0058745339_p1719074216521"></a><a name="en-us_topic_0058745339_p1719074216521"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0058745339_section48864997204742"></a>

[Table 2](#en-us_topic_0058745339_table44724688204850)  describes the request parameters.

**Table  2**  Request parameter

<a name="en-us_topic_0058745339_table44724688204850"></a>
<table><thead align="left"><tr id="en-us_topic_0058745339_row1798761204850"><th class="cellrowborder" valign="top" width="17.69%" id="mcps1.2.5.1.1"><p id="en-us_topic_0058745339_p39560242204918"><a name="en-us_topic_0058745339_p39560242204918"></a><a name="en-us_topic_0058745339_p39560242204918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.080000000000002%" id="mcps1.2.5.1.2"><p id="p4117282186"><a name="p4117282186"></a><a name="p4117282186"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0058745339_p50263001204918"><a name="en-us_topic_0058745339_p50263001204918"></a><a name="en-us_topic_0058745339_p50263001204918"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.080000000000005%" id="mcps1.2.5.1.4"><p id="en-us_topic_0058745339_p2596798204918"><a name="en-us_topic_0058745339_p2596798204918"></a><a name="en-us_topic_0058745339_p2596798204918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0058745339_row5848663204850"><td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0058745339_p22382703204933"><a name="en-us_topic_0058745339_p22382703204933"></a><a name="en-us_topic_0058745339_p22382703204933"></a>rebuild</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.2.5.1.2 "><p id="p11111228191811"><a name="p11111228191811"></a><a name="p11111228191811"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0058745339_p1059631204933"><a name="en-us_topic_0058745339_p1059631204933"></a><a name="en-us_topic_0058745339_p1059631204933"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="52.080000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0058745339_p40030009204933"><a name="en-us_topic_0058745339_p40030009204933"></a><a name="en-us_topic_0058745339_p40030009204933"></a>Rebuilds an ECS.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **rebuild**  parameters

<a name="en-us_topic_0058745339_table59377750205027"></a>
<table><thead align="left"><tr id="en-us_topic_0058745339_row1841518205027"><th class="cellrowborder" valign="top" width="17.681768176817684%" id="mcps1.2.5.1.1"><p id="p1568292016586"><a name="p1568292016586"></a><a name="p1568292016586"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.2.5.1.2"><p id="p1639583116187"><a name="p1639583116187"></a><a name="p1639583116187"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.201320132013203%" id="mcps1.2.5.1.3"><p id="p146981320145813"><a name="p146981320145813"></a><a name="p146981320145813"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.945194519451945%" id="mcps1.2.5.1.4"><p id="p1869842018581"><a name="p1869842018581"></a><a name="p1869842018581"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0058745339_row20042728205027"><td class="cellrowborder" valign="top" width="17.681768176817684%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0058745339_p29571470205128"><a name="en-us_topic_0058745339_p29571470205128"></a><a name="en-us_topic_0058745339_p29571470205128"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="p939512315184"><a name="p939512315184"></a><a name="p939512315184"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.201320132013203%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0058745339_p46478847205128"><a name="en-us_topic_0058745339_p46478847205128"></a><a name="en-us_topic_0058745339_p46478847205128"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.945194519451945%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0058745339_p239617401318"><a name="en-us_topic_0058745339_p239617401318"></a><a name="en-us_topic_0058745339_p239617401318"></a>Specifies the name of the rebuilt ECS.</p>
<p id="en-us_topic_0058745339_p5042904205128"><a name="en-us_topic_0058745339_p5042904205128"></a><a name="en-us_topic_0058745339_p5042904205128"></a>The value contains 1 to 254 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row57219807205027"><td class="cellrowborder" valign="top" width="17.681768176817684%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0058745339_p52398862205128"><a name="en-us_topic_0058745339_p52398862205128"></a><a name="en-us_topic_0058745339_p52398862205128"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="p10395103115182"><a name="p10395103115182"></a><a name="p10395103115182"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.201320132013203%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0058745339_p16449439205128"><a name="en-us_topic_0058745339_p16449439205128"></a><a name="en-us_topic_0058745339_p16449439205128"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.945194519451945%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0058745339_p1672891161318"><a name="en-us_topic_0058745339_p1672891161318"></a><a name="en-us_topic_0058745339_p1672891161318"></a>Specifies the metadata of the rebuilt ECS.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row32218260205027"><td class="cellrowborder" valign="top" width="17.681768176817684%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0058745339_p2194767205128"><a name="en-us_topic_0058745339_p2194767205128"></a><a name="en-us_topic_0058745339_p2194767205128"></a>imageRef</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="p339610315183"><a name="p339610315183"></a><a name="p339610315183"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.201320132013203%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0058745339_p43558409205128"><a name="en-us_topic_0058745339_p43558409205128"></a><a name="en-us_topic_0058745339_p43558409205128"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.945194519451945%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0058745339_p37180395205128"><a name="en-us_topic_0058745339_p37180395205128"></a><a name="en-us_topic_0058745339_p37180395205128"></a>Specifies the image ID or URL.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row9353828101214"><td class="cellrowborder" valign="top" width="17.681768176817684%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0058745339_p16353828151216"><a name="en-us_topic_0058745339_p16353828151216"></a><a name="en-us_topic_0058745339_p16353828151216"></a>adminPass</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="p12396183110189"><a name="p12396183110189"></a><a name="p12396183110189"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.201320132013203%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0058745339_p179096118134"><a name="en-us_topic_0058745339_p179096118134"></a><a name="en-us_topic_0058745339_p179096118134"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.945194519451945%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0058745339_p20354192813125"><a name="en-us_topic_0058745339_p20354192813125"></a><a name="en-us_topic_0058745339_p20354192813125"></a>Specifies the password for logging in to the rebuilt ECS. This parameter does not take effect.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row1071203310123"><td class="cellrowborder" valign="top" width="17.681768176817684%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0058745339_p793719508123"><a name="en-us_topic_0058745339_p793719508123"></a><a name="en-us_topic_0058745339_p793719508123"></a>OS-DCF:diskConfig</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="p53961031141813"><a name="p53961031141813"></a><a name="p53961031141813"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.201320132013203%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0058745339_p489821151317"><a name="en-us_topic_0058745339_p489821151317"></a><a name="en-us_topic_0058745339_p489821151317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.945194519451945%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0058745339_p1779133118132"><a name="en-us_topic_0058745339_p1779133118132"></a><a name="en-us_topic_0058745339_p1779133118132"></a>Not supported</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row10417162481217"><td class="cellrowborder" valign="top" width="17.681768176817684%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0058745339_p989235491212"><a name="en-us_topic_0058745339_p989235491212"></a><a name="en-us_topic_0058745339_p989235491212"></a>preserve_ephemeral</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="p1539673112183"><a name="p1539673112183"></a><a name="p1539673112183"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.201320132013203%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0058745339_p3418172481218"><a name="en-us_topic_0058745339_p3418172481218"></a><a name="en-us_topic_0058745339_p3418172481218"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.945194519451945%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0058745339_p4418112471220"><a name="en-us_topic_0058745339_p4418112471220"></a><a name="en-us_topic_0058745339_p4418112471220"></a>Specifies whether to retain the temporary disk. This parameter is not supported.</p>
</td>
</tr>
<tr id="row2615592185"><td class="cellrowborder" valign="top" width="17.681768176817684%" headers="mcps1.2.5.1.1 "><p id="p162596184"><a name="p162596184"></a><a name="p162596184"></a>key_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="p7396123181820"><a name="p7396123181820"></a><a name="p7396123181820"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.201320132013203%" headers="mcps1.2.5.1.3 "><p id="p196105911183"><a name="p196105911183"></a><a name="p196105911183"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.945194519451945%" headers="mcps1.2.5.1.4 "><p id="p14625910182"><a name="p14625910182"></a><a name="p14625910182"></a>Specifies the key pair name. If the value is null, the existing key pair is left blank.</p>
<p id="p1613950102115"><a name="p1613950102115"></a><a name="p1613950102115"></a>This field is supported in microversion 2.54.</p>
</td>
</tr>
<tr id="row1412464616713"><td class="cellrowborder" valign="top" width="17.681768176817684%" headers="mcps1.2.5.1.1 "><p id="p24211473719"><a name="p24211473719"></a><a name="p24211473719"></a>user_data</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="p13396163118181"><a name="p13396163118181"></a><a name="p13396163118181"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.201320132013203%" headers="mcps1.2.5.1.3 "><p id="p1542110471478"><a name="p1542110471478"></a><a name="p1542110471478"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.945194519451945%" headers="mcps1.2.5.1.4 "><p id="p13421447279"><a name="p13421447279"></a><a name="p13421447279"></a>Specifies the user data. This parameter is an extended attribute. The character string contains 1 to 65,534 characters and must be encrypted using Base64.</p>
<p id="p74211447674"><a name="p74211447674"></a><a name="p74211447674"></a>This field is supported in microversion 2.57.</p>
<p id="p151383081516"><a name="p151383081516"></a><a name="p151383081516"></a>For more information about the user data to be injected, see "Injecting User Data into ECSs" in <em>Elastic Cloud Server User Guide</em>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0058745339_section3406845205255"></a>

[Table 4](#en-us_topic_0058745339_table49173801205341)  describes the response parameters.

**Table  4**  Response parameters

<a name="en-us_topic_0058745339_table49173801205341"></a>
<table><thead align="left"><tr id="en-us_topic_0058745339_row38681531205341"><th class="cellrowborder" valign="top" width="17.638236176382364%" id="mcps1.2.4.1.1"><p id="en-us_topic_0058745339_p6106389205358"><a name="en-us_topic_0058745339_p6106389205358"></a><a name="en-us_topic_0058745339_p6106389205358"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.14828517148285%" id="mcps1.2.4.1.2"><p id="en-us_topic_0058745339_p24855533205358"><a name="en-us_topic_0058745339_p24855533205358"></a><a name="en-us_topic_0058745339_p24855533205358"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.21347865213478%" id="mcps1.2.4.1.3"><p id="en-us_topic_0058745339_p2614453205358"><a name="en-us_topic_0058745339_p2614453205358"></a><a name="en-us_topic_0058745339_p2614453205358"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0058745339_row39606926205341"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p43945661205412"><a name="en-us_topic_0058745339_p43945661205412"></a><a name="en-us_topic_0058745339_p43945661205412"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p2828827205412"><a name="en-us_topic_0058745339_p2828827205412"></a><a name="en-us_topic_0058745339_p2828827205412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p974868915521"><a name="en-us_topic_0058745339_p974868915521"></a><a name="en-us_topic_0058745339_p974868915521"></a>Specifies the ECS status.</p>
<p id="en-us_topic_0058745339_p5554125915523"><a name="en-us_topic_0058745339_p5554125915523"></a><a name="en-us_topic_0058745339_p5554125915523"></a>Values:</p>
<a name="en-us_topic_0058745339_ul4409511215559"></a><a name="en-us_topic_0058745339_ul4409511215559"></a><ul id="en-us_topic_0058745339_ul4409511215559"><li><strong id="b1404992615559"><a name="b1404992615559"></a><a name="b1404992615559"></a>ACTIVE</strong></li><li><strong id="b5934047815559"><a name="b5934047815559"></a><a name="b5934047815559"></a>REBOOT</strong></li><li><strong id="b6430225415559"><a name="b6430225415559"></a><a name="b6430225415559"></a>HARD_REBOOT</strong></li><li><strong id="b4184937615559"><a name="b4184937615559"></a><a name="b4184937615559"></a>REBUILD</strong></li><li><strong id="b4110007015559"><a name="b4110007015559"></a><a name="b4110007015559"></a>MIGRATING</strong></li><li><strong id="b3435631115559"><a name="b3435631115559"></a><a name="b3435631115559"></a>BUILD</strong></li><li><strong id="b4077135015559"><a name="b4077135015559"></a><a name="b4077135015559"></a>SHUTOFF</strong></li><li><strong id="b3139783515559"><a name="b3139783515559"></a><a name="b3139783515559"></a>RESIZE</strong></li><li><strong id="b1414506315559"><a name="b1414506315559"></a><a name="b1414506315559"></a>VERIFY_RESIZE</strong></li><li><strong id="b6019670715559"><a name="b6019670715559"></a><a name="b6019670715559"></a>ERROR</strong></li><li><strong id="b489945615559"><a name="b489945615559"></a><a name="b489945615559"></a>DELETED</strong></li></ul>
<p id="p98198168558"><a name="p98198168558"></a><a name="p98198168558"></a>For details, see <a href="ecs-statuses.md">ECS Statuses</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row18260674205341"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p41230700205412"><a name="en-us_topic_0058745339_p41230700205412"></a><a name="en-us_topic_0058745339_p41230700205412"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p51352393205412"><a name="en-us_topic_0058745339_p51352393205412"></a><a name="en-us_topic_0058745339_p51352393205412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p36554948205412"><a name="en-us_topic_0058745339_p36554948205412"></a><a name="en-us_topic_0058745339_p36554948205412"></a>Specifies the time when the ECS was updated last time.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row58340703205341"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p6338506205412"><a name="en-us_topic_0058745339_p6338506205412"></a><a name="en-us_topic_0058745339_p6338506205412"></a>hostId</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p43657009205412"><a name="en-us_topic_0058745339_p43657009205412"></a><a name="en-us_topic_0058745339_p43657009205412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p13004714205412"><a name="en-us_topic_0058745339_p13004714205412"></a><a name="en-us_topic_0058745339_p13004714205412"></a>Specifies the ID of the host on which the ECS is deployed.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row11730016205341"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p18087298205412"><a name="en-us_topic_0058745339_p18087298205412"></a><a name="en-us_topic_0058745339_p18087298205412"></a>addresses</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p55785035205412"><a name="en-us_topic_0058745339_p55785035205412"></a><a name="en-us_topic_0058745339_p55785035205412"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p60985304205412"><a name="en-us_topic_0058745339_p60985304205412"></a><a name="en-us_topic_0058745339_p60985304205412"></a>Specifies the network attribute of the ECS.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row2865349205341"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p32218820205412"><a name="en-us_topic_0058745339_p32218820205412"></a><a name="en-us_topic_0058745339_p32218820205412"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p59587610205412"><a name="en-us_topic_0058745339_p59587610205412"></a><a name="en-us_topic_0058745339_p59587610205412"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p45182573205412"><a name="en-us_topic_0058745339_p45182573205412"></a><a name="en-us_topic_0058745339_p45182573205412"></a>Specifies the description of the ECS.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row12453079205341"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p54752905205412"><a name="en-us_topic_0058745339_p54752905205412"></a><a name="en-us_topic_0058745339_p54752905205412"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p5800295205412"><a name="en-us_topic_0058745339_p5800295205412"></a><a name="en-us_topic_0058745339_p5800295205412"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p5010132205412"><a name="en-us_topic_0058745339_p5010132205412"></a><a name="en-us_topic_0058745339_p5010132205412"></a>Specifies the ECS image information. For the ECS that boots from a volume, the value is left blank.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row40450152205341"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p28507858205412"><a name="en-us_topic_0058745339_p28507858205412"></a><a name="en-us_topic_0058745339_p28507858205412"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p27435137205412"><a name="en-us_topic_0058745339_p27435137205412"></a><a name="en-us_topic_0058745339_p27435137205412"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p15962877205412"><a name="en-us_topic_0058745339_p15962877205412"></a><a name="en-us_topic_0058745339_p15962877205412"></a>Specifies the ECS flavor.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row8503055205341"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p27103976205412"><a name="en-us_topic_0058745339_p27103976205412"></a><a name="en-us_topic_0058745339_p27103976205412"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p47938434205412"><a name="en-us_topic_0058745339_p47938434205412"></a><a name="en-us_topic_0058745339_p47938434205412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p51933601205412"><a name="en-us_topic_0058745339_p51933601205412"></a><a name="en-us_topic_0058745339_p51933601205412"></a>Specifies the ECS ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row13299823205341"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p10195868205412"><a name="en-us_topic_0058745339_p10195868205412"></a><a name="en-us_topic_0058745339_p10195868205412"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p20558988205412"><a name="en-us_topic_0058745339_p20558988205412"></a><a name="en-us_topic_0058745339_p20558988205412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p65814145205412"><a name="en-us_topic_0058745339_p65814145205412"></a><a name="en-us_topic_0058745339_p65814145205412"></a>Specifies the user UUID of the ECS.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row44286797202934"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p28836818203017"><a name="en-us_topic_0058745339_p28836818203017"></a><a name="en-us_topic_0058745339_p28836818203017"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p54080902203017"><a name="en-us_topic_0058745339_p54080902203017"></a><a name="en-us_topic_0058745339_p54080902203017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p20236732203017"><a name="en-us_topic_0058745339_p20236732203017"></a><a name="en-us_topic_0058745339_p20236732203017"></a>Specifies the ECS name.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row26755982202937"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p55736572203017"><a name="en-us_topic_0058745339_p55736572203017"></a><a name="en-us_topic_0058745339_p55736572203017"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p18368516203017"><a name="en-us_topic_0058745339_p18368516203017"></a><a name="en-us_topic_0058745339_p18368516203017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p55424556203017"><a name="en-us_topic_0058745339_p55424556203017"></a><a name="en-us_topic_0058745339_p55424556203017"></a>Specifies the UUID of the tenant who owns the ECS.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row43950511202941"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p4965641203017"><a name="en-us_topic_0058745339_p4965641203017"></a><a name="en-us_topic_0058745339_p4965641203017"></a>OS-DCF:diskConfig</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p66672654203017"><a name="en-us_topic_0058745339_p66672654203017"></a><a name="en-us_topic_0058745339_p66672654203017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p23709405203017"><a name="en-us_topic_0058745339_p23709405203017"></a><a name="en-us_topic_0058745339_p23709405203017"></a>Specifies the diskConfig type. It is an extended attributed.</p>
<a name="en-us_topic_0058745339_ul12058054203017"></a><a name="en-us_topic_0058745339_ul12058054203017"></a><ul id="en-us_topic_0058745339_ul12058054203017"><li><strong id="en-us_topic_0058745339_b19223538"><a name="en-us_topic_0058745339_b19223538"></a><a name="en-us_topic_0058745339_b19223538"></a>MANUAL</strong>: The image space cannot be expanded.</li><li><strong id="en-us_topic_0058745339_b13602746"><a name="en-us_topic_0058745339_b13602746"></a><a name="en-us_topic_0058745339_b13602746"></a>AUTO</strong>: The image space on the system disk will be automatically expanded to keep the same as that set in the flavor.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0058745339_row10229070202944"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p58100889203017"><a name="en-us_topic_0058745339_p58100889203017"></a><a name="en-us_topic_0058745339_p58100889203017"></a>accessIPv4</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p8551536203017"><a name="en-us_topic_0058745339_p8551536203017"></a><a name="en-us_topic_0058745339_p8551536203017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p3622325203017"><a name="en-us_topic_0058745339_p3622325203017"></a><a name="en-us_topic_0058745339_p3622325203017"></a>Discarded</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row35508689202947"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p23429640203017"><a name="en-us_topic_0058745339_p23429640203017"></a><a name="en-us_topic_0058745339_p23429640203017"></a>accessIPv6</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p18752687203017"><a name="en-us_topic_0058745339_p18752687203017"></a><a name="en-us_topic_0058745339_p18752687203017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p25834270203017"><a name="en-us_topic_0058745339_p25834270203017"></a><a name="en-us_topic_0058745339_p25834270203017"></a>Discarded</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row37751476202950"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p42701424203017"><a name="en-us_topic_0058745339_p42701424203017"></a><a name="en-us_topic_0058745339_p42701424203017"></a>progress</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p36263280203017"><a name="en-us_topic_0058745339_p36263280203017"></a><a name="en-us_topic_0058745339_p36263280203017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p22458237203017"><a name="en-us_topic_0058745339_p22458237203017"></a><a name="en-us_topic_0058745339_p22458237203017"></a>Specifies the ECS creation progress.</p>
</td>
</tr>
<tr id="en-us_topic_0058745339_row6638586820302"><td class="cellrowborder" valign="top" width="17.638236176382364%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0058745339_p64601528203017"><a name="en-us_topic_0058745339_p64601528203017"></a><a name="en-us_topic_0058745339_p64601528203017"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="17.14828517148285%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0058745339_p65341292203017"><a name="en-us_topic_0058745339_p65341292203017"></a><a name="en-us_topic_0058745339_p65341292203017"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="65.21347865213478%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0058745339_p12793900203017"><a name="en-us_topic_0058745339_p12793900203017"></a><a name="en-us_topic_0058745339_p12793900203017"></a>Specifies the ECS metadata.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0058745339_section6318101715279"></a>

```
POST https://{endpoint}/v2/{project_id}/servers/{server_id}/action
POST https://{endpoint}/v2.1/{project_id}/servers/{server_id}/action
```

```
{
    "rebuild" : {
        "imageRef" : "3ed456f5-3d8f-4383-a6c9-312032afcd1a",
        "name" : "rebuildName",
       "metadata" : {
            "rebuild" : "rebuild vm"
        }
    }
}
```

## Example Response<a name="section1515353712613"></a>

```
{
    "server": {
        "tenant_id": "7459f9935ed2422eb9800fea1d4d9378",
        "image": {
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://172.30.32.132:443/7459f9935ed2422eb9800fea1d4d9378/images/3ed456f5-3d8f-4383-a6c9-312032afcd1a"
                }
            ],
            "id": "3ed456f5-3d8f-4383-a6c9-312032afcd1a"
        },
        "accessIPv4": "",
        "addresses": {
            "443dd9e3-c165-4764-ad92-b17fcf12a3eb": [
                {
                    "addr": "192.168.0.119",
                    "version": 4
                }
            ]
        },
        "metadata": {
            "name": "rebuildName"
        },
        "accessIPv6": "",
        "created": "2016-09-19T01:13:26Z",
        "hostId": "fd16ebd9c2629e8595875cc1e1400fa67f392431d7937fcc9cf37671",
        "adminPass": "qGVjnEjY3ZoY",
        "flavor": {
            "links": [
                {
                    "rel": "bookmark",
                    "href": "https://172.30.32.132:443/7459f9935ed2422eb9800fea1d4d9378/flavors/normal1"
                }
            ],
            "id": "normal1"
        },
        "OS-DCF:diskConfig": "MANUAL",
        "user_id": "ed2965d80d394be0b41e56f50ac650ca",
        "name": "rebuildName",
        "progress": 0,
        "links": [
            {
                "rel": "self",
                "href": "https://172.30.32.132:443/v2/7459f9935ed2422eb9800fea1d4d9378/servers/ea681a24-9b24-4f49-98ef-8e1f73acf19e"
            },
            {
                "rel": "bookmark",
                "href": "https://172.30.32.132:443/7459f9935ed2422eb9800fea1d4d9378/servers/ea681a24-9b24-4f49-98ef-8e1f73acf19e"
            }
        ],
        "id": "ea681a24-9b24-4f49-98ef-8e1f73acf19e",
        "updated": "2016-09-19T07:22:05Z",
        "status": "REBUILD"
    }
}
```

## Returned Values<a name="en-us_topic_0058745339_section128741313191616"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

