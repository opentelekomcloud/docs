# Querying a User Project List<a name="en-us_topic_0057845622"></a>

## Function Description<a name="s5888597838b0425a92e3419fb766c7f5"></a>

This interface is used to query the project list of a specified user.

## URI<a name="s46d3616bd4c54e55ba97a528518a5890"></a>

-   URI format

    GET /v3/users/\{user\_id\}/projects

-   URI parameter description

    <a name="table1690112711746"></a>
    <table><thead align="left"><tr id="row1180244311746"><th class="cellrowborder" valign="top" width="24.80751924807519%" id="mcps1.1.5.1.1"><p id="p5931366311746"><a name="p5931366311746"></a><a name="p5931366311746"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.437456254374563%" id="mcps1.1.5.1.2"><p id="p5975008711746"><a name="p5975008711746"></a><a name="p5975008711746"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.817518248175183%" id="mcps1.1.5.1.3"><p id="p3744864411746"><a name="p3744864411746"></a><a name="p3744864411746"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.937506249375062%" id="mcps1.1.5.1.4"><p id="p1500648611746"><a name="p1500648611746"></a><a name="p1500648611746"></a><strong id="b842352706114032"><a name="b842352706114032"></a><a name="b842352706114032"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row885731011746"><td class="cellrowborder" valign="top" width="24.80751924807519%" headers="mcps1.1.5.1.1 "><p id="p6364498611746"><a name="p6364498611746"></a><a name="p6364498611746"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.437456254374563%" headers="mcps1.1.5.1.2 "><p id="p2340461911746"><a name="p2340461911746"></a><a name="p2340461911746"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.817518248175183%" headers="mcps1.1.5.1.3 "><p id="p1262955411746"><a name="p1262955411746"></a><a name="p1262955411746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.937506249375062%" headers="mcps1.1.5.1.4 "><p id="p5016602911746"><a name="p5016602911746"></a><a name="p5016602911746"></a>User ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="se7fe5cac0d544e119c49322cc1707eb6"></a>

