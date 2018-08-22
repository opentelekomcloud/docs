# Deleting a Subnet<a name="EN-US_TOPIC_0020090594"></a>

## Function<a name="section36031167"></a>

This interface is used to delete a subnet.

## URI<a name="section55845053"></a>

-   DELETE /v1/\{tenant\_id\}/vpcs/\{vpc\_id\}/subnets/\{subnet\_id\}
-   Parameter description

    <a name="table23279683"></a><table><thead align="left"><tr id="row57883273"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p58033516"><a name="p58033516"></a><a name="p58033516"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p3094327"><a name="p3094327"></a><a name="p3094327"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p49313939"><a name="p49313939"></a><a name="p49313939"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35006119"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p16923420"><a name="p16923420"></a><a name="p16923420"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p28619802"><a name="p28619802"></a><a name="p28619802"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p36502600"><a name="p36502600"></a><a name="p36502600"></a>Specifies the tenant ID of the operator.</p>
    </td>
    </tr>
    <tr id="row29689498122133"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p37198247122136"><a name="p37198247122136"></a><a name="p37198247122136"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p60268063122136"><a name="p60268063122136"></a><a name="p60268063122136"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p49874919122136"><a name="p49874919122136"></a><a name="p49874919122136"></a>Specifies the ID of the subnet VPC.</p>
    </td>
    </tr>
    <tr id="row60087944"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p35285314"><a name="p35285314"></a><a name="p35285314"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p39538176"><a name="p39538176"></a><a name="p39538176"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p48475691"><a name="p48475691"></a><a name="p48475691"></a>Specifies the subnet ID, which uniquely identifies the subnet.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section32843429"></a>

-   Parameter description

    None

-   Example request

    None


## Response<a name="section27155410"></a>

Example response

```
None
```

## Returned Value<a name="section43072099"></a>

-   Normal

    204

-   Abnormal

    <a name="table5431697995418"></a><table><thead align="left"><tr id="row2941221595418"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p3357920895418"><a name="p3357920895418"></a><a name="p3357920895418"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p3556129395418"><a name="p3556129395418"></a><a name="p3556129395418"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6189246295418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4723355795418"><a name="p4723355795418"></a><a name="p4723355795418"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p71287195418"><a name="p71287195418"></a><a name="p71287195418"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row641584595418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4992141395418"><a name="p4992141395418"></a><a name="p4992141395418"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1710266295418"><a name="p1710266295418"></a><a name="p1710266295418"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1970623495418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5270113595418"><a name="p5270113595418"></a><a name="p5270113595418"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4093352895418"><a name="p4093352895418"></a><a name="p4093352895418"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row3285743695418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4420663995418"><a name="p4420663995418"></a><a name="p4420663995418"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2396797895418"><a name="p2396797895418"></a><a name="p2396797895418"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row1438521495418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2435172295418"><a name="p2435172295418"></a><a name="p2435172295418"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2633243395418"><a name="p2633243395418"></a><a name="p2633243395418"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row3566531195418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p320910195418"><a name="p320910195418"></a><a name="p320910195418"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5861060395418"><a name="p5861060395418"></a><a name="p5861060395418"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row5773337995418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4589214195418"><a name="p4589214195418"></a><a name="p4589214195418"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2627593195418"><a name="p2627593195418"></a><a name="p2627593195418"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row3515679195418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2912784795418"><a name="p2912784795418"></a><a name="p2912784795418"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1054542495418"><a name="p1054542495418"></a><a name="p1054542495418"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row2779995395418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3720368195418"><a name="p3720368195418"></a><a name="p3720368195418"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p6070815795418"><a name="p6070815795418"></a><a name="p6070815795418"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row950250895418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3150567095418"><a name="p3150567095418"></a><a name="p3150567095418"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p182249795418"><a name="p182249795418"></a><a name="p182249795418"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row1640247895418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5353236595418"><a name="p5353236595418"></a><a name="p5353236595418"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4115430495418"><a name="p4115430495418"></a><a name="p4115430495418"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row3484442195418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p382584295418"><a name="p382584295418"></a><a name="p382584295418"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4145776795418"><a name="p4145776795418"></a><a name="p4145776795418"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row3757558995418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2372383495418"><a name="p2372383495418"></a><a name="p2372383495418"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4258237995418"><a name="p4258237995418"></a><a name="p4258237995418"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row4769709895418"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3825976295418"><a name="p3825976295418"></a><a name="p3825976295418"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1203300295418"><a name="p1203300295418"></a><a name="p1203300295418"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section85821649202813"></a>

For details, see section  [Error Codes](error-codes-27.md).

