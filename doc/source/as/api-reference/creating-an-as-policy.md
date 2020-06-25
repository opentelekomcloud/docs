# Creating an AS Policy<a name="EN-US_TOPIC_0043063062"></a>

## Function<a name="section46628683"></a>

This interface is used to create an AS policy.

-   An AS policy defines whether to increase or decrease the number of instances in an AS group. If the number and the expected number of instances in an AS group are different due to the execution of the AS policy, AS automatically adjusts the number of instances to the expected.
-   AS supports the following policies: alarm-triggered policy, periodic policy, and scheduled policy.
-   In the execution of the AS policy, you can set the number of instances to be scaled or perform a scaling action according to a percentage specified in the AS policy.

## URI<a name="section17004965"></a>

POST /autoscaling-api/v1/\{project\_id\}/scaling\_policy

**Table  1**  Parameter description

<a name="table38292076"></a>
<table><thead align="left"><tr id="row61695723"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p31297682"><a name="p31297682"></a><a name="p31297682"></a><strong id="b451615735317"><a name="b451615735317"></a><a name="b451615735317"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p52084342"><a name="p52084342"></a><a name="p52084342"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p58082174"><a name="p58082174"></a><a name="p58082174"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p7035667"><a name="p7035667"></a><a name="p7035667"></a><strong id="b09691576532"><a name="b09691576532"></a><a name="b09691576532"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row33018140"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p57223682"><a name="p57223682"></a><a name="p57223682"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p4606636"><a name="p4606636"></a><a name="p4606636"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p37593218"><a name="p37593218"></a><a name="p37593218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section18826965"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table5563313"></a>
    <table><thead align="left"><tr id="row20109663"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.1"><p id="p18270010"><a name="p18270010"></a><a name="p18270010"></a><strong id="b128046811534"><a name="b128046811534"></a><a name="b128046811534"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.2"><p id="p3475817"><a name="p3475817"></a><a name="p3475817"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p13105749"><a name="p13105749"></a><a name="p13105749"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.45454545454546%" id="mcps1.2.5.1.4"><p id="p54932709"><a name="p54932709"></a><a name="p54932709"></a><strong id="b19644199185318"><a name="b19644199185318"></a><a name="b19644199185318"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46564252"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p13608105"><a name="p13608105"></a><a name="p13608105"></a>scaling_policy_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p28514710"><a name="p28514710"></a><a name="p28514710"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p27990155"><a name="p27990155"></a><a name="p27990155"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p52610097"><a name="p52610097"></a><a name="p52610097"></a>Specifies the AS policy name. The name contains only letters, digits, underscores (_), and hyphens (-), and cannot exceed 64 characters.</p>
    </td>
    </tr>
    <tr id="row62813139112932"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p50487343112944"><a name="p50487343112944"></a><a name="p50487343112944"></a>scaling_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p62942986112944"><a name="p62942986112944"></a><a name="p62942986112944"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p65217081112944"><a name="p65217081112944"></a><a name="p65217081112944"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p48092197112944"><a name="p48092197112944"></a><a name="p48092197112944"></a>Specifies the AS group ID, which can be obtained using the API for querying AS groups. For details, see <a href="querying-as-groups.md">Querying AS Groups</a>.</p>
    </td>
    </tr>
    <tr id="row3728830"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p33599791"><a name="p33599791"></a><a name="p33599791"></a>scaling_policy_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p37228582"><a name="p37228582"></a><a name="p37228582"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p62725128"><a name="p62725128"></a><a name="p62725128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p47570623"><a name="p47570623"></a><a name="p47570623"></a>Specifies the AS policy type.</p>
    <a name="ul10238415193016"></a><a name="ul10238415193016"></a><ul id="ul10238415193016"><li><strong id="b50338569152840"><a name="b50338569152840"></a><a name="b50338569152840"></a>ALARM</strong> (corresponding to <strong id="b50393943152840"><a name="b50393943152840"></a><a name="b50393943152840"></a>alarm_id</strong>): indicates that the scaling action is triggered by an alarm.</li><li><strong id="b4853647152840"><a name="b4853647152840"></a><a name="b4853647152840"></a>SCHEDULED</strong> (corresponding to <strong id="b43682830152840"><a name="b43682830152840"></a><a name="b43682830152840"></a>scheduled_policy</strong>): indicates that the scaling action is triggered as scheduled.</li><li><strong id="b11927655152840"><a name="b11927655152840"></a><a name="b11927655152840"></a>RECURRENCE</strong> (corresponding to <strong id="b40240031152840"><a name="b40240031152840"></a><a name="b40240031152840"></a>scheduled_policy</strong>): indicates that the scaling action is triggered periodically.</li></ul>
    </td>
    </tr>
    <tr id="row54645451"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p64205424"><a name="p64205424"></a><a name="p64205424"></a>alarm_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p33256841"><a name="p33256841"></a><a name="p33256841"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p9449599"><a name="p9449599"></a><a name="p9449599"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p2176687103755"><a name="p2176687103755"></a><a name="p2176687103755"></a>Specifies the alarm rule ID. This parameter is mandatory when <strong id="b842352706153331"><a name="b842352706153331"></a><a name="b842352706153331"></a>scaling_policy_type</strong> is set to <strong id="b842352706153340"><a name="b842352706153340"></a><a name="b842352706153340"></a>ALARM</strong>. After this parameter is specified, the value of <strong id="b842352706153543"><a name="b842352706153543"></a><a name="b842352706153543"></a>scheduled_policy</strong> does not take effect.</p>
    <p id="p280497851247"><a name="p280497851247"></a><a name="p280497851247"></a>After you create an alarm policy, the system automatically adds an alarm triggering activity of the autoscaling type to the <strong id="b84235270619718"><a name="b84235270619718"></a><a name="b84235270619718"></a>alarm_actions</strong> field in the alarm rule specified by the parameter value.</p>
    </td>
    </tr>
    <tr id="row43653635"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p46283551"><a name="p46283551"></a><a name="p46283551"></a>scheduled_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p57980147"><a name="p57980147"></a><a name="p57980147"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="a4c03d226ca78442f99e13b8d363cd51d"><a name="a4c03d226ca78442f99e13b8d363cd51d"></a><a name="a4c03d226ca78442f99e13b8d363cd51d"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p34708966"><a name="p34708966"></a><a name="p34708966"></a>Specifies the periodic or scheduled AS policy. This parameter is mandatory when <strong id="b842352706171742"><a name="b842352706171742"></a><a name="b842352706171742"></a>scaling_policy_type</strong> is set to <strong id="b842352706171747"><a name="b842352706171747"></a><a name="b842352706171747"></a>SCHEDULED</strong> or <strong id="b842352706171752"><a name="b842352706171752"></a><a name="b842352706171752"></a>RECURRENCE</strong>. After this parameter is specified, the value of <strong id="b84235270614268"><a name="b84235270614268"></a><a name="b84235270614268"></a>alarm_id</strong> does not take effect. For details, see <a href="#table1736886710241">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row43945239"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p2794612"><a name="p2794612"></a><a name="p2794612"></a>scaling_policy_action</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p25037038"><a name="p25037038"></a><a name="p25037038"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p153681238184114"><a name="p153681238184114"></a><a name="p153681238184114"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p52618583"><a name="p52618583"></a><a name="p52618583"></a>Specifies the scaling action of the AS policy. For details, see <a href="#table2371051010342">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row3805200"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p39785801"><a name="p39785801"></a><a name="p39785801"></a>cool_down_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p1424418"><a name="p1424418"></a><a name="p1424418"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p48268995"><a name="p48268995"></a><a name="p48268995"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.5.1.4 "><p id="p2033614820549"><a name="p2033614820549"></a><a name="p2033614820549"></a>Specifies the cooldown period (in seconds). The value ranges from 0 to 86400 and is 300 by default.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scheduled\_policy**  field description

    <a name="table1736886710241"></a>
    <table><thead align="left"><tr id="r71a1a0c14b8449ae9c19a6c4f3a27f2a"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.1"><p id="a103344d6752d4ce2a271ee3f63ead9e0"><a name="a103344d6752d4ce2a271ee3f63ead9e0"></a><a name="a103344d6752d4ce2a271ee3f63ead9e0"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.2"><p id="p366931181079"><a name="p366931181079"></a><a name="p366931181079"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="afef6d9584333496a8c5ffbc00c9697dd"><a name="afef6d9584333496a8c5ffbc00c9697dd"></a><a name="afef6d9584333496a8c5ffbc00c9697dd"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.5.1.4"><p id="en-us_topic_0021400636_p361788155424"><a name="en-us_topic_0021400636_p361788155424"></a><a name="en-us_topic_0021400636_p361788155424"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r9d26d183ebcb408d8b6873deab234856"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="ae60918cef42b4e0894459d8e5a8b586c"><a name="ae60918cef42b4e0894459d8e5a8b586c"></a><a name="ae60918cef42b4e0894459d8e5a8b586c"></a>launch_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p193525921079"><a name="p193525921079"></a><a name="p193525921079"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="a600202acd6db495281de660f1221973d"><a name="a600202acd6db495281de660f1221973d"></a><a name="a600202acd6db495281de660f1221973d"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="a8acac5089bd3423da0d691e85a2b06a4"><a name="a8acac5089bd3423da0d691e85a2b06a4"></a><a name="a8acac5089bd3423da0d691e85a2b06a4"></a>Specifies the time when the scaling action is triggered. The time format complies with UTC.</p>
    <a name="u17ff5ce1e7d24df8b69d30baeb489534"></a><a name="u17ff5ce1e7d24df8b69d30baeb489534"></a><ul id="u17ff5ce1e7d24df8b69d30baeb489534"><li>If <strong>scaling_policy_type</strong> is set to <strong>SCHEDULED</strong>, the time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</li><li>If <strong>scaling_policy_type</strong> is set to <strong>RECURRENCE</strong>, the time format is <strong>hh:mm</strong>.</li></ul>
    </td>
    </tr>
    <tr id="r71db331768414f028a65da7aaf7f9814"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="a2e081bd068fa4052822b23fe468c6f00"><a name="a2e081bd068fa4052822b23fe468c6f00"></a><a name="a2e081bd068fa4052822b23fe468c6f00"></a>recurrence_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p240561431079"><a name="p240561431079"></a><a name="p240561431079"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="a89ed2a5e669f4fc7941e232ed3d33370"><a name="a89ed2a5e669f4fc7941e232ed3d33370"></a><a name="a89ed2a5e669f4fc7941e232ed3d33370"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="a98a0b043879341a4a678b7fbb4e068d9"><a name="a98a0b043879341a4a678b7fbb4e068d9"></a><a name="a98a0b043879341a4a678b7fbb4e068d9"></a>Specifies the periodic triggering type. This parameter is mandatory when <strong id="b842352706172110"><a name="b842352706172110"></a><a name="b842352706172110"></a>scaling_policy_type</strong> is set to <strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>RECURRENCE</strong>.</p>
    <a name="ul17833134534913"></a><a name="ul17833134534913"></a><ul id="ul17833134534913"><li><strong>Daily</strong>: indicates that the scaling action is triggered once a day.</li><li><strong>Weekly</strong>: indicates that the scaling action is triggered once a week.</li><li><strong>Monthly</strong>: indicates that the scaling action is triggered once a month.</li></ul>
    </td>
    </tr>
    <tr id="r5b4081bb97fe4c749ec56bf067b3d37e"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="ab0c3d939c02d4f0e892ef0ae889f33c6"><a name="ab0c3d939c02d4f0e892ef0ae889f33c6"></a><a name="ab0c3d939c02d4f0e892ef0ae889f33c6"></a>recurrence_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p23905621079"><a name="p23905621079"></a><a name="p23905621079"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="a5c08ed2e549149c9b609e1e11dd8b49d"><a name="a5c08ed2e549149c9b609e1e11dd8b49d"></a><a name="a5c08ed2e549149c9b609e1e11dd8b49d"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="a07f48cfcdafa4ffd87bba3b4e90c0111"><a name="a07f48cfcdafa4ffd87bba3b4e90c0111"></a><a name="a07f48cfcdafa4ffd87bba3b4e90c0111"></a>Specifies the day when a periodic scaling action is triggered. This parameter is mandatory when <strong id="b1779882921"><a name="b1779882921"></a><a name="b1779882921"></a>scaling_policy_type</strong> is set to <strong id="b2101096697"><a name="b2101096697"></a><a name="b2101096697"></a>RECURRENCE</strong>.</p>
    <a name="uaaa702fc2e874c3a9cad601322271ee0"></a><a name="uaaa702fc2e874c3a9cad601322271ee0"></a><ul id="uaaa702fc2e874c3a9cad601322271ee0"><li>If <strong>recurrence_type</strong> is set to <strong>Daily</strong>, the value is <strong>null</strong>, indicating that the scaling action is triggered once a day.</li><li>If <strong>recurrence_type</strong> is set to <strong>Weekly</strong>, the value ranges from <strong>1</strong> (Sunday) to <strong>7</strong> (Saturday). The digits refer to dates in each week and separated by a comma, such as <strong>1,3,5</strong>.</li><li>If <strong id="b84235270617528"><a name="b84235270617528"></a><a name="b84235270617528"></a>recurrence_type</strong> is set to <strong>Monthly</strong>, the value ranges from <strong>1</strong> to <strong>31</strong>. The digits refer to the dates in each month and separated by a comma, such as <strong>1,10,13,28</strong>.</li></ul>
    </td>
    </tr>
    <tr id="r60fb8a7a17c346f8928b404e0b93db76"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="ad9da8c2101cb4ad6b314e73f107cc4c4"><a name="ad9da8c2101cb4ad6b314e73f107cc4c4"></a><a name="ad9da8c2101cb4ad6b314e73f107cc4c4"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p594178421079"><a name="p594178421079"></a><a name="p594178421079"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="a0a2523d6aba94e1586e2c505a81da73c"><a name="a0a2523d6aba94e1586e2c505a81da73c"></a><a name="a0a2523d6aba94e1586e2c505a81da73c"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="a34f741f8f41f49bda82f908ffb12b680"><a name="a34f741f8f41f49bda82f908ffb12b680"></a><a name="a34f741f8f41f49bda82f908ffb12b680"></a>Specifies the start time of the scaling action triggered periodically. The time format complies with UTC. The default value is the local time.</p>
    <p id="a7271cbc17afb4bacb091905b4655e705"><a name="a7271cbc17afb4bacb091905b4655e705"></a><a name="a7271cbc17afb4bacb091905b4655e705"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    <tr id="r45c085bdc7ba45079851ba1d2ef8d897"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="a9aad49cfc3274586976001f3bfdf5719"><a name="a9aad49cfc3274586976001f3bfdf5719"></a><a name="a9aad49cfc3274586976001f3bfdf5719"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p481158781079"><a name="p481158781079"></a><a name="p481158781079"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="acee7a98428ea4dba93a7020ef11dd7b9"><a name="acee7a98428ea4dba93a7020ef11dd7b9"></a><a name="acee7a98428ea4dba93a7020ef11dd7b9"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="a57b435fb6ab3467bafe191d8ac989e2d"><a name="a57b435fb6ab3467bafe191d8ac989e2d"></a><a name="a57b435fb6ab3467bafe191d8ac989e2d"></a>Specifies the end time of the scaling action triggered periodically. The time format complies with UTC. This parameter is mandatory when <strong id="b842352706173440"><a name="b842352706173440"></a><a name="b842352706173440"></a>scaling_policy_type</strong> is set to <strong id="b842352706173444"><a name="b842352706173444"></a><a name="b842352706173444"></a>RECURRENCE</strong>.</p>
    <p id="aab98d253597346778f2f046a5e022aa9"><a name="aab98d253597346778f2f046a5e022aa9"></a><a name="aab98d253597346778f2f046a5e022aa9"></a>When the scaling action is triggered periodically, the end time cannot be earlier than the current and start time.</p>
    <p id="a06fe304a198d4e069ddd3946c5f1179d"><a name="a06fe304a198d4e069ddd3946c5f1179d"></a><a name="a06fe304a198d4e069ddd3946c5f1179d"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **scaling\_policy\_action**  field description

    <a name="table2371051010342"></a>
    <table><thead align="left"><tr id="re1f0786afb8b4e88a8fc1ea46d03b82a"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="aec3e6ac917d14dfeb7ffb65860bb1306"><a name="aec3e6ac917d14dfeb7ffb65860bb1306"></a><a name="aec3e6ac917d14dfeb7ffb65860bb1306"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p161699610619"><a name="p161699610619"></a><a name="p161699610619"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="adf1eacf282f34f0c87a7f239f00b4faf"><a name="adf1eacf282f34f0c87a7f239f00b4faf"></a><a name="adf1eacf282f34f0c87a7f239f00b4faf"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="adbb947caa2164ef080b97285f51e2ca4"><a name="adbb947caa2164ef080b97285f51e2ca4"></a><a name="adbb947caa2164ef080b97285f51e2ca4"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r6132212f59bc42529826e44935a5cfaf"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="ae05d19776675443bb90e03221ee13658"><a name="ae05d19776675443bb90e03221ee13658"></a><a name="ae05d19776675443bb90e03221ee13658"></a>operation</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p6386788410619"><a name="p6386788410619"></a><a name="p6386788410619"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="ab3f64183c0044f0cb0c72b8b7c381c66"><a name="ab3f64183c0044f0cb0c72b8b7c381c66"></a><a name="ab3f64183c0044f0cb0c72b8b7c381c66"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="a5c8d1942ad2246beaa196587336c303e"><a name="a5c8d1942ad2246beaa196587336c303e"></a><a name="a5c8d1942ad2246beaa196587336c303e"></a>Specifies the operation to be performed. The default operation is <strong>ADD</strong>.</p>
    <a name="ul17377291387"></a><a name="ul17377291387"></a><ul id="ul17377291387"><li><strong>ADD</strong>: adds specified number of instances to the AS group.</li><li><strong id="b84235270611343"><a name="b84235270611343"></a><a name="b84235270611343"></a>REMOVE/REDUCE</strong>: removes or reduces specified number of instances from the AS group.</li><li><strong>SET</strong>: sets the number of instances in the AS group.</li></ul>
    </td>
    </tr>
    <tr id="rd780cce224684db9a0a0fff71c2cc5ce"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p26677605172946"><a name="p26677605172946"></a><a name="p26677605172946"></a>instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p13402436172946"><a name="p13402436172946"></a><a name="p13402436172946"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p11855564172946"><a name="p11855564172946"></a><a name="p11855564172946"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p20776612172946"><a name="p20776612172946"></a><a name="p20776612172946"></a>Specifies the number of instances to be operated. The default number is <strong>1</strong>. The value range is as follows for a default quota:</p>
    <a name="ul897214318562"></a><a name="ul897214318562"></a><ul id="ul897214318562"><li>If <strong id="b12649189115414"><a name="b12649189115414"></a><a name="b12649189115414"></a>operation</strong> is set to <strong id="b976871918548"><a name="b976871918548"></a><a name="b976871918548"></a>SET</strong>, the value range is 0 to 200.</li><li>If <strong id="b13160165618541"><a name="b13160165618541"></a><a name="b13160165618541"></a>operation</strong> is set to <strong id="b2029714596546"><a name="b2029714596546"></a><a name="b2029714596546"></a>ADD</strong>, <strong id="b798416185520"><a name="b798416185520"></a><a name="b798416185520"></a>REMOVE</strong>, or <strong id="b7950192184120"><a name="b7950192184120"></a><a name="b7950192184120"></a>REDUCE</strong>, the value range is 1 to 200.</li></ul>
    <div class="note" id="note99603584562"><a name="note99603584562"></a><a name="note99603584562"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p696175820561"><a name="p696175820561"></a><a name="p696175820561"></a>Either <strong id="b842352706105430"><a name="b842352706105430"></a><a name="b842352706105430"></a>instance_number</strong> or <strong id="b842352706105435"><a name="b842352706105435"></a><a name="b842352706105435"></a>instance_percentage</strong> is required.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row4165649917933"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p17249893172946"><a name="p17249893172946"></a><a name="p17249893172946"></a>instance_percentage</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p55064094172946"><a name="p55064094172946"></a><a name="p55064094172946"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p31006664172946"><a name="p31006664172946"></a><a name="p31006664172946"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p083717531563"><a name="p083717531563"></a><a name="p083717531563"></a>Specifies the percentage of instances to be operated. You can increase, decrease, or set the number of instances in an AS group to the specified percentage of the current number of instances. If <strong id="b587711610207"><a name="b587711610207"></a><a name="b587711610207"></a>operation</strong> is set to <strong id="b7766189182012"><a name="b7766189182012"></a><a name="b7766189182012"></a>ADD</strong>, <strong id="b155020126201"><a name="b155020126201"></a><a name="b155020126201"></a>REMOVE</strong> or <strong id="b1958414415402"><a name="b1958414415402"></a><a name="b1958414415402"></a>REDUCE</strong>, the value of this parameter is an integer from 1 to 20000. If <strong id="b15177335112010"><a name="b15177335112010"></a><a name="b15177335112010"></a>operation</strong> is set to <strong id="b15787182814204"><a name="b15787182814204"></a><a name="b15787182814204"></a>SET</strong>, the value is an integer from 0 to 20000.</p>
    <p id="p55280357172946"><a name="p55280357172946"></a><a name="p55280357172946"></a>If neither <strong id="b8423527061122"><a name="b8423527061122"></a><a name="b8423527061122"></a>instance_number</strong> nor <strong id="b8423527061126"><a name="b8423527061126"></a><a name="b8423527061126"></a>instance_percentage</strong> is specified, the number of instances to be operated is 1.</p>
    <p id="p27761166172946"><a name="p27761166172946"></a><a name="p27761166172946"></a>Either <strong id="b317105073"><a name="b317105073"></a><a name="b317105073"></a>instance_number</strong> or <strong id="b1543533074"><a name="b1543533074"></a><a name="b1543533074"></a>instance_percentage</strong> is required.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    This example shows how to create a periodic AS policy named  **as-policy-7a75**. The policy takes effect from 2015-12-14T03:34Z through 2015-12-27T03:34Z. During this period, one instance will be added to AS group with ID  **5bc3aa02-b83e-454c-aba1-4d2095c68f8b**  at 16:00 every day.

    ```
    POST https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_policy
    
    {
        "scaling_policy_name": "as-policy-7a75",
        "scaling_policy_action": {
            "operation": "ADD",
            "instance_number": 1
        },
        "cool_down_time": 900,
        "scheduled_policy": {
            "launch_time": "16:00",
            "recurrence_type": "Daily",
            "start_time": "2015-12-14T03:34Z",
            "end_time": "2015-12-27T03:34Z"
        },
        "scaling_policy_type": "RECURRENCE",
        "scaling_group_id": "5bc3aa02-b83e-454c-aba1-4d2095c68f8b"
    }
    ```


