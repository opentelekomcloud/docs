# Deleting an AS Configuration<a name="EN-US_TOPIC_0043063060"></a>

## Function<a name="section5380904"></a>

This interface is used to delete a specified AS configuration.

>![](/images/icon-note.gif) **NOTE:**   
>AS configurations used by AS groups cannot be deleted.  

## URI<a name="section48428136"></a>

DELETE /autoscaling-api/v1/\{project\_id\}/scaling\_configuration/\{scaling\_configuration\_id\}

**Table  1**  Parameter description

<a name="table14499957"></a>
<table><thead align="left"><tr id="row65119131"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.1"><p id="p40158284"><a name="p40158284"></a><a name="p40158284"></a><strong id="b2298523125017"><a name="b2298523125017"></a><a name="b2298523125017"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p31595610"><a name="p31595610"></a><a name="p31595610"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p9107628"><a name="p9107628"></a><a name="p9107628"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p66629291"><a name="p66629291"></a><a name="p66629291"></a><strong id="b27931723135018"><a name="b27931723135018"></a><a name="b27931723135018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row28263486"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p7641038"><a name="p7641038"></a><a name="p7641038"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p14944322"><a name="p14944322"></a><a name="p14944322"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p2530563"><a name="p2530563"></a><a name="p2530563"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row32841145"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p42887128"><a name="p42887128"></a><a name="p42887128"></a>scaling_ configuration _id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p51305376"><a name="p51305376"></a><a name="p51305376"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p62094776"><a name="p62094776"></a><a name="p62094776"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p63620936"><a name="p63620936"></a><a name="p63620936"></a>Specifies the AS configuration ID. For details, see <a href="querying-as-configurations.md">Querying AS Configurations</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section33200047"></a>

-   Request parameters

    None

-   Example request

    This example shows how to delete the AS configuration with ID  **6afe46f9-7d3d-4046-8748-3b2a1085ad86**.

    ```
    DELETE https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_configuration/6afe46f9-7d3d-4046-8748-3b2a1085ad86
    ```


## Response Message<a name="section30364973"></a>

-   Response parameters

    None

-   Example response

    None


## Returned Values<a name="section4849307"></a>

-   Normal

    204

-   Abnormal

    <a name="table23361726"></a>
    <table><thead align="left"><tr id="row63863782"><th class="cellrowborder" valign="top" width="44.17%" id="mcps1.1.3.1.1"><p id="p5583857"><a name="p5583857"></a><a name="p5583857"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.83%" id="mcps1.1.3.1.2"><p id="p49639248"><a name="p49639248"></a><a name="p49639248"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61356140"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p3791404"><a name="p3791404"></a><a name="p3791404"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p38668280"><a name="p38668280"></a><a name="p38668280"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row12470207"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p3453833"><a name="p3453833"></a><a name="p3453833"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p11325076"><a name="p11325076"></a><a name="p11325076"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row34816825"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p1590600"><a name="p1590600"></a><a name="p1590600"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p61729771"><a name="p61729771"></a><a name="p61729771"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row18697032"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p38064613"><a name="p38064613"></a><a name="p38064613"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p63334794"><a name="p63334794"></a><a name="p63334794"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row33142240"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p166885"><a name="p166885"></a><a name="p166885"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p13517702"><a name="p13517702"></a><a name="p13517702"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row54550461"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p56511253"><a name="p56511253"></a><a name="p56511253"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p14008765"><a name="p14008765"></a><a name="p14008765"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row58970022"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p11842506"><a name="p11842506"></a><a name="p11842506"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p19718930"><a name="p19718930"></a><a name="p19718930"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row43252647"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p13803553"><a name="p13803553"></a><a name="p13803553"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p44346036"><a name="p44346036"></a><a name="p44346036"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row63570006"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p48896832"><a name="p48896832"></a><a name="p48896832"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p1220438"><a name="p1220438"></a><a name="p1220438"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row10983950"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p17284754"><a name="p17284754"></a><a name="p17284754"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p57887863"><a name="p57887863"></a><a name="p57887863"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row51228725"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p55886094"><a name="p55886094"></a><a name="p55886094"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p30479771"><a name="p30479771"></a><a name="p30479771"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row5882489"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p6719600"><a name="p6719600"></a><a name="p6719600"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p7416719"><a name="p7416719"></a><a name="p7416719"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row66750478"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p38079613"><a name="p38079613"></a><a name="p38079613"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p64549801"><a name="p64549801"></a><a name="p64549801"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row44077297"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="p13491266"><a name="p13491266"></a><a name="p13491266"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="p19050756"><a name="p19050756"></a><a name="p19050756"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

