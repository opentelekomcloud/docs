# Batch Updating or Deleting Tags of a Backup Policy<a name="EN-US_TOPIC_0067142132"></a>

## Function<a name="section63962185"></a>

This interface is used to update or delete the tags of a backup policy.

## URI<a name="section38788755"></a>

-   URI format

    POST /v2/\{project\_id\}/backuppolicy/\{policy\_id\}/tags/action

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
    <tr id="row49177768142544"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p23976272142544"><a name="p23976272142544"></a><a name="p23976272142544"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p63029893142544"><a name="p63029893142544"></a><a name="p63029893142544"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p5147694142544"><a name="p5147694142544"></a><a name="p5147694142544"></a>Backup policy ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13554483"></a>

-   Parameter description

    <a name="table62260077183541"></a>
    <table><thead align="left"><tr id="row18137457183541"><th class="cellrowborder" valign="top" width="21.42%" id="mcps1.1.5.1.1"><p id="p1431817452527"><a name="p1431817452527"></a><a name="p1431817452527"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.34%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.49%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.75%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12496319183541"><td class="cellrowborder" valign="top" width="21.42%" headers="mcps1.1.5.1.1 "><p id="p5568910183541"><a name="p5568910183541"></a><a name="p5568910183541"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p48428590183541"><a name="p48428590183541"></a><a name="p48428590183541"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.3 "><p id="p30401735183541"><a name="p30401735183541"></a><a name="p30401735183541"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.75%" headers="mcps1.1.5.1.4 "><p id="p46621440183541"><a name="p46621440183541"></a><a name="p46621440183541"></a>Operator (case-sensitive). Possible values are:</p>
    <p id="p35549830192731"><a name="p35549830192731"></a><a name="p35549830192731"></a><strong id="b842352706113353"><a name="b842352706113353"></a><a name="b842352706113353"></a>create</strong>: indicates creating tags. A tag will be created when no tag with the same key exists.</p>
    <p id="p4070115192755"><a name="p4070115192755"></a><a name="p4070115192755"></a><strong id="b842352706113449"><a name="b842352706113449"></a><a name="b842352706113449"></a>update</strong>: indicates updating tags. A tag will be created when no tag with the same key exists.</p>
    <p id="p18240257183541"><a name="p18240257183541"></a><a name="p18240257183541"></a><strong id="b842352706154310"><a name="b842352706154310"></a><a name="b842352706154310"></a>delete</strong>: indicates deleting tags.</p>
    </td>
    </tr>
    <tr id="row29944588183541"><td class="cellrowborder" valign="top" width="21.42%" headers="mcps1.1.5.1.1 "><p id="p9592589183541"><a name="p9592589183541"></a><a name="p9592589183541"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p38802283183541"><a name="p38802283183541"></a><a name="p38802283183541"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.3 "><p id="p55977229183541"><a name="p55977229183541"></a><a name="p55977229183541"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.75%" headers="mcps1.1.5.1.4 "><p id="p37861724183541"><a name="p37861724183541"></a><a name="p37861724183541"></a>List of tags you want to operate</p>
    </td>
    </tr>
    <tr id="row5211199183541"><td class="cellrowborder" valign="top" width="21.42%" headers="mcps1.1.5.1.1 "><p id="p19454012183541"><a name="p19454012183541"></a><a name="p19454012183541"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p32271129183541"><a name="p32271129183541"></a><a name="p32271129183541"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.3 "><p id="p63824638183541"><a name="p63824638183541"></a><a name="p63824638183541"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.75%" headers="mcps1.1.5.1.4 "><p id="p2413204183541"><a name="p2413204183541"></a><a name="p2413204183541"></a>Tag key. It cannot be left null. When <strong id="b842352706172029"><a name="b842352706172029"></a><a name="b842352706172029"></a>action</strong>&nbsp;is&nbsp;<strong id="b842352706172035"><a name="b842352706172035"></a><a name="b842352706172035"></a>create</strong>&nbsp;or&nbsp;<strong id="b842352706191216"><a name="b842352706191216"></a><a name="b842352706191216"></a>update</strong>, the maximum length of a tag key is 36 characters; when&nbsp;<strong id="b842352706172051"><a name="b842352706172051"></a><a name="b842352706172051"></a>action</strong>&nbsp;is&nbsp;<strong id="b842352706172056"><a name="b842352706172056"></a><a name="b842352706172056"></a>delete</strong>, that is 127 characters.&nbsp;A tag key cannot contain non-printable ASCII characters (0-31) and the following special characters: =*&lt;&gt;\,|/</p>
    </td>
    </tr>
    <tr id="row21718841183541"><td class="cellrowborder" valign="top" width="21.42%" headers="mcps1.1.5.1.1 "><p id="p14395674183541"><a name="p14395674183541"></a><a name="p14395674183541"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p25198977183541"><a name="p25198977183541"></a><a name="p25198977183541"></a>No (mandatory when <strong id="b842352706211644"><a name="b842352706211644"></a><a name="b842352706211644"></a>action</strong>&nbsp;is set to&nbsp;<strong id="b84235270616530"><a name="b84235270616530"></a><a name="b84235270616530"></a>create</strong>&nbsp;and optional when&nbsp;<strong id="b842352706211644_1"><a name="b842352706211644_1"></a><a name="b842352706211644_1"></a>action</strong>&nbsp;is set to&nbsp;<strong id="b842352706211650"><a name="b842352706211650"></a><a name="b842352706211650"></a>delete</strong>)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.3 "><p id="p27851219183541"><a name="p27851219183541"></a><a name="p27851219183541"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.75%" headers="mcps1.1.5.1.4 "><p id="p41356282183541"><a name="p41356282183541"></a><a name="p41356282183541"></a>Tag value. When <strong id="b842352706172029_1"><a name="b842352706172029_1"></a><a name="b842352706172029_1"></a>action</strong>&nbsp;is&nbsp;<strong id="b842352706172035_1"><a name="b842352706172035_1"></a><a name="b842352706172035_1"></a>create</strong>&nbsp;or&nbsp;<strong id="b84235270619134"><a name="b84235270619134"></a><a name="b84235270619134"></a>update</strong>, the maximum length of a tag value is 43 characters; when&nbsp;<strong id="b842352706172051_1"><a name="b842352706172051_1"></a><a name="b842352706172051_1"></a>action</strong>&nbsp;is&nbsp;<strong id="b842352706172056_1"><a name="b842352706172056_1"></a><a name="b842352706172056_1"></a>delete</strong>, that is 255 characters.&nbsp;A tag value can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "action":"delete",
        "tags":[{
            "key":"0f187b65-8d0e-4fc0-9096-3b55d330531e",
            "value":"volume"
            },{
            "key":"0f187b65-8d0e-4fc0-9096-3b55d330531d",
            "value":"volume"
        }]
    }
    ```


## Response<a name="section54881489"></a>

-   Parameter description

    <a name="table2553741120254"></a>
    <table><thead align="left"><tr id="row84520220254"><th class="cellrowborder" valign="top" width="24.72%" id="mcps1.1.4.1.1"><p id="p2604058769"><a name="p2604058769"></a><a name="p2604058769"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.18%" id="mcps1.1.4.1.2"><p id="p560416581616"><a name="p560416581616"></a><a name="p560416581616"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.1%" id="mcps1.1.4.1.3"><p id="p96041581567"><a name="p96041581567"></a><a name="p96041581567"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4113847020254"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.1.4.1.1 "><p id="p4388173520254"><a name="p4388173520254"></a><a name="p4388173520254"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.1.4.1.2 "><p id="p534483917131"><a name="p534483917131"></a><a name="p534483917131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.1.4.1.3 "><p id="p1103955520254"><a name="p1103955520254"></a><a name="p1103955520254"></a>Error message returned after an error occurs</p>
    </td>
    </tr>
    <tr id="row3224713720254"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.1.4.1.1 "><p id="p6188131520254"><a name="p6188131520254"></a><a name="p6188131520254"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.1.4.1.2 "><p id="p3027879417131"><a name="p3027879417131"></a><a name="p3027879417131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.1.4.1.3 "><p id="p6179451720254"><a name="p6179451720254"></a><a name="p6179451720254"></a>Error code returned after an error occurs</p>
    <p id="p1927974620254"><a name="p1927974620254"></a><a name="p1927974620254"></a>For details about error codes, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "error": {
            "message": "XXXX",
            "code": "XXX"
        }
    }
    ```


## Status Codes<a name="section24171358"></a>

-   Normal

    204

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

