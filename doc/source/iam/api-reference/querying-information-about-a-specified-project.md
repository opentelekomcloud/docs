# Querying Information About a Specified Project<a name="en-us_topic_0066154567"></a>

## Function Description<a name="section19935195953515"></a>

This interface is used to query detailed information about a project based on the project ID.

## URI<a name="section1935145911357"></a>

-   URI format

    GET /v3/projects/\{project\_id\}

-   URI parameter description

    <a name="table1893565913351"></a>
    <table><thead align="left"><tr id="row09361359123517"><th class="cellrowborder" valign="top" width="22.207779222077793%" id="mcps1.1.5.1.1"><p id="p11936175963512"><a name="p11936175963512"></a><a name="p11936175963512"></a><strong id="b2465687218314"><a name="b2465687218314"></a><a name="b2465687218314"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.41785821417858%" id="mcps1.1.5.1.2"><p id="p16936115915351"><a name="p16936115915351"></a><a name="p16936115915351"></a><strong id="ac429376f11ae472b87ff4be326afb9d8_1"><a name="ac429376f11ae472b87ff4be326afb9d8_1"></a><a name="ac429376f11ae472b87ff4be326afb9d8_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.03789621037896%" id="mcps1.1.5.1.3"><p id="p17936145912357"><a name="p17936145912357"></a><a name="p17936145912357"></a><strong id="b10222588183127_1"><a name="b10222588183127_1"></a><a name="b10222588183127_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.33646635336466%" id="mcps1.1.5.1.4"><p id="p8936105919358"><a name="p8936105919358"></a><a name="p8936105919358"></a><strong id="b6981351183141"><a name="b6981351183141"></a><a name="b6981351183141"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1993655983519"><td class="cellrowborder" valign="top" width="22.207779222077793%" headers="mcps1.1.5.1.1 "><p id="p193655973518"><a name="p193655973518"></a><a name="p193655973518"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41785821417858%" headers="mcps1.1.5.1.2 "><p id="p13936175953511"><a name="p13936175953511"></a><a name="p13936175953511"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.03789621037896%" headers="mcps1.1.5.1.3 "><p id="p1093614590357"><a name="p1093614590357"></a><a name="p1093614590357"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.33646635336466%" headers="mcps1.1.5.1.4 "><p id="p109368599354"><a name="p109368599354"></a><a name="p109368599354"></a>Project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section199361259143511"></a>

-   Request header parameter description

    <a name="table693655912359"></a>
    <table><thead align="left"><tr id="row393615592358"><th class="cellrowborder" valign="top" width="22.21%" id="mcps1.1.5.1.1"><p id="p1793645910353"><a name="p1793645910353"></a><a name="p1793645910353"></a><strong id="b31449777183441"><a name="b31449777183441"></a><a name="b31449777183441"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.15%" id="mcps1.1.5.1.2"><p id="p10937459173515"><a name="p10937459173515"></a><a name="p10937459173515"></a><strong id="ac429376f11ae472b87ff4be326afb9d8_3"><a name="ac429376f11ae472b87ff4be326afb9d8_3"></a><a name="ac429376f11ae472b87ff4be326afb9d8_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.15%" id="mcps1.1.5.1.3"><p id="p9937259113513"><a name="p9937259113513"></a><a name="p9937259113513"></a><strong id="b10222588183127_3"><a name="b10222588183127_3"></a><a name="b10222588183127_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.49%" id="mcps1.1.5.1.4"><p id="p129378597357"><a name="p129378597357"></a><a name="p129378597357"></a><strong id="b4615667118353"><a name="b4615667118353"></a><a name="b4615667118353"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row693710598354"><td class="cellrowborder" valign="top" width="22.21%" headers="mcps1.1.5.1.1 "><p id="p493710593358"><a name="p493710593358"></a><a name="p493710593358"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.15%" headers="mcps1.1.5.1.2 "><p id="p3937165913358"><a name="p3937165913358"></a><a name="p3937165913358"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.15%" headers="mcps1.1.5.1.3 "><p id="p49375592351"><a name="p49375592351"></a><a name="p49375592351"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.5.1.4 "><p id="p193713595351"><a name="p193713595351"></a><a name="p193713595351"></a>Authenticated token.</p>
    </td>
    </tr>
    <tr id="row19373595350"><td class="cellrowborder" valign="top" width="22.21%" headers="mcps1.1.5.1.1 "><p id="p9937135912358"><a name="p9937135912358"></a><a name="p9937135912358"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.15%" headers="mcps1.1.5.1.2 "><p id="p8937155973512"><a name="p8937155973512"></a><a name="p8937155973512"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.15%" headers="mcps1.1.5.1.3 "><p id="p29371159103518"><a name="p29371159103518"></a><a name="p29371159103518"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.5.1.4 "><p id="p193795920356"><a name="p193795920356"></a><a name="p193795920356"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    Obtaining information about the project whose ID is project\_id=619d3e78f61b4be68bc5aa0b59edcf7b

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://10.64.23.150:31943/v3/projects/619d3e78f61b4be68bc5aa0b59edcf7b
    ```


## Response<a name="section293813595352"></a>

-   Sample response

```
{
  "project": {
    "is_domain": false,
    "description": "",
    "links": {
      "self": "None/v3/projects/2e93d63d8d2249f5a4ac5e2c78586a6e"
    },
    "enabled": true,
    "id": "2e93d63d8d2249f5a4ac5e2c78586a6e",
    "parent_id": "44c0781c83484eb9a4a5d4d233522cea",
    "domain_id": "44c0781c83484eb9a4a5d4d233522cea",
    "name": "MOS"   //Default project name of OBS
  }
}
```

## Status Codes<a name="section594020590359"></a>

<a name="table179401559183514"></a>
<table><thead align="left"><tr id="row169401559133520"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p5940155913353"><a name="p5940155913353"></a><a name="p5940155913353"></a><strong id="b13348955183548"><a name="b13348955183548"></a><a name="b13348955183548"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p1494035916353"><a name="p1494035916353"></a><a name="p1494035916353"></a><strong id="b3211761218363"><a name="b3211761218363"></a><a name="b3211761218363"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row3942185963517"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2942125933518"><a name="p2942125933518"></a><a name="p2942125933518"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p794285911357"><a name="p794285911357"></a><a name="p794285911357"></a>The request is successful.</p>
</td>
</tr>
<tr id="row1494285920350"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p094295913357"><a name="p094295913357"></a><a name="p094295913357"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p14942135920353"><a name="p14942135920353"></a><a name="p14942135920353"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row14942185913516"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p994255919358"><a name="p994255919358"></a><a name="p994255919358"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3942155993513"><a name="p3942155993513"></a><a name="p3942155993513"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row1494295910356"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p99421759203517"><a name="p99421759203517"></a><a name="p99421759203517"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5942195912351"><a name="p5942195912351"></a><a name="p5942195912351"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row209421659163510"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p159428594358"><a name="p159428594358"></a><a name="p159428594358"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1394295911357"><a name="p1394295911357"></a><a name="p1394295911357"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row3942859163516"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p894215993514"><a name="p894215993514"></a><a name="p894215993514"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p14942115963512"><a name="p14942115963512"></a><a name="p14942115963512"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

