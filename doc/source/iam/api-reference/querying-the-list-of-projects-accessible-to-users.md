# Querying the List of Projects Accessible to Users<a name="en-us_topic_0057845558"></a>

## Function Description<a name="section37234380165120"></a>

This interface is used to query the list of projects accessible to users.

## URI<a name="section61801097192146"></a>

URI format

GET /v3/auth/projects

## Request<a name="section63890395165120"></a>

-   Request header parameter description

    <a name="table6220953919369"></a>
    <table><thead align="left"><tr id="row5697606319369"><th class="cellrowborder" valign="top" width="22.88%" id="mcps1.1.5.1.1"><p id="p5527391819369"><a name="p5527391819369"></a><a name="p5527391819369"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.81%" id="mcps1.1.5.1.2"><p id="p4800235119369"><a name="p4800235119369"></a><a name="p4800235119369"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.48%" id="mcps1.1.5.1.3"><p id="p6298525419369"><a name="p6298525419369"></a><a name="p6298525419369"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.83%" id="mcps1.1.5.1.4"><p id="p153191219369"><a name="p153191219369"></a><a name="p153191219369"></a><strong id="a76acf34e8e7b48948763ec1b460ad92f"><a name="a76acf34e8e7b48948763ec1b460ad92f"></a><a name="a76acf34e8e7b48948763ec1b460ad92f"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61263798114243"><td class="cellrowborder" valign="top" width="22.88%" headers="mcps1.1.5.1.1 "><p id="p3477825114246"><a name="p3477825114246"></a><a name="p3477825114246"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.81%" headers="mcps1.1.5.1.2 "><p id="p13268390114246"><a name="p13268390114246"></a><a name="p13268390114246"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.48%" headers="mcps1.1.5.1.3 "><p id="p997820114246"><a name="p997820114246"></a><a name="p997820114246"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.83%" headers="mcps1.1.5.1.4 "><p id="p13714602114246"><a name="p13714602114246"></a><a name="p13714602114246"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row1297318319369"><td class="cellrowborder" valign="top" width="22.88%" headers="mcps1.1.5.1.1 "><p id="p5165841919369"><a name="p5165841919369"></a><a name="p5165841919369"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.81%" headers="mcps1.1.5.1.2 "><p id="p2358241119369"><a name="p2358241119369"></a><a name="p2358241119369"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.48%" headers="mcps1.1.5.1.3 "><p id="p3112715219369"><a name="p3112715219369"></a><a name="p3112715219369"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.83%" headers="mcps1.1.5.1.4 "><p id="p3310810221217"><a name="p3310810221217"></a><a name="p3310810221217"></a>An authenticated token of the user.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET /v3/auth/projects
    ```


## Response<a name="section23133376165120"></a>

-   Response body parameter description

    <a name="table61864177165120"></a>
    <table><thead align="left"><tr id="row53394193165120"><th class="cellrowborder" valign="top" width="23.01%" id="mcps1.1.5.1.1"><p id="p29962347165120"><a name="p29962347165120"></a><a name="p29962347165120"></a><strong id="b9413284164823"><a name="b9413284164823"></a><a name="b9413284164823"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.55%" id="mcps1.1.5.1.2"><p id="p11031025165120"><a name="p11031025165120"></a><a name="p11031025165120"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.61%" id="mcps1.1.5.1.3"><p id="p21097869165120"><a name="p21097869165120"></a><a name="p21097869165120"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.83%" id="mcps1.1.5.1.4"><p id="p31205796165120"><a name="p31205796165120"></a><a name="p31205796165120"></a><strong id="b50726443164823"><a name="b50726443164823"></a><a name="b50726443164823"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44641568165120"><td class="cellrowborder" valign="top" width="23.01%" headers="mcps1.1.5.1.1 "><p id="p59197289165120"><a name="p59197289165120"></a><a name="p59197289165120"></a>projects</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.1.5.1.2 "><p id="p30251110165120"><a name="p30251110165120"></a><a name="p30251110165120"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.1.5.1.3 "><p id="p34420864165120"><a name="p34420864165120"></a><a name="p34420864165120"></a>JSONArray</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.83%" headers="mcps1.1.5.1.4 "><p id="p36626590165120"><a name="p36626590165120"></a><a name="p36626590165120"></a>List of projects.</p>
    </td>
    </tr>
    <tr id="row61203858165120"><td class="cellrowborder" valign="top" width="23.01%" headers="mcps1.1.5.1.1 "><p id="p58565490165120"><a name="p58565490165120"></a><a name="p58565490165120"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.1.5.1.2 "><p id="p46184267165120"><a name="p46184267165120"></a><a name="p46184267165120"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.1.5.1.3 "><p id="p49938116165120"><a name="p49938116165120"></a><a name="p49938116165120"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.83%" headers="mcps1.1.5.1.4 "><p id="p18455557165120"><a name="p18455557165120"></a><a name="p18455557165120"></a>Resource links of a project.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Description for the project format

    <a name="t3ef10d134105438f922a72ac36adbe13"></a>
    <table><thead align="left"><tr id="ra836795da3204436ad115c6d63f33cb3"><th class="cellrowborder" valign="top" width="22.88%" id="mcps1.1.5.1.1"><p id="a915f4fa2492a4fa3b5fc5b52cb975ed3"><a name="a915f4fa2492a4fa3b5fc5b52cb975ed3"></a><a name="a915f4fa2492a4fa3b5fc5b52cb975ed3"></a><strong id="b24591867173012"><a name="b24591867173012"></a><a name="b24591867173012"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.55%" id="mcps1.1.5.1.2"><p id="aeb29128c8bc6489593aaf12297635c52"><a name="aeb29128c8bc6489593aaf12297635c52"></a><a name="aeb29128c8bc6489593aaf12297635c52"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.68%" id="mcps1.1.5.1.3"><p id="a367df15999ce47aa8fa2550bb2d3df9a"><a name="a367df15999ce47aa8fa2550bb2d3df9a"></a><a name="a367df15999ce47aa8fa2550bb2d3df9a"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.89%" id="mcps1.1.5.1.4"><p id="a16a6b7e4145e4fbabf25e75163ec3f95"><a name="a16a6b7e4145e4fbabf25e75163ec3f95"></a><a name="a16a6b7e4145e4fbabf25e75163ec3f95"></a><strong id="b54537216173012"><a name="b54537216173012"></a><a name="b54537216173012"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rb2ba995189ec478eb5d1181d3bb7be1c"><td class="cellrowborder" valign="top" width="22.88%" headers="mcps1.1.5.1.1 "><p id="aa1005da54f2c4746ae99676d14ab012d"><a name="aa1005da54f2c4746ae99676d14ab012d"></a><a name="aa1005da54f2c4746ae99676d14ab012d"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.1.5.1.2 "><p id="a6d0540b177e34775b18c670cf5cd46bc"><a name="a6d0540b177e34775b18c670cf5cd46bc"></a><a name="a6d0540b177e34775b18c670cf5cd46bc"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.1.5.1.3 "><p id="a65f6a6fc5a364d868072c58eeab90325"><a name="a65f6a6fc5a364d868072c58eeab90325"></a><a name="a65f6a6fc5a364d868072c58eeab90325"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="ababe5d21d4764e209d225a4cea9b9fa2"><a name="ababe5d21d4764e209d225a4cea9b9fa2"></a><a name="ababe5d21d4764e209d225a4cea9b9fa2"></a>Project description.</p>
    </td>
    </tr>
    <tr id="r41522dc2bd8d475b8d2a16af17d5213b"><td class="cellrowborder" valign="top" width="22.88%" headers="mcps1.1.5.1.1 "><p id="a2501c5b12ff94e338c0930e6c321af90"><a name="a2501c5b12ff94e338c0930e6c321af90"></a><a name="a2501c5b12ff94e338c0930e6c321af90"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.1.5.1.2 "><p id="af10224f581d946cb91a49683adf34271"><a name="af10224f581d946cb91a49683adf34271"></a><a name="af10224f581d946cb91a49683adf34271"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.1.5.1.3 "><p id="a0316e95fb756489a82f70ae562c523b4"><a name="a0316e95fb756489a82f70ae562c523b4"></a><a name="a0316e95fb756489a82f70ae562c523b4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="af5ce8c5c520f468895f28d74f6eb4540"><a name="af5ce8c5c520f468895f28d74f6eb4540"></a><a name="af5ce8c5c520f468895f28d74f6eb4540"></a>ID of a project.</p>
    </td>
    </tr>
    <tr id="r1208cbb1496440d89eb758b2cd80d578"><td class="cellrowborder" valign="top" width="22.88%" headers="mcps1.1.5.1.1 "><p id="a4504807eb899465fb0ce3ac82d7013dc"><a name="a4504807eb899465fb0ce3ac82d7013dc"></a><a name="a4504807eb899465fb0ce3ac82d7013dc"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0026585113_p386591205643"><a name="en-us_topic_0026585113_p386591205643"></a><a name="en-us_topic_0026585113_p386591205643"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.1.5.1.3 "><p id="a293aacc9b5354786a8b30a063a186b02"><a name="a293aacc9b5354786a8b30a063a186b02"></a><a name="a293aacc9b5354786a8b30a063a186b02"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="aa1138dcdd40340039e621e7abf0332e1"><a name="aa1138dcdd40340039e621e7abf0332e1"></a><a name="aa1138dcdd40340039e621e7abf0332e1"></a>ID of the domain where a project is located.</p>
    </td>
    </tr>
    <tr id="rbe8775b4e77a4b08be093de05e7bcbf3"><td class="cellrowborder" valign="top" width="22.88%" headers="mcps1.1.5.1.1 "><p id="acc4c499e1b2f4bdd98e5c7acd4e8861b"><a name="acc4c499e1b2f4bdd98e5c7acd4e8861b"></a><a name="acc4c499e1b2f4bdd98e5c7acd4e8861b"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.1.5.1.2 "><p id="a4bf5dfe715d342e0a883343cbcf8181a"><a name="a4bf5dfe715d342e0a883343cbcf8181a"></a><a name="a4bf5dfe715d342e0a883343cbcf8181a"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.1.5.1.3 "><p id="a8c424bac7d93444dbc647a1d5c5c21e4"><a name="a8c424bac7d93444dbc647a1d5c5c21e4"></a><a name="a8c424bac7d93444dbc647a1d5c5c21e4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="afc48731c8a2e4c66a56ac245f7a1e34e"><a name="afc48731c8a2e4c66a56ac245f7a1e34e"></a><a name="afc48731c8a2e4c66a56ac245f7a1e34e"></a>Project name.</p>
    </td>
    </tr>
    <tr id="row884150412952"><td class="cellrowborder" valign="top" width="22.88%" headers="mcps1.1.5.1.1 "><p id="p4507320312952"><a name="p4507320312952"></a><a name="p4507320312952"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.1.5.1.2 "><p id="p2705079812952"><a name="p2705079812952"></a><a name="p2705079812952"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.1.5.1.3 "><p id="p4363103412952"><a name="p4363103412952"></a><a name="p4363103412952"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="p4445286212952"><a name="p4445286212952"></a><a name="p4445286212952"></a>Resource links of a project.</p>
    </td>
    </tr>
    <tr id="row19356972201441"><td class="cellrowborder" valign="top" width="22.88%" headers="mcps1.1.5.1.1 "><p id="p29605601201441"><a name="p29605601201441"></a><a name="p29605601201441"></a>is_domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.1.5.1.2 "><p id="p21596807201441"><a name="p21596807201441"></a><a name="p21596807201441"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.1.5.1.3 "><p id="p39263216201441"><a name="p39263216201441"></a><a name="p39263216201441"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="p59347844201441"><a name="p59347844201441"></a><a name="p59347844201441"></a>Is domain or not.</p>
    </td>
    </tr>
    <tr id="row46028278201453"><td class="cellrowborder" valign="top" width="22.88%" headers="mcps1.1.5.1.1 "><p id="p27327398201453"><a name="p27327398201453"></a><a name="p27327398201453"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.1.5.1.2 "><p id="p1690706201453"><a name="p1690706201453"></a><a name="p1690706201453"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.1.5.1.3 "><p id="p57286369201453"><a name="p57286369201453"></a><a name="p57286369201453"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.1.5.1.4 "><p id="p30534075201453"><a name="p30534075201453"></a><a name="p30534075201453"></a>Whether a project is available.</p>
    </td>
    </tr>
    <tr id="row14242324201510"><td class="cellrowborder" valign="top" width="22.88%" headers="mcps1.1.5.1.1 "><p id="p35305259201510"><a name="p35305259201510"></a><a name="p35305259201510"></a>parent_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.1.5.1.2 "><p id="p17738677201510"><a name="p17738677201510"></a><a name="p17738677201510"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.1.5.1.3 "><p id="p53557531201510"><a name="p53557531201510"></a><a name="p53557531201510"></a>String</p>
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
          "name": "region"
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
          "name": "{project_name}"
        }
      ]
    }
    ```


