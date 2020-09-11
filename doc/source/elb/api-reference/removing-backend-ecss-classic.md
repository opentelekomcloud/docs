# Removing Backend ECSs<a name="EN-US_TOPIC_0096561518"></a>

## Function<a name="en-us_topic_0020100171_section27335113"></a>

This API is used to remove backend ECSs from a listener. Multiple backend ECSs can be removed concurrently.

## URI<a name="en-us_topic_0020100171_section44689431"></a>

POST /v1.0/\{project\_id\}/elbaas/listeners/\{listener\_id\}/members/action

**Table  1**  Parameter description

<a name="en-us_topic_0020100171_table2389883410956"></a>
<table><thead align="left"><tr id="en-us_topic_0020100171_row6552405110956"><th class="cellrowborder" valign="top" width="14.851485148514849%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100171_p584790010956"><a name="en-us_topic_0020100171_p584790010956"></a><a name="en-us_topic_0020100171_p584790010956"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.86138613861386%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100171_p55718895101226"><a name="en-us_topic_0020100171_p55718895101226"></a><a name="en-us_topic_0020100171_p55718895101226"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.83168316831683%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100171_p391789010956"><a name="en-us_topic_0020100171_p391789010956"></a><a name="en-us_topic_0020100171_p391789010956"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.45544554455445%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100171_p4891364410956"><a name="en-us_topic_0020100171_p4891364410956"></a><a name="en-us_topic_0020100171_p4891364410956"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100171_row16412010101055"><td class="cellrowborder" valign="top" width="14.851485148514849%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100171_p16610190181117"><a name="en-us_topic_0020100171_p16610190181117"></a><a name="en-us_topic_0020100171_p16610190181117"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.86138613861386%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100171_p16936681101226"><a name="en-us_topic_0020100171_p16936681101226"></a><a name="en-us_topic_0020100171_p16936681101226"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.83168316831683%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100171_p61742775101339"><a name="en-us_topic_0020100171_p61742775101339"></a><a name="en-us_topic_0020100171_p61742775101339"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455445%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100171_p5121289310110"><a name="en-us_topic_0020100171_p5121289310110"></a><a name="en-us_topic_0020100171_p5121289310110"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020100171_row13982057101051"><td class="cellrowborder" valign="top" width="14.851485148514849%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100171_p2167081910110"><a name="en-us_topic_0020100171_p2167081910110"></a><a name="en-us_topic_0020100171_p2167081910110"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.86138613861386%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100171_p29693948101226"><a name="en-us_topic_0020100171_p29693948101226"></a><a name="en-us_topic_0020100171_p29693948101226"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.83168316831683%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100171_p13055406101341"><a name="en-us_topic_0020100171_p13055406101341"></a><a name="en-us_topic_0020100171_p13055406101341"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455445%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100171_p848439410110"><a name="en-us_topic_0020100171_p848439410110"></a><a name="en-us_topic_0020100171_p848439410110"></a>Specifies the listener ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020100171_row258221010956"><td class="cellrowborder" valign="top" width="14.851485148514849%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100171_p783249410956"><a name="en-us_topic_0020100171_p783249410956"></a><a name="en-us_topic_0020100171_p783249410956"></a>removeMember</p>
</td>
<td class="cellrowborder" valign="top" width="13.86138613861386%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100171_p56399567101226"><a name="en-us_topic_0020100171_p56399567101226"></a><a name="en-us_topic_0020100171_p56399567101226"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.83168316831683%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100171_p3045224510956"><a name="en-us_topic_0020100171_p3045224510956"></a><a name="en-us_topic_0020100171_p3045224510956"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455445%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100171_p5376203310956"><a name="en-us_topic_0020100171_p5376203310956"></a><a name="en-us_topic_0020100171_p5376203310956"></a>Lists the removed backend ECSs.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **removeMember**  parameter description

<a name="en-us_topic_0020100171_table2866234101024"></a>
<table><thead align="left"><tr id="en-us_topic_0020100171_row42680771101024"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100171_p34590428101024"><a name="en-us_topic_0020100171_p34590428101024"></a><a name="en-us_topic_0020100171_p34590428101024"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100171_p50361318101024"><a name="en-us_topic_0020100171_p50361318101024"></a><a name="en-us_topic_0020100171_p50361318101024"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100171_p52734985101024"><a name="en-us_topic_0020100171_p52734985101024"></a><a name="en-us_topic_0020100171_p52734985101024"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100171_p43675372101024"><a name="en-us_topic_0020100171_p43675372101024"></a><a name="en-us_topic_0020100171_p43675372101024"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100171_row64960772101024"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100171_p27331197101024"><a name="en-us_topic_0020100171_p27331197101024"></a><a name="en-us_topic_0020100171_p27331197101024"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100171_p66343318101024"><a name="en-us_topic_0020100171_p66343318101024"></a><a name="en-us_topic_0020100171_p66343318101024"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100171_p5099639101024"><a name="en-us_topic_0020100171_p5099639101024"></a><a name="en-us_topic_0020100171_p5099639101024"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100171_p35821662193932"><a name="en-us_topic_0020100171_p35821662193932"></a><a name="en-us_topic_0020100171_p35821662193932"></a>Specifies the backend ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100171_section66660559"></a>

-   Request parameters

    None


-   Example request

    ```
    {
        "removeMember": [
            {
                "id": "34695d664b182fa69b98228032b0e239"
            }
        ]
    }
    ```


## Response<a name="en-us_topic_0020100171_section63074124"></a>

