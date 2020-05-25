# Querying Information and Status of a Specified Project<a name="en-us_topic_0079466135"></a>

## Function Description<a name="section18319181453614"></a>

This interface is used to query details about a specified project, including the project status.

## URI<a name="section1032051453615"></a>

-   URI format

    GET /v3-ext/projects/\{project\_id\}


-   URI parameter description

    <a name="table1532018142366"></a>
    <table><thead align="left"><tr id="row103201149368"><th class="cellrowborder" valign="top" width="19.17%" id="mcps1.1.5.1.1"><p id="p1932041417367"><a name="p1932041417367"></a><a name="p1932041417367"></a><strong id="aa8facb3d00804940b0eeff8a3856d83c"><a name="aa8facb3d00804940b0eeff8a3856d83c"></a><a name="aa8facb3d00804940b0eeff8a3856d83c"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.84%" id="mcps1.1.5.1.2"><p id="p1232071411368"><a name="p1232071411368"></a><a name="p1232071411368"></a><strong id="a5e64fa141cf14e14991ed8d6cda54ff2"><a name="a5e64fa141cf14e14991ed8d6cda54ff2"></a><a name="a5e64fa141cf14e14991ed8d6cda54ff2"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.12%" id="mcps1.1.5.1.3"><p id="p832051411369"><a name="p832051411369"></a><a name="p832051411369"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.87%" id="mcps1.1.5.1.4"><p id="p2320191423611"><a name="p2320191423611"></a><a name="p2320191423611"></a><strong id="b20601766145329_1"><a name="b20601766145329_1"></a><a name="b20601766145329_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row183201814193615"><td class="cellrowborder" valign="top" width="19.17%" headers="mcps1.1.5.1.1 "><p id="p432071415365"><a name="p432071415365"></a><a name="p432071415365"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.5.1.2 "><p id="p83202014163620"><a name="p83202014163620"></a><a name="p83202014163620"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.12%" headers="mcps1.1.5.1.3 "><p id="p3320161415362"><a name="p3320161415362"></a><a name="p3320161415362"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87%" headers="mcps1.1.5.1.4 "><p id="p332091410362"><a name="p332091410362"></a><a name="p332091410362"></a>Project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="section132251415368"></a>

