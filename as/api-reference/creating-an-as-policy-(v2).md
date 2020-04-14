# Creating an AS Policy \(V2\)<a name="EN-US_TOPIC_0103010240"></a>

## Function<a name="section384010584211"></a>

This interface is used to create an AS policy for an AS group or bandwidth.

The difference between the V2 and V1 interfaces for creating an AS policy is that V2 supports creating an AS policy for adjusting bandwidth and differentiating scaling resources by their types.

## URI<a name="section10265184815423"></a>

POST /autoscaling-api/v2/\{project\_id\}/scaling\_policy

**Table  1**  Parameter description

<a name="table169543711435"></a>
<table><thead align="left"><tr id="row13696163774311"><th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.5.1.1"><p id="p1279614712431"><a name="p1279614712431"></a><a name="p1279614712431"></a><strong id="b11494155113536"><a name="b11494155113536"></a><a name="b11494155113536"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.2"><p id="p279694716432"><a name="p279694716432"></a><a name="p279694716432"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.3"><p id="p207961347134317"><a name="p207961347134317"></a><a name="p207961347134317"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.554455445544555%" id="mcps1.2.5.1.4"><p id="p9796647104314"><a name="p9796647104314"></a><a name="p9796647104314"></a><strong id="b1527116529538"><a name="b1527116529538"></a><a name="b1527116529538"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row14696183764311"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.1 "><p id="p879674711433"><a name="p879674711433"></a><a name="p879674711433"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p157961847154317"><a name="p157961847154317"></a><a name="p157961847154317"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p1679634714436"><a name="p1679634714436"></a><a name="p1679634714436"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section2677384410"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table2201101210456"></a>
    <table><thead align="left"><tr id="row12020125459"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p17592192817454"><a name="p17592192817454"></a><a name="p17592192817454"></a><strong id="b124308538536"><a name="b124308538536"></a><a name="b124308538536"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p45921928114511"><a name="p45921928114511"></a><a name="p45921928114511"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p2592132816453"><a name="p2592132816453"></a><a name="p2592132816453"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p559214289456"><a name="p559214289456"></a><a name="p559214289456"></a><strong id="b15272105416537"><a name="b15272105416537"></a><a name="b15272105416537"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52021512204518"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1659213281452"><a name="p1659213281452"></a><a name="p1659213281452"></a>scaling_policy_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p259292814514"><a name="p259292814514"></a><a name="p259292814514"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p9592202874514"><a name="p9592202874514"></a><a name="p9592202874514"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p559262834520"><a name="p559262834520"></a><a name="p559262834520"></a>Specifies the AS policy name. The name contains only letters, digits, underscores (_), and hyphens (-), and cannot exceed 64 characters.</p>
    </td>
    </tr>
    <tr id="row820251216459"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p6592122819459"><a name="p6592122819459"></a><a name="p6592122819459"></a>scaling_resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p125925282456"><a name="p125925282456"></a><a name="p125925282456"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p17592328124517"><a name="p17592328124517"></a><a name="p17592328124517"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1259311288457"><a name="p1259311288457"></a><a name="p1259311288457"></a>Specifies the scaling resource ID, which is the unique ID of an AS group or bandwidth.</p>
    <a name="ul712911394401"></a><a name="ul712911394401"></a><ul id="ul712911394401"><li>If <strong id="b14391174651513"><a name="b14391174651513"></a><a name="b14391174651513"></a>scaling_resource_type</strong> is set to <strong id="b156051651101519"><a name="b156051651101519"></a><a name="b156051651101519"></a>SCALING_GROUP</strong>, this parameter indicates the unique AS group ID.</li><li>If <strong id="b7180161951611"><a name="b7180161951611"></a><a name="b7180161951611"></a>scaling_resource_type</strong> is set to <strong id="b682413238165"><a name="b682413238165"></a><a name="b682413238165"></a>BANDWIDTH</strong>, this parameter indicates the unique bandwidth ID.</li></ul>
    </td>
    </tr>
    <tr id="row17203171294512"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1959342811457"><a name="p1959342811457"></a><a name="p1959342811457"></a>scaling_resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p1459313284450"><a name="p1459313284450"></a><a name="p1459313284450"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p135931928174517"><a name="p135931928174517"></a><a name="p135931928174517"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p759312894514"><a name="p759312894514"></a><a name="p759312894514"></a>Specifies the scaling resource type.</p>
    <a name="ul959382812457"></a><a name="ul959382812457"></a><ul id="ul959382812457"><li>AS group: <strong id="b84235270691950"><a name="b84235270691950"></a><a name="b84235270691950"></a>SCALING_GROUP</strong></li><li>Bandwidth: <strong id="b8423527069204"><a name="b8423527069204"></a><a name="b8423527069204"></a>BANDWIDTH</strong></li></ul>
    </td>
    </tr>
    <tr id="row1720351244514"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p19593228114519"><a name="p19593228114519"></a><a name="p19593228114519"></a>scaling_policy_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p205937286458"><a name="p205937286458"></a><a name="p205937286458"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p185931028174514"><a name="p185931028174514"></a><a name="p185931028174514"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p3593142819452"><a name="p3593142819452"></a><a name="p3593142819452"></a>Specifies the AS policy type.</p>
    <a name="ul14593528184513"></a><a name="ul14593528184513"></a><ul id="ul14593528184513"><li><strong id="b8908878154133"><a name="b8908878154133"></a><a name="b8908878154133"></a>ALARM</strong> (corresponding to <strong id="b13071039154133"><a name="b13071039154133"></a><a name="b13071039154133"></a>alarm_id</strong>): indicates that the scaling action is triggered by an alarm. </li><li><strong id="b47749798154133"><a name="b47749798154133"></a><a name="b47749798154133"></a>SCHEDULED</strong> (corresponding to <strong id="b27095003154133"><a name="b27095003154133"></a><a name="b27095003154133"></a>scheduled_policy</strong>): indicates that the scaling action is triggered as scheduled.</li><li><strong id="b48283661154133"><a name="b48283661154133"></a><a name="b48283661154133"></a>RECURRENCE</strong> (corresponding to <strong id="b31899767154133"><a name="b31899767154133"></a><a name="b31899767154133"></a>scheduled_policy</strong>): indicates that the scaling action is triggered periodically.</li></ul>
    </td>
    </tr>
    <tr id="row52037123452"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p15594112854517"><a name="p15594112854517"></a><a name="p15594112854517"></a>alarm_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p259442834514"><a name="p259442834514"></a><a name="p259442834514"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p125941128194517"><a name="p125941128194517"></a><a name="p125941128194517"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p65945288457"><a name="p65945288457"></a><a name="p65945288457"></a>Specifies the alarm rule ID. This parameter is mandatory when <strong id="b842352706153331"><a name="b842352706153331"></a><a name="b842352706153331"></a>scaling_policy_type</strong> is set to <strong id="b842352706153340"><a name="b842352706153340"></a><a name="b842352706153340"></a>ALARM</strong>. After this parameter is specified, the value of <strong id="b842352706153543"><a name="b842352706153543"></a><a name="b842352706153543"></a>scheduled_policy</strong> does not take effect.</p>
    <p id="p65947283452"><a name="p65947283452"></a><a name="p65947283452"></a>After you create an alarm policy, the system automatically adds an alarm triggering activity of the autoscaling type to the <strong id="b84235270619718"><a name="b84235270619718"></a><a name="b84235270619718"></a>alarm_actions</strong> field in the alarm rule specified by the parameter value.</p>
    <p id="p18594112815454"><a name="p18594112815454"></a><a name="p18594112815454"></a>You can obtain the parameter value by querying Cloud Eye alarm rules. </p>
    </td>
    </tr>
    <tr id="row5203121244518"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p159411286451"><a name="p159411286451"></a><a name="p159411286451"></a>scheduled_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p45941328174510"><a name="p45941328174510"></a><a name="p45941328174510"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="a4c03d226ca78442f99e13b8d363cd51d"><a name="a4c03d226ca78442f99e13b8d363cd51d"></a><a name="a4c03d226ca78442f99e13b8d363cd51d"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1859414287454"><a name="p1859414287454"></a><a name="p1859414287454"></a>Specifies the periodic or scheduled AS policy. This parameter is mandatory when <strong id="b842352706171742"><a name="b842352706171742"></a><a name="b842352706171742"></a>scaling_policy_type</strong> is set to <strong id="b842352706171747"><a name="b842352706171747"></a><a name="b842352706171747"></a>SCHEDULED</strong> or <strong id="b842352706171752"><a name="b842352706171752"></a><a name="b842352706171752"></a>RECURRENCE</strong>. After this parameter is specified, the value of <strong id="b84235270614268"><a name="b84235270614268"></a><a name="b84235270614268"></a>alarm_id</strong> does not take effect. For details, see <a href="#table10424101264616">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row7203121211450"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1059420285454"><a name="p1059420285454"></a><a name="p1059420285454"></a>scaling_policy_action</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p1259402884516"><a name="p1259402884516"></a><a name="p1259402884516"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1574044754119"><a name="p1574044754119"></a><a name="p1574044754119"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p12594528104514"><a name="p12594528104514"></a><a name="p12594528104514"></a>Specifies the scaling action of the AS policy. For details, see <a href="#table14148153113492">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row420381284513"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p759572814455"><a name="p759572814455"></a><a name="p759572814455"></a>cool_down_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p11595172824510"><a name="p11595172824510"></a><a name="p11595172824510"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1459512824515"><a name="p1459512824515"></a><a name="p1459512824515"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p45958289453"><a name="p45958289453"></a><a name="p45958289453"></a>Specifies the cooldown period (in seconds). The value ranges from 0 to 86400 and is 300 by default.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scheduled\_policy**  field description

    <a name="table10424101264616"></a>
    <table><thead align="left"><tr id="row04247128463"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p1436872914616"><a name="p1436872914616"></a><a name="p1436872914616"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p536822910460"><a name="p536822910460"></a><a name="p536822910460"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p12368142912468"><a name="p12368142912468"></a><a name="p12368142912468"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p10368229174610"><a name="p10368229174610"></a><a name="p10368229174610"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row144243125465"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p5368629204611"><a name="p5368629204611"></a><a name="p5368629204611"></a>launch_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p163681629114614"><a name="p163681629114614"></a><a name="p163681629114614"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p33681296461"><a name="p33681296461"></a><a name="p33681296461"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p20368142914465"><a name="p20368142914465"></a><a name="p20368142914465"></a>Specifies the time when the scaling action is triggered. The time format complies with UTC.</p>
    <a name="ul103681229164620"></a><a name="ul103681229164620"></a><ul id="ul103681229164620"><li>If <strong>scaling_policy_type</strong> is set to <strong>SCHEDULED</strong>, the time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</li><li>If <strong>scaling_policy_type</strong> is set to <strong>RECURRENCE</strong>, the time format is <strong>hh:mm</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row0424412154617"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p1736819298466"><a name="p1736819298466"></a><a name="p1736819298466"></a>recurrence_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p2368112913463"><a name="p2368112913463"></a><a name="p2368112913463"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p13368229194611"><a name="p13368229194611"></a><a name="p13368229194611"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p8368429184610"><a name="p8368429184610"></a><a name="p8368429184610"></a>Specifies the periodic triggering type. This parameter is mandatory when <strong id="b842352706172110"><a name="b842352706172110"></a><a name="b842352706172110"></a>scaling_policy_type</strong> is set to <strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>RECURRENCE</strong>.</p>
    <a name="ul863212301573"></a><a name="ul863212301573"></a><ul id="ul863212301573"><li><strong>Daily</strong>: indicates that the scaling action is triggered once a day.</li><li><strong>Weekly</strong>: indicates that the scaling action is triggered once a week.</li><li><strong id="b387417421849"><a name="b387417421849"></a><a name="b387417421849"></a>Monthly</strong>: indicates that the scaling action is triggered once a month.</li></ul>
    </td>
    </tr>
    <tr id="row114247121463"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p13697293462"><a name="p13697293462"></a><a name="p13697293462"></a>recurrence_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p9369152912468"><a name="p9369152912468"></a><a name="p9369152912468"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1369172910462"><a name="p1369172910462"></a><a name="p1369172910462"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="a07f48cfcdafa4ffd87bba3b4e90c0111"><a name="a07f48cfcdafa4ffd87bba3b4e90c0111"></a><a name="a07f48cfcdafa4ffd87bba3b4e90c0111"></a>Specifies the day when a periodic scaling action is triggered. This parameter is mandatory when <strong id="b14071725125218"><a name="b14071725125218"></a><a name="b14071725125218"></a>scaling_policy_type</strong> is set to <strong id="b1840852525212"><a name="b1840852525212"></a><a name="b1840852525212"></a>RECURRENCE</strong>.</p>
    <a name="ul436942914464"></a><a name="ul436942914464"></a><ul id="ul436942914464"><li>If <strong>recurrence_type</strong> is set to <strong>Daily</strong>, the value is <strong>null</strong>, indicating that the scaling action is triggered once a day.</li><li>If <strong>recurrence_type</strong> is set to <strong>Weekly</strong>, the value ranges from <strong>1</strong> (Sunday) to <strong>7</strong> (Saturday). The digits refer to dates in each week and separated by a comma, such as <strong>1,3,5</strong>.</li><li>If <strong id="b84235270617528"><a name="b84235270617528"></a><a name="b84235270617528"></a>recurrence_type</strong> is set to <strong>Monthly</strong>, the value ranges from <strong>1</strong> to <strong>31</strong>. The digits refer to the dates in each month and separated by a comma, such as <strong>1,10,13,28</strong>.<div class="note" id="note1181534852717"><a name="note1181534852717"></a><a name="note1181534852717"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p281624817271"><a name="p281624817271"></a><a name="p281624817271"></a>When <strong id="b2323101020414"><a name="b2323101020414"></a><a name="b2323101020414"></a>recurrence_type</strong> is set to <strong id="b932318101418"><a name="b932318101418"></a><a name="b932318101418"></a>Daily</strong>, this parameter does not take effect.</p>
    </div></div>
    </li></ul>
    </td>
    </tr>
    <tr id="row18424141294615"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p163691829174618"><a name="p163691829174618"></a><a name="p163691829174618"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p7369182914614"><a name="p7369182914614"></a><a name="p7369182914614"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p10369729194615"><a name="p10369729194615"></a><a name="p10369729194615"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p183691295469"><a name="p183691295469"></a><a name="p183691295469"></a>Specifies the start time of the scaling action triggered periodically. The time format complies with UTC. The default value is the local time.</p>
    <p id="p037052919466"><a name="p037052919466"></a><a name="p037052919466"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    <tr id="row19425912204620"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p137012924616"><a name="p137012924616"></a><a name="p137012924616"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p237015297461"><a name="p237015297461"></a><a name="p237015297461"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p03701429134615"><a name="p03701429134615"></a><a name="p03701429134615"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p13370192974611"><a name="p13370192974611"></a><a name="p13370192974611"></a>Specifies the end time of the scaling action triggered periodically. The time format complies with UTC. This parameter is mandatory when <strong id="b842352706173440"><a name="b842352706173440"></a><a name="b842352706173440"></a>scaling_policy_type</strong> is set to <strong id="b842352706173444"><a name="b842352706173444"></a><a name="b842352706173444"></a>RECURRENCE</strong>. When the scaling action is triggered periodically, the end time cannot be earlier than the current and start time.</p>
    <p id="p203703299462"><a name="p203703299462"></a><a name="p203703299462"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **scaling\_policy\_action**  field description

    <a name="table14148153113492"></a>
    <table><thead align="left"><tr id="row914933174911"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p1984914718496"><a name="p1984914718496"></a><a name="p1984914718496"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.2"><p id="p68491047104920"><a name="p68491047104920"></a><a name="p68491047104920"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="p12849747144916"><a name="p12849747144916"></a><a name="p12849747144916"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.45454545454546%" id="mcps1.2.5.1.4"><p id="p98494475496"><a name="p98494475496"></a><a name="p98494475496"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19149123164911"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p118491447144918"><a name="p118491447144918"></a><a name="p118491447144918"></a>operation</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p12849647124917"><a name="p12849647124917"></a><a name="p12849647124917"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p19849164719493"><a name="p19849164719493"></a><a name="p19849164719493"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><div class="p" id="p12849194711498"><a name="p12849194711498"></a><a name="p12849194711498"></a>Specifies the operation to be performed. The default operation is <strong id="b1898710304536"><a name="b1898710304536"></a><a name="b1898710304536"></a>ADD</strong>.<a name="ul627111141476"></a><a name="ul627111141476"></a><ul id="ul627111141476"><li>If <strong id="b13175144944616"><a name="b13175144944616"></a><a name="b13175144944616"></a>scaling_resource_type</strong> is set to <strong id="b1906755154616"><a name="b1906755154616"></a><a name="b1906755154616"></a>SCALING_GROUP</strong>, the following operations are supported:<a name="ul4517141421818"></a><a name="ul4517141421818"></a><ul id="ul4517141421818"><li><strong id="b8423527069234"><a name="b8423527069234"></a><a name="b8423527069234"></a>ADD</strong>: indicates adding instances.</li><li><strong id="b84235270692351"><a name="b84235270692351"></a><a name="b84235270692351"></a>REMOVE/REDUCE</strong>: indicates removing or reducing instances.</li><li><strong id="b84235270692418"><a name="b84235270692418"></a><a name="b84235270692418"></a>SET</strong>: indicates setting the number of instances to a specified value.</li></ul>
    </li><li>If <strong id="b142804917503"><a name="b142804917503"></a><a name="b142804917503"></a>scaling_resource_type</strong> is set to <strong id="b1741712985119"><a name="b1741712985119"></a><a name="b1741712985119"></a>BANDWIDTH</strong>, the following operations are supported:<a name="ul10599126171711"></a><a name="ul10599126171711"></a><ul id="ul10599126171711"><li><strong id="b643951612511"><a name="b643951612511"></a><a name="b643951612511"></a>ADD</strong>: indicates adding instances.</li><li><strong id="b190727587"><a name="b190727587"></a><a name="b190727587"></a>REDUCE</strong>: indicates reducing instances.</li><li><strong id="b410655124"><a name="b410655124"></a><a name="b410655124"></a>SET</strong>: indicates setting the number of instances to a specified value.</li></ul>
    </li></ul>
    </div>
    </td>
    </tr>
    <tr id="row8149143119496"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p484914764910"><a name="p484914764910"></a><a name="p484914764910"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p208491947124912"><a name="p208491947124912"></a><a name="p208491947124912"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p5849247124914"><a name="p5849247124914"></a><a name="p5849247124914"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p18849194784912"><a name="p18849194784912"></a><a name="p18849194784912"></a>Specifies the operation size. The value is an integer from 0 to 300. The default value is <strong id="b11732181112413"><a name="b11732181112413"></a><a name="b11732181112413"></a>1</strong>. This parameter can be set to <strong id="b5635125912547"><a name="b5635125912547"></a><a name="b5635125912547"></a>0</strong> only when <strong id="b9320322105511"><a name="b9320322105511"></a><a name="b9320322105511"></a>operation</strong> is set to <strong id="b196421525125513"><a name="b196421525125513"></a><a name="b196421525125513"></a>SET</strong>.</p>
    <a name="ul1883910551366"></a><a name="ul1883910551366"></a><ul id="ul1883910551366"><li>If <strong>scaling_resource_type</strong> is set to <strong>SCALING_GROUP</strong>, this parameter indicates the number of instances. The value is an integer from 0 to 300 and the default value is <strong>1</strong>.</li><li>If <strong>scaling_resource_type</strong> is set to <strong>BANDWIDTH</strong>, this parameter indicates the bandwidth (Mbit/s). The value is an integer from 1 to 300 and the default value is <strong>1</strong>.</li><li>If <strong id="b8423527061619"><a name="b8423527061619"></a><a name="b8423527061619"></a>scaling_resource_type</strong> is set to <strong id="b84235270616122"><a name="b84235270616122"></a><a name="b84235270616122"></a>SCALING_GROUP</strong>, either <strong id="b842352706105430"><a name="b842352706105430"></a><a name="b842352706105430"></a>size</strong> or <strong id="b842352706105435"><a name="b842352706105435"></a><a name="b842352706105435"></a>percentage</strong> can be set.</li></ul>
    </td>
    </tr>
    <tr id="row16150133114912"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p184984724914"><a name="p184984724914"></a><a name="p184984724914"></a>percentage</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p785044715492"><a name="p785044715492"></a><a name="p785044715492"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p178501847124913"><a name="p178501847124913"></a><a name="p178501847124913"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p38501247184913"><a name="p38501247184913"></a><a name="p38501247184913"></a>Specifies the percentage of instances to be operated. If <strong id="b16372183920211"><a name="b16372183920211"></a><a name="b16372183920211"></a>operation</strong> is set to <strong id="b1037363917217"><a name="b1037363917217"></a><a name="b1037363917217"></a>ADD</strong>, <strong id="b11642163516565"><a name="b11642163516565"></a><a name="b11642163516565"></a>REMOVE</strong>, or <strong id="b1237543912118"><a name="b1237543912118"></a><a name="b1237543912118"></a>REDUCE</strong>, the value of this parameter is an integer from 1 to 20000. If <strong id="b13375939102115"><a name="b13375939102115"></a><a name="b13375939102115"></a>operation</strong> is set to <strong id="b23771239132117"><a name="b23771239132117"></a><a name="b23771239132117"></a>SET</strong>, the value is an integer from 0 to 20000.</p>
    <a name="ul1740120777"></a><a name="ul1740120777"></a><ul id="ul1740120777"><li>If <strong id="b84235270616313"><a name="b84235270616313"></a><a name="b84235270616313"></a>scaling_resource_type</strong> is set to <strong id="b84235270616320"><a name="b84235270616320"></a><a name="b84235270616320"></a>SCALING_GROUP</strong>, either <strong id="b190074049516530"><a name="b190074049516530"></a><a name="b190074049516530"></a>size</strong> or <strong id="b35265935816530"><a name="b35265935816530"></a><a name="b35265935816530"></a>percentage</strong> can be set. If neither <strong id="b84235270616550"><a name="b84235270616550"></a><a name="b84235270616550"></a>size</strong> nor <strong id="b84235270616556"><a name="b84235270616556"></a><a name="b84235270616556"></a>percentage</strong> is set, the default value of <strong id="b8423527061667"><a name="b8423527061667"></a><a name="b8423527061667"></a>size</strong> is <strong id="b84235270616612"><a name="b84235270616612"></a><a name="b84235270616612"></a>1</strong>.</li><li>If <strong id="b7913672816"><a name="b7913672816"></a><a name="b7913672816"></a>scaling_resource_type</strong> is set to <strong id="b0590640112810"><a name="b0590640112810"></a><a name="b0590640112810"></a>BANDWIDTH</strong>, <strong id="b51941644192810"><a name="b51941644192810"></a><a name="b51941644192810"></a>percentage</strong> is unavailable.</li></ul>
    </td>
    </tr>
    <tr id="row2150173194911"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p4850347164914"><a name="p4850347164914"></a><a name="p4850347164914"></a>limits</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p4850547184915"><a name="p4850547184915"></a><a name="p4850547184915"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p385004711497"><a name="p385004711497"></a><a name="p385004711497"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p11850647164919"><a name="p11850647164919"></a><a name="p11850647164919"></a>Specifies the operation restrictions.</p>
    <p id="p1785064744911"><a name="p1785064744911"></a><a name="p1785064744911"></a>If <strong id="b172916117291"><a name="b172916117291"></a><a name="b172916117291"></a>scaling_resource_type</strong> is set to <strong id="b172949118294"><a name="b172949118294"></a><a name="b172949118294"></a>BANDWIDTH</strong> and <strong id="b129451172919"><a name="b129451172919"></a><a name="b129451172919"></a>operation</strong> is not <strong id="b2029515172914"><a name="b2029515172914"></a><a name="b2029515172914"></a>SET</strong>, this parameter takes effect and the unit is Mbit/s.</p>
    <a name="ul19875103016377"></a><a name="ul19875103016377"></a><ul id="ul19875103016377"><li>If <strong id="b11433157115"><a name="b11433157115"></a><a name="b11433157115"></a>operation</strong> is set to <strong id="b1414531516119"><a name="b1414531516119"></a><a name="b1414531516119"></a>ADD</strong>, this parameter indicates the maximum bandwidth allowed.</li><li>If <strong>operation</strong> is set to <strong>REDUCE</strong>, this parameter indicates the minimum bandwidth allowed.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    This example shows how to create an alarm policy named  **hth\_aspolicy\_1**  with the following configurations: The alarm rule ID is  **al1513822380493GvlJKZwA8**; when the alarm threshold is reached according to the alarm rule, the bandwidth with ID  **8ade64b5-d685-40b8-8582-4ce306ea37a6**  will be increased by 1 Mbit/s until the bandwidth reaches 10 Mbit/s.

    ```
    POST https://{Endpoint}/autoscaling-api/v2/{project_id}/scaling_policy
    
    { 
        "alarm_id": "al1513822380493GvlJKZwA8",
        "cool_down_time": 900,
        "scaling_resource_id": "8ade64b5-d685-40b8-8582-4ce306ea37a6",
        "scaling_resource_type": "BANDWIDTH",
        "scaling_policy_action": {
               "size": 1,
               "operation": "ADD",
               "limits": 10
        },
        "scaling_policy_name": "hth_aspolicy_1",
        "scaling_policy_type": "ALARM"
    }
    ```


