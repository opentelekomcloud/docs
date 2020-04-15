# Creating a Replication Consistency Group \(Deprecated\)<a name="evs_04_2049"></a>

## Function<a name="en-us_topic_0079693007_section10543355"></a>

This API is used to create a replication consistency group for the specified EVS replication pairs.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API has been deprecated. To use this function, see  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Constraints<a name="en-us_topic_0079693007_section35695699"></a>

-   At least one EVS replication pair must be added when you create the replication consistency group.
-   The EVS replication pairs to be added to the group must be in the  **available**  state.

## URI<a name="en-us_topic_0079693007_section52825835"></a>

-   URI format

    POST /v2/\{project\_id\}/os-vendor-replication-consistency-groups

-   Parameter description

    <a name="en-us_topic_0079693007_table12721335"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693007_row27645849"><th class="cellrowborder" valign="top" width="26.83%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079693007_p24721334"><a name="en-us_topic_0079693007_p24721334"></a><a name="en-us_topic_0079693007_p24721334"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="29.270000000000003%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079693007_p50297731105511"><a name="en-us_topic_0079693007_p50297731105511"></a><a name="en-us_topic_0079693007_p50297731105511"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.9%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079693007_p57597090105541"><a name="en-us_topic_0079693007_p57597090105541"></a><a name="en-us_topic_0079693007_p57597090105541"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693007_row14570748"><td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693007_p39379979"><a name="en-us_topic_0079693007_p39379979"></a><a name="en-us_topic_0079693007_p39379979"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693007_p60581432105519"><a name="en-us_topic_0079693007_p60581432105519"></a><a name="en-us_topic_0079693007_p60581432105519"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693007_p35329099"><a name="en-us_topic_0079693007_p35329099"></a><a name="en-us_topic_0079693007_p35329099"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079693007_section5670474"></a>

