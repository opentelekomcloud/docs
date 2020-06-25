# Associating Resources with a Backup Policy<a name="EN-US_TOPIC_0043410561"></a>

## Function<a name="section63962185"></a>

This interface is used to associate one or more resources with a backup policy.

## URI<a name="section38788755"></a>

-   URI format

    POST /v2/\{project\_id\}/backuppolicyresources

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
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p1749919435171"><a name="p1749919435171"></a><a name="p1749919435171"></a>Project ID</p>
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
    <tbody><tr id="row54696960135436"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p1268755135436"><a name="p1268755135436"></a><a name="p1268755135436"></a>backup_policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p35660302135436"><a name="p35660302135436"></a><a name="p35660302135436"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p2803354135436"><a name="p2803354135436"></a><a name="p2803354135436"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p25745118135436"><a name="p25745118135436"></a><a name="p25745118135436"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row20300660135439"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p33740768135439"><a name="p33740768135439"></a><a name="p33740768135439"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p48647684135439"><a name="p48647684135439"></a><a name="p48647684135439"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p48148361135439"><a name="p48148361135439"></a><a name="p48148361135439"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p7703191135439"><a name="p7703191135439"></a><a name="p7703191135439"></a>Information about the associated resource</p>
    </td>
    </tr>
    <tr id="row187031441791"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p385596811791"><a name="p385596811791"></a><a name="p385596811791"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p363264551791"><a name="p363264551791"></a><a name="p363264551791"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p567617131791"><a name="p567617131791"></a><a name="p567617131791"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p663915513410"><a name="p663915513410"></a><a name="p663915513410"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row50598521"><td class="cellrowborder" valign="top" width="26.697330266973307%" headers="mcps1.1.5.1.1 "><p id="p44217312144451"><a name="p44217312144451"></a><a name="p44217312144451"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.968703129687032%" headers="mcps1.1.5.1.2 "><p id="p56460178"><a name="p56460178"></a><a name="p56460178"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35836416358364%" headers="mcps1.1.5.1.3 "><p id="p1152258104112"><a name="p1152258104112"></a><a name="p1152258104112"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97560243975603%" headers="mcps1.1.5.1.4 "><p id="p9871675"><a name="p9871675"></a><a name="p9871675"></a>Resource type, which can only be</p>
    <a name="ul39729095135536"></a><a name="ul39729095135536"></a><ul id="ul39729095135536"><li>volume</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "backup_policy_id":"915d1fd8-63cb-4054-a2b0-2778210e3a75",
        "resources":[{
            "resource_id":"0f187b65-8d0e-4fc0-9096-3b55d330531e",
            "resource_type":"volume"
            },{
            "resource_id":"0f187b65-8d0e-4fc0-9096-3b55d330531d",
            "resource_type":"volume"
        }]
    }
    ```


## Response<a name="section54881489"></a>

-   Parameter description

    <a name="table2553741120254"></a>
    <table><thead align="left"><tr id="row84520220254"><th class="cellrowborder" valign="top" width="29.182918291829186%" id="mcps1.1.4.1.1"><p id="p119011542194118"><a name="p119011542194118"></a><a name="p119011542194118"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.471547154715473%" id="mcps1.1.4.1.2"><p id="p1791720422411"><a name="p1791720422411"></a><a name="p1791720422411"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.345534553455344%" id="mcps1.1.4.1.3"><p id="p1991710420411"><a name="p1991710420411"></a><a name="p1991710420411"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row894248020254"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p34048608151944"><a name="p34048608151944"></a><a name="p34048608151944"></a>success_resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p4563373217131"><a name="p4563373217131"></a><a name="p4563373217131"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p1948402220254"><a name="p1948402220254"></a><a name="p1948402220254"></a>List of successfully associated resources</p>
    </td>
    </tr>
    <tr id="row3672267314750"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p2174653814750"><a name="p2174653814750"></a><a name="p2174653814750"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p3334646914827"><a name="p3334646914827"></a><a name="p3334646914827"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p1670948714827"><a name="p1670948714827"></a><a name="p1670948714827"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row5182283914185"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p3690039614185"><a name="p3690039614185"></a><a name="p3690039614185"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p4182715614185"><a name="p4182715614185"></a><a name="p4182715614185"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p3255643814185"><a name="p3255643814185"></a><a name="p3255643814185"></a>Resource type</p>
    </td>
    </tr>
    <tr id="row39803290161322"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p49744334161337"><a name="p49744334161337"></a><a name="p49744334161337"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p50980705161322"><a name="p50980705161322"></a><a name="p50980705161322"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p35796472161322"><a name="p35796472161322"></a><a name="p35796472161322"></a>AZ to which the resource belongs</p>
    </td>
    </tr>
    <tr id="row30624379161326"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p51300887161344"><a name="p51300887161344"></a><a name="p51300887161344"></a>os_vol_host_attr</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p10645677161326"><a name="p10645677161326"></a><a name="p10645677161326"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p56993489161326"><a name="p56993489161326"></a><a name="p56993489161326"></a>Point of delivery (POD) to which the resource belongs</p>
    </td>
    </tr>
    <tr id="row958813314845"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p123148821495"><a name="p123148821495"></a><a name="p123148821495"></a>fail_resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p659806001495"><a name="p659806001495"></a><a name="p659806001495"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p428284081495"><a name="p428284081495"></a><a name="p428284081495"></a>List of the resources that fail to be associated</p>
    </td>
    </tr>
    <tr id="row360840251490"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p162881861495"><a name="p162881861495"></a><a name="p162881861495"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p294768701495"><a name="p294768701495"></a><a name="p294768701495"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p388162951495"><a name="p388162951495"></a><a name="p388162951495"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row53090096143137"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p58456527143140"><a name="p58456527143140"></a><a name="p58456527143140"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p6115899143140"><a name="p6115899143140"></a><a name="p6115899143140"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p25625836143140"><a name="p25625836143140"></a><a name="p25625836143140"></a>Resource type</p>
    </td>
    </tr>
    <tr id="row21260704161354"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p6370218016143"><a name="p6370218016143"></a><a name="p6370218016143"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p25924749161354"><a name="p25924749161354"></a><a name="p25924749161354"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p25799631161440"><a name="p25799631161440"></a><a name="p25799631161440"></a>AZ to which the resource belongs</p>
    </td>
    </tr>
    <tr id="row51996891161357"><td class="cellrowborder" valign="top" width="29.182918291829186%" headers="mcps1.1.4.1.1 "><p id="p6666443616143"><a name="p6666443616143"></a><a name="p6666443616143"></a>os_vol_host_attr</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.471547154715473%" headers="mcps1.1.4.1.2 "><p id="p64355875161357"><a name="p64355875161357"></a><a name="p64355875161357"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.345534553455344%" headers="mcps1.1.4.1.3 "><p id="p17449444161440"><a name="p17449444161440"></a><a name="p17449444161440"></a>POD to which the resource belongs</p>
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
        "success_resources": [
            {
                "resource_id": "bce8d47a-af17-4169-901f-4c7ae9f29c2c",
                "os_vol_host_attr": "pod01.eu-de-01",
                "availability_zone": "eu-de-01",
                "resource_type": "volume"
            }
        ], 
        "fail_resources": [ ]
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

