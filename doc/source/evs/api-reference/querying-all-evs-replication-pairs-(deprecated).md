# Querying All EVS Replication Pairs \(Deprecated\)<a name="evs_04_2046"></a>

## Function<a name="en-us_topic_0079693004_section31430389"></a>

This API is used to query all EVS replication pairs of the current tenant.

>![](/images/icon-note.gif) **NOTE:**   
>This API has been deprecated. To use this function, see  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Constraints<a name="en-us_topic_0079693004_section28631516"></a>

None

## URI<a name="en-us_topic_0079693004_section56357057"></a>

-   URI format

    GET /v2/\{project\_id\}/os-vendor-replications

-   Parameter description

    <a name="en-us_topic_0079693004_table45616947"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693004_row39731869"><th class="cellrowborder" valign="top" width="27.71%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079693004_p64164835"><a name="en-us_topic_0079693004_p64164835"></a><a name="en-us_topic_0079693004_p64164835"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.12%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079693004_p29969153"><a name="en-us_topic_0079693004_p29969153"></a><a name="en-us_topic_0079693004_p29969153"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.17%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079693004_p4140323110136"><a name="en-us_topic_0079693004_p4140323110136"></a><a name="en-us_topic_0079693004_p4140323110136"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693004_row24688256"><td class="cellrowborder" valign="top" width="27.71%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693004_p53591696"><a name="en-us_topic_0079693004_p53591696"></a><a name="en-us_topic_0079693004_p53591696"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.12%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693004_p59759668101537"><a name="en-us_topic_0079693004_p59759668101537"></a><a name="en-us_topic_0079693004_p59759668101537"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.17%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693004_p24283812"><a name="en-us_topic_0079693004_p24283812"></a><a name="en-us_topic_0079693004_p24283812"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079693004_section37451465"></a>

