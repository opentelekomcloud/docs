# Querying AS Policy Details<a name="EN-US_TOPIC_0043063043"></a>

## Function<a name="section54800025"></a>

This interface is used to query details about a specified AS policy by policy ID.

## URI<a name="section23438178"></a>

GET /autoscaling-api/v1/\{project\_id\}/scaling\_policy/\{scaling\_policy\_id\}

**Table  1**  Parameter description

<a name="table2322177"></a>
<table><thead align="left"><tr id="row50916422"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.1"><p id="p30589524"><a name="p30589524"></a><a name="p30589524"></a><strong id="b16740952175715"><a name="b16740952175715"></a><a name="b16740952175715"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p61832419"><a name="p61832419"></a><a name="p61832419"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p42370075"><a name="p42370075"></a><a name="p42370075"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42%" id="mcps1.2.5.1.4"><p id="p9424035"><a name="p9424035"></a><a name="p9424035"></a><strong id="b16568155313573"><a name="b16568155313573"></a><a name="b16568155313573"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row25149347"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p23831236"><a name="p23831236"></a><a name="p23831236"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p51281965"><a name="p51281965"></a><a name="p51281965"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p60198535"><a name="p60198535"></a><a name="p60198535"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row62644428"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p41033878"><a name="p41033878"></a><a name="p41033878"></a>scaling_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p35409804"><a name="p35409804"></a><a name="p35409804"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p49621912"><a name="p49621912"></a><a name="p49621912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p59951903"><a name="p59951903"></a><a name="p59951903"></a>Specifies the AS policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section9617010"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query details about the AS policy with ID  **fd7d63ce-8f5c-443e-b9a0-bef9386b23b3**.

    ```
    GET https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_policy/fd7d63ce-8f5c-443e-b9a0-bef9386b23b3
    ```


