# Querying Details About a Replication Consistency Group \(Deprecated\)<a name="evs_04_2052"></a>

## Function<a name="en-us_topic_0079692912_section66054074"></a>

This API is used to query the details about a replication consistency group, including the name, ID, and status of the consistency group.

>![](/images/icon-note.gif) **NOTE:**   
>This API has been deprecated. To use this function, see  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Constraints<a name="en-us_topic_0079692912_section36364960"></a>

None

## URI<a name="en-us_topic_0079692912_section58849189"></a>

-   URI format

    GET /v2/\{project\_id\}/os-vendor-replication-consistency-groups/\{replication\_consistency\_group\_id\}

-   Parameter description

    <a name="en-us_topic_0079692912_table25692540"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692912_row27037160"><th class="cellrowborder" valign="top" width="25.61%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079692912_p42526340"><a name="en-us_topic_0079692912_p42526340"></a><a name="en-us_topic_0079692912_p42526340"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.490000000000002%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079692912_p22081476"><a name="en-us_topic_0079692912_p22081476"></a><a name="en-us_topic_0079692912_p22081476"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.9%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079692912_p55636561"><a name="en-us_topic_0079692912_p55636561"></a><a name="en-us_topic_0079692912_p55636561"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079692912_row10267631"><td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692912_p26371793"><a name="en-us_topic_0079692912_p26371793"></a><a name="en-us_topic_0079692912_p26371793"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.490000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692912_p55740512"><a name="en-us_topic_0079692912_p55740512"></a><a name="en-us_topic_0079692912_p55740512"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692912_p37302179"><a name="en-us_topic_0079692912_p37302179"></a><a name="en-us_topic_0079692912_p37302179"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692912_row175293"><td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692912_p550835520286"><a name="en-us_topic_0079692912_p550835520286"></a><a name="en-us_topic_0079692912_p550835520286"></a>replication_consistency_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.490000000000002%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692912_p9248440"><a name="en-us_topic_0079692912_p9248440"></a><a name="en-us_topic_0079692912_p9248440"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692912_p12605589"><a name="en-us_topic_0079692912_p12605589"></a><a name="en-us_topic_0079692912_p12605589"></a>Specifies the ID of the replication consistency group.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079692912_section59880657"></a>

None

## Response<a name="en-us_topic_0079692912_section2055005"></a>

