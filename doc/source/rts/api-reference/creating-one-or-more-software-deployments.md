# Creating One or More Software Deployments<a name="EN-US_TOPIC_0085277558"></a>

## Function<a name="en-us_topic_0085081135_section5314816"></a>

This API is used to create one or more software deployments.

## URI<a name="en-us_topic_0085081135_section47833347"></a>

POST /v1/\{project\_id\}/software\_deployments

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b127511157512"><a name="b127511157512"></a><a name="b127511157512"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b118241169515"><a name="b118241169515"></a><a name="b118241169515"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b511312331051"><a name="b511312331051"></a><a name="b511312331051"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b3725101014516"><a name="b3725101014516"></a><a name="b3725101014516"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10601725277"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1765464961019"><a name="p1765464961019"></a><a name="p1765464961019"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p0655184916104"><a name="p0655184916104"></a><a name="p0655184916104"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p865694971017"><a name="p865694971017"></a><a name="p865694971017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p13658144921010"><a name="p13658144921010"></a><a name="p13658144921010"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0085081135_section27846943"></a>

<a name="en-us_topic_0085081135_table2851385316"></a>
<table><thead align="left"><tr id="en-us_topic_0085081135_row711513185311"><th class="cellrowborder" valign="top" width="15%" id="mcps1.1.6.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b14951722659"><a name="b14951722659"></a><a name="b14951722659"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.1.6.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b143395247510"><a name="b143395247510"></a><a name="b143395247510"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.1.6.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b317282617519"><a name="b317282617519"></a><a name="b317282617519"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.4"><p id="p18709155145010"><a name="p18709155145010"></a><a name="p18709155145010"></a><strong id="b1224320271259"><a name="b1224320271259"></a><a name="b1224320271259"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.1.6.1.5"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b13519928455"><a name="b13519928455"></a><a name="b13519928455"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0085081135_row416813155310"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081135_p1297955218510"><a name="en-us_topic_0085081135_p1297955218510"></a><a name="en-us_topic_0085081135_p1297955218510"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p4976326232"><a name="p4976326232"></a><a name="p4976326232"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081135_p1297917521051"><a name="en-us_topic_0085081135_p1297917521051"></a><a name="en-us_topic_0085081135_p1297917521051"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081135_p1897925213518"><a name="en-us_topic_0085081135_p1897925213518"></a><a name="en-us_topic_0085081135_p1897925213518"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081135_p14979175211512"><a name="en-us_topic_0085081135_p14979175211512"></a><a name="en-us_topic_0085081135_p14979175211512"></a>Specifies the stack action that triggers this software deployment.</p>
</td>
</tr>
<tr id="en-us_topic_0085081135_row1120181355313"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081135_p897916521150"><a name="en-us_topic_0085081135_p897916521150"></a><a name="en-us_topic_0085081135_p897916521150"></a>config_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p6976726235"><a name="p6976726235"></a><a name="p6976726235"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081135_p119797524516"><a name="en-us_topic_0085081135_p119797524516"></a><a name="en-us_topic_0085081135_p119797524516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081135_p29792528519"><a name="en-us_topic_0085081135_p29792528519"></a><a name="en-us_topic_0085081135_p29792528519"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081135_p1497965216519"><a name="en-us_topic_0085081135_p1497965216519"></a><a name="en-us_topic_0085081135_p1497965216519"></a>Specifies the ID of the software configuration running on a server.</p>
</td>
</tr>
<tr id="en-us_topic_0085081135_row65036351657"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081135_p1597975212510"><a name="en-us_topic_0085081135_p1597975212510"></a><a name="en-us_topic_0085081135_p1597975212510"></a>input_values</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p159766262318"><a name="p159766262318"></a><a name="p159766262318"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081135_p11979852557"><a name="en-us_topic_0085081135_p11979852557"></a><a name="en-us_topic_0085081135_p11979852557"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081135_p1598055216518"><a name="en-us_topic_0085081135_p1598055216518"></a><a name="en-us_topic_0085081135_p1598055216518"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081135_p79801052452"><a name="en-us_topic_0085081135_p79801052452"></a><a name="en-us_topic_0085081135_p79801052452"></a>Specifies input data stored in the form of a key-value pair.</p>
</td>
</tr>
<tr id="en-us_topic_0085081135_row1950623518511"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081135_p898018521151"><a name="en-us_topic_0085081135_p898018521151"></a><a name="en-us_topic_0085081135_p898018521151"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p109767261937"><a name="p109767261937"></a><a name="p109767261937"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081135_p19980652959"><a name="en-us_topic_0085081135_p19980652959"></a><a name="en-us_topic_0085081135_p19980652959"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081135_p18980135216519"><a name="en-us_topic_0085081135_p18980135216519"></a><a name="en-us_topic_0085081135_p18980135216519"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081135_p498075210512"><a name="en-us_topic_0085081135_p498075210512"></a><a name="en-us_topic_0085081135_p498075210512"></a>Specifies the ID of the server deployed using the software configuration.</p>
</td>
</tr>
<tr id="en-us_topic_0085081135_row8758114011513"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081135_p149801452154"><a name="en-us_topic_0085081135_p149801452154"></a><a name="en-us_topic_0085081135_p149801452154"></a>stack_user_project_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p16976626734"><a name="p16976626734"></a><a name="p16976626734"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081135_p19801052652"><a name="en-us_topic_0085081135_p19801052652"></a><a name="en-us_topic_0085081135_p19801052652"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081135_p398095210512"><a name="en-us_topic_0085081135_p398095210512"></a><a name="en-us_topic_0085081135_p398095210512"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081135_p1098015525519"><a name="en-us_topic_0085081135_p1098015525519"></a><a name="en-us_topic_0085081135_p1098015525519"></a>Specifies the ID of the authenticated tenant who can perform operations on the deployment resources.</p>
</td>
</tr>
<tr id="en-us_topic_0085081135_row67581940851"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081135_p1498018526512"><a name="en-us_topic_0085081135_p1498018526512"></a><a name="en-us_topic_0085081135_p1498018526512"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p79761126836"><a name="p79761126836"></a><a name="p79761126836"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081135_p14980452656"><a name="en-us_topic_0085081135_p14980452656"></a><a name="en-us_topic_0085081135_p14980452656"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081135_p8980185218516"><a name="en-us_topic_0085081135_p8980185218516"></a><a name="en-us_topic_0085081135_p8980185218516"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081135_p179809521158"><a name="en-us_topic_0085081135_p179809521158"></a><a name="en-us_topic_0085081135_p179809521158"></a>Specifies the status of software deployments. Valid values include <strong id="en-us_topic_0085081138_b842352706153059"><a name="en-us_topic_0085081138_b842352706153059"></a><a name="en-us_topic_0085081138_b842352706153059"></a>COMPLETE</strong>, <strong id="en-us_topic_0085081138_b84235270615313"><a name="en-us_topic_0085081138_b84235270615313"></a><a name="en-us_topic_0085081138_b84235270615313"></a>IN_PROGRESS</strong>, and <strong id="en-us_topic_0085081138_b84235270615318"><a name="en-us_topic_0085081138_b84235270615318"></a><a name="en-us_topic_0085081138_b84235270615318"></a>FAILED</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0085081135_row175854013514"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081135_p1398055214519"><a name="en-us_topic_0085081135_p1398055214519"></a><a name="en-us_topic_0085081135_p1398055214519"></a>status_reason</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.6.1.2 "><p id="p179766268317"><a name="p179766268317"></a><a name="p179766268317"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081135_p1980205216510"><a name="en-us_topic_0085081135_p1980205216510"></a><a name="en-us_topic_0085081135_p1980205216510"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081135_p7980205220514"><a name="en-us_topic_0085081135_p7980205220514"></a><a name="en-us_topic_0085081135_p7980205220514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081135_p898012521750"><a name="en-us_topic_0085081135_p898012521750"></a><a name="en-us_topic_0085081135_p898012521750"></a>Specifies the cause of the software deployment status.</p>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="en-us_topic_0085081135_section49295902"></a>

