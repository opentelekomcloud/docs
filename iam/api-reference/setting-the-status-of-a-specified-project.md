# Setting the Status of a Specified Project<a name="en-us_topic_0074171149"></a>

## Function Description<a name="section18319181453614"></a>

This interface is used to set the status of a specified project. The project statuses include  **Normal**  and  **Suspended**.

## URI<a name="section1032051453615"></a>

-   URI format

    PUT /v3-ext/projects/\{project\_id\}


-   URI parameter description

    <a name="table1532018142366"></a>
    <table><thead align="left"><tr id="row103201149368"><th class="cellrowborder" valign="top" width="19.830000000000002%" id="mcps1.1.5.1.1"><p id="p1932041417367"><a name="p1932041417367"></a><a name="p1932041417367"></a><strong id="en-us_topic_0026586105_b842352706143612"><a name="en-us_topic_0026586105_b842352706143612"></a><a name="en-us_topic_0026586105_b842352706143612"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.78%" id="mcps1.1.5.1.2"><p id="p1232071411368"><a name="p1232071411368"></a><a name="p1232071411368"></a><strong id="en-us_topic_0026586105_b842352706143621"><a name="en-us_topic_0026586105_b842352706143621"></a><a name="en-us_topic_0026586105_b842352706143621"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.12%" id="mcps1.1.5.1.3"><p id="p832051411369"><a name="p832051411369"></a><a name="p832051411369"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.269999999999996%" id="mcps1.1.5.1.4"><p id="p2320191423611"><a name="p2320191423611"></a><a name="p2320191423611"></a><strong id="b20601766145329_1"><a name="b20601766145329_1"></a><a name="b20601766145329_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row183201814193615"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.1.5.1.1 "><p id="p432071415365"><a name="p432071415365"></a><a name="p432071415365"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.78%" headers="mcps1.1.5.1.2 "><p id="p83202014163620"><a name="p83202014163620"></a><a name="p83202014163620"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.12%" headers="mcps1.1.5.1.3 "><p id="p3320161415362"><a name="p3320161415362"></a><a name="p3320161415362"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.269999999999996%" headers="mcps1.1.5.1.4 "><p id="p332091410362"><a name="p332091410362"></a><a name="p332091410362"></a>Project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="section132251415368"></a>

-   Request header parameter description

    <a name="table3322161493613"></a>
    <table><thead align="left"><tr id="row11322131413615"><th class="cellrowborder" valign="top" width="19.688031196880313%" id="mcps1.1.5.1.1"><p id="p1432218149369"><a name="p1432218149369"></a><a name="p1432218149369"></a><strong id="b1798532095"><a name="b1798532095"></a><a name="b1798532095"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.98820117988201%" id="mcps1.1.5.1.2"><p id="p8322161443614"><a name="p8322161443614"></a><a name="p8322161443614"></a><strong id="b798071134"><a name="b798071134"></a><a name="b798071134"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.958204179582044%" id="mcps1.1.5.1.3"><p id="p19322111433620"><a name="p19322111433620"></a><a name="p19322111433620"></a><strong id="b842352706143526_5"><a name="b842352706143526_5"></a><a name="b842352706143526_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.36556344365563%" id="mcps1.1.5.1.4"><p id="p73221614143617"><a name="p73221614143617"></a><a name="p73221614143617"></a><strong id="b20601766145329_5"><a name="b20601766145329_5"></a><a name="b20601766145329_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row113221514113620"><td class="cellrowborder" valign="top" width="19.688031196880313%" headers="mcps1.1.5.1.1 "><p id="p123221314183616"><a name="p123221314183616"></a><a name="p123221314183616"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.98820117988201%" headers="mcps1.1.5.1.2 "><p id="p15322181419363"><a name="p15322181419363"></a><a name="p15322181419363"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.958204179582044%" headers="mcps1.1.5.1.3 "><p id="p432215149367"><a name="p432215149367"></a><a name="p432215149367"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.36556344365563%" headers="mcps1.1.5.1.4 "><p id="p1332281419368"><a name="p1332281419368"></a><a name="p1332281419368"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row1332261493613"><td class="cellrowborder" valign="top" width="19.688031196880313%" headers="mcps1.1.5.1.1 "><p id="p113221814143614"><a name="p113221814143614"></a><a name="p113221814143614"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.98820117988201%" headers="mcps1.1.5.1.2 "><p id="p8322714173618"><a name="p8322714173618"></a><a name="p8322714173618"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.958204179582044%" headers="mcps1.1.5.1.3 "><p id="p1322014123615"><a name="p1322014123615"></a><a name="p1322014123615"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.36556344365563%" headers="mcps1.1.5.1.4 "><p id="p2354060691653"><a name="p2354060691653"></a><a name="p2354060691653"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request body parameter description

    <a name="table2644112114413"></a>
    <table><thead align="left"><tr id="row964432117412"><th class="cellrowborder" valign="top" width="19.7%" id="mcps1.1.5.1.1"><p id="p764416211842"><a name="p764416211842"></a><a name="p764416211842"></a><strong id="b842352706102426"><a name="b842352706102426"></a><a name="b842352706102426"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.060000000000002%" id="mcps1.1.5.1.2"><p id="p156441821741"><a name="p156441821741"></a><a name="p156441821741"></a><strong id="b842352706102429"><a name="b842352706102429"></a><a name="b842352706102429"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.97%" id="mcps1.1.5.1.3"><p id="p106441212047"><a name="p106441212047"></a><a name="p106441212047"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.269999999999996%" id="mcps1.1.5.1.4"><p id="p176442215416"><a name="p176442215416"></a><a name="p176442215416"></a><strong id="b20601766145329_3"><a name="b20601766145329_3"></a><a name="b20601766145329_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1365942119417"><td class="cellrowborder" valign="top" width="19.7%" headers="mcps1.1.5.1.1 "><p id="p865922118416"><a name="p865922118416"></a><a name="p865922118416"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p1265914211416"><a name="p1265914211416"></a><a name="p1265914211416"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.1.5.1.3 "><p id="p1065902117414"><a name="p1065902117414"></a><a name="p1065902117414"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.269999999999996%" headers="mcps1.1.5.1.4 "><p id="p1065992116416"><a name="p1065992116416"></a><a name="p1065992116416"></a>Project status. The value can be <strong id="b842352706102534"><a name="b842352706102534"></a><a name="b842352706102534"></a>suspended</strong> or <strong id="b842352706102531"><a name="b842352706102531"></a><a name="b842352706102531"></a>normal</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   **suspended**: indicates that the project is suspended.  
    >-   **normal**: indicates that the project is normal.  

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -X "X-Auth-Token:$token" -X PUT -d '{"project": {"status":"suspended"}}'https://10.145.93.56:31943/v3-ext/projects/5c9f5525d9d24c5bbf91e74d86772029
    ```


## **Response**<a name="section1732319140365"></a>

No response body.

## **Status Codes**<a name="section20323151411368"></a>

<a name="table8323141453613"></a>
<table><thead align="left"><tr id="row932381403612"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p14323514173615"><a name="p14323514173615"></a><a name="p14323514173615"></a><strong id="b842352706183230_3"><a name="b842352706183230_3"></a><a name="b842352706183230_3"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p10323141463613"><a name="p10323141463613"></a><a name="p10323141463613"></a><strong id="b20601766145329_7"><a name="b20601766145329_7"></a><a name="b20601766145329_7"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row132319142366"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p16323714103613"><a name="p16323714103613"></a><a name="p16323714103613"></a>204</p>
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

