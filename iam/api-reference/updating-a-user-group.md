# Updating a User Group<a name="en-us_topic_0057845600"></a>

## Function Description<a name="section495175389414"></a>

This interface is used to update user group information.

## URI<a name="section3019338085013"></a>

-   URI format

    PATCH /v3/groups/\{group\_id\}

-   URI parameter description

    <a name="en-us_topic_0032920307_table36168141"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row15662289"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p60685926"><a name="en-us_topic_0032920307_p60685926"></a><a name="en-us_topic_0032920307_p60685926"></a><strong id="b842352706111956"><a name="b842352706111956"></a><a name="b842352706111956"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.24%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p16612996"><a name="en-us_topic_0032920307_p16612996"></a><a name="en-us_topic_0032920307_p16612996"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.98%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p3475410"><a name="en-us_topic_0032920307_p3475410"></a><a name="en-us_topic_0032920307_p3475410"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p13072760"><a name="en-us_topic_0032920307_p13072760"></a><a name="en-us_topic_0032920307_p13072760"></a><strong id="b20601766145329"><a name="b20601766145329"></a><a name="b20601766145329"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row52260639"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p5253358"><a name="en-us_topic_0032920307_p5253358"></a><a name="en-us_topic_0032920307_p5253358"></a>group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p22868878"><a name="en-us_topic_0032920307_p22868878"></a><a name="en-us_topic_0032920307_p22868878"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.98%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p40439847"><a name="en-us_topic_0032920307_p40439847"></a><a name="en-us_topic_0032920307_p40439847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p54402144"><a name="en-us_topic_0032920307_p54402144"></a><a name="en-us_topic_0032920307_p54402144"></a>ID of a user group.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="section1437107585444"></a>

