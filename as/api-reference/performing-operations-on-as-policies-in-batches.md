# Performing Operations on AS Policies in Batches<a name="EN-US_TOPIC_0105593193"></a>

## Function<a name="section10263773"></a>

This interface is used to enable, disable, or delete AS policies in batches.

-   A batch operation can be performed on a maximum of 20 AS policies at a time.

## URI<a name="section25265097"></a>

POST /autoscaling-api/v1/\{project\_id\}/scaling\_policies/action

**Table  1**  Parameter description

<a name="table10023380"></a>
<table><thead align="left"><tr id="row17946858"><th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.5.1.1"><p id="p44409397"><a name="p44409397"></a><a name="p44409397"></a><strong id="b1433165413591"><a name="b1433165413591"></a><a name="b1433165413591"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.2"><p id="p40391380"><a name="p40391380"></a><a name="p40391380"></a><strong id="b842352706141528"><a name="b842352706141528"></a><a name="b842352706141528"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.3"><p id="p50476336"><a name="p50476336"></a><a name="p50476336"></a><strong id="b84235270693914"><a name="b84235270693914"></a><a name="b84235270693914"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41.584158415841586%" id="mcps1.2.5.1.4"><p id="p62051376"><a name="p62051376"></a><a name="p62051376"></a><strong id="b499105510591"><a name="b499105510591"></a><a name="b499105510591"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row60105532"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.1 "><p id="p36709949"><a name="p36709949"></a><a name="p36709949"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p20715931"><a name="p20715931"></a><a name="p20715931"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.3 "><p id="p268861"><a name="p268861"></a><a name="p268861"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.584158415841586%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section42782262104146"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table60799090"></a>
    <table><thead align="left"><tr id="row8858194"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p46425119"><a name="p46425119"></a><a name="p46425119"></a><strong id="b355175615599"><a name="b355175615599"></a><a name="b355175615599"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.2"><p id="p2338313"><a name="p2338313"></a><a name="p2338313"></a><strong id="b718281895"><a name="b718281895"></a><a name="b718281895"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p55185655"><a name="p55185655"></a><a name="p55185655"></a><strong id="b527450907"><a name="b527450907"></a><a name="b527450907"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41%" id="mcps1.2.5.1.4"><p id="p40853074"><a name="p40853074"></a><a name="p40853074"></a><strong id="b188775995912"><a name="b188775995912"></a><a name="b188775995912"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20764673"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p4216941"><a name="p4216941"></a><a name="p4216941"></a>scaling_policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.2 "><p id="p6027901"><a name="p6027901"></a><a name="p6027901"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p18497945"><a name="p18497945"></a><a name="p18497945"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.4 "><p id="p21938602"><a name="p21938602"></a><a name="p21938602"></a>Specifies the AS policy ID.</p>
    </td>
    </tr>
    <tr id="row416365216942"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p4883500616945"><a name="p4883500616945"></a><a name="p4883500616945"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.2 "><p id="p6332141216945"><a name="p6332141216945"></a><a name="p6332141216945"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p2876071816945"><a name="p2876071816945"></a><a name="p2876071816945"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.4 "><p id="p52855456104651"><a name="p52855456104651"></a><a name="p52855456104651"></a>Specifies an action to be performed on AS policies in batches. The options are as follows:</p>
    <a name="ul23014345104621"></a><a name="ul23014345104621"></a><ul id="ul23014345104621"><li><strong id="b16734192141618"><a name="b16734192141618"></a><a name="b16734192141618"></a>delete</strong>: deletes AS policies.</li><li><strong id="b84235270617755"><a name="b84235270617755"></a><a name="b84235270617755"></a>resume</strong>: enables AS policies.</li><li><strong id="b8423527061784"><a name="b8423527061784"></a><a name="b8423527061784"></a>pause</strong>: disables AS policies.</li></ul>
    </td>
    </tr>
    <tr id="row1888584433413"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p1754244916917"><a name="p1754244916917"></a><a name="p1754244916917"></a>force_delete</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.2 "><p id="p1165227516917"><a name="p1165227516917"></a><a name="p1165227516917"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p431024216917"><a name="p431024216917"></a><a name="p431024216917"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.4 "><p id="p1256132114711"><a name="p1256132114711"></a><a name="p1256132114711"></a>Specifies whether to forcibly delete an AS policy. If the value is set to <strong id="b54151328135418"><a name="b54151328135418"></a><a name="b54151328135418"></a>no</strong>, in-progress AS policies cannot be deleted. Options:</p>
    <a name="ul1463112774710"></a><a name="ul1463112774710"></a><ul id="ul1463112774710"><li><strong id="b48691541543"><a name="b48691541543"></a><a name="b48691541543"></a>no</strong> (default): indicates that the AS policy is not forcibly deleted.</li><li><strong id="b9938131365518"><a name="b9938131365518"></a><a name="b9938131365518"></a>yes</strong>: indicates that the AS policy is forcibly deleted.</li></ul>
    <p id="p61828895105430"><a name="p61828895105430"></a><a name="p61828895105430"></a>This parameter is available only when <strong id="b273152918148"><a name="b273152918148"></a><a name="b273152918148"></a>action</strong> is set to <strong id="b47314292147"><a name="b47314292147"></a><a name="b47314292147"></a>delete</strong>.</p>
    </td>
    </tr>
    <tr id="row15675420212"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p2252119229"><a name="p2252119229"></a><a name="p2252119229"></a>delete_alarm</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.2 "><p id="p725101122210"><a name="p725101122210"></a><a name="p725101122210"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p6253152211"><a name="p6253152211"></a><a name="p6253152211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.4 "><p id="p102571112217"><a name="p102571112217"></a><a name="p102571112217"></a>Specifies whether to delete the alarm rule used by the alarm policy. The value can be <strong id="b1650342519514"><a name="b1650342519514"></a><a name="b1650342519514"></a>yes</strong> or <strong id="b131741628195117"><a name="b131741628195117"></a><a name="b131741628195117"></a>no</strong> (default).</p>
    <p id="p526101132213"><a name="p526101132213"></a><a name="p526101132213"></a>This parameter is available only when <strong id="b2099542969"><a name="b2099542969"></a><a name="b2099542969"></a>action</strong> is set to <strong id="b632250777"><a name="b632250777"></a><a name="b632250777"></a>delete</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    This example shows how to enable the AS policies with IDs  **policy\_id1**  and  **policy\_id2**  in a batch.

    ```
    POST https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_policies/action
    
    {
        "action": "resume",
        "scaling_policy_id": [
            "policy_id1",
            "policy_id2"
        ]
    }
    ```


