# Querying AS Configurations<a name="EN-US_TOPIC_0043063056"></a>

## Function<a name="section27863937"></a>

This interface is used to query AS configurations based on search criteria. The results are displayed by page.

-   Search criteria can be the AS configuration name, image ID, start line number, and number of records.
-   If no search criteria are specified, a maximum of 20 AS configurations can be queried for a tenant by default.

## URI<a name="section49448848"></a>

GET /autoscaling-api/v1/\{project\_id\}/scaling\_configuration

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You can type the question mark \(?\) and ampersand \(&\) at the end of the URI to define multiple search criteria. AS configurations can be searched by all optional parameters in the following table. For details, see the example request.  

**Table  1**  Parameter description

<a name="table59952436"></a>
<table><thead align="left"><tr id="row38679683"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.1"><p id="p46046605"><a name="p46046605"></a><a name="p46046605"></a><strong id="b8717226124815"><a name="b8717226124815"></a><a name="b8717226124815"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p38787544"><a name="p38787544"></a><a name="p38787544"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p54783372"><a name="p54783372"></a><a name="p54783372"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.2.5.1.4"><p id="p8268111"><a name="p8268111"></a><a name="p8268111"></a><strong id="b1496832844814"><a name="b1496832844814"></a><a name="b1496832844814"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row65737292"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p23120425"><a name="p23120425"></a><a name="p23120425"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p60815118"><a name="p60815118"></a><a name="p60815118"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p27077540"><a name="p27077540"></a><a name="p27077540"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row9521066"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p33008913"><a name="p33008913"></a><a name="p33008913"></a>scaling_configuration_name</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p56476259"><a name="p56476259"></a><a name="p56476259"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p11174282"><a name="p11174282"></a><a name="p11174282"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="p32701678"><a name="p32701678"></a><a name="p32701678"></a>Specifies the AS configuration name.</p>
<p id="p271118441192"><a name="p271118441192"></a><a name="p271118441192"></a>Supports fuzzy search. </p>
</td>
</tr>
<tr id="row25879650"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p15876907"><a name="p15876907"></a><a name="p15876907"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p10961125"><a name="p10961125"></a><a name="p10961125"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p15435960"><a name="p15435960"></a><a name="p15435960"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="p42353227"><a name="p42353227"></a><a name="p42353227"></a>Specifies the image ID. It is same as <strong id="b13817591495328"><a name="b13817591495328"></a><a name="b13817591495328"></a>imageRef</strong>.</p>
</td>
</tr>
<tr id="row45634724"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p5425146"><a name="p5425146"></a><a name="p5425146"></a>start_number</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p36783718"><a name="p36783718"></a><a name="p36783718"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p26691149"><a name="p26691149"></a><a name="p26691149"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="p59373825"><a name="p59373825"></a><a name="p59373825"></a>Specifies the start line number. The default value is <strong id="b1052981016453"><a name="b1052981016453"></a><a name="b1052981016453"></a>0</strong>. The minimum parameter value is <strong id="b18744142621611"><a name="b18744142621611"></a><a name="b18744142621611"></a>0</strong>.</p>
</td>
</tr>
<tr id="row63386473"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p34030663"><a name="p34030663"></a><a name="p34030663"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p5020285"><a name="p5020285"></a><a name="p5020285"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p3989940"><a name="p3989940"></a><a name="p3989940"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="p21968676"><a name="p21968676"></a><a name="p21968676"></a>Specifies the number of query records. The default value is <strong id="b168447885495335"><a name="b168447885495335"></a><a name="b168447885495335"></a>20</strong>. The value range is 0 to 100.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section42386454"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query the AS configurations with image ID  **37ca2b35-6fc7-47ab-93c7-900324809c5c**.

    ```
    GET https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_configuration?image_id=37ca2b35-6fc7-47ab-93c7-900324809c5c
    ```