-   Request header parameter description

    <a name="t68c7bd10e66a4380a1e6cdc78ca95669"></a>
    <table><thead align="left"><tr id="r584496594a404ce18918a40e6e57c2ec"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="ac3a989cc5d3a405889eabb47dee84b04"><a name="ac3a989cc5d3a405889eabb47dee84b04"></a><a name="ac3a989cc5d3a405889eabb47dee84b04"></a><strong id="b37071144173012"><a name="b37071144173012"></a><a name="b37071144173012"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="a69a20ac00b86496aa8418517c542b0da"><a name="a69a20ac00b86496aa8418517c542b0da"></a><a name="a69a20ac00b86496aa8418517c542b0da"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="a92c23d4441054df0972e025aeb3a8d7f"><a name="a92c23d4441054df0972e025aeb3a8d7f"></a><a name="a92c23d4441054df0972e025aeb3a8d7f"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="abe6882c44cf4402d8ed7706b9278f33b"><a name="abe6882c44cf4402d8ed7706b9278f33b"></a><a name="abe6882c44cf4402d8ed7706b9278f33b"></a><strong id="b59476291173012"><a name="b59476291173012"></a><a name="b59476291173012"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r5d63069d6a8a426e8b25b94d1b4d302a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="ad4fb6253385c46ab8720a0e13f573694"><a name="ad4fb6253385c46ab8720a0e13f573694"></a><a name="ad4fb6253385c46ab8720a0e13f573694"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="a6b33800bcb2a446695b1d33a2d751554"><a name="a6b33800bcb2a446695b1d33a2d751554"></a><a name="a6b33800bcb2a446695b1d33a2d751554"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="ab34a5e95b76b4b79a72da0734025f211"><a name="ab34a5e95b76b4b79a72da0734025f211"></a><a name="ab34a5e95b76b4b79a72da0734025f211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="a716277ae541d4553bb10490f9c02593d"><a name="a716277ae541d4553bb10490f9c02593d"></a><a name="a716277ae541d4553bb10490f9c02593d"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row29501427115257"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p6637478211538"><a name="p6637478211538"></a><a name="p6637478211538"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p764826811538"><a name="p764826811538"></a><a name="p764826811538"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p1553001111538"><a name="p1553001111538"></a><a name="p1553001111538"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p45468619174958"><a name="p45468619174958"></a><a name="p45468619174958"></a>Authenticated token with the <strong id="b4964525615147"><a name="b4964525615147"></a><a name="b4964525615147"></a>Security Administrator</strong> permission or token of the user.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://172.30.48.86:31943/v3/users/43cbe5e77aaf4665bbb962062dc1fc9d/projects
    ```


## Response<a name="s3a08e13bb5b34dc2ba4dcd84a0d51cf5"></a>

-   Response body parameter description

    <a name="t1266dd240c3649048c9f42af34a0686b"></a>
    <table><thead align="left"><tr id="rd8ac2cd80e4b47d684b61df4f3c570cf"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="ad167d1bf89ca443eac693ea562da12a3"><a name="ad167d1bf89ca443eac693ea562da12a3"></a><a name="ad167d1bf89ca443eac693ea562da12a3"></a><strong id="b1789753173012"><a name="b1789753173012"></a><a name="b1789753173012"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="aad08ea1f8c8e4a42a1a81112a74cb237"><a name="aad08ea1f8c8e4a42a1a81112a74cb237"></a><a name="aad08ea1f8c8e4a42a1a81112a74cb237"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="a9b5fafff0348408893dcc06fbe0b1186"><a name="a9b5fafff0348408893dcc06fbe0b1186"></a><a name="a9b5fafff0348408893dcc06fbe0b1186"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="ad002a0bf107a468884a5777e55f837f6"><a name="ad002a0bf107a468884a5777e55f837f6"></a><a name="ad002a0bf107a468884a5777e55f837f6"></a><strong id="b24920709173012"><a name="b24920709173012"></a><a name="b24920709173012"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="ref3b81e8e64e418c961ca1bce6f25280"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="abb2b4d81b907497da50ad4f12760f7dc"><a name="abb2b4d81b907497da50ad4f12760f7dc"></a><a name="abb2b4d81b907497da50ad4f12760f7dc"></a>projects</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="a7e49a4eaca054e36ba774b0cdc492081"><a name="a7e49a4eaca054e36ba774b0cdc492081"></a><a name="a7e49a4eaca054e36ba774b0cdc492081"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="af41e29e0e266400c900609efde3aaf39"><a name="af41e29e0e266400c900609efde3aaf39"></a><a name="af41e29e0e266400c900609efde3aaf39"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="a8ded0409c6d948dc82f7f779a4cfa5b8"><a name="a8ded0409c6d948dc82f7f779a4cfa5b8"></a><a name="a8ded0409c6d948dc82f7f779a4cfa5b8"></a>List of projects.</p>
    </td>
    </tr>
    <tr id="row64217163172552"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p34207706172552"><a name="p34207706172552"></a><a name="p34207706172552"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p19360826172552"><a name="p19360826172552"></a><a name="p19360826172552"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p24723091172552"><a name="p24723091172552"></a><a name="p24723091172552"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p56413324172552"><a name="p56413324172552"></a><a name="p56413324172552"></a>Resource links of a project.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the project format

    <a name="t3ef10d134105438f922a72ac36adbe13"></a>
    <table><thead align="left"><tr id="ra836795da3204436ad115c6d63f33cb3"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="a915f4fa2492a4fa3b5fc5b52cb975ed3"><a name="a915f4fa2492a4fa3b5fc5b52cb975ed3"></a><a name="a915f4fa2492a4fa3b5fc5b52cb975ed3"></a><strong id="b24591867173012"><a name="b24591867173012"></a><a name="b24591867173012"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="aeb29128c8bc6489593aaf12297635c52"><a name="aeb29128c8bc6489593aaf12297635c52"></a><a name="aeb29128c8bc6489593aaf12297635c52"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_7"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.11%" id="mcps1.1.5.1.3"><p id="a367df15999ce47aa8fa2550bb2d3df9a"><a name="a367df15999ce47aa8fa2550bb2d3df9a"></a><a name="a367df15999ce47aa8fa2550bb2d3df9a"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_7"><a name="a703d34a49a2f4162bc1a1a439f655f95_7"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.89%" id="mcps1.1.5.1.4"><p id="a16a6b7e4145e4fbabf25e75163ec3f95"><a name="a16a6b7e4145e4fbabf25e75163ec3f95"></a><a name="a16a6b7e4145e4fbabf25e75163ec3f95"></a><strong id="b54537216173012"><a name="b54537216173012"></a><a name="b54537216173012"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rb2ba995189ec478eb5d1181d3bb7be1c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="aa1005da54f2c4746ae99676d14ab012d"><a name="aa1005da54f2c4746ae99676d14ab012d"></a><a name="aa1005da54f2c4746ae99676d14ab012d"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="a6d0540b177e34775b18c670cf5cd46bc"><a name="a6d0540b177e34775b18c670cf5cd46bc"></a><a name="a6d0540b177e34775b18c670cf5cd46bc"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="a65f6a6fc5a364d868072c58eeab90325"><a name="a65f6a6fc5a364d868072c58eeab90325"></a><a name="a65f6a6fc5a364d868072c58eeab90325"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="ababe5d21d4764e209d225a4cea9b9fa2"><a name="ababe5d21d4764e209d225a4cea9b9fa2"></a><a name="ababe5d21d4764e209d225a4cea9b9fa2"></a>Project description.</p>
    </td>
    </tr>
    <tr id="r41522dc2bd8d475b8d2a16af17d5213b"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="a2501c5b12ff94e338c0930e6c321af90"><a name="a2501c5b12ff94e338c0930e6c321af90"></a><a name="a2501c5b12ff94e338c0930e6c321af90"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="af10224f581d946cb91a49683adf34271"><a name="af10224f581d946cb91a49683adf34271"></a><a name="af10224f581d946cb91a49683adf34271"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="a0316e95fb756489a82f70ae562c523b4"><a name="a0316e95fb756489a82f70ae562c523b4"></a><a name="a0316e95fb756489a82f70ae562c523b4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="af5ce8c5c520f468895f28d74f6eb4540"><a name="af5ce8c5c520f468895f28d74f6eb4540"></a><a name="af5ce8c5c520f468895f28d74f6eb4540"></a>Project ID.</p>
    </td>
    </tr>
    <tr id="r1208cbb1496440d89eb758b2cd80d578"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="a4504807eb899465fb0ce3ac82d7013dc"><a name="a4504807eb899465fb0ce3ac82d7013dc"></a><a name="a4504807eb899465fb0ce3ac82d7013dc"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0026585113_p386591205643"><a name="en-us_topic_0026585113_p386591205643"></a><a name="en-us_topic_0026585113_p386591205643"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="a293aacc9b5354786a8b30a063a186b02"><a name="a293aacc9b5354786a8b30a063a186b02"></a><a name="a293aacc9b5354786a8b30a063a186b02"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="aa1138dcdd40340039e621e7abf0332e1"><a name="aa1138dcdd40340039e621e7abf0332e1"></a><a name="aa1138dcdd40340039e621e7abf0332e1"></a>ID of the domain where a project is located.</p>
    </td>
    </tr>
    <tr id="rbe8775b4e77a4b08be093de05e7bcbf3"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="acc4c499e1b2f4bdd98e5c7acd4e8861b"><a name="acc4c499e1b2f4bdd98e5c7acd4e8861b"></a><a name="acc4c499e1b2f4bdd98e5c7acd4e8861b"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="a4bf5dfe715d342e0a883343cbcf8181a"><a name="a4bf5dfe715d342e0a883343cbcf8181a"></a><a name="a4bf5dfe715d342e0a883343cbcf8181a"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="a8c424bac7d93444dbc647a1d5c5c21e4"><a name="a8c424bac7d93444dbc647a1d5c5c21e4"></a><a name="a8c424bac7d93444dbc647a1d5c5c21e4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="afc48731c8a2e4c66a56ac245f7a1e34e"><a name="afc48731c8a2e4c66a56ac245f7a1e34e"></a><a name="afc48731c8a2e4c66a56ac245f7a1e34e"></a>Project name.</p>
    </td>
    </tr>
    <tr id="row884150412952"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p4507320312952"><a name="p4507320312952"></a><a name="p4507320312952"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p2705079812952"><a name="p2705079812952"></a><a name="p2705079812952"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p4363103412952"><a name="p4363103412952"></a><a name="p4363103412952"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="p4445286212952"><a name="p4445286212952"></a><a name="p4445286212952"></a>Resource links of a project.</p>
    </td>
    </tr>
    <tr id="row19356972201441"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p29605601201441"><a name="p29605601201441"></a><a name="p29605601201441"></a>is_domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p21596807201441"><a name="p21596807201441"></a><a name="p21596807201441"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p39263216201441"><a name="p39263216201441"></a><a name="p39263216201441"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="p59347844201441"><a name="p59347844201441"></a><a name="p59347844201441"></a>Is domain or not.</p>
    </td>
    </tr>
    <tr id="row46028278201453"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p27327398201453"><a name="p27327398201453"></a><a name="p27327398201453"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p1690706201453"><a name="p1690706201453"></a><a name="p1690706201453"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p57286369201453"><a name="p57286369201453"></a><a name="p57286369201453"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="p30534075201453"><a name="p30534075201453"></a><a name="p30534075201453"></a>Whether a project is available.</p>
    </td>
    </tr>
    <tr id="row14242324201510"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p35305259201510"><a name="p35305259201510"></a><a name="p35305259201510"></a>parent_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p17738677201510"><a name="p17738677201510"></a><a name="p17738677201510"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p53557531201510"><a name="p53557531201510"></a><a name="p53557531201510"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="p62242884201510"><a name="p62242884201510"></a><a name="p62242884201510"></a>Parent ID of the project.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample response

    ```
    {
      "links": {
        "self": "www.example.com/v3/auth/projects",
        "previous": null,
        "next": null
      },
      "projects": [
        {
          "is_domain": false,
          "description": "",
          "links": {
            "self": "www.example.com/v3/projects/9041929bcc6e4bfe85add4e7b96ffdd7"
          },
          "enabled": true,
          "id": "9041929bcc6e4bfe85add4e7b96ffdd7",
          "parent_id": "398998b5392f4150ad48fe456d6de4f1",
          "domain_id": "398998b5392f4150ad48fe456d6de4f1",
          "name": "region_name"
        },
        {
          "is_domain": false,
          "description": "",
          "links": {
            "self": "www.example.com/v3/projects/ee65ca70d3cf43aaa1ea6492ce15f289"
          },
          "enabled": true,
          "id": "ee65ca70d3cf43aaa1ea6492ce15f289",
          "parent_id": "398998b5392f4150ad48fe456d6de4f1",
          "domain_id": "398998b5392f4150ad48fe456d6de4f1",
          "name": "MOS"   //Default project name of OBS
        }
      ]
    }
    ```


## Status Codes<a name="section29181700172949"></a>

<a name="en-us_topic_0035544336_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0035544336_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035544336_p51565323"><a name="en-us_topic_0035544336_p51565323"></a><a name="en-us_topic_0035544336_p51565323"></a><strong id="b59755198173012"><a name="b59755198173012"></a><a name="b59755198173012"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035544336_p16041657"><a name="en-us_topic_0035544336_p16041657"></a><a name="en-us_topic_0035544336_p16041657"></a><strong id="b7886949173012"><a name="b7886949173012"></a><a name="b7886949173012"></a>Description</strong></p>
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