-   Parameter description

    <a name="en-us_topic_0079693004_table19766715"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693004_row14848410"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079693004_p61870584"><a name="en-us_topic_0079693004_p61870584"></a><a name="en-us_topic_0079693004_p61870584"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079693004_p48554935101525"><a name="en-us_topic_0079693004_p48554935101525"></a><a name="en-us_topic_0079693004_p48554935101525"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.1.5.1.3"><p id="en-us_topic_0079693004_p58493292"><a name="en-us_topic_0079693004_p58493292"></a><a name="en-us_topic_0079693004_p58493292"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.35353535353536%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079693004_p6530115101630"><a name="en-us_topic_0079693004_p6530115101630"></a><a name="en-us_topic_0079693004_p6530115101630"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693004_row46007650"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693004_p35632194"><a name="en-us_topic_0079693004_p35632194"></a><a name="en-us_topic_0079693004_p35632194"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693004_p14494794101545"><a name="en-us_topic_0079693004_p14494794101545"></a><a name="en-us_topic_0079693004_p14494794101545"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693004_p42656148"><a name="en-us_topic_0079693004_p42656148"></a><a name="en-us_topic_0079693004_p42656148"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693004_p32595925"><a name="en-us_topic_0079693004_p32595925"></a><a name="en-us_topic_0079693004_p32595925"></a>Specifies the ID of the last EVS replication pair on the previous page, and the next EVS replication pair ID is returned.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row24927872"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693004_p5891777"><a name="en-us_topic_0079693004_p5891777"></a><a name="en-us_topic_0079693004_p5891777"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693004_p7471967"><a name="en-us_topic_0079693004_p7471967"></a><a name="en-us_topic_0079693004_p7471967"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693004_p1249601"><a name="en-us_topic_0079693004_p1249601"></a><a name="en-us_topic_0079693004_p1249601"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693004_p34108880"><a name="en-us_topic_0079693004_p34108880"></a><a name="en-us_topic_0079693004_p34108880"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="p516982121111"><a name="p516982121111"></a><a name="p516982121111"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row38544467"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693004_p35094160"><a name="en-us_topic_0079693004_p35094160"></a><a name="en-us_topic_0079693004_p35094160"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693004_p24054701"><a name="en-us_topic_0079693004_p24054701"></a><a name="en-us_topic_0079693004_p24054701"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693004_p2273746"><a name="en-us_topic_0079693004_p2273746"></a><a name="en-us_topic_0079693004_p2273746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693004_p38919089173129"><a name="en-us_topic_0079693004_p38919089173129"></a><a name="en-us_topic_0079693004_p38919089173129"></a>Specifies that the returned results are sorted by keyword. The default keyword is <strong id="b842352706153317"><a name="b842352706153317"></a><a name="b842352706153317"></a>created_at</strong>, indicating that the EVS replication pairs are sorted by creation time.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row46948589"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693004_p44739342"><a name="en-us_topic_0079693004_p44739342"></a><a name="en-us_topic_0079693004_p44739342"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693004_p8117"><a name="en-us_topic_0079693004_p8117"></a><a name="en-us_topic_0079693004_p8117"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693004_p657479"><a name="en-us_topic_0079693004_p657479"></a><a name="en-us_topic_0079693004_p657479"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693004_p180193872074"><a name="en-us_topic_0079693004_p180193872074"></a><a name="en-us_topic_0079693004_p180193872074"></a>Specifies that the returned results are sorted by ascending or descending order. The default value is <strong id="b84235270615371"><a name="b84235270615371"></a><a name="b84235270615371"></a>desc</strong>, indicating that the EVS replication pairs are sorted by descending order.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row9540645"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693004_p34594790"><a name="en-us_topic_0079693004_p34594790"></a><a name="en-us_topic_0079693004_p34594790"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693004_p50714607"><a name="en-us_topic_0079693004_p50714607"></a><a name="en-us_topic_0079693004_p50714607"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693004_p14242537"><a name="en-us_topic_0079693004_p14242537"></a><a name="en-us_topic_0079693004_p14242537"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693004_p12794876"><a name="en-us_topic_0079693004_p12794876"></a><a name="en-us_topic_0079693004_p12794876"></a>Specifies the offset.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row25654779"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693004_p64771222"><a name="en-us_topic_0079693004_p64771222"></a><a name="en-us_topic_0079693004_p64771222"></a>changes-since</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693004_p11977605"><a name="en-us_topic_0079693004_p11977605"></a><a name="en-us_topic_0079693004_p11977605"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693004_p30661937"><a name="en-us_topic_0079693004_p30661937"></a><a name="en-us_topic_0079693004_p30661937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693004_p1776639820755"><a name="en-us_topic_0079693004_p1776639820755"></a><a name="en-us_topic_0079693004_p1776639820755"></a>Specifies to query all the EVS replication pairs that have been updated from the specified time point to the current time.</p>
    </td>
    </tr>
    <tr id="row17034078122721"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.5.1.1 "><p id="p27157254122957"><a name="p27157254122957"></a><a name="p27157254122957"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.2 "><p id="p7970749123112"><a name="p7970749123112"></a><a name="p7970749123112"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="p4714405122957"><a name="p4714405122957"></a><a name="p4714405122957"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.4 "><p id="p46322488122957"><a name="p46322488122957"></a><a name="p46322488122957"></a>Specifies the name of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="row66984039122940"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.5.1.1 "><p id="p17846986122957"><a name="p17846986122957"></a><a name="p17846986122957"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.2 "><p id="p39313832123112"><a name="p39313832123112"></a><a name="p39313832123112"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="p56222186122957"><a name="p56222186122957"></a><a name="p56222186122957"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.4 "><p id="p57703194122957"><a name="p57703194122957"></a><a name="p57703194122957"></a>Specifies the status of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="row50394873122944"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.5.1.1 "><p id="p29558020122957"><a name="p29558020122957"></a><a name="p29558020122957"></a>replication_consistency_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.2 "><p id="p4298840123112"><a name="p4298840123112"></a><a name="p4298840123112"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="p52667185122957"><a name="p52667185122957"></a><a name="p52667185122957"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.4 "><p id="p38183572122957"><a name="p38183572122957"></a><a name="p38183572122957"></a>Specifies the ID of the replication consistency group where the EVS replication pair belongs.</p>
    </td>
    </tr>
    <tr id="row52751732122948"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.5.1.1 "><p id="p52754395122957"><a name="p52754395122957"></a><a name="p52754395122957"></a>volume_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.2 "><p id="p46847073123112"><a name="p46847073123112"></a><a name="p46847073123112"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="p41180110122957"><a name="p41180110122957"></a><a name="p41180110122957"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.4 "><p id="p47254634122957"><a name="p47254634122957"></a><a name="p47254634122957"></a>Specifies the IDs of the EVS disks used to create the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="row19094355112057"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.5.1.1 "><p id="p3138948112057"><a name="p3138948112057"></a><a name="p3138948112057"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.2 "><p id="p36910885112137"><a name="p36910885112137"></a><a name="p36910885112137"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="p36991672112137"><a name="p36991672112137"></a><a name="p36991672112137"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.4 "><p id="p41147491112057"><a name="p41147491112057"></a><a name="p41147491112057"></a>Specifies the ID of an EVS disk.</p>
    </td>
    </tr>
    <tr id="row2248500122953"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.5.1.1 "><p id="p21781616122957"><a name="p21781616122957"></a><a name="p21781616122957"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.2 "><p id="p60213340123112"><a name="p60213340123112"></a><a name="p60213340123112"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="p34411645122957"><a name="p34411645122957"></a><a name="p34411645122957"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.35353535353536%" headers="mcps1.1.5.1.4 "><p id="p35879852122957"><a name="p35879852122957"></a><a name="p35879852122957"></a>Specifies the primary site of the EVS replication pair.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    None


