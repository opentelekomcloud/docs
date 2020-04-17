# Expanding EVS Disks in a Replication Consistency Group \(Deprecated\)<a name="evs_04_2059"></a>

## Function<a name="en-us_topic_0079692995_section39582655"></a>

This API is used to expand the EVS disks in one or multiple EVS replication pairs. In such an expansion operation, two EVS disks in one EVS replication pair are expanded together.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The  **status**  and  **replication\_status**  values of the replication consistency group remain unchanged before and after capacity expansion. When  **200**  is returned, the capacity expansion is complete.  
>If the expansion fails, contact technical support engineers to locate and rectify the fault. After the fault is rectified, expand the disks again.  
>If the capacities of multiple EVS replication pairs in a protection group are expanded, an error indicating incorrect capacity will occur after the capacity expansion.  
>This API has been deprecated. To use this function, see  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Constraints<a name="en-us_topic_0079692995_section66053444"></a>

-   The  **status**  value of the replication consistency group must be  **available**.
-   The  **replication\_status**  value of the replication consistency group cannot be  **error**.

## URI<a name="en-us_topic_0079692995_section57610085"></a>

-   URI

    POST /v2/\{project\_id\}/os-vendor-replication-consistency-groups/\{replication\_consistency\_group\_id\}/action

-   Parameter description

    <a name="en-us_topic_0079692995_table60281111"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692995_row54232412"><th class="cellrowborder" valign="top" width="26.83%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079692995_p30749271"><a name="en-us_topic_0079692995_p30749271"></a><a name="en-us_topic_0079692995_p30749271"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="29.270000000000003%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079692995_p38400427145446"><a name="en-us_topic_0079692995_p38400427145446"></a><a name="en-us_topic_0079692995_p38400427145446"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.9%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079692995_p59349811145459"><a name="en-us_topic_0079692995_p59349811145459"></a><a name="en-us_topic_0079692995_p59349811145459"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079692995_row16706408"><td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692995_p11041789"><a name="en-us_topic_0079692995_p11041789"></a><a name="en-us_topic_0079692995_p11041789"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692995_p21969731"><a name="en-us_topic_0079692995_p21969731"></a><a name="en-us_topic_0079692995_p21969731"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692995_p60677888"><a name="en-us_topic_0079692995_p60677888"></a><a name="en-us_topic_0079692995_p60677888"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692995_row9230088"><td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692995_p45753361203514"><a name="en-us_topic_0079692995_p45753361203514"></a><a name="en-us_topic_0079692995_p45753361203514"></a>replication_consistency_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692995_p26412257"><a name="en-us_topic_0079692995_p26412257"></a><a name="en-us_topic_0079692995_p26412257"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692995_p15736877"><a name="en-us_topic_0079692995_p15736877"></a><a name="en-us_topic_0079692995_p15736877"></a>Specifies the ID of the replication consistency group.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079692995_section48728718"></a>