-   Response parameters

    **Table  3**  Parameter description

    <a name="en-us_topic_0020100171_table34189722154820"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100171_row28187955154820"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100171_p1522982154820"><a name="en-us_topic_0020100171_p1522982154820"></a><a name="en-us_topic_0020100171_p1522982154820"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100171_p1435599194226"><a name="en-us_topic_0020100171_p1435599194226"></a><a name="en-us_topic_0020100171_p1435599194226"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="72%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100171_p60179296154820"><a name="en-us_topic_0020100171_p60179296154820"></a><a name="en-us_topic_0020100171_p60179296154820"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100171_row42684789154820"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100171_p34915899154820"><a name="en-us_topic_0020100171_p34915899154820"></a><a name="en-us_topic_0020100171_p34915899154820"></a>uri</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100171_p23729422194226"><a name="en-us_topic_0020100171_p23729422194226"></a><a name="en-us_topic_0020100171_p23729422194226"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100171_p40664312154820"><a name="en-us_topic_0020100171_p40664312154820"></a><a name="en-us_topic_0020100171_p40664312154820"></a>Specifies the URI of the task for removing a backend ECS. It is returned by Combined API.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100171_row30434496154820"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100171_p49275074154820"><a name="en-us_topic_0020100171_p49275074154820"></a><a name="en-us_topic_0020100171_p49275074154820"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100171_p51771047194226"><a name="en-us_topic_0020100171_p51771047194226"></a><a name="en-us_topic_0020100171_p51771047194226"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100171_p30367149154820"><a name="en-us_topic_0020100171_p30367149154820"></a><a name="en-us_topic_0020100171_p30367149154820"></a>Specifies the unique ID assigned to the task for removing a backend ECS in Combined API.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "uri": "/v1/55300f3c8f764c06b1a32e2302edc305/jobs/4010b39b4fd3d5ff014fd3f160fd006c",
        "job_id": "4010b39b4fd3d5ff014fd3f160fd006c"
    }
    ```


## Status Code<a name="en-us_topic_0020100171_section30796205"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100171_table2880523115166"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100171_row4595411015166"><th class="cellrowborder" valign="top" width="28.810000000000002%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100171_p3129546315166"><a name="en-us_topic_0020100171_p3129546315166"></a><a name="en-us_topic_0020100171_p3129546315166"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.95%" id="mcps1.1.4.1.2"><p id="p11764826191817"><a name="p11764826191817"></a><a name="p11764826191817"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100171_p5190458015166"><a name="en-us_topic_0020100171_p5190458015166"></a><a name="en-us_topic_0020100171_p5190458015166"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100171_row4352147015166"><td class="cellrowborder" valign="top" width="28.810000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100171_p3557817215166"><a name="en-us_topic_0020100171_p3557817215166"></a><a name="en-us_topic_0020100171_p3557817215166"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.95%" headers="mcps1.1.4.1.2 "><p id="p11757124041812"><a name="p11757124041812"></a><a name="p11757124041812"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100171_p6325968715166"><a name="en-us_topic_0020100171_p6325968715166"></a><a name="en-us_topic_0020100171_p6325968715166"></a>Request error</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100171_row3246627215166"><td class="cellrowborder" valign="top" width="28.810000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100171_p1252239315166"><a name="en-us_topic_0020100171_p1252239315166"></a><a name="en-us_topic_0020100171_p1252239315166"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.95%" headers="mcps1.1.4.1.2 "><p id="p167581340151820"><a name="p167581340151820"></a><a name="p167581340151820"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100171_p768088215166"><a name="en-us_topic_0020100171_p768088215166"></a><a name="en-us_topic_0020100171_p768088215166"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100171_row201907415166"><td class="cellrowborder" valign="top" width="28.810000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100171_p2932727815166"><a name="en-us_topic_0020100171_p2932727815166"></a><a name="en-us_topic_0020100171_p2932727815166"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.95%" headers="mcps1.1.4.1.2 "><p id="p675815402181"><a name="p675815402181"></a><a name="p675815402181"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100171_p2669934315166"><a name="en-us_topic_0020100171_p2669934315166"></a><a name="en-us_topic_0020100171_p2669934315166"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100171_row3896750315166"><td class="cellrowborder" valign="top" width="28.810000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100171_p225119415166"><a name="en-us_topic_0020100171_p225119415166"></a><a name="en-us_topic_0020100171_p225119415166"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.95%" headers="mcps1.1.4.1.2 "><p id="p075817408183"><a name="p075817408183"></a><a name="p075817408183"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100171_p4812903815166"><a name="en-us_topic_0020100171_p4812903815166"></a><a name="en-us_topic_0020100171_p4812903815166"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100171_row3050815815166"><td class="cellrowborder" valign="top" width="28.810000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100171_p5524172915166"><a name="en-us_topic_0020100171_p5524172915166"></a><a name="en-us_topic_0020100171_p5524172915166"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.95%" headers="mcps1.1.4.1.2 "><p id="p975854041812"><a name="p975854041812"></a><a name="p975854041812"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100171_p4539507315166"><a name="en-us_topic_0020100171_p4539507315166"></a><a name="en-us_topic_0020100171_p4539507315166"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100171_row590247515166"><td class="cellrowborder" valign="top" width="28.810000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100171_p833844815166"><a name="en-us_topic_0020100171_p833844815166"></a><a name="en-us_topic_0020100171_p833844815166"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.95%" headers="mcps1.1.4.1.2 "><p id="p9758104017181"><a name="p9758104017181"></a><a name="p9758104017181"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100171_p432570215166"><a name="en-us_topic_0020100171_p432570215166"></a><a name="en-us_topic_0020100171_p432570215166"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