## Response Message<a name="section33206990"></a>

-   Response parameters

    None

-   Example response

    None


## Returned Values<a name="section30427456"></a>

-   Normal

    204

-   Abnormal

    <a name="table46788488"></a>
    <table><thead align="left"><tr id="row8624464"><th class="cellrowborder" valign="top" width="44.18%" id="mcps1.1.3.1.1"><p id="p27492955"><a name="p27492955"></a><a name="p27492955"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.82%" id="mcps1.1.3.1.2"><p id="p12336887"><a name="p12336887"></a><a name="p12336887"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59763787"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p9028608"><a name="p9028608"></a><a name="p9028608"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p60228670"><a name="p60228670"></a><a name="p60228670"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row5187119"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row9367865"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p20599592"><a name="p20599592"></a><a name="p20599592"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p57954280"><a name="p57954280"></a><a name="p57954280"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row51826478"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p37195178"><a name="p37195178"></a><a name="p37195178"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p60019402"><a name="p60019402"></a><a name="p60019402"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row3303707"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p66273709"><a name="p66273709"></a><a name="p66273709"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p66570199"><a name="p66570199"></a><a name="p66570199"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row62260885"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p9966935"><a name="p9966935"></a><a name="p9966935"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p2015430"><a name="p2015430"></a><a name="p2015430"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row18138873"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p59962646"><a name="p59962646"></a><a name="p59962646"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p25136147"><a name="p25136147"></a><a name="p25136147"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row24898733"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p3531486"><a name="p3531486"></a><a name="p3531486"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p17614915"><a name="p17614915"></a><a name="p17614915"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row24316508"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p23480171"><a name="p23480171"></a><a name="p23480171"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p22845731"><a name="p22845731"></a><a name="p22845731"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row4284989"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p11539844"><a name="p11539844"></a><a name="p11539844"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p62312200"><a name="p62312200"></a><a name="p62312200"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row23938892"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p60002101"><a name="p60002101"></a><a name="p60002101"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p28332047"><a name="p28332047"></a><a name="p28332047"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row53661838"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p51641620"><a name="p51641620"></a><a name="p51641620"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p22221662"><a name="p22221662"></a><a name="p22221662"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row65777232"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p26355580"><a name="p26355580"></a><a name="p26355580"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p54427232"><a name="p54427232"></a><a name="p54427232"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row20083047"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p16114131"><a name="p16114131"></a><a name="p16114131"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p30176268"><a name="p30176268"></a><a name="p30176268"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