## Response Message<a name="section35224963"></a>

-   Response parameters

    **Table  5**  Response parameters

    <a name="table32455223"></a>
    <table><thead align="left"><tr id="row51926520"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p45298596"><a name="p45298596"></a><a name="p45298596"></a><strong id="b19479181614539"><a name="b19479181614539"></a><a name="b19479181614539"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p45307656"><a name="p45307656"></a><a name="p45307656"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.4.1.3"><p id="p46041549"><a name="p46041549"></a><a name="p46041549"></a><strong id="b953018165312"><a name="b953018165312"></a><a name="b953018165312"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38378011"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p21611161"><a name="p21611161"></a><a name="p21611161"></a>scaling_policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p5673583"><a name="p5673583"></a><a name="p5673583"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p56907078"><a name="p56907078"></a><a name="p56907078"></a>Specifies the AS policy ID.</p>
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


## Returned Values<a name="section48589216"></a>

-   Normal

    200

-   Abnormal

    <a name="table55475379"></a>
    <table><thead align="left"><tr id="row47787886"><th class="cellrowborder" valign="top" width="35%" id="mcps1.1.3.1.1"><p id="p45613538"><a name="p45613538"></a><a name="p45613538"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.1.3.1.2"><p id="p3709091"><a name="p3709091"></a><a name="p3709091"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32000920"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p41937705"><a name="p41937705"></a><a name="p41937705"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p41510976"><a name="p41510976"></a><a name="p41510976"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row38054464"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p62512728"><a name="p62512728"></a><a name="p62512728"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p30366184"><a name="p30366184"></a><a name="p30366184"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row4860205"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p58132325"><a name="p58132325"></a><a name="p58132325"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p11097898"><a name="p11097898"></a><a name="p11097898"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row32772220"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p37304191"><a name="p37304191"></a><a name="p37304191"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p1740610"><a name="p1740610"></a><a name="p1740610"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row15665491"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p60945241"><a name="p60945241"></a><a name="p60945241"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p37617525"><a name="p37617525"></a><a name="p37617525"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row3013405"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p42759282"><a name="p42759282"></a><a name="p42759282"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p40949840"><a name="p40949840"></a><a name="p40949840"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row33004241"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p56097870"><a name="p56097870"></a><a name="p56097870"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p47633640"><a name="p47633640"></a><a name="p47633640"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row26049579"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p29641146"><a name="p29641146"></a><a name="p29641146"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p52122650"><a name="p52122650"></a><a name="p52122650"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row66450672"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p13795340"><a name="p13795340"></a><a name="p13795340"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p43680716"><a name="p43680716"></a><a name="p43680716"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row57582125"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p33640543"><a name="p33640543"></a><a name="p33640543"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p40529449"><a name="p40529449"></a><a name="p40529449"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row29220727"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p18068697"><a name="p18068697"></a><a name="p18068697"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p54278376"><a name="p54278376"></a><a name="p54278376"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row18743339"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p41815528"><a name="p41815528"></a><a name="p41815528"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p31614597"><a name="p31614597"></a><a name="p31614597"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row16095919"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p28701056"><a name="p28701056"></a><a name="p28701056"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p43084165"><a name="p43084165"></a><a name="p43084165"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row52213166"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p1408093"><a name="p1408093"></a><a name="p1408093"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p46946741"><a name="p46946741"></a><a name="p46946741"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

