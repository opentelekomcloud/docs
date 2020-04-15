# Pausing a Replication Consistency Group \(Deprecated\)<a name="evs_04_2057"></a>

## Function<a name="en-us_topic_0079692997_section63544148"></a>

This API is used to pause a replication consistency group, that is, to pause the data synchronization in all EVS replication pairs of a replication consistency group.

Before deleting or updating a replication consistency group, you need to pause the replication consistency group.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API has been deprecated. To use this function, see  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Constraints<a name="en-us_topic_0079692997_section18568063"></a>

None

## URI<a name="en-us_topic_0079692997_section32894845"></a>

-   URI format

    POST /v2/\{project\_id\}/os-vendor-replication-consistency-groups/\{replication\_consistency\_group\_id\}/action

-   Parameter description

    <a name="en-us_topic_0079692997_table20038698"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692997_row64530307"><th class="cellrowborder" valign="top" width="26.19%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079692997_p663907641549"><a name="en-us_topic_0079692997_p663907641549"></a><a name="en-us_topic_0079692997_p663907641549"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="29.759999999999998%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079692997_p60632485"><a name="en-us_topic_0079692997_p60632485"></a><a name="en-us_topic_0079692997_p60632485"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.05%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079692997_p55501577"><a name="en-us_topic_0079692997_p55501577"></a><a name="en-us_topic_0079692997_p55501577"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079692997_row66442792"><td class="cellrowborder" valign="top" width="26.19%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692997_p13157104"><a name="en-us_topic_0079692997_p13157104"></a><a name="en-us_topic_0079692997_p13157104"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.759999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692997_p59092488"><a name="en-us_topic_0079692997_p59092488"></a><a name="en-us_topic_0079692997_p59092488"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.05%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692997_p17907785"><a name="en-us_topic_0079692997_p17907785"></a><a name="en-us_topic_0079692997_p17907785"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692997_row26952341"><td class="cellrowborder" valign="top" width="26.19%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692997_p21100049203910"><a name="en-us_topic_0079692997_p21100049203910"></a><a name="en-us_topic_0079692997_p21100049203910"></a>replication_consistency_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.759999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692997_p2675193615723"><a name="en-us_topic_0079692997_p2675193615723"></a><a name="en-us_topic_0079692997_p2675193615723"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.05%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692997_p14114947"><a name="en-us_topic_0079692997_p14114947"></a><a name="en-us_topic_0079692997_p14114947"></a>Specifies the ID of the replication consistency group.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079692997_section27618155"></a>

-   Parameter description

    <a name="en-us_topic_0079692997_table65045669"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692997_row26965262"><th class="cellrowborder" valign="top" width="22.772277227722775%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079692997_p1872144815838"><a name="en-us_topic_0079692997_p1872144815838"></a><a name="en-us_topic_0079692997_p1872144815838"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.752475247524753%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079692997_p4004231915838"><a name="en-us_topic_0079692997_p4004231915838"></a><a name="en-us_topic_0079692997_p4004231915838"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.1.5.1.3"><p id="en-us_topic_0079692997_p2220239815838"><a name="en-us_topic_0079692997_p2220239815838"></a><a name="en-us_topic_0079692997_p2220239815838"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.64356435643564%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079692997_p5356383815838"><a name="en-us_topic_0079692997_p5356383815838"></a><a name="en-us_topic_0079692997_p5356383815838"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079692997_row10634019"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692997_p33059085203926"><a name="en-us_topic_0079692997_p33059085203926"></a><a name="en-us_topic_0079692997_p33059085203926"></a>os-stop-replication-consistency-group</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692997_p1232803915840"><a name="en-us_topic_0079692997_p1232803915840"></a><a name="en-us_topic_0079692997_p1232803915840"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692997_p49204239"><a name="en-us_topic_0079692997_p49204239"></a><a name="en-us_topic_0079692997_p49204239"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692997_p16180233203935"><a name="en-us_topic_0079692997_p16180233203935"></a><a name="en-us_topic_0079692997_p16180233203935"></a>The parameter value is null, indicating that the replication consistency group will be paused.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "os-stop-replication-consistency-group": null
    }
    ```


## Response<a name="en-us_topic_0079692997_section47236811"></a>

None

## Status Codes<a name="en-us_topic_0079692997_section22478116"></a>

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


