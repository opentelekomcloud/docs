# Updating a Bandwidth<a name="vpc_bandwidth_0003"></a>

## Function<a name="section16581154"></a>

This API is used to update information about a bandwidth.

## URI<a name="section15012662"></a>

PUT /v1/\{project\_id\}/bandwidths/\{bandwidth\_id\}

[Table 1](#table25281875)  describes the parameters.

**Table  1**  Parameter description

<a name="table25281875"></a>
<table><thead align="left"><tr id="row26712487"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p16227847"><a name="p16227847"></a><a name="p16227847"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p39387211"><a name="p39387211"></a><a name="p39387211"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p36247516"><a name="p36247516"></a><a name="p36247516"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row50367649"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p53247746"><a name="p53247746"></a><a name="p53247746"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18100201"><a name="p18100201"></a><a name="p18100201"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row41709209"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p23002745"><a name="p23002745"></a><a name="p23002745"></a>bandwidth_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p51283066"><a name="p51283066"></a><a name="p51283066"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60287683"><a name="p60287683"></a><a name="p60287683"></a>Specifies the bandwidth ID, which uniquely identifies the bandwidth.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section896237"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table3057854815556"></a>
    <table><thead align="left"><tr id="row6286666315556"><th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.2.5.1.1"><p id="p5903494715556"><a name="p5903494715556"></a><a name="p5903494715556"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.2"><p id="p1710139915556"><a name="p1710139915556"></a><a name="p1710139915556"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.380000000000003%" id="mcps1.2.5.1.3"><p id="p4303610815556"><a name="p4303610815556"></a><a name="p4303610815556"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.47%" id="mcps1.2.5.1.4"><p id="p6337274615556"><a name="p6337274615556"></a><a name="p6337274615556"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3291877615556"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.2.5.1.1 "><p id="p4917516615556"><a name="p4917516615556"></a><a name="p4917516615556"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.2 "><p id="p2376550915556"><a name="p2376550915556"></a><a name="p2376550915556"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.380000000000003%" headers="mcps1.2.5.1.3 "><p id="p4595806815556"><a name="p4595806815556"></a><a name="p4595806815556"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.47%" headers="mcps1.2.5.1.4 "><p id="p1610901815556"><a name="p1610901815556"></a><a name="p1610901815556"></a>Specifies the bandwidth objects. For details, see <a href="#table31854691">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **bandwidth**  field

    <a name="table31854691"></a>
    <table><thead align="left"><tr id="row6882862"><th class="cellrowborder" valign="top" width="13.350000000000001%" id="mcps1.2.5.1.1"><p id="p20640979"><a name="p20640979"></a><a name="p20640979"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.17%" id="mcps1.2.5.1.2"><p id="p61306625"><a name="p61306625"></a><a name="p61306625"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.229999999999999%" id="mcps1.2.5.1.3"><p id="p5200653172316"><a name="p5200653172316"></a><a name="p5200653172316"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.25%" id="mcps1.2.5.1.4"><p id="p66889567"><a name="p66889567"></a><a name="p66889567"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49345813"><td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.2.5.1.1 "><p id="p37587916"><a name="p37587916"></a><a name="p37587916"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.2.5.1.2 "><p id="p24722347"><a name="p24722347"></a><a name="p24722347"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.5.1.3 "><p id="p18599757172316"><a name="p18599757172316"></a><a name="p18599757172316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.25%" headers="mcps1.2.5.1.4 "><a name="ul5677198174113"></a><a name="ul5677198174113"></a><ul id="ul5677198174113"><li>Specifies the bandwidth name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.). If the value is left blank, the name of the bandwidth is not changed.</li><li>Either parameter <strong id="b84235270621475"><a name="b84235270621475"></a><a name="b84235270621475"></a>name</strong> or <strong id="b84235270621478"><a name="b84235270621478"></a><a name="b84235270621478"></a>size</strong> must be specified.</li></ul>
    </td>
    </tr>
    <tr id="row10796581"><td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.2.5.1.1 "><p id="p2107829"><a name="p2107829"></a><a name="p2107829"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.2.5.1.2 "><p id="p36516433"><a name="p36516433"></a><a name="p36516433"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.5.1.3 "><p id="p30185329172316"><a name="p30185329172316"></a><a name="p30185329172316"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.25%" headers="mcps1.2.5.1.4 "><a name="ul1396719655311"></a><a name="ul1396719655311"></a><ul id="ul1396719655311"><li>Specifies the bandwidth size in Mbit/s.</li><li>The value ranges from 1 Mbit/s to 1000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the available bandwidth range on the management console.) If the parameter is not included, the bandwidth size is not changed.</li><li>Either parameter <strong id="b2045315149"><a name="b2045315149"></a><a name="b2045315149"></a>name</strong> or <strong id="b1434415927"><a name="b1434415927"></a><a name="b1434415927"></a>size</strong> must be specified.</li><li>If a decimal fraction (for example <strong>10.2</strong>) or a character string (for example <strong>"10"</strong>) is specified, the specified value will be automatically converted to an integer.</li><li>The minimum unit for bandwidth adjustment varies depending on the bandwidth range. The details are as follows:<a name="ul9790510185"></a><a name="ul9790510185"></a><ul id="ul9790510185"><li>The minimum unit is 1 Mbit/s if the allowed bandwidth size ranges from 0 to 300 Mbit/s (with 300 Mbit/s included).</li><li>The minimum unit is 50 Mbit/s if the allowed bandwidth size ranges 300 Mbit/s to 1000 Mbit/s (with 1000 Mbit/s included).</li><li>The minimum unit is 500 Mbit/s if the allowed bandwidth size is greater than 1000 Mbit/s.</li></ul>
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


