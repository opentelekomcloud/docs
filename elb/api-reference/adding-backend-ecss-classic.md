# Adding Backend ECSs<a name="EN-US_TOPIC_0096561517"></a>

## Function<a name="en-us_topic_0020100170_section27437792"></a>

This API is used to add backend ECSs to a listener for monitoring.

To add backend ECSs to a UDP listener, IP addresses can be pinged and UDP services must be enabled.

## URI<a name="en-us_topic_0020100170_section45613538"></a>

POST /v1.0/\{project\_id\}/elbaas/listeners/\{listener\_id\}/members

**Table  1**  Parameter description

<a name="en-us_topic_0020100170_table43741849"></a>
<table><thead align="left"><tr id="en-us_topic_0020100170_row37304191"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100170_p1740610"><a name="en-us_topic_0020100170_p1740610"></a><a name="en-us_topic_0020100170_p1740610"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100170_p6771693"><a name="en-us_topic_0020100170_p6771693"></a><a name="en-us_topic_0020100170_p6771693"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100170_p3486881217106"><a name="en-us_topic_0020100170_p3486881217106"></a><a name="en-us_topic_0020100170_p3486881217106"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100170_p11636265"><a name="en-us_topic_0020100170_p11636265"></a><a name="en-us_topic_0020100170_p11636265"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100170_row3013405"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100170_p581271111018"><a name="en-us_topic_0020100170_p581271111018"></a><a name="en-us_topic_0020100170_p581271111018"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100170_p40949840"><a name="en-us_topic_0020100170_p40949840"></a><a name="en-us_topic_0020100170_p40949840"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100170_p580152017106"><a name="en-us_topic_0020100170_p580152017106"></a><a name="en-us_topic_0020100170_p580152017106"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100170_p28602718"><a name="en-us_topic_0020100170_p28602718"></a><a name="en-us_topic_0020100170_p28602718"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020100170_row56097870"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100170_p47633640"><a name="en-us_topic_0020100170_p47633640"></a><a name="en-us_topic_0020100170_p47633640"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100170_p33119622"><a name="en-us_topic_0020100170_p33119622"></a><a name="en-us_topic_0020100170_p33119622"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100170_p16114117106"><a name="en-us_topic_0020100170_p16114117106"></a><a name="en-us_topic_0020100170_p16114117106"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100170_p65443729"><a name="en-us_topic_0020100170_p65443729"></a><a name="en-us_topic_0020100170_p65443729"></a>Specifies the listener ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020100170_row52122650"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100170_p61185139"><a name="en-us_topic_0020100170_p61185139"></a><a name="en-us_topic_0020100170_p61185139"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100170_p57049196"><a name="en-us_topic_0020100170_p57049196"></a><a name="en-us_topic_0020100170_p57049196"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100170_p1305248317106"><a name="en-us_topic_0020100170_p1305248317106"></a><a name="en-us_topic_0020100170_p1305248317106"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100170_p48477080"><a name="en-us_topic_0020100170_p48477080"></a><a name="en-us_topic_0020100170_p48477080"></a>Specifies the backend ECS ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020100170_row33640543"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100170_p40529449"><a name="en-us_topic_0020100170_p40529449"></a><a name="en-us_topic_0020100170_p40529449"></a>address</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100170_p61659956"><a name="en-us_topic_0020100170_p61659956"></a><a name="en-us_topic_0020100170_p61659956"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100170_p5061817717106"><a name="en-us_topic_0020100170_p5061817717106"></a><a name="en-us_topic_0020100170_p5061817717106"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100170_p54278376"><a name="en-us_topic_0020100170_p54278376"></a><a name="en-us_topic_0020100170_p54278376"></a>Specifies the private IP address of the backend ECS.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100170_section7868661"></a>

-   Request parameters

    None


-   Example request

    ```
    [
        {
            "server_id": "dbecb618-2259-405f-ab17-9b68c4f541b0",
            "address": "172.16.0.31"
        }
    ]
    ```


## Response<a name="en-us_topic_0020100170_section3709091"></a>