-   Request header parameter description

    <a name="en-us_topic_0032920307_table21736211"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row48433347"><th class="cellrowborder" valign="top" width="19.49%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p30787047"><a name="en-us_topic_0032920307_p30787047"></a><a name="en-us_topic_0032920307_p30787047"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p10722842"><a name="en-us_topic_0032920307_p10722842"></a><a name="en-us_topic_0032920307_p10722842"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.299999999999997%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p63243911"><a name="en-us_topic_0032920307_p63243911"></a><a name="en-us_topic_0032920307_p63243911"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.35%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p22483156"><a name="en-us_topic_0032920307_p22483156"></a><a name="en-us_topic_0032920307_p22483156"></a><strong id="b27441562172015"><a name="b27441562172015"></a><a name="b27441562172015"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row9196329"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p6705199"><a name="en-us_topic_0032920307_p6705199"></a><a name="en-us_topic_0032920307_p6705199"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p6250253"><a name="en-us_topic_0032920307_p6250253"></a><a name="en-us_topic_0032920307_p6250253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36508524"><a name="en-us_topic_0032920307_p36508524"></a><a name="en-us_topic_0032920307_p36508524"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.35%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p4400500"><a name="en-us_topic_0032920307_p4400500"></a><a name="en-us_topic_0032920307_p4400500"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032920307_row39604502"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p53848109"><a name="en-us_topic_0032920307_p53848109"></a><a name="en-us_topic_0032920307_p53848109"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p66729601"><a name="en-us_topic_0032920307_p66729601"></a><a name="en-us_topic_0032920307_p66729601"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36388601"><a name="en-us_topic_0032920307_p36388601"></a><a name="en-us_topic_0032920307_p36388601"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.35%" headers="mcps1.1.5.1.4 "><p id="p4222254811619"><a name="p4222254811619"></a><a name="p4222254811619"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request body parameter description

    <a name="table2693202185751"></a>
    <table><thead align="left"><tr id="row3098410285751"><th class="cellrowborder" valign="top" width="19.49%" id="mcps1.1.5.1.1"><p id="p2668435285751"><a name="p2668435285751"></a><a name="p2668435285751"></a><strong id="b2033878828"><a name="b2033878828"></a><a name="b2033878828"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.2"><p id="p1394889485751"><a name="p1394889485751"></a><a name="p1394889485751"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.7%" id="mcps1.1.5.1.3"><p id="p5611863385751"><a name="p5611863385751"></a><a name="p5611863385751"></a><strong id="b842352706143526_5"><a name="b842352706143526_5"></a><a name="b842352706143526_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.95%" id="mcps1.1.5.1.4"><p id="p4931540085751"><a name="p4931540085751"></a><a name="p4931540085751"></a><strong id="b43875778172015_1"><a name="b43875778172015_1"></a><a name="b43875778172015_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3512445285751"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p2650832485751"><a name="p2650832485751"></a><a name="p2650832485751"></a>group</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p6679947285751"><a name="p6679947285751"></a><a name="p6679947285751"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.1.5.1.3 "><p id="p132615487190"><a name="p132615487190"></a><a name="p132615487190"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.95%" headers="mcps1.1.5.1.4 "><p id="p5045921585751"><a name="p5045921585751"></a><a name="p5045921585751"></a>Request body of a group.</p>
    </td>
    </tr>
    <tr id="row5147975685751"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p911072085751"><a name="p911072085751"></a><a name="p911072085751"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p6687968385751"><a name="p6687968385751"></a><a name="p6687968385751"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.1.5.1.3 "><p id="p4854528085751"><a name="p4854528085751"></a><a name="p4854528085751"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.95%" headers="mcps1.1.5.1.4 "><p id="p3985359785751"><a name="p3985359785751"></a><a name="p3985359785751"></a>Description for a user group. The length is less than or equal to 255 characters.</p>
    </td>
    </tr>
    <tr id="row146168639717"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p644429109717"><a name="p644429109717"></a><a name="p644429109717"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p524932549717"><a name="p524932549717"></a><a name="p524932549717"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.1.5.1.3 "><p id="p240951669717"><a name="p240951669717"></a><a name="p240951669717"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.95%" headers="mcps1.1.5.1.4 "><p id="p55514069717"><a name="p55514069717"></a><a name="p55514069717"></a>ID of the domain to which a user group belongs.</p>
    </td>
    </tr>
    <tr id="row80338309723"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p51956079723"><a name="p51956079723"></a><a name="p51956079723"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p181910179723"><a name="p181910179723"></a><a name="p181910179723"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.1.5.1.3 "><p id="p641862599723"><a name="p641862599723"></a><a name="p641862599723"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.95%" headers="mcps1.1.5.1.4 "><p id="p317045109723"><a name="p317045109723"></a><a name="p317045109723"></a>Name of a user group. The length is less than or equal to 64 characters.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X PATCH -d'{"group": {"description": "Contract developers 2016"}}' https://172.30.48.86:31943/v3/groups/aaec2abd4eba430fbf61541ffde76650
    ```


## **Response**<a name="section422798898594"></a>

-   Response body parameter description

    <a name="table1806279685948"></a>
    <table><thead align="left"><tr id="row5888700685948"><th class="cellrowborder" valign="top" width="19.54%" id="mcps1.1.5.1.1"><p id="p511814385948"><a name="p511814385948"></a><a name="p511814385948"></a><strong id="b534056319"><a name="b534056319"></a><a name="b534056319"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.73%" id="mcps1.1.5.1.2"><p id="p10317145635110"><a name="p10317145635110"></a><a name="p10317145635110"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_7"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.08%" id="mcps1.1.5.1.3"><p id="p1191643385948"><a name="p1191643385948"></a><a name="p1191643385948"></a><strong id="b842352706143526_7"><a name="b842352706143526_7"></a><a name="b842352706143526_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.65%" id="mcps1.1.5.1.4"><p id="p2570700385948"><a name="p2570700385948"></a><a name="p2570700385948"></a><strong id="b43875778172015_3"><a name="b43875778172015_3"></a><a name="b43875778172015_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row189251885948"><td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.1.5.1.1 "><p id="p1907628285948"><a name="p1907628285948"></a><a name="p1907628285948"></a>group</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.73%" headers="mcps1.1.5.1.2 "><p id="p1331715617511"><a name="p1331715617511"></a><a name="p1331715617511"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.1.5.1.3 "><p id="p167497385948"><a name="p167497385948"></a><a name="p167497385948"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.65%" headers="mcps1.1.5.1.4 "><p id="p145516285948"><a name="p145516285948"></a><a name="p145516285948"></a>Response body of a user group.</p>
    </td>
    </tr>
    <tr id="row1309646185948"><td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.1.5.1.1 "><p id="p5418040185948"><a name="p5418040185948"></a><a name="p5418040185948"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.73%" headers="mcps1.1.5.1.2 "><p id="p6317185612512"><a name="p6317185612512"></a><a name="p6317185612512"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.1.5.1.3 "><p id="p2653635485948"><a name="p2653635485948"></a><a name="p2653635485948"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.65%" headers="mcps1.1.5.1.4 "><p id="p196103185948"><a name="p196103185948"></a><a name="p196103185948"></a>Description for a user group.</p>
    </td>
    </tr>
    <tr id="row1764928085948"><td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.1.5.1.1 "><p id="p2030561585948"><a name="p2030561585948"></a><a name="p2030561585948"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.73%" headers="mcps1.1.5.1.2 "><p id="p631785655110"><a name="p631785655110"></a><a name="p631785655110"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.1.5.1.3 "><p id="p3414215185948"><a name="p3414215185948"></a><a name="p3414215185948"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.65%" headers="mcps1.1.5.1.4 "><p id="p1405083185948"><a name="p1405083185948"></a><a name="p1405083185948"></a>ID of the domain to which a user group belongs.</p>
    </td>
    </tr>
    <tr id="row5934861685948"><td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.1.5.1.1 "><p id="p4250862085948"><a name="p4250862085948"></a><a name="p4250862085948"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.73%" headers="mcps1.1.5.1.2 "><p id="p13317155615115"><a name="p13317155615115"></a><a name="p13317155615115"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.1.5.1.3 "><p id="p2064619685948"><a name="p2064619685948"></a><a name="p2064619685948"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.65%" headers="mcps1.1.5.1.4 "><p id="p6172919385948"><a name="p6172919385948"></a><a name="p6172919385948"></a>ID of a user group.</p>
    </td>
    </tr>
    <tr id="row1869182785948"><td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.1.5.1.1 "><p id="p3764304685948"><a name="p3764304685948"></a><a name="p3764304685948"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.73%" headers="mcps1.1.5.1.2 "><p id="p103173569514"><a name="p103173569514"></a><a name="p103173569514"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.1.5.1.3 "><p id="p2918786585948"><a name="p2918786585948"></a><a name="p2918786585948"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.65%" headers="mcps1.1.5.1.4 "><p id="p1540683685948"><a name="p1540683685948"></a><a name="p1540683685948"></a>Resource links of a user group.</p>
    </td>
    </tr>
    <tr id="row444380085948"><td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.1.5.1.1 "><p id="p2440355685948"><a name="p2440355685948"></a><a name="p2440355685948"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.73%" headers="mcps1.1.5.1.2 "><p id="p163171563512"><a name="p163171563512"></a><a name="p163171563512"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.08%" headers="mcps1.1.5.1.3 "><p id="p3053098785948"><a name="p3053098785948"></a><a name="p3053098785948"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.65%" headers="mcps1.1.5.1.4 "><p id="p5709090385948"><a name="p5709090385948"></a><a name="p5709090385948"></a>Name of a user group.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
      "group": {
        "domain_id": "d54061ebcb5145dd814f8eb3fe9b7ac0",
        "description": "Contract developers 2016",
        "id": "aaec2abd4eba430fbf61541ffde76650",
        "links": {
          "self": "https://sample.domain.com/v3/groups/aaec2abd4eba430fbf61541ffde76650"
        },
        "name": "jixiang1"
      }
    }
    ```


