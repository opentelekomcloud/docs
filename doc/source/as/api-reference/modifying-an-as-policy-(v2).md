# Modifying an AS Policy \(V2\)<a name="EN-US_TOPIC_0103010241"></a>

## Function<a name="section162101610131118"></a>

This interface is used to modify a specified AS policy.

The difference between the V2 and V1 interfaces for modifying an AS policy is that V2 supports modifying a scaling resource type.

## URI<a name="section172511349131118"></a>

PUT /autoscaling-api/v2/\{project\_id\}/scaling\_policy/\{scaling\_policy\_id\}

**Table  1**  Parameter description

<a name="table196449220128"></a>
<table><thead align="left"><tr id="row968662121215"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p16686102141210"><a name="p16686102141210"></a><a name="p16686102141210"></a><strong id="b103135717555"><a name="b103135717555"></a><a name="b103135717555"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p116867220122"><a name="p116867220122"></a><a name="p116867220122"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p668614251210"><a name="p668614251210"></a><a name="p668614251210"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p0686026125"><a name="p0686026125"></a><a name="p0686026125"></a><strong id="b12353815550"><a name="b12353815550"></a><a name="b12353815550"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row20686172111219"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p20686626126"><a name="p20686626126"></a><a name="p20686626126"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p156866215123"><a name="p156866215123"></a><a name="p156866215123"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1068612212127"><a name="p1068612212127"></a><a name="p1068612212127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row9686625124"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p26871321123"><a name="p26871321123"></a><a name="p26871321123"></a>scaling_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p1468714215127"><a name="p1468714215127"></a><a name="p1468714215127"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p16871624125"><a name="p16871624125"></a><a name="p16871624125"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p65325544"><a name="p65325544"></a><a name="p65325544"></a>Specifies an AS policy ID. For details, see <a href="querying-as-policies-(v2).md">Querying AS Policies (V2)</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section935221761218"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table1179511327124"></a>
    <table><thead align="left"><tr id="row092313221219"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.5.1.1"><p id="p1292320329126"><a name="p1292320329126"></a><a name="p1292320329126"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.2"><p id="p9923193231211"><a name="p9923193231211"></a><a name="p9923193231211"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.3"><p id="p29231832131217"><a name="p29231832131217"></a><a name="p29231832131217"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.45454545454546%" id="mcps1.2.5.1.4"><p id="p13923203221213"><a name="p13923203221213"></a><a name="p13923203221213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1292315328122"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p15923113215123"><a name="p15923113215123"></a><a name="p15923113215123"></a>scaling_policy_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p15923193216120"><a name="p15923193216120"></a><a name="p15923193216120"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p29231932171213"><a name="p29231932171213"></a><a name="p29231932171213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p52610097"><a name="p52610097"></a><a name="p52610097"></a>Specifies the AS policy name. The name contains only letters, digits, underscores (_), and hyphens (-), and cannot exceed 64 characters.</p>
    </td>
    </tr>
    <tr id="row892314324124"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p129233321127"><a name="p129233321127"></a><a name="p129233321127"></a>scaling_policy_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p792319325121"><a name="p792319325121"></a><a name="p792319325121"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p1292353231210"><a name="p1292353231210"></a><a name="p1292353231210"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p292343251218"><a name="p292343251218"></a><a name="p292343251218"></a>Specifies the AS policy type.</p>
    <a name="ul492363291213"></a><a name="ul492363291213"></a><ul id="ul492363291213"><li><strong id="b8908878154133"><a name="b8908878154133"></a><a name="b8908878154133"></a>ALARM</strong> (corresponding to <strong id="b13071039154133"><a name="b13071039154133"></a><a name="b13071039154133"></a>alarm_id</strong>): indicates that the scaling action is triggered by an alarm.</li><li><strong id="b47749798154133"><a name="b47749798154133"></a><a name="b47749798154133"></a>SCHEDULED</strong> (corresponding to <strong id="b27095003154133"><a name="b27095003154133"></a><a name="b27095003154133"></a>scheduled_policy</strong>): indicates that the scaling action is triggered as scheduled.</li><li><strong id="b48283661154133"><a name="b48283661154133"></a><a name="b48283661154133"></a>RECURRENCE</strong> (corresponding to <strong id="b31899767154133"><a name="b31899767154133"></a><a name="b31899767154133"></a>scheduled_policy</strong>): indicates that the scaling action is triggered periodically.</li></ul>
    </td>
    </tr>
    <tr id="row692411324122"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p1392483218122"><a name="p1392483218122"></a><a name="p1392483218122"></a>scaling_resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p209246327127"><a name="p209246327127"></a><a name="p209246327127"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p12924183221220"><a name="p12924183221220"></a><a name="p12924183221220"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p1692511320121"><a name="p1692511320121"></a><a name="p1692511320121"></a>Specifies the scaling resource ID, which is the ID of a unique AS group or bandwidth.</p>
    </td>
    </tr>
    <tr id="row149261432181211"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p3926232181213"><a name="p3926232181213"></a><a name="p3926232181213"></a>scaling_resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p11926032161216"><a name="p11926032161216"></a><a name="p11926032161216"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p179268324123"><a name="p179268324123"></a><a name="p179268324123"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p89262032131220"><a name="p89262032131220"></a><a name="p89262032131220"></a>Specifies the scaling resource type.</p>
    <a name="ul592653214122"></a><a name="ul592653214122"></a><ul id="ul592653214122"><li>AS group: <strong id="b84235270691950"><a name="b84235270691950"></a><a name="b84235270691950"></a>SCALING_GROUP</strong></li><li>Bandwidth: <strong id="b8423527069204"><a name="b8423527069204"></a><a name="b8423527069204"></a>BANDWIDTH</strong></li></ul>
    </td>
    </tr>
    <tr id="row4926832121212"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p20926183213124"><a name="p20926183213124"></a><a name="p20926183213124"></a>alarm_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p19926132141212"><a name="p19926132141212"></a><a name="p19926132141212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p11926103211210"><a name="p11926103211210"></a><a name="p11926103211210"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p692653216125"><a name="p692653216125"></a><a name="p692653216125"></a>Specifies the alarm rule ID. This parameter is mandatory when <strong id="b842352706153331"><a name="b842352706153331"></a><a name="b842352706153331"></a>scaling_policy_type</strong> is set to <strong id="b842352706153340"><a name="b842352706153340"></a><a name="b842352706153340"></a>ALARM</strong>. After this parameter is specified, the value of <strong id="b842352706153543"><a name="b842352706153543"></a><a name="b842352706153543"></a>scheduled_policy</strong> does not take effect.</p>
    <p id="p129265329129"><a name="p129265329129"></a><a name="p129265329129"></a>After you modify an alarm policy, the system automatically adds an alarm triggering activity of the autoscaling type to the <strong id="b84235270619718"><a name="b84235270619718"></a><a name="b84235270619718"></a>alarm_actions</strong> field in the alarm rule specified by the parameter value.</p>
    <p id="p79261732101214"><a name="p79261732101214"></a><a name="p79261732101214"></a>You can obtain the parameter value by querying Cloud Eye alarm rules. </p>
    </td>
    </tr>
    <tr id="row129261932161214"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p119267328123"><a name="p119267328123"></a><a name="p119267328123"></a>scheduled_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p1592673211217"><a name="p1592673211217"></a><a name="p1592673211217"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="a4c03d226ca78442f99e13b8d363cd51d"><a name="a4c03d226ca78442f99e13b8d363cd51d"></a><a name="a4c03d226ca78442f99e13b8d363cd51d"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p149267329126"><a name="p149267329126"></a><a name="p149267329126"></a>Specifies the periodic or scheduled AS policy. This parameter is mandatory when <strong id="b842352706171742"><a name="b842352706171742"></a><a name="b842352706171742"></a>scaling_policy_type</strong> is set to <strong id="b842352706171747"><a name="b842352706171747"></a><a name="b842352706171747"></a>SCHEDULED</strong> or <strong id="b842352706171752"><a name="b842352706171752"></a><a name="b842352706171752"></a>RECURRENCE</strong>. After this parameter is specified, the value of <strong id="b84235270614268"><a name="b84235270614268"></a><a name="b84235270614268"></a>alarm_id</strong> does not take effect. For details, see <a href="#table412818526127">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row1926183211127"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p3926332111211"><a name="p3926332111211"></a><a name="p3926332111211"></a>scaling_policy_action</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p12926153217121"><a name="p12926153217121"></a><a name="p12926153217121"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p20899186174214"><a name="p20899186174214"></a><a name="p20899186174214"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p7926732101219"><a name="p7926732101219"></a><a name="p7926732101219"></a>Specifies the scaling action of the AS policy. For details, see <a href="#table2418132017131">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row39264322122"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p19926183219126"><a name="p19926183219126"></a><a name="p19926183219126"></a>cool_down_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p12926032121213"><a name="p12926032121213"></a><a name="p12926032121213"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p19263324126"><a name="p19263324126"></a><a name="p19263324126"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p292753214122"><a name="p292753214122"></a><a name="p292753214122"></a>Specifies the cooldown period (in seconds). The value ranges from 0 to 86400.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scheduled\_policy**  field description

    <a name="table412818526127"></a>
    <table><thead align="left"><tr id="row425265215123"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.1"><p id="p15252185210120"><a name="p15252185210120"></a><a name="p15252185210120"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.2"><p id="p2025295291211"><a name="p2025295291211"></a><a name="p2025295291211"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="p17252252141218"><a name="p17252252141218"></a><a name="p17252252141218"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.5.1.4"><p id="p162521352141220"><a name="p162521352141220"></a><a name="p162521352141220"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16252155213129"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p112521052151215"><a name="p112521052151215"></a><a name="p112521052151215"></a>launch_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p162521752191211"><a name="p162521752191211"></a><a name="p162521752191211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p52521052201214"><a name="p52521052201214"></a><a name="p52521052201214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p1025225261220"><a name="p1025225261220"></a><a name="p1025225261220"></a>Specifies the time when the scaling action is triggered. The time format complies with UTC.</p>
    <a name="ul4252652101215"></a><a name="ul4252652101215"></a><ul id="ul4252652101215"><li>If <strong>scaling_policy_type</strong> is set to <strong>SCHEDULED</strong>, the time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</li><li>If <strong>scaling_policy_type</strong> is set to <strong>RECURRENCE</strong>, the time format is <strong>hh:mm</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row16252125271218"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p18252115281210"><a name="p18252115281210"></a><a name="p18252115281210"></a>recurrence_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p72521252181217"><a name="p72521252181217"></a><a name="p72521252181217"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p152521152101214"><a name="p152521152101214"></a><a name="p152521152101214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p7252552111219"><a name="p7252552111219"></a><a name="p7252552111219"></a>Specifies the periodic triggering type. This parameter is mandatory when <strong id="b842352706172110"><a name="b842352706172110"></a><a name="b842352706172110"></a>scaling_policy_type</strong> is set to <strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>RECURRENCE</strong>.</p>
    <a name="ul1470172810520"></a><a name="ul1470172810520"></a><ul id="ul1470172810520"><li><strong>Daily</strong>: indicates that the scaling action is triggered once a day.</li><li><strong>Weekly</strong>: indicates that the scaling action is triggered once a week.</li><li><strong>Monthly</strong>: indicates that the scaling action is triggered once a month.</li></ul>
    </td>
    </tr>
    <tr id="row125285261215"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p1425213524126"><a name="p1425213524126"></a><a name="p1425213524126"></a>recurrence_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p1225265216124"><a name="p1225265216124"></a><a name="p1225265216124"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p225219524124"><a name="p225219524124"></a><a name="p225219524124"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="a07f48cfcdafa4ffd87bba3b4e90c0111"><a name="a07f48cfcdafa4ffd87bba3b4e90c0111"></a><a name="a07f48cfcdafa4ffd87bba3b4e90c0111"></a>Specifies the day when a periodic scaling action is triggered. This parameter is mandatory when <strong id="b1266624155318"><a name="b1266624155318"></a><a name="b1266624155318"></a>scaling_policy_type</strong> is set to <strong id="b4267122417533"><a name="b4267122417533"></a><a name="b4267122417533"></a>RECURRENCE</strong>.</p>
    <a name="ul225285218123"></a><a name="ul225285218123"></a><ul id="ul225285218123"><li>If <strong>recurrence_type</strong> is set to <strong>Daily</strong>, the value is <strong>null</strong>, indicating that the scaling action is triggered once a day.</li><li>If <strong>recurrence_type</strong> is set to <strong>Weekly</strong>, the value ranges from <strong>1</strong> (Sunday) to <strong>7</strong> (Saturday). The digits refer to dates in each week and separated by a comma, such as <strong>1,3,5</strong>.</li><li>If <strong id="b84235270617528"><a name="b84235270617528"></a><a name="b84235270617528"></a>recurrence_type</strong> is set to <strong>Monthly</strong>, the value ranges from <strong>1</strong> to <strong>31</strong>. The digits refer to the dates in each month and separated by a comma, such as <strong>1,10,13,28</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row132532052111211"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p2253135212128"><a name="p2253135212128"></a><a name="p2253135212128"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p142531752171215"><a name="p142531752171215"></a><a name="p142531752171215"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p17253165201214"><a name="p17253165201214"></a><a name="p17253165201214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p1925311523128"><a name="p1925311523128"></a><a name="p1925311523128"></a>Specifies the start time of the scaling action triggered periodically. The time format complies with UTC.</p>
    <p id="p9253952121215"><a name="p9253952121215"></a><a name="p9253952121215"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    <tr id="row525385215128"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p15253135211127"><a name="p15253135211127"></a><a name="p15253135211127"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p925313529121"><a name="p925313529121"></a><a name="p925313529121"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p5253165291219"><a name="p5253165291219"></a><a name="p5253165291219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p52539521129"><a name="p52539521129"></a><a name="p52539521129"></a>Specifies the end time of the scaling action triggered periodically. The time format complies with UTC. This parameter is mandatory when <strong id="b842352706173440"><a name="b842352706173440"></a><a name="b842352706173440"></a>scaling_policy_type</strong> is set to <strong id="b842352706173444"><a name="b842352706173444"></a><a name="b842352706173444"></a>RECURRENCE</strong>.</p>
    <p id="p8253852181215"><a name="p8253852181215"></a><a name="p8253852181215"></a>When the scaling action is triggered periodically, the end time cannot be earlier than the current and start time.</p>
    <p id="p525315211215"><a name="p525315211215"></a><a name="p525315211215"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **scaling\_policy\_action**  field description

    <a name="table2418132017131"></a>
    <table><thead align="left"><tr id="en-us_topic_0103010240_row914933174911"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="en-us_topic_0103010240_p1984914718496"><a name="en-us_topic_0103010240_p1984914718496"></a><a name="en-us_topic_0103010240_p1984914718496"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.2"><p id="en-us_topic_0103010240_p68491047104920"><a name="en-us_topic_0103010240_p68491047104920"></a><a name="en-us_topic_0103010240_p68491047104920"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="en-us_topic_0103010240_p12849747144916"><a name="en-us_topic_0103010240_p12849747144916"></a><a name="en-us_topic_0103010240_p12849747144916"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.45454545454546%" id="mcps1.2.5.1.4"><p id="en-us_topic_0103010240_p98494475496"><a name="en-us_topic_0103010240_p98494475496"></a><a name="en-us_topic_0103010240_p98494475496"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0103010240_row19149123164911"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0103010240_p118491447144918"><a name="en-us_topic_0103010240_p118491447144918"></a><a name="en-us_topic_0103010240_p118491447144918"></a>operation</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0103010240_p12849647124917"><a name="en-us_topic_0103010240_p12849647124917"></a><a name="en-us_topic_0103010240_p12849647124917"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0103010240_p19849164719493"><a name="en-us_topic_0103010240_p19849164719493"></a><a name="en-us_topic_0103010240_p19849164719493"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0103010240_p12849194711498"><a name="en-us_topic_0103010240_p12849194711498"></a><a name="en-us_topic_0103010240_p12849194711498"></a>Specifies the operation to be performed. The default operation is <strong id="en-us_topic_0103010240_b1898710304536"><a name="en-us_topic_0103010240_b1898710304536"></a><a name="en-us_topic_0103010240_b1898710304536"></a>ADD</strong>.<a name="en-us_topic_0103010240_ul627111141476"></a><a name="en-us_topic_0103010240_ul627111141476"></a><ul id="en-us_topic_0103010240_ul627111141476"><li>If <strong id="en-us_topic_0103010240_b13175144944616"><a name="en-us_topic_0103010240_b13175144944616"></a><a name="en-us_topic_0103010240_b13175144944616"></a>scaling_resource_type</strong> is set to <strong id="en-us_topic_0103010240_b1906755154616"><a name="en-us_topic_0103010240_b1906755154616"></a><a name="en-us_topic_0103010240_b1906755154616"></a>SCALING_GROUP</strong>, the following operations are supported:<a name="en-us_topic_0103010240_ul4517141421818"></a><a name="en-us_topic_0103010240_ul4517141421818"></a><ul id="en-us_topic_0103010240_ul4517141421818"><li><strong id="en-us_topic_0103010240_b8423527069234"><a name="en-us_topic_0103010240_b8423527069234"></a><a name="en-us_topic_0103010240_b8423527069234"></a>ADD</strong>: indicates adding instances.</li><li><strong id="en-us_topic_0103010240_b84235270692351"><a name="en-us_topic_0103010240_b84235270692351"></a><a name="en-us_topic_0103010240_b84235270692351"></a>REMOVE/REDUCE</strong>: indicates removing or reducing instances.</li><li><strong id="en-us_topic_0103010240_b84235270692418"><a name="en-us_topic_0103010240_b84235270692418"></a><a name="en-us_topic_0103010240_b84235270692418"></a>SET</strong>: indicates setting the number of instances to a specified value.</li></ul>
    </li><li>If <strong id="en-us_topic_0103010240_b142804917503"><a name="en-us_topic_0103010240_b142804917503"></a><a name="en-us_topic_0103010240_b142804917503"></a>scaling_resource_type</strong> is set to <strong id="en-us_topic_0103010240_b1741712985119"><a name="en-us_topic_0103010240_b1741712985119"></a><a name="en-us_topic_0103010240_b1741712985119"></a>BANDWIDTH</strong>, the following operations are supported:<a name="en-us_topic_0103010240_ul10599126171711"></a><a name="en-us_topic_0103010240_ul10599126171711"></a><ul id="en-us_topic_0103010240_ul10599126171711"><li><strong id="en-us_topic_0103010240_b643951612511"><a name="en-us_topic_0103010240_b643951612511"></a><a name="en-us_topic_0103010240_b643951612511"></a>ADD</strong>: indicates adding instances.</li><li><strong id="en-us_topic_0103010240_b190727587"><a name="en-us_topic_0103010240_b190727587"></a><a name="en-us_topic_0103010240_b190727587"></a>REDUCE</strong>: indicates reducing instances.</li><li><strong id="en-us_topic_0103010240_b410655124"><a name="en-us_topic_0103010240_b410655124"></a><a name="en-us_topic_0103010240_b410655124"></a>SET</strong>: indicates setting the number of instances to a specified value.</li></ul>
    </li></ul>
    </div>
    </td>
    </tr>
    <tr id="en-us_topic_0103010240_row8149143119496"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0103010240_p484914764910"><a name="en-us_topic_0103010240_p484914764910"></a><a name="en-us_topic_0103010240_p484914764910"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0103010240_p208491947124912"><a name="en-us_topic_0103010240_p208491947124912"></a><a name="en-us_topic_0103010240_p208491947124912"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0103010240_p5849247124914"><a name="en-us_topic_0103010240_p5849247124914"></a><a name="en-us_topic_0103010240_p5849247124914"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0103010240_p18849194784912"><a name="en-us_topic_0103010240_p18849194784912"></a><a name="en-us_topic_0103010240_p18849194784912"></a>Specifies the operation size. The value is an integer from 0 to 300. The default value is <strong id="en-us_topic_0103010240_b11732181112413"><a name="en-us_topic_0103010240_b11732181112413"></a><a name="en-us_topic_0103010240_b11732181112413"></a>1</strong>. This parameter can be set to <strong id="en-us_topic_0103010240_b5635125912547"><a name="en-us_topic_0103010240_b5635125912547"></a><a name="en-us_topic_0103010240_b5635125912547"></a>0</strong> only when <strong id="en-us_topic_0103010240_b9320322105511"><a name="en-us_topic_0103010240_b9320322105511"></a><a name="en-us_topic_0103010240_b9320322105511"></a>operation</strong> is set to <strong id="en-us_topic_0103010240_b196421525125513"><a name="en-us_topic_0103010240_b196421525125513"></a><a name="en-us_topic_0103010240_b196421525125513"></a>SET</strong>.</p>
    <a name="en-us_topic_0103010240_ul1883910551366"></a><a name="en-us_topic_0103010240_ul1883910551366"></a><ul id="en-us_topic_0103010240_ul1883910551366"><li>If <strong>scaling_resource_type</strong> is set to <strong>SCALING_GROUP</strong>, this parameter indicates the number of instances. The value is an integer from 0 to 300 and the default value is <strong>1</strong>.</li><li>If <strong>scaling_resource_type</strong> is set to <strong>BANDWIDTH</strong>, this parameter indicates the bandwidth (Mbit/s). The value is an integer from 1 to 300 and the default value is <strong>1</strong>.</li><li>If <strong id="en-us_topic_0103010240_b8423527061619"><a name="en-us_topic_0103010240_b8423527061619"></a><a name="en-us_topic_0103010240_b8423527061619"></a>scaling_resource_type</strong> is set to <strong id="en-us_topic_0103010240_b84235270616122"><a name="en-us_topic_0103010240_b84235270616122"></a><a name="en-us_topic_0103010240_b84235270616122"></a>SCALING_GROUP</strong>, either <strong id="en-us_topic_0103010240_b842352706105430"><a name="en-us_topic_0103010240_b842352706105430"></a><a name="en-us_topic_0103010240_b842352706105430"></a>size</strong> or <strong id="en-us_topic_0103010240_b842352706105435"><a name="en-us_topic_0103010240_b842352706105435"></a><a name="en-us_topic_0103010240_b842352706105435"></a>percentage</strong> can be set.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0103010240_row16150133114912"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0103010240_p184984724914"><a name="en-us_topic_0103010240_p184984724914"></a><a name="en-us_topic_0103010240_p184984724914"></a>percentage</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0103010240_p785044715492"><a name="en-us_topic_0103010240_p785044715492"></a><a name="en-us_topic_0103010240_p785044715492"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0103010240_p178501847124913"><a name="en-us_topic_0103010240_p178501847124913"></a><a name="en-us_topic_0103010240_p178501847124913"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0103010240_p38501247184913"><a name="en-us_topic_0103010240_p38501247184913"></a><a name="en-us_topic_0103010240_p38501247184913"></a>Specifies the percentage of instances to be operated. If <strong id="en-us_topic_0103010240_b16372183920211"><a name="en-us_topic_0103010240_b16372183920211"></a><a name="en-us_topic_0103010240_b16372183920211"></a>operation</strong> is set to <strong id="en-us_topic_0103010240_b1037363917217"><a name="en-us_topic_0103010240_b1037363917217"></a><a name="en-us_topic_0103010240_b1037363917217"></a>ADD</strong>, <strong id="en-us_topic_0103010240_b11642163516565"><a name="en-us_topic_0103010240_b11642163516565"></a><a name="en-us_topic_0103010240_b11642163516565"></a>REMOVE</strong>, or <strong id="en-us_topic_0103010240_b1237543912118"><a name="en-us_topic_0103010240_b1237543912118"></a><a name="en-us_topic_0103010240_b1237543912118"></a>REDUCE</strong>, the value of this parameter is an integer from 1 to 20000. If <strong id="en-us_topic_0103010240_b13375939102115"><a name="en-us_topic_0103010240_b13375939102115"></a><a name="en-us_topic_0103010240_b13375939102115"></a>operation</strong> is set to <strong id="en-us_topic_0103010240_b23771239132117"><a name="en-us_topic_0103010240_b23771239132117"></a><a name="en-us_topic_0103010240_b23771239132117"></a>SET</strong>, the value is an integer from 0 to 20000.</p>
    <a name="en-us_topic_0103010240_ul1740120777"></a><a name="en-us_topic_0103010240_ul1740120777"></a><ul id="en-us_topic_0103010240_ul1740120777"><li>If <strong id="en-us_topic_0103010240_b84235270616313"><a name="en-us_topic_0103010240_b84235270616313"></a><a name="en-us_topic_0103010240_b84235270616313"></a>scaling_resource_type</strong> is set to <strong id="en-us_topic_0103010240_b84235270616320"><a name="en-us_topic_0103010240_b84235270616320"></a><a name="en-us_topic_0103010240_b84235270616320"></a>SCALING_GROUP</strong>, either <strong id="en-us_topic_0103010240_b190074049516530"><a name="en-us_topic_0103010240_b190074049516530"></a><a name="en-us_topic_0103010240_b190074049516530"></a>size</strong> or <strong id="en-us_topic_0103010240_b35265935816530"><a name="en-us_topic_0103010240_b35265935816530"></a><a name="en-us_topic_0103010240_b35265935816530"></a>percentage</strong> can be set. If neither <strong id="en-us_topic_0103010240_b84235270616550"><a name="en-us_topic_0103010240_b84235270616550"></a><a name="en-us_topic_0103010240_b84235270616550"></a>size</strong> nor <strong id="en-us_topic_0103010240_b84235270616556"><a name="en-us_topic_0103010240_b84235270616556"></a><a name="en-us_topic_0103010240_b84235270616556"></a>percentage</strong> is set, the default value of <strong id="en-us_topic_0103010240_b8423527061667"><a name="en-us_topic_0103010240_b8423527061667"></a><a name="en-us_topic_0103010240_b8423527061667"></a>size</strong> is <strong id="en-us_topic_0103010240_b84235270616612"><a name="en-us_topic_0103010240_b84235270616612"></a><a name="en-us_topic_0103010240_b84235270616612"></a>1</strong>.</li><li>If <strong id="en-us_topic_0103010240_b7913672816"><a name="en-us_topic_0103010240_b7913672816"></a><a name="en-us_topic_0103010240_b7913672816"></a>scaling_resource_type</strong> is set to <strong id="en-us_topic_0103010240_b0590640112810"><a name="en-us_topic_0103010240_b0590640112810"></a><a name="en-us_topic_0103010240_b0590640112810"></a>BANDWIDTH</strong>, <strong id="en-us_topic_0103010240_b51941644192810"><a name="en-us_topic_0103010240_b51941644192810"></a><a name="en-us_topic_0103010240_b51941644192810"></a>percentage</strong> is unavailable.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0103010240_row2150173194911"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0103010240_p4850347164914"><a name="en-us_topic_0103010240_p4850347164914"></a><a name="en-us_topic_0103010240_p4850347164914"></a>limits</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0103010240_p4850547184915"><a name="en-us_topic_0103010240_p4850547184915"></a><a name="en-us_topic_0103010240_p4850547184915"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0103010240_p385004711497"><a name="en-us_topic_0103010240_p385004711497"></a><a name="en-us_topic_0103010240_p385004711497"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0103010240_p11850647164919"><a name="en-us_topic_0103010240_p11850647164919"></a><a name="en-us_topic_0103010240_p11850647164919"></a>Specifies the operation restrictions.</p>
    <p id="en-us_topic_0103010240_p1785064744911"><a name="en-us_topic_0103010240_p1785064744911"></a><a name="en-us_topic_0103010240_p1785064744911"></a>If <strong id="en-us_topic_0103010240_b172916117291"><a name="en-us_topic_0103010240_b172916117291"></a><a name="en-us_topic_0103010240_b172916117291"></a>scaling_resource_type</strong> is set to <strong id="en-us_topic_0103010240_b172949118294"><a name="en-us_topic_0103010240_b172949118294"></a><a name="en-us_topic_0103010240_b172949118294"></a>BANDWIDTH</strong> and <strong id="en-us_topic_0103010240_b129451172919"><a name="en-us_topic_0103010240_b129451172919"></a><a name="en-us_topic_0103010240_b129451172919"></a>operation</strong> is not <strong id="en-us_topic_0103010240_b2029515172914"><a name="en-us_topic_0103010240_b2029515172914"></a><a name="en-us_topic_0103010240_b2029515172914"></a>SET</strong>, this parameter takes effect and the unit is Mbit/s.</p>
    <a name="en-us_topic_0103010240_ul19875103016377"></a><a name="en-us_topic_0103010240_ul19875103016377"></a><ul id="en-us_topic_0103010240_ul19875103016377"><li>If <strong id="en-us_topic_0103010240_b11433157115"><a name="en-us_topic_0103010240_b11433157115"></a><a name="en-us_topic_0103010240_b11433157115"></a>operation</strong> is set to <strong id="en-us_topic_0103010240_b1414531516119"><a name="en-us_topic_0103010240_b1414531516119"></a><a name="en-us_topic_0103010240_b1414531516119"></a>ADD</strong>, this parameter indicates the maximum bandwidth allowed.</li><li>If <strong>operation</strong> is set to <strong>REDUCE</strong>, this parameter indicates the minimum bandwidth allowed.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    This example shows how to modify an AS policy with ID  **0h327883-324n-4dzd-9c61-68d03ee191dd**. The modification is as follows: The AS policy name is changed to  **hth\_aspolicy\_1**; the alarm ID is changed to  **al1513822380493GvlJKZwA8**; the cooldown period is changed to 900 seconds; the policy execution action is to add a bandwidth of 1 Mbit/s until the bandwidth reaches 10 Mbit/s.

    ```
    PUT https://{Endpoint}/autoscaling-api/v2/{project_id}/scaling_policy/0h327883-324n-4dzd-9c61-68d03ee191dd
    
    {
        "alarm_id": "al1513822380493GvlJKZwA8",
        "cool_down_time": 900,
        "scaling_policy_action": {
               "size": 1,
               "operation": "ADD",
               "limits": 10
        },
        "scaling_policy_name": "hth_aspolicy_1",
        "scaling_policy_type": "ALARM"
    }
    ```


