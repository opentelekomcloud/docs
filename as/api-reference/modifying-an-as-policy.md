# Modifying an AS Policy<a name="EN-US_TOPIC_0043063080"></a>

## Function<a name="section38035443"></a>

This interface is used to modify a specified AS policy.

## URI<a name="section6774674"></a>

PUT /autoscaling-api/v1/\{project\_id\}/scaling\_policy/\{scaling\_policy\_id\}

**Table  1**  Parameter description

<a name="table12837735"></a>
<table><thead align="left"><tr id="row25617672"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.1"><p id="p61765553"><a name="p61765553"></a><a name="p61765553"></a><strong id="b17750832195414"><a name="b17750832195414"></a><a name="b17750832195414"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p36953931"><a name="p36953931"></a><a name="p36953931"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p40478462"><a name="p40478462"></a><a name="p40478462"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p57529969"><a name="p57529969"></a><a name="p57529969"></a><strong id="b1935153316541"><a name="b1935153316541"></a><a name="b1935153316541"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row29415884"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p33876408"><a name="p33876408"></a><a name="p33876408"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p59634524"><a name="p59634524"></a><a name="p59634524"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p65667169"><a name="p65667169"></a><a name="p65667169"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row22746728"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p30545685"><a name="p30545685"></a><a name="p30545685"></a>scaling_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p58281439"><a name="p58281439"></a><a name="p58281439"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p23176109"><a name="p23176109"></a><a name="p23176109"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p65325544"><a name="p65325544"></a><a name="p65325544"></a>Specifies an AS policy ID. For details, see <a href="querying-as-policies.md">Querying AS Policies</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section60972066"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table57664987"></a>
    <table><thead align="left"><tr id="row64660974"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p3047552"><a name="p3047552"></a><a name="p3047552"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p45525183"><a name="p45525183"></a><a name="p45525183"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p63661202"><a name="p63661202"></a><a name="p63661202"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p56283746"><a name="p56283746"></a><a name="p56283746"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62689558"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p44689431"><a name="p44689431"></a><a name="p44689431"></a>scaling_policy_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p63074124"><a name="p63074124"></a><a name="p63074124"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p8730397"><a name="p8730397"></a><a name="p8730397"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p52610097"><a name="p52610097"></a><a name="p52610097"></a>Specifies the AS policy name. The name contains only letters, digits, underscores (_), and hyphens (-), and cannot exceed 64 characters.</p>
    </td>
    </tr>
    <tr id="row56226836"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p58079852"><a name="p58079852"></a><a name="p58079852"></a>scaling_policy_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p6847548"><a name="p6847548"></a><a name="p6847548"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p17780525"><a name="p17780525"></a><a name="p17780525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p30936422"><a name="p30936422"></a><a name="p30936422"></a>Specifies the AS policy type.</p>
    <a name="ul44233651193034"></a><a name="ul44233651193034"></a><ul id="ul44233651193034"><li><strong id="b8908878154133"><a name="b8908878154133"></a><a name="b8908878154133"></a>ALARM</strong> (corresponding to <strong id="b13071039154133"><a name="b13071039154133"></a><a name="b13071039154133"></a>alarm_id</strong>): indicates that the scaling action is triggered by an alarm. </li><li><strong id="b47749798154133"><a name="b47749798154133"></a><a name="b47749798154133"></a>SCHEDULED</strong> (corresponding to <strong id="b27095003154133"><a name="b27095003154133"></a><a name="b27095003154133"></a>scheduled_policy</strong>): indicates that the scaling action is triggered as scheduled.</li><li><strong id="b48283661154133"><a name="b48283661154133"></a><a name="b48283661154133"></a>RECURRENCE</strong> (corresponding to <strong id="b31899767154133"><a name="b31899767154133"></a><a name="b31899767154133"></a>scheduled_policy</strong>): indicates that the scaling action is triggered periodically.</li></ul>
    </td>
    </tr>
    <tr id="row36666067"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p17161430"><a name="p17161430"></a><a name="p17161430"></a>alarm_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p47898561"><a name="p47898561"></a><a name="p47898561"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p54578237"><a name="p54578237"></a><a name="p54578237"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p9582029104355"><a name="p9582029104355"></a><a name="p9582029104355"></a>Specifies the alarm rule ID. This parameter is mandatory when <strong id="b842352706153331"><a name="b842352706153331"></a><a name="b842352706153331"></a>scaling_policy_type</strong> is set to <strong id="b842352706153340"><a name="b842352706153340"></a><a name="b842352706153340"></a>ALARM</strong>. After this parameter is specified, the value of <strong id="b842352706153543"><a name="b842352706153543"></a><a name="b842352706153543"></a>scheduled_policy</strong> does not take effect.</p>
    <p id="p6030106312521"><a name="p6030106312521"></a><a name="p6030106312521"></a>After you modify an alarm policy, the system automatically adds an alarm triggering activity of the autoscaling type to the <strong id="b84235270619718"><a name="b84235270619718"></a><a name="b84235270619718"></a>alarm_actions</strong> field in the alarm rule specified by the parameter value.</p>
    <p id="p583865912521"><a name="p583865912521"></a><a name="p583865912521"></a>You can obtain the parameter value by querying Cloud Eye alarm rules. </p>
    </td>
    </tr>
    <tr id="row59087616"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p21367612"><a name="p21367612"></a><a name="p21367612"></a>scheduled_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p53055045"><a name="p53055045"></a><a name="p53055045"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="a4c03d226ca78442f99e13b8d363cd51d"><a name="a4c03d226ca78442f99e13b8d363cd51d"></a><a name="a4c03d226ca78442f99e13b8d363cd51d"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p476380"><a name="p476380"></a><a name="p476380"></a>Specifies the periodic or scheduled AS policy. This parameter is mandatory when <strong id="b842352706171742"><a name="b842352706171742"></a><a name="b842352706171742"></a>scaling_policy_type</strong> is set to <strong id="b842352706171747"><a name="b842352706171747"></a><a name="b842352706171747"></a>SCHEDULED</strong> or <strong id="b842352706171752"><a name="b842352706171752"></a><a name="b842352706171752"></a>RECURRENCE</strong>. After this parameter is specified, the value of <strong id="b84235270614268"><a name="b84235270614268"></a><a name="b84235270614268"></a>alarm_id</strong> does not take effect. For details, see <a href="#t759e6d15d244474e8f286185ede143fb">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row4287423"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p11736974"><a name="p11736974"></a><a name="p11736974"></a>scaling_policy_action</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p11170862"><a name="p11170862"></a><a name="p11170862"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p167395571418"><a name="p167395571418"></a><a name="p167395571418"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p9150720"><a name="p9150720"></a><a name="p9150720"></a>Specifies the scaling action of the AS policy. For details, see <a href="#t34390832ab524bcc8123c0f9a056064f">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row15247616"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p27097356"><a name="p27097356"></a><a name="p27097356"></a>cool_down_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p47402253"><a name="p47402253"></a><a name="p47402253"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p14377323"><a name="p14377323"></a><a name="p14377323"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p23712525"><a name="p23712525"></a><a name="p23712525"></a>Specifies the cooldown period (in seconds). The value ranges from 0 to 86400.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scheduled\_policy**  field description

    <a name="t759e6d15d244474e8f286185ede143fb"></a>
    <table><thead align="left"><tr id="rce98b9668cd747c88039421afe5ce935"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="ad9ac3007570a4752b2b2dbc0fb04dadc"><a name="ad9ac3007570a4752b2b2dbc0fb04dadc"></a><a name="ad9ac3007570a4752b2b2dbc0fb04dadc"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020845960_p366931181079"><a name="en-us_topic_0020845960_p366931181079"></a><a name="en-us_topic_0020845960_p366931181079"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="a602246198adf4a79a13bc4317d4c0d4f"><a name="a602246198adf4a79a13bc4317d4c0d4f"></a><a name="a602246198adf4a79a13bc4317d4c0d4f"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="a8cbfa8dcb0b943ff8e789755123fec83"><a name="a8cbfa8dcb0b943ff8e789755123fec83"></a><a name="a8cbfa8dcb0b943ff8e789755123fec83"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r43de461181294c56b28da56a1f604b09"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="abc19a41a8f594f1ba6701e10da50a078"><a name="abc19a41a8f594f1ba6701e10da50a078"></a><a name="abc19a41a8f594f1ba6701e10da50a078"></a>launch_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020845960_p193525921079"><a name="en-us_topic_0020845960_p193525921079"></a><a name="en-us_topic_0020845960_p193525921079"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="a15ae7b8585d24e48abc6b9bf45636fda"><a name="a15ae7b8585d24e48abc6b9bf45636fda"></a><a name="a15ae7b8585d24e48abc6b9bf45636fda"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="a61510df8f8ad43319d6df7c903934e43"><a name="a61510df8f8ad43319d6df7c903934e43"></a><a name="a61510df8f8ad43319d6df7c903934e43"></a>Specifies the time when the scaling action is triggered. The time format complies with UTC.</p>
    <a name="uf00af89403894ffc8ec87c36bc988668"></a><a name="uf00af89403894ffc8ec87c36bc988668"></a><ul id="uf00af89403894ffc8ec87c36bc988668"><li>If <strong>scaling_policy_type</strong> is set to <strong>SCHEDULED</strong>, the time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</li><li>If <strong>scaling_policy_type</strong> is set to <strong>RECURRENCE</strong>, the time format is <strong>hh:mm</strong>.</li></ul>
    </td>
    </tr>
    <tr id="rbd5ec7242fef4c03b21636ac14160d9e"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="a18479f6b70b34f29b2b90d754f59282a"><a name="a18479f6b70b34f29b2b90d754f59282a"></a><a name="a18479f6b70b34f29b2b90d754f59282a"></a>recurrence_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020845960_p240561431079"><a name="en-us_topic_0020845960_p240561431079"></a><a name="en-us_topic_0020845960_p240561431079"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="ae1f14fa2e6a54531aeffd26874fea267"><a name="ae1f14fa2e6a54531aeffd26874fea267"></a><a name="ae1f14fa2e6a54531aeffd26874fea267"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="aec06182f642543c6b455c58bfdaffadd"><a name="aec06182f642543c6b455c58bfdaffadd"></a><a name="aec06182f642543c6b455c58bfdaffadd"></a>Specifies the periodic triggering type. This parameter is mandatory when <strong id="b842352706172110"><a name="b842352706172110"></a><a name="b842352706172110"></a>scaling_policy_type</strong> is set to <strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>RECURRENCE</strong>.</p>
    <a name="ul2889151214615"></a><a name="ul2889151214615"></a><ul id="ul2889151214615"><li><strong>Daily</strong>: indicates that the scaling action is triggered once a day.</li><li><strong>Weekly</strong>: indicates that the scaling action is triggered once a week.</li><li><strong>Monthly</strong>: indicates that the scaling action is triggered once a month.</li></ul>
    </td>
    </tr>
    <tr id="r0a62cf7acbad402386b6375b0d8b1353"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="a36de9ca6c86e45a3b06fa24eedf584ad"><a name="a36de9ca6c86e45a3b06fa24eedf584ad"></a><a name="a36de9ca6c86e45a3b06fa24eedf584ad"></a>recurrence_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020845960_p23905621079"><a name="en-us_topic_0020845960_p23905621079"></a><a name="en-us_topic_0020845960_p23905621079"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="ad2c0647319f843e0a6c26a2fe1e57172"><a name="ad2c0647319f843e0a6c26a2fe1e57172"></a><a name="ad2c0647319f843e0a6c26a2fe1e57172"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="a07f48cfcdafa4ffd87bba3b4e90c0111"><a name="a07f48cfcdafa4ffd87bba3b4e90c0111"></a><a name="a07f48cfcdafa4ffd87bba3b4e90c0111"></a>Specifies the day when a periodic scaling action is triggered. This parameter is mandatory when <strong>scaling_policy_type</strong> is set to <strong>RECURRENCE</strong>.</p>
    <a name="u339136fb44714869865eb1ccb9d659cd"></a><a name="u339136fb44714869865eb1ccb9d659cd"></a><ul id="u339136fb44714869865eb1ccb9d659cd"><li>If <strong>recurrence_type</strong> is set to <strong>Daily</strong>, the value is <strong>null</strong>, indicating that the scaling action is triggered once a day.</li><li>If <strong>recurrence_type</strong> is set to <strong>Weekly</strong>, the value ranges from <strong>1</strong> (Sunday) to <strong>7</strong> (Saturday). The digits refer to dates in each week and separated by a comma, such as <strong>1,3,5</strong>.</li><li>If <strong id="b84235270617528"><a name="b84235270617528"></a><a name="b84235270617528"></a>recurrence_type</strong> is set to <strong>Monthly</strong>, the value ranges from <strong>1</strong> to <strong>31</strong>. The digits refer to the dates in each month and separated by a comma, such as <strong>1,10,13,28</strong>.</li></ul>
    </td>
    </tr>
    <tr id="r4c08c4f22c3b4df1a3a5403eeddc4354"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="a0c2c51e444dd4e29ba2b60d5461e12c2"><a name="a0c2c51e444dd4e29ba2b60d5461e12c2"></a><a name="a0c2c51e444dd4e29ba2b60d5461e12c2"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020845960_p594178421079"><a name="en-us_topic_0020845960_p594178421079"></a><a name="en-us_topic_0020845960_p594178421079"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="a615a9f0c0305423db2f2ddf584c93d4b"><a name="a615a9f0c0305423db2f2ddf584c93d4b"></a><a name="a615a9f0c0305423db2f2ddf584c93d4b"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="a9fd1aed571e0410681f98248360eb0e0"><a name="a9fd1aed571e0410681f98248360eb0e0"></a><a name="a9fd1aed571e0410681f98248360eb0e0"></a>Specifies the start time of the scaling action triggered periodically. The time format complies with UTC.</p>
    <p id="aea18ea5bcc1d42469166346b0e654f95"><a name="aea18ea5bcc1d42469166346b0e654f95"></a><a name="aea18ea5bcc1d42469166346b0e654f95"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    <tr id="r2ca2a0e358dc475ca68e9d3916d479c5"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="ad750922d2cc94d0d9be7f5cfa9629ad0"><a name="ad750922d2cc94d0d9be7f5cfa9629ad0"></a><a name="ad750922d2cc94d0d9be7f5cfa9629ad0"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020845960_p481158781079"><a name="en-us_topic_0020845960_p481158781079"></a><a name="en-us_topic_0020845960_p481158781079"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="adfb428f0abfd4adc9ea6b4ac94f5357a"><a name="adfb428f0abfd4adc9ea6b4ac94f5357a"></a><a name="adfb428f0abfd4adc9ea6b4ac94f5357a"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="ad0f134288f51466e8329969670b77dd3"><a name="ad0f134288f51466e8329969670b77dd3"></a><a name="ad0f134288f51466e8329969670b77dd3"></a>Specifies the end time of the scaling action triggered periodically. The time format complies with UTC. This parameter is mandatory when <strong id="b842352706173440"><a name="b842352706173440"></a><a name="b842352706173440"></a>scaling_policy_type</strong> is set to <strong id="b842352706173444"><a name="b842352706173444"></a><a name="b842352706173444"></a>RECURRENCE</strong>.</p>
    <p id="af47b13bb74d8445098a267eecf33d26b"><a name="af47b13bb74d8445098a267eecf33d26b"></a><a name="af47b13bb74d8445098a267eecf33d26b"></a>When the scaling action is triggered periodically, the end time cannot be earlier than the current and start time.</p>
    <p id="aa2999aa7024c474389f0f97b6fe10b2f"><a name="aa2999aa7024c474389f0f97b6fe10b2f"></a><a name="aa2999aa7024c474389f0f97b6fe10b2f"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **scaling\_policy\_action**  field description

    <a name="t34390832ab524bcc8123c0f9a056064f"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063062_re1f0786afb8b4e88a8fc1ea46d03b82a"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="en-us_topic_0043063062_aec3e6ac917d14dfeb7ffb65860bb1306"><a name="en-us_topic_0043063062_aec3e6ac917d14dfeb7ffb65860bb1306"></a><a name="en-us_topic_0043063062_aec3e6ac917d14dfeb7ffb65860bb1306"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="en-us_topic_0043063062_p161699610619"><a name="en-us_topic_0043063062_p161699610619"></a><a name="en-us_topic_0043063062_p161699610619"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0043063062_adf1eacf282f34f0c87a7f239f00b4faf"><a name="en-us_topic_0043063062_adf1eacf282f34f0c87a7f239f00b4faf"></a><a name="en-us_topic_0043063062_adf1eacf282f34f0c87a7f239f00b4faf"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="en-us_topic_0043063062_adbb947caa2164ef080b97285f51e2ca4"><a name="en-us_topic_0043063062_adbb947caa2164ef080b97285f51e2ca4"></a><a name="en-us_topic_0043063062_adbb947caa2164ef080b97285f51e2ca4"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063062_r6132212f59bc42529826e44935a5cfaf"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0043063062_ae05d19776675443bb90e03221ee13658"><a name="en-us_topic_0043063062_ae05d19776675443bb90e03221ee13658"></a><a name="en-us_topic_0043063062_ae05d19776675443bb90e03221ee13658"></a>operation</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0043063062_p6386788410619"><a name="en-us_topic_0043063062_p6386788410619"></a><a name="en-us_topic_0043063062_p6386788410619"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0043063062_ab3f64183c0044f0cb0c72b8b7c381c66"><a name="en-us_topic_0043063062_ab3f64183c0044f0cb0c72b8b7c381c66"></a><a name="en-us_topic_0043063062_ab3f64183c0044f0cb0c72b8b7c381c66"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0043063062_a5c8d1942ad2246beaa196587336c303e"><a name="en-us_topic_0043063062_a5c8d1942ad2246beaa196587336c303e"></a><a name="en-us_topic_0043063062_a5c8d1942ad2246beaa196587336c303e"></a>Specifies the operation to be performed. The default operation is <strong>ADD</strong>.</p>
    <a name="en-us_topic_0043063062_ul17377291387"></a><a name="en-us_topic_0043063062_ul17377291387"></a><ul id="en-us_topic_0043063062_ul17377291387"><li><strong>ADD</strong>: adds specified number of instances to the AS group.</li><li><strong id="en-us_topic_0043063062_b84235270611343"><a name="en-us_topic_0043063062_b84235270611343"></a><a name="en-us_topic_0043063062_b84235270611343"></a>REMOVE/REDUCE</strong>: removes or reduces specified number of instances from the AS group.</li><li><strong>SET</strong>: sets the number of instances in the AS group.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0043063062_rd780cce224684db9a0a0fff71c2cc5ce"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0043063062_p26677605172946"><a name="en-us_topic_0043063062_p26677605172946"></a><a name="en-us_topic_0043063062_p26677605172946"></a>instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0043063062_p13402436172946"><a name="en-us_topic_0043063062_p13402436172946"></a><a name="en-us_topic_0043063062_p13402436172946"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0043063062_p11855564172946"><a name="en-us_topic_0043063062_p11855564172946"></a><a name="en-us_topic_0043063062_p11855564172946"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0043063062_p20776612172946"><a name="en-us_topic_0043063062_p20776612172946"></a><a name="en-us_topic_0043063062_p20776612172946"></a>Specifies the number of instances to be operated. The default number is <strong>1</strong>. The value range is as follows for a default quota:</p>
    <a name="en-us_topic_0043063062_ul897214318562"></a><a name="en-us_topic_0043063062_ul897214318562"></a><ul id="en-us_topic_0043063062_ul897214318562"><li>If <strong id="en-us_topic_0043063062_b12649189115414"><a name="en-us_topic_0043063062_b12649189115414"></a><a name="en-us_topic_0043063062_b12649189115414"></a>operation</strong> is set to <strong id="en-us_topic_0043063062_b976871918548"><a name="en-us_topic_0043063062_b976871918548"></a><a name="en-us_topic_0043063062_b976871918548"></a>SET</strong>, the value range is 0 to 200.</li><li>If <strong id="en-us_topic_0043063062_b13160165618541"><a name="en-us_topic_0043063062_b13160165618541"></a><a name="en-us_topic_0043063062_b13160165618541"></a>operation</strong> is set to <strong id="en-us_topic_0043063062_b2029714596546"><a name="en-us_topic_0043063062_b2029714596546"></a><a name="en-us_topic_0043063062_b2029714596546"></a>ADD</strong>, <strong id="en-us_topic_0043063062_b798416185520"><a name="en-us_topic_0043063062_b798416185520"></a><a name="en-us_topic_0043063062_b798416185520"></a>REMOVE</strong>, or <strong id="en-us_topic_0043063062_b7950192184120"><a name="en-us_topic_0043063062_b7950192184120"></a><a name="en-us_topic_0043063062_b7950192184120"></a>REDUCE</strong>, the value range is 1 to 200.</li></ul>
    <div class="note" id="en-us_topic_0043063062_note99603584562"><a name="en-us_topic_0043063062_note99603584562"></a><a name="en-us_topic_0043063062_note99603584562"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0043063062_p696175820561"><a name="en-us_topic_0043063062_p696175820561"></a><a name="en-us_topic_0043063062_p696175820561"></a>Either <strong id="en-us_topic_0043063062_b842352706105430"><a name="en-us_topic_0043063062_b842352706105430"></a><a name="en-us_topic_0043063062_b842352706105430"></a>instance_number</strong> or <strong id="en-us_topic_0043063062_b842352706105435"><a name="en-us_topic_0043063062_b842352706105435"></a><a name="en-us_topic_0043063062_b842352706105435"></a>instance_percentage</strong> is required.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0043063062_row4165649917933"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0043063062_p17249893172946"><a name="en-us_topic_0043063062_p17249893172946"></a><a name="en-us_topic_0043063062_p17249893172946"></a>instance_percentage</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0043063062_p55064094172946"><a name="en-us_topic_0043063062_p55064094172946"></a><a name="en-us_topic_0043063062_p55064094172946"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0043063062_p31006664172946"><a name="en-us_topic_0043063062_p31006664172946"></a><a name="en-us_topic_0043063062_p31006664172946"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0043063062_p083717531563"><a name="en-us_topic_0043063062_p083717531563"></a><a name="en-us_topic_0043063062_p083717531563"></a>Specifies the percentage of instances to be operated. You can increase, decrease, or set the number of instances in an AS group to the specified percentage of the current number of instances. If <strong id="en-us_topic_0043063062_b587711610207"><a name="en-us_topic_0043063062_b587711610207"></a><a name="en-us_topic_0043063062_b587711610207"></a>operation</strong> is set to <strong id="en-us_topic_0043063062_b7766189182012"><a name="en-us_topic_0043063062_b7766189182012"></a><a name="en-us_topic_0043063062_b7766189182012"></a>ADD</strong>, <strong id="en-us_topic_0043063062_b155020126201"><a name="en-us_topic_0043063062_b155020126201"></a><a name="en-us_topic_0043063062_b155020126201"></a>REMOVE</strong> or <strong id="en-us_topic_0043063062_b1958414415402"><a name="en-us_topic_0043063062_b1958414415402"></a><a name="en-us_topic_0043063062_b1958414415402"></a>REDUCE</strong>, the value of this parameter is an integer from 1 to 20000. If <strong id="en-us_topic_0043063062_b15177335112010"><a name="en-us_topic_0043063062_b15177335112010"></a><a name="en-us_topic_0043063062_b15177335112010"></a>operation</strong> is set to <strong id="en-us_topic_0043063062_b15787182814204"><a name="en-us_topic_0043063062_b15787182814204"></a><a name="en-us_topic_0043063062_b15787182814204"></a>SET</strong>, the value is an integer from 0 to 20000.</p>
    <p id="en-us_topic_0043063062_p55280357172946"><a name="en-us_topic_0043063062_p55280357172946"></a><a name="en-us_topic_0043063062_p55280357172946"></a>If neither <strong id="en-us_topic_0043063062_b8423527061122"><a name="en-us_topic_0043063062_b8423527061122"></a><a name="en-us_topic_0043063062_b8423527061122"></a>instance_number</strong> nor <strong id="en-us_topic_0043063062_b8423527061126"><a name="en-us_topic_0043063062_b8423527061126"></a><a name="en-us_topic_0043063062_b8423527061126"></a>instance_percentage</strong> is specified, the number of instances to be operated is 1.</p>
    <p id="en-us_topic_0043063062_p27761166172946"><a name="en-us_topic_0043063062_p27761166172946"></a><a name="en-us_topic_0043063062_p27761166172946"></a>Either <strong id="en-us_topic_0043063062_b317105073"><a name="en-us_topic_0043063062_b317105073"></a><a name="en-us_topic_0043063062_b317105073"></a>instance_number</strong> or <strong id="en-us_topic_0043063062_b1543533074"><a name="en-us_topic_0043063062_b1543533074"></a><a name="en-us_topic_0043063062_b1543533074"></a>instance_percentage</strong> is required.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    This example shows how to modify the periodic AS policy with ID  **0h327883-324n-4dzd-9c61-68d03ee191dd**  for an AS group with two instances. The modification is as follows: The AS policy name is changed to  **policy\_01**, and the modification is executed at 16:00 every day from 2016-01-08T17:31Z through 2016-02-08T17:31Z.

    ```
    PUT https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_policy/0h327883-324n-4dzd-9c61-68d03ee191dd
    
    {
        "scaling_policy_type": "RECURRENCE",
        "scaling_policy_name": "policy_01",
        "scheduled_policy": {
            "launch_time": "16:00",
            "recurrence_type": "Daily",
            "end_time": "2016-02-08T17:31Z",
            "start_time": "2016-01-08T17:31Z"
        },
        "scaling_policy_action": {
            "operation": "SET",
            "instance_number": 2
        }
    }
    ```