## Status Codes<a name="section58962517165120"></a>

<a name="table11234582165120"></a>
<table><thead align="left"><tr id="row19742440165120"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p55633806165120"><a name="p55633806165120"></a><a name="p55633806165120"></a><strong id="b84235270618317"><a name="b84235270618317"></a><a name="b84235270618317"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p10044408165120"><a name="p10044408165120"></a><a name="p10044408165120"></a><strong id="b15670140164823"><a name="b15670140164823"></a><a name="b15670140164823"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row8290702165120"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p458298165120"><a name="p458298165120"></a><a name="p458298165120"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p37122145165120"><a name="p37122145165120"></a><a name="p37122145165120"></a>The request is successful.</p>
</td>
</tr>
<tr id="row65663855165120"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p17172061165120"><a name="p17172061165120"></a><a name="p17172061165120"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p48759675165120"><a name="p48759675165120"></a><a name="p48759675165120"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row36183891165120"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p45214077165120"><a name="p45214077165120"></a><a name="p45214077165120"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p38461611165120"><a name="p38461611165120"></a><a name="p38461611165120"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row10610183165120"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p54118519165120"><a name="p54118519165120"></a><a name="p54118519165120"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p21523936165120"><a name="p21523936165120"></a><a name="p21523936165120"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row59497697165120"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p54584113165120"><a name="p54584113165120"></a><a name="p54584113165120"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p59237005165120"><a name="p59237005165120"></a><a name="p59237005165120"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row63371004165120"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p32777686165120"><a name="p32777686165120"></a><a name="p32777686165120"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p37746929165120"><a name="p37746929165120"></a><a name="p37746929165120"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row4178046165120"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2877469165120"><a name="p2877469165120"></a><a name="p2877469165120"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p31748432165120"><a name="p31748432165120"></a><a name="p31748432165120"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row17300437165120"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p59158146165120"><a name="p59158146165120"></a><a name="p59158146165120"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p27080503165120"><a name="p27080503165120"></a><a name="p27080503165120"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

