# Deleting an AS Group<a name="EN-US_TOPIC_0043063041"></a>

## Function<a name="section6292375"></a>

This interface is used to delete a specified AS group.

-   **force\_delete**  specifies whether to forcibly delete an AS group, remove the ECS instances and release them when the AS group is running instances or performing scaling actions. By default, its value is  **no**, which means not to forcibly delete the AS group.
-   If the value of  **force\_delete**  is set to  **no**, the AS group can be deleted only when both the following conditions are met:
    -   The AS group is performing no scaling action.
    -   The number of running ECS instances \(**current\_instance\_number**\) is  **0**.


-   If the value of  **force\_delete**  is set to  **yes**, the AS group enters the  **DELETING**  state, rejecting new requests for scaling actions while completing the existing scaling actions. Then, all ECS instances are removed from the AS group and the AS group is deleted. Note that the manually added ECS instances will be removed from the AS group and the ECS instances automatically created by AS will be automatically deleted.

## URI<a name="section56631376"></a>

DELETE /autoscaling-api/v1/\{project\_id\}/scaling\_group/\{scaling\_group\_id\}?force\_delete=no

**Table  1**  Parameter description

<a name="table37235194"></a>
<table><thead align="left"><tr id="row2211792"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.1"><p id="p44937496"><a name="p44937496"></a><a name="p44937496"></a><strong id="b78081348143812"><a name="b78081348143812"></a><a name="b78081348143812"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p16058544"><a name="p16058544"></a><a name="p16058544"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p25673664"><a name="p25673664"></a><a name="p25673664"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p66300913"><a name="p66300913"></a><a name="p66300913"></a><strong id="b214155018380"><a name="b214155018380"></a><a name="b214155018380"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1664874"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p637140"><a name="p637140"></a><a name="p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p51608407"><a name="p51608407"></a><a name="p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p19531418"><a name="p19531418"></a><a name="p19531418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row11324657"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p44882061"><a name="p44882061"></a><a name="p44882061"></a>scaling_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p11568292"><a name="p11568292"></a><a name="p11568292"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p64616480"><a name="p64616480"></a><a name="p64616480"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p66552425"><a name="p66552425"></a><a name="p66552425"></a>Specifies the AS group ID.</p>
</td>
</tr>
<tr id="row28118938103444"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p33651750103458"><a name="p33651750103458"></a><a name="p33651750103458"></a>force_delete</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p41437229103458"><a name="p41437229103458"></a><a name="p41437229103458"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p972380103458"><a name="p972380103458"></a><a name="p972380103458"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p8494439174810"><a name="p8494439174810"></a><a name="p8494439174810"></a>Specifies whether to forcibly delete an AS group. Options:</p>
<a name="ul87011242493"></a><a name="ul87011242493"></a><ul id="ul87011242493"><li><strong id="b19703443286"><a name="b19703443286"></a><a name="b19703443286"></a>no</strong> (default): indicates that the AS group is not forcibly deleted.</li><li><strong id="b293019512285"><a name="b293019512285"></a><a name="b293019512285"></a>yes</strong>: indicates to forcibly delete an AS group.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section39920339"></a>

-   Request parameters

    None

-   Example request

    This example shows how to forcibly delete the AS group with ID  **a8327883-6b07-4497-9c61-68d03ee193a1**.

    ```
    DELETE https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group/a8327883-6b07-4497-9c61-68d03ee193a1?force_delete=yes
    ```


## Response Message<a name="section23738738"></a>

-   Response parameters

    None

-   Example response

    None


## Returned Values<a name="section12322052"></a>

-   Normal

    204

-   Abnormal

    <a name="table40541937"></a>
    <table><thead align="left"><tr id="row53487552"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p37524445"><a name="p37524445"></a><a name="p37524445"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p19581186"><a name="p19581186"></a><a name="p19581186"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42572248"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p25800070"><a name="p25800070"></a><a name="p25800070"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p9430965"><a name="p9430965"></a><a name="p9430965"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row17769829"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p30070007"><a name="p30070007"></a><a name="p30070007"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p19751518"><a name="p19751518"></a><a name="p19751518"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row43545941"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p37560342"><a name="p37560342"></a><a name="p37560342"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p22488863"><a name="p22488863"></a><a name="p22488863"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1073183"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p19818984"><a name="p19818984"></a><a name="p19818984"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p61833870"><a name="p61833870"></a><a name="p61833870"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row19633919"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p46843578"><a name="p46843578"></a><a name="p46843578"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p36233478"><a name="p36233478"></a><a name="p36233478"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row57665850"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p40422241"><a name="p40422241"></a><a name="p40422241"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p52976109"><a name="p52976109"></a><a name="p52976109"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row7022941"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p31987323"><a name="p31987323"></a><a name="p31987323"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p40836337"><a name="p40836337"></a><a name="p40836337"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row31982717"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p40463275"><a name="p40463275"></a><a name="p40463275"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p56299846"><a name="p56299846"></a><a name="p56299846"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row36936567"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p39071968"><a name="p39071968"></a><a name="p39071968"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p10712809"><a name="p10712809"></a><a name="p10712809"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row29306417"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p25009549"><a name="p25009549"></a><a name="p25009549"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p12507614"><a name="p12507614"></a><a name="p12507614"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row45459670"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p58354673"><a name="p58354673"></a><a name="p58354673"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p29108085"><a name="p29108085"></a><a name="p29108085"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row60646173"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p13392976"><a name="p13392976"></a><a name="p13392976"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p11089280"><a name="p11089280"></a><a name="p11089280"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row32694658"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p31021623"><a name="p31021623"></a><a name="p31021623"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p29723549"><a name="p29723549"></a><a name="p29723549"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row66185354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p59413435"><a name="p59413435"></a><a name="p59413435"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p47758962"><a name="p47758962"></a><a name="p47758962"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