-   Request header parameter description

    <a name="table3322161493613"></a>
    <table><thead align="left"><tr id="row11322131413615"><th class="cellrowborder" valign="top" width="19.29%" id="mcps1.1.5.1.1"><p id="p1432218149369"><a name="p1432218149369"></a><a name="p1432218149369"></a><strong id="b557420963"><a name="b557420963"></a><a name="b557420963"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.52%" id="mcps1.1.5.1.2"><p id="p8322161443614"><a name="p8322161443614"></a><a name="p8322161443614"></a><strong id="b1028464529"><a name="b1028464529"></a><a name="b1028464529"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.82%" id="mcps1.1.5.1.3"><p id="p19322111433620"><a name="p19322111433620"></a><a name="p19322111433620"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.37%" id="mcps1.1.5.1.4"><p id="p73221614143617"><a name="p73221614143617"></a><a name="p73221614143617"></a><strong id="b20601766145329_3"><a name="b20601766145329_3"></a><a name="b20601766145329_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row113221514113620"><td class="cellrowborder" valign="top" width="19.29%" headers="mcps1.1.5.1.1 "><p id="p123221314183616"><a name="p123221314183616"></a><a name="p123221314183616"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.52%" headers="mcps1.1.5.1.2 "><p id="p15322181419363"><a name="p15322181419363"></a><a name="p15322181419363"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82%" headers="mcps1.1.5.1.3 "><p id="p432215149367"><a name="p432215149367"></a><a name="p432215149367"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.1.5.1.4 "><p id="p1332281419368"><a name="p1332281419368"></a><a name="p1332281419368"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row1332261493613"><td class="cellrowborder" valign="top" width="19.29%" headers="mcps1.1.5.1.1 "><p id="p113221814143614"><a name="p113221814143614"></a><a name="p113221814143614"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.52%" headers="mcps1.1.5.1.2 "><p id="p8322714173618"><a name="p8322714173618"></a><a name="p8322714173618"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82%" headers="mcps1.1.5.1.3 "><p id="p1322014123615"><a name="p1322014123615"></a><a name="p1322014123615"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.1.5.1.4 "><p id="p5300989191815"><a name="p5300989191815"></a><a name="p5300989191815"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -X "X-Auth-Token:$token" -X GET https://10.145.93.56:31943/v3-ext/projects/5c9f5525d9d24c5bbf91e74d86772029
    ```


## **Response**<a name="section1732319140365"></a>

-   Response body parameter description

    <a name="table61864177165120"></a>
    <table><thead align="left"><tr id="row53394193165120"><th class="cellrowborder" valign="top" width="19.428057194280573%" id="mcps1.1.5.1.1"><p id="p29962347165120"><a name="p29962347165120"></a><a name="p29962347165120"></a><strong id="b2103509817"><a name="b2103509817"></a><a name="b2103509817"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.62813718628137%" id="mcps1.1.5.1.2"><p id="p11031025165120"><a name="p11031025165120"></a><a name="p11031025165120"></a><strong id="b1803197689"><a name="b1803197689"></a><a name="b1803197689"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.568243175682433%" id="mcps1.1.5.1.3"><p id="p21097869165120"><a name="p21097869165120"></a><a name="p21097869165120"></a><strong id="b842352706143526_5"><a name="b842352706143526_5"></a><a name="b842352706143526_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.375562443755626%" id="mcps1.1.5.1.4"><p id="p31205796165120"><a name="p31205796165120"></a><a name="p31205796165120"></a><strong id="b20601766145329_5"><a name="b20601766145329_5"></a><a name="b20601766145329_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44641568165120"><td class="cellrowborder" valign="top" width="19.428057194280573%" headers="mcps1.1.5.1.1 "><p id="p59197289165120"><a name="p59197289165120"></a><a name="p59197289165120"></a>project</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.62813718628137%" headers="mcps1.1.5.1.2 "><p id="p30251110165120"><a name="p30251110165120"></a><a name="p30251110165120"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.568243175682433%" headers="mcps1.1.5.1.3 "><p id="p34420864165120"><a name="p34420864165120"></a><a name="p34420864165120"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.375562443755626%" headers="mcps1.1.5.1.4 "><p id="p36626590165120"><a name="p36626590165120"></a><a name="p36626590165120"></a>Project information.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Description for the project format

    <a name="t3ef10d134105438f922a72ac36adbe13"></a>
    <table><thead align="left"><tr id="ra836795da3204436ad115c6d63f33cb3"><th class="cellrowborder" valign="top" width="19.43%" id="mcps1.1.5.1.1"><p id="a915f4fa2492a4fa3b5fc5b52cb975ed3"><a name="a915f4fa2492a4fa3b5fc5b52cb975ed3"></a><a name="a915f4fa2492a4fa3b5fc5b52cb975ed3"></a><strong id="b1431627538"><a name="b1431627538"></a><a name="b1431627538"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.63%" id="mcps1.1.5.1.2"><p id="aeb29128c8bc6489593aaf12297635c52"><a name="aeb29128c8bc6489593aaf12297635c52"></a><a name="aeb29128c8bc6489593aaf12297635c52"></a><strong id="b526360164"><a name="b526360164"></a><a name="b526360164"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.77%" id="mcps1.1.5.1.3"><p id="a367df15999ce47aa8fa2550bb2d3df9a"><a name="a367df15999ce47aa8fa2550bb2d3df9a"></a><a name="a367df15999ce47aa8fa2550bb2d3df9a"></a><strong id="b842352706143526_7"><a name="b842352706143526_7"></a><a name="b842352706143526_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.17%" id="mcps1.1.5.1.4"><p id="a16a6b7e4145e4fbabf25e75163ec3f95"><a name="a16a6b7e4145e4fbabf25e75163ec3f95"></a><a name="a16a6b7e4145e4fbabf25e75163ec3f95"></a><strong id="b20601766145329_7"><a name="b20601766145329_7"></a><a name="b20601766145329_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rb2ba995189ec478eb5d1181d3bb7be1c"><td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.1 "><p id="aa1005da54f2c4746ae99676d14ab012d"><a name="aa1005da54f2c4746ae99676d14ab012d"></a><a name="aa1005da54f2c4746ae99676d14ab012d"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.2 "><p id="a6d0540b177e34775b18c670cf5cd46bc"><a name="a6d0540b177e34775b18c670cf5cd46bc"></a><a name="a6d0540b177e34775b18c670cf5cd46bc"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.1.5.1.3 "><p id="a65f6a6fc5a364d868072c58eeab90325"><a name="a65f6a6fc5a364d868072c58eeab90325"></a><a name="a65f6a6fc5a364d868072c58eeab90325"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.5.1.4 "><p id="ababe5d21d4764e209d225a4cea9b9fa2"><a name="ababe5d21d4764e209d225a4cea9b9fa2"></a><a name="ababe5d21d4764e209d225a4cea9b9fa2"></a>Project description.</p>
    </td>
    </tr>
    <tr id="r41522dc2bd8d475b8d2a16af17d5213b"><td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.1 "><p id="a2501c5b12ff94e338c0930e6c321af90"><a name="a2501c5b12ff94e338c0930e6c321af90"></a><a name="a2501c5b12ff94e338c0930e6c321af90"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.2 "><p id="af10224f581d946cb91a49683adf34271"><a name="af10224f581d946cb91a49683adf34271"></a><a name="af10224f581d946cb91a49683adf34271"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.1.5.1.3 "><p id="a0316e95fb756489a82f70ae562c523b4"><a name="a0316e95fb756489a82f70ae562c523b4"></a><a name="a0316e95fb756489a82f70ae562c523b4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.5.1.4 "><p id="af5ce8c5c520f468895f28d74f6eb4540"><a name="af5ce8c5c520f468895f28d74f6eb4540"></a><a name="af5ce8c5c520f468895f28d74f6eb4540"></a>Project ID.</p>
    </td>
    </tr>
    <tr id="r1208cbb1496440d89eb758b2cd80d578"><td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.1 "><p id="a4504807eb899465fb0ce3ac82d7013dc"><a name="a4504807eb899465fb0ce3ac82d7013dc"></a><a name="a4504807eb899465fb0ce3ac82d7013dc"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0026585113_p386591205643"><a name="en-us_topic_0026585113_p386591205643"></a><a name="en-us_topic_0026585113_p386591205643"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.1.5.1.3 "><p id="a293aacc9b5354786a8b30a063a186b02"><a name="a293aacc9b5354786a8b30a063a186b02"></a><a name="a293aacc9b5354786a8b30a063a186b02"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.5.1.4 "><p id="aa1138dcdd40340039e621e7abf0332e1"><a name="aa1138dcdd40340039e621e7abf0332e1"></a><a name="aa1138dcdd40340039e621e7abf0332e1"></a>ID of the domain that a project belongs to.</p>
    </td>
    </tr>
    <tr id="rbe8775b4e77a4b08be093de05e7bcbf3"><td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.1 "><p id="acc4c499e1b2f4bdd98e5c7acd4e8861b"><a name="acc4c499e1b2f4bdd98e5c7acd4e8861b"></a><a name="acc4c499e1b2f4bdd98e5c7acd4e8861b"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.2 "><p id="a4bf5dfe715d342e0a883343cbcf8181a"><a name="a4bf5dfe715d342e0a883343cbcf8181a"></a><a name="a4bf5dfe715d342e0a883343cbcf8181a"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.1.5.1.3 "><p id="a8c424bac7d93444dbc647a1d5c5c21e4"><a name="a8c424bac7d93444dbc647a1d5c5c21e4"></a><a name="a8c424bac7d93444dbc647a1d5c5c21e4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.5.1.4 "><p id="afc48731c8a2e4c66a56ac245f7a1e34e"><a name="afc48731c8a2e4c66a56ac245f7a1e34e"></a><a name="afc48731c8a2e4c66a56ac245f7a1e34e"></a>Project name.</p>
    </td>
    </tr>
    <tr id="row19356972201441"><td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.1 "><p id="p29605601201441"><a name="p29605601201441"></a><a name="p29605601201441"></a>is_domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.2 "><p id="p21596807201441"><a name="p21596807201441"></a><a name="p21596807201441"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.1.5.1.3 "><p id="p39263216201441"><a name="p39263216201441"></a><a name="p39263216201441"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.5.1.4 "><p id="p59347844201441"><a name="p59347844201441"></a><a name="p59347844201441"></a>Is domain or not.</p>
    </td>
    </tr>
    <tr id="row46028278201453"><td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.1 "><p id="p27327398201453"><a name="p27327398201453"></a><a name="p27327398201453"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.2 "><p id="p1690706201453"><a name="p1690706201453"></a><a name="p1690706201453"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.1.5.1.3 "><p id="p57286369201453"><a name="p57286369201453"></a><a name="p57286369201453"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.5.1.4 "><p id="p30534075201453"><a name="p30534075201453"></a><a name="p30534075201453"></a>Whether a project is available.</p>
    </td>
    </tr>
    <tr id="row14242324201510"><td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.1 "><p id="p35305259201510"><a name="p35305259201510"></a><a name="p35305259201510"></a>parent_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.2 "><p id="p17738677201510"><a name="p17738677201510"></a><a name="p17738677201510"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.1.5.1.3 "><p id="p53557531201510"><a name="p53557531201510"></a><a name="p53557531201510"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.5.1.4 "><p id="p62242884201510"><a name="p62242884201510"></a><a name="p62242884201510"></a>Parent ID of a project.</p>
    </td>
    </tr>
    <tr id="row118851458123110"><td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.1 "><p id="p15782326153214"><a name="p15782326153214"></a><a name="p15782326153214"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.2 "><p id="p11781226203213"><a name="p11781226203213"></a><a name="p11781226203213"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.1.5.1.3 "><p id="p19781142613218"><a name="p19781142613218"></a><a name="p19781142613218"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.5.1.4 "><p id="p1478012616328"><a name="p1478012616328"></a><a name="p1478012616328"></a>Project status.</p>
    </td>
    </tr>
    <tr id="row1876014312321"><td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.1 "><p id="p188853587312"><a name="p188853587312"></a><a name="p188853587312"></a>suspended_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.2 "><p id="p1488519586315"><a name="p1488519586315"></a><a name="p1488519586315"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.1.5.1.3 "><p id="p14885258123120"><a name="p14885258123120"></a><a name="p14885258123120"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.5.1.4 "><p id="p178857581319"><a name="p178857581319"></a><a name="p178857581319"></a>Time when a project is suspended.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
      "project": { 
        "is_domain": false, 
        "description": "", 
        "enabled": true, 
        "id": "ee65ca70d3cf43aaa1ea6492ce15f289", 
        "parent_id": "9041929bcc6e4bfe85add4e7b96ffdd7", 
        "domain_id": "398998b5392f4150ad48fe456d6de4f1", 
        "name": "{region_id}_test1", 
        "status": "suspended", 
        "suspended_time": "2017-08-17T02:50:23.000000" 
      } 
    }
    ```


