# Querying AS Configuration Details<a name="EN-US_TOPIC_0043063052"></a>

## Function<a name="section59796890"></a>

This interface is used to query details about an AS configuration by configuration ID.

## URI<a name="section1301106"></a>

GET /autoscaling-api/v1/\{project\_id\}/scaling\_configuration/\{scaling\_configuration\_id\}

**Table  1**  Parameter description

<a name="table43304686"></a>
<table><thead align="left"><tr id="row38709481"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p48460267"><a name="p48460267"></a><a name="p48460267"></a><strong id="b626144934919"><a name="b626144934919"></a><a name="b626144934919"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p32967578"><a name="p32967578"></a><a name="p32967578"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p53128157"><a name="p53128157"></a><a name="p53128157"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42%" id="mcps1.2.5.1.4"><p id="p8413469"><a name="p8413469"></a><a name="p8413469"></a><strong id="b20498651134917"><a name="b20498651134917"></a><a name="b20498651134917"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10402369"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p37285554"><a name="p37285554"></a><a name="p37285554"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p230999"><a name="p230999"></a><a name="p230999"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p18710936"><a name="p18710936"></a><a name="p18710936"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row17173591"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p48883615"><a name="p48883615"></a><a name="p48883615"></a>scaling_configuration_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p149855"><a name="p149855"></a><a name="p149855"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p12138304"><a name="p12138304"></a><a name="p12138304"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p43678569"><a name="p43678569"></a><a name="p43678569"></a>Specifies an AS configuration ID, which is unique globally. For details, see <a href="querying-as-configuration-details.md">Querying AS Configuration Details</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section11709955"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query details about the AS configuration with ID  **6afe46f9-7d3d-4046-8748-3b2a1085ad86**.

    ```
    GET https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_configuration/6afe46f9-7d3d-4046-8748-3b2a1085ad86
    ```


