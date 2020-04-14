# Deleting a Tag of a Backup Policy<a name="EN-US_TOPIC_0098527677"></a>

## Function<a name="section108351649184010"></a>

This interface is used to delete a tag of a backup policy.

## URI<a name="section20183144811183"></a>

-   URI format

    DELETE /v2/\{project\_id\}/backuppolicy/\{policy\_id\}/tags/\{key\}

-   Parameter description

    <a name="table14190134812183"></a>
    <table><thead align="left"><tr id="row919494861812"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p1519410487188"><a name="p1519410487188"></a><a name="p1519410487188"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p19196144831810"><a name="p19196144831810"></a><a name="p19196144831810"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p21981348181815"><a name="p21981348181815"></a><a name="p21981348181815"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row21989482185"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p18202134820189"><a name="p18202134820189"></a><a name="p18202134820189"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p92045489189"><a name="p92045489189"></a><a name="p92045489189"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p17206248171815"><a name="p17206248171815"></a><a name="p17206248171815"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row49177768142544"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p23976272142544"><a name="p23976272142544"></a><a name="p23976272142544"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p63029893142544"><a name="p63029893142544"></a><a name="p63029893142544"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p5147694142544"><a name="p5147694142544"></a><a name="p5147694142544"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row53206241954"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1732019245512"><a name="p1732019245512"></a><a name="p1732019245512"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p14320122419511"><a name="p14320122419511"></a><a name="p14320122419511"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p1083805315049"><a name="p1083805315049"></a><a name="p1083805315049"></a>Tag key</p>
    <div class="note" id="note2907504615142"><a name="note2907504615142"></a><a name="note2907504615142"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p6002113015142"><a name="p6002113015142"></a><a name="p6002113015142"></a>If the key contains special characters, encode it using ASCII first.</p>
    <p id="p2165614015240"><a name="p2165614015240"></a><a name="p2165614015240"></a>For example, the number sign (#) will be displayed as <strong id="b929615181459"><a name="b929615181459"></a><a name="b929615181459"></a>%23</strong> after encoding.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section18213184812181"></a>

-   Example request

    ```
    DELETE /v2/{project_id}/backuppolicy/{policy_id}/tags/{key}
    ```


## Response<a name="section8277104817184"></a>

-   Parameter description

    <a name="table112811848161817"></a>
    <table><thead align="left"><tr id="row1128594817182"><th class="cellrowborder" valign="top" width="24.72%" id="mcps1.1.4.1.1"><p id="p1431817452527"><a name="p1431817452527"></a><a name="p1431817452527"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.18%" id="mcps1.1.4.1.2"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.1%" id="mcps1.1.4.1.3"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row22921348151817"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.1.4.1.1 "><p id="p4295248131816"><a name="p4295248131816"></a><a name="p4295248131816"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.1.4.1.2 "><p id="p122991448181818"><a name="p122991448181818"></a><a name="p122991448181818"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.1.4.1.3 "><p id="p2300204817183"><a name="p2300204817183"></a><a name="p2300204817183"></a>Error message returned after an error occurs</p>
    </td>
    </tr>
    <tr id="row13301114816189"><td class="cellrowborder" valign="top" width="24.72%" headers="mcps1.1.4.1.1 "><p id="p130215483188"><a name="p130215483188"></a><a name="p130215483188"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.1.4.1.2 "><p id="p17305144813183"><a name="p17305144813183"></a><a name="p17305144813183"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.1.4.1.3 "><p id="p173061448101814"><a name="p173061448101814"></a><a name="p173061448101814"></a>Error code returned after an error occurs</p>
    <p id="p730816482184"><a name="p730816482184"></a><a name="p730816482184"></a>For details about error codes, see <a href="error-codes.md">Error Codes</a>.</p>
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


## Status Codes<a name="section10992114984011"></a>

-   Normal

    204

-   Abnormal

    <a name="table20999649174011"></a>
    <table><thead align="left"><tr id="row55350114010"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p15825012406"><a name="p15825012406"></a><a name="p15825012406"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p211185014408"><a name="p211185014408"></a><a name="p211185014408"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row714185044010"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p14164502401"><a name="p14164502401"></a><a name="p14164502401"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1318450114013"><a name="p1318450114013"></a><a name="p1318450114013"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row02018506406"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p22135044019"><a name="p22135044019"></a><a name="p22135044019"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p122315014020"><a name="p122315014020"></a><a name="p122315014020"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row2251150134015"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1925150174011"><a name="p1925150174011"></a><a name="p1925150174011"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p8274503409"><a name="p8274503409"></a><a name="p8274503409"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1227650164012"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1228050104013"><a name="p1228050104013"></a><a name="p1228050104013"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5295509400"><a name="p5295509400"></a><a name="p5295509400"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row23175011403"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p23213504402"><a name="p23213504402"></a><a name="p23213504402"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p43516501404"><a name="p43516501404"></a><a name="p43516501404"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row83611502407"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p16383504401"><a name="p16383504401"></a><a name="p16383504401"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p104055019400"><a name="p104055019400"></a><a name="p104055019400"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row540650124015"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2042165011405"><a name="p2042165011405"></a><a name="p2042165011405"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p144475018402"><a name="p144475018402"></a><a name="p144475018402"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row184415074019"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p8466501405"><a name="p8466501405"></a><a name="p8466501405"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p144818507405"><a name="p144818507405"></a><a name="p144818507405"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row1149175014019"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p165115044016"><a name="p165115044016"></a><a name="p165115044016"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p15551750184018"><a name="p15551750184018"></a><a name="p15551750184018"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row25555064015"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1357750144020"><a name="p1357750144020"></a><a name="p1357750144020"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4582050164011"><a name="p4582050164011"></a><a name="p4582050164011"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row659750124014"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1160105024013"><a name="p1160105024013"></a><a name="p1160105024013"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p46211509405"><a name="p46211509405"></a><a name="p46211509405"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row46495020409"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p96516502405"><a name="p96516502405"></a><a name="p96516502405"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p568175064017"><a name="p568175064017"></a><a name="p568175064017"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row569125054014"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p67255010404"><a name="p67255010404"></a><a name="p67255010404"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p47325016407"><a name="p47325016407"></a><a name="p47325016407"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row6736506407"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p19751750174013"><a name="p19751750174013"></a><a name="p19751750174013"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p376150114013"><a name="p376150114013"></a><a name="p376150114013"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