## Response Message<a name="section1537864501420"></a>

-   Response parameters

    **Table  5**  Response parameters

    <a name="table546316312154"></a>
    <table><thead align="left"><tr id="row194905318158"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p13490133112156"><a name="p13490133112156"></a><a name="p13490133112156"></a><strong id="b66531816105520"><a name="b66531816105520"></a><a name="b66531816105520"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p14490193171515"><a name="p14490193171515"></a><a name="p14490193171515"></a><strong id="b84235270693914"><a name="b84235270693914"></a><a name="b84235270693914"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52%" id="mcps1.2.4.1.3"><p id="p8490183118158"><a name="p8490183118158"></a><a name="p8490183118158"></a><strong id="b817691818558"><a name="b817691818558"></a><a name="b817691818558"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row74906318156"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p19490193181518"><a name="p19490193181518"></a><a name="p19490193181518"></a>scaling_policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p149018313154"><a name="p149018313154"></a><a name="p149018313154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p17490113112150"><a name="p17490113112150"></a><a name="p17490113112150"></a>Specifies the AS policy ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    { 
         "scaling_policy_id": "0h327883-324n-4dzd-9c61-68d03ee191dd"  
    }
    ```


## Returned Values<a name="section18212125191619"></a>

-   Normal

    200

-   Abnormal

    <a name="table1658372311162"></a>
    <table><thead align="left"><tr id="row5658132331619"><th class="cellrowborder" valign="top" width="35%" id="mcps1.1.3.1.1"><p id="p1465862381619"><a name="p1465862381619"></a><a name="p1465862381619"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.1.3.1.2"><p id="p96595234168"><a name="p96595234168"></a><a name="p96595234168"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8659523101612"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p865952319161"><a name="p865952319161"></a><a name="p865952319161"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p665982318164"><a name="p665982318164"></a><a name="p665982318164"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row106596233164"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p26591123201618"><a name="p26591123201618"></a><a name="p26591123201618"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p36599231160"><a name="p36599231160"></a><a name="p36599231160"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row36592023151610"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p465917233169"><a name="p465917233169"></a><a name="p465917233169"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p065962317161"><a name="p065962317161"></a><a name="p065962317161"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1565920239163"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p1365942315167"><a name="p1365942315167"></a><a name="p1365942315167"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p14659152321616"><a name="p14659152321616"></a><a name="p14659152321616"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row16659323181613"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p96591239161"><a name="p96591239161"></a><a name="p96591239161"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p1265942371615"><a name="p1265942371615"></a><a name="p1265942371615"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row16591123191619"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p12659172381615"><a name="p12659172381615"></a><a name="p12659172381615"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p1365982313169"><a name="p1365982313169"></a><a name="p1365982313169"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row165992317167"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p2659122310166"><a name="p2659122310166"></a><a name="p2659122310166"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p3659162391619"><a name="p3659162391619"></a><a name="p3659162391619"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row1565952316167"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p16599238164"><a name="p16599238164"></a><a name="p16599238164"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p17659152316164"><a name="p17659152316164"></a><a name="p17659152316164"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row565913231168"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p2065914235168"><a name="p2065914235168"></a><a name="p2065914235168"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p1365962341614"><a name="p1365962341614"></a><a name="p1365962341614"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row36591923111619"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p11659623181616"><a name="p11659623181616"></a><a name="p11659623181616"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p196593235163"><a name="p196593235163"></a><a name="p196593235163"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row3659623181619"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p19659182319161"><a name="p19659182319161"></a><a name="p19659182319161"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p36593231168"><a name="p36593231168"></a><a name="p36593231168"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row1166032312164"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p16660102361616"><a name="p16660102361616"></a><a name="p16660102361616"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p76607239160"><a name="p76607239160"></a><a name="p76607239160"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row16601623111615"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p166062341610"><a name="p166062341610"></a><a name="p166062341610"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p1266082371619"><a name="p1266082371619"></a><a name="p1266082371619"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row36603235161"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p9660162301616"><a name="p9660162301616"></a><a name="p9660162301616"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p3660423101617"><a name="p3660423101617"></a><a name="p3660423101617"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