## Response Message<a name="section38280736"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table46071449"></a>
    <table><thead align="left"><tr id="row58067579"><th class="cellrowborder" valign="top" width="28.637136286371362%" id="mcps1.2.4.1.1"><p id="p5853458"><a name="p5853458"></a><a name="p5853458"></a><strong id="b1260655264910"><a name="b1260655264910"></a><a name="b1260655264910"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.636836316368367%" id="mcps1.2.4.1.2"><p id="p4368081"><a name="p4368081"></a><a name="p4368081"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.726027397260275%" id="mcps1.2.4.1.3"><p id="p18270305"><a name="p18270305"></a><a name="p18270305"></a><strong id="b121353164915"><a name="b121353164915"></a><a name="b121353164915"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3499754"><td class="cellrowborder" valign="top" width="28.637136286371362%" headers="mcps1.2.4.1.1 "><p id="p15044627"><a name="p15044627"></a><a name="p15044627"></a>scaling_configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.636836316368367%" headers="mcps1.2.4.1.2 "><p id="a4c03d226ca78442f99e13b8d363cd51d"><a name="a4c03d226ca78442f99e13b8d363cd51d"></a><a name="a4c03d226ca78442f99e13b8d363cd51d"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.726027397260275%" headers="mcps1.2.4.1.3 "><p id="p57767782"><a name="p57767782"></a><a name="p57767782"></a>Provides AS configuration details.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scaling\_configurations**  field description

    <a name="table804974795643"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063056_re3411f14be354adaa992fb18acd266b3"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="en-us_topic_0043063056_p1849874874120"><a name="en-us_topic_0043063056_p1849874874120"></a><a name="en-us_topic_0043063056_p1849874874120"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.4.1.2"><p id="en-us_topic_0043063056_a66bf54ec342041dbbdb3e94e61a16755"><a name="en-us_topic_0043063056_a66bf54ec342041dbbdb3e94e61a16755"></a><a name="en-us_topic_0043063056_a66bf54ec342041dbbdb3e94e61a16755"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65.34653465346535%" id="mcps1.2.4.1.3"><p id="en-us_topic_0043063056_p5247352114118"><a name="en-us_topic_0043063056_p5247352114118"></a><a name="en-us_topic_0043063056_p5247352114118"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063056_r9f15de2a91214389817570a65795d934"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_a7126d41fd1b24b1eab2eda1d5a38f8e2"><a name="en-us_topic_0043063056_a7126d41fd1b24b1eab2eda1d5a38f8e2"></a><a name="en-us_topic_0043063056_a7126d41fd1b24b1eab2eda1d5a38f8e2"></a>scaling_configuration_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_en-us_topic_0021400633_p540708615530"><a name="en-us_topic_0043063056_en-us_topic_0021400633_p540708615530"></a><a name="en-us_topic_0043063056_en-us_topic_0021400633_p540708615530"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.34653465346535%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_a11b18fd45aa842a488d336849f50eeee"><a name="en-us_topic_0043063056_a11b18fd45aa842a488d336849f50eeee"></a><a name="en-us_topic_0043063056_a11b18fd45aa842a488d336849f50eeee"></a>Specifies the AS configuration ID. This parameter is globally unique.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_r4a558da7a6aa4ab29aaf4550f7b1f0e0"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_a046a22f1fc274961a10019bfb674fff4"><a name="en-us_topic_0043063056_a046a22f1fc274961a10019bfb674fff4"></a><a name="en-us_topic_0043063056_a046a22f1fc274961a10019bfb674fff4"></a>tenant</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_a25cae146c2cd4a769583d20b5424e047"><a name="en-us_topic_0043063056_a25cae146c2cd4a769583d20b5424e047"></a><a name="en-us_topic_0043063056_a25cae146c2cd4a769583d20b5424e047"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.34653465346535%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_a2d4137196ed147e4a4f4e8653db5ec24"><a name="en-us_topic_0043063056_a2d4137196ed147e4a4f4e8653db5ec24"></a><a name="en-us_topic_0043063056_a2d4137196ed147e4a4f4e8653db5ec24"></a>Specifies the tenant ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_r505b7d00ed454198a1a21dced5c0243f"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_en-us_topic_0021400633_p870139315530"><a name="en-us_topic_0043063056_en-us_topic_0021400633_p870139315530"></a><a name="en-us_topic_0043063056_en-us_topic_0021400633_p870139315530"></a>scaling_configuration_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_afb8c974ea725478993cd9a4990ca109f"><a name="en-us_topic_0043063056_afb8c974ea725478993cd9a4990ca109f"></a><a name="en-us_topic_0043063056_afb8c974ea725478993cd9a4990ca109f"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.34653465346535%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_a89afcf2708b144269ae6b3940fa2666a"><a name="en-us_topic_0043063056_a89afcf2708b144269ae6b3940fa2666a"></a><a name="en-us_topic_0043063056_a89afcf2708b144269ae6b3940fa2666a"></a>Specifies the AS configuration name.</p>
    <p id="en-us_topic_0043063056_p194013251584"><a name="en-us_topic_0043063056_p194013251584"></a><a name="en-us_topic_0043063056_p194013251584"></a>Supports fuzzy search. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_r77a46c0e9c70450eb409e8ebe23beea8"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_ae15692552b404d298e68d5ef197ea04c"><a name="en-us_topic_0043063056_ae15692552b404d298e68d5ef197ea04c"></a><a name="en-us_topic_0043063056_ae15692552b404d298e68d5ef197ea04c"></a>instance_config</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_a4c03d226ca78442f99e13b8d363cd51d"><a name="en-us_topic_0043063056_a4c03d226ca78442f99e13b8d363cd51d"></a><a name="en-us_topic_0043063056_a4c03d226ca78442f99e13b8d363cd51d"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.34653465346535%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_abaccb7574422492eb4b4c527d09a3c61"><a name="en-us_topic_0043063056_abaccb7574422492eb4b4c527d09a3c61"></a><a name="en-us_topic_0043063056_abaccb7574422492eb4b4c527d09a3c61"></a>Specifies the information about instance configurations.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_r3d8f7bcb6bf94470b87dacfd57738024"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_ad1ffb6d1bec1482dbccf57977263949e"><a name="en-us_topic_0043063056_ad1ffb6d1bec1482dbccf57977263949e"></a><a name="en-us_topic_0043063056_ad1ffb6d1bec1482dbccf57977263949e"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_en-us_topic_0021400633_p383746415530"><a name="en-us_topic_0043063056_en-us_topic_0021400633_p383746415530"></a><a name="en-us_topic_0043063056_en-us_topic_0021400633_p383746415530"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.34653465346535%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_ab5da0c2e034149cd87f2879a3f041b7e"><a name="en-us_topic_0043063056_ab5da0c2e034149cd87f2879a3f041b7e"></a><a name="en-us_topic_0043063056_ab5da0c2e034149cd87f2879a3f041b7e"></a>Specifies the time when AS configurations are created. The time format complies with UTC.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **instance\_config**  field description

    <a name="t08d46afec43b4300b4ba48b3e75718de"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063056_r4c26d84153be4464b22847e9b6182390"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="en-us_topic_0043063056_p1871345814416"><a name="en-us_topic_0043063056_p1871345814416"></a><a name="en-us_topic_0043063056_p1871345814416"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0043063056_a4950d94907064b47a4bda4858a33cdc0"><a name="en-us_topic_0043063056_a4950d94907064b47a4bda4858a33cdc0"></a><a name="en-us_topic_0043063056_a4950d94907064b47a4bda4858a33cdc0"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.4.1.3"><p id="en-us_topic_0043063056_p43861545411"><a name="en-us_topic_0043063056_p43861545411"></a><a name="en-us_topic_0043063056_p43861545411"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063056_r91b06878f5da4447abf9b85bf4c82bc6"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_a509afeee56a44a43897bac222c61f3ff"><a name="en-us_topic_0043063056_a509afeee56a44a43897bac222c61f3ff"></a><a name="en-us_topic_0043063056_a509afeee56a44a43897bac222c61f3ff"></a>flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_af5eccdf2dbd04ef8ae9a07f3f57472e0"><a name="en-us_topic_0043063056_af5eccdf2dbd04ef8ae9a07f3f57472e0"></a><a name="en-us_topic_0043063056_af5eccdf2dbd04ef8ae9a07f3f57472e0"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_a068eef21ab6b4492876594074b9a6ea8"><a name="en-us_topic_0043063056_a068eef21ab6b4492876594074b9a6ea8"></a><a name="en-us_topic_0043063056_a068eef21ab6b4492876594074b9a6ea8"></a>Specifies the ECS flavor ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_rc85492fa8fb7484b8f9ce867ee9c9db6"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_a0ef3b55b17824d92a0b4fff8a3b9fc6f"><a name="en-us_topic_0043063056_a0ef3b55b17824d92a0b4fff8a3b9fc6f"></a><a name="en-us_topic_0043063056_a0ef3b55b17824d92a0b4fff8a3b9fc6f"></a>imageRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_a0b7ade9132b143a18449fed7c25c1794"><a name="en-us_topic_0043063056_a0b7ade9132b143a18449fed7c25c1794"></a><a name="en-us_topic_0043063056_a0b7ade9132b143a18449fed7c25c1794"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_a1aafc582cb754139946238475192748d"><a name="en-us_topic_0043063056_a1aafc582cb754139946238475192748d"></a><a name="en-us_topic_0043063056_a1aafc582cb754139946238475192748d"></a>Specifies the image ID. It is same as <strong id="en-us_topic_0043063056_b49305385195432"><a name="en-us_topic_0043063056_b49305385195432"></a><a name="en-us_topic_0043063056_b49305385195432"></a>image_id</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_r7d3d6a0636424a11aef13684aeacd387"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_a2fd0f5cb13fa4b2e9cce0a57e5755405"><a name="en-us_topic_0043063056_a2fd0f5cb13fa4b2e9cce0a57e5755405"></a><a name="en-us_topic_0043063056_a2fd0f5cb13fa4b2e9cce0a57e5755405"></a>disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_a59f1976b777c49dabc9f22e498393078"><a name="en-us_topic_0043063056_a59f1976b777c49dabc9f22e498393078"></a><a name="en-us_topic_0043063056_a59f1976b777c49dabc9f22e498393078"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_aeafe48e042c04c619ee16094cf39bdca"><a name="en-us_topic_0043063056_aeafe48e042c04c619ee16094cf39bdca"></a><a name="en-us_topic_0043063056_aeafe48e042c04c619ee16094cf39bdca"></a>Specifies the disk group information.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_r6e4032bddf7042c591aaf8e609c9354c"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_a50a891366c5d4110b123106b59f3c018"><a name="en-us_topic_0043063056_a50a891366c5d4110b123106b59f3c018"></a><a name="en-us_topic_0043063056_a50a891366c5d4110b123106b59f3c018"></a>key_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_a319a3f9f58b14a71a0d011f5c7d05786"><a name="en-us_topic_0043063056_a319a3f9f58b14a71a0d011f5c7d05786"></a><a name="en-us_topic_0043063056_a319a3f9f58b14a71a0d011f5c7d05786"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_a20acb6297a7047d9b012e3a896ff7552"><a name="en-us_topic_0043063056_a20acb6297a7047d9b012e3a896ff7552"></a><a name="en-us_topic_0043063056_a20acb6297a7047d9b012e3a896ff7552"></a>Specifies the name of the SSH key pair used to log in to the ECS.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row77791051114"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p979151011119"><a name="en-us_topic_0043063056_p979151011119"></a><a name="en-us_topic_0043063056_p979151011119"></a>key_fingerprint</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p5790105112"><a name="en-us_topic_0043063056_p5790105112"></a><a name="en-us_topic_0043063056_p5790105112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p47931011118"><a name="en-us_topic_0043063056_p47931011118"></a><a name="en-us_topic_0043063056_p47931011118"></a>Specifies the fingerprint of the SSH key pair used to log in to the ECS.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row51826829134657"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p37223645134657"><a name="en-us_topic_0043063056_p37223645134657"></a><a name="en-us_topic_0043063056_p37223645134657"></a>instance_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p62325286134657"><a name="en-us_topic_0043063056_p62325286134657"></a><a name="en-us_topic_0043063056_p62325286134657"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p15183375134657"><a name="en-us_topic_0043063056_p15183375134657"></a><a name="en-us_topic_0043063056_p15183375134657"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row4559936913472"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p256138513472"><a name="en-us_topic_0043063056_p256138513472"></a><a name="en-us_topic_0043063056_p256138513472"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p614564213472"><a name="en-us_topic_0043063056_p614564213472"></a><a name="en-us_topic_0043063056_p614564213472"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p2803499513472"><a name="en-us_topic_0043063056_p2803499513472"></a><a name="en-us_topic_0043063056_p2803499513472"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row2971225584928"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p3186239984935"><a name="en-us_topic_0043063056_p3186239984935"></a><a name="en-us_topic_0043063056_p3186239984935"></a>adminPass</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p3071753084935"><a name="en-us_topic_0043063056_p3071753084935"></a><a name="en-us_topic_0043063056_p3071753084935"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p509197784935"><a name="en-us_topic_0043063056_p509197784935"></a><a name="en-us_topic_0043063056_p509197784935"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_r20296d7eb44f447f8a64bbc0a96e87d2"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_a44d4ff71822642e8a3299c7beebc4da7"><a name="en-us_topic_0043063056_a44d4ff71822642e8a3299c7beebc4da7"></a><a name="en-us_topic_0043063056_a44d4ff71822642e8a3299c7beebc4da7"></a>personality</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_af0a4b1b96a534569986e2f66b4c3a81f"><a name="en-us_topic_0043063056_af0a4b1b96a534569986e2f66b4c3a81f"></a><a name="en-us_topic_0043063056_af0a4b1b96a534569986e2f66b4c3a81f"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_a76bd6d9b0fcf4bc795d8cd02cd71669b"><a name="en-us_topic_0043063056_a76bd6d9b0fcf4bc795d8cd02cd71669b"></a><a name="en-us_topic_0043063056_a76bd6d9b0fcf4bc795d8cd02cd71669b"></a>Specifies information about the injected file.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row44468644105118"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p45190439105118"><a name="en-us_topic_0043063056_p45190439105118"></a><a name="en-us_topic_0043063056_p45190439105118"></a>public_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p7974334164019"><a name="en-us_topic_0043063056_p7974334164019"></a><a name="en-us_topic_0043063056_p7974334164019"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p28440782105253"><a name="en-us_topic_0043063056_p28440782105253"></a><a name="en-us_topic_0043063056_p28440782105253"></a>Specifies the EIP of the ECS.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row2317114819113"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p6492371719113"><a name="en-us_topic_0043063056_p6492371719113"></a><a name="en-us_topic_0043063056_p6492371719113"></a>user_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p2432969419113"><a name="en-us_topic_0043063056_p2432969419113"></a><a name="en-us_topic_0043063056_p2432969419113"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p2454815919113"><a name="en-us_topic_0043063056_p2454815919113"></a><a name="en-us_topic_0043063056_p2454815919113"></a>Specifies the Cloud-Init user data, which is encoded using Base64.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row6280717710057"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p5421657810057"><a name="en-us_topic_0043063056_p5421657810057"></a><a name="en-us_topic_0043063056_p5421657810057"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p82114373404"><a name="en-us_topic_0043063056_p82114373404"></a><a name="en-us_topic_0043063056_p82114373404"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p3799511910057"><a name="en-us_topic_0043063056_p3799511910057"></a><a name="en-us_topic_0043063056_p3799511910057"></a>Specifies the ECS metadata.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row573525920305"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p142651412133115"><a name="en-us_topic_0043063056_p142651412133115"></a><a name="en-us_topic_0043063056_p142651412133115"></a>security_groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p10265121214315"><a name="en-us_topic_0043063056_p10265121214315"></a><a name="en-us_topic_0043063056_p10265121214315"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p426516120315"><a name="en-us_topic_0043063056_p426516120315"></a><a name="en-us_topic_0043063056_p426516120315"></a>Specifies the security group information.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row126532511417"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p4890202120414"><a name="en-us_topic_0043063056_p4890202120414"></a><a name="en-us_topic_0043063056_p4890202120414"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p689412111418"><a name="en-us_topic_0043063056_p689412111418"></a><a name="en-us_topic_0043063056_p689412111418"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p139176258419"><a name="en-us_topic_0043063056_p139176258419"></a><a name="en-us_topic_0043063056_p139176258419"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row256615121749"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p15902821041"><a name="en-us_topic_0043063056_p15902821041"></a><a name="en-us_topic_0043063056_p15902821041"></a>tenancy</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p7908142115419"><a name="en-us_topic_0043063056_p7908142115419"></a><a name="en-us_topic_0043063056_p7908142115419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p5924225648"><a name="en-us_topic_0043063056_p5924225648"></a><a name="en-us_topic_0043063056_p5924225648"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row175331784410"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p11916162112417"><a name="en-us_topic_0043063056_p11916162112417"></a><a name="en-us_topic_0043063056_p11916162112417"></a>dedicated_host_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p1592118211644"><a name="en-us_topic_0043063056_p1592118211644"></a><a name="en-us_topic_0043063056_p1592118211644"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p189323251348"><a name="en-us_topic_0043063056_p189323251348"></a><a name="en-us_topic_0043063056_p189323251348"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row1204184305014"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p1777713012214"><a name="en-us_topic_0043063056_p1777713012214"></a><a name="en-us_topic_0043063056_p1777713012214"></a>market_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p1297185818506"><a name="en-us_topic_0043063056_p1297185818506"></a><a name="en-us_topic_0043063056_p1297185818506"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p0897134016220"><a name="en-us_topic_0043063056_p0897134016220"></a><a name="en-us_topic_0043063056_p0897134016220"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row5954330123112"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p5541123713114"><a name="en-us_topic_0043063056_p5541123713114"></a><a name="en-us_topic_0043063056_p5541123713114"></a>multi_flavor_priority_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p454113711316"><a name="en-us_topic_0043063056_p454113711316"></a><a name="en-us_topic_0043063056_p454113711316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p13506749103211"><a name="en-us_topic_0043063056_p13506749103211"></a><a name="en-us_topic_0043063056_p13506749103211"></a>This parameter is reserved.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **disk**  field description

    <a name="t6dbbae28041c4559b932843975249c4a"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063056_row85230949436"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="en-us_topic_0043063056_p9529321424"><a name="en-us_topic_0043063056_p9529321424"></a><a name="en-us_topic_0043063056_p9529321424"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.4.1.2"><p id="en-us_topic_0043063056_p183385979436"><a name="en-us_topic_0043063056_p183385979436"></a><a name="en-us_topic_0043063056_p183385979436"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.35643564356435%" id="mcps1.2.4.1.3"><p id="en-us_topic_0043063056_p90314069436"><a name="en-us_topic_0043063056_p90314069436"></a><a name="en-us_topic_0043063056_p90314069436"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063056_row604552559436"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p650374489436"><a name="en-us_topic_0043063056_p650374489436"></a><a name="en-us_topic_0043063056_p650374489436"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p335419309436"><a name="en-us_topic_0043063056_p335419309436"></a><a name="en-us_topic_0043063056_p335419309436"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p325417969436"><a name="en-us_topic_0043063056_p325417969436"></a><a name="en-us_topic_0043063056_p325417969436"></a>Specifies the disk size. The unit is GB.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row244407149436"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p335408289436"><a name="en-us_topic_0043063056_p335408289436"></a><a name="en-us_topic_0043063056_p335408289436"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p324525719436"><a name="en-us_topic_0043063056_p324525719436"></a><a name="en-us_topic_0043063056_p324525719436"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p114125909436"><a name="en-us_topic_0043063056_p114125909436"></a><a name="en-us_topic_0043063056_p114125909436"></a>Specifies the disk type.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row356044519436"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p653882729436"><a name="en-us_topic_0043063056_p653882729436"></a><a name="en-us_topic_0043063056_p653882729436"></a>disk_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p619586619436"><a name="en-us_topic_0043063056_p619586619436"></a><a name="en-us_topic_0043063056_p619586619436"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p525956599436"><a name="en-us_topic_0043063056_p525956599436"></a><a name="en-us_topic_0043063056_p525956599436"></a>Specifies whether the disk is a system disk or a data disk. <strong id="en-us_topic_0043063056_b7990615609568"><a name="en-us_topic_0043063056_b7990615609568"></a><a name="en-us_topic_0043063056_b7990615609568"></a>DATA</strong> indicates a data disk. <strong id="en-us_topic_0043063056_b85809941095610"><a name="en-us_topic_0043063056_b85809941095610"></a><a name="en-us_topic_0043063056_b85809941095610"></a>SYS</strong> indicates a system disk.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row4877147810558"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p503431291064"><a name="en-us_topic_0043063056_p503431291064"></a><a name="en-us_topic_0043063056_p503431291064"></a>dedicated_storage_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p5228260410629"><a name="en-us_topic_0043063056_p5228260410629"></a><a name="en-us_topic_0043063056_p5228260410629"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p703253010629"><a name="en-us_topic_0043063056_p703253010629"></a><a name="en-us_topic_0043063056_p703253010629"></a>Specifies the ID of the DSS device for the disk.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row619300651062"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p587013661064"><a name="en-us_topic_0043063056_p587013661064"></a><a name="en-us_topic_0043063056_p587013661064"></a>data_disk_image_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p6132989810629"><a name="en-us_topic_0043063056_p6132989810629"></a><a name="en-us_topic_0043063056_p6132989810629"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p166583810629"><a name="en-us_topic_0043063056_p166583810629"></a><a name="en-us_topic_0043063056_p166583810629"></a>Specifies the ID of the data disk image for creating a data disk.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row56552928152851"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p35860216152911"><a name="en-us_topic_0043063056_p35860216152911"></a><a name="en-us_topic_0043063056_p35860216152911"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p18996409152911"><a name="en-us_topic_0043063056_p18996409152911"></a><a name="en-us_topic_0043063056_p18996409152911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p14285369152911"><a name="en-us_topic_0043063056_p14285369152911"></a><a name="en-us_topic_0043063056_p14285369152911"></a>Specifies the disk backup snapshot ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row1828110519421"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p12748155016294"><a name="en-us_topic_0043063056_p12748155016294"></a><a name="en-us_topic_0043063056_p12748155016294"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p197488507290"><a name="en-us_topic_0043063056_p197488507290"></a><a name="en-us_topic_0043063056_p197488507290"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p6748135052911"><a name="en-us_topic_0043063056_p6748135052911"></a><a name="en-us_topic_0043063056_p6748135052911"></a>Specifies the metadata for creating disks. For details, see <a href="querying-as-configurations.md#table17912164981110">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **personality**  field description

    <a name="tb122d46cc6a3494ba8624460faeacc1b"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063056_row2268379894321"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="en-us_topic_0043063056_p2544835194321"><a name="en-us_topic_0043063056_p2544835194321"></a><a name="en-us_topic_0043063056_p2544835194321"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0043063056_p4805058594321"><a name="en-us_topic_0043063056_p4805058594321"></a><a name="en-us_topic_0043063056_p4805058594321"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.4.1.3"><p id="en-us_topic_0043063056_p6689220494321"><a name="en-us_topic_0043063056_p6689220494321"></a><a name="en-us_topic_0043063056_p6689220494321"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063056_row4955942394321"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p5489029894321"><a name="en-us_topic_0043063056_p5489029894321"></a><a name="en-us_topic_0043063056_p5489029894321"></a>path</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p1692915894321"><a name="en-us_topic_0043063056_p1692915894321"></a><a name="en-us_topic_0043063056_p1692915894321"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p2908455494321"><a name="en-us_topic_0043063056_p2908455494321"></a><a name="en-us_topic_0043063056_p2908455494321"></a>Specifies the path of the injected file.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_row3326409394321"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p1003698794321"><a name="en-us_topic_0043063056_p1003698794321"></a><a name="en-us_topic_0043063056_p1003698794321"></a>content</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p768958594321"><a name="en-us_topic_0043063056_p768958594321"></a><a name="en-us_topic_0043063056_p768958594321"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p1887664894321"><a name="en-us_topic_0043063056_p1887664894321"></a><a name="en-us_topic_0043063056_p1887664894321"></a>Specifies the content of the file to be injected. The file content is encoded using Base64.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **public\_ip**  field description

    <a name="t9b2d3f75e7df4ac69cb775aa03f1a5c6"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063056_rf04af88fbbdf4ecba6a3e6e9aad079f9"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.4.1.1"><p id="en-us_topic_0043063056_afd8569082e55402cba696b519061600b"><a name="en-us_topic_0043063056_afd8569082e55402cba696b519061600b"></a><a name="en-us_topic_0043063056_afd8569082e55402cba696b519061600b"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.4.1.2"><p id="en-us_topic_0043063056_a38d2527b49394965871d7bd5036301d3"><a name="en-us_topic_0043063056_a38d2527b49394965871d7bd5036301d3"></a><a name="en-us_topic_0043063056_a38d2527b49394965871d7bd5036301d3"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65.65656565656566%" id="mcps1.2.4.1.3"><p id="en-us_topic_0043063056_en-us_topic_0020845949_p851285010312"><a name="en-us_topic_0043063056_en-us_topic_0020845949_p851285010312"></a><a name="en-us_topic_0043063056_en-us_topic_0020845949_p851285010312"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063056_r17b93926a7a2473d8e6ca47bb5be9b79"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_a89bdcceda9414a71ae0c7e3d72dabb83"><a name="en-us_topic_0043063056_a89bdcceda9414a71ae0c7e3d72dabb83"></a><a name="en-us_topic_0043063056_a89bdcceda9414a71ae0c7e3d72dabb83"></a>eip</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p5916204120407"><a name="en-us_topic_0043063056_p5916204120407"></a><a name="en-us_topic_0043063056_p5916204120407"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.65656565656566%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_a47ccd07d509f4dd3824f47e9247aea59"><a name="en-us_topic_0043063056_a47ccd07d509f4dd3824f47e9247aea59"></a><a name="en-us_topic_0043063056_a47ccd07d509f4dd3824f47e9247aea59"></a>Specifies the automatically assigned EIP.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8** **eip**  field description

    <a name="td189812958774b49aec372fef2504d3c"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063056_r87ed6857ffae47088b1500be4cc20349"><th class="cellrowborder" valign="top" width="22.74227422742274%" id="mcps1.2.4.1.1"><p id="en-us_topic_0043063056_ad86da605a6b94513b3155b6e54b5083f"><a name="en-us_topic_0043063056_ad86da605a6b94513b3155b6e54b5083f"></a><a name="en-us_topic_0043063056_ad86da605a6b94513b3155b6e54b5083f"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.101710171017103%" id="mcps1.2.4.1.2"><p id="en-us_topic_0043063056_a6a6ab8033ed94d40afe36b99d987b71c"><a name="en-us_topic_0043063056_a6a6ab8033ed94d40afe36b99d987b71c"></a><a name="en-us_topic_0043063056_a6a6ab8033ed94d40afe36b99d987b71c"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="60.15601560156016%" id="mcps1.2.4.1.3"><p id="en-us_topic_0043063056_a9baeb04a7c2f4c9c852c1e5874dbbffd"><a name="en-us_topic_0043063056_a9baeb04a7c2f4c9c852c1e5874dbbffd"></a><a name="en-us_topic_0043063056_a9baeb04a7c2f4c9c852c1e5874dbbffd"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063056_rd79e7d1ab1d647efa45dc111cbe4c367"><td class="cellrowborder" valign="top" width="22.74227422742274%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_ae77f47be6732497c98ea0a0e1b66e2c2"><a name="en-us_topic_0043063056_ae77f47be6732497c98ea0a0e1b66e2c2"></a><a name="en-us_topic_0043063056_ae77f47be6732497c98ea0a0e1b66e2c2"></a>ip_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.101710171017103%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_ac063c9e758fe40d3b7ccbf9d5b4e0dba"><a name="en-us_topic_0043063056_ac063c9e758fe40d3b7ccbf9d5b4e0dba"></a><a name="en-us_topic_0043063056_ac063c9e758fe40d3b7ccbf9d5b4e0dba"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.15601560156016%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_a9098437854d542a899c5e69e2c3c3d2e"><a name="en-us_topic_0043063056_a9098437854d542a899c5e69e2c3c3d2e"></a><a name="en-us_topic_0043063056_a9098437854d542a899c5e69e2c3c3d2e"></a>Specifies the IP address type.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_r4ec4d379ab0a44ccb3f2bd1e38b8f2ba"><td class="cellrowborder" valign="top" width="22.74227422742274%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_a523db77199174a00aa2acaa39b3880e7"><a name="en-us_topic_0043063056_a523db77199174a00aa2acaa39b3880e7"></a><a name="en-us_topic_0043063056_a523db77199174a00aa2acaa39b3880e7"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.101710171017103%" headers="mcps1.2.4.1.2 "><p id="p85011294113"><a name="p85011294113"></a><a name="p85011294113"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.15601560156016%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_a0f936b6301a74ddb82af834687c9be56"><a name="en-us_topic_0043063056_a0f936b6301a74ddb82af834687c9be56"></a><a name="en-us_topic_0043063056_a0f936b6301a74ddb82af834687c9be56"></a>Specifies the bandwidth of an IP address.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9** **bandwidth**  field description

    <a name="t88a38bbf7c8a406581b9be9554c31d79"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063056_r423eaa8930174f0ba29e71993bff93da"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="en-us_topic_0043063056_a4232ce3904fd45eaa61c236eff6ebf85"><a name="en-us_topic_0043063056_a4232ce3904fd45eaa61c236eff6ebf85"></a><a name="en-us_topic_0043063056_a4232ce3904fd45eaa61c236eff6ebf85"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.4.1.2"><p id="en-us_topic_0043063056_a71c241ffcd524934b5b87de8f59b40e1"><a name="en-us_topic_0043063056_a71c241ffcd524934b5b87de8f59b40e1"></a><a name="en-us_topic_0043063056_a71c241ffcd524934b5b87de8f59b40e1"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.35643564356435%" id="mcps1.2.4.1.3"><p id="en-us_topic_0043063056_a7c976ed70ac74bf0a8eac92204ccedcf"><a name="en-us_topic_0043063056_a7c976ed70ac74bf0a8eac92204ccedcf"></a><a name="en-us_topic_0043063056_a7c976ed70ac74bf0a8eac92204ccedcf"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063056_r4b82bcc1304f4adc86aed5c0fb8a4257"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_ae94d06d07bdd40128a583075ebfb2b8c"><a name="en-us_topic_0043063056_ae94d06d07bdd40128a583075ebfb2b8c"></a><a name="en-us_topic_0043063056_ae94d06d07bdd40128a583075ebfb2b8c"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_ae718de7e54424fb7b76d8ec75da93d28"><a name="en-us_topic_0043063056_ae718de7e54424fb7b76d8ec75da93d28"></a><a name="en-us_topic_0043063056_ae718de7e54424fb7b76d8ec75da93d28"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p22263891102758"><a name="en-us_topic_0043063056_p22263891102758"></a><a name="en-us_topic_0043063056_p22263891102758"></a>Specifies the bandwidth (Mbit/s).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_r835b10f4ea2440a59008ed01cf5406e5"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_en-us_topic_0020845949_p840519103344"><a name="en-us_topic_0043063056_en-us_topic_0020845949_p840519103344"></a><a name="en-us_topic_0043063056_en-us_topic_0020845949_p840519103344"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_a2318067ce92d452f860add6c1534c47a"><a name="en-us_topic_0043063056_a2318067ce92d452f860add6c1534c47a"></a><a name="en-us_topic_0043063056_a2318067ce92d452f860add6c1534c47a"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_ac10c2cfc7cd146fdb8123d9cf26f04c1"><a name="en-us_topic_0043063056_ac10c2cfc7cd146fdb8123d9cf26f04c1"></a><a name="en-us_topic_0043063056_ac10c2cfc7cd146fdb8123d9cf26f04c1"></a>Specifies the bandwidth sharing type.</p>
    <p id="en-us_topic_0043063056_p1623102512610"><a name="en-us_topic_0043063056_p1623102512610"></a><a name="en-us_topic_0043063056_p1623102512610"></a>Enumerated values of the sharing type:</p>
    <a name="en-us_topic_0043063056_ul8989111213019"></a><a name="en-us_topic_0043063056_ul8989111213019"></a><ul id="en-us_topic_0043063056_ul8989111213019"><li><strong id="en-us_topic_0043063056_b84235270604852"><a name="en-us_topic_0043063056_b84235270604852"></a><a name="en-us_topic_0043063056_b84235270604852"></a>PER</strong>: dedicated</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0043063056_rd34a9ea5552b45ec8738f5fa3b72a148"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_a37f22f3f0df7441a8edd20467578ef30"><a name="en-us_topic_0043063056_a37f22f3f0df7441a8edd20467578ef30"></a><a name="en-us_topic_0043063056_a37f22f3f0df7441a8edd20467578ef30"></a>charging_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_ad87bdc85b8464970a124eab512415764"><a name="en-us_topic_0043063056_ad87bdc85b8464970a124eab512415764"></a><a name="en-us_topic_0043063056_ad87bdc85b8464970a124eab512415764"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35643564356435%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_a7b09462d7de24bfdb18f5fc46eb08da2"><a name="en-us_topic_0043063056_a7b09462d7de24bfdb18f5fc46eb08da2"></a><a name="en-us_topic_0043063056_a7b09462d7de24bfdb18f5fc46eb08da2"></a>Specifies the bandwidth billing mode.</p>
    <a name="en-us_topic_0043063056_u7a851e86e06a442c942f1c43a416b218"></a><a name="en-us_topic_0043063056_u7a851e86e06a442c942f1c43a416b218"></a><ul id="en-us_topic_0043063056_u7a851e86e06a442c942f1c43a416b218"><li><strong id="en-us_topic_0043063056_b842352706184041"><a name="en-us_topic_0043063056_b842352706184041"></a><a name="en-us_topic_0043063056_b842352706184041"></a>traffic</strong>: billed by traffic.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  10** **metadata**  field description

    <a name="tc523f8f5d3b046b9af465168ec900566"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063056_row5794517795435"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0043063056_p6304778595435"><a name="en-us_topic_0043063056_p6304778595435"></a><a name="en-us_topic_0043063056_p6304778595435"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="en-us_topic_0043063056_p6459317995435"><a name="en-us_topic_0043063056_p6459317995435"></a><a name="en-us_topic_0043063056_p6459317995435"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="en-us_topic_0043063056_p6466497295435"><a name="en-us_topic_0043063056_p6466497295435"></a><a name="en-us_topic_0043063056_p6466497295435"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063056_row337137495435"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0043063056_p460751359557"><a name="en-us_topic_0043063056_p460751359557"></a><a name="en-us_topic_0043063056_p460751359557"></a>User-defined key-value pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0043063056_p406410849557"><a name="en-us_topic_0043063056_p406410849557"></a><a name="en-us_topic_0043063056_p406410849557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0043063056_p35935409557"><a name="en-us_topic_0043063056_p35935409557"></a><a name="en-us_topic_0043063056_p35935409557"></a>Specifies the key and value pair of the metadata.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  11** **security\_groups**  field description

    <a name="table121274211250"></a>
    <table><thead align="left"><tr id="row21632216254"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.4.1.1"><p id="p516332116258"><a name="p516332116258"></a><a name="p516332116258"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.24%" id="mcps1.2.4.1.2"><p id="p1316313216252"><a name="p1316313216252"></a><a name="p1316313216252"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="60.019999999999996%" id="mcps1.2.4.1.3"><p id="p0163521152518"><a name="p0163521152518"></a><a name="p0163521152518"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51635216253"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.4.1.1 "><p id="p121631221182519"><a name="p121631221182519"></a><a name="p121631221182519"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24%" headers="mcps1.2.4.1.2 "><p id="p5163182142517"><a name="p5163182142517"></a><a name="p5163182142517"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.019999999999996%" headers="mcps1.2.4.1.3 "><p id="p16163132182511"><a name="p16163132182511"></a><a name="p16163132182511"></a>Specifies the security group ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "scaling_configuration": {
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
                "adminPass": "***",
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
            "create_time": "2015-07-23T01:04:07Z"
        }
    }
    ```


## Returned Values<a name="section8982304"></a>

-   Normal

    200

-   Abnormal

    <a name="table21746729"></a>
    <table><thead align="left"><tr id="row61647805"><th class="cellrowborder" valign="top" width="44.54%" id="mcps1.1.3.1.1"><p id="p27416314"><a name="p27416314"></a><a name="p27416314"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.46%" id="mcps1.1.3.1.2"><p id="p6128980"><a name="p6128980"></a><a name="p6128980"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26685362"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p14030717"><a name="p14030717"></a><a name="p14030717"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p62746268"><a name="p62746268"></a><a name="p62746268"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row27845503"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p40893240"><a name="p40893240"></a><a name="p40893240"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p24018105"><a name="p24018105"></a><a name="p24018105"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row14836356"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p60894213"><a name="p60894213"></a><a name="p60894213"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p33484259"><a name="p33484259"></a><a name="p33484259"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row32922880"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p49507636"><a name="p49507636"></a><a name="p49507636"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p50695543"><a name="p50695543"></a><a name="p50695543"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row53606711"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p47176343"><a name="p47176343"></a><a name="p47176343"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p63187419"><a name="p63187419"></a><a name="p63187419"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row31815862"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p26948044"><a name="p26948044"></a><a name="p26948044"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p35307962"><a name="p35307962"></a><a name="p35307962"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row49336210"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p36810105"><a name="p36810105"></a><a name="p36810105"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p28828491"><a name="p28828491"></a><a name="p28828491"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row58129833"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p10896009"><a name="p10896009"></a><a name="p10896009"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p10161546"><a name="p10161546"></a><a name="p10161546"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row24345054"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p25792371"><a name="p25792371"></a><a name="p25792371"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p8807292"><a name="p8807292"></a><a name="p8807292"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row12156768"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p45174131"><a name="p45174131"></a><a name="p45174131"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p35225966"><a name="p35225966"></a><a name="p35225966"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row48598242"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p44143566"><a name="p44143566"></a><a name="p44143566"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p18859061"><a name="p18859061"></a><a name="p18859061"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row35513827"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p58047761"><a name="p58047761"></a><a name="p58047761"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p4248175"><a name="p4248175"></a><a name="p4248175"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row38233575"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p9911889"><a name="p9911889"></a><a name="p9911889"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p64665535"><a name="p64665535"></a><a name="p64665535"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row45118907"><td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.3.1.1 "><p id="p30752875"><a name="p30752875"></a><a name="p30752875"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.46%" headers="mcps1.1.3.1.2 "><p id="p7954964"><a name="p7954964"></a><a name="p7954964"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