## Response Message<a name="section11877685"></a>

-   Response parameters

    <a name="table8914235"></a>
    <table><thead align="left"><tr id="row41110918"><th class="cellrowborder" valign="top" width="27.312731273127312%" id="mcps1.1.4.1.1"><p id="p41650091"><a name="p41650091"></a><a name="p41650091"></a><strong id="b5533173717545"><a name="b5533173717545"></a><a name="b5533173717545"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.682168216821683%" id="mcps1.1.4.1.2"><p id="p18214233"><a name="p18214233"></a><a name="p18214233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.00510051005101%" id="mcps1.1.4.1.3"><p id="p66066743"><a name="p66066743"></a><a name="p66066743"></a><strong id="b123320384541"><a name="b123320384541"></a><a name="b123320384541"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49805933"><td class="cellrowborder" valign="top" width="27.312731273127312%" headers="mcps1.1.4.1.1 "><p id="p7748772"><a name="p7748772"></a><a name="p7748772"></a>scaling_policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.682168216821683%" headers="mcps1.1.4.1.2 "><p id="p23670787"><a name="p23670787"></a><a name="p23670787"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.00510051005101%" headers="mcps1.1.4.1.3 "><p id="p38285619"><a name="p38285619"></a><a name="p38285619"></a>Specifies the AS policy ID.</p>
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


