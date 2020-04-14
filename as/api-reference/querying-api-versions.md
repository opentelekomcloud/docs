# Querying API Versions<a name="EN-US_TOPIC_0133153746"></a>

## Function<a name="section11355891"></a>

This interface is used to query all API versions of the AS service.

## URI<a name="section35094160"></a>

GET /

## Request Message<a name="section47411987"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query all versions of an API.

    ```
    GET https://{Endpoint}/
    ```


## Response Message<a name="section24054701"></a>

-   Response parameters

    **Table  1**  Response parameters

    <a name="table59665636"></a>
    <table><thead align="left"><tr id="row28755990"><th class="cellrowborder" valign="top" width="18.73%" id="mcps1.2.4.1.1"><p id="p47533853"><a name="p47533853"></a><a name="p47533853"></a><strong id="b992010528465"><a name="b992010528465"></a><a name="b992010528465"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.31%" id="mcps1.2.4.1.2"><p id="p25036876"><a name="p25036876"></a><a name="p25036876"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.96%" id="mcps1.2.4.1.3"><p id="p14721100"><a name="p14721100"></a><a name="p14721100"></a><strong id="b9643175312469"><a name="b9643175312469"></a><a name="b9643175312469"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34736162"><td class="cellrowborder" valign="top" width="18.73%" headers="mcps1.2.4.1.1 "><p id="p1654215818362"><a name="p1654215818362"></a><a name="p1654215818362"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.31%" headers="mcps1.2.4.1.2 "><p id="p2257160"><a name="p2257160"></a><a name="p2257160"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.96%" headers="mcps1.2.4.1.3 "><p id="p48612303"><a name="p48612303"></a><a name="p48612303"></a>Specifies the API versions.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **versions**  field description

    <a name="table5036780310489"></a>
    <table><thead align="left"><tr id="r1f3f90a6acc94015acc80b9d6b53f072"><th class="cellrowborder" valign="top" width="18.67%" id="mcps1.2.4.1.1"><p id="ad0d15c1370cb450fb7e6011b8baff160"><a name="ad0d15c1370cb450fb7e6011b8baff160"></a><a name="ad0d15c1370cb450fb7e6011b8baff160"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.23%" id="mcps1.2.4.1.2"><p id="a2273dfb9dd3341b0b5cbf801a0aa70fc"><a name="a2273dfb9dd3341b0b5cbf801a0aa70fc"></a><a name="a2273dfb9dd3341b0b5cbf801a0aa70fc"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65.10000000000001%" id="mcps1.2.4.1.3"><p id="a479b45e1fbfc44118151c43b5ecb82f1"><a name="a479b45e1fbfc44118151c43b5ecb82f1"></a><a name="a479b45e1fbfc44118151c43b5ecb82f1"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rdd24623b54f94a86b0f655ec659180e9"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="ab9c8eb8b964943509fca83cc70a4e489"><a name="ab9c8eb8b964943509fca83cc70a4e489"></a><a name="ab9c8eb8b964943509fca83cc70a4e489"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="a43cc5f338c7e429c861f7dbb2dcb3229"><a name="a43cc5f338c7e429c861f7dbb2dcb3229"></a><a name="a43cc5f338c7e429c861f7dbb2dcb3229"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.10000000000001%" headers="mcps1.2.4.1.3 "><p id="a5c153a8f0b8d4f26af1405cdcbcec1cc"><a name="a5c153a8f0b8d4f26af1405cdcbcec1cc"></a><a name="a5c153a8f0b8d4f26af1405cdcbcec1cc"></a>Specifies the API version ID.</p>
    </td>
    </tr>
    <tr id="r784e679e20ef42c7b5f0d9caebb3d506"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="af5650be6710143e49d288b78f41a9c9d"><a name="af5650be6710143e49d288b78f41a9c9d"></a><a name="af5650be6710143e49d288b78f41a9c9d"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="aa41878c3fbc74f52be50c47e0dd26a46"><a name="aa41878c3fbc74f52be50c47e0dd26a46"></a><a name="aa41878c3fbc74f52be50c47e0dd26a46"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.10000000000001%" headers="mcps1.2.4.1.3 "><p id="a37d79d061a9f47c5beee1f98f4c4611b"><a name="a37d79d061a9f47c5beee1f98f4c4611b"></a><a name="a37d79d061a9f47c5beee1f98f4c4611b"></a>Specifies the API URL. For details, see <a href="#t759e6d15d244474e8f286185ede143fb">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="r06fe5129bbc1493289f623afe4a4f1a2"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p9107111411399"><a name="p9107111411399"></a><a name="p9107111411399"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="a89734c8a12d44d69ab229cf5857bdf05"><a name="a89734c8a12d44d69ab229cf5857bdf05"></a><a name="a89734c8a12d44d69ab229cf5857bdf05"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.10000000000001%" headers="mcps1.2.4.1.3 "><p id="p19907734114018"><a name="p19907734114018"></a><a name="p19907734114018"></a>Specifies the earliest supported API version number.</p>
    </td>
    </tr>
    <tr id="rac189e8b65c5430eb4503bf1d1bbb4d7"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="ab5c5c2b93a134f18a2455224014556e9"><a name="ab5c5c2b93a134f18a2455224014556e9"></a><a name="ab5c5c2b93a134f18a2455224014556e9"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="a2de7247f99c143e09e698f0ef82f62bc"><a name="a2de7247f99c143e09e698f0ef82f62bc"></a><a name="a2de7247f99c143e09e698f0ef82f62bc"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.10000000000001%" headers="mcps1.2.4.1.3 "><p id="a65ce06cd4813480498062e1de2541bd3"><a name="a65ce06cd4813480498062e1de2541bd3"></a><a name="a65ce06cd4813480498062e1de2541bd3"></a>Specifies the API version status.</p>
    <a name="ud3dc362d60f54fc08039ec57e921e5a6"></a><a name="ud3dc362d60f54fc08039ec57e921e5a6"></a><ul id="ud3dc362d60f54fc08039ec57e921e5a6"><li><strong id="b52752029175412"><a name="b52752029175412"></a><a name="b52752029175412"></a>CURRENT</strong>: indicates a primary version.</li><li><strong>SUPPORTED</strong>: indicates an earlier version which is still supported.</li><li><strong id="b250813045513"><a name="b250813045513"></a><a name="b250813045513"></a>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</li></ul>
    </td>
    </tr>
    <tr id="r4dfedc0bd4ff45f2ac05364f99f01708"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="a306f2c2ef05e47f78c5e0fc5440cea3c"><a name="a306f2c2ef05e47f78c5e0fc5440cea3c"></a><a name="a306f2c2ef05e47f78c5e0fc5440cea3c"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="a979f525a997c4d1e8808195ca9d7f53e"><a name="a979f525a997c4d1e8808195ca9d7f53e"></a><a name="a979f525a997c4d1e8808195ca9d7f53e"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.10000000000001%" headers="mcps1.2.4.1.3 "><p id="p1255911034615"><a name="p1255911034615"></a><a name="p1255911034615"></a>Specifies the release date of an API version.</p>
    </td>
    </tr>
    <tr id="r45a3cc4c3f6943639ac3843c688f6865"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="a52a9f640ec724f40a4829ddf066e0837"><a name="a52a9f640ec724f40a4829ddf066e0837"></a><a name="a52a9f640ec724f40a4829ddf066e0837"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="a015154a0e4094475a717b23650fa6cf1"><a name="a015154a0e4094475a717b23650fa6cf1"></a><a name="a015154a0e4094475a717b23650fa6cf1"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.10000000000001%" headers="mcps1.2.4.1.3 "><p id="adefe07f521ca4e0aab9007ea28bebc7d"><a name="adefe07f521ca4e0aab9007ea28bebc7d"></a><a name="adefe07f521ca4e0aab9007ea28bebc7d"></a>Specifies the latest supported API version number.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **links**  field description

    <a name="t759e6d15d244474e8f286185ede143fb"></a>
    <table><thead align="left"><tr id="rce98b9668cd747c88039421afe5ce935"><th class="cellrowborder" valign="top" width="18.68%" id="mcps1.2.4.1.1"><p id="ad9ac3007570a4752b2b2dbc0fb04dadc"><a name="ad9ac3007570a4752b2b2dbc0fb04dadc"></a><a name="ad9ac3007570a4752b2b2dbc0fb04dadc"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.23%" id="mcps1.2.4.1.2"><p id="a602246198adf4a79a13bc4317d4c0d4f"><a name="a602246198adf4a79a13bc4317d4c0d4f"></a><a name="a602246198adf4a79a13bc4317d4c0d4f"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65.09%" id="mcps1.2.4.1.3"><p id="a8cbfa8dcb0b943ff8e789755123fec83"><a name="a8cbfa8dcb0b943ff8e789755123fec83"></a><a name="a8cbfa8dcb0b943ff8e789755123fec83"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r43de461181294c56b28da56a1f604b09"><td class="cellrowborder" valign="top" width="18.68%" headers="mcps1.2.4.1.1 "><p id="abc19a41a8f594f1ba6701e10da50a078"><a name="abc19a41a8f594f1ba6701e10da50a078"></a><a name="abc19a41a8f594f1ba6701e10da50a078"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="a15ae7b8585d24e48abc6b9bf45636fda"><a name="a15ae7b8585d24e48abc6b9bf45636fda"></a><a name="a15ae7b8585d24e48abc6b9bf45636fda"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.09%" headers="mcps1.2.4.1.3 "><p id="p139393206480"><a name="p139393206480"></a><a name="p139393206480"></a>Specifies the API Uniform Resource Locator (URL).</p>
    </td>
    </tr>
    <tr id="rbd5ec7242fef4c03b21636ac14160d9e"><td class="cellrowborder" valign="top" width="18.68%" headers="mcps1.2.4.1.1 "><p id="a18479f6b70b34f29b2b90d754f59282a"><a name="a18479f6b70b34f29b2b90d754f59282a"></a><a name="a18479f6b70b34f29b2b90d754f59282a"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="ae1f14fa2e6a54531aeffd26874fea267"><a name="ae1f14fa2e6a54531aeffd26874fea267"></a><a name="ae1f14fa2e6a54531aeffd26874fea267"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.09%" headers="mcps1.2.4.1.3 "><p id="p115877381483"><a name="p115877381483"></a><a name="p115877381483"></a>Specifies the API URL dependency.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "versions": [
        {
          "id": "v1",
          "links": [
            {
              "href": "https://as.XXX.mycloud.com/autoscaling-api/v1/",
              "rel": "self"
            }
          ],
          "min_version": "",
          "status": "CURRENT",
          "updated": "2016-06-30T00:00:00Z",
          "version": ""
        },
        {
          "id": "v2",
          "links": [
            {
              "href": "https://as.XXX.mycloud.com/autoscaling-api/v2/",
              "rel": "self"
            }
          ],
          "min_version": "",
          "status": "SUPPORTED",
          "updated": "2018-03-30T00:00:00Z",
          "version": ""
        }
      ]
    }
    ```


## Returned Values<a name="section15165719"></a>

-   Normal

    200

-   Abnormal

    <a name="table5908907"></a>
    <table><thead align="left"><tr id="row16065622"><th class="cellrowborder" valign="top" width="44.17%" id="mcps1.1.3.1.1"><p id="p26246992"><a name="p26246992"></a><a name="p26246992"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.83%" id="mcps1.1.3.1.2"><p id="p45631627"><a name="p45631627"></a><a name="p45631627"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5174319"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p16466658"><a name="p16466658"></a><a name="p16466658"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p58730959"><a name="p58730959"></a><a name="p58730959"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row58816586"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p66523006"><a name="p66523006"></a><a name="p66523006"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p19654399"><a name="p19654399"></a><a name="p19654399"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row42671863"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p33868885"><a name="p33868885"></a><a name="p33868885"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p59025204"><a name="p59025204"></a><a name="p59025204"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row61464796"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p12592542"><a name="p12592542"></a><a name="p12592542"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p13362997"><a name="p13362997"></a><a name="p13362997"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row53158116"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p10840149"><a name="p10840149"></a><a name="p10840149"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p5636878"><a name="p5636878"></a><a name="p5636878"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row50731910"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p15644031"><a name="p15644031"></a><a name="p15644031"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p59206997"><a name="p59206997"></a><a name="p59206997"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row63100926"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p10901353"><a name="p10901353"></a><a name="p10901353"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p10594405"><a name="p10594405"></a><a name="p10594405"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row28240785"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p5802216"><a name="p5802216"></a><a name="p5802216"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p217508"><a name="p217508"></a><a name="p217508"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row1957580"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p24346266"><a name="p24346266"></a><a name="p24346266"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p25890496"><a name="p25890496"></a><a name="p25890496"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row31687876"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p16581154"><a name="p16581154"></a><a name="p16581154"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p896237"><a name="p896237"></a><a name="p896237"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row8066134"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p49377135"><a name="p49377135"></a><a name="p49377135"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p40124968"><a name="p40124968"></a><a name="p40124968"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row25580392"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p58745844"><a name="p58745844"></a><a name="p58745844"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p60792949"><a name="p60792949"></a><a name="p60792949"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row10265637"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p26210288"><a name="p26210288"></a><a name="p26210288"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p42658596"><a name="p42658596"></a><a name="p42658596"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row48383044"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p26712487"><a name="p26712487"></a><a name="p26712487"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p16227847"><a name="p16227847"></a><a name="p16227847"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

