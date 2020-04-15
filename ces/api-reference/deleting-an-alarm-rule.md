# Deleting an Alarm Rule<a name="EN-US_TOPIC_0171212631"></a>

## Function<a name="section438541220332"></a>

This API is used to delete an alarm rule.

## URI<a name="section4284924220332"></a>

DELETE /V1.0/\{project\_id\}/alarms/\{alarm\_id\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="table6195694220332"></a>
    <table><thead align="left"><tr id="row3240387120332"><th class="cellrowborder" valign="top" width="19.99%" id="mcps1.2.4.1.1"><p id="p746789920332"><a name="p746789920332"></a><a name="p746789920332"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.93%" id="mcps1.2.4.1.2"><p id="p92007920332"><a name="p92007920332"></a><a name="p92007920332"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.08%" id="mcps1.2.4.1.3"><p id="p741760420332"><a name="p741760420332"></a><a name="p741760420332"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6395507420332"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="p1297848020332"><a name="p1297848020332"></a><a name="p1297848020332"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p4462392620332"><a name="p4462392620332"></a><a name="p4462392620332"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.08%" headers="mcps1.2.4.1.3 "><p id="p5776825320332"><a name="p5776825320332"></a><a name="p5776825320332"></a>Specifies the project ID.</p>
    <p id="p126259299619"><a name="p126259299619"></a><a name="p126259299619"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row52895577203555"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="p56683338203555"><a name="p56683338203555"></a><a name="p56683338203555"></a>alarm_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p27947631203555"><a name="p27947631203555"></a><a name="p27947631203555"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.08%" headers="mcps1.2.4.1.3 "><p id="p49165616203555"><a name="p49165616203555"></a><a name="p49165616203555"></a>Specifies the alarm rule ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example

    ```
    DELETE https://{Cloud Eye endpoint}/V1.0/{project_id}/alarms/al1441967036681YkazZ0deN
    ```


## Request<a name="section1403745820332"></a>

The request has no message body.

## Response<a name="section5063939020332"></a>

The response has no message body.

## Returned Values<a name="section624021320332"></a>

-   Normal

    204

-   Abnormal

    <a name="table5391277220332"></a>
    <table><thead align="left"><tr id="row5214588820332"><th class="cellrowborder" valign="top" width="30.830000000000002%" id="mcps1.1.3.1.1"><p id="p6306739920332"><a name="p6306739920332"></a><a name="p6306739920332"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="69.17%" id="mcps1.1.3.1.2"><p id="p818568620332"><a name="p818568620332"></a><a name="p818568620332"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5906085420332"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.1.3.1.1 "><p id="p1919988720332"><a name="p1919988720332"></a><a name="p1919988720332"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.1.3.1.2 "><p id="p1168698420332"><a name="p1168698420332"></a><a name="p1168698420332"></a>Request error</p>
    </td>
    </tr>
    <tr id="row3807399220332"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.1.3.1.1 "><p id="p6409448420332"><a name="p6409448420332"></a><a name="p6409448420332"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.1.3.1.2 "><p id="p2427074120332"><a name="p2427074120332"></a><a name="p2427074120332"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="row1711008520332"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.1.3.1.1 "><p id="p4373966420332"><a name="p4373966420332"></a><a name="p4373966420332"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.1.3.1.2 "><p id="p5325190820332"><a name="p5325190820332"></a><a name="p5325190820332"></a>You are forbidden to access the page requested.</p>
    </td>
    </tr>
    <tr id="row950512420332"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.1.3.1.1 "><p id="p3171757520332"><a name="p3171757520332"></a><a name="p3171757520332"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.1.3.1.2 "><p id="p1898679120332"><a name="p1898679120332"></a><a name="p1898679120332"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row3666339320332"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.1.3.1.1 "><p id="p1694483820332"><a name="p1694483820332"></a><a name="p1694483820332"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.1.3.1.2 "><p id="p3035465220332"><a name="p3035465220332"></a><a name="p3035465220332"></a>Concurrent requests are excessive.</p>
    </td>
    </tr>
    <tr id="row475641720332"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.1.3.1.1 "><p id="p4972547420332"><a name="p4972547420332"></a><a name="p4972547420332"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.1.3.1.2 "><p id="p123162520332"><a name="p123162520332"></a><a name="p123162520332"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row1108462520332"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.1.3.1.1 "><p id="p2543941720332"><a name="p2543941720332"></a><a name="p2543941720332"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.1.3.1.2 "><p id="p4732687320332"><a name="p4732687320332"></a><a name="p4732687320332"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section13819114315466"></a>

For details, see  [Error Codes](error-codes.md).

