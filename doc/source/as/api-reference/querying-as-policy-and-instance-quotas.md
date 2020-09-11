# Querying AS policy and instance quotas<a name="EN-US_TOPIC_0043063020"></a>

## Function<a name="section59572368"></a>

This interface is used to query the total quotas and used quotas of AS policies and instances of a specified AS group by group ID. 

## URI<a name="section66389266"></a>

GET /autoscaling-api/v1/\{project\_id\}/quotas/\{scaling\_group\_id\}

**Table  1**  Parameter description

<a name="table43451153111642"></a>
<table><thead align="left"><tr id="row37743918111642"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.1"><p id="p37358531111642"><a name="p37358531111642"></a><a name="p37358531111642"></a><strong id="b797713116415"><a name="b797713116415"></a><a name="b797713116415"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p6142156111642"><a name="p6142156111642"></a><a name="p6142156111642"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p27752626111642"><a name="p27752626111642"></a><a name="p27752626111642"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p33370204111642"><a name="p33370204111642"></a><a name="p33370204111642"></a><strong id="b492210331943"><a name="b492210331943"></a><a name="b492210331943"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row18631986111642"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p32795934111642"><a name="p32795934111642"></a><a name="p32795934111642"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p39224965111642"><a name="p39224965111642"></a><a name="p39224965111642"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p23105617111642"><a name="p23105617111642"></a><a name="p23105617111642"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row40360840111714"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p48002636111714"><a name="p48002636111714"></a><a name="p48002636111714"></a>scaling_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p63008308111714"><a name="p63008308111714"></a><a name="p63008308111714"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p3399337111714"><a name="p3399337111714"></a><a name="p3399337111714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p6910866111714"><a name="p6910866111714"></a><a name="p6910866111714"></a>Specifies the AS group ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section60632485"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query the total quotas and used quotas of the AS policies and instances in the AS group with ID  **e5d27f5c-dd76-4a61-b4bc-a67c5686719a**.

    ```
    GET https://{Endpoint}/autoscaling-api/v1/{project_id}/quotas/e5d27f5c-dd76-4a61-b4bc-a67c5686719a
    ```


