# Disassociating Resources from a Backup Policy<a name="EN-US_TOPIC_0043410562"></a>

## Function<a name="section63962185"></a>

This interface is used to disassociate one or more resources from a backup policy.

## URI<a name="section38788755"></a>

-   URI format

    POST /v2/\{project\_id\}/backuppolicyresources/\{policy\_id\}/deleted\_resources

-   Parameter description

    <a name="table60344938"></a>
    <table><thead align="left"><tr id="row59011071"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p15167431"><a name="p15167431"></a><a name="p15167431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p20602375"><a name="p20602375"></a><a name="p20602375"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p58179688"><a name="p58179688"></a><a name="p58179688"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14934289"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1717931"><a name="p1717931"></a><a name="p1717931"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p4934750"><a name="p4934750"></a><a name="p4934750"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row5830466319813"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p2505725719813"><a name="p2505725719813"></a><a name="p2505725719813"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p1637192319813"><a name="p1637192319813"></a><a name="p1637192319813"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p5105740619813"><a name="p5105740619813"></a><a name="p5105740619813"></a>Backup policy ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13554483"></a>

-   Parameter description

    <a name="table48412952"></a>
    <table><thead align="left"><tr id="row28932175"><th class="cellrowborder" valign="top" width="26.697330266973307%" id="mcps1.1.5.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.968703129687032%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.35836416358364%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.97560243975603%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50598521"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p62709075141636"><a name="p62709075141636"></a><a name="p62709075141636"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p46270351141636"><a name="p46270351141636"></a><a name="p46270351141636"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p56910918141636"><a name="p56910918141636"></a><a name="p56910918141636"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p46381666141636"><a name="p46381666141636"></a><a name="p46381666141636"></a>Information about the associated resource</p>
    </td>
    </tr>
    <tr id="row21736211"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p56476584141636"><a name="p56476584141636"></a><a name="p56476584141636"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p11200558141636"><a name="p11200558141636"></a><a name="p11200558141636"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p34830005141636"><a name="p34830005141636"></a><a name="p34830005141636"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p2658148141636"><a name="p2658148141636"></a><a name="p2658148141636"></a>Resource ID</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "resources": [
            {
                "resource_id": "bce8d47a-af17-4169-901f-4c7ae9f29c2c"
            }
        ]
    }
    ```


## Response<a name="section54881489"></a>

-   Parameter description

    <a name="table2553741120254"></a>
    <table><thead align="left"><tr id="row84520220254"><th class="cellrowborder" valign="top" width="29.182918291829186%" id="mcps1.1.4.1.1"><p id="p13266172411430"><a name="p13266172411430"></a><a name="p13266172411430"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.471547154715473%" id="mcps1.1.4.1.2"><p id="p112661924124316"><a name="p112661924124316"></a><a name="p112661924124316"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.345534553455344%" id="mcps1.1.4.1.3"><p id="p22662244436"><a name="p22662244436"></a><a name="p22662244436"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row894248020254"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p66058194175518"><a name="p66058194175518"></a><a name="p66058194175518"></a>success_resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p46347549175518"><a name="p46347549175518"></a><a name="p46347549175518"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p25472099175518"><a name="p25472099175518"></a><a name="p25472099175518"></a>List of successfully disassociated resources</p>
    </td>
    </tr>
    <tr id="row5784910817556"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p53393589175518"><a name="p53393589175518"></a><a name="p53393589175518"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p39485486175518"><a name="p39485486175518"></a><a name="p39485486175518"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p31870002175518"><a name="p31870002175518"></a><a name="p31870002175518"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row17830778175510"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p12639851175518"><a name="p12639851175518"></a><a name="p12639851175518"></a>fail_resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p63501382175518"><a name="p63501382175518"></a><a name="p63501382175518"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p35977553175518"><a name="p35977553175518"></a><a name="p35977553175518"></a>List of the resources that fail to be disassociated</p>
    </td>
    </tr>
    <tr id="row45118677175514"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p57955965175518"><a name="p57955965175518"></a><a name="p57955965175518"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p23058063175518"><a name="p23058063175518"></a><a name="p23058063175518"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p89659175518"><a name="p89659175518"></a><a name="p89659175518"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row4113847020254"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p4388173520254"><a name="p4388173520254"></a><a name="p4388173520254"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p534483917131"><a name="p534483917131"></a><a name="p534483917131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p1103955520254"><a name="p1103955520254"></a><a name="p1103955520254"></a>Error message returned after an error occurs</p>
    </td>
    </tr>
    <tr id="row3224713720254"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p6188131520254"><a name="p6188131520254"></a><a name="p6188131520254"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p3027879417131"><a name="p3027879417131"></a><a name="p3027879417131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p6179451720254"><a name="p6179451720254"></a><a name="p6179451720254"></a>Error code returned after an error occurs</p>
    <p id="p1927974620254"><a name="p1927974620254"></a><a name="p1927974620254"></a>For details about error codes, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    { 
        "success_resources": [],
        "fail_resources": [ 
        { 
             "resource_id": "bbba7509-f457-4732-97f1-a8e24b6ed9bc" 
        }] 
    }
    ```

    or

    ```
    {
        "error": {
            "code": "XXXX",
            "message": "XXX"
        }
    }
    ```


