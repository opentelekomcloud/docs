# Querying Details of an AS Policy \(V2\)<a name="EN-US_TOPIC_0103010243"></a>

## Function<a name="section16272157227"></a>

This interface is used to query details about a specified AS policy by policy ID.

The difference between the V2 and V1 interfaces for querying details of an AS policy is that V2 contains scaling resource types in response messages.

## URI<a name="section1057514299222"></a>

GET /autoscaling-api/v2/\{project\_id\}/scaling\_policy/\{scaling\_policy\_id\}

**Table  1**  Parameter description

<a name="table18577192913227"></a>
<table><thead align="left"><tr id="row460813297221"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.1"><p id="p56081829132215"><a name="p56081829132215"></a><a name="p56081829132215"></a><strong id="b98281234175817"><a name="b98281234175817"></a><a name="b98281234175817"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p66081294222"><a name="p66081294222"></a><a name="p66081294222"></a><strong id="b842352706141528"><a name="b842352706141528"></a><a name="b842352706141528"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.3"><p id="p66084294228"><a name="p66084294228"></a><a name="p66084294228"></a><strong id="b84235270693914"><a name="b84235270693914"></a><a name="b84235270693914"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38%" id="mcps1.2.5.1.4"><p id="p1460832962213"><a name="p1460832962213"></a><a name="p1460832962213"></a><strong id="b6221937115820"><a name="b6221937115820"></a><a name="b6221937115820"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row136081329112212"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p196081629142213"><a name="p196081629142213"></a><a name="p196081629142213"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p12608129142214"><a name="p12608129142214"></a><a name="p12608129142214"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p66081029162214"><a name="p66081029162214"></a><a name="p66081029162214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row2608152902220"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p66086295221"><a name="p66086295221"></a><a name="p66086295221"></a>scaling_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p126087293225"><a name="p126087293225"></a><a name="p126087293225"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p17608029132210"><a name="p17608029132210"></a><a name="p17608029132210"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.4 "><p id="p13608929102216"><a name="p13608929102216"></a><a name="p13608929102216"></a>Specifies the AS policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section15620184022220"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query details about the AS policy with ID  **906f73ff-56e8-41b2-a005-8157d0c60361**.

    ```
    GET https://{Endpoint}/autoscaling-api/v2/{project_id}/scaling_policy/906f73ff-56e8-41b2-a005-8157d0c60361
    ```


