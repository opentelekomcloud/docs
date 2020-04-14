# Querying a User List<a name="en-us_topic_0057845638"></a>

## Function Description<a name="s5888597838b0425a92e3419fb766c7f5"></a>

This interface is used to query a user list.

## URI<a name="s46d3616bd4c54e55ba97a528518a5890"></a>

-   URI format

    GET /v3/users

-   URI parameter description

    <a name="table2671410511552"></a>
    <table><thead align="left"><tr id="row2181345411552"><th class="cellrowborder" valign="top" width="22.14%" id="mcps1.1.5.1.1"><p id="p4197580011552"><a name="p4197580011552"></a><a name="p4197580011552"></a><strong id="a6f95694edbbb43d8a152536754b86c82_1"><a name="a6f95694edbbb43d8a152536754b86c82_1"></a><a name="a6f95694edbbb43d8a152536754b86c82_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.09%" id="mcps1.1.5.1.2"><p id="p5555552611552"><a name="p5555552611552"></a><a name="p5555552611552"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.11%" id="mcps1.1.5.1.3"><p id="p3157154611552"><a name="p3157154611552"></a><a name="p3157154611552"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.66%" id="mcps1.1.5.1.4"><p id="p4296341111552"><a name="p4296341111552"></a><a name="p4296341111552"></a><strong id="b842352706114032"><a name="b842352706114032"></a><a name="b842352706114032"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2571374511552"><td class="cellrowborder" valign="top" width="22.14%" headers="mcps1.1.5.1.1 "><p id="p6330725211552"><a name="p6330725211552"></a><a name="p6330725211552"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p2212117911552"><a name="p2212117911552"></a><a name="p2212117911552"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.5.1.3 "><p id="p4769668011552"><a name="p4769668011552"></a><a name="p4769668011552"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.1.5.1.4 "><p id="p928844211552"><a name="p928844211552"></a><a name="p928844211552"></a>ID of the domain that a user belongs to.</p>
    </td>
    </tr>
    <tr id="row1416632711552"><td class="cellrowborder" valign="top" width="22.14%" headers="mcps1.1.5.1.1 "><p id="p6660449211552"><a name="p6660449211552"></a><a name="p6660449211552"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p4626117411552"><a name="p4626117411552"></a><a name="p4626117411552"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.5.1.3 "><p id="p5328411711552"><a name="p5328411711552"></a><a name="p5328411711552"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.1.5.1.4 "><p id="p2702541811552"><a name="p2702541811552"></a><a name="p2702541811552"></a>Whether a user is enabled. <strong id="b35734309114924"><a name="b35734309114924"></a><a name="b35734309114924"></a>true</strong> indicates that the user is enabled. <strong id="b51021073114926"><a name="b51021073114926"></a><a name="b51021073114926"></a>false</strong> indicates that the user is disabled. The default value is <strong id="b10453693114924"><a name="b10453693114924"></a><a name="b10453693114924"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="row4157523011552"><td class="cellrowborder" valign="top" width="22.14%" headers="mcps1.1.5.1.1 "><p id="p4466247811552"><a name="p4466247811552"></a><a name="p4466247811552"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p3321824211552"><a name="p3321824211552"></a><a name="p3321824211552"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.5.1.3 "><p id="p4240978811552"><a name="p4240978811552"></a><a name="p4240978811552"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.1.5.1.4 "><p id="p1727292311552"><a name="p1727292311552"></a><a name="p1727292311552"></a>Username.</p>
    </td>
    </tr>
    <tr id="row923064925220"><td class="cellrowborder" valign="top" width="22.14%" headers="mcps1.1.5.1.1 "><p id="p122311493521"><a name="p122311493521"></a><a name="p122311493521"></a>password_expires_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p1823334995215"><a name="p1823334995215"></a><a name="p1823334995215"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.5.1.3 "><p id="p623364945219"><a name="p623364945219"></a><a name="p623364945219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.66%" headers="mcps1.1.5.1.4 "><p id="p1123314965211"><a name="p1123314965211"></a><a name="p1123314965211"></a>Password expiration time. The format is <strong id="b842352706153618"><a name="b842352706153618"></a><a name="b842352706153618"></a>password_expires_at=</strong><em id="i842352697153316"><a name="i842352697153316"></a><a name="i842352697153316"></a>operator</em><strong id="b842352706153622"><a name="b842352706153622"></a><a name="b842352706153622"></a>:</strong><em id="i842352697153329"><a name="i842352697153329"></a><a name="i842352697153329"></a>timestamp</em>.</p>
    <p id="p1838112538569"><a name="p1838112538569"></a><a name="p1838112538569"></a>Example:</p>
    <pre class="screen" id="screen85910169576"><a name="screen85910169576"></a><a name="screen85910169576"></a>password_expires_at=lt:2016-12-08T22:02:00Z</pre>
    <a name="ul9511557111910"></a><a name="ul9511557111910"></a><ul id="ul9511557111910"><li>The value of <strong id="b842352706153734"><a name="b842352706153734"></a><a name="b842352706153734"></a>operator</strong> can be <strong id="b842352706153825"><a name="b842352706153825"></a><a name="b842352706153825"></a>lt</strong>, <strong id="b842352706153821"><a name="b842352706153821"></a><a name="b842352706153821"></a>lte</strong>, <strong id="b842352706153814"><a name="b842352706153814"></a><a name="b842352706153814"></a>gt</strong>, <strong id="b84235270615388"><a name="b84235270615388"></a><a name="b84235270615388"></a>gte</strong>, <strong id="b84235270615384"><a name="b84235270615384"></a><a name="b84235270615384"></a>eq</strong>, or <strong id="b84235270615380"><a name="b84235270615380"></a><a name="b84235270615380"></a>neq</strong>.<a name="ul1162653632014"></a><a name="ul1162653632014"></a><ul id="ul1162653632014"><li><strong id="b84235270615395"><a name="b84235270615395"></a><a name="b84235270615395"></a>lt</strong>: The expiration time is earlier than <em id="i842352697154057"><a name="i842352697154057"></a><a name="i842352697154057"></a>timestamp</em>.</li><li><strong id="b842352706154029"><a name="b842352706154029"></a><a name="b842352706154029"></a>lte</strong>: The expiration time is earlier than or equal to <em id="i84235269715416"><a name="i84235269715416"></a><a name="i84235269715416"></a>timestamp</em>.</li><li><strong id="b1953037015"><a name="b1953037015"></a><a name="b1953037015"></a>gt</strong>: The expiration time is later than <em id="i84235269715427"><a name="i84235269715427"></a><a name="i84235269715427"></a>timestamp</em>.</li><li><strong id="b1566226623"><a name="b1566226623"></a><a name="b1566226623"></a>gte</strong>: The expiration time is equal to or later than <em id="i714542272"><a name="i714542272"></a><a name="i714542272"></a>timestamp</em>.</li><li><strong id="b939446570"><a name="b939446570"></a><a name="b939446570"></a>eq</strong>: The expiration time is equal to <em id="i117644983"><a name="i117644983"></a><a name="i117644983"></a>timestamp</em>.</li><li><strong id="b1302685372"><a name="b1302685372"></a><a name="b1302685372"></a>neq</strong>: The expiration time is not equal to <em id="i33290378"><a name="i33290378"></a><a name="i33290378"></a>timestamp</em>.</li></ul>
    </li><li>The <strong id="b842352706154327"><a name="b842352706154327"></a><a name="b842352706154327"></a>timestamp</strong> format is <strong id="b842352706154332"><a name="b842352706154332"></a><a name="b842352706154332"></a>YYYY-MM-DDTHH:mm:ssZ</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="se7fe5cac0d544e119c49322cc1707eb6"></a>

