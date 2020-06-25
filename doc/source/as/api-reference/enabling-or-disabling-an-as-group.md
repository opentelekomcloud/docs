# Enabling or Disabling an AS Group<a name="EN-US_TOPIC_0043063017"></a>

## Function<a name="section44766395"></a>

This interface is used to enable or disable a specified AS group.

>![](/images/icon-note.gif) **NOTE:**   
>For a disabled AS group, AS does not automatically trigger any scaling actions. When an AS group has an in-progress scaling action, the scaling action does not stop immediately after the AS group is disabled.  

## URI<a name="section244376"></a>

POST /autoscaling-api/v1/\{project\_id\}/scaling\_group/\{scaling\_group\_id\}/action

**Table  1**  Parameter description

<a name="table37174709"></a>
<table><thead align="left"><tr id="row12886548"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.1"><p id="p37177477"><a name="p37177477"></a><a name="p37177477"></a><strong id="b5958142010398"><a name="b5958142010398"></a><a name="b5958142010398"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p58585662"><a name="p58585662"></a><a name="p58585662"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p47818216"><a name="p47818216"></a><a name="p47818216"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.5.1.4"><p id="p48070315"><a name="p48070315"></a><a name="p48070315"></a><strong id="b787972220392"><a name="b787972220392"></a><a name="b787972220392"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1381422"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p44786329"><a name="p44786329"></a><a name="p44786329"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p3814037"><a name="p3814037"></a><a name="p3814037"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p40501577"><a name="p40501577"></a><a name="p40501577"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row64858964"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p19084765"><a name="p19084765"></a><a name="p19084765"></a>scaling_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p2362138"><a name="p2362138"></a><a name="p2362138"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p57115508"><a name="p57115508"></a><a name="p57115508"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p62953426"><a name="p62953426"></a><a name="p62953426"></a>Specifies the AS group ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section2199391"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table42688671"></a>
    <table><thead align="left"><tr id="row6074405"><th class="cellrowborder" valign="top" width="19.607843137254903%" id="mcps1.2.5.1.1"><p id="p22264835"><a name="p22264835"></a><a name="p22264835"></a><strong id="b16457182313913"><a name="b16457182313913"></a><a name="b16457182313913"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.588235294117645%" id="mcps1.2.5.1.2"><p id="p58621221"><a name="p58621221"></a><a name="p58621221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.627450980392158%" id="mcps1.2.5.1.3"><p id="p50698484"><a name="p50698484"></a><a name="p50698484"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.17647058823529%" id="mcps1.2.5.1.4"><p id="p12936535"><a name="p12936535"></a><a name="p12936535"></a><strong id="b5634152410396"><a name="b5634152410396"></a><a name="b5634152410396"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41226423"><td class="cellrowborder" valign="top" width="19.607843137254903%" headers="mcps1.2.5.1.1 "><p id="p51005947"><a name="p51005947"></a><a name="p51005947"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.588235294117645%" headers="mcps1.2.5.1.2 "><p id="p37841036"><a name="p37841036"></a><a name="p37841036"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.627450980392158%" headers="mcps1.2.5.1.3 "><p id="p45225041"><a name="p45225041"></a><a name="p45225041"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.17647058823529%" headers="mcps1.2.5.1.4 "><p id="p3552977619244"><a name="p3552977619244"></a><a name="p3552977619244"></a>Specifies a flag for enabling or disabling an AS group.</p>
    <a name="ul6530813782310"></a><a name="ul6530813782310"></a><ul id="ul6530813782310"><li><strong id="b84235270617755"><a name="b84235270617755"></a><a name="b84235270617755"></a>resume</strong>: enables the AS group.</li><li><strong id="b8423527061784"><a name="b8423527061784"></a><a name="b8423527061784"></a>pause</strong>: disables the AS group.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    This example shows how to enable the AS group with ID  **a8327883-6b07-4497-9c61-68d03ee193a1**.

    ```
    POST https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group/a8327883-6b07-4497-9c61-68d03ee193a1/action
    
    {
        "action": "resume"
    }
    ```


## Response Message<a name="section19794519"></a>

-   Response parameters

    None

-   Example response

    None


## Returned Values<a name="section43932946"></a>

-   Normal

    204

-   Abnormal

    <a name="table24812117"></a>
    <table><thead align="left"><tr id="row10022287"><th class="cellrowborder" valign="top" width="43.61%" id="mcps1.1.3.1.1"><p id="p6498885"><a name="p6498885"></a><a name="p6498885"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.38999999999999%" id="mcps1.1.3.1.2"><p id="p56647676"><a name="p56647676"></a><a name="p56647676"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row25059035"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p16515979"><a name="p16515979"></a><a name="p16515979"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p62725940"><a name="p62725940"></a><a name="p62725940"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row27662549"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p26073957"><a name="p26073957"></a><a name="p26073957"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p31615745"><a name="p31615745"></a><a name="p31615745"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row16106256"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p29538346"><a name="p29538346"></a><a name="p29538346"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p43795845"><a name="p43795845"></a><a name="p43795845"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row58618290"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p50461073"><a name="p50461073"></a><a name="p50461073"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p60815108"><a name="p60815108"></a><a name="p60815108"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row10465065"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p42363926"><a name="p42363926"></a><a name="p42363926"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p8925963"><a name="p8925963"></a><a name="p8925963"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row13224809"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p64576574"><a name="p64576574"></a><a name="p64576574"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p63319983"><a name="p63319983"></a><a name="p63319983"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row33008942"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p56478678"><a name="p56478678"></a><a name="p56478678"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p11370190"><a name="p11370190"></a><a name="p11370190"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row35222847"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p34478387"><a name="p34478387"></a><a name="p34478387"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p41285963"><a name="p41285963"></a><a name="p41285963"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row36029352"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p32696434"><a name="p32696434"></a><a name="p32696434"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p31165525"><a name="p31165525"></a><a name="p31165525"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row12054271"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p36871865"><a name="p36871865"></a><a name="p36871865"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p33831071"><a name="p33831071"></a><a name="p33831071"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row36044191"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p33898355"><a name="p33898355"></a><a name="p33898355"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p61412264"><a name="p61412264"></a><a name="p61412264"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row15839470"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p7928727"><a name="p7928727"></a><a name="p7928727"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p38247156"><a name="p38247156"></a><a name="p38247156"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row8680090"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p31998689"><a name="p31998689"></a><a name="p31998689"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p41757008"><a name="p41757008"></a><a name="p41757008"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row40268759"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p40544022"><a name="p40544022"></a><a name="p40544022"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p62840338"><a name="p62840338"></a><a name="p62840338"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