<a name="table1848113219424"></a>
<table><thead align="left"><tr id="row1448393210428"><th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.5.1.1"><p id="p209321135175813"><a name="p209321135175813"></a><a name="p209321135175813"></a><strong id="b126711633712"><a name="b126711633712"></a><a name="b126711633712"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.950000000000001%" id="mcps1.1.5.1.2"><p id="p11935193518588"><a name="p11935193518588"></a><a name="p11935193518588"></a><strong id="b17669174672"><a name="b17669174672"></a><a name="b17669174672"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.1.5.1.3"><p id="p169381335195816"><a name="p169381335195816"></a><a name="p169381335195816"></a><strong id="b18841155714"><a name="b18841155714"></a><a name="b18841155714"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.5.1.4"><p id="p12943183505814"><a name="p12943183505814"></a><a name="p12943183505814"></a><strong id="b2085982014711"><a name="b2085982014711"></a><a name="b2085982014711"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row16483193216420"><td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.1 "><p id="p134831332154212"><a name="p134831332154212"></a><a name="p134831332154212"></a>software_deployment</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p113191713619"><a name="p113191713619"></a><a name="p113191713619"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="p13483103214428"><a name="p13483103214428"></a><a name="p13483103214428"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.5.1.4 "><p id="p14835328427"><a name="p14835328427"></a><a name="p14835328427"></a>Specifies the software deployment resource object.</p>
</td>
</tr>
</tbody>
</table>