-   Response parameters

    **Table  2**  Parameter description

    <a name="en-us_topic_0020100170_table5674616315485"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100170_row5776705315485"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100170_p4861969415485"><a name="en-us_topic_0020100170_p4861969415485"></a><a name="en-us_topic_0020100170_p4861969415485"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100170_p54243921194143"><a name="en-us_topic_0020100170_p54243921194143"></a><a name="en-us_topic_0020100170_p54243921194143"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="70%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100170_p2538749515485"><a name="en-us_topic_0020100170_p2538749515485"></a><a name="en-us_topic_0020100170_p2538749515485"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100170_row4312123015485"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100170_p315877015485"><a name="en-us_topic_0020100170_p315877015485"></a><a name="en-us_topic_0020100170_p315877015485"></a>uri</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100170_p3467534319420"><a name="en-us_topic_0020100170_p3467534319420"></a><a name="en-us_topic_0020100170_p3467534319420"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100170_p5516315115485"><a name="en-us_topic_0020100170_p5516315115485"></a><a name="en-us_topic_0020100170_p5516315115485"></a>Specifies the URI of the job for adding a backend ECS. It is returned by Combined API.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100170_row2670631315485"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100170_p1572777215485"><a name="en-us_topic_0020100170_p1572777215485"></a><a name="en-us_topic_0020100170_p1572777215485"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100170_p4539238919420"><a name="en-us_topic_0020100170_p4539238919420"></a><a name="en-us_topic_0020100170_p4539238919420"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100170_p4358967415485"><a name="en-us_topic_0020100170_p4358967415485"></a><a name="en-us_topic_0020100170_p4358967415485"></a>Specifies the unique ID assigned to the job for adding a backend ECS in Combined API.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "uri": "/v1/55300f3c8f764c06b1a32e2302edc305/jobs/4010b39b4fd3d5ff014fd3ec3ed8002d",
        "job_id": "4010b39b4fd3d5ff014fd3ec3ed8002d"
    }
    ```


## Status Code<a name="en-us_topic_0020100170_section33381819"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100170_table61845484151557"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100170_row50942692151557"><th class="cellrowborder" valign="top" width="12.13%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100170_p32717378151557"><a name="en-us_topic_0020100170_p32717378151557"></a><a name="en-us_topic_0020100170_p32717378151557"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.63%" id="mcps1.1.4.1.2"><p id="p1716210441164"><a name="p1716210441164"></a><a name="p1716210441164"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100170_p32861965151557"><a name="en-us_topic_0020100170_p32861965151557"></a><a name="en-us_topic_0020100170_p32861965151557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100170_row44573484151557"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100170_p53682440151557"><a name="en-us_topic_0020100170_p53682440151557"></a><a name="en-us_topic_0020100170_p53682440151557"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p5319115621611"><a name="p5319115621611"></a><a name="p5319115621611"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100170_p53310344151557"><a name="en-us_topic_0020100170_p53310344151557"></a><a name="en-us_topic_0020100170_p53310344151557"></a>Request error</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100170_row10031049151557"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100170_p7208635151557"><a name="en-us_topic_0020100170_p7208635151557"></a><a name="en-us_topic_0020100170_p7208635151557"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p1431965661612"><a name="p1431965661612"></a><a name="p1431965661612"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100170_p47028549151557"><a name="en-us_topic_0020100170_p47028549151557"></a><a name="en-us_topic_0020100170_p47028549151557"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100170_row20603763151557"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100170_p58292117151557"><a name="en-us_topic_0020100170_p58292117151557"></a><a name="en-us_topic_0020100170_p58292117151557"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p19319456111614"><a name="p19319456111614"></a><a name="p19319456111614"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100170_p24041060151557"><a name="en-us_topic_0020100170_p24041060151557"></a><a name="en-us_topic_0020100170_p24041060151557"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100170_row15042951151557"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100170_p10519556151557"><a name="en-us_topic_0020100170_p10519556151557"></a><a name="en-us_topic_0020100170_p10519556151557"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p031916561161"><a name="p031916561161"></a><a name="p031916561161"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100170_p46777697151557"><a name="en-us_topic_0020100170_p46777697151557"></a><a name="en-us_topic_0020100170_p46777697151557"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100170_row18346091151557"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100170_p9638396151557"><a name="en-us_topic_0020100170_p9638396151557"></a><a name="en-us_topic_0020100170_p9638396151557"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p1631925611616"><a name="p1631925611616"></a><a name="p1631925611616"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100170_p42512577151557"><a name="en-us_topic_0020100170_p42512577151557"></a><a name="en-us_topic_0020100170_p42512577151557"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100170_row47068874151557"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100170_p54482489151557"><a name="en-us_topic_0020100170_p54482489151557"></a><a name="en-us_topic_0020100170_p54482489151557"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.63%" headers="mcps1.1.4.1.2 "><p id="p1531965691616"><a name="p1531965691616"></a><a name="p1531965691616"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100170_p51005521151557"><a name="en-us_topic_0020100170_p51005521151557"></a><a name="en-us_topic_0020100170_p51005521151557"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


