# Deleting a Certificate<a name="EN-US_TOPIC_0096561524"></a>

## Function<a name="en-us_topic_0032340348_section65858198"></a>

This API is used to delete a certificate.

## URI<a name="en-us_topic_0032340348_section55852871"></a>

DELETE /v1.0/\{project\_id\}/elbaas/certificate/\{certificate\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0032340348_table60083059"></a>
<table><thead align="left"><tr id="en-us_topic_0032340348_row2365466"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="en-us_topic_0032340348_p57385070"><a name="en-us_topic_0032340348_p57385070"></a><a name="en-us_topic_0032340348_p57385070"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0032340348_p17679057"><a name="en-us_topic_0032340348_p17679057"></a><a name="en-us_topic_0032340348_p17679057"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0032340348_p8494842115611"><a name="en-us_topic_0032340348_p8494842115611"></a><a name="en-us_topic_0032340348_p8494842115611"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.5.1.4"><p id="en-us_topic_0032340348_p22717550"><a name="en-us_topic_0032340348_p22717550"></a><a name="en-us_topic_0032340348_p22717550"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0032340348_row2494884611413"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p1618112015176"><a name="p1618112015176"></a><a name="p1618112015176"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0032340348_p277447511413"><a name="en-us_topic_0032340348_p277447511413"></a><a name="en-us_topic_0032340348_p277447511413"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0032340348_p34302895115611"><a name="en-us_topic_0032340348_p34302895115611"></a><a name="en-us_topic_0032340348_p34302895115611"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0032340348_p1683029111413"><a name="en-us_topic_0032340348_p1683029111413"></a><a name="en-us_topic_0032340348_p1683029111413"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0032340348_row56497187115316"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0032340348_p27676371115320"><a name="en-us_topic_0032340348_p27676371115320"></a><a name="en-us_topic_0032340348_p27676371115320"></a>certificate_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0032340348_p27193612115320"><a name="en-us_topic_0032340348_p27193612115320"></a><a name="en-us_topic_0032340348_p27193612115320"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0032340348_p42313093115611"><a name="en-us_topic_0032340348_p42313093115611"></a><a name="en-us_topic_0032340348_p42313093115611"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0032340348_p55198969115320"><a name="en-us_topic_0032340348_p55198969115320"></a><a name="en-us_topic_0032340348_p55198969115320"></a>Specifies the certificate ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0032340348_section32913796"></a>

-   Request parameters

    None


-   Example request

    None


## Response<a name="en-us_topic_0032340348_section27788708"></a>

-   Response parameters

    None


-   Example response

    None


## Status Code<a name="en-us_topic_0032340348_section48771786"></a>

-   Normal

    204

-   Abnormal

    <a name="en-us_topic_0032340348_table48328251151534"></a>
    <table><thead align="left"><tr id="en-us_topic_0032340348_row64711061151534"><th class="cellrowborder" valign="top" width="10.17%" id="mcps1.1.4.1.1"><p id="en-us_topic_0032340348_p7104561151534"><a name="en-us_topic_0032340348_p7104561151534"></a><a name="en-us_topic_0032340348_p7104561151534"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.59%" id="mcps1.1.4.1.2"><p id="p5462524132411"><a name="p5462524132411"></a><a name="p5462524132411"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0032340348_p38598594151534"><a name="en-us_topic_0032340348_p38598594151534"></a><a name="en-us_topic_0032340348_p38598594151534"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032340348_row39478448151534"><td class="cellrowborder" valign="top" width="10.17%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0032340348_p43637730151534"><a name="en-us_topic_0032340348_p43637730151534"></a><a name="en-us_topic_0032340348_p43637730151534"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.59%" headers="mcps1.1.4.1.2 "><p id="p20926113432416"><a name="p20926113432416"></a><a name="p20926113432416"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0032340348_p44995265151534"><a name="en-us_topic_0032340348_p44995265151534"></a><a name="en-us_topic_0032340348_p44995265151534"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340348_row2304204151534"><td class="cellrowborder" valign="top" width="10.17%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0032340348_p52422873151534"><a name="en-us_topic_0032340348_p52422873151534"></a><a name="en-us_topic_0032340348_p52422873151534"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.59%" headers="mcps1.1.4.1.2 "><p id="p15926034112413"><a name="p15926034112413"></a><a name="p15926034112413"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0032340348_p18394310151534"><a name="en-us_topic_0032340348_p18394310151534"></a><a name="en-us_topic_0032340348_p18394310151534"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340348_row31331064151534"><td class="cellrowborder" valign="top" width="10.17%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0032340348_p54788249151534"><a name="en-us_topic_0032340348_p54788249151534"></a><a name="en-us_topic_0032340348_p54788249151534"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.59%" headers="mcps1.1.4.1.2 "><p id="p199261834152412"><a name="p199261834152412"></a><a name="p199261834152412"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0032340348_p8663150151534"><a name="en-us_topic_0032340348_p8663150151534"></a><a name="en-us_topic_0032340348_p8663150151534"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340348_row10859487151534"><td class="cellrowborder" valign="top" width="10.17%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0032340348_p7203294151534"><a name="en-us_topic_0032340348_p7203294151534"></a><a name="en-us_topic_0032340348_p7203294151534"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.59%" headers="mcps1.1.4.1.2 "><p id="p1492663472418"><a name="p1492663472418"></a><a name="p1492663472418"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0032340348_p46595974151534"><a name="en-us_topic_0032340348_p46595974151534"></a><a name="en-us_topic_0032340348_p46595974151534"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340348_row16710584151534"><td class="cellrowborder" valign="top" width="10.17%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0032340348_p11380079151534"><a name="en-us_topic_0032340348_p11380079151534"></a><a name="en-us_topic_0032340348_p11380079151534"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.59%" headers="mcps1.1.4.1.2 "><p id="p10926103410244"><a name="p10926103410244"></a><a name="p10926103410244"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0032340348_p49371235151534"><a name="en-us_topic_0032340348_p49371235151534"></a><a name="en-us_topic_0032340348_p49371235151534"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032340348_row41687935151534"><td class="cellrowborder" valign="top" width="10.17%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0032340348_p21279576151534"><a name="en-us_topic_0032340348_p21279576151534"></a><a name="en-us_topic_0032340348_p21279576151534"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.59%" headers="mcps1.1.4.1.2 "><p id="p7926113411242"><a name="p7926113411242"></a><a name="p7926113411242"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0032340348_p45924130151534"><a name="en-us_topic_0032340348_p45924130151534"></a><a name="en-us_topic_0032340348_p45924130151534"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