-   Parameter description

    <a name="table1473320317169"></a>
    <table><thead align="left"><tr id="row17733113111611"><th class="cellrowborder" valign="top" width="23.797620237976204%" id="mcps1.1.5.1.1"><p id="p15733193191614"><a name="p15733193191614"></a><a name="p15733193191614"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.938006199380062%" id="mcps1.1.5.1.2"><p id="p1773313351620"><a name="p1773313351620"></a><a name="p1773313351620"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.307969203079693%" id="mcps1.1.5.1.3"><p id="p147339318161"><a name="p147339318161"></a><a name="p147339318161"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.95640435956404%" id="mcps1.1.5.1.4"><p id="p4748932168"><a name="p4748932168"></a><a name="p4748932168"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row274814391619"><td class="cellrowborder" valign="top" width="23.797620237976204%" headers="mcps1.1.5.1.1 "><p id="p1074883161611"><a name="p1074883161611"></a><a name="p1074883161611"></a>replication_consistency_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.938006199380062%" headers="mcps1.1.5.1.2 "><p id="p177488319167"><a name="p177488319167"></a><a name="p177488319167"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.307969203079693%" headers="mcps1.1.5.1.3 "><p id="p474863101618"><a name="p474863101618"></a><a name="p474863101618"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.95640435956404%" headers="mcps1.1.5.1.4 "><p id="p174863151611"><a name="p174863151611"></a><a name="p174863151611"></a>Specifies to create the replication consistency group. For details, see <a href="#en-us_topic_0079693007_li206293">•Parameters in the replication_consistency_group field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="en-us_topic_0079693007_li206293"></a>Parameters in the  **replication\_consistency\_group**  field

    <a name="en-us_topic_0079693007_table1856645"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693007_row29445360"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079693007_p54520436105611"><a name="en-us_topic_0079693007_p54520436105611"></a><a name="en-us_topic_0079693007_p54520436105611"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079693007_p54079232105611"><a name="en-us_topic_0079693007_p54079232105611"></a><a name="en-us_topic_0079693007_p54079232105611"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.3"><p id="en-us_topic_0079693007_p18341639105611"><a name="en-us_topic_0079693007_p18341639105611"></a><a name="en-us_topic_0079693007_p18341639105611"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="34%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079693007_p9277811105611"><a name="en-us_topic_0079693007_p9277811105611"></a><a name="en-us_topic_0079693007_p9277811105611"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693007_row40488209"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693007_p58319463"><a name="en-us_topic_0079693007_p58319463"></a><a name="en-us_topic_0079693007_p58319463"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693007_p33516961105616"><a name="en-us_topic_0079693007_p33516961105616"></a><a name="en-us_topic_0079693007_p33516961105616"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693007_p46366269"><a name="en-us_topic_0079693007_p46366269"></a><a name="en-us_topic_0079693007_p46366269"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693007_p64680333"><a name="en-us_topic_0079693007_p64680333"></a><a name="en-us_topic_0079693007_p64680333"></a>Specifies the name of the replication consistency group. The name can contain a maximum of 255 bytes.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693007_row45252091"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693007_p41540743"><a name="en-us_topic_0079693007_p41540743"></a><a name="en-us_topic_0079693007_p41540743"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693007_p9356983"><a name="en-us_topic_0079693007_p9356983"></a><a name="en-us_topic_0079693007_p9356983"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693007_p19718131"><a name="en-us_topic_0079693007_p19718131"></a><a name="en-us_topic_0079693007_p19718131"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693007_p53664804"><a name="en-us_topic_0079693007_p53664804"></a><a name="en-us_topic_0079693007_p53664804"></a>Specifies the description of the replication consistency group. The description can contain a maximum of 255 bytes.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693007_row13221196"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693007_p62459745201432"><a name="en-us_topic_0079693007_p62459745201432"></a><a name="en-us_topic_0079693007_p62459745201432"></a>replication_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693007_p39619499"><a name="en-us_topic_0079693007_p39619499"></a><a name="en-us_topic_0079693007_p39619499"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693007_p55062814"><a name="en-us_topic_0079693007_p55062814"></a><a name="en-us_topic_0079693007_p55062814"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693007_p40897114191733"><a name="en-us_topic_0079693007_p40897114191733"></a><a name="en-us_topic_0079693007_p40897114191733"></a>Specifies the IDs of the EVS replication pairs used to create the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693007_row9691430"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p3959632895853"><a name="p3959632895853"></a><a name="p3959632895853"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693007_p54404257105630"><a name="en-us_topic_0079693007_p54404257105630"></a><a name="en-us_topic_0079693007_p54404257105630"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693007_p19399120"><a name="en-us_topic_0079693007_p19399120"></a><a name="en-us_topic_0079693007_p19399120"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693007_p27824865"><a name="en-us_topic_0079693007_p27824865"></a><a name="en-us_topic_0079693007_p27824865"></a>Specifies the current primary AZ, that is, the AZ where the production disks belong.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693007_row49097200"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693007_p17450296"><a name="en-us_topic_0079693007_p17450296"></a><a name="en-us_topic_0079693007_p17450296"></a>replication_model</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693007_p16346926105630"><a name="en-us_topic_0079693007_p16346926105630"></a><a name="en-us_topic_0079693007_p16346926105630"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693007_p3672032"><a name="en-us_topic_0079693007_p3672032"></a><a name="en-us_topic_0079693007_p3672032"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693007_p28999185"><a name="en-us_topic_0079693007_p28999185"></a><a name="en-us_topic_0079693007_p28999185"></a>Specifies the type of the created replication consistency group. Currently, only type <strong id="b842352706164226"><a name="b842352706164226"></a><a name="b842352706164226"></a>hypermetro</strong> is supported.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "replication_consistency_group": {
            "name": "my replication consistency group", 
            "description": "my replication consistency group", 
            "replication_ids": [
                "18aa67ea-c7cb-4826-800d-50e67f0de75b", 
                "375d23be-3658-498f-8b50-d3b950a890ec"
            ], 
            "priority_station": "az2.dc2", 
            "replication_model": "hypermetro"
        }
    }
    ```


## Response<a name="en-us_topic_0079693007_section51034272"></a>

-   Parameter description

    <a name="en-us_topic_0079693007_table44149718"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693007_row35316297"><th class="cellrowborder" valign="top" width="30.259999999999998%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079693007_p58412109105953"><a name="en-us_topic_0079693007_p58412109105953"></a><a name="en-us_topic_0079693007_p58412109105953"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.37%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079693007_p58082052"><a name="en-us_topic_0079693007_p58082052"></a><a name="en-us_topic_0079693007_p58082052"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.370000000000005%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079693007_p7025744"><a name="en-us_topic_0079693007_p7025744"></a><a name="en-us_topic_0079693007_p7025744"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4790162431817"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.1.4.1.1 "><p id="p117901724121813"><a name="p117901724121813"></a><a name="p117901724121813"></a>replication_consistency_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.1.4.1.2 "><p id="p10790202413183"><a name="p10790202413183"></a><a name="p10790202413183"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p97907246187"><a name="p97907246187"></a><a name="p97907246187"></a>Specifies the replication consistency group information.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693007_row32214417"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693007_p59231023"><a name="en-us_topic_0079693007_p59231023"></a><a name="en-us_topic_0079693007_p59231023"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693007_p54423456"><a name="en-us_topic_0079693007_p54423456"></a><a name="en-us_topic_0079693007_p54423456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693007_p46223811"><a name="en-us_topic_0079693007_p46223811"></a><a name="en-us_topic_0079693007_p46223811"></a>Specifies the ID of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693007_row13361120"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693007_p8508925"><a name="en-us_topic_0079693007_p8508925"></a><a name="en-us_topic_0079693007_p8508925"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693007_p59592696"><a name="en-us_topic_0079693007_p59592696"></a><a name="en-us_topic_0079693007_p59592696"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693007_p62279078"><a name="en-us_topic_0079693007_p62279078"></a><a name="en-us_topic_0079693007_p62279078"></a>Specifies the name of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693007_row23640798"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693007_p35856517"><a name="en-us_topic_0079693007_p35856517"></a><a name="en-us_topic_0079693007_p35856517"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693007_p38039934"><a name="en-us_topic_0079693007_p38039934"></a><a name="en-us_topic_0079693007_p38039934"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693007_p61335842"><a name="en-us_topic_0079693007_p61335842"></a><a name="en-us_topic_0079693007_p61335842"></a>Specifies the description of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693007_row15151670"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693007_p19325759"><a name="en-us_topic_0079693007_p19325759"></a><a name="en-us_topic_0079693007_p19325759"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693007_p27666764"><a name="en-us_topic_0079693007_p27666764"></a><a name="en-us_topic_0079693007_p27666764"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693007_p26415391"><a name="en-us_topic_0079693007_p26415391"></a><a name="en-us_topic_0079693007_p26415391"></a>Specifies the status of the replication consistency group. For details, see <a href="replication-consistency-group-status-(deprecated).md">Replication Consistency Group Status (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="row29807427192827"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.1.4.1.1 "><p id="p65591352192827"><a name="p65591352192827"></a><a name="p65591352192827"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.1.4.1.2 "><p id="p42825952192827"><a name="p42825952192827"></a><a name="p42825952192827"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p46350050192827"><a name="p46350050192827"></a><a name="p46350050192827"></a>Specifies the primary site of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693007_row36411928"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693007_p63685038"><a name="en-us_topic_0079693007_p63685038"></a><a name="en-us_topic_0079693007_p63685038"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693007_p17753217"><a name="en-us_topic_0079693007_p17753217"></a><a name="en-us_topic_0079693007_p17753217"></a>datetime</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693007_p28724493"><a name="en-us_topic_0079693007_p28724493"></a><a name="en-us_topic_0079693007_p28724493"></a>Specifies the creation time.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693007_row57193853"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693007_p2190491"><a name="en-us_topic_0079693007_p2190491"></a><a name="en-us_topic_0079693007_p2190491"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693007_p10515080"><a name="en-us_topic_0079693007_p10515080"></a><a name="en-us_topic_0079693007_p10515080"></a>datetime</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693007_p46415143"><a name="en-us_topic_0079693007_p46415143"></a><a name="en-us_topic_0079693007_p46415143"></a>Specifies the update time.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "replication_consistency_group": {
            "id": "91085433-9499-4a68-b2c6-35072467ccd2", 
            "name": "my replication consistency group", 
            "description": "my replication consistency group", 
            "status": "creating", 
            "priority_station": "az2.dc2", 
            "created_at": "2017-09-28T05:08:32.839953", 
            "updated_at": null
        }
    }
    ```


## Status Codes<a name="en-us_topic_0079693007_section56655270"></a>

-   Normal

    <a name="evs_04_2044_table4315991194956"></a>
    <table><thead align="left"><tr id="evs_04_2044_row2336641294956"><th class="cellrowborder" valign="top" width="42.59%" id="mcps1.1.3.1.1"><p id="evs_04_2044_p1363125894956"><a name="evs_04_2044_p1363125894956"></a><a name="evs_04_2044_p1363125894956"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.410000000000004%" id="mcps1.1.3.1.2"><p id="evs_04_2044_p3039012494956"><a name="evs_04_2044_p3039012494956"></a><a name="evs_04_2044_p3039012494956"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2044_row507566794956"><td class="cellrowborder" valign="top" width="42.59%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p847584694956"><a name="evs_04_2044_p847584694956"></a><a name="evs_04_2044_p847584694956"></a>202</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.410000000000004%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p1545496394956"><a name="evs_04_2044_p1545496394956"></a><a name="evs_04_2044_p1545496394956"></a>The server has accepted the request.</p>
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


