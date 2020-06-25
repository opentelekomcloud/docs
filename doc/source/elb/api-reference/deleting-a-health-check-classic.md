# Deleting a Health Check<a name="EN-US_TOPIC_0096561513"></a>

## Function<a name="en-us_topic_0020100165_section65858198"></a>

This API is used to delete a health check.

## URI<a name="en-us_topic_0020100165_section55852871"></a>

DELETE /v1.0/\{project\_id\}/elbaas/healthcheck/\{healthcheck\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0020100165_table60083059"></a>
<table><thead align="left"><tr id="en-us_topic_0020100165_row2365466"><th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100165_p57385070"><a name="en-us_topic_0020100165_p57385070"></a><a name="en-us_topic_0020100165_p57385070"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100165_p17679057"><a name="en-us_topic_0020100165_p17679057"></a><a name="en-us_topic_0020100165_p17679057"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100165_p8494842115611"><a name="en-us_topic_0020100165_p8494842115611"></a><a name="en-us_topic_0020100165_p8494842115611"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="54.545454545454554%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100165_p22717550"><a name="en-us_topic_0020100165_p22717550"></a><a name="en-us_topic_0020100165_p22717550"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row466316104617"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.1 "><p id="p196651616468"><a name="p196651616468"></a><a name="p196651616468"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p76661615469"><a name="p76661615469"></a><a name="p76661615469"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p866181644614"><a name="p866181644614"></a><a name="p866181644614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.5.1.4 "><p id="p136616164464"><a name="p136616164464"></a><a name="p136616164464"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020100165_row56497187115316"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100165_p27676371115320"><a name="en-us_topic_0020100165_p27676371115320"></a><a name="en-us_topic_0020100165_p27676371115320"></a>healthcheck_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100165_p27193612115320"><a name="en-us_topic_0020100165_p27193612115320"></a><a name="en-us_topic_0020100165_p27193612115320"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100165_p42313093115611"><a name="en-us_topic_0020100165_p42313093115611"></a><a name="en-us_topic_0020100165_p42313093115611"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100165_p55198969115320"><a name="en-us_topic_0020100165_p55198969115320"></a><a name="en-us_topic_0020100165_p55198969115320"></a>Specifies the health check ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100165_section32913796"></a>

-   Request parameters

    None


-   Example request

    None


## Response<a name="en-us_topic_0020100165_section27788708"></a>

-   Response parameters

    None


-   Example response

    None


## Status Code<a name="en-us_topic_0020100165_section48771786"></a>

-   Normal

    204

-   Abnormal

    <a name="en-us_topic_0020100165_table48328251151534"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100165_row64711061151534"><th class="cellrowborder" valign="top" width="12.520000000000001%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100165_p7104561151534"><a name="en-us_topic_0020100165_p7104561151534"></a><a name="en-us_topic_0020100165_p7104561151534"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.24%" id="mcps1.1.4.1.2"><p id="p1755217517138"><a name="p1755217517138"></a><a name="p1755217517138"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100165_p38598594151534"><a name="en-us_topic_0020100165_p38598594151534"></a><a name="en-us_topic_0020100165_p38598594151534"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100165_row39478448151534"><td class="cellrowborder" valign="top" width="12.520000000000001%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100165_p43637730151534"><a name="en-us_topic_0020100165_p43637730151534"></a><a name="en-us_topic_0020100165_p43637730151534"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.24%" headers="mcps1.1.4.1.2 "><p id="p130022481320"><a name="p130022481320"></a><a name="p130022481320"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100165_p44995265151534"><a name="en-us_topic_0020100165_p44995265151534"></a><a name="en-us_topic_0020100165_p44995265151534"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100165_row2304204151534"><td class="cellrowborder" valign="top" width="12.520000000000001%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100165_p52422873151534"><a name="en-us_topic_0020100165_p52422873151534"></a><a name="en-us_topic_0020100165_p52422873151534"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.24%" headers="mcps1.1.4.1.2 "><p id="p2300142441310"><a name="p2300142441310"></a><a name="p2300142441310"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100165_p18394310151534"><a name="en-us_topic_0020100165_p18394310151534"></a><a name="en-us_topic_0020100165_p18394310151534"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100165_row31331064151534"><td class="cellrowborder" valign="top" width="12.520000000000001%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100165_p54788249151534"><a name="en-us_topic_0020100165_p54788249151534"></a><a name="en-us_topic_0020100165_p54788249151534"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.24%" headers="mcps1.1.4.1.2 "><p id="p1830182410138"><a name="p1830182410138"></a><a name="p1830182410138"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100165_p8663150151534"><a name="en-us_topic_0020100165_p8663150151534"></a><a name="en-us_topic_0020100165_p8663150151534"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100165_row10859487151534"><td class="cellrowborder" valign="top" width="12.520000000000001%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100165_p7203294151534"><a name="en-us_topic_0020100165_p7203294151534"></a><a name="en-us_topic_0020100165_p7203294151534"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.24%" headers="mcps1.1.4.1.2 "><p id="p1130192441311"><a name="p1130192441311"></a><a name="p1130192441311"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100165_p46595974151534"><a name="en-us_topic_0020100165_p46595974151534"></a><a name="en-us_topic_0020100165_p46595974151534"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100165_row16710584151534"><td class="cellrowborder" valign="top" width="12.520000000000001%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100165_p11380079151534"><a name="en-us_topic_0020100165_p11380079151534"></a><a name="en-us_topic_0020100165_p11380079151534"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.24%" headers="mcps1.1.4.1.2 "><p id="p12301162413131"><a name="p12301162413131"></a><a name="p12301162413131"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100165_p49371235151534"><a name="en-us_topic_0020100165_p49371235151534"></a><a name="en-us_topic_0020100165_p49371235151534"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100165_row41687935151534"><td class="cellrowborder" valign="top" width="12.520000000000001%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100165_p21279576151534"><a name="en-us_topic_0020100165_p21279576151534"></a><a name="en-us_topic_0020100165_p21279576151534"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.24%" headers="mcps1.1.4.1.2 "><p id="p23011824131319"><a name="p23011824131319"></a><a name="p23011824131319"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100165_p45924130151534"><a name="en-us_topic_0020100165_p45924130151534"></a><a name="en-us_topic_0020100165_p45924130151534"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


