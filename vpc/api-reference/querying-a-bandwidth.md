# Querying a Bandwidth<a name="vpc_bandwidth_0001"></a>

## Function<a name="section65488131"></a>

This API is used to query details about a bandwidth.

## URI<a name="section52522275"></a>

GET /v1/\{project\_id\}/bandwidths/\{bandwidth\_id\}

[Table 1](#table40002310)  describes the parameters.

**Table  1**  Parameter description

<a name="table40002310"></a>
<table><thead align="left"><tr id="row55023063"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p27683123"><a name="p27683123"></a><a name="p27683123"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p27740487"><a name="p27740487"></a><a name="p27740487"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p32387004"><a name="p32387004"></a><a name="p32387004"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6101690"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p24474856"><a name="p24474856"></a><a name="p24474856"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p36306286"><a name="p36306286"></a><a name="p36306286"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row26390432"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p57250251"><a name="p57250251"></a><a name="p57250251"></a>bandwidth_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6758730"><a name="p6758730"></a><a name="p6758730"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10586246"><a name="p10586246"></a><a name="p10586246"></a>Specifies the bandwidth ID, which uniquely identifies the bandwidth.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section2938434"></a>

-   Request parameter

    None

-   Example request

    None


## Response Message<a name="section26445914"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table16054594155348"></a>
    <table><thead align="left"><tr id="row50617932155348"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p6411865155348"><a name="p6411865155348"></a><a name="p6411865155348"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p58099771155348"><a name="p58099771155348"></a><a name="p58099771155348"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="p8461025155348"><a name="p8461025155348"></a><a name="p8461025155348"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14254431155348"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p13758302155348"><a name="p13758302155348"></a><a name="p13758302155348"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p6803198155348"><a name="p6803198155348"></a><a name="p6803198155348"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="p60584419155348"><a name="p60584419155348"></a><a name="p60584419155348"></a>Specifies the bandwidth object.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **bandwidth**  field

    <a name="table60972066"></a>
    <table><thead align="left"><tr id="row10740297"><th class="cellrowborder" valign="top" width="25.28%" id="mcps1.2.4.1.1"><p id="p64657722"><a name="p64657722"></a><a name="p64657722"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.96%" id="mcps1.2.4.1.2"><p id="p48285594171334"><a name="p48285594171334"></a><a name="p48285594171334"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.760000000000005%" id="mcps1.2.4.1.3"><p id="p24185120"><a name="p24185120"></a><a name="p24185120"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12837735"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p33223577"><a name="p33223577"></a><a name="p33223577"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="p18819060171334"><a name="p18819060171334"></a><a name="p18819060171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="ul144011136327"></a><a name="ul144011136327"></a><ul id="ul144011136327"><li>Specifies the bandwidth name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="row61765553"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p36953931"><a name="p36953931"></a><a name="p36953931"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="p47948882171334"><a name="p47948882171334"></a><a name="p47948882171334"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="ul334719207325"></a><a name="ul334719207325"></a><ul id="ul334719207325"><li>Specifies the bandwidth size.</li><li>The value ranges from 1 Mbit/s to 1000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the bandwidth range of each region on the management console.)</li></ul>
    </td>
    </tr>
    <tr id="row63416368"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p36452220"><a name="p36452220"></a><a name="p36452220"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="p58654237171334"><a name="p58654237171334"></a><a name="p58654237171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><p id="p17440495"><a name="p17440495"></a><a name="p17440495"></a>Specifies the bandwidth ID, which uniquely identifies the bandwidth.</p>
    </td>
    </tr>
    <tr id="row22746728"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p30545685"><a name="p30545685"></a><a name="p30545685"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="p53372732171334"><a name="p53372732171334"></a><a name="p53372732171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="ul26455237335"></a><a name="ul26455237335"></a><ul id="ul26455237335"><li>The value is <strong id="b25288513165924"><a name="b25288513165924"></a><a name="b25288513165924"></a>PER</strong>, indicating that the bandwidth is dedicated.</li></ul>
    </td>
    </tr>
    <tr id="row51058985"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p42137138"><a name="p42137138"></a><a name="p42137138"></a>publicip_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="p26395826172022"><a name="p26395826172022"></a><a name="p26395826172022"></a>Array of <a href="#table30936422">publicip_info</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="ul187519405337"></a><a name="ul187519405337"></a><ul id="ul187519405337"><li>Specifies information about the EIP that uses the bandwidth. For details, see <a href="#table30936422">Table 4</a>.</li></ul>
    </td>
    </tr>
    <tr id="row36079911"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p36791668"><a name="p36791668"></a><a name="p36791668"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="p4444568171334"><a name="p4444568171334"></a><a name="p4444568171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><p id="p61029421345"><a name="p61029421345"></a><a name="p61029421345"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row8730397"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p36073588"><a name="p36073588"></a><a name="p36073588"></a>bandwidth_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="p24465700171334"><a name="p24465700171334"></a><a name="p24465700171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="ul6910164734619"></a><a name="ul6910164734619"></a><ul id="ul6910164734619"><li>Specifies the bandwidth type.</li><li>The value is <strong id="b842352706102437"><a name="b842352706102437"></a><a name="b842352706102437"></a>bgp</strong>. </li></ul>
    </td>
    </tr>
    <tr id="row2300081817338"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p3464166173311"><a name="p3464166173311"></a><a name="p3464166173311"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="p45598234173311"><a name="p45598234173311"></a><a name="p45598234173311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="ul15362566343"></a><a name="ul15362566343"></a><ul id="ul15362566343"><li>If the value is <strong id="b13611135114303"><a name="b13611135114303"></a><a name="b13611135114303"></a>traffic</strong>, the bandwidth is billed by traffic.</li></ul>
    </td>
    </tr>
    <tr id="row915144611317"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="p6438749153119"><a name="p6438749153119"></a><a name="p6438749153119"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="p1843814491317"><a name="p1843814491317"></a><a name="p1843814491317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="ul114381249113115"></a><a name="ul114381249113115"></a><ul id="ul114381249113115"><li>Specifies the bandwidth status.</li><li>Possible values are as follows:<a name="ul1943874963116"></a><a name="ul1943874963116"></a><ul id="ul1943874963116"><li><strong id="b84235270610153"><a name="b84235270610153"></a><a name="b84235270610153"></a>FREEZED</strong> (Frozen)</li><li><strong id="b53754535164857"><a name="b53754535164857"></a><a name="b53754535164857"></a>NORMAL</strong> (Normal)</li></ul>
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
    <tr id="row4287423"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p11736974"><a name="p11736974"></a><a name="p11736974"></a>publicip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="p852626317154"><a name="p852626317154"></a><a name="p852626317154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><p id="p23386368"><a name="p23386368"></a><a name="p23386368"></a>Specifies the obtained EIP if only IPv4 EIPs are available. </p>
    </td>
    </tr>
    <tr id="row9150720"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="p3010817"><a name="p3010817"></a><a name="p3010817"></a>publicip_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="p1953867017154"><a name="p1953867017154"></a><a name="p1953867017154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><a name="ul11964539104914"></a><a name="ul11964539104914"></a><ul id="ul11964539104914"><li>Specifies the EIP type.</li><li>The value can be <strong id="b065211252535"><a name="b065211252535"></a><a name="b065211252535"></a>5_bgp</strong> and <strong id="b3653112535314"><a name="b3653112535314"></a><a name="b3653112535314"></a>5_mailbgp</strong>.</li><li>The configured value must be supported by the system. </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "bandwidth": {
        "id": "3cbd5ae9-368f-4bc8-8841-f2ecc322c64a",
        "name": "EIPResourceSetup_1553594229",
        "size": 5,
        "share_type": "PER",
        "publicip_info": [
          {
            "publicip_id": "22b02f40-b95f-465a-ae9b-7c8b0f042a41",
            "publicip_address": "10.xx.xx.62",
            "ip_version": 4,
            "publicip_type": "5_bgp"
          }
        ],
        "tenant_id": "26ae5181a416420998eb2093aaed84d9",
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