## Response Message<a name="section45933772"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table53507960"></a>
    <table><thead align="left"><tr id="row16725372"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p12577900"><a name="p12577900"></a><a name="p12577900"></a><strong id="b1025643012482"><a name="b1025643012482"></a><a name="b1025643012482"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="p12176960"><a name="p12176960"></a><a name="p12176960"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.4.1.3"><p id="p46809697"><a name="p46809697"></a><a name="p46809697"></a><strong id="b13645434144814"><a name="b13645434144814"></a><a name="b13645434144814"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33489078"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p28260775"><a name="p28260775"></a><a name="p28260775"></a>total_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p7421470"><a name="p7421470"></a><a name="p7421470"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p64268160"><a name="p64268160"></a><a name="p64268160"></a>Specifies the total number of query records.</p>
    </td>
    </tr>
    <tr id="row41542534"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p9502070"><a name="p9502070"></a><a name="p9502070"></a>start_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p31470215"><a name="p31470215"></a><a name="p31470215"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p66059488"><a name="p66059488"></a><a name="p66059488"></a>Specifies the start line number.</p>
    </td>
    </tr>
    <tr id="row57664488"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p40311937"><a name="p40311937"></a><a name="p40311937"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p44041463"><a name="p44041463"></a><a name="p44041463"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p10588721"><a name="p10588721"></a><a name="p10588721"></a>Specifies the number of query records.</p>
    </td>
    </tr>
    <tr id="row28189627"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1658455"><a name="p1658455"></a><a name="p1658455"></a>scaling_configurations</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p117163"><a name="p117163"></a><a name="p117163"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p9490272"><a name="p9490272"></a><a name="p9490272"></a>Specifies the AS configuration list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scaling\_configurations**  field description

    <a name="table5681858093547"></a>
    <table><thead align="left"><tr id="re3411f14be354adaa992fb18acd266b3"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="p1849874874120"><a name="p1849874874120"></a><a name="p1849874874120"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.4.1.2"><p id="a66bf54ec342041dbbdb3e94e61a16755"><a name="a66bf54ec342041dbbdb3e94e61a16755"></a><a name="a66bf54ec342041dbbdb3e94e61a16755"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65.34653465346535%" id="mcps1.2.4.1.3"><p id="p5247352114118"><a name="p5247352114118"></a><a name="p5247352114118"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r9f15de2a91214389817570a65795d934"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="a7126d41fd1b24b1eab2eda1d5a38f8e2"><a name="a7126d41fd1b24b1eab2eda1d5a38f8e2"></a><a name="a7126d41fd1b24b1eab2eda1d5a38f8e2"></a>scaling_configuration_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0021400633_p540708615530"><a name="en-us_topic_0021400633_p540708615530"></a><a name="en-us_topic_0021400633_p540708615530"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.34653465346535%" headers="mcps1.2.4.1.3 "><p id="a11b18fd45aa842a488d336849f50eeee"><a name="a11b18fd45aa842a488d336849f50eeee"></a><a name="a11b18fd45aa842a488d336849f50eeee"></a>Specifies the AS configuration ID. This parameter is globally unique.</p>
    </td>
    </tr>
    <tr id="r4a558da7a6aa4ab29aaf4550f7b1f0e0"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="a046a22f1fc274961a10019bfb674fff4"><a name="a046a22f1fc274961a10019bfb674fff4"></a><a name="a046a22f1fc274961a10019bfb674fff4"></a>tenant</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="a25cae146c2cd4a769583d20b5424e047"><a name="a25cae146c2cd4a769583d20b5424e047"></a><a name="a25cae146c2cd4a769583d20b5424e047"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.34653465346535%" headers="mcps1.2.4.1.3 "><p id="a2d4137196ed147e4a4f4e8653db5ec24"><a name="a2d4137196ed147e4a4f4e8653db5ec24"></a><a name="a2d4137196ed147e4a4f4e8653db5ec24"></a>Specifies the tenant ID.</p>
    </td>
    </tr>
    <tr id="r505b7d00ed454198a1a21dced5c0243f"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0021400633_p870139315530"><a name="en-us_topic_0021400633_p870139315530"></a><a name="en-us_topic_0021400633_p870139315530"></a>scaling_configuration_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="afb8c974ea725478993cd9a4990ca109f"><a name="afb8c974ea725478993cd9a4990ca109f"></a><a name="afb8c974ea725478993cd9a4990ca109f"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.34653465346535%" headers="mcps1.2.4.1.3 "><p id="a89afcf2708b144269ae6b3940fa2666a"><a name="a89afcf2708b144269ae6b3940fa2666a"></a><a name="a89afcf2708b144269ae6b3940fa2666a"></a>Specifies the AS configuration name.</p>
    <p id="p194013251584"><a name="p194013251584"></a><a name="p194013251584"></a>Supports fuzzy search. </p>
    </td>
    </tr>
    <tr id="r77a46c0e9c70450eb409e8ebe23beea8"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="ae15692552b404d298e68d5ef197ea04c"><a name="ae15692552b404d298e68d5ef197ea04c"></a><a name="ae15692552b404d298e68d5ef197ea04c"></a>instance_config</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="a4c03d226ca78442f99e13b8d363cd51d"><a name="a4c03d226ca78442f99e13b8d363cd51d"></a><a name="a4c03d226ca78442f99e13b8d363cd51d"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.34653465346535%" headers="mcps1.2.4.1.3 "><p id="abaccb7574422492eb4b4c527d09a3c61"><a name="abaccb7574422492eb4b4c527d09a3c61"></a><a name="abaccb7574422492eb4b4c527d09a3c61"></a>Specifies the information about instance configurations.</p>
    </td>
    </tr>
    <tr id="r3d8f7bcb6bf94470b87dacfd57738024"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="ad1ffb6d1bec1482dbccf57977263949e"><a name="ad1ffb6d1bec1482dbccf57977263949e"></a><a name="ad1ffb6d1bec1482dbccf57977263949e"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0021400633_p383746415530"><a name="en-us_topic_0021400633_p383746415530"></a><a name="en-us_topic_0021400633_p383746415530"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.34653465346535%" headers="mcps1.2.4.1.3 "><p id="ab5da0c2e034149cd87f2879a3f041b7e"><a name="ab5da0c2e034149cd87f2879a3f041b7e"></a><a name="ab5da0c2e034149cd87f2879a3f041b7e"></a>Specifies the time when AS configurations are created. The time format complies with UTC.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **instance\_config**  field description

    <a name="table420823093759"></a>
    <table><thead align="left"><tr id="r4c26d84153be4464b22847e9b6182390"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p1871345814416"><a name="p1871345814416"></a><a name="p1871345814416"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="a4950d94907064b47a4bda4858a33cdc0"><a name="a4950d94907064b47a4bda4858a33cdc0"></a><a name="a4950d94907064b47a4bda4858a33cdc0"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.4.1.3"><p id="p43861545411"><a name="p43861545411"></a><a name="p43861545411"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r91b06878f5da4447abf9b85bf4c82bc6"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="a509afeee56a44a43897bac222c61f3ff"><a name="a509afeee56a44a43897bac222c61f3ff"></a><a name="a509afeee56a44a43897bac222c61f3ff"></a>flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="af5eccdf2dbd04ef8ae9a07f3f57472e0"><a name="af5eccdf2dbd04ef8ae9a07f3f57472e0"></a><a name="af5eccdf2dbd04ef8ae9a07f3f57472e0"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="a068eef21ab6b4492876594074b9a6ea8"><a name="a068eef21ab6b4492876594074b9a6ea8"></a><a name="a068eef21ab6b4492876594074b9a6ea8"></a>Specifies the ECS flavor ID.</p>
    </td>
    </tr>
    <tr id="rc85492fa8fb7484b8f9ce867ee9c9db6"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="a0ef3b55b17824d92a0b4fff8a3b9fc6f"><a name="a0ef3b55b17824d92a0b4fff8a3b9fc6f"></a><a name="a0ef3b55b17824d92a0b4fff8a3b9fc6f"></a>imageRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="a0b7ade9132b143a18449fed7c25c1794"><a name="a0b7ade9132b143a18449fed7c25c1794"></a><a name="a0b7ade9132b143a18449fed7c25c1794"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="a1aafc582cb754139946238475192748d"><a name="a1aafc582cb754139946238475192748d"></a><a name="a1aafc582cb754139946238475192748d"></a>Specifies the image ID. It is same as <strong id="b49305385195432"><a name="b49305385195432"></a><a name="b49305385195432"></a>image_id</strong>.</p>
    </td>
    </tr>
    <tr id="r7d3d6a0636424a11aef13684aeacd387"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="a2fd0f5cb13fa4b2e9cce0a57e5755405"><a name="a2fd0f5cb13fa4b2e9cce0a57e5755405"></a><a name="a2fd0f5cb13fa4b2e9cce0a57e5755405"></a>disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="a59f1976b777c49dabc9f22e498393078"><a name="a59f1976b777c49dabc9f22e498393078"></a><a name="a59f1976b777c49dabc9f22e498393078"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="aeafe48e042c04c619ee16094cf39bdca"><a name="aeafe48e042c04c619ee16094cf39bdca"></a><a name="aeafe48e042c04c619ee16094cf39bdca"></a>Specifies the disk group information.</p>
    </td>
    </tr>
    <tr id="r6e4032bddf7042c591aaf8e609c9354c"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="a50a891366c5d4110b123106b59f3c018"><a name="a50a891366c5d4110b123106b59f3c018"></a><a name="a50a891366c5d4110b123106b59f3c018"></a>key_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="a319a3f9f58b14a71a0d011f5c7d05786"><a name="a319a3f9f58b14a71a0d011f5c7d05786"></a><a name="a319a3f9f58b14a71a0d011f5c7d05786"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="a20acb6297a7047d9b012e3a896ff7552"><a name="a20acb6297a7047d9b012e3a896ff7552"></a><a name="a20acb6297a7047d9b012e3a896ff7552"></a>Specifies the name of the SSH key pair used to log in to the ECS.</p>
    </td>
    </tr>
    <tr id="row77791051114"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p979151011119"><a name="p979151011119"></a><a name="p979151011119"></a>key_fingerprint</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p5790105112"><a name="p5790105112"></a><a name="p5790105112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p47931011118"><a name="p47931011118"></a><a name="p47931011118"></a>Specifies the fingerprint of the SSH key pair used to log in to the ECS.</p>
    </td>
    </tr>
    <tr id="row51826829134657"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p37223645134657"><a name="p37223645134657"></a><a name="p37223645134657"></a>instance_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p62325286134657"><a name="p62325286134657"></a><a name="p62325286134657"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p15183375134657"><a name="p15183375134657"></a><a name="p15183375134657"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="row4559936913472"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p256138513472"><a name="p256138513472"></a><a name="p256138513472"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p614564213472"><a name="p614564213472"></a><a name="p614564213472"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p2803499513472"><a name="p2803499513472"></a><a name="p2803499513472"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="row2971225584928"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p3186239984935"><a name="p3186239984935"></a><a name="p3186239984935"></a>adminPass</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p3071753084935"><a name="p3071753084935"></a><a name="p3071753084935"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p509197784935"><a name="p509197784935"></a><a name="p509197784935"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="r20296d7eb44f447f8a64bbc0a96e87d2"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="a44d4ff71822642e8a3299c7beebc4da7"><a name="a44d4ff71822642e8a3299c7beebc4da7"></a><a name="a44d4ff71822642e8a3299c7beebc4da7"></a>personality</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="af0a4b1b96a534569986e2f66b4c3a81f"><a name="af0a4b1b96a534569986e2f66b4c3a81f"></a><a name="af0a4b1b96a534569986e2f66b4c3a81f"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="a76bd6d9b0fcf4bc795d8cd02cd71669b"><a name="a76bd6d9b0fcf4bc795d8cd02cd71669b"></a><a name="a76bd6d9b0fcf4bc795d8cd02cd71669b"></a>Specifies information about the injected file.</p>
    </td>
    </tr>
    <tr id="row44468644105118"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p45190439105118"><a name="p45190439105118"></a><a name="p45190439105118"></a>public_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p7974334164019"><a name="p7974334164019"></a><a name="p7974334164019"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p28440782105253"><a name="p28440782105253"></a><a name="p28440782105253"></a>Specifies the EIP of the ECS.</p>
    </td>
    </tr>
    <tr id="row2317114819113"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p6492371719113"><a name="p6492371719113"></a><a name="p6492371719113"></a>user_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p2432969419113"><a name="p2432969419113"></a><a name="p2432969419113"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p2454815919113"><a name="p2454815919113"></a><a name="p2454815919113"></a>Specifies the Cloud-Init user data, which is encoded using Base64.</p>
    </td>
    </tr>
    <tr id="row6280717710057"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p5421657810057"><a name="p5421657810057"></a><a name="p5421657810057"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p82114373404"><a name="p82114373404"></a><a name="p82114373404"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p3799511910057"><a name="p3799511910057"></a><a name="p3799511910057"></a>Specifies the ECS metadata.</p>
    </td>
    </tr>
    <tr id="row573525920305"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p142651412133115"><a name="p142651412133115"></a><a name="p142651412133115"></a>security_groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p10265121214315"><a name="p10265121214315"></a><a name="p10265121214315"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p426516120315"><a name="p426516120315"></a><a name="p426516120315"></a>Specifies the security group information.</p>
    </td>
    </tr>
    <tr id="row126532511417"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p4890202120414"><a name="p4890202120414"></a><a name="p4890202120414"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p689412111418"><a name="p689412111418"></a><a name="p689412111418"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p139176258419"><a name="p139176258419"></a><a name="p139176258419"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="row256615121749"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p15902821041"><a name="p15902821041"></a><a name="p15902821041"></a>tenancy</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p7908142115419"><a name="p7908142115419"></a><a name="p7908142115419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p5924225648"><a name="p5924225648"></a><a name="p5924225648"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="row175331784410"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p11916162112417"><a name="p11916162112417"></a><a name="p11916162112417"></a>dedicated_host_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p1592118211644"><a name="p1592118211644"></a><a name="p1592118211644"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p189323251348"><a name="p189323251348"></a><a name="p189323251348"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="row1204184305014"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1777713012214"><a name="p1777713012214"></a><a name="p1777713012214"></a>market_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p1297185818506"><a name="p1297185818506"></a><a name="p1297185818506"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p0897134016220"><a name="p0897134016220"></a><a name="p0897134016220"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="row5954330123112"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p5541123713114"><a name="p5541123713114"></a><a name="p5541123713114"></a>multi_flavor_priority_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p454113711316"><a name="p454113711316"></a><a name="p454113711316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p13506749103211"><a name="p13506749103211"></a><a name="p13506749103211"></a>This parameter is reserved.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **disk**  field description

    <a name="table2679008093849"></a>
    <table><thead align="left"><tr id="row85230949436"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="p9529321424"><a name="p9529321424"></a><a name="p9529321424"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.4.1.2"><p id="p183385979436"><a name="p183385979436"></a><a name="p183385979436"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.35643564356435%" id="mcps1.2.4.1.3"><p id="p90314069436"><a name="p90314069436"></a><a name="p90314069436"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row604552559436"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p650374489436"><a name="p650374489436"></a><a name="p650374489436"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="p335419309436"><a name="p335419309436"></a><a name="p335419309436"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="p325417969436"><a name="p325417969436"></a><a name="p325417969436"></a>Specifies the disk size. The unit is GB.</p>
    </td>
    </tr>
    <tr id="row244407149436"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p335408289436"><a name="p335408289436"></a><a name="p335408289436"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="p324525719436"><a name="p324525719436"></a><a name="p324525719436"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="p114125909436"><a name="p114125909436"></a><a name="p114125909436"></a>Specifies the disk type.</p>
    </td>
    </tr>
    <tr id="row356044519436"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p653882729436"><a name="p653882729436"></a><a name="p653882729436"></a>disk_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="p619586619436"><a name="p619586619436"></a><a name="p619586619436"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="p525956599436"><a name="p525956599436"></a><a name="p525956599436"></a>Specifies whether the disk is a system disk or a data disk. <strong id="b7990615609568"><a name="b7990615609568"></a><a name="b7990615609568"></a>DATA</strong> indicates a data disk. <strong id="b85809941095610"><a name="b85809941095610"></a><a name="b85809941095610"></a>SYS</strong> indicates a system disk.</p>
    </td>
    </tr>
    <tr id="row4877147810558"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p503431291064"><a name="p503431291064"></a><a name="p503431291064"></a>dedicated_storage_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="p5228260410629"><a name="p5228260410629"></a><a name="p5228260410629"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="p703253010629"><a name="p703253010629"></a><a name="p703253010629"></a>Specifies the ID of the DSS device for the disk.</p>
    </td>
    </tr>
    <tr id="row619300651062"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p587013661064"><a name="p587013661064"></a><a name="p587013661064"></a>data_disk_image_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="p6132989810629"><a name="p6132989810629"></a><a name="p6132989810629"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="p166583810629"><a name="p166583810629"></a><a name="p166583810629"></a>Specifies the ID of the data disk image for creating a data disk.</p>
    </td>
    </tr>
    <tr id="row56552928152851"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p35860216152911"><a name="p35860216152911"></a><a name="p35860216152911"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="p18996409152911"><a name="p18996409152911"></a><a name="p18996409152911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="p14285369152911"><a name="p14285369152911"></a><a name="p14285369152911"></a>Specifies the disk backup snapshot ID.</p>
    </td>
    </tr>
    <tr id="row1828110519421"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p12748155016294"><a name="p12748155016294"></a><a name="p12748155016294"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="p197488507290"><a name="p197488507290"></a><a name="p197488507290"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="p6748135052911"><a name="p6748135052911"></a><a name="p6748135052911"></a>Specifies the metadata for creating disks. For details, see <a href="#table17912164981110">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **metadata**  Field Description for Creating Disks

    <a name="table17912164981110"></a>
    <table><thead align="left"><tr id="row79145499112"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="p3914164912115"><a name="p3914164912115"></a><a name="p3914164912115"></a><strong id="b1826320269412"><a name="b1826320269412"></a><a name="b1826320269412"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.4.1.2"><p id="p1991410491115"><a name="p1991410491115"></a><a name="p1991410491115"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.35643564356435%" id="mcps1.2.4.1.3"><p id="p169141849141117"><a name="p169141849141117"></a><a name="p169141849141117"></a><strong id="b1260927644"><a name="b1260927644"></a><a name="b1260927644"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1891504941119"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p091684941119"><a name="p091684941119"></a><a name="p091684941119"></a>__system__encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="p0916549131120"><a name="p0916549131120"></a><a name="p0916549131120"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="p791624941117"><a name="p791624941117"></a><a name="p791624941117"></a>Specifies encryption in <strong id="b1438855173918"><a name="b1438855173918"></a><a name="b1438855173918"></a>metadata</strong>. The value can be <strong id="b193891513393"><a name="b193891513393"></a><a name="b193891513393"></a>0</strong> (encryption disabled) or <strong id="b173901451103914"><a name="b173901451103914"></a><a name="b173901451103914"></a>1</strong> (encryption enabled).</p>
    <p id="p20916184951114"><a name="p20916184951114"></a><a name="p20916184951114"></a>If this parameter does not exist, the disk will not be encrypted by default.</p>
    </td>
    </tr>
    <tr id="row1991654913112"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p17916949171112"><a name="p17916949171112"></a><a name="p17916949171112"></a>__system__cmkid</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="p2916164911112"><a name="p2916164911112"></a><a name="p2916164911112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="p20916194915112"><a name="p20916194915112"></a><a name="p20916194915112"></a>Specifies the CMK ID, which indicates encryption in <strong id="b133078414409"><a name="b133078414409"></a><a name="b133078414409"></a>metadata</strong>. This parameter is used with <strong id="b5308184144018"><a name="b5308184144018"></a><a name="b5308184144018"></a>__system__encrypted</strong>.</p>
    <div class="note" id="note179161149181116"><a name="note179161149181116"></a><a name="note179161149181116"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p791616494116"><a name="p791616494116"></a><a name="p791616494116"></a>For details about how to obtain the CMK ID, see "Querying the List of CMKs" in <em id="i051673617488"><a name="i051673617488"></a><a name="i051673617488"></a>Key Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **personality**  field description

    <a name="table1186638793926"></a>
    <table><thead align="left"><tr id="row2268379894321"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p2544835194321"><a name="p2544835194321"></a><a name="p2544835194321"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="p4805058594321"><a name="p4805058594321"></a><a name="p4805058594321"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.4.1.3"><p id="p6689220494321"><a name="p6689220494321"></a><a name="p6689220494321"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4955942394321"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p5489029894321"><a name="p5489029894321"></a><a name="p5489029894321"></a>path</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p1692915894321"><a name="p1692915894321"></a><a name="p1692915894321"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p2908455494321"><a name="p2908455494321"></a><a name="p2908455494321"></a>Specifies the path of the injected file.</p>
    </td>
    </tr>
    <tr id="row3326409394321"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1003698794321"><a name="p1003698794321"></a><a name="p1003698794321"></a>content</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p768958594321"><a name="p768958594321"></a><a name="p768958594321"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p1887664894321"><a name="p1887664894321"></a><a name="p1887664894321"></a>Specifies the content of the file to be injected. The file content is encoded using Base64.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8** **public\_ip**  field description

    <a name="tcdec56e5b04447d7b37ba3897d12796c"></a>
    <table><thead align="left"><tr id="rf04af88fbbdf4ecba6a3e6e9aad079f9"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.4.1.1"><p id="afd8569082e55402cba696b519061600b"><a name="afd8569082e55402cba696b519061600b"></a><a name="afd8569082e55402cba696b519061600b"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.4.1.2"><p id="a38d2527b49394965871d7bd5036301d3"><a name="a38d2527b49394965871d7bd5036301d3"></a><a name="a38d2527b49394965871d7bd5036301d3"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65.65656565656566%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020845949_p851285010312"><a name="en-us_topic_0020845949_p851285010312"></a><a name="en-us_topic_0020845949_p851285010312"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r17b93926a7a2473d8e6ca47bb5be9b79"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="a89bdcceda9414a71ae0c7e3d72dabb83"><a name="a89bdcceda9414a71ae0c7e3d72dabb83"></a><a name="a89bdcceda9414a71ae0c7e3d72dabb83"></a>eip</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="p5916204120407"><a name="p5916204120407"></a><a name="p5916204120407"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.65656565656566%" headers="mcps1.2.4.1.3 "><p id="a47ccd07d509f4dd3824f47e9247aea59"><a name="a47ccd07d509f4dd3824f47e9247aea59"></a><a name="a47ccd07d509f4dd3824f47e9247aea59"></a>Specifies the automatically assigned EIP.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9** **eip**  field description

    <a name="tdd0bc92fd16345d48c819c97641a369f"></a>
    <table><thead align="left"><tr id="r87ed6857ffae47088b1500be4cc20349"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="ad86da605a6b94513b3155b6e54b5083f"><a name="ad86da605a6b94513b3155b6e54b5083f"></a><a name="ad86da605a6b94513b3155b6e54b5083f"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="a6a6ab8033ed94d40afe36b99d987b71c"><a name="a6a6ab8033ed94d40afe36b99d987b71c"></a><a name="a6a6ab8033ed94d40afe36b99d987b71c"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.4.1.3"><p id="a9baeb04a7c2f4c9c852c1e5874dbbffd"><a name="a9baeb04a7c2f4c9c852c1e5874dbbffd"></a><a name="a9baeb04a7c2f4c9c852c1e5874dbbffd"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rd79e7d1ab1d647efa45dc111cbe4c367"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="ae77f47be6732497c98ea0a0e1b66e2c2"><a name="ae77f47be6732497c98ea0a0e1b66e2c2"></a><a name="ae77f47be6732497c98ea0a0e1b66e2c2"></a>ip_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="ac063c9e758fe40d3b7ccbf9d5b4e0dba"><a name="ac063c9e758fe40d3b7ccbf9d5b4e0dba"></a><a name="ac063c9e758fe40d3b7ccbf9d5b4e0dba"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="a9098437854d542a899c5e69e2c3c3d2e"><a name="a9098437854d542a899c5e69e2c3c3d2e"></a><a name="a9098437854d542a899c5e69e2c3c3d2e"></a>Specifies the IP address type.</p>
    </td>
    </tr>
    <tr id="r4ec4d379ab0a44ccb3f2bd1e38b8f2ba"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="a523db77199174a00aa2acaa39b3880e7"><a name="a523db77199174a00aa2acaa39b3880e7"></a><a name="a523db77199174a00aa2acaa39b3880e7"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p189015439402"><a name="p189015439402"></a><a name="p189015439402"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="a0f936b6301a74ddb82af834687c9be56"><a name="a0f936b6301a74ddb82af834687c9be56"></a><a name="a0f936b6301a74ddb82af834687c9be56"></a>Specifies the bandwidth of an IP address.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  10** **bandwidth**  field description

    <a name="t5334015bf90941a996bc1c9ca7ef4637"></a>
    <table><thead align="left"><tr id="r423eaa8930174f0ba29e71993bff93da"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="a4232ce3904fd45eaa61c236eff6ebf85"><a name="a4232ce3904fd45eaa61c236eff6ebf85"></a><a name="a4232ce3904fd45eaa61c236eff6ebf85"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.4.1.2"><p id="a71c241ffcd524934b5b87de8f59b40e1"><a name="a71c241ffcd524934b5b87de8f59b40e1"></a><a name="a71c241ffcd524934b5b87de8f59b40e1"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.35643564356435%" id="mcps1.2.4.1.3"><p id="a7c976ed70ac74bf0a8eac92204ccedcf"><a name="a7c976ed70ac74bf0a8eac92204ccedcf"></a><a name="a7c976ed70ac74bf0a8eac92204ccedcf"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r4b82bcc1304f4adc86aed5c0fb8a4257"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="ae94d06d07bdd40128a583075ebfb2b8c"><a name="ae94d06d07bdd40128a583075ebfb2b8c"></a><a name="ae94d06d07bdd40128a583075ebfb2b8c"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="ae718de7e54424fb7b76d8ec75da93d28"><a name="ae718de7e54424fb7b76d8ec75da93d28"></a><a name="ae718de7e54424fb7b76d8ec75da93d28"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="p22263891102758"><a name="p22263891102758"></a><a name="p22263891102758"></a>Specifies the bandwidth (Mbit/s).</p>
    </td>
    </tr>
    <tr id="r835b10f4ea2440a59008ed01cf5406e5"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020845949_p840519103344"><a name="en-us_topic_0020845949_p840519103344"></a><a name="en-us_topic_0020845949_p840519103344"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="a2318067ce92d452f860add6c1534c47a"><a name="a2318067ce92d452f860add6c1534c47a"></a><a name="a2318067ce92d452f860add6c1534c47a"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="ac10c2cfc7cd146fdb8123d9cf26f04c1"><a name="ac10c2cfc7cd146fdb8123d9cf26f04c1"></a><a name="ac10c2cfc7cd146fdb8123d9cf26f04c1"></a>Specifies the bandwidth sharing type.</p>
    <p id="p1623102512610"><a name="p1623102512610"></a><a name="p1623102512610"></a>Enumerated values of the sharing type:</p>
    <a name="ul8989111213019"></a><a name="ul8989111213019"></a><ul id="ul8989111213019"><li><strong id="b84235270604852"><a name="b84235270604852"></a><a name="b84235270604852"></a>PER</strong>: dedicated</li></ul>
    </td>
    </tr>
    <tr id="rd34a9ea5552b45ec8738f5fa3b72a148"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="a37f22f3f0df7441a8edd20467578ef30"><a name="a37f22f3f0df7441a8edd20467578ef30"></a><a name="a37f22f3f0df7441a8edd20467578ef30"></a>charging_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="ad87bdc85b8464970a124eab512415764"><a name="ad87bdc85b8464970a124eab512415764"></a><a name="ad87bdc85b8464970a124eab512415764"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="a7b09462d7de24bfdb18f5fc46eb08da2"><a name="a7b09462d7de24bfdb18f5fc46eb08da2"></a><a name="a7b09462d7de24bfdb18f5fc46eb08da2"></a>Specifies the bandwidth billing mode.</p>
    <a name="u7a851e86e06a442c942f1c43a416b218"></a><a name="u7a851e86e06a442c942f1c43a416b218"></a><ul id="u7a851e86e06a442c942f1c43a416b218"><li><strong id="b842352706184041"><a name="b842352706184041"></a><a name="b842352706184041"></a>traffic</strong>: billed by traffic.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  11** **metadata**  field description

    <a name="table6119722495435"></a>
    <table><thead align="left"><tr id="row5794517795435"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p6304778595435"><a name="p6304778595435"></a><a name="p6304778595435"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="p6459317995435"><a name="p6459317995435"></a><a name="p6459317995435"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p6466497295435"><a name="p6466497295435"></a><a name="p6466497295435"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row337137495435"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p460751359557"><a name="p460751359557"></a><a name="p460751359557"></a>User-defined key-value pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p406410849557"><a name="p406410849557"></a><a name="p406410849557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p35935409557"><a name="p35935409557"></a><a name="p35935409557"></a>Specifies the key and value pair of the metadata.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  12** **security\_groups**  field description

    <a name="table121274211250"></a>
    <table><thead align="left"><tr id="row21632216254"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p516332116258"><a name="p516332116258"></a><a name="p516332116258"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="p1316313216252"><a name="p1316313216252"></a><a name="p1316313216252"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p0163521152518"><a name="p0163521152518"></a><a name="p0163521152518"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51635216253"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p121631221182519"><a name="p121631221182519"></a><a name="p121631221182519"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p5163182142517"><a name="p5163182142517"></a><a name="p5163182142517"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p16163132182511"><a name="p16163132182511"></a><a name="p16163132182511"></a>Specifies the security group ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "limit": 20,
        "total_number": 2,
        "start_number": 0,
        "scaling_configurations": [
            {
                "tenant": "ce061903a53545dcaddb300093b477d2",
                "scaling_configuration_id": "6afe46f9-7d3d-4046-8748-3b2a1085ad86",
                "scaling_configuration_name": " config_name_1",
                "instance_config": {
                    "disk": [
                        {
                            "size": 40,
                            "volume_type": "SATA",
                            "disk_type": "SYS"
                        },
                        {
                            "size": 100,
                            "volume_type": "SATA",
                            "disk_type": "DATA"
                        }
                    ],
                    "personality": null,
                    "instance_name": null,
                    "instance_id": null,
                    "flavorRef": "103",
                    "imageRef": "37ca2b35-6fc7-47ab-93c7-900324809c5c",
                    "key_name": "keypair01",
                    "public_ip": null,
                    "user_data": null,
                    "metadate": {},
                    "security_groups": [{
                         "id": "6c22a6c0-b5d2-4a84-ac56-51090dcc33be"
                    }],
                },
                "create_time": "2015-07-23T01:04:07Z"
            },
            {
                "tenant": "ce061903a53545dcaddb300093b477d2",
                "scaling_configuration_id": "24a8c5f3-c713-4aba-ac29-c17101009e5d",
                "scaling_configuration_name": "config_name_2",
                "instance_config": {
                    "disk": [
                        {
                            "size": 40,
                            "volume_type": "SATA",
                            "disk_type": "SYS"
                        }
                    ],
                    "personality": null,
                    "instance_name": null,
                    "instance_id": null,
                    "flavorRef": "103",
                    "imageRef": "37ca2b35-6fc7-47ab-93c7-900324809c5c",
                    "key_name": "keypair01",
                    "public_ip": null,
                    "user_data": null,
                    "metadata": {},
                    "security_groups": [{
                         "id": "6c22a6c0-b5d2-4a84-ac56-51090dcc33be"
                    }],
                    "multi_flavor_priority_policy": "PICK_FIRST"
                },
                "create_time": "2015-07-22T01:08:41Z"
            }
        ]
    }
    ```


## Returned Values<a name="section10750772"></a>

-   Normal

    200

-   Abnormal

    <a name="table3623379"></a>
    <table><thead align="left"><tr id="row13858403"><th class="cellrowborder" valign="top" width="43.8%" id="mcps1.1.3.1.1"><p id="p48788849"><a name="p48788849"></a><a name="p48788849"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.2%" id="mcps1.1.3.1.2"><p id="p59582700"><a name="p59582700"></a><a name="p59582700"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61469371"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p12963143"><a name="p12963143"></a><a name="p12963143"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p43381623"><a name="p43381623"></a><a name="p43381623"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row54890288"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p16928338"><a name="p16928338"></a><a name="p16928338"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p29018124"><a name="p29018124"></a><a name="p29018124"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row59836530"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p14920772"><a name="p14920772"></a><a name="p14920772"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p623043"><a name="p623043"></a><a name="p623043"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row5607390"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p51545483"><a name="p51545483"></a><a name="p51545483"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p14434584"><a name="p14434584"></a><a name="p14434584"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row62802394"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p53829147"><a name="p53829147"></a><a name="p53829147"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p65193616"><a name="p65193616"></a><a name="p65193616"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row49871633"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p13070512"><a name="p13070512"></a><a name="p13070512"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p52078584"><a name="p52078584"></a><a name="p52078584"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row66054074"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p48779793"><a name="p48779793"></a><a name="p48779793"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p58849189"><a name="p58849189"></a><a name="p58849189"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row59880657"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p18495050"><a name="p18495050"></a><a name="p18495050"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p21704116"><a name="p21704116"></a><a name="p21704116"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row61119323"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p51718129"><a name="p51718129"></a><a name="p51718129"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p28418891"><a name="p28418891"></a><a name="p28418891"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row54443429"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p47841633"><a name="p47841633"></a><a name="p47841633"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p49967061"><a name="p49967061"></a><a name="p49967061"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row47050372"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p52983808"><a name="p52983808"></a><a name="p52983808"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p63830089"><a name="p63830089"></a><a name="p63830089"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row37599894"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p25692540"><a name="p25692540"></a><a name="p25692540"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p720995"><a name="p720995"></a><a name="p720995"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row6488958"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p55843593"><a name="p55843593"></a><a name="p55843593"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p27037160"><a name="p27037160"></a><a name="p27037160"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row42007851"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p47192740"><a name="p47192740"></a><a name="p47192740"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p64515557"><a name="p64515557"></a><a name="p64515557"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