## **Status Codes**<a name="section5556784894735"></a>

<a name="en-us_topic_0032920307_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0032920307_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0032920307_p51565323"><a name="en-us_topic_0032920307_p51565323"></a><a name="en-us_topic_0032920307_p51565323"></a><strong id="b19435058172015"><a name="b19435058172015"></a><a name="b19435058172015"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0032920307_p16041657"><a name="en-us_topic_0032920307_p16041657"></a><a name="en-us_topic_0032920307_p16041657"></a><strong id="b8187389172015"><a name="b8187389172015"></a><a name="b8187389172015"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0032920307_row24305815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p22613965"><a name="en-us_topic_0032920307_p22613965"></a><a name="en-us_topic_0032920307_p22613965"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p19791876"><a name="en-us_topic_0032920307_p19791876"></a><a name="en-us_topic_0032920307_p19791876"></a>The request is successful.</p>
</td>
</tr>
<tr id="en-us_topic_0032920307_row43909159"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p66980994"><a name="en-us_topic_0032920307_p66980994"></a><a name="en-us_topic_0032920307_p66980994"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p56751409"><a name="en-us_topic_0032920307_p56751409"></a><a name="en-us_topic_0032920307_p56751409"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row460808479497"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p120744399497"><a name="p120744399497"></a><a name="p120744399497"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p385055099497"><a name="p385055099497"></a><a name="p385055099497"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="en-us_topic_0032920307_row41000636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p32717189"><a name="en-us_topic_0032920307_p32717189"></a><a name="en-us_topic_0032920307_p32717189"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p32846614"><a name="en-us_topic_0032920307_p32846614"></a><a name="en-us_topic_0032920307_p32846614"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row2569718985351"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2994811485351"><a name="p2994811485351"></a><a name="p2994811485351"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p987817085351"><a name="p987817085351"></a><a name="p987817085351"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row3670434485410"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6190364385410"><a name="p6190364385410"></a><a name="p6190364385410"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4813919085410"><a name="p4813919085410"></a><a name="p4813919085410"></a>A resource conflict occurs.</p>
</td>
</tr>
<tr id="row4492325585415"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p165611385415"><a name="p165611385415"></a><a name="p165611385415"></a>501</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p6703633385415"><a name="p6703633385415"></a><a name="p6703633385415"></a>The API is not implemented.</p>
</td>
</tr>
</tbody>
</table>