## Response Message<a name="section19444226"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table51227795"></a>
    <table><thead align="left"><tr id="row28165387"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p66803900"><a name="p66803900"></a><a name="p66803900"></a><strong id="b197965695718"><a name="b197965695718"></a><a name="b197965695718"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p42406858"><a name="p42406858"></a><a name="p42406858"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p12403484"><a name="p12403484"></a><a name="p12403484"></a><strong id="b0937145635719"><a name="b0937145635719"></a><a name="b0937145635719"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65158171"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p43320494"><a name="p43320494"></a><a name="p43320494"></a>scaling_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a4c03d226ca78442f99e13b8d363cd51d"><a name="a4c03d226ca78442f99e13b8d363cd51d"></a><a name="a4c03d226ca78442f99e13b8d363cd51d"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p19726002"><a name="p19726002"></a><a name="p19726002"></a>Specifies details about the AS policy. For details, see <a href="#t2a6ea1b88928469f849918033ac9b323">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scaling\_policy**  field description

    <a name="t2a6ea1b88928469f849918033ac9b323"></a>
    <table><thead align="left"><tr id="re7fc67a6f30742f184c131a457e53ca5"><th class="cellrowborder" valign="top" width="26.75%" id="mcps1.2.4.1.1"><p id="a2330d17810fb4b43a6ebbe9d04b2aa3b"><a name="a2330d17810fb4b43a6ebbe9d04b2aa3b"></a><a name="a2330d17810fb4b43a6ebbe9d04b2aa3b"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.3%" id="mcps1.2.4.1.2"><p id="aab479e40ee0346cb8a8b030caeeb0f84"><a name="aab479e40ee0346cb8a8b030caeeb0f84"></a><a name="aab479e40ee0346cb8a8b030caeeb0f84"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.949999999999996%" id="mcps1.2.4.1.3"><p id="ae40c31b78ab94c12a1a91a7295be29fb"><a name="ae40c31b78ab94c12a1a91a7295be29fb"></a><a name="ae40c31b78ab94c12a1a91a7295be29fb"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r1683eaa1734e43f5a12c575711758d16"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="a6abf6c7be3604db9b6c46839194a3a15"><a name="a6abf6c7be3604db9b6c46839194a3a15"></a><a name="a6abf6c7be3604db9b6c46839194a3a15"></a>scaling_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="ad538eb3174dc4989a6c0faf284230a81"><a name="ad538eb3174dc4989a6c0faf284230a81"></a><a name="ad538eb3174dc4989a6c0faf284230a81"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.949999999999996%" headers="mcps1.2.4.1.3 "><p id="a45b014225549462381f627ea62b55386"><a name="a45b014225549462381f627ea62b55386"></a><a name="a45b014225549462381f627ea62b55386"></a>Specifies the AS group ID.</p>
    </td>
    </tr>
    <tr id="re13fedab1aec49069bf8acce2001bbe9"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="a64d074b4826a446d99eebfaa0461c1c2"><a name="a64d074b4826a446d99eebfaa0461c1c2"></a><a name="a64d074b4826a446d99eebfaa0461c1c2"></a>scaling_policy_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="ac6391aa790b344d382bd9c6d90451154"><a name="ac6391aa790b344d382bd9c6d90451154"></a><a name="ac6391aa790b344d382bd9c6d90451154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.949999999999996%" headers="mcps1.2.4.1.3 "><p id="a4f14d62c607845018ba6ca369d5db676"><a name="a4f14d62c607845018ba6ca369d5db676"></a><a name="a4f14d62c607845018ba6ca369d5db676"></a>Specifies the AS policy name.</p>
    <p id="p759283241212"><a name="p759283241212"></a><a name="p759283241212"></a>Supports fuzzy search. </p>
    </td>
    </tr>
    <tr id="r045fa9d1df9340e1847f6d9d49fbe56c"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="a19c5fc7554914d9dbc27ad969f9f2010"><a name="a19c5fc7554914d9dbc27ad969f9f2010"></a><a name="a19c5fc7554914d9dbc27ad969f9f2010"></a>scaling_policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="a7463801383b6416c99eb0ea94f28e0a3"><a name="a7463801383b6416c99eb0ea94f28e0a3"></a><a name="a7463801383b6416c99eb0ea94f28e0a3"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.949999999999996%" headers="mcps1.2.4.1.3 "><p id="a92c30c4499884aa4a3e2ee2436960112"><a name="a92c30c4499884aa4a3e2ee2436960112"></a><a name="a92c30c4499884aa4a3e2ee2436960112"></a>Specifies the AS policy ID.</p>
    </td>
    </tr>
    <tr id="rcd972a9b2e6444b18a456387618e6186"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="ab5acea3930d44329bd0c741c06efb707"><a name="ab5acea3930d44329bd0c741c06efb707"></a><a name="ab5acea3930d44329bd0c741c06efb707"></a>policy_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="ad495ddbab5954c219019266b1440a8f5"><a name="ad495ddbab5954c219019266b1440a8f5"></a><a name="ad495ddbab5954c219019266b1440a8f5"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.949999999999996%" headers="mcps1.2.4.1.3 "><p id="a486f2eb901a04e03b7dcbca9913aa531"><a name="a486f2eb901a04e03b7dcbca9913aa531"></a><a name="a486f2eb901a04e03b7dcbca9913aa531"></a>Specifies the AS policy status.</p>
    <a name="u37a87bcee6664e788c30239a9d8bd359"></a><a name="u37a87bcee6664e788c30239a9d8bd359"></a><ul id="u37a87bcee6664e788c30239a9d8bd359"><li><strong id="b146004133475"><a name="b146004133475"></a><a name="b146004133475"></a>INSERVICE</strong>: The AS policy is enabled.</li><li><strong id="b119120160479"><a name="b119120160479"></a><a name="b119120160479"></a>PAUSED</strong>: The AS policy is disabled.</li><li><strong id="b168144171473"><a name="b168144171473"></a><a name="b168144171473"></a>EXECUTING</strong>: The AS policy is being executed.</li></ul>
    </td>
    </tr>
    <tr id="r1227084f4790495d98311413452978ca"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="a5acc905fa779462db9ce34d404d166dc"><a name="a5acc905fa779462db9ce34d404d166dc"></a><a name="a5acc905fa779462db9ce34d404d166dc"></a>scaling_policy_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="a53e43ad265c04294994adbbd71a4240a"><a name="a53e43ad265c04294994adbbd71a4240a"></a><a name="a53e43ad265c04294994adbbd71a4240a"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.949999999999996%" headers="mcps1.2.4.1.3 "><p id="a74e06dc4d9d0421bad729ced813c2fbf"><a name="a74e06dc4d9d0421bad729ced813c2fbf"></a><a name="a74e06dc4d9d0421bad729ced813c2fbf"></a>Specifies the AS policy type.</p>
    <a name="ua99da6c954d14b9f8e73af19c844fac9"></a><a name="ua99da6c954d14b9f8e73af19c844fac9"></a><ul id="ua99da6c954d14b9f8e73af19c844fac9"><li><strong>ALARM</strong>: indicates that the scaling action is triggered by an alarm. A value is returned for <strong>alarm_id</strong>, and no value is returned for <strong>scheduled_policy</strong>.</li><li><strong id="b842352706174318"><a name="b842352706174318"></a><a name="b842352706174318"></a>SCHEDULED</strong>: indicates that the scaling action is triggered as scheduled. A value is returned for <strong id="b842352706174359"><a name="b842352706174359"></a><a name="b842352706174359"></a>scheduled_policy</strong>, and no value is returned for <strong id="b842352706174456"><a name="b842352706174456"></a><a name="b842352706174456"></a>alarm_id</strong>, <strong id="b84235270617451"><a name="b84235270617451"></a><a name="b84235270617451"></a>recurrence_type</strong>, <strong id="b84235270617457"><a name="b84235270617457"></a><a name="b84235270617457"></a>recurrence_value</strong>, <strong id="b842352706174512"><a name="b842352706174512"></a><a name="b842352706174512"></a>start_time</strong>, or <strong id="b842352706174516"><a name="b842352706174516"></a><a name="b842352706174516"></a>end_time</strong>.</li><li><strong id="b1079706252"><a name="b1079706252"></a><a name="b1079706252"></a>RECURRENCE</strong>: indicates that the scaling action is triggered periodically. Values are returned for <strong id="b688988950"><a name="b688988950"></a><a name="b688988950"></a>scheduled_policy</strong>, <strong id="b1121671907174638"><a name="b1121671907174638"></a><a name="b1121671907174638"></a>recurrence_type</strong>, <strong id="b413073752174638"><a name="b413073752174638"></a><a name="b413073752174638"></a>recurrence_value</strong>, <strong id="b1481332545174638"><a name="b1481332545174638"></a><a name="b1481332545174638"></a>start_time</strong>, and <strong id="b331387069174638"><a name="b331387069174638"></a><a name="b331387069174638"></a>end_time</strong>, and no value is returned for <strong id="b1395089429"><a name="b1395089429"></a><a name="b1395089429"></a>alarm_id</strong>.</li></ul>
    </td>
    </tr>
    <tr id="re6c8601d7735402289d3df1aa513dd38"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="ae4c58dc938a244639096cf46c69ea43c"><a name="ae4c58dc938a244639096cf46c69ea43c"></a><a name="ae4c58dc938a244639096cf46c69ea43c"></a>alarm_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="a37e95fc8ec0e48dc95603de5d5f327da"><a name="a37e95fc8ec0e48dc95603de5d5f327da"></a><a name="a37e95fc8ec0e48dc95603de5d5f327da"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.949999999999996%" headers="mcps1.2.4.1.3 "><p id="a623ce02737344aeab494b0d1af22e05e"><a name="a623ce02737344aeab494b0d1af22e05e"></a><a name="a623ce02737344aeab494b0d1af22e05e"></a>Specifies the alarm ID.</p>
    </td>
    </tr>
    <tr id="r4076ad4eb9d04e35ab070a631c2933a1"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="ae25c25829e9e4e909498fa48248176dc"><a name="ae25c25829e9e4e909498fa48248176dc"></a><a name="ae25c25829e9e4e909498fa48248176dc"></a>scheduled_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="p48071024318"><a name="p48071024318"></a><a name="p48071024318"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.949999999999996%" headers="mcps1.2.4.1.3 "><p id="a181fa2e6e6cd40f7a909d92a134fd7e1"><a name="a181fa2e6e6cd40f7a909d92a134fd7e1"></a><a name="a181fa2e6e6cd40f7a909d92a134fd7e1"></a>Specifies the periodic or scheduled AS policy. For details, see <a href="#t651e0a18c39047e8b0a9be40295e858c">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="r12e92bd949a14326a63ce9d7fd818a29"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="a1b0d050a78c24b6eb7523a36622f423f"><a name="a1b0d050a78c24b6eb7523a36622f423f"></a><a name="a1b0d050a78c24b6eb7523a36622f423f"></a>scaling_policy_action</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="p1580941264312"><a name="p1580941264312"></a><a name="p1580941264312"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.949999999999996%" headers="mcps1.2.4.1.3 "><p id="aed4902e2ba7445f7be377a690a18fd3a"><a name="aed4902e2ba7445f7be377a690a18fd3a"></a><a name="aed4902e2ba7445f7be377a690a18fd3a"></a>Specifies the scaling action of the AS policy. For details, see <a href="#te023df2ee8be4d3b801cdd19ea6c9844">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="rc6a22a7abdae451eb4870e4e1a0b0246"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="af63d2fb7c0ee4d7ebdd03a38d9a4e133"><a name="af63d2fb7c0ee4d7ebdd03a38d9a4e133"></a><a name="af63d2fb7c0ee4d7ebdd03a38d9a4e133"></a>cool_down_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="a28e9d3c14d4b442e82f14e6001fb23cd"><a name="a28e9d3c14d4b442e82f14e6001fb23cd"></a><a name="a28e9d3c14d4b442e82f14e6001fb23cd"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.949999999999996%" headers="mcps1.2.4.1.3 "><p id="a3d33cb93dd934726b19effc167b03466"><a name="a3d33cb93dd934726b19effc167b03466"></a><a name="a3d33cb93dd934726b19effc167b03466"></a>Specifies the cooldown period (s).</p>
    </td>
    </tr>
    <tr id="r0e00840d49e84352b06ead2720ff0097"><td class="cellrowborder" valign="top" width="26.75%" headers="mcps1.2.4.1.1 "><p id="a221a388b4c184276ab6e809b0393fd34"><a name="a221a388b4c184276ab6e809b0393fd34"></a><a name="a221a388b4c184276ab6e809b0393fd34"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="a8b5669595594430cbc04610bc6c7709b"><a name="a8b5669595594430cbc04610bc6c7709b"></a><a name="a8b5669595594430cbc04610bc6c7709b"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.949999999999996%" headers="mcps1.2.4.1.3 "><p id="a591a730d8d71490f902f01d310f929d0"><a name="a591a730d8d71490f902f01d310f929d0"></a><a name="a591a730d8d71490f902f01d310f929d0"></a>Specifies the time when an AS policy was created. The time format complies with UTC.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **scheduled\_policy**  field description

    <a name="t651e0a18c39047e8b0a9be40295e858c"></a>
    <table><thead align="left"><tr id="r70c860c3c45345fab0a3c5259a71c71a"><th class="cellrowborder" valign="top" width="26.57%" id="mcps1.2.4.1.1"><p id="aa6989ce6997340d198939fde85c773a1"><a name="aa6989ce6997340d198939fde85c773a1"></a><a name="aa6989ce6997340d198939fde85c773a1"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.3%" id="mcps1.2.4.1.2"><p id="a9380e820b72c4d2eaa2941846ffd7b37"><a name="a9380e820b72c4d2eaa2941846ffd7b37"></a><a name="a9380e820b72c4d2eaa2941846ffd7b37"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.13%" id="mcps1.2.4.1.3"><p id="a7959c4611a6b4147b637a8638dfe5e77"><a name="a7959c4611a6b4147b637a8638dfe5e77"></a><a name="a7959c4611a6b4147b637a8638dfe5e77"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="re705198ad97743a3a1446f281bc76925"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="acfd712cbb76e412b909d12ea3430db52"><a name="acfd712cbb76e412b909d12ea3430db52"></a><a name="acfd712cbb76e412b909d12ea3430db52"></a>launch_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="ac57bde3a2c304b888b6ac396e12672d1"><a name="ac57bde3a2c304b888b6ac396e12672d1"></a><a name="ac57bde3a2c304b888b6ac396e12672d1"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="a775ce34e70a947da96cf6e2634aaa65d"><a name="a775ce34e70a947da96cf6e2634aaa65d"></a><a name="a775ce34e70a947da96cf6e2634aaa65d"></a>Specifies the time when the scaling action is triggered. The time format complies with UTC.</p>
    <a name="ua100c9e0b46e42e89dc8bd38e170207b"></a><a name="ua100c9e0b46e42e89dc8bd38e170207b"></a><ul id="ua100c9e0b46e42e89dc8bd38e170207b"><li>If <strong>scaling_policy_type</strong> is set to <strong>SCHEDULED</strong>, the time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</li><li>If <strong>scaling_policy_type</strong> is set to <strong>RECURRENCE</strong>, the time format is <strong>hh:mm</strong>.</li></ul>
    </td>
    </tr>
    <tr id="r471a85b072ff47338816f1925a59cff5"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="a465461555f5249238b99265def2f1bda"><a name="a465461555f5249238b99265def2f1bda"></a><a name="a465461555f5249238b99265def2f1bda"></a>recurrence_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="aece703b64e4f4d2c98a7772fab81572c"><a name="aece703b64e4f4d2c98a7772fab81572c"></a><a name="aece703b64e4f4d2c98a7772fab81572c"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="a09ebdaa3cca44f1392b26efafc92f5af"><a name="a09ebdaa3cca44f1392b26efafc92f5af"></a><a name="a09ebdaa3cca44f1392b26efafc92f5af"></a>Specifies the type of a periodically triggered scaling action.</p>
    <a name="ul81291706320"></a><a name="ul81291706320"></a><ul id="ul81291706320"><li><strong>Daily</strong>: indicates that the scaling action is triggered once a day.</li><li><strong>Weekly</strong>: indicates that the scaling action is triggered once a week.</li><li><strong>Monthly</strong>: indicates that the scaling action is triggered once a month.</li></ul>
    </td>
    </tr>
    <tr id="r9d4a440c2dd14f039b26e5a700cf1745"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="a5c865f47baad4350bc82f3c1911fe134"><a name="a5c865f47baad4350bc82f3c1911fe134"></a><a name="a5c865f47baad4350bc82f3c1911fe134"></a>recurrence_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="a27b1d2ae1784451f8898e4c1eced139a"><a name="a27b1d2ae1784451f8898e4c1eced139a"></a><a name="a27b1d2ae1784451f8898e4c1eced139a"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="a62556f878eae4c52aa03fb3b1c0c4d79"><a name="a62556f878eae4c52aa03fb3b1c0c4d79"></a><a name="a62556f878eae4c52aa03fb3b1c0c4d79"></a>Specifies the frequency at which scaling actions are triggered.</p>
    <a name="u8b21647227e64c63a492ba84439b7fe0"></a><a name="u8b21647227e64c63a492ba84439b7fe0"></a><ul id="u8b21647227e64c63a492ba84439b7fe0"><li>If <strong>recurrence_type</strong> is set to <strong>Daily</strong>, the value is <strong>null</strong>, indicating that the scaling action is triggered once a day.</li><li>If <strong>recurrence_type</strong> is set to <strong>Weekly</strong>, the value ranges from <strong>1</strong> (Sunday) to <strong>7</strong> (Saturday). The digits refer to dates in each week and separated by a comma, such as <strong>1,3,5</strong>.</li><li>If <strong id="b84235270617528"><a name="b84235270617528"></a><a name="b84235270617528"></a>recurrence_type</strong> is set to <strong>Monthly</strong>, the value ranges from <strong>1</strong> to <strong>31</strong>. The digits refer to the dates in each month and separated by a comma, such as <strong>1,10,13,28</strong>.</li></ul>
    </td>
    </tr>
    <tr id="r369c897c21b547b885c942156fea7164"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="a1fbe8e6217d24874b4d1b5ff97855bb5"><a name="a1fbe8e6217d24874b4d1b5ff97855bb5"></a><a name="a1fbe8e6217d24874b4d1b5ff97855bb5"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="a1d115943644144b8a94203800bb02a3f"><a name="a1d115943644144b8a94203800bb02a3f"></a><a name="a1d115943644144b8a94203800bb02a3f"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="a9a8c3a3fbc8f4337966ef7af365e1fea"><a name="a9a8c3a3fbc8f4337966ef7af365e1fea"></a><a name="a9a8c3a3fbc8f4337966ef7af365e1fea"></a>Specifies the start time of the scaling action triggered periodically. The time format complies with UTC.</p>
    <p id="a7783b07bff6c401ab7f33d7c4d461bc7"><a name="a7783b07bff6c401ab7f33d7c4d461bc7"></a><a name="a7783b07bff6c401ab7f33d7c4d461bc7"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    <tr id="r42dc7a56b9954ba9b8f8ef36981787c0"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="ac12e80cb48d74a03a66f8f346d318a43"><a name="ac12e80cb48d74a03a66f8f346d318a43"></a><a name="ac12e80cb48d74a03a66f8f346d318a43"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="a4aba6ac61ebc45bcb5629a79688d901c"><a name="a4aba6ac61ebc45bcb5629a79688d901c"></a><a name="a4aba6ac61ebc45bcb5629a79688d901c"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="af79d800631784861b9121cf1b2f58470"><a name="af79d800631784861b9121cf1b2f58470"></a><a name="af79d800631784861b9121cf1b2f58470"></a>Specifies the end time of the scaling action triggered periodically. The time format complies with UTC.</p>
    <p id="a2ceaf265f4014cb6abed4109aed80988"><a name="a2ceaf265f4014cb6abed4109aed80988"></a><a name="a2ceaf265f4014cb6abed4109aed80988"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **scaling\_policy\_action**  field description

    <a name="te023df2ee8be4d3b801cdd19ea6c9844"></a>
    <table><thead align="left"><tr id="rc005130818ef46b88be52c086600191e"><th class="cellrowborder" valign="top" width="26.57%" id="mcps1.2.4.1.1"><p id="a5befe73ee04d42baba72ffdaf366d0fd"><a name="a5befe73ee04d42baba72ffdaf366d0fd"></a><a name="a5befe73ee04d42baba72ffdaf366d0fd"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.3%" id="mcps1.2.4.1.2"><p id="a8575ed2abca747368ed26f4cdce2485b"><a name="a8575ed2abca747368ed26f4cdce2485b"></a><a name="a8575ed2abca747368ed26f4cdce2485b"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.13%" id="mcps1.2.4.1.3"><p id="a865b54f8ccb94e55aa1d4901167d50b1"><a name="a865b54f8ccb94e55aa1d4901167d50b1"></a><a name="a865b54f8ccb94e55aa1d4901167d50b1"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rd13af8ee8bdb43fbbec69c5d477c2ab1"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="a732867155f88459191bfeac9ec81e99a"><a name="a732867155f88459191bfeac9ec81e99a"></a><a name="a732867155f88459191bfeac9ec81e99a"></a>operation</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="a7a143b52935e4c7585c9f86d90b77021"><a name="a7a143b52935e4c7585c9f86d90b77021"></a><a name="a7a143b52935e4c7585c9f86d90b77021"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="ac324300c4cb34a45b4e0000493499503"><a name="ac324300c4cb34a45b4e0000493499503"></a><a name="ac324300c4cb34a45b4e0000493499503"></a>Specifies the scaling action.</p>
    <a name="ul539153022"></a><a name="ul539153022"></a><ul id="ul539153022"><li><strong id="b5907351145015"><a name="b5907351145015"></a><a name="b5907351145015"></a>ADD</strong>: adds specified number of instances to the AS group.</li><li><strong id="b447635814477"><a name="b447635814477"></a><a name="b447635814477"></a>REMOVE</strong>: removes specified number of instances from the AS group.</li><li><strong>SET</strong>: sets the number of instances in the AS group.</li></ul>
    </td>
    </tr>
    <tr id="r3366c359b5bc4333bdef2734871d66f5"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="a423f634b5eaf432b9a81eb771bcbd4d3"><a name="a423f634b5eaf432b9a81eb771bcbd4d3"></a><a name="a423f634b5eaf432b9a81eb771bcbd4d3"></a>instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="ae29f514cb9844cccb25925cae2b198ad"><a name="ae29f514cb9844cccb25925cae2b198ad"></a><a name="ae29f514cb9844cccb25925cae2b198ad"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="ac0f067fd4e4f46e99b1dd442e975b2c3"><a name="ac0f067fd4e4f46e99b1dd442e975b2c3"></a><a name="ac0f067fd4e4f46e99b1dd442e975b2c3"></a>Specifies the number of instances to be operated.</p>
    </td>
    </tr>
    <tr id="row20622786173125"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="p29296277173128"><a name="p29296277173128"></a><a name="p29296277173128"></a>instance_percentage</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="p24188207173128"><a name="p24188207173128"></a><a name="p24188207173128"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="p13087733173128"><a name="p13087733173128"></a><a name="p13087733173128"></a>Specifies the percentage of instances to be operated.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "scaling_policy": {
            "scaling_policy_id": "fd7d63ce-8f5c-443e-b9a0-bef9386b23b3",
            "scaling_group_id": "e5d27f5c-dd76-4a61-b4bc-a67c5686719a",
    "scaling_policy_name": "Scheduled 1",
            "scaling_policy_type": "SCHEDULED",
            "scheduled_policy": {
                "launch_time": "2015-07-24T01:21Z"
            },
            "cool_down_time": 300,
            "scaling_policy_action": {
                "operation": "REMOVE",
                "instance_number": 1
            },
            "policy_status": "INSERVICE",
            "create_time": "2015-07-24T01:09:30Z"
        }
    }
    ```


## Returned Values<a name="section40780307"></a>

-   Normal

    200

-   Abnormal

    <a name="table29346720"></a>
    <table><thead align="left"><tr id="row9393336"><th class="cellrowborder" valign="top" width="44.36%" id="mcps1.1.3.1.1"><p id="p22662742"><a name="p22662742"></a><a name="p22662742"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.64%" id="mcps1.1.3.1.2"><p id="p23742817"><a name="p23742817"></a><a name="p23742817"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44120000"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p16950236"><a name="p16950236"></a><a name="p16950236"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p30791836"><a name="p30791836"></a><a name="p30791836"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row8691069"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p32887983"><a name="p32887983"></a><a name="p32887983"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p46680953"><a name="p46680953"></a><a name="p46680953"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row17475399"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p6221225"><a name="p6221225"></a><a name="p6221225"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p34157240"><a name="p34157240"></a><a name="p34157240"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row38979707"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p3239736"><a name="p3239736"></a><a name="p3239736"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p61092053"><a name="p61092053"></a><a name="p61092053"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row12957567"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p42930000"><a name="p42930000"></a><a name="p42930000"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p54777941"><a name="p54777941"></a><a name="p54777941"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row23239422"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p3345069"><a name="p3345069"></a><a name="p3345069"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p2515205"><a name="p2515205"></a><a name="p2515205"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row22636847"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p21645334"><a name="p21645334"></a><a name="p21645334"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p8441658"><a name="p8441658"></a><a name="p8441658"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row8866062"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p47062423"><a name="p47062423"></a><a name="p47062423"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p53959953"><a name="p53959953"></a><a name="p53959953"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row15877536"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p11012038"><a name="p11012038"></a><a name="p11012038"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p19559856"><a name="p19559856"></a><a name="p19559856"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row41820978"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p32056062"><a name="p32056062"></a><a name="p32056062"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p46404226"><a name="p46404226"></a><a name="p46404226"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row14984857"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p5813925"><a name="p5813925"></a><a name="p5813925"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p1165950"><a name="p1165950"></a><a name="p1165950"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row10493555"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p44671593"><a name="p44671593"></a><a name="p44671593"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p61629280"><a name="p61629280"></a><a name="p61629280"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row17792611"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p31915390"><a name="p31915390"></a><a name="p31915390"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p35009773"><a name="p35009773"></a><a name="p35009773"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row46652504"><td class="cellrowborder" valign="top" width="44.36%" headers="mcps1.1.3.1.1 "><p id="p20756449"><a name="p20756449"></a><a name="p20756449"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.1.3.1.2 "><p id="p3550770"><a name="p3550770"></a><a name="p3550770"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

