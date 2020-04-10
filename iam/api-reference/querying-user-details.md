# Querying User Details<a name="en-us_topic_0057845652"></a>

## Function Description<a name="s5888597838b0425a92e3419fb766c7f5"></a>

This interface is used to query detailed information about a specified user.

## URI<a name="s46d3616bd4c54e55ba97a528518a5890"></a>

-   URI format

    GET /v3/users/\{user\_id\}

-   URI parameter description

    <a name="table12695788105445"></a>
    <table><thead align="left"><tr id="row2052093105445"><th class="cellrowborder" valign="top" width="21.61%" id="mcps1.1.5.1.1"><p id="p42010912105445"><a name="p42010912105445"></a><a name="p42010912105445"></a><strong id="a6f95694edbbb43d8a152536754b86c82_1"><a name="a6f95694edbbb43d8a152536754b86c82_1"></a><a name="a6f95694edbbb43d8a152536754b86c82_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.28%" id="mcps1.1.5.1.2"><p id="p17489287105445"><a name="p17489287105445"></a><a name="p17489287105445"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.49%" id="mcps1.1.5.1.3"><p id="p58168660105445"><a name="p58168660105445"></a><a name="p58168660105445"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.62%" id="mcps1.1.5.1.4"><p id="p63581350105445"><a name="p63581350105445"></a><a name="p63581350105445"></a><strong id="b842352706114032"><a name="b842352706114032"></a><a name="b842352706114032"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8541085105445"><td class="cellrowborder" valign="top" width="21.61%" headers="mcps1.1.5.1.1 "><p id="p2158168105445"><a name="p2158168105445"></a><a name="p2158168105445"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.1.5.1.2 "><p id="p66884857105445"><a name="p66884857105445"></a><a name="p66884857105445"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.3 "><p id="p6689695105445"><a name="p6689695105445"></a><a name="p6689695105445"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.62%" headers="mcps1.1.5.1.4 "><p id="p1895018105445"><a name="p1895018105445"></a><a name="p1895018105445"></a>User ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="se7fe5cac0d544e119c49322cc1707eb6"></a>