## Response Message<a name="section8821459"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table51227795"></a>
    <table><thead align="left"><tr id="row28165387"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p66803900"><a name="p66803900"></a><a name="p66803900"></a><strong id="b138543161513"><a name="b138543161513"></a><a name="b138543161513"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p42406858"><a name="p42406858"></a><a name="p42406858"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="61%" id="mcps1.2.4.1.3"><p id="p12403484"><a name="p12403484"></a><a name="p12403484"></a><strong id="b652513231052"><a name="b652513231052"></a><a name="b652513231052"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65158171"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p43320494"><a name="p43320494"></a><a name="p43320494"></a>quotas</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p77023552159"><a name="p77023552159"></a><a name="p77023552159"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p19726002"><a name="p19726002"></a><a name="p19726002"></a>Specifies quota details. For details, see <a href="#table38082817101238">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **quotas**  field description

    <a name="table38082817101238"></a>
    <table><thead align="left"><tr id="row15394684101238"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p14228182101238"><a name="p14228182101238"></a><a name="p14228182101238"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="p11632094101238"><a name="p11632094101238"></a><a name="p11632094101238"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p2675571101238"><a name="p2675571101238"></a><a name="p2675571101238"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52155966101238"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p39009890101238"><a name="p39009890101238"></a><a name="p39009890101238"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p51160430101238"><a name="p51160430101238"></a><a name="p51160430101238"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p50354170101238"><a name="p50354170101238"></a><a name="p50354170101238"></a>Specifies resources. For details, see <a href="#table49912400111831">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **resources**  field description

    <a name="table49912400111831"></a>
    <table><thead align="left"><tr id="en-us_topic_0023629325_row47328638"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0023629325_p8414476"><a name="en-us_topic_0023629325_p8414476"></a><a name="en-us_topic_0023629325_p8414476"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="en-us_topic_0023629325_p10483995"><a name="en-us_topic_0023629325_p10483995"></a><a name="en-us_topic_0023629325_p10483995"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p166745230596"><a name="p166745230596"></a><a name="p166745230596"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0023629325_row66020315"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0023629325_p46045275"><a name="en-us_topic_0023629325_p46045275"></a><a name="en-us_topic_0023629325_p46045275"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0023629325_p38679804"><a name="en-us_topic_0023629325_p38679804"></a><a name="en-us_topic_0023629325_p38679804"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p5293191015598"><a name="p5293191015598"></a><a name="p5293191015598"></a>Specifies the quota type.</p>
    <a name="ul9271512125912"></a><a name="ul9271512125912"></a><ul id="ul9271512125912"><li><strong id="b10332125919254"><a name="b10332125919254"></a><a name="b10332125919254"></a>scaling_Policy</strong>: indicates AS policies.</li><li><strong id="b172741330102610"><a name="b172741330102610"></a><a name="b172741330102610"></a>scaling_Instance</strong>: indicates instances.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0023629325_row11854613"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0023629325_p20699582"><a name="en-us_topic_0023629325_p20699582"></a><a name="en-us_topic_0023629325_p20699582"></a>used</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0023629325_p66053444"><a name="en-us_topic_0023629325_p66053444"></a><a name="en-us_topic_0023629325_p66053444"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0023629325_p48728718"><a name="en-us_topic_0023629325_p48728718"></a><a name="en-us_topic_0023629325_p48728718"></a>Specifies the used quota.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0023629325_row35905280"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0023629325_p22646572"><a name="en-us_topic_0023629325_p22646572"></a><a name="en-us_topic_0023629325_p22646572"></a>quota</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0023629325_p22433040"><a name="en-us_topic_0023629325_p22433040"></a><a name="en-us_topic_0023629325_p22433040"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0023629325_p5136981"><a name="en-us_topic_0023629325_p5136981"></a><a name="en-us_topic_0023629325_p5136981"></a>Specifies the total quota.</p>
    </td>
    </tr>
    <tr id="rc59af1fd68aa4416b9beae4ef5bea63b"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="a4b11e2ed89834661854fd6e10eac1f73"><a name="a4b11e2ed89834661854fd6e10eac1f73"></a><a name="a4b11e2ed89834661854fd6e10eac1f73"></a>max</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="a985ead989bff412eb0ef2b671f52ad6c"><a name="a985ead989bff412eb0ef2b671f52ad6c"></a><a name="a985ead989bff412eb0ef2b671f52ad6c"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="a2c7c700dec33419dae168096457fb307"><a name="a2c7c700dec33419dae168096457fb307"></a><a name="a2c7c700dec33419dae168096457fb307"></a>Specifies the quota upper limit.</p>
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
                    "type": "scaling_Policy",
                    "used": 2,
                    "quota": 50,
                    "max": 50
                },
                {
                    "type": "scaling_Instance",
                    "used": 0,
                    "quota": 200,
                    "max": 1000
                }
            ]
        }
    }
    ```


## Returned Values<a name="section12284267"></a>

-   Normal

    200

-   Abnormal

    <a name="table50448354"></a>
    <table><thead align="left"><tr id="row29530116"><th class="cellrowborder" valign="top" width="43.61%" id="mcps1.1.3.1.1"><p id="p43129175"><a name="p43129175"></a><a name="p43129175"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.38999999999999%" id="mcps1.1.3.1.2"><p id="p3802258"><a name="p3802258"></a><a name="p3802258"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39547486"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p49229794"><a name="p49229794"></a><a name="p49229794"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p28190407"><a name="p28190407"></a><a name="p28190407"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row52387077"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p15494878"><a name="p15494878"></a><a name="p15494878"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p47125611"><a name="p47125611"></a><a name="p47125611"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row21477321"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p61941440"><a name="p61941440"></a><a name="p61941440"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p51200735"><a name="p51200735"></a><a name="p51200735"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row58153438"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p12808013"><a name="p12808013"></a><a name="p12808013"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p30816121"><a name="p30816121"></a><a name="p30816121"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row8909633"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p50591634"><a name="p50591634"></a><a name="p50591634"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p4281684"><a name="p4281684"></a><a name="p4281684"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row38535158"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p34340132"><a name="p34340132"></a><a name="p34340132"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p30087318"><a name="p30087318"></a><a name="p30087318"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row2350413"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p56165728"><a name="p56165728"></a><a name="p56165728"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p53130157"><a name="p53130157"></a><a name="p53130157"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row8409368"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p10070188"><a name="p10070188"></a><a name="p10070188"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p10378893"><a name="p10378893"></a><a name="p10378893"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row26301173"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p50020275"><a name="p50020275"></a><a name="p50020275"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p25110514"><a name="p25110514"></a><a name="p25110514"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row24668042"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p51954348"><a name="p51954348"></a><a name="p51954348"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p47552675"><a name="p47552675"></a><a name="p47552675"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row25320898"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p37726867"><a name="p37726867"></a><a name="p37726867"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p35977388"><a name="p35977388"></a><a name="p35977388"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row55361044"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p55059565"><a name="p55059565"></a><a name="p55059565"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p30639779"><a name="p30639779"></a><a name="p30639779"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row7322556"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p56256135"><a name="p56256135"></a><a name="p56256135"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p60453091"><a name="p60453091"></a><a name="p60453091"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row7206911"><td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.3.1.1 "><p id="p46888886"><a name="p46888886"></a><a name="p46888886"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.38999999999999%" headers="mcps1.1.3.1.2 "><p id="p39903442"><a name="p39903442"></a><a name="p39903442"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