## Response Message<a name="section8066134"></a>

-   Response parameter

    **Table  4**  Response parameter

    <a name="table58151089155516"></a>
    <table><thead align="left"><tr id="row25417629155516"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p45562050155516"><a name="p45562050155516"></a><a name="p45562050155516"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p29734214155516"><a name="p29734214155516"></a><a name="p29734214155516"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="p59661173155516"><a name="p59661173155516"></a><a name="p59661173155516"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row716877155516"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p58067061155516"><a name="p58067061155516"></a><a name="p58067061155516"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p967638155516"><a name="p967638155516"></a><a name="p967638155516"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="p34319839155516"><a name="p34319839155516"></a><a name="p34319839155516"></a>Specifies the bandwidth objects. For details, see <a href="#table17227723">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Description of the  **bandwidths**  field

    <a name="table17227723"></a>
    <table><thead align="left"><tr id="row57600065"><th class="cellrowborder" valign="top" width="26.730000000000004%" id="mcps1.2.4.1.1"><p id="p35093725"><a name="p35093725"></a><a name="p35093725"></a><strong id="b1051561924911"><a name="b1051561924911"></a><a name="b1051561924911"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.92%" id="mcps1.2.4.1.2"><p id="p42606680172022"><a name="p42606680172022"></a><a name="p42606680172022"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.35000000000001%" id="mcps1.2.4.1.3"><p id="p66526832"><a name="p66526832"></a><a name="p66526832"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19964345"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="p6499254"><a name="p6499254"></a><a name="p6499254"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="p28589065172022"><a name="p28589065172022"></a><a name="p28589065172022"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="ul1630720166145"></a><a name="ul1630720166145"></a><ul id="ul1630720166145"><li>Specifies the bandwidth name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="row11415673"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="p52254296"><a name="p52254296"></a><a name="p52254296"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="p34012930172022"><a name="p34012930172022"></a><a name="p34012930172022"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="ul1730751620144"></a><a name="ul1730751620144"></a><ul id="ul1730751620144"><li>Specifies the bandwidth size in Mbit/s.</li><li>The value ranges from 1 Mbit/s to 2000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the available bandwidth range on the management console.)</li></ul>
    </td>
    </tr>
    <tr id="row24927872"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="p5891777"><a name="p5891777"></a><a name="p5891777"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="p3583980172022"><a name="p3583980172022"></a><a name="p3583980172022"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><p id="p11246416"><a name="p11246416"></a><a name="p11246416"></a>Specifies the bandwidth ID, which uniquely identifies the bandwidth.</p>
    </td>
    </tr>
    <tr id="row34108880"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="p11355891"><a name="p11355891"></a><a name="p11355891"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="p21866991172022"><a name="p21866991172022"></a><a name="p21866991172022"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="ul540194517378"></a><a name="ul540194517378"></a><ul id="ul540194517378"><li>The value is <strong id="b25288513165924"><a name="b25288513165924"></a><a name="b25288513165924"></a>PER</strong>, indicating that the bandwidth is dedicated.</li></ul>
    </td>
    </tr>
    <tr id="row49955752"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="p19884118"><a name="p19884118"></a><a name="p19884118"></a>publicip_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="p26395826172022"><a name="p26395826172022"></a><a name="p26395826172022"></a>Array of <a href="#table30936422">publicip_info</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="ul154130570376"></a><a name="ul154130570376"></a><ul id="ul154130570376"><li>Specifies information about the EIP that uses the bandwidth. For details, see <a href="#table30936422">Table 6</a>.</li></ul>
    </td>
    </tr>
    <tr id="row12794876"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="p29752015"><a name="p29752015"></a><a name="p29752015"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="p57687133172022"><a name="p57687133172022"></a><a name="p57687133172022"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><p id="p1539621310512"><a name="p1539621310512"></a><a name="p1539621310512"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row29288625"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="p23568445"><a name="p23568445"></a><a name="p23568445"></a>bandwidth_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="p42146201172022"><a name="p42146201172022"></a><a name="p42146201172022"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="ul12723142619163"></a><a name="ul12723142619163"></a><ul id="ul12723142619163"><li>Specifies the bandwidth type.</li><li>The value is <strong id="b756116538522"><a name="b756116538522"></a><a name="b756116538522"></a>bgp</strong>. </li></ul>
    </td>
    </tr>
    <tr id="row58843898173344"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="p18916883173347"><a name="p18916883173347"></a><a name="p18916883173347"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="p29386093173347"><a name="p29386093173347"></a><a name="p29386093173347"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="ul19561144916384"></a><a name="ul19561144916384"></a><ul id="ul19561144916384"><li>If the value is <strong id="b164011341133220"><a name="b164011341133220"></a><a name="b164011341133220"></a>traffic</strong>, the bandwidth is billed by traffic.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **publicip\_info**  objects

    <a name="table30936422"></a>
    <table><thead align="left"><tr id="row17161430"><th class="cellrowborder" valign="top" width="25.740000000000002%" id="mcps1.2.4.1.1"><p id="p47898561"><a name="p47898561"></a><a name="p47898561"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.5%" id="mcps1.2.4.1.2"><p id="p2828296517154"><a name="p2828296517154"></a><a name="p2828296517154"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.76%" id="mcps1.2.4.1.3"><p id="p58761073"><a name="p58761073"></a><a name="p58761073"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62026502"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p58090788"><a name="p58090788"></a><a name="p58090788"></a>publicip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="p921881117154"><a name="p921881117154"></a><a name="p921881117154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><p id="p476380"><a name="p476380"></a><a name="p476380"></a>Specifies the ID of the EIP that uses the bandwidth.</p>
    </td>
    </tr>
    <tr id="row4287423"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p108302031181710"><a name="p108302031181710"></a><a name="p108302031181710"></a>publicip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="p68300316174"><a name="p68300316174"></a><a name="p68300316174"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><p id="p198309316175"><a name="p198309316175"></a><a name="p198309316175"></a>Specifies the obtained EIP if only IPv4 EIPs are available. </p>
    </td>
    </tr>
    <tr id="row9150720"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p3010817"><a name="p3010817"></a><a name="p3010817"></a>publicip_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="p1953867017154"><a name="p1953867017154"></a><a name="p1953867017154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><a name="ul13831731151713"></a><a name="ul13831731151713"></a><ul id="ul13831731151713"><li>Specifies the EIP type.</li><li>The value can be <strong id="b91117519116"><a name="b91117519116"></a><a name="b91117519116"></a>5_bgp</strong> and <strong id="b1811119512013"><a name="b1811119512013"></a><a name="b1811119512013"></a>5_mailbgp</strong>.</li><li>The configured value must be supported by the system. </li></ul>
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


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

