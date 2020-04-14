# Querying a Bandwidth<a name="eip_apiBandwidth_0001"></a>

## Function<a name="en-us_topic_0201534167_section65488131"></a>

This API is used to query details about a bandwidth.

## URI<a name="en-us_topic_0201534167_section52522275"></a>

GET /v1/\{project\_id\}/bandwidths/\{bandwidth\_id\}

[Table 1](#en-us_topic_0201534167_table40002310)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534167_table40002310"></a>
<table><thead align="left"><tr id="en-us_topic_0201534167_row55023063"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534167_p27683123"><a name="en-us_topic_0201534167_p27683123"></a><a name="en-us_topic_0201534167_p27683123"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534167_p27740487"><a name="en-us_topic_0201534167_p27740487"></a><a name="en-us_topic_0201534167_p27740487"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534167_p32387004"><a name="en-us_topic_0201534167_p32387004"></a><a name="en-us_topic_0201534167_p32387004"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534167_row6101690"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p24474856"><a name="en-us_topic_0201534167_p24474856"></a><a name="en-us_topic_0201534167_p24474856"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p36306286"><a name="en-us_topic_0201534167_p36306286"></a><a name="en-us_topic_0201534167_p36306286"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534167_p10487112"><a name="en-us_topic_0201534167_p10487112"></a><a name="en-us_topic_0201534167_p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="en-us_topic_0201534167_row26390432"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p57250251"><a name="en-us_topic_0201534167_p57250251"></a><a name="en-us_topic_0201534167_p57250251"></a>bandwidth_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p6758730"><a name="en-us_topic_0201534167_p6758730"></a><a name="en-us_topic_0201534167_p6758730"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534167_p10586246"><a name="en-us_topic_0201534167_p10586246"></a><a name="en-us_topic_0201534167_p10586246"></a>Specifies the bandwidth ID, which uniquely identifies the bandwidth.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534167_section2938434"></a>

-   Request parameter

    None

-   Example request

    None


## Response Message<a name="en-us_topic_0201534167_section26445914"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="en-us_topic_0201534167_table16054594155348"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534167_row50617932155348"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534167_p6411865155348"><a name="en-us_topic_0201534167_p6411865155348"></a><a name="en-us_topic_0201534167_p6411865155348"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534167_p58099771155348"><a name="en-us_topic_0201534167_p58099771155348"></a><a name="en-us_topic_0201534167_p58099771155348"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534167_p8461025155348"><a name="en-us_topic_0201534167_p8461025155348"></a><a name="en-us_topic_0201534167_p8461025155348"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534167_row14254431155348"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p13758302155348"><a name="en-us_topic_0201534167_p13758302155348"></a><a name="en-us_topic_0201534167_p13758302155348"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p6803198155348"><a name="en-us_topic_0201534167_p6803198155348"></a><a name="en-us_topic_0201534167_p6803198155348"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534167_p60584419155348"><a name="en-us_topic_0201534167_p60584419155348"></a><a name="en-us_topic_0201534167_p60584419155348"></a>Specifies the bandwidth object.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **bandwidth**  field

    <a name="en-us_topic_0201534167_table60972066"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534167_row10740297"><th class="cellrowborder" valign="top" width="25.28%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534167_p64657722"><a name="en-us_topic_0201534167_p64657722"></a><a name="en-us_topic_0201534167_p64657722"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.96%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534167_p48285594171334"><a name="en-us_topic_0201534167_p48285594171334"></a><a name="en-us_topic_0201534167_p48285594171334"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.760000000000005%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534167_p24185120"><a name="en-us_topic_0201534167_p24185120"></a><a name="en-us_topic_0201534167_p24185120"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534167_row12837735"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p33223577"><a name="en-us_topic_0201534167_p33223577"></a><a name="en-us_topic_0201534167_p33223577"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p18819060171334"><a name="en-us_topic_0201534167_p18819060171334"></a><a name="en-us_topic_0201534167_p18819060171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534167_ul144011136327"></a><a name="en-us_topic_0201534167_ul144011136327"></a><ul id="en-us_topic_0201534167_ul144011136327"><li>Specifies the bandwidth name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534167_row61765553"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p36953931"><a name="en-us_topic_0201534167_p36953931"></a><a name="en-us_topic_0201534167_p36953931"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p47948882171334"><a name="en-us_topic_0201534167_p47948882171334"></a><a name="en-us_topic_0201534167_p47948882171334"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534167_ul334719207325"></a><a name="en-us_topic_0201534167_ul334719207325"></a><ul id="en-us_topic_0201534167_ul334719207325"><li>Specifies the bandwidth size.</li><li>The value ranges from 1 Mbit/s to 1000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the bandwidth range of each region on the management console.)</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534167_row63416368"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p36452220"><a name="en-us_topic_0201534167_p36452220"></a><a name="en-us_topic_0201534167_p36452220"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p58654237171334"><a name="en-us_topic_0201534167_p58654237171334"></a><a name="en-us_topic_0201534167_p58654237171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534167_p17440495"><a name="en-us_topic_0201534167_p17440495"></a><a name="en-us_topic_0201534167_p17440495"></a>Specifies the bandwidth ID, which uniquely identifies the bandwidth.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534167_row22746728"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p30545685"><a name="en-us_topic_0201534167_p30545685"></a><a name="en-us_topic_0201534167_p30545685"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p53372732171334"><a name="en-us_topic_0201534167_p53372732171334"></a><a name="en-us_topic_0201534167_p53372732171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534167_ul26455237335"></a><a name="en-us_topic_0201534167_ul26455237335"></a><ul id="en-us_topic_0201534167_ul26455237335"><li>The value is <strong id="en-us_topic_0201534167_b25288513165924"><a name="en-us_topic_0201534167_b25288513165924"></a><a name="en-us_topic_0201534167_b25288513165924"></a>PER</strong>, indicating that the bandwidth is dedicated.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534167_row51058985"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p42137138"><a name="en-us_topic_0201534167_p42137138"></a><a name="en-us_topic_0201534167_p42137138"></a>publicip_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p26395826172022"><a name="en-us_topic_0201534167_p26395826172022"></a><a name="en-us_topic_0201534167_p26395826172022"></a>Array of <a href="#en-us_topic_0201534167_table30936422">publicip_info</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534167_ul187519405337"></a><a name="en-us_topic_0201534167_ul187519405337"></a><ul id="en-us_topic_0201534167_ul187519405337"><li>Specifies information about the EIP that uses the bandwidth. For details, see <a href="#en-us_topic_0201534167_table30936422">Table 4</a>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534167_row36079911"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p36791668"><a name="en-us_topic_0201534167_p36791668"></a><a name="en-us_topic_0201534167_p36791668"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p4444568171334"><a name="en-us_topic_0201534167_p4444568171334"></a><a name="en-us_topic_0201534167_p4444568171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534167_p61029421345"><a name="en-us_topic_0201534167_p61029421345"></a><a name="en-us_topic_0201534167_p61029421345"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534167_row8730397"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p36073588"><a name="en-us_topic_0201534167_p36073588"></a><a name="en-us_topic_0201534167_p36073588"></a>bandwidth_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p24465700171334"><a name="en-us_topic_0201534167_p24465700171334"></a><a name="en-us_topic_0201534167_p24465700171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534167_ul6910164734619"></a><a name="en-us_topic_0201534167_ul6910164734619"></a><ul id="en-us_topic_0201534167_ul6910164734619"><li>Specifies the bandwidth type.</li><li>The value is <strong id="en-us_topic_0201534167_b842352706102437"><a name="en-us_topic_0201534167_b842352706102437"></a><a name="en-us_topic_0201534167_b842352706102437"></a>bgp</strong>. </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534167_row2300081817338"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p3464166173311"><a name="en-us_topic_0201534167_p3464166173311"></a><a name="en-us_topic_0201534167_p3464166173311"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p45598234173311"><a name="en-us_topic_0201534167_p45598234173311"></a><a name="en-us_topic_0201534167_p45598234173311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534167_ul15362566343"></a><a name="en-us_topic_0201534167_ul15362566343"></a><ul id="en-us_topic_0201534167_ul15362566343"><li>If the value is <strong id="en-us_topic_0201534167_b13611135114303"><a name="en-us_topic_0201534167_b13611135114303"></a><a name="en-us_topic_0201534167_b13611135114303"></a>traffic</strong>, the bandwidth is billed by traffic.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534167_row915144611317"><td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p6438749153119"><a name="en-us_topic_0201534167_p6438749153119"></a><a name="en-us_topic_0201534167_p6438749153119"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.96%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p1843814491317"><a name="en-us_topic_0201534167_p1843814491317"></a><a name="en-us_topic_0201534167_p1843814491317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534167_ul114381249113115"></a><a name="en-us_topic_0201534167_ul114381249113115"></a><ul id="en-us_topic_0201534167_ul114381249113115"><li>Specifies the bandwidth status.</li><li>Possible values are as follows:<a name="en-us_topic_0201534167_ul1943874963116"></a><a name="en-us_topic_0201534167_ul1943874963116"></a><ul id="en-us_topic_0201534167_ul1943874963116"><li><strong id="en-us_topic_0201534167_b84235270610153"><a name="en-us_topic_0201534167_b84235270610153"></a><a name="en-us_topic_0201534167_b84235270610153"></a>FREEZED</strong> (Frozen)</li><li><strong id="en-us_topic_0201534167_b53754535164857"><a name="en-us_topic_0201534167_b53754535164857"></a><a name="en-us_topic_0201534167_b53754535164857"></a>NORMAL</strong> (Normal)</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **publicip\_info**  object

    <a name="en-us_topic_0201534167_table30936422"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534167_row17161430"><th class="cellrowborder" valign="top" width="25.740000000000002%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534167_p47898561"><a name="en-us_topic_0201534167_p47898561"></a><a name="en-us_topic_0201534167_p47898561"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.5%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534167_p2828296517154"><a name="en-us_topic_0201534167_p2828296517154"></a><a name="en-us_topic_0201534167_p2828296517154"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.76%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534167_p58761073"><a name="en-us_topic_0201534167_p58761073"></a><a name="en-us_topic_0201534167_p58761073"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534167_row62026502"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p58090788"><a name="en-us_topic_0201534167_p58090788"></a><a name="en-us_topic_0201534167_p58090788"></a>publicip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p921881117154"><a name="en-us_topic_0201534167_p921881117154"></a><a name="en-us_topic_0201534167_p921881117154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534167_p476380"><a name="en-us_topic_0201534167_p476380"></a><a name="en-us_topic_0201534167_p476380"></a>Specifies the ID of the EIP that uses the bandwidth.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534167_row4287423"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p11736974"><a name="en-us_topic_0201534167_p11736974"></a><a name="en-us_topic_0201534167_p11736974"></a>publicip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p852626317154"><a name="en-us_topic_0201534167_p852626317154"></a><a name="en-us_topic_0201534167_p852626317154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534167_p23386368"><a name="en-us_topic_0201534167_p23386368"></a><a name="en-us_topic_0201534167_p23386368"></a>Specifies the obtained EIP if only IPv4 EIPs are available. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534167_row9150720"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534167_p3010817"><a name="en-us_topic_0201534167_p3010817"></a><a name="en-us_topic_0201534167_p3010817"></a>publicip_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534167_p1953867017154"><a name="en-us_topic_0201534167_p1953867017154"></a><a name="en-us_topic_0201534167_p1953867017154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534167_ul11964539104914"></a><a name="en-us_topic_0201534167_ul11964539104914"></a><ul id="en-us_topic_0201534167_ul11964539104914"><li>Specifies the EIP type.</li><li>The value can be <strong id="en-us_topic_0201534167_b065211252535"><a name="en-us_topic_0201534167_b065211252535"></a><a name="en-us_topic_0201534167_b065211252535"></a>5_bgp</strong> and <strong id="en-us_topic_0201534167_b3653112535314"><a name="en-us_topic_0201534167_b3653112535314"></a><a name="en-us_topic_0201534167_b3653112535314"></a>5_mailbgp</strong>.</li><li>The configured value must be supported by the system. </li></ul>
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


## Status Code<a name="en-us_topic_0201534167_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534167_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

