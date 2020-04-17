# Querying Details About an EVS Replication Pair \(Deprecated\)<a name="evs_04_2047"></a>

## Function<a name="en-us_topic_0079693005_section33821816"></a>

This API is used to query the details about an EVS replication pair, including the name, ID, and status of the replication pair.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API has been deprecated. To use this function, see  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Constraints<a name="en-us_topic_0079693005_section27151449"></a>

None

## URI<a name="en-us_topic_0079693005_section51783759"></a>

-   URI format

    GET /v2/\{project\_id\}/os-vendor-replications/\{replication\_id\}

-   Parameter description

    <a name="en-us_topic_0079693005_table9617010"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693005_row36115021"><th class="cellrowborder" valign="top" width="27.380000000000003%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079693005_p48529539103853"><a name="en-us_topic_0079693005_p48529539103853"></a><a name="en-us_topic_0079693005_p48529539103853"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="29.76%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079693005_p56366974"><a name="en-us_topic_0079693005_p56366974"></a><a name="en-us_topic_0079693005_p56366974"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.86000000000001%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079693005_p53878657"><a name="en-us_topic_0079693005_p53878657"></a><a name="en-us_topic_0079693005_p53878657"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693005_row2095077"><td class="cellrowborder" valign="top" width="27.380000000000003%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693005_p35483542"><a name="en-us_topic_0079693005_p35483542"></a><a name="en-us_topic_0079693005_p35483542"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693005_p55594619"><a name="en-us_topic_0079693005_p55594619"></a><a name="en-us_topic_0079693005_p55594619"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.86000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693005_p19620867"><a name="en-us_topic_0079693005_p19620867"></a><a name="en-us_topic_0079693005_p19620867"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693005_row42370075"><td class="cellrowborder" valign="top" width="27.380000000000003%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693005_p5822879820122"><a name="en-us_topic_0079693005_p5822879820122"></a><a name="en-us_topic_0079693005_p5822879820122"></a>replication_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693005_p25149347"><a name="en-us_topic_0079693005_p25149347"></a><a name="en-us_topic_0079693005_p25149347"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.86000000000001%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693005_p51281965"><a name="en-us_topic_0079693005_p51281965"></a><a name="en-us_topic_0079693005_p51281965"></a>Specifies the ID of the EVS replication pair.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079693005_section63400648"></a>

None

## Response<a name="en-us_topic_0079693005_section33734921"></a>

