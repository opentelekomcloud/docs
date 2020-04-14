# Querying AS Quotas<a name="EN-US_TOPIC_0043063063"></a>

## Function<a name="section11009764"></a>

This interface is used to query the total quotas and used quotas of AS groups, AS configurations, bandwidth scaling policies, AS policies, and instances for a specified tenant.

## URI<a name="section31979016"></a>

GET /autoscaling-api/v1/\{project\_id\}/quotas

**Table  1**  Parameter description

<a name="table2199097"></a>
<table><thead align="left"><tr id="row41000636"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p32717189"><a name="p32717189"></a><a name="p32717189"></a><strong id="b13990340838"><a name="b13990340838"></a><a name="b13990340838"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p32846614"><a name="p32846614"></a><a name="p32846614"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="p43330072"><a name="p43330072"></a><a name="p43330072"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.2.5.1.4"><p id="p20074930"><a name="p20074930"></a><a name="p20074930"></a><strong id="b12998154316311"><a name="b12998154316311"></a><a name="b12998154316311"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row15456653"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p44029393"><a name="p44029393"></a><a name="p44029393"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p9611044"><a name="p9611044"></a><a name="p9611044"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p40297137"><a name="p40297137"></a><a name="p40297137"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section19375690"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query the total quotas and used quotas of AS groups, AS configurations, bandwidth scaling policies, AS policies, and instances for a specified tenant.

    ```
    GET https://{Endpoint}/autoscaling-api/v1/{project_id}/quotas
    ```


