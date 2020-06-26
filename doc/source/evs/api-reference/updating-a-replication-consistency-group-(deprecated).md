# Updating a Replication Consistency Group \(Deprecated\)<a name="evs_04_2053"></a>

## Function<a name="en-us_topic_0079692913_section62509834"></a>

This API is used to update a replication consistency group. An update includes the following operations:

-   Update the name or description of the replication consistency group.
-   Add EVS replication pairs to or remove EVS replication pairs from the replication consistency group.

    >![](/images/icon-note.gif) **NOTE:**   
    >This API has been deprecated. To use this function, see  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  


## Constraints<a name="en-us_topic_0079692913_section2750866"></a>

-   The replication consistency group must be paused before the update.
-   Data needs to be synchronized after a replication consistency group update.

## URI<a name="en-us_topic_0079692913_section24757801"></a>

-   URI format

    PUT /v2/\{project\_id\}/os-vendor-replication-consistency-groups/\{replication\_consistency\_group\_id\}

-   Parameter description

    <a name="en-us_topic_0079692913_table57198891"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692913_row34359256"><th class="cellrowborder" valign="top" width="25.61%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079692913_p5489842314181"><a name="en-us_topic_0079692913_p5489842314181"></a><a name="en-us_topic_0079692913_p5489842314181"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.490000000000002%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079692913_p2925486214187"><a name="en-us_topic_0079692913_p2925486214187"></a><a name="en-us_topic_0079692913_p2925486214187"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.9%" id="mcps1.1.4.1.3"><p id="p149061731133513"><a name="p149061731133513"></a><a name="p149061731133513"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079692913_row17446726"><td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692913_p3898676"><a name="en-us_topic_0079692913_p3898676"></a><a name="en-us_topic_0079692913_p3898676"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.490000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692913_p38093407141813"><a name="en-us_topic_0079692913_p38093407141813"></a><a name="en-us_topic_0079692913_p38093407141813"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692913_p64356400"><a name="en-us_topic_0079692913_p64356400"></a><a name="en-us_topic_0079692913_p64356400"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692913_row42336695"><td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692913_p4696894820329"><a name="en-us_topic_0079692913_p4696894820329"></a><a name="en-us_topic_0079692913_p4696894820329"></a>replication_consistency_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.490000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692913_p38451097141827"><a name="en-us_topic_0079692913_p38451097141827"></a><a name="en-us_topic_0079692913_p38451097141827"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692913_p14913854"><a name="en-us_topic_0079692913_p14913854"></a><a name="en-us_topic_0079692913_p14913854"></a>Specifies the ID of the replication consistency group.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079692913_section21493617"></a>