## Returned Values<a name="section39790309"></a>

-   Normal

    200

-   Abnormal

    <a name="table55108945"></a>
    <table><thead align="left"><tr id="row19299281"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p19737894"><a name="p19737894"></a><a name="p19737894"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p55265559"><a name="p55265559"></a><a name="p55265559"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47325326"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p8146160"><a name="p8146160"></a><a name="p8146160"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p55859239"><a name="p55859239"></a><a name="p55859239"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row32971110"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p53414263"><a name="p53414263"></a><a name="p53414263"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p31588048"><a name="p31588048"></a><a name="p31588048"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row15856984"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p9347313"><a name="p9347313"></a><a name="p9347313"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p18934887"><a name="p18934887"></a><a name="p18934887"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row36196256"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p46215595"><a name="p46215595"></a><a name="p46215595"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p52475719"><a name="p52475719"></a><a name="p52475719"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row2519427"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2747002"><a name="p2747002"></a><a name="p2747002"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p21180630"><a name="p21180630"></a><a name="p21180630"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row56407950"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p5641212"><a name="p5641212"></a><a name="p5641212"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p54284994"><a name="p54284994"></a><a name="p54284994"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row18802902"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p46640084"><a name="p46640084"></a><a name="p46640084"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p19750463"><a name="p19750463"></a><a name="p19750463"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row43536440"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p36790769"><a name="p36790769"></a><a name="p36790769"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p27262282"><a name="p27262282"></a><a name="p27262282"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row44033946"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p9979846"><a name="p9979846"></a><a name="p9979846"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p3061223"><a name="p3061223"></a><a name="p3061223"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row27551015"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p17039762"><a name="p17039762"></a><a name="p17039762"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p38043494"><a name="p38043494"></a><a name="p38043494"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row6847126"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p17746329"><a name="p17746329"></a><a name="p17746329"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p28166553"><a name="p28166553"></a><a name="p28166553"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row52172387"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p65213800"><a name="p65213800"></a><a name="p65213800"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p47826462"><a name="p47826462"></a><a name="p47826462"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row27784979"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p35990804"><a name="p35990804"></a><a name="p35990804"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p29574043"><a name="p29574043"></a><a name="p29574043"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row64839795"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p17532027"><a name="p17532027"></a><a name="p17532027"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p10808059"><a name="p10808059"></a><a name="p10808059"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

