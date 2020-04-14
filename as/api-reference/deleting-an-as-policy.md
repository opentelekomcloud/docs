# Deleting an AS Policy<a name="EN-US_TOPIC_0043063065"></a>

## Function<a name="section52228449"></a>

This interface is used to delete a specified AS policy.

## URI<a name="section294000"></a>

DELETE /autoscaling-api/v1/\{project\_id\}/scaling\_policy/\{scaling\_policy\_id\}

**Table  1**  Parameter description

<a name="table27228238"></a>
<table><thead align="left"><tr id="row23955663"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.1"><p id="p61360575"><a name="p61360575"></a><a name="p61360575"></a><strong id="b139824360598"><a name="b139824360598"></a><a name="b139824360598"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p4150696"><a name="p4150696"></a><a name="p4150696"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p662065"><a name="p662065"></a><a name="p662065"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="40%" id="mcps1.2.5.1.4"><p id="p53627266"><a name="p53627266"></a><a name="p53627266"></a><strong id="b9479153795910"><a name="b9479153795910"></a><a name="b9479153795910"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row48841284"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p63829918"><a name="p63829918"></a><a name="p63829918"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p2840889"><a name="p2840889"></a><a name="p2840889"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p28785469"><a name="p28785469"></a><a name="p28785469"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row46641368"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p19854472"><a name="p19854472"></a><a name="p19854472"></a>scaling_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p64708380"><a name="p64708380"></a><a name="p64708380"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p6887421"><a name="p6887421"></a><a name="p6887421"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p21010194"><a name="p21010194"></a><a name="p21010194"></a>Specifies the AS policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section2646004"></a>

-   Request parameters

    None

-   Example request

    This example shows how to delete the AS policy with ID  **906f73ff-56e8-41b2-a005-8157d0c60361**.

    ```
    DELETE https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_policy/906f73ff-56e8-41b2-a005-8157d0c60361
    ```


## Response Message<a name="section23814038"></a>

-   Response parameters

    None

-   Example response

    None


## Returned Values<a name="section12999751"></a>

-   Normal

    204

-   Abnormal

    <a name="table10983475"></a>
    <table><thead align="left"><tr id="row23209052"><th class="cellrowborder" valign="top" width="43.61%" id="mcps1.1.3.1.1"><p id="p885082"><a name="p885082"></a><a name="p885082"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.38999999999999%" id="mcps1.1.3.1.2"><p id="p4582792"><a name="p4582792"></a><a name="p4582792"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35661838"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p2927765"><a name="p2927765"></a><a name="p2927765"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p35822404"><a name="p35822404"></a><a name="p35822404"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row53966187"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p9185002"><a name="p9185002"></a><a name="p9185002"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p5787686"><a name="p5787686"></a><a name="p5787686"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row52089174"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p58473527"><a name="p58473527"></a><a name="p58473527"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p38735241"><a name="p38735241"></a><a name="p38735241"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row13072851"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p52268049"><a name="p52268049"></a><a name="p52268049"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p5853587"><a name="p5853587"></a><a name="p5853587"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row52682290"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p39407061"><a name="p39407061"></a><a name="p39407061"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p37855410"><a name="p37855410"></a><a name="p37855410"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row5154373"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p14851049"><a name="p14851049"></a><a name="p14851049"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p62084314"><a name="p62084314"></a><a name="p62084314"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row21887914"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p28090616"><a name="p28090616"></a><a name="p28090616"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p60747463"><a name="p60747463"></a><a name="p60747463"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row9856263"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p60159801"><a name="p60159801"></a><a name="p60159801"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p41105728"><a name="p41105728"></a><a name="p41105728"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row34407239"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p35522984"><a name="p35522984"></a><a name="p35522984"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p58789457"><a name="p58789457"></a><a name="p58789457"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row59343073"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p42059594"><a name="p42059594"></a><a name="p42059594"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p51383952"><a name="p51383952"></a><a name="p51383952"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row59802385"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p12154988"><a name="p12154988"></a><a name="p12154988"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p45029976"><a name="p45029976"></a><a name="p45029976"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row2616604"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p10618339"><a name="p10618339"></a><a name="p10618339"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p54779151"><a name="p54779151"></a><a name="p54779151"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row23250319"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p4227661"><a name="p4227661"></a><a name="p4227661"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p6896227"><a name="p6896227"></a><a name="p6896227"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row62066047"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p61293901"><a name="p61293901"></a><a name="p61293901"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p65858952"><a name="p65858952"></a><a name="p65858952"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

