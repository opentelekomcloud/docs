# Removing a Specified Instance from an AS Group<a name="EN-US_TOPIC_0043063059"></a>

## Function<a name="section59572368"></a>

This interface is used to remove a specified instance from an AS group.

-   You can remove instances only in  **INSERVICE**  state and only when the number of instances after the removal is greater than or equal to the minimum number of instances allowed.

-   You can remove instances from an AS group only when no scaling action is in progress.

## URI<a name="section66389266"></a>

DELETE /autoscaling-api/v1/\{project\_id\}/scaling\_group\_instance/\{instance\_id\}?instance\_delete=yes

**Table  1**  Parameter description

<a name="table17907785"></a>
<table><thead align="left"><tr id="row64797609"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p14114947"><a name="p14114947"></a><a name="p14114947"></a><strong id="b161962195212"><a name="b161962195212"></a><a name="b161962195212"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p2460041"><a name="p2460041"></a><a name="p2460041"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p65045669"><a name="p65045669"></a><a name="p65045669"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="p34207804"><a name="p34207804"></a><a name="p34207804"></a><strong id="b93712365216"><a name="b93712365216"></a><a name="b93712365216"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19368760"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p25365761"><a name="p25365761"></a><a name="p25365761"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p41360766"><a name="p41360766"></a><a name="p41360766"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p61887768"><a name="p61887768"></a><a name="p61887768"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row19026538"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p64754634"><a name="p64754634"></a><a name="p64754634"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p10634019"><a name="p10634019"></a><a name="p10634019"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p56049180"><a name="p56049180"></a><a name="p56049180"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p43689693"><a name="p43689693"></a><a name="p43689693"></a>Specifies the instance ID. For details, see <a href="querying-instances-in-an-as-group.md">Querying Instances in an AS Group</a>.</p>
</td>
</tr>
<tr id="row57662920"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p40184969"><a name="p40184969"></a><a name="p40184969"></a>instance_delete</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p33757095"><a name="p33757095"></a><a name="p33757095"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p49970185"><a name="p49970185"></a><a name="p49970185"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p18389193518112"><a name="p18389193518112"></a><a name="p18389193518112"></a>Specifies whether an instance is deleted when it is removed from the AS group.</p>
<p id="p11671043414"><a name="p11671043414"></a><a name="p11671043414"></a>Options:</p>
<a name="ul1072017441112"></a><a name="ul1072017441112"></a><ul id="ul1072017441112"><li><strong id="b18912471083"><a name="b18912471083"></a><a name="b18912471083"></a>no</strong> (default): The instance will not be deleted.</li><li><strong id="b15582714914"><a name="b15582714914"></a><a name="b15582714914"></a>yes</strong>: The instance will be deleted.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section60632485"></a>

-   Request parameters

    None

-   Example request

    This example shows how to remove but not delete the instance with ID  **b25c1589-c96c-465b-9fef-d06540d1945c**  from an AS group.

    ```
    DELETE https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group_instance/b25c1589-c96c-465b-9fef-d06540d1945c?instance_delete=no
    ```


## Response Message<a name="section8821459"></a>

-   Response parameters

    None

-   Example response

    None


## Returned Values<a name="section12284267"></a>

-   Normal

    204

-   Abnormal

    <a name="table50448354"></a>
    <table><thead align="left"><tr id="row29530116"><th class="cellrowborder" valign="top" width="43.99%" id="mcps1.1.3.1.1"><p id="p43129175"><a name="p43129175"></a><a name="p43129175"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.010000000000005%" id="mcps1.1.3.1.2"><p id="p3802258"><a name="p3802258"></a><a name="p3802258"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39547486"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p49229794"><a name="p49229794"></a><a name="p49229794"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p28190407"><a name="p28190407"></a><a name="p28190407"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row52387077"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p15494878"><a name="p15494878"></a><a name="p15494878"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p47125611"><a name="p47125611"></a><a name="p47125611"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row21477321"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p61941440"><a name="p61941440"></a><a name="p61941440"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p51200735"><a name="p51200735"></a><a name="p51200735"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row58153438"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p12808013"><a name="p12808013"></a><a name="p12808013"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p30816121"><a name="p30816121"></a><a name="p30816121"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row8909633"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p50591634"><a name="p50591634"></a><a name="p50591634"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p4281684"><a name="p4281684"></a><a name="p4281684"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row38535158"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p34340132"><a name="p34340132"></a><a name="p34340132"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p30087318"><a name="p30087318"></a><a name="p30087318"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row2350413"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p56165728"><a name="p56165728"></a><a name="p56165728"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p53130157"><a name="p53130157"></a><a name="p53130157"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row8409368"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p10070188"><a name="p10070188"></a><a name="p10070188"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p10378893"><a name="p10378893"></a><a name="p10378893"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row26301173"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p50020275"><a name="p50020275"></a><a name="p50020275"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p25110514"><a name="p25110514"></a><a name="p25110514"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row24668042"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p51954348"><a name="p51954348"></a><a name="p51954348"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p47552675"><a name="p47552675"></a><a name="p47552675"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row25320898"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p37726867"><a name="p37726867"></a><a name="p37726867"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p35977388"><a name="p35977388"></a><a name="p35977388"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row55361044"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p55059565"><a name="p55059565"></a><a name="p55059565"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p30639779"><a name="p30639779"></a><a name="p30639779"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row7322556"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p56256135"><a name="p56256135"></a><a name="p56256135"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p60453091"><a name="p60453091"></a><a name="p60453091"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row7206911"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p46888886"><a name="p46888886"></a><a name="p46888886"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p39903442"><a name="p39903442"></a><a name="p39903442"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