## Response Message<a name="section271118558221"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table16716175516228"></a>
    <table><thead align="left"><tr id="row1568568220"><th class="cellrowborder" valign="top" width="26.507349265073493%" id="mcps1.2.4.1.1"><p id="p7795617226"><a name="p7795617226"></a><a name="p7795617226"></a><strong id="b194321438185819"><a name="b194321438185819"></a><a name="b194321438185819"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.44815518448155%" id="mcps1.2.4.1.2"><p id="p27456142215"><a name="p27456142215"></a><a name="p27456142215"></a><strong id="b690704614"><a name="b690704614"></a><a name="b690704614"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.04449555044495%" id="mcps1.2.4.1.3"><p id="p127115632214"><a name="p127115632214"></a><a name="p127115632214"></a><strong id="b4305143925815"><a name="b4305143925815"></a><a name="b4305143925815"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row87175622210"><td class="cellrowborder" valign="top" width="26.507349265073493%" headers="mcps1.2.4.1.1 "><p id="p11795622215"><a name="p11795622215"></a><a name="p11795622215"></a>scaling_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.44815518448155%" headers="mcps1.2.4.1.2 "><p id="a4c03d226ca78442f99e13b8d363cd51d"><a name="a4c03d226ca78442f99e13b8d363cd51d"></a><a name="a4c03d226ca78442f99e13b8d363cd51d"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.04449555044495%" headers="mcps1.2.4.1.3 "><p id="p671556172214"><a name="p671556172214"></a><a name="p671556172214"></a>Specifies details about the AS policy. For details, see <a href="#table10729655182210">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scaling\_policy**  field description

    <a name="table10729655182210"></a>
    <table><thead align="left"><tr id="row971956152212"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.1"><p id="p5785612215"><a name="p5785612215"></a><a name="p5785612215"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.4.1.2"><p id="p27155612214"><a name="p27155612214"></a><a name="p27155612214"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.1%" id="mcps1.2.4.1.3"><p id="p1277568221"><a name="p1277568221"></a><a name="p1277568221"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13885612214"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p08205611223"><a name="p08205611223"></a><a name="p08205611223"></a>scaling_resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p2814561228"><a name="p2814561228"></a><a name="p2814561228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p1481956112219"><a name="p1481956112219"></a><a name="p1481956112219"></a>Specifies the scaling resource ID.</p>
    </td>
    </tr>
    <tr id="row178145692211"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p9875610228"><a name="p9875610228"></a><a name="p9875610228"></a>scaling_resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p168165622218"><a name="p168165622218"></a><a name="p168165622218"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p08156182216"><a name="p08156182216"></a><a name="p08156182216"></a>Specifies the scaling resource type.</p>
    <a name="ul7825614222"></a><a name="ul7825614222"></a><ul id="ul7825614222"><li>AS group: <strong id="b84235270691950"><a name="b84235270691950"></a><a name="b84235270691950"></a>SCALING_GROUP</strong></li><li>Bandwidth: <strong id="b8423527069204"><a name="b8423527069204"></a><a name="b8423527069204"></a>BANDWIDTH</strong></li></ul>
    </td>
    </tr>
    <tr id="row38175619221"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p08115614223"><a name="p08115614223"></a><a name="p08115614223"></a>scaling_policy_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p15865682217"><a name="p15865682217"></a><a name="p15865682217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p5825692211"><a name="p5825692211"></a><a name="p5825692211"></a>Specifies the AS policy name.</p>
    <p id="p121115239911"><a name="p121115239911"></a><a name="p121115239911"></a>Supports fuzzy search. </p>
    </td>
    </tr>
    <tr id="row5818563229"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p48165662211"><a name="p48165662211"></a><a name="p48165662211"></a>scaling_policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p4895612224"><a name="p4895612224"></a><a name="p4895612224"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p128145672211"><a name="p128145672211"></a><a name="p128145672211"></a>Specifies the AS policy ID.</p>
    </td>
    </tr>
    <tr id="row108856172218"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p158105692217"><a name="p158105692217"></a><a name="p158105692217"></a>policy_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p2895614224"><a name="p2895614224"></a><a name="p2895614224"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p118115618226"><a name="p118115618226"></a><a name="p118115618226"></a>Specifies the AS policy status.</p>
    <a name="ul6912561227"></a><a name="ul6912561227"></a><ul id="ul6912561227"><li><strong id="b45761523105018"><a name="b45761523105018"></a><a name="b45761523105018"></a>INSERVICE</strong>: The AS policy is enabled.</li><li><strong id="b17790122516505"><a name="b17790122516505"></a><a name="b17790122516505"></a>PAUSED</strong>: The AS policy is disabled.</li><li><strong id="b842352706171746"><a name="b842352706171746"></a><a name="b842352706171746"></a>EXECUTING</strong>: The AS policy is being executed.</li></ul>
    </td>
    </tr>
    <tr id="row139175613226"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p14925611228"><a name="p14925611228"></a><a name="p14925611228"></a>scaling_policy_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p2935615225"><a name="p2935615225"></a><a name="p2935615225"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p18912563224"><a name="p18912563224"></a><a name="p18912563224"></a>Specifies the AS policy type.</p>
    <a name="ul5935652220"></a><a name="ul5935652220"></a><ul id="ul5935652220"><li><strong>ALARM</strong>: indicates that the scaling action is triggered by an alarm. A value is returned for <strong>alarm_id</strong>, and no value is returned for <strong>scheduled_policy</strong>.</li><li><strong id="b842352706174318"><a name="b842352706174318"></a><a name="b842352706174318"></a>SCHEDULED</strong>: indicates that the scaling action is triggered as scheduled. A value is returned for <strong id="b842352706174359"><a name="b842352706174359"></a><a name="b842352706174359"></a>scheduled_policy</strong>, and no value is returned for <strong id="b842352706174456"><a name="b842352706174456"></a><a name="b842352706174456"></a>alarm_id</strong>, <strong id="b84235270617451"><a name="b84235270617451"></a><a name="b84235270617451"></a>recurrence_type</strong>, <strong id="b84235270617457"><a name="b84235270617457"></a><a name="b84235270617457"></a>recurrence_value</strong>, <strong id="b842352706174512"><a name="b842352706174512"></a><a name="b842352706174512"></a>start_time</strong>, or <strong id="b842352706174516"><a name="b842352706174516"></a><a name="b842352706174516"></a>end_time</strong>.</li><li><strong id="b1896012950"><a name="b1896012950"></a><a name="b1896012950"></a>RECURRENCE</strong>: indicates that the scaling action is triggered periodically. Values are returned for <strong id="b118374559"><a name="b118374559"></a><a name="b118374559"></a>scheduled_policy</strong>, <strong id="b1121671907174638"><a name="b1121671907174638"></a><a name="b1121671907174638"></a>recurrence_type</strong>, <strong id="b413073752174638"><a name="b413073752174638"></a><a name="b413073752174638"></a>recurrence_value</strong>, <strong id="b1481332545174638"><a name="b1481332545174638"></a><a name="b1481332545174638"></a>start_time</strong>, and <strong id="b331387069174638"><a name="b331387069174638"></a><a name="b331387069174638"></a>end_time</strong>, and no value is returned for <strong id="b809583280"><a name="b809583280"></a><a name="b809583280"></a>alarm_id</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row9917562220"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p18915692212"><a name="p18915692212"></a><a name="p18915692212"></a>alarm_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p15913563226"><a name="p15913563226"></a><a name="p15913563226"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p14995642215"><a name="p14995642215"></a><a name="p14995642215"></a>Specifies the alarm ID.</p>
    </td>
    </tr>
    <tr id="row139135616226"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p091956172215"><a name="p091956172215"></a><a name="p091956172215"></a>scheduled_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p192973114432"><a name="p192973114432"></a><a name="p192973114432"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p1891456122210"><a name="p1891456122210"></a><a name="p1891456122210"></a>Specifies the periodic or scheduled AS policy. For details, see <a href="#table179725552211">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row89556122216"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p10995610224"><a name="p10995610224"></a><a name="p10995610224"></a>scaling_policy_action</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p1617315359431"><a name="p1617315359431"></a><a name="p1617315359431"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p1710155610222"><a name="p1710155610222"></a><a name="p1710155610222"></a>Specifies the scaling action of the AS policy. For details, see <a href="#table483105512229">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row210556142211"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p610185652215"><a name="p610185652215"></a><a name="p610185652215"></a>cool_down_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p1110756102219"><a name="p1110756102219"></a><a name="p1110756102219"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p1510156162210"><a name="p1510156162210"></a><a name="p1510156162210"></a>Specifies the cooldown period (s).</p>
    </td>
    </tr>
    <tr id="row19101556112214"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p810175619222"><a name="p810175619222"></a><a name="p810175619222"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p1210115611229"><a name="p1210115611229"></a><a name="p1210115611229"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p21014567224"><a name="p21014567224"></a><a name="p21014567224"></a>Specifies the time when an AS policy was created. The time format complies with UTC.</p>
    </td>
    </tr>
    <tr id="row8280367175820"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p65915113175834"><a name="p65915113175834"></a><a name="p65915113175834"></a>meta_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p1011216376436"><a name="p1011216376436"></a><a name="p1011216376436"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p41667816175834"><a name="p41667816175834"></a><a name="p41667816175834"></a>Provides additional information. For details, see <a href="#table14568680175854">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **scheduled\_policy**  field description

    <a name="table179725552211"></a>
    <table><thead align="left"><tr id="row511155632217"><th class="cellrowborder" valign="top" width="26.26%" id="mcps1.2.4.1.1"><p id="p511556192217"><a name="p511556192217"></a><a name="p511556192217"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.2"><p id="p181195611223"><a name="p181195611223"></a><a name="p181195611223"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.559999999999995%" id="mcps1.2.4.1.3"><p id="p811195610228"><a name="p811195610228"></a><a name="p811195610228"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1811175662215"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p91125617222"><a name="p91125617222"></a><a name="p91125617222"></a>launch_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p16111756162215"><a name="p16111756162215"></a><a name="p16111756162215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p191175610221"><a name="p191175610221"></a><a name="p191175610221"></a>Specifies the time when the scaling action is triggered. The time format complies with UTC.</p>
    <a name="ul41112567221"></a><a name="ul41112567221"></a><ul id="ul41112567221"><li>If <strong>scaling_policy_type</strong> is set to <strong>SCHEDULED</strong>, the time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</li><li>If <strong>scaling_policy_type</strong> is set to <strong>RECURRENCE</strong>, the time format is <strong>hh:mm</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row91175618225"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p1411155662212"><a name="p1411155662212"></a><a name="p1411155662212"></a>recurrence_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1611205612226"><a name="p1611205612226"></a><a name="p1611205612226"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p0110564224"><a name="p0110564224"></a><a name="p0110564224"></a>Specifies the type of a periodically triggered scaling action.</p>
    <a name="ul750792918211"></a><a name="ul750792918211"></a><ul id="ul750792918211"><li><strong>Daily</strong>: indicates that the scaling action is triggered once a day.</li><li><strong>Weekly</strong>: indicates that the scaling action is triggered once a week.</li><li><strong>Monthly</strong>: indicates that the scaling action is triggered once a month.</li></ul>
    </td>
    </tr>
    <tr id="row16141569226"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p181417563221"><a name="p181417563221"></a><a name="p181417563221"></a>recurrence_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p2014125632212"><a name="p2014125632212"></a><a name="p2014125632212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p2014956162216"><a name="p2014956162216"></a><a name="p2014956162216"></a>Specifies the frequency at which scaling actions are triggered.</p>
    <a name="ul201465692212"></a><a name="ul201465692212"></a><ul id="ul201465692212"><li>If <strong>recurrence_type</strong> is set to <strong>Daily</strong>, the value is <strong>null</strong>, indicating that the scaling action is triggered once a day.</li><li>If <strong>recurrence_type</strong> is set to <strong>Weekly</strong>, the value ranges from <strong>1</strong> (Sunday) to <strong>7</strong> (Saturday). The digits refer to dates in each week and separated by a comma, such as <strong>1,3,5</strong>.</li><li>If <strong id="b84235270617528"><a name="b84235270617528"></a><a name="b84235270617528"></a>recurrence_type</strong> is set to <strong>Monthly</strong>, the value ranges from <strong>1</strong> to <strong>31</strong>. The digits refer to the dates in each month and separated by a comma, such as <strong>1,10,13,28</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row11445615223"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p13141756172213"><a name="p13141756172213"></a><a name="p13141756172213"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p61485682213"><a name="p61485682213"></a><a name="p61485682213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p215135612216"><a name="p215135612216"></a><a name="p215135612216"></a>Specifies the start time of the scaling action triggered periodically. The time format complies with UTC.</p>
    <p id="p1815185652218"><a name="p1815185652218"></a><a name="p1815185652218"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    <tr id="row15151056142213"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p1615556102211"><a name="p1615556102211"></a><a name="p1615556102211"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p215145642216"><a name="p215145642216"></a><a name="p215145642216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p13151056112217"><a name="p13151056112217"></a><a name="p13151056112217"></a>Specifies the end time of the scaling action triggered periodically. The time format complies with UTC.</p>
    <p id="p71515622217"><a name="p71515622217"></a><a name="p71515622217"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **scaling\_policy\_action**  field description

    <a name="table483105512229"></a>
    <table><thead align="left"><tr id="row1115556162215"><th class="cellrowborder" valign="top" width="26.26%" id="mcps1.2.4.1.1"><p id="p915105622213"><a name="p915105622213"></a><a name="p915105622213"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.2"><p id="p515456122217"><a name="p515456122217"></a><a name="p515456122217"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.559999999999995%" id="mcps1.2.4.1.3"><p id="p415356112219"><a name="p415356112219"></a><a name="p415356112219"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row162375692220"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p0231756162212"><a name="p0231756162212"></a><a name="p0231756162212"></a>operation</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p22385652217"><a name="p22385652217"></a><a name="p22385652217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p102355612220"><a name="p102355612220"></a><a name="p102355612220"></a>Specifies the scaling action.</p>
    <a name="ul193981245217"></a><a name="ul193981245217"></a><ul id="ul193981245217"><li><strong id="b167911758205010"><a name="b167911758205010"></a><a name="b167911758205010"></a>ADD</strong>: indicates adding instances.</li><li><strong id="b84235270692351"><a name="b84235270692351"></a><a name="b84235270692351"></a>REDUCE</strong>: indicates reducing instances.</li><li><strong id="b84235270692418"><a name="b84235270692418"></a><a name="b84235270692418"></a>SET</strong>: indicates setting the number of instances to a specified value.</li></ul>
    </td>
    </tr>
    <tr id="row202355682217"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p2023175692218"><a name="p2023175692218"></a><a name="p2023175692218"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p12232564225"><a name="p12232564225"></a><a name="p12232564225"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p1123556122215"><a name="p1123556122215"></a><a name="p1123556122215"></a>Specifies the operation size.</p>
    </td>
    </tr>
    <tr id="row15231656162219"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p1623205617226"><a name="p1623205617226"></a><a name="p1623205617226"></a>percentage</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p923956192210"><a name="p923956192210"></a><a name="p923956192210"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p4233560223"><a name="p4233560223"></a><a name="p4233560223"></a>Specifies the percentage of instances to be operated.</p>
    </td>
    </tr>
    <tr id="row92314569222"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p6231256202211"><a name="p6231256202211"></a><a name="p6231256202211"></a>limits</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1523195612216"><a name="p1523195612216"></a><a name="p1523195612216"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p524556122214"><a name="p524556122214"></a><a name="p524556122214"></a>Specifies the operation restrictions.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **meta\_data**  field description

    <a name="table14568680175854"></a>
    <table><thead align="left"><tr id="row25036975175854"><th class="cellrowborder" valign="top" width="26.26%" id="mcps1.2.4.1.1"><p id="p4598303175854"><a name="p4598303175854"></a><a name="p4598303175854"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.2"><p id="p36918294175854"><a name="p36918294175854"></a><a name="p36918294175854"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.559999999999995%" id="mcps1.2.4.1.3"><p id="p37591800175854"><a name="p37591800175854"></a><a name="p37591800175854"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15117177175854"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p14729123175854"><a name="p14729123175854"></a><a name="p14729123175854"></a>Additional field key-value pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p52208315175854"><a name="p52208315175854"></a><a name="p52208315175854"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p1015136175854"><a name="p1015136175854"></a><a name="p1015136175854"></a>Specifies the key and value of the metadata.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "scaling_policy": {
               "scaling_policy_id": "906f73ff-56e8-41b2-a005-8157d0c60361",
               "scaling_policy_name": "hth_aspolicy_1",
               "scaling_resource_id": "8ade64b5-d685-40b8-8582-4ce306ea37a6",
               "scaling_resource_type": "BANDWIDTH",
               "scaling_policy_type": "ALARM",
               "alarm_id": "al1513822380493GvlJKZwA8",
               "scheduled_policy": {
               },
               "cool_down_time": 900,
               "scaling_policy_action": {
                      "operation": "ADD",
                      "size": 1,
                      "limits": 111
               },
               "policy_status": "INSERVICE",
               "create_time": "2018-03-21T08:03:35Z",
               "meta_data": {
                   "metadata_eip_id": "263f0886-de6a-4e21-ad83-814ca9f3844e",
                   "metadata_eip_address": "255.255.255.255"
               }
        }
    }
    ```


## Returned Values<a name="section15837125411231"></a>

-   Normal

    200

-   Abnormal

    <a name="table744011712248"></a>
    <table><thead align="left"><tr id="row1352312178246"><th class="cellrowborder" valign="top" width="43.69%" id="mcps1.1.3.1.1"><p id="p12523121792413"><a name="p12523121792413"></a><a name="p12523121792413"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.31%" id="mcps1.1.3.1.2"><p id="p15523161782415"><a name="p15523161782415"></a><a name="p15523161782415"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19523417112410"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p1252361713241"><a name="p1252361713241"></a><a name="p1252361713241"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p5523101719246"><a name="p5523101719246"></a><a name="p5523101719246"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row1552315172245"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p852311171245"><a name="p852311171245"></a><a name="p852311171245"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p052312177248"><a name="p052312177248"></a><a name="p052312177248"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row952311179244"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p1523141732417"><a name="p1523141732417"></a><a name="p1523141732417"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p18523817162419"><a name="p18523817162419"></a><a name="p18523817162419"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row5523111714248"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p352481762417"><a name="p352481762417"></a><a name="p352481762417"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p75248171241"><a name="p75248171241"></a><a name="p75248171241"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row7524417132417"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p25241517122412"><a name="p25241517122412"></a><a name="p25241517122412"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p652412175245"><a name="p652412175245"></a><a name="p652412175245"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row1524917152411"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p45241517132413"><a name="p45241517132413"></a><a name="p45241517132413"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p75241117112413"><a name="p75241117112413"></a><a name="p75241117112413"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row9524717152413"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p55241917172412"><a name="p55241917172412"></a><a name="p55241917172412"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p7524171710242"><a name="p7524171710242"></a><a name="p7524171710242"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row1052401714244"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p35241817102415"><a name="p35241817102415"></a><a name="p35241817102415"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p752481772418"><a name="p752481772418"></a><a name="p752481772418"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row19524917112410"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p9524191742414"><a name="p9524191742414"></a><a name="p9524191742414"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p15241170241"><a name="p15241170241"></a><a name="p15241170241"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row1524121762417"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p1752421762411"><a name="p1752421762411"></a><a name="p1752421762411"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p2525191719246"><a name="p2525191719246"></a><a name="p2525191719246"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row115259174244"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p65251217122420"><a name="p65251217122420"></a><a name="p65251217122420"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p752571712419"><a name="p752571712419"></a><a name="p752571712419"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row17525217172418"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p145256172247"><a name="p145256172247"></a><a name="p145256172247"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p1752571752412"><a name="p1752571752412"></a><a name="p1752571752412"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row205258179249"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p752591715243"><a name="p752591715243"></a><a name="p752591715243"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p16525131711247"><a name="p16525131711247"></a><a name="p16525131711247"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row4525161716249"><td class="cellrowborder" valign="top" width="43.69%" headers="mcps1.1.3.1.1 "><p id="p1652531714240"><a name="p1652531714240"></a><a name="p1652531714240"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.31%" headers="mcps1.1.3.1.2 "><p id="p10525191702418"><a name="p10525191702418"></a><a name="p10525191702418"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

