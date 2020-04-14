# Adding an EIP to a Shared Bandwidth<a name="eip_apisharedbandwidth_0004"></a>

## Function<a name="en-us_topic_0201534131_section16581154"></a>

This API is used to add an EIP to a shared bandwidth.

## URI<a name="en-us_topic_0201534131_section15012662"></a>

POST /v2.0/\{project\_id\}/bandwidths/\{bandwidth\_id\}/insert

[Table 1](#en-us_topic_0201534131_table25281875)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534131_table25281875"></a>
<table><thead align="left"><tr id="en-us_topic_0201534131_row26712487"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534131_p16227847"><a name="en-us_topic_0201534131_p16227847"></a><a name="en-us_topic_0201534131_p16227847"></a><strong id="en-us_topic_0201534131_b842352706195711"><a name="en-us_topic_0201534131_b842352706195711"></a><a name="en-us_topic_0201534131_b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534131_p39387211"><a name="en-us_topic_0201534131_p39387211"></a><a name="en-us_topic_0201534131_p39387211"></a><strong id="en-us_topic_0201534131_b84235270615219"><a name="en-us_topic_0201534131_b84235270615219"></a><a name="en-us_topic_0201534131_b84235270615219"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534131_p36247516"><a name="en-us_topic_0201534131_p36247516"></a><a name="en-us_topic_0201534131_p36247516"></a><strong id="en-us_topic_0201534131_b8423527061645"><a name="en-us_topic_0201534131_b8423527061645"></a><a name="en-us_topic_0201534131_b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534131_row50367649"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p53247746"><a name="en-us_topic_0201534131_p53247746"></a><a name="en-us_topic_0201534131_p53247746"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p18100201"><a name="en-us_topic_0201534131_p18100201"></a><a name="en-us_topic_0201534131_p18100201"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534131_p10487112"><a name="en-us_topic_0201534131_p10487112"></a><a name="en-us_topic_0201534131_p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="en-us_topic_0201534131_row41709209"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p23002745"><a name="en-us_topic_0201534131_p23002745"></a><a name="en-us_topic_0201534131_p23002745"></a>bandwidth_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p51283066"><a name="en-us_topic_0201534131_p51283066"></a><a name="en-us_topic_0201534131_p51283066"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534131_p60287683"><a name="en-us_topic_0201534131_p60287683"></a><a name="en-us_topic_0201534131_p60287683"></a>Specifies the bandwidth ID, which uniquely identifies the bandwidth.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534131_section896237"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="en-us_topic_0201534131_table3057854815556"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534131_row6286666315556"><th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534131_p5903494715556"><a name="en-us_topic_0201534131_p5903494715556"></a><a name="en-us_topic_0201534131_p5903494715556"></a><strong id="en-us_topic_0201534131_b967586923"><a name="en-us_topic_0201534131_b967586923"></a><a name="en-us_topic_0201534131_b967586923"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534131_p1710139915556"><a name="en-us_topic_0201534131_p1710139915556"></a><a name="en-us_topic_0201534131_p1710139915556"></a><strong id="en-us_topic_0201534131_b1201484593"><a name="en-us_topic_0201534131_b1201484593"></a><a name="en-us_topic_0201534131_b1201484593"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534131_p4303610815556"><a name="en-us_topic_0201534131_p4303610815556"></a><a name="en-us_topic_0201534131_p4303610815556"></a><strong id="en-us_topic_0201534131_b842352706145623"><a name="en-us_topic_0201534131_b842352706145623"></a><a name="en-us_topic_0201534131_b842352706145623"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.18%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534131_p6337274615556"><a name="en-us_topic_0201534131_p6337274615556"></a><a name="en-us_topic_0201534131_p6337274615556"></a><strong id="en-us_topic_0201534131_b2124860567"><a name="en-us_topic_0201534131_b2124860567"></a><a name="en-us_topic_0201534131_b2124860567"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534131_row3291877615556"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534131_p4917516615556"><a name="en-us_topic_0201534131_p4917516615556"></a><a name="en-us_topic_0201534131_p4917516615556"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534131_p2376550915556"><a name="en-us_topic_0201534131_p2376550915556"></a><a name="en-us_topic_0201534131_p2376550915556"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534131_p4595806815556"><a name="en-us_topic_0201534131_p4595806815556"></a><a name="en-us_topic_0201534131_p4595806815556"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534131_p1610901815556"><a name="en-us_topic_0201534131_p1610901815556"></a><a name="en-us_topic_0201534131_p1610901815556"></a>Specifies the bandwidth objects. For details, see <a href="#en-us_topic_0201534131_table31854691">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **bandwidth**  field

    <a name="en-us_topic_0201534131_table31854691"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534131_row6882862"><th class="cellrowborder" valign="top" width="13.350000000000001%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534131_p20640979"><a name="en-us_topic_0201534131_p20640979"></a><a name="en-us_topic_0201534131_p20640979"></a><strong id="en-us_topic_0201534131_b1469488726"><a name="en-us_topic_0201534131_b1469488726"></a><a name="en-us_topic_0201534131_b1469488726"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.91%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534131_p61306625"><a name="en-us_topic_0201534131_p61306625"></a><a name="en-us_topic_0201534131_p61306625"></a><strong id="en-us_topic_0201534131_b1380298516"><a name="en-us_topic_0201534131_b1380298516"></a><a name="en-us_topic_0201534131_b1380298516"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.91%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534131_p5200653172316"><a name="en-us_topic_0201534131_p5200653172316"></a><a name="en-us_topic_0201534131_p5200653172316"></a><strong id="en-us_topic_0201534131_b773133847"><a name="en-us_topic_0201534131_b773133847"></a><a name="en-us_topic_0201534131_b773133847"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="58.830000000000005%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534131_p66889567"><a name="en-us_topic_0201534131_p66889567"></a><a name="en-us_topic_0201534131_p66889567"></a><strong id="en-us_topic_0201534131_b583552449"><a name="en-us_topic_0201534131_b583552449"></a><a name="en-us_topic_0201534131_b583552449"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534131_row49345813"><td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534131_p37587916"><a name="en-us_topic_0201534131_p37587916"></a><a name="en-us_topic_0201534131_p37587916"></a>publicip_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534131_p24722347"><a name="en-us_topic_0201534131_p24722347"></a><a name="en-us_topic_0201534131_p24722347"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534131_p18599757172316"><a name="en-us_topic_0201534131_p18599757172316"></a><a name="en-us_topic_0201534131_p18599757172316"></a>Array of <a href="#en-us_topic_0201534131_table30936422">publicip_info</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.830000000000005%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0201534131_ul1057071610312"></a><a name="en-us_topic_0201534131_ul1057071610312"></a><ul id="en-us_topic_0201534131_ul1057071610312"><li>Specifies information about the EIP to be added to the shared bandwidth. For details, see <a href="#en-us_topic_0201534131_table30936422">Table 4</a>.</li><li>The bandwidth, whose type is <strong id="en-us_topic_0201534131_b283219143914"><a name="en-us_topic_0201534131_b283219143914"></a><a name="en-us_topic_0201534131_b283219143914"></a>WHOLE</strong>, can be used by multiple EIPs. The number of EIPs varies depending on the tenant quota. By default, a shared bandwidth can be used by up to 20 EIPs.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **publicip\_info**  object

    <a name="en-us_topic_0201534131_table30936422"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534131_row17161430"><th class="cellrowborder" valign="top" width="14.29%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534131_p47898561"><a name="en-us_topic_0201534131_p47898561"></a><a name="en-us_topic_0201534131_p47898561"></a><strong id="en-us_topic_0201534131_b491960029"><a name="en-us_topic_0201534131_b491960029"></a><a name="en-us_topic_0201534131_b491960029"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.03%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534131_p169718416504"><a name="en-us_topic_0201534131_p169718416504"></a><a name="en-us_topic_0201534131_p169718416504"></a><strong id="en-us_topic_0201534131_b2031628634"><a name="en-us_topic_0201534131_b2031628634"></a><a name="en-us_topic_0201534131_b2031628634"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.96%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534131_p2828296517154"><a name="en-us_topic_0201534131_p2828296517154"></a><a name="en-us_topic_0201534131_p2828296517154"></a><strong id="en-us_topic_0201534131_b1448854919"><a name="en-us_topic_0201534131_b1448854919"></a><a name="en-us_topic_0201534131_b1448854919"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.72%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534131_p58761073"><a name="en-us_topic_0201534131_p58761073"></a><a name="en-us_topic_0201534131_p58761073"></a><strong id="en-us_topic_0201534131_b2130370400"><a name="en-us_topic_0201534131_b2130370400"></a><a name="en-us_topic_0201534131_b2130370400"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534131_row62026502"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534131_p58090788"><a name="en-us_topic_0201534131_p58090788"></a><a name="en-us_topic_0201534131_p58090788"></a>publicip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534131_p79716416504"><a name="en-us_topic_0201534131_p79716416504"></a><a name="en-us_topic_0201534131_p79716416504"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534131_p921881117154"><a name="en-us_topic_0201534131_p921881117154"></a><a name="en-us_topic_0201534131_p921881117154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.72%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534131_p476380"><a name="en-us_topic_0201534131_p476380"></a><a name="en-us_topic_0201534131_p476380"></a>Specifies the ID of the EIP that uses the bandwidth.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{Endpoint}/v2.0/{project_id}/bandwidths/{bandwidth_id}/insert
    
    {
      "bandwidth": {
        "publicip_info": [
          {
            "publicip_id": "29b114d1-2d41-4741-a1f0-b6f80aabceff",
            "publici_type": "5_bgp"
          }
        ]
      }
    }
    ```


## Response Message<a name="en-us_topic_0201534131_section8066134"></a>

-   Response parameter

    **Table  5**  Response parameter

    <a name="en-us_topic_0201534131_table58151089155516"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534131_row25417629155516"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534131_p45562050155516"><a name="en-us_topic_0201534131_p45562050155516"></a><a name="en-us_topic_0201534131_p45562050155516"></a><strong id="en-us_topic_0201534131_b1556032444"><a name="en-us_topic_0201534131_b1556032444"></a><a name="en-us_topic_0201534131_b1556032444"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534131_p29734214155516"><a name="en-us_topic_0201534131_p29734214155516"></a><a name="en-us_topic_0201534131_p29734214155516"></a><strong id="en-us_topic_0201534131_b4683229"><a name="en-us_topic_0201534131_b4683229"></a><a name="en-us_topic_0201534131_b4683229"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534131_p59661173155516"><a name="en-us_topic_0201534131_p59661173155516"></a><a name="en-us_topic_0201534131_p59661173155516"></a><strong id="en-us_topic_0201534131_b513201462"><a name="en-us_topic_0201534131_b513201462"></a><a name="en-us_topic_0201534131_b513201462"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534131_row716877155516"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p58067061155516"><a name="en-us_topic_0201534131_p58067061155516"></a><a name="en-us_topic_0201534131_p58067061155516"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p967638155516"><a name="en-us_topic_0201534131_p967638155516"></a><a name="en-us_topic_0201534131_p967638155516"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534131_p34319839155516"><a name="en-us_topic_0201534131_p34319839155516"></a><a name="en-us_topic_0201534131_p34319839155516"></a>Specifies the bandwidth objects. For details, see <a href="#en-us_topic_0201534131_table138718569112">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Description of the  **bandwidth**  field

    <a name="en-us_topic_0201534131_table138718569112"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534131_row128705614111"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534131_p787856121118"><a name="en-us_topic_0201534131_p787856121118"></a><a name="en-us_topic_0201534131_p787856121118"></a><strong id="en-us_topic_0201534131_b1521082968"><a name="en-us_topic_0201534131_b1521082968"></a><a name="en-us_topic_0201534131_b1521082968"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534131_p2088556181119"><a name="en-us_topic_0201534131_p2088556181119"></a><a name="en-us_topic_0201534131_p2088556181119"></a><strong id="en-us_topic_0201534131_b2008957825"><a name="en-us_topic_0201534131_b2008957825"></a><a name="en-us_topic_0201534131_b2008957825"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534131_p1888115661112"><a name="en-us_topic_0201534131_p1888115661112"></a><a name="en-us_topic_0201534131_p1888115661112"></a><strong id="en-us_topic_0201534131_b98133953"><a name="en-us_topic_0201534131_b98133953"></a><a name="en-us_topic_0201534131_b98133953"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534131_row1688115611112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p78865651114"><a name="en-us_topic_0201534131_p78865651114"></a><a name="en-us_topic_0201534131_p78865651114"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p1588256131115"><a name="en-us_topic_0201534131_p1588256131115"></a><a name="en-us_topic_0201534131_p1588256131115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534131_ul181211824134816"></a><a name="en-us_topic_0201534131_ul181211824134816"></a><ul id="en-us_topic_0201534131_ul181211824134816"><li>Specifies the bandwidth name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534131_row17881356171113"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p20882056151111"><a name="en-us_topic_0201534131_p20882056151111"></a><a name="en-us_topic_0201534131_p20882056151111"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p208855641111"><a name="en-us_topic_0201534131_p208855641111"></a><a name="en-us_topic_0201534131_p208855641111"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534131_ul19451840174816"></a><a name="en-us_topic_0201534131_ul19451840174816"></a><ul id="en-us_topic_0201534131_ul19451840174816"><li>Specifies the bandwidth size.</li><li>The value ranges from 5 Mbit/s to 2000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the available bandwidth range on the management console.)</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534131_row488105641111"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p10881056191119"><a name="en-us_topic_0201534131_p10881056191119"></a><a name="en-us_topic_0201534131_p10881056191119"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p88816566118"><a name="en-us_topic_0201534131_p88816566118"></a><a name="en-us_topic_0201534131_p88816566118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534131_p48813561118"><a name="en-us_topic_0201534131_p48813561118"></a><a name="en-us_topic_0201534131_p48813561118"></a>Specifies the bandwidth ID, which uniquely identifies the bandwidth.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534131_row158855661120"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p17881856151120"><a name="en-us_topic_0201534131_p17881856151120"></a><a name="en-us_topic_0201534131_p17881856151120"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p18887564112"><a name="en-us_topic_0201534131_p18887564112"></a><a name="en-us_topic_0201534131_p18887564112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534131_ul4262181884915"></a><a name="en-us_topic_0201534131_ul4262181884915"></a><ul id="en-us_topic_0201534131_ul4262181884915"><li>Specifies whether the bandwidth is shared or dedicated.</li><li>The value can be <strong id="en-us_topic_0201534131_b10809173018716"><a name="en-us_topic_0201534131_b10809173018716"></a><a name="en-us_topic_0201534131_b10809173018716"></a>PER</strong> or <strong id="en-us_topic_0201534131_b1981114301775"><a name="en-us_topic_0201534131_b1981114301775"></a><a name="en-us_topic_0201534131_b1981114301775"></a>WHOLE</strong>.<a name="en-us_topic_0201534131_ul313253512484"></a><a name="en-us_topic_0201534131_ul313253512484"></a><ul id="en-us_topic_0201534131_ul313253512484"><li><strong id="en-us_topic_0201534131_b56755321579"><a name="en-us_topic_0201534131_b56755321579"></a><a name="en-us_topic_0201534131_b56755321579"></a>WHOLE</strong>: Shared bandwidth</li><li><strong id="en-us_topic_0201534131_b35118341875"><a name="en-us_topic_0201534131_b35118341875"></a><a name="en-us_topic_0201534131_b35118341875"></a>PER</strong>: Dedicated bandwidth</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534131_row1089195616112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p88910565118"><a name="en-us_topic_0201534131_p88910565118"></a><a name="en-us_topic_0201534131_p88910565118"></a>publicip_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p289456141114"><a name="en-us_topic_0201534131_p289456141114"></a><a name="en-us_topic_0201534131_p289456141114"></a>Array of <a href="#en-us_topic_0201534131_table51281965">publicip_info</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534131_ul14114132894913"></a><a name="en-us_topic_0201534131_ul14114132894913"></a><ul id="en-us_topic_0201534131_ul14114132894913"><li>Specifies information about the EIP that uses the bandwidth. For details, see <a href="#en-us_topic_0201534131_table51281965">Table 7</a>.</li><li>The bandwidth, whose type is <strong id="en-us_topic_0201534131_b543919864012"><a name="en-us_topic_0201534131_b543919864012"></a><a name="en-us_topic_0201534131_b543919864012"></a>WHOLE</strong>, can be used by multiple EIPs. The bandwidth, whose type is <strong id="en-us_topic_0201534131_b1440984408"><a name="en-us_topic_0201534131_b1440984408"></a><a name="en-us_topic_0201534131_b1440984408"></a>PER</strong>, can be used by only one EIP.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534131_row1489156171117"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p489456141120"><a name="en-us_topic_0201534131_p489456141120"></a><a name="en-us_topic_0201534131_p489456141120"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p19891756141115"><a name="en-us_topic_0201534131_p19891756141115"></a><a name="en-us_topic_0201534131_p19891756141115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534131_p19517617121017"><a name="en-us_topic_0201534131_p19517617121017"></a><a name="en-us_topic_0201534131_p19517617121017"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534131_row1089056121112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p1989105620112"><a name="en-us_topic_0201534131_p1989105620112"></a><a name="en-us_topic_0201534131_p1989105620112"></a>bandwidth_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p158995611110"><a name="en-us_topic_0201534131_p158995611110"></a><a name="en-us_topic_0201534131_p158995611110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534131_ul5731955125012"></a><a name="en-us_topic_0201534131_ul5731955125012"></a><ul id="en-us_topic_0201534131_ul5731955125012"><li>Specifies the bandwidth type. The default value for the shared bandwidth is <strong id="en-us_topic_0201534131_b11237113941913"><a name="en-us_topic_0201534131_b11237113941913"></a><a name="en-us_topic_0201534131_b11237113941913"></a>share</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534131_row1590155616116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p1090356181119"><a name="en-us_topic_0201534131_p1090356181119"></a><a name="en-us_topic_0201534131_p1090356181119"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p69010561114"><a name="en-us_topic_0201534131_p69010561114"></a><a name="en-us_topic_0201534131_p69010561114"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534131_ul690195631110"></a><a name="en-us_topic_0201534131_ul690195631110"></a><ul id="en-us_topic_0201534131_ul690195631110"><li>Specifies that the bandwidth is billed by bandwidth.</li><li>The value can be <strong id="en-us_topic_0201534131_b842352706191239"><a name="en-us_topic_0201534131_b842352706191239"></a><a name="en-us_topic_0201534131_b842352706191239"></a>traffic</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534131_row9477203041814"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p16479330181816"><a name="en-us_topic_0201534131_p16479330181816"></a><a name="en-us_topic_0201534131_p16479330181816"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p5479163011185"><a name="en-us_topic_0201534131_p5479163011185"></a><a name="en-us_topic_0201534131_p5479163011185"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534131_ul114381249113115"></a><a name="en-us_topic_0201534131_ul114381249113115"></a><ul id="en-us_topic_0201534131_ul114381249113115"><li>Specifies the bandwidth status.</li><li>Possible values are as follows:<a name="en-us_topic_0201534131_ul1943874963116"></a><a name="en-us_topic_0201534131_ul1943874963116"></a><ul id="en-us_topic_0201534131_ul1943874963116"><li><strong id="en-us_topic_0201534131_b84235270610153"><a name="en-us_topic_0201534131_b84235270610153"></a><a name="en-us_topic_0201534131_b84235270610153"></a>FREEZED</strong> (Frozen)</li><li><strong id="en-us_topic_0201534131_b53754535164857"><a name="en-us_topic_0201534131_b53754535164857"></a><a name="en-us_topic_0201534131_b53754535164857"></a>NORMAL</strong> (Normal)</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **publicip\_info**  objects

    <a name="en-us_topic_0201534131_table51281965"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534131_row26928941"><th class="cellrowborder" valign="top" width="26.71%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534131_p33760584"><a name="en-us_topic_0201534131_p33760584"></a><a name="en-us_topic_0201534131_p33760584"></a><strong id="en-us_topic_0201534131_b586071395"><a name="en-us_topic_0201534131_b586071395"></a><a name="en-us_topic_0201534131_b586071395"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.6%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534131_p37114580172552"><a name="en-us_topic_0201534131_p37114580172552"></a><a name="en-us_topic_0201534131_p37114580172552"></a><strong id="en-us_topic_0201534131_b153784261"><a name="en-us_topic_0201534131_b153784261"></a><a name="en-us_topic_0201534131_b153784261"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.69%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534131_p43944024"><a name="en-us_topic_0201534131_p43944024"></a><a name="en-us_topic_0201534131_p43944024"></a><strong id="en-us_topic_0201534131_b870407789"><a name="en-us_topic_0201534131_b870407789"></a><a name="en-us_topic_0201534131_b870407789"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534131_row2696221"><td class="cellrowborder" valign="top" width="26.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p17067371"><a name="en-us_topic_0201534131_p17067371"></a><a name="en-us_topic_0201534131_p17067371"></a>publicip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p53490986172552"><a name="en-us_topic_0201534131_p53490986172552"></a><a name="en-us_topic_0201534131_p53490986172552"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534131_p3792141220526"><a name="en-us_topic_0201534131_p3792141220526"></a><a name="en-us_topic_0201534131_p3792141220526"></a>Specifies the ID of the EIP that uses the bandwidth.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534131_row963478"><td class="cellrowborder" valign="top" width="26.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p621304517467"><a name="en-us_topic_0201534131_p621304517467"></a><a name="en-us_topic_0201534131_p621304517467"></a>publicip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p1021574544615"><a name="en-us_topic_0201534131_p1021574544615"></a><a name="en-us_topic_0201534131_p1021574544615"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534131_p198309316175"><a name="en-us_topic_0201534131_p198309316175"></a><a name="en-us_topic_0201534131_p198309316175"></a>Specifies the obtained EIP if only IPv4 EIPs are available. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534131_row32534423"><td class="cellrowborder" valign="top" width="26.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534131_p18042568"><a name="en-us_topic_0201534131_p18042568"></a><a name="en-us_topic_0201534131_p18042568"></a>publicip_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534131_p42115453172552"><a name="en-us_topic_0201534131_p42115453172552"></a><a name="en-us_topic_0201534131_p42115453172552"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.69%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534131_ul13831731151713"></a><a name="en-us_topic_0201534131_ul13831731151713"></a><ul id="en-us_topic_0201534131_ul13831731151713"><li>Specifies the EIP type.</li><li>The value can be <strong id="en-us_topic_0201534131_b1559816261243"><a name="en-us_topic_0201534131_b1559816261243"></a><a name="en-us_topic_0201534131_b1559816261243"></a>5_bgp</strong> and <strong id="en-us_topic_0201534131_b1459910261412"><a name="en-us_topic_0201534131_b1459910261412"></a><a name="en-us_topic_0201534131_b1459910261412"></a>5_mailbgp</strong>.</li><li>The configured value must be supported by the system. </li></ul>
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
            "share_type": "WHOLE",
            "publicip_info": [
                {
                    "publicip_id": "1d184b2c-4ec9-49b5-a3f9-27600a76ba3f",
                    "publicip_address": "99.xx.xx.82",
                    "publicip_type": "5_bgp",
                    "ip_version": 4
                }
            ],
            "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
            "charge_mode": "traffic",
            "bandwidth_type": "share",
            
        }
    }
    ```


## Status Code<a name="en-us_topic_0201534131_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534131_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