## **Status Codes**<a name="section20323151411368"></a>

<a name="table8323141453613"></a>
<table><thead align="left"><tr id="row932381403612"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p14323514173615"><a name="p14323514173615"></a><a name="p14323514173615"></a><strong id="b842352706183230_3"><a name="b842352706183230_3"></a><a name="b842352706183230_3"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p10323141463613"><a name="p10323141463613"></a><a name="p10323141463613"></a><strong id="b20601766145329_9"><a name="b20601766145329_9"></a><a name="b20601766145329_9"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row132319142366"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p16323714103613"><a name="p16323714103613"></a><a name="p16323714103613"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5323614133611"><a name="p5323614133611"></a><a name="p5323614133611"></a>The request is successful.</p>
</td>
</tr>
<tr id="row43234147366"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1632321443618"><a name="p1632321443618"></a><a name="p1632321443618"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p432310148363"><a name="p432310148363"></a><a name="p432310148363"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row3323114113619"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p832311411365"><a name="p832311411365"></a><a name="p832311411365"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p14323121419361"><a name="p14323121419361"></a><a name="p14323121419361"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row15323514113619"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p13323131419361"><a name="p13323131419361"></a><a name="p13323131419361"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p12323914143611"><a name="p12323914143611"></a><a name="p12323914143611"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row1832313143362"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p20324171414362"><a name="p20324171414362"></a><a name="p20324171414362"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p33243147365"><a name="p33243147365"></a><a name="p33243147365"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row143245147365"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1732412140368"><a name="p1732412140368"></a><a name="p1732412140368"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p232416145368"><a name="p232416145368"></a><a name="p232416145368"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row83241314123618"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5324181453616"><a name="p5324181453616"></a><a name="p5324181453616"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p232411417363"><a name="p232411417363"></a><a name="p232411417363"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

