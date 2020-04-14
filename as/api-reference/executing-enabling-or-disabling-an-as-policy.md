# Executing, Enabling, or Disabling an AS Policy<a name="EN-US_TOPIC_0043063075"></a>

## Function<a name="section40235071"></a>

This interface is used to immediately execute, enable, or disable a specified AS policy.

An AS policy can be executed only when the AS group and AS policy are in the  **INSERVICE**  state. Otherwise, the execution fails.

## URI<a name="section26571327"></a>

POST /autoscaling-api/v1/\{project\_id\}/scaling\_policy/\{scaling\_policy\_id\}/action

**Table  1**  Parameter description

<a name="table63687043"></a>
<table><thead align="left"><tr id="row46742451"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.1"><p id="p28042199"><a name="p28042199"></a><a name="p28042199"></a><strong id="b15212911135915"><a name="b15212911135915"></a><a name="b15212911135915"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p56825610"><a name="p56825610"></a><a name="p56825610"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.3"><p id="p39471735"><a name="p39471735"></a><a name="p39471735"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="38%" id="mcps1.2.5.1.4"><p id="p43093956"><a name="p43093956"></a><a name="p43093956"></a><strong id="b16962014145913"><a name="b16962014145913"></a><a name="b16962014145913"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row949529"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p9803039"><a name="p9803039"></a><a name="p9803039"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p55848701"><a name="p55848701"></a><a name="p55848701"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p27450972"><a name="p27450972"></a><a name="p27450972"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row13317766"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p4997277"><a name="p4997277"></a><a name="p4997277"></a>scaling_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p2126321"><a name="p2126321"></a><a name="p2126321"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="p38014313"><a name="p38014313"></a><a name="p38014313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.4 "><p id="p59260526"><a name="p59260526"></a><a name="p59260526"></a>Specifies the AS policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section37815352"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table17322790"></a>
    <table><thead align="left"><tr id="row19920592"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p2955276"><a name="p2955276"></a><a name="p2955276"></a><strong id="b1646401655912"><a name="b1646401655912"></a><a name="b1646401655912"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p38050837"><a name="p38050837"></a><a name="p38050837"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.3"><p id="p62218962"><a name="p62218962"></a><a name="p62218962"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38%" id="mcps1.2.5.1.4"><p id="p0772218550"><a name="p0772218550"></a><a name="p0772218550"></a><strong id="b6315161725911"><a name="b6315161725911"></a><a name="b6315161725911"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62503562"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p29623765"><a name="p29623765"></a><a name="p29623765"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p50714740"><a name="p50714740"></a><a name="p50714740"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p14253264"><a name="p14253264"></a><a name="p14253264"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.5.1.4 "><p id="p3552977619244"><a name="p3552977619244"></a><a name="p3552977619244"></a>Specifies the operation for an AS policy.</p>
    <a name="ul6530813782310"></a><a name="ul6530813782310"></a><ul id="ul6530813782310"><li><strong id="b115031530511"><a name="b115031530511"></a><a name="b115031530511"></a>execute</strong>: immediately executes the AS policy.</li><li><strong id="b84235270617755"><a name="b84235270617755"></a><a name="b84235270617755"></a>resume</strong>: enables the AS group.</li><li><strong id="b8423527061784"><a name="b8423527061784"></a><a name="b8423527061784"></a>pause</strong>: disables the AS group.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    This example shows how to immediately execute the AS policy with ID  **906f73ff-56e8-41b2-a005-8157d0c60361**.

    ```
    POST https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_policy/906f73ff-56e8-41b2-a005-8157d0c60361/action
    
    {
        "action": "execute"
    }
    ```


## Response Message<a name="section4793853"></a>

-   Response parameters

    None

-   Example response

    None


## Returned Values<a name="section43144677"></a>

-   Normal

    204

-   Abnormal

    <a name="table52801617"></a>
    <table><thead align="left"><tr id="row4862753"><th class="cellrowborder" valign="top" width="43.99%" id="mcps1.1.3.1.1"><p id="p58338722"><a name="p58338722"></a><a name="p58338722"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.010000000000005%" id="mcps1.1.3.1.2"><p id="p27816043"><a name="p27816043"></a><a name="p27816043"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38507045"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p32062968"><a name="p32062968"></a><a name="p32062968"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p46963595"><a name="p46963595"></a><a name="p46963595"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row20019172"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p10940218"><a name="p10940218"></a><a name="p10940218"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p13742502"><a name="p13742502"></a><a name="p13742502"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row56573654"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p19063291"><a name="p19063291"></a><a name="p19063291"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p622761"><a name="p622761"></a><a name="p622761"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row5604850"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p51339711"><a name="p51339711"></a><a name="p51339711"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p64875945"><a name="p64875945"></a><a name="p64875945"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row47012596"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p49923923"><a name="p49923923"></a><a name="p49923923"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p17305987"><a name="p17305987"></a><a name="p17305987"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row21536161"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p66707469"><a name="p66707469"></a><a name="p66707469"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p34595869"><a name="p34595869"></a><a name="p34595869"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row42927366"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p54564616"><a name="p54564616"></a><a name="p54564616"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p57657762"><a name="p57657762"></a><a name="p57657762"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row49157816"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p22360170"><a name="p22360170"></a><a name="p22360170"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p66343369"><a name="p66343369"></a><a name="p66343369"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row60219412"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p45934241"><a name="p45934241"></a><a name="p45934241"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p29686030"><a name="p29686030"></a><a name="p29686030"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row65847680"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p32061857"><a name="p32061857"></a><a name="p32061857"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p46873590"><a name="p46873590"></a><a name="p46873590"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row19209127"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p12435494"><a name="p12435494"></a><a name="p12435494"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p642126"><a name="p642126"></a><a name="p642126"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row5779136"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p65456887"><a name="p65456887"></a><a name="p65456887"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p407659"><a name="p407659"></a><a name="p407659"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row3668935"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p28748320"><a name="p28748320"></a><a name="p28748320"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p46912618"><a name="p46912618"></a><a name="p46912618"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row19560385"><td class="cellrowborder" valign="top" width="43.99%" headers="mcps1.1.3.1.1 "><p id="p40887351"><a name="p40887351"></a><a name="p40887351"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.010000000000005%" headers="mcps1.1.3.1.2 "><p id="p23541105"><a name="p23541105"></a><a name="p23541105"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