-   Parameter description

    <a name="en-us_topic_0079692995_table36221483"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692995_row2537905"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079692995_p58125178145537"><a name="en-us_topic_0079692995_p58125178145537"></a><a name="en-us_topic_0079692995_p58125178145537"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079692995_p10518955145537"><a name="en-us_topic_0079692995_p10518955145537"></a><a name="en-us_topic_0079692995_p10518955145537"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.1.5.1.3"><p id="en-us_topic_0079692995_p46729058145537"><a name="en-us_topic_0079692995_p46729058145537"></a><a name="en-us_topic_0079692995_p46729058145537"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="35%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079692995_p26957316145537"><a name="en-us_topic_0079692995_p26957316145537"></a><a name="en-us_topic_0079692995_p26957316145537"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079692995_row61660876"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p66677196113435"><a name="p66677196113435"></a><a name="p66677196113435"></a>os-extend-replication-volumes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p32143823113435"><a name="p32143823113435"></a><a name="p32143823113435"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p53512850113435"><a name="p53512850113435"></a><a name="p53512850113435"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.5.1.4 "><p id="p39573565113435"><a name="p39573565113435"></a><a name="p39573565113435"></a>Specifies the EVS disk expansion operation.</p>
    </td>
    </tr>
    <tr id="row4794279113415"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p59426629113435"><a name="p59426629113435"></a><a name="p59426629113435"></a>replications</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p48827612113435"><a name="p48827612113435"></a><a name="p48827612113435"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p62722520113435"><a name="p62722520113435"></a><a name="p62722520113435"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.5.1.4 "><p id="p47359393113435"><a name="p47359393113435"></a><a name="p47359393113435"></a>Specifies the expansion information of one or multiple EVS replication pairs.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameters in the  **replications**  field

    <a name="table1248526215628"></a>
    <table><thead align="left"><tr id="row47877207215628"><th class="cellrowborder" valign="top" width="24.197580241975803%" id="mcps1.1.5.1.1"><p id="p52848519215628"><a name="p52848519215628"></a><a name="p52848519215628"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.73832616738326%" id="mcps1.1.5.1.2"><p id="p52871619215628"><a name="p52871619215628"></a><a name="p52871619215628"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.14868513148685%" id="mcps1.1.5.1.3"><p id="p54742772215628"><a name="p54742772215628"></a><a name="p54742772215628"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.1.5.1.4"><p id="p4979586215628"><a name="p4979586215628"></a><a name="p4979586215628"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54508746215628"><td class="cellrowborder" valign="top" width="24.197580241975803%" headers="mcps1.1.5.1.1 "><p id="p53132321215628"><a name="p53132321215628"></a><a name="p53132321215628"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.73832616738326%" headers="mcps1.1.5.1.2 "><p id="p8750773215628"><a name="p8750773215628"></a><a name="p8750773215628"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.14868513148685%" headers="mcps1.1.5.1.3 "><p id="p37724013215628"><a name="p37724013215628"></a><a name="p37724013215628"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.1.5.1.4 "><p id="p35746226215628"><a name="p35746226215628"></a><a name="p35746226215628"></a>Specifies the IDs of EVS replication pairs.</p>
    </td>
    </tr>
    <tr id="row53280580215628"><td class="cellrowborder" valign="top" width="24.197580241975803%" headers="mcps1.1.5.1.1 "><p id="p20759751215628"><a name="p20759751215628"></a><a name="p20759751215628"></a>new_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.73832616738326%" headers="mcps1.1.5.1.2 "><p id="p3818250215628"><a name="p3818250215628"></a><a name="p3818250215628"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.14868513148685%" headers="mcps1.1.5.1.3 "><p id="p40842805215628"><a name="p40842805215628"></a><a name="p40842805215628"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.1.5.1.4 "><p id="p19932913215628"><a name="p19932913215628"></a><a name="p19932913215628"></a>Specifies the disk capacity after expansion in the EVS replication pair. The unit is GB.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    { 
        "os-extend-replication-volumes": {
            "replications": [
                {"id": "25132c7a-bf71-4d18-8a2e-1ad11416c057", "new_size": 10},
                {"id": "6a61d65c-269e-4592-8a89-95742b075b1a", "new_size": 20}
            ]
        }
    }
    ```


## Response<a name="en-us_topic_0079692995_section35905280"></a>

None

## Status Codes<a name="en-us_topic_0079692995_section54712068"></a>

-   Normal

    <a name="evs_04_2046_table4315991194956"></a>
    <table><thead align="left"><tr id="evs_04_2046_row2336641294956"><th class="cellrowborder" valign="top" width="42.59%" id="mcps1.1.3.1.1"><p id="evs_04_2046_p1363125894956"><a name="evs_04_2046_p1363125894956"></a><a name="evs_04_2046_p1363125894956"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.410000000000004%" id="mcps1.1.3.1.2"><p id="evs_04_2046_p3039012494956"><a name="evs_04_2046_p3039012494956"></a><a name="evs_04_2046_p3039012494956"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2046_row507566794956"><td class="cellrowborder" valign="top" width="42.59%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_p847584694956"><a name="evs_04_2046_p847584694956"></a><a name="evs_04_2046_p847584694956"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.410000000000004%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_p1545496394956"><a name="evs_04_2046_p1545496394956"></a><a name="evs_04_2046_p1545496394956"></a>The server has processed the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="evs_04_2046_evs_04_2044_table22458872203835"></a>
    <table><thead align="left"><tr id="evs_04_2046_evs_04_2044_row35704554203835"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="evs_04_2046_evs_04_2044_p6387753203835"><a name="evs_04_2046_evs_04_2044_p6387753203835"></a><a name="evs_04_2046_evs_04_2044_p6387753203835"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="evs_04_2046_evs_04_2044_p47646009203835"><a name="evs_04_2046_evs_04_2044_p47646009203835"></a><a name="evs_04_2046_evs_04_2044_p47646009203835"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2046_evs_04_2044_row34121538203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p12381163203835"><a name="evs_04_2046_evs_04_2044_p12381163203835"></a><a name="evs_04_2046_evs_04_2044_p12381163203835"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p63350108203835"><a name="evs_04_2046_evs_04_2044_p63350108203835"></a><a name="evs_04_2046_evs_04_2044_p63350108203835"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="evs_04_2046_evs_04_2044_row33280063203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p11330608203835"><a name="evs_04_2046_evs_04_2044_p11330608203835"></a><a name="evs_04_2046_evs_04_2044_p11330608203835"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p45364094203835"><a name="evs_04_2046_evs_04_2044_p45364094203835"></a><a name="evs_04_2046_evs_04_2044_p45364094203835"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="evs_04_2046_evs_04_2044_row5623667203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p52863895203835"><a name="evs_04_2046_evs_04_2044_p52863895203835"></a><a name="evs_04_2046_evs_04_2044_p52863895203835"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p54117066203835"><a name="evs_04_2046_evs_04_2044_p54117066203835"></a><a name="evs_04_2046_evs_04_2044_p54117066203835"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="evs_04_2046_evs_04_2044_row17291554203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p58438642203835"><a name="evs_04_2046_evs_04_2044_p58438642203835"></a><a name="evs_04_2046_evs_04_2044_p58438642203835"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p35909542203835"><a name="evs_04_2046_evs_04_2044_p35909542203835"></a><a name="evs_04_2046_evs_04_2044_p35909542203835"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="evs_04_2046_evs_04_2044_row54750425203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p5599455203835"><a name="evs_04_2046_evs_04_2044_p5599455203835"></a><a name="evs_04_2046_evs_04_2044_p5599455203835"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p50902717203835"><a name="evs_04_2046_evs_04_2044_p50902717203835"></a><a name="evs_04_2046_evs_04_2044_p50902717203835"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="evs_04_2046_evs_04_2044_row55471277203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p63988484203835"><a name="evs_04_2046_evs_04_2044_p63988484203835"></a><a name="evs_04_2046_evs_04_2044_p63988484203835"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p15684678203835"><a name="evs_04_2046_evs_04_2044_p15684678203835"></a><a name="evs_04_2046_evs_04_2044_p15684678203835"></a>The response generated by the server cannot be accepted by the client.</p>
    </td>
    </tr>
    <tr id="evs_04_2046_evs_04_2044_row6944380203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p25623884203835"><a name="evs_04_2046_evs_04_2044_p25623884203835"></a><a name="evs_04_2046_evs_04_2044_p25623884203835"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p62268733203835"><a name="evs_04_2046_evs_04_2044_p62268733203835"></a><a name="evs_04_2046_evs_04_2044_p62268733203835"></a>You must use the proxy server for authentication. Then, the request can be processed.</p>
    </td>
    </tr>
    <tr id="evs_04_2046_evs_04_2044_row23547689203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p28314670203835"><a name="evs_04_2046_evs_04_2044_p28314670203835"></a><a name="evs_04_2046_evs_04_2044_p28314670203835"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p11786919203835"><a name="evs_04_2046_evs_04_2044_p11786919203835"></a><a name="evs_04_2046_evs_04_2044_p11786919203835"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="evs_04_2046_evs_04_2044_row38973411203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p2729702203835"><a name="evs_04_2046_evs_04_2044_p2729702203835"></a><a name="evs_04_2046_evs_04_2044_p2729702203835"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p19779281203835"><a name="evs_04_2046_evs_04_2044_p19779281203835"></a><a name="evs_04_2046_evs_04_2044_p19779281203835"></a>The request cannot be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="evs_04_2046_evs_04_2044_row43795805203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p57799353203835"><a name="evs_04_2046_evs_04_2044_p57799353203835"></a><a name="evs_04_2046_evs_04_2044_p57799353203835"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p51235984203835"><a name="evs_04_2046_evs_04_2044_p51235984203835"></a><a name="evs_04_2046_evs_04_2044_p51235984203835"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="evs_04_2046_evs_04_2044_row58470678203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p38504500203835"><a name="evs_04_2046_evs_04_2044_p38504500203835"></a><a name="evs_04_2046_evs_04_2044_p38504500203835"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p31856770203835"><a name="evs_04_2046_evs_04_2044_p31856770203835"></a><a name="evs_04_2046_evs_04_2044_p31856770203835"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="evs_04_2046_evs_04_2044_row18275474203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p3918444203835"><a name="evs_04_2046_evs_04_2044_p3918444203835"></a><a name="evs_04_2046_evs_04_2044_p3918444203835"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p48958538203835"><a name="evs_04_2046_evs_04_2044_p48958538203835"></a><a name="evs_04_2046_evs_04_2044_p48958538203835"></a>Failed to complete the request because the server has received an invalid response.</p>
    </td>
    </tr>
    <tr id="evs_04_2046_evs_04_2044_row37973662203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p55967806203835"><a name="evs_04_2046_evs_04_2044_p55967806203835"></a><a name="evs_04_2046_evs_04_2044_p55967806203835"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p37098455203835"><a name="evs_04_2046_evs_04_2044_p37098455203835"></a><a name="evs_04_2046_evs_04_2044_p37098455203835"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="evs_04_2046_evs_04_2044_row65450640203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_evs_04_2044_p67010448203835"><a name="evs_04_2046_evs_04_2044_p67010448203835"></a><a name="evs_04_2046_evs_04_2044_p67010448203835"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_evs_04_2044_p59137180203835"><a name="evs_04_2046_evs_04_2044_p59137180203835"></a><a name="evs_04_2046_evs_04_2044_p59137180203835"></a>A gateway timeout error occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