-   Request header parameter description

    <a name="t68c7bd10e66a4380a1e6cdc78ca95669"></a>
    <table><thead align="left"><tr id="r584496594a404ce18918a40e6e57c2ec"><th class="cellrowborder" valign="top" width="21.81218121812181%" id="mcps1.1.5.1.1"><p id="ac3a989cc5d3a405889eabb47dee84b04"><a name="ac3a989cc5d3a405889eabb47dee84b04"></a><a name="ac3a989cc5d3a405889eabb47dee84b04"></a><strong id="a6f95694edbbb43d8a152536754b86c82_3"><a name="a6f95694edbbb43d8a152536754b86c82_3"></a><a name="a6f95694edbbb43d8a152536754b86c82_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.352035203520348%" id="mcps1.1.5.1.2"><p id="a69a20ac00b86496aa8418517c542b0da"><a name="a69a20ac00b86496aa8418517c542b0da"></a><a name="a69a20ac00b86496aa8418517c542b0da"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.092009200920092%" id="mcps1.1.5.1.3"><p id="a92c23d4441054df0972e025aeb3a8d7f"><a name="a92c23d4441054df0972e025aeb3a8d7f"></a><a name="a92c23d4441054df0972e025aeb3a8d7f"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.743774377437745%" id="mcps1.1.5.1.4"><p id="abe6882c44cf4402d8ed7706b9278f33b"><a name="abe6882c44cf4402d8ed7706b9278f33b"></a><a name="abe6882c44cf4402d8ed7706b9278f33b"></a><strong id="b50354700121445"><a name="b50354700121445"></a><a name="b50354700121445"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r5d63069d6a8a426e8b25b94d1b4d302a"><td class="cellrowborder" valign="top" width="21.81218121812181%" headers="mcps1.1.5.1.1 "><p id="ad4fb6253385c46ab8720a0e13f573694"><a name="ad4fb6253385c46ab8720a0e13f573694"></a><a name="ad4fb6253385c46ab8720a0e13f573694"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.352035203520348%" headers="mcps1.1.5.1.2 "><p id="a6b33800bcb2a446695b1d33a2d751554"><a name="a6b33800bcb2a446695b1d33a2d751554"></a><a name="a6b33800bcb2a446695b1d33a2d751554"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.092009200920092%" headers="mcps1.1.5.1.3 "><p id="ab34a5e95b76b4b79a72da0734025f211"><a name="ab34a5e95b76b4b79a72da0734025f211"></a><a name="ab34a5e95b76b4b79a72da0734025f211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.743774377437745%" headers="mcps1.1.5.1.4 "><p id="a716277ae541d4553bb10490f9c02593d"><a name="a716277ae541d4553bb10490f9c02593d"></a><a name="a716277ae541d4553bb10490f9c02593d"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row29501427115257"><td class="cellrowborder" valign="top" width="21.81218121812181%" headers="mcps1.1.5.1.1 "><p id="p6637478211538"><a name="p6637478211538"></a><a name="p6637478211538"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.352035203520348%" headers="mcps1.1.5.1.2 "><p id="p764826811538"><a name="p764826811538"></a><a name="p764826811538"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.092009200920092%" headers="mcps1.1.5.1.3 "><p id="p1553001111538"><a name="p1553001111538"></a><a name="p1553001111538"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.743774377437745%" headers="mcps1.1.5.1.4 "><p id="p3577810173953"><a name="p3577810173953"></a><a name="p3577810173953"></a>Authenticated token with the <strong id="b32749661102843"><a name="b32749661102843"></a><a name="b32749661102843"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://172.30.48.86:31943/v3/users
    ```


## Response<a name="s3a08e13bb5b34dc2ba4dcd84a0d51cf5"></a>

-   Response body parameter description

    <a name="t1266dd240c3649048c9f42af34a0686b"></a>
    <table><thead align="left"><tr id="rd8ac2cd80e4b47d684b61df4f3c570cf"><th class="cellrowborder" valign="top" width="21.68%" id="mcps1.1.5.1.1"><p id="ad167d1bf89ca443eac693ea562da12a3"><a name="ad167d1bf89ca443eac693ea562da12a3"></a><a name="ad167d1bf89ca443eac693ea562da12a3"></a><strong id="a6f95694edbbb43d8a152536754b86c82_5"><a name="a6f95694edbbb43d8a152536754b86c82_5"></a><a name="a6f95694edbbb43d8a152536754b86c82_5"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.49%" id="mcps1.1.5.1.2"><p id="aad08ea1f8c8e4a42a1a81112a74cb237"><a name="aad08ea1f8c8e4a42a1a81112a74cb237"></a><a name="aad08ea1f8c8e4a42a1a81112a74cb237"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.349999999999998%" id="mcps1.1.5.1.3"><p id="a9b5fafff0348408893dcc06fbe0b1186"><a name="a9b5fafff0348408893dcc06fbe0b1186"></a><a name="a9b5fafff0348408893dcc06fbe0b1186"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.480000000000004%" id="mcps1.1.5.1.4"><p id="ad002a0bf107a468884a5777e55f837f6"><a name="ad002a0bf107a468884a5777e55f837f6"></a><a name="ad002a0bf107a468884a5777e55f837f6"></a><strong id="b30945568121445"><a name="b30945568121445"></a><a name="b30945568121445"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="ref3b81e8e64e418c961ca1bce6f25280"><td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.1.5.1.1 "><p id="abb2b4d81b907497da50ad4f12760f7dc"><a name="abb2b4d81b907497da50ad4f12760f7dc"></a><a name="abb2b4d81b907497da50ad4f12760f7dc"></a>users</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.2 "><p id="a7e49a4eaca054e36ba774b0cdc492081"><a name="a7e49a4eaca054e36ba774b0cdc492081"></a><a name="a7e49a4eaca054e36ba774b0cdc492081"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.349999999999998%" headers="mcps1.1.5.1.3 "><p id="p9747112319316"><a name="p9747112319316"></a><a name="p9747112319316"></a>JSONArray</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.480000000000004%" headers="mcps1.1.5.1.4 "><p id="a8ded0409c6d948dc82f7f779a4cfa5b8"><a name="a8ded0409c6d948dc82f7f779a4cfa5b8"></a><a name="a8ded0409c6d948dc82f7f779a4cfa5b8"></a>User list.</p>
    </td>
    </tr>
    <tr id="row43686692165815"><td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.1.5.1.1 "><p id="p48961187165815"><a name="p48961187165815"></a><a name="p48961187165815"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.2 "><p id="p6433206165815"><a name="p6433206165815"></a><a name="p6433206165815"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.349999999999998%" headers="mcps1.1.5.1.3 "><p id="p819418211314"><a name="p819418211314"></a><a name="p819418211314"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.480000000000004%" headers="mcps1.1.5.1.4 "><p id="p63901882165815"><a name="p63901882165815"></a><a name="p63901882165815"></a>Links of a user resource.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the user format

    <a name="table683623312113"></a>
    <table><thead align="left"><tr id="row19845533162112"><th class="cellrowborder" valign="top" width="19.81%" id="mcps1.1.5.1.1"><p id="p484813315212"><a name="p484813315212"></a><a name="p484813315212"></a><strong id="a6f95694edbbb43d8a152536754b86c82_7"><a name="a6f95694edbbb43d8a152536754b86c82_7"></a><a name="a6f95694edbbb43d8a152536754b86c82_7"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.45%" id="mcps1.1.5.1.2"><p id="p88525332215"><a name="p88525332215"></a><a name="p88525332215"></a><strong id="b1670597098"><a name="b1670597098"></a><a name="b1670597098"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.91%" id="mcps1.1.5.1.3"><p id="p14856183320218"><a name="p14856183320218"></a><a name="p14856183320218"></a><strong id="b14476260"><a name="b14476260"></a><a name="b14476260"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.83%" id="mcps1.1.5.1.4"><p id="p286173320218"><a name="p286173320218"></a><a name="p286173320218"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3863153311217"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p88666332215"><a name="p88666332215"></a><a name="p88666332215"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p386916336212"><a name="p386916336212"></a><a name="p386916336212"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p7871123352112"><a name="p7871123352112"></a><a name="p7871123352112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p6874133172114"><a name="p6874133172114"></a><a name="p6874133172114"></a>Description for a user.</p>
    </td>
    </tr>
    <tr id="row128753339212"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p18877113392115"><a name="p18877113392115"></a><a name="p18877113392115"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p1487933362114"><a name="p1487933362114"></a><a name="p1487933362114"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p1388513334213"><a name="p1388513334213"></a><a name="p1388513334213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p3888143315211"><a name="p3888143315211"></a><a name="p3888143315211"></a>ID of the tenant that the user belongs to.</p>
    </td>
    </tr>
    <tr id="row089017338215"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p1389315339212"><a name="p1389315339212"></a><a name="p1389315339212"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p3896123318213"><a name="p3896123318213"></a><a name="p3896123318213"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p13899103317210"><a name="p13899103317210"></a><a name="p13899103317210"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p12901113312215"><a name="p12901113312215"></a><a name="p12901113312215"></a>Indicates whether the user is enabled. The value can be <strong id="b0372455203917"><a name="b0372455203917"></a><a name="b0372455203917"></a>true</strong> or <strong id="b4751556173915"><a name="b4751556173915"></a><a name="b4751556173915"></a>false</strong>. The default value is <strong id="b74111258193916"><a name="b74111258193916"></a><a name="b74111258193916"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="row29030337213"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p890513302110"><a name="p890513302110"></a><a name="p890513302110"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p189081733112118"><a name="p189081733112118"></a><a name="p189081733112118"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p691093332117"><a name="p691093332117"></a><a name="p691093332117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p091212333214"><a name="p091212333214"></a><a name="p091212333214"></a>User ID.</p>
    </td>
    </tr>
    <tr id="row20913123342114"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p1391415332215"><a name="p1391415332215"></a><a name="p1391415332215"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p391693315216"><a name="p391693315216"></a><a name="p391693315216"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p189191933182113"><a name="p189191933182113"></a><a name="p189191933182113"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p192211334219"><a name="p192211334219"></a><a name="p192211334219"></a>User resource links.</p>
    </td>
    </tr>
    <tr id="row179247335217"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p119261133192110"><a name="p119261133192110"></a><a name="p119261133192110"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p189291933142116"><a name="p189291933142116"></a><a name="p189291933142116"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p493213315214"><a name="p493213315214"></a><a name="p493213315214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p29351333192112"><a name="p29351333192112"></a><a name="p29351333192112"></a>Username</p>
    </td>
    </tr>
    <tr id="row193643316211"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p1393815334212"><a name="p1393815334212"></a><a name="p1393815334212"></a>password_expires_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p1194143312119"><a name="p1194143312119"></a><a name="p1194143312119"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p18943633142112"><a name="p18943633142112"></a><a name="p18943633142112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p294619332218"><a name="p294619332218"></a><a name="p294619332218"></a>UTC time when the password will expire. <strong id="b1483686226114627"><a name="b1483686226114627"></a><a name="b1483686226114627"></a>null</strong> indicates that the password will not expire.</p>
    </td>
    </tr>
    <tr id="row294912331214"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p17951143302120"><a name="p17951143302120"></a><a name="p17951143302120"></a>pwd_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p11955533102116"><a name="p11955533102116"></a><a name="p11955533102116"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p29573333214"><a name="p29573333214"></a><a name="p29573333214"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p09601033172120"><a name="p09601033172120"></a><a name="p09601033172120"></a>Password status. <strong id="b355111133319"><a name="b355111133319"></a><a name="b355111133319"></a>true</strong> means that the password needs to be changed, and <strong id="b11550112333"><a name="b11550112333"></a><a name="b11550112333"></a>false</strong> means that the password is normal.</p>
    </td>
    </tr>
    <tr id="row496283313218"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p179691433202117"><a name="p179691433202117"></a><a name="p179691433202117"></a>pwd_strength</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p15972333142118"><a name="p15972333142118"></a><a name="p15972333142118"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p14974113312218"><a name="p14974113312218"></a><a name="p14974113312218"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p69781233112115"><a name="p69781233112115"></a><a name="p69781233112115"></a>Password strength. The value can be <strong id="b153847174517"><a name="b153847174517"></a><a name="b153847174517"></a>high</strong>, <strong id="b8634162184518"><a name="b8634162184518"></a><a name="b8634162184518"></a>mid</strong>, or <strong id="b107749304513"><a name="b107749304513"></a><a name="b107749304513"></a>low</strong>.</p>
    </td>
    </tr>
    <tr id="row3979173362110"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p16982433112119"><a name="p16982433112119"></a><a name="p16982433112119"></a>mobile</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p179855333218"><a name="p179855333218"></a><a name="p179855333218"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p1198913337219"><a name="p1198913337219"></a><a name="p1198913337219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p299293302113"><a name="p299293302113"></a><a name="p299293302113"></a>Mobile number of the user.</p>
    </td>
    </tr>
    <tr id="row12993103382113"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p89961133152119"><a name="p89961133152119"></a><a name="p89961133152119"></a>email</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p159991333132113"><a name="p159991333132113"></a><a name="p159991333132113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p82153416214"><a name="p82153416214"></a><a name="p82153416214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p94153412215"><a name="p94153412215"></a><a name="p94153412215"></a>Email address of the user.</p>
    </td>
    </tr>
    <tr id="row1851134102111"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p1671834142117"><a name="p1671834142117"></a><a name="p1671834142117"></a>forceResetPwd</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p2101534142113"><a name="p2101534142113"></a><a name="p2101534142113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p1412133452113"><a name="p1412133452113"></a><a name="p1412133452113"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p1015173472110"><a name="p1015173472110"></a><a name="p1015173472110"></a>Indicates whether password reset is required at the next login.</p>
    </td>
    </tr>
    <tr id="row1161234152117"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p519173417211"><a name="p519173417211"></a><a name="p519173417211"></a>default_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p18213344218"><a name="p18213344218"></a><a name="p18213344218"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p423193420211"><a name="p423193420211"></a><a name="p423193420211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p1925143462116"><a name="p1925143462116"></a><a name="p1925143462116"></a>ID of the project that is displayed by default when the user logs in to the console.</p>
    </td>
    </tr>
    <tr id="row9263348215"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p1330334112110"><a name="p1330334112110"></a><a name="p1330334112110"></a>last_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="p1232193418212"><a name="p1232193418212"></a><a name="p1232193418212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p17361734142110"><a name="p17361734142110"></a><a name="p17361734142110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="p203843472112"><a name="p203843472112"></a><a name="p203843472112"></a>ID of the project that the user lastly accessed before exiting the system.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample response

    ```
    {
        "users": [{
            "name": "username",
            "links": {
                "self": "https://sample.domain.com/v3/users/6d8b04e3bf99445b8f76300xxx"
            },
            "description": "1234",
            "domain_id": "88b16b6440684467b8825d7xxx",
            "enabled": false,
            "id": "6d8b04e3bf99445b8f763009xxx",
            "default_project_id": "263fd9",
            "password_expires_at": "2016-12-07T00:00:00.000000Z",
            "pwd_status": true,
            "pwd_strength": "high",
            "mobile": "",
            "email": "",
            "forceResetPwd": false,
            "last_project_id": ""
        }],
        "links": {
            "self": "https://sample.domain.com/v3/users?domain_id=88b16b6440684467b882xxx154d8&enabled=false",
            "previous": null,
            "next": null
        }
    }
    ```


## Status Codes<a name="sbfe93ca4c2b9427dbb2218a4e72da6a8"></a>

<a name="en-us_topic_0035544336_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0035544336_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035544336_p51565323"><a name="en-us_topic_0035544336_p51565323"></a><a name="en-us_topic_0035544336_p51565323"></a><strong id="b842352706183757"><a name="b842352706183757"></a><a name="b842352706183757"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035544336_p16041657"><a name="en-us_topic_0035544336_p16041657"></a><a name="en-us_topic_0035544336_p16041657"></a><strong id="b38983553121445"><a name="b38983553121445"></a><a name="b38983553121445"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035544336_row24305815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035544336_p22613965"><a name="en-us_topic_0035544336_p22613965"></a><a name="en-us_topic_0035544336_p22613965"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035544336_p19791876"><a name="en-us_topic_0035544336_p19791876"></a><a name="en-us_topic_0035544336_p19791876"></a>The request is successful.</p>
</td>
</tr>
<tr id="en-us_topic_0035544336_row43909159"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035544336_p66980994"><a name="en-us_topic_0035544336_p66980994"></a><a name="en-us_topic_0035544336_p66980994"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035544336_p56751409"><a name="en-us_topic_0035544336_p56751409"></a><a name="en-us_topic_0035544336_p56751409"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="rb99fbab78bc54ae4953661763b573830"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aef55745ff0834933af36d690e2e339b8"><a name="aef55745ff0834933af36d690e2e339b8"></a><a name="aef55745ff0834933af36d690e2e339b8"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a480215738ced4bf5a8feafa2681db93b"><a name="a480215738ced4bf5a8feafa2681db93b"></a><a name="a480215738ced4bf5a8feafa2681db93b"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="en-us_topic_0035544336_row41000636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035544336_p32717189"><a name="en-us_topic_0035544336_p32717189"></a><a name="en-us_topic_0035544336_p32717189"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae678037f26d640f5a985c943e2ffb92e"><a name="ae678037f26d640f5a985c943e2ffb92e"></a><a name="ae678037f26d640f5a985c943e2ffb92e"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="r1fd5c05b7b6b4c048f3f7b9ddbc755b0"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a5d7e2305922e4f9098442a900792dae1"><a name="a5d7e2305922e4f9098442a900792dae1"></a><a name="a5d7e2305922e4f9098442a900792dae1"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a9edf299d0513460caaac8a2a19b76e9a"><a name="a9edf299d0513460caaac8a2a19b76e9a"></a><a name="a9edf299d0513460caaac8a2a19b76e9a"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="rbb5133f150fd42eebde8dd6e390ecbd5"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ad1a2754016e44193a97043265cd611cf"><a name="ad1a2754016e44193a97043265cd611cf"></a><a name="ad1a2754016e44193a97043265cd611cf"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a81837d461ef445259c5a6e9e1ce0e32a"><a name="a81837d461ef445259c5a6e9e1ce0e32a"></a><a name="a81837d461ef445259c5a6e9e1ce0e32a"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="r2cecff297b1a412f956a312d3cd7acc9"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1f617621d1bc4a9facb1c84d1946002b"><a name="a1f617621d1bc4a9facb1c84d1946002b"></a><a name="a1f617621d1bc4a9facb1c84d1946002b"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ac31ead3ee2db40eea8ae45b2779a09e9"><a name="ac31ead3ee2db40eea8ae45b2779a09e9"></a><a name="ac31ead3ee2db40eea8ae45b2779a09e9"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="rd71e0e00759f4179a2dccaf345ba9f2f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1657c5ca5ebd4a2cbacbdb35fc9b7601"><a name="a1657c5ca5ebd4a2cbacbdb35fc9b7601"></a><a name="a1657c5ca5ebd4a2cbacbdb35fc9b7601"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a88b4b14048564e12942b8151dc791b99"><a name="a88b4b14048564e12942b8151dc791b99"></a><a name="a88b4b14048564e12942b8151dc791b99"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="r5647e5fd26974514ac66cc3925f30601"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a16dfaa16ceac4a33a468c0ae158292fb"><a name="a16dfaa16ceac4a33a468c0ae158292fb"></a><a name="a16dfaa16ceac4a33a468c0ae158292fb"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a5635c1924d9648a8be89b1e5dcf0a87b"><a name="a5635c1924d9648a8be89b1e5dcf0a87b"></a><a name="a5635c1924d9648a8be89b1e5dcf0a87b"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