-   Parameter description

    <a name="en-us_topic_0079693005_table43944024"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693005_row26973745"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079693005_p5401774610457"><a name="en-us_topic_0079693005_p5401774610457"></a><a name="en-us_topic_0079693005_p5401774610457"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.67%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079693005_p852360510457"><a name="en-us_topic_0079693005_p852360510457"></a><a name="en-us_topic_0079693005_p852360510457"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.33%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079693005_p1932338510457"><a name="en-us_topic_0079693005_p1932338510457"></a><a name="en-us_topic_0079693005_p1932338510457"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1494517871317"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p18945587137"><a name="p18945587137"></a><a name="p18945587137"></a>replication</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="p1894515861311"><a name="p1894515861311"></a><a name="p1894515861311"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="p169451815139"><a name="p169451815139"></a><a name="p169451815139"></a>Specifies the details of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693005_row55810719"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693005_p24374351"><a name="en-us_topic_0079693005_p24374351"></a><a name="en-us_topic_0079693005_p24374351"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693005_p66803900"><a name="en-us_topic_0079693005_p66803900"></a><a name="en-us_topic_0079693005_p66803900"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693005_p42406858"><a name="en-us_topic_0079693005_p42406858"></a><a name="en-us_topic_0079693005_p42406858"></a>Specifies the ID of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693005_row46117407"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693005_p44522499"><a name="en-us_topic_0079693005_p44522499"></a><a name="en-us_topic_0079693005_p44522499"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693005_p54340131"><a name="en-us_topic_0079693005_p54340131"></a><a name="en-us_topic_0079693005_p54340131"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693005_p39474480"><a name="en-us_topic_0079693005_p39474480"></a><a name="en-us_topic_0079693005_p39474480"></a>Specifies the name of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693005_row19726002"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693005_p54302323"><a name="en-us_topic_0079693005_p54302323"></a><a name="en-us_topic_0079693005_p54302323"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693005_p63691513"><a name="en-us_topic_0079693005_p63691513"></a><a name="en-us_topic_0079693005_p63691513"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693005_p58738960"><a name="en-us_topic_0079693005_p58738960"></a><a name="en-us_topic_0079693005_p58738960"></a>Specifies the description of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693005_row58888592"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693005_p5246632"><a name="en-us_topic_0079693005_p5246632"></a><a name="en-us_topic_0079693005_p5246632"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693005_p63415529"><a name="en-us_topic_0079693005_p63415529"></a><a name="en-us_topic_0079693005_p63415529"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693005_p36384226"><a name="en-us_topic_0079693005_p36384226"></a><a name="en-us_topic_0079693005_p36384226"></a>Specifies the status of the EVS replication pair. For details, see <a href="evs-replication-pair-status-(deprecated).md">EVS Replication Pair Status (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693005_row59022586"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693005_p66771664201239"><a name="en-us_topic_0079693005_p66771664201239"></a><a name="en-us_topic_0079693005_p66771664201239"></a>replication_consistency_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693005_p3715619"><a name="en-us_topic_0079693005_p3715619"></a><a name="en-us_topic_0079693005_p3715619"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693005_p25050057191231"><a name="en-us_topic_0079693005_p25050057191231"></a><a name="en-us_topic_0079693005_p25050057191231"></a>Specifies the ID of the replication consistency group where the EVS replication pair belongs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693005_row24331897"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693005_p24726637"><a name="en-us_topic_0079693005_p24726637"></a><a name="en-us_topic_0079693005_p24726637"></a>volume_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693005_p29346720"><a name="en-us_topic_0079693005_p29346720"></a><a name="en-us_topic_0079693005_p29346720"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693005_p28274094"><a name="en-us_topic_0079693005_p28274094"></a><a name="en-us_topic_0079693005_p28274094"></a>Specifies the IDs of the EVS disks used to create the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693005_row53140254"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693005_p9393336"><a name="en-us_topic_0079693005_p9393336"></a><a name="en-us_topic_0079693005_p9393336"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693005_p23742817"><a name="en-us_topic_0079693005_p23742817"></a><a name="en-us_topic_0079693005_p23742817"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693005_p44120000"><a name="en-us_topic_0079693005_p44120000"></a><a name="en-us_topic_0079693005_p44120000"></a>Specifies the primary site of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693005_row61535683"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693005_p18334396"><a name="en-us_topic_0079693005_p18334396"></a><a name="en-us_topic_0079693005_p18334396"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693005_p32887983"><a name="en-us_topic_0079693005_p32887983"></a><a name="en-us_topic_0079693005_p32887983"></a>datetime</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693005_p46680953"><a name="en-us_topic_0079693005_p46680953"></a><a name="en-us_topic_0079693005_p46680953"></a>Specifies the creation time.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693005_row17475399"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693005_p6221225"><a name="en-us_topic_0079693005_p6221225"></a><a name="en-us_topic_0079693005_p6221225"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693005_p15273051"><a name="en-us_topic_0079693005_p15273051"></a><a name="en-us_topic_0079693005_p15273051"></a>datetime</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693005_p29157627"><a name="en-us_topic_0079693005_p29157627"></a><a name="en-us_topic_0079693005_p29157627"></a>Specifies the update time.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693005_row61092053"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693005_p49509242"><a name="en-us_topic_0079693005_p49509242"></a><a name="en-us_topic_0079693005_p49509242"></a>replication_model</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693005_p23239422"><a name="en-us_topic_0079693005_p23239422"></a><a name="en-us_topic_0079693005_p23239422"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693005_p3345069"><a name="en-us_topic_0079693005_p3345069"></a><a name="en-us_topic_0079693005_p3345069"></a>Specifies the replication type of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693005_row30105629"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693005_p22636847"><a name="en-us_topic_0079693005_p22636847"></a><a name="en-us_topic_0079693005_p22636847"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693005_p8441658"><a name="en-us_topic_0079693005_p8441658"></a><a name="en-us_topic_0079693005_p8441658"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693005_p12685698"><a name="en-us_topic_0079693005_p12685698"></a><a name="en-us_topic_0079693005_p12685698"></a>Specifies the replication status of the EVS replication pair. For details, see <a href="evs-replication-pair-status-(deprecated).md">EVS Replication Pair Status (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="row2994811414536"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p39867082145328"><a name="p39867082145328"></a><a name="p39867082145328"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="p44685082145328"><a name="p44685082145328"></a><a name="p44685082145328"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="p62721872145328"><a name="p62721872145328"></a><a name="p62721872145328"></a>Specifies the synchronization progress of the EVS replication pair.</p>
    <p id="p4264555412116"><a name="p4264555412116"></a><a name="p4264555412116"></a>Unit: %</p>
    </td>
    </tr>
    <tr id="row10223145112630"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p14895941112656"><a name="p14895941112656"></a><a name="p14895941112656"></a>failure_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="p21765492112656"><a name="p21765492112656"></a><a name="p21765492112656"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="p18174445112656"><a name="p18174445112656"></a><a name="p18174445112656"></a>Specifies the returned error code if the EVS replication pair status is <strong id="b842352706173222"><a name="b842352706173222"></a><a name="b842352706173222"></a>error</strong>. For details, see <a href="details-of-evs-replication-failure_detail-values-(deprecated).md">Details of EVS Replication failure_detail Values (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="row18783936112634"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p28724278112656"><a name="p28724278112656"></a><a name="p28724278112656"></a>record_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="p18298883112656"><a name="p18298883112656"></a><a name="p18298883112656"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><p id="p5814593112656"><a name="p5814593112656"></a><a name="p5814593112656"></a>Specifies the billing record of the replication pair. For details, see <a href="#li59982790112347">Parameters in the record_metadata field</a>.</p>
    </td>
    </tr>
    <tr id="row95841310505"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.4.1.1 "><p id="p14308739114614"><a name="p14308739114614"></a><a name="p14308739114614"></a>fault_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.2 "><p id="p930863913466"><a name="p930863913466"></a><a name="p930863913466"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.33%" headers="mcps1.1.4.1.3 "><div class="p" id="p143081839144612"><a name="p143081839144612"></a><a name="p143081839144612"></a>Specifies the fault level of the EVS replication pair. The value can be as follows:<a name="evs_04_2046_ul14417182479"></a><a name="evs_04_2046_ul14417182479"></a><ul id="evs_04_2046_ul14417182479"><li><strong id="evs_04_2046_b84235270620364"><a name="evs_04_2046_b84235270620364"></a><a name="evs_04_2046_b84235270620364"></a>0</strong>: indicates that no fault occurs.</li><li><strong id="evs_04_2046_b842352706203620"><a name="evs_04_2046_b842352706203620"></a><a name="evs_04_2046_b842352706203620"></a>2</strong>: indicates that the production disk does not have read/write permissions. In this case, you are advised to perform a failover.</li><li><strong id="evs_04_2046_b84235270620377"><a name="evs_04_2046_b84235270620377"></a><a name="evs_04_2046_b84235270620377"></a>5</strong>: indicates that the replication link is disconnected. In this case, a failover cannot be performed. Contact technical support engineers.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li59982790112347"></a>Parameters in the  **record\_metadata**  field

    <a name="table39584085112347"></a>
    <table><thead align="left"><tr id="row46712658112347"><th class="cellrowborder" valign="top" width="31.506849315068493%" id="mcps1.1.4.1.1"><p id="p25628967112347"><a name="p25628967112347"></a><a name="p25628967112347"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.28767123287671%" id="mcps1.1.4.1.2"><p id="p43950230112347"><a name="p43950230112347"></a><a name="p43950230112347"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.205479452054796%" id="mcps1.1.4.1.3"><p id="p3198848112347"><a name="p3198848112347"></a><a name="p3198848112347"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57780118112347"><td class="cellrowborder" valign="top" width="31.506849315068493%" headers="mcps1.1.4.1.1 "><p id="p49678018112347"><a name="p49678018112347"></a><a name="p49678018112347"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.1.4.1.2 "><p id="p56833141112347"><a name="p56833141112347"></a><a name="p56833141112347"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.205479452054796%" headers="mcps1.1.4.1.3 "><p id="p40081742112347"><a name="p40081742112347"></a><a name="p40081742112347"></a>Specifies the type of the EVS disks in the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="row25191363112347"><td class="cellrowborder" valign="top" width="31.506849315068493%" headers="mcps1.1.4.1.1 "><p id="p27234489112347"><a name="p27234489112347"></a><a name="p27234489112347"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.1.4.1.2 "><p id="p41689551112347"><a name="p41689551112347"></a><a name="p41689551112347"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.205479452054796%" headers="mcps1.1.4.1.3 "><p id="p21410495112347"><a name="p21410495112347"></a><a name="p21410495112347"></a>Specifies whether the EVS disks in the EVS replication pair are shared EVS disks.</p>
    </td>
    </tr>
    <tr id="row174684233917"><td class="cellrowborder" valign="top" width="31.506849315068493%" headers="mcps1.1.4.1.1 "><p id="p9862487398"><a name="p9862487398"></a><a name="p9862487398"></a>volume_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.1.4.1.2 "><p id="p10862487395"><a name="p10862487395"></a><a name="p10862487395"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.205479452054796%" headers="mcps1.1.4.1.3 "><p id="p6869488395"><a name="p6869488395"></a><a name="p6869488395"></a>Specifies the size of each EVS disk in the EVS replication pair. The unit is GB.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "replication": {
            "status": "available", 
            "priority_station": "az2.dc2", 
            "volume_ids": "a623cd91-89f9-4baf-a5aa-7774d2bfcb8b,3e8fdded-64bb-4c60-a55e-2e4bc3d240d6", 
            "record_metadata": "{\"volume_size\": 10,\"volume_type\": \"ssd\", \"multiattach\": false}", 
            "name": "yes", 
            "created_at": "2017-09-30T10:14:32.747000", 
            "updated_at": "2017-09-30T10:14:34.505912", 
            "replication_consistency_group_id": null, 
            "replication_status": "active", 
            "fault_level": "0", 
            "replication_model": "hypermetro", 
            "id": "dddd9746-14df-4823-be9d-7b4f4f8518ed", 
            "description": "yes", 
            "progress": "100"
        }
    }
    ```


## Status Codes<a name="en-us_topic_0079693005_section35178835"></a>

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


