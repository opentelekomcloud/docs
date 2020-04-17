# Reprotecting a Replication Consistency Group \(Deprecated\)<a name="evs_04_2058"></a>

## Function<a name="en-us_topic_0079692998_section33089041"></a>

This API is used to reprotect a replication consistency group. After resources in a faulty AZ have been restored and functioned as DR resources, a reprotection can be performed to synchronize data in all EVS replication pairs of a replication consistency group.

A reprotection can only be performed after the resources in the faulty primary AZ have been restored and can be used to synchronize data in all EVS replication pairs of a replication consistency group.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API has been deprecated. To use this function, see  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Constraints<a name="en-us_topic_0079692998_section29829272"></a>

-   The replication consistency group failover is complete.
-   The resources in the faulty AZ have been restored.
-   The replication consistency group status is  **failovered**.

## URI<a name="en-us_topic_0079692998_section27997"></a>

-   URI format

    POST /v2/\{project\_id\}/os-vendor-replication-consistency-groups/\{replication\_consistency\_group\_id\}/action

-   Parameter description

    <a name="en-us_topic_0079692998_table53759727"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692998_row7714425"><th class="cellrowborder" valign="top" width="26.83%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079692998_p29128759151416"><a name="en-us_topic_0079692998_p29128759151416"></a><a name="en-us_topic_0079692998_p29128759151416"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.490000000000002%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079692998_p14263389"><a name="en-us_topic_0079692998_p14263389"></a><a name="en-us_topic_0079692998_p14263389"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.68%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079692998_p32345284"><a name="en-us_topic_0079692998_p32345284"></a><a name="en-us_topic_0079692998_p32345284"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079692998_row2722332"><td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692998_p19182316"><a name="en-us_topic_0079692998_p19182316"></a><a name="en-us_topic_0079692998_p19182316"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.490000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692998_p10263773"><a name="en-us_topic_0079692998_p10263773"></a><a name="en-us_topic_0079692998_p10263773"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.68%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692998_p30427456"><a name="en-us_topic_0079692998_p30427456"></a><a name="en-us_topic_0079692998_p30427456"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692998_row5411655"><td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692998_p35003079204049"><a name="en-us_topic_0079692998_p35003079204049"></a><a name="en-us_topic_0079692998_p35003079204049"></a>replication_consistency_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.490000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692998_p5282487"><a name="en-us_topic_0079692998_p5282487"></a><a name="en-us_topic_0079692998_p5282487"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.68%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692998_p30225241"><a name="en-us_topic_0079692998_p30225241"></a><a name="en-us_topic_0079692998_p30225241"></a>Specifies the ID of the replication consistency group.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079692998_section251973"></a>

-   Parameter description

    <a name="en-us_topic_0079692998_table1113708"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692998_row1994095"><th class="cellrowborder" valign="top" width="24%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079692998_p63027149151532"><a name="en-us_topic_0079692998_p63027149151532"></a><a name="en-us_topic_0079692998_p63027149151532"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079692998_p4925445151532"><a name="en-us_topic_0079692998_p4925445151532"></a><a name="en-us_topic_0079692998_p4925445151532"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.3"><p id="en-us_topic_0079692998_p63416778151532"><a name="en-us_topic_0079692998_p63416778151532"></a><a name="en-us_topic_0079692998_p63416778151532"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="35%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079692998_p36485379151532"><a name="en-us_topic_0079692998_p36485379151532"></a><a name="en-us_topic_0079692998_p36485379151532"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079692998_row21591473"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692998_p5269608420414"><a name="en-us_topic_0079692998_p5269608420414"></a><a name="en-us_topic_0079692998_p5269608420414"></a>os-reprotect-replication-consistency-group</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692998_p61954093"><a name="en-us_topic_0079692998_p61954093"></a><a name="en-us_topic_0079692998_p61954093"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692998_p52225656"><a name="en-us_topic_0079692998_p52225656"></a><a name="en-us_topic_0079692998_p52225656"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692998_p5028360204111"><a name="en-us_topic_0079692998_p5028360204111"></a><a name="en-us_topic_0079692998_p5028360204111"></a>The parameter value is null, indicating that the replication consistency group will be reprotected.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "os-reprotect-replication-consistency-group": null
    }
    ```


## Response<a name="en-us_topic_0079692998_section2267763"></a>

None

## Status Codes<a name="en-us_topic_0079692998_section20409871"></a>

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


