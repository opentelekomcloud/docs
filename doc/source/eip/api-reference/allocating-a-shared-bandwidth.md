# Allocating a Shared Bandwidth<a name="eip_apisharedbandwidth_0001"></a>

## Function<a name="en-us_topic_0201534115_section65488131"></a>

This API is used to allocate a shared bandwidth.

## URI<a name="en-us_topic_0201534115_section52522275"></a>

POST /v2.0/\{project\_id\}/bandwidths

[Table 1](#en-us_topic_0201534115_table40002310)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534115_table40002310"></a>
<table><thead align="left"><tr id="en-us_topic_0201534115_row55023063"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534115_p27683123"><a name="en-us_topic_0201534115_p27683123"></a><a name="en-us_topic_0201534115_p27683123"></a><strong id="en-us_topic_0201534115_b842352706195711"><a name="en-us_topic_0201534115_b842352706195711"></a><a name="en-us_topic_0201534115_b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534115_p27740487"><a name="en-us_topic_0201534115_p27740487"></a><a name="en-us_topic_0201534115_p27740487"></a><strong id="en-us_topic_0201534115_b84235270615219"><a name="en-us_topic_0201534115_b84235270615219"></a><a name="en-us_topic_0201534115_b84235270615219"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534115_p32387004"><a name="en-us_topic_0201534115_p32387004"></a><a name="en-us_topic_0201534115_p32387004"></a><strong id="en-us_topic_0201534115_b8423527061645"><a name="en-us_topic_0201534115_b8423527061645"></a><a name="en-us_topic_0201534115_b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534115_row6101690"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p24474856"><a name="en-us_topic_0201534115_p24474856"></a><a name="en-us_topic_0201534115_p24474856"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p36306286"><a name="en-us_topic_0201534115_p36306286"></a><a name="en-us_topic_0201534115_p36306286"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534115_p10487112"><a name="en-us_topic_0201534115_p10487112"></a><a name="en-us_topic_0201534115_p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534115_section1838275013814"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="en-us_topic_0201534115_table62031189151043"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534115_row4339910151043"><th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534115_p15988448151043"><a name="en-us_topic_0201534115_p15988448151043"></a><a name="en-us_topic_0201534115_p15988448151043"></a><strong id="en-us_topic_0201534115_b1130454113"><a name="en-us_topic_0201534115_b1130454113"></a><a name="en-us_topic_0201534115_b1130454113"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534115_p19995902151043"><a name="en-us_topic_0201534115_p19995902151043"></a><a name="en-us_topic_0201534115_p19995902151043"></a><strong id="en-us_topic_0201534115_b251887268"><a name="en-us_topic_0201534115_b251887268"></a><a name="en-us_topic_0201534115_b251887268"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534115_p9055369151043"><a name="en-us_topic_0201534115_p9055369151043"></a><a name="en-us_topic_0201534115_p9055369151043"></a><strong id="en-us_topic_0201534115_b842352706145623"><a name="en-us_topic_0201534115_b842352706145623"></a><a name="en-us_topic_0201534115_b842352706145623"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.18%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534115_p62396264151043"><a name="en-us_topic_0201534115_p62396264151043"></a><a name="en-us_topic_0201534115_p62396264151043"></a><strong id="en-us_topic_0201534115_b1345192204"><a name="en-us_topic_0201534115_b1345192204"></a><a name="en-us_topic_0201534115_b1345192204"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534115_row13560713151050"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534115_p24675975151050"><a name="en-us_topic_0201534115_p24675975151050"></a><a name="en-us_topic_0201534115_p24675975151050"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534115_p52596998151050"><a name="en-us_topic_0201534115_p52596998151050"></a><a name="en-us_topic_0201534115_p52596998151050"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534115_p12429959151120"><a name="en-us_topic_0201534115_p12429959151120"></a><a name="en-us_topic_0201534115_p12429959151120"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534115_p1744019151120"><a name="en-us_topic_0201534115_p1744019151120"></a><a name="en-us_topic_0201534115_p1744019151120"></a>Specifies the bandwidth objects. For details, see <a href="#en-us_topic_0201534115_table11041789">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **bandwidth**  field

    <a name="en-us_topic_0201534115_table11041789"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534115_row60677888"><th class="cellrowborder" valign="top" width="30.82691730826917%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534115_p15961928"><a name="en-us_topic_0201534115_p15961928"></a><a name="en-us_topic_0201534115_p15961928"></a><strong id="en-us_topic_0201534115_b1210086870"><a name="en-us_topic_0201534115_b1210086870"></a><a name="en-us_topic_0201534115_b1210086870"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.108289171082887%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534115_p17847776"><a name="en-us_topic_0201534115_p17847776"></a><a name="en-us_topic_0201534115_p17847776"></a><strong id="en-us_topic_0201534115_b1975046447"><a name="en-us_topic_0201534115_b1975046447"></a><a name="en-us_topic_0201534115_b1975046447"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.237876212378758%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534115_p3784029918155"><a name="en-us_topic_0201534115_p3784029918155"></a><a name="en-us_topic_0201534115_p3784029918155"></a><strong id="en-us_topic_0201534115_b1612043368"><a name="en-us_topic_0201534115_b1612043368"></a><a name="en-us_topic_0201534115_b1612043368"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.82691730826917%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534115_p36383728"><a name="en-us_topic_0201534115_p36383728"></a><a name="en-us_topic_0201534115_p36383728"></a><strong id="en-us_topic_0201534115_b160541551"><a name="en-us_topic_0201534115_b160541551"></a><a name="en-us_topic_0201534115_b160541551"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534115_row61400865"><td class="cellrowborder" valign="top" width="30.82691730826917%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534115_p7414170"><a name="en-us_topic_0201534115_p7414170"></a><a name="en-us_topic_0201534115_p7414170"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.108289171082887%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534115_p1525924410101"><a name="en-us_topic_0201534115_p1525924410101"></a><a name="en-us_topic_0201534115_p1525924410101"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.237876212378758%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534115_p4516535118155"><a name="en-us_topic_0201534115_p4516535118155"></a><a name="en-us_topic_0201534115_p4516535118155"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.82691730826917%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534115_p31677898"><a name="en-us_topic_0201534115_p31677898"></a><a name="en-us_topic_0201534115_p31677898"></a>Specifies the bandwidth name.</p>
    <p id="en-us_topic_0201534115_p57557895"><a name="en-us_topic_0201534115_p57557895"></a><a name="en-us_topic_0201534115_p57557895"></a>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534115_row15772917"><td class="cellrowborder" valign="top" width="30.82691730826917%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534115_p2537905"><a name="en-us_topic_0201534115_p2537905"></a><a name="en-us_topic_0201534115_p2537905"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.108289171082887%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534115_p4243749"><a name="en-us_topic_0201534115_p4243749"></a><a name="en-us_topic_0201534115_p4243749"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.237876212378758%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534115_p3451484018155"><a name="en-us_topic_0201534115_p3451484018155"></a><a name="en-us_topic_0201534115_p3451484018155"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.82691730826917%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0201534115_ul9790510185"></a><a name="en-us_topic_0201534115_ul9790510185"></a><ul id="en-us_topic_0201534115_ul9790510185"><li>Specifies the bandwidth size. The shared bandwidth has a minimum limit, which may vary depending on sites. The default minimum value is 5 Mbit/s.</li><li>The value ranges from 5 Mbit/s to 2000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the available bandwidth range on the management console.)</li><li>If a decimal fraction (for example <strong>10.2</strong>) or a character string (for example <strong>"10"</strong>) is specified, the specified value will be automatically converted to an integer.</li><li>The minimum unit for bandwidth adjustment varies depending on the bandwidth range. The details are as follows:<a name="en-us_topic_0201534115_ul8496121414572"></a><a name="en-us_topic_0201534115_ul8496121414572"></a><ul id="en-us_topic_0201534115_ul8496121414572"><li>The minimum unit is 1 Mbit/s if the allowed bandwidth size ranges from 0 to 300 Mbit/s (with 300 Mbit/s included).</li><li>The minimum unit is 50 Mbit/s if the allowed bandwidth size ranges 300 Mbit/s to 1000 Mbit/s (with 1000 Mbit/s included).</li><li>The minimum unit is 500 Mbit/s if the allowed bandwidth size is greater than 1000 Mbit/s.</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{Endpoint}/v2.0/{project_id}/bandwidths
    
    {
        "bandwidth": {
            "name": "bandwidth123",
            "size": 10
        }
    }
    ```


## Response Message<a name="en-us_topic_0201534115_section1412808"></a>

-   Response parameter

    **Table  4**  Response parameter

    <a name="en-us_topic_0201534115_table16054594155348"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534115_row50617932155348"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534115_p6411865155348"><a name="en-us_topic_0201534115_p6411865155348"></a><a name="en-us_topic_0201534115_p6411865155348"></a><strong id="en-us_topic_0201534115_b189172116"><a name="en-us_topic_0201534115_b189172116"></a><a name="en-us_topic_0201534115_b189172116"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534115_p58099771155348"><a name="en-us_topic_0201534115_p58099771155348"></a><a name="en-us_topic_0201534115_p58099771155348"></a><strong id="en-us_topic_0201534115_b1939014495"><a name="en-us_topic_0201534115_b1939014495"></a><a name="en-us_topic_0201534115_b1939014495"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534115_p8461025155348"><a name="en-us_topic_0201534115_p8461025155348"></a><a name="en-us_topic_0201534115_p8461025155348"></a><strong id="en-us_topic_0201534115_b1057182162"><a name="en-us_topic_0201534115_b1057182162"></a><a name="en-us_topic_0201534115_b1057182162"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534115_row14254431155348"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p13758302155348"><a name="en-us_topic_0201534115_p13758302155348"></a><a name="en-us_topic_0201534115_p13758302155348"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p6803198155348"><a name="en-us_topic_0201534115_p6803198155348"></a><a name="en-us_topic_0201534115_p6803198155348"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534115_p60584419155348"><a name="en-us_topic_0201534115_p60584419155348"></a><a name="en-us_topic_0201534115_p60584419155348"></a>Specifies the bandwidth objects. For details, see <a href="#en-us_topic_0201534115_table60972066">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Description of the  **bandwidth**  field

    <a name="en-us_topic_0201534115_table60972066"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534115_row10740297"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534115_p64657722"><a name="en-us_topic_0201534115_p64657722"></a><a name="en-us_topic_0201534115_p64657722"></a><strong id="en-us_topic_0201534115_b300456131"><a name="en-us_topic_0201534115_b300456131"></a><a name="en-us_topic_0201534115_b300456131"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534115_p48285594171334"><a name="en-us_topic_0201534115_p48285594171334"></a><a name="en-us_topic_0201534115_p48285594171334"></a><strong id="en-us_topic_0201534115_b862887105"><a name="en-us_topic_0201534115_b862887105"></a><a name="en-us_topic_0201534115_b862887105"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534115_p24185120"><a name="en-us_topic_0201534115_p24185120"></a><a name="en-us_topic_0201534115_p24185120"></a><strong id="en-us_topic_0201534115_b859677418"><a name="en-us_topic_0201534115_b859677418"></a><a name="en-us_topic_0201534115_b859677418"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534115_row12837735"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p33223577"><a name="en-us_topic_0201534115_p33223577"></a><a name="en-us_topic_0201534115_p33223577"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p18819060171334"><a name="en-us_topic_0201534115_p18819060171334"></a><a name="en-us_topic_0201534115_p18819060171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534115_ul181211824134816"></a><a name="en-us_topic_0201534115_ul181211824134816"></a><ul id="en-us_topic_0201534115_ul181211824134816"><li>Specifies the bandwidth name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534115_row61765553"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p36953931"><a name="en-us_topic_0201534115_p36953931"></a><a name="en-us_topic_0201534115_p36953931"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p47948882171334"><a name="en-us_topic_0201534115_p47948882171334"></a><a name="en-us_topic_0201534115_p47948882171334"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534115_ul19451840174816"></a><a name="en-us_topic_0201534115_ul19451840174816"></a><ul id="en-us_topic_0201534115_ul19451840174816"><li>Specifies the bandwidth size.</li><li>The value ranges from 5 Mbit/s to 2000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the available bandwidth range on the management console.)</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534115_row63416368"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p36452220"><a name="en-us_topic_0201534115_p36452220"></a><a name="en-us_topic_0201534115_p36452220"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p58654237171334"><a name="en-us_topic_0201534115_p58654237171334"></a><a name="en-us_topic_0201534115_p58654237171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534115_p17440495"><a name="en-us_topic_0201534115_p17440495"></a><a name="en-us_topic_0201534115_p17440495"></a>Specifies the bandwidth ID, which uniquely identifies the bandwidth.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534115_row22746728"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p30545685"><a name="en-us_topic_0201534115_p30545685"></a><a name="en-us_topic_0201534115_p30545685"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p53372732171334"><a name="en-us_topic_0201534115_p53372732171334"></a><a name="en-us_topic_0201534115_p53372732171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534115_ul4262181884915"></a><a name="en-us_topic_0201534115_ul4262181884915"></a><ul id="en-us_topic_0201534115_ul4262181884915"><li>Specifies whether the bandwidth is shared or dedicated.</li><li>The value can be <strong>PER</strong> or <strong>WHOLE</strong>.<a name="en-us_topic_0201534115_ul313253512484"></a><a name="en-us_topic_0201534115_ul313253512484"></a><ul id="en-us_topic_0201534115_ul313253512484"><li><strong id="en-us_topic_0201534115_b16682925181913"><a name="en-us_topic_0201534115_b16682925181913"></a><a name="en-us_topic_0201534115_b16682925181913"></a>WHOLE</strong>: Shared bandwidth</li><li><strong id="en-us_topic_0201534115_b154451296198"><a name="en-us_topic_0201534115_b154451296198"></a><a name="en-us_topic_0201534115_b154451296198"></a>PER</strong>: Dedicated bandwidth</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534115_row51058985"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p42137138"><a name="en-us_topic_0201534115_p42137138"></a><a name="en-us_topic_0201534115_p42137138"></a>publicip_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p28224024171334"><a name="en-us_topic_0201534115_p28224024171334"></a><a name="en-us_topic_0201534115_p28224024171334"></a>Array of <a href="#en-us_topic_0201534115_table30936422">publicip_info</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534115_ul14114132894913"></a><a name="en-us_topic_0201534115_ul14114132894913"></a><ul id="en-us_topic_0201534115_ul14114132894913"><li>Specifies information about the EIP that uses the bandwidth. For details, see <a href="#en-us_topic_0201534115_table30936422">Table 6</a>.</li><li>The bandwidth, whose type is <strong id="en-us_topic_0201534115_b967111236338"><a name="en-us_topic_0201534115_b967111236338"></a><a name="en-us_topic_0201534115_b967111236338"></a>WHOLE</strong>, can be used by multiple EIPs. The bandwidth, whose type is <strong id="en-us_topic_0201534115_b15673102310332"><a name="en-us_topic_0201534115_b15673102310332"></a><a name="en-us_topic_0201534115_b15673102310332"></a>PER</strong>, can be used by only one EIP.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534115_row36079911"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p36791668"><a name="en-us_topic_0201534115_p36791668"></a><a name="en-us_topic_0201534115_p36791668"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p4444568171334"><a name="en-us_topic_0201534115_p4444568171334"></a><a name="en-us_topic_0201534115_p4444568171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534115_p16528103118518"><a name="en-us_topic_0201534115_p16528103118518"></a><a name="en-us_topic_0201534115_p16528103118518"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534115_row8730397"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p36073588"><a name="en-us_topic_0201534115_p36073588"></a><a name="en-us_topic_0201534115_p36073588"></a>bandwidth_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p24465700171334"><a name="en-us_topic_0201534115_p24465700171334"></a><a name="en-us_topic_0201534115_p24465700171334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534115_ul5731955125012"></a><a name="en-us_topic_0201534115_ul5731955125012"></a><ul id="en-us_topic_0201534115_ul5731955125012"><li>Specifies the bandwidth type. The default value for the shared bandwidth is <strong id="en-us_topic_0201534115_b750936389173824"><a name="en-us_topic_0201534115_b750936389173824"></a><a name="en-us_topic_0201534115_b750936389173824"></a>share</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534115_row2300081817338"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p3464166173311"><a name="en-us_topic_0201534115_p3464166173311"></a><a name="en-us_topic_0201534115_p3464166173311"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p45598234173311"><a name="en-us_topic_0201534115_p45598234173311"></a><a name="en-us_topic_0201534115_p45598234173311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534115_ul193819183512"></a><a name="en-us_topic_0201534115_ul193819183512"></a><ul id="en-us_topic_0201534115_ul193819183512"><li>Specifies that the bandwidth is billed by bandwidth.</li><li>The value can be <strong id="en-us_topic_0201534115_b842352706191239"><a name="en-us_topic_0201534115_b842352706191239"></a><a name="en-us_topic_0201534115_b842352706191239"></a>traffic</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534115_row9477203041814"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p16479330181816"><a name="en-us_topic_0201534115_p16479330181816"></a><a name="en-us_topic_0201534115_p16479330181816"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p5479163011185"><a name="en-us_topic_0201534115_p5479163011185"></a><a name="en-us_topic_0201534115_p5479163011185"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534115_ul114381249113115"></a><a name="en-us_topic_0201534115_ul114381249113115"></a><ul id="en-us_topic_0201534115_ul114381249113115"><li>Specifies the bandwidth status.</li><li>Possible values are as follows:<a name="en-us_topic_0201534115_ul1943874963116"></a><a name="en-us_topic_0201534115_ul1943874963116"></a><ul id="en-us_topic_0201534115_ul1943874963116"><li><strong id="en-us_topic_0201534115_b84235270610153"><a name="en-us_topic_0201534115_b84235270610153"></a><a name="en-us_topic_0201534115_b84235270610153"></a>FREEZED</strong> (Frozen)</li><li><strong id="en-us_topic_0201534115_b53754535164857"><a name="en-us_topic_0201534115_b53754535164857"></a><a name="en-us_topic_0201534115_b53754535164857"></a>NORMAL</strong> (Normal)</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **publicip\_info**  object

    <a name="en-us_topic_0201534115_table30936422"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534115_row17161430"><th class="cellrowborder" valign="top" width="25.740000000000002%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534115_p47898561"><a name="en-us_topic_0201534115_p47898561"></a><a name="en-us_topic_0201534115_p47898561"></a><strong id="en-us_topic_0201534115_b359857734"><a name="en-us_topic_0201534115_b359857734"></a><a name="en-us_topic_0201534115_b359857734"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.5%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534115_p2828296517154"><a name="en-us_topic_0201534115_p2828296517154"></a><a name="en-us_topic_0201534115_p2828296517154"></a><strong id="en-us_topic_0201534115_b209122150"><a name="en-us_topic_0201534115_b209122150"></a><a name="en-us_topic_0201534115_b209122150"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.76%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534115_p58761073"><a name="en-us_topic_0201534115_p58761073"></a><a name="en-us_topic_0201534115_p58761073"></a><strong id="en-us_topic_0201534115_b2078255891"><a name="en-us_topic_0201534115_b2078255891"></a><a name="en-us_topic_0201534115_b2078255891"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534115_row62026502"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p58090788"><a name="en-us_topic_0201534115_p58090788"></a><a name="en-us_topic_0201534115_p58090788"></a>publicip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p921881117154"><a name="en-us_topic_0201534115_p921881117154"></a><a name="en-us_topic_0201534115_p921881117154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534115_p3792141220526"><a name="en-us_topic_0201534115_p3792141220526"></a><a name="en-us_topic_0201534115_p3792141220526"></a>Specifies the ID of the EIP that uses the bandwidth.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534115_row1565124218464"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p621304517467"><a name="en-us_topic_0201534115_p621304517467"></a><a name="en-us_topic_0201534115_p621304517467"></a>publicip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p1021574544615"><a name="en-us_topic_0201534115_p1021574544615"></a><a name="en-us_topic_0201534115_p1021574544615"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534115_p198309316175"><a name="en-us_topic_0201534115_p198309316175"></a><a name="en-us_topic_0201534115_p198309316175"></a>Specifies the obtained EIP if only IPv4 EIPs are available. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534115_row9150720"><td class="cellrowborder" valign="top" width="25.740000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534115_p3010817"><a name="en-us_topic_0201534115_p3010817"></a><a name="en-us_topic_0201534115_p3010817"></a>publicip_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.5%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534115_p1953867017154"><a name="en-us_topic_0201534115_p1953867017154"></a><a name="en-us_topic_0201534115_p1953867017154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534115_ul13831731151713"></a><a name="en-us_topic_0201534115_ul13831731151713"></a><ul id="en-us_topic_0201534115_ul13831731151713"><li>Specifies the EIP type.</li><li>The value can be <strong id="en-us_topic_0201534115_b678774411214"><a name="en-us_topic_0201534115_b678774411214"></a><a name="en-us_topic_0201534115_b678774411214"></a>5_bgp</strong> and <strong id="en-us_topic_0201534115_b19788544026"><a name="en-us_topic_0201534115_b19788544026"></a><a name="en-us_topic_0201534115_b19788544026"></a>5_mailbgp</strong>.</li><li>The configured value must be supported by the system. </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "bandwidth": {
        "id": "1bffc5f2-ff19-45a6-96d2-dfdca49cc387",
        "name": "bandwidth123",
        "size": 10,
        "share_type": "WHOLE",
        "publicip_info": [],
        "tenant_id": "26ae5181a416420998eb2093aaed84d9",
        "bandwidth_type": "share",
        "charge_mode": "bandwidth",
        "status": "NORMAL"
      }
    }
    ```


## Status Code<a name="en-us_topic_0201534115_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534115_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

