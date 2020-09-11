# Modifying a Load Balancer<a name="EN-US_TOPIC_0096561502"></a>

## Function<a name="en-us_topic_0020100180_section14774201"></a>

This API is used to modify the name, description, bandwidth, and administrative status of a load balancer.

## URI<a name="en-us_topic_0020100180_section65858952"></a>

PUT /v1.0/\{project\_id\}/elbaas/loadbalancers/\{loadbalancer\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0020100180_table60701234"></a>
<table><thead align="left"><tr id="en-us_topic_0020100180_row28107703"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100180_p62131436"><a name="en-us_topic_0020100180_p62131436"></a><a name="en-us_topic_0020100180_p62131436"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100180_p66590397"><a name="en-us_topic_0020100180_p66590397"></a><a name="en-us_topic_0020100180_p66590397"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100180_p33376525175115"><a name="en-us_topic_0020100180_p33376525175115"></a><a name="en-us_topic_0020100180_p33376525175115"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100180_p25113108"><a name="en-us_topic_0020100180_p25113108"></a><a name="en-us_topic_0020100180_p25113108"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100180_row20895830"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100180_p147097427438"><a name="en-us_topic_0020100180_p147097427438"></a><a name="en-us_topic_0020100180_p147097427438"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100180_p61244865"><a name="en-us_topic_0020100180_p61244865"></a><a name="en-us_topic_0020100180_p61244865"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100180_p19144033175115"><a name="en-us_topic_0020100180_p19144033175115"></a><a name="en-us_topic_0020100180_p19144033175115"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100180_p61887033"><a name="en-us_topic_0020100180_p61887033"></a><a name="en-us_topic_0020100180_p61887033"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020100180_row20112390"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100180_p18490928"><a name="en-us_topic_0020100180_p18490928"></a><a name="en-us_topic_0020100180_p18490928"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100180_p21370227"><a name="en-us_topic_0020100180_p21370227"></a><a name="en-us_topic_0020100180_p21370227"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100180_p7162841175115"><a name="en-us_topic_0020100180_p7162841175115"></a><a name="en-us_topic_0020100180_p7162841175115"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100180_p53266806"><a name="en-us_topic_0020100180_p53266806"></a><a name="en-us_topic_0020100180_p53266806"></a>Specifies the load balancer ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020100180_row9639207"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100180_p42578285"><a name="en-us_topic_0020100180_p42578285"></a><a name="en-us_topic_0020100180_p42578285"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100180_p26289097"><a name="en-us_topic_0020100180_p26289097"></a><a name="en-us_topic_0020100180_p26289097"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100180_p43319262175115"><a name="en-us_topic_0020100180_p43319262175115"></a><a name="en-us_topic_0020100180_p43319262175115"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100180_ul3723649510411"></a><a name="en-us_topic_0020100180_ul3723649510411"></a><ul id="en-us_topic_0020100180_ul3723649510411"><li>Specifies the load balancer name.</li><li>The value is a string of 1 to 64 characters that consist of Chinese characters, letters, digits, underscores (_), and hyphens (-).</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100180_row49761220"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100180_p4126994"><a name="en-us_topic_0020100180_p4126994"></a><a name="en-us_topic_0020100180_p4126994"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100180_p65851064"><a name="en-us_topic_0020100180_p65851064"></a><a name="en-us_topic_0020100180_p65851064"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100180_p19199319175115"><a name="en-us_topic_0020100180_p19199319175115"></a><a name="en-us_topic_0020100180_p19199319175115"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100180_ul3786846510422"></a><a name="en-us_topic_0020100180_ul3786846510422"></a><ul id="en-us_topic_0020100180_ul3786846510422"><li>Provides supplementary information about the load balancer.</li><li>The value contains 0 to 128 characters and cannot contain angle brackets (&lt; and &gt;).</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100180_row17708965"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100180_p25140036"><a name="en-us_topic_0020100180_p25140036"></a><a name="en-us_topic_0020100180_p25140036"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100180_p23077024"><a name="en-us_topic_0020100180_p23077024"></a><a name="en-us_topic_0020100180_p23077024"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100180_p11641005175115"><a name="en-us_topic_0020100180_p11641005175115"></a><a name="en-us_topic_0020100180_p11641005175115"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100180_ul1560228310434"></a><a name="en-us_topic_0020100180_ul1560228310434"></a><ul id="en-us_topic_0020100180_ul1560228310434"><li>Specifies the bandwidth (Mbit/s). This parameter is mandatory when <strong id="en-us_topic_0020100178_b84235270614519"><a name="en-us_topic_0020100178_b84235270614519"></a><a name="en-us_topic_0020100178_b84235270614519"></a>type</strong>&nbsp;is set to&nbsp;<strong id="en-us_topic_0020100178_b842352706145112"><a name="en-us_topic_0020100178_b842352706145112"></a><a name="en-us_topic_0020100178_b842352706145112"></a>External</strong>.</li><li>The value ranges from 1 to 500.<p id="en-us_topic_0020100178_p116594145716"><a name="en-us_topic_0020100178_p116594145716"></a><a name="en-us_topic_0020100178_p116594145716"></a>(The specific range may vary depending on the configuration in each region. You can see the bandwidth range of each region on the management console.)</p>
</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100180_row29706771"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100180_p57438237"><a name="en-us_topic_0020100180_p57438237"></a><a name="en-us_topic_0020100180_p57438237"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100180_p21985640"><a name="en-us_topic_0020100180_p21985640"></a><a name="en-us_topic_0020100180_p21985640"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100180_p3397319175115"><a name="en-us_topic_0020100180_p3397319175115"></a><a name="en-us_topic_0020100180_p3397319175115"></a>Integer/Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100180_ul61364802191255"></a><a name="en-us_topic_0020100180_ul61364802191255"></a><ul id="en-us_topic_0020100180_ul61364802191255"><li>Specifies the administrative status of the load balancer.</li><li>Optional values:<p id="en-us_topic_0020100180_p30211343114910"><a name="en-us_topic_0020100180_p30211343114910"></a><a name="en-us_topic_0020100180_p30211343114910"></a><strong id="en-us_topic_0020100180_b842352706162920"><a name="en-us_topic_0020100180_b842352706162920"></a><a name="en-us_topic_0020100180_b842352706162920"></a>0</strong> or <strong id="en-us_topic_0020100180_b842352706162916"><a name="en-us_topic_0020100180_b842352706162916"></a><a name="en-us_topic_0020100180_b842352706162916"></a>false</strong>: indicates that the load balancer is stopped. Only tenants are allowed to enter these two values. </p>
<p id="en-us_topic_0020100180_p20886257114912"><a name="en-us_topic_0020100180_p20886257114912"></a><a name="en-us_topic_0020100180_p20886257114912"></a><strong id="en-us_topic_0020100180_b842352706163138"><a name="en-us_topic_0020100180_b842352706163138"></a><a name="en-us_topic_0020100180_b842352706163138"></a>1</strong> or <strong id="en-us_topic_0020100180_b842352706163141"><a name="en-us_topic_0020100180_b842352706163141"></a><a name="en-us_topic_0020100180_b842352706163141"></a>true</strong>: indicates that the load balancer is running properly.</p>
<p id="en-us_topic_0020100180_p5341487114913"><a name="en-us_topic_0020100180_p5341487114913"></a><a name="en-us_topic_0020100180_p5341487114913"></a><strong id="en-us_topic_0020100180_b842352706163213"><a name="en-us_topic_0020100180_b842352706163213"></a><a name="en-us_topic_0020100180_b842352706163213"></a>2</strong> or <strong id="en-us_topic_0020100180_b842352706163217"><a name="en-us_topic_0020100180_b842352706163217"></a><a name="en-us_topic_0020100180_b842352706163217"></a>false</strong>: indicates that the load balancer is frozen. Only the administrator is allowed to enter the two values. </p>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100180_section55859657"></a>

-   Request parameters

    None


-   Example request

    ```
    {
        "description": "simple lb",
        "name": "loadbalancer1",
        "bandwidth": 200,
        "admin_state_up": true
    }
    ```


## Response<a name="en-us_topic_0020100180_section32974871"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0020100180_table46446566154513"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100180_row29945423154513"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100180_p9660181154513"><a name="en-us_topic_0020100180_p9660181154513"></a><a name="en-us_topic_0020100180_p9660181154513"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100180_p3913213217371"><a name="en-us_topic_0020100180_p3913213217371"></a><a name="en-us_topic_0020100180_p3913213217371"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="67%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100180_p29686088154513"><a name="en-us_topic_0020100180_p29686088154513"></a><a name="en-us_topic_0020100180_p29686088154513"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100180_row55762948154513"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100180_p20504973154513"><a name="en-us_topic_0020100180_p20504973154513"></a><a name="en-us_topic_0020100180_p20504973154513"></a>uri</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100180_p5451562217371"><a name="en-us_topic_0020100180_p5451562217371"></a><a name="en-us_topic_0020100180_p5451562217371"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100180_p46968100154513"><a name="en-us_topic_0020100180_p46968100154513"></a><a name="en-us_topic_0020100180_p46968100154513"></a>Specifies the URI returned by Combined API after the job for modifying a load balancer is issued.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100180_row20059719154513"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100180_p14224534154513"><a name="en-us_topic_0020100180_p14224534154513"></a><a name="en-us_topic_0020100180_p14224534154513"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100180_p1344144117371"><a name="en-us_topic_0020100180_p1344144117371"></a><a name="en-us_topic_0020100180_p1344144117371"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100180_p45851855154513"><a name="en-us_topic_0020100180_p45851855154513"></a><a name="en-us_topic_0020100180_p45851855154513"></a>Specifies the unique job ID in Combined API. </p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "uri": "/v1/73cd9140bec7427ab9952b4ed75924e0/jobs/4010b39d4fbb4645014fcfddf4b32d15",
        "job_id": "4010b39d4fbb4645014fcfddf4b32d15"
    }
    ```


## Status Code<a name="en-us_topic_0020100180_section28338386"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100180_table11568432151419"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100180_row3241383151419"><th class="cellrowborder" valign="top" width="13.56%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100180_p61225504151419"><a name="en-us_topic_0020100180_p61225504151419"></a><a name="en-us_topic_0020100180_p61225504151419"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.2%" id="mcps1.1.4.1.2"><p id="p1465453925113"><a name="p1465453925113"></a><a name="p1465453925113"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100180_p60318797151419"><a name="en-us_topic_0020100180_p60318797151419"></a><a name="en-us_topic_0020100180_p60318797151419"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100180_row53984407151419"><td class="cellrowborder" valign="top" width="13.56%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100180_p10660837151419"><a name="en-us_topic_0020100180_p10660837151419"></a><a name="en-us_topic_0020100180_p10660837151419"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.2%" headers="mcps1.1.4.1.2 "><p id="p1913315455215"><a name="p1913315455215"></a><a name="p1913315455215"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100180_p58221472151419"><a name="en-us_topic_0020100180_p58221472151419"></a><a name="en-us_topic_0020100180_p58221472151419"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100180_row54231201151419"><td class="cellrowborder" valign="top" width="13.56%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100180_p30651178151419"><a name="en-us_topic_0020100180_p30651178151419"></a><a name="en-us_topic_0020100180_p30651178151419"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.2%" headers="mcps1.1.4.1.2 "><p id="p12133045526"><a name="p12133045526"></a><a name="p12133045526"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100180_p66826323151419"><a name="en-us_topic_0020100180_p66826323151419"></a><a name="en-us_topic_0020100180_p66826323151419"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100180_row64565995151419"><td class="cellrowborder" valign="top" width="13.56%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100180_p62463079151419"><a name="en-us_topic_0020100180_p62463079151419"></a><a name="en-us_topic_0020100180_p62463079151419"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.2%" headers="mcps1.1.4.1.2 "><p id="p111331240528"><a name="p111331240528"></a><a name="p111331240528"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100180_p26344664151419"><a name="en-us_topic_0020100180_p26344664151419"></a><a name="en-us_topic_0020100180_p26344664151419"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100180_row35775392151419"><td class="cellrowborder" valign="top" width="13.56%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100180_p12125659151419"><a name="en-us_topic_0020100180_p12125659151419"></a><a name="en-us_topic_0020100180_p12125659151419"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.2%" headers="mcps1.1.4.1.2 "><p id="p61336410522"><a name="p61336410522"></a><a name="p61336410522"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100180_p42654335151419"><a name="en-us_topic_0020100180_p42654335151419"></a><a name="en-us_topic_0020100180_p42654335151419"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100180_row48344695151419"><td class="cellrowborder" valign="top" width="13.56%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100180_p23606218151419"><a name="en-us_topic_0020100180_p23606218151419"></a><a name="en-us_topic_0020100180_p23606218151419"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.2%" headers="mcps1.1.4.1.2 "><p id="p31331841522"><a name="p31331841522"></a><a name="p31331841522"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100180_p33055514151419"><a name="en-us_topic_0020100180_p33055514151419"></a><a name="en-us_topic_0020100180_p33055514151419"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100180_row29064172151419"><td class="cellrowborder" valign="top" width="13.56%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100180_p5387713151419"><a name="en-us_topic_0020100180_p5387713151419"></a><a name="en-us_topic_0020100180_p5387713151419"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.2%" headers="mcps1.1.4.1.2 "><p id="p20133843526"><a name="p20133843526"></a><a name="p20133843526"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100180_p33751623151419"><a name="en-us_topic_0020100180_p33751623151419"></a><a name="en-us_topic_0020100180_p33751623151419"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


