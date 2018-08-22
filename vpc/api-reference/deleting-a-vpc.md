# Deleting a VPC<a name="EN-US_TOPIC_0020090627"></a>

## Function<a name="section15422169"></a>

This interface is used to delete a VPC.

## URI<a name="section4581796"></a>

-   DELETE /v1/\{tenant\_id\}/vpcs/\{vpc\_id\}
-   Parameter description

    <a name="table47834478"></a><table><thead align="left"><tr id="row29612923"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p49836563"><a name="p49836563"></a><a name="p49836563"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p10229816"><a name="p10229816"></a><a name="p10229816"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p23308753"><a name="p23308753"></a><a name="p23308753"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8960839"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p54739329"><a name="p54739329"></a><a name="p54739329"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p4700647"><a name="p4700647"></a><a name="p4700647"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p45208163"><a name="p45208163"></a><a name="p45208163"></a>Specifies the tenant ID of the operator.</p>
    </td>
    </tr>
    <tr id="row4220283"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p6298672"><a name="p6298672"></a><a name="p6298672"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p40430446"><a name="p40430446"></a><a name="p40430446"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p53640668"><a name="p53640668"></a><a name="p53640668"></a>Specifies the VPC ID, which uniquely identifies the VPC.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section41236172"></a>

-   Parameter description

    None

-   Example request

    None


## Response<a name="section35581233"></a>

-   Example response

    None


## Returned Value<a name="section51795644"></a>

-   Normal

    204

-   Abnormal

    <a name="table3859260195140"></a><table><thead align="left"><tr id="row3885338495140"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p6011637695140"><a name="p6011637695140"></a><a name="p6011637695140"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p3758829795140"><a name="p3758829795140"></a><a name="p3758829795140"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2475321895140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5885367695140"><a name="p5885367695140"></a><a name="p5885367695140"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p241847995140"><a name="p241847995140"></a><a name="p241847995140"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row2176631395140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1824089995140"><a name="p1824089995140"></a><a name="p1824089995140"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p111783395140"><a name="p111783395140"></a><a name="p111783395140"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1006050595140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p959457395140"><a name="p959457395140"></a><a name="p959457395140"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3896297895140"><a name="p3896297895140"></a><a name="p3896297895140"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1512248895140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1696204995140"><a name="p1696204995140"></a><a name="p1696204995140"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3174873495140"><a name="p3174873495140"></a><a name="p3174873495140"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row1730315695140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5937839595140"><a name="p5937839595140"></a><a name="p5937839595140"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4492068295140"><a name="p4492068295140"></a><a name="p4492068295140"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row163296195140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p6516099295140"><a name="p6516099295140"></a><a name="p6516099295140"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4354898895140"><a name="p4354898895140"></a><a name="p4354898895140"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row5639657295140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p471958195140"><a name="p471958195140"></a><a name="p471958195140"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4674177595140"><a name="p4674177595140"></a><a name="p4674177595140"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row1802279395140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5056016795140"><a name="p5056016795140"></a><a name="p5056016795140"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p173287395140"><a name="p173287395140"></a><a name="p173287395140"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row1559586495140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5530543595140"><a name="p5530543595140"></a><a name="p5530543595140"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5055528895140"><a name="p5055528895140"></a><a name="p5055528895140"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row5234441195140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1203887995140"><a name="p1203887995140"></a><a name="p1203887995140"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3562513695140"><a name="p3562513695140"></a><a name="p3562513695140"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row5219076895140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p6670268695140"><a name="p6670268695140"></a><a name="p6670268695140"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3420852595140"><a name="p3420852595140"></a><a name="p3420852595140"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row3944127795140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4062683195140"><a name="p4062683195140"></a><a name="p4062683195140"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p243903095140"><a name="p243903095140"></a><a name="p243903095140"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row2195127795140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3322302295140"><a name="p3322302295140"></a><a name="p3322302295140"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p671026395140"><a name="p671026395140"></a><a name="p671026395140"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row6039237595140"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5994419295140"><a name="p5994419295140"></a><a name="p5994419295140"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2364138295140"><a name="p2364138295140"></a><a name="p2364138295140"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section85821649202813"></a>

For details, see section  [Error Codes](error-codes-27.md).