## Response Message<a name="section1133152055814"></a>

-   Response parameters

    **Table  5**  Response parameters

    <a name="table2454125213587"></a>
    <table><thead align="left"><tr id="row134541952105817"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p14813106591"><a name="p14813106591"></a><a name="p14813106591"></a><strong id="b1420924125415"><a name="b1420924125415"></a><a name="b1420924125415"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p1181314014595"><a name="p1181314014595"></a><a name="p1181314014595"></a><strong id="b84235270693914"><a name="b84235270693914"></a><a name="b84235270693914"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="p1681360205913"><a name="p1681360205913"></a><a name="p1681360205913"></a><strong id="b1434595105411"><a name="b1434595105411"></a><a name="b1434595105411"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row645511524585"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p198134045919"><a name="p198134045919"></a><a name="p198134045919"></a>scaling_policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p12814130195914"><a name="p12814130195914"></a><a name="p12814130195914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="p168144045917"><a name="p168144045917"></a><a name="p168144045917"></a>Specifies the AS policy ID.</p>
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


## Returned Values<a name="section12531175212811"></a>

-   Normal

    200

-   Abnormal

    <a name="table98255396918"></a>
    <table><thead align="left"><tr id="row16826103916915"><th class="cellrowborder" valign="top" width="37%" id="mcps1.1.3.1.1"><p id="p7898152092"><a name="p7898152092"></a><a name="p7898152092"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.1.3.1.2"><p id="p489816521797"><a name="p489816521797"></a><a name="p489816521797"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1382614391590"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p11898552298"><a name="p11898552298"></a><a name="p11898552298"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p108981852296"><a name="p108981852296"></a><a name="p108981852296"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row11826143918912"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1289811521910"><a name="p1289811521910"></a><a name="p1289811521910"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p14898105216917"><a name="p14898105216917"></a><a name="p14898105216917"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row082613391793"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p178981652891"><a name="p178981652891"></a><a name="p178981652891"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1389818529914"><a name="p1389818529914"></a><a name="p1389818529914"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1982663913918"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p15899105212914"><a name="p15899105212914"></a><a name="p15899105212914"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1589915521498"><a name="p1589915521498"></a><a name="p1589915521498"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row882683911914"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p168991652792"><a name="p168991652792"></a><a name="p168991652792"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p489910525915"><a name="p489910525915"></a><a name="p489910525915"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row118266391992"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p789914525916"><a name="p789914525916"></a><a name="p789914525916"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p38991952398"><a name="p38991952398"></a><a name="p38991952398"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row1982653916915"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p5899205214917"><a name="p5899205214917"></a><a name="p5899205214917"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p8899155218920"><a name="p8899155218920"></a><a name="p8899155218920"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row68261139391"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p489919521493"><a name="p489919521493"></a><a name="p489919521493"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p148997521199"><a name="p148997521199"></a><a name="p148997521199"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row118263391996"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1989910521296"><a name="p1989910521296"></a><a name="p1989910521296"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p2899125213915"><a name="p2899125213915"></a><a name="p2899125213915"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row1882643913911"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p138998521697"><a name="p138998521697"></a><a name="p138998521697"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1089975215917"><a name="p1089975215917"></a><a name="p1089975215917"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row178261339094"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1989915521793"><a name="p1989915521793"></a><a name="p1989915521793"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p6899105217917"><a name="p6899105217917"></a><a name="p6899105217917"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row382612399913"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p889915525910"><a name="p889915525910"></a><a name="p889915525910"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1990095214918"><a name="p1990095214918"></a><a name="p1990095214918"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row78261039593"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p169001052195"><a name="p169001052195"></a><a name="p169001052195"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p14900155215918"><a name="p14900155215918"></a><a name="p14900155215918"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row682615391991"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p99001552295"><a name="p99001552295"></a><a name="p99001552295"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p159009521193"><a name="p159009521193"></a><a name="p159009521193"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

