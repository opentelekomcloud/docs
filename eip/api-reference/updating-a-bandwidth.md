# Updating a Bandwidth<a name="eip_apiBandwidth_0003"></a>

## Function<a name="en-us_topic_0201534310_section16581154"></a>

This API is used to update information about a bandwidth.

## URI<a name="en-us_topic_0201534310_section15012662"></a>

PUT /v1/\{project\_id\}/bandwidths/\{bandwidth\_id\}

[Table 1](#en-us_topic_0201534310_table25281875)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534310_table25281875"></a>
<table><thead align="left"><tr id="en-us_topic_0201534310_row26712487"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534310_p16227847"><a name="en-us_topic_0201534310_p16227847"></a><a name="en-us_topic_0201534310_p16227847"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534310_p39387211"><a name="en-us_topic_0201534310_p39387211"></a><a name="en-us_topic_0201534310_p39387211"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534310_p36247516"><a name="en-us_topic_0201534310_p36247516"></a><a name="en-us_topic_0201534310_p36247516"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534310_row50367649"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p53247746"><a name="en-us_topic_0201534310_p53247746"></a><a name="en-us_topic_0201534310_p53247746"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p18100201"><a name="en-us_topic_0201534310_p18100201"></a><a name="en-us_topic_0201534310_p18100201"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534310_p10487112"><a name="en-us_topic_0201534310_p10487112"></a><a name="en-us_topic_0201534310_p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="en-us_topic_0201534310_row41709209"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p23002745"><a name="en-us_topic_0201534310_p23002745"></a><a name="en-us_topic_0201534310_p23002745"></a>bandwidth_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p51283066"><a name="en-us_topic_0201534310_p51283066"></a><a name="en-us_topic_0201534310_p51283066"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534310_p60287683"><a name="en-us_topic_0201534310_p60287683"></a><a name="en-us_topic_0201534310_p60287683"></a>Specifies the bandwidth ID, which uniquely identifies the bandwidth.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534310_section896237"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="en-us_topic_0201534310_table3057854815556"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534310_row6286666315556"><th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534310_p5903494715556"><a name="en-us_topic_0201534310_p5903494715556"></a><a name="en-us_topic_0201534310_p5903494715556"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534310_p1710139915556"><a name="en-us_topic_0201534310_p1710139915556"></a><a name="en-us_topic_0201534310_p1710139915556"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.380000000000003%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534310_p4303610815556"><a name="en-us_topic_0201534310_p4303610815556"></a><a name="en-us_topic_0201534310_p4303610815556"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.47%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534310_p6337274615556"><a name="en-us_topic_0201534310_p6337274615556"></a><a name="en-us_topic_0201534310_p6337274615556"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534310_row3291877615556"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534310_p4917516615556"><a name="en-us_topic_0201534310_p4917516615556"></a><a name="en-us_topic_0201534310_p4917516615556"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534310_p2376550915556"><a name="en-us_topic_0201534310_p2376550915556"></a><a name="en-us_topic_0201534310_p2376550915556"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.380000000000003%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534310_p4595806815556"><a name="en-us_topic_0201534310_p4595806815556"></a><a name="en-us_topic_0201534310_p4595806815556"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534310_p1610901815556"><a name="en-us_topic_0201534310_p1610901815556"></a><a name="en-us_topic_0201534310_p1610901815556"></a>Specifies the bandwidth objects. For details, see <a href="#en-us_topic_0201534310_table31854691">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **bandwidth**  field

    <a name="en-us_topic_0201534310_table31854691"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534310_row6882862"><th class="cellrowborder" valign="top" width="13.350000000000001%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534310_p20640979"><a name="en-us_topic_0201534310_p20640979"></a><a name="en-us_topic_0201534310_p20640979"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.17%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534310_p61306625"><a name="en-us_topic_0201534310_p61306625"></a><a name="en-us_topic_0201534310_p61306625"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.229999999999999%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534310_p5200653172316"><a name="en-us_topic_0201534310_p5200653172316"></a><a name="en-us_topic_0201534310_p5200653172316"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.25%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534310_p66889567"><a name="en-us_topic_0201534310_p66889567"></a><a name="en-us_topic_0201534310_p66889567"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534310_row49345813"><td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534310_p37587916"><a name="en-us_topic_0201534310_p37587916"></a><a name="en-us_topic_0201534310_p37587916"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534310_p24722347"><a name="en-us_topic_0201534310_p24722347"></a><a name="en-us_topic_0201534310_p24722347"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534310_p18599757172316"><a name="en-us_topic_0201534310_p18599757172316"></a><a name="en-us_topic_0201534310_p18599757172316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.25%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0201534310_ul5677198174113"></a><a name="en-us_topic_0201534310_ul5677198174113"></a><ul id="en-us_topic_0201534310_ul5677198174113"><li>Specifies the bandwidth name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.). If the value is left blank, the name of the bandwidth is not changed.</li><li>Either parameter <strong id="en-us_topic_0201534310_b84235270621475"><a name="en-us_topic_0201534310_b84235270621475"></a><a name="en-us_topic_0201534310_b84235270621475"></a>name</strong> or <strong id="en-us_topic_0201534310_b84235270621478"><a name="en-us_topic_0201534310_b84235270621478"></a><a name="en-us_topic_0201534310_b84235270621478"></a>size</strong> must be specified.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534310_row10796581"><td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534310_p2107829"><a name="en-us_topic_0201534310_p2107829"></a><a name="en-us_topic_0201534310_p2107829"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534310_p36516433"><a name="en-us_topic_0201534310_p36516433"></a><a name="en-us_topic_0201534310_p36516433"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534310_p30185329172316"><a name="en-us_topic_0201534310_p30185329172316"></a><a name="en-us_topic_0201534310_p30185329172316"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.25%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0201534310_ul1396719655311"></a><a name="en-us_topic_0201534310_ul1396719655311"></a><ul id="en-us_topic_0201534310_ul1396719655311"><li>Specifies the bandwidth size in Mbit/s.</li><li>The value ranges from 1 Mbit/s to 1000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the available bandwidth range on the management console.) If the parameter is not included, the bandwidth size is not changed.</li><li>Either parameter <strong id="en-us_topic_0201534310_b2045315149"><a name="en-us_topic_0201534310_b2045315149"></a><a name="en-us_topic_0201534310_b2045315149"></a>name</strong> or <strong id="en-us_topic_0201534310_b1434415927"><a name="en-us_topic_0201534310_b1434415927"></a><a name="en-us_topic_0201534310_b1434415927"></a>size</strong> must be specified.</li><li>If a decimal fraction (for example <strong>10.2</strong>) or a character string (for example <strong>"10"</strong>) is specified, the specified value will be automatically converted to an integer.</li><li>The minimum unit for bandwidth adjustment varies depending on the bandwidth range. The details are as follows:<a name="en-us_topic_0201534310_ul9790510185"></a><a name="en-us_topic_0201534310_ul9790510185"></a><ul id="en-us_topic_0201534310_ul9790510185"><li>The minimum unit is 1 Mbit/s if the allowed bandwidth size ranges from 0 to 300 Mbit/s (with 300 Mbit/s included).</li><li>The minimum unit is 50 Mbit/s if the allowed bandwidth size ranges 300 Mbit/s to 1000 Mbit/s (with 1000 Mbit/s included).</li><li>The minimum unit is 500 Mbit/s if the allowed bandwidth size is greater than 1000 Mbit/s.</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    PUT https://{Endpoint}/v1/{project_id}/bandwidths/{bandwidth_id} 
    
    {
        "bandwidth":
            {"name": "bandwidth123",
             "size": 10
            }
    }
    ```


## Response Message<a name="en-us_topic_0201534310_section8066134"></a>

-   Response parameter

    **Table  4**  Response parameter

    <a name="en-us_topic_0201534310_table58151089155516"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534310_row25417629155516"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534310_p45562050155516"><a name="en-us_topic_0201534310_p45562050155516"></a><a name="en-us_topic_0201534310_p45562050155516"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534310_p29734214155516"><a name="en-us_topic_0201534310_p29734214155516"></a><a name="en-us_topic_0201534310_p29734214155516"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534310_p59661173155516"><a name="en-us_topic_0201534310_p59661173155516"></a><a name="en-us_topic_0201534310_p59661173155516"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534310_row716877155516"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p58067061155516"><a name="en-us_topic_0201534310_p58067061155516"></a><a name="en-us_topic_0201534310_p58067061155516"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p967638155516"><a name="en-us_topic_0201534310_p967638155516"></a><a name="en-us_topic_0201534310_p967638155516"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534310_p34319839155516"><a name="en-us_topic_0201534310_p34319839155516"></a><a name="en-us_topic_0201534310_p34319839155516"></a>Specifies the bandwidth objects. For details, see <a href="#en-us_topic_0201534310_table17227723">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Description of the  **bandwidths**  field

    <a name="en-us_topic_0201534310_table17227723"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534310_row57600065"><th class="cellrowborder" valign="top" width="26.730000000000004%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534310_p35093725"><a name="en-us_topic_0201534310_p35093725"></a><a name="en-us_topic_0201534310_p35093725"></a><strong id="en-us_topic_0201534310_b1051561924911"><a name="en-us_topic_0201534310_b1051561924911"></a><a name="en-us_topic_0201534310_b1051561924911"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.92%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534310_p42606680172022"><a name="en-us_topic_0201534310_p42606680172022"></a><a name="en-us_topic_0201534310_p42606680172022"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.35000000000001%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534310_p66526832"><a name="en-us_topic_0201534310_p66526832"></a><a name="en-us_topic_0201534310_p66526832"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534310_row19964345"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p6499254"><a name="en-us_topic_0201534310_p6499254"></a><a name="en-us_topic_0201534310_p6499254"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p28589065172022"><a name="en-us_topic_0201534310_p28589065172022"></a><a name="en-us_topic_0201534310_p28589065172022"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534310_ul1630720166145"></a><a name="en-us_topic_0201534310_ul1630720166145"></a><ul id="en-us_topic_0201534310_ul1630720166145"><li>Specifies the bandwidth name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534310_row11415673"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p52254296"><a name="en-us_topic_0201534310_p52254296"></a><a name="en-us_topic_0201534310_p52254296"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p34012930172022"><a name="en-us_topic_0201534310_p34012930172022"></a><a name="en-us_topic_0201534310_p34012930172022"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534310_ul1730751620144"></a><a name="en-us_topic_0201534310_ul1730751620144"></a><ul id="en-us_topic_0201534310_ul1730751620144"><li>Specifies the bandwidth size in Mbit/s.</li><li>The value ranges from 1 Mbit/s to 2000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the available bandwidth range on the management console.)</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534310_row24927872"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p5891777"><a name="en-us_topic_0201534310_p5891777"></a><a name="en-us_topic_0201534310_p5891777"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p3583980172022"><a name="en-us_topic_0201534310_p3583980172022"></a><a name="en-us_topic_0201534310_p3583980172022"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534310_p11246416"><a name="en-us_topic_0201534310_p11246416"></a><a name="en-us_topic_0201534310_p11246416"></a>Specifies the bandwidth ID, which uniquely identifies the bandwidth.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534310_row34108880"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p11355891"><a name="en-us_topic_0201534310_p11355891"></a><a name="en-us_topic_0201534310_p11355891"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p21866991172022"><a name="en-us_topic_0201534310_p21866991172022"></a><a name="en-us_topic_0201534310_p21866991172022"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534310_ul540194517378"></a><a name="en-us_topic_0201534310_ul540194517378"></a><ul id="en-us_topic_0201534310_ul540194517378"><li>The value is <strong id="en-us_topic_0201534310_b25288513165924"><a name="en-us_topic_0201534310_b25288513165924"></a><a name="en-us_topic_0201534310_b25288513165924"></a>PER</strong>, indicating that the bandwidth is dedicated.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534310_row49955752"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p19884118"><a name="en-us_topic_0201534310_p19884118"></a><a name="en-us_topic_0201534310_p19884118"></a>publicip_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p26395826172022"><a name="en-us_topic_0201534310_p26395826172022"></a><a name="en-us_topic_0201534310_p26395826172022"></a>Array of <a href="#en-us_topic_0201534310_table30936422">publicip_info</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534310_ul154130570376"></a><a name="en-us_topic_0201534310_ul154130570376"></a><ul id="en-us_topic_0201534310_ul154130570376"><li>Specifies information about the EIP that uses the bandwidth. For details, see <a href="#en-us_topic_0201534310_table30936422">Table 6</a>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534310_row12794876"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p29752015"><a name="en-us_topic_0201534310_p29752015"></a><a name="en-us_topic_0201534310_p29752015"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p57687133172022"><a name="en-us_topic_0201534310_p57687133172022"></a><a name="en-us_topic_0201534310_p57687133172022"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534310_p1539621310512"><a name="en-us_topic_0201534310_p1539621310512"></a><a name="en-us_topic_0201534310_p1539621310512"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534310_row29288625"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p23568445"><a name="en-us_topic_0201534310_p23568445"></a><a name="en-us_topic_0201534310_p23568445"></a>bandwidth_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p42146201172022"><a name="en-us_topic_0201534310_p42146201172022"></a><a name="en-us_topic_0201534310_p42146201172022"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534310_ul12723142619163"></a><a name="en-us_topic_0201534310_ul12723142619163"></a><ul id="en-us_topic_0201534310_ul12723142619163"><li>Specifies the bandwidth type.</li><li>The value is <strong id="en-us_topic_0201534310_b756116538522"><a name="en-us_topic_0201534310_b756116538522"></a><a name="en-us_topic_0201534310_b756116538522"></a>bgp</strong>. </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534310_row58843898173344"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p18916883173347"><a name="en-us_topic_0201534310_p18916883173347"></a><a name="en-us_topic_0201534310_p18916883173347"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p29386093173347"><a name="en-us_topic_0201534310_p29386093173347"></a><a name="en-us_topic_0201534310_p29386093173347"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534310_ul19561144916384"></a><a name="en-us_topic_0201534310_ul19561144916384"></a><ul id="en-us_topic_0201534310_ul19561144916384"><li>If the value is <strong id="en-us_topic_0201534310_b164011341133220"><a name="en-us_topic_0201534310_b164011341133220"></a><a name="en-us_topic_0201534310_b164011341133220"></a>traffic</strong>, the bandwidth is billed by traffic.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **publicip\_info**  objects

    <a name="en-us_topic_0201534310_table30936422"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534310_row17161430"><th class="cellrowborder" valign="top" width="25.740000000000002%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534310_p47898561"><a name="en-us_topic_0201534310_p47898561"></a><a name="en-us_topic_0201534310_p47898561"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.5%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534310_p2828296517154"><a name="en-us_topic_0201534310_p2828296517154"></a><a name="en-us_topic_0201534310_p2828296517154"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.76%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534310_p58761073"><a name="en-us_topic_0201534310_p58761073"></a><a name="en-us_topic_0201534310_p58761073"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534310_row62026502"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p58090788"><a name="en-us_topic_0201534310_p58090788"></a><a name="en-us_topic_0201534310_p58090788"></a>publicip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p921881117154"><a name="en-us_topic_0201534310_p921881117154"></a><a name="en-us_topic_0201534310_p921881117154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534310_p476380"><a name="en-us_topic_0201534310_p476380"></a><a name="en-us_topic_0201534310_p476380"></a>Specifies the ID of the EIP that uses the bandwidth.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534310_row4287423"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p108302031181710"><a name="en-us_topic_0201534310_p108302031181710"></a><a name="en-us_topic_0201534310_p108302031181710"></a>publicip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p68300316174"><a name="en-us_topic_0201534310_p68300316174"></a><a name="en-us_topic_0201534310_p68300316174"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534310_p198309316175"><a name="en-us_topic_0201534310_p198309316175"></a><a name="en-us_topic_0201534310_p198309316175"></a>Specifies the obtained EIP if only IPv4 EIPs are available. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534310_row9150720"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534310_p3010817"><a name="en-us_topic_0201534310_p3010817"></a><a name="en-us_topic_0201534310_p3010817"></a>publicip_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534310_p1953867017154"><a name="en-us_topic_0201534310_p1953867017154"></a><a name="en-us_topic_0201534310_p1953867017154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534310_ul13831731151713"></a><a name="en-us_topic_0201534310_ul13831731151713"></a><ul id="en-us_topic_0201534310_ul13831731151713"><li>Specifies the EIP type.</li><li>The value can be <strong id="en-us_topic_0201534310_b91117519116"><a name="en-us_topic_0201534310_b91117519116"></a><a name="en-us_topic_0201534310_b91117519116"></a>5_bgp</strong> and <strong id="en-us_topic_0201534310_b1811119512013"><a name="en-us_topic_0201534310_b1811119512013"></a><a name="en-us_topic_0201534310_b1811119512013"></a>5_mailbgp</strong>.</li><li>The configured value must be supported by the system. </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "bandwidth": {
            "id": "3fa5b383-5a73-4dcb-a314-c6128546d855",
            "name": "bandwidth123",
            "size": 10,
            "share_type": "PER",
            "publicip_info": [
                {
                    "publicip_id": "6285e7be-fd9f-497c-bc2d-dd0bdea6efe0",
                    "publicip_address": "161.xx.xx.9",
                    "publicip_type": "5_bgp",  
                    "ip_version": 4            
                }
            ],
            "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
            "bandwidth_type": "bgp",
            "charge_mode": "traffic",
            
             "status": "NORMAL" 
        }
    }
    ```


## Status Code<a name="en-us_topic_0201534310_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534310_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