**software\_deployment**  structure information

<a name="en-us_topic_0085081135_table58541283"></a>
<table><thead align="left"><tr id="en-us_topic_0085081135_row14014710"><th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.5.1.1"><p id="p97571939195819"><a name="p97571939195819"></a><a name="p97571939195819"></a><strong id="b7914194219712"><a name="b7914194219712"></a><a name="b7914194219712"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.950000000000001%" id="mcps1.1.5.1.2"><p id="p1876118392588"><a name="p1876118392588"></a><a name="p1876118392588"></a><strong id="b181873445712"><a name="b181873445712"></a><a name="b181873445712"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.1.5.1.3"><p id="p5762113915582"><a name="p5762113915582"></a><a name="p5762113915582"></a><strong id="b1765884510713"><a name="b1765884510713"></a><a name="b1765884510713"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.5.1.4"><p id="p137691396589"><a name="p137691396589"></a><a name="p137691396589"></a><strong id="b11847104614716"><a name="b11847104614716"></a><a name="b11847104614716"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0085081135_row20801079"><td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081135_p11917211970"><a name="en-us_topic_0085081135_p11917211970"></a><a name="en-us_topic_0085081135_p11917211970"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p1970176460"><a name="p1970176460"></a><a name="p1970176460"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081135_p81942119710"><a name="en-us_topic_0085081135_p81942119710"></a><a name="en-us_topic_0085081135_p81942119710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081135_p3192211776"><a name="en-us_topic_0085081135_p3192211776"></a><a name="en-us_topic_0085081135_p3192211776"></a>Specifies the stack action that triggers this software deployment.</p>
</td>
</tr>
<tr id="en-us_topic_0085081135_row20715858"><td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081135_p7192211278"><a name="en-us_topic_0085081135_p7192211278"></a><a name="en-us_topic_0085081135_p7192211278"></a>config_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p16701961263"><a name="p16701961263"></a><a name="p16701961263"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081135_p31982114714"><a name="en-us_topic_0085081135_p31982114714"></a><a name="en-us_topic_0085081135_p31982114714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081135_p12196211974"><a name="en-us_topic_0085081135_p12196211974"></a><a name="en-us_topic_0085081135_p12196211974"></a>Specifies the ID of the software configuration running on a server.</p>
</td>
</tr>
<tr id="en-us_topic_0085081135_row26021030"><td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081135_p194601337675"><a name="en-us_topic_0085081135_p194601337675"></a><a name="en-us_topic_0085081135_p194601337675"></a>creation_time</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p270161168"><a name="p270161168"></a><a name="p270161168"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081135_p2046011371672"><a name="en-us_topic_0085081135_p2046011371672"></a><a name="en-us_topic_0085081135_p2046011371672"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.5.1.4 "><p id="p4953122718227"><a name="p4953122718227"></a><a name="p4953122718227"></a>Specifies the creation time. The timestamp uses the ISO 8601 format:</p>
<pre class="screen" id="screen873823210224"><a name="screen873823210224"></a><a name="screen873823210224"></a>CCYY-MM-DDThh:mm:ss&plusmn;hh:mm</pre>
</td>
</tr>
<tr id="en-us_topic_0085081135_row45386595"><td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081135_p146183718711"><a name="en-us_topic_0085081135_p146183718711"></a><a name="en-us_topic_0085081135_p146183718711"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p989210452075"><a name="p989210452075"></a><a name="p989210452075"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081135_p24610371876"><a name="en-us_topic_0085081135_p24610371876"></a><a name="en-us_topic_0085081135_p24610371876"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081135_p146123714712"><a name="en-us_topic_0085081135_p146123714712"></a><a name="en-us_topic_0085081135_p146123714712"></a>Specifies the software deployment UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0085081135_row23709572"><td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081135_p11461173714717"><a name="en-us_topic_0085081135_p11461173714717"></a><a name="en-us_topic_0085081135_p11461173714717"></a>input_values</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p178965452077"><a name="p178965452077"></a><a name="p178965452077"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081135_p15461937879"><a name="en-us_topic_0085081135_p15461937879"></a><a name="en-us_topic_0085081135_p15461937879"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081135_p746133714711"><a name="en-us_topic_0085081135_p746133714711"></a><a name="en-us_topic_0085081135_p746133714711"></a>Specifies input data stored in the form of a key-value pair.</p>
</td>
</tr>
<tr id="en-us_topic_0085081135_row1676488279"><td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081135_p1746118377716"><a name="en-us_topic_0085081135_p1746118377716"></a><a name="en-us_topic_0085081135_p1746118377716"></a>output_values</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p99009454712"><a name="p99009454712"></a><a name="p99009454712"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081135_p1346116375715"><a name="en-us_topic_0085081135_p1346116375715"></a><a name="en-us_topic_0085081135_p1346116375715"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081135_p746118373714"><a name="en-us_topic_0085081135_p746118373714"></a><a name="en-us_topic_0085081135_p746118373714"></a>Specifies output data stored in the form of a key-value pair.</p>
</td>
</tr>
<tr id="en-us_topic_0085081135_row876414818717"><td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081135_p5461637576"><a name="en-us_topic_0085081135_p5461637576"></a><a name="en-us_topic_0085081135_p5461637576"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p1590374519714"><a name="p1590374519714"></a><a name="p1590374519714"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081135_p94622037278"><a name="en-us_topic_0085081135_p94622037278"></a><a name="en-us_topic_0085081135_p94622037278"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081135_p14622371976"><a name="en-us_topic_0085081135_p14622371976"></a><a name="en-us_topic_0085081135_p14622371976"></a>Specifies the server ID.</p>
</td>
</tr>
<tr id="en-us_topic_0085081135_row576428579"><td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081135_p104624371376"><a name="en-us_topic_0085081135_p104624371376"></a><a name="en-us_topic_0085081135_p104624371376"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p159062458715"><a name="p159062458715"></a><a name="p159062458715"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081135_p44629372717"><a name="en-us_topic_0085081135_p44629372717"></a><a name="en-us_topic_0085081135_p44629372717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081135_p14621637271"><a name="en-us_topic_0085081135_p14621637271"></a><a name="en-us_topic_0085081135_p14621637271"></a>Specifies the status of software deployments. Valid values include <strong id="b122065266819"><a name="b122065266819"></a><a name="b122065266819"></a>COMPLETE</strong>, <strong id="b1620713261810"><a name="b1620713261810"></a><a name="b1620713261810"></a>IN_PROGRESS</strong>, and <strong id="b520813267812"><a name="b520813267812"></a><a name="b520813267812"></a>FAILED</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0085081135_row17648812714"><td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081135_p446217371712"><a name="en-us_topic_0085081135_p446217371712"></a><a name="en-us_topic_0085081135_p446217371712"></a>status_reason</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.1.5.1.2 "><p id="p8909545274"><a name="p8909545274"></a><a name="p8909545274"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081135_p20462337772"><a name="en-us_topic_0085081135_p20462337772"></a><a name="en-us_topic_0085081135_p20462337772"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081135_p04623374717"><a name="en-us_topic_0085081135_p04623374717"></a><a name="en-us_topic_0085081135_p04623374717"></a>Specifies the cause of the software deployment status.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0085081135_section41009935"></a>

