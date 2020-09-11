# Querying Bandwidths<a name="vpc_bandwidth_0002"></a>

## Function<a name="section44718725"></a>

This API is used to query bandwidths using search criteria.

## URI<a name="section66924213"></a>

GET /v1/\{project\_id\}/bandwidths

Example:

```
GET https://{Endpoint}/v1/{project_id}/bandwidths?limit={limit}&marker={marker}
```

[Table 1](#table62833603)  describes the parameters.

**Table  1**  Parameter description

<a name="table62833603"></a>
<table><thead align="left"><tr id="row55919726"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.5.1.1"><p id="p33203949"><a name="p33203949"></a><a name="p33203949"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="21.05%" id="mcps1.2.5.1.2"><p id="p5165373"><a name="p5165373"></a><a name="p5165373"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.11%" id="mcps1.2.5.1.3"><p id="p59831061171936"><a name="p59831061171936"></a><a name="p59831061171936"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.86%" id="mcps1.2.5.1.4"><p id="p15742086"><a name="p15742086"></a><a name="p15742086"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row40559"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.1 "><p id="p3285280"><a name="p3285280"></a><a name="p3285280"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.2 "><p id="p64781122"><a name="p64781122"></a><a name="p64781122"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.5.1.3 "><p id="p14477807171936"><a name="p14477807171936"></a><a name="p14477807171936"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.86%" headers="mcps1.2.5.1.4 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row47906786"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.1 "><p id="p55244468"><a name="p55244468"></a><a name="p55244468"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.2 "><p id="p45616947"><a name="p45616947"></a><a name="p45616947"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.5.1.3 "><p id="p31851746171936"><a name="p31851746171936"></a><a name="p31851746171936"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.86%" headers="mcps1.2.5.1.4 "><p id="p54367574"><a name="p54367574"></a><a name="p54367574"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row19546120"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.1 "><p id="p39731869"><a name="p39731869"></a><a name="p39731869"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.2 "><p id="p64164835"><a name="p64164835"></a><a name="p64164835"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.5.1.3 "><p id="p29854613171936"><a name="p29854613171936"></a><a name="p29854613171936"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.86%" headers="mcps1.2.5.1.4 "><a name="ul1632320333519"></a><a name="ul1632320333519"></a><ul id="ul1632320333519"><li>Specifies the number of records returned on each page.</li><li>The value ranges from 0 to intmax.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section65447007"></a>

-   Request parameter

    None

-   Example request

    None


## Response Message<a name="section52152158"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table2569960155435"></a>
    <table><thead align="left"><tr id="row46935377155435"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p43669182155435"><a name="p43669182155435"></a><a name="p43669182155435"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p25764441155435"><a name="p25764441155435"></a><a name="p25764441155435"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="p6544983155435"><a name="p6544983155435"></a><a name="p6544983155435"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60381654155435"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p59075838155435"><a name="p59075838155435"></a><a name="p59075838155435"></a>bandwidths</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p42885478155435"><a name="p42885478155435"></a><a name="p42885478155435"></a>Array of <a href="#table17227723">bandwidths</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="p57892147155435"><a name="p57892147155435"></a><a name="p57892147155435"></a>Specifies the bandwidth objects. For details, see <a href="#table17227723">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **bandwidths**  field

    <a name="table17227723"></a>
    <table><thead align="left"><tr id="row57600065"><th class="cellrowborder" valign="top" width="26.730000000000004%" id="mcps1.2.4.1.1"><p id="p35093725"><a name="p35093725"></a><a name="p35093725"></a>Name</p>
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
    <p id="p785111375011"><a name="p785111375011"></a><a name="p785111375011"></a>If this parameter is not set, the list of all bandwidths will be returned by default.</p>
    </td>
    </tr>
    <tr id="row49955752"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="p19884118"><a name="p19884118"></a><a name="p19884118"></a>publicip_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="p26395826172022"><a name="p26395826172022"></a><a name="p26395826172022"></a>Array of <a href="#table30936422">publicip_info</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="ul154130570376"></a><a name="ul154130570376"></a><ul id="ul154130570376"><li>Specifies information about the EIP that uses the bandwidth. For details, see <a href="#table30936422">Table 4</a>.</li></ul>
    </td>
    </tr>
    <tr id="row12794876"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="p29752015"><a name="p29752015"></a><a name="p29752015"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="p57687133172022"><a name="p57687133172022"></a><a name="p57687133172022"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><p id="p78154550413"><a name="p78154550413"></a><a name="p78154550413"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row29288625"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="p23568445"><a name="p23568445"></a><a name="p23568445"></a>bandwidth_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="p42146201172022"><a name="p42146201172022"></a><a name="p42146201172022"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="ul12723142619163"></a><a name="ul12723142619163"></a><ul id="ul12723142619163"><li>Specifies the bandwidth type.</li><li>The value is <strong id="b8473181711375"><a name="b8473181711375"></a><a name="b8473181711375"></a>bgp</strong>. </li></ul>
    </td>
    </tr>
    <tr id="row58843898173344"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="p18916883173347"><a name="p18916883173347"></a><a name="p18916883173347"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="p29386093173347"><a name="p29386093173347"></a><a name="p29386093173347"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="ul19561144916384"></a><a name="ul19561144916384"></a><ul id="ul19561144916384"><li>If the value is <strong id="b492435718311"><a name="b492435718311"></a><a name="b492435718311"></a>traffic</strong>, the bandwidth is billed by traffic.</li></ul>
    </td>
    </tr>
    <tr id="row48981943163316"><td class="cellrowborder" valign="top" width="26.730000000000004%" headers="mcps1.2.4.1.1 "><p id="p1813212463332"><a name="p1813212463332"></a><a name="p1813212463332"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.92%" headers="mcps1.2.4.1.2 "><p id="p913274612339"><a name="p913274612339"></a><a name="p913274612339"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.35000000000001%" headers="mcps1.2.4.1.3 "><a name="ul1613254663316"></a><a name="ul1613254663316"></a><ul id="ul1613254663316"><li>Specifies the bandwidth status.</li><li>Possible values are as follows:<a name="ul613234613312"></a><a name="ul613234613312"></a><ul id="ul613234613312"><li><strong id="b84235270610153"><a name="b84235270610153"></a><a name="b84235270610153"></a>FREEZED</strong> (Frozen)</li><li><strong id="b53754535164857"><a name="b53754535164857"></a><a name="b53754535164857"></a>NORMAL</strong> (Normal)</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **publicip\_info**  object

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
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><a name="ul13831731151713"></a><a name="ul13831731151713"></a><ul id="ul13831731151713"><li>Specifies the EIP type.</li><li>The value can be <strong id="b188327795913"><a name="b188327795913"></a><a name="b188327795913"></a>5_bgp</strong> and <strong id="b1283307125915"><a name="b1283307125915"></a><a name="b1283307125915"></a>5_mailbgp</strong>.</li><li>The configured value must be supported by the system. </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "bandwidths": [
        {
          "id": "09b99c91-da7c-449f-94e2-f4934c5b2a71",
          "name": "vpngw-f632a7b0-ef50-4ac5-97e9-ddc56b3d5977",
          "size": 2000,
          "share_type": "PER",
          "publicip_info": [
            {
              "publicip_id": "2a65923c-7133-415d-ae3b-cf9635a942c5",
              "publicip_address": "10.xx.xx.3",
              "ip_version": 4,
              "publicip_type": "5_bgp"
            }
          ],
          "tenant_id": "26ae5181a416420998eb2093aaed84d9",
          "bandwidth_type": "bgp",
          "charge_mode": "traffic",
          "status": "NORMAL"
        },
        {
          "id": "0a583ff1-b43e-4000-ade3-e7af0097f832",
          "name": "vpngw-7e880d5b-f458-40ad-a7e5-735c44cd8b7d",
          "size": 300,
          "share_type": "PER",
          "publicip_info": [
            {
              "publicip_id": "c754bc9a-16d5-4763-9674-d7561917aa80",
              "publicip_address": "10.xx.xx.9",
              "ip_version": 4,
              "publicip_type": "5_bgp"
            }
          ],
          "tenant_id": "26ae5181a416420998eb2093aaed84d9",
          "bandwidth_type": "bgp",
          "charge_mode": "traffic",
          "status": "NORMAL"
        },
        {
          "id": "0a673f00-3640-4a13-949e-7049b2916baf",
          "name": "bandwidth123",
          "size": 10,
          "share_type": "PER",
          "publicip_info": [
            {
              "publicip_id": "cec7fb70-2f82-4561-bd83-2121fb642fdc",
              "publicip_address": "10.xx.xx.184",
              "ip_version": 4,
              "publicip_type": "5_bgp"
            }
          ],
          "tenant_id": "26ae5181a416420998eb2093aaed84d9",
          "bandwidth_type": "bgp",
          "charge_mode": "traffic",
          "status": "NORMAL"
        },
        {
          "id": "0dde1eae-1783-46dc-998c-930fbe261ff9",
          "name": "bandwidth123",
          "size": 100,
          "share_type": "PER",
          "publicip_info": [
            {
              "publicip_id": "24232038-e178-40ad-80e4-5abb75db84be",
              "publicip_address": "10.xx.xx.101",
              "ip_version": 4,
              "publicip_type": "5_bgp"
            }
          ],
          "tenant_id": "26ae5181a416420998eb2093aaed84d9",
          "bandwidth_type": "bgp",
          "charge_mode": "traffic",
          "status": "NORMAL"
        }
      ]
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