-   Parameter description

    <a name="en-us_topic_0079692912_table13080057"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692912_row10852974"><th class="cellrowborder" valign="top" width="30.26302630263026%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079692912_p50509670113448"><a name="en-us_topic_0079692912_p50509670113448"></a><a name="en-us_topic_0079692912_p50509670113448"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.682368236823685%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079692912_p10376603113448"><a name="en-us_topic_0079692912_p10376603113448"></a><a name="en-us_topic_0079692912_p10376603113448"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.05460546054606%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079692912_p35198527113448"><a name="en-us_topic_0079692912_p35198527113448"></a><a name="en-us_topic_0079692912_p35198527113448"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16982347234"><td class="cellrowborder" valign="top" width="30.26302630263026%" headers="mcps1.1.4.1.1 "><p id="p798334182310"><a name="p798334182310"></a><a name="p798334182310"></a>replication_consistency_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.682368236823685%" headers="mcps1.1.4.1.2 "><p id="p09843472318"><a name="p09843472318"></a><a name="p09843472318"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.05460546054606%" headers="mcps1.1.4.1.3 "><p id="p19823462316"><a name="p19823462316"></a><a name="p19823462316"></a>Specifies the details of replication consistency groups.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692912_row23909939"><td class="cellrowborder" valign="top" width="30.26302630263026%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692912_p57656925"><a name="en-us_topic_0079692912_p57656925"></a><a name="en-us_topic_0079692912_p57656925"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.682368236823685%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692912_p61529894"><a name="en-us_topic_0079692912_p61529894"></a><a name="en-us_topic_0079692912_p61529894"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.05460546054606%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692912_p37299013192230"><a name="en-us_topic_0079692912_p37299013192230"></a><a name="en-us_topic_0079692912_p37299013192230"></a>Specifies the ID of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692912_row26571712"><td class="cellrowborder" valign="top" width="30.26302630263026%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692912_p4825033"><a name="en-us_topic_0079692912_p4825033"></a><a name="en-us_topic_0079692912_p4825033"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.682368236823685%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692912_p48766684"><a name="en-us_topic_0079692912_p48766684"></a><a name="en-us_topic_0079692912_p48766684"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.05460546054606%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692912_p17679985192238"><a name="en-us_topic_0079692912_p17679985192238"></a><a name="en-us_topic_0079692912_p17679985192238"></a>Specifies the name of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692912_row50323820"><td class="cellrowborder" valign="top" width="30.26302630263026%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692912_p49697630"><a name="en-us_topic_0079692912_p49697630"></a><a name="en-us_topic_0079692912_p49697630"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.682368236823685%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692912_p51294256"><a name="en-us_topic_0079692912_p51294256"></a><a name="en-us_topic_0079692912_p51294256"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.05460546054606%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692912_p56546120192246"><a name="en-us_topic_0079692912_p56546120192246"></a><a name="en-us_topic_0079692912_p56546120192246"></a>Specifies the description of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692912_row13875810"><td class="cellrowborder" valign="top" width="30.26302630263026%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692912_p50198807"><a name="en-us_topic_0079692912_p50198807"></a><a name="en-us_topic_0079692912_p50198807"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.682368236823685%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692912_p51181499"><a name="en-us_topic_0079692912_p51181499"></a><a name="en-us_topic_0079692912_p51181499"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.05460546054606%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692912_p52060794"><a name="en-us_topic_0079692912_p52060794"></a><a name="en-us_topic_0079692912_p52060794"></a>Specifies the status of the replication consistency group. For details, see <a href="replication-consistency-group-status-(deprecated).md">Replication Consistency Group Status (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692912_row65893970"><td class="cellrowborder" valign="top" width="30.26302630263026%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692912_p35811316"><a name="en-us_topic_0079692912_p35811316"></a><a name="en-us_topic_0079692912_p35811316"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.682368236823685%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692912_p9915935"><a name="en-us_topic_0079692912_p9915935"></a><a name="en-us_topic_0079692912_p9915935"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.05460546054606%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692912_p64993271"><a name="en-us_topic_0079692912_p64993271"></a><a name="en-us_topic_0079692912_p64993271"></a>Specifies the primary site of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692912_row48068532"><td class="cellrowborder" valign="top" width="30.26302630263026%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692912_p1237054"><a name="en-us_topic_0079692912_p1237054"></a><a name="en-us_topic_0079692912_p1237054"></a>replication_model</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.682368236823685%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692912_p63253060"><a name="en-us_topic_0079692912_p63253060"></a><a name="en-us_topic_0079692912_p63253060"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.05460546054606%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692912_p23224207"><a name="en-us_topic_0079692912_p23224207"></a><a name="en-us_topic_0079692912_p23224207"></a>Specifies the replication type of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692912_row7691275"><td class="cellrowborder" valign="top" width="30.26302630263026%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692912_p19013575"><a name="en-us_topic_0079692912_p19013575"></a><a name="en-us_topic_0079692912_p19013575"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.682368236823685%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692912_p59796890"><a name="en-us_topic_0079692912_p59796890"></a><a name="en-us_topic_0079692912_p59796890"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.05460546054606%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692912_p11709955"><a name="en-us_topic_0079692912_p11709955"></a><a name="en-us_topic_0079692912_p11709955"></a>Specifies the replication status of the replication consistency group. For details, see <a href="replication-consistency-group-status-(deprecated).md">Replication Consistency Group Status (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="row2058426917155"><td class="cellrowborder" valign="top" width="30.26302630263026%" headers="mcps1.1.4.1.1 "><p id="p464461771727"><a name="p464461771727"></a><a name="p464461771727"></a>replication_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.682368236823685%" headers="mcps1.1.4.1.2 "><p id="p4714637121815"><a name="p4714637121815"></a><a name="p4714637121815"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.05460546054606%" headers="mcps1.1.4.1.3 "><p id="p5969800317155"><a name="p5969800317155"></a><a name="p5969800317155"></a>Specifies the IDs of all EVS replication pairs in the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692912_row41583755"><td class="cellrowborder" valign="top" width="30.26302630263026%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692912_p12841014"><a name="en-us_topic_0079692912_p12841014"></a><a name="en-us_topic_0079692912_p12841014"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.682368236823685%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692912_p28272749"><a name="en-us_topic_0079692912_p28272749"></a><a name="en-us_topic_0079692912_p28272749"></a>datetime</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.05460546054606%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692912_p8391370"><a name="en-us_topic_0079692912_p8391370"></a><a name="en-us_topic_0079692912_p8391370"></a>Specifies the creation time.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692912_row8413469"><td class="cellrowborder" valign="top" width="30.26302630263026%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692912_p10402369"><a name="en-us_topic_0079692912_p10402369"></a><a name="en-us_topic_0079692912_p10402369"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.682368236823685%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692912_p230999"><a name="en-us_topic_0079692912_p230999"></a><a name="en-us_topic_0079692912_p230999"></a>datetime</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.05460546054606%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692912_p18710936"><a name="en-us_topic_0079692912_p18710936"></a><a name="en-us_topic_0079692912_p18710936"></a>Specifies the update time.</p>
    </td>
    </tr>
    <tr id="row33277399113048"><td class="cellrowborder" valign="top" width="30.26302630263026%" headers="mcps1.1.4.1.1 "><p id="p9317681113050"><a name="p9317681113050"></a><a name="p9317681113050"></a>failure_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.682368236823685%" headers="mcps1.1.4.1.2 "><p id="p64243632113050"><a name="p64243632113050"></a><a name="p64243632113050"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.05460546054606%" headers="mcps1.1.4.1.3 "><p id="p36351667113050"><a name="p36351667113050"></a><a name="p36351667113050"></a>Specifies the returned error code if the status of the replication consistency group is <strong id="b842352706173222"><a name="b842352706173222"></a><a name="b842352706173222"></a>error</strong>. For details, see <a href="details-of-evs-replication-failure_detail-values-(deprecated).md">Details of EVS Replication failure_detail Values (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="row1595192912313"><td class="cellrowborder" valign="top" width="30.26302630263026%" headers="mcps1.1.4.1.1 "><p id="p3193205912567"><a name="p3193205912567"></a><a name="p3193205912567"></a>fault_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.682368236823685%" headers="mcps1.1.4.1.2 "><p id="p6193165985616"><a name="p6193165985616"></a><a name="p6193165985616"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.05460546054606%" headers="mcps1.1.4.1.3 "><div class="p" id="p1919345911565"><a name="p1919345911565"></a><a name="p1919345911565"></a>Specifies the fault level of the replication consistency group. The value can be as follows:<a name="evs_04_2051_ul1837105465719"></a><a name="evs_04_2051_ul1837105465719"></a><ul id="evs_04_2051_ul1837105465719"><li><strong id="evs_04_2051_b84235270620364"><a name="evs_04_2051_b84235270620364"></a><a name="evs_04_2051_b84235270620364"></a>0</strong>: indicates that no fault occurs.</li><li><strong id="evs_04_2051_b842352706203620"><a name="evs_04_2051_b842352706203620"></a><a name="evs_04_2051_b842352706203620"></a>2</strong>: indicates that a production disk in the replication consistency group does not have read/write permissions. In this case, you are advised to perform a failover.</li><li><strong id="evs_04_2051_b84235270620377"><a name="evs_04_2051_b84235270620377"></a><a name="evs_04_2051_b84235270620377"></a>5</strong>: indicates that the replication link is disconnected. In this case, a failover cannot be performed. Contact technical support engineers.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {  
        "replication_consistency_group": {  
            "id": "bd35d31b-7ab9-47fc-84c6-3d326c6fa6cb",   
            "name": " replicationcgtest",   
            "description": "my replicationcg pair",   
            "status": "available",   
            "priority_staion": "az2.dc2",   
            "replication_model": "hypermetro",
            "fault_level": "0",   
            "replication_status": "active-stopped",  
            "replication_ids": [  
                "e5bd643b-7407-4a0e-8d9a-2a88903e8812"  
            ],   
            "created_at": "2017-09-30T07:37:06.035360",   
            "updated_at": null  
        }  
    }
    ```


## Status Codes<a name="en-us_topic_0079692912_section18495050"></a>

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