## Status Codes<a name="section24171358"></a>

-   Normal

    200

-   Abnormal

    <a name="table51230787"></a>
    <table><thead align="left"><tr id="row60503138"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p1807185"><a name="p1807185"></a><a name="p1807185"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p12164329"><a name="p12164329"></a><a name="p12164329"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45786577"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17725233"><a name="p17725233"></a><a name="p17725233"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p26457778"><a name="p26457778"></a><a name="p26457778"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row36793414"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p27476571"><a name="p27476571"></a><a name="p27476571"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p11009764"><a name="p11009764"></a><a name="p11009764"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row31979016"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p40163483"><a name="p40163483"></a><a name="p40163483"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p32016662"><a name="p32016662"></a><a name="p32016662"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row4499052116376"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2035357816376"><a name="p2035357816376"></a><a name="p2035357816376"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3802708716376"><a name="p3802708716376"></a><a name="p3802708716376"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row8462523163725"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p14375766163725"><a name="p14375766163725"></a><a name="p14375766163725"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p23586373163725"><a name="p23586373163725"></a><a name="p23586373163725"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row60343628163758"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p55995701163758"><a name="p55995701163758"></a><a name="p55995701163758"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p39357967163758"><a name="p39357967163758"></a><a name="p39357967163758"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row32079544163754"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p48306260163754"><a name="p48306260163754"></a><a name="p48306260163754"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p20492948163754"><a name="p20492948163754"></a><a name="p20492948163754"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row28680770163738"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p41441040163738"><a name="p41441040163738"></a><a name="p41441040163738"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1281119163738"><a name="p1281119163738"></a><a name="p1281119163738"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row65552906164354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p8185203164354"><a name="p8185203164354"></a><a name="p8185203164354"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p59021712164354"><a name="p59021712164354"></a><a name="p59021712164354"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row19714506"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p53371190"><a name="p53371190"></a><a name="p53371190"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p28099101"><a name="p28099101"></a><a name="p28099101"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row32688750164938"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p30543097164938"><a name="p30543097164938"></a><a name="p30543097164938"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p58071768164938"><a name="p58071768164938"></a><a name="p58071768164938"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row11809518164943"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17046908164943"><a name="p17046908164943"></a><a name="p17046908164943"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38622347164943"><a name="p38622347164943"></a><a name="p38622347164943"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row38399341164956"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p23338889164956"><a name="p23338889164956"></a><a name="p23338889164956"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p11401882164956"><a name="p11401882164956"></a><a name="p11401882164956"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row51565323"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p16041657"><a name="p16041657"></a><a name="p16041657"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p24305815"><a name="p24305815"></a><a name="p24305815"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