-   Parameter description

    <a name="table2056153717259"></a>
    <table><thead align="left"><tr id="row12721537182520"><th class="cellrowborder" valign="top" width="23.97239723972397%" id="mcps1.1.5.1.1"><p id="p18721037182512"><a name="p18721037182512"></a><a name="p18721037182512"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.142014201420142%" id="mcps1.1.5.1.2"><p id="p472103718254"><a name="p472103718254"></a><a name="p472103718254"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.67176717671767%" id="mcps1.1.5.1.3"><p id="p1172123752518"><a name="p1172123752518"></a><a name="p1172123752518"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.213821382138214%" id="mcps1.1.5.1.4"><p id="p672123762512"><a name="p672123762512"></a><a name="p672123762512"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row872537112520"><td class="cellrowborder" valign="top" width="23.97239723972397%" headers="mcps1.1.5.1.1 "><p id="p14950105620255"><a name="p14950105620255"></a><a name="p14950105620255"></a>replication_consistency_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.142014201420142%" headers="mcps1.1.5.1.2 "><p id="p77293722513"><a name="p77293722513"></a><a name="p77293722513"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.67176717671767%" headers="mcps1.1.5.1.3 "><p id="p372237112517"><a name="p372237112517"></a><a name="p372237112517"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.213821382138214%" headers="mcps1.1.5.1.4 "><p id="p8871537162516"><a name="p8871537162516"></a><a name="p8871537162516"></a>Specifies the replication consistency group information.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameters in the  **replication\_consistency\_group**  field

    <a name="en-us_topic_0079692913_table45699530"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692913_row29858833"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079692913_p44262263141853"><a name="en-us_topic_0079692913_p44262263141853"></a><a name="en-us_topic_0079692913_p44262263141853"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.262626262626267%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079692913_p28473563141853"><a name="en-us_topic_0079692913_p28473563141853"></a><a name="en-us_topic_0079692913_p28473563141853"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.1.5.1.3"><p id="en-us_topic_0079692913_p24657230141853"><a name="en-us_topic_0079692913_p24657230141853"></a><a name="en-us_topic_0079692913_p24657230141853"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="34.343434343434346%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079692913_p51078651141853"><a name="en-us_topic_0079692913_p51078651141853"></a><a name="en-us_topic_0079692913_p51078651141853"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079692913_row16130451"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692913_p31498117"><a name="en-us_topic_0079692913_p31498117"></a><a name="en-us_topic_0079692913_p31498117"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692913_p19274594141955"><a name="en-us_topic_0079692913_p19274594141955"></a><a name="en-us_topic_0079692913_p19274594141955"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692913_p30957904"><a name="en-us_topic_0079692913_p30957904"></a><a name="en-us_topic_0079692913_p30957904"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692913_p23499784203042"><a name="en-us_topic_0079692913_p23499784203042"></a><a name="en-us_topic_0079692913_p23499784203042"></a>Specifies the name of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692913_row19734077"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692913_p54956439"><a name="en-us_topic_0079692913_p54956439"></a><a name="en-us_topic_0079692913_p54956439"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692913_p1158998114203"><a name="en-us_topic_0079692913_p1158998114203"></a><a name="en-us_topic_0079692913_p1158998114203"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692913_p60384317"><a name="en-us_topic_0079692913_p60384317"></a><a name="en-us_topic_0079692913_p60384317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692913_p18582878203042"><a name="en-us_topic_0079692913_p18582878203042"></a><a name="en-us_topic_0079692913_p18582878203042"></a>Specifies the description of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692913_row63861276"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692913_p5380904"><a name="en-us_topic_0079692913_p5380904"></a><a name="en-us_topic_0079692913_p5380904"></a>replication_model</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692913_p1335505814203"><a name="en-us_topic_0079692913_p1335505814203"></a><a name="en-us_topic_0079692913_p1335505814203"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692913_p4849307"><a name="en-us_topic_0079692913_p4849307"></a><a name="en-us_topic_0079692913_p4849307"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692913_p58036456203042"><a name="en-us_topic_0079692913_p58036456203042"></a><a name="en-us_topic_0079692913_p58036456203042"></a>Specifies the type of the replication consistency group. Currently, only type <strong id="b842352706164226"><a name="b842352706164226"></a><a name="b842352706164226"></a>hypermetro</strong> is supported.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692913_row45484537"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692913_p8850162203054"><a name="en-us_topic_0079692913_p8850162203054"></a><a name="en-us_topic_0079692913_p8850162203054"></a>add_replication_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692913_p1246324914203"><a name="en-us_topic_0079692913_p1246324914203"></a><a name="en-us_topic_0079692913_p1246324914203"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692913_p3493029"><a name="en-us_topic_0079692913_p3493029"></a><a name="en-us_topic_0079692913_p3493029"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692913_p14499957"><a name="en-us_topic_0079692913_p14499957"></a><a name="en-us_topic_0079692913_p14499957"></a>Specifies the IDs of the EVS replication pairs to be added.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692913_row63390755"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692913_p9317873203054"><a name="en-us_topic_0079692913_p9317873203054"></a><a name="en-us_topic_0079692913_p9317873203054"></a>remove_replication_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.262626262626267%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692913_p521635114203"><a name="en-us_topic_0079692913_p521635114203"></a><a name="en-us_topic_0079692913_p521635114203"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692913_p65119131"><a name="en-us_topic_0079692913_p65119131"></a><a name="en-us_topic_0079692913_p65119131"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.343434343434346%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692913_p40158284"><a name="en-us_topic_0079692913_p40158284"></a><a name="en-us_topic_0079692913_p40158284"></a>Specifies the IDs of the EVS replication pairs to be removed.</p>
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
            "replication_model": "hypermetro", 
            "add_replication_ids": [
                "0fc12f4e-381d-4f4a-acb0-9890c1683afe", 
                "0aee8399-4aeb-4d84-8d77-9d8a9d3dbe1a"
            ], 
            "remove_replication_ids": [
                "6b27b8b3-95d2-44e3-9cb2-f7de9e8739f2", 
                "cadeda61-7817-466e-bc0c-96448c4d106e"
            ]
        }
    }
    ```


## Response<a name="en-us_topic_0079692913_section59224828"></a>

-   Parameter description

    <a name="en-us_topic_0079692913_table27134857"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692913_row63620936"><th class="cellrowborder" valign="top" width="22.448979591836736%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079692913_p15132433144236"><a name="en-us_topic_0079692913_p15132433144236"></a><a name="en-us_topic_0079692913_p15132433144236"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.489795918367346%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079692913_p17767584144236"><a name="en-us_topic_0079692913_p17767584144236"></a><a name="en-us_topic_0079692913_p17767584144236"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.346938775510207%" id="mcps1.1.5.1.3"><p id="en-us_topic_0079692913_p29888195144236"><a name="en-us_topic_0079692913_p29888195144236"></a><a name="en-us_topic_0079692913_p29888195144236"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.714285714285715%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079692913_p5024739144236"><a name="en-us_topic_0079692913_p5024739144236"></a><a name="en-us_topic_0079692913_p5024739144236"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11829843132713"><td class="cellrowborder" valign="top" width="22.448979591836736%" headers="mcps1.1.5.1.1 "><p id="p4829843172717"><a name="p4829843172717"></a><a name="p4829843172717"></a>replication_consistency_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.489795918367346%" headers="mcps1.1.5.1.2 "><p id="p582974322719"><a name="p582974322719"></a><a name="p582974322719"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.346938775510207%" headers="mcps1.1.5.1.3 "><p id="p0829643112719"><a name="p0829643112719"></a><a name="p0829643112719"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.714285714285715%" headers="mcps1.1.5.1.4 "><p id="p1982914310275"><a name="p1982914310275"></a><a name="p1982914310275"></a>Specifies the replication consistency group information.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692913_row59548322"><td class="cellrowborder" valign="top" width="22.448979591836736%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692913_p58684749"><a name="en-us_topic_0079692913_p58684749"></a><a name="en-us_topic_0079692913_p58684749"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.489795918367346%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692913_p55844233"><a name="en-us_topic_0079692913_p55844233"></a><a name="en-us_topic_0079692913_p55844233"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.346938775510207%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692913_p27089021"><a name="en-us_topic_0079692913_p27089021"></a><a name="en-us_topic_0079692913_p27089021"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.714285714285715%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692913_p27199193203237"><a name="en-us_topic_0079692913_p27199193203237"></a><a name="en-us_topic_0079692913_p27199193203237"></a>Specifies the ID of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692913_row17890920"><td class="cellrowborder" valign="top" width="22.448979591836736%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692913_p39878449"><a name="en-us_topic_0079692913_p39878449"></a><a name="en-us_topic_0079692913_p39878449"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.489795918367346%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692913_p8928942"><a name="en-us_topic_0079692913_p8928942"></a><a name="en-us_topic_0079692913_p8928942"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.346938775510207%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692913_p52155720"><a name="en-us_topic_0079692913_p52155720"></a><a name="en-us_topic_0079692913_p52155720"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.714285714285715%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692913_p35856765203237"><a name="en-us_topic_0079692913_p35856765203237"></a><a name="en-us_topic_0079692913_p35856765203237"></a>Specifies the name of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="row151072917937"><td class="cellrowborder" valign="top" width="22.448979591836736%" headers="mcps1.1.5.1.1 "><p id="p842339217109"><a name="p842339217109"></a><a name="p842339217109"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.489795918367346%" headers="mcps1.1.5.1.2 "><p id="p1120616417109"><a name="p1120616417109"></a><a name="p1120616417109"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.346938775510207%" headers="mcps1.1.5.1.3 "><p id="p3528405517109"><a name="p3528405517109"></a><a name="p3528405517109"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.714285714285715%" headers="mcps1.1.5.1.4 "><p id="p3943624417109"><a name="p3943624417109"></a><a name="p3943624417109"></a>Specifies the description of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="row4938940517940"><td class="cellrowborder" valign="top" width="22.448979591836736%" headers="mcps1.1.5.1.1 "><p id="p31642600171025"><a name="p31642600171025"></a><a name="p31642600171025"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.489795918367346%" headers="mcps1.1.5.1.2 "><p id="p12913816171025"><a name="p12913816171025"></a><a name="p12913816171025"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.346938775510207%" headers="mcps1.1.5.1.3 "><p id="p39386156171025"><a name="p39386156171025"></a><a name="p39386156171025"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.714285714285715%" headers="mcps1.1.5.1.4 "><p id="p36162061171025"><a name="p36162061171025"></a><a name="p36162061171025"></a>Specifies the status of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="row2194426117944"><td class="cellrowborder" valign="top" width="22.448979591836736%" headers="mcps1.1.5.1.1 "><p id="p31862399171035"><a name="p31862399171035"></a><a name="p31862399171035"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.489795918367346%" headers="mcps1.1.5.1.2 "><p id="p30717530171035"><a name="p30717530171035"></a><a name="p30717530171035"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.346938775510207%" headers="mcps1.1.5.1.3 "><p id="p5091977171035"><a name="p5091977171035"></a><a name="p5091977171035"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.714285714285715%" headers="mcps1.1.5.1.4 "><p id="p9796981171035"><a name="p9796981171035"></a><a name="p9796981171035"></a>Specifies the primary site of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="row5110111517947"><td class="cellrowborder" valign="top" width="22.448979591836736%" headers="mcps1.1.5.1.1 "><p id="p403321171046"><a name="p403321171046"></a><a name="p403321171046"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.489795918367346%" headers="mcps1.1.5.1.2 "><p id="p32669002171046"><a name="p32669002171046"></a><a name="p32669002171046"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.346938775510207%" headers="mcps1.1.5.1.3 "><p id="p28943500171046"><a name="p28943500171046"></a><a name="p28943500171046"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.714285714285715%" headers="mcps1.1.5.1.4 "><p id="p62722150171046"><a name="p62722150171046"></a><a name="p62722150171046"></a>Specifies the time when the replication consistency group was created.</p>
    </td>
    </tr>
    <tr id="row3882740717949"><td class="cellrowborder" valign="top" width="22.448979591836736%" headers="mcps1.1.5.1.1 "><p id="p9609341171121"><a name="p9609341171121"></a><a name="p9609341171121"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.489795918367346%" headers="mcps1.1.5.1.2 "><p id="p28196592171113"><a name="p28196592171113"></a><a name="p28196592171113"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.346938775510207%" headers="mcps1.1.5.1.3 "><p id="p2222645171113"><a name="p2222645171113"></a><a name="p2222645171113"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.714285714285715%" headers="mcps1.1.5.1.4 "><p id="p57018793171132"><a name="p57018793171132"></a><a name="p57018793171132"></a>Specifies the time when the replication consistency group was updated.</p>
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
            "status": "updating", 
            "priority_station": "az2.dc2", 
            "created_at": "2017-10-19T03:57:36.577967", 
            "updated_at": "2017-10-19T04:45:26.467988"
        }
    }
    ```


## Status Codes<a name="en-us_topic_0079692913_section63261412"></a>

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


