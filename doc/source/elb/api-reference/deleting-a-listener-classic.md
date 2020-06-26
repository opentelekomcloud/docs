# Deleting a Listener<a name="EN-US_TOPIC_0096561507"></a>

## Function<a name="en-us_topic_0020100159_section60620523"></a>

This API is used to delete a listener.

## URI<a name="en-us_topic_0020100159_section8713795"></a>

DELETE /v1.0/\{project\_id\}/elbaas/listeners/\{listener\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0020100159_table14476932"></a>
<table><thead align="left"><tr id="en-us_topic_0020100159_row6756797"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100159_p10429724"><a name="en-us_topic_0020100159_p10429724"></a><a name="en-us_topic_0020100159_p10429724"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100159_p39501348"><a name="en-us_topic_0020100159_p39501348"></a><a name="en-us_topic_0020100159_p39501348"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100159_p45676946114930"><a name="en-us_topic_0020100159_p45676946114930"></a><a name="en-us_topic_0020100159_p45676946114930"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100159_p45492604"><a name="en-us_topic_0020100159_p45492604"></a><a name="en-us_topic_0020100159_p45492604"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100159_row581260011313"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p1121217613563"><a name="p1121217613563"></a><a name="p1121217613563"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100159_p952708311313"><a name="en-us_topic_0020100159_p952708311313"></a><a name="en-us_topic_0020100159_p952708311313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100159_p45365676114930"><a name="en-us_topic_0020100159_p45365676114930"></a><a name="en-us_topic_0020100159_p45365676114930"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100159_p3349624511313"><a name="en-us_topic_0020100159_p3349624511313"></a><a name="en-us_topic_0020100159_p3349624511313"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020100159_row61022284"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100159_p43857981"><a name="en-us_topic_0020100159_p43857981"></a><a name="en-us_topic_0020100159_p43857981"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100159_p62835574"><a name="en-us_topic_0020100159_p62835574"></a><a name="en-us_topic_0020100159_p62835574"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100159_p54492625114925"><a name="en-us_topic_0020100159_p54492625114925"></a><a name="en-us_topic_0020100159_p54492625114925"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100159_p56516768"><a name="en-us_topic_0020100159_p56516768"></a><a name="en-us_topic_0020100159_p56516768"></a>Specifies the listener ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100159_section11315292"></a>

-   Request parameters

    None


-   Example request

    None


## Response<a name="en-us_topic_0020100159_section34728767"></a>

-   Response parameters

    None


-   Example response

    None


## Status Code<a name="en-us_topic_0020100159_section44123454"></a>

-   Normal

    204

-   Abnormal

    <a name="en-us_topic_0020100159_table61925025151452"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100159_row50148870151452"><th class="cellrowborder" valign="top" width="12.13%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100159_p35526664151452"><a name="en-us_topic_0020100159_p35526664151452"></a><a name="en-us_topic_0020100159_p35526664151452"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.63%" id="mcps1.1.4.1.2"><p id="p49174305427"><a name="p49174305427"></a><a name="p49174305427"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100159_p59087522151452"><a name="en-us_topic_0020100159_p59087522151452"></a><a name="en-us_topic_0020100159_p59087522151452"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100159_row21359997151452"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100159_p52438209151452"><a name="en-us_topic_0020100159_p52438209151452"></a><a name="en-us_topic_0020100159_p52438209151452"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p426325214214"><a name="p426325214214"></a><a name="p426325214214"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100159_p19636500151452"><a name="en-us_topic_0020100159_p19636500151452"></a><a name="en-us_topic_0020100159_p19636500151452"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100159_row42510780151452"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100159_p20821164151452"><a name="en-us_topic_0020100159_p20821164151452"></a><a name="en-us_topic_0020100159_p20821164151452"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p15263352124211"><a name="p15263352124211"></a><a name="p15263352124211"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100159_p8792704151452"><a name="en-us_topic_0020100159_p8792704151452"></a><a name="en-us_topic_0020100159_p8792704151452"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100159_row12025475151452"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100159_p34539433151452"><a name="en-us_topic_0020100159_p34539433151452"></a><a name="en-us_topic_0020100159_p34539433151452"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p526310522424"><a name="p526310522424"></a><a name="p526310522424"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100159_p46230695151452"><a name="en-us_topic_0020100159_p46230695151452"></a><a name="en-us_topic_0020100159_p46230695151452"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100159_row13423079151452"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100159_p13527646151452"><a name="en-us_topic_0020100159_p13527646151452"></a><a name="en-us_topic_0020100159_p13527646151452"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p62631752144210"><a name="p62631752144210"></a><a name="p62631752144210"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100159_p21997504151452"><a name="en-us_topic_0020100159_p21997504151452"></a><a name="en-us_topic_0020100159_p21997504151452"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100159_row63759814151452"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100159_p64271286151452"><a name="en-us_topic_0020100159_p64271286151452"></a><a name="en-us_topic_0020100159_p64271286151452"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p1426311528422"><a name="p1426311528422"></a><a name="p1426311528422"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100159_p38591687151452"><a name="en-us_topic_0020100159_p38591687151452"></a><a name="en-us_topic_0020100159_p38591687151452"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100159_row11780867151452"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100159_p14726184151452"><a name="en-us_topic_0020100159_p14726184151452"></a><a name="en-us_topic_0020100159_p14726184151452"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p8263155294215"><a name="p8263155294215"></a><a name="p8263155294215"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100159_p51970241151452"><a name="en-us_topic_0020100159_p51970241151452"></a><a name="en-us_topic_0020100159_p51970241151452"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