-   Request header parameter description

    <a name="t68c7bd10e66a4380a1e6cdc78ca95669"></a>
    <table><thead align="left"><tr id="r584496594a404ce18918a40e6e57c2ec"><th class="cellrowborder" valign="top" width="21.68%" id="mcps1.1.5.1.1"><p id="ac3a989cc5d3a405889eabb47dee84b04"><a name="ac3a989cc5d3a405889eabb47dee84b04"></a><a name="ac3a989cc5d3a405889eabb47dee84b04"></a><strong id="a6f95694edbbb43d8a152536754b86c82_3"><a name="a6f95694edbbb43d8a152536754b86c82_3"></a><a name="a6f95694edbbb43d8a152536754b86c82_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.09%" id="mcps1.1.5.1.2"><p id="a69a20ac00b86496aa8418517c542b0da"><a name="a69a20ac00b86496aa8418517c542b0da"></a><a name="a69a20ac00b86496aa8418517c542b0da"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.560000000000002%" id="mcps1.1.5.1.3"><p id="a92c23d4441054df0972e025aeb3a8d7f"><a name="a92c23d4441054df0972e025aeb3a8d7f"></a><a name="a92c23d4441054df0972e025aeb3a8d7f"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.669999999999995%" id="mcps1.1.5.1.4"><p id="abe6882c44cf4402d8ed7706b9278f33b"><a name="abe6882c44cf4402d8ed7706b9278f33b"></a><a name="abe6882c44cf4402d8ed7706b9278f33b"></a><strong id="b4440558117299"><a name="b4440558117299"></a><a name="b4440558117299"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r5d63069d6a8a426e8b25b94d1b4d302a"><td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.1.5.1.1 "><p id="ad4fb6253385c46ab8720a0e13f573694"><a name="ad4fb6253385c46ab8720a0e13f573694"></a><a name="ad4fb6253385c46ab8720a0e13f573694"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="a6b33800bcb2a446695b1d33a2d751554"><a name="a6b33800bcb2a446695b1d33a2d751554"></a><a name="a6b33800bcb2a446695b1d33a2d751554"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.560000000000002%" headers="mcps1.1.5.1.3 "><p id="ab34a5e95b76b4b79a72da0734025f211"><a name="ab34a5e95b76b4b79a72da0734025f211"></a><a name="ab34a5e95b76b4b79a72da0734025f211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.669999999999995%" headers="mcps1.1.5.1.4 "><p id="a716277ae541d4553bb10490f9c02593d"><a name="a716277ae541d4553bb10490f9c02593d"></a><a name="a716277ae541d4553bb10490f9c02593d"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row29501427115257"><td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.1.5.1.1 "><p id="p6637478211538"><a name="p6637478211538"></a><a name="p6637478211538"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p764826811538"><a name="p764826811538"></a><a name="p764826811538"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.560000000000002%" headers="mcps1.1.5.1.3 "><p id="p1553001111538"><a name="p1553001111538"></a><a name="p1553001111538"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.669999999999995%" headers="mcps1.1.5.1.4 "><p id="p4997141111538"><a name="p4997141111538"></a><a name="p4997141111538"></a>An authenticated token with <strong id="b43461543154119"><a name="b43461543154119"></a><a name="b43461543154119"></a>Security Administrator</strong> permissions or a user token</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://172.30.48.86:31943/v3/users/43cbe5e77aaf4665bbb962062dc1fc9d
    ```


## Response<a name="s3a08e13bb5b34dc2ba4dcd84a0d51cf5"></a>

-   Response body parameter description

    <a name="t1266dd240c3649048c9f42af34a0686b"></a>
    <table><thead align="left"><tr id="rd8ac2cd80e4b47d684b61df4f3c570cf"><th class="cellrowborder" valign="top" width="21.68%" id="mcps1.1.5.1.1"><p id="ad167d1bf89ca443eac693ea562da12a3"><a name="ad167d1bf89ca443eac693ea562da12a3"></a><a name="ad167d1bf89ca443eac693ea562da12a3"></a><strong id="a6f95694edbbb43d8a152536754b86c82_5"><a name="a6f95694edbbb43d8a152536754b86c82_5"></a><a name="a6f95694edbbb43d8a152536754b86c82_5"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.22%" id="mcps1.1.5.1.2"><p id="aad08ea1f8c8e4a42a1a81112a74cb237"><a name="aad08ea1f8c8e4a42a1a81112a74cb237"></a><a name="aad08ea1f8c8e4a42a1a81112a74cb237"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.1.5.1.3"><p id="a9b5fafff0348408893dcc06fbe0b1186"><a name="a9b5fafff0348408893dcc06fbe0b1186"></a><a name="a9b5fafff0348408893dcc06fbe0b1186"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.480000000000004%" id="mcps1.1.5.1.4"><p id="ad002a0bf107a468884a5777e55f837f6"><a name="ad002a0bf107a468884a5777e55f837f6"></a><a name="ad002a0bf107a468884a5777e55f837f6"></a><strong id="b5037987417299"><a name="b5037987417299"></a><a name="b5037987417299"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="ref3b81e8e64e418c961ca1bce6f25280"><td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.1.5.1.1 "><p id="abb2b4d81b907497da50ad4f12760f7dc"><a name="abb2b4d81b907497da50ad4f12760f7dc"></a><a name="abb2b4d81b907497da50ad4f12760f7dc"></a>user</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.5.1.2 "><p id="a7e49a4eaca054e36ba774b0cdc492081"><a name="a7e49a4eaca054e36ba774b0cdc492081"></a><a name="a7e49a4eaca054e36ba774b0cdc492081"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.1.5.1.3 "><p id="p53073101236"><a name="p53073101236"></a><a name="p53073101236"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.480000000000004%" headers="mcps1.1.5.1.4 "><p id="a8ded0409c6d948dc82f7f779a4cfa5b8"><a name="a8ded0409c6d948dc82f7f779a4cfa5b8"></a><a name="a8ded0409c6d948dc82f7f779a4cfa5b8"></a>User details</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the user format

    <a name="t3ef10d134105438f922a72ac36adbe13"></a>
    <table><thead align="left"><tr id="en-us_topic_0147658916_row19845533162112"><th class="cellrowborder" valign="top" width="19.81%" id="mcps1.1.5.1.1"><p id="en-us_topic_0147658916_p484813315212"><a name="en-us_topic_0147658916_p484813315212"></a><a name="en-us_topic_0147658916_p484813315212"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.45%" id="mcps1.1.5.1.2"><p id="en-us_topic_0147658916_p88525332215"><a name="en-us_topic_0147658916_p88525332215"></a><a name="en-us_topic_0147658916_p88525332215"></a><strong id="b630783158"><a name="b630783158"></a><a name="b630783158"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.91%" id="mcps1.1.5.1.3"><p id="en-us_topic_0147658916_p14856183320218"><a name="en-us_topic_0147658916_p14856183320218"></a><a name="en-us_topic_0147658916_p14856183320218"></a><strong id="b1001076490"><a name="b1001076490"></a><a name="b1001076490"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.83%" id="mcps1.1.5.1.4"><p id="en-us_topic_0147658916_p286173320218"><a name="en-us_topic_0147658916_p286173320218"></a><a name="en-us_topic_0147658916_p286173320218"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0147658916_row3863153311217"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p88666332215"><a name="en-us_topic_0147658916_p88666332215"></a><a name="en-us_topic_0147658916_p88666332215"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p386916336212"><a name="en-us_topic_0147658916_p386916336212"></a><a name="en-us_topic_0147658916_p386916336212"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p7871123352112"><a name="en-us_topic_0147658916_p7871123352112"></a><a name="en-us_topic_0147658916_p7871123352112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p6874133172114"><a name="en-us_topic_0147658916_p6874133172114"></a><a name="en-us_topic_0147658916_p6874133172114"></a>Description for a user.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0147658916_row128753339212"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p18877113392115"><a name="en-us_topic_0147658916_p18877113392115"></a><a name="en-us_topic_0147658916_p18877113392115"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p1487933362114"><a name="en-us_topic_0147658916_p1487933362114"></a><a name="en-us_topic_0147658916_p1487933362114"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p1388513334213"><a name="en-us_topic_0147658916_p1388513334213"></a><a name="en-us_topic_0147658916_p1388513334213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p3888143315211"><a name="en-us_topic_0147658916_p3888143315211"></a><a name="en-us_topic_0147658916_p3888143315211"></a>ID of the tenant that the user belongs to.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0147658916_row089017338215"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p1389315339212"><a name="en-us_topic_0147658916_p1389315339212"></a><a name="en-us_topic_0147658916_p1389315339212"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p3896123318213"><a name="en-us_topic_0147658916_p3896123318213"></a><a name="en-us_topic_0147658916_p3896123318213"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p13899103317210"><a name="en-us_topic_0147658916_p13899103317210"></a><a name="en-us_topic_0147658916_p13899103317210"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p12901113312215"><a name="en-us_topic_0147658916_p12901113312215"></a><a name="en-us_topic_0147658916_p12901113312215"></a>Indicates whether the user is enabled. The value can be <strong id="b0372455203917"><a name="b0372455203917"></a><a name="b0372455203917"></a>true</strong> or <strong id="b4751556173915"><a name="b4751556173915"></a><a name="b4751556173915"></a>false</strong>. The default value is <strong id="b74111258193916"><a name="b74111258193916"></a><a name="b74111258193916"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0147658916_row29030337213"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p890513302110"><a name="en-us_topic_0147658916_p890513302110"></a><a name="en-us_topic_0147658916_p890513302110"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p189081733112118"><a name="en-us_topic_0147658916_p189081733112118"></a><a name="en-us_topic_0147658916_p189081733112118"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p691093332117"><a name="en-us_topic_0147658916_p691093332117"></a><a name="en-us_topic_0147658916_p691093332117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p091212333214"><a name="en-us_topic_0147658916_p091212333214"></a><a name="en-us_topic_0147658916_p091212333214"></a>ID of a user.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0147658916_row20913123342114"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p1391415332215"><a name="en-us_topic_0147658916_p1391415332215"></a><a name="en-us_topic_0147658916_p1391415332215"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p391693315216"><a name="en-us_topic_0147658916_p391693315216"></a><a name="en-us_topic_0147658916_p391693315216"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p189191933182113"><a name="en-us_topic_0147658916_p189191933182113"></a><a name="en-us_topic_0147658916_p189191933182113"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p192211334219"><a name="en-us_topic_0147658916_p192211334219"></a><a name="en-us_topic_0147658916_p192211334219"></a>Links of a user resource.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0147658916_row179247335217"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p119261133192110"><a name="en-us_topic_0147658916_p119261133192110"></a><a name="en-us_topic_0147658916_p119261133192110"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p189291933142116"><a name="en-us_topic_0147658916_p189291933142116"></a><a name="en-us_topic_0147658916_p189291933142116"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p493213315214"><a name="en-us_topic_0147658916_p493213315214"></a><a name="en-us_topic_0147658916_p493213315214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p29351333192112"><a name="en-us_topic_0147658916_p29351333192112"></a><a name="en-us_topic_0147658916_p29351333192112"></a>Username</p>
    </td>
    </tr>
    <tr id="en-us_topic_0147658916_row193643316211"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p1393815334212"><a name="en-us_topic_0147658916_p1393815334212"></a><a name="en-us_topic_0147658916_p1393815334212"></a>password_expires_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p1194143312119"><a name="en-us_topic_0147658916_p1194143312119"></a><a name="en-us_topic_0147658916_p1194143312119"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p18943633142112"><a name="en-us_topic_0147658916_p18943633142112"></a><a name="en-us_topic_0147658916_p18943633142112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p294619332218"><a name="en-us_topic_0147658916_p294619332218"></a><a name="en-us_topic_0147658916_p294619332218"></a>UTC time when the password will expire. <strong id="b177491551105718"><a name="b177491551105718"></a><a name="b177491551105718"></a>null</strong> indicates that the password has unlimited validity.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0147658916_row294912331214"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p17951143302120"><a name="en-us_topic_0147658916_p17951143302120"></a><a name="en-us_topic_0147658916_p17951143302120"></a>pwd_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p11955533102116"><a name="en-us_topic_0147658916_p11955533102116"></a><a name="en-us_topic_0147658916_p11955533102116"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p29573333214"><a name="en-us_topic_0147658916_p29573333214"></a><a name="en-us_topic_0147658916_p29573333214"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p09601033172120"><a name="en-us_topic_0147658916_p09601033172120"></a><a name="en-us_topic_0147658916_p09601033172120"></a>Password status. <strong id="b355111133319"><a name="b355111133319"></a><a name="b355111133319"></a>true</strong> means that the password needs to be changed, and <strong id="b11550112333"><a name="b11550112333"></a><a name="b11550112333"></a>false</strong> means that the password is normal.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0147658916_row496283313218"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p179691433202117"><a name="en-us_topic_0147658916_p179691433202117"></a><a name="en-us_topic_0147658916_p179691433202117"></a>pwd_strength</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p15972333142118"><a name="en-us_topic_0147658916_p15972333142118"></a><a name="en-us_topic_0147658916_p15972333142118"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p14974113312218"><a name="en-us_topic_0147658916_p14974113312218"></a><a name="en-us_topic_0147658916_p14974113312218"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p69781233112115"><a name="en-us_topic_0147658916_p69781233112115"></a><a name="en-us_topic_0147658916_p69781233112115"></a>Password strength. The value can be <strong id="b153847174517"><a name="b153847174517"></a><a name="b153847174517"></a>high</strong>, <strong id="b8634162184518"><a name="b8634162184518"></a><a name="b8634162184518"></a>mid</strong>, or <strong id="b107749304513"><a name="b107749304513"></a><a name="b107749304513"></a>low</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0147658916_row3979173362110"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p16982433112119"><a name="en-us_topic_0147658916_p16982433112119"></a><a name="en-us_topic_0147658916_p16982433112119"></a>mobile</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p179855333218"><a name="en-us_topic_0147658916_p179855333218"></a><a name="en-us_topic_0147658916_p179855333218"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p1198913337219"><a name="en-us_topic_0147658916_p1198913337219"></a><a name="en-us_topic_0147658916_p1198913337219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p299293302113"><a name="en-us_topic_0147658916_p299293302113"></a><a name="en-us_topic_0147658916_p299293302113"></a>Mobile number of the user.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0147658916_row12993103382113"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p89961133152119"><a name="en-us_topic_0147658916_p89961133152119"></a><a name="en-us_topic_0147658916_p89961133152119"></a>email</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p159991333132113"><a name="en-us_topic_0147658916_p159991333132113"></a><a name="en-us_topic_0147658916_p159991333132113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p82153416214"><a name="en-us_topic_0147658916_p82153416214"></a><a name="en-us_topic_0147658916_p82153416214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p94153412215"><a name="en-us_topic_0147658916_p94153412215"></a><a name="en-us_topic_0147658916_p94153412215"></a>Email address of the user.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0147658916_row1851134102111"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p1671834142117"><a name="en-us_topic_0147658916_p1671834142117"></a><a name="en-us_topic_0147658916_p1671834142117"></a>forceResetPwd</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p2101534142113"><a name="en-us_topic_0147658916_p2101534142113"></a><a name="en-us_topic_0147658916_p2101534142113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p1412133452113"><a name="en-us_topic_0147658916_p1412133452113"></a><a name="en-us_topic_0147658916_p1412133452113"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p1015173472110"><a name="en-us_topic_0147658916_p1015173472110"></a><a name="en-us_topic_0147658916_p1015173472110"></a>Indicates whether password reset is required at the next login.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0147658916_row1161234152117"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p519173417211"><a name="en-us_topic_0147658916_p519173417211"></a><a name="en-us_topic_0147658916_p519173417211"></a>default_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p18213344218"><a name="en-us_topic_0147658916_p18213344218"></a><a name="en-us_topic_0147658916_p18213344218"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p423193420211"><a name="en-us_topic_0147658916_p423193420211"></a><a name="en-us_topic_0147658916_p423193420211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p1925143462116"><a name="en-us_topic_0147658916_p1925143462116"></a><a name="en-us_topic_0147658916_p1925143462116"></a>ID of the project that is displayed by default when the user logs in to the console.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0147658916_row9263348215"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0147658916_p1330334112110"><a name="en-us_topic_0147658916_p1330334112110"></a><a name="en-us_topic_0147658916_p1330334112110"></a>last_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0147658916_p1232193418212"><a name="en-us_topic_0147658916_p1232193418212"></a><a name="en-us_topic_0147658916_p1232193418212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0147658916_p17361734142110"><a name="en-us_topic_0147658916_p17361734142110"></a><a name="en-us_topic_0147658916_p17361734142110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0147658916_p203843472112"><a name="en-us_topic_0147658916_p203843472112"></a><a name="en-us_topic_0147658916_p203843472112"></a>ID of the project that the user lastly accessed before exiting the system.</p>
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
<table><thead align="left"><tr id="en-us_topic_0035544336_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035544336_p51565323"><a name="en-us_topic_0035544336_p51565323"></a><a name="en-us_topic_0035544336_p51565323"></a><strong id="b1994117617299"><a name="b1994117617299"></a><a name="b1994117617299"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035544336_p16041657"><a name="en-us_topic_0035544336_p16041657"></a><a name="en-us_topic_0035544336_p16041657"></a><strong id="b4160312517299"><a name="b4160312517299"></a><a name="b4160312517299"></a>Description</strong></p>
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