## Response<a name="en-us_topic_0079693004_section1518871"></a>

-   Parameter description

    <a name="en-us_topic_0079693004_table22044110"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693004_row18774354"><th class="cellrowborder" valign="top" width="32.43%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079693004_p22340429101755"><a name="en-us_topic_0079693004_p22340429101755"></a><a name="en-us_topic_0079693004_p22340429101755"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.62%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079693004_p3472651101811"><a name="en-us_topic_0079693004_p3472651101811"></a><a name="en-us_topic_0079693004_p3472651101811"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.95%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079693004_p48686995101818"><a name="en-us_topic_0079693004_p48686995101818"></a><a name="en-us_topic_0079693004_p48686995101818"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6293173918919"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="p12938391599"><a name="p12938391599"></a><a name="p12938391599"></a>replications</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="p660318133116"><a name="p660318133116"></a><a name="p660318133116"></a>List&lt;replication&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="p220451513124"><a name="p220451513124"></a><a name="p220451513124"></a>Specifies the EVS replication pairs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row43163346"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693004_p6570122"><a name="en-us_topic_0079693004_p6570122"></a><a name="en-us_topic_0079693004_p6570122"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693004_p22681099"><a name="en-us_topic_0079693004_p22681099"></a><a name="en-us_topic_0079693004_p22681099"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693004_p25229732"><a name="en-us_topic_0079693004_p25229732"></a><a name="en-us_topic_0079693004_p25229732"></a>Specifies the ID of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row25741004"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693004_p4646565"><a name="en-us_topic_0079693004_p4646565"></a><a name="en-us_topic_0079693004_p4646565"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693004_p18691797"><a name="en-us_topic_0079693004_p18691797"></a><a name="en-us_topic_0079693004_p18691797"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693004_p37640571"><a name="en-us_topic_0079693004_p37640571"></a><a name="en-us_topic_0079693004_p37640571"></a>Specifies the name of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row3220827"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693004_p59560431"><a name="en-us_topic_0079693004_p59560431"></a><a name="en-us_topic_0079693004_p59560431"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693004_p1078370"><a name="en-us_topic_0079693004_p1078370"></a><a name="en-us_topic_0079693004_p1078370"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693004_p20239120"><a name="en-us_topic_0079693004_p20239120"></a><a name="en-us_topic_0079693004_p20239120"></a>Specifies the description of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row47934352"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693004_p57477322"><a name="en-us_topic_0079693004_p57477322"></a><a name="en-us_topic_0079693004_p57477322"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693004_p24005299"><a name="en-us_topic_0079693004_p24005299"></a><a name="en-us_topic_0079693004_p24005299"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693004_p65381042"><a name="en-us_topic_0079693004_p65381042"></a><a name="en-us_topic_0079693004_p65381042"></a>Specifies the status of the EVS replication pair. For details, see <a href="evs-replication-pair-status-(deprecated).md">EVS Replication Pair Status (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row51558469"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693004_p6032614120913"><a name="en-us_topic_0079693004_p6032614120913"></a><a name="en-us_topic_0079693004_p6032614120913"></a>replication_consistency_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693004_p3647249"><a name="en-us_topic_0079693004_p3647249"></a><a name="en-us_topic_0079693004_p3647249"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693004_p366446520926"><a name="en-us_topic_0079693004_p366446520926"></a><a name="en-us_topic_0079693004_p366446520926"></a>Specifies the ID of the replication consistency group where the EVS replication pair belongs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row41599065"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693004_p14081115"><a name="en-us_topic_0079693004_p14081115"></a><a name="en-us_topic_0079693004_p14081115"></a>volume_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693004_p44403789"><a name="en-us_topic_0079693004_p44403789"></a><a name="en-us_topic_0079693004_p44403789"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693004_p39937165"><a name="en-us_topic_0079693004_p39937165"></a><a name="en-us_topic_0079693004_p39937165"></a>Specifies the IDs of the EVS disks used to create the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row23890167"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693004_p56055356"><a name="en-us_topic_0079693004_p56055356"></a><a name="en-us_topic_0079693004_p56055356"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693004_p22620416"><a name="en-us_topic_0079693004_p22620416"></a><a name="en-us_topic_0079693004_p22620416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693004_p20314447"><a name="en-us_topic_0079693004_p20314447"></a><a name="en-us_topic_0079693004_p20314447"></a>Specifies the primary site of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row48612303"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693004_p45282433"><a name="en-us_topic_0079693004_p45282433"></a><a name="en-us_topic_0079693004_p45282433"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693004_p7106508"><a name="en-us_topic_0079693004_p7106508"></a><a name="en-us_topic_0079693004_p7106508"></a>datetime</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693004_p38756276"><a name="en-us_topic_0079693004_p38756276"></a><a name="en-us_topic_0079693004_p38756276"></a>Specifies the creation time.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693004_row13262169"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693004_p493939"><a name="en-us_topic_0079693004_p493939"></a><a name="en-us_topic_0079693004_p493939"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693004_p19513753"><a name="en-us_topic_0079693004_p19513753"></a><a name="en-us_topic_0079693004_p19513753"></a>datetime</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693004_p37110132"><a name="en-us_topic_0079693004_p37110132"></a><a name="en-us_topic_0079693004_p37110132"></a>Specifies the update time.</p>
    </td>
    </tr>
    <tr id="row5000287412655"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="p4830887612719"><a name="p4830887612719"></a><a name="p4830887612719"></a>replication_model</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="p6648476612719"><a name="p6648476612719"></a><a name="p6648476612719"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="p1655697412719"><a name="p1655697412719"></a><a name="p1655697412719"></a>Specifies the replication type of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="row1644950812659"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="p3814358012727"><a name="p3814358012727"></a><a name="p3814358012727"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="p1107750912727"><a name="p1107750912727"></a><a name="p1107750912727"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="p2486305912727"><a name="p2486305912727"></a><a name="p2486305912727"></a>Specifies the replication status of the EVS replication pair. For details, see <a href="evs-replication-pair-status-(deprecated).md">EVS Replication Pair Status (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="row406124361272"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="p2899896512743"><a name="p2899896512743"></a><a name="p2899896512743"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="p5900537712754"><a name="p5900537712754"></a><a name="p5900537712754"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="p398805061284"><a name="p398805061284"></a><a name="p398805061284"></a>Specifies the synchronization progress of the EVS replication pair.</p>
    <p id="p2683021812743"><a name="p2683021812743"></a><a name="p2683021812743"></a>Unit: %</p>
    </td>
    </tr>
    <tr id="row12414232112238"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="p31102734112255"><a name="p31102734112255"></a><a name="p31102734112255"></a>failure_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="p54097582112255"><a name="p54097582112255"></a><a name="p54097582112255"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="p19828045112255"><a name="p19828045112255"></a><a name="p19828045112255"></a>Specifies the returned error code if the EVS replication pair status is <strong id="b842352706173222"><a name="b842352706173222"></a><a name="b842352706173222"></a>error</strong>. For details, see <a href="details-of-evs-replication-failure_detail-values-(deprecated).md">Details of EVS Replication failure_detail Values (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="row25316905112243"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="p65942053112255"><a name="p65942053112255"></a><a name="p65942053112255"></a>record_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="p62072811112255"><a name="p62072811112255"></a><a name="p62072811112255"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="p61841826112255"><a name="p61841826112255"></a><a name="p61841826112255"></a>Specifies the billing record of the replication pair. For details, see <a href="#li59982790112347">Parameters in the record_metadata field</a>.</p>
    </td>
    </tr>
    <tr id="row97668314463"><td class="cellrowborder" valign="top" width="32.43%" headers="mcps1.1.4.1.1 "><p id="p14308739114614"><a name="p14308739114614"></a><a name="p14308739114614"></a>fault_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.1.4.1.2 "><p id="p930863913466"><a name="p930863913466"></a><a name="p930863913466"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><div class="p" id="p143081839144612"><a name="p143081839144612"></a><a name="p143081839144612"></a>Specifies the fault level of the EVS replication pair. The value can be as follows:<a name="ul14417182479"></a><a name="ul14417182479"></a><ul id="ul14417182479"><li><strong id="b84235270620364"><a name="b84235270620364"></a><a name="b84235270620364"></a>0</strong>: indicates that no fault occurs.</li><li><strong id="b842352706203620"><a name="b842352706203620"></a><a name="b842352706203620"></a>2</strong>: indicates that the production disk does not have read/write permissions. In this case, you are advised to perform a failover.</li><li><strong id="b84235270620377"><a name="b84235270620377"></a><a name="b84235270620377"></a>5</strong>: indicates that the replication link is disconnected. In this case, a failover cannot be performed. Contact technical support engineers.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li59982790112347"></a>Parameters in the  **record\_metadata**  field

    <a name="table39584085112347"></a>
    <table><thead align="left"><tr id="row46712658112347"><th class="cellrowborder" valign="top" width="32.43324332433243%" id="mcps1.1.4.1.1"><p id="p25628967112347"><a name="p25628967112347"></a><a name="p25628967112347"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.972297229722972%" id="mcps1.1.4.1.2"><p id="p43950230112347"><a name="p43950230112347"></a><a name="p43950230112347"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.594459445944594%" id="mcps1.1.4.1.3"><p id="p3198848112347"><a name="p3198848112347"></a><a name="p3198848112347"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57780118112347"><td class="cellrowborder" valign="top" width="32.43324332433243%" headers="mcps1.1.4.1.1 "><p id="p49678018112347"><a name="p49678018112347"></a><a name="p49678018112347"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.972297229722972%" headers="mcps1.1.4.1.2 "><p id="p56833141112347"><a name="p56833141112347"></a><a name="p56833141112347"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.594459445944594%" headers="mcps1.1.4.1.3 "><p id="p40081742112347"><a name="p40081742112347"></a><a name="p40081742112347"></a>Specifies the type of the EVS disks in the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="row25191363112347"><td class="cellrowborder" valign="top" width="32.43324332433243%" headers="mcps1.1.4.1.1 "><p id="p27234489112347"><a name="p27234489112347"></a><a name="p27234489112347"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.972297229722972%" headers="mcps1.1.4.1.2 "><p id="p41689551112347"><a name="p41689551112347"></a><a name="p41689551112347"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.594459445944594%" headers="mcps1.1.4.1.3 "><p id="p21410495112347"><a name="p21410495112347"></a><a name="p21410495112347"></a>Specifies whether the EVS disks in the EVS replication pair are shared EVS disks.</p>
    </td>
    </tr>
    <tr id="row06443253820"><td class="cellrowborder" valign="top" width="32.43324332433243%" headers="mcps1.1.4.1.1 "><p id="p186616903815"><a name="p186616903815"></a><a name="p186616903815"></a>volume_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.972297229722972%" headers="mcps1.1.4.1.2 "><p id="p17661196382"><a name="p17661196382"></a><a name="p17661196382"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.594459445944594%" headers="mcps1.1.4.1.3 "><p id="p176659193810"><a name="p176659193810"></a><a name="p176659193810"></a>Specifies the size of each EVS disk in the EVS replication pair. The unit is GB.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "replications": [
            {
                "status": "available", 
                "replication_model": "hypermetro", 
                "description": "replication", 
                "record_metadata": "{ \"volume_size\": 5, \"volume_type\": \"ssd\", \"multiattach\": false}", 
                "updated_at": "2017-11-27T12:08:01.463824", 
                "replication_status": "inactive", 
                "fault_level": "0", 
                "id": "190081db-9023-431d-a51a-197faf3762b5", 
                "replication_consistency_group_id": null, 
                "priority_station": "az2.dc2", 
                "volume_ids": "288a6cac-1352-460f-9b93-bfd41979f805,905d5dee-2ce4-406b-bb8a-314b3e92643e", 
                "name": "replication", 
                "created_at": "2017-11-27T12:07:59.993903", 
                "progress": null
            }, 
            {
                "status": "available", 
                "replication_model": "hypermetro", 
                "description": "replication", 
                "record_metadata": "{ \"volume_size\": 10, \"volume_type\": \"ssd\", \"multiattach\": false}", 
                "updated_at": "2017-11-28T06:16:30.725816", 
                "replication_status": "active", 
                "fault_level": "0", 
                "id": "6690b30a-b40c-4a50-bd4a-7e5c1e28b821", 
                "replication_consistency_group_id": "13b582e6-092e-4f7a-9260-8eb7a4ad860e", 
                "priority_station": "az3.dc3", 
                "volume_ids": "f3bd8265-130a-4917-815b-a074ddb06850,32eb83a2-dd2f-480d-a49e-7af6edf3c7c7", 
                "name": "replication", 
                "created_at": "2017-11-27T11:37:24.459062", 
                "progress": "100"
            }
        ]
    }
    ```


## Status Codes<a name="en-us_topic_0079693004_section13669843"></a>

-   Normal

    <a name="table4315991194956"></a>
    <table><thead align="left"><tr id="row2336641294956"><th class="cellrowborder" valign="top" width="42.59%" id="mcps1.1.3.1.1"><p id="p1363125894956"><a name="p1363125894956"></a><a name="p1363125894956"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.410000000000004%" id="mcps1.1.3.1.2"><p id="p3039012494956"><a name="p3039012494956"></a><a name="p3039012494956"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row507566794956"><td class="cellrowborder" valign="top" width="42.59%" headers="mcps1.1.3.1.1 "><p id="p847584694956"><a name="p847584694956"></a><a name="p847584694956"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.410000000000004%" headers="mcps1.1.3.1.2 "><p id="p1545496394956"><a name="p1545496394956"></a><a name="p1545496394956"></a>The server has processed the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="evs_04_2044_table22458872203835"></a>
    <table><thead align="left"><tr id="evs_04_2044_row35704554203835"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="evs_04_2044_p6387753203835"><a name="evs_04_2044_p6387753203835"></a><a name="evs_04_2044_p6387753203835"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="evs_04_2044_p47646009203835"><a name="evs_04_2044_p47646009203835"></a><a name="evs_04_2044_p47646009203835"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2044_row34121538203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p12381163203835"><a name="evs_04_2044_p12381163203835"></a><a name="evs_04_2044_p12381163203835"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p63350108203835"><a name="evs_04_2044_p63350108203835"></a><a name="evs_04_2044_p63350108203835"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row33280063203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p11330608203835"><a name="evs_04_2044_p11330608203835"></a><a name="evs_04_2044_p11330608203835"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p45364094203835"><a name="evs_04_2044_p45364094203835"></a><a name="evs_04_2044_p45364094203835"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row5623667203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p52863895203835"><a name="evs_04_2044_p52863895203835"></a><a name="evs_04_2044_p52863895203835"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p54117066203835"><a name="evs_04_2044_p54117066203835"></a><a name="evs_04_2044_p54117066203835"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row17291554203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p58438642203835"><a name="evs_04_2044_p58438642203835"></a><a name="evs_04_2044_p58438642203835"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p35909542203835"><a name="evs_04_2044_p35909542203835"></a><a name="evs_04_2044_p35909542203835"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row54750425203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p5599455203835"><a name="evs_04_2044_p5599455203835"></a><a name="evs_04_2044_p5599455203835"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p50902717203835"><a name="evs_04_2044_p50902717203835"></a><a name="evs_04_2044_p50902717203835"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row55471277203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p63988484203835"><a name="evs_04_2044_p63988484203835"></a><a name="evs_04_2044_p63988484203835"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p15684678203835"><a name="evs_04_2044_p15684678203835"></a><a name="evs_04_2044_p15684678203835"></a>The response generated by the server cannot be accepted by the client.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row6944380203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p25623884203835"><a name="evs_04_2044_p25623884203835"></a><a name="evs_04_2044_p25623884203835"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p62268733203835"><a name="evs_04_2044_p62268733203835"></a><a name="evs_04_2044_p62268733203835"></a>You must use the proxy server for authentication. Then, the request can be processed.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row23547689203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p28314670203835"><a name="evs_04_2044_p28314670203835"></a><a name="evs_04_2044_p28314670203835"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p11786919203835"><a name="evs_04_2044_p11786919203835"></a><a name="evs_04_2044_p11786919203835"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row38973411203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p2729702203835"><a name="evs_04_2044_p2729702203835"></a><a name="evs_04_2044_p2729702203835"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p19779281203835"><a name="evs_04_2044_p19779281203835"></a><a name="evs_04_2044_p19779281203835"></a>The request cannot be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row43795805203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p57799353203835"><a name="evs_04_2044_p57799353203835"></a><a name="evs_04_2044_p57799353203835"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p51235984203835"><a name="evs_04_2044_p51235984203835"></a><a name="evs_04_2044_p51235984203835"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row58470678203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p38504500203835"><a name="evs_04_2044_p38504500203835"></a><a name="evs_04_2044_p38504500203835"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p31856770203835"><a name="evs_04_2044_p31856770203835"></a><a name="evs_04_2044_p31856770203835"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row18275474203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p3918444203835"><a name="evs_04_2044_p3918444203835"></a><a name="evs_04_2044_p3918444203835"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p48958538203835"><a name="evs_04_2044_p48958538203835"></a><a name="evs_04_2044_p48958538203835"></a>Failed to complete the request because the server has received an invalid response.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row37973662203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p55967806203835"><a name="evs_04_2044_p55967806203835"></a><a name="evs_04_2044_p55967806203835"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p37098455203835"><a name="evs_04_2044_p37098455203835"></a><a name="evs_04_2044_p37098455203835"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row65450640203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p67010448203835"><a name="evs_04_2044_p67010448203835"></a><a name="evs_04_2044_p67010448203835"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p59137180203835"><a name="evs_04_2044_p59137180203835"></a><a name="evs_04_2044_p59137180203835"></a>A gateway timeout error occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