```
POST /v1/95d02433133a4c0a87ba6967474a2ad3/software_deployments
{
    "status": "IN_PROGRESS",
    "server_id": "ec14c864-096e-4e27-bb8a-2c2b4dc6f3f5",
    "config_id": "8da95794-2ad9-4979-8ae5-739ce314c5cd",
    "stack_user_project_id": "c024bfada67845ddb17d2b0c0be8cd79",
    "action": "CREATE",
    "status_reason": "Deploy data available"
}
```

## Response Example<a name="en-us_topic_0085081135_section33545101"></a>

```
{
    "software_deployment": {
        "status": "IN_PROGRESS",
        "server_id": "ec14c864-096e-4e27-bb8a-2c2b4dc6f3f5",
        "config_id": "8da95794-2ad9-4979-8ae5-739ce314c5cd",
        "output_values": null,
        "input_values": null,
        "action": "CREATE",
        "status_reason": "Deploy data available",
        "id": "ef422fa5-719a-419e-a10c-72e3a367b0b8",
        "creation_time": "2015-01-31T15:12:36Z"
    }
}
```

## Return Code<a name="en-us_topic_0085081135_section33470456"></a>

**Table  2**  Normal return code

<a name="table01411862119"></a>
<table><thead align="left"><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><strong id="en-us_topic_0084581285_b14910172512114"><a name="en-us_topic_0084581285_b14910172512114"></a><a name="en-us_topic_0084581285_b14910172512114"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a>Request was successful.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table19512103414"></a>
<table><thead align="left"><tr id="row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p129561510144"><a name="p129561510144"></a><a name="p129561510144"></a><strong id="b16201185417820"><a name="b16201185417820"></a><a name="b16201185417820"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p4959810444"><a name="p4959810444"></a><a name="p4959810444"></a><strong id="b32881748483"><a name="b32881748483"></a><a name="b32881748483"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p9959161020418"><a name="p9959161020418"></a><a name="p9959161020418"></a><strong id="b1632515715817"><a name="b1632515715817"></a><a name="b1632515715817"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p896118101840"><a name="p896118101840"></a><a name="p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p1296211015416"><a name="p1296211015416"></a><a name="p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p9963110146"><a name="p9963110146"></a><a name="p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p18134027201912"><a name="p18134027201912"></a><a name="p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p1713419274191"><a name="p1713419274191"></a><a name="p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p11134162718196"><a name="p11134162718196"></a><a name="p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
<tr id="row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p19789174972712"><a name="p19789174972712"></a><a name="p19789174972712"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p779364918272"><a name="p779364918272"></a><a name="p779364918272"></a>Internal Server Error</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p196546319198"><a name="p196546319198"></a><a name="p196546319198"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