## Response Message<a name="section40163483"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table51227795"></a>
    <table><thead align="left"><tr id="row28165387"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p66803900"><a name="p66803900"></a><a name="p66803900"></a><strong id="b57666451535"><a name="b57666451535"></a><a name="b57666451535"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="p42406858"><a name="p42406858"></a><a name="p42406858"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62%" id="mcps1.2.4.1.3"><p id="p12403484"><a name="p12403484"></a><a name="p12403484"></a><strong id="b915144719319"><a name="b915144719319"></a><a name="b915144719319"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65158171"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p43320494"><a name="p43320494"></a><a name="p43320494"></a>quotas</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p77023552159"><a name="p77023552159"></a><a name="p77023552159"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p19726002"><a name="p19726002"></a><a name="p19726002"></a>Specifies quota details. For details, see <a href="#table5036780310489">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **quotas**  field description

    <a name="table5036780310489"></a>
    <table><thead align="left"><tr id="r1f3f90a6acc94015acc80b9d6b53f072"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="ad0d15c1370cb450fb7e6011b8baff160"><a name="ad0d15c1370cb450fb7e6011b8baff160"></a><a name="ad0d15c1370cb450fb7e6011b8baff160"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="a2273dfb9dd3341b0b5cbf801a0aa70fc"><a name="a2273dfb9dd3341b0b5cbf801a0aa70fc"></a><a name="a2273dfb9dd3341b0b5cbf801a0aa70fc"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="a479b45e1fbfc44118151c43b5ecb82f1"><a name="a479b45e1fbfc44118151c43b5ecb82f1"></a><a name="a479b45e1fbfc44118151c43b5ecb82f1"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rdd24623b54f94a86b0f655ec659180e9"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="ab9c8eb8b964943509fca83cc70a4e489"><a name="ab9c8eb8b964943509fca83cc70a4e489"></a><a name="ab9c8eb8b964943509fca83cc70a4e489"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="a43cc5f338c7e429c861f7dbb2dcb3229"><a name="a43cc5f338c7e429c861f7dbb2dcb3229"></a><a name="a43cc5f338c7e429c861f7dbb2dcb3229"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="a5c153a8f0b8d4f26af1405cdcbcec1cc"><a name="a5c153a8f0b8d4f26af1405cdcbcec1cc"></a><a name="a5c153a8f0b8d4f26af1405cdcbcec1cc"></a>Specifies resources. For details, see <a href="#table61002694">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **resources**  field description

    <a name="table61002694"></a>
    <table><thead align="left"><tr id="row47328638"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="p8414476"><a name="p8414476"></a><a name="p8414476"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p10483995"><a name="p10483995"></a><a name="p10483995"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62%" id="mcps1.2.4.1.3"><p id="p43897299"><a name="p43897299"></a><a name="p43897299"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66020315"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p46045275"><a name="p46045275"></a><a name="p46045275"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p38679804"><a name="p38679804"></a><a name="p38679804"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p46056421"><a name="p46056421"></a><a name="p46056421"></a>Specifies the quota type.</p>
    <a name="ua99da6c954d14b9f8e73af19c844fac9"></a><a name="ua99da6c954d14b9f8e73af19c844fac9"></a><ul id="ua99da6c954d14b9f8e73af19c844fac9"><li><strong id="b842352706185635"><a name="b842352706185635"></a><a name="b842352706185635"></a>scaling_Group</strong>: AS group quota</li><li><strong id="b842352706185647"><a name="b842352706185647"></a><a name="b842352706185647"></a>scaling_Config</strong>: AS configuration quota</li><li><strong id="b842352706185656"><a name="b842352706185656"></a><a name="b842352706185656"></a>scaling_Policy</strong>: AS policy quota</li><li><strong id="b842352706185737"><a name="b842352706185737"></a><a name="b842352706185737"></a>scaling_Instance</strong>: instance quota</li><li><strong id="b1750820364133"><a name="b1750820364133"></a><a name="b1750820364133"></a>bandwidth_scaling_policy</strong>: bandwidth scaling policy quota</li></ul>
    </td>
    </tr>
    <tr id="row11854613"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p20699582"><a name="p20699582"></a><a name="p20699582"></a>used</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p66053444"><a name="p66053444"></a><a name="p66053444"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p48728718"><a name="p48728718"></a><a name="p48728718"></a>Specifies the used amount of the quota.</p>
    <p id="p60330192195232"><a name="p60330192195232"></a><a name="p60330192195232"></a>When <strong id="b84235270615576"><a name="b84235270615576"></a><a name="b84235270615576"></a>type</strong> is set to <strong id="b842352706155714"><a name="b842352706155714"></a><a name="b842352706155714"></a>scaling_Policy</strong> or <strong id="b842352706155718"><a name="b842352706155718"></a><a name="b842352706155718"></a>scaling_Instance</strong>, this parameter is reserved, and the system returns <strong id="b842352706163219"><a name="b842352706163219"></a><a name="b842352706163219"></a>-1</strong> as the parameter value. You can query the used quota of AS policies and AS instances in a specified AS group. For details, see <a href="querying-as-policy-and-instance-quotas.md">Querying AS policy and instance quotas</a>.</p>
    </td>
    </tr>
    <tr id="row35905280"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p22646572"><a name="p22646572"></a><a name="p22646572"></a>quota</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p22433040"><a name="p22433040"></a><a name="p22433040"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p5136981"><a name="p5136981"></a><a name="p5136981"></a>Specifies the total quota.</p>
    </td>
    </tr>
    <tr id="row14705260193547"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p50275448193547"><a name="p50275448193547"></a><a name="p50275448193547"></a>max</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p45779455193547"><a name="p45779455193547"></a><a name="p45779455193547"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p17148395193547"><a name="p17148395193547"></a><a name="p17148395193547"></a>Specifies the quota upper limit.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "quotas": {
            "resources": [
                {
                    "type": "scaling_Group",
                    "used": 2,
                    "quota": 25,
                    "max": 50
                },
                {
                    "type": "scaling_Config",
                    "used": 3,
                    "quota": 100,
                    "max": 200
                },
                {
                    "type": "scaling_Policy",
                    "used": -1,
                    "quota": 50,
                    "max": 50
                },
                {
                    "type": "scaling_Instance",
                    "used": -1,
                    "quota": 200,
                    "max": 1000
                },
                {
                    "type": "bandwidth_scaling_policy",
                    "used": 1,
                    "quota": 10,
                    "max": 100
                }
            ]
        }
    }
    ```


## Returned Values<a name="section25927028"></a>

-   Normal

    200

-   Abnormal

    <a name="table44024689"></a>
    <table><thead align="left"><tr id="row17847776"><th class="cellrowborder" valign="top" width="44.18%" id="mcps1.1.3.1.1"><p id="p36383728"><a name="p36383728"></a><a name="p36383728"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.82%" id="mcps1.1.3.1.2"><p id="p61400865"><a name="p61400865"></a><a name="p61400865"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7414170"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p63676932"><a name="p63676932"></a><a name="p63676932"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p57557895"><a name="p57557895"></a><a name="p57557895"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row48259009"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p16665627"><a name="p16665627"></a><a name="p16665627"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p7738529"><a name="p7738529"></a><a name="p7738529"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row2537905"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p4243749"><a name="p4243749"></a><a name="p4243749"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p8199418"><a name="p8199418"></a><a name="p8199418"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row6685904"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p4687385"><a name="p4687385"></a><a name="p4687385"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p44133910"><a name="p44133910"></a><a name="p44133910"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row61660876"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p28475059"><a name="p28475059"></a><a name="p28475059"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p24778434"><a name="p24778434"></a><a name="p24778434"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row21679321"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p11194552"><a name="p11194552"></a><a name="p11194552"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p34343508"><a name="p34343508"></a><a name="p34343508"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row40656116"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p4811061"><a name="p4811061"></a><a name="p4811061"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p54151655"><a name="p54151655"></a><a name="p54151655"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row17602849"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p16544703"><a name="p16544703"></a><a name="p16544703"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p65052577"><a name="p65052577"></a><a name="p65052577"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row48602288"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p44471219"><a name="p44471219"></a><a name="p44471219"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p45399024"><a name="p45399024"></a><a name="p45399024"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row5938035"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p11218807"><a name="p11218807"></a><a name="p11218807"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p36308168"><a name="p36308168"></a><a name="p36308168"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row58338056"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p27762102"><a name="p27762102"></a><a name="p27762102"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p34137829"><a name="p34137829"></a><a name="p34137829"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row38805013"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p56198311"><a name="p56198311"></a><a name="p56198311"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p55769358"><a name="p55769358"></a><a name="p55769358"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row32162181"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p54999878"><a name="p54999878"></a><a name="p54999878"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p25805135"><a name="p25805135"></a><a name="p25805135"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row30919631"><td class="cellrowborder" valign="top" width="44.18%" headers="mcps1.1.3.1.1 "><p id="p21462168"><a name="p21462168"></a><a name="p21462168"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.82%" headers="mcps1.1.3.1.2 "><p id="p60714046"><a name="p60714046"></a><a name="p60714046"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

