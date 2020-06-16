# Adding an EIP to a Shared Bandwidth<a name="vpc_sharebandwidth_0004"></a>

## Function<a name="section16581154"></a>

This API is used to add an EIP to a shared bandwidth.

## URI<a name="section15012662"></a>

POST /v2.0/\{project\_id\}/bandwidths/\{bandwidth\_id\}/insert

[Table 1](#table25281875)  describes the parameters.

**Table  1**  Parameter description

<a name="table25281875"></a>
<table><thead align="left"><tr id="row26712487"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p16227847"><a name="p16227847"></a><a name="p16227847"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p39387211"><a name="p39387211"></a><a name="p39387211"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p36247516"><a name="p36247516"></a><a name="p36247516"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
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
    <table><thead align="left"><tr id="row6286666315556"><th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.2.5.1.1"><p id="p5903494715556"><a name="p5903494715556"></a><a name="p5903494715556"></a><strong id="b967586923"><a name="b967586923"></a><a name="b967586923"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.5.1.2"><p id="p1710139915556"><a name="p1710139915556"></a><a name="p1710139915556"></a><strong id="b1201484593"><a name="b1201484593"></a><a name="b1201484593"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.3"><p id="p4303610815556"><a name="p4303610815556"></a><a name="p4303610815556"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.18%" id="mcps1.2.5.1.4"><p id="p6337274615556"><a name="p6337274615556"></a><a name="p6337274615556"></a><strong id="b2124860567"><a name="b2124860567"></a><a name="b2124860567"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3291877615556"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.2.5.1.1 "><p id="p4917516615556"><a name="p4917516615556"></a><a name="p4917516615556"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.2 "><p id="p2376550915556"><a name="p2376550915556"></a><a name="p2376550915556"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.3 "><p id="p4595806815556"><a name="p4595806815556"></a><a name="p4595806815556"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="p1610901815556"><a name="p1610901815556"></a><a name="p1610901815556"></a>Specifies the bandwidth objects. For details, see <a href="#table31854691">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **bandwidth**  field

    <a name="table31854691"></a>
    <table><thead align="left"><tr id="row6882862"><th class="cellrowborder" valign="top" width="13.350000000000001%" id="mcps1.2.5.1.1"><p id="p20640979"><a name="p20640979"></a><a name="p20640979"></a><strong id="b1469488726"><a name="b1469488726"></a><a name="b1469488726"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.91%" id="mcps1.2.5.1.2"><p id="p61306625"><a name="p61306625"></a><a name="p61306625"></a><strong id="b1380298516"><a name="b1380298516"></a><a name="b1380298516"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.91%" id="mcps1.2.5.1.3"><p id="p5200653172316"><a name="p5200653172316"></a><a name="p5200653172316"></a><strong id="b773133847"><a name="b773133847"></a><a name="b773133847"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="58.830000000000005%" id="mcps1.2.5.1.4"><p id="p66889567"><a name="p66889567"></a><a name="p66889567"></a><strong id="b583552449"><a name="b583552449"></a><a name="b583552449"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49345813"><td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.2.5.1.1 "><p id="p37587916"><a name="p37587916"></a><a name="p37587916"></a>publicip_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.2.5.1.2 "><p id="p24722347"><a name="p24722347"></a><a name="p24722347"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.2.5.1.3 "><p id="p18599757172316"><a name="p18599757172316"></a><a name="p18599757172316"></a>Array of <a href="#table30936422">publicip_info</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.830000000000005%" headers="mcps1.2.5.1.4 "><a name="ul1057071610312"></a><a name="ul1057071610312"></a><ul id="ul1057071610312"><li>Specifies information about the EIP to be added to the shared bandwidth. For details, see <a href="#table30936422">Table 4</a>.</li><li>The bandwidth, whose type is <strong id="b283219143914"><a name="b283219143914"></a><a name="b283219143914"></a>WHOLE</strong>, can be used by multiple EIPs. The number of EIPs varies depending on the tenant quota. By default, a shared bandwidth can be used by up to 20 EIPs.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **publicip\_info**  object

    <a name="table30936422"></a>
    <table><thead align="left"><tr id="row17161430"><th class="cellrowborder" valign="top" width="14.29%" id="mcps1.2.5.1.1"><p id="p47898561"><a name="p47898561"></a><a name="p47898561"></a><strong id="b491960029"><a name="b491960029"></a><a name="b491960029"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.03%" id="mcps1.2.5.1.2"><p id="p169718416504"><a name="p169718416504"></a><a name="p169718416504"></a><strong id="b2031628634"><a name="b2031628634"></a><a name="b2031628634"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.96%" id="mcps1.2.5.1.3"><p id="p2828296517154"><a name="p2828296517154"></a><a name="p2828296517154"></a><strong id="b1448854919"><a name="b1448854919"></a><a name="b1448854919"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.72%" id="mcps1.2.5.1.4"><p id="p58761073"><a name="p58761073"></a><a name="p58761073"></a><strong id="b2130370400"><a name="b2130370400"></a><a name="b2130370400"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62026502"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.2.5.1.1 "><p id="p58090788"><a name="p58090788"></a><a name="p58090788"></a>publicip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.5.1.2 "><p id="p79716416504"><a name="p79716416504"></a><a name="p79716416504"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.2.5.1.3 "><p id="p921881117154"><a name="p921881117154"></a><a name="p921881117154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.72%" headers="mcps1.2.5.1.4 "><p id="p476380"><a name="p476380"></a><a name="p476380"></a>Specifies the ID of the EIP that uses the bandwidth.</p>
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


## Response Message<a name="section8066134"></a>

-   Response parameter

    **Table  5**  Response parameter

    <a name="table58151089155516"></a>
    <table><thead align="left"><tr id="row25417629155516"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p45562050155516"><a name="p45562050155516"></a><a name="p45562050155516"></a><strong id="b1556032444"><a name="b1556032444"></a><a name="b1556032444"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p29734214155516"><a name="p29734214155516"></a><a name="p29734214155516"></a><strong id="b4683229"><a name="b4683229"></a><a name="b4683229"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="p59661173155516"><a name="p59661173155516"></a><a name="p59661173155516"></a><strong id="b513201462"><a name="b513201462"></a><a name="b513201462"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row716877155516"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p58067061155516"><a name="p58067061155516"></a><a name="p58067061155516"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p967638155516"><a name="p967638155516"></a><a name="p967638155516"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="p34319839155516"><a name="p34319839155516"></a><a name="p34319839155516"></a>Specifies the bandwidth objects. For details, see <a href="#table138718569112">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Description of the  **bandwidth**  field

    <a name="table138718569112"></a>
    <table><thead align="left"><tr id="row128705614111"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p787856121118"><a name="p787856121118"></a><a name="p787856121118"></a><strong id="b1521082968"><a name="b1521082968"></a><a name="b1521082968"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.2"><p id="p2088556181119"><a name="p2088556181119"></a><a name="p2088556181119"></a><strong id="b2008957825"><a name="b2008957825"></a><a name="b2008957825"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p1888115661112"><a name="p1888115661112"></a><a name="p1888115661112"></a><strong id="b98133953"><a name="b98133953"></a><a name="b98133953"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1688115611112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p78865651114"><a name="p78865651114"></a><a name="p78865651114"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p1588256131115"><a name="p1588256131115"></a><a name="p1588256131115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="ul181211824134816"></a><a name="ul181211824134816"></a><ul id="ul181211824134816"><li>Specifies the bandwidth name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="row17881356171113"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p20882056151111"><a name="p20882056151111"></a><a name="p20882056151111"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p208855641111"><a name="p208855641111"></a><a name="p208855641111"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="ul19451840174816"></a><a name="ul19451840174816"></a><ul id="ul19451840174816"><li>Specifies the bandwidth size.</li><li>The value ranges from 5 Mbit/s to 2000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the available bandwidth range on the management console.)</li></ul>
    </td>
    </tr>
    <tr id="row488105641111"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p10881056191119"><a name="p10881056191119"></a><a name="p10881056191119"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p88816566118"><a name="p88816566118"></a><a name="p88816566118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p48813561118"><a name="p48813561118"></a><a name="p48813561118"></a>Specifies the bandwidth ID, which uniquely identifies the bandwidth.</p>
    </td>
    </tr>
    <tr id="row158855661120"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p17881856151120"><a name="p17881856151120"></a><a name="p17881856151120"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p18887564112"><a name="p18887564112"></a><a name="p18887564112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="ul4262181884915"></a><a name="ul4262181884915"></a><ul id="ul4262181884915"><li>Specifies whether the bandwidth is shared or dedicated.</li><li>The value can be <strong id="b10809173018716"><a name="b10809173018716"></a><a name="b10809173018716"></a>PER</strong> or <strong id="b1981114301775"><a name="b1981114301775"></a><a name="b1981114301775"></a>WHOLE</strong>.<a name="ul313253512484"></a><a name="ul313253512484"></a><ul id="ul313253512484"><li><strong id="b56755321579"><a name="b56755321579"></a><a name="b56755321579"></a>WHOLE</strong>: Shared bandwidth</li><li><strong id="b35118341875"><a name="b35118341875"></a><a name="b35118341875"></a>PER</strong>: Dedicated bandwidth</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row1089195616112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p88910565118"><a name="p88910565118"></a><a name="p88910565118"></a>publicip_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p289456141114"><a name="p289456141114"></a><a name="p289456141114"></a>Array of <a href="#table51281965">publicip_info</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="ul14114132894913"></a><a name="ul14114132894913"></a><ul id="ul14114132894913"><li>Specifies information about the EIP that uses the bandwidth. For details, see <a href="#table51281965">Table 7</a>.</li><li>The bandwidth, whose type is <strong id="b543919864012"><a name="b543919864012"></a><a name="b543919864012"></a>WHOLE</strong>, can be used by multiple EIPs. The bandwidth, whose type is <strong id="b1440984408"><a name="b1440984408"></a><a name="b1440984408"></a>PER</strong>, can be used by only one EIP.</li></ul>
    </td>
    </tr>
    <tr id="row1489156171117"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p489456141120"><a name="p489456141120"></a><a name="p489456141120"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p19891756141115"><a name="p19891756141115"></a><a name="p19891756141115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p19517617121017"><a name="p19517617121017"></a><a name="p19517617121017"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row1089056121112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1989105620112"><a name="p1989105620112"></a><a name="p1989105620112"></a>bandwidth_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p158995611110"><a name="p158995611110"></a><a name="p158995611110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="ul5731955125012"></a><a name="ul5731955125012"></a><ul id="ul5731955125012"><li>Specifies the bandwidth type. The default value for the shared bandwidth is <strong id="b11237113941913"><a name="b11237113941913"></a><a name="b11237113941913"></a>share</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row1590155616116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1090356181119"><a name="p1090356181119"></a><a name="p1090356181119"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p69010561114"><a name="p69010561114"></a><a name="p69010561114"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="ul690195631110"></a><a name="ul690195631110"></a><ul id="ul690195631110"><li>Specifies that the bandwidth is billed by bandwidth.</li><li>The value can be <strong id="b842352706191239"><a name="b842352706191239"></a><a name="b842352706191239"></a>traffic</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row9477203041814"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p16479330181816"><a name="p16479330181816"></a><a name="p16479330181816"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p5479163011185"><a name="p5479163011185"></a><a name="p5479163011185"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="ul114381249113115"></a><a name="ul114381249113115"></a><ul id="ul114381249113115"><li>Specifies the bandwidth status.</li><li>Possible values are as follows:<a name="ul1943874963116"></a><a name="ul1943874963116"></a><ul id="ul1943874963116"><li><strong id="b84235270610153"><a name="b84235270610153"></a><a name="b84235270610153"></a>FREEZED</strong> (Frozen)</li><li><strong id="b53754535164857"><a name="b53754535164857"></a><a name="b53754535164857"></a>NORMAL</strong> (Normal)</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **publicip\_info**  objects

    <a name="table51281965"></a>
    <table><thead align="left"><tr id="row26928941"><th class="cellrowborder" valign="top" width="26.71%" id="mcps1.2.4.1.1"><p id="p33760584"><a name="p33760584"></a><a name="p33760584"></a><strong id="b586071395"><a name="b586071395"></a><a name="b586071395"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.6%" id="mcps1.2.4.1.2"><p id="p37114580172552"><a name="p37114580172552"></a><a name="p37114580172552"></a><strong id="b153784261"><a name="b153784261"></a><a name="b153784261"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.69%" id="mcps1.2.4.1.3"><p id="p43944024"><a name="p43944024"></a><a name="p43944024"></a><strong id="b870407789"><a name="b870407789"></a><a name="b870407789"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2696221"><td class="cellrowborder" valign="top" width="26.71%" headers="mcps1.2.4.1.1 "><p id="p17067371"><a name="p17067371"></a><a name="p17067371"></a>publicip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.4.1.2 "><p id="p53490986172552"><a name="p53490986172552"></a><a name="p53490986172552"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.69%" headers="mcps1.2.4.1.3 "><p id="p3792141220526"><a name="p3792141220526"></a><a name="p3792141220526"></a>Specifies the ID of the EIP that uses the bandwidth.</p>
    </td>
    </tr>
    <tr id="row963478"><td class="cellrowborder" valign="top" width="26.71%" headers="mcps1.2.4.1.1 "><p id="p621304517467"><a name="p621304517467"></a><a name="p621304517467"></a>publicip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.4.1.2 "><p id="p1021574544615"><a name="p1021574544615"></a><a name="p1021574544615"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.69%" headers="mcps1.2.4.1.3 "><p id="p198309316175"><a name="p198309316175"></a><a name="p198309316175"></a>Specifies the obtained EIP if only IPv4 EIPs are available. </p>
    </td>
    </tr>
    <tr id="row32534423"><td class="cellrowborder" valign="top" width="26.71%" headers="mcps1.2.4.1.1 "><p id="p18042568"><a name="p18042568"></a><a name="p18042568"></a>publicip_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.4.1.2 "><p id="p42115453172552"><a name="p42115453172552"></a><a name="p42115453172552"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.69%" headers="mcps1.2.4.1.3 "><a name="ul13831731151713"></a><a name="ul13831731151713"></a><ul id="ul13831731151713"><li>Specifies the EIP type.</li><li>The value can be <strong id="b1559816261243"><a name="b1559816261243"></a><a name="b1559816261243"></a>5_bgp</strong> and <strong id="b1459910261412"><a name="b1459910261412"></a><a name="b1459910261412"></a>5_mailbgp</strong>.</li><li>The configured value must be supported by the system. </li></ul>
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


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

